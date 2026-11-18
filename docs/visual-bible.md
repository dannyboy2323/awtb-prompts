# ADVENTURES WITH THE BULL — Visual Bible (Stories 1–2)

_Built Nov 18 2026 from the 130 published images on adventureswiththebull.com (74 + 56 inline panels, 2 covers + 2 portrait covers, 2 postcards). Every tag was assigned by visually reviewing each image against its surrounding manuscript text. Companion files: `data/panel-manifest.json` (machine-readable), `pipeline-corrections.md`, and the sheets in `references/`._

> **Use order for any image prompt:** `image-prompt-library.md` blocks → this file's *canonical descriptors* → the sheet in `references/` as the visual ground truth. When the three disagree, the **published panels win** (they are what readers have already accepted as canon).

---

## 1. Published image system (what the site actually does)

| Item | Published reality |
|---|---|
| Inline panel size | **1:1**, 1024×1024 or 1008×1008 `webp` |
| Panel density | **~1 panel per ~100 words** (S1: 74 panels / 7,834 words; S2: 56 / 8,443). Median words between panels: 92 (S1), 77 (S2) |
| Panel placement in Sanity | Portable Text `panelImage` block `{alignment: "left"\|"right", alt, image}`; **alignment strictly alternates** right/left (S1 starts `right`, S2 starts `left`) |
| Covers | `coverImage` = **1:1 1024px** (alt says "Landscape" but it is square); `coverImagePortrait` = **9:16, 1152×2048** |
| Postcard | `postcard` = PNG 3840×2880 / 4480×2998 — a **photo composite** (real photos of Danny & Daniel over comic art), not LoRA output |
| Alt text | S1 descriptive ("danny eating"); S2 generic ("panel image") — automation must write real alt text |
| Render modes | ~95% full-bleed inked scenes; rest isolated-on-white splatter/torn-edge vignettes (donut/action beats) |

## 2. Style DNA (verified against all panels)
Mike-Mignola-inflected inked comic art: heavy black ink, flat cel color, deep blacks, amber/ochre/burnt-red palette, halftone grain, hard geometric shadows, cinematic framing. Recurring rendering devices: warm single-source lamp light (interiors), orange-gold dusk/“gold hour” skies (exteriors), torn/deckled or splatter edges for emphasis panels. Reference: `references/style/`.

**Drift to guard against:** painterly/realistic skin (S2-p48 suit panel, S2-p29 street) and a more "digital poster" look in a few S2 panels (S2-p44–47 model-sheet style with bold outlines/flat backgrounds). Those are *character model-sheet* panels — fine for the villains, but do not let them set the scene style.

## 3. Canonical characters (see `references/characters/`)

| Character | Canonical look (from published panels) | Hero panels | Trigger | Known gaps |
|---|---|---|---|---|
| **Danny** | Bald; very long chest-length beard; neck/forearm/torso ornamental tattoos; big athletic build; plain dark tee + jeans | S1-p05/10/14/50/71/74, S2-p01/04/14 | `CHARACTERDADDANNY23` | **Beard tone drifts** dark brown ↔ auburn ↔ sun-bleached blond-brown across panels; the prompt library fixes it at "dark chocolate brown". Decide the canon (recommend: dark brown with auburn highlights in warm light). |
| **Daniel** | Tall lean 11-yr-old; messy brown hair; gray/olive hoodie; brown-belt gi; always fully clothed | S1-p20/24/26/36/59/72, S2-p05/07/23/30/54 | `CHARACTERDANIELBULL23` | S1-p09 and S2-p55 show Daniel much younger (flashbacks) — mark as such |
| **Grandpa** | Older, lean; swept-back brown-gray hair; short graying beard; wire-rim glasses; dark work jacket; drives a truck | S1-p15 | none | **Only 1 panel.** Need 3–4 approved renders. The pipeline library's "flannel/mug" block does *not* match S1-p15 — reconcile. |
| **Jen** | Early 40s; long straight black hair; fitted dark top/leggings | S2-p10 | none | **Only 1 panel.** Library block says "dark hair pulled back"; the panel shows hair worn loose. |
| **Johnny Cash** | Black frock coat/shirt; dark pompadour; luminous halo or cyan edge-glow hologram | S1-p37, S2-p32, S2-p34 | none (use flux-2-pro refs) | Two looks: glowing outline hologram (S1) vs. solid radiant (S2). Keep edge-glow as the "hologram" signifier. |
| **Old-Timer** | Ancient; **milk-white eyes**; white/gray beard; era costume | S1-p64, S2-p43 | none | S2-p42 (dominoes) is a candidate appearance without white eyes — confirm against manuscript |
| **Teddy Roosevelt** | Pince-nez, big mustache, Rough Rider hat, neckerchief, bandolier | S1-p44/61 | none | historical figure |
| **Biggie Smalls** | Coogi sweaters, gold chain, mic | S2-p40/51 | none | historical figure |
| **The Prosecutor** | Tall, thin, pointy face, slicked hair, pinstripe, red tie | S2-p44/45 | `CHARACTERPROSECUTOR` ⚠ | S1-p48 reads more "noir fedora/badge" than model sheet |
| **The Hater** | Short, portly, jowly, lazy eye, acne, navy Fun Police/FBOP uniform | S2-p46/47 | `CHARACTERHATER` | S1-p49 wears a campaign hat; S2 shows lank hair, no hat |

