"""Tests for tools/build_character_docs.py."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_character_docs as b  # noqa: E402


def test_extract_bible_stops_at_next_heading():
    text = "# A\nfoo\n---\n# B\nbar\n"
    assert b.extract_bible(text, "# A") == "# A\nfoo\n"
    assert b.extract_bible(text, "# B") == "# B\nbar\n"
    assert b.extract_bible(text, "# Z") is None


def test_extract_block_first_fence_after_marker():
    lib = "### 3.1 X\n\n```\nBLOCK ONE\n```\n\n### 3.2 Y\n```\nBLOCK TWO\n```\n"
    assert b.extract_block(lib, "### 3.2 Y") == "BLOCK TWO"
    assert b.extract_block(lib, "### nope") is None
    assert b.extract_block(lib, None) is None


def test_resolve_refs_dedups(tmp_path):
    (tmp_path / "a").mkdir()
    (tmp_path / "a/x.webp").write_bytes(b"x")
    got = b.resolve_refs(tmp_path, ["a/*.webp", "a/x.webp"])
    assert [p.name for p in got] == ["x.webp"]


def test_every_character_has_unique_slug():
    slugs = [c.slug for c in b.CHARACTERS]
    assert len(slugs) == len(set(slugs))
    assert "jenni" in slugs


def test_repo_docs_are_current():
    """The checked-in generated docs must match the generator (run build_character_docs.py to refresh)."""
    assert b.build(check=True) == []
