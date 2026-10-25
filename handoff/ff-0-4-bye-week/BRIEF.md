# ff-0-4-bye-week: Onyx sample Short for The Fantasy Footballers (Andy Holloway, Jason Moore, Mike Wright) (batch 5)

## ▶ STATUS: resume here
- **YT 2026-10-24 11:37 UTC: YT FINAL RE-DELIVERED (59.94 fps), awaiting Affan's review.** `outputs/ff-0-4-bye-week.sample-yt.final.mp4`
  = `X:\Claude Projects\Exports\ff-0-4-bye-week.yt.final.mp4` (md5 75c6a92c..., byte-identical; H.264 High 1080x1920 59.94, 2572 f,
  42.91 s, AAC; decode clean; -12.1 LUFS, peak -2.1 dBFS, LRA 2.3; proof `outputs/...sample-yt.proof-sheet.jpg`). Built from v7 (v6 picture +
  the s09 split top static again): Chronos x2 per shot (+ jump cuts 355, 729) -> `yt/work/mg60.py` (1946 MG frames = the native 59.94 renders)
  -> `yt_build final --skip picture`. The 11:05 file was superseded by a pre-hand-back review (`yt/work/patch_r2.py`): mg08 / mg09 showed
  INVENTED scores (151.8-162.4, 147.0-149.2, 'lost by 2.2') on ANDY's real charity league labelled YOUR TEAM; now ANDY'S TEAM (AH) with only
  what he said (#2 / 2ND-HIGHEST vs #1 / HIGHEST SCORE; BIG SCORE; TOUGH LUCK; ANDY'S RECORD 0-2), so YOUR TEAM (the viewer's example) stays
  0-4 -> 2-4. Also: AS TOLD ON THE SHOW stays on through the trophy, s01 push x1.10, landing thuds on the s09 / s13 split entrances (49 cues).
  Jump cuts measured on the source eyes: 729 (split, static crop) ~7 px vertical, 355 (head-tracked A) ~9 px vertical / 23 px sideways (he turns).
  Whooshes stay 18 dB under the voice peak on purpose: ~9-11 dB under the ticks / thuds / cards that land the same entrances (~5-6 under the
  booms, which r1 asked to lower). Superseded 60p pictures kept: `yt/work/picture.whip59.v5*.mov`, `...v6-tracked.mov`.
  Taste calls for Affan: the invented generic team names (BIG GAME HUNTERS etc.), the EXAMPLE tag on the points card, the hook copy
  'THE FANTASY FOOTBALLERS / 0-4? DON'T PANIC-TRADE', the Tarantula bed.
- **YT 2026-10-24 ~10:50 UTC: v5 (29.97) = the reviewed cut; FINAL 59.94 IN PROGRESS.** v1-v4 QA (mine: sheets `yt/work/qa-v*.jpg`,
  cut-neighbourhood sheets, per-cue SFX levels) + ONE sonnet reviewer (r1, `yt/work/qa-r1/`): fixed L tiles over the scores (mg09), the
  JUGGERNAUT chip overflow (mg06), names touching BYE pills + the row swap overlap (mg13, opaque climbing row), the TRADE chip over a
  label (mg12), a 0-4 team now plays WEEK 5 (mg12; was "WK 7"), booms 3-4 dB down (their sub out-weighed three words), flap cues on the
  visible flap, split chins clear of the seam (fy_out 0.60), the Iris-garbled wall poster behind Mike painted out (base_inpaint), headers
  out of the top band, split-bottom MGs below the watermark and above y 1620. Kept by design: the whip's mirrored edge (the reference
  look), the s05 jump cut (head-tracked; he turns his head). Final = Chronos x2 per shot (+ the jump cuts 355, 729) → `yt/work/mg60.py`
  puts the NATIVE 59.94 MG frames back over the interpolated ones → `yt_build final --skip picture` at fps_out 59.94.
- **YT 2026-10-24 ~10:05 UTC: v1 DRAFT BUILDING (29.97 fps).** Plan = `yt/plan.py` (13 shots: 4 A, 3 SPLIT, 6 MG; every boundary a scene
  change), MGs = `yt/mg/build_mg.py` (9 HyperFrames comps at 59.94: mg02 standings, mg03 IN BETWEEN slider, mg04 record vs points, mg06
  week scores, mg08 week 1, mg09 week 2 + 0-2, mg10 split-flap 0-4 → 0-7 + trophy, mg12 bye grid + trade, mg13 standings 0-4 → 2-4;
  checked on event sheets `yt/work/mgcheck/`), spec = `yt/build_spec.py` (head-tracked A shots, zoomkeys ×1.07-1.18 landing in 0.6-0.9 s,
  captions on the seam y 1060, 70 chunks, cyan = the listener's question / yellow = Mike / red = Andy, name tags for Mike + Andy, 47 cues
  from a fresh Epidemic set, Tarantula drumless bed 13 LU under from 25 s). Next: v1 QA → fixes → sonnet reviewer → Chronos x2 with every
  joint → native-60 MG frames swapped in → final 59.94.
