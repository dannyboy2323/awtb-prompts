"""Generate the per-character documentation folders under ``characters/``.

For every recurring character this builds::

    characters/<slug>/bible.md          # extracted from canon/character-bible.md (Jenni's is hand-written; kept)
    characters/<slug>/image-guide.md    # model route, trigger, prompt block, refs, drift, sample prompt
    characters/<slug>/reference-sheet.jpg   # contact sheet of the approved/candidate reference images

and a top-level ``characters/README.md`` index.  Everything is derived from the single source of truth
(``canon/character-bible.md``, ``docs/image-prompt-library.md``, ``tools/replicate_versions.json`` and the
``references/`` tree), so re-running after a canon change keeps the docs in sync.

Usage::

    python3 tools/build_character_docs.py            # rewrite everything
    python3 tools/build_character_docs.py --check    # exit 1 if a generated file is out of date
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STYLE_BLOCK_HINT = "docs/image-prompt-library.md §2 (the STANDARD STYLE BLOCK — append verbatim, never alter)"


@dataclass
class Character:
    """Static description of one character's image-generation setup."""

    slug: str
    name: str
    bible_heading: str | None          # '# HEADING' in canon/character-bible.md (None = no dossier)
    route: str                          # human-readable route
    model: str | None                   # Replicate model slug, if any
    trigger: str | None = None
    library_marker: str | None = None   # text that precedes the fenced block in the prompt library
    ref_globs: list[str] = field(default_factory=list)
    status: str = ""
    drift: list[str] = field(default_factory=list)
    rules: list[str] = field(default_factory=list)
    sample_scene: str = ""


