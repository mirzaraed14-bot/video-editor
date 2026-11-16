# @affanwizu two-layer captions (TEST tooling, 2026-11-16)

Urdu script (Noto Nastaliq Urdu) over Roman Urdu, gold, soft glow: the new strategy measured in
`research/affanwizu-bilingual-captions/REFERENCE.md`. Not the locked deliverable yet; the Roman .srt still ships with every job.

1. `captions.txt` as always (Roman, `build.py ... --srt`), then `captions.ur.txt`: one Urdu-script line per Roman cue, same `@time`,
   his English spelled in Urdu letters, nothing translated, quotes on the same lines.
2. `node render_cues.mjs <job> <job>/work/bilingual/A '<json params>'` → one transparent PNG per cue (headless Chrome, HarfBuzz shapes Nastaliq).
3. `python assemble.py <job> <cue dir> <job>/outputs/<name>.bilingual.mp4` (burned preview) and `... <name>.bilingual.mov --alpha`
   (transparent layer for V2 at 00:00).

Params used on ABW11 Seq 09/10 (footage band y420-1500, chin median ~y1100): `{"urSize":72,"urBase":1328,"roBase":1420,"bandY":1100,"bandH":420,
"glow":"0 0 3px rgba(255,215,0,0.4), 0 0 16px rgba(255,215,0,0.85), 0 0 28px rgba(255,200,0,0.5)"}`; variant B adds
`"roFont":"Times New Roman","roWeight":400`; variant C adds `"shadow":"3px 4px 3px rgba(0,0,0,0.55)"`.
