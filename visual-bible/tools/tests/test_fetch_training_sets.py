"""Offline tests for fetch_training_sets."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from PIL import Image

import fetch_training_sets as f


def test_extract_urls_dedupes_and_sorts():
    """Duplicate base URLs collapse and order is stable."""
    h = '<a href="https://lh3.googleusercontent.com/pw/BBB=w9">x</a>' \
        '"https://lh3.googleusercontent.com/pw/AAA" "https://lh3.googleusercontent.com/pw/BBB"'
    assert f.extract_urls(h) == [
        "https://lh3.googleusercontent.com/pw/AAA",
        "https://lh3.googleusercontent.com/pw/BBB",
    ]


def test_make_sheet_writes(tmp_path):
    """A sheet is written for a handful of images."""
    fs = []
    for i in range(3):
        p = tmp_path / f"{i}.jpg"
        Image.new("RGB", (50, 50), "red").save(p)
        fs.append(str(p))
    out = tmp_path / "s.jpg"
    f.make_sheet(fs, "t", str(out))
    assert out.exists()
