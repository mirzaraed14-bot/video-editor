# BRIEF: Double Coverage sample, Masvidal UFC pay (Onyx, YouTube look)

## ▶ STATUS 2026-11-26 ~09:00 PKT (Sonnet builder): BUILDING, v3 check render in progress. Not final.
- Cut done: `outputs/doublecoverage-masvidal-ufc-pay.mp4` 39.74 s, 1191 f, 29.97 fps, 8 pieces, all edges frame-grid hand-set (`work/cut/make_edl.py`), large-v3 read of the cut verbatim.
- Fallbacks taken (DIRECTION § 1): "But" KEPT (voiced flap, no gap: P2b starts on "But at least minimum"), "fight, so then" kept continuous, "you know," kept, "like you said," kept (so S11-S13 = ONE continuous run, no joint). Audio wording: "against Usman IN five days notice", "the money THAT I brought in", "called upon me", UFC (ASR hears "UC").
- Burns clip: `ufc-rise-of-gilbert-burns.mp4` (the first pull hit a bot check). Boxing = `pbc-wilder-fury2-full` 720p (S3 pan on the face-off, S11 bottom arena wide).
- Re-run: `bash projects/doublecoverage-masvidal-ufc-pay/yt/run_all.sh vN [grade|overlay]`; cut: `work/cut/make_edl.py` -> `splice_local.sh` -> `retime.py` (whisperx venv); B clips: `yt/cutclips.py`.

(older status below)
## ▶ STATUS 2026-11-26 ~05:20 PKT: SEQUENCE v2 sent for Affan's OK. Nothing built. State and log: `RUN.md`; the sequence: `SEQUENCE.md`.

## The prospect
- Double Coverage Podcast (@DOUBL3COVERAGEPODCAST, 565K subs, host Mystic Zach; N3on appears). Yes from Zach Hirsch 2026-11-24
  17:03 UTC: "Yep, that's fine but our YouTube shorts page is now @doublecoveragetv so would prefer if you reviewed a clip from there."
- Sponsors: DraftKings (read in this episode), Hims, Lucy, MyBookie. Weekly 30-80 min studio interviews.
- **Check 5 fails** (their Shorts are strong: median 6.2 % of subs on @doublecoveragetv). Affan said build anyway (relayed by the main
  Onyx session, ~04:10 PKT 11-26). Numbers: `RUN.md` § Check 5.

## Platform pick (PLAYBOOK § 0): YouTube-first, one look
1. The yes points at a YouTube Shorts page.
2. Instagram: none found. All 39 episode descriptions and 121 Short descriptions list only @doubl3coverage (5 posts, 3 followers); @mysticzach is another
   podcast's page (742 followers, last reel ~Jan 2025). Their clips reach IG only through clipper pages (@propodcastclips, 21 likes).
3. So: the YouTube look (`presets/youtube-shorts/onyx-samples-youtube/`), 30 fps native, no Topaz (Onyx rule since 10-31).

## Sources (download log)
| File | From | Size | Use |
|---|---|---|---|
| `research/shorts/lcHRLhBrPCA.mp4` | @doublecoveragetv Short "How Masvidal lost $20M to the UFC" (1080x1920, 29.97) | 6.6 MB | reference: the Short we enhance |
| `research/shorts/kqL9xIn468o.mp4` | @doublecoveragetv Short "When MJ & LT Golfed for $38K" (1080x1920, 23.976) | 13.3 MB | candidate, not picked |
| `research/episodes/7_gYEexEk00.audio.m4a` | the Masvidal episode audio (55:27) | 53.8 MB | full transcript (large-v3) |
| `research/episodes/7_gYEexEk00.pay-2130-2605.mkv` | the episode VIDEO, 21:30-26:05 (1920x1080 VP9, 29.97, the best offered; clock = episode 1289.4546 s + t) | 86.5 MB | the build source + frame check (`research/frames/beats-sheet.jpg`) |
(paths relative to `projects/_onyx-doublecoverage-2026-11/`)

