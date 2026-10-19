# successstory-vivian-5m: Onyx sample Short for Scott D. Clary (Success Story), guest Vivian Tu (batch 2)

## ▶ STATUS: resume here
- **2026-10-14: Affan swapped the bed: "Thelema", his file (copied to `yt/assets/audio/Thelema.mp3`), from 2.724 s, levels as shipped (YT 13.6 window-held, IG 13 LU under). Mix-only rebuilds (picture PSNR inf vs the approved finals): YT = yt v3, IG = ig v9. Finals + `X:\Claude Projects\Exports\` replaced; old finals kept as `outputs/*.final.prev-epidemic-bed.mp4`. -12.1 / -13.0 LUFS; ig_qa flags only the known "sh*t" asterisk (Affan's taste call, same as the shipped v8).**
- **2026-10-12 11:01: main-session QA r2: YT SHIPS; IG mix fixed → IG final = ig v8** (mix only; picture = v7, max frame diff 0.3/255):
  bed 17.2 → 13.0 LU under the voice (`bed_under_lu` 13: the kit's 17 is outside Affan's 12-14), glass ticks 2 → 8 dB under the voice
  peak (`sfx_rel` tick-glass -6; thud-thin -2, hit-soft -3), a crisp glass tick added on the four entrances that had only a soft whoosh
  (notify 7.58, todo 17.18, compare 38.75 / 42.08). -13.1 LUFS / -1.8 dBTP; cue peaks -4…-12 dB under the voice peak (median -6.4). ig_qa:
  all PASS except the known `punct` false positive (the `*` of "SH*T"). Final + `~/Downloads/successstory-vivian-5m.ig.final.mp4` overwritten.
- **2026-10-12 09:50: BOTH LOOKS FINAL.** Next: Affan's review (taste), then the reaction video (`reference/3XvQd-wj4PI.mp4` = the "before").
  - **YT** `outputs/successstory-vivian-5m.sample-yt.final.mp4` (= yt v2) + `~/Downloads/successstory-vivian-5m.yt.final.mp4`: 44.0 s, 30 fps,
    -12.0 LUFS / -1.7 dBTP. v2 = v1 + her NAME in the hook (main-session QA r1: "Vivian is never named"): "EX-WALL STREET'S VIVIAN TU / VS A
    TIKTOK GUY" (the cleaner drops "·"/","); picture and audio otherwise identical to v1 (diff 0.0, null -228 dB).
  - **IG** `outputs/successstory-vivian-5m.sample-ig.final.mp4` (= ig v7) + `~/Downloads/successstory-vivian-5m.ig.final.mp4`: 44.0 s, 60 fps
    output, -13.1 LUFS / -1.8 dBTP, 24 designed events (5.5 / 10 s), 37 cues, full-window 20 %. Named: hook kicker "Vivian Tu on investing",
    titlecard "THE GUEST · VIVIAN TU · ex-Wall Street trader · 8M+ followers" (3.8 s), credit bar "Success Story with Scott D. Clary · Vivian
    Tu". ig_qa: every check PASS except `punct` (the `*` of "SH*T": a kit false positive, see below). Caption contrast ≥ 6.7:1 on all B-roll.
  - **Better than batch 1 (IG):** zero jump cuts on a one-camera source (every joint on a cut or under a racked card, asserted); the honest
    receipt as a growing "The math" list ($252K paid in · ≈$3.9M at 10 % · "$5M" = 10.8 %); diegetic TikTok notify; the 18 → 60 neon
    re-roll; a ticked "At 60, he says" list; HUD reticles on her answer and on the patient; the closing "$5M vs zero, and need it" compare
    lands on the button; caption contrast measured and shaded per shot.
- **2026-10-12 08:02: YT LOOK FINAL** = `outputs/successstory-vivian-5m.sample-yt.final.mp4` (= v1) + `C:\Users\affan\Downloads\successstory-vivian-5m.yt.final.mp4`.
  44.0 s, 1320 f @30, -12.0 LUFS / -1.7 dBTP / LRA 2.5, clean decode. Build: `python yt/build_spec.py` → `kit/yt_build.py projects/<job> <v>`
  (shots, chunks, cues: `yt/build_spec.py`; storyboard as built: `yt/STORYBOARD.md`). QA by measurement: 52/52 chunks = their words, only
  ! ? quotes; white seam line rows 1089-1094 on all 3 splits; captions constant at y 1092; no held/duplicate frames in any shot; one picture
  jump per cut; every joint on a shot boundary or inside B-roll; cues isolated (whooshes ~21 dB under the voice peak = batch-1 level, thud
  9.7 dB under); bed 13.6 LU under; "shit" muted (digital silence 34.445-34.83). One fresh-eyes reviewer round (Sonnet): 0 HIGH/MED,
  4 LOW framing notes, all fixed in v1 (s10 balloon text under the captions, s11 face off the edge, s14 head cut, s17 wallet unreadable).
  Decisions to flag: "8M+ followers" is NOT printed in the YT look (hook = "EX-WALL STREET TRADER / VS A TIKTOK GUY"; the IG kicker gets it);
  the profanity is muted per the YT README (the cut keeps it; un-mute = delete `audio.mute`).
- **Better than batch 1 (YT):** the white seam line + captions on it from frame 1; zero same-camera jump cuts by construction (every joint
  hidden, asserted in build_spec); 4K source restored to its true 30p + Topaz; a B-roll event as a beat (the light dies on "dark", with a
  reverberant thud); one recurring stock "character" (the same silhouetted old man decrepit → alone); every number literal ("18" candles,
  a "60th" balloon, $500 into a jar).
- **2026-10-12 09:40: IG v6 building** (v5 = a wasted rebuild of v4: a syntax error kept the old spec). Rounds so far: v1 (ig_capy: i03 lips
  under the line; racked neons crossing the caption band; the $500 neon repeated the captions; the $5M→$3.9M re-roll finished on the exit
  frame; the $0 neon unreadable) → v2 (receipt moved to a "The math" list; reticles measured on the window picture) → v3 (`captions.pct` 100;
  list rows shortened; a leak on the 18 cut) → v4 (bright B-roll behind white captions measured 1.0-2.7:1 → `grade.shade` per shot, all
  ≥ 4.6:1 now) → fresh-eyes reviewer (Sonnet) on v4: the math card's bottom inside the caption band (MED-HIGH), the todo's right edge, the serif
  "$0"/"$500" reading "$o"/"$5oo", the patient reticle 50 px off, the silhouette's head cut; gold heroes over her white collar (LOW, kept:
  legible, and moving the stack off the mouth breaks Affan's rule) → v6 fixes all but that one.
  `ig_qa` = PASS on everything except `punct`, which flags the `*` of the starred "SH*T" (captext keeps in-word asterisks, "F*CKED" is in
  its docstring; ig_qa's whitelist lacks `*`): a kit false positive, reported, not worked around.
- **2026-10-12 08:25: PHASE B (Instagram v2) IN PROGRESS.** `ig/build_spec.py` (look v2, same cut, same Topaz base, the YT B-roll reused in
  the window). The 11 joints: ON a cut to in-window B-roll (40, 115, 315, 792, 939, 1046, 1138; 66 inside the roulette) or UNDER a racked
  full-window card (163 titlecard, 440 neon "from age 18 → to age 60", 671 neon "“$5M”" → "≈$3.9M · $252K paid in · 10 %/yr"); asserted.
  Cards: hook (top bar), credit, titlecard (Vivian Tu · ex-Wall Street trader · 8M+ followers), TikTok notify, "$500 a month" neon, the
  18→60 neon, a todo "At 60, he says" (bones aching / decrepit / can't do anything), the $5M→$3.9M neon, a reticle on "okay so don't do
  it", a "$0" neon, the closing compare ($5M and need it vs $0 and need it), leaks on 3 scene changes, the thud on the dying light.
  Captions: stack, accent #F2C14E, "sh*t" starred via `ig/work/transcript.ig.json` (audio unmuted in IG). Build: `kit/ig_build.py
  projects/<job> <v> --preview`, check: `kit/ig_qa.py projects/<job> outputs/<job>.sample-ig.<v>.mp4 --sheet` (must PASS).
- (08:00) the main session said the v2 kit is ready: `presets/youtube-shorts/onyx-samples/kit/V2-HOWTO.md`,
  spec `"look": "v2"`, example `projects/_onyx-batch2-2026-10/kit-demo/ig/build_spec.py`, self-check `kit/ig_qa.py` must PASS. Same cut,
  same Topaz base. Output `outputs/<job>.sample-ig.final.mp4` + `~/Downloads/<job>.ig.final.mp4`.
- 2026-10-12: job opened. Affan APPROVED the pick (`_onyx-batch2-2026-10/PICKS.md`, research `_onyx-batch2-2026-10/clary/research.md` § C #1).
  ONE clip, edited TWICE: `ig/` = the Instagram look (`presets/youtube-shorts/onyx-samples/` + his 2026-10-12 direction: big black bars,
  animated captions, many refined premium motion graphics, crisp SFX, "an expensive video") and `yt/` = the Sean Ryan look
  (`presets/youtube-shorts/onyx-samples-youtube/` + a WHITE LINE on every split with the captions ON it, constant from frame 1).
  PHASE A (this agent, now): the cut + the YT version. PHASE B: the IG version, only after the main session says the v2 kit is ready.
- 2026-10-12 06:41: **time zero normalised.** The download's video starts at pts 9.979 s and its audio at 0 (the audio was cut 10 s
  early at a webm cluster), but BOTH streams' `start_time` tags read 0, so `splice.sh`'s `video_offset` would not have caught it.
  `raw/5Yvqswkt-1A_001320-001555.mkv` = `-ss 9.979` input seek (AV1 stream copy from the first keyframe) + FLAC padded to 0
  (`aresample=async=1:first_pts=0`). **t_file = t_episode − 800.000 s** (verified on the transcript: "our" 56.73 vs VTT 14:16.8,
  "I'd" 105.32 vs 15:05.4). Lip sync measured after the fix: mouth-motion × voice-envelope correlation peaks at +1…+3 frames @60 on
  two spans (corr 0.30 / 0.27), the normal lip lead.
- 2026-10-12 06:50: **transcribed** (`transcript/words.json`, WhisperX GPU). Slice re-ASR (faster-whisper large-v3) of every kept span
  agrees word for word; "60" (79.87-81.01) is one drawn-out word in her "decrepit" voice, not a merged repeat; spoken "wanna" (WhisperX
  "want to"); "$500 a month", "Finally" confirmed.
- **Source facts that drive the build:** 3840x2160 AV1 "60 fps" that is really 30p (every frame doubled; the pair phase flips inside
  the take). The cut range (file 52-111 s) is ONE continuous camera on Vivian, no camera cut at all, so every rough-cut joint must land
  under B-roll or exactly on a shot boundary (no same-camera jump cuts, Affan's rule). Decision: the YT version is built at **30 fps**
  (the content's real rate; the base is decimated 60→30 with `decimate=cycle=2` after the splice, then Topaz); Chronos on a doubled
  60p would turn the whole speaker into 60p "soap" motion against 25/30 fps stock, which the cinematic Sean Ryan look does not want.
- Next: author `cuts.json` (plan below), polish-boundaries, splice, decimate, Topaz FI (GPU lock), faces, storyboard, B-roll.

## The cut (approved beats, research § C #1; file times = episode − 800 s)
Planned segments (file s): "We have now," 52.0-53.3 · [drop "again,"] "turned" 53.9-54.5 · [2.3 s pause] "our economy into a casino." 56.7-58.2 ·
[drop "So again, the rich get richer…" + "And I think"] "people don't wanna hear" 66.2-67.7 · "that the strategy is slow and steady. I saw a
video the other day on TikTok. It was a guy who was like," 68.0-73.2 · "If starting at 18, you put away $500 a month and you invest it."
73.6-77.75 · "Finally, at the time when I am 60 and my bones are aching and I am decrepit and I can't do anything," 78.1-85.8 · "I will have
$5 million and be able to spend all of my time at the hospital." 86.15-90.05 · [drop "And like that was the bit."] "He was like saying that
that advice was bad. And I always like to respond to that like, OK, so don't do it." 92.1-96.9 · "Now you're 60 and decrepit and in a
hospital and you don't have shit." 97.2-100.8 · "Who's taking care of you now? And things are about to get real dark for you." 101.8-104.8 ·
"I'd rather have $5 million and need it than not have $5 million and need it." 105.2-111.15 (button "need it"). ≈ 43 s.
Hook = beat 1 (casino image + contradiction). Debt: "what's wrong with $5 million at 60?". Second loop: "Who's taking care of you now?".
Voices: Vivian = main (white → red); the TikTok guy she quotes (beat 4, "If starting at 18 … at the hospital") = cyan.

## GATE 5 (on screen)
- "8M+ followers" (never 10M); "ex-Wall Street trader" (JPMorgan, AP via Fortune 2026-02-20).
- "$5 million" is the TikTok guy's claim: in quotes / his colour; the honest number is ≈ $3.9M at 10 % ($252K paid in) if a graphic prints one.
- Profanity: captioned "SH*T"; YT look README § 5 = muted in the audio (YouTube monetisation).

## Download log (batch-2 downloads approved by Affan 2026-10-12)
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `raw/5Yvqswkt-1A_<section>.mkv` | https://www.youtube.com/watch?v=5Yvqswkt-1A "Why the Old Money Rules Are Dead (2026-09-14)", 0:13:20-0:15:55 (yt-dlp, best ≤ 2160p + audio) | 213.8 MB (done 2026-10-12, in `work/raw-orig/`) | the source of the cut |
| r1 | `reference/3XvQd-wj4PI.mp4` | https://www.youtube.com/shorts/3XvQd-wj4PI "The worst financial advice." (the Short named in the permission email) | 5.7 MB (done 2026-10-12) | the "before" for the reaction video |
| m1 | `yt/assets/audio/ES_DOX - Lennon Hutton.wav` (music bed, WAV full mix; the track has no drum stem) | Epidemic Sound recording 07e2e4ec-0727-4b5a-a76a-c360d6afb20e "DOX", Lennon Hutton (ambient, dark, restless, pulses; 74 bpm; 3:57), `mcp__epidemic-sound__DownloadRecording` | ~40-70 MB | the YT bed (≈ 13.6 LU under the voice) |
| y02 | `yt/assets/broll/y02-roulette.mp4` | Pexels, free licence: https://www.pexels.com/video/35728855/ → https://videos.pexels.com/video-files/35728855/15142669_3840_2160_60fps.mp4 | ~30-90 MB | "turned our economy into a casino" |
| y04 | `yt/assets/broll/y04-tortoise.mp4` | Pexels: https://www.pexels.com/video/30051567/ → https://videos.pexels.com/video-files/30051567/12890034_2160_3840_60fps.mp4 | ~30-90 MB | "slow and steady" |
| y05 | `yt/assets/broll/y05-phone-scrolling.mp4` | Pexels: https://www.pexels.com/video/38410498/ → https://videos.pexels.com/video-files/38410498/16310022_2160_3840_25fps.mp4 | ~30-90 MB | "I saw a video the other day" |
| y06 | `yt/assets/broll/y06-guy-filming-himself.mp4` | Pexels: https://www.pexels.com/video/8360258/ → https://videos.pexels.com/video-files/8360258/8360258-uhd_2160_4096_25fps.mp4 | ~40-120 MB | SPLIT bottom, "on TikTok, it was a guy who was like" |
| y07 | `yt/assets/broll/y07-number-18-candles.jpg` (still) | Pexels photo: https://www.pexels.com/photo/8014933/ → https://images.pexels.com/photos/8014933/pexels-photo-8014933.jpeg | ~1-4 MB | "if starting at 18" |
| y08 | `yt/assets/broll/y08-money-into-jar.mp4` | Pexels: https://www.pexels.com/video/7710820/ → https://videos.pexels.com/video-files/7710820/7710820-uhd_4096_2160_25fps.mp4 | ~30-90 MB | "you put away $500 a month" |
| y09 | `yt/assets/broll/y09-trading-app.mp4` | Pexels: https://www.pexels.com/video/6799742/ → https://videos.pexels.com/video-files/6799742/6799742-uhd_2160_3840_30fps.mp4 | ~20-60 MB | "and you invest it" |
| y10 | `yt/assets/broll/y10-60th-birthday-balloon.mp4` | Pexels: https://www.pexels.com/video/7866820/ → https://videos.pexels.com/video-files/7866820/7866820-hd_1080_1920_30fps.mp4 (native vertical 1080) | ~5-20 MB | "when I am 60" |
| y11 | `yt/assets/broll/y11-elderly-man-in-pain.mp4` | Pexels: https://www.pexels.com/video/7299358/ → https://videos.pexels.com/video-files/7299358/7299358-uhd_2160_3840_30fps.mp4 | ~20-60 MB | SPLIT bottom, "my bones are aching, I am decrepit" |
| y12 | `yt/assets/broll/y12-man-cane-sits-down.mp4` | Pexels: https://www.pexels.com/video/8860233/ → https://videos.pexels.com/video-files/8860233/8860233-uhd_4096_2160_25fps.mp4 | ~40-150 MB | "and I can't do anything" |
| y13 | `yt/assets/broll/y13-cash-briefcase.mp4` | Pexels: https://www.pexels.com/video/6266255/ → https://videos.pexels.com/video-files/6266255/6266255-uhd_2160_3840_25fps.mp4 | ~20-60 MB | "I will have $5 million" |
| y14 | `yt/assets/broll/y14-cane-hospital-corridor.mp4` | Pexels: https://www.pexels.com/video/32767737/ → https://videos.pexels.com/video-files/32767737/13968921_3840_2160_60fps.mp4 | ~30-90 MB | "all of my time at the hospital" |
| y16 | `yt/assets/broll/y16-patient-hospital-bed.mp4` | Pexels: https://www.pexels.com/video/6011438/ → https://videos.pexels.com/video-files/6011438/6011438-uhd_3840_2160_25fps.mp4 | ~20-60 MB | "now you're 60 and decrepit and in a hospital" |
| y17 | `yt/assets/broll/y17-empty-wallet.mp4` | Pexels: https://www.pexels.com/video/7924953/ → https://videos.pexels.com/video-files/7924953/7924953-uhd_2160_3840_24fps.mp4 | ~20-60 MB | SPLIT bottom, "and you don't have sh*t" |
| y18 | `yt/assets/broll/y18-alone-by-window.mp4` | Pexels: https://www.pexels.com/video/8860241/ → https://videos.pexels.com/video-files/8860241/8860241-uhd_2160_4096_25fps.mp4 | ~40-120 MB | "who's taking care of you now?" (same man and room as y12) |
| y19a | `yt/assets/broll/y19a-fluorescent-light.mp4` (to be REVERSED: the light goes off) | Pexels: https://www.pexels.com/video/9945022/ → https://videos.pexels.com/video-files/9945022/9945022-uhd_2160_3840_24fps.mp4 | ~10-40 MB | "things are about to get real dark for you" |
| y19b | `yt/assets/broll/y19b-hallway-lights.mp4` (alternate, reversed) | Pexels: https://www.pexels.com/video/6279825/ → https://videos.pexels.com/video-files/6279825/6279825-uhd_2160_3840_24fps.mp4 | ~20-60 MB | same row, alternate |
| y05b | `yt/assets/broll/y05b-man-phone-in-bed.mp4` | Pexels: https://www.pexels.com/video/7131726/ → https://videos.pexels.com/video-files/7131726/7131726-uhd_2160_4096_30fps.mp4 | ~30-90 MB | replaces y05 (its screen runs Instagram Reels with real usernames and a footballer's likeness: wrong app for "on TikTok"); the screen faces away |
| y02b | `yt/assets/broll/y02b-roulette-portrait.mp4` | Pexels: https://www.pexels.com/video/9954987/ → https://videos.pexels.com/video-files/9954987/9954987-uhd_2160_3840_25fps.mp4 | ~40-120 MB | replaces y02 (its 9:16 crop is mostly the spindle; this one shows the whole wheel) |
| y11b | `yt/assets/broll/y11b-elderly-man-in-pain-wide.mp4` | Pexels: https://www.pexels.com/video/7297851/ → https://videos.pexels.com/video-files/7297851/7297851-uhd_3840_2160_30fps.mp4 | ~20-60 MB | replaces y11 in the SPLIT bottom (landscape panel; same man, wider) |
| y17b | `yt/assets/broll/y17b-empty-wallet-wide.mp4` | Pexels: https://www.pexels.com/video/11099870/ → https://videos.pexels.com/video-files/11099870/11099870-hd_1920_1080_24fps.mp4 | ~10-40 MB | replaces y17 in the SPLIT bottom (QA r1 LOW: the black wallet read as "a dark object"; this one opens an empty brown wallet, landscape) |
| p0 | `work/pexels/thumbs/<id>.jpg` | Pexels search-result preview thumbnails (images.pexels.com, `w=750`), ~60 candidates from 24 searches (casino, tortoise, phone scrolling, man recording himself, money jar, stock app, elderly man, back pain, cane, cash stacks, hospital corridor/bed, empty wallet, lonely elderly, lights off) | ~60-120 KB each, ≤ 120 files | B-roll selection only |

Actual sizes (done 2026-10-12): y02-roulette.mp4 29MB · y02b-roulette-portrait.mp4 68MB · y04-tortoise.mp4 137MB · y05b-man-phone-in-bed.mp4 25MB · y06-guy-filming-himself.mp4 70MB · y07-number-18-candles.jpg 3MB · y08-money-into-jar.mp4 19MB · y09-trading-app.mp4 23MB · y10-60th-birthday-balloon.mp4 5MB · y11-elderly-man-in-pain.mp4 30MB · y11b-elderly-man-in-pain-wide.mp4 25MB · y12-man-cane-sits-down.mp4 31MB · y13-cash-briefcase.mp4 24MB · y14-cane-hospital-corridor.mp4 19MB · y16-patient-hospital-bed.mp4 22MB · y17-empty-wallet.mp4 30MB · y17b-empty-wallet-wide.mp4 24MB · y18-alone-by-window.mp4 8MB · y19-light-dies.mp4 5MB · y19a-fluorescent-light.mp4 19MB · y19b-hallway-lights.mp4 32MB · ES_DOX - Lennon Hutton.wav 66MB. Rejected (kept in work/rejected-broll/ or unused): y05 (Instagram UI), y02 (crop = spindle), y11 (portrait crop too tight), y17 (unreadable), y19b (alternate, unused). y19-light-dies.mp4 = LOCAL derivative of y19a (source frames 22-78, reversed).
