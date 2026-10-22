# RUN — "How Michael Jackson's Siblings Found Out He Died 💔" (Abundance Wisdom short)

## ▶ STATUS: resume here (2026-10-22 ~08:00) — v5 EXPORTED, waiting on his review
**`outputs/mj-siblings-found-out.v5.mp4` -> `X:\Claude Projects\Exports\mj-siblings-found-out.v5.mp4`** (58.25 s, 3495 f,
1080x1920 60 fps, -14.1 LUFS, -2.9 dBTP). Fixes for his four v4 notes, all measured on the render:
1. Colour: one-pass assembly (no splice drift) + HIS fitted grade. Cheek skin v4 -> v5: La Toya luma 0.31 -> 0.63 (R/G 3.02 ->
   1.70), Tito 0.17 -> 0.40 (2.64 -> 1.76), Jermaine 0.28 -> 0.39 (sat 0.30 -> 0.48); Marlon n=1 (sunglasses beat YuNet):
   0.70 / 1.50, natural by eye. Tito sat 0.60 / 1.38x source luma (above the planned ~0.5 / 1.2-1.3x; reads natural).
2. Artifacts: overlays skip Topaz (O8 grey MJ clean at 1:1); the sharpen stack is gone; `despeckle` (5x5 opening on skin,
   setups JC + MM) removes Topaz's white forehead dots. File is 121 MB vs 521 MB: same encoder (crf 12), less noise.
3. SFX all -10 dB.
4. Lips: every speaker's mouth clear of the captions (lip_check + a 0.25 s strip over Tito's T2 run); Tito's zooms pivot on
   his lips at depth 0.85 (face top >= 203 measured); Jermaine's name card moved above his band (y0 175).
Open with him: Marlon kept at 300 % (his ask was "zoom in further, even if softer"; lips above the captions needs ~600 %, so
the captions sit on his nose and his mouth stays free — his call); 30 vs 60 fps; final name/place; flags O6 / O5 / J2 / J3b.

## (previous) STATUS (2026-10-22, later) — v5: framing + audio DONE, picture assembly next
- Lips vs captions (`build/lip_check.py`, zoom included): ALL clear. Tito re-framed nose y834 (`Y_override.TC`) and his three
  zoom layers pivot ON his lip line y1084 (`zoom_pivot_override` in timeline.json, applied by centers.py), so a push-in never
  carries his lips into the caption band (y1093+). Trade: at the deepest push-in his forehead top runs into the top 200 px.
  La Toya clear; Jermaine (letterbox) + Marlon (full-frame, his call 2026-10-22) carry the captions on the nose, mouth free.
- Audio re-mixed with every SFX -10 dB (`renders/mjs_audio.wav`, v4 kept as `mjs_audio_v4.wav`): -14.1 LUFS, -2.9 dBFS peak.
- Running: Tito segments re-rendered at Y 834 -> Topaz -> `renders/mjstito_aligned.mov` (now in `build/assemble_plan.json`).
- Next: `uv run -q python build/assemble.py build/assemble_plan.json renders/mjs_v5_picture.mov` -> finish render v5
  (`finish.py render renders/mjs_v5_picture.mov captions/caps_capcut.mov outputs/mj-siblings-found-out.v5.mp4 --audio
  renders/mjs_audio.wav`) -> gate (skin per sibling, lips, TP on the mp4, contact sheet) -> Exports.