### B-roll (official sources, paths relative to this job)
| File | From | Size (est.) | Use |
|---|---|---|---|
| `yt/assets/broll/src/ufc251-fight-motion.mp4` | UFC (official) "UFC 251: Fight Motion" ULKXidThmdY, whole 325 s, H.264 <=1080p | ~100 MB | beat 1 (the fight, slow motion) |
| `yt/assets/broll/src/pbc-wilder-fury2-highlights.mp4` | Premier Boxing Champions (official promoter) "Wilder vs Fury 2 HIGHLIGHTS: February 22, 2020" yyLotcY6Ego, whole 93 s | ~30 MB | beat 2 (a boxing mega-fight), beat 7 split |
| `yt/assets/broll/src/ufc251-weighin-faceoffs.mp4` | UFC (official) "UFC 251: Weigh-in Faceoffs" IgzTO211Wec, whole 260 s | ~70 MB | beat 1 alternative (both faces still: the name label) |
| `yt/assets/broll/src/ufc-burns-vs-woodley-free-fight.mp4` | UFC Espanol (official) "#UFCWinnipeg Pelea Gratis: Burns vs Woodley" 64eTWP_STxw, section 0:00-6:00 | NOT PULLED | 07:19 "Sign in to confirm you're not a bot" on this one video (the next 3 pulls worked, so no IP block; the video is region-blocked in BR/KR) |
| `yt/assets/broll/src/ufc-rise-of-gilbert-burns.mp4` | UFC (official) "Rise of Gilbert Burns" YOWv7qvkNYU (2020-05-25, before UFC 251), whole 218 s | ~60 MB | beat 5 (Gilbert Burns), replaces the UFC Espanol pull |
| `yt/assets/broll/src/pbc-wilder-fury2-full-0000-0500.mp4` | Premier Boxing Champions (official) "Wilder vs Fury 2 FULL FIGHT: February 22, 2020" GDM-ov7ZR40, section 0:00-5:00: came at 1280x720 59.94 (the upload has no 1080p in any codec: a 1080p request at 07:42 answered "Requested format is not available") | 133 MB | beats 2 + 7 (boxing): 720p is the best that exists |
| `yt/assets/broll/src/ufc-dana-white-ufc251.mp4` | UFC (official) "Dana White talks UFC 251 trends, Masvidal stepping in, Fight Island" OhnkUrjWBzM, section 0:00-2:00 | ~35 MB | beat 5 ("me and the UFC ... negotiations") |
| `yt/assets/broll/src/ufc-masvidal-last-7-days.mp4` | UFC (official) "Jorge Masvidal on the last 7 days, making weight and fighting for a title" dV9c9pg6zAI, whole 185 s | ~50 MB | beat 8 (five days' notice, Fight Island) |
| `yt/assets/broll/src/ufc251-super-necessary-promo.mp4` | UFC (official) "UFC 251: Usman vs Masvidal - Super Necessary" K702FXSAn7k, whole 191 s | ~55 MB | spare fight-week / Fight Island shots |
(B-roll pulled 2026-11-26 by main through `yt/assets/broll/pull_broll.sh`, one spaced queue; ESPN DOC captured by the builder, URL in DIRECTION.md.)


## Audio (measured on the episode audio, 21:30-26:00)
- The splice of the v2 cut (36.66 s, `research/cutcheck/splice-v2.wav`): -27.6 LUFS integrated. The chapter's peak is -6.5 dBFS, its noise floor -57.7 dB:
  no music bed under the voice. It needs the measured static gain (voice-gain.py), no denoise expected.
- The ASR re-read of the splice reads every joint as a clean sentence (`research/cutcheck/splice-v2.txt`, small.en; large-v3 slice
  ASR on every joint at build).

## Their Short (what we beat)
16 s, 84,303 views at 30 days. Speaker on top + UFC 251 / boxing footage below, one-word Impact-style captions, a "DOUBLE COVERAGE
PODCAST" bug. It ends mid-word ("I didn't get 20"). The teardown table, ours vs theirs: `SEQUENCE.md`.

## What this sample does better than the last one (every-video-better rule)
Barbell Logic (11-23) had a talking coach and a demo. This one carries a story with a twist, and its receipt is a real news story
on screen (ESPN, 2020-07-06), the batch-3 DOC device. It runs one number end to end ($20M), so the viewer never has to reconcile
two figures.
