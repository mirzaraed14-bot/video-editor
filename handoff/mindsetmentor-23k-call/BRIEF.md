# mindsetmentor-23k-call: Onyx sample Short for The Mindset Mentor (Rob Dial)

## ▶ STATUS: resume here
- **2026-10-07: FINAL = v15** (QA rev2-r1 fixed): the HR cutaway reframed (window centre cy 0.62: her mouth above the constant caption line; it must run to ~f962 because Rob's own video carries this stock cutaway until then), the $23,000 hit on the landed number (kit: 0.92 x the count), hit/chime +2-3 dB, scene whooshes +3 dB, the credit on a pill (it crossed the mic logo), "And she goes," 0.15 s earlier, captions $23K (no commas, kit), the base re-spliced frame-exact (+4 frames of room tone so "today" decays; one frame the old time-trim had dropped at f496 restored) and Topaz re-run on it. 49.63 s at 59.94 fps, -13.0 LUFS, clean decode.
- **2026-10-07: REVISED FINAL = v13** (Affan's review 2). Hook for strangers: title "He quit his job / almost broke / Then his old HR called" (was "Aren't you worried?"). Captions white + yellow emphasis words (was all yellow), ONE constant position (top 919, just under the lips), no full stops/commas, rendered at 59.94 fps so the rise is smooth. Same-camera shots merged (no punch-ins; one framing z1.05, a gentle push-in), the HR cutaway is one shot. Cards moved below the caption line (y 1100). Sound: the Epidemic kit (assets/sfx/epidemic) at peaks 5-8 dB under the voice's: a light swoosh on the hook, a phone vibration on each call card, a glass pop on the chip, a hit on the $23,000 landing, a notification chime on the bank card, a soft whoosh on every scene change (18 cues; the old -22 dB filler ticks removed). The "wow" Affan noted is in Pomp's video, not this one. Clean decode.
- **2026-10-06 (night): FINAL = v11** — Topaz frame interpolation (Affan's rule; no Iris on this native-4K source; the cut has no repeated frames, so Chronos changed nothing visible: 1185 frames exact). base_hq = `outputs/mindsetmentor-23k-call.topaz-fi.mov`. Captions: lip gap 0.13, moves on cuts (10); "right around $23,000." stays ABOVE the number card (kit: above while within 90 px of the open-mouth line; v10 had dropped it 400 px below). Audio null vs v9, clean decode; final + ~/Downloads replaced.
- **2026-10-06 (later): FINAL = v9** — the lip-line captions now MOVE ON THE CUT: a chunk on screen across a cut takes each shot's own height (before, it kept one shot's height and sat on the other shot's mouth for a few frames; found by Pomp's r3 QA), and a chunk that would appear 1-2 frames before a cut appears on it. Kit `ig_capy.py` (moves/show/hide) + `ig_overlay.py`. Picture and sound untouched (audio null -91 dB vs the previous final), clean decode; final + ~/Downloads replaced.
- **2026-10-06: FINAL = v8, CAPTIONS MOVED UP UNDER THE LIPS** (Affan's review: "the distance between the captions and the lips needs to be shorter"). `kit/ig_capy.py` places every chunk just below the speaker's lower lip, per shot (chunk y 786-1044, was a fixed 1428; above the $19,672 card while it is up); picture, cards and sound unchanged from the earlier final. Clean decode, audio = picture; `outputs/mindsetmentor-23k-call.final.mp4` + ~/Downloads replaced.
- **2026-10-06: FINAL = v6** (`outputs/mindsetmentor-23k-call.final.mp4`, copy in ~/Downloads). 3 QA rounds (work/qa/r1-*, r2-*, r3-*), the r3 fixes verified frame by frame on v6 (no frozen cutaway tail, 34 sound cues at -13.0 LUFS / -1.8 dBTP, clean decode, the bank card says "Wire transfer incoming"). Next for this job: Affan's review, then his reaction video and the delivery email draft (Affan sends).
- 2026-10-05: job opened (batch 1, `projects/_onyx-batch-2026-10/BATCH.md`). Research: `_onyx-batch-2026-10/robdial/research.md`.
- **Platform: INSTAGRAM** (@robdialjr: 1.7M followers, ~2.4 reels a day, settled median ~85K = 5 % of followers, top 164K;
  YouTube Shorts: 3.2 a day, median 15.6K = 1.44 % of 1.08M subs → Reels earn ~5x the views per post). Look:
  `presets/youtube-shorts/onyx-samples/` (minimal motion graphics), with a fresh Instagram reference study before the build.
- **Moment (Claude's pick, batch mode):** "The $23,000 call", `bU0EQgb4lr4` ("THIS is all you need to manifest what you want.
  (actually)", 2026-09-18) ~1:47–4:12, minus the ad read (~3:28–4:01). Down to his last few thousand dollars in Austin, his mom
  asks "aren't you worried?", he says no ("if I worry, I'm blocking it"); 2–4 days later his old company's HR calls: "pull over…
  we owe you about $23,000". Why: a told story with dialogue, an objection, a twist and a number at the end (AW-VIRAL-STUDY:
  concrete moments beat advice; Abundance Wisdom's own genre). Runner-up: "the morning my Instagram disappeared" (`G5XZFDGgwQc`).
- **Condition from his team:** credit Rob properly → "Rob Dial · The Mindset Mentor" (or @robdialjr) on screen, not in the hook.
- 2026-10-05 20:30: r1 + ref1 pulled (153 MB 4K VP9, 4.7 MB). Transcribed. Rough cut v1 = `outputs/mindsetmentor-23k-call.mp4`
  (52.5 s, 17 segments, dead-air gate passed). Slice-ASR of every joint (`work/joint_asr.py`): **two joints still leak a fragment**:
  joint 0→1 (~4.9 s, a stray "I" after "dollars": end seg0 in the dip at raw 22.44, pin no_refine) and joint 10→11 (~33.1 s,
  "something AND so I pull over": end seg10 at raw ~84.66, pin no_refine). Then re-splice, re-run joint_asr, fresh-eyes pass.
- Instagram reference study 2 (log it in the preset LESSONS): Mel Robbins (12.8M; reels 1.3–2.1M) = one static shot + white
  caption boxes, no graphics; Jay Shetty 4.8M reel = 1 s of him in B&W, then warm cinematic stock B-roll under his voice, small
  white captions; Rob's own reels = B&W grade + small yellow sentence-case captions. **Plan for this sample:** Rob B&W, warm B-roll
  for the story (faceless when he says "I"), his yellow captions, three graphics only (incoming call, $23,000, bank wire), credit
  line "Rob Dial · The Mindset Mentor", soft bed + SFX on events. B-roll picks so far: Pexels 26448343 (Austin 360 bridge),
  27374367 (hands on wheel), mirror/road shots 12601957 / 18575769.
- **Next:** fix the two joints → B-roll downloads (log here first) → Topaz on the cut ranges → `ig/spec.json` → build → QA.

## Download log (every file logged BEFORE it is pulled)
| # | File | Source URL | Section | Approx size | Status |
|---|---|---|---|---|---|
| r1 | `raw/bU0EQgb4lr4_0140-0425.mkv` (best video ≤2160p, VP9, + the English audio track) | https://www.youtube.com/watch?v=bU0EQgb4lr4 | 1:40–4:25 (2.75 min) | ~350 MB | pending |
| ref1 | `reference/9X2cV2V5Vdw.mp4` (the Short named in the permission email, "Keep space for your happiness", H.264) | https://www.youtube.com/shorts/9X2cV2V5Vdw | whole (17 s) | ~5 MB | pending |
| b01 | `ig/assets/broll/b01-austin-360-bridge.mp4` (Pennybacker / 360 Bridge, Austin, aerial; 2160x3840, 60 fps) | https://videos.pexels.com/video-files/26448343/11953243_2160_3840_60fps.mp4 (Pexels 26448343, free licence) | whole | 68.0 MB | done 2026-10-06 |
| b02 | `ig/assets/broll/b02-day-to-night-timelapse.mp4` (clouds, day to night; 1080x1920, 30 fps) | https://videos.pexels.com/video-files/6666205/6666205-hd_1080_1920_30fps.mp4 (Pexels 6666205) | whole | 19.9 MB | done 2026-10-06 |
| b03 | `ig/assets/broll/b03-sunny-highway-pov.mp4` (windshield POV, sunny highway; 2160x3840, 30 fps) | https://videos.pexels.com/video-files/32793911/13979420_2160_3840_30fps.mp4 (Pexels 32793911) | whole | 95.5 MB | done 2026-10-06 |
| b04 | `ig/assets/broll/b04-hands-on-wheel.mp4` (hands on a steering wheel, faceless; 2160x3840, 30 fps) | https://videos.pexels.com/video-files/27374367/12127400_2160_3840_30fps.mp4 (Pexels 27374367) | whole | 20.9 MB | done 2026-10-06 |
| b05 | `ig/assets/broll/b05-man-looking-at-sea.mp4` (man from behind looking at the sea, faceless; 2160x3840, 24 fps) | https://videos.pexels.com/video-files/13057015/13057015-uhd_2160_3840_24fps.mp4 (Pexels 13057015) | whole | 29.0 MB | done 2026-10-06 |
| b06 | `ig/assets/broll/b06-side-mirror-highway.mp4` (side mirror on a highway; 1080x1920, 30 fps) | https://videos.pexels.com/video-files/12601957/12601957-hd_1080_1920_30fps.mp4 (Pexels 12601957) | whole | 12.6 MB | done 2026-10-06 |
| m1 | `ig/assets/audio/ES_Insight - Megan Wofford.wav` (the music bed: hopeful contemporary classical, 74 BPM, no drums; full mix) | Epidemic Sound recording 2a0d28b0-13a3-4732-b183-b6351dcc0a66 (Affan's subscription, MCP DownloadRecording WAV FULL) | whole (3:33) | 59 MB | done 2026-10-06 |
