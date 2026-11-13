# RUN — skool-vsl-2026-11

## ▶ STATUS: resume here (REVIEW 2 DONE, 2026-11-14 ~04:20): main re-saved in ABW11; he exports
**His review 2:**
- "You cut 'for a whole year' too early." **as3b** now ends where "year" decays (417.435; the aligner's "or" at 417.34 was the r of "year"), +18 f. Its A1 ramp is dropped because it ends in silence.
- **His own edit, kept:** after hand-over he ripple-deleted **g6 "and you stay"** on all main tracks (a doubled phrase: g7 itself starts "you stay"; the bounce ASR had hidden the repeat).
  - My replay first overwrote it (V1 46 → 47). It was recovered from the 03:43 auto-save (`work/autosave/`, `read_seq.py`) and is now permanent in the EDL: g6 flags `ever`, so it is main-only and the evergreen keeps it.
  - Main is now 46 pieces and matches his V1 piece for piece, plus the as3b fix.
- **Main seal:** g13 → **g13m** (608 f, his 49-f cut; "Free till you hit it" / "Terms" on their words). The evergreen keeps g13 (657 f).
- **His V2 grade layers** (razored at 68.218 by his ripple) are kept; the second one is extended to the new end, 99.983.
- **Rebuilt on main:** V1/A1 46 (EDL-exact, 19 motion pieces, chain on all, ramps g5/d1a), V3 19, V4 `cap-alpha-g`, SFX 30.
- **Checks:** gate 0 FAIL; mix −16.9 LUFS, no flags; max A1 joint step −40.6 dBFS; as-heard "…I refund every dollar and you stay in free until you hit the terms", "…for a whole year". Frames: `work/rev1/rev2-aside-end.jpg`.
- **The evergreen is unchanged** since rev 1.
- **Lesson** (lab-notes + memory): diff live V1 against the delivered EDL before ANY replay.

## ▶ STATUS (REVISION 1 DONE, 2026-11-14 ~02:45, superseded by review 2 above)
**Export these two** (the "(pre-rev1 snapshot)" sequences beside them are backups):
- **"Skool VSL 2026-11"** (main): V1 47 / V2 his grade layer / V3 19 / V4 cap-alpha-e / A1 47 / A2+A3 30 SFX; ends 1:40.50.
- **"Skool VSL 2026-11 evergreen"**: V1 37 / V3 16 / V4 cap-e-alpha-e / A1 37 / A2+A3 27 SFX; ends 1:22.75; no grade layer.

**Fresh-eyes review (Sonnet; `review/REV1-REVIEW-BRIEF.md` → `review/rev1-findings.md`), all 141 + 110 program frames:**
- 1 defect: help1 opened on a downward READING glance (src 101.70–102.06, under "and have helped", so it can't be trimmed).
  - g06 now holds 26 f past the cut (`g06-c`, 597 f).
  - Its old wipe to black (built for g06→g07) is removed, so it hard-cuts to him on the lens.
  - Captions stay visible over that tail (`hide_end`), with no collision.
  - Verified on program frames: `work/rev1/g06-cut-check.jpg`.
- Uncertain items, judged:
  - one-frame eyes-low at the d3 tail (blink);
  - the last caption over g18 is spoken there (as in rev 0);
  - g08/g11 plan-vs-build copy is rev 0's, unchanged;
  - Methos "5.2M in 2 months" doesn't contradict "monetized with 10M": it's the path to the threshold.
- The remaining areas are clean: new face spans, CTA headroom, every graphic edge, the g13 underline is gone, the dissolves frame-diff smooth, and the captions.

**Gate:** 0 FAIL (`hf-graphics/qa-rev1.txt`). **Mix:** −16.9 / −16.7 LUFS, peak −5.6. **Joints:** within 12 px on both cuts.

**Last checks (advisor, final):**
- **Vertical reading scan:** `work/plan/gaze_down.py`, a lid-opening measure calibrated on help1's glance (reading 0.21–0.29, on lens 0.34–0.38; threshold in `work/plan/gaze-down-threshold.json`), run over all 19 face pieces (`transcript/gaze-down-main.json`). Every flag was checked on 4K eye crops (`work/rev1/down-eyes.jpg`, `down-sheet.jpg`):
  - help1: fixed (g06 hold).
  - **cta_m 386.79–386.94:** a 0.15 s downward nod on "pick". Natural, left as is: no graphic can cover a face CTA.
  - **d3 382.53–382.83:** a 0.3 s downward glance mid-sentence. Unchanged from rev 0, which he watched and did not flag.
  - Everything else is blinks, smiles/squints, or the g2 hand-gesture head-dip (adjudicated in rev 0).
- **g13** shows "Terms pinned inside" with no underline. **g11's** gold lines are its data streams (unchanged).
- **Final audio:**
  - `mech_scan` on the final EDL shows only the accepted flags.
  - A hard-cut bounce plus the 4 ramps (`work/bounce-final-*.wav`): max joint step −40.6 dBFS on both cuts; re-heard clean.
- **Overlay clearance** after the re-framing (the hook base is now 1.067; rev 0 had more): every face overlay keeps ≥ ~140 px from his head (`work/rev1/overlay-clearance.jpg`).

**Lessons from his review 1** (no channel preset owns this job; the durable ones are saved to memory as `feedback-natural-speech-whole-lines`, `feedback-subtle-transitions` and the 2026-11-14 entry in `feedback-premium-sfx`):
1. A copy-rule excision that breaks a one-breath sentence reads as a botched cut. → Keep spoken lines whole; copy rules govern on-screen text.
2. "Happening more than once" means scan the WHOLE cut. → `work/plan/mech_scan.py` + slice ASR + an A1 joint step scan before every delivery.
3. Push-through zooms read cheap. → Soft dissolves through the plate (`REV1-BRIEF.md`).
4. Reused kit SFX (counter, paper, ticks) read cheap. → A fresh Epidemic set per job, swish family only, crest-aligned.
5. A zoom at the CTA pushed his head out. → Head test on the transformed frame (`gen_v1.py` + `hair_top.py`); no IOD size matching (yaw noise).
6. An FS→face cut must land on the lens. → The gaze check must cover pitch (looking DOWN), not only the screen-side yaw. The iris-yaw check missed help1's head.

## ▶ STATUS (REVISION 1, advisor final-check fixes, 2026-11-14 ~02:20, superseded)
The block below was the first "built" state. The advisor's final check sent these back, and they are now done:
- **SFX were rebuilt to his written rules:**
  - the swish family only (`sfx/crisp/`, tails trimmed to crest + 0.2 s);
  - press-soft (foley drops), impact-soft and swell-soft ("Impact"/"Riser" titles) are no longer used;
  - count-ups, presses, settles and cuts to the face are silent;
  - 30 cues main, 27 evergreen, placed, mix flags none.
- **Size match is OFF** in `gen_v1.py`. The interocular distance swings with yaw (~9 % scatter on program frames). Position lock, centring and vertical balance stay; the head test passes on all 19 pieces.
- **A1 joint scan** (sample step + 5 ms RMS each side):
  - help1 now ends at 103.053, keeping the whole "s" of "others" (it was clipped at −31 dB). Everything after shifts +11 frames, and plans, words, captions, V3 and SFX were rebuilt.
  - Level ramps sit INSIDE the clips at the edges that cut inside sound: g5 out 10 ms, g6 in 8 ms, d1a in 8 ms, as3b out 25 ms (`work/plan/a1_ramps.py`, read back on both cuts).
- **Premiere:** V1/A1 were replayed and re-baked again on both cuts (47/37 exact). V3 was re-placed (19/16); his layer was re-trimmed to the new content end (100.5005).
- **Gate:** 0 FAIL. **Mix:** −16.9 / −16.7 LUFS, peak −5.6 dBFS.
- **Captions** are being re-rendered as `-e` for the +11-frame shift, then go to V4.

## ▶ STATUS (REVISION 1 BUILT, 2026-11-14 ~02:15, partly superseded by the block above)
**Where each Tella note landed:**
1. **SFX:** a fresh Epidemic set in `sfx/` (31 takes, 7 soft classes, screened by `sfx/tools/sfxtool.py`; `sfx/LIBRARY.md`). The old set is off both timelines.
   - No counter, paper, pen, tick, click or riser sounds.
   - The 600M count is a soft swell cresting on the landing.
   - Every cue is crest-aligned to its motion (`work/plan/sfx_plan.py`) and levelled by measurement, 14–19 dB under the voice.
   - Main has 34 cues, evergreen 31. Mix: −16.9 / −16.7 LUFS, peak −5.2 dBFS, 0 weak cues (`work/plan/mix_check.py`).
   - Not heard by ear (silent work). The builder flags the foley-sourced takes and swell-soft-1 ("Asphalt Reversed", on the 600M count) as first to audition.
2. **Retakes:** the deleted "Views" is cut. The whole cut was re-scanned (mech scan + slice ASR); found and fixed the help1 stumble, the d1a "af" cut-off, the as2 "pack" cut-off, and two hesitations.
3. **Transition line restored:** "and have helped countless others, to get theirs monetized as well", on the lens.
4. **Methos restored** to "…with 10 million engaged views"; g07 re-timed.
5. **g09→g10→g11:** the push-throughs are now soft dissolves through the plate. Real-speed preview: `review/rev1-dissolves-g09-g11.mp4`.
6. **Guarantee:** natural speech ("…10 million engaged views, I refund every dollar, and you stay in free…"). The g13 red underline is removed.
7. **Feb 1:** the 0.45 s silence after "31st" is cut.
8. **CTA:** one take, no push, no zoom-in. Head lock + size match; measured headroom 88 px (`gen_v1.py` head test).
9. **Pauses** around "pick annual" / "349" are gone; "349" starts at its breath.
10. **The Skool aside** is restored (main only), three takes head-locked, with its hesitations trimmed.
11. **Sign-off** is his one take, with the g18 end card arriving on "inside".

**Lengths:** main 98.3 s of speech, ends at 1:40.3. Evergreen 80.6 s, ends at 1:22.6. Main is now ~8 s past "90 seconds".

**Verified:**
- V1/A1 match the EDL, lip sync exact.
- QA gate 0 FAIL (`hf-graphics/qa-rev1.txt`; 71 waived with reasons, g16a/g16b/g17 waivers added).
- Program-frame grabs: `work/grabs/rev1m` (142) + `rev1e` (111).
  - Every face joint within 9.5 px (`work/plan/joint_check.py`). IOD "size" readings up to 12 % are head turns, checked by eye (`work/rev1/joints-size.jpg`).
  - Sheets: `work/rev1/face-sheet.jpg`, `gfx-sheet.jpg`, `ever-sheet.jpg`.
- g16b's lockup is centred (it sat low once the price block left), rendered `-e`.
- Project saved.

**Not done / his call:**
- No grade on the evergreen (only main has his V2 layer).
- Captions say "package" where he says "packet".

## ▶ STATUS (REVISION 1 BUILD in progress, 2026-11-14 01:40, superseded)
- **Cut locked:** `transcript/build-cuts-v2.py` → `transcript/cuts.json` (47 pieces, 98.31 s) + `cuts-evergreen.json` (37, 80.56 s).
  - Every piece has a stable ID and is frame-snapped.
  - The pre-rev1 EDLs are `transcript/cuts.r0.json` / `cuts-evergreen.r0.json`.
  - Verified by bounce + ASR (`work/bounce-v2-*.heard.txt`), slice ASR at every changed edge, and `work/plan/mech_scan.py`.
  - Remaining scan flags are accepted: word-onset cut-ins at g2/g6/d1a; help1/help2 have no words in words.json; "after" is doubled by the aligner.
  - **Extra pause trims, measured:**
    - help1 starts on its own "and" (101.69); 100.43–101.30 is a stumble.
    - price starts at the breath.
    - as2 is split at the 0.55 s "a … three-month" hesitation.
    - as3 is split, with its 0.5 s comma pause cut to ~0.2 s.
  - **Edge fixes:** d1a starts at 303.687 (one "after"; 303.865 cut off "af"). as2's end is 408.708, after "package"; 408.55 was mid-word.
- **Downstream re-keyed BY PIECE ID** (no index math left):
  - `work/plan/make_plan.py` → `graphics-plan.json` + `graphics-plan-evergreen.json`;
  - `words_by_comp.py`;
  - `tl_words_v2.py`: timeline words = piece texts force-aligned on each cut's bounce, which replaces the timed DROP lists;
  - `make_captions.py` (both cuts from their own words) and `make_cap_comp.py`;
  - `joints.py` + `hair_top.py` + `gen_v1.py` (windows from `work/plan/face-windows.json`);
  - `place_gfx_ever.py` (reads the evergreen plan).
- **New face spans checked:** gaze clean (`transcript/gaze-face-rev1.json`, 7 spans, 0 glances); dandruff none (`work/rev1/speck-sheet.jpg`).
- **Premiere (ABW11), both sequences:**
  - V1/A1 cleared and replayed: main 47/47, evergreen 37/37, EDL match and lip sync 0 mismatches.
  - Motion baked (`work/pp-v1*.jsx`):
    - head lock with SIZE matching;
    - centred chains and a vertical balance;
    - pushes on "They don't" and "I take the risk" only, none at the CTA;
    - head test passes on all 19 face pieces (measured hair top ≥ 24 px; CTA 88 px).
  - Audio chain re-measured: kept speech −19.8 LUFS → +3 dB (0.6875) → −6 dBFS limiter, on all clips.
  - His V2 adjustment layer was trimmed 100.367 → 100.317 (the content end); its Lumetri is untouched.
- **Graphics:**
  - A Sonnet builder re-timed g04, g07, g13 (red underline `#u1` removed), g14, g15 and g17.
  - g16 was split into g16a (price) + g16b (pinned lockup).
  - The g09→g10→g11 push-throughs became soft dissolves through the plate (`hf-graphics/gfx/REV1-BRIEF.md`).
  - Renders are `-d` (g10 `-e`: its note now enters at 2.10 so it reads before the dissolve).
  - Main V3: 19 rows placed and verified (`place-graphics.py`, needs `PYTHONUTF8=1`, lab-notes). Evergreen V3: 16 rows, 0 mismatches.
- **Next:**
  - captions cap-d / cap-e-d render → V4 on both;
  - SFX: the builder's fresh Epidemic set in `sfx/` → re-plan by the new comp anchors (`work/plan/sfx_plan.py`), calibrate, clear the old A2/A3, place;
  - QA gate, program grabs + joint check, mix check, save, advisor, hand-over.

## ▶ STATUS (REVISION 1 from his Tella review, 2026-11-14 00:15)
**His Tella 1** (`review/tella1/guide.mp4`, 5:15; transcript `review/tella1/transcript.json`). "Overall the editing style is fine… refine THIS project, don't rebuild." His timeline edits, read back (data, keep):
- razors on V1 at src 40.240 / 387.654 / 389.689 (markers of the notes below);
- an **Adjustment Layer + Lumetri on V2 of the main**, 0–100.367: it runs ~13 s past the cut, so trim it to the content end and leave its grade untouched;
- nothing on the evergreen.

The notes, resolved:
1. **SFX not premium.** Go back to Epidemic and pick refined, expensive sounds. The 600M **counter is "absolutely terrible"**. The **paper "tear"**: "we're not tearing anything". The whole set gets replaced.
2. **Retakes left in:** "Views… views" at the g04 start (raw 39.38, a deleted take). Real start = 40.24 (his razor). "Happening a lot more than once" → run the fresh-eyes mechanical pass on the whole cut.
3. **Restore the transition line** before Maciej, so "Mac is not me": "and have helped countless others get theirs monetized as well" (last take, raw 101.12–102.85 + 105.82–107.3). On the lens.
4. **Methos:** don't cut "to getting it monetized" halfway. Restore "…with 10 million engaged views" (raw to ~173.2).
5. **Push-through transitions (g09→g10→g11) too dynamic** ("going in and popping out"). Make them subtle, minimal, refined, expensive.
6. **Guarantee:** "…10 million | views | I refund" is cut mid-speech twice. Restore natural speech ("10 million engaged views, I refund every dollar"). **Remove the red underline** under "Miss 1K subs + 10M Shorts views?" ("what is this line doing").
7. **Feb 1:** cut the silence inside "after January 31st … the requirement literally doubles" (raw 304.85–305.38).
8. **"Click JOIN, pick annual":** a weird zoom-in ("why am I going down and zooming in"); his head goes up out of the frame. The face must sit centred vertically. No push there; reframe.
9. **Pauses around "pick annual" / "349":** trim them (raw 387.6–389.6). This also removes the glance that g16's early start covered.
10. **Restore the Skool aside** (main only, it's price): "actually I priced it at three months, but Skool doesn't have a three-month package, so I just gave the 349 price tag for the whole year, so you can stay here for a whole year" (raw ~397.3–417.1, on the lens).
11. **Sign-off in his ONE take:** "I will see you, ladies and gentlemen, inside" (raw 460.64–462.80).

**Overrides of the copy rules, by his explicit instruction:** "countless others" (3), spoken "engaged" (4, 6), "priced it at three months" (10). On-screen copy keeps "10M Shorts views".

## ▶ STATUS (BUILT before his review, 2026-11-13 ~22:00, superseded)
- **Deliverable:** two sequences in ABW11 (bin "Skool VSL 2026-11"):
  - **"Skool VSL 2026-11"** (main, 1:27, 5215 f):
    - V1 42 pieces (head lock + drift + 3 pushes);
    - V3 18 graphics (`hf-graphics/placement.json`);
    - V4 captions `cap-alpha-c.mov`;
    - A1 +3 dB → −6 dBFS limiter;
    - A2/A3 39 SFX.
  - **"Skool VSL 2026-11 evergreen"** (1:17, 4613 f):
    - no Feb 1 block, no price;
    - V3 16 graphics (`work/place_gfx_ever.py`), g16e in place of g14–g16;
    - V4 `cap-e-alpha-c.mov`;
    - A2/A3 34 SFX.
  - Grade NOT applied (`work/grade/ember-gold-v2.cube`, his call). Music lane empty (his job).
- **Verified:**
  - **QA gate:** green (0 FAIL; 66 waived with render evidence; g09 targeted re-check 0 FAIL).
  - **Review:** 3 review passes (round 1: two reviewers; round 2: one reviewer over both cuts; round 3: my targeted re-check of the round-2 fixes on program frames). Round-2 verdicts: F2 g09 payoff hold, fixed; F4 caption early lead, fixed; F1 pinned-lockup lead, kept by design (readable hold); F3 not a defect (mid-entrance sample).
  - **Head lock on program frames:** every face joint ≤ 17 px across, ≤ 6 px vertical.
    - The advisor's final check caught a missed face-to-face joint at 73.11 (pieces 33→34 sat in separate windows: a 120 px / +9.6 % same-camera punch). Fixed: one window [33, 34, 35], main V1 re-baked, now −0.1 / +0.2 px. A natural 6.7 % size difference remains, under the g15 JOIN chip landing on that joint.
  - **Lip sync:** V1 vs A1 start/end/in point 0.00 ms on all 42 + 37 pairs.
  - **Project:** ABW11 saved under the lock 22:2x with the final state (read back: main V1 42 / V3 18 / V4 cap-alpha-c / A1 42 / SFX 39; evergreen 37 / 16 / cap-e-alpha-c / 37 / 34).
  - **SFX takes:** all 38 are stereo (no pan-law offset on the calibration).
  - **Mix (offline bounce, `work/plan/mix_check.py`):** −16.5 LUFS, −2.0 dBFS peak on both cuts. SFX re-levelled by measurement (`work/plan/sfx_calibrate.py`): hits 11–13 dB under the voice, whooshes ~20. Placed file+time+level read back 39/39 and 34/34.
  - **Dandruff:** none found. 4K boosted crops of hair, collar/chest and shoulders cover all 7 face windows (`work/speck/check*.jpg`); the red dots at the crown are the neon sign behind his head.
  - **Reading:** one real glance (74.97, tail of "pick annual") now under g16; no other face piece reads (yaw + iris + eye crops).
- **Not done / open:**
  - A third full fan-out round was not run (lean usage). The round-2 fixes have only the targeted re-check.
  - Clicks/ticks read weak in the phone band on a 50 ms RMS metric; they are sharp transients at about −7 dBFS sample peak. Not verified by ear (silent work).
  - SFX come from his approved CA-011/CA-007 premium sets, not a fresh Epidemic set.
  - The About page / pinned terms still need his edits (PLAN § Before this goes live).

## ▶ STATUS (round-1 fixes, 2026-11-13 ~21:00, superseded)
- **In ABW11 (shared; every activation goes through `work/pp.py` window with a verified name|id gate):**
  - **"Skool VSL 2026-11" (main):** V1 42 pieces (motion re-baked, `work/pp-v1.jsx`, head-lock cap 1.25 and the corrected base formula: 0 residual), V3 18 graphics (round-1 versions still placed), V4 captions (`cap-alpha.mov`, round 1), A1 chain at **+3 dB** (voice-gain.py: kept speech −19.6 LUFS; the first +6 came from a mono bounce), A2/A3 39 SFX = `work/sfx-main.json` (0 missing/extra).
  - **"Skool VSL 2026-11 evergreen":** V1 37 pieces (`transcript/cuts-evergreen.json`, 0 mismatches), motion baked (`work/pp-v1-ever.jsx`), A1 +3 dB, A2/A3 34 SFX = `work/sfx-evergreen.json`. **No graphics or captions yet** (`work/place_gfx_ever.py`, `work/pp-captions.jsx` with cap-e).
  - **No GRADE layer:** `grade-layer` failed on Premiere 25.0 (lab-notes) and the approved default is ungraded until Affan OKs; the cube is `work/grade/ember-gold-v2.cube`.
- **QA gate:** `graphics-qa.py` green (0 FAIL; 65 waived with render evidence in `hf-graphics/qa-waivers.json`). Missing assertion to report: no post-transform font-size check.
- **Review round 1** (2 Sonnet reviewers, `hf-graphics/review/r1/`; findings verified by me on full-res frames instead of a skeptic per finding, lean usage), fixed:
  - captions over full-screens / double draw / restated lines / gold word on every line;
  - g03 strike invisible (exit removed; the cut to g04 is the exit);
  - g06 badge text at 9–11 px (qualifier now an unscaled 28 px label);
  - 28 px floor (`_head.html` kicker/chip);
  - g09 top label carried off-frame (camera travel 400 → 190 px);
  - g13 rim text → approved words only;
  - g14 qualifier now stays on through the bars;
  - g16 rebuilt: the card TOP only (the live description is a bare promise plus a $69 button), typed $349/year, JOIN pressed on "year", the pinned lockup holds ~2.4 s, "Tomorrow → first Short"; it **starts 19 frames earlier (74.925)** to cover a reading glance in the tail of "pick annual"; g15 shortened to 109 frames;
  - g16e gets the same lockup;
  - the SFX for g16/g16e moved.
  - Adjudicated, not changed: plan copy synced to the build (g03, g04, g06, g07, g08); "gentlemen" in the transcript is an aligner artefact (slice ASR: it ends 461.82–462.10 raw, piece 41 starts 462.17); piece 24's head-down at 51.6–52.5 s is a gesture (eyes on his miming hand); piece 0's tail has a blink plus ~3 frames of eye drift.
- **Rendering:** `hf-graphics/gfx/render-r2.sh` (g03 g05 g06 g07 g09 g12 g13 g14 g15 g16 g16e g17 g18, cap, cap-e; VER=b).
- **Next:** place-graphics `--plan --write` + `--apply` on main → captions cap-alpha-b on V4 → evergreen V3 (`place_gfx_ever.py`) + V4 (cap-e-alpha-b) → re-run the gate → round-2 grabs on BOTH cuts incl. the unsampled moments (g05 BURIED 15.6–16.6, g06 underline ~23.6, g10 notes 42.2/43.0, g13 terms 65.6, g14 underline 68.9) → round-2 review → advisor → save → hand over (he exports).

## ▶ STATUS (build start, 2026-11-13 18:05, superseded)
- **Affan's OK (~17:20):**
  - **G1:** NO 36M callout. G1 shows the whole AW Shorts grid sorted Popular as the portfolio.
  - **Confirmed:** faceless, viral, and "ESL" = VSL.
  - **New ask:** clean dandruff specks on his shirt and head.
  - **Disk:** C: freed, but all work stays on X:.
  - **Other calls keep their defaults:** grade shown as test frames, captions ON, he exports.
- **Done in the build:**
  - **Gaze:** iris check on the face windows: every glance falls in a cut gap (`transcript/gaze-face.json`).
  - **Dandruff:** NONE found (4K boosted crops of hair, shoulders, collar and chest at 3 times; `work/speck/`). Re-check on the final.
  - **Captures:** R1 (542K), R2 (Popular grid), R3, R4/R5 (About page), R6 (YouTube help) → `hf-graphics/gfx/assets/captures/` (YouTube in dark theme via the PREF cookie). Crops: `crop-*.png`.
  - **Design system and comps:** `hf-graphics/gfx/src/_head.html` + `emit.py` + `snap.mjs` (headless probe) + `render.sh` (59.94, no STEP_FPS: a deliberate departure from the default preset's 12 fps, per the bible's smooth look).
  - **Look test:** g06, g07, g13 rendered → `review/look-test.mp4` + `review/grade-compare.jpg`, sent to Affan 17:51.
  - **Grade:** `work/grade/ember-gold-v2.cube` (one LUT, used for both the test frames and Premiere).
  - **Captions:** `hf-graphics/gfx/captions.json` / `captions-evergreen.json` → comps `cap` / `cap-e` (emitted, not yet rendered).
  - **SFX:** `work/sfx-main.json` / `work/sfx-evergreen.json` (39 / 35 cues, his CA-011 + CA-007 premium sets, no take twice within 60 s).
  - **V1 motion:** `work/pp-v1.jsx` (base per face window, head-steady offsets, drift, 3 pushes; from `work/plan/gen_v1.py`).
- **Running:**
  - A Sonnet builder is making the other 16 comps per `hf-graphics/gfx/BUILD-BRIEF.md`.
  - Premiere window 1 (import + create sequence) is waiting on `ACTIVE-WINDOW.lock`, held by another session since 17:50.
- **Next:** replay the EDL on V1 → Scale 50 + `pp-v1.jsx` → audio polish → grade adjustment layer (cube) → place graphics on V3, captions on V4, SFX on A2/A3 → edit-review → advisor → the evergreen sequence → hand over (he exports).

## ▶ STATUS (pre-build, superseded)
- **Stage:** PRE-BUILD. Max-effort gate order is plan in text → Affan's OK → build. Nothing is built until he says OK.
- **Done:**
  - Intake and sync.
  - Reading measured: `transcript/eye-line-raw.json`, Otsu threshold 0.26, separation 3.37 SD.
  - The words: `transcript/words.json` (align-only fallback; see below).
  - The keep map: `transcript/build-cuts.py` → `transcript/cuts.json`, 42 pieces.
  - Both endings bounced and verified by ear: `work/bounce-*.heard.txt`. Main is 85.0 s of speech, evergreen 75.0 s.
  - **`PLAN.md` v2 is final and SENT to Affan (2026-11-13).**
  - Advisor call 1 (before the plan) and call 2 (on the final plan) done.
  - Cold read done: Sonnet, 25 items, 24 applied, 1 noted.
- **Waiting on:** Affan's OK of PLAN.md, plus his answers to PLAN § Your calls. Defaults: 36M R2 yes · grade shown as test frames · captions ON · he exports · faceless/viral kept.
- **Also waiting on:** C: space freed before the build; R7–R12 captures (all optional, with fallbacks).
- **After the OK:** run `gaze_raw.py` on the 7 face windows → record captures R1–R6 → 10 s look test + 3 graded/ungraded frames → full build per PLAN § How it's built.
- **Transcript caveat:** WhisperX large-v3 ran out of memory twice (C: full). `words.json` = the hand-over's large-v3 text (+10.3934 s) with numbers spelled out, aligned by wav2vec2 (`work/plan/align_only.py`). Edges are verified by the bounce re-transcription plus slice ASR.
- **Brief + sources:** `C:\Users\affan\AppData\Roaming\Claude\side-session-notes\local_58421d66-9faf-454f-a5e9-4b2e8149f8f9\vsl-2026-11-13\HANDOVER.md`. Style bible (written by another session's research agent): `..\vsl-style-bible.md` in that notes folder. Not there yet as of 16:20.

## Step 0
- **Job:** Skool sales video (VSL) for "Youtube Shorts Skool" (skool.com/abundance-school). Target runtime is about 2:00.
- **Format:** 3840×2160 at 59.94 fps, horizontal, so 16:9 long-form. Delivered at 1920×1080, or 4K if Affan wants it.
- **Lane:** premiere (`.setup-complete`). LANES.md Premiere column: steps 2–6 are ✅, step 7 review is ✋, and step 8 export is ✋ the creator. Export is a decision for the plan: Affan exports, or he OKs `exportAsMediaDirect`.
- **Preset:** `presets/youtube/default/` for mechanics (cards, creative moves, SFX plan). The LOOK is Affan's red and gold brief plus the style bible, which beat the default overlay look and the Autumn grade for this video. Grade choice goes in the plan.
- **Sources:**
  - `raw/skool-vsl-synced.mov` is the working raw: the camera picture (C1472, 4K HEVC 59.94, 7:53.97) with the OBS mic muxed on.
  - The mic starts **+10.3934 s** into the camera. Drift is −7.9 ms over 299 s (0.47 frames), so a constant offset is used. Measured by `workflows/sync-dual-audio.py`.
  - The originals' copies are in `work/raw-orig/` (C1472.MP4 and obs-mic-2026-11-13.mp4). The originals themselves are untouched: `X:\Recordings\Onyx\C1472.MP4` and `E:\Shorts\...\Batch Batch\2026-11-13 03-02-59.mp4`.
- **Clock:** every time in this job is on the CAMERA clock, which is the hand-over's OBS clock + 10.39 s.

## Request coverage (owner → evidence)
1. A ~2:00 VSL cut from the 11-13 take, per the hand-over keep/cut map → rough-cut → `transcript/cuts.json` plus the re-transcribed cut.
2. Every reading moment is FULLY masked with overlays, motion graphics and 3D → `transcript/eye-line*.json` → graphics-plan coverage table.
3. Visual demos of what he describes → graphics-plan.
4. Minimal, glowy red and gold, 3D, sharp gradients, subtle eased zooms, an educational-channel blend (Iman Gadzhi as one reference, not a clone) → style bible → PLAN § Look.
5. Offer copy rules on every spoken and on-screen word (70 Shorts in 90 days, "10M Shorts views" never "engaged", 540K+, 600M+ across all channels, only Methos and Maciej as proof, no calls, no "priced at three months") → PLAN § Copy check + the cold read.
6. Real captures only for numbers and proof → PLAN § Captures. Studio 36M, member-area screens and the pinned terms (once they say 70) all need Affan.
7. The Feb 1 lines are one removable block, plus an evergreen ending → two exports.
8. The kit says "Burn in captions" → flagged in PLAN; Affan decides.
9. Export the main version and the evergreen version into `outputs/`.
10. Gate: Fable advisor ×2 (the advisor tool is `claude-fable-5-2`, checked in this session's .jsonl), a cold read of the final plan, and Affan's OK before the build.

## Constraints
- Shared checkout: work in `projects/skool-vsl-2026-11/` only. No commits. Premiere is shared, so check the `lanes/premiere/ACTIVE-WINDOW.lock` and the active project before driving it.
- Lean usage: the weekly limit is at 80 % until Mon 16 Nov ~02:00 UTC.
- **C: is nearly full** (0.8 GB free at 16:18 after deleting this job's own temp folders). Every temp file goes to `work/tmp` on X:. 4K HEVC decode can hit out-of-memory while Premiere holds ~9.5 GB, so analysis runs on `work/proxy-4fps-960.mp4`.

## Steps
| # | Step | Status | Evidence |
|---|---|---|---|
| 1 | Intake | done | `raw/skool-vsl-synced.mov`, `work/raw-orig/` |
| 2 | Rough cut | EDL done (RENDER=0), proven by ear | `transcript/cuts.json`, `work/bounce-main.heard.txt`, `work/bounce-evergreen.heard.txt` |
| 3–8 | | pending (waits on Affan's OK of `PLAN.md`) | |

## Flags to report
- C: is at 0.8 GB free, a machine-wide risk (pagefile, other sessions).
- "ESL" in his brief is read as dictation noise for "style"/"VSL".
- Before this video goes live, the About page and pinned terms must say 70 Shorts in 90 days.

## Skipped, and why
- Gate item 1 (Instagram and YouTube proof per beat, other tellings, other voices) does NOT apply: this is a VSL of his own footage, with nothing to source. Said in the plan.
