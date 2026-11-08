# RUN: mj-showed-his-mother (AW Short, "What Michael Jackson Showed His Mother 💔")

## ▶ STATUS: resume here
**2026-11-08: v3 DELIVERED beside v1 and v2 (both untouched), waiting for his review.** `What Michael Jackson Showed His Mother (v3).mov`, sha256 bf9b49d0c9c80dc3…, 60 fps, 2310 frames, −14.0 LUFS / −1.6 dBTP. Only O6 changed from v2: his note "This Is It overlay still jittery, use a Higgsfield-enhanced still, face in the middle" -> `dl_ov/hf/o2_still_up_c.png` with a slow push-in on his face. Everything else = v2.

## ▶ previous status
**HIS NOTE ON v2 (2026-11-08): This Is It overlay "still jittery": replace it with a STILL of MJ announcing This Is It, Higgsfield-enhanced; "the rest of the video is solid". Still = O2 4K upscale frame 19.45 s, 9:16 crop x 1150, Higgsfield 4K -> `dl_ov/hf/o2_still_up.png` (2 credits); HIS NOTE: face must be in the MIDDLE -> re-cropped at x 1364 and upscaled again: **`dl_ov/hf/o2_still_up_c.png` is the one to use** (2 more credits). Builder is making v3 (only O6 changes) -> `outputs/... (v3).mov`; then I check frames and deliver beside v1/v2 (never rename: he may have imported them).**

