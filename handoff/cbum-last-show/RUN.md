# RUN — cbum-last-show ("THE LAST SHOW", Chris Bumstead, Abundance Wisdom long-form #3)

## ▶ STATUS: resume here
**2026-10-21 ~16:30: HIS TWO NEW ASKS (watching the restored sequence) ARE PLACED AND SAVED.** Evidence + stills:
`review/redo-2-fixes/` (`id-evidence.jpg`, `4a-tags-corrected.png`, `subscribe-alert-2m16.png`).
- **Line-up label "thats not shaun brh": he was right.** The left man's bib is never legible in the 4a shot, and Shaun Clarida (#7)
  is a bald Black athlete (Fitness Volt winners photo), so the earlier "#7 = Clarida" was never proven. His tag is DROPPED; only
  Chris (#5) and Martin (#8, legible on his bib; the medal winner) are named (`c4-4a-tags-alpha-d.mov`, tracked, pointer SFX
  retimed). Every Martin image re-checked against the winners photo (co-08, co-10, cob-21, c3-martin, c3-3a-martin, c3-arnold,
  c4-finals-twomen with bib 8 visible, c4-martin-olympia): all the same bald, clean-shaven man. (co-10's result ledger sits over
  this same line-up; it lists names, it points at no one.)
- **Subscribe alerts (his ask; overrides the default no-CTA rule for this film):** `cta-sub-alpha.mov` (kit tag language, bell
  rings once, "Abundance Wisdom", 3.0 s, lower-left) on V3 at **2:16.4, 4:40.2, 8:01.4**: calm face windows with nothing on V2-V5,
  ≥ 30 s from both mid-rolls, none in the cold open / end screen / after the health-scare trailer. One soft "letter set down on
  a table" SFX each (three different Epidemic takes). Build: `python work/redo/cta/build_cta.py`. A full SFX rebuild must now
  include the section: `--sections co,co-b,titles,ch1,ch2,ch3,ch4,ch5,cta`.

**2026-10-21 ~15:00: HIS SECOND REVIEW (of the redo) IS FIXED, VERIFIED AND SAVED: waiting on his watch.** Report: **`work/redo/REPORT-REVIEW-2.md`**. He reviewed the DAMAGED copy by mistake; the resolved list is
`review/critique-2026-10-21-redo/NOTES.md` (REAL vs damaged-only). Fixed on the restored sequence, each placed by readback and saved:
- **c4-pre4f removed** (0.37 s vlog flash before 4f); sweep: no V2 cover < 1 s, no 1-3 frame V2 gap, every V1 gap covered. The face
  gate's 2 "reading" flags (138.08, 526.54) are padding artifacts: the last 8 frames before both cuts are eye contact (checked by frame).
