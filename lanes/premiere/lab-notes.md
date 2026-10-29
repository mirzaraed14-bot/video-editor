# Premiere lane: lab notes

**The locks that are true only on this lane.** Moved out of the root `CLAUDE.md` Lab Notes on 2026-09-03 so the universal locks read as universal: every bullet here is Premiere mechanics, none of it is a look decision (those stay in the presets) and none of it is pipeline law (that stays in `CLAUDE.md`).

- **Never render the flat cut on this lane; the audio polish is step 3, right after the replay.** `RENDER=0 splice.sh` → `premiere-bridge.mjs replay` (time-to-timeline is the metric, transcription the only slow step). No gain, no level-matching during the cut. Then `uv run lanes/premiere/audio-polish.py projects/<job> --apply` (measured gain + Hard Limiter −6 dBFS as clip effects on every A1 clip, readback-verified); a re-replay discards clip effects, re-apply before saving. Owner: `premiere-pro` skill § Step 3.
- **The lane = the `premiere-pro` skill driving the pinned `vendor/premiere-mcp/` engine (v1.2.3) through the CEP bridge panel**, or headless via `lanes/premiere/premiere-bridge.mjs` (`replay` / `zoom` / `frame` / `grade-layer`, no MCP session needed). Graphics on the timeline validated 2026-07-18; AME banned (exportAsMediaDirect via ES if a bounce is truly needed); `zoom` takes `at` (sequence time) or `offset` (frames) and clears only from the ramp start. Read-back-after-write, always. Wiring and pin: the skill.
- **The grade layer goes UNDER the graphics, on the track the preset's map reserves for it** (youtube/default: V2, [`presets/youtube/default/README.md`](../../presets/youtube/default/README.md) § Timeline architecture; vox-collage inverts it and is opt-in by name). `node lanes/premiere/premiere-bridge.mjs grade-layer` mints the layer at the sequence's size and lays it; retrofitting under placed graphics is QE `addTracks(1, 1, 0, 0, 0, 0, 0)` (inserts a track, nothing re-laid); never move graphics by re-`overwriteClip`. Look locked to Autumn-Rec709 at 70/115, no correction step. Owner: [`premiere-grading.md`](premiere-grading.md).
- **`.lookparams` pid 4 is the explicit empty sentinel, never self-closing** (a self-closing pid 4 = "project appears to be damaged"); `grade-lut.py selfcheck` proves every params file offline and `apply` refuses a failing one. **Under a locked screen the bridge, replay, polish, grade and frame grabs all work; Premiere's UI does not**: `lanes/premiere/premiere-dismiss.sh --check` (exit 2 = invisible modal) then bare to dismiss; after ANY refused open, nothing else opens until it reports zero. Owner: `premiere-grading.md`.
- **Lumetri's LUT is unreachable through scripting and is written into the `.prproj` by `grade-lut.py`.** The MCP `apply_lut` is a measured no-op and UNSAFE on a grade layer; writing the Blob through ES poisons the instance; `BinaryHash` is validated and silently discards a wrong payload; the LUT goes in Creative > Look; params are version-bound. Three failures all read as "the grade does nothing" and none shows in a readback: verify from a program render with the layer toggled, on a track you confirmed is unmuted. Owner: `premiere-grading.md`.
- **YouTube export = CBR 50, not VBR.** VideoToolbox VBR treats the target as a ceiling (a 27-min 4K landed at 17.6 Mbps); set `ADBEVideoBitrateEncoding` to 0 in the `.epr`; 50 Mbps is the measured VMAF ceiling. Working preset, tracked and shipped: [`premiere-templates/youtube-2160p-h264-cbr50.epr`](premiere-templates/youtube-2160p-h264-cbr50.epr) (3840×2160, CBR, target = max = 50 Mbps, AAC 320k). Poll `lsof` for completion.
- **Project files live at `projects/<job>/premiere/<job>.prproj`, never Premiere's save-dialog default (the pruned Auto-Save folder).** A relocation leaves its Auto-Saves in the old folder; sweep them to `premiere/archive/` and verify the move via `app.project.path`, not the filesystem.
- **Drive the editor in the background; never front it.** `./workflows/window-grab.sh <App> <out.png>` captures a window's own buffer; most verification is a readback. The one exception is a PLANNED capture (`workflows/screen-record.sh`, a `capture` cell in the graphics plan): production footage of the timeline filling, not a verification frame, fronted for the take and said so in the report. Timeline colour labels are stamped from the project item at insert time and not scriptable per clip: label the item, then lay. Launch = `./lanes/premiere/premiere-up.sh [project]` with the CEP autostart patch applied by `apply-autostart-patch.py` (re-run after any engine re-clone).
- **Windows: verify a caption track (or any on-screen state) with a PrintWindow grab (2026-09-25).** `window-grab.sh` is macOS-only, and QE `exportFramePNG` throws here. But user32 `PrintWindow(hwnd, hdc, 2)` (PW_RENDERFULLCONTENT) on Premiere's main window captures the GPU Program monitor too, without fronting it. Park the playhead with `seq.setPlayerPosition(ticks)` first. This closes the "no caption READ API" gap: the track (C1) and the rendered caption are both visible. The panels' timecode readouts do NOT repaint in a background grab (they stay stale); the picture and caption do, so judge by the picture. Script: `powershell -ExecutionPolicy Bypass -File lanes/premiere/window-grab.ps1 -Out <png>` (the machine policy blocks unsigned scripts; Bypass is per-call only).
- **Never escalate a stuck quit to `kill` / `kill -9`.** Premiere logs any non-graceful exit as a CRASH: the next launch opens on an error-report modal that blocks the CEP panel, so bridge autostart silently fails, and post-kill timeline state comes back subtly wrong even after a `save_project` that returned success. Save through the bridge, quit gracefully (ExtendScript `app.quit`, not an AppleEvent), then wait on the pid — and if it still will not quit, STOP and hand the app back to be quit by hand. `premiere-up.sh --restart` already refuses to escalate and exits with that instruction; keep it that way.
- **OBS recordings carry two identical AAC tracks and Premiere silently refuses the file.** Remux losslessly first (`ffmpeg -i raw.mp4 -map 0:v:0 -map 0:a:0 -c copy -movflags +faststart out.mp4`); duration is unchanged so an EDL still applies. Clip deletion IS scriptable: `moveBin` into a fresh bin, then `deleteBin`.
- **yt-dlp downloads headed into Premiere must be H.264:** `-f "bv*[vcodec^=avc1]+ba[ext=m4a]/b[vcodec^=avc1]"` (Premiere cannot import AV1).
- **Generated b-roll lands with `videoTracks[n].overwriteClip` + `audioTracks[n].overwriteClip` at the same nudged time** (V3 + A2 under the grade map, so it stays ungraded; drop on V1 to grade it). Motion Scale 200 is a vox-4K habit, never ported elsewhere. `execute_extendscript` returns "undefined" for bare statements: wrap in an IIFE with `return`.
- **Step-6 SFX placement is `place-sfx.py` (validated 2026-09-03), and after the creator's hand pass `--diff` runs BEFORE any re-place** (`--apply` overwrites hand edits; the diff is how they become rules). Mechanics (QE `addTracks`, the slice in/out that must be CLEARED, the Level encoding, the multi-line bridge log): `premiere-pro` § Step 6.
- **A render longer than its slot must be trimmed BEFORE it is laid (2026-09-04).** `overwriteClip` then `clip.end = t` eats the head of the next clip on the track and the trim does not give it back (g15 lost 2 frames to a longer g14 swap). `place-graphics.py` now sets the item's in/out to the row's span before `overwriteClip`; any hand ES placement does the same.
- **The music bed is `place-music.py`: selected `audio/` file → A5, sustained-entrance trim, −20 dB flat bed, 2s tail (current default, 2026-09-12), `--bounce` for the proof.** Explicit user levels override the default. `workflows/music-onset.py` supplies a candidate; listen/inspect the entrance and use the source-in override when needed. Sparse opening transients are not the song starting.
- **A time-varying music Level is written through `setValueAtKey` on the first key, never `setValue`.** Historical proof below used −18 dB; the current default is −20 dB. A static `setValue` + keys reads back −18 everywhere (getValue, getValueAtTime, getValueAtKey) yet PLAYS at ≈ −64 (Effect Controls showed −64 while playing, −18 paused) — that bad first placement is why the bed was first called silent; rewritten through the first key, −18 was kept. Proof is a music-only bounce via `exportAsMediaDirect` with the system `Wave48mono24.epr` (tracks 0–3 `setMute(1)`, numeric, then `setMute(0)`): −18 read −35.1 LUFS, 14 LU under the −21.1 LUFS mix. Place, then verify by bounce, not readback. Encoding, tail keys and mechanics: `premiere-pro` § Background music.
- **The music clip's source in-point is its verified sustained entrance, not 0 or the first `silence_end`.** Early isolated hits fooled the old silence-crossing rule on your-job. Use the current background-music skill's sustained-onset method, frame-snap the chosen in-point, and prove it in playback. Fade keys remain SOURCE time: `inPoint + (end − 2.0)`.
- **Every placement row is FRAME-SNAPPED before it reaches Premiere (2026-09-07).** Premiere floors seconds to ticks TWICE on a placement (the item out-point `END − START` and the end pin), so a row whose seconds sit a hair under the frame tick (a plan end written `16.783` for the cut at 16.78343, a builder end rounded to 4 decimals) lands one frame short of its V1 cut and the outgoing shot flashes for a frame (g4 g5 g17 g21 on your-job, proven on a program grab of frame 502). `place-graphics.py` `snap` now rounds every derived start/end to the nearest frame (5 decimals) so the nudge always lands above the tick; a stale `placement.json` keeps its old values within 1.5 frames, so after the fix re-derive from scratch and `--remove` + `--apply` the affected ids.
- **The bridge `frame` command now absolutizes a relative `out` against the CALLER's cwd, creates the parent folder, and fails if the PNG did not land (2026-09-08).** It used to hand the raw string to Premiere, whose cwd is its own app folder, and report success either way: 184 grabs landed nowhere on the first review-evidence pass (2026-09-07). `<out>.png` is the promised filename, so a trailing `.png` is stripped.
- **A source larger than the sequence lands at Motion Scale 100 on `overwriteClip`, i.e. CENTER-CROPPED (2026-09-07, your-job: 4K sections on the 1080 intro sequence).** Premiere's scale-to-frame-size preference does not apply to scripted placement, and the readback says 100 either way, so prove it from a program frame against the fitted raw (center-crop matched at Δ0.4, fit at Δ60). Fix per clip: Motion > Scale = sequence width / source width (3840 → 50.0; a 3836-wide capture → 50.06, or a 1 px bar shows each side). Multi-section audio polish is scoped with `audio-polish.py <section> --apply --range FROM TO` (each take shoots at its own level).
- **Converting a placed 1080 sequence to 4K is one ES pass (2026-09-07, your-job):** `seq.setSettings` with videoFrameWidth/Height 3840/2160 takes effect on a populated timeline; every already-placed clip keeps Motion Scale 100 = its native pixels, so set 200 on the 1080 footage, the placeholder AND the GRADE adjustment layer (its Motion scales the layer's BOUNDS, which is exactly the coverage needed — verify by toggling the layer and reading the corners), 100 on true-4K sources (100.1 on a 3836-wide capture). Graphics are re-rendered at 4K as a new version and swapped by `place-graphics.py`, never scaled: a comp keeps its 1080 layout on a `scale(2)` stage inside a 3840x2160 root, NEVER `#root{zoom:2}` (the mechanism and the measured failure: `graphics-build` § render gotchas), 5–55 s per render.
- **A MONO clip's Amplify has ONE `Gain` slider (no Left/Right), same −96..+48 range, and it plays under Premiere's −3 dB centre pan law on a stereo master (2026-09-07, your-job's three camera sections).** `audio-polish.py` writes `Gain` at gain+3 for mono clips so the master hears the measured level; the proof is a voice-only bounce (`exportAsMediaDirect` with in/out, other tracks muted): stereo intro −21.0 LUFS at the −6 ceiling, mono section −21.3 LUFS with peaks −8.9 in the mono WAV (−5.9 on the master). A verify script that assumes Left/Right dies on the first mono clip with a bare CEP `evalScript` failure, not a property error.
- **The export can be scripted: `seq.exportAsMediaDirect(out, epr, 0)` through the bridge renders in-Premiere with no AME (2026-09-07, your-job 4K, you asked for it).** The bridge call times out at 45 s while Premiere keeps writing; watch the file with `lsof` (closed + non-zero = done), never ffprobe mid-write. The locked `youtube-2160p-h264-cbr50.epr` carries `ADBEVideoFPS` = 30.00, yet a 29.97 sequence came out 30000/1001 (the exporter matched the sequence rate); `youtube-2160p-h264-cbr50-2997.epr` says 29.97 explicitly for that case. Measured against YouTube's published spec (High profile, 4:2:0, 35–45 Mbps at 2160p30, AAC 384k): CBR 50 sits above the range at the VMAF ceiling, Premiere's AAC menu tops out at 320k, and Max Render Quality is moot with GPU scaling.
- **`./prune.sh --apply` deletes graphics that live Premiere timelines use (found 2026-10-26).** Its `hf-*/**/renders` pass treats the render folder as cache, but on this lane those `.mov`s ARE the placed clips: the dry run listed 130.8 GB, of which ~130 GB was referenced by the ABW8/ABW10 auto-saves (World Stops 34 GB while it was being edited). Workaround until prune.sh checks references: never `--apply` on a Premiere machine; clear by the per-file manifests from a reference check (`projects/_storage-audit-2026-10-26/`), which reads every `.prproj` / `.aep` for paths under `projects/` (gzip XML; `<FilePath>` / `<ActualMediaFilePath>`).
- **A timeline change is bracketed OFFLINE from the auto-saves (2026-09-10, your-job).** A `.prproj` is gzip XML; `<Start>`/`<End>` ticks ÷ 8,475,667,200 = frames at 29.97 (254016000000 ticks/s × 1001/30000), so diffing those values between two auto-saves says WHEN a cut moved without opening anything. A 10-frame drag of a V1 clip (source in/out unchanged, the previous clip's tail overwritten, a 10-frame hole left behind) landed between two auto-saves while the only commands running were file reads, i.e. from the Premiere UI; the next placer save then persisted it, because `--verify` reads the graphics rows only, never V1. The repair primitives: `trackItem.move(seconds)` is a RELATIVE shift (the vendor passes a plain number) and linked audio follows; `clip.end = t` extends a clip (speed stays 1) but the DOM's `outPoint` reads STALE afterwards, so the proof is a voice-only bounce over in/out (`exportAsMediaDirect(wav, Wave48mono24.epr, 1)`) cross-correlated against the raw source, never the readback; `seq.clearInPoint` does not exist, `setInPoint(-400000)` restores the unset state.

- **Fractional-fps razor calls require frame proof (your-job, 2026-09-11).** The vendor `razor_timeline_at_time` formats timecode from fractional fps and cut three frames late at 23.976 while reporting success. Compute integer frame indices and nominal-24 non-drop timecode for 24000/1001, as the bridge `frame` command does; use the equivalent correct timebase for other rates. Verify actual V1/A1 start/end AND source in/out against the EDL after the cut. A continuous split shares one timeline boundary and one source boundary; never accept the returned requested timestamp as proof.
- **A version swap is finished only after native proof and save.** Use a new render filename, reconcile the placed clip's media path, source in/out and timeline bounds, and inspect the changed frame plus both joins with track state verified. Do not claim a render fix is saved merely because the new MP4 exists or the placement JSON points to it; prove the live item and `app.project.path`, then save. Unused project-bin items are not themselves phantom timeline clips.

- **Windows + Premiere 25.0 (2026-09-13, marvels-wolverine-reviews; a fix session is queued, until then these are the workarounds).** `app.newProject` returns false on a backslash path: forward slashes for `newProject`, backslashes for `exportAsMediaDirect` output paths. QE `exportFramePNG` throws "Unknown error": a program-frame proof is `exportAsMediaDirect` with the system PNG preset over a one-frame in/out (the `review-frames.py` bridge grab is broken here; evidence is composited from the EDL + placed renders, per-layer ffmpeg extract + PIL stack, never the 2-input ffmpeg overlay, which dropped overlays). The `grade-layer` donor and Look params are Premiere 26 (project format v45): `importSequences` returns true and imports nothing on 25.0, so step 4 is manual (adjustment layer on V2 → Lumetri → Creative > Look = `assets/luts/rec709/Autumn-Rec709.cube`, Intensity 70, Saturation 115) or update to 26. **Audio items are floored to a 29.97 grid** even on a 59.94 sequence (up to 33 ms, beyond `place-sfx.py`'s 1.5-frame tolerance): snap the plan's slice edges to 1001/30000 first (`sfx-plan.unsnapped.json` keeps the original). Replay and bridge calls time out at 45 s while still completing: verify by readback, never retry blind. `polish-boundaries.py` wrote a literal `/tmp` (→ `E:\tmp`) while `splice.sh` reads Git Bash `/tmp` (AppData\Local\Temp); **fixed 2026-09-19**: it resolves `cygpath -w /tmp`, and its stale-EDL guard now accepts splice's own byte-identical write (the snap took 9.8 s here, past its 5 s slack). `voice-gain.py` builds one `aselect` with a `between()` per segment and ffmpeg 9.0.1 fails with "Cannot allocate memory" past ~200 segments: measure from a concatenated kept-speech WAV + `ebur128` instead. **Run every Python that reads comps or the plan with `PYTHONUTF8=1`** (`graphics-qa.py` decodes `×` as an em dash through cp1252 and false-flags it; `place-graphics.py --sync-plan` double-encoded 64 strings, `·` → `Â·`). hyperframes caps render fps at 240, so at 59.94 the 8× motion-blur lock is impossible: `MBLUR_SS=4 MBLUR_SHUTTER=3`. Preset frame counts written at 29.97 double at 59.94 (push-ins 36 frames for the locked 0.6 s).

## 2026-09-16 · `replay` APPENDS, and its 45 s timeout is a lie (gta-san-andreas-hot-coffee)

**The bug, in the order it bites:**

1. `premiere-bridge.mjs replay` **does not clear the sequence** — it reads the append position off
   the last laid clip and overwrites from there. On an EMPTY sequence that is invisible. On a
   sequence that already holds a cut, it stacks a second copy after the first.
2. Its ExtendScript call **times out client-side at 45 s while Premiere keeps executing.** The first
   replay of 258 segments onto an empty timeline took ~34 s and returned cleanly. The second, onto a
   populated timeline, ran past 45 s; the bridge reported
   `ExtendScript execution timed out after 45000ms` and Premiere **finished the work anyway**.
3. So the timeout reads like a failure and invites a retry — and every retry appends another full
   copy. Two "failed" replays left `Sequence 12` at **2382.5 s (39:42) instead of 795 s (13:15)**:
   three stacked copies of the same cut.

**Rules:**
- **A timed-out replay is NOT a failed replay.** Before retrying, wait for the bridge to answer
  `ping` again, then read the sequence duration. If it grew, the replay landed — do not re-run.
- **Clear the sequence before every replay after the first.** The skill's § Step 2 already says to
  empty the timeline before the replay; that step is mandatory, not a first-run convenience.
- While Premiere is mid-script the bridge returns `bridge_unavailable` for everything, including
  `ping`. That is a BUSY signal, not a dead panel — do not send anyone to Window → Extensions.
- **2026-09-23, Windows + 25.0 (monetized-before-gta6): the same trap with a THIRD error text.** A 148-segment
  replay, sent seconds after importing a 9.6 GB clip, failed after 6 s with `MCP Bridge is not running … Do not
  retry until the panel says Connected`; the next `ping` timed out; the heartbeat file was still fresh. Premiere
  had executed the whole script: 296 clips (148 V1 + 148 A1), all within a frame of the EDL. Any failure text from
  `replay` (timeout, not running, unavailable) → ping until it answers, count clips, never re-run blind.

## 2026-09-23 · Windows + 25.0: modals, paths and still clips (monetized-before-gta6 overlays)

- **A native modal blocks the bridge, and the bridge reports it as "MCP Bridge is not running".** Seen twice: the
  FCP XML export opens a **Translation Report** dialog, and a failed import opens **File Import Failure**. Check
  Premiere's windows (EnumWindows on its pid); the dialogs are class `#32770` and close with `WM_CLOSE` sent to that
  handle only. Their text is custom-drawn, so read it with `PrintWindow` into a PNG. (`premiere-dismiss.sh` is macOS-only.)
- **The bridge strips one level of backslash escaping.** A path written `E:\\Claude...` in the script reaches
  ExtendScript as `E:\Claude` → `E:Claude`, and `importFiles` fails behind a File Import Failure modal. **Use forward
  slashes for `importFiles`**; for `exportAsMediaDirect` write four backslashes in the script source.
- **`projectItem.changeMediaPath()` fails with a File Import Failure modal** for a PNG that `importFiles` accepts.
  Relinking is out: give a rebuilt file a new name and import it. Imported files are also **locked on disk**.
- **A still laid with in/out lands one frame short** (out-point quantization). **`trackItem.end = <Time>` is writable
  and exact**: pin the end to the slot's own `end.ticks` after every overwrite.
- **Helper functions declared before the IIFE make the bridge return "undefined"** (the script still runs). Put
  everything inside one wrapper that returns the result.
- **QE `getSequenceAt()` scan missed the active sequence**; `qe.project.getActiveSequence()` works.
- **The Drop Shadow effect is nearly invisible on a dark background**: at 100 % opacity it darkened a luma-27 matte to
  23. Bake shadows into the asset instead.
- **Frame proof on Windows**: `exportAsMediaDirect(out, ".../systempresets/3F3F3F3F_504E4720/PNG Sequence (Match
  Source).epr", 1)` over a one-frame sequence in/out, then restore in/out. It writes `<name>0.png`.
- Recovery is a timeline edit on the creator's live project, so it can be blocked by the session's
  permission mode (it was here: `execute_extendscript`, `select_all_clips` and even the read-only
  `get_total_clip_count` were all refused). Have the creator clear the sequence by hand
  (click the timeline, Ctrl+A, Delete) rather than trying to route around the refusal.

**Also on this job:** `voice-gain.py` died on a 258-segment EDL — one `aselect` expression per kept
range ran to 7.7 kB and ffmpeg answered `Error initializing filters … Cannot allocate memory`. Fixed
upstream in `workflows/voice-gain.py` by measuring in batches of 40 and recombining by energy. Note
it still decodes the whole source once per batch, so it took ~15 min on a 12 GB master.

**And a Windows path trap:** `splice.sh` is bash, so its `/tmp` is `%TEMP%`; a Python helper writing
to the literal `/tmp` lands on `E:\tmp` instead. `polish-boundaries.py` hit this — its polished EDL
went somewhere `splice.sh` never looked, and the splice silently consumed the STALE pre-polish cuts.
Always check the EDL bash can actually see before re-splicing.

## 2026-09-16 — placing a second picture layer (V2), gta-san-andreas-hot-coffee

- **`getMediaPath()` returns BACKSLASHES on Windows.** A placement file written by Python carries
  forward slashes, so `findByPath` never matched, the script re-imported on every call and then
  reported `ERROR: import failed`. Normalise both sides (lower-case, separators to `/`) before
  comparing. Build the normaliser with `String.fromCharCode(92)` rather than a backslash literal: a
  literal does not survive Python's string escaping on the way into ExtendScript, and what reaches
  Premiere is `/\/g`, an unterminated regex, which comes back as the generic
  "ExtendScript execution failed via CEP evalScript()".
- **`projectItem.setOutPoint(seconds)` quantises to the SOURCE frame grid, not the sequence's.**
  A 24 fps clip in a 59.94 sequence landed **3 timeline frames short** of the requested slot and the
  end pin (`if clip.end > END`) only ever shortened, so it could not give them back. → over-trim by
  0.2 s, lay it, then set `clip.end` UNCONDITIONALLY. The overhang is either overwritten by the next
  clip laid on the track or removed by the pin.
- **Kling renders 1928x1076.** In a 1920x1080 sequence `clip.projectItem.setScaleToFrameSize()`
  right after placement FITS it, landing Motion > Scale at 96 with a few px of the track below
  showing on every side. Do it per clip, not as a pass afterwards. **That inset is a look on some
  channels, so it is not automatically a defect** — see the 2026-09-17 entry below.
- **A hole on a picture layer ABOVE the face shows the face.** V2 gaps are not cosmetic on this
  channel, so `place-reenactments.py --verify` fails on any intra-block gap over one frame.
- **`--apply` is idempotent by (basename, start)**, which is what makes a bridge timeout safe: re-run
  and it places only what is missing. 72 clips went down in one pass after two bugs, with one clip
  left 3 frames short from an aborted earlier attempt — the verify caught it by name.

## 2026-09-16 — the MASTER is where a music-bed job clips, and no API reaches it

- **A sequence's audio TRACK exposes no effects and no volume through the DOM** (`seq.audioTracks[n]`
  keys are only `clips, id, mediaType, name, transitions`, probed on Premiere 25.0), and the MASTER
  track is not in `audioTracks` at all. So there is no scripted master limiter and no scripted track
  trim: **the only lever on the summed mix is the clip levels**, which means the level bands have to
  be right for the job's track layout, not just for the house.
- **The house SFX bands were measured on a job with NO music bed.** On a channel that always has one
  the master sums voice + music + every cue, and the first full export measured **+0.008 dBFS true
  peak** (`ebur128 peak=true`; `astats` flat factor 0, so a handful of samples, not sustained
  flat-topping) against YouTube's −1 dBTP. Integrated was −17.0 LUFS, which was right — only the peak
  was wrong. Fix: the CHANNEL preset carries its own `targets_dbfs`, 2 dB under the house bands, and
  nothing in the creator's music or the measured voice chain is touched.
- **`place-sfx.py --plan <file>`** now lets a second cue sheet share these mechanics. `readback()`
  filters by the LIBRARY FOLDER of row 0, so two sheets drawing on two folders never see each other's
  clips and each stays independently verifiable. Used here for the reenactment layer's diegetic sound
  (`broll/reenact/sfx-diegetic.json`, the job's own `assets/sfx/`) alongside the graphics cue sheet.
  **A second sheet needs the same 29.97 source-grid snap as the first** — the quirk is the host's, not
  the plan's.
- **`place-graphics.py --remove` matched nothing on Windows** and said so silently by printing `[]`:
  it took the basename with `p.split("/").pop()` while `getMediaPath()` returns backslashes. Fixed to
  split on both separators. Overwriting a render in place and re-verifying turned out to be enough
  anyway — Premiere re-read the changed file at the same path without a remove/replace cycle.
- **Frame grabs for a program-monitor proof:** `ExportFrame.epr` is a **720x480 Targa**, useless.
  Use the system `IngestPresets/Transcode/Match Source - H.264 High Bitrate.epr` over a one-frame
  in/out — it keeps the sequence resolution and rate — then pull the PNG with ffmpeg. `seq.clearInPoint`
  and `clearOutPoint` **do not exist** (calling them is a bare evalScript failure); put the in/out back
  with `setInPoint(0); setOutPoint(seq.end / 254016000000)`. And **no extra dot in the output stem**:
  Premiere read `f0002.50.png` as a folder path and refused it with "OutputFilePath is in a folder that
  doesn't exist".
- **There is no 1080p export preset in the repo.** Minted `youtube-1080p5994-h264-cbr24.epr` from the
  locked 2160p one by patching four `<ParamValue>`s: width 1920, height 1080, `ADBEVideoFPS`
  **4237833600** (59.94 in ticks), target = max = 24 Mbps, CBR kept at `ADBEVideoBitrateEncoding` 0.
  Measured out at 25.5 Mbps for a 12:07 programme, 2.3 GB.

## 2026-09-17 — three more bridge/export traps

- **`exportAsMediaDirect` MUST BE SERIALISED.** It returns immediately and Premiere keeps writing.
  Firing the next one first overwrites the sequence in/out, and the earlier export dies half-written
  as a zero-byte `.m4v` / `.aac` pair that never becomes an mp4. A batch of twelve frame grabs landed
  six. Wait for each output to appear AND stop growing before asking for the next.
- **The CEP bridge can drop mid-run with Premiere still open.** It went down between two placement
  calls; `tasklist` showed Premiere alive on the same PID. There is no way to restart a CEP panel
  from outside, and `premiere-up.sh` is macOS-only, so the recovery is the creator clicking
  **Window > Extensions > MCP Bridge > Start Bridge**. This is survivable only because every placer's
  `--apply` is idempotent: after the click, re-running placed exactly the 11 rows that were missing.
  **Keep every placer idempotent by (file, start, track) — it is what makes a dropped bridge a pause
  rather than a rollback.**
- **`a % b * 2` is `(a % b) * 2`** — same precedence, left-associative. A readback that formatted a
  track index into two `%d` slots died with "not enough arguments for format string"; the repeat has
  to be parenthesised: `% (((v,)) * 2)`.
- **A readback must tolerate a track that does not exist yet.** The plan wanted V7, the sequence had
  six tracks, and `seq.videoTracks[6]` threw a bare evalScript failure before `place()` ever got the
  chance to provision it. Return `[]` above the track count instead.

## 2026-09-19 — a KEYFRAMED parameter hides behind its first `<value>` in the FCP XML

- **The creator's face nests carry a keyframed Scale ramp (100 → 110) and the parser reported them at
  100.** The keyframes ARE in the XML — `<parameter>` carries a static `<value>` and then one
  `<keyframe><when/><value/></keyframe>` per key — but `parse_fcpxml.py` read the first `<value>` and
  stopped, so the post-mortem logged the nests as "no effects". Wrong, and the creator had to say so.
  **Fixed:** `param()` now returns `{min, max, keyframes}` when it sees ≥ 2 keys; re-run on Hot Coffee it
  finds **31 keyframed clips, every face nest at 100 → 110 with 2 keys** — the gradual zoom, exactly as
  described. Rule: **a parameter is a range until proven static**; any reader that takes the first value
  of a Motion/Opacity/Level param is reporting a ramp as a number. (The DOM route — `isTimeVarying()`,
  `getKeys()` — is still the check when an XML export hangs.)
- **The first `</track>` after the sequence's `<video>` is NOT the end of V1** — a nested clipitem embeds
  its child `<sequence>` with its own `<track>`s, so a naive slice of "V1" ends inside the first nest
  (a verification pass found "1 nest" on a track that holds 26). Depth-match, always.

## 2026-09-18 — the post-mortem read: what the FCP XML cannot tell you, and the DOM can

- **★ THE EFFECT STACK IS DOM-ONLY.** Color Matte (a synthetic item), Drop Shadow, BCC Film Grain and
  every third-party effect come out of `exportAsFinalCutProXML` as "not translated" — the creator's
  whole overlay look (V2 matte + grain, overlay at 96 with a shadow) was INVISIBLE in three XML exports
  and took one `clip.components[*].properties[*].getValue()` sweep to read. Labels and Motion scale
  are XML-only; effects are DOM-only. Read both, never just one. `projectItem.isSequence()` /
  `getMediaPath()` empty = SYNTHETIC tells a matte from media.
- **`exportAsFinalCutProXML` HANGS on this sequence** (Sequence 12: 330 clips, 27 nests, mattes) — by
  name via `P.sequences[i]` AND as the active sequence after `openSequence()`; the bridge returns
  nothing, no file appears, the 180 s call times out. Sequence 11 exported in 5 s. Two earlier exports
  of 12 worked (one truncated mid-write), so it is a dialog or size threshold, not a rule. **The
  substitute is a full DOM readback** (`transcript/timeline-final.dom.json`: track, name, start, end,
  scale for every clip) — enough for any diff. `openSequence(sequenceID)` itself works fine; put the
  creator's view back afterwards.
- **A flat clipitem scan inside a track block reads the NESTED sequence's sub-clips too**, at
  nest-relative times: 21 phantom "punch-ins" at 2–15 s, overlapping each other. Blank every child
  `<sequence>` span before scanning; read the nests separately for what is inside them
  (`parse_fcpxml.py` does both). A nest carries its label once; its sub-clips carry the punch-ins.
- **FCP `audiolevels` level is LINEAR (1.0 = 0 dB): dB = 20·log10(v).** It is NOT the DOM's Volume
  Level encoding (v = 10^((dB−15)/20)). Reading the XML with the DOM formula turns a −24 dB music bed
  into "+8 dB".
- **A Kling clip in a 59.94 sequence reads as speed ×1.03–1.04 in the XML** — the 24 fps source grid
  against the timeline grid, not a speed change. Real changes here were ×0.5 on two stills.

## 2026-09-17 — placing SFX: stacked layers, the audio grid, and reading the timeline FIRST

- **★ TWO CUES AT THE SAME INSTANT ON ONE AUDIO TRACK: the second REPLACES the first.** `place-sfx.py`
  lays each slice with `overwriteClip`, which does exactly what it says. An ambience bed built as two
  layers (a room tone plus a machine hum, both starting together) aimed both at A6: seven cues
  vanished silently and an eighth landed **18 s late**, at the end of the clip that had taken its
  slot. **One track per simultaneous layer** — room tone on A6, machine hum on A7. The readback is
  what caught it; the apply itself reported eight placements and looked fine.
- **★ NEVER PASS `-v error` TO `volumedetect` (or to any ffmpeg filter you are reading a number
  out of).** Its result is logged at INFO level, so `-v error` hides it, the parse falls through to
  the default, and the "measured" gain is whatever the default happens to be. Here that put **28
  ambience beds at −63…−68 dBFS instead of −30** — rendered, placed, read back, verified, and
  completely inaudible. Every check passed because every check was checking placement, not level.
  Use `-hide_banner -nostats` and **make a missing measurement RAISE**: a measuring function must
  never return a value that is also a plausible answer. Caught only by diffing the exported audio
  against the previous master window by window — do that after any pass that adds sound.
- **A pass that reads the timeline can read its OWN output.** The de-dup swept A4→numTracks, which
  now includes the A6/A7 beds this same script had just placed; `ovNNN-ambience.wav` matched the
  ambience keyword and vetoed every bed on the re-run (59 cues collapsed to 29). Scope the read to
  the tracks you do not own, and filter your own naming convention out of it anyway.
- **An out point FLOORS to the 29.97 audio grid, so put the plan on that grid first.** A 2.500 s
  slice reads back as **2.469** (74 × 1001/30000) and the placer calls it drift. Snap both `at` and
  `src_out` DOWN to a multiple of 1001/30000 before applying, or every apply reports a drift it
  cannot resolve.
- **`place-sfx.py` prints `r['event']` and `r['gid']` in its report**, so a hand-built plan without
  those keys places every clip and then dies with a `KeyError` on the summary line — the work landed,
  the run looked like a crash. Carry `event` and `gid` on every row.
- **READ THE TIMELINE BEFORE PLANNING SOUND, not just the picture.** The creator had already
  hand-placed diegetic sound the plan would have doubled: bank-terminal beeps across the hex-editor
  shots, a designed press-conference ambience across the whole press run, the desk phone, three
  rubber stamps and hall room tone in the courtroom. **De-duplicate by SOUND CLASS, not by track** —
  a first pass vetoed on any overlap and killed seven good beds because a `Scissors` graphics tick
  happened to fall inside them. An existing ambience vetoes a planned bed; an existing diegetic spot
  vetoes a planned spot; a designed busy ambience (crowd + shutters) vetoes planned spots too.

## 2026-09-17 — a fit is not a hole, and the creator's number is the spec

**This section replaces one I wrote the same day claiming the 96 % fit was a defect. It was not.**

- **`projectItem.setScaleToFrameSize()` sets Motion > Scale to 96, not 100**, for a Kling source
  (1928x1076, AR 1.792) in a 1920x1080 frame (AR 1.778): a FIT, inset on every side, so whatever is
  on the track below shows as a border. **Measure it before calling it anything** — the extreme edge
  columns of an exported frame read (62,0,3) here, invisible in a contact sheet.
- **★ THEN ASK WHOSE BORDER IT IS.** On this job it was the creator's: a colour mat with film grain
  under the overlay track, reading as a dark red drop shadow. I filled to 101.5 across 59 clips and
  destroyed a look they had built by hand. **On a timeline a human has edited, a value that is
  IDENTICAL across every clip of a class is a decision, not a bug** — a defect is never that
  uniform. Confirm the intent before changing a look, whatever the geometry says.
- **Recover the original values from an FCP XML, never from memory or a guess.** `export_as_fcp_xml`
  is the only way to read per-clip Motion scale, so an XML taken before a batch operation is the undo
  that `multiple_undo` cannot give you across a session. Parse the sequence's own `<video>` (a
  `<video>` is also nested inside every `<file>`), then per clipitem
  `<effectid>basic</effectid> … <parameterid>scale</parameterid> … <value>`. **A clip with no Basic
  Motion filter is at the default 100 — that is a value to restore too, not a blank to fill.**
- **Setting Scale while `Uniform Scale` is TRUE gets re-normalised back.** `setValue(101)` reported
  101 on the next `getValue()` in the same call and read **100** afterwards. What sticks: turn Uniform
  Scale OFF, set Scale AND Scale Width, turn it back ON, set Scale again. (Verified both directions,
  59 clips up and 58 back down.)
- **The delivery preset is NOT in the Premiere tree.** `Settings/IngestPresets/Transcode/Match Source
  - H.264 High Bitrate.epr` is an INGEST preset and encodes **Main profile at ~10.6 Mbps** — half the
  bitrate of a real master, and easy to ship by accident because the name says "High Bitrate". The
  25 Mbps High-profile delivery preset lives in Media Encoder's system presets:
  `C:/Program Files/Adobe/Adobe Media Encoder 2025/MediaIO/systempresets/3F3F3F3F_4D6F6F56/H264 Match
  Source - High bitrate.epr` (usable by `exportAsMediaDirect` without AME ever opening).
  **ffprobe every export for `profile` and `bit_rate` against the previous master before finalizing**
  — duration and resolution match on both, so only the bitrate gives it away.
- **The bridge pretty-prints an ExtendScript return through `JSON.parse`,** so a `JSON.stringify`
  result comes back on stdout as indented JSON: `json.loads(stdout)`, not a `find('[[')` on one line.

## 2026-09-18 — scripted import stopped working mid-session (ABW6, @affanwizu captions)

- **`app.project.importFiles` / `changeMediaPath` began failing partway through a session** that had
  imported a ProRes 4444 alpha fine 45 min earlier: a modal **"File Import Failure"** for every new file
  (even a blank 1 s ProRes), and for an H.264 MP4 `importFiles` returned `true` and added NOTHING.
  A Premiere restart did not clear it. The files were fine (the creator's manual drag of the same .mov
  worked at once). The modal blocks the CEP panel, so the bridge reads as "not running".
  **Workaround:** close the dialog (it is a top-level window titled "File Import Failure" owned by the
  Premiere process; WM_CLOSE dismisses it), then have the creator drag the file onto the track, and read it back.
  Before a swap, IMPORT FIRST and remove the old clip only after the new item exists, so a failed import
  never leaves the track empty. Root cause not found. The `frame` / `export_frame` grabs also failed that session.
- The Windows "We can't open … ap4h" toast is the Windows player (no ProRes 4444), not Premiere.

## 2026-09-19 — a SLOW call reads as "Bridge is not running" (gta6-travis-scott-hired, Windows, Premiere 25.0)

- **`place-graphics.py --apply` died mid-run with `MCP Bridge is not running`, twice, with the panel
  live.** Cause: the panel writes `bridge-heartbeat.json` between polls, and a single ExtendScript
  that runs past ~4 s (here: `importFiles` of a 59.94 fps mp4 inside `place()`) blocks it; the
  server checks the heartbeat after 1.5 s, finds it older than 2.5 s and aborts. **Premiere still
  finishes the call** — each "failed" run had placed three to five more clips. Workaround that
  worked: import every remaining render in ONE ES call first (let the Node side time out, poll
  `ping` until the panel answers), then `--apply` only overwrites, which is fast; wrap it in a
  retry that re-runs `--apply` after a failed run (placed rows are kept, so it is idempotent) and
  finish on `--verify`. Never trust the error text as "Premiere is down": read the timeline back.
- **`seq.exportAsFinalCutProXML(path)` returns false on a forward-slash path on Windows**; the same
  call with backslashes writes the file. (Same family as `exportAsMediaDirect`, line 33.)
- **The 29.97 audio floor hits the SOURCE IN-POINT too, not only the timeline start** (same job, step 6). A slice starting
  at 0.430 s in its file landed at 0.400: 30 ms of the transient gone and the hit 30 ms late; `place-sfx.py --verify` caught
  the six that crossed its 25 ms tolerance, the rest slid silently. Snap `at`, `src_in` AND the duration to the nearest
  1001/30000 frame before placing (`projects/gta6-travis-scott-hired/hf-graphics/sfx-snap.py`, which keeps
  `sfx-plan.unsnapped.json`).
- **A same-track SFX cascade leaves a stray fragment when the later cue is SHORTER than the tail it cuts into:**
  `overwriteClip` trims the earlier clip at the later one's in, and whatever of it runs past the later one's out survives as
  its own clip (one extra Pop on A4 at 101.735). Trim every overlapped cue in the PLAN to end at the next cue's start (and
  drop one left under two frames, it is a doubling), then place; `sfx-snap.py` does both.

## 2026-09-19 — nesting face runs from ExtendScript, which has no Nest (gta6-travis-scott-hired, Premiere 25.0)

- **No nest API, no menu commands:** `app.findMenuCommandId` / `app.executeCommand` are `undefined` here, and the MCP's
  `nest_clips` only builds a new sequence from whole SOURCE items (it neither trims nor replaces anything). What works,
  proven on a throwaway clone first: target ONLY V1, set the sequence in/out to the run, `seq.createSubsequence(false)`
  (a V1-only subsequence: the trimmed jump cuts with their source in-points, no audio clips), then
  `seq.overwriteClip(sub.projectItem, t, 0, <scratch audio index>)`. The placed nest still gets an EMPTY audio item: route
  it to a track that is empty over the run and `remove(false, false)` it; the V1 nest survives and A1 is never touched.
  Restore targeting and in/out afterwards (this sequence's unset in-point reads `-400000`). `lanes/premiere/face-nests.py`.
- **A snap is HOLD interpolation** (`setInterpolationTypeAtKey(key, 4, 1)`): sampled 100 on the frame before, 125 after.
  Linear is 0. A ramp's midpoint read 105.01 between 100 and 110.
- **ExtendScript has no `Array.prototype.forEach`** (a script died halfway through on it: on the clone, luckily). Plain loops.
- **The bridge returns a script's value only when the whole script IS one function expression:** helper `function`s
  declared before the IIFE made it return `undefined` while the edit still ran. Put helpers inside the IIFE.

## 2026-09-20 — reading a SHIPPED sequence back (the post-mortem pass, Premiere 25.0 / Windows)

- **`exportAsFinalCutProXML` did NOT hang here** on a 488 s sequence with 38 nests, 5 video and 7 audio tracks
  (1.76 MB in seconds) — the Hot Coffee hang is not a rule. Backslash path, as always. `lanes/premiere/parse-fcpxml.py`
  reads it; **the DOM sweep is still needed for effects** (Lumetri, Drop Shadow, film grain) and for clip volume.
- **The FCP XML splits every audio track into its two channels**, so its "A5/A6" is one real track and the pairs do
  not even carry equal clip counts. Track identity comes from the DOM (`audioTracks[i]`), never from XML track order.
- ☠️ **A one-frame `exportAsMediaDirect` for a frame proof is a trap on this machine.** The PNG Sequence preset fails
  with "You do not have permission to create or delete the output file" (E: job folder AND the user's Downloads), and
  the `Match Source - H.264 High Bitrate` ingest preset starts, writes 0-byte `.m4v`/`.aac` temp files, times the
  bridge out at 45 s, **leaves the files locked and the panel unresponsive to every later call**. Do not reach for it
  mid-session: read geometry and effects from the DOM, and look at the creator's SOURCE assets on disk instead
  (the actual jpg/png/mp4 the timeline points at) — that answered every question the frames would have.
- **An Essential Graphics text layer's copy is not readable:** `Text.Source Text` returns a binary blob through the
  DOM, and the XML does not carry it either. A creator's own title cards can be located and timed, never quoted.
- **Premiere 25.0 has NO clip colour-label API — read it from the `.prproj` instead (2026-09-22).** Every documented route returns nothing: `getColorLabel` is not a function on the DOM TrackItem, the QE clip exposes no such property, `export_as_fcp_xml` times out at 45 s without writing a file, and `select_clips_by_color` reports `count: 0` at all sixteen indices. The project file is gzipped XML and does carry it, but the 829 `BE.Prefs.LabelColors` entries under `ProjectItem` are **bin** labels and a red herring — a timeline clip's label is `asl.clip.label.name` on the **VideoClip**, with that clip's `InPoint`/`OutPoint` alongside it (which is what lets you join a block to the dialogue under it). Chain: `VideoClipTrackItem → ClipTrackItem → SubClip[ObjectRef] → SubClip → Clip[ObjectRef] → VideoClip → Clip → Properties`. Two different reference attributes are in play: `ObjectRef` points at `ObjectID`, `ObjectURef` at `ObjectUID`; tracks are reached via `Sequence → TrackGroups/TrackGroup/Second[ObjectRef] → VideoTrackGroup → TrackGroup/Tracks/Track[Index=0][ObjectURef]`. Ticks per second = 254016000000. Save through the bridge first, work on a COPY, never write the project. Working reader: `projects/gta6-pc-release/brief/readlabels.py`.
- **`importFiles` takes ONE path per call through the CEP bridge (2026-09-22).** An array of 18 absolute paths fails `execute_extendscript` outright with "ExtendScript execution failed via CEP evalScript()" — a scripting failure, not a timeout, and not a length problem (the script was only 2.8 KB). The identical call with a single path succeeds every time, so loop it; the loop is cheap and lets you skip names already in the bin. Also strip non-ASCII from filenames before they reach the bridge (emoji and full-width punctuation from `yt-dlp` titles are a real source of this). Working driver: the `importall.py` pattern in `projects/gta6-pc-release/`.
- **Higgsfield `generate_image` FAILS when `resolution: "2k"` is passed explicitly (2026-09-22)** — omit it and the server picks (1344x752 typically, sometimes larger). Failed jobs cost nothing. To get 4K, generate at the default then `upscale_image` (2 credits, preflightable only once a real `image_id` exists, and it returns 3856x2160).

## 2026-09-23 — in-points floor to the SOURCE grid too; splits must sit on both grids (mj-allegations, Premiere 25.0)

- setInPoint floors to the source's own frame grid exactly like setOutPoint (a 29.97 source moves in
  33 ms steps), and with the timeline end pinned the out-point moves with it: up to 41 ms was clipped
  off a word's tail. Workaround: pre-snap every in-point UP to the source grid (+0.1 ms) so the floor
  lands where you meant. presets/youtube-shorts/abundance-wisdom/resolve_beats.py does this.
- Splitting one continuous source into two clips (for two crops) skips or repeats a sliver of audio
  unless the split time is on the source grid AND the first piece's length is a whole number of
  timeline frames (50 fps source on a 60 fps sequence: split on a 0.1 s grid). plan_placement.py
  searches for that point. Proven by readback: both splits 0.0 ms apart.

## 2026-09-25 — a failed `importFiles` opens a MODAL that silently blocks the whole bridge (gta6-vice-city-sign, Premiere 25.0, Windows)

- `importFiles` given a hand-escaped Windows path (`'E:\\Claude Projects\\…'` inside a JSON-wrapped ES
  string) reached Premiere as `E:Claude Projects…` and raised **"File Import Failure — The importer reported a
  generic error"**. The dialog is modal: the panel keeps writing its heartbeat, but every later command queues
  unanswered and `ping` reports the bridge down. Premiere reads as "Responding" at near-zero CPU.
- Fix: build the path as `new File('E:/forward/slashes/…')`, check `f.exists`, pass `f.fsName` to `importFiles`.
- To see a modal behind other windows: enumerate the Premiere process's visible top-level windows (Win32
  `EnumWindows`), render the dialog with `PrintWindow(hwnd, hdc, 2)` (a screen grab captures whatever covers
  it), and dismiss it with `PostMessage(hwnd, WM_CLOSE)`. The queued commands drain on their own afterwards.
- `replay` threw "MCP Bridge is not running" but the ES had executed in full (146/146 clips, frame-exact); only
  its trailing `save_project` never ran. Read the sequence back and save by hand; never re-run a replay blind
  (it appends after the last V1 clip).

## 2026-09-30 — bridge output and Windows frame proofs (gta6-hurricanes overlays)

- `node premiere-bridge.mjs execute_extendscript` prints ONLY the result on **stdout** (a JSON string like
  `"placed"`, or a pretty-printed object when the ES returned JSON); every log line goes to **stderr**. Parse
  `json.loads(stdout.strip())` first. Searching stdout for `'\n"'` misses a result that starts at position 0 and a
  parser that falls back to the first `{` grabs the echoed `with args: {` from a merged stream.
- The bridge `frame` command still throws on Windows. The working proof is the lab-notes route: set a one-frame
  sequence in/out, `exportAsMediaDirect(<stem>, ".../MediaIO/systempresets/3F3F3F3F_504E4720/PNG Sequence (Match
  Source).epr", 1)`, restore in/out. **A dot in the stem fails as "You do not have permission to create or delete
  the output file"**: `f133.5` fails, `f1335` works. Build the paths with `os.path.join`, never hand-escaped.
- A 43-block timeline guard compared positions rounded to 3 decimals against a 4-decimal snapshot and refused on
  pure rounding; compare with a 2 ms tolerance.
- **The PNG grab lands as `<stem>0` with NO extension** on 25.0 here (not `<stem>0.png`); PIL opens it as-is. An
  unset sequence in/out reads back `in -400000 / out 0`, and `setInPoint(-400000)` + `setOutPoint(0)` restores that.
- **QE razor on a 59.94 sequence cuts frame-exact** with `qe.project.getActiveSequence().getAudioTrackAt(n).razor(tc)`,
  `tc` = the integer frame `round(T*60000/1001)` written as 60-frame non-drop `HH:MM:SS:FF` (display format 108):
  22 ranges razored and lifted on A2, worst edge 0.1 ms off the plan (the music drop-outs under the cut zooms).
- **An audio clip's timeline START is not floored to 29.97** (the 2026-09-13 flooring hits a slice's source in/out):
  44 pops placed on odd 59.94 frames, bounced A3-only (`Wave48mono24.epr`, other tracks `setMute(1)` then
  `setMute(0)`), every onset exactly on plan (3.8 ms late = the file's own transient offset).

## 2026-10-03 — inserting clips between butt-joined blocks (nick-walker-never-mr-olympia, Sequence 24)

- **An overwrite whose source out-point rounds past the slot eats the next clip's HEAD.** A piece cut to a whole
  number of 60 fps frames from a 23.976/24/29.97 source landed 1–2 frames long, overwrote the head of the host block
  after it, and trimming the piece back (`clip.end = t`) left a 1–2 frame hole: the head is not restored. Lay the
  piece ~20 ms SHORT (`setOutPoint(in + dur - 0.02)`), then extend its tail with `clip.end = at + dur`.
- **`trackItem.start = t` repairs a trimmed head without moving the end** (start earlier, end unchanged, the source
  in point extends): proven by rendering the block's first frame and matching it to camera frame 20124 (the
  restored in), not 20125 (a slip). The DOM's `inPoint` reads STALE afterwards, exactly like `outPoint` after
  `end =`; verify positions and lengths, or a rendered frame, never the in point.
- **Opening a gap in butt-joined V1+A1 blocks:** `clip.move(delta)` per clip, latest first, V1 then A1, skipping an
  A1 clip already carried by a linked move: 118 + 119 moves, every block exact. `overwriteClip` on V1 with an A/V
  item lays its audio on A1 too.
- **Speaker attribution by voiceprint works in the WhisperX venv:** `pyannote/wespeaker-voxceleb-resnet34-LM`
  through `pyannote.audio` `Inference(window='whole')`, audio passed as an in-memory waveform (torchcodec is broken
  on this box). Two references 8–10 s each separate cleanly (Bob vs Shawn −0.03); same speaker scores 0.6–0.8.
  `resemblyzer` needs a C++ compiler on Windows (webrtcvad), so it does not install here.
- **`face-nests.py` left a ZERO-length copy of the replaced clip at the run's edge** on a 60.00 fps sequence (14 of 25
  runs, Sequence 24): the nest is overwritten at S + 1e-4 and the original survives as a 0-frame item. Invisible in
  playback, but it is junk on the creator's timeline and breaks "the clip at time t" lookups. Fixed in the tool: right
  after the overwrite it removes any sub-half-frame V1 item touching the run (no ripple) and reports `stubs`.