## (previous) STATUS (2026-10-22 ~08:00) — v5 REVISION IN PROGRESS (his review of v4)
**His v4 notes:** (1) grade makes Black skin "too black / chocolate", not the real colour; (2) artifacts + pixelation on faces
(worst: the grey Oprah MJ overlay O8); (3) SFX 10 dB lower; (4) captions cover speakers' mouths in places.
**Measured (build/skin_stats.py, landmark cheeks):** HIS grade BRIGHTENS dark skin (Ronnie pre 0.293 -> final 0.346 luma;
MJ-skin pre 0.443 -> 0.590, R/G 1.52 -> 1.60, sat ~kept). OUR grade (trial layer-43 = Nick Walker fit) DARKENED it:
LaToya 0.546 -> 0.310 (R/G 1.90 -> 2.97), Tito 0.291 -> 0.161 (1.94 -> 2.69); Jermaine went grey (sat 0.66 -> 0.30, my 0.45 gain).
**ROOT CAUSE FOUND (2026-10-22):** the "too black / chocolate" skin was mostly MY splice tools: their rawvideo pipe was untagged,
ffmpeg read it as BT.601 and re-encoded to BT.709 on EVERY generation (skin ~7 % darker + redder per pass; v4 went through 5:
raw Y 119 -> 73). Topaz itself keeps colour (0.546 -> 0.532). Fixed (input tagged BT.709 in align_frames / splice_ranges /
splice_pick: Y/U/V now identical) + v5 picture assembled in ONE pass from first-generation sources (`build/assemble.py`,
`build/assemble_plan.json` -> `renders/mjs_v5_picture.mov`); overlays come straight from Stage A (skip Topaz = no pixelation).
The grade is also replaced by HIS fitted curves (`build/fit_grade.py` -> `grade_curves.json`, validated on his MJ pair).
SFX already -10 dB in audio.py (re-mix pending).
**Plan (advisor-checked):**
1. Grade = per-channel quantile curves FITTED on his pair `Final Renders/mj_stab_chr2_iris3.mov` -> `MJ Final Skin.mp4`
   (centre region, no caption rows, no letterbox/dip frames); VALIDATE by applying to the pre files (must reproduce
   ~0.59/0.50/1.60 on MJ; Ronnie pre brighter than 0.29, not redder). Replace grade(): curves + saturation key + vignette;
   DROP the PRE sharpen bands + Sharpen 40. Reset sat_level to 1.0, re-level per sibling: luma ~1.2-1.3x source, sat ~0.5,
   R/G within 0.15 of source.
2. Artifacts: check O8 + a Tito face at stage A / Topaz / v4; if Topaz breaks overlays -> overlays SKIP Topaz (splice stage A
   overlay frames straight in, all of O1-O8).
3. Captions: YuNet mouth landmarks on v4 + zoom z(t) -> list frames with the lower lip in y1093-1200; fix only flagged setups.
   ASK HIM: Marlon (lips up => CBS crawl back: letterbox him [recommended] or ~390 % punch) and ABC Jermaine (lips up =>
   more banner at the band bottom; he showed it in his own rough).
4. One Stage A re-render after framing is decided; Topaz default on faces only, tweak only J1 run + M2.
5. SFX: whooshes -10 -> -20, hits -8 -> -18, card whooshes -14 -> -24 (audio.py put() rel_db); re-measure TP on the mp4.
Gate v5: skin on target per sibling, zero lip/caption overlap frames, TP <= -1 on the mp4, one contact sheet, weekly usage.

