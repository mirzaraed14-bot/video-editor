---
name: premiere-pro
description: "The PRIMARY finishing path — hand the rough cut to Adobe Premiere Pro, where you do the real editing and project work. Rebuilds the rough cut AS separate, trimmable clips on the Premiere timeline — it replays the edit decision list (cuts.json) against the raw footage, NOT a single flattened export — so every cut is a real edit point you can ripple/slip/slide. Triggers: send to premiere, open in premiere, finish in premiere, hand off to premiere, add the rough cut to premiere, edit this in premiere, take it into premiere."
---

# To Premiere — Rough Cut Handoff

**The primary path (2026-07-27) — and the zero-instruction DEFAULT (2026-08-28).** Edits happen inside an editing app, Premiere by default: a bare "do a rough cut" brings the job here after the cut (step 2), and **the chat-only lane is never inferred** from a job's content. Clients finish in their own app (`capcut` / `davinci-resolve`); a client with no app gets asked first. HyperFrames stays the graphics engine feeding this timeline.

**This skill's job is the HANDOFF** — the cut onto a Premiere timeline as real, trimmable edit points, plus the step-3 audio polish and the step-4 grade — not the whole edit. **On a long-form `youtube/default` job the graphics pass (step 5) then runs here as the DEFAULT next step, unprompted.** Captions are short-form only; the final render stays your. **Colour is no longer your by default (2026-08-31):** the grade is step 4, one adjustment layer on V2 under the graphics, scripted, look locked (Autumn-Rec709 as a Creative Look at Intensity 70 / Saturation 115, 2026-09-01).

**The cut is rebuilt AS cuts — not dropped in as one flat clip.** `rough-cut` already decided every edit and saved it as an EDL (`cuts.json`); this skill *replays* that EDL against the **raw footage**, so each kept segment becomes its own V1 clip at the exact edit points the rough cut produced and every boundary is real — rippable, slippable, re-trimmable against the original takes. Importing the flattened `outputs/<job>.mp4` is the *fallback* (§ Fallback).

## 🔒 STEP INDEX: what this lane does at each pipeline step

**This skill carries HOW, never WHAT.** The look, the numbers and the definition of done live in the
format's preset ([`presets/youtube/default/README.md`](../../../presets/youtube/default/README.md) for
long-form): read it for the target, the row below for the mechanics. Cross-lane:
[`LANES.md`](../../../LANES.md).

| # | Step | On this lane (mechanics in the § of the same number below) |
|---|------|--------------|
| 1 | Intake | universal, no Premiere involvement (CLAUDE.md § Pipeline) |
| 2 | Rough cut → replay | ✅ scripted, EDL replayed as separate trimmable clips on V1 |
| 3 | Audio polish | ✅ scripted: `audio-polish.py --apply`, the measured gain + Hard Limiter as clip effects, readback-verified |
| 4 | Color grade | ✅ scripted: `grade-layer` then `grade-lut.py apply`, hands-off → [`lanes/premiere/premiere-grading.md`](../../../lanes/premiere/premiere-grading.md) |
| 5 | Graphics | ✅ scripted: place alpha movs on the graphics track, bake footage moves |
| 6 | SFX | ✅ scripted: `place-sfx.py` puts the universal plan on A2–A4, readback-verified (validated on two reference jobs, 2026-09-03) |
| 7 | Review | ✋ the creator's. The run pauses here. |
| 8 | Export | ✅ scripted on the creator's go: `seq.exportAsMediaDirect` through the bridge with the CBR-50 4K `.epr` (no AME, validated 2026-09-07); by default the run stops at step 7 and you say when |

Captions are a step-5 overlay on the short-form presets, placed by `place-graphics.py` like any
graphic (long-form takes YouTube CC); background music is opt-in and scripted: `lanes/premiere/place-music.py` (§ Background music below).

## When to use

Any trigger phrase above, or a rough cut exists and you want it finished in Premiere. With no rough cut yet, run `rough-cut` **with `RENDER=0` on the splice** — the EDL + canonical transcript generate in ~8 seconds and this skill needs nothing else. **Never render a flat MP4 for a Premiere-finish job** (2026-07-22): [`lanes/premiere/lab-notes.md`](../../../lanes/premiere/lab-notes.md).

