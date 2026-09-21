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
