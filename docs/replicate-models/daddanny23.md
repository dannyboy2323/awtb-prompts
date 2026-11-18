## Basic model info

Model name: dannyboy2323/character-daddanny23
Model description: Used to generate graphic novel style illustration panels of Danny for AWTB


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

### Example (https://replicate.com/p/wrwje7nthdrmt0cykre8cx1rm0)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDADDANNY23, completely bald shaved head, very long thick chest-length brown beard, neck tattoos, black shirt, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, against a solid white background, NOT photorealistic, NOT a photograph",
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
  "https://replicate.delivery/xezq/PnwJuZ8CiHYyLxo3H23GG7fhlfRrv3gtefxmVHgH29elwJk1C/out-0.webp"
]
```


### Example (https://replicate.com/p/dp9ymd2vnsrmt0cykrhaxywsh8)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDADDANNY23, completely bald shaved head, very long thick chest-length dark brown beard, dark chocolate brown beard, deep espresso brown beard color, neck tattoos, black shirt, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, against a solid white background, NOT photorealistic, NOT a photograph, strong facial likeness preserved, character face accuracy critical, CHARACTERDADDANNY23 facial features dominant, federal prison release scene, massive imposing concrete prison gate swinging open behind him, harsh morning backlight silhouetting the figure from behind casting a long dramatic shadow forward, figure walking forward toward viewer with slow deliberate weight, a single battered paper bag of belongings clutched in one fist, razor-wire fence receding into deep shadow on both sides, cold institutional grey concrete walls flanking the exit, faded black stenciled letters reading \"PROCESSING\" above the gate, a single guard tower looming in the upper background barely visible in shadow, cracked asphalt ground beneath worn boots, oppressive negative space above the figure, sparse desolate landscape beyond the gate, freedom and menace in equal measure, the quiet devastation of a man stepping back into a world that kept moving without him\n\ue056\ue03b\ue0c1\ue0fb\ue0f9\ue0ce",
  "go_fast": false,
  "lora_scale": 1.1,
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
  "https://replicate.delivery/xezq/0ex0fw6JXysoMUQ2X0KXzfp46vd4WHegfE2lztzXC9JLfUIrF/out-0.webp",
  "https://replicate.delivery/xezq/GP5Yeny0Ic0RIiwKyTc9G0WlzYMpem4Je159tfrsBMdkPFyaB/out-1.webp"
]
```


### Example (https://replicate.com/p/x8j6x910y5rmt0cykrmbv4hxw0)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDADDANNY23, completely bald shaved head, very long thick chest-length dark brown beard, dark chocolate brown beard, deep espresso brown beard color, neck tattoos, black shirt, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph, strong facial likeness preserved, character face accuracy critical, CHARACTERDADDANNY23 facial features dominant, prison release exterior scene, figure standing just outside the prison gate with the massive concrete walls and razor wire receding behind him, a small crowd of waiting figures in the middle distance across a cracked asphalt lot, one small boy standing apart from the crowd slightly forward, roughly 12 years old, dark hair, looking directly at the released figure, neither moving yet, the weight of the moment suspended between them, warm amber backlight from low morning sun cutting across the lot and separating the boy from the crowd, long dramatic shadows stretching across the ground between father and son, emotional distance rendered as physical distance, the crowd blurred and de-emphasized in deep shadow, all focus pulled to the two figures and the charged empty space between them, cinematic wide shot panel, devastating quiet, the reunion not yet begun\n",
  "go_fast": false,
  "lora_scale": 1.1,
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
  "https://replicate.delivery/xezq/KVaLgEdqmeReG0lvcpmMMyMYDYiaSw30faZzPhaD2CVmzCZtA/out-0.webp",
  "https://replicate.delivery/xezq/lSqShvspsGImGJlLprPMVK8Xf1aV7KS8uY4Hwx6rkmg5sQWLA/out-1.webp"
]
```


### Example (https://replicate.com/p/jkrv7sgkf5rmw0cykrmt3yesh4)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDADDANNY23, completely bald shaved head, very long thick chest-length dark brown beard, dark chocolate brown beard, deep espresso brown beard color, neck tattoos, black shirt, athletic build, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph, strong facial likeness preserved, character face accuracy critical, CHARACTERDADDANNY23 facial features dominant, prison release exterior scene, figure standing just outside the prison gate with the massive concrete walls and razor wire receding behind him, a small crowd of waiting figures in the middle distance across a cracked asphalt lot, one small boy standing apart from the crowd slightly forward, roughly 12 years old, dark hair, looking directly at the released figure, neither moving yet, the weight of the moment suspended between them, warm amber backlight from low morning sun cutting across the lot and separating the boy from the crowd, long dramatic shadows stretching across the ground between father and son, emotional distance rendered as physical distance, the crowd blurred and de-emphasized in deep shadow, all focus pulled to the two figures and the charged empty space between them, cinematic wide shot panel, devastating quiet, the reunion not yet begun\n",
  "go_fast": false,
  "lora_scale": 1.1,
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
  "https://replicate.delivery/xezq/wYMrnJqGYAoXOVOzSdbWUTB5pXTxZrSTFKfvHrz0vegvahsWA/out-0.webp",
  "https://replicate.delivery/xezq/IYapfJptwPzKdKu2BZQ597nD5IZe2mSy9UezsAT9QNjeqFyaB/out-1.webp"
]
```


