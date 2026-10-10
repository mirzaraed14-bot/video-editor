# RUN — aw-code-trial-parents: rebuild an Abundance Wisdom short ENTIRELY IN CODE, matched frame by frame

## ▶ STATUS: resume here
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
