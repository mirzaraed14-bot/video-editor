# LANES — which app can do which step, and where the recipe lives

**The law this file enforces: the PRESET says WHAT, the APP SKILL says HOW.**

A preset is a LOOK. Every number in it (a frame count, a scale percentage, a hex, a dB, a
duration) means the same thing in every editor, and every graphic it specifies is rendered by
HyperFrames into a file any NLE can take. So the preset never carries app mechanics, and an app
skill never carries look decisions. That split is what makes ONE preset produce the SAME video on
any lane.

It is also why the mechanics live with the app and not with the preset: placing an alpha mov at a
timecode is identical whether the job is `youtube/default` or `instagram/explainer`. Written into
each preset it would be re-written once per preset per app. Written into the app skill it is
written once, and a new preset inherits every lane for free.

**This file is the third piece: the index that connects them.** At step N on lane L, read the
preset's § step N for the target, then this file's row N for where lane L's mechanics are.

## Where the lanes live

**Every app-specific file is under [`lanes/`](lanes/README.md), one folder per finish surface: `lanes/premiere/`, `lanes/resolve/`, `lanes/capcut/`, `lanes/chat-only/`** (since 2026-09-03). Scripts, templates, lane sheets and each lane's `lab-notes.md` (the locks true only on that app). The app skill in `.claude/skills/` is the HOW doc for the lane and points into its folder; `workflows/` at the root holds only universal utilities. So the two questions have two homes: "is step N defined and done" is answered by `CLAUDE.md` § The Pipeline and `projects/<job>/RUN.md`; "does app X have a scripted recipe for step N" is answered here and in `lanes/<app>/`. Never let the second question's answer leak into the first (the chat-only lane having no grade stage is a lane fact, not a pipeline fact).

## How to read a cell

| | |
|---|---|
| ✅ | **Scripted and validated.** A command or an API call exists and has been run on a real job. |
| ✋ | **Manual, by design.** Nothing to script, or the creator owns it. Do it by hand from the preset's numbers. |
| ⚠️ | **Unvalidated recipe.** The mechanism is documented and consistent with what is known, but no job has run it. Treat the first run as a test: verify by measurement, then upgrade this cell. |
| ⛔ | **Gap.** No recipe. Do it by hand from the preset's numbers and **say so out loud** — see below. |
| — | **Nothing lane-specific.** The step is universal; the lane changes nothing about it. |

**If an app skill's STEP INDEX disagrees with this matrix, this matrix wins.**

**Short-form presets carry only step 5, captions included.** `instagram/explainer` and
`tiktok/raw` are LOOKS for the graphics step (cards, hook card, and the caption layer both presets
run by default); every other step takes the universal target stated in this file's step rows
(step 3, step 6, step 8). A short-form job reads its style doc for step 5 and this file for the rest.

## The matrix

Steps are the pipeline in CLAUDE.md § The Pipeline. Lanes are the four finish surfaces.

| # | Step | Premiere | Resolve | CapCut | chat-only |
|---|------|----------|---------|--------|-----------|
| 1 | Intake | — | — | — | — |
| 2 | Rough cut → replay | ✅ | ✅ | ✅ | — |
| 3 | Audio polish | ✅ | ✅ | ⚠️ | — baked by splice |
| 4 | Color grade (long-form) | ✅ | ⚠️ | ⛔ | ⛔ |
| 5 | Graphics | ✅ | ✅ | ✅ | ✅ |
| 6 | SFX | ✅ | ⛔ plan only | ⛔ plan only | ⛔ plan only |
| 7 | Review | ✋ | ✋ | ✋ | ✋ |
| 8 | Export | ✋ the creator | ✅ | ✅ | — the render IS the file |
| + | Background music (opt-in) | ✅ | ✋ A5 track | ✋ audio track | ✅ |

### Where each cell's recipe lives

**Step 1 — Intake.** Universal: copy (never move) into `projects/<job>/raw/`. No lane involvement.

**Step 2 — Rough cut, then the EDL replay.** The cut itself is universal (`rough-cut`: WhisperX,
kill, splice `RENDER=0`). Only the replay is per-lane, and all three apps rebuild the same
`transcript/cuts.json` as separate trimmable clips.

- Premiere ✅ `node lanes/premiere/premiere-bridge.mjs replay …` — `premiere-pro` § Step 2
- Resolve ✅ `media_pool create_timeline_from_clips`, one call — `davinci-resolve` § Step 2
- CapCut ✅ `uv run lanes/capcut/capcut-bridge.py replay <job>` — `capcut` § Procedure 2
- chat-only — no replay; `splice.sh` renders the flat cut, on the SECOND splice after `polish-boundaries.py` (the first runs `RENDER=0` on every lane) — `rough-cut` § Polish the boundaries

**Step 3 — Audio polish. This section is the ONE home of the universal audio target.** One static
pass over the whole timeline, never dynamic loudnorm, never per-segment gain, re-applied after any
timeline rebuild (a rebuild discards clip effects). The house chain:

    gain = round(−17 − measured)  →  hard limiter at −6 dBFS

