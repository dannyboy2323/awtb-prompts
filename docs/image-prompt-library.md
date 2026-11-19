# ADVENTURES WITH THE BULL

## Image Prompt Library — Standard Style, Character Blocks, Proven Prompts

### Version 1.0 — Nov 2026 (consolidates `prompts-cover.md` and the example prompts in `docs-*.md`)

---

> _This is the single source of truth for how every image in the series is prompted. Every cover and every inline panel is assembled from the blocks below in a fixed order. Do not freelance the style block. Do not shorten the character blocks. Consistency across 1,500 stories depends on the same words being sent every time._

---

## 1. PROMPT ASSEMBLY ORDER

Every prompt is built by concatenating these blocks, in this order, comma-separated:

```
[STYLE BLOCK]  +  [CHARACTER BLOCK(s) with trigger token(s)]  +  [ANATOMY GUARD]  +  [SCENE]  +  [COMPOSITION / CAMERA]  +  [BACKGROUND RULE]
```

- **STYLE BLOCK** always first. The LoRA models were trained on it; it anchors the look.
- **CHARACTER BLOCK** immediately after style, with the trigger token first in the block. Repeat the trigger token up to three times for face-critical panels (proven to improve likeness — see `docs-danielbull23.md` examples).
- **ANATOMY GUARD** before the scene — it suppresses the Flux-dev failure modes (extra limbs, merged figures).
- **SCENE** is written from the manuscript, specific and sensory, 80–200 words.
- **COMPOSITION / CAMERA** last so it controls the frame.
- **BACKGROUND RULE**: `against a solid white background` for isolated character studies; omit for full scenes.

For **flux-2-pro / gpt-image-2** (non-LoRA models): drop the trigger tokens, drop the negative-phrased guards (those models misread negatives — describe what you want instead), keep the style block.

---

## 2. THE STANDARD STYLE BLOCK (verbatim — never alter)

```
2D graphic novel illustration, inked comic book art, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph
```

**Strengthened variant** (use when outputs drift toward painterly/realistic — proven in the Danny journal panel):

```
Mike Mignola art style, Hellboy comic art style, 2D graphic novel illustration, inked comic book art, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph, NOT realistic, NOT painted, styled exactly like a Mignola Hellboy comic panel
```

**Flux-2-pro / gpt-image-2 variant** (positive-only phrasing):

```
2D graphic novel illustration in the style of a Mike Mignola inked comic panel, bold heavy black ink linework, dramatic chiaroscuro, deep blacks with muted earth tones, desaturated ochres and burnt reds, warm amber accents, rough crosshatching and halftone grain, woodcut-like rendering, strong geometric shadow shapes, flat cel shading, colored ink on paper, hand-inked comic book art
```

---

## 3. CHARACTER BLOCKS

### 3.1 DANNY — model `dannyboy2323/character-daddanny23` — trigger `CHARACTERDADDANNY23`

```
CHARACTERDADDANNY23, completely bald shaved head, very long thick chest-length light brown beard, warm light brown beard color, NOT red, NOT orange, NOT grey, neck tattoos, athletic build, plain dark t-shirt and jeans, strong facial likeness preserved, character face accuracy critical, CHARACTERDADDANNY23 facial features dominant
```

Notes:
- `lora_scale` 1.0–1.1. Use 1.1 for face-critical panels.
- The t-shirt is canon (series rule: jeans and a t-shirt, always). When Danny is in period costume, write the costume **over** the t-shirt: `wearing a [period garment] over a plain dark t-shirt, jeans visible beneath`.
- Full-back tattoo coverage was proven in the shirtless rear-view example; use sparingly.
- **Canon (author, 2026-11-18): Danny's beard is LIGHT BROWN.** Tested: the model follows "light brown" but drifts orange/ginger and grows the beard past the chest unless "NOT red, NOT orange, NOT grey" and "chest-length" are present (see `references/generated-refs/danny-light-beard-test/`).

### 3.2 DANIEL — model `dannyboy2323/character-danielbull23` — trigger `CHARACTERDANIELBULL23`

```
CHARACTERDANIELBULL23, CHARACTERDANIELBULL23, CHARACTERDANIELBULL23, young boy, slim build, tall for his age, brown hair, messy brown hair, the face and likeness of CHARACTERDANIELBULL23 clearly preserved and fully dominant, young boy with specific brown hair and facial features of CHARACTERDANIELBULL23 fully intact and recognizable, the likeness and facial identity of CHARACTERDANIELBULL23 is the single most important element of this image above all else
```

