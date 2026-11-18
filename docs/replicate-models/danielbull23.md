## Basic model info

Model name: dannyboy2323/character-danielbull23
Model description: Graphic novel illustration panels of Daniel for AWTB


## Model inputs

- prompt (required): Prompt for generated image. If you include the `trigger_word` used in the training process you are more likely to activate the trained object, style, or concept in the resulting image. (string)
- image (optional): Input image for image to image or inpainting mode. If provided, aspect_ratio, width, and height inputs are ignored. (string)
- mask (optional): Image mask for image inpainting mode. If provided, aspect_ratio, width, and height inputs are ignored. (string)
- aspect_ratio (optional): Aspect ratio for the generated image. If custom is selected, uses height and width below & will run in bf16 mode (string)
- height (optional): Height of generated image. Only works if `aspect_ratio` is set to custom. Will be rounded to nearest multiple of 16. Incompatible with fast generation (integer)
- width (optional): Width of generated image. Only works if `aspect_ratio` is set to custom. Will be rounded to nearest multiple of 16. Incompatible with fast generation (integer)
- prompt_strength (optional): Prompt strength when using img2img. 1.0 corresponds to full destruction of information in image (number)
- model (optional): Which model to run inference with. The dev model performs best with around 28 inference steps but the schnell model only needs 4 steps. (string)
- num_outputs (optional): Number of outputs to generate (integer)
- num_inference_steps (optional): Number of denoising steps. More steps can give more detailed images, but take longer. (integer)
- guidance_scale (optional): Guidance scale for the diffusion process. Lower values can give more realistic images. Good values to try are 2, 2.5, 3 and 3.5 (number)
- seed (optional): Random seed. Set for reproducible generation (integer)
- output_format (optional): Format of the output images (string)
- output_quality (optional): Quality when saving the output images, from 0 to 100. 100 is best quality, 0 is lowest quality. Not relevant for .png outputs (integer)
- disable_safety_checker (optional): Disable safety checker for generated images. (boolean)
- go_fast (optional): Run faster predictions with model optimized for speed (currently fp8 quantized); disable to run in original bf16 (boolean)
- megapixels (optional): Approximate number of megapixels for generated image (string)
- lora_scale (optional): Determines how strongly the main LoRA should be applied. Sane results between 0 and 1 for base inference. For go_fast we apply a 1.5x multiplier to this value; we've generally seen good performance when scaling the base value by that amount. You may still need to experiment to find the best value for your particular lora. (number)
- extra_lora (optional): Load LoRA weights. Supports Replicate models in the format <owner>/<username> or <owner>/<username>/<version>, HuggingFace URLs in the format huggingface.co/<owner>/<model-name>, CivitAI URLs in the format civitai.com/models/<id>[/<model-name>], or arbitrary .safetensors URLs from the Internet. For example, 'fofr/flux-pixar-cars' (string)
- extra_lora_scale (optional): Determines how strongly the extra LoRA should be applied. Sane results between 0 and 1 for base inference. For go_fast we apply a 1.5x multiplier to this value; we've generally seen good performance when scaling the base value by that amount. You may still need to experiment to find the best value for your particular lora. (number)


## Model output schema

{
  "type": "array",
  "items": {
    "type": "string",
    "format": "uri"
  },
  "title": "Output"
}

If the input or output schema includes a format of URI, it is referring to a file.


## Example inputs and outputs

Use these example outputs to better understand the types of inputs the model accepts, and the types of outputs the model returns:

