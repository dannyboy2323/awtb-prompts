# Visual-bible toolkit

Reproducible extraction of everything published on adventureswiththebull.com.

```bash
pip install -r requirements.txt
python3 tools/visual_bible/awtb_visual.py all            # Sanity -> cache/ -> references/ sheets + data/panel-manifest.json
python3 tools/visual_bible/fetch_training_sets.py cache/training   # LoRA training albums + sheets
python3 tools/build_prompt_registry.py                   # docs/replicate-models -> prompts/registry.json
python3 -m pytest tools/tests -q
```

`panel_tags.py` holds the hand-reviewed tags (character / place / object, hero | ok | detail | offmodel). Edit it, then rerun `sheets` and `manifest`.
