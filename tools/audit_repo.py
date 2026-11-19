"""Coverage audit for the AWTB config repository.

Checks that the repository contains everything an LLM needs to generate a story end to end:
canon docs, asset libraries, per-character bibles / image guides / references, Replicate model docs and
version pins, story outlines/manuscripts, workflow docs, and that no secrets are committed.

Usage::

    python3 tools/audit_repo.py            # print a table, exit 1 on any failure
    python3 tools/audit_repo.py --markdown # emit a Markdown table (used for AUDIT.md)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

CANON = ["series-bible", "character-bible", "world-guide", "style-voice-guide", "timeline-continuity-bible",
         "theme-symbol-guide", "project-instructions"]
ASSETS = ["adventures.md", "intros.yaml", "phrases.yaml", "prison_sayings.yaml", "story_lessons.yaml", "dad-jokes.yaml"]
DOCS = ["docs/image-generation-pipeline.md", "docs/image-prompt-library.md", "docs/visual-bible.md",
        "docs/pipeline-corrections.md", "WORKFLOW.md", "README.md"]
MODELS = ["dannyboy2323/character-daddanny23", "dannyboy2323/character-danielbull23", "dannyboy2323/character-hater",
          "dannyboy2323/character-prosecutor", "black-forest-labs/flux-2-pro", "black-forest-labs/flux-2-max", "openai/gpt-image-2"]
SECRET_PATTERNS = [re.compile(r"r8_[A-Za-z0-9]{20,}"), re.compile(r"sk-[A-Za-z0-9]{20,}"),
                   re.compile(r"ghp_[A-Za-z0-9]{20,}")]
Result = tuple[str, bool, str]


def check_files(root: Path) -> list[Result]:
    """Verify required canon/asset/doc files exist and are non-empty."""
    res: list[Result] = []
    for name in CANON:
        p = root / "canon" / f"{name}.md"
        res.append((f"canon/{name}.md", p.is_file() and p.stat().st_size > 500, ""))
    for name in ASSETS:
        p = root / "assets" / name
        res.append((f"assets/{name}", p.is_file() and p.stat().st_size > 200, ""))
    for name in DOCS:
        p = root / name
        res.append((name, p.is_file() and p.stat().st_size > 200, ""))
    return res


def check_characters(root: Path) -> list[Result]:
    """Every character folder has an image guide; dossier characters have a bible; imaged ones have references."""
    res: list[Result] = []
    base = root / "characters"
    for d in sorted(p for p in base.iterdir() if p.is_dir()):
        guide = (d / "image-guide.md").is_file()
        bible = (d / "bible.md").is_file()
        sheet = (d / "reference-sheet.jpg").is_file()
        res.append((f"characters/{d.name}/image-guide.md", guide, ""))
        res.append((f"characters/{d.name}/bible.md", bible or d.name in {"teddy-roosevelt", "biggie"}, "historical figure: no dossier" if not bible else ""))
        res.append((f"characters/{d.name}/reference-sheet.jpg", sheet or d.name in {"marcus-chen"}, "no refs yet" if not sheet else ""))
    return res


def check_models(root: Path) -> list[Result]:
    """Each model used has a pinned version and appears in the docs/registry."""
    pins = json.loads((root / "tools/replicate_versions.json").read_text())
    docs_text = "\n".join(p.read_text() for p in (root / "docs").rglob("*.md"))
    reg = (root / "prompts/registry.json").read_text()
    res: list[Result] = []
    for m in MODELS:
        res.append((f"pin: {m}", m in pins, ""))
        res.append((f"documented: {m}", m in docs_text or m in reg, ""))
    return res


def check_stories(root: Path) -> list[Result]:
    """Outlines exist for stories 1–3; story 1 has a manuscript."""
    res: list[Result] = []
    for n in (1, 2, 3):
        res.append((f"story{n:03d} outline", (root / f"stories/story{n:03d}/story{n:03d}-outline.md").is_file(), ""))
    res.append(("story001 manuscript", (root / "stories/story001/story001-manuscript.md").is_file(), ""))
    res.append(("story002 manuscript", (root / "stories/story002/story002-manuscript.md").is_file(),
                "MISSING — not in the Claude Project; supply or extract from the published site"))
    return res


def check_secrets(root: Path) -> list[Result]:
    """No obvious secrets in tracked text files."""
    bad: list[str] = []
    for p in root.rglob("*"):
        if not p.is_file() or ".git" in p.parts or "__pycache__" in p.parts or ".pytest_cache" in p.parts or p.suffix.lower() in {".webp", ".jpg", ".png", ".jpeg", ".pyc"}:
            continue
        if p.stat().st_size > 2_000_000:
            continue
        try:
            txt = p.read_text(errors="ignore")
        except OSError:
            continue
        if any(rx.search(txt) for rx in SECRET_PATTERNS):
            bad.append(str(p.relative_to(root)))
    return [("no secrets committed", not bad, ", ".join(bad))]


def run(root: Path = ROOT) -> list[Result]:
    """Run every check."""
    return check_files(root) + check_characters(root) + check_models(root) + check_stories(root) + check_secrets(root)


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--markdown", action="store_true")
    args = ap.parse_args(argv)
    results = run()
    fails = [r for r in results if not r[1]]
    if args.markdown:
        print("| Check | Result | Note |\n|---|---|---|")
        for name, ok, note in results:
            print(f"| `{name}` | {'PASS' if ok else 'FAIL'} | {note} |")
    else:
        for name, ok, note in results:
            print(f"{'PASS' if ok else 'FAIL'}  {name}  {note}")
        print(f"\n{len(results) - len(fails)}/{len(results)} passed")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