- **A Premiere `exportAsMediaDirect` mp4 carries a stream GROUP, and `ffprobe -show_entries stream=... -of csv=p=0`
  then prints the stream twice** ("1920,1080", blank, "1920,1080"): a `split(',')` parse dies. Read `-of json` and take
  `streams[0]` (`overlays/card.py probe()`).
- **`exportAsMediaDirect` can answer `bridge_unavailable` while Premiere goes on and writes the file** (a 4.4 s nest,
  2026-10-03): watch the output file for a stable size, never re-fire the export.
- **A dip's frames are judged at the PEAK, not one frame before it**: 97.9 % Black Video over a bright card still reads
  mean 23 in the rendered PNG (the sequence composites non-linearly), while the 100 % key frame reads 0.00.
- **Replacing every third-party clip with a rendered card, editably:** card on the track above at the same span, the V1
  clip's `disabled = true` (video item only; its linked A1 item stays enabled, read back), the zoom as Motion > Scale
  keys on the card. Undo for one clip = delete the card, re-enable the V1 video.

- **2026-10-04 · `in` is a reserved word in ExtendScript (ES3): `{in: x}` as an object key kills the whole script**
  with the bridge's generic "ExtendScript execution failed via CEP evalScript()" — a syntax error, not a host failure.
  Same for `class`, `default`, `new` etc. as bare keys: rename (`ip:`) or quote them.
