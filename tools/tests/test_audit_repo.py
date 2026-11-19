"""Tests for tools/audit_repo.py."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import audit_repo as a  # noqa: E402


def test_secret_scan_flags_token(tmp_path):
    (tmp_path / "x.md").write_text("token r8_" + "A" * 30)
    res = a.check_secrets(tmp_path)
    assert res[0][1] is False


def test_secret_scan_clean(tmp_path):
    (tmp_path / "x.md").write_text("nothing here")
    assert a.check_secrets(tmp_path)[0][1] is True


def test_repo_known_gaps_only():
    """The repository audit must be fully green."""
    fails = {name for name, ok, _ in a.run() if not ok}
    assert fails == set()
