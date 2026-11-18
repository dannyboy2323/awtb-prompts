#!/usr/bin/env python3
"""Generate candidate reference renders for characters without a trained LoRA.

Uses flux-2-pro with published panels (public Sanity CDN URLs from ``data/panel-manifest.json``)
as ``input_images`` so the candidates stay faithful to what readers have already seen.
Outputs go to ``references/generated-refs/<character>/`` (candidates).  Approving one means
copying it to ``references/approved/<character>-NN.webp``.

Usage::

    export REPLICATE_API_TOKEN=...   # never written to disk
    python3 tools/generate_reference_candidates.py --max-predictions 12
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_story_images as g  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
STYLE = g.STYLE_BLOCK_PREFIXES[2] + (
    ", bold heavy black ink linework, dramatic chiaroscuro, deep blacks with muted earth tones, "
    "desaturated ochres and burnt reds, warm amber accents, rough crosshatching and halftone grain, "
    "woodcut-like rendering, strong geometric shadow shapes, flat cel shading, colored ink on paper"
)
TAIL = ("head and upper body portrait facing slightly three-quarter, plain solid white background, "
        "clean uncluttered composition, plain panel with no lettering or signatures")

# character -> (panel ids from the manifest used as visual references, description)
CHARACTERS: dict[str, tuple[list[str], str]] = {
    "johnny_cash": (["S1-p37", "S2-p32", "S2-p34"],
        "Johnny Cash as a translucent luminous holographic apparition, soft amber-white edge glow, "
        "dressed entirely in black, black coat and black shirt, dark swept-back hair, deeply lined weathered face, calm dry half-smile"),
    "old_timer": (["S1-p64", "S2-p43"],
        "the same ancient man as the references, deeply weathered face, milk-white clouded eyes that nonetheless seem to see everything, "
        "long white beard, a slight knowing amused smile, plain timeless wool coat"),
    "jen": (["S2-p10"],
        "the same woman as the reference, early forties, composed and warm, dark hair pulled back, clean strong facial structure, "
        "tired eyes that miss nothing, practical stylish clothing"),
    "grandpa": (["S1-p15"],
        "the same man as the reference, seventies, lean and quiet, flannel shirt, reading glasses pushed up on his forehead, unbothered expression"),
    "jenni": ([],
        "a beautiful woman in her late forties with understated natural beauty, no makeup, long natural wavy surfer blonde hair the color of dry hay "
        "worn loose and a little wild, fine-line botanical tattoos up one forearm, silver rings on most fingers, thrifted men's chambray shirt with rolled sleeves, "
        "warm open amused expression"),
}


# Per-character render attempts, tried in order until one succeeds.  Only documented, per-request
# knobs are used (flux-2-pro ``safety_tolerance``); the LoRA routes never relax any filter.
ATTEMPTS: dict[str, list[dict]] = {
    "johnny_cash": [
        {"route": "flux2pro", "safety_tolerance": 4},
        {"route": "gptimage2"},
        {"route": "flux2pro", "safety_tolerance": 5, "no_refs": True},
    ],
}


def panel_urls(manifest: dict) -> dict[str, str]:
    """Map panel id (e.g. ``S1-p37``) to its CDN URL."""
    out: dict[str, str] = {}
    for s in manifest["stories"]:
        for p in s.get("panels", []):
            out[p["id"]] = p["url"]
    return out


def build_spec(name: str, urls: dict[str, str]) -> g.ImageSpec:
    """Build the flux-2-pro ImageSpec for one character."""
    ids, desc = CHARACTERS[name]
    refs = [urls[i] for i in ids if i in urls]
    return g.ImageSpec(id=f"ref-{name}", kind="panel", page=0, slot="A", aspect_ratio="1:1",
                       route="flux2pro", prompt=f"{STYLE}, {desc}, {TAIL}", reference_images=refs)


def main(argv: list[str] | None = None) -> int:
    """Render ``--per`` candidates for each character and write them to references/generated-refs/."""
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--per", type=int, default=2, help="candidates per character")
    ap.add_argument("--only", nargs="*", help="subset of characters")
    ap.add_argument("--max-predictions", type=int, default=12)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    manifest = json.loads((ROOT / "data" / "panel-manifest.json").read_text())
    urls = panel_urls(manifest)
    pins = json.loads((ROOT / "tools" / "replicate_versions.json").read_text())
    names = a.only or list(CHARACTERS)
    if a.dry_run:
        for n in names:
            s = build_spec(n, urls)
            print(n, len(s.reference_images), "refs;", s.prompt[:90], "...")
        return 0
    client = g.ReplicateClient(os.environ["REPLICATE_API_TOKEN"], pins)
    budget = a.max_predictions
    log = []
    for n in names:
        spec = build_spec(n, urls)
        out_dir = ROOT / "references" / "generated-refs" / n
        for i in range(a.per):
            outs = None
            for att in ATTEMPTS.get(n, [{"route": "flux2pro"}]):
                if budget <= 0:
                    print("budget exhausted")
                    break
                budget -= 1
                sp = build_spec(n, urls)
                sp.route = att["route"]
                if att.get("no_refs"):
                    sp.reference_images = []
                inp = g.build_input(sp)
                inp["seed"] = 1000 + i
                if "safety_tolerance" in att and sp.route == "flux2pro":
                    inp["safety_tolerance"] = att["safety_tolerance"]
                model = g.ROUTES[sp.route]["model"]
                try:
                    outs, pred, ver = client.predict(model, inp)
                    break
                except RuntimeError as e:  # record the failure and try the next attempt
                    print("FAILED", n, i + 1, att, str(e)[:120])
                    log.append({"character": n, "attempt": att, "error": str(e)[:300]})
            if not outs:
                break
            dest = client.download(outs[0], out_dir / f"{n}-cand{i + 1}.webp")
            log.append({"character": n, "file": str(dest.relative_to(ROOT)), "prediction": pred, "version": ver,
                        "seed": inp["seed"], "model": model, "attempt": att, "prompt": sp.prompt, "reference_images": sp.reference_images})
            print("wrote", dest.relative_to(ROOT))
    lp = ROOT / "references" / "generated-refs" / "log.json"
    prev = json.loads(lp.read_text()) if lp.exists() else []
    lp.write_text(json.dumps(prev + log, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
