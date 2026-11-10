# onthatnote-john-legend-reaction: Affan's reaction to our On That Note samples (ABW10 "On That Note reaction", batch 7, v2 standard)

## ▶ STATUS: resume here
- 2026-11-09 23:10 (polish): (1) the 27.00 view was a STALE grab (grab-0027.00.png dated 19:26): the live V1 piece 24.817-28.817 is one clip at scale 230, fresh grabs 26.0/26.5/27.0/27.5/28.0 are one zoomed panel, hl sweep lined up. (2) score-r2 -> `score-r3` (kindsotn `big`: card w 960, copy Inter Bold 43 = cap 31 px, numbers 54 = cap 39, labels Inter SB 34 = cap 25, THEIRS/OURS Bebas 46 = cap 33). (3) letter-r3 -> `letter-r4` (sub Inter 34 = cap 25, TO: Bebas 44 = cap 31; seal still right of the name). Both swapped on V4 (swapmg.py, one importFiles each), ABW10 saved, length unchanged 175.667, verify 0, premcheck6 61/0, grabs + edge frames `work/s4/sheet.jpg`. plan.json = pre-polish plan with only these two graphics replaced (do NOT re-run build_plan without audio7 --write after it).
- 2026-11-09 22:40 (shift 3): RE-PLACED in ABW10 "On That Note reaction" (bin "Onyx batch 7 reactions (2026-11-09)"), **175.667 s (2:55.67)**, ABW10 saved, active sequence (Sequence 49) restored. Cut = two energy-checked joint trims (raw 369.367->369.417, 30.517->30.583; `work/endcheck-r2.txt`).
  Verify: `apply --verify` 0 problems (V5 A4, sfx A2 51 + A4 6); push + full view 0; clipgain6 96/96; bedride6 175/175 keys; premcheck6 56 files 0 failing; `claudecheck_o` 0 exposed (`work/claudecheck-r3.txt`); leakcheck 0 leaks; headlock sim worst residual 0.0 px, only 2 size flags (3.2 s, 170.7 s; allowed).
  Fix list -> evidence (grabs `work/grab-*.png`, sheets `work/s3/sheet0-5.jpg`, edge frames `work/s3/edge1.jpg`, `edge2.jpg`):
  1. 17b fan covers + type 156.48-164.87: DONE (sheet4; "BOTH VERSIONS / yours to UPLOAD" at 157.5, swap to "an APPRECIATION gift" by 160).
  2. Letter seal clear of the text: DONE (seal right of "On That Note"; sheet5). 3. SFX audibility: DONE, 53 cues min +6.3 dB over bed, peaks <= -8.5 dBFS (`work/audio-report.txt`).
  4. Joint proof: energy proof all joints + Whisper reads of joints 0-30 clean; GPU jointcheck `work/jointcheck.txt` (95 joints) read: no clipped word seen by eye (ASR noise only: "thrones", "organism").
  R2 description panel legible: DONE (sheet1 10.0-11.5, 26.0, 28.0). R3 strip below the player: DONE (sheet2 33.5/35.5). R7 first caption at 0.000: DONE (grab 0.00). R8 hook sub-lines: DONE. R9 EXTRA DETAILS branch: DONE (grab 88.0). R11 copy: DONE ("the setup / centered / the conversation").
  Face never bare > ~4 s: longest bare stretch 172.05-175.67 (3.6 s). First 5 s frame by frame every 0.5 s: sheet0.
  OPEN (reported to main): (a) ~2-3 frame near-bare face at 164.867-164.88 where the 17b exit ghost has faded and the letter card has not yet risen (edge1.jpg), and a near-bare 156.47-156.48 between the badge fade and the fan entrance: fix = overlap the letter rise with the fan exit (re-render letter-r3, sem queue); (b) mouse cursor visible inside screen views (e.g. 5.0-6.0, 11.5, 28.0) and 63 layout-check "gaps" = the crop_left strip (by design); (c) SFX tap-class (wood/block/felt) is ~33 % of cues by family, no single sound > 12 %; (d) `headjump.py` ignores the head lock and flags 21 cuts: use `headlock.py` sim (0 px) + Premiere edge grabs 16.07/16.08, 153.63/153.65, 168.42/168.43 (match).
  Run notes: audio7 --write must run AFTER build_plan (levels), `tools/premo.sh` phases added: redo2, fin, fin2, grabs; build_plan END = V1 end (a stray bed clip stretched it to 175.8).
  Re-place after any change: `premo.sh <job> redo` + `redo2`, build_plan, audio7 --write, `lay`/`fin`/`fin2`.

