# Effects catalog (2026-10-08)

80 named signature moves from 8 premium documentary channels, so the creator can direct with a code ("FX-34 on 3c").
- **Text index:** `CATALOG.md` (codes, names, one line each, plus the by-beat list for SAME NIGHT).
- **Visual page:** https://claude.ai/artifact/5CwtCxEuZcX2shfYcfF96B (private). Source: `catalog-page.html` + `web/` (republish
  the same file to update). `index.html` is the local version that uses `shots/`.
- **Data:** `catalog.json` (merged, coded), `work/<code>/effects.json` (per-channel analysis), `shots/` (full-size frames).
- **Codes, stable by channel block:** FX-01–10 Johnny Harris · 11–20 MagnatesMedia · 21–30 LEMMiNO · 31–40 Patrick Cc: ·
  41–50 Dodford · 51–60 Coffeezilla · 61–70 Jon Bois · 71–80 JxmyHighroller.

How it was made: first 10 min of one video per channel, sampled every 2 s in the creator's Chrome (yt-dlp was blocked),
one sub-agent per channel named 10 techniques, then 4-frame strips at each move. Frames are reference only, never used in
an edit. Capture gotcha: Chrome won't read AV1 frames at 1080p (and sometimes 720p) into a canvas; drop to 720p/480p and
check frames differ. Rebuild: `python build_catalog.py && python build_page.py`.
