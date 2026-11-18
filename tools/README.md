# AWTB image tools

`generate_story_images.py` renders a story's cover (16:9 + 1:1) and inline panels from a
manifest (`storyNNN-panels.json`) via Replicate, validates every prompt against the series'
consistency rules, runs automated QA, overlays the cover title, and writes outputs + an
audit-trail manifest. Full procedure: `image-generation-pipeline.md`. Prompt blocks:
`image-prompt-library.md`.

```bash
pip install requests pillow pytest
export REPLICATE_API_TOKEN=...                       # from the project's replicate-key.txt
python tools/generate_story_images.py stories/story003/story003-panels.json --dry-run
python tools/generate_story_images.py stories/story003/story003-panels.json --max-predictions 40
python -m pytest tools/tests -q
```

Config: `tools/cover_style.json` (title font/colors), `tools/replicate_versions.json` (version pins),
`references/approved/` (approved reference renders for characters without a trained LoRA).
