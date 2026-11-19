# AWTB — End-to-End Story Workflow (concept → published draft)

_Version 1.0 — 2026-11-18. This is the operating manual for generating one complete Adventures with the Bull story per week with no manual steps by the author. Everything an agent needs is in this repository; paths are relative to the repo root._

**Cadence:** one story per week. Target: the agent produces a **100% complete Sanity DRAFT** (text, all images, metadata) and stops. **The author approves and publishes** (publishing is the only human gate).

## 0. Inputs the agent must load first
| Need | Where |
|---|---|
| Authority docs | `canon/series-bible.md`, `canon/character-bible.md` (+ `characters/<name>/bible.md`), `canon/world-guide.md`, `canon/style-voice-guide.md`, `canon/timeline-continuity-bible.md`, `canon/theme-symbol-guide.md`, `canon/project-instructions.md` |
| Asset libraries (each used once) | `assets/adventures.md`, `intros.yaml`, `phrases.yaml`, `prison_sayings.yaml`, `story_lessons.yaml`, `dad-jokes.yaml` |
| Prior stories | `stories/storyNNN/storyNNN-outline.md` and `…-manuscript.md` for every earlier story (continuity!) |
| Image system | `docs/image-generation-pipeline.md`, `docs/image-prompt-library.md`, `docs/visual-bible.md`, `characters/*/image-guide.md`, `references/`, `prompts/registry.json`, `tools/replicate_versions.json` |
| Secrets (never committed) | `REPLICATE_API_TOKEN` (env); Sanity write access (see §7) |

## 1. Pipeline overview
```
 1 Select assets ─► 2 Outline ─► 3 Manuscript ─► 4 QA gate (13+1 elements) ─► 5 Panel plan
        ─► 6 Covers (1:1, 9:16) + postcard ─► 7 Inline panels ─► 8 Image QA ─► 9 Alt text + metadata
        ─► 10 Sanity DRAFT (browser or API) ─► 11 Author approval ─► 12 Publish ─► 13 Close-out (mark assets consumed, commit)
```

## 2. Step-by-step

### 1 · Select assets (state choices; the author may redirect)
- Story number N = last published + 1. Pick the next adventure in `assets/adventures.md` (non-consumed), the dedication (`intros.yaml`), prison saying, lesson #N (`story_lessons.yaml`), dad joke #N (`dad-jokes.yaml`, from Story 3 on), and journal phrases.
- Confirm nothing is reused (grep prior manuscripts). Record the choices at the top of `stories/storyNNN/storyNNN-outline.md`.

### 2 · Outline → `stories/storyNNN/storyNNN-outline.md`
Beat-by-beat plan covering all **Thirteen Required Elements + Dad Joke (14)** and the Old-Timer's nugget, Fun Police subplot, flashback (hold the "held" reveals per the timeline), and the Danny/Daniel emotional spine. Follow the format of `stories/story003/story003-outline.md`.

### 3 · Manuscript → `stories/storyNNN/storyNNN-manuscript.md`
Write the full story in Danny's first-person voice (see `canon/style-voice-guide.md`). Target 7,500–9,000 words (S1 7,834; S2 8,443). Build in stages (outline → sections → polish).

### 4 · QA gate (blocking)
Run the checklist in `canon/project-instructions.md` ("Quality Self-Assessment") and the continuity checklist in `canon/timeline-continuity-bible.md`. Every box must be yes; if not, revise.

### 5 · Panel plan → `stories/storyNNN/storyNNN-panels.json`
~1 panel per ~100 words (S1 74, S2 56 panels). For each panel: id, anchor paragraph, characters present, route, prompt (assembled per `docs/image-prompt-library.md` §1), aspect ratio (1:1), alignment (strictly alternating `right`/`left`). Respect the rules: Fun Police never share a render with Danny/Daniel; fart register new each story; Daniel always fully clothed.

### 6 · Covers & postcard
- `coverImage` 1:1 (1024) and `coverImagePortrait` 9:16 (1152×2048): generated with the cover template (`prompts/…`, `docs/history/prompts-cover.md`, `tools/cover_style.json`); title text overlaid by `tools/generate_story_images.py --title-mode overlay`.
- `postcard`: photo composite (real photos of Danny & Daniel over comic art) — **currently author-supplied** (see AUDIT.md "Missing").

### 7 · Inline panels
`python3 tools/generate_story_images.py stories/storyNNN/storyNNN-panels.json --out stories/storyNNN/images` (dry-run first with `--dry-run`). Routes: Danny/Daniel/Hater/Prosecutor LoRAs; Jenni/Jen/Grandpa/Old-Timer via flux-2-max/pro with references from `references/approved/`; Johnny Cash via gpt-image-2. Pinned versions in `tools/replicate_versions.json`. Never set `disable_safety_checker`. Retries/429 handled by the runner.

### 8 · Image QA
`image_qa` (size/aspect/duplicate detection) + visual check against `references/characters/*` and `characters/*/image-guide.md` drift notes (Danny beard colour, Hater anti-Hellboy, Cash hologram). Regenerate failures with a new seed; keep prompts/seeds in the manifest.

### 9 · Alt text + metadata
Write a real descriptive `alt` for every panel (S2's "panel image" is a defect). Slug = kebab-case of title; `publishedAt` = intended Saturday.

### 10 · Sanity DRAFT (see §7 for access)
Create a **draft** `story` document (id `drafts.<uuid>`): title, slug, publishedAt, `coverImage`, `coverImagePortrait`, `postcard`, and `body` Portable Text interleaving `block` paragraphs with `panelImage {alignment, alt, image}`. Upload each image to Sanity assets first. Do **not** publish.

### 11 · Author approval → 12 · Publish
Author reviews the draft in Studio and publishes. (Agent may publish only if explicitly told.)

### 13 · Close-out
Mark consumed assets in the asset files; commit `stories/storyNNN/` + images + manifest + `prompts/registry.json` entries (set `status: proven` for shipped prompts); update `canon/timeline-continuity-bible.md` trackers; sync the Claude Project docs; `git push`.

## 3. Folder layout for each story
```
stories/storyNNN/
  storyNNN-outline.md
  storyNNN-manuscript.md
  storyNNN-panels.json        # manifest (ImageSpec list)
  images/                     # final webp: cover, cover-portrait, postcard, panels
```

## 4. Quality gates (summary)
Thirteen elements + dad joke · no asset reuse · continuity with prior manuscripts · image QA · alt text complete · Sanity draft complete · tests green (`python3 -m pytest tools/tests -q`).

## 5. Sanity schema notes (from the live site)
Project `d205mlci`, dataset `production`. Public read: `https://d205mlci.apicdn.sanity.io/v2021-06-07/data/query/production?query=…`. `story` fields: `title`, `slug`, `publishedAt`, `coverImage`, `coverImagePortrait`, `postcard`, `body[]` (`block` | `panelImage`). Published panels are 1:1 webp ~1008–1024 px; `alignment` alternates. Studio lives on the site's Studio URL (confirm — see AUDIT.md).

## 6. Weekly operating loop
Mon: assets + outline · Tue–Wed: manuscript + QA · Thu: panels/covers · Fri: Sanity draft + notify author · Sat: author publishes.

## 7. Accessing Sanity Studio (draft creation)
Preferred: Chrome extension session on the author's signed-in browser (Studio login), automating the Studio UI. Alternative (more reliable): a Sanity **API write token** (Editor role) stored as an environment secret → create the draft via the Mutations API (`createOrReplace` with a `drafts.` id) and upload images with the Assets API. See AUDIT.md for the exact open items.
