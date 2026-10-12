# victorantonio-marketing-first: Onyx sample Short for Victor Antonio (batch 2)

## ▶ STATUS: resume here
- **2026-10-12 11:15: QA r2 (`_onyx-batch2-2026-10/review/qa-r2.md`, round 3 of 3) applied; finals = YT v6, IG v6** (outputs +
  Downloads replaced). YT: the s14b split (top reframed at the source's layout switch, f713) is now Randy Gage's photo full-bleed
  (a real scene change); the face-split joint at f825 is covered by the lunch-table B-roll (s17 = old s17 + s18a); captions show
  no comma/colon ("250K", "THREE FORTY-EIGHT / PM", "I MADE $17K"); bed 12.6 LU under (was 14.3); the hook gets a shutter on landing.
  -12.1 LUFS, -1.7 dBTP, lipcheck PASS. IG: a bottom shade under the caption block on every B-roll shot (a 0.70 gradient, window
  y 380-600), bed 13 LU under (was 17), glass ticks -6 dB (`sfx_rel`, ~8 under the voice peak), a shutter on each card entrance, a
  glass tick on each compare side, a soft impact as each wordscene opens; ig_qa PASS (51 cues, -13.1 LUFS, -1.5 dBTP).
  Left (LOW, verify by ear): the "I" (24.37 s) and "says" (27.50 s) segment starts: moving either out by a frame brings back the /k/
  click of "strategic" or the vowel of "off" (measured), so they stay.
- **2026-10-12 10:30: QA r1 (independent review `_onyx-batch2-2026-10/review/yt-qa-r1.md`) applied; BOTH finals re-rendered and
  replaced (outputs + Downloads).** Cut now 51.57 s / 1547 f:
  - V1 HIGH, real: he says "seventeen THOUSAND" (raw slice ASR x3: `$17[68.30-69.10] ,000[69.10-69.92]`, then "That's one seven"
    at 70.06-70.98; my earlier slice ended at 69.08). Segment 4 now ends at 69.80; captions "I MADE $17K" / IG "$17K". Topaz re-run on
    that take only (105 f) and stream-copy concatenated (1547 packets = frames; PSNR vs the base flat across the joins).
  - V2-V4: no whip / reframe between shots of Victor's camera: s13 -> s14a -> s14b hard cuts with ONE top framing; B-roll inserted
    between split and face (s18a lunch table, s25a Randy Gage's photo); s19 B-roll runs through old f1024.
  - V5: joints at old f621 / f873 / f1507 now sit on B-roll edges (same done for the Instagram face shots: old 223, 621, 751, 873,
    1083, 1101). Spec frames authored on the old timeline, mapped by SHIFT (+22 from old f535) in both build_specs.
  - V6: "could" is right (four raw slices) -> fixed in words.json + captions; "says" kept: two full-context raw slices read
    "off, says" / "off and says", the cut starts on the /s/ of "says".
  - YT v5: -12.1 LUFS, -1.5 dBTP, clean, lipcheck PASS, captions == words. IG v5: ig_qa PASS (-13.1 LUFS, 172 words once).
- **2026-10-12 08:30: YouTube look FINAL** = v4 on the Topaz 4K base: `outputs/victorantonio-marketing-first.sample-yt.final.mp4` + copy
  `C:\Users\affan\Downloads\victorantonio-marketing-first.yt.final.mp4`. 50.83 s, 1525 f at 30 fps, -12.1 LUFS, -1.7 dBFS peak, clean
  decode; 29 shots (B 54 % / SPLIT 23 % / A 23 %), 25 whips + 3 hard cuts; 14 SFX cues; build `python yt/build.py <v>`.
  Topaz note: its segment list came from a layout map 1 frame off; the only casualty is Topaz frame 292 (PSNR 11 vs the base: a
  wrong-layout frame), which NO shot uses (B-roll covers 223-352 in both looks); f688-691 checked: no FI ghost.
- **2026-10-12 09:20: Instagram v2 look FINAL** = ig v4: `outputs/victorantonio-marketing-first.sample-ig.final.mp4` + copy
  `C:\Users\affan\Downloads\victorantonio-marketing-first.ig.final.mp4`. Same 50.83 s cut, rendered at 60 fps (3050 f), -13.1 LUFS,
  -1.6 dBTP; `kit/ig_qa.py` RESULT: PASS (decode, loudness, 172 words once and in order, punctuation, one caption y 1088 inside the
  window, 43 cues for 33 designed events, 5.9 events per 10 s, full-window scenes 19 %). Storyboard `ig/STORYBOARD.md`; spec
  `ig/build_spec.py`; job-local passes `ig/caption_tune.py` + `ig/overlay_patch.py`; build `python ig/build.py <v>`.
  IG QA rounds: v1 → the neon washed out over his white blinds (moved to the top bar), "250 / 000" split in two caption words and
  lowercase "i'm / randy gage" (job-local caption words `ig/work/words.json`), ig_qa rejects the ':' of "3:48" (spoken as "three
  forty-eight" in the IG captions), list meta truncated, Randy reticle box measured, serif heroes doubled under wordscenes (demoted),
  St John's lips under the line (reframed); v2 → i18 lips 8 px under the line (reframed), the bleed showed a stray B-roll / text over
  his face (a centred-Victor shot under it, then no bleed); v3/v4 clean.
- **Phase A + B DONE.** Open for Affan: the reaction video (he records), the delivery email (draft only; Affan sends).
- YouTube QA (v1 → v4): the constant caption line moved 1092 → **1190** (his webcam is tight: the mouth sits at 52-55 % of his frame and
  he leans ~100 px; `work/scripts/lipcheck.py` PASS: every A frame's lower lip ≥ 13 px above the caption caps); A / split-top framing
  solved per shot from its own detections (`frame_shot` in build_spec); s14 cut at the base's real layout change f691; the guesses
  play ONE word at a time in the hook slot (a stacked list of three was cramped and unreadable); SFX levels from the MEASURED file
  peaks (the manifest's were off by 2-7 dB): `work/scripts/sfxcheck.py`; captions vs words: every chunk = its words, ! ? quotes only.
- **Time base (measured):** the section's AUDIO starts at episode **0:47:50.0**, not 0:47:55 (yt-dlp took the audio from the fragment
  before; WhisperX vs the scout captions agree to ±0.1 s): **t_file = t_episode − 2870 s**. Video starts at container 4.646 s (keyframe);
  `splice.sh` handles it. Note for scripts: a plain ffmpeg decode PADS those 4.6 s with copies of frame 1 (frame n = container n/30).
- **No `--diarize`:** no Hugging Face token on this machine and pyannote/speaker-diarization-3.1 is not cached (transcribe.sh exits).
  Speakers attributed instead by wespeaker embeddings (cached; `work/scripts/emb*.py`, the Pomp QA method): **St John says the skyscraper
  line** (cos to Victor −0.01) and **Victor says "Right"** (louder on his mic, V 0.38 vs S 0.00). Every other kept line is Victor (V 0.58–0.83).
- **What he actually says (slice re-ASR + envelope, fixed in `transcript/words.json`, originals in `work/words.whisperx-orig.json`):**
  "it's 2001" (not "is"), "two hundred and fifty thousand" ends at 17.44 (WhisperX squeezed it and planted a phantom "okay"),
  **"My first year, I made seventeen."** (no "thousand": four syllables, then "That's one seven"; the YouTube captions' "$17,000" is
  their normalisation), "You **can** have the best message", "off, **says**, Victor" (no "He"), "Uh" between "two kids" and "we got debt" cut.
- Source layouts (an auto-cycling template): TWOUP (St John x 0-960 | Victor x 960-1920, same scale as Victor full), VICTOR full,
  STJOHN full; "The Rural Sales Show" logo burned in at x 1735-1880, y 895-1040 (no credit: painted out / cropped). Per base frame:
  `work/base_layout.json`.
- 2026-10-12: job opened. Affan APPROVED the pick (`_onyx-batch2-2026-10/PICKS.md`, research `_onyx-batch2-2026-10/antonio/research.md`).
  ONE clip, edited TWICE: `ig/` = the Instagram look (`presets/youtube-shorts/onyx-samples/` + his 2026-10-12 direction: big black bars,
  animated captions, many refined premium motion graphics, crisp SFX, "an expensive video") and `yt/` = the Sean Ryan look
  (`presets/youtube-shorts/onyx-samples-youtube/` + a WHITE LINE on every split with the captions ON it, constant from frame 1).

## Cut sheet (EDL `transcript/cuts.json`, all segments pinned; episode time = source + 2870 s; cut time on the 50.83 s base)
| seg | cut (s) | source (s) | words |
|---|---|---|---|
| 1 | 0.00-7.43 | 10.067-17.500 | I'm CEO of a technology company, my base salary, it's 2001, was 250,000. |
| 2 | 7.43-13.50 | 26.967-33.033 | May 9th, 2001, 3:48 p.m. I decide to quit because I want to be a speaker like Zig Ziglar. |
| 3 | 13.50-14.17 | 42.500-43.167 | We have two kids. |
| 4 | 14.17-15.07 | 43.500-44.400 | We got debt. |
| 5 | 15.07-17.83 | 66.300-69.067 | My first year, I made $17,000. |
| 6 | 17.83-20.70 | 76.400-79.267 | (St John) That's like dropping from a skyscraper to a bungalow. (Victor) Right. |
| 7 | 20.70-23.63 | 101.433-104.367 | There's a speaker, I can say his name, by the name of Randy Gage. |
| 8 | 23.63-25.03 | 145.067-146.467 | I sat next to him, right? |
| 9 | 25.03-26.77 | 150.467-152.200 | and I'm apparently whining. |
| 10 | 26.77-28.33 | 175.267-176.833 | says, Victor, let me ask you a question. I said, |
| 11 | 28.33-29.10 | 177.367-178.133 | what's your question? |
| 12 | 29.10-30.67 | 178.700-180.267 | He said, what business are you in? |
| 13 | 30.67-32.37 | 189.333-191.033 | And I said, in the speaking business. |
| 14 | 32.37-34.67 | 191.467-193.767 | And he goes, no, that's not the business you're in. |
| 15 | 34.67-36.10 | 197.900-199.333 | Okay, the training business. |
| 16 | 36.10-36.70 | 200.267-200.867 | No, |
| 17 | 36.70-38.87 | 201.700-203.867 | the motivation business, no. |
| 18 | 38.87-42.73 | 212.867-216.733 | And I said, okay, you tell me, Randy, you tell me what business am I in? |
| 19 | 42.73-43.60 | 219.900-220.767 | And he says, |
| 20 | 43.60-47.37 | 221.267-225.033 | you're in the marketing business first. Everything else is second. |
| 21 | 47.37-50.23 | 249.167-252.033 | You could have the best message in the world, but if nobody knows you exist... |
| 22 | 50.23-50.83 | 253.000-253.600 | Who cares? |

## Download log (batch-2 downloads approved by Affan 2026-10-12)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `raw/A_JBRthrFB4_<section>.mkv` | https://www.youtube.com/watch?v=A_JBRthrFB4 "How I Became One of the Top Sales Speakers In The World (The Rural Sales Show, host St John Craner; NO credit, Affan 2026-10-12)", 0:47:55-0:52:10 (yt-dlp, best ≤ 2160p + audio) | 55.6 MB (done 2026-10-12, in `work/raw-orig/`) | the source of the cut |
| r1 | `reference/xOy_Gc_0Q4s.mp4` | https://www.youtube.com/shorts/xOy_Gc_0Q4s Why Most Salespeople Can "Talk" But Can't "Speak" (the Short named in the permission email) | 3.4 MB (done 2026-10-12) | the "before" for the reaction video |
| p* | scratch only: Pexels PREVIEW stills `https://images.pexels.com/videos/<id>/pictures/preview-<n>.jpg` (≈ 5 KB each, 123×218, up to ~200 files) for picking the B-roll; never used in the video | Pexels (free licence) | ≈ 1 MB total | B-roll selection (logged 2026-10-12 07:25, before pulling) |
| i1 | `yt/assets/broll/y14-randy-gage.jpg` | Wikimedia Commons `File:Randy_Paul.jpg` (CC0, "Gage speaking to a seminar", the Wikipedia infobox photo of Randy Gage) https://upload.wikimedia.org/wikipedia/commons/6/69/Randy_Paul.jpg | 0.12 MB (1600×1071; done) | "by the name of Randy Gage" (real photo; identity = Wikipedia's article image) |
| i2 | `yt/assets/broll/y07-zig-ziglar.jpg` | Wikimedia Commons `File:Zig_Ziglar_at_Get_Motivated_Seminar,_Cow_Palace_2009-3-24_3.JPG` (CC BY-SA 3.0 / GFDL, User:BrokenSphere; credit needed if posted) https://upload.wikimedia.org/wikipedia/commons/f/ff/Zig_Ziglar_at_Get_Motivated_Seminar%2C_Cow_Palace_2009-3-24_3.JPG | 1.6 MB (2288×1712; done; REJECTED: a soft photo of a projection screen → work/rejected-broll/) | "a speaker like Zig Ziglar" (real photo, on stage) — used only if sharp at full size |

### Download log, YouTube-look B-roll (Pexels, free licence; logged 2026-10-12 07:35 BEFORE pulling; sizes filled in after)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| y02 | `yt/assets/broll/y02-ceo-glass-office.mp4` | https://www.pexels.com/video/businessman-looking-through-a-glass-window-8572175/ → https://videos.pexels.com/video-files/8572175/8572175-uhd_1440_2732_25fps.mp4 | 53.0 MB (done) | "CEO of a technology company" (a suited man at a high-rise glass window) |
| y04 | `yt/assets/broll/y04-counting-cash.mp4` | https://www.pexels.com/video/a-person-counting-dollar-bills-6266251/ → https://videos.pexels.com/video-files/6266251/6266251-uhd_1440_2560_25fps.mp4 | 15.1 MB (done) | "was 250,000" (hands fanning $100 bills) |
| y05 | `yt/assets/broll/y05-clock-hands.mp4` | https://www.pexels.com/video/close-up-of-clock-hands-7034335/ → https://videos.pexels.com/video-files/7034335/7034335-hd_1080_1920_25fps.mp4 | 3.6 MB (done) | "May 9th, 2001, 3:48 p.m." (clock dial close-up; no readable time) |
| y06 | `yt/assets/broll/y06-quit-box.mp4` | https://www.pexels.com/video/a-man-carrying-a-box-with-things-on-it-9365579/ → https://videos.pexels.com/video-files/9365579/9365579-hd_1080_1920_25fps.mp4 | 12.0 MB (done) | "I decide to quit" (an employee carrying his desk box) |
| y08 | `yt/assets/broll/y08-two-kids.mp4` | https://www.pexels.com/video/two-little-girls-eating-popcorn-5267105/ → https://videos.pexels.com/video-files/5267105/5267105-uhd_1440_2732_30fps.mp4 | 12.6 MB (done) | "We have two kids" |
| y09 | `yt/assets/broll/y09-past-due-bill.mp4` | https://www.pexels.com/video/a-stressed-man-reading-a-past-due-bill-7924459/ → https://videos.pexels.com/video-files/7924459/7924459-uhd_1440_2560_24fps.mp4 | 7.3 MB (done) | "We got debt" (a PAST DUE bill) |
| y11 | `yt/assets/broll/y11-skyscraper.mp4` | https://www.pexels.com/video/tallest-tower-in-the-city-5354697/ → https://videos.pexels.com/video-files/5354697/5354697-uhd_1440_2560_24fps.mp4 | 20.1 MB (done) | "dropping from a skyscraper" |
| y12 | `yt/assets/broll/y12-bungalow.mp4` | https://www.pexels.com/video/a-view-of-a-house-with-a-roof-and-a-fence-20314189/ → https://videos.pexels.com/video-files/20314189/20314189-uhd_1440_2560_24fps.mp4 | 19.7 MB (done) | "to a bungalow" (a small one-storey house) |
| y15 | `yt/assets/broll/y15-lunch-table.mp4` | https://www.pexels.com/video/people-having-conversation-while-eating-8717541/ → https://videos.pexels.com/video-files/8717541/8717541-uhd_1440_2560_25fps.mp4 | 12.6 MB (done) | "I sat next to him" (a conference lunch table) |
| y19 | `yt/assets/broll/y19-speaker-mic.mp4` | https://www.pexels.com/video/engaging-business-conference-speaker-presentation-34917507/ → https://videos.pexels.com/video-files/34917507/14791158_1080_1920_60fps.mp4 | 4.6 MB (done) | "the speaking business" (a conference speaker with a mic) |
| y22 | `yt/assets/broll/y22-trainer-whiteboard.mp4` | https://www.pexels.com/video/woman-writing-on-a-whiteboard-8344225/ → https://videos.pexels.com/video-files/8344225/8344225-uhd_1440_2560_25fps.mp4 | 9.5 MB (done) | "the training business" (a trainer at a flip chart) |
| y23 | `yt/assets/broll/y23-arena-crowd.mp4` | https://www.pexels.com/video/people-are-standing-in-a-large-crowd-and-clapping-16229182/ → https://videos.pexels.com/video-files/16229182/16229182-uhd_1440_2560_60fps.mp4 | 28.3 MB (done) | "the motivation business" (an arena crowd clapping) |
| y26 | `yt/assets/broll/y26-times-square.mp4` | https://www.pexels.com/video/vivid-times-square-digital-billboards-at-daytime-31997525/ → https://videos.pexels.com/video-files/31997525/13636429_1440_2560_30fps.mp4 | 61.2 MB (done) | "the marketing business first" (Times Square billboards) |
| y27 | `yt/assets/broll/y27-empty-hall.mp4` | https://www.pexels.com/video/elegant-empty-concert-hall-interior-view-35122004/ → https://videos.pexels.com/video-files/35122004/14879058_2560_1440_30fps.mp4 | 4.3 MB (done) | "if nobody knows you exist" (an empty concert hall) |
| y07alt | `yt/assets/broll/y07alt-presenter.mp4` | https://www.pexels.com/video/a-man-standing-while-having-a-presentation-7413802/ → https://videos.pexels.com/video-files/7413802/7413802-hd_1080_1920_24fps.mp4 | 5.9 MB (done) | fallback for the Zig Ziglar split if the Commons photo is soft |
| y07 | `yt/assets/broll/y07-speaker-arena.mp4` | https://www.pexels.com/video/speaker-addressing-illuminated-audience-at-night-35451425/ → https://videos.pexels.com/video-files/35451425/15019450_2560_1440_32fps.mp4 | 59.7 MB (done) | "a speaker like Zig Ziglar" (a speaker at a podium before an arena of phone lights; replaces the Commons Zig photo, which is a soft photo of a projection screen: REJECTED, HQ rule) |
| m1 | `yt/assets/audio/ES_There Is Still Time - John Utah.wav` (music bed, WAV full mix; the track has no drum stem) | Epidemic Sound recording 35742269-95a6-4f37-a2eb-1a497bda9623 ("There Is Still Time", John Utah; mysterious, pulses, suspense; 80 bpm; 3:31) | 60.8 MB (done) | the one bed (logged 2026-10-12 07:45 before pulling); bed_in ≈ 49 s puts the track's 87-96 s lift on "you're in the marketing business first" |
