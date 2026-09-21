---
name: edit-video
description: "Runs the WHOLE edit end to end: the eight-step pipeline in order, from a raw clip to an exported file, with a durable per-job RUN.md so the run survives a compaction and can be resumed cold. Owns the ORDER, the STATE and the GATES only — every step's how-to stays in its own skill or preset. Enforces that step N is finished to its definition of done before N+1 starts, and that a step which cannot run is announced as skipped, never passed over in silence. Triggers: edit this video, do the whole edit, run the whole pipeline, full edit, edit this end to end, take this from raw to export, run the pipeline, edit the latest project, resume the edit, where were we on this job, continue the edit."
---

# Edit Video — the whole run

**This skill owns the LINE, never the STEP.** It knows what order things happen in, what "done"
means for each one, and where the run is up to. It knows nothing about how to cut a word, author a
comp, or bake a zoom — that lives in each step's own skill or preset, and this skill routes there.

The failure it exists to prevent: "do the whole edit" was previously the CLAUDE.md pipeline table
plus a session's reading of it. Nothing carried state, so a compaction mid-job lost the place;
nothing enforced finishing a step before starting the next; and a step that could not run could be
passed over without anybody noticing.

## 🔒 THE FIRST THING, ALWAYS: read `RUN.md`

Before anything else, look for **`projects/<job>/RUN.md`**.

- **It exists** → this job is already underway. Read it, report where the run is in one line, and
  resume at the first step that is not `done`. **Never restart an unchanged step marked `done`**, and never
  re-replay a timeline the creator has hand-edited since.
- **It does not exist** → this is a fresh run. Create it (template below) after resolving the job.

This is unconditional. A fresh context that starts cutting because it did not look is exactly the
bug this skill exists to kill.

## The line

Eight steps, in order, every job. The full spec is CLAUDE.md § The Pipeline; this table is the
gate list — what has to be TRUE before the next step starts.