`uv run workflows/voice-gain.py projects/<job>` measures the raw's KEPT speech ranges
(`transcript/cuts.json`, ebur128 — never the whole take, dead air drags the number down) and returns
the whole-dB gain onto **−17 LUFS integrated pre-limiter**; a quiet shoot gets more, a hot shoot
less. The limiter is FIXED at **−6 dBFS**, so peaks land about 8 dB over the ceiling and it works
every stressed syllable — that saturation is the point (2026-09-03, calibrated on
`your-job`).

- Premiere ✅ `uv run lanes/premiere/audio-polish.py projects/<job> --apply` (`--verify` reads it back): the measured Amplify + Hard Limiter as clip effects on every A1 clip — `premiere-pro` § Step 3
- Resolve ✅ the same chain, baked into the media (its API has no audio-FX surface): `normalize-sections.sh` takes the `voice-gain.py` gain and the −6 dBFS limiter to each source file, then `replace-clips.py` swaps the copies under the locked timeline — [`lanes/resolve/resolve-audio-polish/`](lanes/resolve/resolve-audio-polish/README.md). (Unified with the house numbers 2026-09-04, the user's call; before that the lane normalized to −16 LUFS / −1 dBFS.)
- CapCut ⚠️ no audio-FX surface in the bridge. Recipe: apply the chain to the SOURCE file with ffmpeg before `replay`, so the draft is built against polished media. Unvalidated — `capcut` § Step 3
- chat-only — `splice.sh` already bakes the identical chain into the render

**Step 4 — Color grade (long-form).** Target (universal): the footage carries the look and **the
graphics carry none of it**, established before a single graphic is placed. The cube and the dial
values are the preset's: [`presets/youtube/default/README.md`](presets/youtube/default/README.md)
§ Grade. Only WHERE the separation lives is per-lane — a track on one app, a grouping on another.

- Premiere ✅ [`lanes/premiere/premiere-grading.md`](lanes/premiere/premiere-grading.md) — `grade-layer` builds the V2 adjustment layer, `grade-lut.py apply` writes the Look. Fully hands-off.
- Resolve ⚠️ the SEPARATION is validated and needs no track shuffle (a color group covers only its members, so the footage joins it and the graphics track does not). Applying the house **cube** through that group is the unvalidated half, and the two Lumetri dials have no scripted equivalent — `davinci-resolve` § Step 4, mechanism playbook in [`lanes/resolve/resolve-grading/`](lanes/resolve/resolve-grading/README.md)
- CapCut ⛔ no LUT surface in the bridge. Hand-apply a filter in the app, or accept an ungraded cut and say so.
- chat-only ⛔ the ffmpeg assemble lane has no grade stage.

**Step 5 — Graphics.** The graphics themselves are universal in the strongest sense: they are
rendered by HyperFrames into files (alpha ProRes 4444 for overlays, opaque mp4 for full-screens)
before any lane is involved. Plan with `graphics-plan`, build with `graphics-build`, converge with
`edit-review` — none of those three is lane-aware. Only PLACING a file and BAKING a footage move
are per-lane.

**The caption layer is part of this step (2026-09-04).** On the short-form presets the plan carries a `captions` cell and the preset's caption builder emits a straight-alpha ProRes 4444 (`hf-graphics/captions/renders/captions-alpha.mov`, no flat render needed); the lane's placer lays it on the top graphics track like any other overlay, spanning the whole cut (Premiere: V5, provisioned by `place-graphics.py`; Resolve: the highest video track, `AppendToTimeline` like any overlay; CapCut: `add-overlay` on the top layer, **premultiplied first** like every CapCut-bound alpha mov; chat-only: the last overlay in the assemble). Nothing burns captions after the render, on any lane. Long-form has no caption layer. **The short-form track map on Premiere** is the same shape as long-form minus the grade: V1 footage, V2 empty, V3 graphics, V4 overlaps, V5 captions.

- Premiere ✅ `uv run lanes/premiere/place-graphics.py projects/<job> --apply` (`--plan --write` first; then `--verify` / `--remove <id>` / `--sync-plan`) + the bridge `zoom` command for baked footage moves; 5c evidence: `uv run lanes/premiere/review-frames.py projects/<job> --round <N>` — `premiere-pro` § Step 5
- Resolve ✅ `AppendToTimeline` with `clipInfo` + a Fusion Transform comp for moves (`TimelineItem` has no keyframe API) — `davinci-resolve` § Step 5
- CapCut ✅ `add-overlay` + `keyframe` — ⚠️ **premultiply every CapCut-bound alpha mov first**; Premiere and Resolve both want STRAIGHT alpha — `capcut` § Procedure 4-6
- chat-only ✅ ffmpeg overlay assemble — [`lanes/chat-only/incremental-graphics.md`](lanes/chat-only/incremental-graphics.md)

**Step 6 — SFX.** Target (universal): [`presets/youtube/default/sfx.md`](presets/youtube/default/sfx.md).
The plan is universal: `uv run workflows/sfx-plan.py projects/<job>` reads the placed graphics and
writes `hf-graphics/sfx-plan.{json,md}` on the first run (one row per sound: timeline time, library file, source
slice, clip level in dB, track). Only PLACING the rows is per-lane. Built 2026-09-03 from a hand-placed reference intro, validated on two jobs. **Every format (2026-09-04):** any
job whose graphics carry motion events gets its sounds. No short-form preset ships its own
`sfx.json` yet, so `sfx-plan.py` reads the `youtube/default` map for every format — one sound
vocabulary, house-wide — and says so in its report.

- Premiere ✅ `uv run lanes/premiere/place-sfx.py projects/<job> --apply` (`--verify`, `--remove`, `--diff`): imports each file once into an `sfx` bin, provisions A2–A4 with QE `addTracks`, sets the item in/out to the slice, `overwriteClip` at the row's frame, writes Volume > Level, reads everything back; `--diff` reports the creator's hand edits (moved / removed / re-leveled / re-sliced / added) against the plan, which is how they become rules — `premiere-pro` § Step 6
- Resolve ⛔ plan only: the universal plan is written; `AppendToTimeline` with `clipInfo` in/out on an audio track can place the rows, but the level write has no validated API path. Hand-place its rows from `hf-graphics/sfx-plan.md` and say so.
- CapCut ⛔ plan only: the universal plan is written; no audio-clip surface in the bridge. Hand-place its rows from `hf-graphics/sfx-plan.md` and say so.
- chat-only ⛔ plan only: an ffmpeg `amix` of the rows onto the render is the obvious recipe and is not written. Hand-mix or ship without and say so.

**Step 7 — Review.** The creator's, on every lane. The run pauses here.

**Step 8 — Export.** Target (universal): one clip into `projects/<job>/outputs/<job>.final.mp4`,
**verified with ffprobe on the finished file** rather than the app's own reported settings. The
encode numbers are per format: long-form = [`presets/youtube/default/README.md`](presets/youtube/default/README.md)
§ Export; short-form = 1080×1920 H.264 MP4, AAC 48 kHz from the lane's own render (captions are
already on the timeline as a step-5 overlay, so nothing burns after the render). Only the encoder
dialog that reaches them is per-lane. Then
`./finalize.sh <job> --apply`, which is lane-agnostic (it only reads `outputs/`).

