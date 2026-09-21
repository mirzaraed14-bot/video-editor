# Abundance Wisdom — LESSONS

One entry per thing a job taught. Newest first. Numbers belong in [README.md](README.md),
procedure in [PLAYBOOK.md](PLAYBOOK.md).

## 2026-09-21 — transitions by block label (comp 06)

- **The signalling rule the creator chose:** label the block, and the label is the transition that
  comes AFTER it. One colour per block, each cut owned by the block before it. It removes the
  ambiguity of labelling pairs. Yellow stays zoom-out; a marker is the escape hatch for a block that
  needs both. → README § 7.
- **Use their own .ffx where the shape matches, and say when it does not.**
  `Simple Brightness Fade In & Out.ffx` and `Music Media Co Uni Expose.ffx` were applied, then
  retimed onto the cut. Their `Gaussian Blur Preset.ffx` ramps UP then down, which is not the
  50 → 0 they asked for, so that one is built directly — and that difference is worth stating
  rather than silently substituting.
- **The cut is where the NEXT block starts, not where this one ends.** They nudge blocks, so block 13
  ended at 31.333 while block 14 began at 31.233; the visible cut is the later layer's in-point.
- **Skip the creator's own annotation layers** (a text layer named `*after his death*`, label 1 Red)
  when walking blocks — they are not shots and their label is not part of the map.
- **Shell gotcha:** writing docs through `python -c` inside bash silently ate every backticked span
  (command substitution). Write markdown with the file tools, not through a shell string.

## 2026-09-21 — creator's review of the first scripted zoom pass (comp 06)

Diffed my 15 zooms against what they left. **9 kept untouched, 4 depths tuned, 2 shots re-timed,
1 curve reshaped.** Nothing was deleted and no layer was re-built by hand.

- **Every one of the 7 face pivots survived unchanged** (y665, 577, 664, 587, 613, 520, 344).
  The `zoom_center.py` rule and the y200 threshold are **validated** — keep them.
- **Depth tweaks, all within ±0.10 of my value:**

  | shot | span | mine | theirs | direction of the fix |
  |---|---|---|---|---|
  | 11.77 | 1.37 s | 0.78 | **0.85** | shallower — they treat ~1.4 s as a TINY block |
  | 13.13 | 3.00 s | 0.70 | **0.80** | shallower — a 3 s shot is not automatically a deep push |
  | 19.57 | 1.73 s | 0.78 | **0.73** | deeper |
  | 21.30 | 6.98 s | 0.70 | **0.67** | deeper — confirms 5 s+ goes past 0.70 (their measured median 0.68) |

  → **Bucket edges to use next time:** tiny (≤ ~1.4 s) 0.85–0.87 · standard 0.78 ·
  long 3–5 s 0.70–0.80 · very long (5 s+) **0.67**. The spread on the 3–5 s band means length alone
  does not decide it; ask, or leave 0.70 and expect a tune.
- **Two shot boundaries nudged** (6.02 → 6.00, and the pull-out 31.33 → 31.23, 0.1 s earlier).
  Zoom spans are theirs to fine-tune; do not re-derive them from the footage layers after their pass.
- **The final shot's curve was reshaped** to a much harder front-load (10 % of the time covering 46 %
  of the move, 88 % by half, versus my 34/60). Candidate rule, one instance only: **the last shot of a
  short lands faster than the house curve.** Watch for it on the next job before making it a rule.
- Everything else kept my curve exactly (0.34 / 0.60 / 0.80 at 10/50/90 %).

## 2026-09-21 — first scripted zoom pass (ABW6 Linked Comp 06)

- **Direction comes from the creator's labels, not from Claude's judgement:** AE label 2 (yellow) =
  pull out, default = push in. They label the footage before handing the comp over. → PLAYBOOK.
