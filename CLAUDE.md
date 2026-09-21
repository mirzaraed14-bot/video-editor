# CLAUDE.md — Video Editor

Your **video production & editing department** — and **only** that. Raw filmed footage comes in, a
finished exported cut goes out: point it at a raw clip and it takes that clip from **raw → fully
edited → exported.** What happens afterward (posting, scheduling) is out of scope. Not a traditional
code repo — a content system where **Claude IS the editor**, one skill per stage in `.claude/skills/`.

---

## 🪟 On Windows? One check first

This system runs natively on **macOS, Windows, and Linux** — no virtual machine. On Windows the
`.sh` scripts run through **Git Bash** (installed with **Git for Windows**), the same shell Claude
Code itself uses. Run `uname -s`: `Darwin` / `Linux` / `MINGW…` / `MSYS…` → you're set, go to **FIRST
RUN**. A command-not-found or PowerShell-looking answer (`C:\…` paths) → Git for Windows is missing:
have the user run `winget install Git.Git` in PowerShell, restart Claude Code, re-check.

> Windows notes: installs go through **winget** (`./check-setup.sh` prints the exact command per
> tool), each followed by a new terminal and one Claude Code restart so PATH updates. Python there is
> `python`, never `python3` (a fake Store stub — the scripts handle it). Apple's hardware encoder is
> a Mac-only speed perk; Windows and Linux render in software, same result, and an NVIDIA GPU is
> auto-detected for transcription. Keep the project folder OUT of Documents, Desktop, Pictures,
> Videos, Music and OneDrive: Controlled Folder Access blocks writes there for Git Bash, node and
> python, and the error reads "No such file or directory", not "permission denied". `./setup.sh`
> checks this first and prints the fix (move the folder, or allow the four apps).

---

## 🚦 FIRST RUN — onboarding gate (read this before doing anything else)

**The first thing to handle when the project opens.** A SessionStart hook
(`.claude/hooks/setup-check.sh`) nags for as long as setup is incomplete. Trigger this flow on **"run
the setup"** / **"set me up"** / **"continue setup"**, **or** on any request to edit a video while
the tools are missing (an edit cannot run without ffmpeg).

