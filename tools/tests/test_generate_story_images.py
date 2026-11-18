"""Unit tests for tools/generate_story_images.py — validation and input building.

Run:  python -m pytest tools/tests -q
No network, no Replicate token required.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import generate_story_images as g  # noqa: E402

STYLE = "2D graphic novel illustration, inked comic book art, Mike Mignola art style, bold heavy ink linework"
HATER_BLOCK = "CHARACTERHATER, THE HATER, fully human, NOT Hellboy, NO horns"


def spec(**kw) -> g.ImageSpec:
    base = dict(id="p01-a", kind="panel", page=1, slot="A", aspect_ratio="1:1", route="daniel", prompt=f"{STYLE}, CHARACTERDANIELBULL23, young boy, eating a donut")
    base.update(kw)
    return g.ImageSpec.from_dict(base)


def test_valid_daniel_panel_passes():
    assert g.validate_spec(spec()) == []


def test_missing_trigger_is_rejected():
    s = spec(prompt=f"{STYLE}, a young boy eating a donut")
    problems = g.validate_spec(s)
    assert any("CHARACTERDANIELBULL23" in p for p in problems)


def test_missing_style_block_is_rejected():
    s = spec(prompt="CHARACTERDANIELBULL23, a boy, photorealistic")
    assert any("style block" in p for p in g.validate_spec(s))


def test_two_lora_route_requires_both_triggers():
    s = spec(route="danny+daniel", prompt=f"{STYLE}, CHARACTERDADDANNY23, bald bearded man and a boy")
    problems = g.validate_spec(s)
    assert any("CHARACTERDANIELBULL23" in p for p in problems)


def test_hater_requires_anti_hellboy_block():
    s = spec(route="hater", prompt=f"{STYLE}, CHARACTERHATER, portly man in a uniform")
    assert any("anti-drift" in p for p in g.validate_spec(s))
    ok = spec(route="hater", prompt=f"{STYLE}, {HATER_BLOCK}, portly man in a uniform")
    assert g.validate_spec(ok) == []


def test_flux2pro_rejects_trigger_tokens():
    s = spec(route="flux2pro", prompt=f"{STYLE}, CHARACTERDADDANNY23 standing in a forest")
    assert any("meaningless" in p for p in g.validate_spec(s))


def test_cover_requires_title_overlay_and_title_space():
    s = spec(id="cover-16x9", kind="cover", page=None, slot=None, aspect_ratio="16:9", prompt=f"{STYLE}, CHARACTERDANIELBULL23, turning a bull")
    problems = g.validate_spec(s)
    assert any("title_overlay" in p for p in problems)
    assert any("title" in p.lower() and "reserve" in p for p in problems)
    ok = spec(id="cover-16x9", kind="cover", page=None, slot=None, aspect_ratio="16:9", prompt=f"{STYLE}, CHARACTERDANIELBULL23, turning a bull, upper third kept clear for title text", title_overlay={"text": "ADVENTURES WITH THE BULL"})
    assert g.validate_spec(ok) == []


def test_safety_checker_cannot_be_disabled():
    s = spec()
    s.qa = {"disable_safety_checker": True}  # smuggled through any field
    assert any("disable_safety_checker" in p for p in g.validate_spec(s))


def test_manifest_requires_two_panels_per_page_and_both_covers(tmp_path: Path):
    data = {
        "story": 3,
        "slug": "i-saved-the-king",
        "title": "I Saved the King",
        "images": [
            {"id": "cover-16x9", "kind": "cover", "aspect_ratio": "16:9", "route": "daniel", "prompt": f"{STYLE}, CHARACTERDANIELBULL23, bull, upper third kept clear for title text", "title_overlay": {"text": "ADVENTURES WITH THE BULL"}},
            {"id": "p01-a", "kind": "panel", "page": 1, "slot": "A", "aspect_ratio": "1:1", "route": "daniel", "prompt": f"{STYLE}, CHARACTERDANIELBULL23, donut"},
        ],
    }
    p = tmp_path / "m.json"
    p.write_text(json.dumps(data))
    m = g.Manifest.load(p)
    problems = g.validate_manifest(m)
    assert any("page 1" in x for x in problems)
    assert any("16:9 and a 1:1" in x for x in problems)


def test_build_input_flux_lora_defaults_and_extra_lora():
    s = spec(route="danny+daniel", prompt=f"{STYLE}, CHARACTERDADDANNY23, CHARACTERDANIELBULL23, two figures", lora_scale=1.1, num_outputs=2)
    inp = g.build_input(s)
    assert inp["model"] == "dev" and inp["num_inference_steps"] == 28 and inp["guidance_scale"] == 3
    assert inp["extra_lora"] == "dannyboy2323/character-danielbull23"
    assert inp["lora_scale"] == 1.1 and inp["num_outputs"] == 2
    assert inp["disable_safety_checker"] is False
    assert inp["aspect_ratio"] == "1:1"


def test_build_input_flux2pro_inlines_refs():
    s = spec(route="flux2pro", prompt=f"{STYLE}, Johnny Cash as a translucent hologram", reference_images=["refs/cash.webp"])
    inp = g.build_input(s, ref_resolver=lambda p: f"data:{p}")
    assert inp["input_images"] == ["data:refs/cash.webp"]
    assert inp["resolution"] == "1 MP"


def test_gpt_aspect_mapping():
    assert g._gpt_aspect("16:9") == "3:2"
    assert g._gpt_aspect("1:1") == "1:1"
    assert g._gpt_aspect("weird") == "auto"


def test_manifest_roundtrip(tmp_path: Path):
    data = {"story": 3, "slug": "s", "title": "T", "notes": "keep me", "images": [spec().to_dict()]}
    p = tmp_path / "m.json"
    p.write_text(json.dumps(data))
    m = g.Manifest.load(p)
    out = tmp_path / "out.json"
    m.dump(out)
    back = json.loads(out.read_text())
    assert back["notes"] == "keep me" and back["images"][0]["id"] == "p01-a"


@pytest.mark.skipif(pytest.importorskip("PIL", reason="Pillow not installed") is None, reason="no PIL")
def test_image_qa_aspect_and_duplicates(tmp_path: Path):
    from PIL import Image

    a = tmp_path / "a.webp"
    b = tmp_path / "b.webp"
    Image.new("RGB", (1024, 1024), "black").save(a)
    Image.new("RGB", (1024, 1024), "black").save(b)
    ok = g.image_qa(a, "1:1")
    assert ok["ok"]
    dup = g.image_qa(b, "1:1", siblings=[a])
    assert not dup["ok"] and any("near-duplicate" in p for p in dup["problems"])
    bad = g.image_qa(a, "16:9")
    assert not bad["ok"]
