# RUN — aw-code-trial-parents: rebuild an Abundance Wisdom short ENTIRELY IN CODE, matched frame by frame

## ▶ STATUS: resume here
**2026-10-11 — his review of the from-raw short: "captions have way too much wiggle, that's the only issue, otherwise it
looks good."** Cause: the Turbulent Displace model was 25 px white noise (each letter wobbled on its own). MEASURED
his real field on his AE export (`render/measure_turb.py`, 10.6k caption patches vs our render with turbulence off):
rms 1.95 px x / 1.58 px y; spatial correlation 0.95 @ 30 px, 0.70 @ 120, 0.29 @ 240, 0 @ 320+ (Size 100 = ~100 px
Gaussian); temporal 0.94 @ 0.1 s, 0.60 @ 0.4 s, 0 @ 1 s. New `aw_render.turbulence`: white noise on a 50 px x 0.1 s
lattice, Gaussian-smoothed (100 px, 0.29 s), normalised to those rms values (checked: 0.98 / 0.69 / 0.16 spatial,
0.94 / 0.57 / 0.34 / 0.07 temporal). Re-render v2 → `outputs/nick-parents.fromraw.v2.*`.
Also found in the review crops: orange words came out YELLOW (BODYBUILDING G 207 vs his 176). Two causes, both fixed:
(1) CapCut's export shifts colour (red down, slight desaturation): `fit/capcut_colour.json` (3x3 through zero, caption
ink rms 7.48 → 4.69) applied in `capcut_blur.roundtrip` → `captions/caps_capcut.v3.mov`; (2) the caption Deep Glow was
added ON TOP of the letters (R clips at 1, G/B keep rising): refit `render/calib_glow2.py` against AE's lossless caption
renders — 'mix' composite (glow held 89 % off the letter's own alpha), colour-word interior 16.7 → 14.0, halo 4.3 → 4.0
(`fit/glow2.json`, used for captions by `aw_render2`; the bars keep fit/glow.json). Orange at 1230: G 164 vs his 179.
Re-render v4 DONE and sent: `outputs/nick-parents.fromraw.v4.final.mp4` = **28.50 dB vs his final** (best so far; AE
stage 29.31 dB vs AE lossless), review files `…v4.side-by-side.phone.mp4`, `…v4.captions-closeup.phone.mp4`,
`v4_caption_check.png` (his vs ours: wiggle gone, orange/red/white match). Waiting on his look at v4.

**2026-10-11 00:10 — THE SHORT IS MADE FROM RAW, NO PREMIERE / AE / CAPCUT, NOTHING DONE BY HIM.**
`outputs/nick-parents.fromraw.final.mp4` (2630 frames + code audio) vs his `Nig Final YT.mov`: **28.93 dB** (rms 9.43,
every 10th frame, half res). Chain: `stageA/seq_render.py render` (raw sources → Seq 28 picture, 43.56 dB vs his
Nig.mov) → `stageB/topaz_his.py` (his exact Topaz commands, headless; bit-exact on his own input) →
`stageB/fix_frame_count.py` (chr-2 repeated a frame at the frame-960 cut on our input: dropped, count = his) →
`render/render_full.py --source … --caption captions/caps_capcut.mov` (AE look + code captions through the CapCut
model) → `render/premiere_pass.py … audio_code.wav`. Review files: `outputs/nick-parents.fromraw.side-by-side(.phone).mp4`,
`outputs/nick-parents.fromraw.captions-closeup(.phone).mp4`, `outputs/fromraw-side-by-side-stills.jpg`.
Where the residual comes from: our Topaz output vs his = 36.6 dB (stabiliser lands 1–4 px apart, Iris detail differs:
Topaz's AI on a not-bit-identical input; 8–16 s weakest), comp 43 L3 (~7 rms, 1 s), comp 45 (flow slow-mo, ~5 rms).
Same AE stage on HIS Topaz file + code captions = 29.94 dB, so the code look/captions are not the limit.
Next ideas (if he wants closer): encode stage A closer to Premiere's H.264 (Topaz reacts to input noise); refine comp 43 L3.

**2026-10-10 evening — GOAL (his words): a one-of-one copy with NO Premiere / AE / CapCut and nothing done by him.**
- **Stage D DONE:** code captions → CapCut model (`captions/caps_capcut.mov`) are closer to his CapCut return than his own
  Premiere caption render is (band rms 3.98 vs 4.50; at caption changes 8.34 vs 10.95). Full AE-stage render with them
  (`outputs/nick-parents.code-ae-stage.codecaps.mp4`): 8.25 rms vs his final (8.12 with his CapCut file).
- **Stage A (sequence render from RAW, `stageA/seq_render.py`) in calibration.** Read from ABW8 (read-only): the short's
  picture = Seq 28 48.467–92.300 (= Nig.mov). Premiere clips (Motion keys in SOURCE time) already 40–47 dB vs Nig.mov.
  AE head-lock comps 40–44 rebuilt WITHOUT AE (layers from `ae_comps4044.txt`, our lock keys, Motion Tile): he moved
  Position on 16/17 layers after the lock (22:46) and before exporting Nig (23:20), measured from Nig by `fit_layers.py`
  (`layer_fit.json`, scales unchanged, 0.8–1.9 rms half-res). Comp 45 (not readable without AE) found by search:
  "Nick Walker - Official IFBB Pro.mp4" ~50.5 s, ~187 %, slowed ~0.55 with blending (`fit_comp45.py` running). V2 is off
  in his export. Decoder fix: `-fps_mode passthrough` (CFR output duplicated the first frame after a seek → off-by-one).
  AE start times are 4-decimal: frame rounding bias being calibrated (`calib_bias.py`).
- **Stage A DONE (first full pass): `outputs/nig.code-seq.mov` = 43.56 dB / rms 1.89 vs his Nig.mov** (every 10th frame),
  from the raw sources only. Keys to it: Premiere Position is a SPATIAL bezier (key value + per-key spatial tangents)
  travelled in arc length by the temporal speed/influence curve: one auto-bezier tangent overshoots the key (the
  last clip's slide was 19 px off with straight paths). Comp 45 = IFBB Pro clip at speed 0.5571 from 50.678 s, 187.07 %,
  pos (616.1, 964.3), slowed with optical-flow interpolation (`flow_interp`). Frame rounding bias 0.01 frame.
  Weakest: comp 45 and the end of comp 43 L3 (~8 rms) → `fit_layer_time.py` (whole-frame slips per layer) running.
- **Stage B PROVEN BIT-EXACT:** `stageB/topaz_his.py` replays his exact Topaz commands (from his own export log): cpe →
  stb + chr-2 + iris-3 → prob-4, headless (167 + 1488 + 670 s). On his Nig.mov it reproduces Nig_stab_chr2_iris3_prob4.mov
  with IDENTICAL decoded frames (video-stream MD5 equal over 2631 frames; files differ by 24 bytes of metadata).
  Now running on our stage-A render → `stageB/code/nig_code_stab_chr2_iris3_prob4.mov`.
  comp 43 L3 (seq 84.0–85.03) keeps ~7 rms vs Nig at every time offset / blend / blur tried: accepted (likely a hand
  tweak of that layer's anchors); all other layers 1–2 rms, timing offsets all 0 (`fit_layer_time.py`).
- Next: finish A → B → C (code captions) → Premiere pass + audio in code → side-by-side vs Nig Final YT.

**2026-10-10 — STAGE D (captions from text) — the Premiere caption layer is SOLVED; CapCut's blur is being fitted.**
`render/cap_render.py` draws his 66 caption graphics from ABW8 (Seq 28) and matches his Premiere caption render
`peace.mov` at **1.25/255 RMS full frame** (was 7.68). What made it exact (all READ from his project, not guessed):
- **Font size 48.0** (a float in the Source Text blob), **tracking 0**, and the font's **GPOS kerning** (`render/kerning.py`;
  this PIL has no raqm, so `getlength()` silently ignores GPOS: 1030 pairs, e.g. AY −122/1000 em). With kerning + true
  outline ink bounds the scale-100 widths fit to 0.23 px RMS over 57 captions. (PIL `getbbox` on one glyph = its ADVANCE
  box, not its ink: that produced a fake −6 px intercept.)
- **The pop is per caption** (`render/cap_pop.py`, `captions/caption_params.json` via `render/caption_params.py`): every
  graphic's Graphic Group carries Scale 100 → 105 at 13.6 % of ITS duration (linear) → 112 at its END (eased: out speed
  = average/infl 1/6, in speed 0/infl 1/3), + a matching Position drift. Stretched to each clip, so no single time curve
  can fit (why build.py's measured POP table was always ~2 % off). Widths follow it to 0.36 px.
- **Each line's own Motion position** (V6 y 0.10573; the V5 lines 0.13854 / 0.13958 / 0.14063 → +63 / +65 / +67 px),
  scale fixed point 5.5 px below the cap top, line-1 cap top 1031.75 (`captions/cap_cal.json`, image-matched).
- **Edge softness**: his text is softer and ~0.3 px heavier per side (+6.6 % ink): blur σ 0.425 then coverage^0.525.
**CapCut (peace.mov → peace2_clean.mp4)** = its optical-flow Motion Blur (blur 0.81, blend 1, multiple 6, bilateral):
- the CapCut return is **6 frames late** vs peace.mov everywhere; the AE layer sits at 0, so his final carries it.
- invisible on the smooth pops; at EVERY caption change the flow reads the cut as one big move between the two layouts:
  the old caption smears toward the new layout over c−4..c−1, the new one back toward the old over c..c+3, with the
  same strength profile at every cut (~6 %, 12 %, 37 %, 100 % | 75–100 %, 37 %, 12 %, 6 % of the displacement);
  horizontal when widths differ, diagonal/vertical when the line count changes. Frames 0–5 hold the first frame.
- `render/capcut_blur.py`: torch Horn–Schunck flow between the frames either side of each change + a one-sided smear;
  `fit` tunes flow smoothness and f(d) against peace2_clean (running), `render` produces the CapCut-equivalent layer.
Next: fit → render the code caption layer through it → feed it to renderer v2 instead of peace2_clean → score vs
Parents Final → side-by-side to the creator.

**2026-10-10 01:20 — FIRST FULL CODE RENDER DONE.** `outputs/nick-parents.code-final.mp4` (stage C in code + his
Premiere pass + code-rebuilt audio) and `outputs/nick-parents.side-by-side.mp4` (code | his final) sent to him.
Scores: vs AE lossless samples 30.5 dB (rms 8.05/255, 197 frames, Universe frames excluded: aerender drew them black);
vs his AE export `Parents Final.mp4` every 10th frame 30.1 dB (rms 8.1). Renders at ~5 fps on his RTX 3060 Ti
(43.8 s short ≈ 9 min). Inputs still HIS in this trial: the Topaz render (stage B), the CapCut caption layer (D), the
sequence render (A). Next, in order: D captions from text (runs readable from ABW8.prproj, `render/read_caption_graphics.py`;
styles by sampling peace.mov) → A sequence render from the raw sources → B Topaz CLI → one end-to-end run from raw.
Optional precision: one AE pass for Turbulent Displace's true field (caption wobble).

**2026-10-09 evening: NO video rendered yet — still calibrating stage C (the look).** Done:
- Zoom (S_BlurMoCurves) model = PROVEN: predicted scale/position vs his final within ~0.3 % / a few px on 12 frames.
- Grade: learned from his Topaz→final pair (`render/fit_grade.py` LUT + vignette, then `render/fit_chain.py` full chain:
  DoG sharpen bands → LUT → Sharpen → vignette). Static shots match closely (frame 2100); held-out rms still ~17/255
  because frames with FAST MOTION differ between his Topaz file and his final (hand at 25.0 s sits elsewhere/blurrier).
  Open question being tested (`render/diag_time.py`, interrupted): is his final frame-blended or time-shifted vs the
  Topaz file? Resolve this BEFORE trusting the fit numbers.
- AE is the creator's (he had ABW9.aep open on Comp 54): no measurement renders through AE until it is free.
Next: settle the timing question → refit → `render/finish.py` (zoom + transitions + glow bars + double + captions) →
first full render → side-by-side vs `Nig Final YT.mov`.

**2026-10-10 ~01:30 — STAGE C (the AE look) CALIBRATED; first full code render running** (`render/render_full.py` →
`outputs/nick-parents.code-ae-stage.mp4`, renderer v2 `render/aw_render2.py`):
- Looks: final model C trained on round-5 data (160 real frames incl. his Martin + Nick Topaz footage, + full-stack
  renders): held-out Looks 2.9/255, FULL GRADE 5.9/255 (was 10.4) — `fit/looks_43_C.pt`, `render/fit_looks3.py`.
- AE lossless samples by situation (before the Universe fix): plain 7.5, BCC flashes 7.8, gaussian 9.4, flash 8.3,
  double 8.3 /255 (~30 dB). Shared Deep Glow for bars + captions: 5.4 (`fit/glow.json`); BCC curves exact; white flash
  0.5; zoom motion blur = 1-frame shutter, 2.1 (`fit/cal.json`); AE Gaussian Blur sigma = 0.2977 × Blurriness.
- **Universe Exposure Blur:** aerender drew it BLACK (both the trans and the full variant; plugin fails headless) →
  calibrated on the one clean AE frame + his GUI export: 'Mix' = transition PROGRESS (50 = peak, 0 = clean); peak =
  linear-light blur sigma 20 × 3 exposure, clip (3.2/255); ramp sigma·k^0.65, stops·k^0.5 (5.4/255) — `fit/expo_fit.json`.
- His YT final = his AE export `Final Renders/Parents Final.mp4` placed on Seq 28 V3, cut at 24.01667 / 29.03333 with
  the middle piece 2 frames earlier, + opacity fade 43.20→43.75 (`render/premiere_pass.py`). Parents Final = the
  full-length scoring target for stage C.

**2026-10-10 00:10 — THE GRADE IS DECOMPOSED (instrument rounds 1-4, `instrument/out*/`, analysis scripts in `render/`):**
his grade layer = PRE (Unsharp 40/r25 → S_Sharpen → BCC Unsharp 20/r30; layer 40 = S_Sharpen only) → LOOKS → POST
(Curves + Lumetri + Hue/Sat) → AE Sharpen 40 → S_Vignette. Measured facts:
- POST is exactly pointwise (Hald vs permuted Hald: 0.000) → exact per-layer LUT from `out3/hald_post_<L>`. POST is what
  differs between the 4 grade layers (L43 vs L40/41/42: ~12/255).
- LOOKS is IDENTICAL on all 4 layers (0.000) and NOT pointwise: a colour-dependent vertical gradient (flat grey: top up
  to ~30 % brighter than bottom) + a strong diffusion glow (5 px dot → ~40 px glow; white square bleeds ~150 px). Learned
  as y-anchored LUTs + multi-scale glow: model B val 4.8/255 in Looks space; model C (`fit_looks2.py`, loss measured
  after POST, glow on input and output) training.
- AE Sharpen = 4-neighbour Laplacian × amount/64 (LS 0.626 for 40; only 0.1 % border pixels off). Caption Sharpen 80 → 1.25.
- Unsharp / BCC Unsharp as DoG bands: 0.58 / 0.86 /255 held-out. S_Sharpen: small (1.5).
- S_Vignette = exact multiplicative mask (`out/flat_white_vignette`).
- Footage decode = AE's within 0.6-0.9/255; the double composite matches AE (0.87).
**Captions (stage D, next):** his FINAL caption text lives in ABW8.prproj as upgraded text graphics (component
`AE.ADBE Text`, `InstanceName` = the caption, e.g. "“A QUITTER”" with curly quotes; style via `ParentStyle`, per-word
colours in the base64 `PremiereFilterPrivateData`) → read them (or the Text component's Source Text JSON over the
bridge), render with `presets/youtube-shorts/abundance-wisdom/build.py`, emulate CapCut's motion blur, and prove it
against `Caption Exports/peace.mov` (Premiere render) → `peace2.mp4` (CapCut return) pixel by pixel.
**Process lesson:** TaskStop on a backgrounded bash loop does NOT kill the python it launched (an orphan
`fit_looks.py 42` kept the GPU busy for 15 min): kill the python PID too.

**Audio:** Seq 28 audio = A1 dialogue stem (`nick3-esv2-37p-bg-10p-music-10p.mp3`, Adobe Podcast) +4.3 dB · A2 ElevenLabs
VO + Studio Reverb ≈0 dB · A3 music at 95 % (Premiere reports a speed-changed clip's in point in scaled time: media =
in × speed) −17.6 dB with his fade/dip keys · A4 SFX −15 dB (`render/audio_mix.py`, `audio_tf.py`). Where the current
timeline equals the exported one the rebuild reaches 20-26 dB SNR; elsewhere (7-10, 24-27, 35-40 s) he edited Seq 28
AFTER exporting, so his export can't score those parts.

**2026-10-09 ~23:15 — AE instrument pass WORKS (v2):** with his consent; AE had his clean ABW7.aep open →
`instrument/instrument.jsx` opens OUR copy, builds 23 measurement comps (7 Comp-47 variants via time-remapped
samplers + Hald/flat/BCC test comps), saves them as `instrument/ABW9_instrument_meas.aep`, reopens his ABW7.aep
(log: `instrument_log.txt`); then `aerender -project …_meas.aep -sound OFF -mfr OFF 100` renders them headless in the background (**`-mfr OFF` is required: with multi-frame rendering on, aerender hung after 2 frames with the GPU full — Deep Glow / Sapphire are not MFR-safe here; off = ~1.3 frames/s**) →
`instrument/out/<variant>/*.tif` (his AE stays free). Lessons: never remove ALL time-remap keys (AE disables remap and
hides the property); the first freeze came from closing the untitled project / dialogs, so the script now logs every
step and refuses a dirty project. Grade v3 (`fit_chain3.py`) adds a highlight BLOOM (his Looks diffusion): held-out
8.30 → 7.2/255. Double section still poor from the export alone (~29): refit on the lossless `grade` variant.

**2026-10-09 late — progress:** frame mapping settled (his final = Topaz frame n, except 24.367–29.017 where it is
n−2, a Premiere-side slip; and a fade-out after 43.3 s that is not in Comp 47). Grade chain v2 (`fit_chain2.py`: DoG
sharpen bands → LUT → Sharpen → smooth spatial gain/offset field, because his Looks preset carries a vertical gradient:
top 10–15 levels brighter at equal luminance) = held-out 8.35/255. Renderer `render/aw_render.py` (all Comp 47 layers as
GPU code) first test: 25–28 dB PSNR vs his final on 6 frames, visually close; the double section (19 s) colour is off.
**AE instrument pass FAILED:** `instrument/instrument.jsx` opened the COPY `ABW9_instrument.aep` via `app.open` from an
`-r` script and AE froze on a modal dialog (not responding, idle CPU) despite `beginSuppressDialogs`; the creator had to
restart AE. Do NOT re-run it without asking him for an AE window first; calibrate against his final export instead.

2026-10-09, started. The creator's ask (voice, 2026-10-09): "analyze my entire Abundance Wisdom channel and make the short
entirely yourself, don't use Premiere … copy exactly the format, the effects, the caption effects, the coloring … as a
trial run replicate one of my shorts frame by frame … so instead of one short per day we can make three … I handle the
sequencing and the psychology, the editing part is completely given to you."

**Trial short: Nick Walker parents** (ABW8 Seq 28 → ABW9.aep Comp 46/47), chosen because every input and every one of
the creator's intermediate renders exists on disk, so each stage can be PROVEN against his real output:

| Stage | His tool | His output (the reference) | Code replacement |
|---|---|---|---|
| A. Sequence render | Premiere Seq 28 + AE head-lock comps 40–44 | `Final Renders/Nig.mov` | ffmpeg/torch from the raw sources + headlock tracks |
| B. Enhance | Topaz (stab, chr2, iris3, prob4) | `Final Renders/Nig_stab_chr2_iris3_prob4.mov` | Topaz's own CLI (`workflows/topaz-iris.py`) |
| C. Finish (THE LOOK) | AE Comp 47 | `Final Renders/Nig Final YT.mov` (picture) | `render/finish.py` (torch, GPU) |
| D. Captions | Premiere captions → CapCut motion blur | `Caption Exports/peace.mov` → `peace2.mp4` | `build.py` + code motion blur |
| E. Audio | Premiere mix | `Nig Final YT.mov` (audio) | ffmpeg |

Order: C first (the look is the whole question), then D, A, B, E, then one end-to-end render from raw.

## Inventory (`inventory/`)
- `comp47_deep.json`: EVERY layer, property, keyframe (+ eases), mask of Comp 47 and its nested comps, dumped read-only
  from `Final Renders/ABW9.aep` (opened into AE's empty untitled project, closed without saving). `params.txt` = readable.
- Comp 47, bottom → top: Topaz footage (0–17.8, 20.733–43.85) + the 17.8–20.733 double (100 % masked y420–1496 over
  its 200 % twin at 23 %); 4 grade adjustment layers (Unsharp 40/25 → S_Sharpen → BCC Unsharp 20/30 → LookSuite →
  Curves → Lumetri → Hue/Sat → Sharpen 40 → S_Vignette); 2 glow-bar precomps (1 %-tall white solids at y414 / y1497,
  Deep Glow + Bevel Alpha + 2× Drop Shadow 5 px); 19 S_BlurMoCurves zooms; 17 transitions; the caption precomp
  (peace2_clean.mp4 at 50 %, Deep Glow r250 exp0.55 unmult + Bevel Alpha 2.4 + 2× Drop Shadow 12 px; in Comp 47
  Sharpen 80 + Turbulent Displace 4/100, position y908).
- Unreadable by script (plugin "custom data"): the LookSuite look, Curves, Lumetri creative/curves/wheels → captured as a
  3D LUT by rendering a Hald CLUT through them (AE used once as a MEASURING INSTRUMENT, never as the editor).

## Rule for this trial
Every stage is judged by numbers against his own render (per-frame PSNR/SSIM + a side-by-side), never by eye alone.
His projects are never saved; measurement projects are COPIES in this folder.