| # | Step | Owned by | Definition of done (all must be true) |
|---|------|----------|----------------------------------------|
| 1 | Intake | _(copy)_ | Raw is **copied** (never moved) into `projects/<job>/raw/`; the original is untouched; the job is named after the content, not the camera file or a date. |
| 2 | Rough cut | `rough-cut` | `transcript/words.json` + `transcript/cuts.json` persisted; canonical `outputs/<job>.transcript.json` written; boundary polish run; the fresh-eyes second pass run; final dialogue-only dead-air gate passes on the final EDL, including protected boundaries; complete outro/handoff retained unless explicitly removed. **App lane:** splice ran `RENDER=0` (no flat MP4) and the EDL is replayed onto the timeline with the clip count read back and matching. |
| 3 | Audio polish | `premiere-pro` / `davinci-resolve` / baked by splice | Gain measured by `workflows/voice-gain.py` (kept speech → −17 LUFS pre-limiter), never a fixed number; the house chain applied to **every** voice clip; **every value read back**; the clip count reported. |
| 4 | Color grade | the format's preset § Grade | **Long-form only.** Grade layer exists **under** the graphics track and **over** the footage, one layer spanning the timeline, **sized to the sequence**; the look verified by measuring a program render, never a readback. Run it where [`LANES.md`](../../../LANES.md) § step 4 has a recipe; on a ⛔ lane do it by hand from the preset's numbers or record it as skipped, in words. |
| 5 | Graphics | `graphics-plan` → `graphics-build` → `edit-review` | `graphics-plan.{json,md}` written; every `capture` cell recorded into `assets/captures/` (an app fronted for a take is SAID in RUN.md); every required evidence beat (including exact prompt walkthroughs, named destinations and restored outro passages) planned, built and placed; **placement FRAME-EXACT**: every row whose end is a V1 cut lands ON it, not a frame short (`graphics-qa.py`'s `cut` check, green); `edit-review` ran to a clean full round. Not done when the last comp lands — done when the loop dries. |
| 6 | SFX | `workflows/sfx-plan.py` → the lane's placer | Every format with graphics. Runs AFTER the step-5c loop dries. `hf-graphics/sfx-plan.{json,md}` written from the PLACED graphics and reviewed as a cut sheet; every planned row placed on the lane's SFX tracks at its frame and level, **read back with zero missing, extra, or drifting cues**. Run the placer where [`LANES.md`](../../../LANES.md) § step 6 has one; a lane without one hand-places from the cut sheet and says so. After graphics change, review the candidate score and update affected cues while preserving approved unaffected rows/levels; then apply and verify. |
| 7 | Review | _(the creator)_ | Handed over with the draft ready to watch. **The run pauses here** — this step completes when you say it does. |
| 8 | Export | lane exporter → `finalize.sh` | A real final file exists in `outputs/`; `finalize.sh --apply` run; the `~/Downloads` copy present. **Never render one just to satisfy the step** (see the Premiere stop below). |

**One conditional pass** slots in without being numbered: **Background music** (opt-in, after 6,
before 7). It either runs or is stated as skipped, same rule as a step. Captions are not a pass: on
a short-form preset they are the `captions` cell of the step-5 plan, built and placed with the
other graphics (2026-09-04); long-form has none.

## Step 0 — resolve the job, before step 1

Do all of this once, up front, and write it into RUN.md so no later step re-derives it:

1. **The job folder.** Newest under `projects/` unless you named one.
2. **Format — probe it, never ask (2026-08-13).** `ffprobe` the raw: height > width means
   short-form, width > height means long-form YouTube. A mixed folder is decided by the clips
   carrying the dialogue — the main takes vote, b-roll and inserts do not. Explainer vs TikTok/raw
   is inferred from content at step 5, not asked. Resolve it ONCE here, write it into RUN.md, and
   state it in the report so one word can override it.
3. **The lane.** The one setup recorded, when `.setup-complete` carries a `lane=` line (a client
   package writes `premiere`, `resolve`, `capcut` or `chat-only` there); otherwise Premiere by
   default with nothing named. A recorded `chat-only` is never re-asked. Never infer the chat-only
   lane from a job's content — on a machine with an app, only an explicit yes gets it.
4. **The preset**, which follows from format.
5. **The lane's coverage.** Read [`LANES.md`](../../../LANES.md) once, top to bottom, for the column
   you are on. Write the ⚠️ and ⛔ cells into RUN.md up front, so a gap is a known cost at the start
   of the run rather than a surprise at the step. It also decides what to say in the opening report.
6. **Source fps and duration**, read once.
7. **Request coverage**, captured in RUN.md before planning: asked-for beats and omissions, verbatim artifacts with their source paths, real destinations to capture, music choice, finish instruction. Map each to its owner and its eventual evidence; a plan that omits a requirement cannot be its own proof of completion.
8. **Whether the video's own claim constrains the run.** A piece that asserts it was edited in one
   pass may not be seeded from an earlier job: no copied `hf-graphics/` comps, renders,
   `graphics-plan.json`, harness files or assets out of another job folder. Only the format's preset
   and its reference files, the repo's `assets/` and system fonts are fair game, and every capture
   and asset is fetched fresh for this job. Reading an earlier job to learn the craft is fine right
   up to the moment it becomes a copied file. Record it as a constraint in RUN.md so a resumed
   session keeps it.

## Running a step

Each step, in this order, no exceptions:

1. **Announce** which step is starting, in one line.
2. **Route — WHAT first, then HOW.** Two reads, the same shape every time:
   - **WHAT** = the format's preset, § this step. The target, the numbers, the definition of done.
     App-independent by construction.
   - **HOW** = [`LANES.md`](../../../LANES.md), the row for this step, which names the lane's status
     and points at the section in that lane's app skill (`premiere-pro` / `davinci-resolve` /
     `capcut`), or at the chat-only sheet.

   Do not re-derive either here. **Never read another lane's mechanics** — an adjustment layer on a
   lane whose equivalent is a color group, a premultiplied alpha mov on a lane that wants straight,
   and a hand-scaled 1080 asset on a timeline that already conformed have each shipped damage.
3. **Handle a ⚠️ or ⛔ cell explicitly.** An unvalidated recipe is a test: run it, then verify by
   measurement and say the result. A gap means do the step by hand from the preset's numbers and
   **say so** — it goes in the report and in RUN.md, same as a skipped step. A step done by hand is
   a normal outcome; a step quietly done differently from the preset is not.
4. **Verify** against the definition-of-done column above. Verification means reading state back
   or measuring an artifact, never assuming a write landed.
5. **Write RUN.md** — current status, verified facts, paths to evidence, and any flag. Keep historical revisions separate from the current clip/graphic/SFX counts. An appended/restored passage reopens its rough-cut, graphics, SFX and ending checks; an old `done` flag does not cover new footage.
6. **Only then** start the next step.

**A step that cannot run is announced out loud and recorded as `skipped`, with the reason.** It
gets said in words and written down; it never silently disappears.

**A blocked step does not block independent work.** Record it and continue where dependencies allow; a missing required capture or failed verification remains unfinished. Do not label the draft complete while a required gate is failed or skipped.

## Where the run STOPS on its own