- **IG 2026-10-24 ~11:10 UTC: IG FINAL DELIVERED (neon-window look, 59.94 fps), awaiting Affan's review.**
  `outputs/ff-0-4-bye-week.sample-ig.final.mp4` = `X:\Claude Projects\Exports\ff-0-4-bye-week.ig.final.mp4` (md5 e2043577…, identical;
  H.264 High 1080x1920 60000/1001, 2572 f, 42.91 s, AAC 256k; decode clean; -12.2 LUFS, TP -2.6 dBTP; bed 13.5 LU under; 30 cues).
  `ig/qa.py` PASS (bars black, no strays, no camera run < 8 f, punctuation, every word once); `ig/motion_check.py` on the Chronos plate
  1.5 % near-zero steps (real 59.94). Shots: stage hook (the question IS the caption: 0-4? + two option chips) → the options slide to IN
  BETWEEN → RECORD 0-4 vs POINTS PER GAME 3RD (EXAMPLE TEAM) → Mike cam + tag → week bars (YOU 4th-most, L) → Andy cam + tag → WEEK 1 /
  WEEK 2 matchup cards with L badges → Andy cam: 0-2 → 0-4/0-5/0-6/0-7 + trophy ("AS TOLD ON THE SHOW") → bye grid (EXAMPLE) with the
  trade → Andy cam: YOUR RECORD 0-4 → 2-4 on "wins". Face never > ~1.8 s without an overlay (asserted in plan.py). One sonnet reviewer
  (defects only) fixed: TP -1.5 → -2.6, the record numerals grazing Andy's cap brim (188 px), the button push 1.16 → 1.12 (cap under the
  label), the card hit 30 ms off the burn's whoosh crest, EXAMPLE on the bars/bye-grid kickers. Kept on purpose: "2-4" (0-4 + his "a
  couple wins"), "'cause" (READY's settled reading). v1 draft kept: `outputs/…sample-ig.v1.mp4`.
  Better than the last IG (MATG, 10-23): 59.94 fps vs 48; the longest bare-face run ~1.8 s (asserted) vs MATG's up to 4.6 s; the record
  is ONE object in one spot across the second half (0-2 → 0-4…0-7 + trophy → 2-4); who's who proven on screen, not assumed. Measured, not
  fixed: Mike's jump cut at 11.85 s moves his eyes ~16 px (fixed frame per the War Dogs review).
- **IG 2026-10-24 ~09:45 UTC: IG BUILDING (neon-window look, IG builder; all files in `ig/`).** Everything anchored to WORDS in
  `ig/plan.py` (shots, framing, caption blocks, events, cues; build/sound/qa import it). Names → faces measured (voiceprint × mouth motion,
  `ig/tools/lipsync_check.py`): teal cap = Mike Wright, cream cap = Andy Holloway. Wide shot / triptych never on screen (0-10.08 s = the
  stage: the hook question, then record vs points). One fixed frame per single, pushes toward the mouth; camera plate cropped from the 4K
  Topaz (no upscaling) → Chronos x2 per take (joints + camera cuts) → 59.94. Fresh Epidemic set + bed ("Mistaken Identity", Blue Saga)
  in `ig/assets/` (every slice ≤ 17.9 dB tonal). Deliver `outputs/ff-0-4-bye-week.sample-ig.final.mp4`.
