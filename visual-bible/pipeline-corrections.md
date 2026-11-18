# Corrections to `claude/image-generation-pipeline.md` and `claude/image-prompt-library.md`

Findings from the published Story 1–2 image sets (pipeline §9 blockers 1–3 and 10). Apply before generating Story 3 images.

| # | Doc says | Published reality | Fix |
|---|---|---|---|
| 1 | "2 inline panels per ~550-word page → 4–6 panels (14 for Story 3)" | **~1 panel per ~100 words**: 74 panels (S1, 7,834 words), 56 (S2, 8,443 words) | Panel planner: one panel per ~90–100 words at paragraph boundaries; ~70–85 panels for a Story-3-length manuscript |
| 2 | Cover 16:9 first, then 1:1 | Site fields are **1:1 (1024)** and **9:16 portrait (1152×2048)**; 16:9 is not used | Generate 1:1 and 9:16 (separate recomposed renders) |
| 3 | Pillow title overlay in cover_style.json | Published covers have rich trade dress (issue box, bull-logo stamp, price/date, subtitle strip, tagline, barcode on S1 portrait) | Extend the cover template to these elements; keep the ochre heavy masthead |
| 4 | Panels referenced by markdown/JSON "convention TBD" | Sanity `story.body` Portable Text with `panelImage` blocks `{_key, _type:"panelImage", alignment, alt, image:{asset:{_ref}}}`; alignment **alternates** right/left | Publisher emits alternating alignment; start side alternates by story (S1 right, S2 left) |
| 5 | Panel format webp/1MP | Confirmed webp, **1024×1024 or 1008×1008** | Keep default model inputs |
| 6 | Postcard not mentioned | Each story has a `postcard` (photo composite PNG ~4000px) | Add a postcard step (composite real photos + comic art) or mark as manual |
| 7 | Alt text | S2 all "panel image" | Generate descriptive alt text per panel |
| 8 | Jen "standing beside a green Jeep" | S2: blue Audi A7 | Resolve canon (see visual-bible §4) |
| 9 | Grandpa "flannel, glasses on forehead, mug of tea" | S1-p15: dark jacket, glasses on face, graying beard, driving a truck | Update the block after choosing canon |
| 10 | Danny beard "dark chocolate brown" only | Published range dark brown → auburn → blond-brown | Choose canon; use warm-light auburn highlights as allowed variation |
| 11 | Fun Police never share a panel with Danny/Daniel | Consistent with published panels (villains appear alone in both stories) | No change |