- **Step 7 is the creator's.** Hand off the draft and stop. Do not proceed to export on your own.
  **Read the notes that come back for the PRINCIPLE, not the wording (2026-09-10).** A note
  given as an example — "maybe it slides out to the right and something slides in from the left" —
  names what you want more of, on any format; say that principle back in one line, then design to it
  with whatever fits the beat. Executed verbatim instead: numbers you dictates (frames, sizes,
  curves), a look or preset you name by name, every locked preset value, and anything you flags as
  exact. Building the example literally ships the letter of the note and misses the taste behind it.
- **Feedback that points at live app state is READ from the app before it is interpreted, on every
  lane.** "the in and out points I set", "the highlighted clip", "this section", "at the playhead" —
  query the finish surface's marks, selection and playhead first (the calls are the lane's, in its
  app skill), read the content back, and only then analyse. Inferring the target from the
  conversation instead once got the wrong segment diagnosed AND deleted (2026-08-28). Nothing marked
  or selected: say so and ask for a timecode. After acting on marks, clear them so they cannot go
  stale over shifted content.
- **On the Premiere lane the automated work ends at "placed + verified."** You render and finish
  there; AME is banned. So step 8 runs only once a real final file exists in `outputs/`. Do not
  render one to close the step.
- **The hard cap in `edit-review`** (3 rounds) still applies inside step 5. If it hits, stop and
  report rather than looping.

## Final handoff gate

Before the run is reported done, reconcile every row of RUN.md § Request coverage against the actual saved sequence, never against `graphics-plan.json` — a plan is not evidence that the thing shipped. Each step's own definition of done carries its proofs; the render- and timeline-side checks are `edit-review` § Final gate.

## `RUN.md` — the state file

Lives at `projects/<job>/RUN.md`. Rewrite the whole file at each step boundary; it is small.

```markdown
# RUN — <job>

**Next action:** <the single next thing, in one line>

| | | |
|---|---|---|
| format | long-form YouTube | probed: 1920x1080 |
| lane | Premiere | `projects/<job>/premiere/<job>.prproj` |
| preset | `presets/youtube/default/` | |
| lane gaps | none | from LANES.md — list every ⚠️/⛔ step for this lane, or "none" |
| source | 30000/1001 fps · 121.02s | |
| constraints | none | or "fresh build — nothing reused from an earlier job" |
| started | 2026-09-01 | |

## Steps

| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | done | `raw/clip-01.mov`, original untouched |
| 2 | Rough cut | done | 35 segments · cuts.json + canonical transcript · replayed, 35/35 verified |
| 3 | Audio polish | done | measured +12 dB (voice-gain.py) → −6 dBFS limiter on 35/35 A1 clips, readback verified |
| 4 | Color grade | done | GRADE layer on V2, Autumn Look @70/115 via `grade-lut.py apply`; frame grab moved 105.9/87.6/90.7 → 99.2/83.5/85.2 |
| 5 | Graphics | done | 25 graphics placed; edit-review clean on round 3 |
| 6 | SFX | done | 124 rows planned, 124/124 placed on A2–A4, readback verified |
| 7 | Review | — | |
| 8 | Export | — | |

## Request coverage
- Asked-for beats / omissions: <request → kept source/timeline evidence>
- Verbatim artifacts / real destinations: <source path → planned beat → native proof>
- Music / finish instruction: <track, reviewed entrance/level; saved timeline or authorized export>

## Flags to report
- g19 typed prompt holds 2.50s (retimed from 0.60s)

## Skipped, and why
- Background music: not asked for.
```

Keep it short. It is a resume doc, not a log: what is true now and what happens next, never a
transcript of how you got here.

## Compaction — write state always, compact rarely

**Write RUN.md at every step boundary, so that whenever a compaction happens, it is safe. This
skill never triggers one — the user types `/compact`.** Never compact inside step 5: the plan feeds
the build feeds the review. **Two boundaries where one genuinely pays**, because the context behind
them is dead weight for everything after: **after step 2** (per-word cut decisions are finished,
only `cuts.json` and the canonical transcript matter downstream) and **after step 5** (comp
authoring, renders and QA measurements are done; steps 6 to 8 need none of it). At each, say in one
line that RUN.md is current and this is a clean place to `/compact`.

## The report, at the end

One block, tight: the format and lane detected, per-step status, **everything skipped and why**,
**every step done by hand because the lane had no recipe**, any flags standing, and the deliverable
path. If the run stopped at step 7 for your review, say that plainly rather than implying the job is
finished.

## Not this skill

How to cut a word (`rough-cut`) · how to author or place a graphic (`graphics-plan`,
`graphics-build`) · how to converge defects (`edit-review`) · app mechanics (`premiere-pro`,
`davinci-resolve`, `capcut`) · look decisions (the presets) · the clipper entry path, which is a
different flow entirely (a finished long-form in, short clips out). This skill only ever decides
**what happens next, and whether the last thing is actually finished.**
