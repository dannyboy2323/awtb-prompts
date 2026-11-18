# awtb-visual-bible

Reference sheets, panel manifest and tooling that keep Adventures with the Bull's inline panels, covers and postcards visually consistent across the automated story pipeline.

```
visual-bible.md          master visual canon + recommendations
pipeline-corrections.md  fixes to the image pipeline docs, from the published Story 1-2 sets
panel-manifest.json      all 130 published images: URLs, sizes, alignment, tags, pacing, context
refs/characters/         Danny, Daniel, Grandpa, Jen, Johnny Cash, Old-Timer, Teddy, Biggie, Prosecutor, Hater
refs/places-objects/     Grandpa's house, Space-Time Continuum, Sacred Flame, donuts, journals, plant, vehicles, prison, Cuba, Brooklyn...
refs/covers/ postcards/ style/
tools/                   awtb_visual.py (fetch/sheets/manifest), panel_tags.py (hand-reviewed tags), tests/
```

## Rebuild
```bash
pip install -r requirements.txt
python3 tools/awtb_visual.py all      # fetches from Sanity, rebuilds sheets + manifest
python3 -m pytest tools/tests -q
```
Adding a story: add its slug to `STORIES`, review its panels, append tags to `panel_tags.py`, rerun.
Source images come from the public Sanity CDN and are cached in `cache/` (git-ignored).
