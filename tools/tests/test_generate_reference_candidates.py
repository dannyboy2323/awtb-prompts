"""Offline tests for tools/generate_reference_candidates.py."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import generate_reference_candidates as r  # noqa: E402
import generate_story_images as g  # noqa: E402

M = json.loads((Path(__file__).resolve().parents[2] / "data" / "panel-manifest.json").read_text())


def test_every_reference_panel_exists_in_manifest():
    """All referenced panel ids resolve to CDN URLs."""
    urls = r.panel_urls(M)
    for name, (ids, _) in r.CHARACTERS.items():
        for i in ids:
            assert i in urls, (name, i)


def test_specs_pass_runner_validation():
    """Candidate specs are valid flux2pro specs (style block, no trigger tokens)."""
    urls = r.panel_urls(M)
    for name in r.CHARACTERS:
        s = r.build_spec(name, urls)
        s.kind, s.page, s.slot = "panel", 1, "A"
        assert g.validate_spec(s) == [], name
