# RUN — skool-vsl-2026-11

## ▶ STATUS: resume here (REVISION 1 from his Tella review, 2026-11-14 00:15)
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
