# jeremyminer-google-88k: Onyx sample Short for Jeremy Miner (NEPQ, 7th Level) (batch 2)

## ▶ STATUS: resume here
- **2026-10-14: Affan swapped the bed: "Black Skinhead (Instrumental)" (Kanye West), his file (from E:\C shit\Telegram Desktop, copied to `yt/assets/audio/`), from 0.144 s, "make sure it's not too loud": YT bed_under_lu 14.5 + turn lift 1 dB (measured 14.2 LU under the voice), IG 14. Mix-only rebuilds (picture PSNR inf vs the approved finals): YT = yt v4, IG = ig v12 = v11's picture (its overlay cache was truncated, so v11's video stream was copied) + the new mix. NOTE: the IG final/export had been v5 (pre-QA-round-3) until now; v12 carries round 3. Finals + `X:\Claude Projects\Exports\` replaced; old finals kept as `outputs/*.final.prev-epidemic-bed.mp4`. ig_qa PASS, -12.1 / -13.0 LUFS.**
- **2026-10-12 (QA round 2 by the main session, `_onyx-batch2-2026-10/review/qa-r2.md`): YouTube SHIPS (yt v2). Instagram round 3
  (the last) applied -> IG final = ig v11.**
  - J-I1/J-I2 (jump cuts): no face-to-face cut on a joint remains. 1439 = the Adobe logo card (i08b, an IG layout of the card: logo right
    of centre, clear of the compare card); 1769 + 1796 = a word scene that starts on "Jeremy," (opaque before the joint) and ends on
    "for"; 2177 / 2321 / 2382 = the $100 stacks B-roll (i13), 2449 = George (i14), 2757 = the calculator keys, 2974 / 3097 = the exec
    woman (i17); 1539 / 1693 were already B (execs).
  - J-I3 (contrast): every B shot gets a bottom shade under the caption block (`SHADE`; execs a deeper one). Measured (`ig/work/
    contrast.py`, white text vs the 90th-pct background under the glyphs): worst 5.5:1 (was 0.8-1.5:1 on the execs).
  - Sound: bed 13 LU under the voice (was 17), glass ticks -6 dB (`sfx_rel`, ~8 dB under the voice peak), thuds -2 / impacts -3, a
    glass tick added on every graphic whose only sound was a whoosh (notify, compares, route), the hot 13.40 leak -4 dB, the second
    compare -5 dB (it sat +2 dB over the voice in a gap). `ig_qa` PASS.
  - Left: J-I7 (hook "How he closed Google in one meeting" is his own title's wording; Affan's call).
- **2026-10-12 (later): REVIEW ROUND (main session's `_onyx-batch2-2026-10/review/yt-qa-r1.md`) APPLIED; finals overwritten (YT = yt v2,
  IG = ig v5, + Downloads). The cut is now 54.80 s / 3288 frames.**
  - J1 (MED, verified on the raw envelope: syllables 237.15-237.33 and 237.49-237.60, a clean dip at 237.37-237.48; large-v3 "you you"):
    the first "you" is CUT (segment split at raw 237.06 | 237.44), slice-ASR now reads "dollars you guys will lose"; `words.json` "you"
    re-stamped to the kept one. Topaz base patched by stream copy (old frames 2757-2778 dropped, PSNR-checked), no GPU re-run.
  - J2 (MED): s12 -> s13 (split) -> s14 are hard cuts with ONE continuous push and the split top = the same crop as the full shot
    (`chain()` in build_spec); at the old f2841 the J1 joint is covered by a new B shot s19b (calculator keys) so s19 -> s20 is no longer
    split -> same camera. Instagram: its split i10 (top reframed 1.45/0.64 -> 1.6/0.5) became the execs B-roll + a leak.
  - J4 (LOW): a thin thud under the hook card, a soft hit on the Adobe card, a thin thud on the s13 split (no whoosh on a hard cut).
  - J3 (LOW) LEFT: the 0.35/0.39 s dead-air trims inside s17 ("a month | times | five months") stay: the literal cover (a calendar)
    played 3 s earlier, and restoring the pauses would re-time both looks again. J5 (LOW) LEFT: frames 0-3 are the source's own
    zoom-in settling (the split top has no hold_in in the kit); the first word starts at 0.04 s.
  - Instagram also: the notify and route cards now enter ON their cuts (they rose 4-5 frames before).
- **2026-10-12: BOTH LOOKS FINAL, awaiting Affan's review.**
  - **Instagram (v2 look) FINAL = ig v3** -> `outputs/jeremyminer-google-88k.sample-ig.final.mp4` + `C:\Users\affan\Downloads\
    jeremyminer-google-88k.ig.final.mp4` (55.17 s, 1080x1920 at 60 fps, -13.1 LUFS, -1.7 dBTP). `ig_qa` RESULT: PASS (every word once,
    one caption y 1059, 36 cues for 27 events, 4.9 events per 10 s, no full-window scenes). 3 rounds: v1 (SFX level FAIL, lower-case
    run-on captions, neon over his head) -> v2 (cased words, breaks, reframes, leaks) -> v3 (`captions.pct` 100: the tight intro shot's
    lips cleared, heroes moved off the numbers the neon shows, a leak at 11.88 s). Previews `*.preview.mp4` (720p).
  - YouTube look FINAL = yt v1 (below). Next: Affan's review of both; lessons go to the presets via the main session.
- **2026-10-12: YOUTUBE LOOK FINAL = yt v1** -> `outputs/jeremyminer-google-88k.sample-yt.final.mp4` + `C:\Users\affan\Downloads\
  jeremyminer-google-88k.yt.final.mp4` (55.17 s, 1080x1920 at 60 fps, -12.1 LUFS, -1.7 dBTP). Measured QA (`yt/work/qa/qa.py v1`):
  clean decode, 67 caption chunks = 171 words once (punctuation rule), every cut on a chunk change, 22 shots tile 3310 frames, 5 SFX
  present at their levels, audio = picture; contact sheets `yt/work/qa/v1/`. Two rounds: v0 (pre-Topaz) -> v1 (s01/s22 cash bottoms,
  60 fps whips, the Topaz base). Next: the Instagram version (below).
- 2026-10-12 (phase A, YouTube look): **rough cut DONE** 55.17 s, 3310 frames at 60 fps, 2560x1440 (`outputs/jeremyminer-google-88k.mp4`,
  19 segments, `transcript/cuts.json`; AMPLIFY_DB 12 measured; audio-qa clean; dead-air gate passed; every joint slice-ASR'd on CPU).
  `transcript/words.json` was PATCHED in 231.2-240.0 of section 3 (WhisperX had squeezed "that's about eleven point, eleven million five
  hundred and thirty six thousand dollars you guys will lose, because" into 231.8-234.2; real times from faster-whisper medium.en + the
  10 ms RMS envelope; the original is `work/cut/words.whisperx-orig.json`).
- Topaz: frame interpolation only (1440p source: `--no-enhance --no-stab`), segments at every joint + the source's own camera changes
  (57/66 intro transition, 108 graphics, 713-733 the original editor's animated punch-in) -> `outputs/jeremyminer-google-88k.topaz-fi.mov`.
- DONE: faces (`yt/work/faces.json`), `yt/STORYBOARD.md` (22 shots), B-roll (15 Pexels clips + the Adobe logo card, all logged below),
  the bed (Epidemic "Type E", Dream Cave), `yt/build_spec.py` -> `yt/spec.json`, overlay comp, mix (-12.1 LUFS, TP -1.8).
- Build: `python ../../presets/youtube-shorts/onyx-samples-youtube/kit/yt_build.py . <version>` (the kit, unchanged); `yt/build.py`
  is a job-local wrapper kept for a hook line the kit's clean() would strip (not needed now: the dotted kicker is the watermark, which
  the kit does not clean). QA: `python yt/work/qa/qa.py <version>`.
- Topaz DONE (`outputs/jeremyminer-google-88k.topaz-fi.mov`, 3310 frames; takes 9 and 16 came back 1 frame short and were redone
  without interpolation: the script's fallback). v0 draft (pre-Topaz base) QA'd: decode clean, -12.1 LUFS / -1.7 dBTP, 67 chunks /
  171 words once, every cut on a chunk change, 5 SFX present. Fixes for v1: the opening and closing split bottoms (s01 / s22 = the
  $100 stacks, a bookend for the loop), whips re-timed for 60 fps (`yt/build.py whip_profile_for`: the reference's 0.33 s whip, not
  0.13 s). v1 = `python yt/build.py v1` on the Topaz base.
- IG v1 built and QA'd (`ig_qa`: FAIL on one SFX level: the first neon's re-roll swell +5 dB over the voice). Round-1 fixes in v2:
  the neon's `rel_db` -8; captions read a job-local cased copy of the transcript (`ig/work/words.cased.json`: WhisperX left section 1
  lower-case and unpunctuated, so "i closed", "google", and blocks running across sentences) + `breaks` at every sentence-start joint +
  "000" dropped ("$88K" once); "88"/"41" out of the hero list (the neon already shows them); i01 z0 1.6 / fy 0.35 and i08 fy 0.37 (ig_capy:
  lips 62 / 20 px under the caption line); two more leaks (3.97 s, 13.40 s: a 5.2 s stretch had no designed sound); the closing "$88,000"
  neon moved from the window (over his head) to the top bar.
- **Phase B started (main session 2026-10-12: the v2 kit is ready):** `ig/build_spec.py` -> `ig/spec.json` ("look": "v2", 18 shots,
  10 cards), faces `ig/work/faces.json`; build `python ../../presets/youtube-shorts/onyx-samples/kit/ig_build.py . <version> --preview`,
  QA `ig_qa.py . outputs/<job>.sample-ig.<version>.mp4 --sheet`.

## Kit lessons for the preset LESSONS (job-local workarounds, presets untouched; reported to the main session)
- `yt_picture.py` Reader CONFORMS 20-32 fps clips at speed 1 (one source frame per output frame): on a 60 fps base that plays 25 fps stock
  at 0.42x. Workaround: `"speed": 1.0001` per B shot / split bottom (the retime path, fps=60). Same engine under `ig_window.py`.
- `workflows/whip-slide.py` steps its 24 fps-measured profile once per frame: at 60 fps the whip lasted 0.13 s. Workaround: `yt/build.py`
  `whip_profile_for(fps)` writes time-resampled `offsets/out/blur/out_blur` into shots.json before the whip pass.
- `captext.clean` strips "·" from YouTube hook lines; the watermark is not cleaned, so the GATE 5 kicker lives there.
- WhisperX squeezed a slowly spoken number line ("eleven million five hundred and thirty six thousand dollars you guys will lose") into
  the 2.4 s BEFORE it (4 s early); a cut built on its stamps held "that's about eleven point" instead. Slice-ASR every joint.
- WhisperX's first 30 s chunk came back lower-case and unpunctuated: the v2 stack captions ran across sentences ("called google We've
  got"). Workaround: a job-local cased/punctuated words file + `breaks` at sentence-start joints.
- `ig_capy` (75th pct) left a tight 0.95 s intro shot's lips 50 px under the line; the burned caption of the original edit forbade a
  higher crop, so `captions.pct` 100 (no picture re-render).

## Predictions (locked 2026-10-12, before sending; for the engine's RESULTS.md via the main session)
- Host response: a reply (60 %), a call (25 %), no reply (15 %). Why a reply: his own channel titled this story "How I Closed Google
  For $88,000" and never cut it as a Short (no Short title has Google or 88,000); the sample shows him his best story in 55 s.
- If posted on his Instagram: 60K-250K plays (his 30-day median is 70.4K); on YouTube Shorts 8K-40K (median 9.35K). Biggest failure
  reason: it reads as a brag retold at a whiteboard (no exchange on tape), and the calculator payoff needs the viewer to follow two numbers.
- Pre-mortem 5K: the stranger does not know NEPQ; the first 9 s are B-roll over his voice (no face until the split + 13 s); a 3-year-old
  story. 5M: "the creator of NEPQ vs Google" + the status flip ("30 minutes before Adobe") is a copyable move; the $11.5M vs $88K receipt.

## What this sample does better than batch 1 (Affan's rule: every video beats the last)
1. **The white seam line + constant seam captions** (his 2026-10-12 note on batch 1: "the one thing I don't like"): every split has the
   line and the captions sit on it at y 1092 for the whole video, so the opening split already shows them there.
2. **The video opens on a split**: his face and the money in the first frame, the line and the captions in place from frame 1.
3. **60 fps end to end**: the native 60 fps source + Topaz interpolation, rendered at 60 (batch 1 rendered 24-30). Stock B-roll plays at
   true speed (the kit's 24/30 conform would have slowed 25 fps stock to 0.42x on a 60 fps base: bypassed per shot, `RT` in build_spec).
4. **Literal, readable nouns**: the real Google sign, the real Adobe logo, the calculator, the cash; and continuity inside the story (the
   same "George" with his calculator for the question and the receipt; one high-rise boardroom shoot for the room).
5. **Premium sound design per beat**, not only whooshes: a soft reverberant hit on the Google reveal and a dark boom under the $11.5M
   receipt, whooshes at the batch-1 -10 dB level, a bed that lifts 2 dB at the calculator close.
6. **The cut was measured, not trusted**: every joint slice-ASR'd, and WhisperX's 4 s misalignment on the number line was caught and fixed
   in words.json (batch 1 found that class of error only in QA).

## The chosen sequence (clips engine: ONE escalation axis, enter on the strongest word, exit on the button)
The video is a solo training at a Vibe board, so the story is a vivid retelling with the exact lines, voiced by Jeremy. Its first 1:15 is
the original editor's intro (graphics, stock footage, burned-in captions over the speaker shots): those frames are never shown; B-roll and
a split cover them. **Axis: STATUS.** They treat him as a nobody ("exactly 60 minutes, just get to your presentation") -> he flips it
("you guys must have a lot of time on your hands, I've got 30-35 minutes before Adobe") -> it works (their demeanor changes) -> the
second loop opens: the stall ("we're totally in, but the budget is gone till January") -> the calculator close ($2.3M a month x 5 months,
George adds it up: $11,536,000 lost vs the $88,000 ask) -> "which is more risky for you guys?" -> "we have to do something" -> button:
"And then they wired that $88,000." The last line runs back into the first ("...I closed an $88,000 deal").

| # | base time | words (episode time) | why it stays |
|---|---|---|---|
| 1 | 0.00-8.22 | "You want to know how I closed an $88,000 deal with a Fortune 100 company in less than 41 minutes" (0:00.1-0:08.9) | the stranger hook: a number + "Fortune 100" + a clock. Enters on "you" because "how I" is fused (no clean onset for "I"; measured) |
| 2 | 8.22-9.12 | "It's called Google." (0:22.0) | the reveal; "one of the very first clients... a search engine... rhymes with Frugal" cut for time |
| 3 | 9.12-13.40 | (the division head) "We've got exactly 60 minutes, so if you could just get to your presentation" (4:50.7) | the belief, said in the room: he is a vendor. "Divisional head comes in" and "a rep will reach out in 2-3 weeks" cut (time) |
| 4 | 13.40-25.65 | "Oh geez, you guys must have a lot of time on your hands. I've got maybe 30, 35 minutes before my next appointment with Adobe across the street. Should we go ahead and jump right into it then?" (5:33.8-5:46.6) | the status flip, his own words; the 0.7 s pause after "geez" kept (timing is the joke) |
| 5 | 25.65-28.22 | "And you literally watch their whole demeanor change." (6:12.6) | proof the flip worked |
| 6 | 28.22-36.28 | "We're totally in, Jeremy, but... we've already allocated our training budget for the year and we have to wait till next year when the new budget comes out in January." (24:38.4-24:52.6) | the objection = the second open loop |
| 7 | 36.28-42.47 | "So two point three million dollars a month times five months. George, do you have your calculator?" (27:28.5-27:35.9) | the calculator close; dead air before "George" trimmed |
| 8 | 42.47-47.35 | "Eleven million five hundred thirty-six thousand dollars you guys will lose" (27:51.8; "that's about eleven point," false start cut) | the receipt |
| 9 | 47.35-53.12 | "Which is more risky for you guys?" / "She looked over to everybody else and she's like, we have to do something." (29:48.6-30:01.9) | the turn; pause before "we" trimmed to ~0.3 s |
| 10 | 53.12-55.17 | "And then they wired that $88,000." (31:11.6) | the button; loops into line 1 |

Dropped (relevant, not necessary now): the Frugal joke, "12 PhDs from Stanford", the sales-training question ("it was all product
training"), the "$80,000 or lose $10 million" aside (his own $10M vs $11.5M figures differ: only the $11,536,000 he computes on tape is used),
"rest is history" and the 244 % uplift (unverified, self-reported).

**GATE 5 (on screen):** "Fortune 100", "$88,000", "41 minutes", "$2.3 million a month", "$11,536,000" are HIS words, captioned as spoken.
No reps-trained count anywhere. Kicker = "JEREMY MINER · CREATOR OF NEPQ". "2018 or something" is his date (not used on screen). Google
= three of its divisions in Tempe, AZ (he says so; the sample shows the Google brand, never a claim of a company-wide deal).

## Download log (batch-2 downloads approved by Affan 2026-10-12)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `raw/lQHdTN4Tp8U_<section>.mkv` | https://www.youtube.com/watch?v=lQHdTN4Tp8U "How I Closed Google For $88,000 (~2023, 33:43)", whole video (the story runs 0:00-31:15) (yt-dlp, best ≤ 2160p + audio) | 584.6 MB (done 2026-10-12, in `work/raw-orig/`) | the source of the cut |
| r1 | `reference/tpdcvJr9QPg.mp4` | https://www.youtube.com/shorts/tpdcvJr9QPg OBJECTION: "I need to sleep on it" (the Short named in the permission email) | 40.8 MB (done 2026-10-12) | the "before" for the reaction video |
| s1-s3 | `raw/lQHdTN4Tp8U_000000-000115.mkv`, `_000420-000630.mkv`, `_002400-003120.mkv` | LOCAL stream-copy sections of v1 (no download): episode 0:00-1:15, 4:20-6:30, 24:00-31:20; audio padded to the video's first frame (keyframe before the request: +0.021 / +1.233 / +1.833 s), so section t = 0 is episode 0.000 / 258.767 / 1438.167 | 38 / 53 / 142 MB | the three story blocks the cut draws from |
| p0 | `work/pexels/thumbs/<id>.jpg`, `work/pexels/big/<id>.jpg` | Pexels search-result preview thumbnails (images.pexels.com, `w=320` / `w=500`), for choosing B-roll | ~15-60 KB each, ≤ 200 files | B-roll selection only |

### Download log, YouTube-look B-roll + music (yt/, 2026-10-12; every file logged BEFORE it is pulled; Pexels free licence)
| # | File | Source | Size (HEAD / est.) | For |
|---|---|---|---|---|
| y02 | `yt/assets/broll/y02-cash-briefcase.mp4` | Pexels 6266255 https://videos.pexels.com/video-files/6266255/6266255-uhd_2160_3840_25fps.mp4 | ~30-60 MB | "how I closed an $88,000 deal" |
| y03 | `yt/assets/broll/y03-towers-low-angle.mp4` | Pexels 7076551 https://videos.pexels.com/video-files/7076551/7076551-uhd_2160_3840_24fps.mp4 | 10.8 MB | "a Fortune 100 company" |
| y04 | `yt/assets/broll/y04-clock-ticking.mp4` | Pexels 7034348 https://videos.pexels.com/video-files/7034348/7034348-hd_1080_1920_25fps.mp4 | ~10-20 MB | "in less than 41 minutes" |
| y05 | `yt/assets/broll/y05-google-nyc.mp4` | Pexels 37692146 "Google building in NYC with yellow taxis" https://videos.pexels.com/video-files/37692146/15981537_1440_2560_24fps.mp4 | 44.5 MB | "It's called Google" |
| y06 | `yt/assets/broll/y06-exec-woman-head-of-table.mp4` | Pexels 7552662 https://videos.pexels.com/video-files/7552662/7552662-hd_1080_1920_25fps.mp4 | ~15-30 MB | the division head: "We've got exactly 60 minutes" |
| y07 | `yt/assets/broll/y07-boardroom-skyline.mp4` | Pexels 7643606 https://videos.pexels.com/video-files/7643606/7643606-uhd_2160_4096_25fps.mp4 | ~40-90 MB | "get to your presentation" (the big conference room) |
| y09 | `yt/assets/broll/y09-man-checks-watch.mp4` | Pexels 7580268 https://videos.pexels.com/video-files/7580268/7580268-uhd_2160_4096_25fps.mp4 | ~40-90 MB | "30, 35 minutes before my next appointment" |
| y10 | `yt/assets/broll/adobe-logo-wordmark.svg` | Wikimedia Commons "Adobe_Systems_logo_and_wordmark.svg" https://upload.wikimedia.org/wikipedia/commons/7/7b/Adobe_Systems_logo_and_wordmark.svg (a real logo) | 2.5 KB | "with Adobe across the street" |
| y12 | `yt/assets/broll/y12-execs-attentive.mp4` | Pexels 7552487 https://videos.pexels.com/video-files/7552487/7552487-hd_1080_1920_25fps.mp4 | ~15-30 MB | SPLIT bottom: "their whole demeanor change" |
| y14 | `yt/assets/broll/y14-business-summary.mp4` | Pexels 6781990 https://videos.pexels.com/video-files/6781990/6781990-uhd_2160_3840_30fps.mp4 | ~20-60 MB | "our training budget for the year" |
| y15 | `yt/assets/broll/y15-calendar-flip.mp4` | Pexels 35332817 https://videos.pexels.com/video-files/35332817/14970418_2160_3840_30fps.mp4 | ~20-50 MB | "wait till next year... January" |
| y17 | `yt/assets/broll/y17-man-calculator.mp4` | Pexels 8479268 https://videos.pexels.com/video-files/8479268/8479268-hd_1080_1920_25fps.mp4 | ~15-30 MB | "George, do you have your calculator?" |
| y18 | `yt/assets/broll/y18-calculator-keys.mp4` | Pexels 6266437 https://videos.pexels.com/video-files/6266437/6266437-uhd_2160_3840_25fps.mp4 | ~30-60 MB | SPLIT bottom: "$11,536,000 you guys will lose" |
| y20 | `yt/assets/broll/y20-boardroom-woman-turns.mp4` | Pexels 7643318 https://videos.pexels.com/video-files/7643318/7643318-uhd_2160_4096_25fps.mp4 | ~60-120 MB | "She looked over to everybody else... we have to do something" |
| y21 | `yt/assets/broll/y21-money-keyboard.mp4` | Pexels 5924997 https://videos.pexels.com/video-files/5924997/5924997-uhd_2160_3840_24fps.mp4 | ~30-60 MB | SPLIT bottom: "they wired that $88,000" |
| y21b | `yt/assets/broll/y21b-hand-on-cash.mp4` | Pexels 6266433 https://videos.pexels.com/video-files/6266433/6266433-uhd_2160_3840_25fps.mp4 | ~30-60 MB | SPLIT bottom of the opening (s01) |

All y-files pulled 2026-10-12 (sizes 4-43 MB, 1080x1920 to 2160x4096, 24-30 fps; `work/look/broll_sheet.jpg`). `y10-adobe-logo.png` is rendered locally from the logged SVG (headless Chrome, `work/adobe/card.html`: red logo, white wordmark, dark card). m0 previews pulled for Type E, Don't Let It Get You Down, Make No Mistakes (`work/music/`).
| m0 | `work/music/preview-<id>.mp3` | Epidemic Sound low-quality previews (audiocdn.epidemicsound.com lqmp3) of 3-4 candidate beds, for choosing | ~1-3 MB each | music choice only |
| m1 | `yt/assets/audio/ES_Type E - Dream Cave.wav` | Epidemic Sound recording 64f6a697-c58a-395d-9656-94217ae35be4 "Type E" (Dream Cave / Johannes Bornlöf; suspense, pulses, build; 120 bpm; 2:04), WAV full mix via `DownloadRecording` | 35.8 MB (done 2026-10-12) | the music bed (its drums stem sits ~15 LU under the full mix: near drum-free) |
