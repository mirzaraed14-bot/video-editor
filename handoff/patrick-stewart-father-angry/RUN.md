# RUN: "Why Patrick Stewart's Father Was So Angry 💔" (Abundance Wisdom short)

## ▶ STATUS: resume here (2026-10-31 ~13:30): DELIVERED v2 (57.77 s) → at his review
- His note on v1: "because he just made me angry and fearful when he was around --- remove this and it will be under
  60" → `seq/edl.py` piece + cover commented out (v1 data `seq/edl.v2.json`), captions.txt 5 lines out, dialogue + mix
  re-built (-14.10 LUFS / -1.60 dBTP), picture = `picture_v1` minus frames 3024-3257 (`renders/picture_v2.mov`),
  finish re-rendered from B6 only (`renders/fin_tail_v2.mp4`, frames 2758-3466; caption turbulence field pinned to the
  v1 length so the splice can't jump) → `outputs/patrick_finish_60_v3.mp4` → **`Patrick Stewart Father.mov` 57.77 s,
  1733 f, 46.8 Mb/s, -14.1 LUFS / -1.6 dBTP, MD5 8ad7c651…** in Final Renders + Exports; v1 kept as `(v1 61.7s).mov`.
  Also fixed on the way: captions/make_words.py now applies edl.py's measured word overrides (the PBS "And" was timed
  1 s early in v1's caption, on "around").

## (previous) STATUS (2026-10-31 ~12:40): DELIVERED v1 → at his review
- `Patrick Stewart Father.mov` (61.67 s, 1850 f @ 30 fps, 45.4 Mb/s, PCM 48 kHz, -14.1 LUFS / -1.6 dBTP measured on the
  file) in `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\` + `X:\Claude Projects\Exports\` (MD5 582aa12e…, same as
  `outputs/`). § 8 QA + § 9 report: `REPORT.md`. Edges `proof/final_edges.jpg`, 1 s sheet `proof/final_sheet.jpg`.
- Picture chain: `renders/picture_v1.mov` → `build/finish.py render` → `outputs/patrick_finish_60.mp4` (v0) → skin
  levelled (LW 0.55 / LIFE 0.62 / WDY2 0.75 + gamma 0.85) on 3 re-rendered ranges (`renders/fin_fix_*.mp4`) →
  `build/splice_multi.py` → `outputs/patrick_finish_60_v2.mp4` → `build/export.py`. v0 kept: `(v0 red skin).mov`.
- A note from him → change the DATA (make_timeline / captions.txt / edl.py), re-render only the touched frame ranges with
  `finish.py render --frames a:b`, splice, export (memory: one finish render per note, no complete re-renders).
- GPU etiquette learned today: another session's 16 WhisperX processes starved finish.py at frame ~2400 for 25 min; the
  parent session got them paused. Check `nvidia-smi` before a long render.

## (previous) STATUS (2026-10-31 ~09:45): HIS TELLA 1 APPLIED TO THE SEQUENCE → FULL CODE BUILD
- His Tella on the preview = BRIEF DECISION 10 (each note, its Tella time, the frame that resolves it). Sequence v2:
  `seq/edl.py` → `seq/edl.json`, **61.73 s / 32 segments** (v1 kept: `seq/edl.v1.*`). B6 = "And this I realise now must
  have been very painful for him" on Alfred's smiling portrait (WDY3 145); B1 card = SIR PATRICK STEWART · PASSED AWAY 28
  OCTOBER 2026 (zoom-out + desaturate, drawn from his head); B3 regiment photo → Higgsfield face restore (refs WDY2 141,
  WDY3 145); B5 CP → AW letterbox; captions colour MIX; Topaz stb `reduce=2`, 25p conformed by repeats before chr-2.
- Build order: kit copy → Higgsfield stills → Stage A (per-shot) → Topaz → finish (grade, cards, captions) → audio → export
  → § 8 QA → § 9 report → LESSONS + memory.
- DONE (~10:40): Higgsfield (16 credits, balance ~1110): `stills/hf/regiment_restored.png` (nano_banana_2_1 4k, refs =
  the two portraits), `sidecap_restored2.png` (no refs: with refs it aged him + reframed, `sidecap_restored.png` rejected),
  `smiling_restored.png`; plain bytedance upscales `*_up4k.png` rejected (soft / letter-like marks by the eyes).
  Proteus: `renders/AMN09_prob4_136.mov` (x4), `renders/CP_prob4_237.mov` (x2), no watermark. `build/make_timeline.py`
  → `build/timeline.json` (32 shots, 15 zooms, 9 transitions); `build/stage_a.py track` (all lock errors <= 2 px except
  LW S02 12 px: check) → `renders/stageA.mov` (60 fps, 3703 f). `build/dialogue.py` → `renders/dialogue.wav`;
  `build/mix.py` → `renders/mix.wav` (-14.10 LUFS, -1.60 dBTP; fresh Epidemic swishes `build/sfx/SOURCES.md`, -21 dB).
  Captions: `captions/make_words.py` → `make_plan.py` (88 captions, 37 coloured) → `render_caps.py` → `capcut_pass.py`.
- DONE (~11:15): Topaz per shot (`--no-enhance --reduce 2`, 32 takes, frame counts kept, no watermark) →
  `renders/stageA_topaz.mov`. Measured per shot (`win/hold_scan.py` + a wobble metric): Chronos evened the cadence on
  AMN09 / LIFE / WDY2 / PBS / RR (repeat share 0.58 → 0.00-0.10) and steadied the newspaper (3.1 → 0.5 px), but on B1
  (LW, near-static) and B5 (CP handheld, 29.97p) it ADDED 3-5 frame holds and the stabiliser raised CP's wobble 4.8 →
  6.2 px, so those two keep their Stage A frames. B4 re-framed (WDY2 y700, 300 px strip, `renders/wdy2_fix*.mov`, its
  own Topaz pass). Spliced: `build/splice_multi.py` → `renders/picture_v1.mov` (3703 f).
  Finish test frames → pre-grade levels: AMN09 gain 0.62 / gamma 1.1 / pre_blur 1.6 / sat 0.45 (was blown out, luma
  0.88), LW sat 0.82. B5 caption = "ARE being told" (by ear, `win/were_are.py`); B8 ends before Rich Roll's "mm-hmm"
  (1626.761) → **61.67 s**, mix re-built (-14.10 LUFS / -1.60 dBTP), captions re-rendered (3700 f).
- RUNNING: `finish.py render renders/picture_v1.mov renders/caps_capcut.mov outputs/patrick_finish_60.mp4 --audio
  renders/mix.wav`. NEXT: `export.py` → `Patrick Stewart Father.mov` → `win/final_edges.py` + § 8 QA on the FILE →
  copies to Final Renders + Exports → REPORT.md → memory.
- Framing notes: LW B1 needs scale >= 2.12 (905 clean rows fill 1920) → 2.2, nose y730, x680 (profile: head whole);
  WDY2 lifted to y790 with a 160 px mirror strip in the bottom UI band; LIFE/AMN09/RR noses sit high in their frames,
  a top mirror strip reflected his head (rejected), so their lips sit ~y700-780; CP letterbox band 211-1122.

## (previous) STATUS (2026-10-31 ~03:30): SEQUENCE PREVIEW SENT, waiting on his OK (then I build everything myself)
- Sent: `X:\Claude Projects\Exports\Patrick Stewart Father - SEQUENCE PREVIEW.mp4` (= `seq/preview.mp4`, 73.53 s, 2206 f,
  -14.4 LUFS, rough 9:16 crops, beat/source tags, the brief's labels/card as plain text; no grade/captions/upscale).
- **Runtime 73.53 s with every word kept** (pauses > 0.30 s tightened to <= 0.2 s) = 1.5 s over the 72 s hard max. Asked:
  keep all words (default) or drop "my father. Understand him," (B7, -1.7 s -> ~71.8 s).
- The sequence = data: `seq/edl.py` -> `seq/edl.json` (36 segments from forced-aligned word edges `win/fa_all.py` -> `win/fa/`,
  2 measured overrides: PBS "And" 230.27-230.56, AMN09 "picked" 150.90) + 8 covers; in/out table `seq/inout.md`;
  preview renderer `seq/preview.py` (cuts checked: `proof/preview_edges.jpg`, sheet `proof/preview_sheet2.jpg`).
- Deviations from the brief's picture (all in the preview, all told to him): B1 cover (LIFE has a CHILDHOOD photo under
  the words; Patrick listening on the LW set, LW 324.21, Janet speaking) · B3 first sentence on BBC's regiment photo (3.3 s)
  · B5 CP is a 480p crowd phone video (no better copy online; CP2 `ChoVkMJtpfo` is a different speech) · B6 LW wide +
  LW Alfred graphic covered (smiling portrait WDY3 145 on "regimental sergeant major", then LW listening 311.92 / 322.44 /
  332.64 @0.84x) · B7 reporter cutaway covered by the regiment photo; "miss now" = side-cap portrait WDY2 141 + 0.3 s hold
  (audio ends at "now"+0.06, the next word follows 0.1 s later) · B8 Picard = PBS's own still (captain's chair, PBS 332.4).
- NEXT on his OK: copy the Kane build kit (`projects/kane-didnt-deserve-it/build/`) → Stage A from `seq/edl.json`
  (framing per shot, LW rows > 905 never shown, head lock on talking shots) → Topaz: Proteus (prob-4, NO Iris) on AMN09 +
  CP + grain, watermark check → zooms / transitions (catalog pass in BRIEF first) → grade cold B1-3 → warming B4 → warmest
  B7-8, skin levelled first → labels/card → captions y≈1060 colour MIX (WhisperX words through the EDL) → audio: per-source
  NR (AMN09, CP), level match, 3-frame crossfades, -14 LUFS / <= -1 dBTP on the ENCODED file, swishes 19-23 dB under, no
  music → `Patrick Stewart Father.mov` to Final Renders + Exports → § 8 QA + § 9 report → LESSONS + memory.

## Job facts
- Format: AW short, 1080×1920, 30 fps export, full bleed (no letterbox, no blur fill), −14 LUFS / ≤ −1 dBTP, no music.
- Runtime target ~66–70 s, hard max 72 s.
- Kit to copy for the build: `projects/kane-didnt-deserve-it/build/` (newest; Janet's kit with the utf-8 and speaker-gain
  fixes) + `projects/katherine-never-got-over-him/build/` (geom.py, head_dx.py).
- Export: `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Patrick Stewart Father.mov` + identical copy in
  `X:\Claude Projects\Exports\`. Never C:, no phone copy unless asked.
- Started by session local_3ae3a4cf (the parent); shared notes folder
  `C:\Users\affan\AppData\Roaming\Claude\side-session-notes\local_3ae3a4cf-7107-4cdf-a50e-e1b313072860\`.

## Sources
| Code | File in raw/ | State |
|---|---|---|
| LIFE | LIFE_Stewart_BBC_Lifeline_CombatStress.mp4 | 1920x1080 25p (bug top-left; B1 words over a CHILDHOOD photo) |
| AMN09 | AMN09_Stewart_Amnesty_speech.mp4 | 640x360 25p (Proteus) |
| WDY2 | WDY2_Stewart_WDYTYA_shellshock.mp4 | 1920x1080 25p (side-cap portrait 23.64-26.72 + 136.28-147.72) |
| CP | CP_Stewart_Comicpalooza_2013.mp4 | 854x480 29.97p crowd phone video (Proteus) |
| LW | LW_Stewart_LooseWomen_2018.mp4 | 1920x1080 25p (lower-third + bug from row 913) |
| PBS | PBS_Stewart_NewsHour_2023.mp4 | 1920x1080 29.97p (Picard captain's-chair still 332-335) |
| RR | RR_Stewart_RichRoll_2023.mp4 | 1920x1080 23.976p |
| WDY3 | WDY3_Stewart_WDYTYA_brother.mp4 | 1920x1080 25p (picture only; smiling portrait 143-148) |
| TNG_*, CP2_* | raw/ | candidates, unused (TNG helm 1080p, Engage 480p; CP2 = a different speech) |
