# gta6-all-fit-inside · Affan Afterhours YouTube Short ("They All Fit Inside", his v5 script)

▶ STATUS: resume here (2026-11-04 23:49): **v4 DELIVERED FOR HIS REVIEW** -> `X:\Claude Projects\Exports\afterhours-gta6-all-fit-inside.v4.mp4` (+ proof-sheet.v4; v3 stays beside it, superseded). His notes on v3 (2026-11-04) applied:
(1) "All of them" = his Shorts slow-mo: 0.8x, pitch kept, punched in 1.16, Vine boom in the breath after "them" (his pick "0.8x + Vine boom";
`work/cut/slowmo.py`, edges `sh()`), (2) every footage B-roll shot + the footage in the crowd / clock / sunset cards motion-interpolated
(`yt/assets/build/smooth_broll.py`, `mg_gta.py clip()`), (3) v4 itself: Topaz Iris 4K base (`outputs/gta6-all-fit-inside.topaz.slow.mov`),
sharpened (cards excluded), "~10x". 1080x1920, 59.94, **3726 frames, 62.16 s**, -12.2 LUFS, TP -2.2 dBFS, 17 swishes + the boom
(cue_check PASS: boom -3.8 dB beside the voice, swishes 19-22 under). QA: every shot moving (YDIF per shot vs v3, nothing frozen), audio vs
the slowed base ncc 0.992-0.999 at lag 0.0 ms, slow-mo frames + detail crop viewed. Music answer still open (no bed). Not uploaded, nothing committed.
Memory note: Adobe apps held ~50 GB tonight; builds now retry on MemoryError (see the v4 command in work/build_v4e.log's caller) and cards
render one per process. Regenerable bulk: `outputs/gta6-all-fit-inside.topaz.mov` (13 GB, unslowed, superseded by topaz.slow.mov),
`work/slowmo/hq_*.mov`, `yt/work/*.raw.*` (prune once he approves).

1080x1920, **59.94 fps native, 3713 frames, 61.95 s**, -12.0 LUFS, true peak -2.2 dBFS, 18 transition swishes (19.0-22.1 dB under the voice,
cue_check PASS), no bed, no watermark. Waiting on: his notes, and his MUSIC answer (he scores it -> keep as is; we lay his script's tension
drone + sub hits -> `background-music` pass + `audio.bed` in the spec). Not uploaded, nothing committed.
QA on v3: audio vs the base cut ncc 0.994-1.000 at lag 0.0 ms (5/20/32/45/58 s); head steady at the 3 face-shot jump cuts (890, 3496,
3568); frame 0 = the split with the five covers, ONE text block until the card leaves, captions from ALL OF THEM (t0 3.75); 30-frame
proof sheet viewed; hair top >= ~150 px on the face shots (v1 had ~80: eye line 0.32 -> 0.36). NOT run (lean mode, no subagents): the
rough-cut fresh-eyes pass and the edit-review rounds; nothing checked by ear (no playback here).
Rebuild: `python yt/build_spec.py` -> `python presets/youtube-shorts/onyx-samples-youtube/kit/yt_build.py projects/gta6-all-fit-inside <ver>`
(`--skip overlay,mix` for picture-only). A note = data + ONE finish render.

Changes from the approved sequencing (say so in the delivery note): the storage bars live in the "drive" card during the list (so the
Newswire receipt owns "Rockstar just confirmed it's up to 212 gigs"); swamp and forest lines = trailer footage first, then the postcard's
text card with the line underlined pink (the postcards are portrait; text would be ~7 px otherwise); no official salon shot exists, so the
gym holds through "gyms, salons"; the crowd card cuts T1's close crowd into the launch trailer's beach.

Kit changes (opt-in, every other job unchanged; backups `*.bak-2026-11-04-gta`): yt_picture.py `whip_profile` passed into shots.json cuts,
and a >40 fps base frame-doubles a 30 fps clip instead of conforming it (it would play 2x); yt-captions.js `popRep`; yt_overlay.py
`captions.pop_rep` + `hook.grad`. Face scan: 47 chair false-face frames dropped (`yt/work/faces.raw.json` keeps the raw scan).

## The ask (2026-11-04, verbatim)
"this video will be edited in the scott clary yt short style, this is a yt short, use gta overlays, explain with motion graphics, and the
motion graphics theme will be black and pink"
Session brief on top of it: no Scott branding (no watermark), black + pink MG palette, official GTA 6 trailer/screenshot footage + his own
GTA 5 B-roll cut on the words (no leaks, fan maps, AI Rockstar characters), each point explained with an MG, sequencing approved before the
build, code-built MP4 at native 59.94 into `X:\Claude Projects\Exports\`, he reviews before posting. Usage TIGHT: lean mode, no new subagents
without asking, builders Sonnet, never Fable. Work in silence.

## Source
- Raw: `X:\Recordings\Afterhours\C1445.MP4` (copied to `raw/C1445.MP4`, original untouched): 1920x1080 h264 59.94p, PCM stereo 48 kHz
  (the camera DOES carry the voice on this shoot), 189.19 s, recorded 2026-11-04 19:31. Room = the video 24/26 setup (Skool neon sign, YouTube
  plaque, red mic, leather chair); he reads the script off a screen to his LEFT.
- Script: `X:\Claude Projects\GTA 6\sweeps\shorts-sweep-2026-11-04.md` § "v5: FINAL" (edit cues, fact table, Don't-say list, prediction).
  He recorded v5 with small wording changes ("A city with narrow roads", "and the NPCs", "So they made the days longer as well").
- Transcripts: `transcript/words.json` (WhisperX: words right, TIMES WRONG between ~55 and ~120 s, it collapsed the retakes) and
  `work/cut/bursts.json` (per-burst faster-whisper large-v3 on RMS bursts, 39 bursts: the times to cut from). `work/cut/fw_raw.*.txt` =
  the whole-file verbatim pass. Eye line: `work/eyeline.json` (Otsu 0.343, separation 4.41 SD).
- Channel: Affan Afterhours, confirmed by the script's home (the GTA 6 workstream sweep) and its pinned-comment plan (the video 26 long-form).

## Look decisions (from the ask + the Scott kit)
- Kit: `presets/youtube-shorts/onyx-samples-youtube/` (README, CLIENT-SHORT-RECIPE), newest reference build
  `projects/_client-scott-clary/herjavec-dwts-crash/` (spec pattern `yt/build_spec.py`), sound template
  `projects/_client-scott-clary/patron-20000-cases/yt/sound.py`.
- Pink = `#EE2A9A` (the channel's current card pink, `presets/youtube/affan-afterhours-facecam/README.md` § 4b; the older channel
  README uses `#FF2E9A`). Gold hook word → pink; red caption wipe → pink; mg-cards teal/navy → pink on black.
