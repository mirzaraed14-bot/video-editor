# Abundance Wisdom — Shorts Style Spec (DRAFT, awaiting approval)

> **Superseded where they disagree by [README.md](README.md)** (measured from the live Premiere + AE
> projects on 2026-09-20). This file is the earlier analysis of three finished exports.

Built on 2026-09-14 from two sources:
- **The director's own walkthrough** of the workflow (§0). **Confirmed** = they said it.
- **Three finished exports** in `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\`:
  `Sequence 41.mov` (Simone Biles, 54.75 s), `Fist Final YT.mov` (Prince Jackson / Jaafar, 32.37 s),
  `struggle.mp4` (Michael Jackson, 9.88 s).
  **Measured** = ffmpeg / WhisperX / pixel sampling. **Observed** = read by eye from 1 fps contact sheets.

---

## 0. The hand workflow today (confirmed)

| # | Step | Where | What |
|---|---|---|---|
| 1 | Ideation | Claude Cowork project (outside this repo) | Every short's analytics logged; viral factors reverse-engineered. Current winner: **correcting misconceptions about famous celebrities** (Michael Jackson especially). |
| 2 | Sourcing | Claude + Chrome | Scours YouTube for soundbites; returns **beats + timestamps as text**. Stitched from many channels into one unique story angle. Speaker preference: **the celebrity about themselves**, else family / people close to them (2.5M-view format). |
| 3 | Assembly | Premiere (by hand) | Downloads the clips, cuts to the timestamps, sequences, removes silences and ums/ahs. |
| 4 | Overlays | Premiere + Higgsfield | Slow-motion topic footage or stills of what's being said, enhanced in Higgsfield. Used where camera quality is poor or a point needs emphasis. Final cut/angle check. |
| 5 | Head lock | After Effects (Dynamic Link) | Warp Stabilizer-style **Stabilize Motion track on the nose** so the face sits at a constant point. Speaking shots only; overlays are never tracked. |
| 6 | Enhance | Topaz Video AI | Preset `Iris Preset` (see §5), running while step 7 happens. |
| 7 | Captions | Premiere → CapCut | Premiere Transcribe draft → timing fixed word by word → spelling fixed by hand → ≤3 words per layer → emphasis words coloured with gradients → **"revised light pop" preset** → caption layer exported alone on black → CapCut **motion blur** → exported as video. |
| 8 | Motion | After Effects | Enhanced video dropped back at its exact position → AE comp → **Sapphire S_BlurMoCurves zoom on every camera/scene change** (custom graph-editor eases) → CapCut caption video on top → **Deep Glow** (drops the black) → **Turbulent Displace** (wavy, not static) → adjustment-layer **fade-to-black / fade-to-white / flash** transitions → export. |
| 9 | Sound | Premiere | SFX where needed, **light Studio Reverb on all speech**, music track, audio mix exported and checked on a phone, levels adjusted. |
| 10 | Export | Premiere | Final export → upload. |

App round trips per short: Premiere → AE → Topaz → Premiere → CapCut → AE → Premiere.

## 1. Format (measured)

- 1080×1920, **60 fps** (Topaz Chronos output), H.264. Two `.mov` with PCM audio, one `.mp4` with AAC.
- Length is story-driven: 10 s (one quote) to 55 s (full arc).

## 2. Story shape (measured + observed)

- **Cold open on the first word** (first word at 0.03–0.13 s). No intro, no logo.
- Open = a news-anchor setup line, or the most emotional quote itself.
- **Ends on the last spoken word** (within 0.03 s of the file end). No outro tail.
- Arc (Biles): setup → problem in her own words → expert explains → emotional low ("I'm sorry") →
  decision to return → new setback → payoff (medal smile).

## 3. Pacing (measured)

| | Seq 41 | Fist | Struggle |
|---|---|---|---|
| Speech pace | 226 wpm | 256 wpm | 164 wpm |
| Pauses > 0.3 s | 7 | 1 | 0 |
| Longest pause | 2.16 s (the "I'm sorry" beat) | 0.72 s | 0.12 s |
| Distinct shots (observed, 1 fps floor) | ~20 → one every ~2.7 s | ~14 → one every ~2.3 s | 2 |

- Dead air cut to almost nothing; the one long pause is a deliberate emotional beat.
- Within a shot the framing changes every ~1–2 s: the BlurMoCurves zooms of step 8.

## 4. Framing (measured)

**A. Full-bleed 9:16**, the default. Face held at a constant point by the nose track (§0 step 5).

**B. Letterbox band** on wide 16:9 sources (two-shots, full routines, TV-branded footage):
- Band from **y≈516 to y≈1406** (890 px tall, full width); clip scaled to about 146% of a 16:9 fit.
- **Glowing white rule** (~6 px plus glow) on the top and bottom edge.
- Behind it: the same clip, scaled to fill, **blurred and darkened** (~40% brightness).
- The band slides vertically into place.
- Not described in the walkthrough yet: how it's built (open question 3).

## 5. The look (confirmed + measured)

**Topaz Video AI 5.0.4, preset `Iris Preset`** (`C:\ProgramData\Topaz Labs LLC\Topaz Video AI\presets\Iris Preset.json`):

| Stage | Settings |
|---|---|
| Enhance | model **iris-3**, video type progressive, auto 2 · detail **73** · sharpen **42** · compression **84** · denoise 14 · deblur 14 · dehalo 20 · add noise 0 · focus fix **Standard** |
| Frame interpolation | model **chr-2** (Chronos), factor 1, duplicate-frame replacement on (threshold 10), output **60 fps** |
| Stabilization | method 1, smoothness **50**, rolling-shutter correction on |
| Grain / motion blur | off |

This is the "enhanced HD" look (painterly skin, crisp detail). Every short also has a
**strong dark oval vignette** (observed; source not named yet, open question 3).

## 6. Captions (confirmed + measured)

- **Font: Gretaros** (`Gretaros-Regular.otf`, installed in the user fonts), ALL CAPS.
- **≤ 3 words per caption** (confirmed), max 2 lines.
- **Timing:** every word appears exactly when it is spoken. Premiere's draft needs fixing by hand today;
  WhisperX word alignment gives this directly.
- **Spelling:** names corrected by ear (captioned COLEMAN and JAAFAR where the transcriber heard
  "Colton" and "Jafar"), so each job needs a corrections file.
- **Size / position (measured):** cap height ≈ 45 px; centred; first line at **y≈1015–1040**, a second
  line stacks below (~60 px pitch).
- **Base:** white, hard dark drop shadow down-right (~4–5 px).
- **Emphasis colour.** Most words stay white; only emphasis words are coloured, and **always as
  gradients, never flat colour** (confirmed). Chosen by the word's meaning:

  | Colour (gradient) | Meaning (confirmed) | Sampled centre | Seen on |
  |---|---|---|---|
  | Red | violence / danger: kill, destroy, drugs, explosives | `#DD2F45` | TAKEN AWAY, PULLED OUT, QUITTER, PAIN |
  | Pink | happiness, parents, children | `#D612F6` (magenta range `#B200E8`→`#F14EFD`) | CHILDHOOD, CHRISTMAS, HER COACHES |
  | Yellow → orange | morning, sunshine, good | `#FCC018` / `#ECD721` | HARD WORK, COMPETITION, SERIOUSLY |
  | Blue | by feel | `#51EEF7` (cyan) | BIRTHDAYS, HISTORY, BRAIN, WORLD |
  | Green, purple | by feel | not sampled yet | — |