### Example (https://replicate.com/p/pr176v5nknrmt0cykr6sjmrkrw)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDANIELBULL23, young boy, slim build, brown hair, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, against a solid white background, NOT photorealistic, NOT a photograph.\nriding a horse and eating a chocolate donut.",
  "go_fast": false,
  "lora_scale": 1,
  "megapixels": "1",
  "num_outputs": 1,
  "aspect_ratio": "1:1",
  "output_format": "webp",
  "guidance_scale": 3,
  "output_quality": 80,
  "prompt_strength": 0.8,
  "extra_lora_scale": 1,
  "num_inference_steps": 28
}
```

#### Output

```json
[
  "https://replicate.delivery/xezq/Wh2fsIXeyUhvWUeRn5q6Vy9UI11s3uHz3AT3Fi5iUAvO9BZtA/out-0.webp"
]
```


### Example (https://replicate.com/p/2rh3fps351rmy0cykr7tkqs9ng)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDANIELBULL23, young boy, slim build, brown hair, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, against a solid white background, NOT photorealistic, NOT a photograph.\nriding a horse and eating a chocolate donut.",
  "go_fast": false,
  "lora_scale": 1.1,
  "megapixels": "1",
  "num_outputs": 1,
  "aspect_ratio": "1:1",
  "output_format": "webp",
  "guidance_scale": 3,
  "output_quality": 80,
  "prompt_strength": 0.8,
  "extra_lora_scale": 1,
  "num_inference_steps": 28
}
```

#### Output

```json
[
  "https://replicate.delivery/xezq/YDXml9FqRtK5ExyjJ1fzCOPOPS6HbnlLbuf2SATF7UEEAhsWA/out-0.webp"
]
```


### Example (https://replicate.com/p/mcekdk5pm9rmy0cykr7tykhbnc)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDANIELBULL23, young boy, slim build, brown hair, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, against a solid white background, NOT photorealistic, NOT a photograph.\nsneakily eating a chocolate donut.",
  "go_fast": false,
  "lora_scale": 1.1,
  "megapixels": "1",
  "num_outputs": 1,
  "aspect_ratio": "1:1",
  "output_format": "webp",
  "guidance_scale": 3,
  "output_quality": 80,
  "prompt_strength": 0.8,
  "extra_lora_scale": 1,
  "num_inference_steps": 28
}
```

#### Output

```json
[
  "https://replicate.delivery/xezq/vdUMIdRjKkoPL5OOkVvfQTnL6dTJFAQel1IJsdPVm2nqAhsWA/out-0.webp"
]
```


### Example (https://replicate.com/p/5x4x1f9am9rmw0cykrcthka9hr)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDANIELBULL23, young boy, slim build, brown hair, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, against a solid white background, NOT photorealistic, NOT a photograph.\ncaught mid-bite on a massive Entenmann's chocolate-glazed donut, EXAGGERATED wide mischievous grin, squinted sly eyes, raised eyebrow, highly expressive comic face, cheeks puffed with donut, thick dark chocolate glaze smeared heavily across his lips, chin, and one cheek, dripping glaze streaks rendered in deep brown ink, both hands gripping the oversized donut with white-knuckle drama, a giant chunk bitten away revealing the soft doughy interior, dramatic crumbs and glaze droplets exploding outward, rendered with bold Mignola ink splatter and expressive shadow shapes.\n",
  "go_fast": false,
  "lora_scale": 1.1,
  "megapixels": "1",
  "num_outputs": 1,
  "aspect_ratio": "1:1",
  "output_format": "webp",
  "guidance_scale": 3,
  "output_quality": 80,
  "prompt_strength": 0.8,
  "extra_lora_scale": 1,
  "num_inference_steps": 28
}
```

#### Output

```json
[
  "https://replicate.delivery/xezq/th5epvLq75StUqHJBq2pzCYf7CJEVhUj4AakymkFcDuuKhsWA/out-0.webp"
]
```


