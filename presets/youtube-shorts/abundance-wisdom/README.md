# Abundance Wisdom — THE LOOK (measured)

Canonical look file for @AbundanceWisdom shorts. Procedure: [PLAYBOOK.md](PLAYBOOK.md).
What jobs taught: [LESSONS.md](LESSONS.md). Earlier export-only analysis: [style-spec.md](style-spec.md)
(superseded where the two disagree).

**Source of these numbers:** full teardown (2026-09-20) of the hand-made "Wacko Jacko" short —
Premiere `ABW6.prproj` / `Sequence 11`, dynamically linked to AE `ABW7.aep` / comp
`ABW6 Linked Comp 03`, plus its renders. Read out of the live projects, not guessed.

---

## 1. Delivery spec

| | |
|---|---|
| Comp / sequence | 1080×1920, **60 fps** |
| Final render | H.264 in .mov, PCM audio, ~25 Mbit/s (`Wacko Final YT.mov`) |
| Loudness of that final | **−15.3 LUFS**, LRA 5.1, true peak −1.4 dBFS |
| Length | 39.27 s (10–55 s across the channel) |

## 2. Layer stack in the AE comp (bottom → top)

| Band | What | Notes |
|---|---|---|
| bottom | **Footage copy at 198 %, opacity 43 %** | the "make it complete" fill (§4) |
| | **Footage at 100 %**, masked | Topaz-enhanced export (§4) |
| | **Glow bars** — 2 × `White Solid 3 Comp 1` | on the mask's top and bottom edge (§5) |
| | **Grade adjustment layer** (`Adjustment Layer 25`) | one per section (§6) |
| | **Zoom adjustment layer** (`Adjustment Layer 26`) | one per shot, S_BlurMoCurves (§3) |
| | **Flash adjustment layer** (`Adjustment Layer 27`) | one per transition (§7) |
| top | **Caption precomp** (CapCut motion-blurred export) | Sharpen + Turbulent Displace (§8) |

74 layers for a 39 s short is normal: 12 shots × (2 footage + 2 bars + 1 zoom) + grades + flashes.

## 3. The zoom — one per shot, Sapphire, never layer scale

**Measured across every instance in the project: 121 zooms in 9 shorts** (ABW 4 comps 72/77/84/91/97/99,
ABW 7 comp 07, ABW6 comps 02/03), 2026-09-21. Where this section disagrees with an earlier note,
this is the one built on all 121.

**The rig.** An **adjustment layer spanning exactly one shot** (keyframes sit on the layer's in and
out points, median offset 0.000 s), carrying **`S_BlurMoCurves`**. **Only two parameters are ever
touched — `Center XY` and `Z Dist`. Everything else stays default, in all 121.** 121 of 121 are
adjustment layers.

**`Z Dist` — the move.**

