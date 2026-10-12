# creatorscience-mrbeast-train: Onyx sample Short for Jay Clouse (Creator Science), guest David Altizer (batch 2)

## ▶ STATUS: resume here
- 2026-10-12 10:30: **QA r2: YouTube SHIPS (yt5 unchanged). Instagram remixed = ig8** (mix only, `--skip picture,overlay`; then
  ig_captions + ig_capy re-run to restore the spec's chunks for ig_qa): bed 17 → 13 LU (measured 12.7 LU under the voice on the stems),
  `sfx_rel` tick-glass −6 (the glass ticks ~8 dB under the voice peak), crisp cues on the entrances that only had a whoosh (pop 5.78 / 7.03
  on the compare, thud 9.17 on the word scene, shutter 30.54 on the route). −13.0 LUFS, −1.6 dBTP, `ig_qa.py` RESULT PASS. Final + Downloads overwritten.
- 2026-10-12 10:10: **QA r1 (`_onyx-batch2-2026-10/review/yt-qa-r1.md`) fixed, both finals re-rendered and overwritten** (YouTube = yt5, Instagram
  = ig7; Downloads copies replaced). Now **46.00 s, 1103 frames**. M1: the stray "I'm" (raw 278.30-278.75) after "your video." is cut
  (segment 15 ends 278.275 in the dip; `words.json` "video." end 278.21; re-spliced at AMPLIFY_DB 7; the Topaz base rebuilt by stream copy:
  old frames 0-998 + 1012-1115, old base kept in `work/topaz-v1-1116f.mov`); ASR on the new mix reads "your video and that's why". M2: both
  thumbnails (1280x720 maxresdefault, the largest YouTube serves) are now FITTED, never upscaled (YouTube s07/s10 FIT 0.84x + a push ≤1.10;
  the comparison panels fit to width over their blur; Instagram i06/i09 FIT 0.82x, reticles re-measured). M3: "MRBEAST" everywhere (YouTube
  chunk "MRBEAST DOES THIS"; Instagram captions read `ig/work/transcript-ig.json`, the cut transcript with "Mr"+"Beast" merged into one word).
  QA: `yt_qa.py` PASS (−12.0 LUFS, −1.7 dBTP), `ig_qa.py` PASS (−13.1, −1.8). Left as is (LOW): M4 "three to 500 million" (his spoken words;
  the screen prints only 313M), M5 short chunks, M6 watermark over the grid panel's small text, M7 tag/click SFX 5-6 dB under the voice peak.
- 2026-10-12 09:25: **BOTH LOOKS FINAL.** YouTube = yt4 (`outputs/creatorscience-mrbeast-train.sample-yt.final.mp4`, `~/Downloads/creatorscience-mrbeast-train.yt.final.mp4`);
  Instagram = ig5 (`outputs/creatorscience-mrbeast-train.sample-ig.final.mp4`, `~/Downloads/creatorscience-mrbeast-train.ig.final.mp4`): 46.55 s,
  −13.1 LUFS, −1.8 dBTP, `ig_qa.py` RESULT PASS (decode, loudness, 164/164 words once, punctuation, caption y 1122 constant inside the
  window, 43 cues / 21 events, 4.5 events per 10 s; NOTE: 20-30 s counts 2 kit events + 2 in-picture tag sounds). ig5 = ig4 + the first
  reticle moved onto the locomotive (measured on ig4) and the compare card narrowed off his cap. Next (Affan): review both; reaction video.
- 2026-10-12 09:20: **PHASE B (Instagram v2) at ig4 (building)**: `ig/build_spec.py` → `ig/spec.json`, run
  `python presets/youtube-shorts/onyx-samples/kit/ig_build.py projects/creatorscience-mrbeast-train <ver>` then `ig_qa.py … outputs/<job>.sample-ig.<ver>.mp4 --sheet`
  (ig3: RESULT PASS, −13.1 LUFS, −1.8 dBTP, 164/164 words, caption y 1128 constant, 43 cues / 21 events, 4.5 events per 10 s).
  Same cut and B-roll as the YouTube version; window shots + the window-size splits `ig/assets/make_ig_graphics.py` (compare, literal,
  click). Rounds: ig1 → ig2 (accent lifted #0060FD → #8EC5FF: the show's blue sank on David's blue wall; picture-side `shade` under the
  caption block on every bright B shot; David on the right third; route card moved off his face and shortened) → ig3 (a "thumbnail"
  reticle + a leak in the thin 15-23 s stretch, the sim-fall sound, route labels that fit, caption blocks break at scene + sentence
  changes) → ig4 (i04 z0 1.08 so his lips clear the line; a block break at f345). Next: ig_qa PASS on ig4 → `.sample-ig.final.mp4` + ~/Downloads.
- **Better than batch 1 (Instagram look):** the v2 letterbox window instead of full-frame cards; word-by-word stack captions with one
  serif hero word per block in a tint of the show's own blue (#0060FD sampled from the episode's graphics); a HUD vocabulary (reticles that
  re-target from the whole thumbnail to the train at the edge), a vertical route card that grows the method node by node, a 1M-vs-2-3K
  compare beside the head, a full-window "huge outlier" word scene, warm leaks only on scene changes, the white-line comparison split
  (viral sim · 2021 vs MrBeast · 2023) and a closing 313M neon receipt in the top bar; the guest named in the hook kicker and credit bar.