### Example (https://replicate.com/p/1cp7dz3m05rmr0cykrgvjj8gf4)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDANIELBULL23, young boy, slim build, brown hair, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, against a solid white background, NOT photorealistic, NOT a photograph.\nEXAGGERATED comic reaction pose, eyes bulging wide in shock, mouth clenched tight in a grimace, body lurching forward from the force, legs stiffened straight, one hand gripping his stomach, chocolate glaze still smeared across his chin, as a MASSIVE catastrophic fart erupts behind him rendered as a towering nuclear mushroom cloud explosion in deep blacks and ochre yellows, the stem of the cloud billowing upward from directly behind his backside, shockwave rings radiating outward, debris and crumbs blasted forward, thick ink motion lines conveying earth-shattering force, the mushroom cloud rendered with dramatic Mignola shadow shapes and heavy crosshatching, equal parts apocalyptic and absurd, comedic disaster energy.\n",
  "go_fast": false,
  "lora_scale": 1.5,
  "megapixels": "1",
  "num_outputs": 1,
  "aspect_ratio": "1:1",
  "output_format": "webp",
  "guidance_scale": 3,
  "output_quality": 80,
  "prompt_strength": 0.8,
  "extra_lora_scale": 1,
  "num_inference_steps": 28
}
```

#### Output

```json
[
  "https://replicate.delivery/xezq/NAkzAN48vMZ3DpFw5eLhMpUAMlyJsuu0PpCeKRq9KJeqlCZtA/out-0.webp"
]
```


### Example (https://replicate.com/p/8bt99mjxahrmw0cykrjbz3vhh0)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDANIELBULL23, young boy, slim build, brown hair, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, against a solid white background, NOT photorealistic, NOT a photograph.\nEXAGGERATED comic reaction pose, eyes bulging wide in shock, mouth clenched tight in a grimace, body lurching forward from the force, legs stiffened straight, one hand gripping his stomach, chocolate glaze still smeared across his chin, as a MASSIVE catastrophic fart erupts behind him rendered as a towering nuclear mushroom cloud explosion in deep blacks and ochre yellows, the stem of the cloud billowing upward from directly behind his backside, shockwave rings radiating outward, debris and crumbs blasted forward, thick ink motion lines conveying earth-shattering force, the mushroom cloud rendered with dramatic Mignola shadow shapes and heavy crosshatching, equal parts apocalyptic and absurd, comedic disaster energy.\n",
  "go_fast": false,
  "lora_scale": 1,
  "megapixels": "1",
  "num_outputs": 2,
  "aspect_ratio": "1:1",
  "output_format": "webp",
  "guidance_scale": 3,
  "output_quality": 80,
  "prompt_strength": 0.8,
  "extra_lora_scale": 1,
  "num_inference_steps": 28
}
```

#### Output

```json
[
  "https://replicate.delivery/xezq/jABrP415EFJRCRre31a9baDoSSx6cFse5hn71yyldDp7VhsWA/out-0.webp",
  "https://replicate.delivery/xezq/QWyug8fOgMxsIysVDUAe2Q7Ed9gfba5OSyRYoXbGePEtXFyaB/out-1.webp"
]
```


