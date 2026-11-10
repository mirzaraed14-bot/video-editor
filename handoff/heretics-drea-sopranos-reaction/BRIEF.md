# heretics-drea-sopranos-reaction: Affan's reaction to Andrew Gold's Short "Are we all doomed?" + our Drea de Matteo sample (ABW10 "heretics reaction", batch 7)

## ▶ STATUS: resume here
- 2026-11-09 ≈23:05 PKT (builder): "heretics reaction" is PLACED AND LAID in ABW10 (bin "Onyx batch 7 reactions (2026-11-09)"), 176.700 s (2:56.7): layout (face head-lock + one eased 100->104 % push keys on every face clip, 143 clip edits, 0 leaks), window (+6 dB Amplify, -6 dBFS Hard Limiter), per-clip gains 111/111,
  captions + 27 MGs on V4/V5, 58 SFX on A2/A4 (3 plays from their FILES), bed on A3 ridden (176 keys), `apply --verify` 0 problems, `premcheck6` 0 failing, offline `claudecheck_h` 0, Premiere grabs of 30 times in work/grabs-sheet.jpg, offline proof sheets work/proof/sheet-*.jpg + head-*.jpg.
  PENDING (queued behind the Premiere lock as work/unface_full.sh, log work/unface_full.log): switch OFF his split FACE layer under the full-window channel page (V2 sits above V1: the grab at 91.5 showed the face under the page) and the V1 SCREEN pieces under every play / portal / page card (main 23:30: no raw-view flash at the card edges); the same two rules are in tools/apply_h.py for any re-layout.
  Then: `ACT_OVERRIDE="Sequence 49" bash tools/prem_h.sh projects/heretics-drea-sopranos-reaction check` for grabs, and `bash work/restore_active.sh "Sequence 49"` if the active sequence is not Sequence 49 (it was restored at 21:07 and after every phase).
  plan.json is FROZEN (never re-run build_plan.py without re-running audio_h + plays_h). Affan exports himself (exportAsMediaDirect never called).

