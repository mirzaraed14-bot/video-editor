# tftc-hospital-bill-reaction: Affan's reaction to our TFTC samples (ABW10 sequence "TFTC reaction")

## ▶ STATUS: resume here
- **2026-10-19 PREPARED IN ABW10** ("TFTC reaction", bin "Onyx batch 3 reactions (2026-10-19)"): 170.87 s (2:50.9); razored at every
  beat/view edge, layout (102 clip edits, --layout-check 0 leaks at keys; 37 between-key slips max 4.6 px into the top bar on single
  frames; the 20 "gaps" are the full-height Films-app player meeting black, covered by the showcase frame), V3 showcase frames / V4 MG
  (16 graphics) / V5 captions, house chain +6 dB into −6 dBFS on all 49 A1 clips, 36 SFX on A2 + A4, Observatory bed on A3 at −19.8 dB
  from 1.13 s, 25 ms ramps at the hard sample edges 15.0 / 17.35 / 73.7 / 86.7 / 91.83 / 129.0 / 136.18 (afade.py), --verify 0
  problems. Proof: `work/grabs-sheet.jpg` (Premiere program-monitor grabs). He exports.
  Plan: 18 MG events (1.46 per 10 s of his 123 s talk), pointing 47 %, labels 0, face-only 27.7 % (16 pieces, 6 punch-ins), SFX 37 cues,
  no sound over 35 %. Review fixes before applying: the Short's first 2.35 s framed BEFORE the description panel opened (view
  short0), the sound-disc view lifted off the taskbar, a select that pointed at a caption the Short no longer showed (dropped), the
  channel card's verified tick removed (TFTC has none on its page; overlays.py channel_card now takes "verified": false), the label
  "RE-CUT FOR MARTY, UNASKED" dropped (he said "in my free time", not "unasked").
- Shared-tool note: apply.py's _overhang() regex matches "layer (" inside a view NAMED "player" (crash in --layout-check): views here
  are called "films".
- Inputs: OBS `raw/2026-10-19 06-32-17.mp4` (copy of E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Batch Batch\), camera
  `X:\Recordings\Onyx\C1380.MP4` (sync `../_onyx-batch3-2026-10/reactions/sync/sync-C1380-06-32-17.json`, +96.42 s, −42 ppm).
- He played: the YouTube look = `projects/tftc-hospital-bill/outputs/tftc-hospital-bill.sample-yt.v1.preview.mp4` (= v1, 38.04 s), the
  Instagram look = `Exports/batch3-drafts-preview/tftc-hospital-bill.sample-ig.final.preview.mp4` (= ig final, 38.05 s), in the Windows
  Films app full screen (video x 878-1684, y 0-1440).

## The cut (3:00 cap, Affan 2026-10-19) — `keep.json` → tools3/author3.py → splice RENDER=0 → polish → splice → `work/pins.json` → seqmap3
- **49 segments, 170.867 s (2:50.9) of 651.0 s raw.** Joints proved twice with cutcheck.py (`work/cutcheck.txt`, `work/cutcheck2.txt`),
  then by the per-stretch WhisperX of the final cut (`work/tightasr/`), which caught "TFTC" losing its last letters (pin 30.18 → 31.13)
  and "before" losing "be-" (pin 106.367 → 106.267).
- Kept: intro (4th take), name + 600M, their Short 2.35 s ("it's gonna be off privacy, it's gonna be off trust"), the title critique,
  sad music, the 2-minute length (max 55 s / 1 min), "20 seconds in I cannot understand what this video is about", "for me, not into
  crypto … requires too much prior context", "editing is bland: no animations, overlays, zooms", OUR YouTube cut WHOLE (0-38 s, with
  his 10-second comment at its pause), his "38 seconds" verdict, the Instagram cut 0-7.2 s, why Instagram prefers minimal, the outro.
- Cut for the cap: the 15M / 20M viral-short tangent, the microphone/noise-gate critique (he says "not my field"), the Thelema music
  tip, "I'm listing all the problems", "I'm not going to review the whole two minutes", the approvals line, fillers / restarts.
- **Graft:** our YouTube cut's first 1.8 s come from his FIRST start (raw 419.37, residual −44 dB vs the preview); his clean third start
  (raw 433.71) carries the aborted play's tail under its first 1.5 s; joined at sample 1.80 (a quiet gap, ±10 ms).
- Sample ranges (sequence): Short 15.00-17.35 · YT 73.70-86.70 + 91.83-116.83 · IG 129.00-136.18.
- Captions source: `transcript/words.tight.json` = tools3/tightasr.sh (per talk stretch) + tightwords3.py `--shift 18.45 0.1` (the
  "before" pin came after the ASR pass) + fixes for/before, it's/is, end/and, going to/gonna (work/tightwords.cmd.json).
- Private screen: the Claude app (raw ~357-372, 545) and File Explorer (raw 372-418) are all inside removed material.

## Look (Reaction E): see build_plan.py docstring. Bed: Epidemic "Observatory" (Out To The World), new, source_in 1.144, −19.8 dB
(bed −11.2 LUFS → ≈ −31 LUFS, 13.6 LU under his voice after +6 dB). Voice: his talk −23.4 LUFS → +6 dB into −6 dBFS.

## Download log
| # | File | Source | Size | Why |
|---|---|---|---|---|
| a1 | `assets/channel-avatar.jpg` | yt3.googleusercontent.com s900 (URL from `_onyx-batch3-2026-10/tftc/meta/shorts_flat.json`; no youtube.com request) | 148 KB | the channel card's real profile picture |
| a2 | `audio/ES_Observatory - Out To The World.wav` | Epidemic Sound recording 0c47304b-4e50-43b2-8230-2397e7991316 (WAV, full) | 55 MB | the bed (never used before) |