CHARACTERS: list[Character] = [
    Character(
        "danny", "Danny Boice (Dad)", "# DANNY BOICE",
        "LoRA (flux-dev)", "dannyboy2323/character-daddanny23", "CHARACTERDADDANNY23",
        "### 3.1 DANNY",
        ["references/training-sets/training-danny.jpg", "references/characters/danny-1.jpg", "references/characters/danny-2.jpg",
         "references/generated-refs/danny-light-beard-test/danny-light-brown.webp"],
        "Trained model + 130 published panels; reference sheets complete.",
        ["Light-brown beard drifts orange/ginger and grows past the chest unless 'NOT red, NOT orange, NOT grey' and 'chest-length' are in the prompt.",
         "Mignola style can make skin painterly; keep the standard style block verbatim."],
        ["Jeans and a t-shirt always (period costume goes OVER the tee).", "Never share a render with the Fun Police.",
         "With Daniel: Danny model primary + extra_lora Daniel, both trigger tokens in the prompt."],
        "CHARACTERDADDANNY23 at a kitchen table writing in a journal, late-night lamplight, plain dark t-shirt, steaming mug",
    ),
    Character(
        "daniel", "Daniel Boice (The Bull)", "# DANIEL BOICE",
        "LoRA (flux-dev)", "dannyboy2323/character-danielbull23", "CHARACTERDANIELBULL23",
        "### 3.2 DANIEL",
        ["references/training-sets/training-daniel.jpg", "references/characters/daniel-1.jpg", "references/characters/daniel-2.jpg"],
        "Trained model + published panels; reference sheets complete.",
        ["Training set is busts only: full-body shots need explicit 'slim build, tall for his age'.", "lora_scale 1.5 held once (mushroom-cloud fart panel)."],
        ["Eleven years old: always fully clothed; pulp-horror styling goes on the environment, not on him.",
         "Comedy register: 'EXAGGERATED comic reaction pose' works."],
        "CHARACTERDANIELBULL23 holding a chocolate-covered donut like a trophy, EXAGGERATED comic reaction pose, kitchen",
    ),
    Character(
        "jen", "Jen Boice (Mom)", "# JEN BOICE",
        "flux-2-pro / flux-2-max with reference images (no LoRA)", "black-forest-labs/flux-2-pro", None,
        "**Jen (the Mother):**",
        ["references/characters/jen.jpg", "references/generated-refs/jen/jen-cand1.webp", "references/generated-refs/jen/jen-cand2.webp"],
        "No approved render set yet — candidates only (pending author approval).",
        ["Her car rotates every story (S1 green Wrangler, S2 blue Audi A7): never reuse, never purple."],
        ["Pass 2–3 approved Jen renders as input_images; describe the car for the current story."],
        "an elegant woman in her early forties beside this story's car, composed warm expression, tired eyes that miss nothing",
    ),
    Character(
        "jenni", "Jenni (Jennifer Lewis, Danny's girlfriend)", "# JENNI",
        "flux-2-max with approved reference images (no LoRA)", "black-forest-labs/flux-2-max", None,
        "**Jenni (the Girlfriend — introduced Story 3)**",
        ["references/approved/jenni/*.webp"],
        "APPROVED reference set (8 images) supplied by the author 2026-11-19.",
        ["Hair is curly (not straight/wavy); flower and gold-turquoise forehead band must stay.",
         "'40-year-old' is a prompt lever for a youthful read; canon age is 47.", "Keep tattoos on BOTH arms."],
        ["Feed 3–6 of the approved images as input_images; vary only camera angle/crop/footwear.",
         "Always the purple Jeep Wrangler 'Delilah' when a vehicle appears.", "Never render her with the Fun Police.",
         "Author's original prompt: `prompts/characters/jenni-prompt.original.md`; exact request/config: `prompts/characters/jenni-request.flux-2-max.json` (aspect 1:1, resolution '1 MP', safety_tolerance 2, webp q80); model doc: `docs/replicate-models/jenni-flux-2-max.md`."],
        "the same woman as the reference images standing barefoot in a warm apartment kitchen, laughing behind both hands",
    ),
    Character(
        "johnny-cash", "Johnny Cash (the Hologram Guide)", "# JOHNNY CASH",
        "gpt-image-2 (flux-2-pro safety-flags the likeness)", "openai/gpt-image-2", None,
        "**Johnny Cash (the Guide)**",
        ["references/approved/johnny_cash-01.webp", "references/approved/johnny_cash-02.webp", "references/characters/johnny_cash.jpg"],
        "APPROVED hologram renders (glowing cyan contour) — the Story 1–2 look.",
        ["flux-2-pro returns E005 even at safety_tolerance 4 — do not retry or bypass; use gpt-image-2."],
        ["ALWAYS an obvious hologram (translucent, cyan contour glow, background visible through him).", "Always dressed in black.",
         "Visible only to Danny and Daniel — nobody else reacts to him."],
        "Johnny Cash as a translucent cyan-contour hologram in black, standing in a period street, speaking to two figures",
    ),
    Character(
        "old-timer", "The Old-Timer", "# THE OLD-TIMER",
        "flux-2-pro with reference images (or LoRA to be trained)", "black-forest-labs/flux-2-pro", None,
        "**The Old-Timer:**",
        ["references/characters/old_timer.jpg", "references/generated-refs/old_timer/old_timer-cand1.webp", "references/generated-refs/old_timer/old_timer-cand2.webp"],
        "Candidates only (pending approval).",
        ["Must stay in period clothing each story but the face, white beard and milk-white eyes are constant."],
        ["Milk-white clouded eyes are canon.", "Costume changes with the era; he is always 'slightly out of place'."],
        "an ancient man of indeterminate age in the clothing of this story's era, milk-white clouded eyes, long white beard, knowing smile",
    ),
    Character(
        "grandpa", "Grandpa (Danny's father)", "# GRANDPA",
        "flux-2-pro with reference images", "black-forest-labs/flux-2-pro", None,
        "**Grandpa (Danny's father):**",
        ["references/characters/grandpa.jpg", "references/generated-refs/grandpa/grandpa-cand1.webp", "references/generated-refs/grandpa/grandpa-cand2.webp"],
        "One published panel (S1-p15) + candidates (pending approval).",
        ["Published panel: swept-back brown-gray hair, short graying beard, wire-rim glasses, dark work jacket, drives a truck — the library's flannel/mug block does NOT match it; reconcile."],
        ["Peripheral character; says 'Evening.'"],
        "a lean quiet man in his seventies with wire-rim glasses and a short graying beard, dark work jacket, at a kitchen window",
    ),
    Character(
        "prosecutor", "The Prosecutor (Fun Police)", "# THE PROSECUTOR",
        "LoRA (flux-dev)", "dannyboy2323/character-prosecutor", "CHARACTERPROSECUTOR",
        "### 3.4 THE PROSECUTOR",
        ["references/training-sets/training-prosecutor.jpg", "references/characters/prosecutor.jpg", "references/generated-refs/prosecutor-trigger-test/plain.webp"],
        "Trained; trigger confirmed (no hash).",
        ["Training set reads more menacing than the bible's vain/hollow — keep expression 'smug, hollow'."],
        ["Period stories: dressed for the era inside a hairbrained scheme (pinstripe suit often underneath). Modern day: slicked-back hair.",
         "Never in the same render as Danny/Daniel (route is hater+prosecutor two-LoRA)."],
        "CHARACTERPROSECUTOR in period costume practising a courtroom pose in a puddle reflection, one hand raised",
    ),
    Character(
        "hater", "The Hater (Fun Police)", "# THE HATER",
        "LoRA (flux-dev)", "dannyboy2323/character-hater", "CHARACTERHATER",
        "### 3.3 THE HATER",
        ["references/training-sets/training-hater.jpg", "references/characters/hater.jpg"],
        "Trained; needs the mandatory anti-Hellboy block.",
        ["The Mignola style drags this model toward Hellboy (red skin, horns): always append the anti-drift block."],
        ["Period stories: era costume (e.g. monk's habit over the uniform; hat doesn't fit under the hood). Modern day: baseball cap with the FBOP logo.",
         "Indomitable; survives everything."],
        "CHARACTERHATER in a monk's habit over his navy uniform, up a tree, holding a squirrel and a clipboard, mid-whine",
    ),
    Character(
        "teddy-roosevelt", "Theodore Roosevelt (Story 1 historical figure)", None,
        "LoRA trained on stills (model slug to be confirmed)", None, None, None,
        ["references/training-sets/training-teddy.jpg", "references/characters/teddy_roosevelt.jpg"],
        "Training set contact sheet captured; model name unconfirmed.",
        ["Round wire spectacles, walrus mustache, slouch hat, khaki Rough Rider uniform, yellow neckerchief with blue polka-dot bandana, bandoliers, saber."],
        ["Public figure from history: fine to depict in the Mignola register; never use photos of living people."],
        "Theodore Roosevelt in Rough Rider khakis and round wire spectacles, grinning, saber raised, Cuban hillside",
    ),
    Character(
        "biggie", "Biggie Smalls (Story 2 historical figure)", None,
        "no trained model (use published panels as references)", None, None, None,
        ["references/characters/biggie.jpg"],
        "Reference sheet from Story 2 published panels.",
        ["Keep period-accurate 1992–94 Brooklyn styling."],
        ["Public figure from history: depict in the Mignola register."],
        "a heavyset young man in a crisp 1990s Brooklyn outfit and Kangol hat, stoop at dusk",
    ),
    Character(
        "marcus-chen", "Marcus Chen (Jen's husband)", "# MARCUS CHEN",
        "no image setup yet", None, None, None, [],
        "No visuals exist; bible only. Add refs before first appearance.",
        [], ["Minor, present-day only."], "",
    ),
    Character(
        "sacred-eternal-fire", "The Sacred Eternal Fire", "# THE SACRED ETERNAL FIRE",
        "any model (an effect, not a character)", None, None, None,
        ["references/places-objects/sacred_eternal_flame.jpg", "references/places-objects/fart_and_shockwaves.jpg"],
        "Effect refs only.", ["Cosmic ring of hooded keepers + standing stones (S1-p66) is the consistent registered image."],
        ["The fart/shockwave register must be NEW each story."], "",
    ),
    Character(
        "time", "Time", "# TIME",
        "any model (an effect, not a character)", None, None, None,
        ["references/places-objects/space_time_continuum.jpg"],
        "Effect refs only.", ["The crack has two registers: fiery canyon fissure (S1) and lightning rift (S2)."],
        ["Bystanders never see the crack."], "",
    ),
]


