# stop-remaking-viral-shorts: AffanWiz Short 4 "Stop Remaking Viral Shorts" (Scott Clary YouTube format)

## ▶ STATUS: resume here
2026-11-09 21:44: **CHECK v7 DELIVERED (replaces v6 and v4), waiting for his review.** `X:\Claude Projects\Exports\affanwiz-stop-remaking-viral-shorts.check.mp4` (+ `.check.proof.jpg`, `affanwiz-stop-remaking-viral-shorts.thumbnail.jpg`); job copy `outputs/stop-remaking-viral-shorts.sample-yt.v7.mp4`. 1080x1920, native 59.94 (2636 f, 43.98 s), Topaz face shots, POP grade + sharpen, green theme. v6 fixed the review round's grid overlap, the label in the top band and the cut-off thumbnail words; v7 fixes the turn card's muddy "TRANSFORM IT A LOT" phase (one clean re-crop) and is otherwise frame-identical to v6, audio byte-identical. If he approves, this file IS the final (no Chronos needed).
- **His call pending:** v7's turn-card crop has the source creator's SPEEDZYY watermark interpolated out (recipe to put it back: RUN.md Next action).
- Gates and the rebuild recipe: `RUN.md` (§ Gates on the delivered check, Next action). Sequence v1 approved ("Yes, build it"). Prediction locked (RESULTS row 4, Claude 3K-35K; his still blank). Nothing committed, nothing uploaded.
- NOT verified: nobody has watched or heard it at real speed (no playback here); the edit-review fresh-eyes subagent rounds were not run (usage lean); the output-level dandruff detector proved invalid (it flags hair highlights), so the dandruff proof is source-level + full-size crops.

## The ask (Affan, voice-dictated, 2026-11-09, relayed by the English Editor session)
1. "There's a little speck of dandruff in my hair, so if you could do any little editing trick to remove it that would be good."
2. "Just improve the editing overall by 1 %, that's what our rule is."
3. "For the theme today let's do green instead of yellow: captions and motion graphics green, and green gradients."

## Channel / format / job (stated for a one-word correction)
- **AffanWiz**, Short 4. Unscripted: no `creator-shorts/CA-*` script, GTA script or Short idea matches; the Skool sign is behind him and the topic is Shorts craft.
- **Short**, 9:16, code-built in the Scott Clary YouTube kit (AffanWiz ENGINE § line 3), like Short 3.
- **Job:** `projects/stop-remaking-viral-shorts`. **Title:** Stop Remaking Viral Shorts (4 words, 26 chars, his own words).
- **Topic overlap:** Short 1 (`reupload-wont-go-viral`) is the same family (re-UPLOADS). This one is about REMAKING someone's viral Short, and its receipts are built, not Short 1's.

