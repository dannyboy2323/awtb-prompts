# ADVENTURES WITH THE BULL

## Image Generation Pipeline — Covers and Inline Panels, Fully Automated

### Version 1.0 — Nov 2026

---

> _Every story is now three deliverables, produced in order, by the agent, without the author touching Replicate: (1) `storyNNN-outline.md`, (2) `storyNNN-manuscript.md`, (3) the image set — a 16:9 cover, a 1:1 cover, and two inline panels per manuscript page. This document is the operating procedure. `image-prompt-library.md` holds the words. `tools/generate_story_images.py` does the API work._

---

## 1. WHEN THIS RUNS

The pipeline is **Step 3 of every story**. It does not start until the manuscript is approved (or, in unattended mode, until the manuscript's self-assessment checklist passes). Order of operations for a story:

1. **Outline** — `storyNNN-outline.md` written, author flags resolved.
2. **Manuscript** — `storyNNN-manuscript.md` written and self-assessed.
3. **Panel plan** — the agent reads the manuscript, paginates it, and writes `storyNNN-panels.json` (the manifest — §3).
4. **Cover art** — 16:9 first, then 1:1 (§4).
5. **Inline panels** — 2 per page, in page order (§5).
6. **QA pass** — automated checks, then a visual review by a *separate* agent that has not seen the prompts (§6).
7. **Delivery** — files named and placed per §8; manifest updated with final URLs/paths; continuity bible image log updated.

---

## 2. PAGINATION — WHAT "2 PER PAGE" MEANS

Published Stories 1 and 2 are the layout reference. Until the author supplies the exact word-count-per-page used on adventureswiththebull.com (see §9, item 1), the pipeline uses this default:

- **One page = ~550 words of manuscript body** (dedication and title excluded).
- A 2–3 page story (per `series-bible.md`) therefore yields **4–6 inline panels**; the Story 3 outline anticipates ~7 pages / 14 panels because the Scotland story is long — if the manuscript runs long, the panel count scales with it. Never fewer than 2 panels per page; never more.
- Panel A sits after the page's first major beat; Panel B after its last. The agent picks the two most *visual* beats on the page — not the two most important ones. A journal paragraph is important; a boy turning a bull is visual.
- **Fixed panels every story** (always generated, always in these positions):
  - Page 1, Panel A or B: **the donut incident**
  - Page 1 or 2: **the fart** (the register must match the manuscript's metaphor)
  - Landing page: **the landing** (both characters in period dress)
  - Mid-story: **Johnny Cash**; **the Old-Timer**; **the Fun Police disaster**
  - Climax page: **Daniel saves the day** (the hero panel — 2 outputs, best chosen)
  - Last page, Panel B: **Danny at the journal** (the "last panel" template)

---

## 3. THE MANIFEST — `storyNNN-panels.json`

The agent writes the manifest from the manuscript before any API call. The script reads only the manifest; it never reads the manuscript. This keeps the creative decision (what to draw) in the agent and the mechanical work (how to render it) in code.

```json
{
  "story": 3,
  "slug": "i-saved-the-king",
  "title": "I Saved the King",
  "images": [
    {
      "id": "cover-16x9",
      "kind": "cover",
      "aspect_ratio": "16:9",
      "route": "daniel",
      "lora_scale": 1.1,
      "num_outputs": 2,
      "prompt": "<STYLE BLOCK>, <DANIEL BLOCK>, <SINGLE-FIGURE GUARD>, <SCENE>, upper third kept clear for title",
      "title_overlay": { "text": "ADVENTURES WITH THE BULL", "subtitle": "Story 3 · I Saved the King" }
    },
    { "id": "cover-1x1", "kind": "cover", "aspect_ratio": "1:1", "route": "daniel", "lora_scale": 1.1, "num_outputs": 2, "prompt": "...", "title_overlay": { "text": "ADVENTURES WITH THE BULL", "subtitle": "Story 3 · I Saved the King" } },
    { "id": "p01-a", "kind": "panel", "page": 1, "slot": "A", "aspect_ratio": "1:1", "route": "danny", "prompt": "..." },
    { "id": "p01-b", "kind": "panel", "page": 1, "slot": "B", "aspect_ratio": "1:1", "route": "daniel", "prompt": "..." },
    { "id": "p02-b", "kind": "panel", "page": 2, "slot": "B", "aspect_ratio": "1:1", "route": "danny+daniel", "prompt": "..." },
    { "id": "p03-a", "kind": "panel", "page": 3, "slot": "A", "aspect_ratio": "1:1", "route": "flux2pro", "reference_images": ["refs/johnny-cash-01.webp", "refs/johnny-cash-02.webp"], "prompt": "..." },
    { "id": "p05-a", "kind": "panel", "page": 5, "slot": "A", "aspect_ratio": "1:1", "route": "hater+prosecutor", "prompt": "..." }
  ]
}
```

**`route` values and what they resolve to** (the script owns this table — `ROUTES` in `generate_story_images.py`):

| route               | model                                           | extra_lora                               | triggers required in prompt                 |
| ------------------- | ----------------------------------------------- | ---------------------------------------- | ------------------------------------------- |
| `danny`             | `dannyboy2323/character-daddanny23`             | —                                        | `CHARACTERDADDANNY23`                       |
| `daniel`            | `dannyboy2323/character-danielbull23`           | —                                        | `CHARACTERDANIELBULL23`                     |
| `danny+daniel`      | `dannyboy2323/character-daddanny23`             | `dannyboy2323/character-danielbull23`    | both                                        |
| `hater`             | `dannyboy2323/character-hater`                  | —                                        | `CHARACTERHATER` (+ anti-Hellboy block)     |
| `prosecutor`        | `dannyboy2323/character-prosecutor`             | —                                        | `CHARACTERPROSECUTOR` ⚠ confirm spelling     |
| `hater+prosecutor`  | `dannyboy2323/character-hater`                  | `dannyboy2323/character-prosecutor`      | both                                        |
| `flux2pro`          | `black-forest-labs/flux-2-pro`                  | n/a (uses `input_images` refs)           | none — plain description, positive phrasing |
| `gptimage2`         | `openai/gpt-image-2`                            | n/a                                      | none — used only for text-heavy composites  |

The script **refuses to submit** a prompt whose route requires a trigger token that is missing from the prompt — this is the single most common consistency failure and it is now impossible.

---

## 4. COVER WORKFLOW

Covers are two-pass because the LoRA models render the characters but cannot render clean title text, and the text-capable models cannot render the characters.

**Pass 1 — art.** Route by who is on the cover (usually `daniel` or `danny+daniel`). `num_outputs: 2`, `lora_scale: 1.1`. Prompt ends with `upper third of the frame kept clear and dark for title text`. Generate **16:9 first**, pick the best, then generate **1:1 as its own render** with the scene recomposed for square — do not crop the 16:9; the composition changes.

**Pass 2 — title.** Default: **Pillow overlay** in the script (`--title-mode pillow`). Deterministic, free, identical typography every story. The script draws `ADVENTURES WITH THE BULL` in the series display font across the top third with a Mignola-style heavy black drop and an ochre fill, plus the story number/title as a smaller line. Font file, color hex codes, and placement margins are read from `cover_style.json` (see §9 — author must supply the font or approve the default).

Alternative (`--title-mode flux2pro`): send the chosen art as `input_images[0]` to flux-2-pro with the instruction `add the title text "ADVENTURES WITH THE BULL" in big bold heavy inked comic lettering across the upper third, matching the ink style, change nothing else`. Use when a hand-lettered look is wanted; costs one more prediction and can perturb the art.

The Story 2 cover prompt (library §7.1) is the compositional reference: the star front-and-center, Danny and Daniel in the frame, the title "big, bold, prevalent."

---

## 5. INLINE PANEL WORKFLOW

For each manifest entry in page order:

1. Assemble the prompt exactly as in the manifest (the agent already built it from `image-prompt-library.md` blocks — the script only validates it).
2. Submit with the route's model and the default inputs (library §6). `num_outputs: 1` for ordinary panels, `2` for hero panels and anything face-critical.
3. Download every output to `work/storyNNN/raw/<id>-<n>.webp`.
4. Run the automated QA (§6.1). If it fails, resubmit once with a new seed and the anatomy guard doubled; if it fails again, mark the panel `needs_review` in the manifest and move on. Never block the batch on one panel.
5. Record the prediction URL, seed, and chosen output in the manifest.

**Multi-character rules:**
- Danny + Daniel → `danny+daniel` route (Danny primary, Daniel as `extra_lora`). Both triggers. Keep them spatially separated in the prompt.
- Either of them + the Fun Police → never in one render. The Fun Police are invisible to Danny and Daniel; they also do not share a panel with them. (This is canon doing the compositing for us.)
- Danny/Daniel + an untrained character (Cash, Old-Timer, Jenni, a historical star) → render with the LoRA route and describe the other figure in plain words. If the untrained character must carry the panel (e.g. Cash alone on the oak), use `flux2pro` with that character's approved reference images.
- Three or more principal figures → split into two panels or render the scene on `flux2pro` with reference images for everyone (Danny's and Daniel's approved LoRA renders double as their flux-2-pro references).

**Daniel — content safety rule.** Daniel is an eleven-year-old. He is always fully clothed, never rendered in distress beyond the story's comic-adventure register, never in a composition that could read as sexualized or as real-world endangerment. Prompts that stress "the face and likeness of CHARACTERDANIELBULL23" are for consistency; `disable_safety_checker` is **never** set. If the safety checker blocks a legitimate panel, change the composition (rear view, wider shot, silhouette) — do not change the checker.

---

## 6. QA

### 6.1 Automated (in the script)
- File exists, non-zero, decodes as an image.
- Aspect ratio matches the request within 2%.
- Near-duplicate check against this story's other panels (perceptual hash) — flags a model that ignored the scene and returned a character study.
- Trigger-token presence (pre-flight, §3).
- Style-block presence — the first 40 characters of the prompt must equal the start of the standard style block (library §2) or its two approved variants.

### 6.2 Visual review (separate agent, has not seen the prompts)
The reviewing agent gets the manuscript page and the two panels, and answers:
1. Is this recognizably Danny / Daniel / the Hater / the Prosecutor (per `character-bible.md`)? Beard color correct? Daniel's hair brown and messy?
2. Is Danny in a t-shirt (or period garment visibly over one)?
3. Does the panel depict a beat that is actually on this page?
4. Anatomy: two arms, two legs, hands plausible, no merged figures?
5. Any text, watermark, signature, or speech bubble? (Fail.)
6. Any Hellboy drift on the Hater? (Fail.)
7. Does the fart panel's register match the manuscript's metaphor (not a prior story's)?
Panels that fail are regenerated with the reviewer's note appended to the scene text.

---

## 7. REFERENCE IMAGES FOR UNTRAINED CHARACTERS

Kept in `refs/` in the AWTB repo and listed in `refs/manifest.json`. Each untrained recurring character needs **3–4 approved renders** on white background in the standard style (Johnny Cash hologram; the Old-Timer — face only, since his costume changes every story; Jen; Jenni; Grandpa). Generate them once with `flux2pro`, have the author approve, and pin them. Every later `flux2pro` panel for that character passes them as `input_images`. When a character has appeared in ≥25 panels, train a LoRA (`ostris/flux-dev-lora-trainer` on Replicate, trigger `CHARACTER<NAME>`) and add a route.

---

## 8. NAMING, STORAGE, DELIVERY

```
stories/
  story003/
    story003-outline.md
    story003-manuscript.md
    story003-panels.json          # manifest with prompts, seeds, prediction URLs, chosen outputs
    images/
      story003-cover-16x9.webp
      story003-cover-1x1.webp
      story003-p01-a.webp
      story003-p01-b.webp
      ...
    raw/                           # every generated candidate, never served
```

- Format `webp`, quality 80 (matches the LoRA defaults and the published site). Author to confirm the site's expected format/dimensions (§9).
- The manifest is the audit trail: every served image has its prompt, model version, seed, and prediction URL recorded.
- After generation, the agent inserts image references into the manuscript at the panel positions using the site's existing convention (§9, item 3) and pushes the story folder to `dannyboy2323/awtb` on a branch `story/003-i-saved-the-king` with a PR.

---

## 9. WHAT THE AUTHOR STILL NEEDS TO ADD TO THE PROJECT CONTEXT

The pipeline is fully specified except for the items below, which exist only on the author's side. **Each one is a blocker for full automation of Story 3's images:**

1. **The published Story 1 and Story 2 image sets** — the actual cover files (16:9 and 1:1) and every inline panel, with a note of which manuscript paragraph each panel sits after. This locks the real words-per-page, the panel aspect ratio (1:1 assumed), the typography, and the placement rhythm. Upload as a zip, or give read access to the site's image directory/CDN.
2. **The prompts used for the Story 1 and Story 2 inline panels.** Only the Story 2 *cover* prompt is in the project. The `docs-*.md` examples are close but are character tests, not the shipped panels.
3. **How the web app references panels** — markdown `![]()` tags in the manuscript, a JSON manifest, MDX components, or database rows? Paste one published story's source as it lives in the repo.
4. **Cover typography** — the font file (or name) used on the Story 1–2 titles, fill/stroke colors, and whether the story number/title appears on the cover. If a layered source (PSD/Figma/Canva) exists, attach it. Otherwise approve the Pillow default described in §4.
5. **Prosecutor model trigger** — `CHARACTERPROSECUTOR` vs. `#CHARACTERPROSECUTOR`, and a `lora_scale` that has produced a good result. The one logged example used a hash and a GTA-style prompt; the series style has never been tested on this model.
6. **Approved reference renders** for Johnny Cash, the Old-Timer, Jen, and Grandpa (3–4 each, white background), or permission for the agent to generate candidates and have the author pick. Jenni is new — the agent will generate candidates from the character-bible description.
7. **Replicate model version hashes** for all four LoRA models (Replicate → model page → Versions), so renders are pinned and reproducible across months.
8. **Repo details** — confirm `dannyboy2323/awtb` is the target, the default branch, the path where story assets live, and whether the agent should open a PR or push to main.
9. **Replicate account guardrails** — confirm billing is active and set a per-story spend ceiling (the script enforces `--max-predictions`, default 40).
10. **Site format** — confirm `webp` and the exact pixel dimensions the reader app expects for covers and panels (the LoRA models output ~1MP; if the site wants 2048px covers, the pipeline adds an upscale step via `philz1337x/clarity-upscaler` or `nightmareai/real-esrgan`).

Items 1–3 are the big ones. With those, the agent can match the published look exactly rather than approximating it.

---

## 10. SECRETS

`replicate-key.txt` is in the project context. The script reads the key from the `REPLICATE_API_TOKEN` environment variable; the agent sets that variable from the project doc at runtime and never writes the key into any generated file, log, manifest, or commit. The key is never echoed in chat.