- Premiere ✅ scripted on the creator's go: `seq.exportAsMediaDirect` through the bridge with `lanes/premiere/premiere-templates/youtube-2160p-h264-cbr50.epr` (`-2997` variant for 29.97 sequences), the file watched with `lsof` and verified with ffprobe; AME stays banned. The run still pauses at step 7 until he says export — `premiere-pro` § Step 8
- Resolve ✅ the native render queue — [`lanes/resolve/resolve-export.md`](lanes/resolve/resolve-export.md)
- CapCut ✅ `uv run lanes/capcut/capcut-bridge.py export` drives the real dialog and verifies the file
- chat-only — the assemble render IS the deliverable

**Background music (conditional, opt-in).** WHAT (the bed level, the onset rule, the tail, the
opt-in ducking): the `background-music` skill. Only placing the track is per-lane.

- chat-only ✅ `mix-music.sh` on the near-final render (onset + tail built in)
- Premiere ✅ `uv run lanes/premiere/place-music.py projects/<job> --apply`, then `--bounce` for the proof (a music-only WAV bounce, no AME): the newest file in `audio/` onto A5, onset-trimmed, level written through the keyframe, 2 s tail — `premiere-pro` § Background music
- Resolve / CapCut ✋ place the track on the music track (A5 on the `youtube/default` map) by hand: source in-point at the measured onset, −20 dB, 2 s tail fade

## When you hit a ⛔ or a ⚠️

**An undocumented lane is not a blocked lane.** Every step's target is a set of numbers in the
preset, and the numbers are executable by hand in any editor. So:

1. **Do the step by hand** from the preset's spec. A footage move is two keyframes and an ease. A
   graphic is a file to drop on an overlay track.
2. **Say so out loud** in the run report, and record it in `projects/<job>/RUN.md` — same rule as a
   skipped step. A step done by hand on a lane that has no recipe is a normal outcome; a step
   quietly done differently from the preset is not.
3. **If it becomes routine, write the recipe into that app's skill** under its step heading, and
   flip this cell. Never write it into the preset.

**Never substitute another lane's mechanics.** The failure this file exists to prevent is a Resolve
job running the Premiere recipe: an adjustment layer where a color group belongs, Motion Scale 200
on a timeline that already auto-conformed, a premultiplied alpha mov on a lane that wants straight.
Each of those looks plausible and ships broken.

## Adding a lane

Three touchpoints, no new machinery:

1. A column in the matrix above, honest about what is ⛔ on day one.
2. A skill for the app, headed by the same step numbers as every other app skill, carrying only
   HOW.
3. Nothing in any preset. If a preset needs to change to support a new app, the split above has
   been broken somewhere. **One deliberate exception:**
   [`presets/youtube/vox-collage/premiere-lane.md`](presets/youtube/vox-collage/premiere-lane.md)
   is app mechanics kept inside its look's folder on purpose, so that look's inverted stack (grade
   ABOVE the graphics) cannot leak into a default job — 2026-08-31.