- **Two ExtendScript traps, both silent:** `moveAfter` throws "cannot move a layer before or after
  itself" when the new layer is already at that index (it aborted the first run with a modal on the
  creator's screen), and **nested `?:` is evaluated LEFT-associatively**, which collapsed every
  depth bucket to one value — the run "succeeded" and was wrong. Print the derived numbers in the
  script's own log and read them before declaring success.
- **Verify a curve by sampling it, not by trusting the eases you set:** re-sampled all 15 applied
  moves and compared against the 108-move house curve — worst deviation 0.022 of the move distance.

## 2026-09-21 — BlurMoCurves, measured across all 121 instances (9 shorts)

- **Two of my earlier "rules" were coincidences of one short and are now retracted:**
  direction alternating shot to shot (really 45 % = chance) and size continuity across a cut
  (really 29 %). Never generalise a craft rule from a single video — n=12 looked convincing and was wrong.
- **Center XY is off-centre 45 % of the time** (x always 540, y median 699, range 83–851): the zoom is
  aimed up into the face. The reference short happened to be all-centre, which hid this.
- **The curve is the signature, and it is not "easy ease":** 35 % of the distance in the first 10 % of
  the time, a long drift, then 18 % in the last 10 %. Verified by sampling the real value through 108
  moves rather than reading keyframe handles — **ease speed/influence numbers were misleading**
  (departure speed reads 44x the average rate, which means nothing until you sample the curve).
- **My earlier interpolation readout said HOLD on every key; it is BEZIER (6613).** Print the raw
  enum number, never a mapped label, when a readback looks impossible.
- **13 of 121 instances do not move at all** — Z Dist parked at 1.00 or 0.80. The effect doubles as a
  static size hold, so "has BlurMoCurves" does not mean "has a zoom".
- Depth scales with shot length (0.19 under 1.5 s → 0.32 over 5 s), and a push-in always departs from
  exactly 1.00. → README § 3.

## 2026-09-21 — per-word caption colour is NOT scriptable in Premiere

- Probed an upgraded caption graphic on the creator's own timeline: its `Text` component
  (`AE.ADBE Text`) exposes only `Source Text` (an opaque blob) plus transform params — **no fill
  colour, no character-range styling**. Opacity/Motion/Vector Motion are settable; the type is not.
- So on the editable route the creator colours the emphasis words by hand. Claude's job is to make
  that pass fast: `caption-colours.md` lists clip number, timecode, the caption, the exact word and
  the creator's own style name, and repeats it grouped by style.
- **The only path to scripted colour is a .mogrt** that exposes a colour swatch (or a separate
  emphasis-text field); the template is authored once by hand in AE/Premiere, then
  `getMGTComponent()` params are settable per instance.

## 2026-09-21 — a rendered caption layer cannot take the creator's preset

- **The mistake:** I delivered captions as a .mov. The creator's "Revised Light pop" is a Premiere
  preset that only applies to graphics, so a video layer locks them out of their own animation.
  **Ask what the caption layer has to accept downstream before choosing its format.**