## ▶ previous status
**2026-11-08: v2 DELIVERED beside v1 (v1 file untouched in both folders), waiting for his review.** `What Michael Jackson Showed His Mother (v2).mov`, sha256 d986082dc07b1bc3…, 1080×1920 **60 fps**, 2310 frames, −14.0 LUFS / −1.6 dBTP. Changes from v1, only his two notes: (1) real per-frame head lock on every speaker shot (v1's kit had smooth_track STATIC on = one median anchor, cover_clamp blocked vertical lock), then (2) his Topaz recipe per shot, segments never crossing a cut, his stabiliser ON for faces (loose, as he works), Chronos + Iris on every video shot: 0 % duplicate frames on every moving shot (Stage A had 16-60 %). Spec `BUILD-v2.md`, proof `proof/v2/`. Open for his eye: Katherine's jump cuts at 18.07 and 23.10 read 25-30 px on a noisy face detector; his own finals measure 0.6-4.5 px frame to frame, ours 1.5-3.5 on most face shots, more on four Katherine shots where the detector wanders.

## ▶ previous status
**HIS NOTE ON v1 (2026-11-08): "no head tracking", and footage is jittery, not native 60 fps smooth (This Is It overlay, others too): "this will be done in the Topaz department"; don't stop until it looks right. Everything else "looks good": change nothing else. v2 in progress: real head lock on speaker shots -> Topaz Iris + Chronos -> 60 fps. My error: I copied Ronaldo's no-Topaz/no-60fps call.**

## ▶ previous status
**2026-11-08: v1 DELIVERED, waiting for his review.** Final Renders + Exports + `outputs/` `What Michael Jackson Showed His Mother.mov`, sha256 de964869e885add6…, 38.50 s, −14.0 LUFS / −1.6 dBTP. Report: `REPORT.md`. Note from him: read ABW10 first if he edited, change only what he named, data + one finish render. Re-run: `build/make_timeline.py` → `build/fit_y.py` → `finish.py centers` → `stage_a.py render` → captions → `build/render_chunks.sh` → `build/mix.py` → `build/export_cta.py`. Shot renumbering makes saved head tracks stale: remap or re-track. Proof: `proof/r1 r2 r3 r4`.

## ▶ previous status
**2026-11-07 ~23:50: TELLA 2 IN, "NOW YOU CAN START THE BUILD". BUILD RUNNING: spec = `BUILD.md` + BRIEF § TELLA 2, § OVERLAY PICKS; his cut = `premiere/his2_readback.tsv`, 38.50 s. Quote: about 5-6 % of the week. Higgsfield 906 -> 901.**
Phase 1 on a Sonnet builder: timeline, dialogue, captions, Stage A, test stills in `proof/r1/`. It stops for my frame check; no full render before that. Then Phase 2, QA, delivery to Final Renders + Exports, REPORT.md, LESSONS.

## Builder log
- 2026-11-08 Phase 1 (Sonnet builder): kit copied from ronaldo-retires into build/ captions/ win/ and patched; `build/make_timeline.py` writes the timeline from `premiere/his2_readback.tsv` (21 shots, 20 A1 pieces, 15 transitions, 2310 frames); nose tracks + smooth + fit_y + centers done; `renders/dialogue.wav` built (-17.6 LUFS pre-mix); assets made: `assets/article_pen.mov` (pen on "Burned Filming Pepsi Ad"), `assets/face_telegraph_neutral.png` (green hair cast removed), `assets/hospital_glove.png` (A9p 681.0), `dl_ov/o2_slow.mp4` (This Is It, slowed). Stage A render running under gpu.lock (`logs/stageA.log`). Next: captions, stills, proof/r1.

## ▶ previous status (~23:10): bits on the timeline, waiting for his approval (given in Tella 2)
**2026-11-07 ~23:10: TELLA 1 PROCESSED. BITS ON THE TIMELINE, WAITING FOR HIS APPROVAL PROMPT. NO BUILD. Nothing saved or exported.**
- `MJ Showed His Mother - raw cut v2`: his re-cut + 4 new bits, 30 fps, short ends at 48.00 s (his cut was 33.33 s), alternates after it from 50.0 s, 9 markers. V1/A1 39 clips, V2 his 2 overlays (unchanged, to be replaced at the build). Read-back = `v2job/placement.json`: 0 mismatches, no gaps in the short. A1 re-ASR from the read-back = his words + the bits (`logs/final_check_v2.log`). Join gaps at the new bits <= 0.06 s.
- His re-cut `MJ Showed His Mother - raw cut` is untouched (33.33 s).
- Details, table of bits and his direction: BRIEF.md § TELLA 1.
- On approval: reread BRIEF § "Creative direction FOR THE BUILD", then build (AW code build, CTA per README § 12, captions per SESSION-START). Higgsfield for the This Is It still: he asked for it in Tella 1; preflight the cost.
- Rebuild v2: `python build_v2.py` -> `place_sequence.py v2job` -> `premiere/run_window2.py` (clear first with `premiere/clear_ours_v2.js`). Keep the dialog watcher up during a window.

## ▶ previous status (~21:30): first raw cut in Premiere, read back, waiting for his direction video
**2026-11-07 ~21:30: SEQUENCE IS IN PREMIERE AND READ BACK. STOPPED, waiting for Affan's creative-direction video. Nothing saved, nothing exported.**
- `MJ Showed His Mother - raw cut` (bin `MJ Showed His Mother`, ABW10.prproj, unsaved) 1080x1920 **30 fps**, 54.97 s: V1/A1 28 clips butt-joined 0-54.967,
  V2 6 picture-only covers, 11 markers (one per line). Read-back (`premiere/readback.tsv`) = plan: 0 mismatches (times, in-points ±1 frame floor, scale, position).
- Audio proof: A1 rebuilt from the read-back in/outs (`seqref/a1_readback.wav`) and re-transcribed (`logs/final_check.log`): all 11 lines in order, no line missing;
  ASR noise only ("overindulgent", "shower sparks", "this is when", "Burns Center" are mishears of reduced words, the source passes read the script words).
  Join gaps ≤ 0.25 s (`edges.py`).
- His active sequence was restored after every window (now `Jermaine Mocked Skin - raw cut`, his or the sister's). Locks released, my dialog-watch stopped.
- Redo / clear: `premiere/clear_ours.js` (V1/V2/A1/A2 + markers of OUR sequence only), then `place.jsx` (all rows; Karen rows need `place_karen.jsx` because her file differs, see below).

## Premiere lessons from this build (belong in lanes/premiere/lab-notes.md; I did not touch lanes/)
1. **Premiere cannot import the yt-dlp merged mp4 `src/PEvTpd37HEM.mp4`** (H.264 Main 640x480 + AAC LC, ffprobe-clean): importFiles returns true, nothing lands, a modal
   "File Import Failure" opens, and the bridge then reads "MCP Bridge is not running" (heartbeat stale) until the modal is closed. A remux did not help either; a re-encode of the
   needed window (`h264/karen-window-570.mp4`, libx264 High crf 12, aac 256k) imported at once. `python lanes/premiere/dialog-watch.py --once` closed the modal.
2. After a failed import `place.jsx` carries on and logs `MISSING SOURCE` for those rows; I lost the output because the bridge call timed out. Run the placer with the dialog watcher up.
3. Laying rows out of order eats the next clip's head: `lay()` over-trims every clip's out by 0.2 s and relies on the NEXT row overwriting it. Re-laying a middle row therefore
   needs every later row re-laid after it (done for Karen then B10, B11: `place_karen.jsx`, `place_tail.jsx`, `run_place2/3.py`).
4. The bridge also goes quiet for 1-2 min after a heavy call. `premiere/pw.py` waits for a ping before each script.

## Sequence
`MJ Showed His Mother - raw cut` in bin `MJ Showed His Mother`, ABW10.prproj (open from the Auto-Save path), 1080x1920, **30 fps** (the other
recent AW raw cuts are 30 fps), V1/A1 = the speaker's A/V, V2 = picture-only covers, 11 markers (one per line, label text in the name/comment).
Length 54.97 s (script said "about 58 s"; tightened pauses ≥ 0.13 s, 3.5 s removed).

## Sources (all kept as downloaded in `src/`; H.264 working copies in `h264/`)
| Use | File | Spec | Note |
|---|---|---|---|
| Lines 1,2,7,8,10 | `E:\Bullshit Folder\Drake\Katherine Jackson on Michael's Changing Face...60 Minutes Australia.mp4` | 1920x1080 H.264 29.97 | local, original |
| Line 11 | `E:\Bullshit Folder\Henry\Michael Jackson - OPRAH WINFREY Interview (1993) 4K 50FPS UPSCALE.mp4` | 1440x1080 H.264 50 fps | local ("4K" is a fan upscale) |
| Lines 3,4,6 | `src/n_UTXQNvP70.mp4` (Donester, Michaelsguardian, 2011) | 640x480 H.264 30, 464 s | best offered (f135); whole upload = audio over a hospital-bed still |
| Line 5 | `src/uCnsBHNk9rg.mp4` (TheJacksonStory compile) | 1920x1080 H.264 30 | audio only (3:43-3:46); burned caption "Tito Jackson on Questlove Supreme" is covered by V2 |
| Line 9 | `src/PEvTpd37HEM.mp4` (karen faye, anna pennazza) → in Premiere `h264/karen-window-570.mp4` (570-605 s re-encoded, times -570) | 640x480 H.264 29.97 | Premiere rejects the original; burned-in Italian subtitles from row 357 and a black strip rows 0-57: CROPPED to rows 58-353 (649 %, very soft) |
| Covers (fire, stairs, crowd) | `src/BqfJZGUNo5A.mp4` (Us Weekly, 2009) → `h264/BqfJZGUNo5A.h264.mp4` | 1440x1080 VP9 24 fps "AI-upscaled" (original 640x480) | Us logo bottom-right is outside the 9:16 crop; caption zone hidden by a 130 % zoom on cover B3a |
| Cover, line 1 | `h264/oprah-still-1351.mp4` | freeze of Oprah 22:31.5 | PLACEHOLDER for "Michael's face" |
| Cover, line 8 | `h264/stage1992-wig-43.mp4` (Bucharest 1992, `E:\Bullshit Folder\Lonely\...Jam - Live in Bucharest...4K60FPS.mkv` 2:08.5-2:13.5, 4:3 picture cropped out of the 4K frame) | 1440x1080 60 fps | Michael on stage, hair visible, sunglasses |
| Not used, kept | `src/0AdrkbuemlM.mp4` (1080p re-upload, 59.5 s), `src/4r-RZrjw3-A.mp4` (640x480 8 s, "1/2 speed" mark, staircase + pyro), `src/5BpE7ylnz24.mp4` (640x480 41 s, rehearsal after the accident) | | |
Searches for a Donester video, the original Questlove Supreme episode and a clean Karen Faye 20/20 upload found nothing usable (see `logs/search.log`).

## Pipeline files
`sources.json` · `beats.json` · `resolve_local.py` (the AW resolver + measured onset/tail edges, floor/ceil frame choice by level, segment-relative
cover anchors; local copy, the shared one is untouched) → `edl.json` → `plan_placement.py --fps 30` → `patch_placement.py` (Karen crop, B3a zoom)
→ `placement.json` → `place_sequence.py` → `premiere/place.jsx`. Gates: `edges.py` (edge loudness + join gaps), `win/asr_plan.py` (plan audio re-ASR),
`framecheck.py` (every frame of every V2 cover), `crops.py` (9:16 proof).

## Gates (before Premiere)
- Plan audio re-ASR = the script's words in order (two mishear artefacts at joins, no missing line). Join gaps: all ≤ 0.25 s.
- Edge loudness: some joins are cuts inside contiguous speech with no silence to land in (B2 "before|Michael", B3 "the|director|gave", B4, B6.2, B7.2, B9):
  they need 15 ms crossfades in the audio pass; NOT done here.
- Covers frame-checked: no minors; Us caption zone hidden (B3a); B5 crowd = adults. The "Tito" cover shows the crowd rush, NOT Tito's face (label is for the voice).
- Phase 1 done 2026-11-08: proof at `proof/r1/test_shots.jpg`, notes `proof/r1/NOTES.md`. Stopped for frame check.
- Phase 2 done 2026-11-08: outputs/What Michael Jackson Showed His Mother.mov (1155 f, -14.0 LUFS, -1.6 dBTP); proof/r3.
- v3 2026-11-08: O6 (26.03-30.03) replaced by the Higgsfield still dl_ov/hf/o2_still_up_c.png (face centred, slow push on the 60 fps grid, no Topaz); rest = v2. outputs/What Michael Jackson Showed His Mother (v3).mov, 2310 f, -14.0 LUFS / -1.6 dBTP; proof/v3/o6.jpg.