### Example (https://replicate.com/p/mjewd4f7bhrmw0cykrqsctvtwc)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDADDANNY23, completely bald shaved head, very long thick chest-length dark brown beard, dark chocolate brown beard, deep espresso brown beard color, neck tattoos, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph, strong facial likeness preserved, character face accuracy critical, CHARACTERDADDANNY23 facial features dominant, rear view from behind, shirtless, powerfully athletic muscular build, broad shoulders, defined back musculature, V-taper torso, entire back and torso covered in dense intricate traditional black tattoos, bold traditional tattoo linework layered across every inch of skin from neck down to waistline, large intricate back piece as centerpiece surrounded by dense traditional filler tattoos, sleeve tattoos extending from neck tattoos downward across shoulders and arms, tattoo designs featuring bold traditional motifs rendered in pure black ink, thick bold outlines with heavy black fill, the tattoo linework blending seamlessly with the Mignola ink illustration style, figure viewed straight from behind standing with weight and authority, beard visible from behind falling over the back of the neck onto upper back, the tattoo coverage telling a story of a life fully committed, dramatic side lighting carving deep shadow into the muscle definition and tattoo linework simultaneously, the back itself treated as a full composition within the panel, raw imposing physical presence\n",
  "go_fast": false,
  "lora_scale": 1.1,
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
  "https://replicate.delivery/xezq/xmOeR3re8JgXZk7aEfpzeW1SMnvJoMtYjBXwWKG55rWBHGyaB/out-0.webp",
  "https://replicate.delivery/xezq/OsOSeFqygbVbAqqFX4esOezBU0lsNcAgtVivaCinnHVgDDZtA/out-1.webp"
]
```


### Example (https://replicate.com/p/eh40bhk4m5rmy0cykrw9cr7bvw)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDADDANNY23, completely bald shaved head, very long thick chest-length dark brown beard, dark chocolate brown beard, deep espresso brown beard color, neck tattoos, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph, strong facial likeness preserved, character face accuracy critical, CHARACTERDADDANNY23 facial features dominant, figure lying on the ground just regaining consciousness, propped up on one elbow pushing himself up from the dirt, disoriented expression giving way to fierce awareness, dressed in authentic 1898 Rough Riders uniform, 1st US Volunteer Cavalry, tan campaign shirt, brown canvas trousers, leather cavalry boots, brown campaign hat with wide brim dented and dusty, canvas cartridge belt across the chest loaded with rifle rounds, canteen on hip, the uniform roughed up and dirt-caked as if just materialized from a temporal rift, a faint residual glow of spacetime energy still dissipating around the edges of his body, the crack in spacetime sealing itself shut in the background behind him with a jagged sliver of cosmic void barely visible as it closes, the ground beneath him is the red dirt and scrub grass of San Juan Hill Cuba 1898, the hill rising steeply behind him, Rough Riders soldiers charging up the hill in the middle distance through gun smoke and chaos, Spanish blockhouse fortifications visible at the crest of the hill, artillery smoke billowing in thick heavy ink clouds across the upper panel, distant muzzle flashes rendered as stark white bursts against deep shadow, American flag barely visible through the smoke carried by a charging soldier in the background, the sounds of battle implied through the visual chaos surrounding the dazed figure, other Rough Riders around him mid-charge paying him no attention consumed by the battle, tropical Cuban vegetation rendered in deep shadow flanking the hill, harsh midday sun beating down creating stark overhead shadows, the figure in the immediate foreground disoriented but already reading the situation with calculating intensity, one hand instinctively reaching for a weapon at his hip, the collision of a man unstuck from time landing in one of history's most famous battles, cinematic low angle shot looking up slightly emphasizing the hill charge behind him, gritty historical war illustration, pulp adventure energy meets cosmic horror",
  "go_fast": false,
  "lora_scale": 1.1,
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
  "https://replicate.delivery/xezq/2b8k0nMmS0KWOBfQZigKosG99uerReCIDzBWPZrPbz92UDZtA/out-0.webp",
  "https://replicate.delivery/xezq/hgjLLMXj4FqzOFHl8HBoMHmwcOo93LqkMZZ2NeH4pK2N1QWLA/out-1.webp"
]
```