### Example (https://replicate.com/p/yk5271pqmnrmt0cykrp9frbw70)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDANIELBULL23, young boy, slim build, brown hair, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt orms, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, against a solid white background, NOT photorealistic, NOT a photograph.\nCHARACTERDANIELBULL23 wedged and stuck inside a jagged crackling rift torn through the fabric of space and time, the crack rendered as a massive splintering fracture with razor sharp edges glowing in deep amber and ochre light, cosmic void visible through the tear filled with swirling galaxies stars and ancient celestial bodies, his body half-swallowed by the rift arms outstretched grasping desperately at the edges, EXAGGERATED expression of wide-eyed alarm and wild-haired chaos as temporal winds whip around him, ghostly afterimage silhouettes of dinosaurs medieval castles ancient Egypt pyramids and primitive cavemen visible in the swirling vortex behind him representing the rush into the past, bold ink motion lines streaming backward through the crack conveying violent time travel momentum, shockwave rings and temporal distortion ripples radiating outward from the fracture point, deep space blacks bleeding into warm earth tone nebula clouds, the crack itself crosshatched with heavy Mignola linework jagged and geometric, time debris including clocks hourglasses ancient coins and fossils tumbling through the void, CINEMATIC WIDE PANEL composition showing the full scale of the cosmic rift dwarfing the boy, brooding cosmic horror meets wide-eyed adventure energy.\n",
  "go_fast": false,
  "lora_scale": 1,
  "megapixels": "1",
  "num_outputs": 2,
  "aspect_ratio": "1:1",
  "output_format": "webp",
  "guidance_scale": 3,
  "output_quality": 80,
  "prompt_strength": 0.8,
  "extra_lora_scale": 1,
  "num_inference_steps": 28
}
```

#### Output

```json
[
  "https://replicate.delivery/xezq/y4kN37pZC4LtKRJSvIfr6iYgXHvmi1SojHFie2xfH12c9CZtA/out-0.webp",
  "https://replicate.delivery/xezq/kVnDGcK8ezRf60SyfiF4j5l5dva62G8fWy5nuCTKMm976FyaB/out-1.webp"
]
```


### Example (https://replicate.com/p/s6pm7hvby5rmr0cykrssa1efy8)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, against a solid white background, NOT photorealistic, NOT a photograph.\na vast jagged crack split violently through the fabric of space and time dominating the center of the composition, the fracture rendered with razor sharp splintering edges and heavy Mignola crosshatching, cosmic void bleeding through the tear filled with swirling ancient galaxies dying stars and deep space blackness, temporal distortion ripples and shockwave rings radiating outward from the fracture in concentric geometric shapes, ghostly silhouettes of prehistoric creatures ancient civilizations and crumbling ruins visible inside the swirling vortex representing the pull into the deep past, time debris of shattered hourglasses fossilized bones ancient scrolls and crumbling stone tablets tumbling through the void, in the distant background THE SACRED FLAME OF LIFE burning as a towering roaring pillar of warm amber and ochre fire, the flame rendered with bold ink strokes radiating outward like a divine sun casting long dramatic shadow shapes across everything, the flame pulsing with ancient energy representing all happiness joy and life force of existence, encircling the sacred flame a ring of ANCIENT HOODED DRUIDS standing perfectly still in silent observation, their robes rendered in deep blacks and earth tones with heavy shadow folds, faces completely obscured within deep hood darkness, long gnarled staff in each hand, their silhouettes small against the immensity of both the flame and the crack conveying ancient wisdom and cosmic scale, dramatic chiaroscuro lighting with the sacred flame casting warm amber light battling against the cold deep black void light of the space time fracture creating a clash of warm and cold dramatic ink shadows across the entire composition, CINEMATIC WIDE PANEL establishing shot, cosmic horror meets ancient mysticism energy, reverent and apocalyptic simultaneously.\n",
  "go_fast": false,
  "lora_scale": 1,
  "megapixels": "1",
  "num_outputs": 2,
  "aspect_ratio": "1:1",
  "output_format": "webp",
  "guidance_scale": 3,
  "output_quality": 80,
  "prompt_strength": 0.8,
  "extra_lora_scale": 1,
  "num_inference_steps": 28
}
```

#### Output

```json
[
  "https://replicate.delivery/xezq/7W4OjpjfepmUpUzjpotDKFftRo9EeIkYegeqd2z6esBdryQWLA/out-0.webp",
  "https://replicate.delivery/xezq/CR1ieUN0eYmAn0SllU5nunFRlgpUWzzjW5LAe8oP8n9sKDZtA/out-1.webp"
]
```