- No watermark, no CTA (no Scott branding; his GTA Short).
- Frame 1 = SPLIT (cam top, the five covers swallowed below) + ONE text block "ALL 5 FIT / INSIDE" 0-3 s; captions from ~3.2 s.

## Build-time notes (do NOT forget)
- The kit's frame numbers are tuned for a 24/30 base: the whip, the caption pop and its 3-4 frame lead, the 4-frame edge snap, the
  head-track sigma. At a 59.94 base they run twice as fast: scale them (add options defaulting to today's behaviour so no other job
  changes). `workflows/mg-cards.py` hardcodes FPS 30 and the teal/navy palette: add `--fps` / palette options, defaults unchanged.
- Official B-roll is 30 fps (trailers, Extended Look) or 29.97 (GTA V gameplay): doubled at 59.94.
- Check in the audio before captions: "If Rockstar opened" (both ASR passes; cut if separate), "clock fell/felt too fast" (script: felt),
  "Headphone shop" (script: "a headphone shop").
- Reading: swamp (55.14-58.36) and forest (64.37-68.41) lines are 100 % reading → full-frame pictures only. Partial looks inside the
  list (~31 s), the shop list (~90-91 s, before the take) and before "because the projections" (~134-135 s, before the take): re-check
  on the cut.
- The kit's payoff rule (mean shot ≥ 3.5 s after the turn) does not fit a stacked list: set `allow_fast_payoff` with the reason.