- 2026-10-12 08:40: **YOUTUBE LOOK FINAL = yt4** → `outputs/creatorscience-mrbeast-train.sample-yt.final.mp4` + `~/Downloads/creatorscience-mrbeast-train.yt.final.mp4`
  (46.55 s, 1116 frames 23.976, −12.0 LUFS, −1.7 dBTP, LRA 1.6; `work/scripts/yt_qa.py` PASS: clean decode, A = V, 164/164 words once,
  punctuation, caption line on the seam y 1092, one spike per cut (no stray frame); `work/scripts/sfx_qa.py`: 17 cues measured vs voice/bed).
  Self-QA rounds: yt1 → yt2 (two-up border, click card above the caption line, card above the captions on s06, short chunks merged) →
  yt3 (free cuts moved onto chunk changes, thumbnails re-made) → yt4 (the receipt never shows a static "0 views"). Thumbnails: Topaz
  Iris 4x was REJECTED (it waxed MrBeast's face and hallucinated a pattern on the sim's sleepers: `work/thumbup/*.REJECTED.mov`); they are
  Lanczos 4x + a gentle unsharp mask. Transcript casing: `corrections.local.json` (mr/beast → Mr/Beast). NEXT: PHASE B (Instagram v2), ig2 building.
- **Better than batch 1 (YouTube look):** the white seam line + captions on it from frame 1 (Affan's batch-2 rule); the opening frame is
  the speaker AND the visual proof (a split of David over MrBeast's own first shot) and the payoff returns to that shot (a true loop);
  diegetic self-made receipts instead of stock stand-ins (a small channel's grid with the 1M outlier, the click on his real video card, a
  0 → 313M count landing on "views"); two "same picture" comparison splits (viral sim vs MrBeast thumbnail; thumbnail vs first seconds);
  the host (Jay) on screen listening, from the episode's own two-up; a guest credit rides the hook (rule 9: who + why in 2 s); every
  third-party clip is a ≤3 s cut on disk, flagged.
- 2026-10-12 08:15: **YouTube look built to yt2** (`outputs/creatorscience-mrbeast-train.sample-yt.yt2.mp4`, −12.0 LUFS, −1.8 dBTP, clean
  decode); spec `yt/build_spec.py`, shots `yt/STORYBOARD.md`, run `bash yt/build.sh <ver> [skip-picture]` (= the kit's yt_build line + the
  job-local guest credit `yt/inject_credit.py`; faces: `yt/work/faces.json` + `yt/faces_adjust.py`). Self-made B-roll:
  `yt/assets/make_graphics.py` (grid, comparison splits, click card, receipt). Waiting on the GPU lock for the two thumbnails' Topaz 4x
  (`work/thumbup/`, then copy `<name>.4x.mov` frame → `work/thumbup/<name>.4x.png` and `yt/assets/broll/y-<name>-thumb-4x.png`, re-run
  `make_graphics.py compare literal click receipt`, rebuild) → yt3 = final candidate → QA → `.sample-yt.final.mp4` + ~/Downloads.
  PHASE B (main session, 08:10: the v2 kit is ready) started in parallel: `ig/build_spec.py`, `ig/assets/make_ig_graphics.py`, build ig1.
- 2026-10-12 07:05: **ROUGH CUT DONE** (17 segments, 46.55 s, 1116 frames at 23.976; `outputs/creatorscience-mrbeast-train.mp4`,
  `transcript/cuts.json`, `outputs/creatorscience-mrbeast-train.transcript.json` 164 words; dead-air gate passed; audio-qa clean,
  AMPLIFY_DB measured 7 dB, limiter 0.003 %). Topaz (Iris 2x + Chronos FI, `--segments` = `work/topaz-segments.txt`) running under the
  GPU lock → `outputs/creatorscience-mrbeast-train.topaz.mov`. Next: B-roll pulls (log below first), Epidemic bed, `yt/build_spec.py`, build, QA.
- 2026-10-12: job opened. Affan APPROVED the pick (`_onyx-batch2-2026-10/PICKS.md`, research `_onyx-batch2-2026-10/clouse/research.md`).
  ONE clip, edited TWICE: `ig/` = the Instagram look (`presets/youtube-shorts/onyx-samples/` + his 2026-10-12 direction: big black bars,
  animated captions, many refined premium motion graphics, crisp SFX, "an expensive video") and `yt/` = the Sean Ryan look
  (`presets/youtube-shorts/onyx-samples-youtube/` + a WHITE LINE on every split with the captions ON it, constant from frame 1).
  PHASE A (this agent) = the cut + the YouTube look; PHASE B (Instagram) waits for the main session's word that the v2 kit is ready.

## Source facts (measured 2026-10-12)
- **Time zero:** the section download's video started 5.743 s after its audio (AV1 1080p 23.976 + Opus). `raw/` = the download trimmed
  at 5.743 s (`-ss 5.743`, video stream-copied from its first keyframe, audio re-encoded FLAC): both streams start at 0, 7415 frames.
  **Sync verified:** the episode's own camera cuts land 0.16-0.22 s before each new speaker's first word (raw 125.265 → Jay "if" 125.484;
  144.660 → David "Yeah" 144.824). **The task's mapping t_file = t_ep − 0:33:40 was off:** words.json vs the show's transcript gives
  **raw t = episode t − 2015.4 s** (raw 0 = episode 0:33:35.4; "Beast does this all the time" raw 45.56 = site [34:21]).
- **Layouts** (`work/layout/layout.json`, `work/base-layout.json`; PLAYBOOK § 5b): David full webcam (sharp, well lit; camo cap,
  blue set), Jay full, a burned-in blue key-point BANNER (y 946-1079 of 1080), a TWO-UP (Jay left box, David right box, blue borders), and
  the episode's own GRAPH-PAPER inserts (David in a small top-right box; they show the BeamNG sim and MrBeast's thumbnail/video). On the
  base cut: David full f0-246 and f1012-1115, TWO-UP f695-807 and f998-1011, PAPER f247-694 and f808-997 (no usable face: B-roll only).
- **Word stamps patched** in `transcript/words.json` (slice-ASR faster-whisper medium.en + 5 ms RMS): "3000" 37.03-37.63 and "views."
  37.66-38.05 (WhisperX had squeezed "three thousand views" into 0.26 s), "that's" 48.11 and "it," end 31.19 (phantom edge words).
- Cut boundaries hand-set on the envelope (all `no_refine`): "Like" dropped before "that's the most literal", the "uh" before "a pit"
  cut, "It was just an animation" dropped (the necessity filter: "there was like an animation" already says it).

## The cut (cut-timeline s)
0.05 "Mr. Beast does this all the time. He'll find outliers." (HOOK) · 2.60 "especially if it's a smaller channel and they have a video with
like a million views, but they're averaging like two or 3000 views." · 9.18 "That's a huge outlier." · 10.34 "One of the best examples is the
train in the pit thumbnail." · 14.44 "There was like an animation of what would happen if a train fell into a sinkhole" · 19.49 "and that
thumbnail is insanely compelling. A train about to go over the edge of a cliff into a sinkhole." · 24.71 "And so what did he do? He essentially
recreated that exact same thumbnail and put his face on it." · 29.04 "So they made the thumbnail and then they literally dug a hole in the
ground, dropped a train in it." · 33.72 "And then you click the video. He's standing in front of a train that's barreling towards a pit. That's
the most literal way to start your video." · 42.30 "And that's why he gets three to 500 million views per video." (button "video", 46.47; end 46.55)
Loop: "…views per video." → "Mr. Beast does this all the time." Format: vertical Short from a 16:9 remote-call episode.

## Download log (batch-2 downloads approved by Affan 2026-10-12; every file logged BEFORE it is pulled)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `raw/7Cn0wncfkNA_<section>.mkv` | https://www.youtube.com/watch?v=7Cn0wncfkNA "How to design GREAT thumbnails (2025-11-16)", 0:33:40-0:38:45 (yt-dlp, best ≤ 2160p + audio) | 40.9 MB (done 2026-10-12, in `work/raw-orig/`) | the source of the cut |
| r1 | `reference/mXV4sFsoy_Q.mp4` | https://www.youtube.com/shorts/mXV4sFsoy_Q How a successful thumbnail concept led to an insane MrBeast video (the Short named in the permission email) | 4.9 MB (done 2026-10-12) | the "before" for the reaction video |
| m1 | `work/yt-src/fuhE6PYnRMc.info.json` (metadata only, no media) | yt-dlp `-j --skip-download` https://www.youtube.com/watch?v=fuhE6PYnRMc (MrBeast "Train Vs Giant Pit") | 1.1 MB (done 2026-10-12 07:03) | GATE 5 refresh: 2023-07-08, **313,524,798 views** (07:03), 10:36 long; chapters: the open = "Fireworks house explosion" 0:00, "Train crash into pit" 9:01-10:36 (most-replayed 10:17-10:30) |
| m2 | `work/yt-src/gaXkhN6aVxI.info.json` (metadata only) | yt-dlp `-j --skip-download` https://www.youtube.com/watch?v=gaXkhN6aVxI (BeamNG Nation "Trains vs Giant Pit") | 0.14 MB (done 07:04) | upload **2021-08-28** (23 months before MrBeast's), 169,541,652 views, 3:00 |
| t1 | `yt/assets/broll/y-mrbeast-thumb.jpg` | https://i.ytimg.com/vi/fuhE6PYnRMc/maxresdefault.jpg (MrBeast's own thumbnail, official image, FLAGGED) | 0.34 MB (done 07:04, 1280x720) | "the train in the pit thumbnail", "put his face on it", the receipt card |
| t2 | `yt/assets/broll/y-sim-thumb.jpg` | https://i.ytimg.com/vi/gaXkhN6aVxI/maxresdefault.jpg (the viral BeamNG sim's thumbnail, FLAGGED) | 0.23 MB (done 07:05, 1280x720) | "that thumbnail is insanely compelling", the "exact same thumbnail" comparison |
| s1 | `work/yt-src/fuhE6PYnRMc_open.mp4` (video only, H.264 1080p 29.97) | MrBeast "Train Vs Giant Pit", section 0:00-0:12 (yt-dlp `--download-sections`) | 9.0 MB (done 07:06): 0.5-2.9 MrBeast in front of the speeding blue train, 3.5-5.3 aerial of the train heading for the pit | ≤ 3 s cut: "he's standing in front of a train barreling towards a pit" (FLAGGED, another creator's clip) |
| s2 | `work/yt-src/gaXkhN6aVxI_sim.mp4` (video only, H.264 1080p60) | BeamNG Nation "Trains vs Giant Pit – BeamNG.Drive" (2021-08-28, 169,541,652 views on 2026-10-12, m2), section 0:00-0:20 | 15.4 MB (done 07:07) | ≤ 3 s cut: "an animation of what would happen if a train fell into a sinkhole" (FLAGGED) |
| s1b | `work/yt-src/fuhE6PYnRMc_crash.mp4` (video only, H.264 1080p) | MrBeast "Train Vs Giant Pit", section 10:16-10:31 (the most-replayed span) | 8.0 MB (done 07:06): the AFTERMATH (dust over the pit, reactions, a merch plug), not the fall: unused |
| s1c | `work/yt-src/fuhE6PYnRMc_fall.mp4` (video only, H.264 ≤1080p) | MrBeast "Train Vs Giant Pit", section 9:58-10:17 (just before s1b: the train going into the pit) | ~10-20 MB | ≤ 3 s cut: "dropped a train in it" (FLAGGED) |
| s2b | `work/yt-src/gaXkhN6aVxI_fall.mp4` (video only, H.264 ≤1080p) | BeamNG Nation "Trains vs Giant Pit", section 0:20-0:32 (s2 ends as the first train reaches the edge; most-replayed 0:23-0:25) | ~8-15 MB | ≤ 3 s cut: the sim train going over the edge (FLAGGED) |
| p1 | `yt/assets/broll/y-small-creator.mp4` | Pexels, free licence: https://www.pexels.com/video/4994156/ → https://videos.pexels.com/video-files/4994156/4994156-uhd_2160_3840_25fps.mp4 | ~30-90 MB | "especially if it's a smaller channel": a creator talking to his camera at home (native vertical 4K) |
| p2 | `yt/assets/broll/y-excavator-dig.mp4` | Pexels, free licence: https://www.pexels.com/video/34521517/ → https://videos.pexels.com/video-files/34521517/14626392_2160_3840_30fps.mp4 | ~30-90 MB | "they literally dug a hole in the ground" (native vertical 4K) |
| p3 | `yt/assets/broll/y-tractor-hole.mp4` | Pexels, free licence: https://www.pexels.com/video/20498440/ → https://videos.pexels.com/video-files/20498440/20498440-uhd_3840_2160_60fps.mp4 | ~40-120 MB | alternate for p2 ("a tractor digging a hole in the ground") |
| e1 | `yt/assets/audio/ES_There Is Still Time - John Utah.wav` (music bed, WAV full mix; the track has NO drum stem) | Epidemic Sound recording 35742269-95a6-4f37-a2eb-1a497bda9623 "There Is Still Time" (John Utah; mysterious, suspense, pulses; 80 bpm; 3:31) | ~35-40 MB | the bed (README § 8: tonal, no drums, builds: its second lift at 1:34-1:42 lands on the story's turn with bed_in 70 s). Picked from 4 LQ previews (Trace, Mindscape, DOX Pt. II: scratch only) by loudness/transient profile |