def extract_bible(canon_text: str, heading: str) -> str | None:
    """Return the dossier for ``heading`` (e.g. '# JEN BOICE') from the character bible, or None."""
    lines = canon_text.split("\n")
    try:
        start = lines.index(heading)
    except ValueError:
        return None
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("# ") and not lines[i].startswith("## "):
            end = i
            break
    body = "\n".join(lines[start:end]).rstrip()
    # trailing '---' separators are decorative
    body = re.sub(r"\n---\s*$", "", body).rstrip()
    return body + "\n"


def extract_block(library_text: str, marker: str | None) -> str | None:
    """Return the first fenced code block that follows ``marker`` in the prompt library."""
    if not marker or marker not in library_text:
        return None
    tail = library_text.split(marker, 1)[1]
    m = re.search(r"```[a-z]*\n(.*?)\n```", tail, re.S)
    return m.group(1) if m else None


def resolve_refs(root: Path, globs: list[str]) -> list[Path]:
    """Expand reference globs (relative to ``root``) into existing files, sorted and de-duplicated."""
    out: list[Path] = []
    for g in globs:
        out.extend(sorted(root.glob(g)))
    seen: set[Path] = set()
    uniq = []
    for p in out:
        if p not in seen and p.is_file():
            seen.add(p)
            uniq.append(p)
    return uniq