## Inputs
OBS `raw/2026-11-09 15-35-10.mp4` (2560x1440, 819.75 s; the reaction ENDS at OBS 383.22, everything after 384 ignored), camera `X:\Recordings\Onyx\C1458.MP4`
(1920x1080, 59.94 fps, covers OBS 0-396). Transcript `transcript/words.json` (WhisperX large-v3). Their Short `../_onyx-batch7-2026-11/_shorts/on-that-note.mp4`;
ours `X:\Claude Projects\Exports\onthatnote-john-legend.yt/.ig.final.mp4`. Bed `audio/ES_Dirty Treasure - Amber Spill.wav` (chosen by main).

## Play maps (xplay2, 2026-11-09; file t = OBS t - offset)
| Play | file | offset | OBS span used | file span |
|---|---|---|---|---|
| K6 their Short | on-that-note.mp4 | 82.80 | 87.99-94.53 | 5.19-11.73 |
| K12 ours YT | yt.final | 243.40 | 243.40-257.35 | 0.00-13.95 |
| K14 ours YT (family tree) | yt.final | 248.38 | 263.02-271.28 | 14.64-22.90 |
| K16 ours IG | ig.final | 291.54 (file 0-2.5 played at offset 290.08, then he re-sought: file 2.0 at OBS 293.54) | 293.70-302.86 (face window; OBS audio muted, file plays from 0) | 0.00-9.16 |

## Deviations from the PLAN
- K16: the PLAN's 10.5 s (OBS 290.11-300.65) includes a 1.0 s glitch where he re-sought the Instagram file (OBS 292.58-293.54, file 2.0-2.5 played twice). The play from the FILE
  is continuous: file 0.00 -> 9.16 ("...the background that I have."), so K16 is 9.16 s, not 10.5 s. Its OBS/face window is moved to 293.70-302.86 (after his 'This is the Instagram format' at 292.41-293.63) so his lips are silent while the file plays.
- Cut length 2:58.4 vs the PLAN's ~2:46 (see STATUS).

## Downloads (logged before pulling)
| File | Source | Size | For |
|---|---|---|---|
| `sfx/src/otn-*.wav` (24 Epidemic SFX, WAV, each < 1 MB, ~7 MB total; downloaded 2026-11-09 ~17:50 via MCP DownloadSoundEffect, signed URL -> `tools/dlsfx.py`) | a5da9fbb Paper Friction Envelope Slide (otn-env-slide) / 6a2298cb Laminated Sheet Slide On Wooden Table (otn-card-slide) / 595ad5e3 Playing Card Turn Over 02 (otn-card-turn) / df71d4c4 Playing Card Place Down 04 (otn-card-down) / 9f76f0f2 Marker Draw Line On Cardboard (otn-marker-1) / 86c26fdb Marker Draw Line 02 (otn-marker-2) / e55a339f Marker Scribble Short (otn-marker-3) / cfb5fe79 Wood Knock Single (otn-wood-1) / 82e590f1 Mirror Finger Tap (otn-tap-2) / 5ffb8ffb Gears Clicking Ticks 03 (otn-ticks-1) / 07ecbd97 Ticks 06 (otn-ticks-2) / 7db16d8b Scissors Cutting 04 (otn-snip-1) / 8486a8e4 Scissors 03 (otn-snip-2) / 098c6a7d Hi Fi Play Button Press (otn-play-1) / 9ddd898b Radio Button Click 01 (otn-play-2) / e3a84a74 Telephone Book Page Turn (otn-page-1) / bc53ff40 Diary Page Turn (otn-page-2) / 8a7d530f Notification Ping Gentle (otn-ping) / 4c432ee5 Heater Switch Click (otn-felt) / 5b12ff9d Playing Card Flick (otn-lift) / 96c562d5 Paper Sheet Fold 01 (otn-fold) / 3c4bcbd5 Envelope Flap (otn-flap) / c406a00b Designed Air Whoosh (otn-air) / 6f9c401c Pen Click 01 (otn-seal) | ~7 MB | the SFX set, chosen by title/duration/tags; measured (envelope, phone band) in `sfxprep6.py`, never by listening |

