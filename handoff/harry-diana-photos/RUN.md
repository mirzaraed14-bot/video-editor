# Harry Diana Photos — RUN

## ▶ STATUS: resume here (2026-11-04 ~20:15): v4 DELIVERED (his review 3 applied), at his review
- **`Harry Diana Photos.mov`** = v4 (sha256 f260cdf5…) in Final Renders + Exports + `outputs/`: 41.63 s, 39.0 Mb/s,
  −14.1 LUFS / −1.6 dBTP, export QA PASS. v3 kept as `(v3).mov` (61aafa85…), v2 `(v2)`, v1 `(v1)` in all three places.
- His review 3 (BRIEF § HIS REVIEW 3): same person + same camera = ONE zoom layer across its jump cuts; a new layer only on
  a change of person / camera / overlay → `make_timeline.py` groups same-source + same-setup face runs again (20 layers):
  0–2.90 (through "yep"), 23.20–29.13, 31.83–33.97. Everything else = v3 (transition curve, long_curve, O3 hold,
  pre_sharp). Render `renders/finish_v4.mp4`; v3's timeline kept as `build/timeline.v3.json` / `zoom_layers.v3.json`.
- Checks: `win/zoom_paper.py` PASS (out 30–43 %/s, in 18–28 %/s, next start ≤ 2.2×), `proof/v4/joints.jpg` (no size step
  at 2.53 / 27.2 / 27.9 / 32.63), `proof/final_edges_v4.jpg` (23 cuts clean, CTA pills in).