## Per-video overrides (this Short only)
- **GREEN replaces yellow/gold** everywhere: caption emphasis voice (spec `captions.palette`), hook key word (`hook.grad`), MG accents and gradients (job-local card code, never the kit), the cover's coloured word. The kit's locked yellow stays untouched.
- **Profanity:** "the f***" starred on screen and muted in the voice (Short 1's default, recipe 4).

## Sequencing v1 (raw source times; his words only)
`SEQUENCE.md` (sent 2026-11-09). Prediction locked: AffanWiz RESULTS row 4, Claude 3K–35K (Affan's still blank).

## Dandruff speck (ask 1)
- One white fleck, ~4 x 3 px at 1080p, in the front hair above his right eye. Top-hat 100-140 vs hair Y ~40.
- **Track:** `work/speck/` = `faces.py` (YuNet every frame) → `detect.py` v2 (hair zone of the face + dark-ring test: the fleck's ring9 p90 ≤ ~55, hair-edge gaps and glints 150-235) → linked track `track_det.json`: **6620 of 7170 frames**, 3.65-114.31 s, gaps ≤ 3 frames, 5 small steps. Verified by eye on 28 crops across the take (`scratch track_v4.jpg`): on the fleck every time. v1 (no face zone) had latched onto the sunglasses hinge at 80-101 s.
- **Fastest head moves:** ≈ 30.5 s and ≈ 74.0 s, 16-18 px per frame.
- **Fix (`work/speck/clean.py`):** YUV planes of every raw frame, only a small ROI touched, lossless H.264 qp 0 → `work/speck/C1454.clean.mov` (outside `raw/`; cuts.json will point at it by absolute path). Fill = soft average of 8 donors 24 px around the fleck, level-matched, glint/level gates as continuous weights, clamped to ring −18/+14, mask = capsule stretched along the head's motion. Two earlier fills were dropped: the plain clamp left a flat plug at 8x; a single cloned donor left a dark smudge (f4822-4826) when it landed in shadow.
- **Gotcha (cost an hour of nothing):** ffmpeg range-converts EVERY pixel when the rawvideo input is untagged and the output is tagged bt709/tv; tag the input identically.
- **Proof on the fastest kept span (f4680-4920, 78.1-82.1 s, face shot 6, 16 px/frame at 80.16 s):** 0 pixels changed outside the patch box (`verify.py`); fleck top-hat 102 → 10 (hair texture 20-45); patch frame-to-frame change 1.02 vs the hair ring 1.76 (ratio 0.58, 0 of 240 frames over 2x: `flicker.py`); the worst six frames at 6x viewed clean; three frames of the graded + sharpened 9:16 viewed clean.
- **Proof files (`work/speck/proof/`):** `speck-full-before.png` / `speck-full-after.png` (1920x1080, f4810), `speck-zoom4x-f4810.png`, `speck-zoom-stills.jpg`, `speck-zoom-realspeed.mp4` (4x crop following the fleck, before | after, 59.94 fps, silent), `speck-916-realspeed.mp4` (9:16 at the Short's framing, POP-ish grade + the Short's sharpen, 59.94 fps, silent).

## Reading (sunglasses take)
`workflows/eye-line.py` on the raw: Otsu 0.292, separation 4.13 SD (reliable), 36 s reading, mostly in the gaps the cut removes. Yaw only; the build gate uses `work/speck/faces.json` (every frame, yaw AND pitch, speech-only calibration), covers until yaw is back at camera level.

## Catalog pass (CLAUDE.md learning loop): `CATALOG.md` read in full, all 137 stills in `shots/` viewed on 4 contact sheets (2026-11-09)
- **Fits this video:** FX-41 Year Ghost ("so 2024"), FX-18 Karaoke Leader Quote + FX-56 CRT Witness TV (the beginner's complaint) with the CRT power-off on "No!", FX-34 Read-Along Highlighter (YouTube's post, green), FX-25 Exhibit Grid (original vs YOURS), FX-38 Hard Push Slide between MG scenes, FX-81 stepped motion (not here: Shorts stay smooth).
- **Not yet used on this channel:** all of the above (`presets/youtube-shorts/affanwiz/UPGRADES.md` lists what Shorts 1-3 used).
- **What the last videos leaned on:** Short 3 = one level-bar object + FX-69/70/71; Short 1 = FX-54/55 on the same YouTube post + slaps; Scott = photo cards on a blurred plate (radar: rest them).
- **Considered, not used:** FX-13 Depth-Sandwich (KILLED on seated close-ups), FX-11 Rival Colour Split (no rivals), FX-43 Tape Morph (no then/now).

## The 1 %: what this one does better than Short 3 (the last of its kind)
1. **A scene per beat instead of one object:** five built worlds (scan-and-copy, 2024 ghost, CRT quote + power-off, exhibit grid, frame-breaking bar), each new to the channel.
2. **A comic beat built into the cut:** the CRT power-off lands his "No!", the H3 register (talking AT beginners) with a laugh, not a lecture.
3. **To-scale numbers:** the 100x bar is drawn to scale and breaks the frame, rather than a number card.
4. **Dandruff removed** (his ask) and **green theme** for this one video.
5. Carried over, not re-learned: POP grade aimed per room + sharpen, drift on every face shot, head tracking, no face jump cut under 0.3 s, captions from frame 1 with the hook below.
- **Research pass still owed before the build:** current best Shorts-about-Shorts (silent storyboard-frame method, `research/longform-style-radar.md`), dated into `research/shorts-style-radar.md`.

## Build (2026-11-09, after his "Yes, build it")
- **Cut:** `work/cut/make_edl.py` → 23 segments, 43.98 s, 2636 f at 59.94, spliced from the cleaned take (abs path in cuts.json); the caption transcript is derived through an identical EDL naming `C1454.MP4` (`work/cut/cuts.snapped.rawname.json`), because words.json is keyed to the raw name. Both verbatim passes on the cut read clean; they settled the ending: "That will be pushed 100 times more". The inaudible "The" was dropped from the captions.
- **Research pass 2** (`research/shorts-style-radar.md`, 2026-11-09): the niche's hits are 7-12 s single ideas; green is the niche's growth colour (vidIQ, SpactYT).
- **Scenes:** two Sonnet builders, briefed with the toolkit `yt/cardkit.py` (green palette, safe zones, motion rules), then reviewed by me frame by frame. Fixed at review:
  1. the 2024 card was a cropped still of his face → a same-camera jump/whip and no A grade: replaced by the kit's own `fx: freeze` on his face shot + `yt/ghost.py` (dim, scanlines, vignette, the green 2024 slam, a 4-frame jitter + RGB fringe) in the overlay;
  2. the COPY printed in the card's last 0.1 s → prints on "recreate", whole by ~4.46 s;
  3. the COPY chip's guard was later than its rise → fixed;
  4. post: tags drawn onto a cached frame left trails (a doubled check) → drawn on a copy;
  5. bars: a 190 px camera tilt pushed the labels into the caption band → 30 px (the 100x bar still breaks the frame top);
  6. v1 captions all green (I had overridden the kit's white "main" voice) → only the emphasis voice is green.
- **SFX:** v1 cue_check read every swish WEAK on a phone (-21..-28 dB phone band) → each re-levelled from its own reading to -18.5 dB phone band (`PHONE_V1` in build_spec).
- **Grade:** Short 3's room-tuned POP (`grade_look`), tested on 3 stills first: cheek hue 19-24, sat .34-.38 (real skin, no orange), p5 8-12, p95 226. Cards excluded from grade and sharpen.
- **Topaz Iris 2x** (`--no-stab --no-fi`, native 59.94) on the base: 3840x2160, 2636 f; no watermark on the frames checked.
- **Second speck** found on the v3 check (output frame 1640): a much fainter particle ~60 px from the first. Pass 2 = `work/speck/track2.py` (offset from the main fleck in face units, refined to its own top-hat peak, 7-frame median) + `clean.py` with SPECK_R0=4.0 on the pass-1 take. Window test: 0 px outside the box, top-hat 24 → 10, ratio 0.59.
- **Cover:** `work/cover.py` → the grid scene's real picture (90M original lit, YOURS dim) + STOP REMAKING / VIRAL SHORTS, REMAKING green.