### Example (https://replicate.com/p/3nr07m3701rmr0cykrxa3drcz0)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDANIELBULL23, young boy, slim build, brown hair, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph.\nSINGLE SOLITARY BOY in the foreground, EXACTLY TWO ARMS EXACTLY TWO LEGS, clean isolated figure, CHARACTERDANIELBULL23 waking up flat on his back on sun-baked Cuban hillside dirt, eyes blinking open in groggy wide-eyed disorientation, propped up on one elbow squinting in confused alarm, dressed in full authentic 1898 Rough Riders uniform, tan khaki campaign shirt with brass buttons, wide-brimmed campaign hat knocked askew, canvas cartridge bandolier across his chest, leather cavalry boots, NO EXTRA LIMBS NO FLOATING BODY PARTS NO ADDITIONAL FIGURES TOUCHING THE FOREGROUND CHARACTER, the boy is completely spatially isolated in the immediate foreground with clear empty ground space surrounding him, background and foreground separated by dramatic chiaroscuro shadow band, distant background rendered exclusively as DARK SILHOUETTES AND INK SMOKE with no anatomical detail, Rough Riders soldiers visible only as flat black gestural silhouettes far up the hill, thick gunsmoke crosshatched ink clouds filling the midground creating a clear visual separation barrier between foreground boy and background battle, Spanish blockhouse at hilltop crest, tropical palm silhouettes, blazing Cuban sun casting hard geometric shadows, EXAGGERATED expression of total bewildered disorientation mouth agape eyes wide, CINEMATIC LOW ANGLE ground level shot, NOT photorealistic, NO EXTRA BODY PARTS, NO MERGED FIGURES, NO FLOATING LIMBS.",
  "go_fast": false,
  "lora_scale": 1,
  "megapixels": "1",
  "num_outputs": 2,
  "aspect_ratio": "1:1",
  "output_format": "webp",
  "guidance_scale": 3,
  "output_quality": 80,
  "prompt_strength": 0.8,
  "extra_lora_scale": 1,
  "num_inference_steps": 28
}
```

#### Output

```json
[
  "https://replicate.delivery/xezq/Bptmn5AUURYdAhfUMVK0Avxfzz2bljrmcU6CVuftHiWfxGyaB/out-0.webp",
  "https://replicate.delivery/xezq/UJ4sxqAbrfS9EKtpkP3V8385y3st82TTNu3YP0feEKrfxGyaB/out-1.webp"
]
```


### Example (https://replicate.com/p/d5kyrehg1xrmy0cykry8j3f1hr)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDANIELBULL23, young boy, slim build, brown hair, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph.\nSINGLE SOLITARY BOY in the foreground, EXACTLY TWO ARMS EXACTLY TWO LEGS, clean isolated figure, CHARACTERDANIELBULL23 standing upright in full panic realization, NO EXTRA LIMBS NO FLOATING BODY PARTS NO ADDITIONAL FIGURES TOUCHING THE FOREGROUND CHARACTER, completely spatially isolated in the immediate foreground with clear empty ground space surrounding him, background and foreground separated by dramatic chiaroscuro shadow band, dressed in full 1898 Rough Riders uniform now fully visible on his standing body, wide-brimmed campaign hat gripped in both hands and held out staring at it in horrified disbelief, head snapping downward looking at his own uniform with EXAGGERATED FULL BODY PANIC REACTION, eyes enormous white circles of pure shock, jaw dropped completely unhinged in a classic comic scream face, eyebrows shooting straight up off his forehead, body recoiling backward in a staggered stumble with one foot lifted mid-backstep, free hand splayed wide open in a full startle gesture, hair standing on end beneath where the hat was, the uniform itself suddenly registering to him rendered with visual emphasis arrows and comic ink speed lines pointing at the bandolier the boots and the campaign shirt as if his own eyes are noticing each piece simultaneously, MULTIPLE COMIC PANIC SWEAT DROPS flying off his face and head in classic manga style rendered in Mignola ink, in the background battle chaos continuing completely indifferent to his crisis, distant flat black silhouettes of Rough Riders charging, thick crosshatched gunsmoke ink clouds forming hard midground barrier, muzzle flash ink bursts at hilltop, tropical palm silhouettes, NO ANATOMICAL DETAIL IN BACKGROUND, all background figures remain pure flat gestural silhouettes, dramatic hard shadow band separating foreground from background, CINEMATIC MEDIUM SHOT framing full body from boots to hair showing complete panic pose, comedic existential horror energy, the specific panic of someone who just realized they are extremely lost in time.\n",
  "go_fast": false,
  "lora_scale": 1,
  "megapixels": "1",
  "num_outputs": 2,
  "aspect_ratio": "1:1",
  "output_format": "webp",
  "guidance_scale": 3,
  "output_quality": 80,
  "prompt_strength": 0.8,
  "extra_lora_scale": 1,
  "num_inference_steps": 28
}
```