- **2026-10-04 · reading another sequence needs no activation**: find it in `app.project.sequences` by name and read
  its tracks; nests resolve through `clip.projectItem.isSequence()` + `projectItem.nodeId`. Only QE razors need the
  sequence ACTIVE; `lanes/premiere/music-dropouts.py` opens it for the edit and puts the creator's view back.
- **2026-10-04 · `exportAsMediaDirect` paths through `execute_extendscript` (Python subprocess + `json.dumps`) take TWO
  backslashes in the script source, not four.** Four reach ExtendScript as doubled separators; `File` still resolves
  them, but the exporter answers "Error: Unknown Error" and writes nothing. Two give single separators and the PNG
  frame proof works (`projects/kick-fake-viewers/review/tools/proof-frames.py`; output is `<name>0` with NO extension,
  rename to .png). The four-backslash note above was for a different call path: test with `new File(p).fsName`.
- **2026-10-04 · a file whose extension lies blocks the bridge**: a CDN image saved as `.png` was a JPEG, `importFiles`
  opened a File Import Failure modal, and the bridge reported "not running". Check magic bytes before importing.
- **A ranged sequence marker takes `marker.end = <seconds as a number>` (2026-10-04, nick-walker-parents).** Assigning a `Time` object fails the whole `evalScript` with no message, AFTER `createMarker` already ran, so a retry leaves a duplicate marker: find markers by name first, delete extras, then set `end` as a number.