Notes:
- `lora_scale` 1.0 default; 1.1 for hero panels; 1.5 was used once for the mushroom-cloud fart panel and held.
- Daniel is 11. **Never** render him in any context that could read as sexualized or endangered beyond the story's cartoon-adventure register. Keep him fully clothed, keep the pulp-horror styling on the environment rather than on him.
- Proven: "EXAGGERATED comic reaction pose" phrasing produces the Daniel comedy register well.
- Multi-character panels with Danny: use the Danny model as primary and pass `extra_lora: "dannyboy2323/character-danielbull23"`, `extra_lora_scale: 1.0`, with BOTH trigger tokens in the prompt.

### 3.3 THE HATER — model `dannyboy2323/character-hater` — trigger `CHARACTERHATER`

```
CHARACTERHATER, THE HATER, fully human, normal human anatomy throughout, normal human head, no horns no growths no supernatural features anywhere on the body, normal human pale peachy skin tone, short and extremely portly obese human male, broad flat nose, wide flaring nostrils, round fleshy face, both eyes fully visible with misaligned wandering gaze apparent, heavy jowls, thick fleshy neck with multiple chins, pronounced buck teeth, ruddy flushed uneven skin with acne, greasy lank hair plastered flat, wide squat body, short stubby arms and legs, slovenly disheveled posture, dark navy blue uniform shirt with FUN POLICE patch on left shoulder, official FBOP shield badge on chest, shirt untucked and straining across the belly, belt sitting low, dark navy uniform trousers hiked too high, uniform hat at the correct angle, scuffed dirty boots
```

**Dress rule (author):** in period stories the Hater wears the era's costume tied into the story's scheme; in the modern day he wears a baseball cap bearing the "FBOP" Fun Police logo.

**Mandatory Hater anti-drift block** (the Mignola style pulls this model toward Hellboy — always include):

```
NOT Hellboy, NOT Hellboy character, NO horns, NO stone fist, NO right hand of doom, NO red skin whatsoever, NO pink skin, NO supernatural features, NO demonic features, NO fictional character likeness, fully original human character
```

### 3.4 THE PROSECUTOR — model `dannyboy2323/character-prosecutor` — trigger `CHARACTERPROSECUTOR`

> **Trigger confirmed 2026-11-18:** `CHARACTERPROSECUTOR` (no hash). Tested with and without the hash at the same seed: both render the on-model Prosecutor in the series style (`references/generated-refs/prosecutor-trigger-test/`), so the plain spelling is canon for consistency with the other models. `lora_scale` 1.0 worked. **Dress rule (author):** in period stories he wears the era's costume integrated into that story's hairbrained scheme; in the modern day he has slicked-back hair.

```
CHARACTERPROSECUTOR, THE PROSECUTOR, tall thin man age 52, long pointy face, aggressively slicked-back dark hair, pinstripe suit one size too small across the shoulders, knockoff gold watch worn on the wrong wrist, cheap very shiny polished shoes, smug self-satisfied courtroom posture, one hand raised mid-objection, hollow vain expression
```

### 3.5 CHARACTERS WITHOUT A TRAINED MODEL (route to `black-forest-labs/flux-2-pro` with reference images, or gpt-image-2)

**Johnny Cash (the Guide)** — _route `gptimage2` (flux-2-pro safety-flags this likeness; verified 2026-11-18)_:
```
Johnny Cash as a translucent luminous holographic apparition, rendered semi-transparent with soft amber-white edge glow, dressed entirely in black, black coat and black shirt, dark swept-back hair, deeply lined weathered face, calm dry half-smile, standing or seated at ease, the background partially visible THROUGH his body, visible only to the two figures looking at him
```
_Reference images: author to supply 3–4 approved renders (see Pipeline §7)._

**The Old-Timer:**
```
an ancient man of indeterminate age in period-appropriate clothing of [ERA], deeply weathered face, milk-white clouded eyes that nonetheless seem to see everything, long white beard, a slight knowing amused smile, unhurried posture, warm and unthreatening, slightly out of place in a way that is easy to dismiss
```
_The milk-white eyes are canon (Stories 2–3). Reference images: author to supply._

**Jen (the Mother):**
```
an elegant woman in her early forties, composed and warm, dark hair pulled back, clean strong facial structure, tired eyes that miss nothing, practical stylish clothing, standing beside [HER CAR FOR THIS STORY — rotates every story; so far an army-green Jeep Wrangler (S1) and a blue Audi A7 (S2); pick something different next time]
```

