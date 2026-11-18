"""Unit tests for awtb_visual and panel_tags (offline - no network)."""
import sys
from pathlib import Path

import pytest
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "visual_bible"))
import awtb_visual as av  # noqa: E402
import panel_tags as tags  # noqa: E402

MAX_PANELS = {1: 74, 2: 56}


def test_asset_url_roundtrip():
    url, name = av.asset_url("image-abc123-1024x1024-webp")
    assert name == "abc123-1024x1024.webp" and url.endswith(name) and "cdn.sanity.io" in url


def test_asset_url_rejects_garbage():
    with pytest.raises(ValueError):
        av.asset_url("file-xyz-pdf")


def test_page_chunks():
    assert av.page_chunks(list(range(45)), 20) == [list(range(20)), list(range(20, 40)), list(range(40, 45))]
    assert av.page_chunks([], 5) == [[]]
    with pytest.raises(ValueError):
        av.page_chunks([1], 0)


def test_wrap_text_never_empty():
    assert av.wrap_text("", 10) == [""]
    assert all(len(l) <= 10 for l in av.wrap_text("a quick brown fox jumps over", 10))


def test_render_mode():
    assert av.render_mode(Image.new("RGB", (200, 200), "white")) == "white-cutout"
    assert av.render_mode(Image.new("RGB", (200, 200), (20, 10, 5))) == "full-bleed"


def test_block_text():
    assert av.block_text({"children": [{"text": "a"}, {"text": "b"}]}) == "ab"


@pytest.mark.parametrize("group", [tags.CHARACTERS, tags.PLACES_OBJECTS])
def test_tags_valid(group):
    for key, spec in group.items():
        assert spec["title"] and spec["descriptor"], key
        seen = set()
        for s, n, role, note in spec["panels"]:
            assert role in av.ROLE_ORDER, (key, s, n)
            assert 1 <= n <= MAX_PANELS[s], (key, s, n)
            assert (s, n) not in seen, f"duplicate {key} S{s}-p{n}"
            assert note
            seen.add((s, n))


def test_every_character_has_a_hero_panel():
    for key, spec in tags.CHARACTERS.items():
        assert any(p[2] == "hero" for p in spec["panels"]), key


def test_draw_sheet_writes_file(tmp_path):
    img = tmp_path / "a.png"
    Image.new("RGB", (100, 100), "red").save(img)
    out = tmp_path / "o" / "s.jpg"
    av.draw_sheet("T", "desc " * 40, "foot", [(img, "cap", "hero"), (img, "cap2", "offmodel")], out)
    assert out.exists() and Image.open(out).width > 500