## (previous) STATUS (2026-10-22 ~07:00)
- **v4 = ALL EIGHT OVERLAYS + lower thirds: `outputs/mj-siblings-found-out.v4.mp4` (58.25 s, 3495 f, -14.1 LUFS, -2.9 dBTP)
  -> `X:\Claude Projects\Exports\mj-siblings-found-out.v4.mp4`. Waiting on his review.**
  Picture `renders/mjs_topaz_final4.mov` (default Topaz + overlays + J2 re-frame + tweak on J1 run/M2 + O2/O3/O5 from his
  downloads; Janet re-framed 1.35 @ (1075, 690) so the zoom never puts her lips under the captions). Tito's card 1.40 s
  (ends before Janet's overlay). Re-finish: `build/finish.py render renders/mjs_topaz_final4.mov captions/caps_capcut.mov
  outputs/<name>.mp4 --audio renders/mjs_audio.wav`.
- Flags for him: O6 Grammys 1984 (weak 'scared' fit, VHS); O5 tiny portrait badge on Jermaine's strap; J2 B&W wall photo
  above Jermaine; ABC banner edge peeks at the band bottom on J3b. Open: 30 vs 60 fps (built 60); final name/place
  (brief: `MJ Siblings Found Out.mov` in `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders`).
- GPU note: a game (Modern Warfare) + Media Encoder on the 8 GB card stalled the finish at 0.2 fps; free GPU = ~10 fps.

- To slot an owed overlay: add it to `build/overlays/picks.json` (proof with `build/overlays/proof.py`), set its shot kind to
  "overlay" in `build/timeline.json`, render its range with `stage_a.py render renders/seg_<id>.mov a:b`, Topaz
  (`aw-code-trial-parents/stageB/topaz_his.py`), `align_frames.py`, `splice_ranges.py renders/mjs_topaz_final.mov ...` ->
  level its saturation (`sat_level[<id>]`, measure like build/sat_probe_ovl.sh) -> re-run the finish:
  `"$HOME/.cache/video-editor/whisperx-venv/Scripts/python.exe" build/finish.py render renders/mjs_topaz_final.mov captions/caps_capcut.mov outputs/<name>.mp4 --audio renders/mjs_audio.wav`
- Final picture chain: `renders/mjs_topaz_final.mov` = default Topaz (+ overlays O1/O6/O7/O8 spliced, J2 re-framed spliced) +
  the jitter tweak on the J1 run (1963-2156) and M2 (3264-3367) only (measured: `renders/jitter_tweak.txt` vs the default).
- Never: save/export his projects (ABW10 untouched since the raw cut), audio playback, C: exports, phone copies.

- **The build follows HIS edit** of the raw cut (dump `seqref/seq_his.tsv`, A1 `seqref/raw/a1.mov`, words `seqref/transcript/`);
  plan + his answers in `BRIEF.md`. Engine = Katherine's, generalised: `build/timeline.json` (35 shots, 20 zoom layers, 19
  transitions, saturation keys, fade), `build/stage_a.py` (multi-source head lock; `track.json` done: 26 locked shots, lock
  error 0.2-1.7 src px; static anchors TW / JW), `build/finish.py` (+ peach transition, lb face shots, per-source sat level),
  `build/audio.py` (per-speaker level match, fresh Epidemic SFX set in `build/sfx/`, -14 LUFS / -1.5 dBTP).
- Framing decisions: Marlon 300 % nose y1215 (CBS crawl out of frame); ABC Jermaine letterboxed 500 % nose y1174 (the
  "abc NEWS EXCLUSIVE" banner mostly below the band; it peeks at the band edge when he leans down, J3b); La Toya / Tito 576 %.
- Running / next: Stage A render `renders/mjs_stageA.mov` (overlay slots black) -> overlay picks (Fable agent ->
  `build/overlays/picks.json`) rendered into their ranges -> Topaz (his chain `aw-code-trial-parents/stageB/topaz_his.py` +
  `build/topaz_tweak.py` where jittery) -> `align_frames.py` -> zoom centres -> finish -> captions (Fable agent ->
  `captions/caps_capcut.mov`) -> audio -> `outputs/` + `X:\Claude Projects\Exports\`.
- Still owed by him: Janet x Piers Morgan (O2/O3), Jermaine x Michael adult clip (O5): their slots render black until then.
- **Progress (2026-10-21 afternoon):** Stage A done; overlays O1 (Katherine 60 Min 2750 s), O6 (Private Home Movies, Grammys 1984
  backstage 1171.88 @0.8x: FLAGGED weak), O7 (Living With MJ pt 3, 32.8 s, hand over face), O8 (Oprah 1993 2013.7, grey) in
  `build/overlays/picks.json` (Fable agents stopped on his order; Sonnet for O6). Topaz default + overlays aligned/spliced ->
  `renders/mjs_topaz_v1.mov` (align band widened 6 -> 24: black slots swallowed 13 frames). Jitter (build/jitter_check.py):
  T1 T2a T2b T2d J1d J3b M1a M2 > 2 px -> tweak chain running (`renders/mjsT_*`), pick per same-setup run with
  `build/splice_pick.py`. J2 re-framed (nose y870: no mirror strip, captions on his collar) -> segment re-render + Topaz running
  (`renders/mjsJ2_*`), splice with `splice_ranges.py ... build/j2_range.json`. Saturation levelled incl. overlays (timeline
  sat_level). Captions DONE: `captions/caps_capcut.mov` (3495 f, verify OK; "EYEBALLS BACK" per Affan). Audio `renders/mjs_audio.wav`
  (re-run audio.py for the -1.5 dBTP ceiling). Next: final topaz -> finish render -> audio -> outputs + Exports.
  Flag for him: J2 wall photo (B&W, two seated figures, teens?) above Jermaine's head.

- **2026-10-21 ~09:00: DIRECTION VIDEO RECEIVED + RESOLVED → `BRIEF.md`** (Tella, 12.6 min). He re-edited our raw cut himself
  (ABC bedside line in beat 3, etc.): the build follows HIS sequence (dump `seqref/seq_his.tsv`). 8 open questions + 2 missing
  overlay files sent; build starts after his answers.
- (earlier) **RAW CUT PLACED + VERIFIED** (his plan: raw sequencing first, then a direction
  video, then the edit, built FULLY IN CODE the Katherine way: `projects/katherine-day-michael-died/RUN.md`).
- **ABW10 → "MJ Siblings Found Out - raw cut"** (bin "MJ Siblings Found Out", 1080×1920 @ 60, cloned from the empty "Onyx
  reaction template (empty)"), **59.10 s**: V1/A1 34 clips butt-joined 0 → 59.10, V2 one 0.2 s picture-only cover, 4 beat
  markers. **ABW10 NOT saved** (he saves). His active "Sequence 15" (empty, his THE LAST SHOW → REDO sfx bin, not ours) was
  restored as active after each placement (on the last one another session had "THE LAST SHOW - rough cut (DAMAGED 07-09, do not use)" active: that was restored).
- Verified: read-back = plan within one frame on all 34 clips (`premiere/readback.tsv`), A/V linked, no shot change inside a
  clip; read-back audio rebuilt (`proof/seq_audio.wav`) + re-transcribed (`proof/seq_words.txt`) = the brief's words in order,
  ends on "…they will leave you alone." (re-transcribed BEFORE Marlon's added line; that line's edges measured by RMS, not re-ASR'd); longest non-speech run per beat 0.19 / 0.25 / 0.23 / 0.25 s (hard rule 1); every
  memorial frame at 4 fps in its 9:16 crop = Marlon + adult brothers only (`proof/memorial_4fps_crops.jpg`, hard rule 4).
  Whole-file ASR inserts an "and" after "steering wheel"; the isolated re-ASR of that join hears none (LM insertion).
- In/out table: `proof/inout_table.md`; crops `proof/crop_sheet.jpg`.
- **Added on his call (2026-10-21):** Marlon's "Not being able to walk across the street without a crowd gathering around
  him" (runtime 54.8 → 59.1 s). **Open for him:** 30 vs 60 fps (built 60). Beat 4 / bedside originals (below).
- Re-place from scratch: `premiere/clear_ours.js` (this sequence only) → `place_sequence.py` → `premiere/place.jsx` →
  `premiere/restore_active.js` (set WANT to his active sequence first) → `premiere/readback.js`.
- Brief saved verbatim: `brief/edit-brief.md`. Pipeline: `beats.json` → `resolve_beats.py` → `edl.json` → `plan_placement.py
  <job> latoya@108.675 tito@33.54 tito@55.448 jermaine_hu@85.152` (+ `framing.json`) → `placement.json`.
- ABW10 open in Premiere is the copy at `E:\Premiere Pro Exports\Adobe Premiere Pro Auto-Save\…\ABW10.prproj` (flagged to him).

## Sources (his SnapDownloader pulls, 2026-10-21; YouTube refuses this PC: 429 + bot check, never bypassed)
| Brief | File (`E:\Bullshit Folder\…`) | Size | Used |
|---|---|---|---|
| 01 Tito | `Henry\!!TITO RECALLS ASKING 'IS HE DEAD'_!!.mp4` | 640×360 @ 29 | beat 2 |
| 02 La Toya | `Henry\La Toya Jackson Opens Up on Michael's Death.mp4` | 640×360 @ 29.97 | beat 1 |
| 03b Jermaine | `Henry\Jermaine-Jackson-on-SnapYT.App.mp4` (Hudson Union) | 854×480 | beat 3 (backup) |
| 04 Larry King 8/8/09 | `JERMAINE-SPEAKS-ABOUT-SnapYT.App.mp4` (studio, chyron "Jermaine on autopsy results") | 720×480 | **no** (beat-4 line absent) |
| 05 memorial brothers | NOT supplied → `Henry\Michael Jackson Memorial Service 1958-2009 (4K).mp4` (CBS2 feed, 1080p60) | | beat 5 (fallback) |
| reference (the detail.) | `Michael-Jacksons-Siblings-SnapYT.App.mp4` | 1080p60 | never cut; transcript in session scratch only |
| (extra) | `Henry\Tito Jackson Blames Michael Jackson's Doctor… (Flashback).mp4` (VladTV, 720p) | | no (not in brief; doctor topic = rule 5) |
He says no higher resolutions exist for these uploads (2026-10-21).

## Flags (for his review)
1. **Beat 4 SKIPPED** (the brief's rule): "why did you leave me… instead of him" is NOT in file 04 (full 10:26 transcript). The
   reference compilation (7:48) shows its real source: **CNN Larry King Live on location at Neverland** (Jermaine, red sweater,
   garden, 4:3); file 04 is the later studio follow-up ("when we were on location at Neverland").
2. **Beat 3 = 03b backup.** The bedside original ("There he was laying there… still soft, and I kissed him") is an **ABC News
   exclusive "Michael Through a Brother's Eyes — Jermaine Jackson's Personal Memories"** (abcnews.com; reference 6:36).
   Also in file 04 at 4:02–4:10, NOT used: "I went to the room and saw him just lifeless. And it just tore my heart out."
3. **Beat 2 picture:** 01 is a CNN package: 2.1 + the freeway half of 2.2 ("…Don't get on the freeway") play over CNN road /
   car b-roll; "She asked me, was I driving?" and "Janet, is he dead? … he's gone" are on Tito's close-up; "melted right
   there" + the start of "I pulled over" sit on the wide two-shot (Tito's back to camera, the reporter facing). CNN bug.
4. **Beat 5 picture:** CBS2 weather crawl + LIVE bug + "MICHAEL JACKSON … FAREWELL" lower third burned into the bottom
   ~25 % (in the 9:16 fill, y ~1560–1720). Cropping above it = ~137 % (brief caps ~115 %). Marlon tight + centred, his
   brothers behind him, Janet edge-of-frame from 2:36:08; no children in any placed frame.
5. Beat 2 joins: Tito's pauses after 'was I driving?', 'And she said,', 'he's gone.' and 'And I just' cut to ~0.2 s
   at measured dips (the CNN bed hid them from the auto-tighten); the soft 'and' after 'melted right there' is kept WHOLE (no
   clean gap before it): '…right there. And I pulled over…'. Beat 3: 'Westwood, / UCLA' and 'and / the people' pauses cut
   to ~0.2 s.
6. Beat 1: the source says "how's he doing?" THREE times + "is he okay?" twice: kept 3 + the first "is he okay?" (no splice
   inside her panic). "I said" is co-articulated with the "And" before it (no silence to cut in). The Ellen two-shot cut
   lands under "weak." (108.675): her own close-up (src 1:51.90) covers those 0.2 s on V2, picture only.
7. Beat 3 keeps "UCLA" ("Westwood, UCLA, we saw…": cutting it means a splice inside continuous speech).
8. Low resolution: La Toya + Tito 640×360 (fill = 533 % in the 9:16), Jermaine 854×480 (400 %).
9. Brief vs house style, left for his direction video: 30 fps (built 60), music bed, −14 LUFS, lower thirds, captions.

## Engineering found on the way
- **wav2vec2 misaligns numbers and stretched words:** Tito's "15 minutes." was placed 57.70–58.06 (really 57.88–58.44) and
  La Toya's "weak." 108.28–108.56 (really 108.29–108.75, decaying to ~108.84): the planned outs would have cut both words.
  Caught by 10 ms RMS, confirmed by an isolated re-ASR of a 3.5 s snippet; `transcript/words.json` patched (`_fixed`).
  Lesson: check every cut edge's RMS against the body level (scratch `edgecheck.py` logic: edge within 6 dB of the body = suspect).
- **scdet (threshold 10) misses dissolves:** Tito's CU → car b-roll dissolve 33.54–34.18 was invisible to it; a 2 fps sheet
  of the range found it, frame-difference located it. Check a sheet of every used range, not just the cut list.
- **Face detector on b-roll / group shots:** false faces in Tito's road b-roll; on the memorial it jumped between brothers →
  `framing.json` (b-roll centred; Marlon measured per piece from `brief/sheets/marlon_x.jpg`).
- Premiere read-back reports in-points on the 60 fps sequence grid (e.g. plan 81.4815 → 81.467); lab-notes (2026-09-23) say
  the source grid. Not settled; the rebuilt audio uses the read-back values.
- GPU contention: three other sessions' WhisperX jobs filled the 8 GB GPU and stalled ours; the CPU run (28 cores) finished
  the four sources in ~25 min.