### Example (https://replicate.com/p/t466d88hfdrmt0cykrxabbf43g)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDADDANNY23, completely bald shaved head, very long thick chest-length dark brown beard, dark chocolate brown beard, deep espresso brown beard color, neck tattoos, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph, strong facial likeness preserved, character face accuracy critical, CHARACTERDADDANNY23 facial features dominant, single figure only in foreground, exactly two arms exactly two legs, correct human anatomy, no extra limbs, no floating limbs, no disembodied body parts, no anatomical errors, clean figure rendering, figure lying on the ground just regaining consciousness, propped up on one elbow pushing himself up from the dirt, disoriented expression giving way to fierce awareness, dressed in authentic 1898 Rough Riders uniform, 1st US Volunteer Cavalry, tan campaign shirt, brown canvas trousers, leather cavalry boots, brown campaign hat with wide brim dented and dusty, canvas cartridge belt across the chest loaded with rifle rounds, canteen on hip, the uniform roughed up and dirt-caked as if just materialized from a temporal rift, a faint residual glow of spacetime energy still dissipating around the edges of his body, the crack in spacetime sealing itself shut in the background behind him with a jagged sliver of cosmic void barely visible as it closes, the ground beneath him is the red dirt and scrub grass of San Juan Hill Cuba 1898, the hill rising steeply behind him, Rough Riders soldiers charging up the hill in the middle distance through gun smoke and chaos kept small and distant in background, Spanish blockhouse fortifications visible at the crest of the hill, artillery smoke billowing in thick heavy ink clouds across the upper panel, distant muzzle flashes rendered as stark white bursts against deep shadow, American flag barely visible through the smoke carried by a charging soldier in the deep background, tropical Cuban vegetation rendered in deep shadow flanking the hill, harsh midday sun beating down creating stark overhead shadows, the figure in the immediate foreground disoriented but already reading the situation with calculating intensity, one hand instinctively reaching for a weapon at his hip, cinematic low angle shot looking up slightly emphasizing the hill charge behind him, gritty historical war illustration, pulp adventure energy meets cosmic horror, background figures kept small distant and minimally detailed to avoid anatomical confusion, negative space used deliberately around the foreground figure to isolate and clarify his silhouette, clean panel borders, no overlapping limbs between foreground and background figures\n",
  "go_fast": false,
  "lora_scale": 1.1,
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
  "https://replicate.delivery/xezq/rDEe27e7yTsjKEQ2NjbGA7OCuvetprbbnsv5f5qijLnlwGyaB/out-0.webp",
  "https://replicate.delivery/xezq/P6Qoy3kscCp2B5p0f8nxXZlW106U433jtTz7zr9tafsJshsWA/out-1.webp"
]
```


### Example (https://replicate.com/p/025mxfvyz9rmw0cykrya8br1zc)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, CHARACTERDADDANNY23, completely bald shaved head, very long thick chest-length dark brown beard, dark chocolate brown beard, deep espresso brown beard color, neck tattoos, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph, strong facial likeness preserved, character face accuracy critical, CHARACTERDADDANNY23 facial features dominant, single figure only in foreground, exactly two arms exactly two legs, correct human anatomy, no extra limbs, no floating limbs, no disembodied body parts, no anatomical errors, clean figure rendering, figure standing upright having just scrambled to his feet, body language of pure shock and disorientation, looking down at himself with wide eyes and expression of absolute bewildered panic, both hands held out in front of him staring at the 1898 Rough Riders uniform he is wearing, head snapping between looking down at his own clothes and looking around wildly at the battle chaos surrounding him, mouth open mid-exclamation, the brooding intensity replaced entirely by raw unfiltered shock and confusion, eyebrows raised high, the long dark beard adding to the wild disheveled energy of the moment, dressed in authentic 1898 Rough Riders uniform, 1st US Volunteer Cavalry, tan campaign shirt, brown canvas trousers, leather cavalry boots, brown campaign hat knocked askew on his bald head at a ridiculous angle, canvas cartridge belt across the chest, the incongruity of this very modern tattooed bald man in period military costume rendered with maximum comic and dramatic tension, neck tattoos visible above the period collar, San Juan Hill Cuba 1898 battle raging in the background, Rough Riders soldiers charging past him in the middle distance ignoring him completely, gun smoke and chaos everywhere, Spanish blockhouse fortifications at the crest of the hill, artillery smoke billowing in heavy ink clouds, muzzle flashes as stark white bursts in deep shadow, tropical Cuban vegetation in deep shadow flanking the scene, harsh midday overhead sun, background figures kept small distant and minimally detailed, negative space used deliberately around the foreground figure to isolate and clarify his silhouette, no overlapping limbs between foreground and background figures, cinematic medium shot framing the full figure, the campaign hat sitting comically crooked on the bald head as a visual punctuation mark of the absurdity of his situation, pure existential panic rendered in Mignola ink, the moment a man realizes he is catastrophically lost in time",
  "go_fast": false,
  "lora_scale": 1.1,
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
  "https://replicate.delivery/xezq/YOh7ByzOCDp9E5LBTD7BOBhBQOnUGwAOXdoeezdd5efh6GyaB/out-0.webp",
  "https://replicate.delivery/xezq/RktTEyoK4AZHFRt2vlH9KY1heRR7hJYIfn8aDkPcNX7ouhsWA/out-1.webp"
]
```


