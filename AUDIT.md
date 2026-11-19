# AWTB Repository Audit

_Run 2026-11-18 with `python3 tools/audit_repo.py --markdown` (re-run any time; it is also a unit test in CI)._

## Automated coverage

| Check | Result | Note |
|---|---|---|
| `canon/series-bible.md` | PASS |  |
| `canon/character-bible.md` | PASS |  |
| `canon/world-guide.md` | PASS |  |
| `canon/style-voice-guide.md` | PASS |  |
| `canon/timeline-continuity-bible.md` | PASS |  |
| `canon/theme-symbol-guide.md` | PASS |  |
| `canon/project-instructions.md` | PASS |  |
| `assets/adventures.md` | PASS |  |
| `assets/intros.yaml` | PASS |  |
| `assets/phrases.yaml` | PASS |  |
| `assets/prison_sayings.yaml` | PASS |  |
| `assets/story_lessons.yaml` | PASS |  |
| `assets/dad-jokes.yaml` | PASS |  |
| `docs/image-generation-pipeline.md` | PASS |  |
| `docs/image-prompt-library.md` | PASS |  |
| `docs/visual-bible.md` | PASS |  |
| `docs/pipeline-corrections.md` | PASS |  |
| `WORKFLOW.md` | PASS |  |
| `README.md` | PASS |  |
| `characters/biggie/image-guide.md` | PASS |  |
| `characters/biggie/bible.md` | PASS | historical figure: no dossier |
| `characters/biggie/reference-sheet.jpg` | PASS |  |
| `characters/daniel/image-guide.md` | PASS |  |
| `characters/daniel/bible.md` | PASS |  |
| `characters/daniel/reference-sheet.jpg` | PASS |  |
| `characters/danny/image-guide.md` | PASS |  |
| `characters/danny/bible.md` | PASS |  |
| `characters/danny/reference-sheet.jpg` | PASS |  |
| `characters/grandpa/image-guide.md` | PASS |  |
| `characters/grandpa/bible.md` | PASS |  |
| `characters/grandpa/reference-sheet.jpg` | PASS |  |
| `characters/hater/image-guide.md` | PASS |  |
| `characters/hater/bible.md` | PASS |  |
| `characters/hater/reference-sheet.jpg` | PASS |  |
| `characters/jen/image-guide.md` | PASS |  |
| `characters/jen/bible.md` | PASS |  |
| `characters/jen/reference-sheet.jpg` | PASS |  |
| `characters/jenni/image-guide.md` | PASS |  |
| `characters/jenni/bible.md` | PASS |  |
| `characters/jenni/reference-sheet.jpg` | PASS |  |
| `characters/johnny-cash/image-guide.md` | PASS |  |
| `characters/johnny-cash/bible.md` | PASS |  |
| `characters/johnny-cash/reference-sheet.jpg` | PASS |  |
| `characters/marcus-chen/image-guide.md` | PASS |  |
| `characters/marcus-chen/bible.md` | PASS |  |
| `characters/marcus-chen/reference-sheet.jpg` | PASS | no refs yet |
| `characters/old-timer/image-guide.md` | PASS |  |
| `characters/old-timer/bible.md` | PASS |  |
| `characters/old-timer/reference-sheet.jpg` | PASS |  |
| `characters/prosecutor/image-guide.md` | PASS |  |
| `characters/prosecutor/bible.md` | PASS |  |
| `characters/prosecutor/reference-sheet.jpg` | PASS |  |
| `characters/sacred-eternal-fire/image-guide.md` | PASS |  |
| `characters/sacred-eternal-fire/bible.md` | PASS |  |
| `characters/sacred-eternal-fire/reference-sheet.jpg` | PASS |  |
| `characters/teddy-roosevelt/image-guide.md` | PASS |  |
| `characters/teddy-roosevelt/bible.md` | PASS | historical figure: no dossier |
| `characters/teddy-roosevelt/reference-sheet.jpg` | PASS |  |
| `characters/time/image-guide.md` | PASS |  |
| `characters/time/bible.md` | PASS |  |
| `characters/time/reference-sheet.jpg` | PASS |  |
| `pin: dannyboy2323/character-daddanny23` | PASS |  |
| `documented: dannyboy2323/character-daddanny23` | PASS |  |
| `pin: dannyboy2323/character-danielbull23` | PASS |  |
| `documented: dannyboy2323/character-danielbull23` | PASS |  |
| `pin: dannyboy2323/character-hater` | PASS |  |
| `documented: dannyboy2323/character-hater` | PASS |  |
| `pin: dannyboy2323/character-prosecutor` | PASS |  |
| `documented: dannyboy2323/character-prosecutor` | PASS |  |
| `pin: black-forest-labs/flux-2-pro` | PASS |  |
| `documented: black-forest-labs/flux-2-pro` | PASS |  |
| `pin: black-forest-labs/flux-2-max` | PASS |  |
| `documented: black-forest-labs/flux-2-max` | PASS |  |
| `pin: openai/gpt-image-2` | PASS |  |
| `documented: openai/gpt-image-2` | PASS |  |
| `story001 outline` | PASS |  |
| `story002 outline` | PASS |  |
| `story003 outline` | PASS |  |
| `story001 manuscript` | PASS |  |
| `story002 manuscript` | PASS | MISSING — not in the Claude Project; supply or extract from the published site |
| `no secrets committed` | PASS |  |

## What is covered (100% of the following)
- **Canon**: series bible, character bible (v1.3 with Jenni v2.0), world guide, style/voice guide, timeline & continuity bible, theme/symbol guide, project instructions → `canon/`.
- **Asset libraries**: adventures, intros (827), phrases (1,329), prison sayings, story lessons (100), dad jokes → `assets/` (+ builder/patch scripts in `tools/assets/`).
- **Characters**: 14 folders in `characters/` — bible (extracted from canon; Jenni's hand-written v2.0), image guide (route, trigger, pinned model, prompt block, refs, drift, rules, sample prompt), reference-sheet contact sheet.
- **Image system**: pipeline, prompt library, visual bible, corrections, model docs for all 7 Replicate models, pinned versions, machine-readable prompt registry (36 runs), runner + QA tooling + 39 tests + CI.
- **References**: published-panel sheets, 130 published webp files, training-set sheets, approved Jenni (8) and Johnny Cash (2) renders, candidate renders for Jen/Grandpa/Old-Timer.
- **Stories**: outlines for Stories 1–3; manuscripts for Stories 1 and 2 (Story 2 extracted from the live site's Sanity document); `data/panel-manifest.json` for the 130 published images.
- **Workflow**: `WORKFLOW.md` (concept → Sanity draft → publish → close-out).

## Known gaps — need the author (details in the chat report)
1. **Sanity write access** (Studio URL + a signed-in browser session, or an Editor API token). Nothing in this repo can create the draft until this exists.
2. **Postcards** are photo composites of real photos of Danny & Daniel — no source photos/process in the repo.
3. **Approved references** for Jen, Grandpa, Old-Timer are *candidates* (pending approval); Teddy Roosevelt's Replicate model name is unrecorded.
4. **Story 1 cover prompt** was never recorded; the cover template is reverse-engineered from Story 2.
5. **Cover typography** (font/size/placement) is approximated in `tools/cover_style.json`.
6. **Jenni canon reconciliations** flagged `[AUTHOR TO CONFIRM]` in `characters/jenni/bible.md` §16.
7. **Claude Project instructions field** cannot be edited by tooling — paste `canon/project-instructions.md` into it.
