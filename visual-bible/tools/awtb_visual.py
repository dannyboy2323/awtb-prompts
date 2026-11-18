#!/usr/bin/env python3
"""AWTB visual bible builder.

Fetches published stories from Sanity, downloads every panel / cover / postcard,
and builds character, place, object, cover, postcard and style reference sheets
plus a machine-readable panel manifest.

Usage (run from the repository root)::

    python3 tools/awtb_visual.py fetch      # Sanity -> cache/ + stories.json
    python3 tools/awtb_visual.py sheets     # build refs/**.jpg
    python3 tools/awtb_visual.py manifest   # build panel-manifest.json
    python3 tools/awtb_visual.py all        # everything above

New stories: append the slug to ``STORIES`` and (after review) panel tags to
``panel_tags.py``; the rest is automatic.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import textwrap
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
import panel_tags as tags  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "cache"
REFS = ROOT / "refs"
PROJECT_ID, DATASET, API_VERSION = "d205mlci", "production", "v2024-01-01"
CDN = f"https://cdn.sanity.io/images/{PROJECT_ID}/{DATASET}/"
STORIES = {1: "riding-with-teddy-roosevelt-and-the-rough-riders", 2: "big-poppa"}
ROLE_ORDER = {"hero": 0, "ok": 1, "detail": 2, "offmodel": 3}
BG, FG, ACCENT, WARN = (24, 20, 17), (240, 226, 196), (214, 150, 52), (200, 52, 40)


# --------------------------------------------------------------------------- helpers
def asset_url(ref: str) -> tuple[str, str]:
    """Convert a Sanity asset ref (``image-<hash>-<WxH>-<ext>``) to ``(cdn_url, filename)``.

    Raises ValueError for refs that do not match the expected shape.
    """
    m = re.match(r"image-([0-9a-f]+)-(\d+)x(\d+)-(\w+)$", ref)
    if not m:
        raise ValueError(f"unrecognised asset ref: {ref!r}")
    h, w, ht, ext = m.groups()
    name = f"{h}-{w}x{ht}.{ext}"
    return CDN + name, name


def block_text(block: dict) -> str:
    """Return the plain text of one Portable Text block."""
    return "".join(c.get("text", "") for c in block.get("children", []))


def page_chunks(items: list, per_page: int) -> list[list]:
    """Split ``items`` into pages of at most ``per_page`` (always at least one page)."""
    if per_page < 1:
        raise ValueError("per_page must be >= 1")
    return [items[i:i + per_page] for i in range(0, len(items), per_page)] or [[]]


def wrap_text(text: str, width: int) -> list[str]:
    """Wrap ``text`` to ``width`` characters per line."""
    return textwrap.wrap(text, width=width) or [""]


def render_mode(img: Image.Image) -> str:
    """Classify a panel as ``white-cutout`` (isolated subject on white) or ``full-bleed``.

    Samples a 24px patch at each corner of a thumbnail and averages brightness.
    """
    g = img.convert("L").resize((128, 128))
    px = g.load()
    vals = [px[x, y] for cx in (0, 104) for cy in (0, 104) for x in range(cx, cx + 24) for y in range(cy, cy + 24)]
    return "white-cutout" if sum(vals) / len(vals) > 225 else "full-bleed"


def font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    """Load a TrueType font if one is available, else Pillow's default at ``size``."""
    for p in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
              "/usr/share/fonts/dejavu/DejaVuSans.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default(size)


# --------------------------------------------------------------------------- fetch
def fetch_story(slug: str) -> dict:
    """Query Sanity's public CDN API for one story document and return it."""
    q = urllib.parse.urlencode({"query": f'*[_type=="story" && slug.current=="{slug}"][0]'})
    url = f"https://{PROJECT_ID}.apicdn.sanity.io/{API_VERSION}/data/query/{DATASET}?{q}"
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)["result"]


def download(ref: str) -> Path:
    """Download an asset (cached) and return its local path."""
    url, name = asset_url(ref)
    CACHE.mkdir(exist_ok=True)
    dest = CACHE / name
    if not dest.exists():
        urllib.request.urlretrieve(url, dest)
    return dest


def cmd_fetch() -> None:
    """Fetch every configured story and write ``cache/stories.json`` (a normalised index)."""
    out = {}
    for n, slug in STORIES.items():
        doc = fetch_story(slug)
        entry = {"story": n, "slug": slug, "title": doc["title"], "id": doc["_id"], "panels": []}
        for key in ("coverImage", "coverImagePortrait", "postcard"):
            im = doc.get(key)
            if im:
                entry[key] = {"file": download(im["asset"]["_ref"]).name, "alt": im.get("alt"), "ref": im["asset"]["_ref"]}
        words, last_text, k = 0, "", 0
        body = doc["body"]
        for i, b in enumerate(body):
            if b["_type"] == "panelImage":
                k += 1
                ref = b["image"]["asset"]["_ref"]
                entry["panels"].append({"n": k, "file": download(ref).name, "ref": ref, "alignment": b.get("alignment"),
                                        "alt": b["image"].get("alt") or b.get("alt"), "words_since_prev_panel": words,
                                        "context": last_text[:160]})
                words = 0
            elif b["_type"] == "block":
                t = block_text(b)
                words += len(t.split())
                if t.strip():
                    last_text = t.strip()
        entry["total_words"] = sum(p["words_since_prev_panel"] for p in entry["panels"]) + words
        out[str(n)] = entry
        print(f"story {n}: {len(entry['panels'])} panels, {entry['total_words']} words")
    (CACHE / "stories.json").write_text(json.dumps(out, indent=1))


