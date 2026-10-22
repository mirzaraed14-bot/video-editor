# RUN — Katherine Jackson, "the day Michael died" (AW short, built FULLY IN CODE)

## ▶ STATUS: resume here (2026-10-21)
- **His review of v2 (2026-10-21), all three fixed:** (1) his morgue still given → `raw/mj-morgue-still.webp`, cropped to the
  photo (`timeline.json` O2 `still_crop`); (2) caption mishear → "KAT YOU HAVE / TO COME DOWN / TO THE HOSPITAL" (transcript
  + captions.txt, caption layer re-rendered; old layer kept in `captions/v1/`); (3) MJ smiling overlay moved DOWN so the
  captions clear his smile (O3 scale 1.25 about src (668, 442)): stage A re-rendered for that segment only, his Topaz chain
  on it, re-gridded and spliced at the purple dips → `renders/kj_topaz_final.v3.mov`.
- **FINAL: `outputs/katherine-day-michael-died.final.mp4`** → `X:\Claude Projects\Exports\`. No phone copy (he does not want them, 2026-10-21).
- To re-finish after any further note: `"$HOME/.cache/video-editor/whisperx-venv/Scripts/python.exe" build/finish.py render
  renders/kj_topaz_final.v3.mov captions/caps_capcut.mov outputs/katherine-day-michael-died.final.mp4 --audio renders/kj_audio.wav`
- v2 (placeholder still) superseded: `outputs/katherine-day-michael-died.v2*.mp4`.
- Never: save/export his projects, shut the PC down while ABW9/ABW10 may be unsaved in AE/Premiere.

## Rules for this build
- No AE / Premiere / CapCut in the build. His projects are read-only (Seq 13 already dumped: `seqref/seq13.txt`).
- Silence: no audio/video playback. Video intermediates on X: only (C: has ~21 GB free). Export copy → `X:\Claude Projects\Exports\`.
- The trial engine (`projects/aw-code-trial-parents/render/`) is hard-wired to Nick Walker's Comp 47 (zooms, transitions,
  double, glow bars, 2-frame slip, grade layer by time): only its primitives are used, from `build/timeline.json`.

## Pipeline (stage = his tool → code)
| Stage | His tool | Code here | State |
|---|---|---|---|
| 1 Intake | — | `raw/katherine-60min.mp4` (copy of the E: source, 1920×1080 29.97 fps) | done |
| 2 Picks | eye | `build/scan_faces.py` (YuNet scan) + `build/pick_sheet.py` (ranked contact sheets, `build/scan/`) | done |
| A Sequence + head lock | Premiere + AE comp 1 | `build/stage_a.py track|sheet|render` (uv opencv env for track, GPU venv for render) → `renders/kj_stageA.v2.mov` | done (v2) |
| B Enhance | Topaz | his chain (`kj2`) + the jitter tweak (`build/topaz_tweak.py` → `kj3`), each re-gridded (`build/align_frames.py`), spliced per shot (`build/splice_topaz.py` → `renders/kj_topaz_final.mov`) | done |
| C Finish | AE comp 2 | `build/finish.py` + `build/timeline.json` + `build/zoom_layers.json` | v1 done |
| D Captions | Premiere → CapCut | agent → `captions/` (70 captions, 20 coloured, 8 italic; NOTES.md) | done |
| E Audio | Premiere | `build/audio.py` | done |

## Decisions (mine, stated for correction)
- **Hook stare:** source 1909.20–1910.97 (K1 setup, mouth still, eyes open; ~15 s before the reporter's question in the
  interview). Sheet: `build/scan/stare_small.jpg` (pick #2).
- **Joe Jackson (O1):** `E:\Bullshit Folder\Henry\EXCLUSIVE LEAK- Joe Jackson's FULL Interview.mp4` 737.0 s, frontal
  close-up, 0.8× optical-flow slow-mo (737.0–738.39), Scale 1.12 about src (922, 466) so the band (src y 0–932) leaves the
  NEWSONE watermark (src y ≥ 946) out. The CNN Piers Morgan interview was rejected (busy set, hat, lower-thirds).
- **MJ smiling (O3):** Oprah 1993 4K (`Henry/`), one shot 2137.0–2144.0, smiling/laughing throughout; 0.8× flow slow-mo
  from 2138.2 (to 2141.24), Scale 1.10 about src (704, 520). Sheet `build/scan/mj_peaks.jpg`.
