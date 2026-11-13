# RUN: mj-family-saw-him-again ("Michael Jackson's Brother Saw Him AGAIN 🥹")

## ▶ STATUS: resume here
- **14 Nov 2026 ~05:00 PKT: r2 DELIVERED after his notes** (King head too low, Katherine overlay bad, the Bad overlay wrong, "Topaz looks horrendous"). `outputs/Michael Jackson's Brother Saw Him AGAIN.mov` = r2 (sha256 in DELIVERY-NOTE.md); the first delivery is kept as `... (r1).mov` in outputs, Final Renders and Exports. **Root cause of the quality note: `build/render_chunks.sh` defaults to `STAGE=renders/stageA.mov`, so r1 was finished from the PRE-Topaz picture; the Topaz pass never reached the file (the stills I showed came from stageT). r2 = `STAGE=renders/stageT.mov` plus native 2x pre-upscale of every source (`build/prep_up.py`, `apply_up.py`).** Katherine is still the soft IG clip (Higgsfield `upscale_video` was denied by the permission classifier: needs his permission rule). 
- **14 Nov 2026 ~01:15 PKT: DELIVERED, waiting on his review.** `outputs/Michael Jackson's Brother Saw Him AGAIN.mov` (H.264 1080x1920, 60 fps, 1998 f, 33.300 s, -14.0 LUFS, -1.6 dBTP, sha256 704218c2374d12ea...), hash-verified copies in `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\` and `X:\Claude Projects\Exports\`. QA `proof/r2/QA.md`, delivery note `DELIVERY-NOTE.md`. A note from him = data + ONE finish render (finish-side values in `build/make_timeline.py`) unless the picture changes (Stage A + `topaz_son.py --redo --only <shots>` + plain `topaz_son.py` to concat).
- **13 Nov ~23:25 PKT: BUILD STARTED FROM HIS CUT.** Affan's narrated Tella 2 ("that's the creative direction, you can start
  your process now") is resolved in `BRIEF.md`.
  - Brief: `BUILD-BRIEF-v2.md`.
  - The timeline is his read-back (`premiere/readback_his_edit.tsv`), plus 8 overlays per his direction (sources in
    `src_ovl/` and E:).
  - The build session `local_7f7e09b5-4016-40fc-bd63-6b5848cae89b` runs to STOP 2 (finish stills); the research session
    checks the frames before any full render.
  - No music in the render (his golden hour stays in his sequence).
- **13 Nov 2026 18:19 PKT: RAW BITS LAID IN ABW11** (brief = `RAW-BITS-BRIEF.md`, replaces BUILD-BRIEF.md). Sequence `MJ Family Saw Him Again - raw bits`
  (bin of the same name, 1080x1920 29.97 non-drop, 166.433 s), read back with 0 mismatches. NOT saved, nothing exported, his active
  sequence restored. Details in § Builder log. No code build, Topaz or captions yet (comes from a read-back of HIS edit).
- **13 Nov ~17:57 PKT: AFFAN APPROVED THE RAW BUILD:** "just put these bits altogether in premiere ill mix and match"
  (after seeing v2 and v3.1 in text). The held build session (`local_7f7e09b5-4016-40fc-bd63-6b5848cae89b`) was sent
  `RAW-BITS-BRIEF.md`:
  - ONE ABW11 sequence "MJ Family Saw Him Again - raw bits", with A = v3.1, B = v2-only bits, C = spares, plus the covers;
  - read back, never saved.

  **Next:** he mixes and matches in Premiere. Then read back HIS edit, and the house-style build follows from it.
  New sources were copied into `src/` (ET Berlin, ET LA, Extra Jackie and Marlon, Becoming Michael, Koalition, King
  podcast part 00).
- **13 Nov ~17:50 PKT: PITCH v3.1 SENT TO AFFAN FOR HIS OK (sequence in text). Nothing built.** His max pass is done
  (`PITCH.md` § Max-effort statement):
  - Instagram 13 searches, YouTube 29 searches and 28 downloads, ~4 h transcribed.
  - Fable advisor x2, an Opus cold read (10 fixes), a Sonnet re-read (5 fixes).
  - The sequence changed: La Toya and TODAY are out; IN is ET Berlin `v9sOjhYNS9w` (Kevin: "the emotion it brings out in
    your uncles", then Jaafar: uncles' calls at the screen test, "even my Uncle Tito, rest in peace to him... emotional on
    the phone"); King's quote now starts at "When I went over..."; Katherine labelled on screen.
  - v2 is in `PITCH-v2.md`.
  - **Waiting on his OK.** Then: rewrite `BUILD-BRIEF.md` for v3.1 (it's SUPERSEDED) and start the raw build in Premiere.
    The held build session (`local_7f7e09b5-4016-40fc-bd63-6b5848cae89b`) has a stale queued addendum: give it the new
    brief, or start fresh.
- **13 Nov 2026 ~03:50 PKT: AFFAN SAID YES.** After seeing the v2 sequence (words, timings, frame sheets) he answered "Yes,
  build it". That locks: PITCH v2 order A (ends on "That's Michael"), the stacked split from frame 1, Marlon OUT. The research
  session (`local_efbcf199-e703-401c-b80c-6b6b226f30be`) PROPOSED one build session (Sonnet, brief = `BUILD-BRIEF.md`): the
  app's session cap refused an auto-start, so it waits as a card (task_a8d5d249) for his click. **Nothing is built yet.** The
  hub should not start another. Build state from here on lives in the builder's log below.
  - **~05:00 PKT:** the hub asked for a retry after archiving 14 sessions. The app refused again, for a different reason:
    a session starts only on Affan's own words in the session that starts it, never on a peer's message. **Still a card
    (task_a8d5d249), still nothing built.** It starts when he clicks the card, or says "start it" to the research session,
    or tells the hub (the hub then starts ONE session from `BUILD-BRIEF.md` and the research session dismisses the card).
  - **~05:05 PKT: Affan asked, before saying start, whether the viral-bits hunt was MAX effort. Answer given: no.**
    - Beat 1 (Jackie) is proven hard. Beats 3-4 have topic proof only, and La Toya's beat has none.
    - Instagram stopped after 3 keyword searches (the 429).
    - Not yet searched: other tellings of King's story, other family voices, the 9.9M Short's exact seconds.
    - Variants and a re-read of v2: none.
    - **Hold the build card until the max pass runs** (YouTube side now, Instagram from 14 Nov, then variants and a fresh
      cold read). Waiting on his word.
  - **~15:55 PKT: Affan: "start it now bruv".** The build session started from the card: `local_7f7e09b5-4016-40fc-bd63-6b5848cae89b`
    ("build-mj-s-brother-saw-h", Sonnet, brief `BUILD-BRIEF.md`). It was told that the cover inventory is done
    (`proof/cover_inventory.md`), and that the max pass keeps running here and may swap a beat or angle at STOP 1.
  - **~15:56 PKT: CORRECTION: Affan did NOT mean the build.** ("like don't start the build start the instagram half research"). I stopped the build session twice (it
    touched nothing: no lock, no files) and sent it HOLD. **His order now (quoted):** "after all the research is done only then
    report to me give me the sequence in text then once i approve start the raw build in premiere". So: the max pass,
    Instagram included, runs NOW, then the sequence in text to him, then his approval, and only then the raw build in Premiere.
- **13 Nov 2026 ~00:30 PKT: PITCHED, NOT BUILT.** Research child of the AW hub (`local_3ae3a4cf-7107-4cdf-a50e-e1b313072860`).
  The pitch, gate statement, sequence and prediction are in `PITCH.md`; the research log is
  `research/aw-mj-pick-2026-11-13.md`.
- **Waiting on:** Affan's yes or no. On a yes, the hub starts ONE build session with the Son template as shipped
  (`projects/mj-son-step-outside/`, HUB.md § HOUSE STYLE: his AE grade, 60 fps, Topaz, head lock, transition zooms,
  captions under the lips, swishes, -14 LUFS), plus stacked splits on the comparison lines and no cutaway in the 0-3 s
  hook (README § 13).
- **PITCH v2 (13 Nov ~00:55) is the one to build**, after an independent cold read (see PITCH § "What the cold read
  changed"). Topaz finish test done (`proof/finish/anchor_same_region.jpg`: all four faces at or above the Prince anchor;
  skin smoothing is his call).
- **Open, for the build:** hear King's "in his/her makeup" by ear; King's 447.98-453.04 sentence must play over BTS
  makeup footage (ScreenRant shows the panel with the child actor there); his calls on the hook split, Option A/B order,
  and whether Marlon goes in; pick cover shots not used in the Son Short.

## Format, lane, preset
- Short-form 9:16, 1080x1920, 60 fps finish. Lane: Premiere (**ABW11**, the current project since 13 Nov; never ABW10), per the AW hub. Preset: AW Shorts
  (`presets/youtube-shorts/abundance-wisdom/`), the Son build as the template.

## Sources on disk (`src/`, all downloaded or copied 12-13 Nov; YouTube through `lock.sh youtube`, >= 60 s apart, no block)
| File | Original | Res | Use |
|---|---|---|---|
| `et_jackie_x__ed--R6lo.mp4` | ET, "Jackie Jackson Bursts Into Tears Over Jaafar's Transformation Into Brother Michael (Exclusive)", 12 Apr 2026, 1.19M | 1920x1080 29.97, 3.1 Mb/s | beats 1-2 |
| `extra_latoya_HxPmogHNs-4.mp4` | Extra, "La Toya Jackson Reveals What Made Her CRY in 'Michael' Biopic (Exclusive)", 21 Apr 2026, 169K | 1920x1080 29.97, 3.4 Mb/s | beat 3 |
| `today_jaafar_rMaeRE55OQg.mp4` | TODAY with Jenna & Sheinelle, "Jaafar Jackson on Auditioning for 'Michael,' Family Reactions, More", 537K (his E: copy) | 1920x1080 29.97, 1.25 Mb/s | beat 4 |
| `screenrant_king_9Aom6-cr9x0.mp4` | ScreenRant Plus, "Michael Cast & Director Reveal...", 22 Apr 2026, 273K | 1920x1080 29.97, 1.08 Mb/s | beat 5 |
| `et_marlon_gfzbvMu_JSw.mp4` | ET, Marlon in Berlin, 13 Apr 2026, 37K | 1920x1080 | optional 6th voice |
Transcripts (WhisperX large-v3 + alignment, local): `transcript/*.words.json`. Frame sheets, spectrograms, anchor tiles:
`proof/`.

## Hard rules carried into the build
No music bed (his job). No minors on frame: never ScreenRant's wide panel (the film's child actor), never ET's or
TODAY's film cutaways of the young Jacksons. Two subtle subscribe prompts, no end screen. Labels low, captions just under
the lips. Silence while working. Premiere through its lock, new sequence only, never save or export his project.

## Builder log
- **2026-11-13 ~18:00-18:20 (Sonnet builder), raw-bits build.**
  - Held first on the research session's word; GO came with `RAW-BITS-BRIEF.md`. No cover inventory redone (`proof/cover_inventory.md`).
  - Media: 25 windows re-encoded into `h264/` (H.264 crf 15, AAC 256k for dialogue, covers picture-only), each starting on a source frame boundary
    with 1 s handles both sides; Katherine's 60 Minutes Australia window cut from the 621 MB original (original untouched); C6 = m4a window copy.
    `tools/rawbits_plan.py` (mezzanines, YuNet face-centred 9:16 crop per clip, layout, `premiere/plan_rawbits.json`), `tools/gen_premiere.py`
    (scripts, from the Son's `place.jsx` + Jermaine's `create_seq_abw11.jsx`), `tools/compare_rawbits.py`.
  - Window: `premiere/run_window.py` took premiere.lock 18:19:07, released 18:19:21 (14 s). ABW11 had his active `Jermaine Jealous - raw cut`; the clone
    of `Sequence 02` was emptied (26 clips removed from the clone, Sequence 02 read 26 before and after); his active sequence restored (`active:` confirmed).
    Nothing saved, nothing exported, ABW10 untouched. dialog-watch.py was running (pid 44360), no closer of my own.
  - Result: V1/A1 15 pieces (A1-A6, B1-B4, C1-C5), V2 8 covers, A2 = C6 (King podcast, audio only, 99.13-166.43 s), 30 sequence markers, nothing on other
    tracks. Read-back `premiere/readback_rawbits.tsv` vs plan: **167 checks, 0 mismatches** (`premiere/compare_rawbits.txt`).
  - Layout: pieces 1 s apart (30 frames), sections 3 s apart (90 frames): A 0-36.54, B 39.54-54.99, C 57.99-98.13 + C6 audio 99.13-166.43.
  - Covers: A1v bj_4k 59.925 (3.3 s, over "he became Michael on that screen"); A2v Berlin 38.0-40.0 (0.4 s past the piece end, into the gap);
    **A4a+A4b REQUIRED** becoming_michael makeup 84.58 (42 f) + Lionsgate 104.60 (67 f) over tl 15.749-19.386 = ET source 46.99-50.62 (the group photo with a boy
    shows 47.05-50.5, `proof/picks/sheet_A4_minor_check.jpg`); **A5a+A5b REQUIRED** Katherine 60M 2749.0 (2.5 s) + Lionsgate 107.67 (77 f) over the whole A5
    (ScreenRant wide panel); A6v Lionsgate 108.55-110.05 on the last 1.5 s; B4v TODAY Katherine 334.4-337.4 over B4's first 3.0 s.
    Contact sheet of the cover picks: `proof/picks/sheet_covers1.jpg`.
  - Bin-only: BIN1 Corso at the wig (IGN 30.976, 1.4 s), BIN2 Jaafar on the set stage (Lionsgate 125.43, 3.5 s).
  - Deviations from the brief: (1) markers are SEQUENCE markers, one per piece/cover at its start (a clip-marker API call was not tried; the proven scripts use sequence
    markers); marker durations did not take (all zero-length). (2) Cover cuts moved to the real shot boundaries: makeup shot starts 84.543 (not 84.5, which is the
    interview shot), Lionsgate A5b starts 107.67 and A6v 108.55 (cuts at 107.649 and 108.525). (3) Lionsgate A4b is a 0.54 s-per-shot photoshoot montage (cuts at
    105.06, 105.61, 106.15, 106.69). (4) Piece in/outs are snapped to source frames (max 1/60 s from the brief). (5) A1v uses the Son's bj_4k pick (not ea_IfxTBylg).
  - Not by ear: the pieces' words were not re-transcribed (raw bits, brief did not ask).
- **2026-11-13 19:49 (Sonnet builder), READ-ONLY read-back of HIS edit** (research session's request): `premiere/run_read.py` took premiere.lock 19:49:31, released 19:49:32; no save, no clip changed, no active-sequence switch (active was `Sequence 04`, left as is). Output `premiere/readback_his_edit.tsv` (all tracks, enabled, speed, Motion, opacity, effects, markers, in/out + work area); diff = `premiere/his_edit_diff.md` (`tools/diff_his_edit.py`). His cut = A1-A6, B4, B1, C1, C4 in 33.3 s with his JVKE music on A2; minors flag: ET group photo (tl 10.58-13.19) and ScreenRant wide panel (tl 18.05-20.55) are uncovered. Premiere's `outPoint` reads in + duration + 5 frames: the diff uses in + duration.
- **2026-11-14 ~00:0x (Sonnet builder), BUILD v2 Phase 1 under way (from `BUILD-BRIEF-v2.md`).** His cut re-read 23:25 (`premiere/readback_his_edit2.tsv`): audio identical to the first read, only A4's V1 picture clip head moved (15.48, under the Tito overlay): built from the second read.
  - Kit copied from `mj-son-step-outside` (build/ captions/ win/), paths patched; `build/make_timeline.py` (21 shots, 1998 frames = 33.300 s, 14 transitions, 15 zoom layers, 4 cards, CTA mids 12.20 / 24.70), `build/dialogue.py` (-16.6 LUFS pre-mix; levels matched per source file), tracks OK (14 locked shots, 0 misses).
  - Overlays: `build/prep_ovl.py` (4K crops with a panning window) + `build/slowmo.py` (Chronos: O1 Billie Jean 22 f -> 106 f, O2 makeup test 38 f -> 126 f (0.74x), O7 Bad head-turn 16 f -> 96 f (0.39x)). Tito = GMB 171.6-175.3, Katherine = La Toya IG video (E! News) 16.0-17.5, Beat It close-up 109.2, brothers still = The Jacksons 2001 frame 631.985 upscaled locally with Topaz Proteus 2x (**Higgsfield connector not available in this session: no upscale spent, placeholder**).
  - **ET group photo (Berlin 47.05-50.53) is never drawn** (asserted in make_timeline: no BRN face shot overlaps 47.0-50.6; the screen-test, brothers and Tito overlays cover tl 9.35-16.58). **King wide panel (A5) hard clamp** x <= 700 of 1920 (child actor at ~850-950): `proof/r1/clamp_check.txt` ALL INSIDE, margins 30 px left / 250 px right.
  - Stage A rendered (`renders/stageA.mov`, 1998 f), Topaz per shot (no stabiliser; SR5 adds Proteus 1x), captions (69 lines, forced alignment; King's "her/his" dropped from the caption: both ASR passes heard "her", prob 0.77) rendered + CapCut pass queued.
- **2026-11-14 ~00:35 (Sonnet builder): STOP 2 REACHED, waiting for the Opus frame check.** Finish stills + `proof/r1/NOTES.md` written (test_shots.jpg, lock_seq.jpg, o3_seq.jpg, fs/). Pipeline state: `renders/stageA.mov` (two-pass closed-loop lock), `renders/stageT.mov` (Topaz, 1998 f), `renders/caps_capcut.mov`, `build/timeline.json` (21 shots, 1998 f), `renders/dialogue.wav`. Nothing rendered in full, no mix, no CTA export, no delivery copy.
  - Open for the check: head lock (YuNet measure still FAILS most shots; hop S01|S02 64 px), Higgsfield connector unavailable (brothers still = local Topaz 2x placeholder), Bad head-turn only 0.71 s of source (slowed 0.39x), Tito talking not confirmable by eye, "her/his" and "me/or" by ear. Details in NOTES.md.
  - Resume: any fix is finish-side (`build/make_timeline.py` values -> `finish.py stills`) unless the picture changes (then Stage A + `topaz_son.py --redo --only <shots>` + a plain `topaz_son.py` to concat). Phase 2 = `render_chunks.sh`, `mix.py`, `export_cta.py`, QA into `proof/r2/QA.md`, delivery.
- **2026-11-14 ~01:15 (Sonnet builder): Phase 2 DONE after the research session's 4 STOP 2 fixes.** Tito -> GMB 63.8-67.5 (talking); CTA pill 1 -> 5.00; S20 tight (scale 3.4); jump-cut hops closed with `build/pin_hops.py` (zero-mean constant pin offsets, S01|S02 199 -> 3 px). Stage A pass 2 + `topaz_son.py --redo` + stills, then `render_chunks.sh` (1998 f), `mix.py` (-14.00 LUFS / -1.60 dBTP), `export_cta.py`, QA (`win/av_lag.py` rewritten for pieces.json: worst 4.0 ms; `win/final_checks.py`: dark-frame scan + sheets; re-ASR similarity 0.982). Delivered to both folders, hash-verified.
  - Kit notes for the next build: `topaz_son.py` here is fixed (a partial `--only` run writes nothing else and never concats; `--redo` no longer overwrites untargeted segments with passthrough); YuNet `head_measure.py` is noisy on sunglasses and reports the nose, so use registration (`pin_hops.py --check`) for jump-cut hops; ECC on a fixed centre crop runs away on a head-pose change (253 px nonsense), use nose-centred crops; Topaz `ffmpeg` crashes on a bare PNG (run a 4-frame clip); `heredoc` strings lose `chr(92)` backslashes, write scripts with the Write tool.
- **2026-11-14 ~05:00 (Sonnet builder), r2 after his notes.** (1) King S12/S13: `Y_override` P5 960 -> 700 (head up, less headroom). (2) Bad overlay: his image 4 = the look-back over the shoulder, Movieclips `Ms4xIJh7V2M` 4.38-5.63 s (found by SIFT match of his screenshot, `tools/find_frame.py`), 4K crop, Chronos 0.76x. (3) Quality: kit trap found, `render_chunks.sh` ran on stageA (no Topaz) for r1; r2 finishes from `renders/stageT.mov` and the Topaz stage is now Proteus 2x on the NATIVE source frames first (`prep_up.py`: face shots, Tito, Katherine, makeup test), Stage A reads the 4K files (`apply_up.py` rewrites timeline/track/picks; make_timeline -> apply_up must run in that order), then Chronos only. (4) Katherine: no better footage found (ET premiere clip `hnyNOYabcHk` has no clean Katherine video); local 2x only; a Higgsfield `upscale_video` test was DENIED by the permission classifier (a 2 s test clip is already uploaded: media_id f0eba857-b157-46c9-a35c-c1962692fcea). Balance 873.75 credits, nothing spent.
  - Kit notes: Stage A can die with a MemoryError on 4K reads when other sessions hold memory (retry); Chronos on a 4K input failed silently (slow-mo before upscaling: `build/o2_up.py` upscales the already-slowed 1080p); `topaz_son.py` can lose one frame on a Chronos-only segment (S10 222 -> 221: pad the last frame with `tpad=stop_mode=clone` before concat); YouTube search + one download went through `lock.sh youtube`, no bot check.