# --------------------------------------------------------------------------- sheets
def load_index() -> dict:
    """Load ``cache/stories.json`` (run ``fetch`` first)."""
    p = CACHE / "stories.json"
    if not p.exists():
        raise SystemExit("cache/stories.json missing - run `awtb_visual.py fetch` first")
    return json.loads(p.read_text())


def panel_path(index: dict, story: int, n: int) -> Path:
    """Return the cached file for panel ``n`` of ``story``."""
    for p in index[str(story)]["panels"]:
        if p["n"] == n:
            return CACHE / p["file"]
    raise KeyError(f"S{story}-p{n:02d} not found")


def draw_sheet(title: str, descriptor: str, footer: str, tiles: list[tuple[Path, str, str]], out: Path,
               cols: int = 5, tile: int = 380) -> None:
    """Render one reference-sheet page.

    ``tiles`` is a list of ``(image_path, caption, role)``; ``role == 'offmodel'`` gets a red frame.
    """
    pad, head = 14, 210
    rows = max(1, -(-len(tiles) // cols))
    width = cols * (tile + pad) + pad
    sheet = Image.new("RGB", (width, head + rows * (tile + 44 + pad) + 30), BG)
    d = ImageDraw.Draw(sheet)
    d.rectangle([0, 0, width, 8], fill=ACCENT)
    d.text((pad, 22), title, font=font(40, True), fill=ACCENT)
    for i, line in enumerate(wrap_text(descriptor, 150)[:5]):
        d.text((pad, 78 + i * 26), line, font=font(20), fill=FG)
    d.text((pad, head - 30), footer, font=font(16), fill=(170, 150, 120))
    for i, (path, cap, role) in enumerate(tiles):
        x, y = pad + (i % cols) * (tile + pad), head + (i // cols) * (tile + 44 + pad)
        im = Image.open(path).convert("RGB")
        im.thumbnail((tile, tile))
        ox, oy = x + (tile - im.width) // 2, y + (tile - im.height) // 2
        sheet.paste(im, (ox, oy))
        color = WARN if role == "offmodel" else (ACCENT if role == "hero" else (90, 80, 66))
        d.rectangle([x, y, x + tile, y + tile], outline=color, width=4 if role in ("hero", "offmodel") else 1)
        ident, _, note = cap.partition(" ")
        d.text((x + 2, y + tile + 4), ident + (" " + note.split("]")[0] + "]" if note.startswith("[") else ""),
               font=font(16, True), fill=color if role != "ok" else FG)
        rest = note.split("] ", 1)[1] if note.startswith("[") and "] " in note else (note if not note.startswith("[") else "")
        d.text((x + 2, y + tile + 24), rest[:44], font=font(14), fill=(190, 172, 140))
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, quality=84)


def sheets_for(group: dict[str, dict], folder: str, index: dict, per_page: int = 20) -> list[Path]:
    """Build paged sheets for every entry of ``group`` under ``refs/<folder>/``; return written paths."""
    written = []
    for key, spec in group.items():
        panels = sorted(spec["panels"], key=lambda p: (ROLE_ORDER[p[2]], p[0], p[1]))
        pages = page_chunks(panels, per_page)
        for pi, chunk in enumerate(pages, 1):
            tiles = [(panel_path(index, s, n), f"S{s}-p{n:02d} [{role}] {note}", role) for s, n, role, note in chunk]
            suffix = f"-{pi}" if len(pages) > 1 else ""
            out = REFS / folder / f"{key}{suffix}.jpg"
            trig = spec.get("trigger")
            footer = (f"LoRA trigger: {trig}   |   " if trig else "") + \
                     f"{len(panels)} panels   |   gold = hero reference   red = off-model / do not use as likeness   |   page {pi}/{len(pages)}"
            draw_sheet(spec["title"], spec["descriptor"], footer, tiles, out)
            written.append(out)
    return written


def cover_sheets(index: dict) -> list[Path]:
    """Build the covers and postcards reference sheets (each story's square cover, portrait cover, postcard)."""
    written = []
    for kind, keys, folder in (("covers", ("coverImage", "coverImagePortrait"), "covers"), ("postcards", ("postcard",), "postcards")):
        tiles = []
        for sid in sorted(index):
            for k in keys:
                e = index[sid].get(k)
                if e:
                    tiles.append((CACHE / e["file"], f"S{sid} {k} - {e.get('alt')}", "hero"))
        desc = {"covers": "Published covers: 1:1 (1024px) and 9:16 portrait (1152x2048). Retro comic-book trade dress: 'ADVENTURES WITH THE BULL' masthead in heavy ochre inked lettering, issue box top-left (story number), publisher bull-logo, price/date stamp, subtitle strip, pull-quote or tagline bottom.",
                "postcards": "Photo-composite souvenir postcards (3840x2880 / 4480x2998 PNG): real photos of Danny and Daniel composited in period costume over inked comic art with stamp, postmark, and hand-lettered 'Hola from Cuba!' / 'We're in Brooklyn!' headline. NOT generated by the LoRA models."}[kind]
        out = REFS / folder / f"{kind}.jpg"
        draw_sheet(f"AWTB {kind.title()}", desc, f"{len(tiles)} images", tiles, out, cols=2 if kind == "covers" else 2, tile=700)
        written.append(out)
    return written


def style_sheet(index: dict) -> list[Path]:
    """Group a sample of panels by render mode and write the style-DNA sheet."""
    buckets: dict[str, list] = {"full-bleed": [], "white-cutout": []}
    for sid in sorted(index):
        for p in index[sid]["panels"]:
            buckets[render_mode(Image.open(CACHE / p["file"]))].append((int(sid), p["n"]))
    written = []
    for mode, items in buckets.items():
        step = max(1, len(items) // 20)
        sample = items[::step][:20]
        tiles = [(panel_path(index, s, n), f"S{s}-p{n:02d}", "ok") for s, n in sample]
        desc = {"full-bleed": "Dominant mode: edge-to-edge inked scene, heavy blacks, amber/ochre/burnt-red palette, halftone grain, cinematic framing.",
                "white-cutout": "Secondary mode: isolated subject on white with ink splatter / torn-edge vignette - used for donut incidents, action beats, and emphasis."}[mode]
        out = REFS / "style" / f"style-{mode}.jpg"
        draw_sheet(f"Style DNA - {mode} ({len(items)} of {sum(map(len, buckets.values()))} panels)", desc, "sampled evenly", tiles, out)
        written.append(out)
    return written


def cmd_sheets() -> None:
    """Build every reference sheet."""
    idx = load_index()
    w = sheets_for(tags.CHARACTERS, "characters", idx)
    w += sheets_for(tags.PLACES_OBJECTS, "places-objects", idx)
    w += cover_sheets(idx) + style_sheet(idx)
    for p in w:
        print("wrote", p.relative_to(ROOT))


# --------------------------------------------------------------------------- manifest
def cmd_manifest() -> None:
    """Write ``panel-manifest.json``: every panel, cover and postcard with tags, URLs and pacing data."""
    idx = load_index()
    by_panel: dict[tuple[int, int], dict] = {}

    def slot(s: int, n: int) -> dict:
        return by_panel.setdefault((s, n), {"characters": {}, "places_objects": {}})

    for key, spec in tags.CHARACTERS.items():
        for s, n, role, note in spec["panels"]:
            slot(s, n)["characters"][key] = {"role": role, "note": note}
    for key, spec in tags.PLACES_OBJECTS.items():
        for s, n, role, note in spec["panels"]:
            slot(s, n)["places_objects"][key] = {"role": role, "note": note}
    out = {"project": PROJECT_ID, "generated_from": "Sanity published stories", "stories": []}
    for sid in sorted(idx):
        e = idx[sid]
        story = {"story": int(sid), "slug": e["slug"], "title": e["title"], "total_words": e["total_words"],
                 "url": f"https://www.adventureswiththebull.com/stories/{e['slug']}", "panels": [],
                 "images": {k: {"alt": e[k]["alt"], "url": CDN + e[k]["file"]} for k in ("coverImage", "coverImagePortrait", "postcard") if k in e}}
        for p in e["panels"]:
            t = by_panel.get((int(sid), p["n"]), {"characters": {}, "places_objects": {}})
            w, h = re.search(r"-(\d+)x(\d+)\.", p["file"]).groups()
            story["panels"].append({"id": f"S{sid}-p{p['n']:02d}", "n": p["n"], "alignment": p["alignment"], "alt": p["alt"],
                                    "size": [int(w), int(h)], "url": CDN + p["file"],
                                    "render_mode": render_mode(Image.open(CACHE / p["file"])),
                                    "words_since_prev_panel": p["words_since_prev_panel"], "context": p["context"],
                                    "characters": t["characters"], "places_objects": t["places_objects"]})
        out["stories"].append(story)
    (ROOT / "panel-manifest.json").write_text(json.dumps(out, indent=1))
    print("wrote panel-manifest.json")


def main(argv: list[str] | None = None) -> None:
    """CLI entry point."""
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cmd", choices=["fetch", "sheets", "manifest", "all"])
    a = ap.parse_args(argv)
    if a.cmd in ("fetch", "all"):
        cmd_fetch()
    if a.cmd in ("sheets", "all"):
        cmd_sheets()
    if a.cmd in ("manifest", "all"):
        cmd_manifest()


if __name__ == "__main__":
    main()
