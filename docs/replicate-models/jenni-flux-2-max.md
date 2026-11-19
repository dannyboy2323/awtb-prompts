Model name: black-forest-labs/flux-2-max
Model description: Used (with reference images) to generate the approved Jenni character reference set. No trained LoRA exists for Jenni.

## Notes
- Author-run on Replicate, 2026-11-19 02:12 UTC; ~40 s per 1 MP image.
- Six `input_images` were earlier Jenni renders (full-body angled/front/side, headshots front/side/angled); the hosted URLs expire, so the approved files are kept in `references/approved/jenni/`.
- Only camera angle/crop and footwear (barefoot vs checkered Vans) were varied between the 8 approved images.
- Settings: `resolution` "1 MP" (1008x1008), `safety_tolerance` 2, `output_format` webp, quality 80, aspect 1:1.

### Example (https://replicate.com/p/kp5v6qy26xrmr0d1y69rk0px0m)

#### Input

```json
{
  "aspect_ratio": "1:1",
  "input_images": [
    "https://replicate.delivery/pbxt/QAzsuKM23gcjmqPibL0B4fHgvoDuA3XQDofVw9tOwmmzDzaX/jenni-full_body-angled.webp",
    "https://replicate.delivery/pbxt/QAzsuA4zCGwgleaaJXL1VIPPFsdxmE35PpByH2D8ZOWddCPs/jenni-full_body-front.webp",
    "https://replicate.delivery/pbxt/QAzsuIQtP3xGjGStl9AowTVpdh9loHrtGUkP6wr3J23w592x/jenni-full_body-side.webp",
    "https://replicate.delivery/pbxt/QAzsuYAwYDAUnSuYd5iIjexV1apTjWsMsFNL7rVaVKUch9yo/jenni-headshot-front.webp",
    "https://replicate.delivery/pbxt/QAzsuhQEqKpg4C8DBEdvo1Il7vEwy0SuKVOsA2tr9TYgpyrO/jenni-headshot-side.webp",
    "https://replicate.delivery/pbxt/QAzsuJFrOTHYbR1fyBudwyGybLO3iA26bppM1IXjHDoKlVQp/jenni-headshot-angled.webp"
  ],
  "output_format": "webp",
  "output_quality": 80,
  "prompt": "2D graphic novel illustration, inked comic book art, 40-year-old pretty woman (bohemian tattoos on arms, hippy-bohemian-gypsy vibe), smiling and happy, with flower in hair, natural curly blond hair, bright blue eyes, light/happy energy, wearing black leggings with a vintage black Nirvana rock t-shirt and checkered black and white vintage Vans sneakers, slender/skinny build, 5' 5\" tall, 110 lbs.  Portrait, full body shot, facing camera. Mike Mignola art style, bold heavy ink linework, dramatic chiaroscuro shadows, deep blacks with muted earth-tone color, desaturated ochres and burnt reds, warm amber tones, gritty pulp horror aesthetic, rough crosshatching, halftone grain texture, woodcut-like rendering, strong geometric shadow shapes, cinematic comic panel composition, dark fantasy illustration, weathered and battle-worn, brooding intensity, flat cel shading with rich earth tones, colored ink illustration, against a solid white background, NOT photorealistic, NOT a photograph",
  "resolution": "1 MP",
  "safety_tolerance": 2
}
```

#### Output

```json
["https://replicate.delivery/xezq/ofDIMpBEf8qQ3kIvCMBiEmzBt06i8HdnBrgWp74LHsF60AjXA/tmpn7xjyszg.webp"]
```