## 2026-10-07 — reaction videos in Affan's live ABW8 (Seqs 33-35), Premiere 25.0, Windows

- **Edit a sequence WITHOUT activating it.** DOM writes on `app.project.sequences[i]` work on any sequence: Motion values and keys,
  `disabled`, `overwriteClip` on its tracks, Volume Level. Only QE needs the active sequence (`addTracks`, `addAudioEffect`). Keep QE
  to ONE short window: `openSequence(target)`, do the work, then `openSequence(prev)` in a `finally`. A parse error between open and
  restore left the creator on the wrong sequence once. Driver: `projects/_onyx-batch-2026-10/reactions/tools/apply.py`.
- **Motion's built-in Crop (Left/Top/Right/Bottom %) is in LAYER space**: it crops the source frame before Scale/Position. Proved on a
  program-monitor grab: a zoomed screen layer cropped to its panel box never leaks into the bars. To keep a crop exact through an
  animated zoom, bake keys every 1/30 s for Scale, Position and all four crops.
- **`track.setLocked()` takes a NUMBER** (`setLocked(0)` / `setLocked(1)`). `setLocked(false)` kills the whole `evalScript` with no
  message.
- **QE `addAudioEffect` returns `false` on a LOCKED audio track**, and `audio-polish.py` then reports "chain missing after add" for
  every clip. Check `isLocked()` first; unlock, apply, re-lock.
- **`overwriteClip` onto an occupied slot**: two graphics that start at the same time on one track make the second placement either
  skip ("exists") or overwrite the first. Overlapping graphics are rendered as ONE layer (a `group`). The placer now replaces a
  different-named clip found at its slot.
- **Never export in the creator's project** (Affan, 2026-10-07): `exportAsMediaDirect` pops an encoding window over his live session.
  He cancelled it by accident, then asked us to stop. A cancelled export answers "User has cancelled the export" and Premiere deletes
  its own `.m4v`/`.aac` temp files. Vertical preset for HIS exports: `premiere-templates/vertical-1080x1920-60-h264-cbr24.epr`
  (`youtube-1080p5994-h264-cbr24.epr` with Width 1080, Height 1920, FPS 4233600000 ticks = 60).

