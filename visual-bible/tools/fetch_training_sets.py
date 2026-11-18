"""Download the four LoRA training albums from public Google Photos share links.

Usage: python3 fetch_training_sets.py OUT_DIR
Writes OUT_DIR/<character>/NN.jpg (w1024) and OUT_DIR/sheets/training-<character>.jpg.
"""
import os
import re
import subprocess
import sys

from PIL import Image, ImageDraw

ALBUMS = {
    "daniel": "ebNhqTtKBB6tiWWs7",
    "danny": "bFSvxbjxSwrqwTie7",
    "hater": "wSejzqJMvN4B4zwo9",
    "prosecutor": "ts3ZNdgmsNtJNJJA8",
    "teddy": "QiPf1ERpcQMbpGJG6",
}
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
URL_RE = re.compile(r"https://lh3\.googleusercontent\.com/pw/[A-Za-z0-9_-]+")


def _curl(url, out=None):
    """Fetch url with curl; return text if out is None else write file."""
    cmd = ["curl", "-sSL", "--max-time", "60", "-A", UA]
    cmd += ["-o", out, url] if out else [url]
    r = subprocess.run(cmd, capture_output=True, text=out is None, check=True)
    return None if out else r.stdout


def extract_urls(html):
    """Return the sorted unique image base URLs found in an album page."""
    return sorted(set(URL_RE.findall(html)))


def make_sheet(files, title, out, cols=6, tile=320):
    """Write a numbered contact sheet for files to out."""
    rows = (len(files) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * tile, rows * tile + 40), "#111")
    d = ImageDraw.Draw(sheet)
    d.text((10, 12), title, fill="white")
    for i, f in enumerate(files):
        im = Image.open(f).convert("RGB").resize((tile - 6, tile - 6))
        x, y = (i % cols) * tile, 40 + (i // cols) * tile
        sheet.paste(im, (x + 3, y + 3))
        d.text((x + 8, y + 8), f"{i + 1:02d}", fill="yellow")
    sheet.save(out, quality=85)


def main(out_dir):
    """Download every album and build its sheet."""
    os.makedirs(os.path.join(out_dir, "sheets"), exist_ok=True)
    for name, short in ALBUMS.items():
        urls = extract_urls(_curl(f"https://photos.app.goo.gl/{short}"))
        d = os.path.join(out_dir, name)
        os.makedirs(d, exist_ok=True)
        files = []
        for i, u in enumerate(urls, 1):
            f = os.path.join(d, f"{i:02d}.jpg")
            _curl(u + "=w1024", f)
            files.append(f)
        make_sheet(files, f"TRAINING SET: {name} ({len(files)} images)",
                   os.path.join(out_dir, "sheets", f"training-{name}.jpg"))
        print(name, len(files))


if __name__ == "__main__":
    main(sys.argv[1])
