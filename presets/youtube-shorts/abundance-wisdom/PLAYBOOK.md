# Abundance Wisdom — THE PROCEDURE

How a short gets built, who does which part, and the exact mechanics Claude uses.
Numbers live in [README.md](README.md). Read both before touching a job.

## Division of labour (agreed 2026-09-14, confirmed by the 2026-09-20 teardown)

| Stage | Owner |
|---|---|
| Idea, angle, beats (Cowork project `X:\Claude Projects\Abundance Wisdom\`) | **Creator** |
| Downloading the source videos | **Creator** |
| Sequencing from the pasted script (§ 0), then the creator's own pass over it | **Claude**, then **Creator** (since 2026-09-23) |
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

### 0. Sequencing (when the creator hands over a script + a bin + an empty sequence)
Build ONLY what they paste (not the Content Engine file's other drafts). Tools in this folder; worked
examples: `projects/mj-allegations`, `projects/eminem-hailie`.
1. `sources.json` per source (`offset`/`window` for long ones, `fps`, camera `cuts` from ffmpeg `scdet`,
   `border` for a baked channel frame). Extract each window's audio LOSSLESSLY to `raw/<key>.mov`,
   then `transcribe.sh <job>`.
2. `beats.json`: segments as word anchors (`find_quote.py` to locate), `"tighten"` on (pauses ≥ 0.13 s
   go), overrides `in`/`out` wherever an edge was MEASURED (10–20 ms RMS; isolated Whisper re-listens
   for fillers and numbers the transcript dropped or mistimed). Repeated line → last take.
3. `resolve_beats.py` → `edl.json`; `plan_placement.py` → `placement.json`; check a contact sheet of the
   actual 9:16 crops, and put faces the detector misses (profiles, listeners, wides) into `framing.json`.
   A face the source never shows ("open on her while she listens") = a beat `"cover"`: a picture-only V2 insert.
4. `place_sequence.py` → run the .jsx (it refuses a non-empty sequence; camera-cut splits become razors on one
   clip, placed from the in-point Premiere actually took) → read back every clip, including that each clip's
   first and last frame sit inside its shot → **rebuild the audio from the read-back in/outs and re-transcribe it
   against the script.** An ending the creator hedges ("if it doesn't land") is judged in context, never isolated.
5. Flag, never hide: shots where the broadcast shows someone else, whip-pans, wides.

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

**Scripted (validated 2026-09-23, ABW8 Linked Comp 02 + 03):**
1. The creator does "Replace with After Effects Composition" over the clips. **Iris (default label)
   = lock; Violet = leave alone.** Save a Premiere copy first and read the labels from it.
2. `head_track.py <job> <v1_live.txt> <idx,...>` → `track.json` (nose per 60 fps frame, source px).
   Build the clip list from the linked comps' OWN layers (read from AE: source, in-point, scale,
   position), since the creator may recut before replacing (`projects/eminem-hailie/brief/`).
   Check the sheet (`uv run track_sheet.py <job>`, frames as AE shows them, in each layer's own scale and
   position): the dot on the speaker's nose, AND the nose inside the creator's crop.
   A source with a baked border (Mike Tyson's uploads) gets `"prescale"` in the map (LESSONS 2026-09-26).
3. Write `headlock_map.json` (comp, layer, clip, tl_offset = the comp's start in the sequence) and
   verify every layer's in-point = tl_start − tl_offset before running anything.
4. `apply_headlock.py <job> <map> <out.jsx>` (holds each nose at its median, `--hold first` for
   frame 1) → `node --check` the .jsx (a syntax error opens a modal in AE that blocks every later
   script) → run with `AfterFX -r`. One undo group, "Head lock (Claude)"; it re-keys cleanly if re-run.
5. `headlock_proof.py jsx …` → run → `headlock_proof.py sheet …`: every LOCK row must hold the nose
   on the crosshair. Never measure it with a face detector on the blown-up comp (LESSONS 2026-09-23).
6. A layer at Scale 100 (letterboxed) is asked about, not locked: Motion Tile would fill the bands.

### 3. Topaz
Run the creator's **`Iris Preset`** through the Topaz CLI
(`C:\Program Files\Topaz Labs LLC\Topaz Video AI\ffmpeg.exe`, filters `tvai_up` / `tvai_fi` / `tvai_stb`):
enhance `iris-3` (detail 73, sharpen 42, compression 84, denoise 14, deblur 14, dehalo 20,
focus-fix Standard), frame interpolation `chr-2` to **60 fps**, stabilisation smoothness 50.
Output naming follows the creator's own convention: `<job>_chr2_iris3.mov`.

**Recommended look, tested 2026-09-23 on ABW8 `hurt.mov` against a competitor frame (Topaz 5.0.4):**
Iris with the SAME sliders but **Focus fix Strong** (25 % down, 4× back up), then a **second
enhancement: Proteus at 1×** (Improve detail 60, Sharpen 60, everything else 0), **grain off**.
The competitor frame is graded and ours is not (the creator grades AFTER Topaz), so compare with
contrast normalised out (Laplacian std ÷ face std): competitor edges 1.9 / texture 0.12; 60 Minutes
close-up: one pass 1.1/0.07, one pass + grain 1.5/0.18, **two passes 1.6/0.10**, two passes + grain
1.9/0.21 (grain overshoots the texture, so leave it off and judge after the grade).
**Cost: two passes ≈ 3× the enhancement time** (7.3 vs 2.2 min for a 49 s short on the 3060 Ti).
Worth it on soft, blown-up sources; skip the second pass when the short is mostly sharp HD (Bashir
was already past the competitor on one pass: 3.0 vs 1.9).
What did NOT help: pushing the Iris sliders (detail 100 / sharpen 70 got SOFTER), Add noise 5
(softer, waxier), Proteus as the only model (softer). The sliders matter little; Focus fix is the lever.
Test harness: CLI `tvai_up` on 0.5 s slices, `ffmpeg -h filter=tvai_up` for the options; GUI value
= CLI value × 100. Before/after: `projects/mj-allegations/topaz-before-after.jpg`.

### 4. Captions (Claude writes, creator morphs)
1. Word timings from WhisperX on the cut's audio — never Premiere's transcribe pass.
   `workflows/sequence-captions.py read <job>/captions "<Sequence>"` rebuilds the live A1 (any number of
   sources) on the sequence clock, then `transcribe.sh`; `… import` puts the .srt on as a caption track.
2. Chunk into **1–3 words**, wall-to-wall, median ≈ 0.75 s (README § 8).
3. Apply the colour and typography rules (README § 8): white by default, one or two gradient
   words per caption, **italic for the other speaker**, asterisks for non-speech, correct name spellings.
4. Build them as Premiere Graphics — line 1 on the caption track, a **second graphic one track up**
   for two-line captions — each growing ≈ 7 % over its own duration.
5. Export the caption layer on black (video tracks hidden).
6. **Hand to the creator** for the CapCut motion blur (blur 0.80 / blend 1.0 / multiple_blur 6 /
   bilateral) and the return trip into AE. Say clearly which file is ready and where it is.
7. **Clean the CapCut return BEFORE it goes into AE:** `python clean_capcut.py "<Caption Exports>/<name>.mp4"`
   → `<name>_clean.mp4` beside it (~4 min for 50 s of 4K). CapCut dirties the black on one frame every ~2 s,
   which the caption stack turns into the one-frame "black static" (LESSONS 2026-09-26). This replaces
   razoring the bad frames out in Premiere and slowing a block to 99 %.
   **Already in AE?** Clean it anyway and re-point the footage item at `<name>_clean.mp4` (FootageItem.replace,
   one undo group; `projects/paris-jackson-masks/captions/capcut/kid2_replace.jsx`): the precomp and its effects stay.

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
6. Caption precomp on top once the creator returns the CapCut file (the `_clean.mp4`, § 4 step 7): scale 50 %, Deep Glow (Unmult),
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
face top above y200), never animated. **Which face:** posters (a box under 35 % of the widest) are
dropped, then the TOP-most face scoring >= 0.8 is protected; with none that sure, the largest box
(close-ups score 0.64-0.76). Never simply the largest box: on stage shots it is a torso or glutes.
A pivot the preview shows is wrong (a painting, a poster, a face pushed off the SIDE) is pinned in
`<work>/centers.override.json` (`center_y`, optional `center_x`).
The house curve is reproduced with temporal eases: departure speed = 44x the average rate at
1.7 % influence, arrival = 17x at 2.8 % — verified by sampling the result (worst deviation 0.022).

Script: **`zoom_pass.py <srcmap.tsv> "<comp>" <work_dir>`** (since 2026-09-24; the layer dump is the
`dump08.jsx` pattern: one row per layer with label, in/out, startTime, adj, enabled, path) → writes
`apply.tsv` + `zoom.jsx` from `zoom_pass.jsx.tmpl`; run it with `AfterFX -r`. Re-runnable (it removes
its own previous layers first), one undo group, tidies its unused solids, reads each Z Dist back.
Face check samples **0.1 s inside** both ends of each block (never the cut frame itself: Topaz can
leave it blurred, and a blurred face isn't detected) and keeps the more protective pivot.
Preview every block at its deepest zoom before running (`projects/eminem-hailie/zoom/preview.py <work_dir>`:
any number of blocks, stills placed as the comp places them).
**Doubles** (a 100 % shot over its 198–229 % twin, same in/out) are ONE block with one zoom above both.
The zooms sit directly under a caption layer if there is one, otherwise on top: always above the glow bars.

### The transition pass (scripted, validated 2026-09-24 on ABW8 comp 06, 2026-09-26 on comp 18)

AFTER the zoom pass, once the creator has relabelled the blocks (README § 7). Re-read the labels first
(a fresh layer dump): the zoom-time labels are stale. `transition_pass.py "<comp>" <out.jsx>` →
`node --check` → run with `AfterFX -r`; the log lands next to the jsx. Doubles merge into one block
(else the twin reads as the next block and the cut lands on the block's own start). The layers go
directly under the caption precomp (a top layer named "…Comp 1" that isn't a glow bar), above the zooms.
Re-runnable: it removes its own `Adjustment Layer 30` / `White Solid Flash` layers first.

**Gotchas that bit once each:** `moveAfter` throws if the layer is already where it would move to;
ExtendScript chains `?:` LEFT-associatively, so nested ternaries silently collapse — use if/else.
