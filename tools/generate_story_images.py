#!/usr/bin/env python3
"""
generate_story_images.py — Adventures with the Bull image pipeline runner.

Reads a story manifest (``storyNNN-panels.json``), validates every prompt
against the series' consistency rules, submits each image to the correct
Replicate model (character LoRAs, flux-2-pro, or gpt-image-2), downloads the
results, runs automated QA, overlays the cover title, and writes the final
files + an updated manifest with seeds and prediction URLs.

The script owns *how* images are rendered. The agent owns *what* is drawn:
it writes the manifest from the manuscript using ``image-prompt-library.md``.
See ``image-generation-pipeline.md`` for the full operating procedure.

Usage::

    export REPLICATE_API_TOKEN=...          # never hard-code; read from env
    python tools/generate_story_images.py stories/story003/story003-panels.json \
        --out stories/story003 --title-mode pillow --max-predictions 40

    # dry run: validate the manifest and print the resolved API calls
    python tools/generate_story_images.py manifest.json --dry-run

Exit codes: 0 success, 1 validation error, 2 API/network error, 3 QA failures
remain after retries (images were still written; see manifest ``needs_review``).
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import logging
import os
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

try:  # optional deps are imported lazily so --dry-run works without them
    import requests  # type: ignore
except Exception:  # pragma: no cover
    requests = None  # type: ignore

LOG = logging.getLogger("awtb.images")

# --------------------------------------------------------------------------- #
# Constants — these mirror image-prompt-library.md §2, §3 and                  #
# image-generation-pipeline.md §3. Change them there first, then here.         #
# --------------------------------------------------------------------------- #

STYLE_BLOCK_PREFIXES = (
    "2D graphic novel illustration, inked comic book art, Mike Mignola art style",
    "Mike Mignola art style, Hellboy comic art style, 2D graphic novel illustration",
    "2D graphic novel illustration in the style of a Mike Mignola inked comic panel",
)

HATER_ANTI_DRIFT_MARKER = "NOT Hellboy"

OWNER = "dannyboy2323"

ROUTES: dict[str, dict[str, Any]] = {
    "danny": {
        "model": f"{OWNER}/character-daddanny23",
        "extra_lora": None,
        "triggers": ["CHARACTERDADDANNY23"],
        "family": "flux-lora",
    },
    "daniel": {
        "model": f"{OWNER}/character-danielbull23",
        "extra_lora": None,
        "triggers": ["CHARACTERDANIELBULL23"],
        "family": "flux-lora",
    },
    "danny+daniel": {
        "model": f"{OWNER}/character-daddanny23",
        "extra_lora": f"{OWNER}/character-danielbull23",
        "triggers": ["CHARACTERDADDANNY23", "CHARACTERDANIELBULL23"],
        "family": "flux-lora",
    },
    "hater": {
        "model": f"{OWNER}/character-hater",
        "extra_lora": None,
        "triggers": ["CHARACTERHATER"],
        "family": "flux-lora",
        "requires_marker": HATER_ANTI_DRIFT_MARKER,
    },
    "prosecutor": {
        # TODO(author): confirm trigger spelling — the only logged run used "#CHARACTERPROSECUTOR".
        "model": f"{OWNER}/character-prosecutor",
        "extra_lora": None,
        "triggers": ["CHARACTERPROSECUTOR"],
        "family": "flux-lora",
    },
    "hater+prosecutor": {
        "model": f"{OWNER}/character-hater",
        "extra_lora": f"{OWNER}/character-prosecutor",
        "triggers": ["CHARACTERHATER", "CHARACTERPROSECUTOR"],
        "family": "flux-lora",
        "requires_marker": HATER_ANTI_DRIFT_MARKER,
    },
    "flux2pro": {
        "model": "black-forest-labs/flux-2-pro",
        "extra_lora": None,
        "triggers": [],
        "family": "flux2pro",
    },
    "gptimage2": {
        "model": "openai/gpt-image-2",
        "extra_lora": None,
        "triggers": [],
        "family": "gptimage2",
    },
}

# Proven defaults for the Flux-dev LoRA models (every logged success used these).
FLUX_LORA_DEFAULTS: dict[str, Any] = {
    "model": "dev",
    "go_fast": False,
    "num_inference_steps": 28,
    "guidance_scale": 3,
    "megapixels": "1",
    "output_format": "webp",
    "output_quality": 80,
    "prompt_strength": 0.8,
    "lora_scale": 1.0,
    "extra_lora_scale": 1.0,
    "num_outputs": 1,
    "disable_safety_checker": False,  # never True — see pipeline §5
}

FLUX2PRO_DEFAULTS: dict[str, Any] = {
    "resolution": "1 MP",
    "output_format": "webp",
    "output_quality": 80,
    "safety_tolerance": 2,
}

GPTIMAGE2_DEFAULTS: dict[str, Any] = {
    "quality": "high",
    "output_format": "webp",
    "number_of_images": 1,
    "background": "opaque",
}

ASPECT_TARGETS = {"16:9": 16 / 9, "1:1": 1.0, "9:16": 9 / 16, "3:2": 1.5, "2:3": 2 / 3, "4:5": 0.8}

REPLICATE_API = "https://api.replicate.com/v1"


# --------------------------------------------------------------------------- #
# Data model                                                                   #
# --------------------------------------------------------------------------- #


@dataclass
class ImageSpec:
    """One image to generate, as declared in the manifest."""

    id: str
    kind: str  # "cover" | "panel"
    prompt: str
    route: str
    aspect_ratio: str = "1:1"
    page: int | None = None
    slot: str | None = None
    lora_scale: float | None = None
    num_outputs: int | None = None
    seed: int | None = None
    reference_images: list[str] = field(default_factory=list)
    title_overlay: dict[str, str] | None = None
    # filled in during the run
    prediction_url: str | None = None
    model_version: str | None = None
    outputs: list[str] = field(default_factory=list)
    chosen: str | None = None
    qa: dict[str, Any] = field(default_factory=dict)
    needs_review: bool = False

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "ImageSpec":
        known = {k: v for k, v in d.items() if k in cls.__dataclass_fields__}
        return cls(**known)

    def to_dict(self) -> dict[str, Any]:
        return {k: getattr(self, k) for k in self.__dataclass_fields__}


@dataclass
class Manifest:
    story: int
    slug: str
    title: str
    images: list[ImageSpec]
    extra: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def load(cls, path: Path) -> "Manifest":
        data = json.loads(path.read_text(encoding="utf-8"))
        images = [ImageSpec.from_dict(i) for i in data.get("images", [])]
        extra = {k: v for k, v in data.items() if k not in {"story", "slug", "title", "images"}}
        return cls(story=int(data["story"]), slug=str(data["slug"]), title=str(data["title"]), images=images, extra=extra)

    def dump(self, path: Path) -> None:
        payload = {"story": self.story, "slug": self.slug, "title": self.title, **self.extra, "images": [i.to_dict() for i in self.images]}
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


# --------------------------------------------------------------------------- #
# Validation — the consistency rules that must never be violated               #
# --------------------------------------------------------------------------- #


class ValidationError(Exception):
    """Raised when a manifest entry breaks a series consistency rule."""


def validate_spec(spec: ImageSpec) -> list[str]:
    """Return a list of human-readable problems with one image spec (empty = OK).

    Rules enforced (see image-prompt-library.md):
      * route must be known
      * prompt must start with an approved style block (LoRA + flux2pro routes)
      * every trigger token the route needs must appear in the prompt
      * Hater routes must include the anti-Hellboy block
      * Daniel must never be rendered with the safety checker disabled (enforced
        by never exposing that knob; checked here for manifests that try)
      * covers must declare a title overlay and leave room for it
      * aspect ratio must be one we know how to QA
    """
    problems: list[str] = []
    route = ROUTES.get(spec.route)
    if route is None:
        return [f"{spec.id}: unknown route '{spec.route}' (known: {', '.join(ROUTES)})"]

    if route["family"] in {"flux-lora", "flux2pro"} and not spec.prompt.startswith(STYLE_BLOCK_PREFIXES):
        problems.append(f"{spec.id}: prompt does not begin with an approved style block")

    for trig in route["triggers"]:
        if trig not in spec.prompt:
            problems.append(f"{spec.id}: route '{spec.route}' requires trigger token {trig} in the prompt")

    marker = route.get("requires_marker")
    if marker and marker not in spec.prompt:
        problems.append(f"{spec.id}: Hater renders must include the anti-drift block containing '{marker}'")

    if route["family"] != "flux-lora" and any(t in spec.prompt for t in ("CHARACTERDADDANNY23", "CHARACTERDANIELBULL23", "CHARACTERHATER", "CHARACTERPROSECUTOR")):
        problems.append(f"{spec.id}: trigger tokens are meaningless on {route['model']} — describe the character in plain words instead")

    if spec.aspect_ratio not in ASPECT_TARGETS:
        problems.append(f"{spec.id}: unsupported aspect_ratio '{spec.aspect_ratio}'")

    if spec.kind == "cover":
        if not spec.title_overlay or not spec.title_overlay.get("text"):
            problems.append(f"{spec.id}: covers must declare title_overlay.text")
        if "title" not in spec.prompt.lower():
            problems.append(f"{spec.id}: cover prompt should reserve space for the title (mention 'kept clear for title text')")

    if spec.kind == "panel" and (spec.page is None or spec.slot not in {"A", "B"}):
        problems.append(f"{spec.id}: panels need 'page' and slot 'A'/'B'")

    if "disable_safety_checker" in json.dumps(spec.to_dict()):
        problems.append(f"{spec.id}: disable_safety_checker is not permitted in this pipeline")

    return problems


def validate_manifest(m: Manifest) -> list[str]:
    """Validate every spec plus manifest-level rules (2 panels per page, unique ids)."""
    problems: list[str] = []
    ids = [i.id for i in m.images]
    if len(ids) != len(set(ids)):
        problems.append("duplicate image ids in manifest")
    pages: dict[int, set[str]] = {}
    for spec in m.images:
        problems.extend(validate_spec(spec))
        if spec.kind == "panel" and spec.page is not None and spec.slot:
            pages.setdefault(spec.page, set()).add(spec.slot)
    for page, slots in sorted(pages.items()):
        if slots != {"A", "B"}:
            problems.append(f"page {page}: expected exactly panels A and B, found {sorted(slots)}")
    kinds = {i.kind for i in m.images}
    if "cover" in kinds:
        ratios = {i.aspect_ratio for i in m.images if i.kind == "cover"}
        if not {"16:9", "1:1"} <= ratios:
            problems.append("covers must include both a 16:9 and a 1:1 render")
    return problems


# --------------------------------------------------------------------------- #
# Prompt → API input                                                           #
# --------------------------------------------------------------------------- #


def build_input(spec: ImageSpec, ref_resolver=lambda p: p) -> dict[str, Any]:
    """Translate an ImageSpec into the exact ``input`` dict for its Replicate model."""
    route = ROUTES[spec.route]
    fam = route["family"]
    if fam == "flux-lora":
        inp = dict(FLUX_LORA_DEFAULTS)
        inp.update({"prompt": spec.prompt, "aspect_ratio": spec.aspect_ratio})
        if route["extra_lora"]:
            inp["extra_lora"] = route["extra_lora"]
        if spec.lora_scale is not None:
            inp["lora_scale"] = spec.lora_scale
        if spec.num_outputs is not None:
            inp["num_outputs"] = spec.num_outputs
        if spec.seed is not None:
            inp["seed"] = spec.seed
        return inp
    if fam == "flux2pro":
        inp = dict(FLUX2PRO_DEFAULTS)
        inp.update({"prompt": spec.prompt, "aspect_ratio": spec.aspect_ratio, "input_images": [ref_resolver(p) for p in spec.reference_images]})
        if spec.seed is not None:
            inp["seed"] = spec.seed
        return inp
    if fam == "gptimage2":
        inp = dict(GPTIMAGE2_DEFAULTS)
        inp.update({"prompt": spec.prompt, "aspect_ratio": _gpt_aspect(spec.aspect_ratio), "input_images": [ref_resolver(p) for p in spec.reference_images]})
        return inp
    raise ValidationError(f"unhandled model family {fam}")


def _gpt_aspect(ar: str) -> str:
    """gpt-image-2 accepts 1:1 / 3:2 / 2:3 (plus 'auto'); map wide covers to 3:2."""
    return {"16:9": "3:2", "9:16": "2:3", "1:1": "1:1", "3:2": "3:2", "2:3": "2:3"}.get(ar, "auto")


# --------------------------------------------------------------------------- #
# Replicate client (thin, dependency-light)                                    #
# --------------------------------------------------------------------------- #


class ReplicateClient:
    """Minimal Replicate REST client: create a prediction, poll, return output URLs."""

    def __init__(self, token: str, version_pins: dict[str, str] | None = None, timeout_s: int = 600):
        if requests is None:
            raise RuntimeError("the 'requests' package is required to call Replicate (pip install requests)")
        self.s = requests.Session()
        self.s.headers.update({"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
        self.version_pins = version_pins or {}
        self.timeout_s = timeout_s

    def predict(self, model: str, inp: dict[str, Any]) -> tuple[list[str], str, str]:
        """Run one prediction. Returns (output_urls, prediction_url, version_used)."""
        version = self.version_pins.get(model)
        if version:
            url = f"{REPLICATE_API}/predictions"
            body: dict[str, Any] = {"version": version, "input": inp}
        else:
            url = f"{REPLICATE_API}/models/{model}/predictions"
            body = {"input": inp}
        r = self.s.post(url, data=json.dumps(body), timeout=60)
        if r.status_code >= 400:
            raise RuntimeError(f"Replicate {r.status_code} creating prediction for {model}: {r.text[:500]}")
        pred = r.json()
        get_url = pred["urls"]["get"]
        t0 = time.time()
        while pred["status"] not in {"succeeded", "failed", "canceled"}:
            if time.time() - t0 > self.timeout_s:
                raise RuntimeError(f"prediction {pred['id']} timed out after {self.timeout_s}s")
            time.sleep(3)
            pred = self.s.get(get_url, timeout=60).json()
        if pred["status"] != "succeeded":
            raise RuntimeError(f"prediction {pred['id']} {pred['status']}: {pred.get('error')}")
        out = pred["output"]
        urls = out if isinstance(out, list) else [out]
        web_url = pred["urls"].get("web") or f"https://replicate.com/p/{pred['id']}"
        return urls, web_url, pred.get("version", version or "")

    def download(self, url: str, dest: Path) -> Path:
        dest.parent.mkdir(parents=True, exist_ok=True)
        with self.s.get(url, stream=True, timeout=120) as r:
            r.raise_for_status()
            with open(dest, "wb") as f:
                for chunk in r.iter_content(1 << 16):
                    f.write(chunk)
        return dest


# --------------------------------------------------------------------------- #
# QA                                                                           #
# --------------------------------------------------------------------------- #


def image_qa(path: Path, aspect_ratio: str, siblings: Iterable[Path] = ()) -> dict[str, Any]:
    """Automated checks: decodes, aspect within 2%, not a near-duplicate of siblings."""
    result: dict[str, Any] = {"ok": True, "problems": []}
    try:
        from PIL import Image  # type: ignore
    except Exception:  # pragma: no cover
        result["problems"].append("Pillow not installed; skipped image checks")
        return result
    try:
        with Image.open(path) as im:
            w, h = im.size
            result["size"] = [w, h]
            target = ASPECT_TARGETS[aspect_ratio]
            if abs((w / h) - target) / target > 0.02:
                result["ok"] = False
                result["problems"].append(f"aspect {w}x{h} off target {aspect_ratio}")
            result["phash"] = _phash(im)
    except Exception as e:  # corrupt download
        return {"ok": False, "problems": [f"cannot decode image: {e}"]}
    for sib in siblings:
        try:
            with Image.open(sib) as sim:
                if _hamming(result["phash"], _phash(sim)) <= 6:
                    result["ok"] = False
                    result["problems"].append(f"near-duplicate of {sib.name}")
        except Exception:
            continue
    return result


def _phash(im, hash_size: int = 8) -> str:
    """Tiny average-hash (good enough to catch identical character studies)."""
    g = im.convert("L").resize((hash_size, hash_size))
    px = list(g.get_flattened_data()) if hasattr(g, "get_flattened_data") else list(g.getdata())
    avg = sum(px) / len(px)
    bits = "".join("1" if p > avg else "0" for p in px)
    return f"{int(bits, 2):0{hash_size * hash_size // 4}x}"


def _hamming(a: str, b: str) -> int:
    return bin(int(a, 16) ^ int(b, 16)).count("1")


# --------------------------------------------------------------------------- #
# Cover title overlay                                                          #
# --------------------------------------------------------------------------- #


def overlay_title(src: Path, dest: Path, text: str, subtitle: str | None, style: dict[str, Any]) -> Path:
    """Draw the series title across the upper third of a cover (deterministic Pillow pass).

    ``style`` keys (from cover_style.json): font_path, fill, stroke, stroke_width,
    title_scale (fraction of width), subtitle_scale, top_margin (fraction of height).
    """
    from PIL import Image, ImageDraw, ImageFont  # type: ignore

    with Image.open(src).convert("RGBA") as im:
        W, H = im.size
        draw = ImageDraw.Draw(im)
        font_path = style.get("font_path")
        size = int(W * style.get("title_scale", 0.085))

        def load(sz: int):
            try:
                return ImageFont.truetype(font_path, sz) if font_path else ImageFont.load_default()
            except Exception:
                return ImageFont.load_default()

        font = load(size)
        # shrink until it fits with margins
        while draw.textlength(text, font=font) > W * 0.92 and size > 12:
            size -= 2
            font = load(size)
        y = int(H * style.get("top_margin", 0.06))
        x = (W - draw.textlength(text, font=font)) / 2
        draw.text((x, y), text, font=font, fill=style.get("fill", "#D9A441"), stroke_width=style.get("stroke_width", max(2, size // 12)), stroke_fill=style.get("stroke", "#0A0A0A"))
        if subtitle:
            sfont = load(int(size * style.get("subtitle_scale", 0.42)))
            sx = (W - draw.textlength(subtitle, font=sfont)) / 2
            draw.text((sx, y + size * 1.15), subtitle, font=sfont, fill=style.get("subtitle_fill", "#EDE3CF"), stroke_width=max(1, size // 24), stroke_fill=style.get("stroke", "#0A0A0A"))
        dest.parent.mkdir(parents=True, exist_ok=True)
        im.convert("RGB").save(dest, "WEBP", quality=style.get("quality", 90))
    return dest


# --------------------------------------------------------------------------- #
# Runner                                                                       #
# --------------------------------------------------------------------------- #


def run(manifest_path: Path, out_dir: Path, *, dry_run: bool, title_mode: str, max_predictions: int, refs_dir: Path | None, version_pins_path: Path | None, cover_style_path: Path | None) -> int:
    """Validate, render, QA, overlay, and write outputs. Returns a process exit code."""
    m = Manifest.load(manifest_path)
    problems = validate_manifest(m)
    if problems:
        for p in problems:
            LOG.error("VALIDATION: %s", p)
        return 1
    LOG.info("manifest OK: story %03d '%s' — %d images", m.story, m.title, len(m.images))

    version_pins = json.loads(version_pins_path.read_text()) if version_pins_path and version_pins_path.exists() else {}
    cover_style = json.loads(cover_style_path.read_text()) if cover_style_path and cover_style_path.exists() else {}

    def resolve_ref(p: str) -> str:
        # Replicate needs URLs or data URIs for input_images; local refs are inlined as data URIs.
        if p.startswith("http"):
            return p
        local = (refs_dir or Path(".")) / p
        import base64, mimetypes

        mime = mimetypes.guess_type(str(local))[0] or "image/webp"
        return f"data:{mime};base64,{base64.b64encode(local.read_bytes()).decode()}"

    if dry_run:
        for spec in m.images:
            inp = build_input(spec, ref_resolver=lambda p: f"<ref:{p}>")
            print(json.dumps({"id": spec.id, "model": ROUTES[spec.route]["model"], "input": {k: (v if k != "prompt" else v[:120] + "…") for k, v in inp.items()}}, indent=2))
        return 0

    token = os.environ.get("REPLICATE_API_TOKEN")
    if not token:
        LOG.error("REPLICATE_API_TOKEN is not set (read it from the project's replicate-key.txt into the environment; never into files)")
        return 2
    client = ReplicateClient(token, version_pins)

    raw_dir = out_dir / "raw"
    img_dir = out_dir / "images"
    raw_dir.mkdir(parents=True, exist_ok=True)
    img_dir.mkdir(parents=True, exist_ok=True)

    budget = max_predictions
    qa_failures = 0
    # Covers first (16:9 before 1:1), then panels in page order — pipeline §1.
    order = sorted(m.images, key=lambda s: (0 if s.kind == "cover" else 1, 0 if s.aspect_ratio == "16:9" else 1, s.page or 0, s.slot or ""))
    produced: list[Path] = []
    for spec in order:
        attempts = 0
        while True:
            if budget <= 0:
                LOG.error("prediction budget exhausted (--max-predictions); stopping")
                m.dump(out_dir / manifest_path.name)
                return 2
            attempts += 1
            budget -= 1
            inp = build_input(spec, ref_resolver=resolve_ref)
            if attempts == 2:  # retry: new seed + doubled anatomy guard
                inp["seed"] = int.from_bytes(hashlib.sha256(f"{spec.id}-retry".encode()).digest()[:4], "big")
                inp["prompt"] = inp["prompt"].replace("clean figure rendering", "clean figure rendering, clean figure rendering, single coherent figure")
            LOG.info("render %s via %s (attempt %d)", spec.id, ROUTES[spec.route]["model"], attempts)
            try:
                urls, pred_url, version = client.predict(ROUTES[spec.route]["model"], inp)
            except Exception as e:
                LOG.error("API error on %s: %s", spec.id, e)
                if attempts >= 2:
                    spec.needs_review = True
                    spec.qa = {"ok": False, "problems": [f"api error: {e}"]}
                    break
                continue
            spec.prediction_url, spec.model_version = pred_url, version
            spec.outputs = []
            qa_results = []
            for n, u in enumerate(urls):
                dest = raw_dir / f"{spec.id}-{attempts}-{n}.webp"
                client.download(u, dest)
                spec.outputs.append(str(dest))
                qa_results.append((dest, image_qa(dest, spec.aspect_ratio, siblings=produced)))
            good = [d for d, q in qa_results if q["ok"]]
            if good:
                spec.chosen = str(good[0])  # the reviewing agent may re-pick later
                spec.qa = dict(qa_results[[d for d, _ in qa_results].index(good[0])][1])
                break
            spec.qa = {"ok": False, "problems": sum((q["problems"] for _, q in qa_results), [])}
            if attempts >= 2:
                spec.needs_review = True
                spec.chosen = spec.outputs[0] if spec.outputs else None
                qa_failures += 1
                break
        if spec.chosen:
            final = img_dir / f"story{m.story:03d}-{spec.id}.webp"
            if spec.kind == "cover" and spec.title_overlay and title_mode == "pillow":
                overlay_title(Path(spec.chosen), final, spec.title_overlay["text"], spec.title_overlay.get("subtitle"), cover_style)
            else:
                final.write_bytes(Path(spec.chosen).read_bytes())
            produced.append(final)
            LOG.info("wrote %s%s", final, " (NEEDS REVIEW)" if spec.needs_review else "")
        m.dump(out_dir / manifest_path.name)  # checkpoint after every image

    LOG.info("done: %d images, %d need review, %d predictions left in budget", len(produced), qa_failures, budget)
    return 3 if qa_failures else 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("manifest", type=Path)
    ap.add_argument("--out", type=Path, default=None, help="story folder (default: manifest's folder)")
    ap.add_argument("--dry-run", action="store_true", help="validate and print API inputs; no network")
    ap.add_argument("--title-mode", choices=["pillow", "none"], default="pillow")
    ap.add_argument("--max-predictions", type=int, default=40, help="hard spend ceiling per run")
    ap.add_argument("--refs", type=Path, default=Path("references/approved"), help="folder holding reference images")
    ap.add_argument("--version-pins", type=Path, default=Path("tools/replicate_versions.json"))
    ap.add_argument("--cover-style", type=Path, default=Path("tools/cover_style.json"))
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args(argv)
    logging.basicConfig(level=logging.DEBUG if a.verbose else logging.INFO, format="%(levelname)s %(message)s")
    out = a.out or a.manifest.parent
    return run(a.manifest, out, dry_run=a.dry_run, title_mode=a.title_mode, max_predictions=a.max_predictions, refs_dir=a.refs, version_pins_path=a.version_pins, cover_style_path=a.cover_style)


if __name__ == "__main__":
    sys.exit(main())
