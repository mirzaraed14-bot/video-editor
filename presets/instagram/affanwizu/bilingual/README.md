# @affanwizu two-layer captions (TEST tooling, 2026-11-16)

Urdu script (Noto Nastaliq Urdu) over Roman Urdu, gold, soft glow: the new strategy measured in
`research/affanwizu-bilingual-captions/REFERENCE.md`. Not the locked deliverable yet; the Roman .srt still ships with every job.
**Scope (his call 2026-11-17): talks only.** A funny video keeps the normal single-line yellow .srt ("this is a funny video so it wont suit").

1. `captions.txt` as always (Roman, `build.py ... --srt`), then `captions.ur.txt`: one Urdu-script line per Roman cue, same `@time`,
   his English spelled in Urdu letters, nothing translated, quotes on the same lines.
2. `node render_cues.mjs <job> <job>/work/bilingual/A '<json params>'` → one transparent PNG per cue (headless Chrome, HarfBuzz shapes Nastaliq).
3. `python linfix.py <cue dir> <cue dir>_lin <job>`: Premiere composites in LINEAR colour, which makes a soft glow ~3x
   stronger than any browser/ffmpeg preview (2026-11-16, "too glowy"); this remaps each pixel's alpha so Premiere shows the
   preview's look. The .mov is built from the `_lin` dir, the burned preview from the unfixed dir.
4. `python assemble.py <job> <cue dir> <job>/outputs/<name>.bilingual-preview.mp4` (burned preview, unfixed cues) and
   `python assemble.py <job> <cue dir>_lin <job>/outputs/<name>.bilingual-layer.mov --alpha` (transparent layer for V2 at 00:00).

Params used on ABW11 Seq 09/10 (footage band y420-1500, chin median ~y1100): `{"urSize":72,"urBase":1328,"roBase":1420,"bandY":1100,"bandH":420,
"glow":"0 0 3px rgba(255,215,0,0.4), 0 0 16px rgba(255,215,0,0.85), 0 0 28px rgba(255,200,0,0.5)"}`; variant B adds
`"roFont":"Times New Roman","roWeight":400`; variant C adds `"shadow":"3px 4px 3px rgba(0,0,0,0.55)"`.

**Current look (his notes 2026-11-16 on Seq 10, v2):** `{"urSize":48,"urBase":1346,"roBase":1420,"bandY":1100,"bandH":420,
"glow":"<same as above>","shadow":"3.75px 4.25px 1px rgba(0,0,0,1)","roCase":"uppercase"}`: Urdu small, Roman in ALL CAPS,
the yellow style's hard shadow drawn above the glow, then `linfix.py`. Place the Urdu baseline from measured ink (`"hide":"ro"` /
`"hide":"ur"` renders one line): max Urdu descent + 12 px above the caps top.