**Is setup done?** One deterministic check: the marker file **`.setup-complete`**, one line,
`lane=<premiere|resolve|capcut|chat-only|pending>`, written by `./setup.sh` once every core tool
verifies. **Missing** ⇒ run the flow below. **`lane=pending`** ⇒ tools done, the which-app question
still open: ask it, then record the answer with `./setup.sh --lane <pick>`. **A real lane** ⇒ done,
skip this gate and work normally (on "continue setup", re-run `./setup.sh` once, verify the lane,
make step 3's offer). That `lane=` line is what every edit reads to know its finish surface.

**The goal: core editing working, fast, with near-zero effort from the user.** Personalization is
OPTIONAL and comes last. The presets ship with a neutral bundled look (Inter fonts, a generic
starter palette, no handles), so nobody else's brand can leak into a video.

1. **Tools: run `./setup.sh` yourself.** Don't ask first and don't hand over a command list; say
   what it's doing as it goes. It detects the OS (macOS → Homebrew, Windows → winget), installs every
   missing core tool, bootstraps the render engine (`npx hyperframes@0.8.16 browser ensure`; its npm
   and telemetry chatter is noise, and the version is pinned — never run `hyperframes upgrade`),
   verifies with `./check-setup.sh`, then probes for editing apps. It is **idempotent: re-run it
   after any interruption.** Its exits:
   - **exit 0** with an `ACTION FOR CLAUDE` line: several editing apps found → step 2. Without one:
     done, `.setup-complete` says which lane → step 3.
   - **exit 2:** this session can't see something just installed (Windows tools after winget,
     Homebrew's PATH on a Mac). Restart, then re-run `./setup.sh`. **exit 3:** it wired a lane into
     `.mcp.json` — restart, then verify the lane.
   - **exit 1:** read the output. Homebrew missing → the user runs the printed one-liner themselves
     (it needs their password), then you re-run `./setup.sh`. Tools still missing → `check-setup.sh`
     printed the exact command per tool: run the brew ones yourself, the user runs the `apt install`
     ones (sudo). A lane installer failed → fix it, then `./setup.sh --lane <that app>`.
   Loop until `./check-setup.sh` shows every core item ✓. (Manual per-OS list: `SETUP.md`.)
2. **Editing app lane: auto-detected, at most one question.** `setup.sh` probes for Premiere Pro,
   DaVinci Resolve and CapCut and records the outcome as the `lane=` line. **One app** → already
   settled: Premiere/Resolve ran their installer (`./setup-premiere.sh` / `./setup-resolve.sh`) and
   exited 3, CapCut needs no install. **Several** → ask ONE line ("Premiere, Resolve and CapCut are
   all here: which do you edit in?"), then run **`./setup.sh --lane <pick>`** yourself; the pick is
   final, never switch unless asked. **None** → `lane=chat-only`: say so in one line, move on, never
   re-ask at edit time.

   **Verify a wired lane after the restart.** First the MCP: its tools must be present in the
   session. If not, the `.mcp.json` servers weren't approved — Claude Code asks on reopening and the
   user must answer **yes**; a "no" is remembered, so the fix is `claude mcp reset-project-choices`
   (run it yourself), one more restart, and a yes. Then the app: **Premiere** → run
   `./lanes/premiere/premiere-up.sh` and confirm `node lanes/premiere/premiere-bridge.mjs ping`
   answers (only if it fails, fall back to **Window → Extensions → MCP Bridge (CEP) → Start Bridge**).
   **Resolve** → ask the `davinci-resolve` MCP for the version, with Resolve running; don't send
   anyone into Preferences, External scripting = Local is its shipped default. **Free edition**
   (the `davinci-resolve` entry in `.mcp.json` carries `DAVINCI_RESOLVE_BRIDGE`): the user must
   first open a project and run **Workspace → Scripts → resolve_bridge** inside Resolve, and every
   Resolve restart needs it again, so say so before the first Resolve call of every session. A
   `BRIDGE_UNAVAILABLE` answer means it isn't running: ask for it, never retry in a loop.
3. **Brand kit: OPTIONAL. Offer once, never block.** Say the editor already works with the neutral
   bundled look, and that whenever they want captions and graphics to sound and look like them they
   can fill in [`brand-kit.md`](brand-kit.md) and say **"apply my brand kit"** (you then follow the
   file-by-file map in its Part B and render one test). Don't walk them through it unless asked.

**Restart walkthrough (be exact and friendly):** *"Quit Claude Code completely (Cmd+Q on Mac / close
the app on Windows), reopen it, open this same folder, and say **continue setup**."* After an MCP was
wired (exit 3), add: *"When it reopens and asks whether to enable the MCP servers, answer yes."*
Never assume a restart loaded anything — verify it.

---

## Brand Kit

The editor's voice and look come **entirely from [`brand-kit.md`](brand-kit.md)** and the presets it
feeds; the signature look is locked in
[`presets/instagram/explainer/signature-style.md`](presets/instagram/explainer/signature-style.md).
Apply both verbatim. Filling the kit in is optional — editing works before any personalization.

---

## The Pipeline — one linear flow, every time

Every job runs the **same eight steps, in order**, raw → done, each finished to its own definition of
done before the next starts. The run is owned by the **`edit-video`** skill, which keeps
`projects/<job>/RUN.md` so it survives a context compaction and resumes cold.

**The finish surface is your editing app by default:** a bare "rough cut" with no lane named means
the lane recorded in `.setup-complete`. A machine recorded as `lane=chat-only` is already on the chat
finish, so never re-ask; on a machine WITH an app, chat-only runs only on an explicit yes to "want
this done straight in chat?", never inferred from a job's content.

**The eight steps are the line for EVERY job on EVERY lane** — what changes per lane is only WHERE a
step happens (steps 3–7 on the app timeline, or in the bundled render engine + ffmpeg on the
chat-only lane). Format doesn't change the flow either: it only changes how **Graphics (step 5)**
behaves (captions included: the short-form presets caption by default as a step-5 overlay; long-form never). Run the line; branch only inside that one step.

🔒 **At every step the route is the same two reads: the PRESET for WHAT (the numbers, identical in
every editor), then [`LANES.md`](LANES.md) for HOW.** A step your app has no recipe for is done by
hand from the preset's numbers and **said out loud**, never with another app's mechanics.

| # | Step | Skill | What happens |
|---|------|-------|--------------|
| 1 | **Intake** | _(copy)_ | Point to a raw file (often in `~/Downloads`). **Copy** it into `projects/<job>/raw/` — never move, never touch the original, so the source survives a bad render. Name `<job>` after the content (see Job naming). |
| 2 | **Rough cut** | `rough-cut` | Always, every format. `transcribe.sh` (WhisperX large-v3 + word alignment) → kill filler and dead air (**the #1 filter: relevant ≠ necessary — good-to-know is fluff, only need-to-know-NOW survives**) → `splice.sh` stitches it frame-snapped, `polish-boundaries.py` sets every word edge → **fresh-eyes second pass** (two subagents ONE TIER BELOW this session's model: Fable → Opus, Opus → Sonnet, Sonnet → Haiku; `model` passed explicitly) → **a STATIC audio chain: the measured amplify from `workflows/voice-gain.py` (kept speech → −17 LUFS pre-limiter) into a −6 dBFS limiter**, never dynamic loudnorm. Produces the cut **and the finished script**, the source of truth downstream. On an app finish it runs `RENDER=0` and replays the EDL onto the timeline. |
| 3 | **Audio polish** | _(in-app / baked by splice)_ | **Every job, immediately after the cut lands on its finish surface.** Same chain everywhere: the gain `workflows/voice-gain.py` measures (kept speech → −17 LUFS pre-limiter, so a quiet shoot gets more and a hot one less) into a −6 dBFS limiter. Premiere: ONE command, `uv run lanes/premiere/audio-polish.py projects/<job> --apply`, and **a timeline rebuild discards the effects, so re-apply after every re-replay**. Chat-only: `splice.sh` baked it in already. Per-lane: [`LANES.md`](LANES.md) § step 3. |
| 4 | **Color grade** | _(in-app)_ | **Long-form, before graphics, and it lives UNDERNEATH them:** ONE adjustment layer spanning the timeline, above the footage and below the graphics (Premiere: V1 footage → V2 grade → V3 graphics). Footage-only is the point — the graphics already ship the colours the preset locks — and it runs first because the graphics QA measures off the shipping picture. **The look is locked: Autumn-Rec709 as a Creative Look at Look Intensity 70, Creative Saturation 115**, shipped captured, so `uv run lanes/premiere/grade-lut.py apply <job>.prproj` replays it hands-off on job one. There is NO colour-correction step. Numbers: [`presets/youtube/default/README.md`](presets/youtube/default/README.md) § Grade. Mechanics: [`LANES.md`](LANES.md) § step 4. |
| 5 | **Graphics** | `graphics-plan` → `graphics-build` → `edit-review` | **Default = the BASIC tier: the format's own `default-overlay-style.md`** ([`presets/youtube/default/`](presets/youtube/default/default-overlay-style.md) long-form · [`presets/instagram/explainer/`](presets/instagram/explainer/default-overlay-style.md) short explainer; TikTok/raw stays hook-card-only): 4–7 face-clear UI cards plus required real captures and written-artifact walkthroughs ([`creative-moves.md`](presets/youtube/default/creative-moves.md) § 4d); named alternate looks are opt-in. Long-form also gets the [creative-moves vocabulary](presets/youtube/default/creative-moves.md) unprompted. **(a)** `graphics-plan` storyboards every graphic and self-reviews, gated by `validate-plan.py`. **(b)** `graphics-build` owns comps, renders and placement (Premiere: `lanes/premiere/place-graphics.py`); the short-form caption layer is one of its graphics, and on the full-tier split-frame explainer it **measures the face crop first**, `uv run workflows/face-frame.py <base-cut>` (locked: hair top 50 px below the y960 seam, measured, never guessed). **(c)** `edit-review` converges it: `uv run workflows/graphics-qa.py projects/<job>` green is the precondition, then fresh-eyes subagent rounds on two dimensions drive the draft to ZERO objective defects before you ever see it — defects only, never taste, cap 3. **The mistakes the system can find, the system fixes.** |
| 6 | **SFX** | `workflows/sfx-plan.py` → lane placer | Sound design synced to the graphics. The PRESET says what: [`presets/youtube/default/sfx.md`](presets/youtube/default/sfx.md) + `sfx.json` (motion event → sound class → library slice → target peak, three tracks by layer depth; entrances are events, exits and cuts back to the face are silent). `uv run workflows/sfx-plan.py projects/<job>` reads the PLACED graphics and writes a cut sheet with a measured level per slice; placement is per lane ([`LANES.md`](LANES.md) § step 6), Premiere `uv run lanes/premiere/place-sfx.py projects/<job> --apply` (`--diff` reports your hand edits first), other lanes by hand. Library: `assets/sfx/`. **After any graphic moves, read the timeline diff, then re-run the plan and re-place, verifying zero missing/extra/drifting cues.** |
| 7 | **Review** | _(manual)_ | You watch and call adjustments — cut this graphic, swap that one, move it, redo. The draft already has zero *objective* defects, so this pass is **taste**, and only taste. **Iterate incrementally:** re-render ONLY the changed part (chat-only mechanics: [`lanes/chat-only/incremental-graphics.md`](lanes/chat-only/incremental-graphics.md)). |
| 8 | **Export** | _(render → `finalize.sh` → `prune.sh`)_ | Render the final, then **finalize**: `./finalize.sh <job>` (dry-run; `--apply` to act) promotes the latest render to the one canonical `outputs/<job>.final.mp4`, retires dead drafts and **drops an export copy in `~/Downloads/`** (`VE_EXPORT_DIR` overrides that target), keeping the base cut, transcript and `hf-graphics/` source so the job can be reopened. Then `./prune.sh --apply` reclaims the regenerable cache. |

**One CONDITIONAL pass hangs off the line — opt-in, so it is not a numbered step.** It has a
fixed slot; run it there or say why it was skipped. (Captions are not a pass: on the short-form
presets they are the top layer of step 5, placed like any other graphic.)

| Pass | When | Slot | What happens |
|---|---|---|---|
| **Background music** | opt-in, format-agnostic (skip unless asked) | after 6, before 7 | `background-music` lays a **flat constant bed** by default: no ducking, no fade-in, −20 dB, the bed starting at the reviewed sustained musical entrance (sparse intro transients do not count), a 2 s tail fade-out only. Ducking and fade-in are **opt-in**. chat-only: a pure audio pass, video copied, no re-encode; Premiere: `lanes/premiere/place-music.py` onto A5, bounce-proved. |

### Your finish surface

On an app finish, steps 3 through 7 happen on that app's timeline. The rough cut is **not** imported
as a flattened export: each lane **rebuilds it as separate, trimmable clips** by replaying the EDL
(`transcript/cuts.json`) against the raw footage, so every cut is a real edit point you can
ripple/slip/slide. That's why step 2 runs `RENDER=0` on an app lane.

- **Premiere Pro** (`premiere-pro` skill) — `node lanes/premiere/premiere-bridge.mjs replay
  <cuts.json> <clipName>`, the headless bridge, no MCP session needed. From there Claude works ON the
  timeline: alpha-ProRes graphics, baked footage moves, audio chains, section label colours, and the
  export via `exportAsMediaDirect` (never queue Adobe Media Encoder). Install: `./setup-premiere.sh`.
- **CapCut** (`capcut` skill, macOS) — no API, so `uv run lanes/capcut/capcut-bridge.py` works two
  lanes: it writes a whole draft straight from the EDL, and drives the running app through the
  accessibility tree for seeks, splits, deletes and its own verified export. The locks that keep it
  working (quit CapCut while the bridge writes, media hardlinked under `~/Movies`, never `replay`
  over a hand-edited draft) live in the skill.
- **DaVinci Resolve** (`davinci-resolve` skill) — `./setup-resolve.sh` wires the MCP onto Resolve's
  official scripting API. The EDL replay is one call, and from there: silence ripple, AI subtitles,
  Fusion graphs, DCTL shaders, native renders. The skill carries what's verified AND what's broken.

**Second entry path: long-form → clips (`clipper`).** The reverse of the line above: transcribe a
finished long-form once, select self-contained hook-and-payoff moments into a reviewed
`clips-plan.json`, then `make-clips.py --build` runs each approved clip through the locked engine
(splice → face-centered 9:16 reframe → TikTok/raw captions → `.final.mp4` + a `~/Downloads/` copy).
Each clip is a standard job folder under `projects/<parent>/clips/<name>/`.

### Format variants — only step 5 changes (captions included)

**Format is AUTO-DETECTED from the raw footage, never asked.** **Vertical** (height > width) →
short-form; **horizontal** → long-form YouTube; a mixed folder is decided by the clips carrying the
substance. Explainer vs TikTok/raw is inferred from content. State the detected format in the report
so it can be overridden with a word — and do the same with the hook and takeaway, read out of the
transcript and stated for correction rather than asked for up front.

| Format | Aspect | Graphics (5) | Captions |
|---|---|---|---|
| **Short · Explainer** (Reels · TikTok · Shorts) | 9:16 · 1080×1920 | top-half graphics, face bottom; `face-frame.py` first, full tier adds `presets/instagram/explainer/signature-style.md` | centered — **locked** |
| **Short · TikTok/raw** (Reels · TikTok · Shorts) | 9:16 · 1080×1920 | **front hook card only** (`presets/tiktok/raw/tiktok-raw-style.md`), then raw | low, under face — **locked** |
| **Long-form** (YouTube) | 16:9 · 1920×1080 (no reframe) | `presets/youtube/default/` cards + creative moves (`youtube/liquid-glass/` and `youtube/vox-collage/` are opt-in by name) | none (YouTube CC) |

The 9:16 reframe happens at the top of Graphics, and safe zones live in each preset's own style doc
— read the preset you're on before building. Long-form has no platform safe bands: never cover the
face or important on-screen content, keep copy off the very edge, and leave the outro's right side
and bottom clear for end-screen cards.

**Short-form safe zones (always, never break):** no key visuals in the **top 200 px** or **bottom
300 px** — face, captions and every key graphic stay inside y `200 → 1620`. Those two bands are
background only (platform UI and device chrome sit there).

## Skills

- **`edit-video`** — **the orchestrator: the whole line, end to end.** "Edit this video" / "do the
  whole edit" routes here. It owns the ORDER, the STATE and the GATES only; each step's how-to stays
  in its own skill or preset. It keeps `projects/<job>/RUN.md`, rewritten at every step boundary, and
  reads it before assuming a fresh start. A step which cannot run is **announced as skipped, never
  passed over in silence**.
- **Core editing:** `rough-cut`, `graphics-plan`, `graphics-build`, `edit-review`, the locked caption
  presets (`presets/instagram/explainer/captions-style.md`, `presets/tiktok/raw/tiktok-raw-style.md`
  + their `build.py`), `background-music`.
- **Finish lanes:** `premiere-pro`, `davinci-resolve`, `capcut` — the HOW docs for the three editing
  apps; [`LANES.md`](LANES.md) is the per-step index across them. **`clipper`** is the reverse entry
  path: a finished long-form in, short-form clips out.
- **HyperFrames suite (engine):** `hyperframes` (+ `-core`, `-cli`, `-animation`, `-audio`,
  `-creative`, `-registry`, `-keyframes`) and `media-use` — the HTML-based video toolkit that renders
  graphics and captions.
- **HyperFrames task workflows (advanced, optional):** `faceless-explainer`, `general-video`,
  `talking-head-recut`, `motion-graphics`, `pr-to-video`, `product-launch-video`,
  `remotion-to-hyperframes`, `slideshow` — vendored extras for one-off builds.

### HyperFrames video-authoring toolkit (vendored)

A general HTML-based video toolkit from `heygen-com/hyperframes`, pinned in `skills-lock.json` and
run via **`npx hyperframes`** on any machine with `node` — `./setup.sh` bootstraps it once
(`npx hyperframes@0.8.16 browser ensure`). **Update via the skills registry, not by hand-editing.**

## Folder Structure

The project root **is** the editing workspace — job folders live directly in `projects/`.

| Path | What's In It |
|------|--------------|
| `.claude/skills/` | The editing skills + the vendored HyperFrames toolkit. |
| [`LANES.md`](LANES.md) | **The routing index: one row per pipeline step, one column per app (Premiere · Resolve · CapCut · chat-only), each cell saying scripted / manual / unvalidated / gap and pointing at the recipe.** Read your step's row before any app-specific work. |
| `lanes/` | Everything app-specific, one folder per finish surface (`premiere/`, `resolve/`, `capcut/`, `chat-only/`): bridge and launch scripts, templates, lane sheets, and each app's own `lab-notes.md`. Start at [`lanes/README.md`](lanes/README.md). |
| `presets/` | **The looks — the WHAT half of every step, and app-independent.** One folder per preset under `presets/<platform>/<preset>/`: `youtube/default/` (long-form — read its `README.md` at the top of a long-form job and its `default-overlay-style.md`, the SCOPE contract, before any graphics pass), `instagram/explainer/` and `tiktok/raw/` (short-form), `youtube/liquid-glass/` and `youtube/vox-collage/` (opt-in by name). A command or an app quirk belongs in `lanes/`. |
| `workflows/` | The universal utilities, identical whichever app you finish in: `sync-dual-audio.py` (step 1, dual-system shoots: GCC-PHAT offset + clock-drift measurement, then muxes the good mic onto the camera picture without re-encoding), `take-map.py` (step 2 on a SCRIPTED shoot: aligns what was said to the written script to find where the creator backed up and re-recorded), `voice-gain.py` (step 3), `sfx-plan.py` (step 6), `dead-air-qa.py` (the step-2 dialogue dead-air gate), `music-onset.py` (the music pass's sustained-entrance measurement), `face-frame.py` + `chin-line.py`, `eye-line.py` (splits a talking-head take into eye-contact and reading segments from head yaw, so a shoot's look-away marker can gate where overlays may sit), `graphics-qa.py` (the step-5 gate) + `render-diff.py` (its parity proof for any re-render), `hand-track.py`, `behind-text.py`, `bake-emoji.py`, `window-grab.sh`, `screen-record.sh` + `page-record.mjs` (record an app window / a web page for a planned `screen-rec` cell). A file whose whole job is one app's mechanics lives in `lanes/<app>/`. |
| `projects/<job>/RUN.md` | **The run's state file**, written by `edit-video` at every step boundary: format, lane, preset, per-step status, what each step produced, and everything skipped with its reason. The first thing to read on a job in progress. |
| `projects/<job>/` | One folder per content piece: `raw/`, `audio/`, `assets/`, `broll/`, finals in `outputs/`. The graphics build lives **durably** in `hf-graphics/` (comps + `render.sh` + a `PROJECT.md` resume doc — never delete it, it's the real progress); only the regenerable cache is disposable, and **nothing lives solely in `/tmp`**. |
| `finalize.sh` · `prune.sh` | Step 8 and its cleanup: finalize promotes the latest render, retires drafts and copies the deliverable to `~/Downloads/`; prune reclaims regenerable dead weight, never `raw/` or `outputs/`. Both dry-run by default. |
| `assets/` | `fonts/`, `logos/`, `sfx/` (the library step 6 draws from), `luts/` (the cubes plus the captured house look, Autumn-Rec709 — see its README), `models/`. **Personalize:** drop your own brand marks in `logos/`. |
| [`brand-kit.md`](brand-kit.md) | The one file you fill in — identity, voice, colours, fonts, hook style. Optional. |
| `transcript-corrections.json` | Upstream transcript fixes (brand and product names, recurring mishears), applied ONCE at step 2, so graphics, captions and long-form all inherit them. Per-job overrides: `projects/<job>/corrections.local.json`. |
| `skills-lock.json` · `check-setup.sh` | The pins for the vendored HyperFrames skills, and the report-only check of the system tools the skills need (ffmpeg, etc.). |
| `RELEASE.md` + `VERSION` | What changed in this build of the system, and which build you have. Check `VERSION` against the download page before reporting a problem. |

**Job naming:** name `<job>` after the video's content — a short kebab-case title (e.g.
`my-first-video`, `cold-dm-teardown`), **never** the camera file (`C1840.MP4`), a date, or a stage
suffix.

## Rules

- **One job: edit the best video possible.** Raw → fully edited → exported. No business or CTA logic
  lives here — captions and end screens carry no sales asks.
- **Surgical changes only.** Touch what's asked; don't "improve" adjacent renders or refactor working
  skills.
- **Fix the source, never stack a correction on a broken artifact.** A step's output is wrong →
  re-run that step from its durable inputs (`transcript/words.json`, `transcript/cuts.json`, the
  `hf-graphics/` comp source), never compensate downstream: a correction layered on a bad output
  accumulates error and hides the cause, and if a fix needs a fix the approach is wrong. The
  step-level instances are the locks below.
- **The PRESET says WHAT; the APP SKILL says HOW; [`LANES.md`](LANES.md) is the index between them.**
  A preset is a look — numbers and rendered files, identical in every editor — so no command, no
  argument quirk and no track index belongs in one.
- **Update HyperFrames via the registry,** not by hand — `skills-lock.json` tracks hashes.
- **Document, don't manufacture.** Authenticity outperforms.
- **Motion craft is the VOX craft layer, not a global one:**
  [`presets/youtube/vox-collage/motion-craft.md`](presets/youtube/vox-collage/motion-craft.md) is
  read ONLY when that look is invoked by name.
- **Repeated line across takes → use the LAST take.** Don't ask.
- **Captions run the whole short-form video by default** — never suppress them under a hook or
  graphic unless told.

## The learning loop — how the editor gets better between jobs

The system improves only through files, never through chat memory. Four writes, every job, unasked:

1. **Channel preset first.** A job for a known channel reads `presets/<platform>/<channel>/` before step 0 (`README.md`
   = the look, `PLAYBOOK.md` = the repeatable procedure, `LESSONS.md` = what earlier jobs taught) and RUN.md names it.
   Affan Afterhours → [`presets/youtube/affan-afterhours/`](presets/youtube/affan-afterhours/README.md).
   @affanwizu (Urdu reels, Roman Urdu CAPTIONS ONLY) → [`presets/instagram/affanwizu/`](presets/instagram/affanwizu/README.md).
2. **The creator's review is data.** After step 7, read what changed on the timeline (`place-graphics.py --diff`,
   `place-sfx.py --diff`, the V1 cut diff) plus what was said, and append each finding to the channel's `LESSONS.md` as
   *lesson → change made → file*. A lesson that repeats becomes a preset number or a PLAYBOOK rule; a one-off stays a lesson.
3. **A tool bug goes into the lane's `lab-notes.md` the day it is found**, with its workaround. RUN.md flags are the
   draft; lab-notes is the record.
4. **Every job carries its own state:** `BRIEF.md` in pre-production, `RUN.md` from intake, each with a "▶ STATUS:
   resume here" block at the top, rewritten at every milestone, so a new session picks the job up cold.

## Lab Notes — the locks

One lock per line, each pointing at the doc that OWNS the rule. Read the owner before re-working a
locked area; every one of these was found the hard way.

- **Transcribe ONCE per video.** WhisperX large-v3 → `projects/<job>/transcript/words.json`, reused
  forever (`--force` to redo); `splice.sh` derives the canonical `outputs/<job>.transcript.json`
  through `cuts.json` by pure arithmetic, and nothing downstream re-transcribes. Spelling and brand
  fixes from `transcript-corrections.json` are applied right there, so every consumer inherits them.
  Owner: `rough-cut`.
- **Audio = STATIC chain, processed ONCE.** One lossless splice, then one polish: the measured gain
  (`workflows/voice-gain.py`, kept speech → −17 LUFS pre-limiter) into a −6 dBFS limiter, then AAC
  256k. Never dynamic loudnorm (it pumps), never per-segment effects (they click); `AMPLIFY_DB=<n>`
  is the hand override when `audio-qa.py` warns about limiter pressure, and later re-encodes stay
  ≥ 256k so nothing downstream degrades the voice.
- **Splice = frame-snapped, J-cut joints, MEASURED boundaries.** Cuts snap to the frame grid
  (un-snapped, concat pads joints with silence until captions desync); joints are 15 ms equal-power
  crossfades over real room tone, never butt-splices, never fades to zero; `refine-cuts.py` and
  `polish-boundaries.py` move every boundary to the word's real acoustic edge and resolve joints
  pairwise (**a continuous split shares ONE boundary; overlapping segments stutter and `splice.sh`
  aborts**). Refinement is NOT idempotent — repair a shipped EDL with `--repair-only`.
- **Both caption presets are LOCKED** →
  [`presets/instagram/explainer/captions-style.md`](presets/instagram/explainer/captions-style.md)
  and [`presets/tiktok/raw/tiktok-raw-style.md`](presets/tiktok/raw/tiktok-raw-style.md) + their
  `build.py`. Build ONLY from the canonical transcript. Captions are a step-5 graphic: the builder
  renders the caption layer as an alpha overlay under `hf-graphics/captions/`, the plan carries the
  `captions` cell, and the lane's placer lays it on the top graphics track like any other overlay.
  Engine is PIL PNG overlays + ffmpeg (this ffmpeg has no drawtext, don't install one) for TikTok/raw,
  HyperFrames for the explainer.
- **Explainer face framing = LOCKED, measured.** `uv run workflows/face-frame.py <base-cut>` prints
  the `#head` `object-position` (hair top 50 px below the seam); `--verify <draft>` must PASS before
  review. Fallback when hair can't be measured: face-box centre → y1385.
- **Graphics builds: one comp per graphic; an emitter only for split-part builds**, so a long
  graphic ships as short parts from ONE shared timeline and a tweak re-renders one part. The base
  rough cut is NEVER re-rendered. Gotchas: `graphics-build`.
- **THE GRADE GOES UNDER THE GRAPHICS, AND THEREFORE BEFORE THEM** — footage graded, graphics
  untouched, look locked to Autumn-Rec709 at 70/115, no correction step. WHAT:
  [`presets/youtube/default/README.md`](presets/youtube/default/README.md) § Grade. HOW:
  [`LANES.md`](LANES.md) § step 4.
- **A screen capture is a PLANNED cell, never improvised, and text is never captured.** A `screen-rec` / `screenshot` cell with no file carries `capture` and the build records it (a page: `workflows/page-record.mjs`, headless; a page behind a login is an `app` capture of the signed-in browser; an app: `screen-record.sh`, which fronts it for the take; stills: `window-grab.sh`); it applies when the thing on screen IS the evidence and cannot be re-typed (a folder, an app state, a click) — a prompt, command or quote is rebuilt verbatim as a graphic, a list of tool names is a card. Owner: `graphics-plan` § THE CAPTURE GATE; the look: `default-overlay-style.md` § SCREEN-REC SCENES.
- **The craft rules are measured, not eyeballed:** density is a cadence and a SPREAD (full-screens
  never 40 s of runtime apart), entrances and exits come from the registry in code (cards rise,
  objects pop, the default exit is `riseOut`, and type NEVER pops — it rises with scissors, or slams
  in Impact), slides and large movements render with motion blur, a full-screen graphic is a short
  SCENE and not a card (at least two phases, at least one visual that is not type, and a camera
  move), type over a scene RACKS THE SCENE OUT (a pre-blurred, pre-darkened clone crossfaded in,
  never a filter tween), overlays sit in the low band and side callouts are MEASURED off the head
  (`uv run workflows/chin-line.py <raw>` prints the floor; add `--edl <cuts.json> --from <t> --to
  <t>` for the callout zone — 60 px off the ear, 80 px off the frame edge, the side with more room),
  accent props glow while type does not, a readable graphic holds 2–3s, and arrowheads are computed
  from the path's end tangent. Owners: [`creative-moves.md`](presets/youtube/default/creative-moves.md),
  [`animations.md`](presets/youtube/default/animations.md) and
  [`default-overlay-style.md`](presets/youtube/default/default-overlay-style.md).
- **Completion is checked against your ORIGINAL REQUEST, not just the graphics plan.** A plan that
  omits a requirement cannot be its own proof of completion: RUN.md carries the coverage and the
  final handoff reconciles it against the saved timeline. Owner: `edit-video` § Request coverage.
- **Live app state is READ before a deictic is interpreted, on every lane.** "the section I marked",
  "the highlighted clip", "at the playhead" → query the finish surface's marks, selection and
  playhead first, then analyse; clear marks after acting. Owner: `edit-video` § Where the run STOPS
  on its own; the lane's calls live in its app skill.
- **A video that claims it was edited in one pass is BUILT that way.** Nothing copied in from an
  earlier job (comps, renders, `graphics-plan.json`, harness files, assets); preset reference files,
  `assets/` and system fonts only, captures fetched fresh. Owner: `edit-video` § Step 0, item 8;
  recorded in RUN.md as a constraint.
- **Per-app locks live with the app**, in `lanes/<app>/lab-notes.md`. Read the one for your lane;
  nothing in it applies to another app.
- **hyperframes is PINNED and bumped deliberately** (`hyperframes@0.8.16`, matching `setup.sh` and
  `SETUP.md`). Never `hyperframes upgrade`; update the vendored skills through the registry so
  `skills-lock.json` stays honest.
