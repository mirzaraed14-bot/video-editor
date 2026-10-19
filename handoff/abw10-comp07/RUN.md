# ABW10 Linked Comp 07 — Katherine Jackson × Paris Jackson short

## ▶ STATUS: resume here (2026-10-18)
- **Head lock DONE in ABW9** (`E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\ABW9.aep`), undo group
  "Head lock (Claude)". **ABW9 NOT saved: Affan saves.**
- **Caption export DONE: `E:\Shorts\Abudance Wisdom Shorts Exports\Caption Exports\katherine-paris.mov`** (H.264
  1080×1920 60 fps + PCM stereo = the clean A1 dialogue, 36.53 s). `paris.mov` already existed there (older job), untouched.
- Next: whatever Affan calls (zoom pass / transitions / caps clean on his CapCut return, recipes in
  `presets/youtube-shorts/abundance-wisdom/SESSION-START.md`).

## Caption export (ABW10 Sequence 07, 0–36.53 s = the sequence out-point)
- Sequence 07 = V1 Comp 05 (0–4.45) · V2 Katherine (4.45–7.85) · V1 Comp 06 (7.85–19.83) · V2 Katherine (19.83–23.10) ·
  V1 Comp 07 (23.10–36.53). Parked Paris clips at 42.1–50.6 are past the out-point: not captioned.
- A1 (17 clips, `seqref/a_clips.txt`) rebuilt to `seqref/a1.wav`, transcribed (`seqref/transcript/words.json`).
- Speakers by voiceprint (lab-notes 2026-10-03 recipe): 0–7.85 = **Katherine** (0.86) although the reporter is on screen
  at 0–1.5; 23.10–25.97 Katherine (0.70) under the reporter cutaway; only 7.85–11.37 is the reporter → italic.
- Mishear: Paris 33.0 s "and off" dropped from captions + `captions/flat/transcript/words.json` (second passes: "and" /
  nothing). "A big stare" confirmed.
- 53 captions, 8 stacked, 19 coloured, `captions/captions.txt`; plan `make_plan.py captions/flat --hang 1.0`; sheet
  `captions/caps_sheet.jpg` checked.

## Comp
ABW10 Linked Comp 07, 1080×1920, 60 fps, 13.43 s, 6 layers, all label 3 (lock), Scale 192, no keys before the lock.

| L | Source | Comp time | Speaker |
|---|---|---|---|
| 1 | Katherine Jackson … 60 Minutes Australia.mp4 | 0.00–2.87 | interviewer (blonde) |
| 2–4 | same | 2.87–7.08 | Katherine Jackson |
| 5–6 | Paris Jackson … Zane Lowe Interview.mp4 | 7.08–13.43 | Paris (L5 starts in profile, turns to ¾) |

## Head lock (PLAYBOOK § 2)
- `headlock/read_comp07.jsx` → `ae_comp07.txt` → `live07.txt` + `headlock_map.json` (tl_offset 0, in-points = tl_start).
- `head_track.py`: 0 missed frames on all 6. `track_sheet.jpg`: dot on the speaker's nose everywhere (`track_paris.jpg`
  = the two Paris rows enlarged).
- `apply_headlock.py` (hold median) → `headlock07.jsx`: 806 Anchor Point keys, Motion Tile on all 6, tile width 100.
  Biggest travel L5 x −112..88 comp px, L4 x −47..140.
- `headlock_proof.jpg`: every LOCK row holds the nose on the crosshair.
- Proof artefact, not a defect: L1's last proof tile (2.85 s) shows the next shot. The source cut is at 2255.7201 s and
  AE's last frame reads 2255.7167 s (the interviewer), only 0.1 source frame before it. Moving L1's out-point
  later by one frame WOULD flash the next shot.