**Jenni (the Girlfriend — introduced Story 3)** — _APPROVED reference set exists: `references/approved/jenni/` (8 images). Route `flux2max` (black-forest-labs/flux-2-max) with 3–6 of those images as `input_images`. Full guide: `characters/jenni/image-guide.md`; bible: `characters/jenni/bible.md`._
```
the same woman as the reference images, 47-year-old pretty woman who reads younger, slender 5'5" 110 lbs, natural curly blond hair with a red flower tucked in, thin gold forehead band with a small turquoise stone, bright blue eyes, light freckles, big happy open smile, turquoise drop earrings, bohemian mandala and botanical tattoos on both arms, silver rings, faded vintage black Nirvana rock t-shirt, black leggings, barefoot (or checkered black-and-white vintage Vans), light happy hippy-bohemian-gypsy energy
```
_Prior (pre-reference) block, retired:_ chambray / one-forearm botanical tattoos — superseded by the author's approved renders (2026-11-18). Chambray remains a valid alternate outfit.

**Grandpa (Danny's father):**
```
a man in his seventies, lean, quiet, flannel shirt, reading glasses pushed up on his forehead, unbothered expression, holding a mug of tea
```
_Minimal canon exists for Grandpa; keep him peripheral in panels._

**Historical figures:** describe from the outline's caricature paragraph. Public figures from history are fine to depict; keep them in the Mignola register. Do not use photographs of real living people as reference inputs.

---

## 4. ANATOMY GUARD BLOCKS

**Single figure (LoRA models):**
```
single figure only in foreground, exactly two arms exactly two legs, correct human anatomy, no extra limbs, no floating limbs, no disembodied body parts, no anatomical errors, clean figure rendering
```

**Multi-figure (LoRA models):**
```
[N] figure composition, each figure spatially isolated with clear empty ground space between them, no overlapping limbs between any figures, exactly two arms and two legs per figure, correct human anatomy throughout, background figures kept small distant and minimally detailed as flat gestural silhouettes with no anatomical detail, foreground and background separated by a dramatic chiaroscuro shadow band, negative space used deliberately around each foreground figure to isolate and clarify its silhouette
```

**No-text / no-watermark (for panels; covers get text added separately):**
```
NO watermark, NO signature, NO text, NO logo, NO artist signature, NO speech bubbles, NO captions
```

**Flux-2-pro positive-only equivalent:**
```
clean uncluttered composition, each figure fully separated with clear space around it, natural proportions and complete anatomy, plain panel with no lettering or signatures
```

---

## 5. COMPOSITION / CAMERA VOCABULARY (pick one or two)

`CINEMATIC WIDE PANEL establishing shot` · `cinematic medium shot framing the full figure` · `cinematic medium close shot from the waist up` · `EXTREME CLOSE UP on the face` · `CINEMATIC LOW ANGLE shot looking up` · `CINEMATIC DUTCH ANGLE` · `rear view from behind` · `over-the-shoulder shot` · `single-source dramatic side lighting` · `harsh midday overhead sun casting hard geometric shadows` · `warm amber backlight from low sun` · `cool blue moonlight through a window` · `thick ink motion lines streaming backward` · `ink splash shapes for dust and debris`

---

## 6. ASPECT RATIOS

| Output                | Model input                                   | Notes                                                                       |
| --------------------- | --------------------------------------------- | --------------------------------------------------------------------------- |
| Cover, wide           | `aspect_ratio: "16:9"`                        | Generate first. Composition must leave the upper third clear for the title. |
| Cover, square         | `aspect_ratio: "1:1"`                         | Generate second as its own render (not a crop) — recompose for square.      |
| Inline panel          | `aspect_ratio: "1:1"`                         | Matches published Stories 1–2 panels. Author to confirm (see Pipeline §7).  |
| Character study / ref | `aspect_ratio: "1:1"`, white background       |                                                                             |

Default model inputs for the LoRA models (proven across all logged runs):

```json
{ "model": "dev", "go_fast": false, "num_inference_steps": 28, "guidance_scale": 3,
  "megapixels": "1", "output_format": "webp", "output_quality": 80,
  "prompt_strength": 0.8, "lora_scale": 1.0, "extra_lora_scale": 1.0, "num_outputs": 2 }
```

---

## 7. PROVEN PROMPTS (verbatim, from successful runs)

### 7.1 Story 2 cover (manual, author-written — the reference for all covers)

```
A graphic novel cover for Story #2 ("Big Poppa" is story name) of Adventures With The Bull. The graphic novel title "Adventures With The Bull" in big bold prevalent print. Style is graphic novel illustration, inked comic book art, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph. The scene on the cover features the rapper The Notorious BIG with a microphone in his hand rapping on the streets of Brooklyn to a large crowd. Front and center in the audience is a 45 year old man (caucasian, long brown beard to his chest, bald shaved head, blue vintage Champion sweatshirt, large hip-hop style gold chain, athletic build) and his son an 11 year old boy (caucasian, messy brown hair, tall and lean, wearing a black Raiders vintage Starter jacket, large hip-hop gold chain, black baseball cap)
```

_Lesson from this prompt: covers describe Danny and Daniel by plain description (not trigger tokens) because the cover was generated on a text-capable model. The pipeline now generates the cover ART with the LoRA models (for likeness) and adds the TITLE in a second pass — see Pipeline §4._

### 7.2 Danny — journal panel (the "last panel" template; reuse every story)

```
[STRENGTHENED STYLE BLOCK], CHARACTERDADDANNY23, completely bald shaved head, very long thick chest-length light brown beard, warm light brown beard color, NOT red, NOT orange, NOT grey, neck tattoos, strong facial likeness preserved, character face accuracy critical, CHARACTERDADDANNY23 facial features dominant, single figure only, exactly two arms exactly two legs, correct human anatomy, no extra limbs, no floating limbs, no disembodied body parts, no anatomical errors, clean figure rendering, figure seated alone at a heavy worn wooden desk deep in the night, hunched slightly forward over an open leather bound travel journal, right hand writing slowly with a pen across the open pages, left hand wrapped around a cracked coffee mug, expression of deep exhausted contemplative brooding, back in present day clothing, plain dark t-shirt, neck tattoos fully visible above the collar, the bald head catching the warm amber glow of a single desk lamp, the long dark beard resting against his chest as he leans forward, [THIS STORY'S SOUVENIR OR COSTUME PIECE] beside the journal, a single desk lamp as the only light source casting a tight warm amber pool across the desk and his face, everything beyond the lamp radius dissolving into pure Mignola black, dramatic single source chiaroscuro lighting, the open journal pages catching warm light, handwritten text rendered as loose illegible scrawl, a window behind him showing the deep blue black of late night, cinematic medium close shot framing the figure from the waist up at the desk, quiet brooding introspection, the last panel of the graphic novel
```

### 7.3 Daniel — donut incident template

```
[STYLE BLOCK], CHARACTERDANIELBULL23, young boy, slim build, brown hair, against a solid white background. caught mid-bite on a massive Entenmann's chocolate-glazed donut, EXAGGERATED wide mischievous grin, squinted sly eyes, raised eyebrow, highly expressive comic face, cheeks puffed with donut, thick dark chocolate glaze smeared heavily across his lips, chin, and one cheek, dripping glaze streaks rendered in deep brown ink, both hands gripping the oversized donut with white-knuckle drama, a giant chunk bitten away revealing the soft doughy interior, dramatic crumbs and glaze droplets exploding outward, rendered with bold Mignola ink splatter and expressive shadow shapes.
```
_Per story: replace the pose with this story's specific donut incident (Story 3: crane stance, swim goggles, containment towel, kitchen timer)._

### 7.4 Daniel — the fart template

```
[STYLE BLOCK], CHARACTERDANIELBULL23, young boy, slim build, brown hair, against a solid white background. EXAGGERATED comic reaction pose, eyes bulging wide in shock, mouth clenched tight in a grimace, body lurching forward from the force, legs stiffened straight, one hand gripping his stomach, chocolate glaze still smeared across his chin, as a MASSIVE catastrophic fart erupts behind him rendered as [THIS STORY'S FART REGISTER — e.g. Story 1: a towering nuclear mushroom cloud in deep blacks and ochre yellows; Story 2: visible concentric bass-wave rings warping the air; Story 3: a cold front — frost crystals feathering outward, sheets of wind-driven snow, the air itself visibly dropping in temperature], shockwave rings radiating outward, debris and crumbs blasted forward, thick ink motion lines conveying earth-shattering force, rendered with dramatic Mignola shadow shapes and heavy crosshatching, equal parts apocalyptic and absurd, comedic disaster energy.
```
_Rule: the fart's visual register must match the manuscript's literary register and must not repeat a prior story's._

### 7.5 The crack (no character — any model)

```
[STYLE BLOCK], against a solid white background. a vast jagged crack split violently through the fabric of space and time dominating the center of the composition, the fracture rendered with razor sharp splintering edges and heavy Mignola crosshatching, cosmic void bleeding through the tear filled with swirling ancient galaxies dying stars and deep space blackness, temporal distortion ripples and shockwave rings radiating outward from the fracture in concentric geometric shapes, ghostly silhouettes of [THIS STORY'S DESTINATION — e.g. Story 3: bare winter oaks, a stone kirk, a white bull, men in wool and plaid] visible inside the swirling vortex, time debris of shattered hourglasses fossilized bones ancient scrolls tumbling through the void, in the distant background THE SACRED FLAME OF LIFE burning as a towering roaring pillar of warm amber and ochre fire, CINEMATIC WIDE PANEL establishing shot, cosmic horror meets ancient mysticism energy, reverent and apocalyptic simultaneously.
```

### 7.6 Landing — Danny + Daniel in period costume (two-LoRA template)

Primary model: Danny. `extra_lora: dannyboy2323/character-danielbull23`.

```
[STYLE BLOCK], CHARACTERDADDANNY23, completely bald shaved head, very long thick chest-length light brown beard, warm light brown beard color, NOT red, NOT orange, NOT grey, neck tattoos, CHARACTERDANIELBULL23, CHARACTERDANIELBULL23, young boy, slim build, tall for his age, messy brown hair, two figure composition, each figure spatially isolated with clear empty ground space between them, no overlapping limbs between the two figures, exactly two arms and two legs per figure, correct human anatomy throughout, CHARACTERDADDANNY23 on the left standing having just regained his footing, disoriented expression giving way to fierce awareness, wearing [PERIOD COSTUME] over a plain dark t-shirt and jeans, the beard and neck tattoos wildly incongruous against [THE SETTING], CHARACTERDANIELBULL23 on the right [DANIEL'S COSTUME AND REACTION], a faint residual glow of spacetime energy still dissipating around the edges of both bodies, the crack in spacetime sealing itself shut in the background behind them, [SETTING RENDERED IN DETAIL — ground, light, weather, period figures as distant silhouettes], background figures kept small distant and minimally detailed, cinematic medium shot framing both full figures, the collision of two people unstuck from time landing in [THE EVENT]
```

### 7.7 Fun Police — Hater + Prosecutor (two-LoRA template)

Primary model: Hater. `extra_lora: dannyboy2323/character-prosecutor`.

```
[STYLE BLOCK], [HATER BLOCK], [HATER ANTI-DRIFT BLOCK], CHARACTERPROSECUTOR, [PROSECUTOR BLOCK], two figure composition, each figure spatially isolated, no overlapping limbs, exactly two arms and two legs per figure, [THIS STORY'S FUN POLICE DISASTER — e.g. Story 3: the Prosecutor in an Elizabethan ruff and slashed doublet over a pinstripe suit clinging to the roof of a wooden cattle pen, the Hater in a brown monk's habit worn over his Fun Police uniform with the uniform hat on top of the hood wedged in the fork of a bare oak tree, a massive wild white bull with black horn tips charging out of the open pen gate below them into a snowy medieval forest], slapstick comic energy, Wile E. Coyote catastrophe mid-moment, cinematic wide shot
```

---

## 8. STORY 3 — PRE-WRITTEN SCENE BLOCKS (to be finalized against the manuscript)

| Slot        | Scene block (append after style + character + guard)                                                                                                                                                                                                                                                                                                                            | Route                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| COVER 16:9  | CHARACTERDANIELBULL23 in a rope-belted wool tunic and sheepskin, both hands gripping the near horn of a massive charging wild white bull with black horn tips, stepping inside the arc of the horns and TURNING its head aside, the bull's body twisting past him, behind him a young nobleman in fur-collared cloak with a raised longsword frozen in shock, a stone forest church and bare winter oaks in snow, a hundred small distant figures as flat silhouettes, upper third of the frame kept clear and dark for title text, CINEMATIC WIDE PANEL, low angle | Daniel LoRA (1.1) → title pass          |
| COVER 1:1   | same scene recomposed vertical-square, bull and boy centered, title space at top                                                                                                                                                                                                                                                                                                 | Daniel LoRA (1.1) → title pass          |
| P1-A        | present-day kitchen, CHARACTERDADDANNY23 in the doorway holding a coffee mug, a blonde woman (Jenni block) seated at the table with rings on her fingers and a chambray shirt, through the window a purple Jeep Wrangler nose to nose with a green Jeep Wrangler in the driveway, warm morning light                                                                            | Danny LoRA                              |
| P1-B        | CHARACTERDANIELBULL23 standing on one leg in a Tae Kwon Do crane stance on a bath towel spread on a kitchen floor, wearing swim goggles, an Entenmann's donut box in one hand, a kitchen timer on the counter, a spiral notebook labeled DONUT EXPERIMENTS VOL 2, chewing with fixed seriousness                                                                                | Daniel LoRA                             |
| P2-A        | CHARACTERDANIELBULL23 in the fart template with the WEATHER register: frost feathering across a kitchen window in the shape of a hillside, visible breath, a towel lifting at the corners, cold air rendered as pale blue-white ink wash, Jenni's blonde hair lifting off her shoulders as she grins behind both hands                                                             | Daniel LoRA                             |
| P2-B        | Landing template, Scotland: knee-length undyed wool tunic over the t-shirt for Danny, hooded cloak, sheepskin and rope belt for Daniel, a black mastiff the size of a hay bale at Daniel's side, frozen leaf-mould ground, snow in the hollows, bare black oaks, peat smoke in the distance                                                                                           | Danny LoRA + Daniel extra_lora          |
| P3-A        | Johnny Cash block, seated on a fallen oak in a winter forest, legs crossed at the ankle, black coat against black trees, translucent, amber-white edge glow                                                                                                                                                                                                                       | flux-2-pro + Cash refs                  |
| P3-B        | CHARACTERDANIELBULL23 standing beside a crouching giant of a young man in wet plaid with a shovel-flat face and patchy red-brown beard (Will o' Rule), the giant crouched to the boy's eye level, the black mastiff between them, forest camp fire behind                                                                                                                         | Daniel LoRA                             |
| P4-A        | Old-Timer block, period: wolf-skin over the shoulders, whittling a small oak bull without looking at it, seated by a fire, milk-white eyes, slight smile                                                                                                                                                                                                                         | flux-2-pro + Old-Timer refs             |
| P4-B        | interior of a tiny stone church lit by a brazier and a few candles, an enormous kneeling man with a face carved to be screaming (Wallace), a young fur-collared nobleman (Bruce) with a longsword raised and frozen mid-air, forty men turning to look at CHARACTERDANIELBULL23 against the back wall in a sheepskin, the boy's expression of total innocent inquiry               | Daniel LoRA                             |
| P5-A        | Fun Police template, Story 3 disaster (ruff, monk's habit, pen roof, tree, white bull)                                                                                                                                                                                                                                                                                            | Hater LoRA + Prosecutor extra_lora      |
| P5-B        | THE TURN — hero panel: same as cover scene but tight — CHARACTERDANIELBULL23 from the waist up, both hands on the black horn tip, weight on the back foot, face in the complete stillness before action, the bull's eye like a coin inches from his face, frost and breath in the air                                                                                              | Daniel LoRA (1.1), 2 outputs, pick best |
| P6-A        | the young nobleman (Bruce) pressing a snapped black horn-tip into CHARACTERDANIELBULL23's open palm, the giant (Will) standing behind with his arms around the neck of the fallen white bull, dusk light, a hundred silhouettes                                                                                                                                                 | Daniel LoRA                             |
| P6-B        | present-day kitchen table with moving boxes against the wall: Jenni (block) holding the black horn-tip and looking at the boy, CHARACTERDANIELBULL23 mid-explanation with the DONUT EXPERIMENTS notebook open, CHARACTERDADDANNY23 seated very still, Grandpa (block) in the background making tea                                                                                                                                                      | Danny LoRA + Daniel extra_lora          |
| P7-A        | apartment parking lot at dusk, a green Jeep Wrangler and a purple Jeep Wrangler nose to nose, two women (Jen block, Jenni block) saying hello across the hoods, a boy's hand waving from the green Jeep window                                                                                                                                                                     | flux-2-pro                              |
| P7-B        | Journal panel template with the black horn-tip beside the journal and a woman's hair tie on the table                                                                                                                                                                                                                                                                             | Danny LoRA                              |

---

_This library is appended to every time a prompt is proven in production. Log the Replicate prediction URL and the chosen seed next to any prompt that becomes a template._
