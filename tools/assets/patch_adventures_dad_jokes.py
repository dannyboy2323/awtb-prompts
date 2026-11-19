"""Write every story's dad joke into adventures.md (Stories 3-100).

Reads /home/claude/dad-jokes-map.json (built by build_dad_jokes.py) and patches
/home/claude/adventures.md in place:

* Stories 4-20 (full entries): replaces "`dad-jokes.yaml` #0NN." with the joke text.
* Story 13 (designated exception): keeps the exception note and adds the joke.
* Stories 21-50 and 76-88 (bold summary entries): appends a "**The Dad Joke (#NN):**" line.
* Stories 51-75 and 89-100 (bullet entries): appends the joke to the bullet.

Fails loudly if any story 3-100 ends up without exactly one joke reference.

Run:  python tools/patch_adventures_dad_jokes.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ADV = Path("/home/claude/adventures.md")
MAP = Path("/home/claude/dad-jokes-map.json")


def main() -> None:
    """Apply the patch and verify coverage."""
    jokes = {int(k): v for k, v in json.loads(MAP.read_text(encoding="utf-8")).items()}
    text = ADV.read_text(encoding="utf-8")

    # Version line
    text = text.replace(
        "### Version 1.1 — Nov 2026 revision:",
        "### Version 1.2 — Nov 2026 revision: every story's dad joke (Element 14) written in from `dad-jokes.yaml` v1.1;",
        1,
    )

    # Stories 4-20 full entries
    for n in range(4, 21):
        if n == 13:
            continue
        old = f"**The Dad Joke:** `dad-jokes.yaml` #{n:03d}."
        assert old in text, f"story {n}: field not found"
        text = text.replace(old, f'**The Dad Joke (#{n:03d}):** _"{jokes[n]}"_', 1)

    # Story 13 — exception note stays, joke added
    old13 = "**The Dad Joke:** Designated exception —"
    assert old13 in text
    text = text.replace(old13, f'**The Dad Joke (#013):** _"{jokes[13]}"_ Designated exception —', 1)

    # Bold summary entries: "**Story NN — TITLE**\n_body_\n" -> add joke line
    def add_after_summary(m: re.Match) -> str:
        n = int(m.group(1))
        return f'{m.group(0)}\n**The Dad Joke (#{n:03d}):** _"{jokes[n]}"_\n'

    text = re.sub(r"\*\*Story (\d+) — [^\n]+\*\*\n(?:_[^\n]+_|\*[^\n]+\*)\n", add_after_summary, text)

    # Bullet entries: "- _NN: ..._" -> append joke inside the italics
    def add_to_bullet(m: re.Match) -> str:
        n = int(m.group(1))
        return f'- _{n}: {m.group(2)} — Dad joke #{n:03d}: "{jokes[n]}"_'

    text = re.sub(r"- _(\d+): (.+?)_$", add_to_bullet, text, flags=re.M)

    # Verify: every story 3-100 references its joke exactly once
    missing = [n for n in range(3, 101) if text.count(jokes[n]) != 1]
    assert not missing, f"stories without exactly one joke reference: {missing}"

    # Pipeline note under HOW TO USE
    text = text.replace(
        "pulled from `dad-jokes.yaml` by story number",
        "written in below from `dad-jokes.yaml` (the index of record) by story number; never reused",
        1,
    )

    ADV.write_text(text, encoding="utf-8")
    print("adventures.md patched: stories 3-100 each carry exactly one unique dad joke")


if __name__ == "__main__":
    main()