- **The editable route that works on Premiere 25.0:**
  1. `make_srt.py` writes an `.srt` (text, timings, `<i>` on the other speaker's lines).
  2. `importFiles` the .srt, then **`seq.createCaptionTrack(item, 0)`** — or the bridge's
     `create_caption_track` with `sequenceId` + `projectItemId`. (`seq.captionTracks` does NOT exist
     on 25.0: probing it throws, which is what killed the first attempt.)
  3. In Premiere: **Upgrade Captions To Graphics** (confirmed present in this build's menu strings)
     turns the track into editable text graphics; select all → text style → drop the preset on.
- **There is no caption READ API**, so a created track cannot be verified by script — say so instead
  of claiming it landed.
- **Trade-off to state plainly:** the rendered layer carries the per-word gradients automatically;
  the editable route needs those ~20 emphasis words coloured by hand (cheat-sheet generated by
  `make_srt.py`). Per-word colour cannot be scripted in Premiere.

## 2026-09-21 — creator's first caption review (Sequence 22)

Six corrections, all now rules:

- **No punctuation except `?` and `!`.** No commas, no full stops. (My first pass carried both.)
- **Sensitive words are censored, not avoided:** `sex` → **S*X**.
- **Pink means love, affection AND women** — hence S*X pink (it is about affection here, not shock),
  LISA MARIE pink ("she was a woman"), KITCHEN pink. Pink is wider than "tenderness". → README § 8.
- **Emphasis colouring is per phrase, by feel:** DAY TO DAY yellow, WAKING UP yellow,
  SOMEBODY blue in "sleeping with somebody". Colour the phrase that carries the beat, not just nouns.
- **The pop was wrong and it shows.** My eased 8 % curve read as a different animation. Measured the
  creator's export frame by frame: a steady climb toward the preset's 112 % (+1.6 % @0.05 s,
  +5.3 % @0.20 s, +9.0 % @0.60 s). `build.py` now interpolates the measured table.
  **Measure the creator's own frames before modelling any animation — the nominal preset values lie.**
- **Open:** a literal application of their Premiere preset is only possible on native text graphics,
  which scripting cannot create. A rendered layer must imitate the curve.

## 2026-09-20 — first captions job (ABW6 · Sequence 22, Lisa Marie / MJ)

- **The caption tooling now exists:** `build.py` (renders the layer) + `make_plan.py`
  (captions.txt + words.json → plan, validating every word against the transcript). Job:
  `projects/lisa-marie-mj/`.
- **Calibration beats guessing:** two caption widths measured off the creator's own export
  ("YOU SHOULD NOT SAY" = 634 px, "REALLY DON'T KNOW" = 603 px) plus the 39 px cap height solve to
  **Gretaros size 52, tracking −0.5**. Rendered strings then landed within 2 px of theirs.
- **Their white captions are flat white**; only the emphasis words carry a gradient (top → bottom,
  darker at top). Sampled stops are in README § 8.
- **Bug found and fixed: per-character tracking must draw on ONE baseline** (`anchor='ls'`).
  Drawing each character with `anchor='lt'` floated every comma and full stop up to cap height,
  so they read as apostrophes. Always QA a frame with punctuation.
- **The deliverable is a black-background .mov**, exactly like their own Premiere caption export, so
  it feeds CapCut directly and skips one export. On the timeline it needs blend mode Screen to preview.
- **Scripted import worked this session** (contrary to the 2026-09-18 note): `importFiles` +
  `overwriteClip` onto the first empty video track, verified by readback.

## 2026-09-20 — teardown of the "Wacko Jacko" short (ABW6 / Sequence 11 → ABW7 / ABW6 Linked Comp 03)

- **Lesson: the zoom is a Sapphire Z-space move, not a scale keyframe.** Every shot gets its own
  adjustment layer with `S_BlurMoCurves`, Z Dist animated across the *entire* shot with
  pop-then-settle easing. → Recorded as README § 3. Never animate layer Scale for the push.
- **Lesson: zoom size is continuous across a cut.** A pull-out starts at the value the previous
  push-in ended on (0.80 → 0.79, 0.84 → 0.69). → README § 3. A zoom that restarts at 1 every shot
  reads as wrong.
- **Lesson: the "complete" letterbox is one mask plus a 198 % / 43 % twin.** The same mask on both
  copies works because masks scale with the layer. → README § 4.
- **Lesson: the glow bar is a 1 %-tall white solid precomp**, glowed with Deep Glow (Unmult),
  bevelled, and double drop-shadowed; it is placed on the mask edge (offset +592 px from layer centre).
  → README § 5.
- **Lesson: the grade is one preset file, not a stack to rebuild.** Four of the nine effects hide
  their settings from scripting (Looks, Curves, Hue/Sat channels, Sapphire), but that is irrelevant:
  the creator's own method is "new adjustment layer, drag `Affan CC Preset` on", and that `.ffx`
  was verified to contain all nine effects. `applyPreset()` reproduces it exactly.
  → README § 6. *(Corrected the same day: the first note said to duplicate their layer — unnecessary.)*
  **Generalise it:** before concluding something can't be scripted, ask the creator how they actually
  do it; a saved preset beats reverse-engineering values.
- **Lesson: two-line captions are two graphics on two tracks**, not one two-line text block; the
  second line sits 59 px below. → README § 8.
- **Lesson: italic marks the other speaker.** The interviewer's questions are italic, the subject's
  answers upright; non-speech is italic inside asterisks. This was invisible in the earlier
  export-only analysis. → README § 8.
- **Lesson: the caption "pop" is a slow ~7 % growth across each caption's life**, not a snap on entry.
  → README § 8.
- **Lesson: the channel's loudness has tightened.** Older shorts ranged −20 to −11.6 LUFS; this one
  is −15.3 LUFS / −1.4 dBTP. Treat −15.3 as the current target until told otherwise.
- **Lesson: the opening can be an ElevenLabs voiceover**, not only source audio (voice
  "Christopher – Gentle and Trustworthy", first 5.57 s), carrying the same Studio Reverb as the speech.
- **Lesson: AE scripting quirks.** `-r` forwards to the running instance, but the script path must be
  unquoted inside the PowerShell ArgumentList array, and a heavy dump can take minutes — chunk it and
  poll for a result file.

### Second pass, same day — gaps closed

- **Lesson: a short is TWO AE comps, not one.** Comp 1 is the head lock, rendered out and sent to
  Topaz; comp 2 is the build. The `_stab_` in `<job>_stab_chr2_iris3.mov` marks the first stage.
  → README § 10.
- **Lesson: the head lock is baked as per-frame Anchor Point keyframes** (linear, one per frame) on a
  heavily scaled layer (≈ 546 %), with **Motion Tile** (Output Height 340, Mirror Edges) covering the
  exposed edges. Earlier note said "write Position keyframes" — wrong property, and it missed Motion
  Tile. → README § 10, PLAYBOOK § 2.
- **Lesson: the "Revised Light pop" is readable** in `Effect Presets and Custom Items.prfpset`
  (Premiere profile folder): Vector Motion Scale 100 → 105 → 112 % over 0.367 s, with the text rising
  0.5 → 0.448 of frame height. No need to eyeball it. → README § 8.
- **Lesson: bar shadows and caption shadows differ** — Distance 5 on the glow bars, 12 on the caption
  precomp. Same two-shadow stack otherwise.
- **Lesson: caption colours are saved Premiere Text Styles**, not per-word fills — Gretaros,
  Gretaris Italic, Red Shade Greators, Pink Shade, Light Blue Shade, Orange Yellow Shade, Green Shade.
  Apply the style by name and the gradient, shadow and weight come with it. → README § 8.
- **Lesson: only three mask bands are ever used** in the reference short: y 440–1484 (h 1044),
  452–1468 (h 1016) and 504–1412 (h 908), with the fill twin at 198 % (217 % / 221 % on two shots).

### Open questions from this teardown (ask before replicating)

1. **The 36-piece speed pattern on the render track.** The finished render is re-imported, sliced into
   36 pieces on a 2-second grid, with speeds alternating **1.0 / 0.99** and the first 0.1 s at **0.7**.
   What is this for — music sync, a retime, or platform-side handling? Claude has not replicated it.
2. **The speech stem naming** `<job>-esv2-27p-bg-10p-music-10p.mp3` — which tool produces it, and do
   the percentages need setting per job?
3. **Music level.** Every clip sits at default gain, so the balance is baked into the stem. How is the
   music level actually set?
4. **Grade sections.** The grade is split into 6 spans with slightly different sharpening
   (BCC Unsharp Amount 17 vs 7, Unsharp Mask on/off). Is that per source-clip quality, by eye, or a rule?