- **c1-1c-push removed** (the push on Breon); `removed-rows.json` in ch1/ch4.
- **co-02 + c3-post rebuilt from his REAL Instagram** (`redo-gfx/assets/img/ig-real/`, fetched 2026-10-21): his own avatar (the B&W crab
  most-muscular; 150 px is the largest served without login), real counts/bio/first six grid tiles; the real 28 Oct 2024 post
  (instagram.com/p/DBrWCDGSdLs: the carousel's first photo, the exact caption, 2,782,954 likes) as the desktop post view, the
  highlighter on "One more run just for fun, giving the people what they want." Files `co-02-b.mp4`, `c3-post-c.mp4` (fades
  out before the c3-prague butt joint; the ledger outside the camera, frame-identical).
- **Prague line-up tags:** the names were RIGHT (bib numbers in the 4a shot = the official sheet: #7 Clarida, #5 Bumstead, #8 Fitzwater =
  the bald clean-shaven man = his Martin photos); he saw them over the damaged copy's wrong shot (01 @ 387 s). The pointers now rest on
  the shoulders and are TRACKED (`work/redo/ch4/track_4a.py` → `c4-4a-tags-alpha-c.mov`). Every Martin image re-checked: correct.
- **4e → host joint:** a 0.4004 s breath opened at 511.394 (`work/redo/ripple_breath.py`: everything after moved, JSONs shifted, the A4
  voice chunk split), Chris's chopped next syllable faded out (A4 chunk ends 511.28), his own room tone bridges the breath
  (`audio/sfx-redo/bridge_4e-c_tail.wav` on A1, `work/redo/fix_4e_joint.py`). Word-level sweep of the other joints: B1 (crowd tail
  `bridge_B1_tail.wav`) and 5a-b (his mp3 cut chopped "now.": one-frame crossfade into `bridge_5a-b_tail.wav`) fixed by
  `work/redo/fix_joints_b1_5a.py`; the rest end cleanly.
- **c4-martin-olympia-b:** opens on 4e's last frame held, dissolving straight into the Martin card (no black).
- **5c/5d:** V1 under the trailer audio is the trailer's own picture, in sync; the tape overlay on 5d is light. Damaged-only.
- **SFX rebuilt** from a fresh Epidemic pool (`audio/sfx-redo/src/pool/`, 124 takes, `work/redo/sfx/POOL.md`): 283 → 213 cues,
  air sounds 135 → 65, 101 distinct takes, no back-to-back repeat (trophy lights rotate 4 switch takes; the tonal hit-soft take removed), every graphic keeps a sound.
  Rebuild = `python work/redo/sfx/build_sfx.py --sections co,co-b,titles,ch1,ch2,ch3,ch4,ch5` → `python work/redo/sfx/fit_tracks.py`
  (3 tracks: trims the least tail where a 4th sound starts) → `python work/redo/place_sfx_redo.py --t0 0 --t1 700 --replace --apply`.
  Placed 213/213 on A2/A5/A6; the 279 now-offline v1 items removed from the "REDO sfx" bin (no Link Media prompt on reopen).
- verify_redo: all PASS but 19's known 5d-b cue-end flag. Tracks: V1 183 · V2 71 · V3 26 · V4 22 · A1 38 · A2 158 · A4 18 · A5 45 ·
  A6 13; end 690.74. LESSONS 23-30 written.
- **NEXT:** his watch of the whole film → his notes → LESSONS + fixes.

**2026-10-21 ~07:30: THE REDO IS BUILT ON THE TIMELINE AND VERIFIED: waiting on the creator's watch (step 7).** Report mapping
his 19 points to the changes and checks: **`work/redo/REPORT-19.md`**. Brief for agents: `work/redo/REDO-PLAN.md`.
He saw cold open v2 (`review/redo-cold-open-v1.mp4`): "the whole intro looks so much better", except 0:25 ("hideous"), rebuilt as
`co-07-c` (LESSONS 21-22).
- **Sequence:** ABW10 › "THE LAST SHOW - rough cut" (id b0896a23…, the RESTORED copy, in the job bin). The damaged copy (id cf0dc4bb…)
  is GONE: deleted from ABW10 on 2026-10-21 with the creator's OK; its restore point is the XML
  `premiere/recovery/DAMAGED-07-09-cf0dc4bb.xml` (777 clipitems). Other restore points: `premiere/redo-start-2026-10-21.xml` (before the
  redo), `premiere/recovery/ABW10-saved-0707.prproj`, `premiere/before-breath-511.394.xml` (before the 4e breath). The duplicate
  "Face nest" sequences from the import stay (harmless).
- **His own edits kept:** his Enhanced-Speech voice mp3 on A3/A4 (+A1) and his two ~0.7 s cuts. The old SFX are NOT in his mp3.
- **Done (all verified by readback; `python work/redo/verify_redo.py` = all PASS):**
  - stage 1: old V2/V3/SFX cleared, 0a freeze + 0b + 0c out of the cold open, ripple −13.56355 s (VO starts 9.359);
  - host head-lock removed; 23 face nests with one eased ≤ 4 % zoom; archive pieces re-centred (no 2.39 bars any more);
  - 99 graphics (co, co-b, titles, ch1-ch5) + 22 subtitle overlays (V4); 278 SFX (A2/A5/A6); levels on 34 A1 inserts;
  - 5d made continuous (`work/redo/fix_5d.py`, 5d-b now 612.512-620.453 from source frame 1304); 5a bleep keyed on the mp3 chunk;
    the A4 chunk ending at 249.816 extended to 250.217; the 0a-c crowd tail bridge (`work/redo/place_tail.py`, a baked WAV).
- **Tracks:** V1 cut + nests · V2 covers · V3 overlays · V4 subtitles · V5 spare · A1 inserts + bridge · A2 bleep tones + SFX ·
  A3/A4 his voice · A5/A6 SFX · A7 nest scratch (keep EMPTY).
- **Tools (job folder):** `work/redo/linemap.py` (live times; expands nests; resolves stale in/out against the plan),
  `place_redo.py` (graphics by section/ids, eased opacity fades, NO overwrite padding), `place_sfx_redo.py`, `apply_levels.py`
  (idempotent bleeps), `nests.py` (+ `plan_nests.py`), `check_coverage.py`, `verify_redo.py`, `preview.py` (offline preview /
  `--audio-only` mix), `redo-gfx/` (kit + renders).
- **After his OK (2026-10-21 ~08:10):** the gold outline TRACKED on Samson at 0:25 (`co-07-d`, `work/redo/co/outline_samson.py`, a matte from
  `hyperframes remove-background`, traced crown → arms → waist; below the waist the matte grabs backdrop) + a line-draw SFX.
  The chapter cards I-V were re-placed as `t-chN-final.mp4` (the titles agent re-rendered them in place after placement), as were
  the subtitles (`s-*-final.mov`). verify_redo: all PASS (19 flags only 5d's stretched cue end; the line ends 620.22, its overlay 620.45).
- **NEXT:** his watch of the whole film in Premiere → his notes → LESSONS + fixes. Music bed is his. Higgsfield upgrades optional
  (`work/redo/*/higgsfield-requests.json`, the daily limit blocked them today).

### (earlier) ▶ STATUS before the redo
**2026-10-21: THE CREATOR'S VERDICT: REDO.** "very mid… not cinematic… feels like a draft… I would not upload this." His video
review is at `review/critique-2026-10-21/` (`guide.mp4`, `guide-transcript.md`, and the fix list **`CRITIQUE.md`**: read it
FIRST). The bar is the Nick Walker long-form (ABW8 Seq 24) + the FX catalog. Keep the grade and the cut; REDO the visual layer,
transitions, host framing, audio levels and subtitles.

Honest causes (not usage):
1. The BRIEF's research decisions became the target instead of his look: "0 % synthetic, real footage only", "≤ 2.5 changes
   / 10 s", near-black F4 cards instead of his gold-matte cards, "freeze instead of slow-mo". So the plan minimised motion
   graphics, Higgsfield images, screenshots and transitions. Metrics passed and the film was bland.
2. Covers were picked from the downloaded archive by availability (the speech reused under many lines), not designed per line.
3. The per-clip head-lock repositioning made his face drift up across cuts; his standard is a nest + one subtle zoom.
4. The freezes under VO came from the plan and were never checked against his taste.
5. The inserts were left at raw level "for the mix step", so the level jumps were audible.
6. The subtitles were drafted but not all placed.
7. The work was split over 3 sessions, and his standing look (memory project-abundance-wisdom-longform) was never written into
   the plan. The checkpoints asked about seconds, not about the look.

**2026-10-20 11:25: overnight close.**
- The chapters session reported DONE (step 5b built + measured + saved).
- ABW10 was saved and Premiere quit cleanly (bridge `app.quit()`; the project was saved first).
- The PC was shut down at the creator's request (`shutdown /s /t 300`).
- Tomorrow, reopen ABW10 › "THE LAST SHOW - rough cut". Still the creator's:
  - grade Looks (`grade/archive/APPLY.md`)
  - music bed + mix (lock 7)
  - 4d words by ear
  - 5c names
  - his watch notes

**2026-10-20 ~11:20: STEP 5b CHAPTERS 1-5 + THE ENDING ARE BUILT ON THE TIMELINE AND MEASURED** (side session, after the cold open).
No cold-open taste notes from the creator had reached this session by 11:20 (his only answers today: no re-records, keep #27), so it ran on the checkpoint defaults.
Restore point before the first chapter write: `premiere/before-chapters-2026-10-20.xml`.
- **On the timeline (ABW10 › "THE LAST SHOW - rough cut", by name, read back, saved; no active-sequence switch, no QE):**
  - **V2, 47 clips** (`work/storyboard/place_ch.py --section all`, idempotent):
    - covers, frame-exact freezes, the c2 six-win flash (6 × 10 frames) and the 4c-c tail cover;
    - black under every ledger / F4 card / headline / dust field over a host clip.
    - Records: `work/storyboard/v2-placement-<section>.json`.
  - **V1 archive motion, 23 pieces** (same script; record `work/storyboard/v1-motion-applied.json`):
    - Every pre-lap cover shares ONE eased curve with the piece it runs into. Measured continuous at all 8 joints (`n → n+1` or a held frame).
    - Framing was chosen by eye on band sheets: 1a +110 px, 1c +112 px (hides the Generation Iron title box), 2a top-anchored,
      2b + 2c one push 1.10 → 1.25 pinned under the band top, Greg 1.12 → 1.15 (hides his inset borders), 4d 1.00 → 1.07 toward Chris,
      5a +80, 5b +40, 2d / 5f 1.10 as 0b.
  - **Head lock + drift on every face run 2-25** (`work/storyboard/headlock_ch.py`; record `work/storyboard/headlock-applied.json`,
    run 1 included):
    - the light chain, re-centred wherever that needs less zoom;
    - the drift (push-in / pull-out) read from each FACE element;
    - a +0.004 zoom margin, so every frame edge is covered.
    - ⚠ Run 11 (c3-host-66, segs 72-78, a sawtooth) needs z 1.159; with its pull-out it peaks at 1.20 ×, a visible softening.
      Run 3 (c1-host-04) is at 1.07.
  - **V3: seven overlay parts C1 C2 C3 C4a(-b) C4b C5 E** (`hf-graphics/build_chapters.py` / `render_chapters.sh` / `verify_chapters.py`,
    placed by `work/storyboard/place_overlay_ch.py`). They tile 85.352 → 705.271 with no gap.
    - Contents: ledgers, date cards, noun tags, year slams, the Instagram / Arnold / scorecard / quote / NSP-headline F4 cards, chapter
      cards II-V, subtitles, the end card "MAYBE. MAYBE NOT." and 17 s of black + dust.
    - All 329 exact-frame checkpoints and the every-frame scan passed on the first renders; the re-rendered C4a-b passed its checkpoints
      (`verify_chapters.py C4a`), not a second full scan. Details and every builder flag: `hf-graphics/PROJECT.md`.
    - ⚠ Several V2 covers over host clips sit moved down or top-anchored (+40 to +138 px): in those spans ONLY the V3 bars hide the
      host's top rows. With V3 switched off (say while grading) his head shows above y 138; switch V3 back on before judging.
    - To swap a placed part later (C4b for 4d, C5 for 5c): render `VER=<x> ./render_chapters.sh C4b`, REMOVE the old part from V3 by
      name first, then `place_overlay_ch.py --parts C4b --apply` (it refuses a filled slot; an overwrite-replace leaves a 0.1 s tail).
  - **SFX: 71 clips on A2/A3** (68 cues + 3 bleep tones). Built by `audio/sfx-chapters/build.py`, +9.06 dB calibration, placed by
    `work/storyboard/place_sfx_ch.py`. Read back: 0 overlaps, 0 missing.
  - **Bleeps** (`work/storyboard/place_bleeps.py`): A1 Level keyed to -inf over each MEASURED word span, 5 ms ramps, plus a 1 kHz tone at
    -17.5 dBFS (level with the voice). The markers were moved onto the spans:
    - 3a 315.065-315.432
    - 5a 575.291-575.942 ("fucking" is 0.65 s; the old marker said 0.2)
    - 5d 629.696-629.946
  - **Markers:** MID-ROLL 1 379.362 (6:19.36) and MID-ROLL 2 551.901 (9:11.90) sit on the black starts. New: END SCREEN 688.271-705.271.
  - `work/storyboard/validate_v2.py`: PASS.
- **Measured previews** (`uv run projects/cbum-last-show/work/storyboard/preview_render.py all --t0 <a> --t1 <b> --label chN --v N` from
  the repo root; generalized today and bit-identical to cold-open v2; reports in `review/chN-measure.md`):

  | | ch1 v2 | ch2 v2 | ch3 v2 | ch4 v1 | ch5 v1 | end v1 |
  |---|---|---|---|---|---|---|
  | host-leak frames outside FACE | 0 | 0 | 0 | 0 | 0 | 0 |
  | picture changes / 10 s (≤ 2.5) | 1.46 | 1.62 | 1.82 | 1.68 | **2.95** | 0.42 |
  | host-run median (≥ 2.5 s) | 4.13 | 2.80 | 4.67 | 3.85 | 4.63 | - |
  | longest stretch without relief (≤ 20 s) | 8.4 | 8.3 | 10.3 | 17.7 | **22.4** | - |
  | colour jumps over 7 (Cb/Cr) | 1 | 10 (6 inside the flash) | 4 | 7 | 7 | 0 |
  | graphics settling < 1 s before a cut | 0 / 10 | 0 / 27 | 0 / 8 | 1 / 20 | 2 / 13 | 0 |
  | SFX / 10 s (≤ 2.5), impacts | 1.83, 0 | 1.62, 1 | 0.82, 0 | 0.81, 0 | 1.09, 0 | 0 |
  | loudness, no music (I / LRA / TP) | -17.2 / 5.1 / +0.1 | -17.9 / 5.2 / -2.6 | -18.8 / 10.1 / -5.6 | -16.0 / 12.3 / -1.1 | -16.9 / 6.8 / -1.1 | - |

  - **ch5 density and stretch:** both come from the trailer's own fast editing (5c / 5d, 614.3-634.6) plus the planned six-echo recap
    montage (median 1.3 s, inside the 1.3-1.6 montage target). Without them ch5 is under 2.5.
  - **The settle "fails", judged from the comps' timelines (not by eye):**
    - ch4 474.107: the detector caught a dust/stepped-push step. The scorecard highlighter settles at 472.25, 2.05 s before its cut.
    - ch5: the 5c date card (0.93 s) and the NOUN #4 tag (0.88 s) settle against the TRAILER'S own internal cuts, as the cold open's
      0c card does.
  - **Colour jumps over 7** are archive ↔ host and archive ↔ archive cuts (02 Olympia, 05 Breon, 07 NSP, 01 kitchen, the flash run).
    ⚠ The previews grade BY SOURCE (`preview_render.py lut_for`): the vlog match on every 04/06/09 clip and the event cube on
    05/07/08/10. `grade/archive/APPLY.md` leaves exactly those UNGRADED in the chapters. So the colour column does not predict
    Premiere's picture; re-measure after the grade hand step with a per-clip grade map. Cadence, leak, settle, SFX and loudness are
    unaffected.
  - **Loudness:** no bed yet. The archive pieces carry no chain (LRA 12 in ch4 = 4a's crowd silence). TP +0.1 in ch1 needs the master
    limiter: the mix step.
- **Held, by rule:**
  - 4d's subtitles (the creator by ear);
  - 5c's subtitles (the speaker names);
  - 4a's undrafted cues, incl. "I disagree".
  - Built: NSP's own "…It was unanimous" (attributed: his voice, his side panels in shot, tagged; facts.md allows that). The build
    held it by default; it is re-rendered as `ch-overlay-C4a-b.mov`. The scorecard card never says "unanimous" / "not one judge".
- **Fixed on the way** (lab-notes 2026-10-20):
  - Premiere floors `setInPoint` to the source frame, then to the sequence grid, so the covers now aim at frame centres. The cold-open
    covers read 6-41 ms early (1 source frame), left as built.
  - The audio Level scale.
  - A top-anchored cover edge exactly on y 138 let one resampled row of host through: they are now tucked 2 px under the bar.
- **NEXT:**
  - the creator watches chapters 1-5 + the ending in Premiere (taste, step 7);
  - the grade hand step, `grade/archive/APPLY.md` § "Later, when the chapter covers are built": the 01 covers c3-host-62, c3-host-70,
    c4-host-89 and the 01 half of c3-host-63 take `cbum-archive-event.cube` by Paste Attributes. The two 02 freeze stills
    (`ch_02_f6734.png` at T 252.75, `ch_02_f3068.png` at 612.18) are new items and need their own Lumetri with
    `cbum-archive-event-02.cube`. The 02 / B1 covers should inherit the master-clip Look (check the first one by eye);
  - the 4d words and the 5c names (then re-render C4b / C5 with `VER=<x>`);
  - the music bed and the mix: lock 7 arena music, the archive piece levels, the master limiter.
- `brief/subtitles-draft.json`'s T for the chapter cues predates the T2 trim (47-49 frames late). The overlay builder re-derives every
  cue from the piece map, so nothing on screen is late. Regenerate the draft with `work/storyboard/subs_draft.py` before editing cues by hand.

**2026-10-20 10:35: the creator WON'T re-record anything ("I aint recording more stuff for this").** So the re-record asks are
CLOSED:
- "On top", #31-32 and "in Prague" stay out (already cut cleanly).
- "In tears" is dropped.
- **#27 "A year later, he wins his first two pro shows" is factually false.** The options are to CUT the sentence (the ledger
  shows the 2017 Pittsburgh/Toronto wins) or to keep it. **The creator: KEEP (2026-10-20). It stays as recorded; no more flagging.**
- Never list re-records to him again on this job.

**2026-10-20 ~08:20: THE COLD OPEN IS BUILT ON THE TIMELINE AND MEASURED.** It waits on the creator: the grade hand step, a watch, his
notes, the music. **Read `brief/cold-open-checkpoint-report.md` first.**
- **Timeline (ABW10 › "THE LAST SHOW - rough cut", by name, saved):**
  - All approved ripples R1-R9 and trims T1 (2a defect) + T2 ("In tears" cut) are applied: `work/storyboard/apply_ripples.py` +
    `fix_anchor_moves.py`. Every clip sits within half a frame of `brief/storyboard-v2.json` T. Restore points:
    `premiere/{before,after}-ripples-2026-10-20.*`.
  - The plan now reads the FROZEN pre-ripple readback `work/storyboard/timeline-readback-pre.json`, so its T = the live timeline.
  - Cold-open V2 (17 clips, `place_covers.py` / `replace_stills.py`), V3 overlay (`place_overlay.py`, hf-graphics parts A/B),
    SFX (`place_sfx_co.py`, `audio/sfx-cold-open/`), the pivot head lock (`headlock_apply.py --run 1`), 0b's push.
- **Preview v2** (`review/cold-open-preview-v2.mp4`, built by `uv run work/storyboard/preview_render.py all --v N` from the repo root),
  measured against the BRIEF:
  - 2.34 changes / 10 s, worst 20 s window 7, median shot 3.25 s, 2 impacts.
  - Colour jump worst 7.03 on SAME NIGHT's Cb/Cr metric (theirs: 13.7).
  - 0 reading frames. -16.6 LUFS with no music (the mix step).
- **Grade (hand step, Lumetri isn't scriptable):** `grade/archive/APPLY.md` § 1 + § 3. Round 2 is one look in per-source and per-clip
  cubes: vlog matches on the 4 cold-open vlog covers, 01b on the 0a run + co-host-03, a trim stacked on 0b. The preview already carries it.
- **Bugs found and fixed today** (in lab-notes):
  - stale in/outPoint after `.start`/`.end` trims;
  - `.end` can overlap the next clip;
  - 3-decimal plan anchors misplaced 3 clips;
  - still keys must sit at inPoint (~3600 s) + t;
  - changeMediaPath raised a blocking modal (the creator closed it);
  - an overwrite-replace leaves a 0.1 s tail of the old clip;
  - my still extractor grabbed the NEXT frame (+5 ms seek), now fixed.
- **Usage:** 5-hour window 20 %, weekly 17 %, Fable 1 % (the creator: speed over frugality until he says otherwise).
- **This session's context is at 85 %: build chapter 1 onward in a FRESH session from this block** (same pipeline per chapter:
  place_covers --section → overlay agent → SFX agent → preview_render --t0/--t1 → measure).

**2026-10-20 ~01:50: 5b PREP DONE BY 7 PARALLEL AGENTS** (the creator OK'd 6-7 here). Every cover has its exact frame, the facts are
checked, the subtitles are drafted, the head lock is measured, and the SFX are shortlisted. Nothing is built, placed or rippled. The gate
`validate_v2.py` still PASSES. The cold open measures 2.27 changes / 10 s, a worst 20 s window of 7, and 10 SFX. Runtime **11:46.06**.
- **Files** (all listed in v2 `legend.finds`):
  - `work/storyboard/finds/covers-{A,B,C}.json`: 43 picks, attached as `pick` on each v2 element. The .md shows them as **PICK**.
  - `finds/facts.{json,md}`, `finds/sfx-shortlist.{json,md}`, `finds/headlock.{json,md}`.
  - `brief/subtitles-draft.{json,md}` + `-t.srt` / `-T-ripple.srt` (regenerate: `PYTHONIOENCODING=utf-8 python work/storyboard/subs_draft.py`).
  - Frame sheets: `work/storyboard/frames/{A,B,C}/`.
- **New in the plan:**
  - **T1:** a -1.20 s DEFECT trim of 2a's head. It opened on "...the best one yet." at speech level; the in point moves 98.00 → 99.20.
  - B1 is a multi-angle edit (~29 cuts, no line-up). The line-ups come from 01's prejudging take 1172.8-1273.5.
  - The co-host-04 two-shot is now the line-up hold. The backstage bald man at 01 423.5 is seen only from behind, so it's the alt.
  - The scorecard and the Arnold beat become rebuilt F4 cards: NSP's frame is watermarked, and no SAME NIGHT export exists.
  - The end screen is black + dust.
  - Every cover pre-lapping into a V1 piece starts at that piece's scale. 02 ≥ 1.05, Greg ≥ 1.10, 1c repositioned off its GI title box.
  - 01's video starts 0.04 s after its audio. That left 0a-b ending on 1-2 frames of shot C; a freeze now covers them.
  - 5b's frame 0 is soft and different; c5-host-107's freeze runs one frame on over it.
  - noun4 gets real speed + a freeze (the trailer's floor shot fades to black at 81.54).
- **SFX calibration:** the shortlist's gains assume a -15.5 dBFS voice peak. This host peaks near -6 dBFS, so add about +9.5 dB.
- **Checkpoint questions:** 15 now (full list in `brief/cold-open-checkpoint.md`). New since 01:10: T1, the head lock (z0 1.2 light
  chain?), host line #27 (false), "not one judge" / "IV · UNANIMOUS", the backstage bald man, the 5-show flash, and 4a "I disagree" / 4d's speaker.
- **Silence:** the facts agent opened YouTube in the built-in browser and its autoplay played aloud. The pane is closed, the rule is in
  memory (feedback-work-in-silence), and it goes into every brief.
- **Usage:** 5-hour window 15 %, weekly all-models 11 %, Fable 0 %.

**2026-10-20 ~01:10: STEP 5a DONE. Storyboard v2 is re-timed onto the ASSEMBLED timeline and its gate passes. NOTHING is built,
placed or rippled. NEXT = the creator's checkpoint decisions, then the cold-open build (step 5b).**
- **Files:**
  - `brief/storyboard-v2.json` is the machine copy. `brief/storyboard-v2.md` is the readable storyboard.
  - `brief/cold-open-checkpoint.md` is the checkpoint plan: the measured table, the shot list, the build order and the decisions.
  - Chain (job folder): `python work/sb_readback.py` (by name, read-only) → `python work/storyboard/build_v2.py` →
    `uv run projects/cbum-last-show/work/storyboard/face_gate.py` (from the repo root) → `python work/storyboard/validate_v2.py`
    (**PASS**) → `python work/storyboard/v2_md.py`.
- **Times:** every element carries t (today's saved timeline) and T (after the planned ripples R1-R9), plus the anchor it hangs on,
  so a changed ripple re-derives everything.
- **Ripples needed (the creator's OK first):**
  - R1 +2.4 s: the 0a freeze + EVLS card.
  - R2 +0.2 s: the black under "die".
  - R3 +0.4 s: the pre-pivot silence.
  - R4 +1.894 s: chapter card I.
  - R5-R8 +2.9 / 2.9 / 3.1 / 3.1 s: the blacks + chapter cards II-V.
  - R9 +0.8 s: the black after 5d.
  - The ending tail is +23.6 s.
  - **Runtime 11:47.26** (11:36 without chapter cards). No trim needed.
- **Creator's ask 1:** 132.5 s FACE / 184.8 s covered, out of 317.3 s of host.
  - `work/storyboard/face_gate.py` measured EVERY frame of every planned face span: **0 reading frames on screen**.
  - It caught 6 glances the 0.25 s eye-line missed: seg 56 (0.77 s), 57 and 141 mid-line, and the tails of 97, 100, 101 and 121.
  - All are covered now. The 5 "want face" reading segments (c1-host-01) are on the results ledger.
- **Cold open, measured on the plan:**
  - 82.36 s to the end of the title.
  - 2.38 picture changes / 10 s and worst 20 s window = 7 (density.py method). Strict, with the pivot's 4 host jump cuts: 2.86 and 9.
  - 1.07 SFX / 10 s, 2 impacts, 3 text events + the title, 0.52 s silence, 0 % synthetic.
  - The title fits its 6.006 s gap; the text card fits its 3.50 s gap.
- **Corrections to the draft found on the footage:**
  - 0c-d's picture is the trailer's IV hospital-bed shot. The plan freezes the crying shot through "die".
  - The draft's "bowed head at trailer 17.5" is ANOTHER man in a gym. co-host-02 moves to 02's own medal moments.
  - 4 shot slivers get freezes / pre-laps: 0c-c head, 5d-b head, 5c-a head and tail.
  - 02 is a broadcast feed, not a locked-off audience wide; only the speech is one shot.
  - 5d now plays the whole scene with "[bleep] this"; 0c is the short version.
- **Timeline facts:**
  - Every sequence marker after the cold open is 4 frames late (the ripple didn't move them), and the 3a bleep marker
    (t 306.473-306.673) is missing.
  - Premiere's outPoint reads stale after an `.end` trim.
  - Both are now in `lanes/premiere/lab-notes.md`.
- **Mid-rolls land at T 6:21 and 9:14** (the blacks after the Ch3 / Ch4 cliffhangers; the BRIEF said ~6:40 / ~9:20).
- **AW LESSONS applied (no conflict found with v2's calls; the three freezes in the open sit inside lesson 12's slow-zoom cap):**
  - 11: every build settles >= 1 s before its cut, which `validate_v2.py` checks. The c2 ledger now holds 1.1 s into seg 52.
  - 16: each face run drifts once, alternating in/out, <= 3.5 % and <= 0.35 %/s.
  - 4: date cards enter over 0.8 s.
  - 13: subtitles style; 17: renders use `-bf 0`.
- **R3's A1 is ROOM TONE, never digital zero** (the splice lock): extend seg 13 into clean raw, else a room-tone clip.
- **The caption audit still has to run.** The NEVER-list check passes on today's copy, but most subtitles are placeholders until their
  text is set (by ear / WhisperX). Run `validate_v2.py` again once they exist.
- **graphics-plan's `validate-plan.py` does NOT apply here.** It takes cut times from the host-only cuts.json (no inserts) and holds
  the plan to youtube/default's rhythm law. `validate_v2.py` is this job's gate, against the live readback.
- **Usage at this checkpoint:** 5-hour window 8 %, weekly all-models 9 %, Fable 0 % (no subagents used in this step).
- **Creator decisions for the checkpoint** (full list in `brief/cold-open-checkpoint.md`):
  - R1-R4 OK?
  - The F2 title style.
  - Q4 chapter cards.
  - LOCK 6 "In tears".
  - The 0c ending.
  - The 0a freeze frame.
  - Plus the pending ones below: 4d by ear, the 5c names, re-records, music.

**2026-10-20: STEP 4 GRADE APPLIED by the creator: a master-clip Lumetri on C1359 (bin "THE LAST SHOW (cbum-last-show)"),
Creative > Look = `grade/cbum-host-grade.cube`, Intensity 100, NO vignette (his call).**
- It grades every host clip and none of the archive, and it survives re-replays. Don't add Lumetri to timeline clips.
- **Measured over the cut, LUT only** (`work/grade/measure.json`):
  - saturation 0.68 → 0.415 ✓, whites 0.63 ✓, blacks neutral ✓.
  - corners/centre stays 1.215: the BRIEF target ≤ 0.70 is NOT met without the vignette, because the LUT darkens the wall
    and the centre patch alike. The creator declined the vignette; offer a softer one only if he asks.
- **Archive regrade** (BRIEF decision 9: event footage low-key, teal shadows, amber skin) is still to do, at the
  graphics/finishing step.

**2026-10-20 ~01:30: ASSEMBLED EDIT VERIFIED BY EAR-PROXY, 11:05.97, SAVED (ABW10 › "THE LAST SHOW - rough cut").**
- **Joint hearing** (`work/insert_joints.py` → `work/insert-joints.md`): every joint touching an insert, rebuilt from
  Premiere's ACTUAL in/outs, plus all 48 pieces heard alone.
  - Two real defects, both in the cold open, FIXED by one by-name ripple (`work/fix_cold_open.py`; 199 clips moved once,
    verified, saved):
    - 0a-b's tail leaked "They're g-": out 1360.48 → 1359.66.
    - 0a-c clipped "Bumstead": out 1372.35 → 1373.10.
  - The other 32 flags were stitch/mishear artifacts: each piece is clean heard alone, "Maybe" is present in 5e-b, and
    5a-a ends on "goal.".
- **Locks:** LOCK 4 ✓ ("IgA", p 0.82). Locks 1, 2, 3, 5 and 6 have verdicts above; LOCK 7 goes to the mix. The B1 posing
  audio carries crowd chatter + arena music: duck it.
- **The rest of the 01:00 block below still holds** (NEXT + creator decisions).

**2026-10-20 ~00:30: THE ASSEMBLED EDIT IS ON THE TIMELINE: ABW10 › "THE LAST SHOW - rough cut", 11:06, SAVED.**
- **On the timeline:**
  - 154 host clips + 48 clip pieces on V1/A1 (202 + 202).
  - Every piece is frame-exact against `brief/insert-plan.json`.
  - Host V1+A1 are exactly shifted. The 154 host audio chains (+8 dB → -6 dBFS) rode along; the 48 inserted clips carry
    no chain yet (their levels are the mix step's).
  - Two empty gaps by design: the TITLE (75.33-81.33) and the Instagram TEXT CARD (265.87-269.37).
  - 8 sequence markers: the bleeps (3a, 5a-b, 5d), 0c's picture-out, 4d's subtitles-by-ear, 5c not-Chris ×2, and the gaps.
- **Tools and records:**
  - `work/place_inserts.py` (by name; `--plan` / `--apply` / `--verify`).
  - Backup before the inserts: `premiere/rough-cut-before-inserts.xml` + `premiere/seq-before-inserts.json`.
  - Layout: `premiere/inserts-layout.json`.
  - One repair was needed: the 25 fps THE END source snapped 4f-b's in point and its overwrite ate 1 frame of the next
    host head; it was restored, and lab-notes + the placer margin are fixed.
- **Picks:** B1 posing = 135.5-142.5 (by eye). The END source was the creator's download (no direct download possible).
- **NEXT** (none of these are done):
  - Step 4 grade: the creator's 1-min hand step, or the baked-copy option. ⚠ A V2 adjustment layer now also covers the
    archive: cut it at every insert or skip it over the archive.
  - Step 5 graphics: re-time the storyboard onto THIS timeline (`premiere/inserts-layout.json` + `work/assembly.py`).
  - The 2.39 band and the archive regrade.
  - Date cards, subtitles (third-party / rough audio), the title and the cards.
  - Step 6 SFX, the mix (ARENA MUSIC under 4a/2b-2d/B1 ducked to -30 dB or replaced, lock 7), the bleeps, the ending
    (black → "Maybe. Maybe not." card → 15-20 s end screen).
- **Creator decisions pending:**
  - LOCK 6 "In tears": not visible, so re-record "Emotional." or drop it.
  - 4d subtitle text BY EAR.
  - 5c speakers' NAMES.
  - Re-records: "On top", #31-32, "in Prague".
  - Confirm "2026" and "mental space".
  - The grade route.
  - Music (he lays his own).
- **The hung GPU job** (python 12452/58516 from 19:54) may still pin the GPU: ask the creator to end it in Task Manager.

**2026-10-19 ~22:30: INSERTS in progress (the clips between the host lines). VIDEO 01 IS IN** (`broll/01_CBum_2024-11_THE-END.mp4`,
the creator's download, 30:16, 1080p25).
- **Clip in/outs:** WhisperX word timings of each source window (`transcript/windows.json` → `transcript/windows/*.json`,
  `work/transcribe-windows.py`). Matched by `work/inserts_match.py` → `work/inserts-match.{json,md}`.
  - 17 of 20 clips matched cleanly.
  - 2a, 2c and 5a needed the full speech (02) and the vlog (09, 0-210 s): the script's caption timestamps were off.
  - 01's windows are w01_1300 (0a/4a/4d) and w01_1690 (4f/4e).
  - **These four windows are transcribing on CPU** (`WIN_DEVICE=cpu`). The 19:54 GPU run HUNG; its python 12452/58516
    is still alive (killing was refused here) and the GPU sits at 100 %, 7.7 GB. The creator may need to end it.
- **Voiceprints** (`work/voiceprint.py` → `work/voiceprint.json`; Chris refs 06 + 09 agree at 0.65):
  - LOCK 1 ✓: the trailer's "I can't do this… afraid I was going to die" = CHRIS (0.49-0.66); "Do you feel
    fearful?" = the interviewer.
  - LOCK 2: 5c "he's Superman…" and "People perceive…" are NOT Chris (≈0). They are the young man and the woman
    (likely his wife) the trailer interviews. Their names are needed for the captions: ask the creator.
  - LOCK 3: 5b = CHRIS (0.64/0.54), not Hany.
- **INSERT PLAN** `brief/insert-plan.json` (`work/make_insert_plan.py`): 38 pieces, 4:08 of clips; 0a/4a/4d/4e/4f PENDING (the
  01 windows are transcribing on CPU). All 18 hand-offs match the real last line of each host block.
  - 2a is kept WHOLE (98.0-124.25, incl. "six Olympias around my neck… who I became along the way": no grafts).
  - 2c is 4 pieces cut at real gaps (WhisperX dropped 3 stretches; recovered by slice re-ASR + `work/falign.py` forced
    alignment), ending on the complete "…that means so much more."
  - 5a-b "I still am fucking very human" gets the f-word BLEEPED (115.4-116.3).
  - Assembled runtime ≈ 9:34 + the five 01 clips ≈ 12:10 (`work/assembly.py`).
- **LOCK 4 (IgA) ✓:** WhisperX writes "IgA disease" at 101.16 (p 0.82) in 1b, so caption it "IgA". **Lock 7** (arena music)
  belongs to the mix and is still live under 4a / 2b-2d / B1.
- **Joint hearing:** `work/insert_joints.py` (running) checks every insert joint as Premiere actually laid it (each source
  snaps its in point to its own frame grid). Verdicts go in `work/insert-joints.md`.
- **LOCK 6 ("in tears")**, full-res face crops of the speech: he is visibly emotional (eyes closed, lips pressed, glassy
  eyes) but NO visible tears in this footage. Fallback: re-record "Emotional." or drop "In tears" from the take.
  CREATOR'S CALL.
- **LOCK 5** also covers 2a 2b 2c 2d 5a: the speech is one stage shot, no audience cutaways; 5a is Chris alone.
  Clean. The 01 clips are still to check.
- **LOCK 5 (no daughters)**, by eye on 1 fps sheets (`work/clip_sheets.py`): 0b 0c 1a 1b 1c 3a 3b 3c 4b 4c 5b 5c 5d 5e
  are all clean. Still to check: 2a, 2c, 5a (09 mentions "now having a child"), and the 01 clips.
- **Notes for the build:**
  - **5d contains "Like, fuck this."** (~57-58 s in the trailer): BLEEP it. 0c's pieces skip it.
  - 0c picture out at 61.94 (the trailer's PERFECTION card follows).
  - 4b shows the real IFBB scorecard (178-194 s), the source for the scorecard freeze.
  - 1c carries a Generation Iron logo bottom-left, mostly inside the 2.39 band crop.

**2026-10-19 ~16:00: step 4 BLOCKED on ONE hand step; step 5a (graphics plan) STARTED.**
- **What the creator asked:** "apply the cc yourself via adjustment layer". It can't be done exactly on this machine:
  - the LUT slot is not scriptable (lab-notes; the grade-lut.py file-write path needs Premiere 26 params and a closed
    project);
  - ABW10 holds NO Adjustment Layer item and NO Lumetri anywhere (`work/grade/lumetri-probe.json`);
  - scripting cannot construct one, and the Premiere 26 donor imports nothing on 25.0.
  - A dial-only rebuild of v4 was REJECTED: global WB/saturation greys the face (v1), and there is no program render to
    verify it with.
- **Options given to the creator:**
  - (a) ~1 min by hand: File › New › Adjustment Layer → V2 → Lumetri → Creative › Look = `grade\cbum-host-grade.cube`
    + the 4 Vignette dials;
  - (b) a baked graded copy of C1359 swapped in by script (exact, no clicks, not adjustable in Premiere, a big render).
  - Default: wait for (a).
- ⚠ **An adjustment layer spanning V2 grades every ARCHIVE clip inserted on V1 later.** That is wrong: the archive gets
  its own low-key regrade, and the violet-wall correction would damage it. So the GRADE clip must be CUT at every archive
  insert (or the archive sits on a track above it). The master-clip plan avoided this.
- **Someone else (the creator or the other session) made "THE LAST SHOW - rough cut" the ACTIVE sequence (~15:50).**
  Re-check who is in it before any lock window.

**2026-10-19 ~15:30: grade v4 APPROVED by the creator. He applies it BY HAND as a master-clip effect on C1359 (the clicks
were sent), then exports 3 stills → `grade/check/check1..3.png`. Then run `python work/grade/verify_frames.py` (job folder).**
- **The LUT** lives at `grade/cbum-host-grade.cube`, a durable copy of `work/grade/`.
- **Starting Vignette values:** Amount -2.0, Midpoint 35, Roundness 0, Feather 70 (no lane notes on Lumetri's vignette
  maths). Tune from the ring gains `verify_frames.py` prints.
- **Why stills by hand:**
  - QE exportFramePNG throws on this machine (lab-notes 2026-09-13 / 10-09).
  - exportAsMediaDirect is off-limits on his projects (memory).
  - A window grab would flip his timeline while he edits another sequence.
- **Picks** (timeline → source, all on camera): 00:00:01:45 → 61.67 · 00:00:21:59 → 123.632 · 00:00:46:57 → 241.6.
  References are in `work/grade/verify/`. The footage is bt709/tv, ffmpeg's decode = an explicit 709 decode (0 diff).

**2026-10-19 ~15:00: STEP 4 host grade BUILT OFFLINE (v4); before/after sent; waiting on the creator's OK, then the creator
applies it by hand once (Premiere's scripting cannot set a Lumetri LUT).**
- **Build:** `work/grade/host_grade.py` writes `work/grade/cbum-host-grade.cube` (33^3) and the vignette, measured with
  look.py's exact metrics over all 630 frames of the cut (`work/grade/measure.json`).
- **v4 against raw:**
  - saturation 0.68 → 0.415 (target ≤ 0.46)
  - corners/centre 1.21 → 0.665 (≤ 0.70)
  - whites 0.70 → 0.51 (≤ 0.80)
  - blacks neutral
  - face box brightness 103 %, face saturation 0.76 → 0.63
- **The look:** the violet wall becomes a slate/deep teal, the lit skin is protected and slightly amber, the neon is
  darker, the teal shadow tone stays out of the blacks.
- **Sheet:** `work/grade/before-after.jpg` (6 sections). Tuning history: v1 greyed the face, v2/v3 over-saturated
  (leather, tinted blacks).
- **Placement plan:** a master-clip effect on C1359 (Lumetri: Creative > Look = the .cube, plus the vignette), so it
  grades every host instance and never the archive inserts, and survives re-replays. Measure a grabbed frame after,
  to match the vignette.

**2026-10-19 ~14:30: STEPS 2 + 3 DONE on ABW10 › "THE LAST SHOW - rough cut". NEXT = step 4 grade (long-form: one adjustment
layer, V2) → step 5 graphics (storyboard draft-1 vs BRIEF first; the creator's Q1-Q9 + pending decisions below).**
- **Step 3:** done with the creator's OK to take the lock.
  - `work/active_window.py` proved the target (DOM + QE + A1 = 154), then ran
    `audio-polish.py --apply --gain 8` and restored Sequence 09.
  - The bridge reported "not running" on that long call, but the script finished.
  - By-name read-back: **154/154 A1 clips = Amplify +8 dB → Hard Limiter -6 dBFS**. Timeline re-verified 154/154, saved.
  - Lab note added (`lanes/premiere/lab-notes.md` 2026-10-19).
- **Video 01 still MISSING:** the direct download was blocked again on 10-19, and the creator is fetching it.
- **Before step 5:** read the storyboard against `work/eye-final.md` (91 % on camera; cover the 5 'want face' reading
  segments) and the final transcript (lines #4, #25, #31-32 absent; #124 ends on 'giants').

**2026-10-19 ~14:00: ON THE TIMELINE: ABW10 › "THE LAST SHOW - rough cut". NEXT = step 3 audio polish (needs the active
window: waiting on the creator's OK to take ACTIVE-WINDOW.lock again).**
- **Where it is:**
  - The creator's pick (10-19): ABW10, which is open from `E:\Premiere Pro Exports\Adobe Premiere Pro Auto-Save\…\ABW10.prproj`.
  - New bin "THE LAST SHOW (cbum-last-show)" holds `X:\Recordings\Abundance Wisdom\C1359.MP4`, a byte-identical original
    of `raw/C1359.MP4`.
  - Sequence "THE LAST SHOW - rough cut": 1920x1080, 59.94, V3/A3.
  - **154 clips on V1 + 154 on A1**, contiguous, every in/out within 1 frame of `transcript/cuts.json`, ending 317.300 s.
    Project saved.
- **Tool:** `work/premiere_seq.py`. All steps go by name (`--import`, `--prepare`, `--replay`, `--verify`, `--save`);
  only `--create` took the lock: 1.5 s, the prior active sequence was restored by id and confirmed by DOM + QE reads.
  The other session's active sequence (Sequence 09) was untouched.
- **Step 3:**
  - `lanes/premiere/audio-polish.py` adds its clip effects through QE on the ACTIVE sequence, so it needs the lock and a
    proven switch to our sequence (`projects/gta6-ign-missions/transcript/active-window.py` pattern, EXPECT_A1 = 154).
  - The creator authorised the lock only for the create, so ask first.
  - **Gain measured:** kept speech -24.6 LUFS, true peak -6.4 dBFS, LRA 4.5 LU, so **+8 dB** to the -17 LUFS target (Amplify v 0.7222) into the -6 dBFS limiter.
- A re-replay discards clip effects: never re-replay after the polish without re-running it.

**2026-10-19 ~13:30: STEP 2 ROUGH CUT DONE AND VERIFIED. NEXT = the Premiere replay. Waiting on the creator: which project.**
- **The cut:** `transcript/cuts.json`, 154 segments, all pinned. Host runtime **5:17** (317.3 s).
- **Final verification:**
  - `work/cluster_sweep.py` (every segment split into speech clusters, each re-heard alone, containment across joints)
    found **0 repeats in 236 clusters**.
  - Its 9 long-word flags are single emphatic words.
  - The sweep caught one more abandoned restart. "He chose to stand next to the giants" now comes from TAKE 1 (863.8), the
    only complete take (`work/fit_test.py`: forced-alignment fit 0.86 against 0.81/0.61 for the restarts).
- **Eye-line on the final cut** (`work/eye_final.py` → `work/eye-final.md`):
  - **91 % on camera** (287.9 s), 29.4 s reading, mostly Ch1/Ch2 results lines.
  - The cold-open pivot (#15-19) is **100 % on camera**, so F3 holds.
  - 5 segments (10.7 s) the storyboard wants on face are reading: cover them.
- The 12:30 note below is superseded where they differ.

**2026-10-19 ~12:30: STEP 2 ROUGH CUT DONE, verified. NEXT = the Premiere replay. Waiting on the creator: which project.**

**The cut**
- `transcript/cuts.json`: 154 segments, all pinned.
- `outputs/cbum-last-show.transcript.json`: 922 words.
- Host runtime **5:18** (raw 19:17). With the script's clips that is ≈ 10-11 min.

**Gates:** dead-air PASSED; no source overlap. The final joint re-hearing (`work/joint-asr.md`) shows only mishears and
window-edge words.

**Reviews:** both fresh-eyes passes ran on sonnet.
- Flow: 3 real defects, fixed.
- Mechanical: 7 more hidden false starts, each confirmed by sub-span re-ASR, fixed by forced alignment
  (`work/realign.py`).
- The lesson is saved as AW LESSONS #18.

**Rebuild from scratch:** `bash projects/cbum-last-show/work/rebuild.sh`, run from the repo root. Re-run `work/realign.py`
(GPU) only if a realign span changes.

**Premiere (2026-10-19 12:30):** the open project is **ABW10.prproj**, loaded from a nested *Auto-Save* folder
(`E:\Premiere Pro Exports\Adobe Premiere Pro Auto-Save\…\ABW10.prproj`). Another session is active on "Wellness Wisdom
reaction". Do NOT open another project or switch the active sequence until the creator answers. The replay pattern is
`projects/gta6-ign-missions/transcript/replay-seq39.py`: by name, chunks of 30, with read-back.

**Creator decisions pending (asked 10-19)**
- Re-record "On top." (#4)?
- Re-record "He didn't tell anyone until after the show. Here's what it was:" (#31-32)?
- Re-record "…next to the giants in Prague" (#124)? It was spoken as "in the Olympia", which is wrong, so the line ends
  on "giants".
- Confirm "2026" (dropped; the ledger shows 2016) and "Mental space" (kept as said).
- Fetch video 01 (X0LLRvrSWu8).

**2026-10-19 ~10:30: ROUGH CUT EDL DONE, gates green so far, in fresh-eyes review. NOT on the Premiere timeline yet.**
- **The EDL:** `transcript/cuts.json` (153 segments, all pinned, frame-snapped) and `outputs/cbum-last-show.transcript.json`
  (925 words). Host runtime is **5:27** (raw 19:17). With the script's clips that is ≈ 10-11 min against the ~12:00 target.
- **Provenance:** `work/cuts-draft.json` (cut_plan) → splice → `polish-boundaries` (108 → 150 segments, 7 ⚠ listed in
  `work/polish-2026-10-19.log`, polished EDL kept as `work/cuts-polished-2026-10-19.json`) → `work/deadair_fix.py` (8
  quiet runs closed) → `dead-air-qa` **PASSED** (0 runs ≥ 0.65 s).
- **words.json was re-timed** at 26 words where WhisperX stretched a word over a retake (`work/words_patch.py`, idempotent;
  the WhisperX original is `transcript/words.whisperx.json`). Rerun the patch if words.json is ever regenerated.
- **Hidden retakes cut:** "with a disease he-", "Six… Six", "is entering an open bo-",
  "that same week-", "one of the la-", "called it a controversial-", "but think" (each in `work/keep-overrides.json` _why).
- **Running:** the script-flow reviewer (sonnet, background) on `work/cut-script.md`, and `work/joint_asr.py` (every joint
  re-heard → `work/joint-asr.md`). Next: the mechanical reviewer (sonnet) adjudicates the joint report + the 7 polish ⚠.
  Then fix, re-gate, replay onto Premiere (ABW8, by name; ACTIVE-WINDOW.lock), audio polish (step 3), report usage.
- **Known transcript mishears:** now fixed at the source in `work/words_patch.py`, not the dictionary.
- **~10:50, ROUND 2.** The flow reviewer (sonnet) and `work/joint_asr.py` (152 joints re-heard, 26 flagged) found six real
  defects; every one was confirmed by slice re-ASR, then fixed:
  - "Breon Ansley" was cut before the surname.
  - "You see… nobody knows now" was kept TWICE.
  - "2019" had its onset clipped.
  - Two more false starts were kept: "and one of the loudest wh-" and "and said a lot of people".
  - **The 863-884 passage was the wrong audio.** WhisperX painted the script over take 2 and skipped 20 s. It is now
    rebuilt from the heard takes.

  Spoken "…giants in the Olympia, in the show" is factually wrong, so #124 ends on "giants". **Creator decisions pending:**
  re-record "in Prague", "On top", and "He didn't tell anyone… Here's what it was"? Confirm "2026" and "mental space".
  The chain is now one script: `work/rebuild.sh` (repo root), running.

**2026-10-19 ~09:50: words.json DONE (09:24, cuda float16, 1051 words); draft cut BUILT, not spliced yet.**

**Files**
- `work/align.json` / `align.md`: the order-aware aligner's result.
- `work/keep-overrides.json`: the hand pass, each fix with its reason.
- `work/cut-plan.md` and `work/cuts-draft.json`: 100 segments, 473.7 s of host before silences are cut. They play in recording
  order, with no source overlap.
- `transcript/take-map.md`.
- `work/slice-asr.json`: independent re-ASR of the gaps.

**Script lines NOT in the recording (tell the creator)**
- #4 "On top." was never said.
- #31–32 "He didn't tell anyone until after the show. Here's what it was:" were never said, so 1a runs into 1b.

**Probable slips (creator to confirm; both ASRs agree)**
- "2016" was spoken as "2026": dropped, and the ledger card carries 2016.
- "Mental peace." was spoken as "Mental space,": kept as said.

**Fixed**
- The #18 stutter is grafted ("for the best bodybuilder, for the best bodybuilder alive").
- "The Open, by the name, has no cap" is grafted to "The Open has no cap".

**Running:** slice re-ASR of the 12 long-span words (→ `work/slice-asr-longspans.txt`), to find retakes hidden inside them
before `/tmp/video-editor/cbum-last-show/cuts.json` → `RENDER=0` splice.

**Video 01:** the direct yt-dlp attempt on 10-19 was bot-blocked again (429 + sign-in), so the creator is fetching it
(SnapDownloader is installed). The `youtube.BLOCKED` flag stays.

**2026-10-19 09:12: transcription QUEUED** behind the GPU lock (held by the Onyx `cutcheck.py` job since 09:11): log
`transcript/transcribe-2026-10-19.log`. Done while it waits:
- `work/align_script.py` is now order-aware. Long sentences anchor on their last strong take; short ones are searched
  between their neighbours' keeps. Years and numbers are normalised, and out-of-order and overlapping keeps are flagged.
- New `work/cut_plan.py` (align + eye-line + storyboard face plan → `work/cut-plan.md` + `work/cuts-draft.json`).
- `corrections.local.json`: name casing.

Both scripts were smoke-tested on the parked C1361 transcript. Then: take-map (`workflows/take-map.py`) for retakes →
align → cut_plan → hand pass → `/tmp/video-editor/cbum-last-show/cuts.json` → `RENDER=0` splice → polish → dead-air gate →
fresh-eyes reviewers, one at a time on `sonnet` (slice re-ASR via the whisperx venv through `lock.sh gpu`, not mlx).

**2026-10-19 (Mon): GO, in a FRESH session** (the creator's call; the old session ran too long). Sources: 9 of 10 IN
(IDM, all h264 1080p, copied into `broll/` under their source names; see the download log). **01 "THE END" (X0LLRvrSWu8) is
still MISSING**: it carries 0a, 4a, 4d, 4e, 4f, so ask for it, but don't block on it.
**State:** the transcription of C1359 NEVER FINISHED (it collided with another session's GPU job on 10-14 and died; no
`words.json`), so there is no rough cut and NO Premiere sequence yet. **First action:** rerun
`projects/_onyx-batch2-2026-10/lock.sh gpu bash .claude/skills/rough-cut/scripts/transcribe.sh projects/cbum-last-show --force`
(it queues behind the shorts sessions' GPU jobs; ≈ 5-10 min once the GPU is free). Then take-map → `work/align_script.py`
(script host sentences ↔ takes) → the cut. Budget (memory feedback-usage-budget; usage 1 % on 10-19): one step at a time, no
parallel agents, report usage at each gate (after the rough cut, after the cold-open preview). 2026-10-19: the creator said "no
Fable for now": run this job on the default model, and don't put subagents on Fable either.

**2026-10-14 19:00: the RIGHT raw is in: `raw/C1359.MP4`** (1156.66 s, 59.94 fps, 1920x1080, PCM 48k; A/V start 0/0; recorded
today). The wrong file (C1361, a MrBeast talk) + its transcript/eye-line are parked in `_parked-wrong-raw-C1361/` (job copies;
originals untouched).
- Eye-line on C1359 DONE: `transcript/eye-line-raw.{json,png}`: Otsu threshold +0.241, separation 3.45 SD = RELIABLE; 322
  segments, camera 494.5 s vs reading 654.2 s (43 % on the lens). Contact-sheet labels checked by eye: correct.
- Host look on the new set (`research/host-look-C1359/look.json`): luma 0.18, saturation 0.68, whites 0.70, corners 1.30 of
  centre (purple/blue neon wall brighter than the face) → the host grade must pull the wall/neon down (target sat ≤ 0.46,
  corners ≤ 0.70).
- WhisperX `transcribe.sh --force` RUNNING since 19:01 (PIDs 70180/64104, OUTSIDE the Onyx GPU lock) → `transcript/words.json`.
  20:10: still running: it collided with the Onyx `spi-link-in-bio` transcription (in the lock since 19:15); two large-v3 on the
  8 GB card overflow VRAM and both crawl. Stopping mine was refused by the permission classifier → left running, the creator
  told. Future GPU jobs from this job go through `projects/_onyx-batch2-2026-10/lock.sh gpu <cmd>`.
- Storyboard DRAFT-1 (Fable agent, 20:10): `brief/storyboard-draft.json`: 91 beats, every one FX-coded, all 128 host sentences
  covered once with a `cover` plan, cold open computed 2.33 changes/10 s, worst 20 s window 7, 0.87 SFX/10 s, 2 impacts, 3 text
  events, 0 % synthetic; est. 13:36 untrimmed / 12:28 with TRIM ORDER 1-5. Generator: `work/storyboard/build_storyboard.py`.
  Deviations + Q1-Q9 for the creator are in the agent's hand-back (summarised in the next checkpoint); review it against the
  BRIEF before building.
- Sources: the Onyx queue never ran (YouTube bot check 08:26-19:28, all blocked); IDM via the creator is the only route
  (`broll/IDM-LIST.txt`). Only 03 (trailer) is in.
**Next action:** words.json → take-map (last take wins) → align host lines to the script → map each kept host line to
camera/reading → rough cut EDL (`RENDER=0`) → Premiere (multi-clip replay once the sources are imported).

| | | |
|---|---|---|
| format | long-form YouTube | probed: 1920x1080 |
| lane | Premiere (`.setup-complete` lane=premiere) | ABW8 project (shared with other sessions: by-name writes, `ACTIVE-WINDOW.lock` for anything on activeSequence/QE) |
| preset | `presets/youtube/abundance-wisdom/` (LESSONS 1-17) + `research/effects-catalog/` (FX-01..81) | no README/PLAYBOOK yet: the look lives in BRIEF.md + the storyboard |
| lane gaps | read LANES.md before step 3 | |
| source | C1359.MP4 · 60000/1001 fps · 1156.66 s · PCM 48k stereo · one take | `raw/C1359.MP4` (copy; original in X:\Recordings\Abundance Wisdom untouched) |
| script | `brief/CBUM-LONGFORM.md` (LOCKED 10 Oct) + `brief/CBUM-LONGFORM-SOURCES.md` | 10 videos + B1 + S1-S3 |
| constraints | the creator exports himself (never exportAsMediaDirect); review renders stay on X: (never C:/Downloads); everything editable in Premiere ("make this in premiere not in yourself") | |
| started | 2026-10-14 | |

## Steps
| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | done | `raw/C1359.MP4` copied (C1361 was the wrong file, parked); script + sources in `brief/` |
| 2 | Rough cut | done | `transcript/cuts.json` 154 seg / 5:17 host; dead-air ✓; 2 sonnet reviews ✓; cluster sweep 0 repeats; replayed onto ABW10 › "THE LAST SHOW - rough cut" (154/154, verified, saved) |
| 3 | Audio polish | done | +8 dB (measured: kept speech -24.6 LUFS) → Hard Limiter -6 dBFS on all 154 A1 clips, read back by name, saved |
| 4 | Color grade | done (host) | master-clip Lumetri on C1359, Look = grade/cbum-host-grade.cube, no vignette (creator); sat 0.415, corners 1.215 (vignette declined); archive regrade pending |
| 5 | Graphics | 5a done, 5b BUILT: cold open + chapters 1-5 + ending on the timeline, every preview measured (`review/*-measure.md`) | INSERTS laid (48 pieces, 11:06, verified, saved); 5a: `brief/storyboard-v2.{json,md}` + `brief/cold-open-checkpoint.md`, validate_v2.py PASS, face gate 0 reading frames; 5b prep (frame picks, facts, subtitles draft, head lock, SFX shortlist) in `work/storyboard/finds/`; the build waits on the creator's 15 checkpoint answers (ripples R1-R9 + T1, F2, Q4, lock 6, head lock, facts) |
| 6 | SFX | built + placed | cold open 11 clips (`audio/sfx-cold-open/`), chapters 71 clips incl. 3 bleep tones (`audio/sfx-chapters/`); bleep mutes on A1; the mix (bed, arena lock 7, archive levels, master limiter) is still to do |
| 7 | Review | — | |
| 8 | Export | — | the creator exports |

## Flags
- 2026-10-14 07:10: every YouTube source bot-blocked (plain yt-dlp). No cookies. IDM list handed over.
- 08:15: 03 trailer IN (1080p, from the research download). 02 came in at 360p only (YouTube's fallback): parked as
  `02_…_360p-standin.mp4`; fetch.sh now requires ≥ 720p. Research: ALL THREE studies DONE (intro diagnosis, cinematic, face-led opens) → BRIEF § Decisions 1-22 + forks F1-F6.

## Sources: download log (probe each on landing: height ≥ 720, H.264, duration ≈ the YouTube length)
| # | file | status |
|---|---|---|
| 01 | `01_CBum_2024-11_THE-END.mp4` | IN 2026-10-19 22:15 (the creator's download, copied from ~/Downloads), h264 1080p 25, 1816.4 s; video starts +0.040 s after audio (1 frame, harmless in Premiere) |
| 02 | `02_CBum_2024-10_Retirement-speech.mp4` | IN 2026-10-19 (IDM), h264 1080p 29.97, 427.2 s; the 360p stand-in is now obsolete |
| 03 | `03_CBum_2026-10_The-Standard-trailer.mp4` | IN, 1080p, 24000/1001, 124 s |
| 04 | `04_CBum_2018-09_Hospital.mp4` | IN (IDM), h264 1080p 59.94, 1697.4 s |
| 05 | `05_GenerationIron_2019-05_Breon-Ansley.mp4` | IN (IDM), h264 1080p 23.976, 901.3 s |
| 06 | `06_CBum_2024-11_One-Last-Ride.mp4` | IN (IDM), h264 1080p 23.976, 1312.5 s |
| 07 | `07_NSP_2024-11_Prague-results.mp4` | IN (IDM), h264 1080p 29.97, 756.0 s |
| 08 | `08_GregDoucette_2024-11_It-wasnt-close.mp4` | IN (IDM), h264 1080p 29.97, 741.1 s |
| 09 | `09_CBum_2025-08_Honest-thoughts.mp4` | IN (IDM), h264 1080p 24, 1193.3 s |
| 10 | `10_NSP_2026-05_Comeback.mp4` | IN (IDM), h264 1080p 29.97, 761.2 s |
| B1 | `B1_CBum_2024-11_Prague-posing.mp4` | IN (IDM), h264 1080p 25, 173.9 s |
Queue format (verified 2026-10-14): our 10 lines use only `bv*[vcodec^=avc1][height<=1080][height>=720]+ba[ext=m4a]`, no
fallback, so a clip without a ≥ 720p H.264 stream fails (no file) and the Onyx session reports it; that one goes to the creator's
IDM. Still probe every landing; a sub-720 file is renamed `_<h>p-standin`, never cut from.