## Inputs
OBS `raw/2026-11-09 15-12-12.mp4` (2560x1440 60 fps, 591.7 s), camera `X:\Recordings\Onyx\C1455.MP4`. Sync: dense-window run (40 windows,
`reactions/sync/sync-C1455-15-12-12.w40.json`): 6 of 39 windows are playback windows (+13..+52 ms); the robust line through the other 33 has
scatter 0.4 ms, camera = OBS + 72.1304 s - 26.1 ppm (72.1286 at 0 s, 72.1132 at 590 s); `sync-C1455-15-12-12.fit.json` holds the inlier windows and
is what seq.json points at (build_seq's line = +72.1223 s at 240 s, -26.1 ppm over 29 windows). No step in the offset.

## Deviations from the PLAN (§ Deviations)
1. K33 piece 487.79-490.75 ends on a stuttered first "it" (490.63-490.75) the PLAN text does not contain; it now ends on "edit" (490.15), then "it will go viral again" from 491.27.
2. Over the cap beyond the PLAN's drop list. With K21 + K29 out the real cut (WhisperX word edges + quietest-frame joints, tight pass at --th -41.7 as main asked) ran 186-189 s against the PLAN's predicted 2:55.5 (the prediction ignores in-word pauses
   and joint pads). The PLAN names only K21, K29 and then "because everyone in the US..." (already out) as droppable; I ALSO dropped K19 ("this whole discussion is very valuable ... starting from the start", beat 12 gone; beat 13 keeps its parked
   "THEIR SHORT" playhead) and tightened the pads (head <= 0.12 s, tail <= 0.10 s). MAIN: confirm or restore K19 (about 6 s) if the plays shorten the cut further. K12 (beat 8) and K24 stay.
3. Plays last as long as their FILES (xplay2 vs the OBS audio): K7 = 6.92 s (file 0 at OBS 76.539), K32 = 12.91 s (449.95), K35 = 6.90 s, not the PLAN's 9.74: in OBS the Instagram play stalled and seeked back (~3 s) so the PLAN's 515.16-524.90 span held about 3 s of replay;
   the IG file reaches "I never got paid" at file 6.87 s.
4. The face push-in (100 -> 104 %) is carried as `push: 4` on every face beat of plan.json; the shared apply has no face keyframes, a job-local copy bakes them in Phase B.

5. Beat 1: the hook tag leaves at the layout change (t = 5.48 s, the start of the split on "and he's been kind enough"), not on "permission" (7.2 s): the split puts his face in the bottom panel, where the card would sit on it.
6. Beat 3: the three credential chips sit in ONE ROW under the 600M card (a stack no longer fits between the card and y 1620).
7. Beat 11: the select (+ chip "MINIMAL · INSTAGRAM aesthetic") rings the Short's white caption line, not the player: the whole player cannot be shown in the 811 px panel without the Claude app, and the white title box is not on the Short's frame at OBS ~190-200.
8. Beat 14: the info modal with "18K Views" is on screen only OBS 335.2-336.7 (= "18,000 views"), so the ring + chip "THIS SHORT · 18K VIEWS" run those 0.6 s; the "895K subscribers" hl_sweep + ring run on the full-window channel page from the joint at OBS 342.5.
9. Beat 21: the live screen during K33 (OBS 475-492) is NOT the Instagram page (it is our sample in a player, then the Short page with the Claude app). The Instagram Reels page is a HELD FRAME of OBS 256 (crop x 1280-2196, y 180-1390; the $500 Reel reads 634K views, the tile is ringed) shown full-window by the job-local `page_still` kind, with his live face inset (`inset_cam`) over it.
10. Scorecard header reads THEIRS / OUR SAMPLE (job patch over kinds7); every play card tag reads "OUR SAMPLE ..." as the PLAN says (NEW-KINDS says "OUR EDIT").
11. `claudecheck.py` (batch 6) flags every frame where the app is anywhere in the OBS frame; here the app is on screen for most of the recording and every split view is cropped right of OBS x 1230 (asserted in build_plan.py), so the proof is `tools/claudecheck_h.py` (view-crop check + the full-window pages measured against the reference).

## Downloads (Epidemic Sound MCP DownloadSoundEffect, WAV, each < 0.9 MB, curl'd into `sfx/src/`; chosen by title / tags / duration, never by ear)
| file | Epidemic id + title | for |
|---|---|---|
| paper-slide | 6a2298cb Paper, Friction, Sheet, Laminated, Slide On Wooden Table | card / scene entrances |
| env-slide | a5da9fbb Paper, Friction, Envelope, Slide | letter card |
| tap-a / tap-b | 72a7ed45 Finger Tap Knock 02 / 82e590f1 Finger Tap Knock 01 | chips, rows |
| marker-a / marker-b | 86c26fdb Marker Pen Draw Line 02 / e55a339f Marker Pen Scribble Short | hl_sweep, select, rings |
| pen-stroke | 36b4db51 Crayon, Draw Straight Line On Paper 02 | path draw |
| ratchet-a / ratchet-b | e209a3d9 Toy Ratchet Wind 06 / 0ce87ad7 Toy Ratchet Wind 03 | count-ups |
| tape-a / tape-b | 098c6a7d Hi Fi Play Button Press / 091c1e6f Plastic Power Button Press | play cards |
| cloth-a / cloth-b | ec69ae2b Cloth Shorts Throw / a431e734 Swish Short Swing Branch | low cards |
| glass | 4b3cd12d Food & Drink, Glassware, Single Glass Clink (replaces a UI-class "ping" that the premium-SFX rule bans; the first download was deleted) | the reveal ping (beat 7) |
| card-slide | 863f9a1a Playing Cards Hand Slide On Table | tile row, twin cards |
| felt-tick | bf593c47 Calculator Press Button Single 02 | glows / lights |
| paper-lift | b7510777 Paper Airplane Pick Up 02 | lifts |
| knock-soft | 6f53c05f Doors Knock Thin Wood | row close |
| page-turn | 051477d3 Magazine Glossy Page Turn 06 | full-screen pages |
| block / blockb | d8443e7e Wood, Impact, Wooden Block, Small, Place Down On Others (+3 semitones twin) | brighter wood taps (tap-a/b measured -6.7/-8.7 dB in the phone band) |
| air-pass | 3eb43b90 Designed Whoosh Soft Resonant | portal |
| fold | da896266 Paper Handle Sheet Fold 04 | letter fold |
Bed (chosen by main, `reactions/BEDS-b7.md`): `audio/ES_Slow Food - Yellowbase.wav` (not downloaded here).

## Levels (measured offline by tools/audio_h.py = audio6 + the plays from their FILES, work/audio-report.txt, mix work/mix.wav; never played)
- Voice: 111 A1 clips, each its own Amplify (clipgain6) so its loud words hit -6 dBFS into the -6 dBFS Hard Limiter; talk gains median +5.7 dB (clip range -0.3..+11.7); talk -15.8 LUFS;
  70 % of 400 ms talk windows and 100 % of the 50 three-second talk windows peak within 1 dB of -6 dBFS (none outside). The three plays come from their FILES on A2 (sfx/play-k7 / play-yt / play-ig.wav,
  gains -2.45 / -3.81 / -3.77 dB, held <= talk + 2 LU); the OBS clips under them are muted (clip gain -96 dB).
- Bed: "Slow Food" (Yellowbase) at -13.1 dB = 8 LU under his talk, ridden +-4 dB (174 keys): 3 s windows min 5.1 / P10 7.0 / median 8.1 / P90 9.0 / max 13.8 LU under the voice (the 5.1-5.6 LU windows are 26.5-26.8 s: the
  Short's own loud intro under the K7 play card). NO bed ducking (main 21:20): the first audio pass used 17 bed notches (deepest 7 dB); they were deleted and the SFX palette rebuilt instead.
- SFX: 58 cues, 12 sounds from a pool of the sounds whose loudest 50 ms sits within ~14 dB of their peak (fold / ratchet / felt-tick / tape / paper-lift / page-turn / paper-slide measured -17..-22 dB and cannot clear the bed with a -8.5 dBFS peak cap);
  EVERY non-play cue's loudest 50 ms clears the bed in that window by >= 6.0 dB (min 6.0), peaks <= -8.5 dBFS (>= 2.5 dB under his -6 peaks); families card-slide 19 %, knock 19 %, stroke 19 %, taps 19 %, swishes 17 %; never the same sound twice in a row.
  Whooshes/air: cloth-a x7, cloth-b x3, air-pass x1 = 19 %. Weakness: knock-soft is used 11 times (19 %) because the gate leaves few sounds that can pass.
- Mix: -15.2 LUFS integrated, -1.2 dBTP.