#### Output

```json
[
  "https://replicate.delivery/xezq/OZqGLWCYWq7kNdoFyJFCfDQKGgplej3j3iW5s8fgakypcDZtA/out-0.webp",
  "https://replicate.delivery/xezq/DXgf9HiU4ax1Uia1qoGq9rChiflJJusT3WKIPfTIR7ZocDZtA/out-1.webp"
]
```


### Example (https://replicate.com/p/cysn02qtdxrmr0cyksavtcy77c)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDANIELBULL23, CHARACTERDANIELBULL23, CHARACTERDANIELBULL23, young boy, slim build, brown hair, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, against a solid white background, NOT photorealistic, NOT a photograph.\nCHARACTERDANIELBULL23 CHARACTERDANIELBULL23, the face and likeness of CHARACTERDANIELBULL23 clearly preserved and dominant, young boy with specific brown hair and facial features of CHARACTERDANIELBULL23 fully intact and recognizable, SINGLE FIGURE ONLY, EXACTLY TWO ARMS EXACTLY TWO LEGS, NO EXTRA LIMBS NO FLOATING BODY PARTS, fully airborne diving lunge through open air, body stretched at a diagonal angle across the frame, arms reaching forward, legs trailing behind fully extended, Rough Riders campaign hat tumbling off behind him, face showing EXAGGERATED fierce determined grimace with clearly rendered recognizable facial features of CHARACTERDANIELBULL23, teeth clenched, eyes narrowed in focus, brown hair whipping backward, uniform jacket billowing behind him, bold ink motion lines streaming behind the figure, dramatic chiaroscuro shadow shapes across the body in Mignola geometry, CINEMATIC DUTCH ANGLE, pure kinetic energy, solid white background, the likeness and facial identity of CHARACTERDANIELBULL23 is the single most important element of this image above all else.",
  "go_fast": false,
  "lora_scale": 1,
  "megapixels": "1",
  "num_outputs": 2,
  "aspect_ratio": "1:1",
  "output_format": "webp",
  "guidance_scale": 3,
  "output_quality": 80,
  "prompt_strength": 0.8,
  "extra_lora_scale": 1,
  "num_inference_steps": 28
}
```

#### Output

```json
[
  "https://replicate.delivery/xezq/8LefMzSBeYVRUo5g9SPv8wNFfNI6YJObOOQezyHKO1YxFRk1C/out-0.webp",
  "https://replicate.delivery/xezq/E0eANgU6WY1gJSQgGTv6MO6Nsx1VkXjjX4XpicQA8eluIisWA/out-1.webp"
]
```


### Example (https://replicate.com/p/e2ns7e7dp9rmy0cyksgrahtt48)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDANIELBULL23, CHARACTERDANIELBULL23, CHARACTERDANIELBULL23, young boy, slim build, brown hair, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph.\nCHARACTERDANIELBULL23 CHARACTERDANIELBULL23, the face and likeness of CHARACTERDANIELBULL23 clearly preserved and fully dominant, young boy with specific brown hair and facial features of CHARACTERDANIELBULL23 fully intact and recognizable, EXTREME CLOSE UP on just the head and eyes of CHARACTERDANIELBULL23 peering over the top edge of a dense Cuban jungle bush, only the top half of his face visible from the nose upward cresting the bush line, wide-brimmed Rough Riders campaign hat pushed low and crooked on his head, eyes enormous and darting sideways in EXAGGERATED terrified hypervigilance, pupils tiny pinpoints of pure fear, eyebrows shooting up into the hat brim, forehead drenched in large comic ink sweat drops, knuckles of both hands visible gripping the top of the bush branches with white knuckle terror, the bush itself rendered in bold dark Mignola ink leaf shapes with heavy crosshatching and deep shadow folds, dense tropical Cuban jungle foliage texture surrounding him, in the background beyond the bush the full chaos of the Battle of San Juan Hill erupting, flat dark ink silhouettes of charging Rough Riders soldiers storming up the hill, Spanish blockhouse fortifications at the hilltop crest, muzzle flash ink burst explosions and thick crosshatched gunsmoke clouds rolling across the battlefield, the bush forming a hard foreground occlusion barrier between the hiding boy and the battle raging behind him, dramatic chiaroscuro lighting with hard Cuban sun casting deep geometric Mignola shadow shapes across his face from above, the contrast between his tiny hidden terrified face and the enormous battle chaos behind him establishing perfect comedic scale, CINEMATIC TIGHT CLOSE UP framing just the hat brim down to the bush line showing only eyes forehead and hands gripping the bush, the likeness and facial identity of CHARACTERDANIELBULL23 is the single most important element of this image above all else, pure comic cowardice meets total war chaos energy, the universal hiding face of someone who wants absolutely no part of what is happening on the other side of that bush.",
  "go_fast": false,
  "lora_scale": 1,
  "megapixels": "1",
  "num_outputs": 2,
  "aspect_ratio": "1:1",
  "output_format": "webp",
  "guidance_scale": 3,
  "output_quality": 80,
  "prompt_strength": 0.8,
  "extra_lora_scale": 1,
  "num_inference_steps": 28
}
```

