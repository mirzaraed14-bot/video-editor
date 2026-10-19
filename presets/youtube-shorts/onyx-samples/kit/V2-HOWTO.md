# V2-HOWTO: the Instagram version of an existing cut, in the batch-2 "expensive" look

One page for a build agent. The look and its numbers: [README § v2 look](../README.md#v2-look-batch-2). The working example to copy:
`projects/_onyx-batch2-2026-10/kit-demo/ig/build_spec.py` (Rich Roll x Bryan Johnson, 46.5 s) and its render
`kit-demo/outputs/kit-demo.sample-ig.v2demo.mp4`. Everything v2 is opt-in through `"look": "v2"`; v1 jobs are untouched.

**Inputs** (made by the job's YouTube version; nothing is re-cut): `outputs/<job>.mp4` (the base cut), `outputs/<job>.transcript.json`,
`outputs/<job>.topaz-fi.mov` (the Topaz base), `transcript/cuts.json` (segment starts, for the camera ranges).
**Output:** `outputs/<job>.sample-ig.<version>.mp4` -> finalise as `outputs/<job>.sample-ig.final.mp4` + `X:\Claude Projects\Exports\<job>.ig.final.mp4`.

**Batch 3 (2026-10-14): read § 4 first.** The kit gained a frame per show (`square`, `void`), the dim-to-lit caption reveal, the hero
diet, a story meter in the bottom bar, the ghost cut-out, chapter cards, a lower-third that returns, bar zones, and three QA gates
(restating cards, slot repeats, leaks). All opt-in: a batch-2 spec renders as before. **No batch-3 sample may repeat batch 2's default
(window + stack + leak-heavy)**: § 4 has the variety rule and the keys.

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
  the top bar for the hook (and, once, a big neon number) · the bottom bar for the credit · batch 3: the bars also carry a lower-third and the story meter (`zone`, § 4), so they hold content on purpose, not 26 px of credit for 90 % of the runtime.
- **Density:** 3-4 designed events per 10 s at least (the demo runs 7), spread evenly (batch 2 swung 2 -> 10 per window: bunched cards, then dead air); the first graphic by ~3 s, the guest's name by ~6 s.
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

## 4. Batch 3: the upgrades (STYLE-RESEARCH § E, 2026-10-14)
Spec: `projects/_onyx-batch3-2026-10/STYLE-RESEARCH.md` § A2 (what read cheap in batch 2), § E (the ranked upgrades), § F (variety).
Demos (2026-10-14, session scratchpad `…/4f6ff510-…/scratchpad/kit-ig/`): `demo-square/` (Vivian Tu: square, stack + dim + hero diet,
top-bar lower-third + return, ghost, story meter, behind, chapter; `outputs/demo-square.sample-ig.demo3.mp4`, `SHEET-demo3.jpg`) and
`demo-void/` (Rob Dial's dark set: void, line + dim, word scene, meter, reticle, chapter; `outputs/demo-void.sample-ig.demo2.mp4`). Their
`ig/build_spec.py` show every key below in use; both pass `ig_qa`. Build time on this machine: ~15-17 min with a fresh 4K window render
(~7 min of it), ~10 min when the window render is cached.

**Variety rule (§ F).** Per prospect pick ONE frame and ONE caption mode; no frame + mode pair more than twice in the batch; never
batch 2's default (window + stack + leaks everywhere). Provisional: DSH square + `word` wide · SPI window + `line` · Moonshots void +
`stack` dim · Priestley square + `stack` dim · TFTC window + `word` mono · Wellness void + `line`. Each BRIEF names its hero card and
one line on what it does better than its closest batch-2 sample.

| Key | What it does (numbers) |
|---|---|
| `"frame": "square"` | 980 x 980 at x 50, y 470, r 40 (Chris Williamson, measured); bars 470 / 470; hook centre y 345, credit y 1540. |
| `"frame": "void"` | Full-bleed 1080 x 1920, no mask, no bars: the speaker's shots get `crush` (x^1.25, black pulled down 0.04: a dark set goes to pure black) + a 35 % vignette; B-roll keeps its grade. **Dark sets only** (a bright set goes grey). Hook default y 340, credit 1570, captions clamped to the safe band 200-1620. The shots frame exactly as the YouTube look's 9:16 (A at z0 >= 1: the face sits where the source puts it; plan the type in the set's dark space, often BELOW the face). Override: `"frame": {"preset": "void", "crush": {"gamma", "black", "kinds"}, "vignette": {"a", "r"}}`. |
| `captions.reveal: "dim"` | `stack` / `line`: the block lands at 40 % white (blur 3) in 0.12 s, each word lights to 100 % on its spoken time (0.10 s); a stack hero waits white and lights IN the accent; a line hero sweeps as it lights. Mark Brazil (554K). `word` has no dim stage. |
| `captions.hero_gap: 4.0` | The hero diet: <= 1 hero per 4 s, and no automatic hero (a block's hero = its `hl` word, else a number, else none; `"auto_hero": true` restores the longest-word fallback). Vivian's cut: 28 heroes -> 8. Keep `hl` to the 6-10 words that carry the story. |
| `"zone": "topbar" \| "bottombar"` | On `lower3` and the bar meter: park it in a bar (top = the hook's line, bottom = the credit's slot); it stays up under full-window scenes. Target: the top bar carries content >= 25 % of the runtime (hook + lower-third + its return gets ~20 %). |
| widget `"layout": "bar"` | STORY METER: `{"label": "Investing from age", "values": [[t, pct, "18"], [t, pct, "60"]], "w": 640, "zone": "bottombar"}`: a 6 px track draws on, the accent fill moves to each pct and the mono value re-rolls (0.45 s power2.inOut) ON the spoken number; the credit dips out under it. Park it 10-30 s for a number the story moves (age, money, count). Sound: glass + data blip per update, a thin thud on the last. |
| lower3 `"again": [t0, t1]` | The same lower-third returns in the last 30 % (2.5-3 s; Mark Brazil 3.5 s + 19.8 s). First show by ~3 s. |
| `ghost` | `{"src": photo / PNG / video + "src_t", "crop": [x0, y0, x1, y1], "h": 480-600, "side": "left", "opacity": 0.65, "mono": true, "scrim": 0.55, "fade_bottom": 0.35}`: the person NAMED fades in beside the speaker (opacity 0 -> 0.65, rise 20 px, blur 8 -> 0 in 0.5 s, 3 % drift, out 0.3 s), never over the face; hold 1.2-2.5 s. By default it STANDS ON the caption line (feet fading out just above it). `crop` cuts the person out of a busy frame first. Cut out locally (`npx hyperframes remove-background`, CPU, cached in `ig/work/ghost/`). Use the REAL person's photo, logged in BRIEF and checked at full size (the HQ-stills rule); never a stock stranger for a named person. Sound: rise-air cresting on the landing + thin thud. |
| `"behind": [...]` (top level) | `{"t0", "t1" (1.5-2.5 s), "text", "lead", "size": 120, "y": window px (default 0.22 x h), "x" (default AUTO), "hide": 0.25}`: ONE heavy-caps phrase (the hook or the payoff word) BEHIND the speaker: ig_window cuts a person matte from the window render (`hyperframes remove-background`, CPU, cached in `ig/work/behind/`), slides the word along its line until the speaker hides ~25 % of it, and composites picture -> shadow -> type -> speaker. Put `y` where the head is narrow (the crown: the build prints the hidden share). Sound: medium whoosh + low thud (ig_v2). Chris Williamson (620K). |
| `chapter` | `{"text": "#2" or one word, "kicker", "bg": accent, "wy"}`: the whole window turns to the show's colour, 0.6-0.9 s, hard in ON a cut; type 150 px Inter Black; a LIGHT accent (gold) becomes a deep tone of itself with the type in the accent, so the white captions running over the card stay readable (white on gold measured ~1.6:1 on the demo). The type centres at 36 % of the window's height, above the caption line. For list moments and a story's turn; counts in the 25 % full-window budget. Thin thud + soft whoosh. |
| `audio.bed_under_lu` | Default now 13 (was 18; every shipped spec sets it, so nothing changes). |

**Gates (ig_qa FAILs; ig_v2 prints them after the density lines):** `restate` = a card may not print > 50 % of the words the captions
on screen with it say (Vivian's todo was 86 %; a neon's big spoken number is exempt, its lead / tail lines count) · `slots` = no more
than 2 side cards in a row in one slot (top-left, low-right, a bar, docked to an object…; batch 2 put 17 of 24 at the top-left) ·
`leaks` <= 2 per video, on real source changes only (batch 2: 4-7) · `top bar` share is a NOTE (target >= 25 %). Run on every batch-2
sample they FAIL exactly where the research said they read cheap.
