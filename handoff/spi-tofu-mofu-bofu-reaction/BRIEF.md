# spi-tofu-mofu-bofu-reaction: Affan's reaction to Pat Flynn's Short "TOFU, MOFU, BOFU" + our two samples (ABW10 "SPI reaction", batch 7)

## ▶ STATUS: resume here
- 2026-11-09 23:30 (FIX SHIFT, PAUSED by main at 23:24: Affan closed ABW10; no Premiere call since). Offline fixes DONE, placement of the fixes in ABW10 was verified once (verifyc 0, clipgain 97/97, bed 164/164, premcheck 63 files 0 failing, claudecheck 0) BEFORE the pause, but the project was closed afterwards: whether that placement was saved is UNKNOWN, so re-place on resume.
  RESUME (after main's "resume"): `bash tools/prem_lay.sh layout push` (push = tools/facepush2.py, cache work/headcache.json already built) ; `bash tools/prem_lay.sh overlays bed afade verify` ; then grabs (`work/grab-times.txt` + the head pairs below) and `uv run --with opencv-python-headless --with numpy python tools/headgrab.py x 2.63:2.67 77.94:77.98 94.48:94.52 114.41:114.45 151.23:151.27 151.33:151.37 157.18:157.22 158.96:159.00 161.03:161.07` (must print 0 over 12 px / 2 %). Never exportAsMediaDirect.
- Fix list (evidence in work/fix/, work/audio-report.txt, plan.json):
  1 hook sub-line: channel card rebuilt (name 54 / handle 42 / subs 42 px, two lines) -> overlays/mg/hook-tag-c.mov (tools/spikinds.py sprite_channel_card2; still work/fix/m3.jpg).
  2/R5 views 28.5-35.5: the page is a STILL of a cursor-free OBS frame (work/fix/page-still.png) through the same view geometry (kind page_still): title bar whole, caps ~39 px (the window cannot hold the face AND a >= 40 px title: Pat's chin is in frame), nothing under the player, no toolbar, no green strip; chip "THE title ITSELF" moved up onto clean shirt (chip_dy -130). page-a-c.mov.
  3 scorecard: kind score2: row copy 42 px (cap ~30), numbers Bebas 72, labels Bebas 46, headers 40. score-c.mov.
  4/R1 description panel: view info_z (OBS x 1766-2230, y 324-672), still work/fix/page-info.png: title whole with 28+ px air, text whole, stat row caps ~47 px, ends above the seam; ring-views = stroke only (box 1960,462,2034,512), the gold marker on 1.7K removed (strength 0). hl-views-c, ring-views-c.
  R2 dashes = the shutter entrance slits of the "pat" cards over his chest: entrance riseup on badge-pat / low-pat1 / low-pat2; badge sub-line 34 px (cap 25), name 40. pat-c.mov.
  R3 / 149.9-151 = the V1 page showing through the twin card's exit: twin-k14/k18 hold (stage out 0, no exit); the YT card itself comes from the export file. twin-k14-c, twin-k18-c.
  R4 78.05 = the play card's 0.2 s alpha ramp / shutter slits showed V1 (muted page + Shorts button column): every frame-track scene now sits on an OPAQUE dark panel for its whole length (tools/underlay_mov.py post-process: play-k5/k11b/k13/k15, mute2, portal-cap/ig, retitle, teasers -c; twin/score2 in render). tools/edgealpha.py: first 9 + last frames alpha 255 on all 16 scenes. The shutter's own slits remain (the entrance signature).
  R6 first caption chunk t0 = 0.000: overlays/captions-c.mov (list-c.txt), plan captions_file captions-c.mov.
  R7 sizes: hook 42, chips 40/34, eyebrow "A MESSAGE FOR PAT" 34 (cap 24), scorecard above.
  R9b no bed dips (tools/audio8.py, DIPS = {}), every cue by its own level: SFX bodies raised (tools/shape_sfx.py +8..+15 dB then a -1 dBFS limiter on weak transients, originals in sfx/pre-shape/); 55/55 cues >= +6.0 dB over the ridden bed (loudest 50 ms), peaks <= -8.7 dBFS (>= 2.5 dB under his -6), voice 100 % of 35 3-s windows within 1 dB of -6.
  R9c variety: 8 new Epidemic sounds (see Downloads, fix shift); largest family 18 % (slide 10, click 10 of 55), no sound twice in a row (tools/tally.py).
  R8 head jumps: MEASURED on the timeline BEFORE the fix (Premiere grabs, tools/headgrab.py): 2.65 dy +26; 77.97 size -3.9 %; 94.5 dx +13.5 / -2.3 %; 114.43 +16.4 %; 151.25 dx +14 / -6.4 %; 151.35 -14.1 %; 157.2 +8 %; 158.98 dx +14 / dy +12; 161.05 dx -12 / -8.5 %. Cause: the old lock read head size from eye-chin landmarks through his sunglasses (sd ~8 %). Fix BUILT, NOT YET PLACED: tools/facepush2.py (median of 5 frames, size = sqrt(face box), sd ~1 %, cache work/headcache.json).
- NOT DONE (paused): placing facepush2 + re-measure R8; Premiere grabs of the changed beats; proof sheet every 1.5 s after the re-place (offline sheet is the OLD one, work/proof/).

## Inputs
OBS `raw/2026-11-09 16-11-03.mp4` (358.45 s), camera `X:/Recordings/Onyx/C1460.MP4` (read-only) in TWO sync pieces:
pre `work/sync-C1460.pre.json` (22 windows OBS<200, offset 23.7231 -> 23.7192, -23.8 ppm, resid 0.28 ms) and post `work/sync-C1460.post.json`
(8 windows OBS>=230, 23.7891 -> 23.7872, -26.5 ppm). STEP +70 ms between OBS 217 and 225 (`work/stepscan.txt`: 3 s windows, lag 23.7191 at 216,
23.7893 at 226; OBS 218-224 is the sample playing = no usable camera audio). Split at OBS 219.0; K4 (ends 218.12) is pre, K14 (227.61+) post.
The dense run `work/sync-w40.json` has two contaminated mixed windows (184.5 outlier 23.7495, 207.45/215.11 read 23.789 although stepscan says 23.719): not used.

## Lip sync (camera C1460, two pieces)
Step +70.5 ms (23.7190 -> 23.7895 at OBS 219) lies in OBS 217-225 (stepscan.py, 3-4 s GCC-PHAT windows, peaks 20-33, residual 0.05 ms around each line; the dense 60 s windows of the w40 run
overlap the step and read 23.789 from OBS 207 on: not used). Per kept talk span the 3 s lag reads: K11 (178-191) 23.7200-23.7198 · K12 (196.6-198.8) 23.7196 · K4 (212-218) 23.7192-23.7191 (all PRE, line 23.7214 at 102 s,
-26.3 ppm) · K14 (227.6-240) 23.7893-23.7889 (POST, line 23.7876 at 266 s, -26.4 ppm). `tools/lipsync.py` (mouth frame-diff energy vs the OBS envelope) is too noisy to add anything (r 0.1-0.4).
`syndump.py` prints the two lines; Premiere in-points are proved by `--verify` later.

## Their Short / our samples: edges (slice ASR + envelope)
Their file gLydjgO_q6s: K5 = 0.00-8.20 (the "funnel." end, quiet 8.18), K11b = 40.32-43.28 ("And you're screaming ... a big problem."). Ours (YT/IG share one timeline): K13 = 0-6.07 (IG gap 6.02-6.09 after
"funnel."), K15 = 6.07-22.70 ("The creator ..." to "big problem.", pause 22.65-22.86; slice ASR: problem. 22.38-22.64, but 22.76), K17 (IG) = 0-6.07. The five OBS placeholders (silent watching) are
tools/plays.json; the play audio comes from the FILES (sfx/play-k*.wav, level-matched to his talk, baked into a -6 dBFS limiter).
43.47-45.23 slice ASR (faster-whisper large-v3, both prompts) and WhisperX hear "I make sure for my pages"; the word is 43.86-44.30 with a sh burst (hf +15 dB 44.02-44.10), a vowel and a faint fricative
tail 44.22-44.28 = "shorts": captioned SHORTS (a fix in plan.caption_fixes). FLAG FOR AFFAN/MAIN: if he said "sure" the caption is wrong.

## Levels (tools/audio7.py = audio6 + plays from files; work/audio-report.txt, mix work/mix.wav)
Voice: 97 A1 clips each its own Amplify, talk gains median +8.6 dB (clip range +2.6..+14.6, held +-6 dB), talk -16.0 LUFS, 69 % of 400 ms talk windows peak within 1 dB of -6 dBFS.
Plays (A2, from files): speech matched to his talk (gains -1.2/-2.3/-2.1/-2.6/-2.2 dB), peaks -6.0 dBFS. Bed "Staying Afloat" at -16.0 dB = -24.1 LUFS ST = 8 LU under his talk, RIDDEN +-4 dB (162 keys):
3 s windows min 4.8 / P10 7.1 / median 8.0 / P90 8.7 / max 9.5 LU (the 4.8 at 96.0 straddles their K11b play). SFX: 56 cues, 16 sounds; every cue's loudest 50 ms is >= +3 dB over the bed
(most +5..+13), peaks -8.5..-14.5 dBFS (>= 2.5 dB under his -6 peaks); whoosh-class = 3 (scroll air-a, portal air-b x1, portal-ig air-a). Mix -15.4 LUFS integrated, -2.0 dBTP.

## Review rules applied after main's 19:00 / 20:00 notes
Views: `crop` (tools/viewcrop.py) hides YouTube's guide sidebar and anything right of the player's button column; views zoomed onto the page text the beat is about (title_z = their title ~40 px caps, info_z = the 69 / 1.7K / Aug 6 row ~47 px).
Labels low (chips on their card moved to y 855/950, lab-best 925: off the top, off the face, above our caption line). THEIRS copy kind (title stack / his voice / a ManyChat thank-you; "NOT REALLY clicky" -> "THE title ITSELF"; "just TALKING" -> "talking TO CAMERA").
Face never bare > ~4 s: the PLAN left 5.2 s (K10) and 8.1 s (K11): three low cards built from the words (low-value "VALUE-BASED CONTENT", low-eat "WHILE YOU'RE eating?", low-will "BUT YOU will WATCH IT"). First caption chunk starts at 0.000.
Head jumps: 28 of 36 face cuts moved the head > 12 px / 2 % (tools/headjump.py, up to 200 px: he moves between takes): the face push is a HEAD LOCK (tools/facepush.py tracks the head at every 0.5 s key and at every clip end, keeps its size and the mouth on y915, then the 100->104 % push). Not re-measured after placement.
Every SFX cue >= 6 dB over the bed (hard gate): tools/audio7.py dips the bed (<= -9 dB, ~0.7 s) under weak cues, 19 dips, 55 cues, min +6.0; weak sounds (felt-tick, key ticks) swapped for tap-a / marker / ratchet; the typing ticks 9 -> 5.
Voice: 100 % of 35 3 s talk windows peak within 1 dB of -6 dBFS (69 % of 400 ms windows).

## Deviations from PLAN.md
1. K13/K15/K17/K11b/K5 durations from the files' own edges (K5 8.20 s not 10, K11b 2.97 s not ~4, K15 16.6 s not 14: it ends on "big problem." and starts on "The creator", never trimmed from its end); the cut is 2:45.1 not 2:40.
2. K12 beat: the scorecard rows are 0.30 s apart (the PLAN's 0.55 s cannot fit K12's 2.0 s) and the card does not hold into the play: K13's play_card replaces it on the V1 edge.
3. K4: two phone cards (teaser kind) side by side, not fanned +-5 deg; they exit with the stage on the V1 edge, not by a slide.
4. Beat 1: the gold underline sweep under "Pat Flynn's" is not built (no OBS box for a face-beat name); the tag itself is settled on frame 0 with entrance none.
5. Beat 5: the scroll gesture is a view anim (0.5 s inOutCubic from `title_up`), without motion blur (the views are Premiere Motion keys).
6. Beat 9: THEIR Short is not desaturated 60 % / dimmed 30 % (play_card has no such key); the chips "just TALKING" and "2:04" sit on the card's top edge.
7. Beat 9 cloth swish -> paper-slide (the PLAN caps the whoosh-class at the three portal/scroll cues).
8. Beat 17: the envelope flap/gold seal is not built: a title_card "TO: PAT FLYNN · Smart Passive Income" + the avatar stamp, with the env-slide / paper-fold sounds.
9. Face push-ins (100 -> 104 %) are keyed by tools/facepush.py (own code, with a head lock) because tools7/push7.py did not exist when I placed.
11. Graphics that overlap are grouped into one .mov (teasers, chips-talk2, pat, letterg) and the base scenes (plays, portals, retitle, twins, scorecard, hl sweeps) ride the frame track V3 (tools/apply_spi.py); chips/cards ride V4.
12. The typing ticks under the retitle are 5, not one per word (audibility gate).
10. The 'oh' (prob 0) after "samples I made", the 'uh' after "represent your brand" and "1.7 000" are dropped/merged in the captions (caption_fixes).

## Downloads (Epidemic Sound MCP DownloadSoundEffect WAV -> curl into sfx/src/, 2026-11-09 ~17:50; signed URLs live 5 min)
18 SFX, each < 0.65 MB: paper-slide 6a2298cb (Paper Friction Sheet Laminated Slide On Wooden Table) · card-slide-a 863f9a1a (Playing Cards Hand Slide On Table) ·
card-slide-b 91b5b50b (Paper Friction Sheet Large Laminated Slide 01) · env-slide a5da9fbb (Paper Friction Envelope Slide) · paper-fold 96c562d5 (Paper Handle Sheet Fold 01) ·
tap-a 331aefcd (Wood Impact Light Hit 01) · tap-b 2b0734c4 (Wooden Pole Hit Wood 03) · felt-tick ba460708 (Felt Tip Pen Lid Remove) · pen-tick 71924810 (Pen Down On Cardboard Sheet 02) ·
marker 86c26fdb (Marker Pen Draw Line On Cardboard Sheet 02) · tape-a 098c6a7d (Hi Fi Play Button Press) · tape-b 7345e5af (Hi Fi Cassette Tape Deck Close) ·
air-a c406a00b (Swooshes Whoosh Designed Generic Air) · air-b 073cf199 (Designed Whoosh Soft Airy) · cloth 79611651 (Cloth Flap Whoosh Soft Short Multiple) ·
ratchet e209a3d9 (Toy Ratchet Wind 06) · key-a f94a21b7 (Keyboard Laptop Key Press Single) · key-b a2cf063f (Keyboard Apple Magic Key Press 02).
The bed `audio/ES_Staying Afloat - Matt Large.wav` was downloaded by main (BEDS-b7.md).

## Downloads, fix shift (Epidemic Sound MCP DownloadSoundEffect WAV -> curl into sfx/src/, 2026-11-09 ~22:00)
8 SFX for variety (R9c): glass-a 416dc4d2 (Glass Tap Small Impact) · glass-b 3fd6ee42 (Glass Jar Hit Clink 02) · glass-c 6e6e14bd (Windows Knock Glass Pane Small Single) ·
click-a 19edc18a (UI Buttons Bubbly Option) · click-b 46216b97 (UI Buttons Confirm Dull) · card-flick 5b12ff9d (Playing Card Flick With Finger) ·
card-place df71d4c4 (Playing Card Single Place Down 04) · card-turn 595ad5e3 (Playing Card Turn Over On Table 02).