#### Output

```json
[
  "https://replicate.delivery/xezq/cJgPj4SMrbpUO1nOkuKKeeUdLY1A1aOnV3AEBBPrTMP9UisWA/out-0.webp",
  "https://replicate.delivery/xezq/sjwxkLd5sSIPNNkbCCXYBM5f7rZE4WC9KnpgRWnN5k8eUisWA/out-1.webp"
]
```


### Example (https://replicate.com/p/shazt3jsvxrmt0cykstsktfe60)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDANIELBULL23, CHARACTERDANIELBULL23, CHARACTERDANIELBULL23, young boy, slim build, brown hair, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph.\nCHARACTERDANIELBULL23 CHARACTERDANIELBULL23, the face and likeness of CHARACTERDANIELBULL23 clearly preserved and fully dominant, young boy with specific brown hair and facial features of CHARACTERDANIELBULL23 fully intact and recognizable, SINGLE FIGURE ONLY, NO EXTRA LIMBS NO FLOATING BODY PARTS, lying completely flat on his back in a boy's bedroom bed, deep in total exhausted unconscious sleep, eyes shut tight, face completely slack and peaceful in pure exhaustion, mouth barely open in a tiny snore, brown hair splayed out messily across the pillow in all directions, body completely buried under a thick rumpled blanket pulled up to his chin with only his head and a tuft of messy hair visible above the covers, the 1898 Rough Riders campaign hat hanging crookedly on the bedpost above his head as the single visual callback to the entire time travel adventure now concluded, the bedroom rendered in deep Mignola night blacks with only a single source of cool blue moonlight streaming through a partially open window casting one dramatic hard geometric shaft of pale light across the bed and his sleeping face, deep shadow filling every corner of the room with rich crosshatched darkness, a boy's bedroom details rendered as dark ink silhouettes, small bookshelf, cluttered desk, posters on the wall barely visible as dark shapes in the deep room shadows, dust motes floating in the moonlight shaft rendered as tiny ink dots, the overwhelming stillness and quiet of deep night rendered through heavy shadow and minimal detail, the campaign hat on the bedpost catching a sliver of moonlight as a deliberate compositional detail connecting this peaceful ending to the wild adventure, CINEMATIC LOW WIDE ANGLE shot from the foot of the bed looking up toward the pillow and window, the bed itself rendered in deep shadow with heavy crosshatched blanket folds, profound stillness and earned exhaustion energy, the deep dreamless sleep of a boy who has been through an absolutely ridiculous amount for one day, adventure concluded, safely home, completely and utterly done.",
  "go_fast": false,
  "lora_scale": 1,
  "megapixels": "1",
  "num_outputs": 2,
  "aspect_ratio": "1:1",
  "output_format": "webp",
  "guidance_scale": 3,
  "output_quality": 80,
  "prompt_strength": 0.8,
  "extra_lora_scale": 1,
  "num_inference_steps": 28
}
```

#### Output

```json
[
  "https://replicate.delivery/xezq/i0SkPEnZ7AImIB87xWGizU3IgwQld8frwbyZKyjCaPVbURWLA/out-0.webp",
  "https://replicate.delivery/xezq/cdsI7aea0wUfxEUAMcW4dfoyaaBCShJEgZhAgdjYFA5tRFZtA/out-1.webp"
]
```


### Example (https://replicate.com/p/za21jms0hnrmw0cyksx9g1tqwr)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDANIELBULL23, CHARACTERDANIELBULL23, CHARACTERDANIELBULL23, young boy, slim build, brown hair, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph.\nCHARACTERDANIELBULL23 CHARACTERDANIELBULL23, the face and likeness of CHARACTERDANIELBULL23 clearly preserved and fully dominant, young boy with specific brown hair and facial features of CHARACTERDANIELBULL23 fully intact and recognizable, SINGLE FIGURE ONLY, EXACTLY TWO ARMS EXACTLY TWO LEGS, NO EXTRA LIMBS NO FLOATING BODY PARTS, completely clean and tidy with NO DIRT NO GRIME NO TOILET PAPER NO DEBRIS, wearing his regular everyday present day clothes, PLAIN BROWN T-SHIRT, modern jeans, clean regular sneakers, walking through the front door of an upscale suburban American home, relaxed and casual body language of a boy arriving home after being dropped off by dad, one hand on the door frame pushing the front door open mid-stride, backpack slung over one shoulder, slight tired but comfortable expression, the kind of low energy contentment of arriving home at the end of a long day, hair naturally messy in a normal everyday way, the setting is a beautiful upscale suburban home with a generous covered front porch, warm present day American suburban architecture rendered in Mignola ink style, wide covered porch with decorative columns rendered in bold geometric ink shapes, porch railing with clean geometric shadow lines, porch light casting a warm amber cone of light downward onto the front steps and entry, potted plants flanking the front door rendered as dark botanical ink shapes, clean welcome mat at the threshold, the front door itself a solid substantial present day residential door with sidelights rendered in deep ink shadow, warm amber interior house light spilling outward through the open door and sidelights into the cool evening air beyond, a well maintained suburban front yard visible beyond the porch in the cool evening darkness, manicured shrubs and a clean concrete path rendered as dark ink silhouettes, a car pulling away in the distant background rendered as a simple dark ink shape with retreating tail lights suggesting dad has just dropped him off, the warm porch light and interior glow creating rich chiaroscuro contrast against the cool blue evening darkness outside, dramatic Mignola geometric shadow shapes falling across the porch floor and boy from the overhead porch light, CINEMATIC MEDIUM SHOT from slightly inside the doorway looking outward catching him mid-stride through the threshold, the likeness and facial identity of CHARACTERDANIELBULL23 is the single most important element of this image above all else, warm suburban homecoming energy, the perfectly ordinary moment of a boy arriving home",
  "go_fast": false,
  "lora_scale": 1,
  "megapixels": "1",
  "num_outputs": 2,
  "aspect_ratio": "1:1",
  "output_format": "webp",
  "guidance_scale": 3,
  "output_quality": 80,
  "prompt_strength": 0.8,
  "extra_lora_scale": 1,
  "num_inference_steps": 28
}
```

#### Output

```json
[
  "https://replicate.delivery/xezq/49gRvIkbed3xOSPJqfKyJaL2MkllvVtPNLe9edyGwsWetVk1C/out-0.webp",
  "https://replicate.delivery/xezq/9KNQLr2iBpYLOt0hy5MFFapdqkyKl58AaRJtofDs7ys3WRWLA/out-1.webp"
]
```


## Model readme

> No readme available for this model.