| `sfx/src/otn-block-1.wav`, `otn-block-2.wav` (2 Epidemic SFX, added after the first measurement: the finger tap otn-tap-2 read +/-4 dB over the bed in 50 ms = inaudible; replaced) | 8e42d60f Wooden Block Small Thin Light Down On Wood 02 / 8822307a Wooden Blocks Small Place Down | ~0.1 MB | tap / tick cues |

## Levels (measured offline by `tools/audio7.py`, `work/audio-report.txt`, mix `work/mix.wav`; a job copy of tools6r3/audio6.py)
- Voice: 96 A1 clips, each its OWN Amplify (clipgain6) so its loud words hit -6 dBFS into the -6 dBFS Hard Limiter; talk gains median +7.4 dB held within +-6 dB; talk -16.3 LUFS, 72 % of 400 ms talk windows peak within 1 dB of -6 dBFS.
- Plays (their Short K6, our samples K12/K14/K16) come from FILES on A2 (`sfx/play-p1..p4.wav`, level-matched to his talk through a -6 dBFS limiter: -16.9 / -16.6 / -17.0 / -16.8 LUFS vs talk -16.3, all peaks -6.0 dBFS); the OBS audio under the four play spans is MUTED (clip gain -96).
- Bed: "Dirty Treasure" (Amber Spill) from 0.064 s (music-onset.py), bed_db -15.8 dB = 8 LU under his talk, RIDDEN +-4 dB (173 keys, bedride6): 3 s windows (voice + plays) min 5.2 / P10 7.3 / median 8.0 / P90 8.7 / max 9.5 LU; the closest windows are 112.0 s (5.2) and 51.9 s (5.8).
- SFX: 48 cues, 24 sounds + 2 added blocks; 9 cues have their loudest 50 ms < 6 dB over the bed (weakest: 19.14 block +-1, 56.24 block +2.0, 21.46 page +2.5, 52.97 wood +2.7), capped by the peak rule against his -6 dBFS voice; none repeats back to back; the tap class is 27 % of cues.
- Mix: -15.7 LUFS integrated, -2.4 dBTP.

## Deviations from the PLAN (so far)
- Cut length 2:55.8 (PLAN predicted ~2:46): the pipeline's head/tail pads and natural gaps. Under the 3:00 cap by 4.2 s.
- K16 play is the continuous file 0-9.16 s (the PLAN's 10.5 s included a re-seek glitch); its face window is OBS 293.70-302.86.
- Beat 3: the gold rule + "my bread & butter" label arrive on "this is my" (0.2 s early) so the label holds 0.6 s before the cut to the channel page; beat 4 starts on the V1 cut at 21.55 ('Shawn Stockman has...').
- Beat 5: the FULL-title strip sits at the TOP of the top panel (the player leaves no free band below its title line at a readable zoom); pointer_tag + strip are sequenced (no overlap).
- Beat 9: HOOK / MIDDLE / PAYOFF labels sit INSIDE their bands (left of the outline they collided with the TANGENT branch).
- Beat 14: kinds7's portal plays B (the Instagram card) muted from file 0 instead of holding it paused.
- Beat 17-18 are ONE face piece (148.0-175.78, one push-in 104 %); K20-K21 (156.6-164.9 + the beat after the badge) stay bare face per the PLAN (face > 4 s without an overlay: flagged).
- The SFX set: 26 Epidemic sounds (BRIEF § Downloads); the weak finger tap was replaced by two wooden-block sounds after the first measurement.
- 2026-11-09 23:30 (polish-2, PAUSED, nothing fixed): Premiere paused by main (Affan closed ABW10). Stepped 36.33 and 42.88 edges (work/s5/b1.jpg): both clean (36.33 = intended screen->card dissolve). Alpha scan of overlays/mg: play-yt1 95.35, play-yt2 112.25, portal-ig 120.517, play-ig 126.333 enter from alpha 0 over ~10 frames on top of the raw screen = same show-through as 95.35. Fix ready, NOT applied: tools/screenoff.py + premo.sh phase screenoff (razor V1 at t0 and t0+0.25, disable the piece), args in work/screenoff.args.
