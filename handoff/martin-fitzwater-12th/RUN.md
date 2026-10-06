# RUN — martin-fitzwater-12th (ABW8 · Sequence 30, AE ABW9.aep comps 50 + 52)

## ▶ STATUS: resume here
**2026-10-06: HEAD LOCK applied (comp 50 L1–L2, comp 52 L1; proven, worst drift 0.002 px) + CAPTIONS on Sequence 30
(72 captions, max 3 words, seen on screen). Neither project saved (the creator saves).**
Waiting on the creator: **comp 50 L3 (6.22–7.13, src 643.15) and L4 (7.13–12.82, src 1206.75) sit at Scale 100 =
letterboxed** (1920×1080 press-conference footage in the 1080×1920 comp): left unlocked (PLAYBOOK § 2 step 6: Motion
Tile would fill the bands) — lock as is, or fill the frame and lock?
Not asked: comp 51 (finals, 255 %).

**2026-10-06: ZOOM PASS (BlurMoCurves) on ABW8 Linked Comp 54** (Topaz render `martin_stab_chr2_iris3_prob4.mov`, 20
blocks, 4 yellow = pull out incl. the 7.2 s Instagram-comment block at 0.67): 20 `Adjustment Layer 29` zooms on top,
Z read back as planned, fresh dump: every block has an exact zoom span. 10 face pivots + 1 side pivot
(`zoom/centers.override.json`: block 12, the man in the cap, x200). Checked full frames for blocks 1, 7 (Martin + Nick
side by side: both faces stay in), 16 (Nick's turn: face in). Note: blocks 14–20 sit at startTime −1.467 (a frame
grab must add 1.467 s). AE not saved.

**2026-10-06: TRANSITIONS on Comp 54** from the creator's labels (`transitions/transitions54.jsx`, log `.txt`): 19 made
(8 Dark Green +30, 4 Purple −90, 4 Peach exposure, 2 Cyan blur, 1 Pink flash; block 20 Aqua = none, last), each read
back at its keys, laid under the caption precomp. AE not saved.

**2026-10-06: CAPCUT CAPTION RETURN CLEANED** — `Caption Exports/martin2.mp4` (in "martin2.mp4 Comp 1" → Comp 54 L1)
→ `martin2_clean.mp4`: 733 frames repaired (26 static frames, one every 2 s, ~35–45 % of the frame; 707 faint 1-frame
specks ≤ 2.4 %); verified on raw luma: no pixel above Y 40 zeroed, no caption pixel (Y > 60) changed. Footage #674
re-pointed in place (`captions/capcut/martin2_replace.jsx`, undo "Clean CapCut caption export (Claude)"): size / fps /
duration and the precomp layer in/out MATCH; caption precomp still the top layer. AE not saved.

## Format / lane
Abundance Wisdom short, 9:16 60 fps. The creator sequenced it (Sequence 30, 0–53.32 s; clips parked after 121 s are
not part of the short). Preset `presets/youtube-shorts/abundance-wisdom/`.

## Head lock (`headlock/`)
read_comps5052.jsx → `ae_comps5052.txt` → `live5052.txt` (3 layers) → `track.json` → `track_sheet.jpg` (dot on the
face: the press-conference speaker, the man in the cap, Nick) → `headlock5052.jsx` (541 Anchor keys + Motion Tile,
undo "Head lock (Claude)") → `headlock_read.json` → drift ≤ 0.002 px.

## Captions (`captions/`)
`sequence-captions.py read` (A1 only, no VO) → reference trimmed to 53.317 s → WhisperX → `transcript/words.json`.
`_fixes`: "I wouldn't start as blocking" → "I went as far as blocking" (decoded from the uncut press-conference source;
the cut at 24.617 joins the words). "Nick responds and says very" is right: Nick's Instagram reply on screen reads "very".
`captions.txt` → `make_plan.py --hang 0.8` → `make_srt.py … seq30-captions` → import. Italic = the fan comment and the
reply the commentator quotes; commentators and Nick upright; 21 of 72 coloured; "bullshit" as spoken (Seq 22 precedent).
