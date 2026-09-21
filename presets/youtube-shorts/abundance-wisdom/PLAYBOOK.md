# Abundance Wisdom — THE PROCEDURE

How a short gets built, who does which part, and the exact mechanics Claude uses.
Numbers live in [README.md](README.md). Read both before touching a job.

## Division of labour (agreed 2026-09-14, confirmed by the 2026-09-20 teardown)

| Stage | Owner |
|---|---|
| Idea, angle, beats (Cowork project `E:\Claude Projects\Abundance Wisdom\`) | **Creator** |
| Downloading the source videos | **Creator** |
| Sequencing / arranging the cut in Premiere, removing ums and silences | **Creator** |
| Higgsfield overlays and stills | **Creator** |
| Music choice | **Creator** |
| CapCut motion-blur pass on the caption export, and placing it back | **Creator** |
| Everything else — head lock, Topaz, caption authoring, the AE build, audio, export | **Claude** |

## The handoff

The creator hands over a **Premiere project + sequence name** (reference: `ABW6.prproj` /
`Sequence 11`). In it:

- **V1/V2** hold the raw source and the working area (the long interview sits far down the timeline,
  past the short itself — ignore everything after the short's end).
- The short occupies **0 → its length** on the upper video track.
- The creator's sequencing is the cut; Claude does not re-time it.

## Claude's line, in order

### 1. Read the cut
Read the sequence through the Premiere bridge (`node lanes/premiere/premiere-bridge.mjs
get_full_sequence_info`, or `execute_extendscript` with an IIFE for anything custom). Record every
shot boundary — these become the spans for zooms, grades and flashes.

### 2. Head lock — its own comp
Track the speaker's nose outside AE (AE's tracker cannot be driven by script), then write the result
in the creator's own shape: **Anchor Point keyframes on every frame** (linear) on a scaled-up layer,
plus **Motion Tile** (Output Height 340, Mirror Edges on) to cover the exposed edges — README § 10.
This is a **separate comp** that gets rendered and handed to Topaz; the build comp comes after.
Speaking shots only; never on overlays or stills.

### 3. Topaz
Run the creator's **`Iris Preset`** through the Topaz CLI
(`C:\Program Files\Topaz Labs LLC\Topaz Video AI\ffmpeg.exe`, filters `tvai_up` / `tvai_fi` / `tvai_stb`):
enhance `iris-3` (detail 73, sharpen 42, compression 84, denoise 14, deblur 14, dehalo 20,
focus-fix Standard), frame interpolation `chr-2` to **60 fps**, stabilisation smoothness 50.
Output naming follows the creator's own convention: `<job>_chr2_iris3.mov`.

### 4. Captions (Claude writes, creator morphs)
1. Word timings from WhisperX on the cut's audio — never Premiere's transcribe pass.
2. Chunk into **1–3 words**, wall-to-wall, median ≈ 0.75 s (README § 8).
3. Apply the colour and typography rules (README § 8): white by default, one or two gradient
   words per caption, **italic for the other speaker**, asterisks for non-speech, correct name spellings.
4. Build them as Premiere Graphics — line 1 on the caption track, a **second graphic one track up**
   for two-line captions — each growing ≈ 7 % over its own duration.
5. Export the caption layer on black (video tracks hidden).
6. **Hand to the creator** for the CapCut motion blur (blur 0.80 / blend 1.0 / multiple_blur 6 /
   bilateral) and the return trip into AE. Say clearly which file is ready and where it is.

### 5. The AE build
Driven by ExtendScript: `Start-Process AfterFX.exe -ArgumentList @("-r", "<path>.jsx")`.
**Pass the path unquoted inside the array** — extra quotes make the script silently never run.
Scripts report back by writing a result file (needs Preferences → Scripting & Expressions →
"Allow Scripts to Write Files and Access Network", already on since 2026-09-14).

Build order per shot:
1. Footage layer, masked, plus its **198 % / 43 %** twin underneath where the source is letterboxed.
2. **Glow bars** on the mask edges.
3. **Grade adjustment layer** per section — create an adjustment layer and
   `applyPreset(File("C:/Users/affan/OneDrive/Documents/Adobe/After Effects 2025/User Presets/Affan CC Preset.ffx"))`.
   That single file carries the whole nine-effect stack, which is exactly what the creator does by
   hand (new adjustment layer, drag the preset on). Never re-enter the values.
4. **Zoom adjustment layer** per shot: `S_BlurMoCurves`, Z Dist across the whole shot,
   pop-then-settle easing, direction alternating and continuous across cuts (README § 3).
5. **Flash / dip adjustment layer** per transition, peak on the cut (README § 7).
6. Caption precomp on top once the creator returns the CapCut file: scale 50 %, Deep Glow (Unmult),
   Bevel Alpha, two Drop Shadows, then Sharpen 70 + Turbulent Displace 4 on the layer in the main comp.

The creator's own script `After Effects - Adjustment Layer T.jsx` (in their User Presets folder)
snaps each adjustment layer to the clip below it and stretches its BlurMoCurves keyframes — match
that behaviour rather than fighting it.

### 6. Audio, back in Premiere
- Speech stem and any voiceover get the **Studio Reverb** settings in README § 9.
- **Whooshes** 0.2–1.0 s before each cut with a Lowpass at 0.642; a camera-flash hit where a
  photo or reveal lands, dry.
- Music: the creator's track, running the full length, no effects.
- Target the channel's current loudness, **−15.3 LUFS**, true peak ≤ −1.4 dBFS.

### 7. Export
Render from AE (`aerender.exe`) or export the sequence through the Premiere bridge; 1080×1920, 60 fps.
Final naming follows `<Job> Final YT.mov`.

## Working rules

- **Never open, save or modify the creator's projects without saying so.** Reads are free; writes
  are announced first.
- **While a script runs, After Effects is busy** — tell the creator not to work in it during a run.
- A big dump script can exceed 4 minutes and look like a failure. Chunk the work (layer ranges) and
  poll for a result file.
- The creator's timelines carry deliberate irregularities (a 0.7× first clip, alternating 0.99×
  segments). Do not "clean these up" — ask (LESSONS.md, open questions).

### The zoom pass (scripted, validated 2026-09-21 on ABW6 Linked Comp 06)

Shots come from the footage layers themselves (one shot per distinct in/out pair; the caption
precomp and adjustment layers are skipped). **The creator labels the direction on the footage:
AE label 2 (yellow) = pull out, anything else = push in.**

Per shot: an adjustment-layer solid named `Adjustment Layer 29`, inserted directly UNDER the caption
layer so captions never zoom, spanning exactly the shot, with `S_BlurMoCurves`.
**Depth (creator's rule): < 1.25 s → 0.87 · < 2.5 s → 0.78 · longer → 0.70**, push-in from 1.00,
pull-out to 1.00. **Center XY from `zoom_center.py`** (face pivot when a centred zoom would lift the
face top above y200), never animated.
The house curve is reproduced with temporal eases: departure speed = 44x the average rate at
1.7 % influence, arrival = 17x at 2.8 % — verified by sampling the result (worst deviation 0.022).

Script: `scratchpad/ae/zoom06.jsx` pattern — always re-runnable (it removes its own previous layers
first) and it tidies the unused solids it creates.

**Gotchas that bit once each:** `moveAfter` throws if the layer is already where it would move to;
ExtendScript chains `?:` LEFT-associatively, so nested ternaries silently collapse — use if/else.