### Example (https://replicate.com/p/sex5wt81wdrmw0cyks1sc57g84)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, against a solid white background, NOT photorealistic, NOT a photograph.\nTEDDY ROOSEVELT mounted on a powerful charging warhorse, rendered as a bold singular heroic ink figure, NO OTHER HUMAN FIGURES IN THE FOREGROUND, Roosevelt in full 1898 Rough Riders commanding officer uniform, round wire-rimmed spectacles catching dramatic light, thick bristling mustache rendered in heavy ink strokes, wide-brimmed campaign hat pressed low and firm against the charging wind, military campaign jacket with officer insignia, leather riding gauntlets gripping the reins with iron authority, cavalry saber raised high overhead in one fist catching the Cuban sun in a dramatic glinting ink highlight, jaw set with absolute iron Roosevelt determination, the warhorse beneath him a massive muscular beast mid-full-gallop with all four hooves leaving the ground in a classic heroic cavalry charge pose, horse musculature rendered with bold Mignola geometric shadow shapes and heavy crosshatching conveying raw power and momentum, thick ink motion lines streaming backward from horse and rider conveying explosive forward velocity, Roosevelt leaning forward into the charge with total fearless momentum, EXAGGERATED heroic comic proportions, square jaw, barrel chest, commanding physical presence radiating authority and unstoppable force, dramatic chiaroscuro lighting with hard Cuban sun casting deep geometric shadow shapes across horse and rider from a sharp overhead angle, dust and earth clods kicked up by hooves rendered as bold ink splash shapes, the composition framing Roosevelt and horse as a single unified heroic silhouette of charging power, San Juan Hill rising in the far distant background rendered purely as flat dark ink shapes with no anatomical detail, faint gunsmoke crosshatched clouds on the horizon, tropical palm silhouettes flanking the edges, CINEMATIC LOW ANGLE shot looking up at horse and rider making them loom massive and heroic against the sky, legendary larger than life energy, the definitive Mignola ink portrait of American Rough Rider audacity.",
  "go_fast": false,
  "lora_scale": 1.1,
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
  "https://replicate.delivery/xezq/2uteFTsbuJzjP6pk7VK117NksXM4OxHY9WRP2HNx3ZeV1hsWA/out-0.webp",
  "https://replicate.delivery/xezq/f54MDnzUXKRFR6CdM0xLFCeVpA0MB78LLO8tNdnZEvSV1hsWA/out-1.webp"
]
```


### Example (https://replicate.com/p/cvymc1cj6nrmr0cyks2t48peg8)

#### Input

```json
{
  "model": "dev",
  "prompt": "Here's the prompt \u2014 structuring the son from behind specifically to keep us well clear of any minor depiction concerns while still telling the story:\n\n2D graphic novel illustration, inked comic book art, CHARACTERDADDANNY23, completely bald shaved head, very long thick chest-length dark brown beard, dark chocolate brown beard, deep espresso brown beard color, neck tattoos, Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph, strong facial likeness preserved, character face accuracy critical, CHARACTERDADDANNY23 facial features dominant, single bald bearded tattooed figure in foreground exactly two arms exactly two legs, correct human anatomy, no extra limbs, no floating limbs, no disembodied body parts, no anatomical errors, clean figure rendering, three figure composition, CHARACTERDADDANNY23 standing on the left facing right toward Teddy Roosevelt, a small boy viewed entirely from behind standing between and slightly in front of them, boy roughly the size and build of a 12 year old, brown messy hair visible beneath an oversized 1898 Rough Riders campaign hat sitting too large on his small head, dressed in a miniature 1898 US infantry uniform slightly too big for his frame, the oversized uniform and hat communicating his youth and small stature purely through silhouette, boy viewed strictly from behind at all times his face never visible, Teddy Roosevelt standing on the right in full 1898 Rough Riders officer uniform, round wire rimmed spectacles, thick mustache, campaign hat, cavalry sword at hip, bandolier across chest, Roosevelt rendered with iconic recognizable features, barrel chested commanding posture, Roosevelt leaning slightly forward with animated enthusiastic expression mid-speech gesturing broadly with one hand toward CHARACTERDADDANNY23, Roosevelt's expression of boisterous delight and fascination at this strange bald tattooed man from another time, CHARACTERDADDANNY23 expression of bewildered disbelief staring back at Roosevelt, the long dark beard and neck tattoos wildly incongruous against the 1898 battlefield setting, the boy between them small and dwarfed by both adult figures his oversized hat and uniform doing all the storytelling work, San Juan Hill Cuba 1898 battle smoke and chaos receding into deep background, tropical vegetation in deep shadow, harsh midday sun overhead casting strong downward shadows on all three figures, background kept minimal and distant, negative space used deliberately around all three figures to isolate and clarify each silhouette, no overlapping limbs between any figures, cinematic medium shot framing all three figures in a single panel, the absurdity and wonder of a man from the future standing on a famous battlefield being enthusiastically addressed by one of history's most outsized personalities, Roosevelt's booming larger than life energy contrasted against the tattooed time traveler's stunned silence, pulp historical adventure meets cosmic displacement",
  "go_fast": false,
  "lora_scale": 1.1,
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
  "https://replicate.delivery/xezq/fLhqXU554iSnWigwg2I9YvGL4H1fdrKeluTPleySSrVufOk1C/out-0.webp",
  "https://replicate.delivery/xezq/NPQzfMmzlaWehEKieaRhyFFoUqOFeNcCLV5De353e9f097QWLA/out-1.webp"
]
```


### Example (https://replicate.com/p/xtd15ne5w1rmr0cykssvpyz7vg)

#### Input

```json
{
  "model": "dev",
  "prompt": "Mike Mignola art style, Hellboy comic art style, 2D graphic novel illustration, inked comic book art, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph, NOT realistic, NOT painted, styled exactly like a Mignola Hellboy comic panel, CHARACTERDADDANNY23, completely bald shaved head, very long thick chest-length dark brown beard, dark chocolate brown beard, deep espresso brown beard color, neck tattoos, strong facial likeness preserved, character face accuracy critical, CHARACTERDADDANNY23 facial features dominant, single figure only, exactly two arms exactly two legs, correct human anatomy, no extra limbs, no floating limbs, no disembodied body parts, no anatomical errors, clean figure rendering, figure seated alone at a heavy worn wooden desk deep in the night, hunched slightly forward over an open leather bound travel journal, right hand writing slowly with a pen across the open pages, left hand wrapped around a cracked coffee mug, expression of deep exhausted contemplative brooding, the look of a man who has seen too much and is trying to make sense of all of it, back in present day clothing, plain dark t-shirt, neck tattoos fully visible above the collar, the bald head catching the warm amber glow of a single desk lamp, the long dark beard resting against his chest as he leans forward, the 1898 Rough Riders campaign hat hanging on the corner of the chair behind him, a single desk lamp as the only light source casting a tight warm amber pool across the desk and his face, everything beyond the lamp radius dissolving into pure Mignola black, dramatic single source chiaroscuro lighting carving deep shadow across the bald head and beard, the open journal pages catching warm light, handwritten text rendered as loose illegible scrawl, small rough thumbnail sketches visible on the journal pages, scattered items across the desk, spent pen, loose crumpled papers, old pocket watch, the room beyond falling into total darkness, a window behind him showing the deep blue black of late night, cinematic medium close shot framing the figure from the waist up at the desk, quiet brooding introspection, the last panel of the graphic novel",
  "go_fast": false,
  "lora_scale": 1.1,
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
  "https://replicate.delivery/xezq/o7CjRGwyxOIEGJ516GXmg6C39qAtdzDsBl0INMoTfv4nTRWLA/out-0.webp",
  "https://replicate.delivery/xezq/9JhjoPMoho57IhizB37hWPUdccr1soRnxAEr1KcvWg6zpIrF/out-1.webp"
]
```


### Example (https://replicate.com/p/j301mmc5p5rmr0cz0tyrpb6e40)

#### Input

```json
{
  "model": "dev",
  "prompt": "2D graphic novel illustration, inked comic book art, bold heavy black ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, flat cel shading with rich earth tones, colored ink illustration, NOT photorealistic, NOT a photograph, NOT realistic, NOT painted, strong facial likeness preserved, character face accuracy critical, facial features dominant, single figure only, exactly two arms exactly two legs, correct human anatomy, no extra limbs, no floating limbs, no disembodied body parts, no anatomical errors, clean figure rendering, CHARACTERDADDANNY23, completely bald shaved head, very long thick chest-length dark brown beard, dark chocolate brown beard, deep espresso brown beard color, neck tattoos, athletic build, laying in his prison cot with eyes open while the prison guard is walking by the doorway shining his flashlight doing count at 5AM",
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
  "https://replicate.delivery/xezq/aveEb4dQ5MRrTqZrewkZcR0Amlme7KMtg99JMeBS5JEhG3MbB/out-0.webp"
]
```


## Model readme

> No readme available for this model.