## 2026-10-08 — graphics + SFX onto Affan's live ABW8 Sequence 36 (nick-martin-same-night, Premiere 25.0, Windows, 60 fps)

- **Hand-written `placement.json` rows must be frame-snapped.** Slot times carried 3 decimals (5.417 for frame 325 = 5.41667);
  `place-graphics.py --apply` trims the item to `END-START` (3.333 s = 199.98 frames, FLOORED to 199) and only ever shortens the
  end pin, so g03 and t01 landed ONE FRAME SHORT and the face on V2 flashed through. `--verify` passed (1.5-frame tolerance).
  Fix: snap every row to `round(round(t*fps)/fps, 5)` before `--apply` (`derive()` already does; a hand-made row does not).
- **`place-sfx.py` with a slice that ends at the media end loses its last 1-2 frames** (`setOutPoint(dur + 1e-4)` is clamped to
  the media's last frame; 0.700 s -> 0.667, 0.160 -> 0.133). Harmless when the slice carries a baked fade-out; `--verify` then
  reports every tail as drift and refuses to save. Record the placed tails in the plan (or make `src_out` frame-floored minus a
  frame), verify, then `save_project`.
- **At 60 fps `MBLUR_SS` caps at 4** (the renderer refuses fps > 240: 60 x 8 = 480). `MBLUR=1 MBLUR_SS=4 MBLUR_SHUTTER=3`.
- **QE `addTracks(0, 0, 1, 1, n, 0, 0)` added a stereo A5** on a sequence with A1-A4 (place-sfx `provision()`), nothing moved.
- **Two Claude sessions in ONE Premiere project (2026-10-08):** DOM edits on named, non-active sequences are safe in parallel
  (the bridge serialises calls). Anything that switches the ACTIVE sequence (QE razor, `addTracks`, `audio-polish.py`,
  playhead grabs) is not: wrap it in `lanes/premiere/ACTIVE-WINDOW.lock` (create with O_EXCL, wait while it exists, stale
  after 15 min; `reactions/tools/apply.py` `active_window`). A save from either session saves the other's half-done edits.
- **Reaction tightening on HIS timeline (2026-10-08, Seq 37/38):** QE razors at every cut edge on every track (one locked window),
  lift (no ripple), then `clip.move(delta)` per clip, earliest first, deltas read fresh, so a clip carried by a linked partner
  reads 0 and is skipped. Then 10 ms Level fades at each new A1 joint. Proof: rebuild A1 offline from the readback and null it
  against the offline-cut audio; a readback rounded to 1 ms fakes a mismatch of a few samples, so read in-points to 0.1 ms.
  `exportAsFinalCutProXML` needs the NATIVE path (`new File(p).fsName`); a forward-slash path returns true and writes nothing.
- **A QE razor on a VIDEO track does not carry the linked audio** (A1 counts unchanged after 76 video razors on Seq 37/38).
- **`Track.isMuted()` on a video track is the track-output eye**: Seq 37 arrived with V1 + V3 off, and the program monitor showed
  only the overlays. Grabs switch outputs on and restore them in a finally (`apply.py --grab-only`). Never leave his toggles changed.

## 2026-10-08 · `app.project.activeSequence = seq` READS BACK but does not switch — a shared-Premiere hazard (gta6-ign-missions)
- **The assignment returned the new name on readback in the same script, yet the NEXT bridge script still saw the old
  active sequence.** `audio-polish.py` (which works on `activeSequence`) therefore ran on another session's Sequence 38 and
  overwrote its 50-clip Amplify (+7 dB → +6 dB) before saving. Nothing was added or removed; one value changed, reported
  to that session at once. **Switch with `app.project.openSequence(sequenceID)`, wait ~1.5 s, then PROVE the target with
  two independent reads (DOM `app.project.activeSequence.name` AND QE `qe.project.getActiveSequence().name`) plus a
  fingerprint only the target has (its A1 clip count) — and refuse to run otherwise.** Re-check the active sequence after
  the command too. Tool: `projects/gta6-ign-missions/transcript/active-window.py` (+ the shared `ACTIVE-WINDOW.lock`).
- **Any tool that acts on `activeSequence` is unsafe while two sessions share one Premiere.** Prefer DOM writes addressed
  to a sequence BY NAME (e.g. `replay-seq39.py`); keep QE-only operations inside a proven active window.

## 2026-10-08 · late: three Premiere findings from the SAME NIGHT fix pass (nick-martin-same-night)
- **A graphic flashed the shot underneath for ONE frame at its head although the placement was frame-exact** (V3 start −
  V2 start = 0 frames). Cause: the libx264 render had B-frames (`has_b_frames=2`), so the mp4 carries negative DTS and an
  edit list (`elst`) that Premiere misreads at the clip head. Fix at the source: `-bf 0` on every libx264 encode in
  `render.sh` (the reference `presets/youtube/default/reference/fullscreen-render.sh` too). Check a render with
  `ffprobe -show_entries stream=has_b_frames` = 0.
- **`place-sfx.py` / `place-graphics.py` take `--sequence "<name>"`**: every script addresses the sequence BY NAME and any
  QE call is refused, so a placement never touches (or depends on) the active sequence while another session holds
  `ACTIVE-WINDOW.lock`. Proven: 14 SFX + 2 bleeps placed on Sequence 36 while Sequence 39 stayed active for the other
  session. DOM `addKey` / `setValueAtKey` on Motion > Scale and Volume > Level also work on a non-active sequence.
- **A short audio slice can land 2 frames short even with media to spare** (a 28-frame bleep came in at 26 with a 3-frame
  pad behind it; `clip.end = t` then moved the end but `outPoint` read back stale). Ask for 2 frames more than you need
  and record the read-back tail in the plan.

## 2026-10-09 · gta6-ign-missions (ABW8 › Sequence 39, Windows, Premiere 2025, shared with another session)
- **`app.project.importFiles([20 paths], true, bin, false)` HUNG Premiere**: its "Import Files" progress dialog sat at 0 %
  with Premiere idle (0.3 CPU-s in 5 s), every bridge call timed out ("Bridge response timeout", heartbeat still alive)
  and the OTHER session's bridge was blocked too. Nothing had been imported. Found by enumerating Premiere's top-level
  windows (Win32 `EnumWindows`, class `#32770` titled "Import Files"; a `PrintWindow` grab showed the empty bar), cleared
  with a posted `WM_CLOSE` (= Cancel; no focus change, no mouse). **Import ONE file per `importFiles` call** (0.6 s each,
  66 + 12 + 4 files clean). Tools: `projects/gta6-ign-missions/hf-graphics/place-seq39.py`, `place-sfx-seq39.py`.
- **QE `exportFramePNG` threw "Unknown error exception" on EVERY timecode** (`HH:MM:SS:FF`, `;` drop-frame, even
  `qs.CTI.timecode`) and to any path (spaces or none) on Sequence 39 this session, so `premiere-bridge.mjs frame` fails
  with "ExtendScript execution failed via CEP evalScript()". No dialog open. Verification fell back to an OFFLINE
  composite rebuilt from Premiere's own readback (V1–V3 start/end/inPoint/media → per-layer stills → overlay):
  `projects/gta6-ign-missions/review/composite-check.py`. Extract each layer as its own still FIRST: stacking seeked
  inputs in one filtergraph emitted the base frame before a layer whose first PTS sat a hair after 0 (4 of 9 frames
  showed the face where the graphic was).
- **The bridge pretty-prints a parsed result across several lines**: a caller that `json.loads` only the LAST stdout line
  reads `}` and fails. Parse the whole stdout.
- **`music-dropouts.py --music-track N` is 1-BASED** (`4` = A4); `3` planned against the SFX on A3. Applied on Seq 39:
  51 ranges, 99 razors, 0 music under a zoom, levels unchanged, video identical.
- **QE video-only razors at 59.94** (`getVideoTrackAt(0).razor(tc)`, integer frame → 60-frame NDF label): 70 razors,
  V1 127 → 197, every cut within half a frame, A1 untouched (127) — the face-pass cut zooms (`transcript/face-pass.py`).
  The Uniform-Scale dance (OFF → Scale + Scale Width → ON → Scale) held on 57 zooms in a SEPARATE readback; a stretch
  gag is Uniform OFF + Scale 100 + Scale Width 380–420.
- **Face position: OpenCV 5 has no `CascadeClassifier`; use the vendored YuNet** (`assets/models/face_detection_yunet_2023mar.onnx`,
  `cv2.FaceDetectorYN`). Pick the most CONFIDENT face (last column), not the largest box: a 392 px false positive on the
  leather chair won on area on 5 of 20 shots.
- **At 59.94 the HyperFrames motion-blur supersample caps at 4** (already noted above for 60): `MBLUR_SS=8` failed the
  render outright; `MBLUR=1 MBLUR_SS=4 MBLUR_SHUTTER=3`.
- **Parallel HyperFrames renders at -P 6 failed 3 of 26 with "FFmpeg cannot start"** (its own `ffmpeg -version` probe
  timing out under load). Re-run the failures at -P 2.
- **A LOCKED track lies to DOM scripts (2026-10-09, Seq 36 V1 locked by the creator):** `clip.remove(false,false)` returns
  `true` and removes nothing; `videoTracks[0].overwriteClip(item, t)` silently lays the picture on the next UNLOCKED video
  track (V2) while the audio still lands on A1. Read `track.isLocked()` before any write. To change one clip on a locked
  track: `setLocked(0)`, the edit, `setLocked(1)` in a Python `finally` (separate bridge calls). `setLocked(true)` THROWS
  in this Premiere (25.0); 0/1 work. ExtendScript `try/finally` with a `return` inside returns `undefined`, so never
  rely on it to report a failure. (`projects/nick-martin-same-night/replace-3c-v1.py`)


## 2026-10-12 · building a sequence from RAW recordings (Onyx reactions, batch 2)
- **A long ExtendScript call outlives the bridge's reply window, but the work still lands.** 104 segments × 2 `overwriteClip` in one
  call came back "MCP Bridge is not running"; Premiere had finished every placement. Batch heavy DOM work (16 segments, 24 Motion
  edits per call) and READ BACK before retrying, never re-run blind (`reactions/tools/build_seq.py`).
- **A 59.94 camera's in-point lands on the 60 fps sequence grid**: `setInPoint` + `overwriteClip` put each camera piece 1-31 ms
  EARLY (mean 16 ms) against the requested sync time. Inside lip-sync tolerance; `build_seq.py --verify` allows 35 ms.
- **Video-only placement = a video-only subclip**: `projectItem.createSubClip(name, 0, end, 0, 1, 0)` (takeVideo 1, takeAudio 0), then
  `setInPoint/OutPoint` + `overwriteClip` on it: the camera's scratch audio never touches A1.
- **A new sequence with his exact settings = `clone()` of an EMPTY sequence of his** (1080x1920 60, his track count), renamed; the
  clone becomes the ACTIVE sequence. `createNewSequenceFromClips` would inherit the camera's 1920x1080.
- **Camera-to-OBS sync**: `workflows/sync-dual-audio.py --report --json-out`; fit the offset line through the windows with peak ≥ 10x
  only (C1349's weak first window sat 40 ms off the other three); window centres are CAMERA time.

## 2026-10-13 · overlapping SFX on ONE audio track: `overwriteClip` splits the earlier sound (Onyx reactions, batch 3)
- **Symptom:** a plan with a whoosh at t and a thud at t + 0.34 s placed both on A2: the readback had 73 clips for 55 cues. Overwriting a
  short clip into the MIDDLE of a longer one splits the longer one: its head ends at the new clip (an abrupt cut mid-sound) and its
  TAIL survives after the new clip as a separate clip that starts mid-waveform (a stray, clicky fragment). 18 such tails in one video.
- **Fix (reactions/tools/apply.py, 2026-10-13):** each cue goes to the first of `plan.sfx_tracks` (default A2, A4) that is free at its
  time (busy = the file's length minus its ES_LEAD trim); when both are sounding, the one that frees first is ENDED at the cue
  (`clip.end = t`), never split. `--overlays` first clears our SFX clips from those tracks, so re-placing is idempotent; `--verify`
  now counts the clips on both tracks against the plan's cue count.
- **Hard audio edges** where a reviewed video starts/stops at full level (a VLC pause, a cut through a music bed): `tools/afade.py`
  puts 25 ms Volume ramps on the A1 clips either side (keys in clip-source time, as the bed's), DOM only, no active sequence.
- **build_seq.py --place** on 60+ segments: the bridge drops after ~16-32 segments per run; `--resume` in a loop finishes it (the
  placed work is always intact). Re-placing after a rough cut changed: `--place --clear`, then `--resume` loops.

## 2026-10-14 — exporting a Dynamic-Linked AE comp (Affan's ABW8 Sequence 53 → ABW9 Linked Comp 79, Premiere/AE 2025, Windows)

- **`exportAsMediaDirect` of a sequence whose picture is a heavy Dynamic-Linked comp runs for HOURS behind a modal dialog.**
  Comp 79 (Sapphire BlurMoCurves, Deep Glow lines, a 4K caption precomp with Turbulent Displace, a LookSuite/BCC/Lumetri grade)
  rendered through the open AE at ~12 s/frame (~1.3 cores): 1 MB of ~110 MB after 13 min, dialog at 0 % → 6–8 h, Premiere
  blocked by "Encoding Sequence 53" (#32770) the whole time. The dialog is NOT in a PrintWindow of the main window: find it with
  EnumWindows on Premiere's PID and PrintWindow its own hwnd. With AE open and the project UNSAVED, Dynamic Link renders the
  in-memory state; closing AE mid-export would fall back to the saved .aep. Quote the time before starting a full export.


## 2026-10-19 · batch-3 reactions (five, ABW10): what the toolkit got wrong and the workaround
- **facex.py locks onto the leather chair.** YuNet scores the tufted leather behind Affan as a face: Wellness one beat (x 323 vs his
  ~1050), Moonshots the outro (284-297 vs ~900), **Priestley EVERY beat (221-527 vs 908-1076)**. `tools3/facefix.py` resets outliers
  to the median, which fails when all beats are wrong: then pass `t0=x` per beat, measured on a camera grid
  (`srcgrid.py <dump> "<seq>" 1 out.jpg t...`, track 1 = the face track). Re-apply after EVERY build_plan.py + facex.py run (the
  plan rebuild resets face_x). Fix candidate: pick the detection nearest the previous beat's x, not the top score.
- **A view is NOT clamped to the recording.** geom.view_motion places whatever cx/cy/z it gets: a view whose half-height in source px
  (994 / 2 / (0.71 z)) exceeds cy shows a black band at the panel top (Priestley short_mock cy 560 z 1.15 → 40 px). Keep
  cy ≥ 700 / z and ≤ 1440 − 700 / z (and the same for x with 760 / z).
- **Between-key slips on camera pushes**: an anim baked at 1/30 s keys bent up to 9.9 px off the panel between keys (Moonshots title
  push). `apply.py` now reads `plan.anim_kps` (default 30); 60 = a key on every frame → max 2.9 px. Set in build_plan.py.
- **--layout-check before --razor can crash** (`view_at` returns None) when a drifting screen clip straddles a face-only edge; razor
  first (it cuts at every face edge), then dump-layout, then check.
- **Joint words: the free ASR times are not evidence.** WhisperX/faster-whisper word times on this desktop audio sit up to ±0.4 s off,
  and an RMS dip cannot tell "here" from "right". Two job-local tools decide instead: `tools3/falign.py` (wav2vec2 forced alignment of
  the KNOWN text in a 2-4 s window; also scores alternative wordings: 'happy' 0.99 vs 'if' 0.49) and `tools3/endtest.py` (Whisper
  large-v3 on each candidate cut end/start, a 0.4 s hard stop appended: "280.833 → 'the case', 281.083 → 'the case here'").
  Both run with the whisperx venv python; endtest under `lock.sh gpu` and needs torch's lib dir on the DLL path (cublas64_12).
- `tools3/tightasr.sh` must be run from the REPO root with `projects/<job>` (its second half cds into the repo).
- **falign.py cannot score digits**: wav2vec2's character set has no numerals, so "1.29" aligns as noise and a wording test with
  digits misleads (DSH: it "found" a second "million"). Spell numbers out ("one point two nine") before comparing variants.
- **Re-rendering an overlay Premiere already imported**: write it under a NEW name (overlays.py `plan["captions_file"]`), then
  `projectItem.changeMediaPath(path, true)` on the clip's project item. The first attempt on a just-written 850 MB file raised a modal
  "File Import Failure: The importer reported a generic error"; the modal blocks the CEP bridge ("MCP Bridge is not running") until it
  closes: find it with EnumWindows on Premiere's PID, PostMessage WM_CLOSE, wait for ping, retry (the retry with a Windows path worked).

## 2026-10-19 · cbum-last-show (ABW10 › "THE LAST SHOW - rough cut", shared with the Onyx session)
- **A long single bridge call reports "MCP Bridge is not running" while the ExtendScript keeps running and FINISHES.**
  `audio-polish.py --apply` on 154 A1 clips: the bridge gave up, then the lock's restore call queued behind the script and
  succeeded. A by-name read-back found all 154 chains correct (`projects/cbum-last-show/work/premiere_seq.py --verify-audio`).
  Never retry blind after this error, because a second `--apply` on a finished chain is harmless but a re-replay is not. Read
  back BY NAME, since `audio-polish.py --verify` reads the ACTIVE sequence, which is the other session's again by then.
- **Creating a sequence while another session works:** `createNewSequenceFromClips` opens (activates) the new sequence,
  so it ran inside ACTIVE-WINDOW.lock for ~1.5 s. `openSequence(prevId)` restored the other session's sequence, proven by
  DOM + QE reads. Everything else (import of ONE file, clear, replay in chunks of 30, verify, save) was by name.
- **"Lay it 20 ms short, then extend the end" is NOT enough for a 25 fps source on a 59.94 timeline (cbum-last-show 2026-10-19).**
  `setInPoint` snapped the 25 fps THE END clip's in point 51 ms early to its own frame grid, so the short overwrite still covered
  ONE frame of the next host clip's head (the host clip shifted to +1 frame, a 1-frame hole after the tail fix). Repair:
  `clip.start = <old start>` on V1 and A1 restores the head (verify by position, not the stale inPoint). The placer now lays
  90 ms short (`projects/cbum-last-show/work/place_inserts.py`); its verify tolerates a ≤ 2-frame in-point snap.
- **After `trackItem.end = x`, `outPoint` reads back STALE (cbum-last-show 2026-10-20).** `work/fix_cold_open.py` trimmed 0a-b and
  0a-c with `.end`, and the by-name readback still gives the OLD outPoint (0a-b 1360.476, true 1359.675; 0a-c 1372.354, true
  1373.122). `end - start` is right. So compute the source out as `inPoint + (end - start)`, never trust `outPoint` after an `.end`
  trim (`projects/cbum-last-show/work/storyboard/tl.py`).
- **A by-name ripple (`clip.move()`) does not move the SEQUENCE markers.** After the -0.0667 s cold-open fix every later marker sits
  4 frames late. Re-set markers by name after any ripple, or key nothing off them.
- **On a speed-changed clip, `trackItem.inPoint` / `outPoint` read back DIVIDED by the speed (ABW10 Seq 12, 2026-10-20).** A 0.8x
  clip of a 215.7 s file read in=250.04 s; the real source in point is in × `getSpeed()` = 200.03 s (`outPoint - inPoint` equals the
  timeline duration, not the source span). Anything that pulls source media off `inPoint` must multiply by `clip.getSpeed()`
  (and check `isSpeedReversed()`): `presets/instagram/affanwizu/sequence_reference.py` does.
- **A head trim by `trackItem.start = x` reads back a STALE inPoint too** (cbum-last-show 2026-10-20, seg 4 trimmed 49 frames: inPoint
  still 83.267, it plays from 84.085; outPoint unchanged and right). So after ANY `.start` / `.end` trim, the true source range is
  `outPoint - (end - start)` (head trim) or `inPoint + (end - start)` (tail trim). Better still, keep the plan as the record and
  verify by position and by eye. `projects/cbum-last-show/work/storyboard/apply_ripples.py`.
- **`trackItem.end = x` past the NEXT clip's start is not refused**: it read back as two overlapping clips on V1/A1 (seg 13 extended
  0.4 s while seg 14 had not moved yet). Order every extension AFTER the move that makes room, and read back for overlaps.
- **Plan anchors must be stored at full precision**: a host clip started 0.5 ms before a 3-decimal ripple anchor, was not shifted,
  and kept its gap on the wrong side (`fix_anchor_moves.py`). Compare clip times to anchors at 1e-6, never against rounded values.
- **A STILL's clip inPoint reads ~3600 s** (PNG on a 59.94 timeline, cbum-last-show 2026-10-20). Motion keys written at source time
  0..d sat before the clip, so it showed a static end value instead of the creep. Key stills at `inPoint + t`, and check with
  `getValueAtTime(inPoint + d/2)`. Video clips key at their real source in.
- **`projectItem.changeMediaPath(<a different PNG>, true)` raised a "File Import Failure" modal** that blocked the bridge for minutes.
  Closing it needs the user: posting WM_CLOSE from a script was refused by the permission check. Swap stills by importing the new file
  and overwriting it onto the same slot instead.
- **Overwriting a "90 ms short" clip onto an EXISTING clip leaves the old clip's last ~0.1 s behind**, and the `end` pin then overlaps it.
  After any overwrite-replace, remove the leftovers by name and read back for overlaps (`work/storyboard/replace_stills.py`).
- **`projectItem.setInPoint(t)` FLOORS t to the source's own frame grid, then the placed clip's in lands on the SEQUENCE grid (floor
  again)** (cbum-last-show 2026-10-20). A 3-decimal pick time sitting a hair below its frame start (05 @23.976: 803.886 vs the frame
  start 803.88644) lands one source frame early; the cold-open covers read back 6-41 ms early this way. Aim the in at the frame's
  CENTRE, `(n + 0.5) / fps`, and read back `inPoint` against `n / fps` (`work/storyboard/place_ch.py` reports "in-err"). The
  residual sequence-grid floor (up to 1 timeline frame for 25 fps sources) shows the previous source frame for one timeline frame:
  harmless inside a shot, so keep picks 1+ frame clear of a shot edge.
- **Audio `Volume > Level` reads 0.17782794 at 0 dB**: the scripting scale is `10 ** ((dB - 15) / 20)` (+15 dB = 1.0, -inf = 0).
  Bleep mutes key Level 0.1778 → 0 → 0 → 0.1778 with 5 ms ramps in the clip's MEDIA time (`work/storyboard/place_bleeps.py`).

## 2026-10-21 · THE LAST SHOW redo (cbum-last-show): four findings on a long, heavily layered sequence
- **Opening the sequence (openSequence) keeps Premiere busy for 5-20 s**: the first probe after it reads "MCP Bridge is not
  running" and the window's restore call failed the same way, leaving the creator's sequence switched. `work/active_window.py`
  now retries its probe (12 x 3 s); restore by id again once the bridge answers, and verify with `ping` (`activeSequence`).
- **`createSubsequence` + `overwriteClip` outlasts the bridge's ~4 s patience** and the call reports `bridge_unavailable` while
  Premiere finishes it. Don't retry blindly: wait until `readback()` answers, PROVE the nest from V1 (name + start), then key it
  in a second short call (`work/redo/nests.py`). `app.project.save()` on this project can exceed 45 s: retry the save.
- **Stale in/out points survive a restart**: after scripted `.start`/`.end` trims (2026-10-20) the readback still reports the
  OLD outPoint of 0a-b (and old inPoints of in-trimmed clips) the next day, from the saved project. A span longer than the
  clip is ambiguous (stale in OR stale out): resolve it against the plan's own source times (`work/redo/linemap.py`).
- **An audio clip laid with `overwriteClip` lands on the video frame grid** (start within half a frame of the requested time),
  so a verify must use a half-frame tolerance, not a 2-decimal match.
- (ffmpeg on this PC, 2026-10: `-filter_complex_script` is gone; use `-/filter_complex <file>`.)
- **⚠ `audioTrack.overwriteClip(<an A/V project item>, t)` lays the VIDEO too, on V1, overwriting it.** (2026-10-21, THE LAST SHOW:
  a 254 ms audio "tail bridge" from the 01 vlog, in/out set with mediaType 2 = audio only, came in on V1 as the WHOLE 1816 s
  video from t, replacing every host clip, insert and nest on V1 after 9.6 s.) Never place an A/V item to make an audio-only
  clip: bake the slice to a WAV (gain + fades) and place THAT (audio-only items stay on their track). Recovery that worked
  without closing the creator's project: the last explicit save was clean, so `app.project.importSequences(<copy of the saved
  .prproj>, [<sequenceID>])` imported the clean sequence (+ duplicates of its nest sequences), verified track by track against
  the readbacks, then the damaged one was renamed and moved to a recovery bin. Never save between the accident and the check.
- **Opening a breath in a built timeline by script (2026-10-21, THE LAST SHOW, `projects/cbum-last-show/work/redo/ripple_breath.py`):**
  there is no ripple-insert in the DOM, but `trackItem.move(D)` per clip works if every track is moved LATEST FIRST (no collisions)
  and the shift is whole frames. A clip spanning the point is split by setting `c.end` and re-laying the rest from its own item with
  `setInPoint/setOutPoint(…, 4)` + `overwriteClip` (audio-only items only). The re-laid in-point is FLOORED to the source frame
  (an mp3 came back 23 ms early): read it back and nudge the start by that amount. Markers do not move with clips: delete and
  re-create them. Shift every job JSON's live times after the point in the same run, or the placers drift.
- **A closed-but-kept damaged sequence still gets reviewed:** after a recovery, close the damaged sequence's TAB immediately (the
  creator watched the damaged copy because it stayed open in his timeline tabs).

## 2026-10-22 · gta6-world-stops (ABW10, shared with the English Editor session) — capture + rough-cut notes
- **`workflows/page-record.mjs` (lane-agnostic, logged here because its stills feed the Premiere graphics):** `--hide` is
  applied ONCE, before `--wait`, so late-loading ads come back (Dexerto's `#bottom-adhesion` bar did) → re-apply the hide
  after the wait; Cloudflare "Verify you are human" walls are saved as if they were the article (Digital Citizen, VGC,
  TweakTown) → look at every PNG, never trust the exit code; it prints no headline box → measure it on the PNG. The
  receipts run used a patched scratchpad copy; the repo file is unchanged.
- **WhisperX collapses numeral tokens** ("GTA 6", "14th", "18th" ≈ 0.1 s) and ends them early, so a cut at
  `word.end + 0.08` clips the tail ("for GTSA", "November 14"). Every numeral-final segment gets an exact-span ASR check;
  extend to the measured decay.
- **A burst-timed (explicit) EDL row must be pinned (`no_refine`) BEFORE polish-boundaries**: unpinned, the polisher
  re-snapped two of them to a WhisperX merged-repeat word ("January." 996.9–998.2) and would have cut a line to nothing.
- **A dead-air split can eat a QUIET word**: the gate's −36 dB threshold read a soft second "fucking" as silence; split
  at its real onset (ASR-verified) instead of the gate's run end.
- **`createNewSequenceFromClips` opened the new sequence (made it ACTIVE) and laid the clip on V1/A1** — run it inside
  ACTIVE-WINDOW.lock, empty the tracks, restore the previous active sequence by id (`projects/gta6-world-stops/transcript/seq23.py`).
- **QE `setSpeed` is NOT a scriptable slow-down on Premiere 2025 (tested on the last clip of "GTA 23 - The Day The World
  Stops", 2026-10-22).** `setSpeed(80, true)` (the vendor MCP's 2-arg form) throws "Not Enough Parameters".
  `setSpeed(0.8, "", false, true, false)` sets ONLY that V1 item to 0.8 — its timeline duration does NOT change (it plays
  0.8 × the source span, the DOM inPoint reads divided by the speed) and the linked A1 clip stays at 1.0 → picture/sound
  desync. Setting it back with `setSpeed(1, …)` read back **0.80427, not 1**. Repair = remove the V1 + A1 pieces by name
  and overwrite the segment again from the EDL (speed 1 on both). → Joke slow-downs stay the creator's (Rate Stretch /
  Ctrl+R takes him seconds); flag the beats, don't script them (`projects/gta6-world-stops/transcript/speed-test.py`).

## 2026-10-22 · streamer-content-machines (ABW10 › "CA-007 Streamer Tier List", 59.94, shared with the Afterhours session)
- **QE `razor(tc)` reads the timecode string in the SEQUENCE's display format, and a 59.94 sequence made with
  `createNewSequenceFromClips` from a 59.94 camera clip displays DROP-FRAME (`getSettings().videoDisplayFormat` = 106).**
  `face-pass.py` built NON-drop strings (`f // 60` seconds, `:` separators): 5 razors in the first minute landed right, the
  other 39 landed 4 frames EARLY per elapsed minute (−4 … −24 frames). Fix: build DF numbering from the frame count:
  `f = round(t*60000/1001); D, M = divmod(f, 35964); fn = f + 36*D + (4*((M-4)//3596) if M > 3 else 0)`, then
  `HH;MM;SS;FF` from `fn` at 60 per second (`projects/streamer-content-machines/work/face_pass.py` `tc()`). Read
  `videoDisplayFormat` before any QE timecode call; verify every razor by position afterwards (the face pass does).
- **⚠ CORRECTED 2026-10-23 — `L.end = x` does NOT extend a clip, it SLIPS it.** The 2026-10-22 "heal" (remove the right
  piece R of a razor, then `L.end = R_end`) kept L's OUT point and moved its IN point back by R's length: the picture
  played up to 4 s EARLY against the voice on A1 (the creator saw lips out of sync at 1:24, 1:56, 2:50, 3:22, 3:49, 4:59,
  5:50; `projects/streamer-content-machines/work/sync_audit.py` found 50 of 203 V1 pieces off, −3 … −240 frames). Every
  V1 read-back gate passed because none compared V1 in-points with A1. **Never heal a razor this way; rebuild V1/A1 from
  the EDL instead, and after ANY V1 edit run a picture-vs-voice offset audit (V1 `inPoint − start` must equal the A1
  clip's under it, within half a frame).**

## 2026-10-22 · gta6-world-stops (ABW10 › "GTA 23 - The Day The World Stops") — graphics + face-pass notes
- **The DF razor fix holds:** `projects/gta6-world-stops/transcript/face-pass.py` reads `videoDisplayFormat` (106) and
  builds `HH;MM;SS;FF` drop-frame strings with the formula above: 36 razors across 7:55, every one verified ON its planned
  frame by position, A1 untouched (175 → 175).
- **`clip.end` set in SECONDS can land short of a butted neighbour:** a V2/V3 end set to the next clip's start (+1e-4 s)
  read back 0.4 ms early (16671.97 frames), because the setter will not overlap the neighbour. Set the end in exact
  frame TICKS instead: `t.ticks = String(Math.round(end * 254016000000 / 4237833600) * 4237833600)` (59.94 = 4237833600
  ticks per frame) → on the boundary, both sides read back the same frame (`hf-graphics/place-seq23.py --fix-ends`).
- **Plan edges must live on the frame grid, not just on V1 cuts:** a word-anchored out-point that is not on a cut stayed
  sub-frame after placement (15 of them, gate OFFGRID). Round every non-cut edge UP to the next frame in the plan
  (overwriteClip already rounds a start up), then check each render still covers its slot before pinning
  (`projects/gta6-world-stops/build-plan.py` § FRAME GRID; `review/gate-frames.py` now fails OFFGRID).
- **Two SFX tracks hold a dense graphics pass if the planner counts collisions first:** 96 cues, one collision (four
  legend ticks 0.3 s apart under a 2.5 s hit) — drop the long cue rather than adding a track mid-session (adding one
  needs the active-sequence lock).
- **`audio-polish.py --verify` reads the ACTIVE sequence, not the job's:** run outside the lock it reported "A1 clips 1 · no
  chain" off the creator's Sequence 19 (read-only, nothing written). Wrap it like `--apply`, inside `active-window.py`
  (EXPECT_A1 = the job's A1 count): 175/175 verified there.
- **After a machine crash, a render that logged `exit=0` can still be a broken file:** `c41-alpha-c.mov` (rendered
  minutes before the crash) had no moov atom (576 KB instead of ~550 MB: the OS never flushed it). Importing it opened
  a modal **"File Import Failure"** dialog that BLOCKS the bridge — every call then answers `bridge_unavailable` while
  Premiere itself reads "Responding". Before any import after a crash: `ffprobe` + a full decode (`ffmpeg -i f -f null -`)
  of every render/plate. To see a modal: enumerate the Premiere process's visible top-level windows (EnumWindows +
  GetWindowText); an error notice can be dismissed with WM_CLOSE (PostMessage 0x0010), then the bridge answers again.

- **2026-10-23 · Censoring a word on a linked A1 (GTA 23 review 1):** QE razor on `getAudioTrackAt(0)` at the two word edges
  (DF timecode on a drop-frame sequence) splits ONLY A1 (V1 count unchanged, read back), then `trackItem.disabled = true` on
  the A1 piece silences it with its picture playing on (reversible: re-enable = word back). 10 ms Volume Level keys on the
  neighbours (`setTimeVarying(true)`, keys in SOURCE time = inPoint + offset; 0 at the edge). Razor AFTER audio-polish: the
  pieces inherit the Amplify + Hard Limiter chain. `transcript/place-censor-seq23.py`.
- **`audio-polish.py --verify` re-measures the gain** (voice-gain.py, ffmpeg per segment over the raw) before it reads the
  chain back: > 10 min on a 7:41 cut, all of it INSIDE the ACTIVE-WINDOW lock with Premiere idle. Expect it; don't kill it.
- **The ACTIVE-WINDOW helper runs its command from the repo root:** pass ABSOLUTE script paths (a relative
  `transcript/x.py` opened the window, failed to start, and closed it: harmless, but the step silently did nothing).
- **FCP XML audio tracks are MONO pairs:** a stereo Premiere track exports as two XML tracks (A1 → XML A1+A2 …), so an XML
  "A8" is Premiere's A4. Count tracks from the sequence, never from the XML.
- **FCP XML drops Scale Width:** a Uniform-OFF stretch exports as scale + a Center offset; read stretches from the DOM.
- **Clip-level SFX tails:** trim each SFX clip to where its tail is 40 dB under its peak (`clip.end` by ticks after the
  overwrite); a 3.35 s cinematic thud occupies a track for 2.3 s instead, so 100 cues fit on A2/A3.
- **2026-10-23 · A creator RIPPLE between two of my write batches shifts everything after it, and a plan-time re-place then
  lands late:** he trimmed 0.35 s at 0:30 of GTA 23 after my save; `stable.py` (a 45 s stillness check) passed, my placer
  matched rows to the timeline with ±1.5 frames, found 77 graphics "missing", and re-laid them 0.35 s late (leaving 0.35 s
  head slivers of his shifted copies). Before ANY re-place on a timeline he may have touched: diff the live SFX/graphics
  starts against the plan (a uniform offset after one time = his ripple), rebuild the EDL from his V1 source in-points
  (merge contiguous clips), adopt it, re-run the plan, THEN place. Never trust a stillness check as a "no edits" check.
- **A render overwritten in place after Premiere imported it goes OFFLINE (red "Media Offline" thumbnails), 2026-10-26
  (paris-jackson-both-versions, co-nouns.mp4 + co-headlines.mp4).** `FORCE=1 render.sh` rewrote two placed comps after a re-time;
  the project items kept their old duration and `isOffline()` read true, while two other overwritten renders happened to refresh.
  The rule render.sh already states holds: **never FORCE over a placed file, render `VER=b`** and re-place; verify every placed
  item with `projectItem.isOffline()` (work/place_co.py --verify does). Superseded offline items left unused in the bin.

## 2026-10-26 · audio chain, DeNoise order, eased nests (paris-jackson-both-versions, ABW10)
- **One QE call adding Amplify + Hard Limiter to 141 A1 clips outlived the bridge timeout:** the bridge answered "MCP Bridge is not
  running" while Premiere finished every add (read back 141/141, none doubled). The script's cleanup died with it, so the
  ACTIVE-WINDOW.lock and the other session's active sequence were left behind until restored by hand. Now: 15 clips per QE call, and
  the restore + lock release sit in a try that survives a bridge error (`work/audio_chain.py`).
- **QE `addAudioEffect` APPENDS:** a DeNoise added to a clip that already has Amplify + Hard Limiter lands AFTER the limiter. To keep the
  ceiling last: find the QE component whose `getParamList()` holds "Maximum Amplitude", `.remove()` it, re-add Hard Limiter, set its
  value again by DOM, read the order back (Volume > Channel Volume > Amplify > DeNoise > Hard Limiter). QE components expose
  getParamList / getParamValue / setParamValue / remove; QE tracks also expose `addAudioEffect` (track effects, unused).
  `work/denoise.py`. DeNoise DOM params: Amount (0-1, default 0.4), Make-Up Gain, Auto Gain, Shelve Type, Output Difference Signal.
- **`setInterpolationTypeAtKey(key, 5)` on a 2-key Motion > Scale read back LINEAR** (the quarter point sat at exactly 25 % of the
  push). Ease = sine.inOut sampled every <= 0.25 s with linear keys (`work/face_nests.py`); the quarter then reads 14.6 %.
- **Audio in-points snap to the sequence frame grid:** music pieces placed with `setInPoint(x, 4)` read back up to ~30 ms early at
  59.94; verify with a 2-frame tolerance and key fades off the READ-BACK in-point.
- **Level keys that only attenuate make the ceiling order-proof:** put all gain (level match included) in Amplify ahead of the Hard
  Limiter and keep Volume > Level at a 0 dB plateau with only fades / mutes; whichever side of the clip effects Premiere runs the fixed
  Volume, nothing can push past the limiter.
- **Audio crossfades by script (B4 "2-4 frame crossfades on every dialogue cut"):** QE `trackItem.addTransition(transition, atStart, duration,
  offset, alignment, singleSided, alignToVideo)` (reflected signature: Object, boolean, string, string, number, boolean, boolean) on the
  INCOMING clip of a butt joint: `qi.addTransition(qe.project.getAudioTransitionByName("Constant Power"), true, "00;00;00;03",
  "00;00;00;00", 0.5, false, false)` lands a 3.00-frame Constant Power centred on the cut (read back on the DOM track's `transitions`:
  start/end). Clip edges do not move; needs the sequence active (locked window). Audio transitions listed by QE: Constant Power,
  Constant Gain, Exponential Fade. 15 per bridge call outlived the bridge once (Premiere finished the chunk); 8 per call was clean.
  `projects/paris-jackson-both-versions/work/a1_fades.py`. QE sequences expose no master track (no bus limiter by script).

## 2026-10-27 · batch-5 reactions v2 (Affan's review: whole intro, SFX by loudness)
- **Camera in-points: ask for the time Premiere's DOUBLE floor turns into the nearest frame.** `setInPoint(f(t) + 1e-4)` on a 59.94 fps
  camera in a 60 fps sequence floors twice and lands −1…−32 ms early. `build_seq3.py --place --nearest` requests `ceil(g·59.94)/59.94 +
  2 µs` for the 1/60 grid point g nearest the sync line: measured −8.3…+12.0 ms over 165 clips (3 sequences), lip sync ≤ 8.8 ms.
- **lipsync.py on a clip INSIDE a sample play is not evidence** (he is silent; peak ≤ 5x mean, lags of 30-113 ms): read only talk clips.
- **A gated SFX level must be written LAST.** build_plan.py rewrites plan.json (cues back to [t, name]); apply.py then fell back to the
  peak rule (10-20 dB louder). apply.py now refuses a `sfx_gated` plan with any cue lacking its level: order build_plan → facex →
  facefix → `tools5/sfxgate5.py --write`.
- **Measure SFX loudness in STEREO.** A mono fold-down under-reads a wide Epidemic swish by up to 5.5 dB (mid vs channel power), so a
  "−18 LU" swish could really sit −13 LU under him; sfxgate5 sums the K-weighted channel powers for him (the OBS stereo A1) and the slice.
- **The music bed as pieces** (`plan.music.gaps`): apply.py places one piece per gap-free span with CONTINUOUS source in-points; a
  placed piece can land one frame long (19.150 vs 19.133): the end is now forced when it is > 4 ms off (was 20 ms).
- **polish-boundaries keeps a WhisperX-stretched word's first burst only** (Brad "I" 181.33-182.51 = "I" + the false start "have"):
  a word check by midpoint calls it missing; `tools5/introcheck.py` counts a word present when >= 60 ms from its start plays.
- **A retake inside one keep range survives the gap split** (MATG "butter which | which is why": the first "which" sat inside the
  kept segment's tail): scan unkept word indices against the kept A segments after every new keep range (pinned out, 64.18).
- **pins.py is re-run safe** (`--rerun`): a pin whose boundary already sits at its target (within half a frame, seqmap3 snaps) is skipped.
- Epidemic risers with a pitched sweep fail the tonal gate (clean riser 01: 24-27 dB, cymbal reverse: 40 dB, whoosh short 02: 29 dB):
  a REVERSED airy swish from the job's own set is a clean soft riser (tonal 12-13 dB).

## 2026-10-27 · batch-5 reactions (Brad Lea, Fantasy Footballers, MATG; ABW10, shared with two other sessions)
- **`Sequence.clone()` MOVES the active sequence to the clone** (build_seq.py `--create`): "Brad Lea reaction" became active
  right after the clone, read back by DOM + QE. `--create` now runs inside `ACTIVE-WINDOW.lock` through
  `projects/_onyx-batch5-2026-10/reactions/tools5/inwindow.py <cmd>` (reads the active id + QE name before, reopens it by id after,
  proves it). Any other session's DOM-only tool that clones a sequence needs the same wrapper.
- **apply.py windows now PROVE the switch** (`open_window` / `prove` / `close_window`): openSequence(id), 1.5 s, then DOM
  activeSequence.sequenceID == ours AND QE getActiveSequence().name == ours AND the A1 clip count matches, else it reopens the
  previous sequence and refuses. `--window` proves again right before and after `audio-polish.py` (which works on the active
  sequence). Saves (`--overlays`) wait while ANOTHER session holds ACTIVE-WINDOW.lock (`safe_save`, max 10 min).
- **apply.py, backward compatible:** `plan.sfx_dir` (job-local SFX slices, looked up before the kit; peaks measured by volumedetect,
  never guessed), whoosh class also for `*whoosh*/*swish*/*swoosh*` slice names and `plan.sfx_whoosh` (the kit test was
  `startswith("whoosh")`: a `cd2-whoosh-*` would have landed 9 dB too hot), `plan.voice_gain_ranges` [[from, to, gain]] (the inserts'
  own gain, audio-polish `--range` inside the same proven window). Backups `apply.py.bak-2026-10-27`.
- **overlays.py, backward compatible (DSH stills byte-identical before/after at 6 times):** entrances `push` / `focus` / `drop`, kinds
  `ink_reveal` (FX-15: a red ink blot from a face on the screen, revealing a ba_wipe master card's first frame), `rows_blur` (FX-35)
  and `quadrant` (FX-69/70), `ba_wipe.fade_in` (0 when an ink lands on its first frame). Backup `overlays.py.bak-2026-10-27`.
- **`overlays.py --still` WRITES `<job>/work/stills.jpg`** (overwrites, no new name): a regression still run on another job clobbers
  its preview sheet (it did: dsh-marriage-contract-reaction/work/stills.jpg, a regenerable preview, was overwritten). Regression
  stills: call `overlays.still()` from a scratch script and save elsewhere.
- **`voice-gain.py` on a reaction measures the samples too:** Brad's kept mix read -23.8 LUFS (+7) but his talk alone -29.5 (+12);
  the OBS mix plays our samples / their Short ~8 LU over his voice. Gain set from his talk (+11: limiter on 6 % of 10 ms windows),
  the inserts +4 (both land -19 LUFS after the -6 dBFS limiter, simulated with alimiter).
- **WhisperX squeezed "600" into a 60 ms token again** (Brad "I've done 600 million", raw 172.68): the real "six hundred" sat in the
  "gap" 172.81-173.38 and author3 split there (jointcheck heard "I've done a million views"; falign found nothing after "done").
- **The GPU was held 35+ min** (another session's transcribe.sh + a Topaz run without the lock, 100 % / 7.9 of 8 GB): jointcheck runs
  on CPU with `CUDA_VISIBLE_DEVICES=""` (its own fallback), tightasr via `tools5/tightasr-cpu.sh` (`WHISPERX_DEVICE=cpu`).
- `tools3/xplay2.py` needs the whisperx venv python (scipy). **The YouTube and Instagram masters of a sample share ONE audio
  track**, so xplay2 matches both at every play: name each play by the higher ncc (1.00 vs 0.90) and its frame, never by the file.

## 2026-10-27 · shorts-cooked-not-your-fault (the @affancuts organic reel, reaction toolkit, ABW10)
- **`build_seq.offset_fn` fits a line through the windows with peak >= 10 and drops the rest:** on C1407 it kept 3 of 4 and fitted
  **+114.8 ppm** (33 ms over the file) where the sync report says 0.1 ppm over all four (7 ms scatter). Long-window GCC-PHAT on the
  whole file reads -1.6 … -8.2 ms against the constant 92.4972 s. Use `"offset": <s>` in seq.json when the report's slope is ~0.
- **A short plain ncc on a near-silent camera mic (speech at -57 dBFS) is noise** (+35 ms median "lag", ncc 0.3); GCC-PHAT per clip
  reads -8.4 … +4.3 ms on all 47 face clips. Lip-sync proof = GCC-PHAT (`projects/shorts-cooked-not-your-fault/work/sync_proof.py`).
- **`overlays.still()` renders every frame from a graphic's t0 up to t** (O(n) per still): ten stills on a 12 s group took > 10 min.
  Random-access kinds can be sampled directly (`fn(i)`): `mgx.py --still` there does it in ~10 s per still.
- **`card_style: "glass"` makes `card_body()` ignore `fill`**: a gold / white / dim tile came out as the glass card. Coloured shapes
  call `O.rrect()` directly.
- **polish-boundaries on a 0.30 s-gap cut** added 5.5 s, clipped the end of "views" (77.49 vs 77.54 raw) and the S of "Scott"
  (222.86 vs 222.70: Whisper then heard "God trusted me"), and re-joined two segments across a deliberately dropped restart ("moments
  from [any part from] every podcast"). Every polished edge was re-measured (falign / endtest / dip) before jointcheck.
- **ProRes overlay renders die mid-file when RAM runs out** (0.7 GB of 31.7 GB free with three sessions + Topaz: ffmpeg "Cannot
  allocate memory", BrokenPipe in overlays.build_mg after 8 of 15 layers). `--check` does not read the movs: ffprobe every
  `overlays/mg/*.mov` frame count against round((t1 - t0) x 60) before anything is placed.
- **Premiere floors a subclip in-point TWICE** (`setInPoint(t, 4)` on a 59.94 camera subclip, overwriteClip into a 60 fps sequence):
  to the camera frame, then to the sequence's 60 grid. The model `floor(floor(t·59.94)/59.94·60)/60` reproduced all 49 read-backs to
  0.00 ms; every in-point sat 14-30 ms early (the lab-note "−1…−32 ms, Premiere's frame snap" above is this). Choosing each request so
  the double floor lands on the 60-grid point nearest the sync line gives a constant +2.8 ms here
  (`projects/shorts-cooked-not-your-fault/work/fix_v2.py`: V2 cleared and re-placed by name, then `build_seq3 --style --verify`).
- **An SFX tail can outlive the picture**: the last cue's 1.6 s slice ran 0.43 s past V1 (sequence end 84.25 vs 83.82) and
  `tools5/bedtrim.py` only trims the bed. Read the max clip end over ALL tracks after `--overlays`; trim the overhang to V1 with a
  short Volume ramp (DOM, by name).
- **The Bash tool's quoted heredoc collapsed each doubled backslash to a single one** in a JSON file (a Windows path became an
  invalid escape): write JSON with python (json.dump), never through a heredoc.

## 2026-10-27 · iphone-duo-clip-angle (ABW10 › "CA-009 iPhone Duo Clip Angles", 59.94 DF, shared with Onyx + GTA 24 sessions)
- **`audio-polish.py --apply` SAVES the whole project at the end** (`if (APPLY && !out.bad.length) app.project.save()`): on a shared
  project that is a save nobody cleared with the other sessions, possibly mid-window. Workaround: a job-local copy without the save
  (`projects/iphone-duo-clip-angle/work/audio_polish_nosave.py`), run in 4 timeline ranges (`--range`) inside one ACTIVE-WINDOW
  lock (`work/audio_chain_run.sh`): 138/138 clips, no bridge timeout. Suggest a `--no-save` flag on the lane tool.
- **V1 laid with zoom edges PRE-SPLIT needs no QE razor and no active window**: replay linked A/V by name, then overwrite V1 from a
  video-only subclip (`createSubClip(…, takeVideo=1, takeAudio=0)`) at the A1 positions split at every face-pass edge
  (`work/rebuild_v1.py`): 206 V1 pieces, A1 untouched (138), sync audit 0 off on the first try.
- **`timeline_words.py`-style readers must read A1, not V1, after a pre-split rebuild** (V1 is no longer clip-for-clip with the EDL).
- **(later, 2026-10-27) Program-monitor grabs lag on a loaded machine:** with the CPU saturated (other sessions' WhisperX / Topaz /
  renders) the monitor rendered 1-3 grabs behind at the 2.5 s settle, so the sheet's tiles showed their neighbours' moments.
  `apply.py --grab-only` now reads `GRAB_WAIT` (s, default 2.5); 12 s gave in-sync sheets.
- **A bridge drop INSIDE `--grab-only` left OUR sequence active** (the finally's restore failed with the same "MCP Bridge is not
  running"): restored by id with `tools5/restore_active.py "<name>"` (inside the lock, DOM + QE proof). apply.py's `es()` now rides out
  "bridge is not running" for ~2 min (12 tries), as it already did for bridge_unavailable.
- **Five SFX vanished after a dense `--overlays` pass** (MATG: two clips 30 ms apart on A2/A4, another 0.5 s later): every placement
  read back "ok" and one level step said NOCLIP, yet the sequence held 37 of 42. A clean re-run (our SFX cleared and re-placed, the
  sub moved 0.2 s off the taiko) placed all 42 and `--verify` passed: always trust `--verify`'s SFX count, never the placement log.
- **The music bed lands one frame past V1** (apply.py tolerates 20 ms), so the REAL sequence end was one frame long:
  `tools5/bedtrim.py <plan>` trims it to V1 (DOM by name). Run it after every `--overlays`.
- **Lip sync from the sequence** (`tools5/lipsync.py`): camera in-points sit −1…−32 ms (mean −16, Premiere's frame snap) off the
  sync line in all three jobs, inside build_seq's 35 ms tolerance; GCC-PHAT on his talk clips 7-30 ms. Readings inside a sample play
  (the camera hears the speakers) are not lip sync: skip them.
- **A per-stretch WhisperX chunk can come back near-empty** (MATG's last 26 s stretch: only its final sentence, placed at the stretch
  start): check every stretch's word count; fall back to seqmap3's raw-mapped words for that stretch (`words.tight.raw.json`).

## 2026-10-27 · gta6-day1-mistakes (ABW10 › "GTA 24 - 14 Mistakes On Day 1", shared with AffanWiz + Onyx, the creator reviewing live)
- **Never run audio-polish.py --apply inside ACTIVE-WINDOW.lock with the gain unmeasured.** Its voice-gain measurement ran >25 min
  inside the window (242 spans, ffmpeg per span on an 8 GB raw, CPU shared with renders); meanwhile the CREATOR opened another
  sequence ("MATG reaction") while reviewing — and audio-polish applies to the ACTIVE sequence. It happened to time out before the
  apply. Now: measure the kept speech OUTSIDE the lock (one pass: extract the voice once, join the EDL spans, ffmpeg ebur128 →
  gain = −17 − LUFS), then `audio-polish.py --apply --gain N` inside a SHORT window; batch every active-sequence step (chain,
  censor razors, A1 crossfades, face razors) into ONE window (`projects/gta6-day1-mistakes/transcript/window1.py`): 1 min, not 25.
- **A process tree killed by `timeout` skips active-window.py's `finally`**: the lock file stays and the prior sequence is not
  restored. Release the lock by hand (rm the one file) and do NOT restore an old sequence over what the creator has open now.
- **gate-frames counted INVISIBLE razors as cuts**: a zoom extended over a piece that runs under a graphic leaves a razor between two
  pieces with continuous source and identical Motion — not a cut anyone sees. The gate now drops those before the SLIVER test.
- **Render-cache hashes must ignore the comp's timeline comment** (`// id · timeline START → END`): it changes on every re-time
  and forced a full re-render; `hf-graphics/gfx/render-changed.sh` hashes the HTML without it.
- **A Claude session running in a git worktree cannot Write/Edit the main checkout's gitignored job folder** (a PreToolUse hook);
  `request_directory` did not lift it. Job files were written with the shell; subagent briefs must say so.
- **The plates' b-roll "soft shadow" was an 18 px HARD slab** (video 23's build-plates.py, carried into 24): `boxblur` on a layer the
  size of the inset cannot spread past its own canvas, so the shadow ended in a straight edge under the rounded corners. Pad the
  shadow layer BEFORE the blur (`pad=iw+160:ih+160:80:80:color=black@0,boxblur=30:2`, overlay centred, +14 px). Any job copying
  that builder: fix it there too (`projects/gta6-world-stops/hf-graphics/gfx/build-plates.py` still has the old line).
- **Re-timing placed graphics:** `place-seq24.py --remove <ids>` then `--apply` (plates + overlays by name); SFX with
  `place-sfx-seq24.py --prune --apply` (prune drops cues the plan no longer has, only from the job's sfx dir), then gate-frames.

## 2026-10-27 · INCIDENT: a test deleted another session's sequence (paris-jackson-both-versions, review 1)
- **`app.project.sequences` is ordered by sequence ID, NOT by creation.** A clone test took `sequences[numSequences - 1]` as "the clone
  just made"; it was another session's "Fantasy Footballers reaction" (highest UUID). The script renamed it, ran QE extracts on it
  (they did nothing: 0 s) and `deleteSequence`d it. The real clone ("<name> Copy", a lower UUID) stayed. Restored with
  `app.project.importSequences(<copy of the last saved .prproj>, [id])` from the save made minutes before (no Undo: another session's
  latest step could have been undone instead). That import kept Premiere busy ("not responding") for minutes.
- **Rules now:** find a clone as the ONE new sequence ID after `clone()`, named exactly "<source> Copy"; never rename anything you did not
  just make; delete only an ID you created in this run AND whose name you checked. `clone()` makes the clone ACTIVE: restore the
  sequence that was active before the test, by ID.
- **QE `sequence.extract(inTC, outTC)`** (two timecode strings, the sequence's display format: 59.94 DF here "HH;MM;SS;FF"): the ripple
  extract across the targeted tracks. Prove it on a correctly identified clone before the real sequence.

## 2026-10-28 · frame grabs on a 59.94 DF sequence, PNG gamma in HyperFrames (paris-jackson-both-versions, review 2)
- **`premiere-bridge.mjs frame` grabs the WRONG frame on a drop-frame sequence, and on this transport it does not run at all.**
  (a) It builds a NON-drop "HH:MM:SS:FF" from the frame count; on a 59.94 DF sequence QE reads it as a DF label, so the grab lands
  early by 4 frames per elapsed minute (minus the tenth): 0.4 s at 6 min, 0.8 s at 13 min. Build the DF label: f += 36·⌊f/35964⌋ +
  4·⌊(f mod 35964 − 4)/3596⌋ (when f mod 35964 > 4), separators ";". Proven by a dissolve landing exactly where its keys are.
  (b) Its ExtendScript carries `//` comments; the file transport collapses newlines, so CEP evalScript fails ("host-side scripting
  failure"). Workaround: `projects/paris-jackson-both-versions/work/review2/grab_frames.py` (comment-free QE call, DF label, under
  ACTIVE-WINDOW.lock). Fixing the bridge itself is open.
- **`exportFramePNG` wants a BACKSLASH Windows path.** "X:/dir/name" throws "Unknown error exception"; "X:\dir\name" works (spaces
  are fine). And a dot in the name is taken as the extension: "end-790.60" writes "end-790.png" (grabs silently overwrite each other).
- **A PNG from ffmpeg carries gAMA/cHRM chunks; Chrome (HyperFrames) applies them, and the frame renders ~24 % darker** (a held frame
  of a graded card: mean 51.7 → 39.4). Re-save through PIL (`Image.open(p).convert('RGB').save(p)`: no chunks) before an <img> in a
  comp; after: 49.9. Any comp that shows a frame grabbed by ffmpeg next to the same footage needs this, or the cut into it jumps.
- **Premiere's auto-save blocks the bridge (2026-10-29).** While the title bar reads "Auto Saving Project: ABW10.prproj" every
  `execute_extendscript` / `ping` times out ("bridge_unavailable") although the process reports Responding; a big project
  (130 sequences, from a deeply nested Auto-Save path) held it 10+ minutes. A failed read-back then looks like "the sequence
  changed": check the reply is not an error before comparing. Wait it out with a background ping loop; never restart Premiere.
  Kane job, same day: a `create_seq.js` clone sent as the save began timed out at 45 s yet COMPLETED after it (the sequence
  existed at 14:31); the calls chained after it never ran, and Premiere showed "Not Responding" at ~0 % CPU until then.
  So: one call per command (never chain on a failed one), read the state after recovery, resend only what is missing,
  and check the window title for "Auto Saving" before every call.
