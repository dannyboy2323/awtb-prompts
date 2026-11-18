#!/usr/bin/env python3
"""Build ``prompts/registry.json`` from the Replicate model docs in ``docs/replicate-models/``.

Every ``### Example (<prediction url>)`` block in those docs is a prompt that was actually run.
The registry records, per run: model, prediction URL, the full input (prompt + settings) and
output URLs, plus a ``status`` field the author/agent upgrades from ``logged`` to ``proven``
(used in a published story) or ``rejected``.  Existing statuses/notes are preserved on rebuild.

Usage::

    python3 tools/build_prompt_registry.py            # rewrite prompts/registry.json
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "replicate-models"
OUT = ROOT / "prompts" / "registry.json"

EXAMPLE_RE = re.compile(
    r"### Example \((?P<url>https://replicate\.com/p/[A-Za-z0-9]+)\)\s+"
    r"#### Input\s+```json\s+(?P<inp>.*?)\s+```\s+"
    r"#### Output\s+```json\s+(?P<out>.*?)\s+```",
    re.S,
)
MODEL_RE = re.compile(r"Model name:\s*(\S+)")


def parse_doc(text: str) -> list[dict]:
    """Return the logged runs found in one model doc (empty list if none)."""
    m = MODEL_RE.search(text)
    model = m.group(1) if m else None
    runs = []
    for e in EXAMPLE_RE.finditer(text):
        try:
            inp = json.loads(e.group("inp"))
            out = json.loads(e.group("out"))
        except json.JSONDecodeError:
            continue
        runs.append({
            "id": e.group("url").rsplit("/", 1)[-1],
            "model": model,
            "prediction_url": e.group("url"),
            "input": inp,
            "outputs": out,
            "status": "logged",
            "notes": "",
        })
    return runs


def build(docs_dir: Path = DOCS, existing: dict | None = None) -> dict:
    """Parse every doc under ``docs_dir`` and merge author statuses from ``existing``."""
    keep = {r["id"]: r for r in (existing or {}).get("runs", [])}
    runs = []
    for f in sorted(docs_dir.glob("*.md")):
        for r in parse_doc(f.read_text(encoding="utf-8")):
            r["source_doc"] = f.name
            if r["id"] in keep:
                r["status"] = keep[r["id"]].get("status", r["status"])
                r["notes"] = keep[r["id"]].get("notes", "")
            runs.append(r)
    return {"schema": 1, "runs": runs}


def main() -> None:
    """CLI entry point."""
    existing = json.loads(OUT.read_text()) if OUT.exists() else None
    reg = build(existing=existing)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(reg, indent=1, ensure_ascii=False))
    print(f"wrote {OUT.relative_to(ROOT)}: {len(reg['runs'])} runs")


if __name__ == "__main__":
    main()
