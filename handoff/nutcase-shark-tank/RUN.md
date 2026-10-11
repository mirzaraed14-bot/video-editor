# RUN — nutcase-shark-tank (ABW9.aep comps 55–59: Steven Bartlett / Nutcase, Shark Tank)

## ▶ STATUS: resume here
**2026-10-10: HEAD LOCK applied — 38 layers across ABW8 Linked Comp 55–59 (2,847 Anchor keys + Motion Tile 340/mirror,
undo "Head lock (Claude)"), proven from AE's read-back anchors (`headlock/headlock_proof_*.jpg`: every LOCK row holds the
nose). ABW9 NOT saved (the creator saves).**
Waiting on the creator:
- **Comp 55 L2** (1.27–3.65, src 197.9) sits at **Scale 100 = letterboxed**: left unlocked (PLAYBOOK § 2 step 6) — lock as
  is, or fill the frame and lock?
- **Comp 57 L1** (0–1.57): Steven's nose sits at x ≈ 1100 for most of the clip, i.e. just RIGHT of the 1080 crop (face
  half out). Locked as framed; the lock is Position-independent, so sliding the layer left keeps it locked.
- **Big swings** (Motion Tile mirror will show at the edges on the extremes): comp 55 L8 (the laughing hoodie guy, y
  −328..+271 comp px), comp 56 L1 (y −274), comp 56 L2 (x −520..237), comp 57 L1 (y +260), comp 59 L4 (x up to +400).
- **Speaker leaves the frame**: comp 56 L2 from frame 118 (≈3.47 s) and comp 59 L4 from frame 100 (≈5.33 s) laugh their
  way out of shot: the lock follows them until then and HOLDS from there (`track.json` `held_from`; raw track in
  `track_raw.json`), so the frame doesn't chase a face that is leaving.

**2026-10-10: CAPCUT CAPTION RETURN CLEANED** — `Caption Exports/seek 2.mp4` (in "seek 2.mp4 Comp 1" → Comp 60 L1)
→ `seek 2_clean.mp4`: 771 of 3494 frames repaired (30 static frames, one every 2 s, ~38–43 % of the frame; 741 faint
1-frame specks ≤ 2.3 %), `captions/capcut/clean.log`. Verified on 16 cleaned frames: caption pixels (Y > 60) unchanged
(≤ 3 levels, ≤ 2 px per frame). Footage #1083 re-pointed in place (`captions/capcut/seek2_replace.jsx`, undo "Clean
CapCut caption export (Claude)"): size / fps / duration and the precomp layer in/out MATCH. AE not saved.

**2026-10-10: TRANSITIONS on Comp 60** from his labels (`transitions/transitions60.jsx`, log `.txt`; labels read fresh in
`transitions/labels60.tsv`): 33 made (12 Dark Green +30, 9 Purple −90, 8 Cyan blur, 4 Peach exposure), each read back.
No transition: blocks 13, 21, 33 (Aqua) and 4, 27, 36, 37 (still YELLOW from the zoom pass: not a transition colour,
flagged to him); 41 = last. His caption precomp "seek 2.mp4 Comp 1" (disabled) is now the top layer; he also added 3
grade layers (Adjustment Layer 32). AE not saved.

**2026-10-10: ZOOM PASS (BlurMoCurves) on ABW8 Linked Comp 60** (his Topaz render `seek topaz_4_stab_chr2_iris3.mov`,
41 blocks, 14 yellow = pull out): 41 `Adjustment Layer 29` zooms with S_BlurMoCurves, 16 face pivots, read back as
planned (start / mid / end Z), fresh dump: exactly one zoom per footage block, all above the footage. Preview
`zoom/zoom-preview.jpg` checked block by block (23, 25, 27 = product shots, centred). Layer 16 (the letterboxed shot) is
his own 126 % fill. No caption layer in the comp yet, so the zooms sit on top. ABW9 NOT saved.

**2026-10-10: CAPTIONS on ABW8 Sequence 40** (= this short): 87 captions, max 3 words, imported as caption track C1
("Subtitle"), seen on screen in the Program monitor. ABW8 NOT saved. Next on the creator: Upgrade Captions To Graphics
→ styles from `captions/caption-colours.md` → "Revised Light pop" → caption export → CapCut → clean.
Flagged: "I'M WELL AWARE OF MY FRIEND" (5.1–6.2 s): both decodes (cut and uncut source) hear these words, "of" at ~0 %
confidence. Italic = the founders (Jess, Ninja), upright = the sharks — say the word and it flips.
Not captioned: the clips parked at 66.15–84.03 s after the 7.75 s gap (not part of the short).

## Captions (`captions/`)
`sequence-captions.py read … "Sequence 40" --voice A1,A2` (A2 carries the 29.0–32.1 s speech) → reference trimmed to
58.4 s (the full read kept in `brief/parked/`) → WhisperX → `transcript/words.json`, `_fixes`: "For children" → "Four
children" and "That case" → "Nutcase" (both decoded from the uncut source 58–88 s) → `captions.txt` (speakers from the
shot list: who is on screen per comp layer) → `make_plan.py --hang 0.8` → `make_srt.py … seq40-captions` → import.
22 of 87 coloured; median 0.58 s (fast talkers; min 0.24 s).

## Head lock (`headlock/`)
read_comps5559.jsx → `ae_comps5559.txt` (39 layers, one source: "Steven Bartlett Grills Entrepreneurs Behind Nutcase!")
→ `live5559.txt` (38 layers; comp 55 L2 skipped) → `head_track.py` → `track.json` (0 missed frames) → `track_sheet.jpg` +
`track_detail.jpg` (clips 9, 14, 19, 21, 27 at 8 frames) → `headlock5559.jsx` → `headlock5559.txt` (all 38 keyed) →
`headlock_read.jsx` / `.json` → `headlock_proof.jpg`. Note: `headlock_proof.py jsx` needs ABSOLUTE paths (a relative
OUT makes AE write next to its own exe).