| | |
|---|---|
| Push in | starts at **exactly 1.00** (69 of 69), ends median **0.77** (range 0.579 – 0.900) |
| Pull out | ends at **1.00** (47 of 52; the other 5 end at 0.80), starts median **0.782** (range 0.64 – 1.00) |
| Depth | median **0.226**, max 0.42 |
| **Depth by block length** (creator's rule, refined by their review of comp 06) | **tiny ≤ ~1.4 s → 0.85–0.87** · **standard 1.5–2.5 s → 0.78** · **3–5 s → 0.70–0.80** (they tuned one 3 s shot up to 0.80; length alone does not settle this band) · **5 s+ → 0.67** |
| Measured depths across 121 zooms | median 0.226, max 0.42 — consistent with the rule above |
| Keys | 2 keys (107 of 121); **14 are three-key out-and-back**, e.g. `1.00 → 0.76 → 1.00` |
| Static holds | **13 of 121 don't move at all** — Z Dist parked flat at 1.00 (9) or 0.80 (4), a held size rather than a move |

**`Center XY` — the face-safety rule (creator, 2026-09-21).** x is **always 540**; y is centre (960)
in 67 of 121 and **off-centre in 54** (median y 699, range 83–851). The reason: the face often sits
high in frame, so zooming about the centre pushes it *further* up until it crops. When that would
happen the origin is moved **onto the face**, so the face holds its place (and appears to come down)
as the shot pushes in. Only on the shots that need it. Never animated — one static key, always.

Claude computes it with `zoom_center.py`: detect the face on the un-zoomed frame, project where the
top of the face lands at the deepest zoom (`p' = p·k + o·(1−k)`, `k = 1/Z`), and if it would rise
above **y200**, pivot on the face centre instead of the frame centre. That threshold fires on 47 % of
shots, matching the creator's own 45 %.

**The curve — this is the signature.** All keys are **Bezier**, but not "easy ease": measured by
sampling the real value through 108 moves, **35 % of the distance is covered in the first 10 % of the
time**, then it drifts, then it closes fast (**18 % in the last 10 %**). 104 of 108 moves front-load
more than a quarter of the distance into that first tenth.

| time through the move | 0 % | 10 % | 20 % | 30 % | 40 % | 50 % | 60 % | 70 % | 80 % | 90 % | 100 % |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **distance covered** | 0.00 | **0.35** | 0.46 | 0.53 | 0.58 | 0.62 | 0.66 | 0.70 | 0.75 | 0.82 | 1.00 |
| *(linear would be)* | 0.00 | 0.10 | 0.20 | 0.30 | 0.40 | 0.50 | 0.60 | 0.70 | 0.80 | 0.90 | 1.00 |

**What is NOT a rule** (both were over-claimed from one short):
- **Direction does not reliably alternate** — 45 % of consecutive pairs flip, i.e. chance.
- **Size is not continuous across cuts** — only 29 % of shots start where the previous ended.
- What does hold: the **first move of a short is a push-in** (6 of 9 shorts; 2 open on a static hold).

## 4. Letterboxed footage: mask + 198 % fill (the "looks complete" trick)

For a shot whose source carries black bars (a 16:9 clip inside the 9:16 frame):

1. **Top copy** — footage at 100 %, position [540,960], with a **4-point rectangular mask**
   (Add mode, feather 0, expansion 0):
   - x always **−60 → 1188** (60 px bleed each side)
   - y = the picture band, e.g. **440 → 1484** (h 1044) or **504 → 1412** (h 908)
2. **Bottom copy** — the *same* footage with the *same* mask, **Scale 198 %**
   (217 % / 221 % on wider shots), **Opacity 43 %**. Masks live in layer space, so the mask scales
   with it and this copy fills the whole frame behind: an enlarged, dimmed picture instead of black bars.
3. **Two glow bars** sit exactly on the mask's top and bottom edge (§5).

## 5. The glow bars

- Source: precomp **`White Solid 3 Comp 1`** — a white solid at **Scale [100, 1]** (a 1 %-tall line),
  sitting at y 368 inside its own 1080×1920 comp.
- Each bar layer in the main comp carries: **Deep Glow** (Exposure **0.55**, **Unmult on**; the rest
  default — Radius 250, Threshold 50, Threshold Smooth 50, Spread 33, Glow Iterations 6, Downsample 75),
  **Bevel Alpha** (Edge Thickness **2.4**, Light Angle −60, Light Intensity 0.4), and **two stacked
  Drop Shadows** (Opacity **255**, Direction 135, **Distance 5**, Softness 0).
  *(The caption precomp uses the same two shadows but at **Distance 12**.)*
- Placement: bar layer y = mask edge + 592 (the line sits 592 px below the layer's centre).
  Reference pairs: mask 504/1412 → bars at y **1088** and **1997**; mask 440/1484 → bars at **1032** and **2074**.

## 6. The grade stack (`Adjustment Layer 25`), one per section

In this order, spanning a section of the timeline rather than the whole thing (6 instances here):

| # | Effect | Values |
|---|---|---|
| 1 | Unsharp Mask | Amount 40, Radius 25 *(disabled on some sections)* |
| 2 | S_Sharpen (Sapphire) | Sharpen Amp 0.5, Small Detail Size 1.5 |
| 3 | BCC Unsharp Mask | Radius 30, **Amount 17 or 7** (7 on softer sources) |
| 4 | **Looks** (Magic Bullet) | preset data **unreadable by script** → copy it, never rebuild |
| 5 | Curves | curve data unreadable by script |
| 6 | Lumetri Color | **Whites +15**, everything else default |
| 7 | Hue/Saturation | master 0 (per-channel data unreadable) |
| 8 | Sharpen | Amount 40 |
| 9 | S_Vignette (Sapphire) | Rel Height **1.573**, Rel Width **1.362** |

✅ **This whole stack IS `Affan CC Preset.ffx`** — verified 2026-09-20: the preset file contains all
nine (Lumetri, Curves, MB LookSuite, S_Vignette, S_Sharpen, Unsharp Mask, BCC Unsharp, Hue/Saturation,
Sharpen). The creator's method is simply: new adjustment layer → drag the preset on.

So Claude does the same in one scripted call — `layer.applyPreset(File("…/Affan CC Preset.ffx"))` —
and the look is identical, including the Looks and Curves data that scripting cannot read by value.
Preset path: `C:\Users\affan\OneDrive\Documents\Adobe\After Effects 2025\User Presets\Affan CC Preset.ffx`.
Never re-enter the numbers by hand.

## 7. Transitions

**The creator labels the BLOCK; the label names the transition that follows it** (agreed 2026-09-21).
One label per block, so each cut is owned by the block before it. A label on the last block is ignored.
Aqua (3) = no transition. Yellow (2) means pull-out for the ZOOM pass; in practice (ABW8, 2026-09-24)
the creator runs the zoom pass first, then relabels blocks — yellow ones included — for transitions.
Build order is therefore always zoom → transitions.

| AE label | Transition | Build |
|---|---|---|
| **10 Purple** | brightness dip to **−90** and back | their preset `Simple Brightness Fade In & Out.ffx`, keys retimed to `cut −0.333 → 0`, **`cut → −90`**, `cut +0.267 → 0` (influence 16.667) |
| **16 Dark Green** | brightness flash to **+30** and back | same preset and timing, peak **+30** |
| **4 Pink** | white solid flash | solid in at the cut, **Opacity 100 → 0 over 0.5 s**, layer 0.817 s (measured across 6 of their flashes: fall 0.38–0.6 s, fast departure) |
| **6 Peach** | **uni.Exposure Blur** | their preset `Music Media Co Uni Expose.ffx`, keys rewritten: **Mix 50 at the cut → 0 after 0.5 s** (their own use: 50 → 0 over 0.48–0.7 s) |
| **14 Cyan** | **Gaussian Blur** | built directly (their `Gaussian Blur Preset.ffx` ramps up *then* down, a different move): **Blurriness 50 at the cut → 0 after 0.7 s**, Repeat Edge Pixels on |

Layer spans: the dips run 0.667 s centred on the cut (comp 03; comp 02 used 0.8 s). The blur and
exposure transitions start **on** the cut and run 0.9 s, with the value decaying inside that.
All transition layers are named `Adjustment Layer 30` (28 = grade, 29 = zoom) and sit directly under
the caption, above the zoom layers.

**Measured across the project before building:** 95 brightness transitions (values −89/−90 and +30),
6 white-solid flashes, and a handful of Gaussian Blur (62–122 → 0) and uni.Exposure (Mix 50 → 0) moves.

## 8. Captions

Built in Premiere as **one Graphic per caption**, exported on black, motion-blurred in CapCut, then
placed back in AE. Measured on the reference short (46 captions over 39.3 s):

| | |
|---|---|
| Font | **Gretaros**, ALL CAPS |
| Cap height | **≈ 40 px** on the 1080-wide frame |
| Line 1 centre | y ≈ **1149** in the caption export; the precomp is then placed at y **898** in AE (62 px up) |
| Second line | a **separate graphic on the track above** (Premiere V3), sitting **+59 px** below line 1 |
| Chunking | **1–3 words**, median **0.75 s**, range 0.23–2.05 s, **wall-to-wall**, no gaps |
| Animation | the **"Revised Light pop"** preset (in `Effect Presets and Custom Items.prfpset`): Vector Motion Scale **100 → 105 → 112 %**. **Measured on screen** (frame by frame, 2026-09-21) it arrives slower than the nominal keys: +1.6 % by 0.05 s, +5.3 % by 0.20 s, +7.0 % by 0.40 s, +9.0 % by 0.60 s, approaching 112 %. `build.py` interpolates those measured values. |
| In AE | Sharpen **70** + **Turbulent Displace** (Displacement Turbulent, Amount **4**, Size 100, Complexity 1, Offset [540,960], Pinning 3, Evolution ramped continuously) |
| In the precomp | CapCut export scaled **50 %** (CapCut renders 4K) + **Deep Glow** (Exposure 0.55, Unmult on) + **Bevel Alpha** 2.4 + **2 × Drop Shadow** (Opacity 255, Distance 12) |
| CapCut blur | blur **0.80**, blend **1.0**, multiple_blur **6**, `bilateral` |
| CapCut export defect | its 4K HEVC lifts the black on one frame every ~2 s (frames 5, 119, 239 …); run `clean_capcut.py` on it before AE, or the stack above renders a one-frame "black static" mesh (LESSONS 2026-09-26) |

**Colour rules** (mid-colour sampled; each is a gradient, most words stay white, one or two coloured per caption):

| Style | Colour (mid) | Meaning in use | Examples |
|---|---|---|---|
| Red Shade Greators | `#DB4649` | the insult / the wound / the shock | WACKO JACKO, INTIMATE, MEDIA, FAKING, SPECULATED, BS |
| Light Blue Shade | `#3ECBDD` | names, places, neutral key nouns | MICHAEL, JACKSON, STUDIO, SOMEBODY |
| Pink Shade | `#DF31E9` | **love, affection, tenderness — and women** | LOVE, S*X, LISA MARIE, TOGETHER, KITCHEN, LOVED, CARE |
| Orange Yellow Shade | `#E6B401` | emphasis / energy | 24 HOURS, DAY TO DAY, WAKING UP, CAREER, CENTER, REAL |

**Punctuation: none except `?` and `!`.** No commas, no full stops — confirmed by the creator
2026-09-21. (Quotes around a quoted insult are still fine.)

**Sensitive words are censored, not dropped:** `sex` → **S*X**, and it takes the Pink Shade,
because on this channel the word is about love and affection rather than shock.

**The colours are saved Text Styles in the Premiere project, not hand-set fills.** `ABW6.prproj`
carries 12 styles; the caption set is:

| Style name | Use |
|---|---|
| **Gretaros** | the default white caption |
| **Gretaris Italic** | the other speaker / non-speech (§ typography below) |
| **Red Shade Greators** | red emphasis |
| **Pink Shade** | magenta emphasis |
| **Light Blue Shade** | cyan emphasis |
| **Orange Yellow Shade** | yellow-orange emphasis |
| **Green Shade** | green emphasis (exists, unused in the reference short) |

(The others — GTA, Cenat PBE, Doc IG Style, Onyx, Calibri — belong to other channels.)
**Apply the style by name; never rebuild the gradient by hand.**

**Typography rules:**
- **ITALIC = the other speaker.** The interviewer's questions are italic; the subject's answers upright.
- **Asterisks + italic = non-speech annotation** (\*SAYS IT AGAIN\*, \*FRUSTRATED\*).
- Quotes kept around quoted insults (“WACKO JACKO”, “HE'S A JACKO”).
- Names spelled correctly even where the audio is unclear.

## 9. Audio

| Track | Content | Treatment |
|---|---|---|
| A1 | speech stem (`<job>-esv2-27p-bg-10p-music-10p.mp3`) | **Studio Reverb**: Room Size 0.697, Decay 0.235, Early Reflections 0.52, ER Delay 0.5, Width 0.25, Diffusion 0.5, Damping 0.5, Low Cut 0.216, High Cut 0.690, **Dry 0.75 / Wet 0.25** |
| A2 | music (here: Patrick Watson — *Je te laisserai des mots*), 0 → end | no effects |
| A3 | **ElevenLabs voiceover** on the opening (voice "Christopher – Gentle and Trustworthy"), 0 → 5.57 | same Studio Reverb |
| A4 | SFX: cinematic whooshes + one camera-flash hit | whooshes carry a **Lowpass** (cutoff 0.642); the camera flash does not |

- **Whoosh placement:** starts **0.2–1.0 s before** its cut so the peak lands on the flash
  (cuts 0.98 / 9.17 / 10.72 / 18.43 / 23.27 / 32.10 ← whooshes 0.68 / 8.97 / 9.73 / 17.63 / 22.73 / 31.83).
- Clip gain stays at default everywhere; balance comes from the pre-mixed stem, not fader moves.

## 10. The head lock (the FIRST AE comp)

Each short passes through **two AE comps**, and the reference project shows both:

- **Comp 1 — the head lock** (e.g. `ABW6 Linked Comp 01`): the cut clips, each one blown up
  (**Scale ≈ 546 %** on the reference layer) and **Anchor Point keyframed on every single frame**
  (36 keys over 1.17 s, **linear** interpolation) so the nose stays on one spot.
  **Motion Tile** (Output Height **340**, **Mirror Edges on**) fills the edges the moves expose.
  This comp is rendered out and fed to Topaz (`<job>_stab_chr2_iris3.mov` — "stab" = this stage).
- **Comp 2 — the build** (e.g. `ABW6 Linked Comp 03`, `ABW6 Linked Comp 02`): the Topaz file comes
  back and gets everything in §§ 2–8.

A still image or an overlay never gets the head lock. Only **Iris (default-label)** clips are locked;
**Violet** clips are left alone (the creator's label, ABW8 2026-09-23). The lock also runs straight on
a "Replace with After Effects Composition" comp at Premiere's own scale (89–267 %); the nose is held
by Anchor keys alone, so re-sliding Position later keeps it. Procedure + proof: PLAYBOOK § 2.

## 11. Endings

The reference short ends on a **still photo** (a Higgsfield-enhanced PNG, 2048×2048, placed at 95 %
scale, x 449) held for 3 s under the closing captions — not on footage.