- **Framing:** Scale 1.92 (his Comp 07 scale for this very source), nose locked at x 540 every frame, ONE height per camera
  setup across all its cuts (K1 y 1086.5, K2 1072.3, reporter 861.9 = the median native framing). Checked against his own
  "Paris Life.mov" (same source): his captions sit across Katherine's nose / under the reporter's lips, same as here.
- **Zoom centres:** `zoom_center.py`'s detector failed on these extreme close-ups (no face / partial boxes), so its RULE was
  applied to MEASURED geometry (scan landmarks + the locked nose): reporter face top y190 → pivot y722; Katherine's face
  centre ≥ 960 → frame centre (his pivot cap). Depth by block length (README §3), PCHIP through the front-loaded table.
- **Letterbox:** band 440–1484, mask x −60..1140, twin 198 % at 47 % (README §4 scale, his newest opacity), 19.2 px glow bars
  on both band edges (trial-fitted Deep Glow stack), bars above the grade, below the zoom.
- **Grey:** Rec.709-luma desaturation at the Hue/Sat position of his grade stack (after the POST LUT, before Sharpen 40 +
  vignette), 27.3 → 30.9 to grey, held, colour back at the 31.17 cut (the purple dip's black hides the switch).
- **Grade:** one grade layer for the whole short = trial layer 43 (his standard section look).
- **SFX:** his whoosh slice on the 11 purple/green transitions (cyan Gaussian ones stay silent — his Nick short also had
  ~11 whooshes over 17 transitions), camera flash on the morgue photo's entrance. Levels = his measured track gains.
- **Audio source:** Seq 13's A1 as is (no Adobe Podcast enhance: that is a web tool step outside this build).
- Topaz jitter tweak mapping (his words → CLI, MY interpretation): "interpolation a few points" = chr-2 `rdt` 0.01 → 0.018–0.03
  (values from his own logs), "second pass a bit higher" = stabiliser `smoothness` 6 → 8.4 (his own value). His logs never
  set `reduce` (jittery-motion passes) ≠ 0, so that knob is left alone. Applied ONLY if the first pass measures jittery.

## Engineering found on the way (all fixed in code)
- **Seq 13 times are 4-decimal rounded** (1.7667 = frame 106.002): matching shots with `t >= t0` put every "…67" cut ONE
  FRAME LATE against the audio. Both renderers now snap every time to the 60 fps grid; v2 cuts verified frame-exact.
- **Head lock: the face detector's nose point wobbles 1–9 src px frame to frame.** Fused track = optical flow (LK, forward-
  backward checked) on the UPPER face (eyes/brows/nose bridge, not the talking mouth) for the fast motion + the detector
  low-passed (σ 6 frames) for position; guard falls back to the detector where flow loses the face. Measured lock error
  (nose-patch shift, src px): better on 22/25 shots, often 2–3× (e.g. 4c 2.24 → 0.80, shot 5 9.43 → 4.18); per shot the
  steadier of the two is kept (`track.json` `used`).
- **Topaz changes the frame count** (kj: 2872 → 2875; kj2: 2874): chr-2 adds/swallows frames near cuts and in the black
  O2 slot, prob-4 adds one at the end. The trial's cut-guess fixer picked wrong frames here, so `align_frames.py` aligns
  output to input by CONTENT (banded DP, drop/hold penalty 25) and streams a 2872-frame file; cuts verified (3 of 17 show
  one Topaz-blended frame at the cut: all under cyan blurs; his own pipeline blurs 2–4 frames per cut, LESSONS 2026-09-24).
- **Topaz full-frame stabilisation partly fights the head lock** (after a lock the BACKGROUND moves; the stabiliser smooths
  it and nudges the face back): measured nose motion after Topaz improved on some shots (5: 2.88 → 0.85) and worsened on
  others (4a 5.59 → 8.03, 11 8.21 → 11.81). That is his "jittery post head tracking" note. K2 values are mostly real head
  turns (a 2D lock cannot remove rotation).
- **Per-shot Topaz (his note: "on jittery shots" only):** measured nose-patch motion default → tweak, mean 3.54 → 3.21;
  the tweak on run 4 (4a–4d), run 6 (6a–6c), 9, 13, 15 (e.g. 4a 8.03 → 5.63, 6a 3.52 → 2.36), the default elsewhere (the tweak
  was worse on steady shots, e.g. 7 0.51 → 1.95). One version per same-setup run; every switch sits on a transition.
