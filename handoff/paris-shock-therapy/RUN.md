# Paris Shock Therapy — RUN

## ▶ STATUS: resume here (2026-11-03): v2 DELIVERED (his note 1: Higgsfield upscales), at his review
- v2 `Paris Shock Therapy.mov` (sha256 1005129…) is in Final Renders + Exports + `outputs/`. v1 is kept as
  `Paris Shock Therapy (v1).mov` in all three.
- What changed (BRIEF § HIS REVIEW NOTE 1):
  - S6 is `assets/mj_paris_redcurtain_hf.png` (Higgsfield 4K, lanczos to 1217 px).
  - S3 is `dl/hf/S3_stroll_topaz_1216x2160.mp4` (Higgsfield Topaz 2160p), plus a pre-grade level on shot S15:
    gain 0.66, gamma 1.08, pre_blur 1.0.
  - Renders: `renders/stageA_v2.mov` → `renders/finish_v2.mp4`. Captions and mix unchanged.
- Recipe as below. Stage A only when the shots or picks change; new render names for every version.

## (previous) STATUS (2026-11-02 ~21:15): v1 DELIVERED, at his review
- `Paris Shock Therapy.mov` is in Final Renders and `X:\Claude Projects\Exports\`, identical to `outputs/` (sha256
  c8c5cf0c…).
  - 42.40 s (his cut), 1080×1920 at 30 fps, 34.9 Mb/s, PCM.
  - −14.1 LUFS / −1.6 dBTP.
  - `build/export.py` QA PASS.
- QA on the file:
  - `proof/final_edges.jpg`: 26 cuts clean.
  - `proof/final_asr.txt`: exact words.
  - `win/lipsync_mesh_v.py`: ECT lag +1.2 / −0.2 frames (was +7).
  - `proof/bilabial_final.jpg`.
  - The B3 head pause is 0.21 s.
- REPORT.md has the full list and the open points: the 42.4 s length, the studio overlay framing, and the childhood shots
  per his Q1.
- **A review note = data + ONE finish render** (memory feedback-fix-only-what-he-named):
  - picture → `build/make_timeline.py` (overlay picks, framing, transitions, sat_level), then `stage_a.py render` only if
    the shots or picks changed (~8 min);
  - captions → `captions/captions.txt` → `make_plan.py` → `render_caps.py render` → `capcut_pass.py`;
  - audio → `build/dialogue.py` / `build/mix.py`;
  - then `build/finish.py render renders/stageA.mov renders/caps_capcut.mov renders/finish.mp4 --audio renders/mix.wav`
    (~8 min) → `build/export.py`.
  - A re-render gets a NEW name if Premiere ever imports it.

## (previous) STATUS (2026-11-02 ~20:15): CODE BUILD RUNNING (his go "Yes, build it")
- His answers are in BRIEF § HIS ANSWERS: Q1 = use the childhood shots, Q2 = caption-only censor (K\*LL MYSELF).
- The catalog pass and the overlay picks are in BRIEF (both written before Stage A).
- **Kit** (Conrad's, copied into `build/` and `captions/`):
  - `build/make_timeline.py` reads HIS cut, `premiere/his_cut.tsv`.
  - Source span = in + (t1 − t0).
  - ECT picture is 6 frames early.
  - 3 freeze frames hide ET's own cuts (Jay frame 255, Paris frames 423 and 1518), each under his flash.
  - It writes `timeline.json` (27 shots, 15 zooms, 12 transitions), `overlays/picks.json` and `pieces.json` (19 audio
    pieces).
- `build/track.json`: the head lock. The raw tracks are kept in `track.raw.json`. Shots with lock error > 3 source px
  (S13, S20, S21, S23, S25, S27) get a smoothed follow (sigma 3 frames) instead of a hard lock.
- Audio:
  - `build/dialogue.py` builds `renders/dialogue.wav` with 15 ms joints and the B3 head fragment ducked.
  - `build/mix.py` builds `renders/mix.wav`: −14.10 LUFS / −1.60 dBTP, swishes −21 dB, ECT card −24 dB, no music.
- Captions:
  - `captions/make_words.py` builds `captions/transcript/words.json`, with "was" and "the" inserted from his A1 ASR.
  - `captions/captions.txt` holds 66 captions, 19 coloured, Jay italic.
  - `make_plan.py` → `render_caps.py render renders/caps_code.mov` → then `capcut_pass.py` (GPU, AFTER Stage A).
- `build/finish.py` adds `ect_mg` (the pulse-line ECT card).
- RUNNING: `build/stage_a.py render renders/stageA.mov` (GPU) and the caption render (CPU).
- NEXT:
  1. `captions/capcut_pass.py renders/caps_code.mov renders/caps_capcut.mov`.
  2. `build/finish.py stills` → check skin, overlays, the MG and labels.
  3. `build/finish.py centers` → `render renders/finish.mp4 --audio renders/mix.wav`.
  4. `build/export.py renders/finish.mp4 renders/mix.wav "outputs/Paris Shock Therapy.mov"`.
  5. QA: every cut frame by frame, a bilabial strip on ECT, final-mix re-ASR, gap check.
  6. Copies to Final Renders + Exports → REPORT.md → LESSONS.

## (previous) STATUS (2026-11-02 ~15:30)
- **His Tella direction 1 is IN and resolved** into BRIEF.md § HIS DIRECTION 1. It covers:
  - his re-cut, 42.40 s, which is the spec (`premiere/his_cut.tsv`, read-only; never re-place over it);
  - 6 overlay slots + 1 motion graphic;
  - 12 transitions (purple / dark green / cyan);
  - the lip-sync fix: the ET On Purpose audio is 0.20 s late, so ECT picture is taken 6 frames earlier.
- **WAITING on his answers + go:**
  - Q1, minors: a photo of Michael with his daughter, and the memorial fallback (she was 11), against the brief's
    no-minors rule;
  - Q2: censor "kill myself"?
  - his OK on the build quote.
- **Build quote:** about 7–10 % of the weekly cap in a FRESH session started from BRIEF.md + RUN.md; more if this long
  session continues. The extra over the usual 4–6 % is sourcing 5 overlay videos + 2 stills and the ECT motion graphic.
  Any sourced still that is too soft goes through Higgsfield; those credits need his approval first.
- On go, the build steps:
  1. Catalog pass into BRIEF.md (CLAUDE.md learning loop 5).
  2. Source the overlays (his drives first, then YouTube with H.264 forced; HQ check).
  3. Code build from HIS cut: copy `projects/conrad-murray-didnt-kill-mj/build/`, with the 6-frame ECT picture slip,
     the transitions per BRIEF and the defect fixes.
  4. −14 LUFS / ≤ −1 dBTP on the file, `.mov` to Final Renders + Exports, §8 QA, REPORT.md.

## (previous) STATUS (2026-11-02 ~01:30)
- **RAW SEQUENCE PLACED in ABW10, NOT saved** (he saves): bin **"Paris Shock Therapy"** › **"Paris Shock Therapy -
  raw cut"** (id `61cd64ac-5454-4e5d-a820-04118a306c84`). It is 1080×1920 **30.00 fps** (clone of "Onyx reaction
  template (empty)" set to 30 / display 104), **47.50 s**:
  - V1/A1 24 clips, source audio only.
  - V2 10 picture-only covers/holds, A2 empty.
  - 5 beat markers (name, card, warning).
- His active sequence ("Sequence 37", `acc40c22-…`) was restored right after placing. The later one-frame fix
  (`premiere/fix_b2_head.js`) ran without switching sequences.
- **Verified by read-back** (`premiere/readback.tsv`, `win/verify.py`):
  - Every clip matches the plan, with no gaps. The ≤ 36 ms in-point shifts are Premiere flooring in-points to the
    30 fps grid, and all of them land in silence.
  - Picture as held: `proof/sim_readback.jpg` shows only Paris or Jay, no Willow, photos or ET graphics.
  - A1 rebuilt from the read-back and re-transcribed (`win/asr_a1.json`): the brief's words, nothing leaked at any of
    the 23 joins, no ET narrator, no Willow.
  - Hard rule 1 on the assembled A1 (`win/gap_check.py`): the longest quiet run is 0.28 s (B5 "louder … thing",
    mid-phrase). All others are ≤ 0.22 s.
- **WAITING for his Tella direction video.** Nothing else runs before it: no build, grade, captions, Topaz or render.
- When it arrives:
  1. Transcribe it, and sample the frames he points at.
  2. Resolve every note into BRIEF.md.
  3. If he re-cut the sequence, dump HIS sequence read-only; his cut is the spec.
  4. Do the catalog pass into BRIEF.md (CLAUDE.md learning loop 5).
  5. **Quote the build cost**, then do the code build (copy the newest AW build, e.g.
     `projects/conrad-murray-didnt-kill-mj/build/`).
- Open questions for him are in BRIEF.md § "Brief vs his standing rules": music, caption height, labels at the bottom,
  censoring "kill myself", the "dry" ending (ET's music is under all of RTT), and the words to settle by ear.

## Job facts
- Brief: `X:\Claude Projects\Abundance Wisdom\PARIS-SHOCK-EDITOR.md`. Decisions: [BRIEF.md](BRIEF.md).
- Export (later): `Paris Shock Therapy.mov` → `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders` + identical copy
  in `X:\Claude Projects\Exports\`. Never C:, no phone copy unless asked.
- House rules: never save or export his Premiere project; never close Premiere or AE; work in silence; no Fable
  agents; one heavy GPU job at a time (check `nvidia-smi`).
- **Shared ABW10 (orchestrator, 2026-11-02): three sessions share it, and Affan has been cancelling import-failure
  dialogs.**
  - Wrap EVERY Premiere window (read-back, dump, place, fix) in the shared lock: `mkdir`
    `projects/_onyx-batch2-2026-10/.locks/premiere.lock` with a 15 s retry loop, write your name and the time into
    `owner`, and remove the directory when the window ends.
  - Never overwrite a file Premiere has already imported; re-renders get new names.
  - `lanes/premiere/dialog-watch.py` closes import-failure modals, so don't run your own closer.
  - Details: `lanes/premiere/lab-notes.md` (2026-11-02), `presets/youtube-shorts/abundance-wisdom/SESSION-START.md`.

## Pipeline
| # | Step | Status |
|---|---|---|
| 1 | Intake: ECT + RTT copied from `E:\Bullshit Folder\Henry\` → `raw/`; `seq_src/` H.264 CRF 12 + PCM 48 k | ✅ |
| 2 | Words (long-form WhisperX, same files) + edges by ear-proxy (`win/snip*.txt`) + picture edges (`win/fstep.py`, `win/focus.py`) | ✅ 47.50 s |
| 2b | Raw sequence in ABW10 (30 fps), read-back verified, A1 re-ASR | ✅ |
| 2c ✓ | His Tella resolved (BRIEF § HIS DIRECTION 1), answers Q1/Q2 | ✅ |
| 3–8 | Code build → export → QA → REPORT | ✅ v1 2026-11-02 |
| — | Music | default none (his rule); the brief asks for a piano: open question |

## The cut (actual, from the read-back; source = the ET clip's own clock)
| Beat | Timeline | Source in → out | Words |
|---|---|---|---|
| 1 | 0:00.00–0:12.43 | ECT 0:27.00–0:28.70 · 0:29.17–0:39.90 | "They knock you out, strap you down … inside of my head." |
| 2 | 0:12.43–0:20.47 | ECT 0:08.50–0:10.33 · 0:11.37–0:16.27 · 0:17.43–0:18.73 | Jay: "The ECT therapy was because of a particular suicide attempt, is that right?" Paris: "I got very, very close, like centimeters away." |
| 3 | 0:20.47–0:24.60 | RTT 1:47.73–1:50.70 · 1:51.53–1:52.70 | "It was really hard, and people would tell me to kill myself every day. And I was depressed." (fallback) |
| 4 | 0:24.60–0:35.27 | ECT 0:48.80–0:52.03 · 0:52.87–1:00.30 | "The side effects are gnarly. I mean, I definitely had days… completely not in my head at all. I'd have, you know, friends visit me, and I don't remember even seeing them." (full sentence) |
| 5 | 0:35.27–0:47.50 | RTT 2:06.40–2:07.17 · 2:07.37–2:07.83 · 2:07.97–2:15.00 · 2:15.20–2:19.13 | "There were some dark, dark times … I feel like my dad would be proud." HARD CUT at ET's cut (2:19.14), before "In 2018" |

V2: B2 head hold (Jay frame 255, 1 f) · B1 tail hold (ECT frame 1193, 3 f) · B3 RTT 1:12.47 + 0:50.43 · B4 ECT 1:09.10
wide + 1:10.30 CU, tail hold frame 1801 (6 f) · B5 RTT 2:04.43, 1:39.30, 0:00.50 (Paris close-ups over Willow).

## How it was built (re-run recipe)
```
python premiere/make_beats.py                                   # sources.json, transcript/words.json, beats.json
python ../../presets/youtube-shorts/abundance-wisdom/resolve_beats.py . --fps 30              # -> edl.json
uv run ../../presets/youtube-shorts/abundance-wisdom/plan_placement.py . --fps 30 <splits in premiere/plan.out's run>  # -> placement.json
python ../../presets/youtube-shorts/abundance-wisdom/place_sequence.py . "Paris Shock Therapy - raw cut" "Paris Shock Therapy" premiere/place.jsx
premiere/pp.py: active.js → create_seq.js → place.jsx → restore_active.js (his ID) → fix_b2_head.js → readback.js > readback.tsv
python win/verify.py ; uv run --with pillow python win/sim.py --readback proof/sim_readback.jpg ; <gpu python> -I win/asr_a1.py
```
Splits (camera cuts inside pieces): ECT@14.1141, 31.8652, 33.7003, 50.6507; RTT@109.1091, 111.9785, 128.6619, 131.2645,
132.2655, 134.9682, 137.7376. **Re-place only if he has NOT edited the sequence**: clear our V1/A1/V2 clips first (the placer
refuses non-empty tracks), and keep the switch window short.

## Notes for the build
- The 2026-11-02 patch adds `--fps` to `resolve_beats.py` / `plan_placement.py` (default 60, unchanged).
- ET bugs: ON PURPOSE (top-left) and ET (bottom-left) sit outside the face crops, except the B4 wide cover, which
  shows "…RPOSE" in the top band. FB icon top-right on RTT 2-shots.
- ET music is under all RTT lines and under B4's first sentence. Level-match the eras in the mix; it can't be removed.
- Thriller card: ET lower-third on RTT 2:13.3–2:16 (2-shot crop slid right; the Willow part is covered).
