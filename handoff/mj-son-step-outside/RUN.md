# RUN: mj-son-step-outside (AW Short, "Why Michael Jackson's Son Had To Step Outside 💔")

## ▶ STATUS: resume here
**2026-11-08 ~23:25: SEQUENCE COMPLETE FOR REVIEW: 5 beats, 35.467 s, read back, STOPPED for Affan's creative direction.** Nothing saved, nothing exported, nothing committed. His active sequence (`Bieber Walked Off - raw cut`) restored after every window. The Bieber sequence and the rejected `Why MJ Gave Away 5 Million - raw cut` were not touched.
- Sequence: `MJ Son Step Outside - raw cut` (bin `MJ Son Step Outside`, ABW10.prproj, unsaved), 1080x1920 30 fps: V1/A1 9 clips, V2 3 picture-only covers, A2-A4 empty, 6 markers. Read-back = `premiere/readback.tsv`; plan = `edl.json` + `premiere/place.jsx`.
- Rebuild from scratch: `python -I edl.py && python -I build_place.py`, delete the sequence by hand (or `python -I premiere/pp.py premiere/delete_ours.js`), then `python -I premiere/run_window.py` (takes premiere.lock, restores his active sequence, never saves).
- Audio proof: `scratch-rb/` = A1 rebuilt from the read-back (`ffmpeg` concat of the h264 files at the read-back in/out), re-transcribed with WhisperX: the table's words in order, with "like" kept in B5 and the Jaafar mishearing "Jafar". Last word ends 35.37 s of 35.467.
- Gate evidence (`BRIEF.md` § QUALITY GATE): ffprobe per file, crop windows and scales per beat, audio verdict per beat, spectrograms `proof/spec/sheet.png`, crop contact sheets `proof/timeline_crops.jpg` (V1 and V2 at 0.4 s steps; covers re-rendered after a crop tweak: `proof/covers_final.jpg`), per-frame ABC layout check (`layoutcheck.py`: every placed ABC span is entirely 3-up / 2-up / full as planned).

## Steps (RUN line, raw-cut scope only)
| Step | State |
|---|---|
| 1 Intake | ABC, ET, Lionsgate downloaded 22:08-22:11 via `lock.sh youtube` (100 s apart, no bot check): `src/`. KIIS read in place (E:). Premiere-safe re-encodes in `h264/`. |
| 2 Rough cut | word-exact EDL (`edl.py`: WhisperX words, valley-based edges, standard tighten, static; no audio chain: no export planned here) |
| 3-6 | SKIPPED on purpose: scope was the cut sequence only (no audio polish, no grade, no graphics, no SFX, no music, no captions, no CTA) |
| 7 Review | Affan |
| 8 Export | Affan exports himself |

## Open items for Affan (decisions, none blocking)
1. ABC crop resolution: B1 484 %, B3-B5 415 %, B5 tail 349 % magnification of the ABC panel pixels (no better source for these lines).
2. B3 uses the table's on-set Prince shot for only 1.3 s (he leans out of a static crop); the brief's "2:08" is 2:00-2:02 in ET/featurette. Identification of the long-haired headset man rests on the brief + face; unambiguous alternative: featurette interview 134.47-136.51.
3. "uh" (B2) and "like" (B5) kept: no silent edge to cut on.
4. Length 35.47 s (table ~37 s): the exact words set it.
5. Optional: B1's picture could be a 1080p on-set featurette shot instead of the 4.8x ABC panel (e.g. the interview shot 134.47-136.51, Prince in the white MICHAEL tee); one swap.

## Hard rules (kept)
No minors on frame; no music; silence (nothing played); premiere.lock per window; new sequence only; no save; no export; YouTube only through lock.sh.

## Tool notes (lab-notes candidates)
- Premiere stores floor_seq(floor_src(in-point requested)): on a 30 fps sequence a 29.97 or 23.976 source must be requested at the first source-frame boundary at/after the target 1/30 s boundary (+0.1 ms), else the in-point lands up to a frame early.
- `app.project.deleteAsset` is not available in this Premiere; `deleteSequence` is. An unused media item stays in the bin.
- A video file whose first frame starts after its audio (re-encode from a window start not on a frame boundary) shifts Premiere's in-point origin by that offset: start the window on a frame boundary.