## What it needs first — the bridge must be live

This skill drives Premiere through the **`premiere-pro` MCP server** (wired in `.mcp.json`), which does nothing unless Premiere is open with the bridge panel running.

**Engine: `vendor/premiere-mcp/`, a pinned local clone of [hetpatel-11/Adobe_Premiere_Pro_MCP](https://github.com/hetpatel-11/Adobe_Premiere_Pro_MCP), pinned at commit `12684e3` = v1.2.3, 283 tools.** Confirm the running engine IS the pin before trusting a tool: `git -C vendor/premiere-mcp rev-parse --short HEAD` must print `12684e3`, and `get_capabilities` must report 283 tools.

⚠️ **Never install the `premiere-pro-mcp` npm package** — a republish carrying a broken hand-rolled CEP `CSInterface` shim (the all-null bridge failure of 2026-07-09). Update only via deliberate `git pull` + a re-run verification pass + the new hash recorded here, then `npm install && npm run build`, re-apply `lanes/premiere/premiere-templates/cep-bridge-autostart.patch`, re-copy `cep-plugin/`, restart Premiere. **Upstream telemetry is OFF two ways** and must stay off: `"telemetry": false` in `~/.premiere-mcp-bridge/config.json` + `PREMIERE_MCP_TELEMETRY=0` in `.mcp.json` env.1. **MCP tools available?** The `premiere-pro` tools (`mcp__premiere-pro__*`) load at session start; if they are missing, `.mcp.json` was added after this session began — have you restart Claude Code once. **No MCP tools at all (session rooted outside this repo)?** Drive the bridge headless: `node lanes/premiere/premiere-bridge.mjs <tool> '<json>'` calls the same handlers through the file bridge — same panel requirement, no MCP session.
2. **Bridge connected?** Call `ping` first; if it errors or times out the panel isn't running. **"Is Premiere running?" is answered ONLY by `lanes/premiere/premiere-pid.sh`** (`--name` prints the process name), never a hand-typed `pgrep` — the process is year-suffixed (`Adobe Premiere Pro 2026`), so `pgrep -x "Adobe Premiere Pro"` says "not running" with the app on screen (2026-09-02) and `pgrep -f` over-matches crashpad and AdobeIPCBroker. A running app with a dead panel is still unreachable: the pid answers "running", only `ping` answers "drivable". **Try the scripted launch FIRST:** `./lanes/premiere/premiere-up.sh [projects/<job>/premiere/<job>.prproj]` launches Premiere with the CEP autostart patch so the bridge comes up on its own (`--restart` never force-kills — a non-graceful exit reads as a crash, and the crash dialog blocks the panel). Only if that fails, tell you in one line:
   > Open Premiere Pro → **Window → Extensions → MCP Bridge (CEP)** → click **Start Bridge** (temp dir defaults to `/tmp/premiere-mcp-bridge`).

   Then retry `ping`, and don't proceed until it returns ok.

The temp dir in the panel **must match** `PREMIERE_TEMP_DIR` in `.mcp.json` (`/tmp/premiere-mcp-bridge`) — that shared folder *is* the bridge. Protocol is `command-<id>.json`/`response-<id>.json` files, and a panel and a server on different protocols cannot interoperate, so re-copy `cep-plugin/` (to `~/Library/Application Support/Adobe/CEP/extensions/MCPBridgeCEP/`) after any engine bump. The clone is gitignored like `.mcp.json`: restore it with `git clone` + checkout the pinned hash + `npm install && npm run build`.

## Step 2: the EDL replay (the handoff itself)

1. **Resolve the job** — newest folder under `projects/` unless you named one.
2. **Locate the EDL + raw footage.** `projects/<job>/transcript/cuts.json` (or `/tmp/video-editor/<job>/cuts.json` on an older job) plus `projects/<job>/raw/`. **Both must exist**; if the EDL is gone from both spots take the **Fallback** path at the end and tell you why. `cuts.json` is `{ "segments": [ { "clip": …, "start": 1.24, "end": 4.60, "transcript": … } ] }` — segment order = timeline order, and `start`/`end` are seconds **in the raw clip**, exactly what Source Monitor in/out points take.
3. **Preflight** the bridge (`ping`).
4. **Create the project** at `projects/<job>/premiere/<job>.prproj` (`create_project`); if it exists, `open_project` instead of clobbering your in-progress work.
5. **Import the raw clips** (`import_media`) — every distinct `clip` in `cuts.json`, from `projects/<job>/raw/`, never the flattened `outputs/<job>.mp4`. **`import_media` takes `filePath`, a single string — one call per file.**
6. **Build a matching sequence.** `create_sequence` without a preset is broken on 26.x ("Not Enough Parameters"); use `create_sequence_from_clips` with an imported raw clip (or ES `createNewSequenceFromClips(name, [item])` + `app.project.activeSequence = seq`) so it inherits the footage's exact dimensions and framerate, then empty the timeline before the replay. **`remove_selected_clips` returns `available:false`** — clear via ES: loop every track backwards, `track.clips[i].remove(false, false)`. Confirm with `get_sequence_settings`.
7. **Replay the EDL onto V1 — ONE command:**
   ```
   node lanes/premiere/premiere-bridge.mjs replay projects/<job>/transcript/cuts.json <clipName>
   ```
   One ExtendScript for the whole EDL — per segment `setInPoint`/`setOutPoint` on the project item then `overwriteClip` onto V1 — saving when it finishes. **Result:** N separate clips on V1, each a real edit point, with the original heads and tails still in the source.
8. **Verify** with `get_sequence_structure` against the EDL: clip N's `startSeconds` == clip N-1's `endSeconds` (no gaps), each clip's `inPointSeconds`/`outPointSeconds` within one frame of the EDL. Then `save_project` and report the `.prproj` path and the segment count on V1.

Four facts the `replay` command encodes, for any NEW ExtendScript that lays clips from an EDL:

- **Nudge every boundary `+1e-4s`.** `setInPoint`/`setOutPoint` FLOOR at tick conversion, so a frame-grid time that serializes a hair low lands one frame EARLY (measured 2026-07-18). Off-grid EDLs unaffected.
- **The append position is READ BACK** off the last laid clip's `end.seconds` after every overwrite, never accumulated — Premiere quantizes each boundary, so a running sum drifts.
- **Clear the items' in/out afterward** (`clearInPoint(4)`/`clearOutPoint(4)`) or your next source-monitor insert is silently trimmed to the last segment.
- **Only on the MCP `overwrite_from_source` route:** the playhead does NOT auto-advance on 26.3, so each overwrite lands on top of the last (symptom: final duration = the longest segment). That route needs `set_playhead_position` + a `get_playhead_position` read-back before every edit. `replay` does not use it.

## Step 3: audio polish, immediately after the replay verifies

**Run it now (2026-08-28), not at picture lock.** Target: the preset § Audio polish.

```
uv run lanes/premiere/audio-polish.py projects/<job> --apply     # measured gain (voice-gain.py) + limiter on every A1 clip, read back, save
uv run lanes/premiere/audio-polish.py projects/<job> --verify    # exit 1 on any clip off the chain
uv run lanes/premiere/audio-polish.py projects/<job> --apply --gain 15   # a named gain, when you call one
```

Validated 2026-09-03 (35/35 clips on a real job, plus the effect-ADD path on a scratch sequence):

- **No per-section audio work during the cut itself (2026-07-30):** no clip gain or
  level-matching between sections while laying the cut, even when one reads several dB quiet.
  Measuring is fine, acting on the measurement is not.
- **The chain, as clip audio effects on every A1 clip:** the gain from `workflows/voice-gain.py`
  (kept speech to −17 LUFS pre-limiter), then QE `addAudioEffect("Amplify")` +
  `addAudioEffect("Hard Limiter")` and DOM property writes: Amplify Left+Right `v=(dB+96)/144`
  (+10 → 0.73611), Hard Limiter "Maximum Amplitude" `v=(dB+100)/100` (−6 → 0.940; leave Input
  Boost/Look-Ahead/Release at defaults). Read every value back (validated 2026-08-28, 31/31 clips).
  One pass over the timeline; effects stay hand-tweakable.
- **A timeline rebuild (clear + re-replay) discards clip effects.** After ANY re-replay, re-apply the
  chain to every A1 clip and re-verify, or the recut ships unpolished audio silently.
- **ES audio effect params are normalized 0..1 over the slider range (2026-07-30):** Amplify
  Left/Right dB = `v*144 − 96` (range −96..+48), Hard Limiter Maximum Amplitude `v = (dB+100)/100`
  (range −100..0). ⚠️ **Two candidate ranges can agree at one point**, so verify any NEW param by
  writing a NON-zero, off-centre value and reading it back before batch-applying.## Step 4: the grade, BEFORE graphics and underneath them

**Full lane recipe and every trap: [`lanes/premiere/premiere-grading.md`](../../../lanes/premiere/premiere-grading.md)**
— read it first, because three separate failures here all present as "the grade does nothing" and
none of them is visible in a readback. The step is two commands' worth of work:

1. `node lanes/premiere/premiere-bridge.mjs grade-layer`, sequence active: provisions V1/V2/V3/V4,
   mints an adjustment layer **at the frame size it reads off the sequence**, lays one instance on
   **V2** spanning V1, names it `GRADE`, adds Lumetri, saves. Idempotent.
2. `./lanes/premiere/premiere-up.sh --quit` → `uv run lanes/premiere/grade-lut.py apply <job>.graded.prproj`
   (a COPY) → `./lanes/premiere/premiere-up.sh <job>.graded.prproj` → frame delta with the layer
   toggled → quit → swap the copy over the job file. **The file must be CLOSED while the tool writes
   it**, and writing into a copy means a refused open is a file that did not open, not a modal.

**Do it before a single graphic is placed** — the track is free at setup and expensive to insert
later, and the graphics QA measures contrast and glow against the shipping picture. Verify from a
bridge `frame` grab with the layer toggled, never the effect readback, and read every track's mute
state first. ☠️ **Never use the MCP's `apply_lut` tool:** a measured no-op that reports
success, and on a clip that already carries a Lumetri (every GRADE layer does) it writes into the
wrong instance and resets it.

## Step 5: graphics on the timeline (validated 2026-07-18, `your-job`)

**The preset you are on IS the architecture — read it first and treat its track map as authoritative.** Long-form default → [`presets/youtube/default/README.md`](../../../presets/youtube/default/README.md) (V1 footage / V2 grade / V3 graphics / V4 accents, at source resolution); the lane-agnostic Premiere craft is below. **Every preset-specific timeline architecture lives in its own preset folder**, including the vox-collage 4K / adjustment-layers-on-top stack ([`presets/youtube/vox-collage/premiere-lane.md`](../../../presets/youtube/vox-collage/premiere-lane.md)): opt-in by name, its grade placement the inverse of the default's, never read on a default job.

**On a long-form `youtube/default` job the graphics pass is part of the DEFAULT edit**, so after the replay, the audio polish and the grade it runs WITHOUT being asked — plan → build → place → bake → converge, every graphic left hand-editable (separate graphics-track clips + real keyframes):

1. **Plan** with `graphics-plan`, which resolves the preset itself (horizontal long-form → `presets/youtube/default/`; other looks are opt-in BY NAME). Anchor beat times to the refined EDL / canonical transcript word timestamps.
2. **Author comps** in `projects/<job>/hf-graphics/gfx/compositions/` and render with the job's `render.sh` (copied from `presets/youtube/default/reference/fullscreen-render.sh`): **`render.sh <id> alpha`** for overlays (ProRes 4444 straight alpha), **`render.sh <id> full`** for full-screen graphics (opaque mp4, film grain baked; bg-dark adds `STEP_FPS=12`). Comp gotchas and the QA gates belong to the **`graphics-build`** skill, which owns the build; `lanes/chat-only/incremental-graphics.md` is the CHAT-ONLY lane and does not apply here. (Universal comp rule: ALL CSS inline, no `<link>`.)
3. **Place overlays on the GRAPHICS track** with **`uv run lanes/premiere/place-graphics.py projects/<job> --plan --write` then `--apply`** (2026-09-02: owns `hf-graphics/placement.json`, derives rows from the plan + newest render version, places what is missing, swaps stale versions, reads every write back; also `--verify` / `--sync-plan` / `--remove <id>`). Underneath: `importFiles` + `seq.videoTracks[N].overwriteClip(item, startSeconds + 1e-4)` (the tick-floor nudge) + `clip.end = t`. ⚠️ **N is 2 (V3) on the youtube/default map** — read the preset track map, never hardcode from memory. Alpha composites natively, no keying. Two traps, each paid for: **a re-render is a NEW filename + a fresh import** (overwriting a placed path half-stales Premiere's frame index), and **a same-track overwrite then trim leaves a crater** (trimming back does NOT restore the neighbour; re-lay it, then read the track back, which `--verify` does). Program grabs come from the bridge `frame` command, never by fronting the app.
4. **Bake footage moves on V1** (they mirror the comp's motion): the `zoom` command for punch-ins, custom ES for reframe pushes — per-frame keys on Transform Scale H+W and Position (normalized [x,y] arrays), all key times in **source-clip time** (`clip.inPoint.seconds + offset`). A move crossing a V1 edit is split: the first clip pushes in and HOLDS to its tail, the next starts held and releases. **The `zoom` command** takes the preset's numbers straight:
   ```
   node lanes/premiere/premiere-bridge.mjs zoom '{"clip":0,"from":115,"to":100,"frames":18,"ease":"quart","fps":"30000/1001"}'          # opening zoom-out, starts at the in point
   node lanes/premiere/premiere-bridge.mjs zoom '{"clip":8,"from":100,"to":115,"frames":18,"ease":"inout","fps":"30000/1001","at":28.3}' # emphasis push-in, starts at a word
   ```
   `fps` = the sequence's exact rational rate; a wrong rate stretches the ramp. `at` is a **sequence**
   time in seconds (feed it the word timestamp minus ~2 frames); `offset` takes frames past the clip's
   in point instead; omit both and the ramp starts at the in point. Three things it handles that a
   hand-rolled bake gets wrong: **keys BEFORE the ramp survive**, so re-baking a push-in cannot
   destroy an opening zoom-out in the same property track; **it refuses rather than half-writes** when
   a ramp would start before the clip or run past its end; and **Motion and Transform are different
   effects** — the bake is on Transform's `Scale Height` and `Scale Width`, so querying `Motion/Scale`
   reports zero keyframes and reads as "no push-ins here". Verify by reading back: on the 18-frame `inout`
   push-in frame 9 must read **107.50**, frame 4 **100.66** and frame 14 **114.34** (a linear bake reads
   107.50 at frame 9 too, so frame 9 alone does not discriminate); on the 18-frame `quart` zoom-out
   frame 9 reads **100.94**. The numbers are the preset's
   ([`presets/youtube/default/README.md`](../../../presets/youtube/default/README.md) § Emphasis push-in).
5. **QA every graphic from the real program render**: `node lanes/premiere/premiere-bridge.mjs frame '{"time":<sec>,"out":"/abs/path-no-ext"}'` — full composite (keyframes, alpha overlays, unsaved state), zero AME. Iterate: edit comp → `VER=<v> render.sh <id>` (new filename, never overwrite a placed path) → `uv run lanes/premiere/place-graphics.py projects/<job> --plan --write` (the newest version wins) → `… --apply` (swaps the stale clip) → re-grab. **A watchable preview goes through Premiere itself, NEVER AME (2026-07-20)**, § Step 8.
6. **Converge with `edit-review` — step 5c, part of the graphics step, not an optional extra.** The build's first-pass QA is the builder grading itself; this is fresh eyes. Run the loop until a full round comes back clean, fixing part-by-part, then move to step 6. **Objective defects must never reach your review (step 7)** — that pass is taste, and only taste.

### Keyframe & effect laws (hard-won, lane-agnostic, do not relearn)

These hold on every Premiere job regardless of preset; none is a look choice.

- Clip keyframes live in **source time**: `inPoint + offset`. Synthetic media (adjustment layers) has inPoint ≈ 3600 s, and it RISES when the head is trimmed.
- **Baked keys are the standard** for any scripted motion: one key per frame (or per 2) sampled off the curve, all linear. Scripted eases are broken/limited; bake the shape.
- Point params (Position/Anchor) are **normalized** (0.5,0.5 = center; for offsets divide px by frame dims); scalars read/write in display units. Always read back.
- Effects apply via QE: `qe.project.getVideoEffectByName` + `qclip.addVideoEffect`; **walk `getItemAt(i)` for `type === "Clip"`** — gaps are items, so a clip that doesn't start at 0 is not item 0.
- **Adjustment layers: intrinsic Motion is inert on the image**, it moves only the layer's bounds (caught 2026-07-22). Image moves = the **Transform effect**; set Scale Height AND Width explicitly (the uniform toggle is untrusted). Prove any new transform assumption with an exaggerated offset + frame grab BEFORE baking hundreds of keys. (Minting the layer: [`lanes/premiere/premiere-grading.md`](../../../lanes/premiere/premiere-grading.md) § 1.)
- **Rendered preview files DROP AI-masked layers (Premiere 26.x)** — green-bar playback lies, yellow is truth. Delete render files (`qe.project.deletePreviewFiles("228CDA18-3625-4d2d-951E-348879E4ED93")`) and never tick "Use Previews" on export; real renders composite correctly.

### Graphics clip lifecycle (also lane-agnostic)

- **Place** — `import_media`, then ES `videoTracks[n].overwriteClip(item, edlTime)`; trim the renderer's +1 pad frame via `c.end = t`. Graphics land ON the EDL cut times (frame-snapped splice ⇒ EDL == timeline).

- **Iterate** — edit the comp → re-render the ONE affected part → `refresh_media` (same duration = in-place, keys/effects survive; duration changed = refresh twice in separate calls, then re-place). Never re-render the whole family for one tweak. **If the re-render changed CONTENT or duration, version the FILENAME (`<id>-b.mov`) and import fresh instead of overwriting the placed path (2026-08-01)** — a same-path rewrite half-stales Premiere's frame index and specific frames come back transparent.- **Anchor beats to MEASURED audio, not raw WhisperX** — word starts run ~50-100 ms late; scan a 5 ms RMS envelope of the base cut around the WhisperX time and land on the acoustic attack, frame-snapped.
- **The editor re-trims between sessions** — read the LIVE timeline before computing anything against it, never docs or memory for clip spans.
- **Re-timing or swapping a graphic orphans its SFX silently** — SFX are aligned to graphic beats, so check the SFX tracks in that window and reconcile affected cues using the step-6 incremental revision procedure, preserving approved unaffected sound design (which is why SFX is step 6, after the graphics defect loop).
- **Generated b-roll:** `videoTracks[n].overwriteClip` + `audioTracks[n].overwriteClip` at the same time so the voice on A1 stays untouched. Track depends on the preset's map and whether the clip should take the grade (above the grade layer = ungraded, usually right for a generated clip).

Three engine facts a graphics pass needs: **⚠ `export_frame`'s TIME argument is broken** (QE reads the string as a FRAMES timecode, so `time: 18` exports frame 18) — always grab through the bridge `frame` command, which converts seconds off the sequence fps; **`remove_effect` is absent** and no-arg QE `removeEffects` returns true while removing nothing, so strip effects with QE `item.getComponentAt(i).remove`, matching `comp.name` and iterating indices BACKWARDS; and **`add_keyframe` writes raw SOURCE time**, so keep computing `inPoint + offset` (the `zoom` command does). Other per-tool arg quirks: read the zod schema in `vendor/premiere-mcp/src/tools/index.ts`, never `--desc`; the measured status map is in the archive (§ Notes).

## Step 6: SFX on the timeline (built 2026-09-03; placed and readback-verified on two reference jobs (120/120 and 122/122 rows, the second reviewed and hand-tuned by ear the same day))

WHAT: [`presets/youtube/default/sfx.md`](../../../presets/youtube/default/sfx.md). The plan is
universal and already written (`uv run workflows/sfx-plan.py projects/<job>` →
`hf-graphics/sfx-plan.{json,md}`); this lane only places it.

```
uv run lanes/premiere/place-sfx.py projects/<job> --apply     # place, set levels, read back, save
uv run lanes/premiere/place-sfx.py projects/<job> --verify    # readback vs the plan (exit 1 on drift)
uv run lanes/premiere/place-sfx.py projects/<job> --diff      # the creator's hand edits vs the plan (MOVED / REMOVED / LEVEL / SLICE / ADDED): the input for the next rule
uv run lanes/premiere/place-sfx.py projects/<job> --remove    # clear ALL library SFX clips, only for a deliberate full replacement
```

**Graphics revisions:** follow [`sfx.md`](../../../presets/youtube/default/sfx.md)'s incremental revision procedure. Diff first; fold hand edits upstream; re-run the plan (a bare re-run rewrites it and names the changed IDs, `--candidate` parks a rescore to merge by hand); remove exact stale affected clips; apply and verify zero missing/extra/drifting cues. `--remove` clears the whole library score and is not the incremental path.

**After the creator's hand pass, `--diff` runs BEFORE any re-place:** `--apply` overwrites hand
edits, and the diff is how they become the next rules in `sfx.json`.

Mechanics, each read back before it is believed: the library file is imported ONCE into an `sfx` bin
and found by media path afterwards; audio tracks come from QE
`addTracks(0, 0, 1, 1, numAudioTracks, 0, 0)` (appends, nothing placed moves); the slice is the
project item's in/out (`setInPoint(t, 4)`) + `audioTracks[n].overwriteClip(item, at + 1e-4)` (the
replay's floor nudge), then in/out cleared; the level is the clip's Volume > Level,
`v = 10^((dB − 15) / 20)` (0 dB = 0.17783, −12 = 0.04467, +5 = 0.31623). A run stops on the first
readback mismatch, and a timeline rebuild drops these clips like the A1 chain: re-run `--apply`.

### Background music (the opt-in pass, after SFX)

The WHAT is the `background-music` skill; on this lane the bed goes on **A5** (the `music` role) by
`place-music.py`, validated on your-job 2026-09-04 (remove → apply → verify → bounce, twice):

```bash
uv run lanes/premiere/place-music.py projects/<job> --apply     # newest audio/ track → A5 at 0, source in at the reviewed sustained entrance, the house bed level written through the keyframe, 2s tail, read back, saved
uv run lanes/premiere/place-music.py projects/<job> --bounce    # music-only WAV via exportAsMediaDirect (no AME): LUFS + "plays from the first frame"
uv run lanes/premiere/place-music.py projects/<job> --verify    # readback vs the numbers
uv run lanes/premiere/place-music.py projects/<job> --remove    # off the track (before a re-place or a level change)
```

The bed's Level uses the same encoding as SFX and is time-varying (the 2 s tail), so it is written
through `setValueAtKey` on the first key, never `setValue` — the readback-lies trap in
[`lanes/premiere/lab-notes.md`](../../../lanes/premiere/lab-notes.md).

## Step 8: export (on the creator's go — scripted, never AME)

**Where the automated work ends by default:** the graphics pass and its defect loop finish at *placed +
verified*, the run pauses at step 7, and the export runs when you say so (you did on your-job,
2026-09-07). **AME is banned** (2026-07-20) for everything — full exports, QA bounces, audio checks
alike — and `export_sequence` queues into it, so the ONLY render route is
`sequence.exportAsMediaDirect(outPath, presetPath, workAreaType)` via `execute_extendscript`: synchronous,
in-Premiere, no AME. `workAreaType` 0 = the whole sequence, 1 = in/out (clear the marks first).

**THE LOCK (the WHAT is the preset README § Export; measured against YouTube's published 2160p SDR spec
2026-09-07 — High profile, 4:2:0, 35–45 Mbps at 24–30 fps, AAC 48 kHz):**
`lanes/premiere/premiere-templates/youtube-2160p-h264-cbr50.epr` — 3840×2160, H.264 High, **CBR** with
target = max = 50 Mbps (`ADBEVideoBitrateEncoding` 0; VideoToolbox VBR treats the target as a ceiling and
landed at 17.6 Mbps once; 50 is the measured VMAF ceiling, 65 scores identically), AAC 320 kbps stereo
(Premiere's AAC menu tops out there; YouTube re-encodes audio anyway), BT.709, moov at the front. Use
`youtube-2160p-h264-cbr50-2997.epr` on a 29.97 sequence (the exporter matched the sequence rate even from the
30.00 file, but say it explicitly). Max Render Quality is off and moot: GPU scaling is already maximum
quality, it only helps CPU-rendered effects.

```bash
# from the repo root, the job's sequence active; OUT + EPR absolute
node lanes/premiere/premiere-bridge.mjs execute_extendscript '{"script":"(function{var s=app.project.activeSequence;s.setInPoint(0);s.setOutPoint(0);return String(s.exportAsMediaDirect(\"<OUT>\", \"<EPR>\", 0));})"}'
```

**The bridge call times out at 45 s while Premiere keeps writing** — that is normal. Watch the FILE: `lsof <out>`
closed + size > 0 = done (a 13:37 4K master took ~17 min and 4.8 GB); never ffprobe mid-write (bogus
duration). Then verify the FILE with ffprobe (resolution, `30000/1001`, High, ~50 Mbps, `yuv420p`, bt709, AAC 48k)
and `./finalize.sh <job> --apply` promotes it + drops the `~/Downloads` copy. VMAF measurements and the
`.epr` patching recipe: the engineering archive.

## Fallback — flat clip import

Only when the EDL is unavailable (old job, `cuts.json` lost from both spots) or you ask for "just the flat cut as a reference":

1. `import_media` the `outputs/<job>.mp4`.
2. `create_sequence_from_clips` with it — the sequence inherits its dimensions/framerate AND the clip lands on V1, so no `add_to_timeline` is needed.
3. Save and tell you it's the **flattened** cut: the individual edit points aren't recoverable, so re-trims mean razoring by eye. For real edit points, re-run `rough-cut` to persist a fresh `cuts.json` and hand off again.

## Notes
- **When you references live timeline state — "the in and out points I set", "the highlighted clip", "what I selected", "at the playhead" — QUERY PREMIERE FIRST, before any interpretation (2026-08-28, you had to demand it).** Your marks and selection are one call away: `seq.getInPoint`/`getOutPoint`, `clip.isSelected` across tracks, `get_playhead_position`. Inferring the target from conversation once got a wrong segment diagnosed AND deleted. Your timeline state IS the instruction. Clear marks (`setInPoint(0)`/`setOutPoint(0)`) after acting on them.
- **Colour is NOT the creator's any more (2026-08-31)** — the grade is step 4. The automated work ends at the render and the export: § Step 8.
- Keep the HANDOFF surgical: import raw + matching sequence + the EDL replayed onto V1.
- **Audio rides along.** `overwrite_from_source` lays the clip's audio onto A1 in lockstep, and segments stay A/V-synced because in/out points apply to the source clip as a whole.
- **Section color-coding (multi-section jobs only): set the project item's label BEFORE the replay** (`item.setColorLabel(idx)`, 0–15) — timeline clips stamp the label at insert time, so relabelling later never recolors laid clips. **Label NAMES lie about rendered color (2026-07-31)**: measure a candidate against the sections already laid with one throwaway clip, never pick by name. The 16 names and the
- **Job projects live at `projects/<job>/premiere/<job>.prproj`, always.** Never let one be born from Premiere's own save dialog — its default is the rotating Auto-Save folder, which Premiere prunes (two job projects were rescued from there 2026-07-17). Superseded drafts go in `premiere/archive/`. A project in the WRONG job folder relocates in ONE call: ES `app.project.save; app.project.saveAs(newPath)` — verified 2026-07-29 with the project open and a live timeline; delete the stale copy afterward. The DOM `saveAs` is NOT the untested `save_project_as` MCP tool.
- **Adjustment layers: scripting can't CONSTRUCT one, it MINTS one from the tracked donor project (solved 2026-07-22), at the SEQUENCE'S size, always (2026-09-02).** The mechanic lives in [`lanes/premiere/premiere-grading.md`](../../../lanes/premiere/premiere-grading.md) § 1; the bridge `grade-layer` command runs it for you.
- `.prfpset` presets and curve-handle geometry are NOT scriptable — bake instead (§ Step 5 keyframe laws). The MCP otherwise exposes the full DOM/QE surface; `get_project_info` discovers state. The measured per-tool status map on the pinned clone — what works, what is broken or absent, what is untested — is in the the engineering archive.
