# RUN: mj-son-step-outside (AW Short, "Why Michael Jackson's Son Had To Step Outside 💔")

## ▶ STATUS: resume here
**2026-11-09 ~17:45: DELIVERED, waiting on his review.** Final = `outputs/Why Michael Jackson's Son Had To Step Outside.mov`: H.264 1080x1920, 60 fps, 2094 frames, 34.900 s, -14.0 LUFS, -1.6 dBTP, sha256 dd9720a88c12eabd... Copied hash-verified to `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\` and `X:\Claude Projects\Exports\`. QA = `proof/r2/QA.md`:
- every A/V-lag piece is +3.9 ms;
- panel clamp ALL INSIDE;
- re-ASR matches;
- every dark frame is a designed dip.

The Opus check of `proof/r2/final_sheet.jpg` + `caps_check.jpg` passed. Remaining limits, all from the sources: MSG is an SD upscale; ABC is magnified 3.5-4.9x; "uh"/"like" are in the audio; vertical head drift can't be locked under the clamp; on P8 (the last 4.8 s) the caption line crosses his mouth (his nostril/upper-lip rule for a close-up that cannot move). A note from him = data + ONE finish render (finish-side values: `caption_shift`, cards, CTA, mix), never a Stage A/Topaz re-run unless the picture changes.
**2026-11-09 ~16:40: PHASE 1 CHECKED (Opus), PHASE 2 RENDER STARTED.** One fix: `caption_shift` -120 → -10. The builder had dropped the line under P8's low lips, which put P1-P7 captions on the chest; that is the Janet v1 mistake (LESSONS 2026-10-28: his height ~y1060, and P8 carries it on the nostril/upper-lip line). Kept: Iris+Proteus on ABC (`scratch-son/ab_cmp.jpg`), no stabiliser on P shots, x-only lock, ABC skin tint, O3 framing. Phase 2 = render → mix (-14 LUFS, no music) → export_cta → QA (`proof/r2/QA.md`: frames, loudness, per-piece A/V lag vs his mezzanines ±1 frame, re-ASR, sheet, clamp). Then I deliver (Final Renders + X:\Claude Projects\Exports).
**2026-11-09 ~14:55: HIS "start the actual render ... after you have locked everything in" + "best quality overlays for all shorts": CODE BUILD STARTED.** Cut locked = `premiere/final_readback.tsv` (his live sequence, unchanged since my last window). Spec `BUILD.md`; Sonnet builder on Phase 1 (stops at `proof/r1/` for my frame check, then Phase 2 render). Overlay upgrades: O1 Billie Jean now the 4K VP9 original (`src4k/bj_4k.webm`), O2 MSG the 2880x2160 original (`src4k/msg_4k.*`), O3 re-stretched with Chronos instead of frame duplication; GQ "Becoming Michael" scanned (`proof/gq/sheet.jpg`): no hair-and-makeup chair footage, so O3 stays the Lionsgate BTS shot. Delivery after QA: Final Renders + X:\Claude Projects\Exports.
**2026-11-09: APPROVED by Affan ("approved", after the overlays and the listed open gaps). Nothing further to build; he saves and exports in ABW10.**
**2026-11-09 ~13:35: Affan's Tella walkthrough (9 Nov) ingested (BRIEF.md § WALKTHROUGH); his three overlay slots are filled on V3 (Jaafar as Michael 1.6-4.3, MSG 2001 7.4-10.533, Jaafar hair/makeup 13.1-14.8), read back, his edits and V1/V2/A1 untouched. Sequence is now 34.9 s (his tightening). Slot 2 was replaced with a sharper 2001 MSG source (Billie Jean 4K upscale, 460.30-463.43; still SD at heart). Open: slot 3 is stretched 0.84x; ABC crops 3.5-4.8x. Rebuild: `python -I build_overlays.py` then `python -I premiere/run_overlays.py` (V3 must be empty).**

(earlier) **2026-11-08 ~23:25: SEQUENCE COMPLETE FOR REVIEW: 5 beats, 35.467 s, read back, STOPPED for Affan's creative direction.** Nothing saved, nothing exported, nothing committed. His active sequence (`Bieber Walked Off - raw cut`) restored after every window. The Bieber sequence and the rejected `Why MJ Gave Away 5 Million - raw cut` were not touched.
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

## Builder log
- 2026-11-09 Phase 1 (Sonnet builder): kit copied from mj-showed-his-mother (build/ captions/ win/), patched; `build/make_timeline.py` from `premiere/final_readback.tsv` (14 shots, 10 A1 pieces, 11 transitions, 2094 frames, END 34.9000). Sources = originals; frame times matched to his mezzanines with `win/sync_match.py` (bj4k 59.935, msg4k 460.326, KIIS 122.9562 / 129.1707, ABC 219.219 / 249.683 / 253.153 / 255.789 / 263.597 / 270.904 / 272.639, LG 125.4587 / 108.6502). O3 = `build/o3_slow.py` (Chronos slowmo, 102 frames). Panel clamp: A3/A2/AF sources carry content_x/content_y, `lock_full` off, face detection runs INSIDE the panel crop; `build/clamp_check.py` = per-frame check (ALL INSIDE). Dialogue built (`renders/dialogue.wav`, -16.5 LUFS pre-mix).
- Stage A rendered twice (renders/stageA.mov = pass 1 after `lock_refine.py` x-only closed loop; the first pass is `stageA.pass0.mov`). head_measure on Stage A: x range 13-63 px, y range 35-109 px (the panel / frame clamps leave no vertical slack: head moves in y are NOT locked, by the hard rule). Captions: `captions/captions.txt` (four 4-word lines of the brief re-split to 3 words), `make_words.py` (one forced-alignment pass, fillers uh/like aligned then dropped, 9/11 = "nine eleven"), `caps_code.mov` rendered. Topaz started (`build/topaz_son.py`, per-shot recipe; ABC panels = Iris Focus fix Strong then Proteus 1x).
- Topaz done: renders/stageT.mov 2094 frames, every segment frame-count ok (S11 retried once after a transient Chronos 'video rate' error). Captions verified (caps_capcut.mov, 6-frame lateness ok). Finish stills r1 running.
- Phase 1 DONE 2026-11-09 ~16:25: renders/stageT.mov (Topaz, no stabiliser on P shots; the stabilised version kept as stageT_stab.mov), captions ok, caption_shift -120, skin tint on ABC, stills + proof/r1/NOTES.md written. Waiting for the Opus frame check; Phase 2 not started.
- Phase 2 note: first finish render had NO captions (render_chunks reads renders/caps_capcut.mov, which was missing); copied captions/caps_capcut.mov there and re-rendering into renders/chunks2 (build/render_chunks2.sh).
- Phase 2 DONE: outputs/Why Michael Jackson's Son Had To Step Outside.mov (2094 f, 60 fps, -14.0 LUFS / -1.6 dBTP); QA in proof/r2/QA.md. Not delivered (Opus session delivers).