- **Animation stack** (confirmed): "revised light pop" preset (pop on entry) → CapCut motion blur (words
  smear into each other on the switch) → Deep Glow → Turbulent Displace (wavy).
- **CapCut motion blur** (read from the drafts in
  `%LOCALAPPDATA%\CapCut\User Data\Projects\com.lveditor.draft\`, identical across 0905/0907/0912):
  `motion_blur_config = { blur: 0.80–0.81, blend: 1.0, multiple_blur: 6, blur_frame_type: "bilateral" }`
  on the caption video. Draft canvas 1080×1920.
  **Ground-truth pair for the fist-bump short** in `E:\Shorts\Abudance Wisdom Shorts Exports\Caption Exports\`:
  `fist.mov` = caption layer before CapCut (1080×1920, 60 fps, H.264, 32.37 s);
  `fist2.mp4` = after CapCut (**2160×3840**, 60 fps, HEVC). Same pairs exist for `deb`; `birth` and
  `untur` have only the before file.
- **Context tag** (observed, not described yet): small line under the caption on archival clips,
  magenta or cyan, in asterisks: `*2020*`, `*PARIS OLYMPICS 2024*`.
- **Punctuation** (observed): curly quotes on quoted speech (“OKAY”); asterisks on non-speech
  (*LAUGHING*); ellipsis on cut-offs (BUT…).

## 7. Motion and transitions (confirmed + observed)

- **Zoom on every camera/scene change:** Sapphire **S_BlurMoCurves**, keyframes shaped in the graph
  editor so it *pops* then settles gradually (never linear). Some shots S-curve in, some zoom out, some mix.
- **Transitions:** adjustment layers for **fade to black, fade to white, flash**.
  Observed use: the dip to black lands on emotional lines ("I'M SORRY", "DO THAT") with the caption
  staying bright; dark → bright reveal on the payoff shot.

## 8. Audio (confirmed + measured)

- Speech = each source clip's original audio + **light Studio Reverb** over all of it.
- **Music bed under the whole short** (0 gaps below −45 dB in all three); in Seq 41 it sits ~6 dB under the voice.
- SFX where needed. The mix is checked on a phone.
- **Loudness varies across exports** (measured):

  | | Integrated | LRA | Peak |
  |---|---|---|---|
  | Seq 41 | −20.0 LUFS | 6.5 LU | −3.8 dBFS |
  | Fist | −17.2 LUFS | 3.2 LU | −0.6 dBFS |
  | Struggle | −11.6 LUFS | 1.4 LU | **0.0 dBFS** |

  **Proposal:** lock one target so every short plays at the same volume on YouTube.

---

## Automated line (proposed)

| # | Step | Who | How |
|---|---|---|---|
**Agreed 2026-09-14:** the director keeps downloading, sequencing, overlays, music choice and the
CapCut motion-blur pass. Claude takes over from the arranged Premiere sequence.

| 1 | Idea + beats + timestamps | **Director** (Cowork project) | unchanged |
| 2 | Download source clips | **Director** | unchanged |
| 3 | Sequencing + silence/um removal in Premiere | **Director** | unchanged: the arranged sequence is the handoff |
| 4 | Higgsfield overlays | **Director** | placed in the sequence before handoff |
| 5 | Head lock | Claude | face tracker on the nose, constant point, speaking shots only |
| 6 | Enhance | Claude | Topaz CLI (`ffmpeg.exe` with `tvai_up` / `tvai_fi` / `tvai_stb`) using the `Iris Preset` values above |
| 7 | Caption layer | Claude builds → **director** runs the CapCut motion-blur pass → Claude places it | word-exact timing, ≤3 words, corrections file, emphasis colours by the §6 meaning table, gradients, pop; exported on black like today |
| 8 | AE edit | Claude | BlurMoCurves zoom on every cut, Affan CC Preset, fade black / white / flash, Deep Glow + Turbulent Displace on the CapCut caption video |
| 9 | Sound | Claude, **director** picks the music | Studio Reverb on speech, SFX, music bed at the director's track, one loudness target |
| 10 | Review + export | **Director** gives taste notes; Claude fixes and exports | every note becomes a rule in this spec |

**Decision pending:** steps 7–8 either **driven inside After Effects by script** (your real Sapphire /
Deep Glow / Turbulent Displace, and you get a normal AE project to tweak) or **rebuilt in this system's
render engine** (no AE dependency, close rather than exact).

## Open questions

1. Is `Iris Preset` (dated 15 Nov 2025) the preset you use on every short today?
2. The "revised light pop" preset: where is it saved? A Premiere preset is a readable `.prfpset` file.
3. Not in the walkthrough: the **letterbox band with glowing lines**, the **oval vignette**, the
   **context tags** (`*2020*`). Where and how are these made?
4. ~~Sample brief~~ **Found:** the Content Engine lives at `X:\Claude Projects\Abundance Wisdom\`. The
   "FINAL LOCKED BUILD" block of a `*-CUT.md` (numbered beats: quote / source title / YouTube URL /
   in → out timestamps) is the step-3 input. Also found: `Abundance Wisdom Main CC Presets` (four AE
   presets `1–4.ffx`, each Lumetri Color + Curves, likely the source of the vignette).
   **Answered:** the grade in use is **`Affan CC Preset.ffx`** (identical to `2.ffx`), in
   `C:\Users\affan\OneDrive\Documents\Adobe\After Effects 2025\User Presets\`. That folder also holds
   `Deep Glow Caps.ffx`, `Deep Glow Line Preset.ffx` (likely the letterbox rules), the fade/brightness
   transition presets, `Brightness + Directional Blur + Blurmocurves.ffx`, and the director's own script
   `After Effects - Adjustment Layer T.jsx` (snaps each adjustment layer to the clip below and stretches
   its S_BlurMoCurves keyframes to fit).
5. **Save a Copy As XML (.aepx)** of one recent AE project (e.g. `ABW7.aep`): it exposes the exact
   BlurMoCurves keyframe graphs, Deep Glow and Turbulent Displace values, and transition timings.
6. One loudness target for every short. OK?
