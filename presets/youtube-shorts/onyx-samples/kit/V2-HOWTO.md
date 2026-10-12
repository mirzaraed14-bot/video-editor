# V2-HOWTO: the Instagram version of an existing cut, in the batch-2 "expensive" look

One page for a build agent. The look and its numbers: [README § v2 look](../README.md#v2-look-batch-2). The working example to copy:
`projects/_onyx-batch2-2026-10/kit-demo/ig/build_spec.py` (Rich Roll x Bryan Johnson, 46.5 s) and its render
`kit-demo/outputs/kit-demo.sample-ig.v2demo.mp4`. Everything v2 is opt-in through `"look": "v2"`; v1 jobs are untouched.

**Inputs** (made by the job's YouTube version; nothing is re-cut): `outputs/<job>.mp4` (the base cut), `outputs/<job>.transcript.json`,
`outputs/<job>.topaz-fi.mov` (the Topaz base), `transcript/cuts.json` (segment starts, for the camera ranges).
**Output:** `outputs/<job>.sample-ig.<version>.mp4` -> finalise as `outputs/<job>.sample-ig.final.mp4` + `X:\Claude Projects\Exports\<job>.ig.final.mp4`.

## 1. Write `ig/build_spec.py` -> `ig/spec.json`
Copy the demo's file and change the job paths. The keys that make it v2:
- `"look": "v2"`; `"frame"` only to change the window (default 1044 x 900 at x 18, y 510, radius 64; the 4:3 square variant is
  `{"x": 0, "y": 555, "w": 1080, "h": 810, "radius": 0}`).
- **Shots** as v1 (`A` / `B` / `FIT` / `SPLIT`, frame-exact on camera cuts), but every crop number is now IN THE WINDOW: `fx_out` 0.60-0.66
  puts the speaker on the right third and frees the window's left side for graphics; `fy_out` 0.37-0.42; `z0` 1.0-1.2 on a 4K close shot
  (the window shows the source at about 1:1), 2.0-2.6 to crop a wide camera onto one person (no stranger in frame). Same-camera shots
  stay ONE shot (no punch-ins). A `SPLIT`'s `split.seam` is in window px (default 450); the white seam line is drawn for you.
- **Faces:** `uv run presets/youtube-shorts/onyx-samples-youtube/kit/yt_faces.py projects/<job> --dir ig` (the spec's own shots), then
  `"faces": "ig/work/faces.json"`.
- **Captions:** `"captions": {"words": "outputs/<job>.transcript.json", "mode": "stack" | "word" | "line", "accent": "<show colour>",
  "chunks": [], "hl": [hero words], "cx": <mouth x when the face is off-centre>, "colors": {"loss": "#FF4D4D", "gain": "#3DDC84"},
  "drop": [...], "breaks": [camera cuts where the speaker changes]}`. `stack` for opinion / story, `word` (`"variant": "mono" | "wide"`)
  for fast talkers, `line` for calm ones or a split-heavy edit (`"on_seam": true` puts the line ON the seam for the whole video).
- **Bars:** `"hook": {"t0": 0.1, "t1": <= 3.0, "kicker": "WHO THIS IS", "lines": [2 short lines], "hl": [one word]}` (top bar) and
  `"credit": "Show · Guest", "credit_t0": 3.0` (bottom bar). No CTA, no Onyx branding.
- **Cards** (`ig_v2.py` docstring has every key): `lower3` · `neon` (a number that re-rolls: `value`/`value2`/`t2`, `lead2`) · `reticle`
  (`box` in canvas px, measured on a frame) · `route` (`"orient": "v"` = a timeline beside the head that grows node by node) · `widget`
  (`todo` / `list` / `progress` / `notify`) · `compare` (`"orient": "v"` beside the head, or `"rack": true` over the blurred picture) ·
  `wordscene` · `titlecard` · `leak` (scene changes only). Anchor every time to a word (`wt("word")`) or a cut, never typed by hand.
- **Audio:** `"audio": {"voice": "outputs/<job>.mp4", "bed": <the job's Epidemic bed>, "bed_under_lu": 13, "sfx_kit": "epidemic",
  "target_i": -13.0, "target_tp": -1.5}`. Every card brings its own sounds (README § v2 SFX map); whooshes are already 15-16 dB down.
  **The bed sits 12-14 LU under the voice (Affan's voice-first rule, 2026-10-08): `bed_under_lu` 13.** (The first v2 builds used 17 and
  QA round 2 flagged every one, 2026-10-12.) Glass ticks peak ~8 dB under the voice peak, and every graphic gets a crisp audible cue of
  its own: a whoosh alone reads as no sound.

## 2. Plan the graphics against the layout (the numbers that keep it premium)
- **Zones:** the face (right third) · the caption line (constant, just under the lips: ig_capy prints it) · Z1 = the window's left
  side ABOVE the caption line (x 78-520, y ~570-990): lower3, neon, compact widgets, the vertical route, the vertical compare ·
  full-window scenes (titlecard, wordscene, racked compare) <= 3 s each, <= 25 % of the runtime, >= 1.5 s of face between two ·
  the top bar only for the hook (and, once, a big neon number) · the bottom bar only for the credit.
- **Density:** 3-4 designed events per 10 s at least (the demo runs 7); the first graphic by ~3 s, the guest's name by ~6 s.
- **Words, not repeats:** a card adds what the captions do not (a name, a number, an object, a list item); the captions run the whole video.
- **Edges:** a full-window scene starts and ends ON a cut or on a word; the report flags an edge 1-3 frames off a cut.

## 3. Build, check, iterate
```
python projects/<job>/ig/build_spec.py
python presets/youtube-shorts/onyx-samples/kit/ig_build.py projects/<job> v1 --preview
python presets/youtube-shorts/onyx-samples/kit/ig_qa.py projects/<job> outputs/<job>.sample-ig.v1.mp4 --sheet
```
`ig_build` prints the caption line (`ig_capy (v2): CONSTANT caption top …`, plus any shot whose lips sit under it: raise that shot's
`fy_out`), cards crossing the caption band, and the density report. The window render (4K, ~5 min) is cached: a card / caption / sound
change re-runs only the finish, the overlay and the mix (`--skip picture` skips even the finish). Iterate the overlay alone with
`cd ig/hf-overlay && npx --yes hyperframes@0.8.16 snapshot . --at 4.5,9.7,… --no-end -o ../work/snaps`.
`ig_qa` must say `RESULT: PASS` (decode, loudness, every word once, only ! ? and quotes, one caption y inside the window, a sound on
every designed event); then look at `ig/work/qa-sheet.jpg` frame by frame (faces never covered, nothing in the top 200 / bottom 300 px
but black, no text over the mouth). Fix and re-render, cap 3 rounds. Then copy the final as in "Output" above and write the BRIEF.