## Sources (official only; fill in as assets land)
| Use | File | From |
|---|---|---|
| Grassrivers postcard ("far deadlier predators") | `X:\Claude Projects\GTA 6\screenshots\rockstar-grassrivers-deadlier-predators.png` | rockstargames.com/VI, his capture 4 Nov |
| Mount Kalaga postcard ("paranoid radicals") | `X:\Claude Projects\GTA 6\screenshots\rockstar-mount-kalaga-paranoid-radicals.png` | same |
| Trailer 1 / Trailer 2 | `projects/gta6-pc-release/broll/Grand Theft Auto VI Trailer {1,2}.mp4` (1080p30) | Rockstar |
| Launch Trailer (gym, bank, stores) | `E:\Bullshit Folder\Henry\Grand Theft Auto VI Launch Trailer.mkv` (2160p30 VP9, 90.0 s) | Rockstar, 15 Oct (verified: its end card reads NOVEMBER 19, 2026 / PRE-ORDER NOW, and the Newswire lists the 15 Oct Launch Trailer) |
| Extended Look | `projects/gta6-pc-release/broll/GTA 6 Official Extended Gameplay.mp4` (index: `projects/gta6-day1-mistakes/broll/SHOTS.md`) | Rockstar |
| GTA V official gameplay | `projects/gta6-pc-release/broll/GTA 5 Official Gameplay Video.mp4` (H.264 720p) / `E:\Bullshit Folder\Canelo\...` (VP9 1080p) | Rockstar |
| Box covers III / VC / SA / IV / V | to fetch (`E:\Bullshit Folder\GTAV_Official_Cover_Art.jpg` has V) | Rockstar cover art |
| Newswire "up to 212 GB" | to capture: rockstargames.com/newswire/article/k4ak9okk485712 (`workflows/page-record.mjs --full`) | Rockstar, 3 Nov |
| Facts on cards | 600,000 vs 55,000 (Garbut to NYT via TechRadar / PC Gamer); "horrifying" (Nelson, Bloomberg 14 Oct via PC Gamer); 80 h (NYT 27 Aug) | his v5 fact table |
| NOT used | `E:\Bullshit Folder\Henry\Grand Theft Auto V Gameplay (PC HD) [1080p60FPS].mp4` (third-party upload), the xQc Extended Look reaction | - |

## Pick test + Bombas (Scott ENGINE; scored, his pick stands; nothing written to Scott's files)
Pick test 1 / 3; Bombas 6.5 / 11 = worse (no B1 / B4, structural for a solo explainer). Breakdown in SEQUENCING.md.

## Prediction (his sweep, v5, logged 4 Nov, mirrored verbatim)
- **YouTube Shorts 5K–150K. IG 10K–200K. TikTok 5K–100K.**
- **Biggest failure risk:** 212GB fatigue in the first second. The swallowed covers have to be frame 1.
- **Pre-mortem, 5K:** number fatigue; a newsreader delivery; the list of shops in the city beat slows things down.
- **Pre-mortem, 500K:** every generation sees its first GTA swallowed; each beat is a new kind of size; "horrifying" and "too fast" land as menace; hours → years at the end; the age war in the comments.

## Decisions and checks after v3 (2026-11-04, own review)
- Swishes screened for narrow tones (feedback-premium-sfx test, max FFT bin above 1 kHz vs its +-40-bin neighbourhood, p90 over the loud
  frames): k1-swish-classic 10.6 dB, k2-dark-fast 11.6 dB, k3-fast-passby 12.8 dB (reject > 20). The Herjavec / Harary-approved set.
- Pops settle at 1.08 (Herjavec 1.10): with the eye line at 0.36 a 1.10 pop puts the hair top at ~140 px, under the ~160 px floor.
- "10x" on the interiors card -> "~10x" (his v5 fact table: Garbut said "an order of magnitude"; "exactly ten times" is on Don't-say).
  "OVER 10x" on the animations card stays (600,000 / 55,000 = 10.9).
- v4 = Topaz Iris 2x on the base (`--no-fi`: the raw is native 59.94, nothing to interpolate) + the sharpen pass (cards renamed mg-*, so
  workflows/sharpen-picture.py leaves the type unsharpened).
- NOT done (lean mode, said in the delivery): the effects-catalog pass and the "better than the last one" line from CLAUDE.md's learning
  loop, the rough-cut fresh-eyes pass, the edit-review rounds; nothing checked by ear.