**Off-model panels (do not use as likeness refs):** S1-p40 (Danny's beard reads grey), S1-p09 & S2-p55 (young Daniel flashbacks), S2-p03 (overalls), S2-p29 (Champion sweatshirt — story-justified), S2-p48 (executive suit flashback). Danny's *standing rule* is jeans + t-shirt; period costume goes over the tee.

## 4. Recurring places, objects and effects (see `references/places-objects/`)
Grandpa's house (interior/exterior), Space-Time Continuum / the Crack, the Sacred Eternal Flame, the fart/shockwave registers, Entenmann's donuts, Danny's journals, the DONUT EXPERIMENTS notebook, the plant, vehicles, prison, Cuba 1898, Brooklyn 1992.

Continuity flags found:
- **Jen's car changes**: army-green Jeep Wrangler (S1) → blue Audi A7 (S2). Library/Story-3 outline assumes the green Jeep. Decide whether this is canon (new car) or a visual slip.
- **Space-time crack has two registers**: fiery canyon fissure (S1) vs. lightning rift ringed by flame-keepers (S2). The cosmic Sacred Flame ring of hooded keepers + standing stones (S1-p66) is consistent across both.
- **Fart register must be new each story** (S1 mushroom cloud; S2 bass-wave rings).

## 5. Covers & postcards (see `references/covers`, `references/postcards`)
Retro comic-book trade dress: heavy ochre "ADVENTURES WITH THE BULL" masthead; issue box top-left (S1 `#01` with crossed-sabers insignia; S2 bull-logo "BULL COMICS GROUP / STORY #2 / APR 2024 / 50¢"); subtitle strip ("A graphic novel of courage, duty and glory" / "Brooklyn's Finest"); pull-quote/tagline bottom; S1 portrait cover has credits + barcode. Covers feature the historical star large, Danny and Daniel foreground. Postcards: period headline ("Hola! from Cuba", "We're in Brooklyn!"), stamp, postmark, hand-lettered caption strips, photo-composite portraits.

## 6. Recommended additional work (prioritized)
1. **Generate approved reference sets** for Grandpa, Jen, Jenni, Johnny Cash and the Old-Timer (3–4 white-background renders each) — the pipeline's `references/` requirement; only 1–5 published panels exist for each.
2. **Decide canon**: Danny's beard tone; Jen's car; the Hater's hat; Prosecutor look (noir vs. model-sheet).
3. **Lock panel density** (~1 per 100 words, alternating alignment, 1:1) — the old plan of "2 per page / 14 panels" would under-deliver ~5×.
4. **Write real alt text** per panel (S2's are all "panel image").
5. **Train additional LoRAs** once ≥25 panels exist (Danny and Daniel already trained; Grandpa/Jen won't reach that soon — use flux-2-pro refs).
6. **Postcard compositing step**: automate (photo cutouts + comic background + stamp/postmark overlay) — currently manual.
7. **Cover templater**: the trade dress is consistent enough to build a Pillow/HTML template (masthead, issue box, price stamp, tagline, barcode) for both 1:1 and 9:16.
8. **Sanity write access** for the publish step: draft creation needs an API write token or Studio browser automation; the public CDN is read-only.