- **2026-10-24 ~09:40 UTC: CUT FINAL + TOPAZ DONE, `work/READY.json` WRITTEN for the IG builder.** Topaz 3840x2160 ProRes, 1286 frames
  (checked; no morph at the 298 sliver). READY notes: speakers per span, joints, cameras + face boxes, the badge inpaint boxes, the
  two settled caption readings ('cause; score), the measured ambience-hole false positives. Next: YT graphics (HyperFrames MGs, `yt/mg/`).
- **2026-10-24 ~09:20 UTC: CUT FINAL, Topaz running (GPU lock).** `outputs/ff-0-4-bye-week.mp4` = 42.910 s / 1286 f @ 29.97
  (30000/1001), 18 segments, AMPLIFY_DB 0 (measured), -17.8 LUFS, peak -5.9 dBFS. audio-qa: timeline exact, 17 joints clean, limiter
  transparent; 3 "ambience holes" (7.94 / 17.95 / 34.37 s) = joints placed in a [p]/[b] closure or the quiet before a word, i.e. room
  tone quieter than the other side, not a crossfade fault (the bed covers them, as on MATG). Dead-air gate PASS. Re-ASR (medium.en,
  `work/tight/reasr.medium.txt`) reads every approved line. Canonical transcript 185 words (`outputs/ff-0-4-bye-week.transcript.json`).
  Topaz: `outputs/ff-0-4-bye-week.topaz.mov` (Iris 2x + FI, segments at every joint + the two camera cuts, `work/topaz.log`).
  **Next:** Topaz done → `work/READY.json` for the IG builder → YT graphics (HyperFrames MGs in `yt/mg/`) → spec → v1 → QA → sonnet
  reviewer → final 59.94 fps.

## The job
- Approved pick (Affan 2026-10-24): `projects/_onyx-batch5-2026-10/ff/PICKS.md` § 3 = `SEQUENCING.md` § 2 ★ 1, "Your fantasy team is
  0-4. Do this before you panic-trade". Eight lines, in order; trims inside lines only.
- Source: YouTube TXDemhCBL4c, "Snap Count Risers + Jason's Confession?! | Fantasy Football 2026 - Ep. 1988" (2026-10-07, 1:00:55,
  1080p H.264 29.97), `raw/TXDemhCBL4c.mp4` (+ info.json; downloaded by the main session). Chapter "0-4 Strategy" 46:54-48:34.
  `raw/TXDemhCBL4c_A.mkv` = LOCAL section 2780.778 → 2948.946 s (video stream-copied from the keyframe, PCM audio decoded from the same
  instant: both start at 0). Section clock = episode − 2780.778 s.
- Look: `presets/youtube-shorts/onyx-samples-youtube/` (Sean Ryan look, kit) + README § 13 devices. Template: `projects/matg-targeting-is-dead/`.
- Deliver: `outputs/ff-0-4-bye-week.sample-yt.final.mp4` + `X:\Claude Projects\Exports\ff-0-4-bye-week.yt.final.mp4` (H.264 1080x1920).
- A second builder makes the Instagram (neon window) version from this cut: `work/READY.json`; `ig/` is theirs.

## The cut (`work/cut_plan.py`: every boundary and pause measured; the comments there carry the numbers)
| # | Speaker | Section time | Kept |
|---|---|---|---|
| L1 HOOK | Andy (reads the listener's question) | 33.400-37.070 | "What do I do if I'm 0-4? Do I make a crazy trade or stay the course?" ("All right. Eli writing in," dropped) |
| L2 | Mike | 37.905-42.175, 43.644-45.245 | "Probably somewhere in between there. It's not always just record. It's how is your team doing. Points. Where are you in points per game?" (the false start "I mean, it's not." and the restart "Point scores. Yeah, like" dropped) |
| L3 | Mike | 51.251-51.652, 53.553-63.330 | "'Cause luck is part of fantasy football. It just is. Sometimes you score the fourth most points every week and you just happen to be up against the juggernaut of the week." (he says "luck" twice: the LAST take kept; the drawn-out "And" dropped) |
| L4 | Andy | 69.636-81.381 | "I'm in a CBS league for St. Jude's and I lost to the highest score in week one. I was the second highest score. I lost in week two, another tough luck loss where I scored a bunch of points, right? So I'm sitting 0-2 in that league." (a 0.27 s "uh" dropped) |
| L5 | Andy | 101.268-105.539 | "We've had people 0-4, 0-5, 0-6. We had an 0-7 win a title." |
| L6 | Andy | 106.673-108.508 | "Staying the course might not be your answer" |
| L7+L8 BUTTON | Andy | 116.316-125.859 | "If you're 0-4 and then you got guys going into bye, maybe that's where you can make a trade for another player whose bye is down the line. You can get a couple wins right now while other people's teams are on bye." |
- Pacing: 9 pauses cut on the 5 ms envelope (126 frames = 4.2 s), every leftover ≈ 0.07-0.11 s of room tone; the rest were ≤ 0.13 s already.
- Speakers on the picture: Mike = teal cap (his single camera 53.687-66.967), Andy = cream "A" cap (his single from 66.967), Jason (white
  cap, glasses) in the middle, silent here. Source cameras: triptych to 34.034, wide (MAIL BAG neon) 34.034-53.687, Mike single,
  Andy single 66.967-128.362. Burned in on every frame: "JOIN OUR COMMUNITY! JOINTHEFOOT.COM" (bottom left) and the show logo
  (bottom right): kept out of every crop (no CTA on the sample).
- Joints on the cut timeline (frames @ 29.97): 110, 238, 286, 298, 355, 384, 463, 538, 596, 692, 729, 850, 925, 975, 1030, 1059, 1139;
  source camera cuts inside segments: 19 (triptych → wide), 302 (wide → Mike single); 538 is also the Mike → Andy camera change.

## GATE 5 (facts on screen)
- No NFL game footage, no league / team / player logos, no ESPN / Yahoo / CBS / Sleeper look-alike UI. Team names on the cards are generic
  ("YOUR TEAM", invented rivals); no real player names.
- "We had an 0-7 win a title" is THEIR story (a listener's league, as told on the show): shown as told, labelled "AS TOLD ON THE SHOW",
  never as a sourced stat.
- Andy's league: a "CBS league for St. Jude's" = a charity league; the cards say "CHARITY LEAGUE" (no St. Jude or CBS logo).
- Week numbers / points on the example cards are illustrative and labelled "EXAMPLE" where a number is not spoken (Mike's record-vs-points
  card). Spoken facts drawn literally: 0-4; 4th-most points → L; WK1 2nd-highest score lost to the highest; WK2 tough-luck loss; 0-2;
  0-4, 0-5, 0-6, 0-7 → title; a player whose bye is "down the line".

## Better than the last sample (MATG, 2026-10-23)
- MATG told its story with screenshots (receipts). This one carries ONE object through the whole Short: "YOUR TEAM", a fantasy-app card
  that starts last in the standings at 0-4, gets checked for points, takes two L stamps, flips to 0-7 → a trophy, trades a bye-week
  player, and ends ticking to 2-4 while the rivals' rows read BYE, on the button word. Every graphic is a purpose-built motion graphic
  timed to the spoken words, not a still pushed in.
- The face is never on screen alone for more than ~3 s (Affan 2026-10-23, the 4 s rule); MATG had up to 4.6 s face stretches.
- 59.94 fps delivery (Chronos x2 per shot) vs MATG's 48.

## Download log
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `raw/TXDemhCBL4c.mp4` | YouTube TXDemhCBL4c (main session's download, `raw/download.log`) | 1.01 GB | the source |
| v2 | `raw/TXDemhCBL4c_A.mkv` | LOCAL derivative of v1 (2780.778-2948.946 s) | 45 MB | the clip the EDL cuts from |
| m1 | `yt/assets/audio/ES_Tarantula - Hysics.wav` + `ES_Tarantula STEMS DRUMS - Hysics.wav` → `bed-tarantula-nodrums.wav` (full − drums) | Epidemic Sound recording af985501-8272-36b4-b3ee-e083a700adfa "Tarantula" (Hysics; electro, mysterious, suspense, 100 bpm, 2:41), `DownloadRecording` WAV FULL + DRUMS; not used by any earlier job (grep 2026-10-24) | 46 + 46 MB | the bed (drumless, 12-14 LU under the voice) |
| x1-x14 | `yt/assets/sfx/<name>.wav` | Epidemic Sound SFX, `DownloadSoundEffect` WAV (`yt/work/sfx_fetch.py`), none used in this repo before (grep of every md/py/json/txt 2026-10-24): d716adfb Whoosh Short Mid Freq Dry 01 · 460b3ae4 Whoosh Short Low Dry 01 · b3b02292 Whoosh Short Wide Noise Dry · 1132a926 Boom Dark Cinematic Snappy Hit · 8862246e Boom Dark Cinematic Hard Hit 02 · 8424841e Boom Dark Cinematic Low Tone · 13b7690c Impact Sudden Heavy Percussive Hit · 3d67b9c7 Wood Impact Elbow Bash On Wooden Desk · d44da88b Playing Card Single Slide Pick Up · 68ca97f2 Wooden Block Small Thin Light Down On Wood 01 · f3c2426d Flip Dot Display Counting Board Loop 02 (sliced to 3 clacks) · 91fc1412 + 82f9409e Stinger Cinematic Hit Metal 05 / 03 · 0e565244 Riser Metal Hit Reverse (tonal 50.7 dB > 20: NOT used) | 0.25-3.9 MB each | one cue per graphic beat, variety (12 files over 47 cues) |
