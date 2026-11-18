"""Tests for tools/build_prompt_registry.py (offline)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import build_prompt_registry as b  # noqa: E402

DOC = """Model name: dannyboy2323/character-x

### Example (https://replicate.com/p/abc123)

#### Input

```json
{"prompt": "hello", "lora_scale": 1}
```

#### Output

```json
["https://replicate.delivery/a/out-0.webp"]
```
"""


def test_parse_doc_extracts_run():
    """One logged example becomes one registry run."""
    runs = b.parse_doc(DOC)
    assert len(runs) == 1
    r = runs[0]
    assert r["id"] == "abc123" and r["model"] == "dannyboy2323/character-x"
    assert r["input"]["prompt"] == "hello" and r["status"] == "logged"


def test_build_preserves_status(tmp_path):
    """Rebuilding keeps an author-assigned status and notes."""
    (tmp_path / "x.md").write_text(DOC)
    existing = {"runs": [{"id": "abc123", "status": "proven", "notes": "S1 p5"}]}
    reg = b.build(tmp_path, existing)
    assert reg["runs"][0]["status"] == "proven" and reg["runs"][0]["notes"] == "S1 p5"


def test_real_docs_parse():
    """The checked-in model docs yield at least one run."""
    assert len(b.build()["runs"]) >= 1
