# awtb-prompts — single source of truth for AWTB image generation

Everything needed to generate images of any kind for **Adventures with the Bull**: prompts, reference
images, model notes, generated outputs, and the tooling that automates it. Story writing lives in the
Claude Project ("AWTB Story Generator"); this repo owns the **visuals**. When a doc here and a project
mirror disagree, **this repo wins**.

## Map

| Path | What lives there |
|---|---|
| `docs/image-generation-pipeline.md` | Operating procedure: manifest → covers → panels → QA → delivery |
| `docs/image-prompt-library.md` | Style block, character blocks, anatomy guards, proven prompt templates |
| `docs/visual-bible.md` | Canonical look of every character/place/object, derived from the 130 published images |
| `docs/pipeline-corrections.md` | Where earlier pipeline assumptions were wrong (panel density, cover ratios, alt text…) |
| `docs/replicate-models/` | Per-model Replicate docs + every logged run (inputs, outputs, prediction URLs) |
| `docs/history/` | Hand-written historical prompts (e.g. Story 2 cover) |
| `prompts/characters/` | Per-character prompt logs (older/newer LoRA versions) |
| `prompts/registry.json` | Machine-readable registry of every logged run; `status`: logged → proven / rejected |
| `references/characters, places-objects, covers, postcards, style` | Reference sheets built from published Stories 1–2 |
| `references/published/story00N/` | The actual published webp files (panels `sN-pNN`, covers, postcards) — visual ground truth |
| `references/training-sets/` | Contact sheets of the LoRA training images (Danny, Daniel, Hater, Prosecutor, Teddy) + album links |
| `references/approved/` | Approved reference renders for untrained characters (Cash, Old-Timer, Jen, Grandpa…) used as `input_images` |
| `data/panel-manifest.json` | All 130 published images: URLs, sizes, alignment, tags, pacing |
| `stories/storyNNN/` | Outline, manuscript, `storyNNN-panels.json`, final `images/` for each story |
| `generated/` | Scratch/experiments (raw candidates are git-ignored) |
| `tools/` | `generate_story_images.py` (Replicate runner), `build_prompt_registry.py`, `visual_bible/` (extraction + sheets), `tests/` |

## Conventions
- **Never commit secrets.** The Replicate token comes from `REPLICATE_API_TOKEN`; `.gitignore` blocks key files.
- Finalized panels: `stories/storyNNN/images/storyNNN-<id>.webp` + the manifest recording prompt, seed, model version and prediction URL.
- Promote a prompt to a template only after it ships: set its `status` to `proven` in `prompts/registry.json` and add it to the prompt library.
- Tests run in CI: `python -m pytest tools/tests -q`.

## Open items (tracked in `docs/pipeline-corrections.md`)
Prosecutor trigger spelling, Replicate version pins (`tools/replicate_versions.json`), canon calls (Danny beard tone, Jen's car, Hater hat, Prosecutor look), approved references for Grandpa / Jen / Johnny Cash / Old-Timer.

## Status (2026-11-18)
- Replicate versions pinned (`tools/replicate_versions.json`).
- Candidate reference renders for Old-Timer, Jen, Grandpa and Jenni are in `references/generated-refs/` (log in `log.json`). Approve by copying to `references/approved/<name>-NN.webp`.
- Johnny Cash: flux-2-pro flags the render (E005) even at `safety_tolerance` 4, but **gpt-image-2 works** (candidate in `references/generated-refs/johnny_cash/`; route Cash through `gptimage2`). The Daniel/Danny LoRA routes never relax the safety checker. A second candidate was throttled (HTTP 429) and can be re-run: `python3 tools/generate_reference_candidates.py --only johnny_cash --per 2`.