## (previous) ▶ STATUS (2026-11-04 ~19:30): v3 DELIVERED (his review 2 applied)
- **`Harry Diana Photos.mov`** = v3 (sha256 61aafa85…) in Final Renders + `X:\Claude Projects\Exports\` + `outputs/`:
  41.63 s, 1080×1920 30 fps, 38.6 Mb/s, −14.1 LUFS / −1.6 dBTP, export QA PASS. v2 kept as `(v2).mov` (887c902c…), v1 as
  `(v1).mov` in all three places. ABW10 checked read-only first: no item references any Harry export.
- Render: `renders/finish_v3b.mp4` (from `renders/stageA_v2.mov` + `caps_capcut.mov`; mix `renders/mix_v2.wav` unchanged).
  `finish_v3.mp4` = the same without the long-shot curve (superseded).
- Checks: `win/zoom_paper.py` PAPER PASS (every cut: out 35–43 %/s, in 18–27 %/s, next start ≤ 3.2× the previous end);
  `proof/zoom_gate_v3.txt` (all 24 shots IN; its one "flip" is S13→S14 read inside the purple dip, the AP clip zooms IN
  from frame 0, +1.6 %/s on the 60 fps finish); `proof/final_edges_v3.jpg` (23 cuts clean, both CTA pills in);
  `proof/v3/joints_deepest.jpg` (same-camera size resets, deepest face frames clear).
- Long shots (> 2.5 s: S01, S04, S15, S23) use `finish.py long_curve` (fixed-speed start burst + end pick-up, timeline
  `zoom_long_after` 2.5), his long shots' measured behaviour; ≤ 2.5 s keep the table (they meet within ~2 % at 2.5 s).

## (previous) ▶ STATUS (2026-11-04 ~17:30): HIS REVIEW 2 (text) being applied → v3
- His note (BRIEF § HIS REVIEW 2): v2's sine-eased zooms "miss the plot"; his zoom is a TRANSITION zoom (strong start,
  drifts, picks up at the end, straight into the next shot at the same intensity); plus "weird artifacts because of the
  Topaz" to fix before he publishes.
- **Measured (done):** `win/his_zoom.py` (frame-by-frame, each frame registered to its shot's first frame; calibrated on v2's
  known zooms, ±1–2 %) on his ABW6 03 / ABW8 34 / ABW8 39 finals: start +30..+65 %/s, middle +2..+9 %/s, end +15..+30 %/s,
  totals +15..+45 %, ~80 % push-ins = README § 3's table. v1 had the table but PULLED OUT on 8 of 23 shots (sign flips at
  cuts, e.g. "Mainly proof" −23 → +53 %/s) and O3's AP clip zooms +92 % on its own (+50 % in < 1 s with ours on top).
  Results in `win/hiszoom/*.txt`.
- **Artifacts (found):** the raw Topaz files are clean; his PRE sharpen bands + Sharpen 40 turn their smooth surfaces into a
  painted look (O1 faces, O3 ambulance, O5/O6 crowd faces, ITV5/ITV10 dark edge halos). `proof/topaz/`.
- **Applied (make_timeline.py, finish.py):** `zoom_curve: 'table'`; ONE zoom per SHOT (restarts at 1.00 on every cut, as
  his 4/4 same-camera joints do), all push-ins at v1's depths, short shots capped at a ~45 %/s start (`depth()`), O3 held.
  Artifacts: NOT Topaz itself (raw upscales + stage A are clean): his PRE sharpen bands crush/ring them. pre_blur and grain
  alone did nothing (`work/v3test/cmp_0/1.png`); new timeline `pre_sharp` (finish.py `grade(..., sh)`): O1/O3/O4/O5/O6
  shots 0.25 + gamma_level 0.85 (not O4's night still) + grain; ITV5/ITV10 0.5 (`work/v3test/cmp_ps_a/b.png`,
  `cmp_O4.png`). O2 untouched. v2's timeline kept as `build/timeline.v2.json` / `zoom_layers.v2.json`.
- **Running:** `finish.py render renders/stageA_v2.mov renders/caps_capcut.mov renders/finish_v3.mp4` (GPU lock held) →
  `win/zoom_gate.py` on it → `export_cta.py renders/finish_v3.mp4 renders/mix_v2.wav` (mix unchanged) → v3 as the main
  name, v2 kept as `(v2).mov`, both folders.

## (previous) ▶ STATUS: resume here (2026-11-04 ~16:20): v2 DELIVERED (his review 1 applied), at his review
- **`Harry Diana Photos.mov`** in Final Renders + `X:\Claude Projects\Exports\` (= `outputs/`, sha256 887c902c…): 41.63 s,
  1080×1920 30 fps, 33.3 Mb/s, −14.1 LUFS / −1.6 dBTP, QA PASS. v1 kept beside it as `Harry Diana Photos (v1).mov`
  (sha256 872076b0…) in all three places.
- His review 1 (BRIEF § HIS REVIEW 1, Tella 2): no wiggle (static anchor per shot, slow follow only on big head moves;
  opening-shot jitter 6.4 → 3.2 px), Cooper 0.8x over the 0.43 s Harry flash straight into the cameramen, every zoom a
  smooth eased push-in (≤ 8 %), NO end screen (picture fades out over the last 0.6 s), CTA mids at 0:21 and 0:35.
- Checks: `proof/v2_checks.jpg`, `proof/final_edges_v2.jpg` (23 cuts clean). Renders: `renders/stageA_v2.mov`,
  `renders/finish_v2.mp4`, `renders/mix_v2.wav`. Same re-render recipe as below (v1 track kept as `build/track.v1.json`).

## (previous) ▶ STATUS: resume here (2026-11-04 ~15:05): v1 DELIVERED, at his review
- **`E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Harry Diana Photos.mov`** + identical
  `X:\Claude Projects\Exports\Harry Diana Photos.mov` (= `outputs/`, sha256 872076b0e69f48cb…): 1080×1920 30 fps,
  1369 frames, 45.63 s (his cut 41.63 s + the 4.0 s Road to 1M end screen), 31.9 Mb/s, PCM 48 kHz, −14.1 LUFS /
  −1.6 dBTP, `build/export_cta.py` QA PASS. Report: [REPORT.md](REPORT.md).
- Checks: `proof/final_edges.jpg` (24 cuts clean), `proof/final_asr.txt` (his cut word for word, no narrator / reporter),
  `proof/cta_check_v0.jpg` (prompts + end screen), `proof/finish_stills_grid.jpg`, `proof/itv_v0_v1.jpg` (Proteus).
- **Subscriber count checked 2026-11-04 ~15:15 (his ask "check yourself"):** @AbundanceWisdom (UCbLhNRQjyvNTqluyjKiJ8jw) shows 540,000 publicly (yt-dlp channel_follower_count; YouTube rounds public counts to 3 figures, the exact number is only in his Studio). The end screen's 540,000 already matches: nothing re-rendered. For a later count: `presets/youtube-shorts/abundance-wisdom/cta/
  cta.py render --only end --fps 30 --subs <N>` → re-run `build/export_cta.py` only, ~2 min, no re-render of the picture).
- **A review note = data + ONE finish render** (fix only what he names):
  picture → `build/make_timeline.py` (overlay picks, framing, transitions), `stage_a.py render` only if face shots change;
  captions → `captions/captions.txt` → `make_plan.py` → `render_caps.py render` (uv `--with fonttools --with scipy --with
  opencv-python-headless`) → `capcut_pass.py`; audio → `build/dialogue.py` / `build/mix.py`; then
  `build/finish.py render renders/stageA_v1.mov renders/caps_capcut.mov renders/finish_vN.mp4 --audio renders/dialogue.wav`
  → `build/export_cta.py renders/finish_vN.mp4 renders/mix.wav "outputs/Harry Diana Photos.mov"` → both folders (keep the
  reviewed v1 as `(v1).mov`). Every GPU job under `.locks/gpu.lock`, every Premiere call under `premiere.lock`.

## (previous) ▶ STATUS: resume here (2026-11-04 ~14:10): CODE BUILD RUNNING (his go "Yes, defaults, build")
- **Done:** catalog pass + overlay picks (BRIEF § HIS GO / CATALOG PASS) · O1–O6 sourced (his drives first: 1987 ITN
  Mallorca + 60M "found out" upload in `dl/drive/`; YouTube H.264: Smithsonian `qRB5UFJLVV0`, AP `e40n9H3SVdY`) ·
  exact played crops (square) → Higgsfield Topaz 2160p ×5 + 4K image ×1 (27 credits, 1,042 → ~1,015) → lanczos 1080 in
  `dl/hf/*_up.mp4`, `dl/hf/O4_ritz_hf.png` · `build/make_timeline.py` from HIS cut (25 shots, 21 zooms, 12 transitions,
  CTA mid 16.75 / 26.00 + end) · `stage_a.py track` + `build/smooth_track.py` (11 shots smoothed, raw kept) ·
  `renders/dialogue.wav` · `renders/mix.wav` (45.63 s incl. the 4 s end screen, −14.10 LUFS / −1.60 dBTP, no music) ·
  captions: `captions/make_words.py` (+5 words heard in his A1) → `captions.txt` (75 captions, 21 coloured, Cooper
  italic) → `renders/caps_code.mov`.
- **Running:** `build/stage_a.py render renders/stageA.mov` (GPU lock; CPU-bound flow in-betweens).
- **Next:** `captions/capcut_pass.py renders/caps_code.mov renders/caps_capcut.mov` (GPU) → `build/finish.py centers` →
  `finish.py stills` (every shot: skin, overlays, labels, CTA band) → `finish.py render renders/stageA.mov
  renders/caps_capcut.mov renders/finish.mp4` → `build/export_cta.py renders/finish.mp4 renders/mix.wav
  "outputs/Harry Diana Photos.mov"` → QA (edges, final ASR, gaps, no crash / no child-at-risk frames) → copies to Final
  Renders + `X:\Claude Projects\Exports\` → REPORT.md → LESSONS.
- No Topaz pass on Stage A (dropped since Conrad: too slow on the shared GPU; Paris shipped without it).

## (previous) ▶ STATUS: resume here (2026-11-04 ~13:30): HIS TELLA 1 IN + RESOLVED → waiting on his answers + go
- **His Tella 1 is resolved into BRIEF.md § HIS DIRECTION 1.** He re-cut the sequence himself (41.63 s, `premiere/his_cut.tsv`:
  his cut is the spec, never re-place over it). Six overlay slots O1–O6, marked on his V2. His A1 is re-ASR'd clean.
- **WAITING on:** (1) children in O2/O5/O6 vs the brief's no-minors rule; (2) O3 "injured" → ambulance/hospital exterior
  instead; (3) O4 "back of her head" → a pre-crash photo instead; (4) CTA mid-2 slot + hard cut into the end screen;
  (5) his subscriber count; (6) Higgsfield credits for the upscales; (7) his go on the build quote.
- **Build quote:** about 7–10 % of the weekly cap in a FRESH session started from BRIEF.md + RUN.md (this session's
  context is long, so continuing here costs more). Same scale as Paris: 6 sourced overlays (search, HQ check, letterbox
  where soft) + the CTA, on top of the usual 4–6 % build. Higgsfield upscales ~2 credits per still, ~5 per clip
  (≈ 15–30 credits for six), his approval first.
- On go: catalog pass into BRIEF.md → source O1–O6 (his drives first, then YouTube with H.264 forced) → code build from
  HIS cut (copy the newest AW build, e.g. `projects/paris-shock-therapy/build/`): Stage A head lock, Topaz, finish.py
  grade/cards/captions/overlays, CTA (README § 12), mix −14 LUFS / ≤ −1 dBTP on the encoded file, `.mov` to Final Renders
  + `X:\Claude Projects\Exports\`, QA, REPORT.md. Every Premiere call takes premiere.lock.

## (previous) STATUS (2026-11-04)
- 2026-11-04: Affan asked for the raw build so he can record his Tella. Checked under premiere.lock: it is still in ABW10,
  byte-identical to the v2 read-back (68 clips), and all 4 bin items are online. Nothing was re-placed. He opens it from
  the bin himself; his active sequence ("Owen Hart Wife - raw cut") was left alone.
- **RAW SEQUENCE PLACED in ABW10, NOT saved** (he saves): bin **"Harry Diana Photos"** › **"Harry Diana Photos - raw
  cut"** (id `253ccf59-794c-4036-9454-4c504a1ab05c`). 1080×1920 **30.00 fps** (clone of "Onyx reaction template
  (empty)" set to 30 / display 104), **48.13 s**:
  - V1/A1: 32 clips each (26 speech pieces + 6 crop razors), source audio only.
  - V2: 4 picture-only clips (B6 covers over ITV's 1997 footage, a hold under ITV's fade under "away", and a 1-frame
    crop fix in B4). A2 empty.
  - 6 beat markers (name, label, warning). No grade, captions, upscale or music.
- His active sequence was restored after each window: "Still Here reaction" after v1, and "Paris Shock Therapy - raw
  cut" after v2 (he had switched to it in between). The 1-frame fixes ran without switching.
- **v2 = v1 re-placed** (2026-11-02 ~16:00): the A1 re-ASR of v1 still heard "you know" before "she would never" (B2). In
  moved 8.70 → 9.17 (the real gap between "know" and "she"). Placed only after the read-back showed our sequence
  unchanged since v1 (`premiere/run_replace.py`). v1 files are in `premiere/v1/`.
- **Verified:** `premiere/readback.tsv` vs the measured edges (`win/verify_eff.py`): every piece holds exactly its
  in/out, no gaps. The only deviations are two crop razors one frame late: B6's sits under a cover, B4's is patched by
  `premiere/fix_b4_frame.js`. Picture (`proof/sim_readback.jpg`): only Harry and Cooper; no wreckage, no 1997 footage, no bugs. A1 rebuilt from the
  read-back and re-ASR'd (`win/asr_a1.json`): the brief's words, first words "the last thing…", last "wiping away";
  nothing leaked at any of the 31 joins (no "you know", "Mm-hmm", "Well", "um", "I've seen", narrator or reporter).
  Hard rule 1 (`win/gap_check.py`): the longest quiet run is 0.18 s.
- **WAITING for his Tella direction video.** Nothing else runs before it: no build, grade, captions, Topaz or render.
- When it arrives:
  1. Transcribe it, and sample the frames he points at.
  2. Resolve every note into BRIEF.md.
  3. If he re-cut the sequence, dump HIS sequence read-only; his cut is the spec (never re-place over it).
  4. Do the catalog pass into BRIEF.md (CLAUDE.md learning loop 5).
  5. **Quote the build cost, CTA included** (§ Subscribe CTA below), then do the code build (copy the newest AW build, e.g.
     `projects/conrad-murray-didnt-kill-mj/build/`). Lean mode (usage tight since 2026-11-02): no new agents without asking.
- Open questions for him: BRIEF.md § "Brief vs his standing rules" and § "Decisions taken in the raw cut".

## Subscribe CTA (Affan 2026-11-03: this is the FIRST Short to ship it; part of the build, not before his Tella)
- Spec: `presets/youtube-shorts/abundance-wisdom/README.md` § 12. Kit (built, don't redesign): `presets/youtube-shorts/
  abundance-wisdom/cta/cta.py` (`rgb, a = cta.frame('mid'|'end', u, cy=1392)`, premultiplied float32). Renders:
  `E:\Shorts\Abudance Wisdom Shorts Exports\CTA\` (`aw-cta-mid-30.mov` 2.8 s ProRes 4444 alpha, `aw-cta-end-30.mov` 3.5 s, `aw-cta-mid-
  sfx.wav` / `aw-cta-end-sfx.wav`, crest on frame 0). He was reviewing the Conrad preview on 2026-11-03: **use whatever
  is in that folder at build time** (design changes come through the orchestrator and get re-rendered there).
- **v2 (after his review of v1, 2026-11-03 17:23–17:27, README § 12 rewritten):** the mid prompt is the same size, slot,
  2.8 s and `cta.frame('mid', …)` call, now with his red Deep Glow and a flare on the click. The END SCREEN is replaced by
  "Road to 1M", **4.0 s** (was 3.5): his gold play-button plaque flips in on a light streak, the count rolls to the
  subscriber number on "ROAD TO 1,000,000", the button is tapped, the count ticks +1, and sparks fly into the plaque.
  **Pad the end WAV to 4.0 s** in the mix.
- **The subscriber count is baked into the end screen: ask him for N in the cost quote** (540,000 on 2026-11-03), then
  re-render before shipping: `uv run -q --with numpy --with pillow --with opencv-python-headless python presets/youtube-
  shorts/abundance-wisdom/cta/cta.py render --only end --fps 30 --subs <N>` (or set `cta.SUBS` / `cta.FPS` in code).
- Mid prompt ×2 at ~35–45 % and ~70–80 %; never in the 0–5 s hook, over a label card or another low-band graphic, in the
  last 3 s, or on the payoff line. Centre y 1392, moved (cy) off a glow bar or a mouth. Sound: the mid WAV's peak ~15–19 dB
  under the local voice peak (Conrad: −12.6 dB on the WAV); the end WAV −15.6 dB. No music under the end screen.
- Provisional slots on the 48.13 s raw (re-place them on whatever cut his Tella leaves):
  - Mid 1 ≈ 0:16.9–0:19.7 (35–41 %): B2 "she would never do this to us… part of a plan". No label there.
  - Mid 2 ≈ 0:33.7–0:36.5 (70–76 %): this lands on B5 "All I saw was the back of my mom's head…". There's no other
    slot in 70–80 % (B6 from 0:37.20 carries the ITV · 2023 label, and the end is the payoff). It's a grim line for a
    subscribe pill: **ask him**, or slide it to ~0:30.9–0:33.7 (64–70 %, B4's tail).
  - End screen: appended after "wiping away" (4.0 s in v2). **The brief's hard rule 7 says "No end card"**; his 2026-11-03 rule adds one.
    Default: HARD CUT from "away" straight into the end screen's black (keeps the hard cut), and confirm with him.

## Job facts
- Brief (locked, his words): `X:\Claude Projects\Abundance Wisdom\HARRY-DIANA-EDITOR.md` (already on disk from 1 Nov; used as is).
  Decisions: [BRIEF.md](BRIEF.md).
- Instruction (via the orchestrator session): same flow as Paris Shock Therapy, "do the sequencing for premiere and await
  my direction video".
- Export (later): `Harry Diana Photos.mov` → `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders` + identical copy in
  `X:\Claude Projects\Exports\`. Never C:, no phone copy unless asked.
- House rules: never save or export his Premiere project; never close Premiere or AE; work in silence; no Fable agents;
  one heavy GPU job at a time (check `nvidia-smi`).
- **Premiere is shared (3 sessions in ABW10, 2026-11-02): every Premiere window takes the ONE shared lock**
  `projects/_onyx-batch2-2026-10/.locks/premiere.lock` (lab-notes 2026-11-02). Built in: `premiere/plock.py`; `pp.py`
  takes it per call, `run_window.py` / `run_replace.py` hold it for the whole window. Never overwrite a file Premiere has
  imported (a re-render gets a new name); `lanes/premiere/dialog-watch.py` closes import-failure modals, so run no closer.
  The v1 window (15:30) and the v2 re-place ran WITHOUT the lock, before the rule; v1's place.jsx collided with the Onyx R2
  builder (bridge drop) but landed in full, and v2 was placed and read back complete.

## Pipeline
| # | Step | Status |
|---|---|---|
| 1 | Intake: 60M + ITV via yt-dlp (H.264) → `raw/`; `seq_src/` H.264 CRF 12 + PCM 48 k (native 29.97 / 25 fps) | ✅ |
| 2 | Words (WhisperX) + edges by ear-proxy (`win/snip*.txt`, `win/fine.py`) + picture edges (`win/fstep25.py`, per-frame luma) | ✅ 48.13 s |
| 2b | Raw sequence in ABW10 (30 fps), read-back verified, A1 re-ASR | ✅ v2 |
| 2c | His Tella direction | ⏳ waiting |
| 3–8 | Code build → export → QA → REPORT | pending (quote first) |
| — | Music | default none (his rule); the brief asks for a piano: open question |

## The cut (actual, from the read-back; source = each upload's own clock)
| Beat | Timeline | Source in → out (pieces) | Words |
|---|---|---|---|
| 1 | 0:00.00–0:11.00 | 60M 1:20.60–1:23.13 · 1:24.67–1:25.03 · 1:25.87–1:27.40 · 1:29.23–1:31.50 · 1:31.73–1:32.47 · 1:33.07–1:34.80 · 1:35.00–1:36.83 | Cooper: "the last thing Mummy saw on this earth was a flashbulb." Harry: "Yep." Cooper: "That's what you saw in the pictures?" Harry: "The pictures showed the reflection of… a group of photographers taking photographs through the window." |
| 2 | 0:11.00–0:19.60 | 60M 0:00.23–0:01.93 · 0:03.50–0:04.73 · 0:04.97–0:07.17 · 0:09.17–0:10.73 · 0:11.53–0:13.43 | Cooper: "You didn't believe she was dead?" Harry: "For a long time. I just refused to accept that she was gone. She would never do this to us, but also… maybe this is all part of a plan." |
| 3 | 0:19.60–0:21.33 | 60M 0:41.53–0:43.27 | "I had huge amounts of hope." |
| 4 | 0:21.33–0:34.07 | 60M 1:01.50–1:03.73 · 1:03.83–1:05.77 · 1:06.27–1:07.93 · 1:08.13–1:13.67 · 1:13.97–1:15.33 | Cooper: "Why did you want to see it?" Harry: "Mainly proof. Proof that she was in the car. Proof that she was injured. And proof that the very paparazzi that chased her into the tunnel were the ones that were taking photographs of her lying half dead on the backseat of the car." |
| 5 | 0:34.07–0:37.20 | 60M 1:47.80–1:49.73 · 1:49.97–1:51.17 | "All I saw was the back of my mom's head, slumped on the back seat." |
| 6 | 0:37.20–0:48.13 | ITV 0:47.20–0:48.13 · 0:48.73–0:50.07 · 1:05.20–1:06.33 · 1:06.87–1:08.80 · 1:11.90–1:12.63 · 1:12.93–1:17.80 | "I cried once, at the burial. And there we were, shaking people's hands, smiling. And the wet hands that we were shaking, we couldn't understand why their hands were wet, but it was all the tears that they were wiping away." HARD CUT |

V2: B4 1-frame crop fix (60M frame 2032) at 0:27.07 · B6 cover 0:39.47–0:42.53 = ITV Harry CU 0:55.00 (over the boys,
1997) · B6 cover 0:42.53–0:46.40 = ITV Harry CU 1:20.73 (over the walkabout + its dissolve) · B6 hold 0:47.80–0:48.13 =
ITV frame 1937 (the wide's last clean frame, over ITV's fade to black under "away").

## How it was built (re-run recipe)
```
python premiere/make_beats.py                                   # sources.json, beats.json, framing.json (effective edges)
python ../../presets/youtube-shorts/abundance-wisdom/resolve_beats.py . --fps 30              # -> edl.json
uv run ../../presets/youtube-shorts/abundance-wisdom/plan_placement.py . --fps 30 60M_Harry_2023@6.973633 60M_Harry_2023@86.953533 60M_Harry_2023@62.529133 60M_Harry_2023@63.663600 60M_Harry_2023@67.834 ITV_Harry_2023@76.04
python ../../presets/youtube-shorts/abundance-wisdom/place_sequence.py . "Harry Diana Photos - raw cut" "Harry Diana Photos" premiere/place.jsx
python premiere/run_window.py      # first time: state → his active → create_seq.js → place.jsx → restore his
python premiere/run_replace.py     # re-place: only if unchanged since premiere/v1/readback.tsv → clear_ours.js → place.jsx → restore
python premiere/pp.py premiere/fix_b4_frame.js ; python premiere/pp.py premiere/readback.js > premiere/readback.tsv
python win/verify_eff.py ; python win/verify.py ; uv run --with pillow python win/sim.py --readback proof/sim_readback.jpg
<gpu python> -I win/asr_a1.py ; uv run --with numpy python win/gap_check.py
```
**Re-place only if he has NOT edited the sequence** (`run_replace.py` checks that itself).
On a re-place, pass the TRUE cut `60M_Harry_2023@67.801067` (not 67.834) and skip `fix_b4_frame.js`: place_sequence already
re-pins razors from the in-points Premiere actually holds, so the one-frame-later split was what put the B4 razor a frame late.

## Notes for the build
- 60M: 60 MINUTES bug top-left; ITV: ITV NEWS bug top-right. Both outside the face crops. ITV's lower-third
  "'HARRY: THE INTERVIEW', ITV1" shows at the bottom of B6 "at the burial" (0:38.13–0:39.47): crop/push-in past it.
- ITV is 720p 25 fps (the best on YouTube): B6 needs the upscale most. The B6 wide (Harry seated, 0:46.40–0:47.80) is
  the softest shot.
- B6 opens on ITV's own fade-up from black (0:37.20–0:37.63).
- 60M's B4 has a medium shot (0:23.50–0:27.07 on the timeline) between close-ups.