def contact_sheet(files: list[Path], dest: Path, thumb: int = 360, cols: int = 4) -> bool:
    """Write a labeled JPEG contact sheet of ``files``. Returns False if there is nothing to draw."""
    if not files:
        return False
    from PIL import Image, ImageDraw

    rows = (len(files) + cols - 1) // cols
    label_h = 36
    sheet = Image.new("RGB", (cols * thumb, rows * (thumb + label_h)), "white")
    draw = ImageDraw.Draw(sheet)
    for i, f in enumerate(files):
        im = Image.open(f).convert("RGB")
        im.thumbnail((thumb, thumb))
        x, y = (i % cols) * thumb, (i // cols) * (thumb + label_h)
        sheet.paste(im, (x + (thumb - im.width) // 2, y))
        draw.text((x + 6, y + thumb + 8), f.name[:48], fill="black")
    dest.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(dest, quality=85)
    return True


def render_image_guide(c: Character, block: str | None, refs: list[Path], pins: dict[str, str], root: Path) -> str:
    """Render ``image-guide.md`` for one character."""
    pin = pins.get(c.model or "", "")
    L = [f"# {c.name} — Image Generation Guide", "",
         f"_Generated by `tools/build_character_docs.py` from canon + the prompt library. Do not hand-edit; edit the sources._", "",
         f"- **Bible:** `characters/{c.slug}/bible.md`" if c.bible_heading else "- **Bible:** none (not a dossier character)",
         f"- **Route:** {c.route}",
         f"- **Replicate model:** `{c.model}`" + (f" (pinned `{pin[:8]}…{pin[-4:]}` in `tools/replicate_versions.json`)" if pin else "") if c.model else "- **Replicate model:** none",
         f"- **Trigger token:** `{c.trigger}`" if c.trigger else "- **Trigger token:** none",
         f"- **Status:** {c.status}", ""]
    L += ["## Prompt block (verbatim from `docs/image-prompt-library.md`)", ""]
    L += (["```", block, "```"] if block else ["_No standard block recorded — write from the bible's physical description._"])
    L += ["", f"Append the standard style block: {STYLE_BLOCK_HINT}.", ""]
    L += ["## Reference images", ""]
    L += ([f"- `{p.relative_to(root)}`" for p in refs] if refs else ["- _None yet._"])
    L += ["", "See also `characters/%s/reference-sheet.jpg`." % c.slug if refs else "", ""]
    if c.rules:
        L += ["## Rules"] + [f"- {r}" for r in c.rules] + [""]
    if c.drift:
        L += ["## Known drift / pitfalls"] + [f"- {d}" for d in c.drift] + [""]
    if c.sample_scene:
        L += ["## Sample scene prompt (fill the style block and aspect ratio from the library)", "",
              "```", f"{c.sample_scene}", "```", ""]
    L += ["## Proven runs", "",
          "See `prompts/registry.json` (filter by this model) and `docs/replicate-models/`.", ""]
    return "\n".join(l for l in L) + "\n"


def build(root: Path = ROOT, check: bool = False) -> list[str]:
    """Generate all character docs. Returns a list of paths that changed (or would change when ``check``)."""
    canon = (root / "canon/character-bible.md").read_text()
    library = (root / "docs/image-prompt-library.md").read_text()
    pins = json.loads((root / "tools/replicate_versions.json").read_text())
    changed: list[str] = []

    def write(path: Path, text: str) -> None:
        old = path.read_text() if path.exists() else None
        if old != text:
            changed.append(str(path.relative_to(root)))
            if not check:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text)

    index = ["# Characters", "",
             "One folder per recurring character: `bible.md` (canon dossier), `image-guide.md` (how to render them), `reference-sheet.jpg`.", "",
             "| Character | Route | Trigger | References | Status |", "|---|---|---|---|---|"]
    for c in CHARACTERS:
        d = root / "characters" / c.slug
        if c.bible_heading and c.slug != "jenni":  # Jenni's v2.0 bible is hand-written and authoritative
            body = extract_bible(canon, c.bible_heading)
            if body:
                write(d / "bible.md", f"<!-- Extracted from canon/character-bible.md by tools/build_character_docs.py. Edit the canon file, not this copy. -->\n\n{body}")
        refs = resolve_refs(root, c.ref_globs)
        write(d / "image-guide.md", render_image_guide(c, extract_block(library, c.library_marker), refs, pins, root))
        if not check and refs:
            contact_sheet(refs, d / "reference-sheet.jpg")
        index.append(f"| [{c.name}](./{c.slug}/image-guide.md) | {c.route} | {('`'+c.trigger+'`') if c.trigger else '—'} | {len(refs)} | {c.status} |")
    write(root / "characters/README.md", "\n".join(index) + "\n")
    return changed


def main(argv: list[str] | None = None) -> int:
    """CLI entry point."""
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--check", action="store_true", help="fail if generated docs are stale")
    args = ap.parse_args(argv)
    changed = build(check=args.check)
    for p in changed:
        print(("STALE " if args.check else "wrote ") + p)
    return 1 if (args.check and changed) else 0


if __name__ == "__main__":
    sys.exit(main())
