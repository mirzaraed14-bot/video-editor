---
name: edit-review
description: "The automated defect loop (step 5c, welded to Graphics): after graphics-build's first pass, the deterministic gate (workflows/graphics-qa.py, must be green) then fresh-eyes subagent review rounds (two dimensions, cap 3) converge the edit to ZERO objective defects before it ever reaches the creator. Defects only, never taste. Reviewers and skeptics run one tier BELOW the session's own model (Fable → Opus, Opus → Sonnet, Sonnet → Haiku, read the current model, never hardcode; `model` must be passed explicitly or agents inherit the session tier); the main session keeps creative judgment and adjudication. Stops on the first full round that finds nothing, then runs the final gate (real render + audio/framing verify) and reports. Triggers: polish loop, polish the edit, review the edit, dial it in, edit review, run the review rounds, converge the edit, one-shot finish."
---

# Edit Review: the defect loop (step 5c, the automated half of Graphics)

Runs after the `graphics-build` first-pass QA and BEFORE the creator sees anything. The builder
grading its own work is why first passes ship flaws; this skill puts fresh eyes on the draft in
review rounds until the objective defects dry up. It replaces waiting for the creator to call the
obvious fixes.

**This is a sub-step of Graphics (5), not a step of its own — it is never deferred (2026-08-31).** Graphics is not finished when the last comp is placed; it is finished
when this loop has run dry. The creator's own review is **pipeline step 7**, it comes after SFX,
and by the time you open the timeline every *objective* defect should already be gone — your pass
is taste, and only taste. A defect that reaches you is a defect this loop failed to catch.

**The contract: defects only, never taste.** The loop converges because defects are binary and
finite; taste never converges. A reviewer that suggests redesigns makes the edit oscillate, not
improve.

## Defect classes: the ONLY valid findings

**Read this before the list. Everything `workflows/graphics-qa.py` owns is OFF-LIMITS to the
reviewers.** A reviewer who believes an unchanged graphic is wrong in a class the script checks
reports it as a **MISSING ASSERTION** (what the script should have caught, with the evidence), never
as a per-graphic defect; the main session adds the assertion. **Deviations are
`hf-graphics/qa-waivers.json`, never prose:** a waiver keyed by graphic and check, with its reason,
showing in the report as `waived`. A sentence in a build report is not evidence (round 2 dismissed a
real 83 ms cut-end flash because the report called it planned).

**The authoritative owner split is the script's own `Checks` / `Not here` docstring block** —
`sed -n '1,60p' workflows/graphics-qa.py`. The `[script]` / `[reviewer]` tags below are copied from
it; when they drift, fix the tool's docstring and re-copy, never invent a third list.

Each class is checkable against evidence (a frame, a timestamp, the plan):

1. **Face/subject covered** by a graphic on any sampled frame. `[SPLIT]` — side-callout clearance (the ink 60 px off the measured `head`) is the script's `face` check; whether any OTHER graphic covers the subject on a sampled frame is yours.
1b. **Band break (long-form)** `[script]` — `default-overlay-style.md` § THE LOW BAND.
1c. **Dead prop glow (long-form)** `[reviewer]` — an accent prop (progress fill, dot, chip, meter
   segment, or a solid-fill icon or glyph inside a card or node) whose glow renders ZERO pixels,
   almost always a `box-shadow` trapped inside an ancestor `overflow:hidden`. **MEASURE
   accent-coloured light OUTSIDE the prop's box on the render, never
   read the CSS.** Glowing type on a BASIC text animation, card headline, eyebrow or caption is the
   same defect inverted — type is default-off, not banned, so a graphic whose subject emits light
   (neon, an LED readout, a terminal accent) may glow its type: flag only the basic-animation case.
   Rule: `default-overlay-style.md` § THE PROP GLOW.
1d. **Off-registry entrance or exit (long-form)** `[SPLIT]` — the registry constants, relative
   `riseOut` and the 12 fps form are the script's; the JUDGMENTS are yours: an entrance split that
   does not track ROLE (peers share one entrance, the odd element out takes the contrast, so a
   different move on every element is the defect, not the fix), and **a same-slot swap whose in
   starts before the out has finished** — two elements in the same place, `riseOut(A, t)` and
   `riseIn(B, t)` at the same time, both on screen for the 0.35s of the out (g19 on your-job,
   2026-09-04, missed by three rounds because the overlap fell between the sampled frames; this is
   why evidence includes a frame ~4 frames after every registry call), and **an overshoot that
   lands on a neighbour**: on the frame 2 after every `pop` or `slam` the grown box (1.10, slam
   1.16) must clear the elements beside it (g16's payoff node slid 16 px over the '2-3 hrs' chip
   for 4 frames, 2026-09-07, missed by three rounds). `graphics-qa.py` asserts this from the
   comp's CSS boxes; what it hands you as `warn` (an SVG neighbour, whose box is its frame and
   not its ink) or `info` (geometry it could not read, including an element a transform moves off
   its CSS box) is YOURS to confirm on the render. For a full-screen's
   near-full-frame first element, count blank lead frames with a **heavy-downscale structural
   diff** so grain does not read as content. Registry: `animations.md`. Flagging a deviation FROM
   the preset spec is always allowed — you are checking conformance, not judging the spec.
1e. **Misaligned arrowhead (long-form)** `[SPLIT]` — that heads are computed is the script's; whether
   they POINT is yours: the head's axis more than ~1° off the path's end tangent, or its base clear
   of the stroke end, measured on the render. **Look hardest at CURVED arrows** — a straight one can
   be eyeballed correctly, which is why the bug ships. Spec: `animations.md` § The arrow.
1f. **Single-frame state change (long-form)** `[reviewer]` — a visible state change that switches
   rather than animates (a background darkening, a blur arriving, a panel lighting up), checkable
   frame-to-frame on the render. Registry entrances whose opacity CUTS by design, and hard
   punch-cuts, are exempt. Rule: `animations.md` § State changes ANIMATE.
1g. **Missing film grain (long-form)** `[script]` — measured as per-pixel noise variance on a flat
   area of the render; section title cards are exempt.
1h. **Rhythm / variety break (long-form)** `[script]` — bare stretches, per-minute density and the
   ANTI-STALE LAW, all against `creative-moves.md` § THE DENSITY NUMBERS. **This is the ONE
   exception to "never more or fewer graphics"** (below): a rhythm break's only fix is adding the
   text animation the law already requires, so report it with the beat and the fill it needs, and
   the main session adjudicates.
1i. **Full-screen reads as a card (long-form)** `[SPLIT]` — the static share and big-beat count are
   the script's `dynamics` check, and that a declared rack reaches the frame edges is its `rack`
   check; whether the phases are really two visual beats, whether a non-type visual is present, and
   whether type over a scene racks at all are yours. Rule: `creative-moves.md` move 2 § A FULL-SCREEN
   IS A SCENE and § THE RACK FOCUS.
2. **Safe-zone break** `[reviewer]` — short-form: key content inside the bands its preset style doc
   states (explainer: `presets/instagram/explainer/default-overlay-style.md` § Placement;
   TikTok/raw: `presets/tiktok/raw/tiktok-raw-style.md` § THE LOOK; also `CLAUDE.md` § Short-form
   safe zones).
   **A reviewer subagent must OPEN that doc — the figures are not restated here.** Long-form: copy
   at the very edge of the frame, or the outro's right side + bottom blocked (end-screen cards).
3. **Copy defect** `[script]` — typo, truncated/clipped text, or copy differing from the cell.
4. **Timing** `[reviewer]` — a graphic's in/out off its word anchor (check against the canonical
   `outputs/<job>.transcript.json`), or a duration that doesn't match the cell.
4b. **Short hold on a READABLE graphic (long-form)** `[reviewer]` — a graphic whose point is content
   the viewer reads or screenshots (prompt, command, code, config, quote) that holds the COMPLETE
   content for under ~2s: the reveal ate the slot. **Count frames where the text is fully present,
   measuring neutral-bright TEXT pixels only** — an accent cursor's blink otherwise reads as
   incomplete. Spec: `creative-moves.md` 4d.
5. **Caption collision** (short-form) `[reviewer]` — a graphic in the locked caption zone.
6. **Motion/render artifact** `[reviewer]` — pop at entrance/exit (missing hard-kill), frozen
   `<video>`, black/blank flash, alpha fringing, duplicated frames at a joint.
6b. **Split-state continuity** `[reviewer]` — a prompt highlight, text or background flashes back to
   its baseline at a part join — the join frames are in the evidence set (`graphics-build` § Long
   graphics ship as split part clips).
7. **Plan fidelity** `[SPLIT]` — the script reconciles ids, times and text-animation copy; a
   deviation in TEMPLATE, side, region or depiction with no `⚠️` note in the build report is yours.
8. **Request/preset coverage** `[reviewer]` — a faithful build of an incomplete plan is still a
   defect. Compare the final transcript and native sequence to the original request, subsequent
   corrections and active preset: complete prompt shown full-screen throughout its explanation,
   actual clauses highlighted on speech, real community/download/product captures where named,
   prescribed dark full-screen scene coverage, and a complete outro/handoff. Inspect the actual
   linked lesson/download destination, not merely a generic community card or landing page.
   Restored/appended dialogue must have its own coverage decisions and SFX. Quote the missing
   requirement and its affected time window; this is conformance, not an optional redesign.

**Banned findings:** redesigns, "this could be better/cooler," different template or copy
phrasing, more or fewer graphics (except a 1h rhythm break or class 8 missing required coverage), tier escalation, and motion-FEEL opinions. Motion character
(fps stepping, easing, hold lengths) is **preset-owned** (2026-08-27): the preset's motion spec IS
the look, tailored deliberately. A reviewer flags only a deviation FROM the preset spec, never the
spec itself. Findings in banned categories are discarded unadjudicated.

## 🔒 The gate comes first: `graphics-qa.py` green is a precondition (2026-09-02)

```bash
uv run workflows/graphics-qa.py projects/<job> --json projects/<job>/hf-graphics/qa-report.json
```

**Non-zero exit = no review round starts.** It sweeps every frame of every render in seconds; what
it owns is its own `Checks` / `Not here` docstring block — read that (`sed -n '1,60p'
workflows/graphics-qa.py`) before a round starts, and hand it to every reviewer. Why the gate sits
here, and the measurements behind the loop's shape: the engineering archive.

**Only a FULL run writes `qa-report.json`,** and only a full run's job-level rows (density, bare
stretch, full-screen share) mean anything: a targeted report's job row is computed from the
selected ids and must not be handed to a reviewer as the job's rhythm.

## The loop

Each **full round**:

1. **Evidence.** Per graphic, grab composite frames at in+2 frames, midpoint, and out−2 frames
   (entrance/exit pops live at the edges; the hold lives in the middle), **plus one frame ~4 frames
   after every registry call inside a hand comp** (read the `riseIn`/`riseOut`/`pop`/`slam`/`drawOn`
   times off its script). **On a `pop` or `slam`, grab the frame at call time +2 as well as the
   +4**: the overshoot peaks at +3 and is settled by +4, so the +4 frame alone never shows it.
   Three samples per graphic cannot see a short event: g19's 0.35s two-lines-stacked swap sat
   between mid and out on your-job and survived three rounds (2026-09-04).
   Lane methods:
   chat-only = ffmpeg frames off the assembled render; Premiere =
   `uv run lanes/premiere/review-frames.py projects/<job> --round <N> [--ids <changed>] [--rest-sheet]`
   (the bridge `frame` command under the hood, never fronting the app; it writes the frames, the
   per-graphic contact sheets and the INDEX.md the reviewers are handed); Resolve = a real render
   (never `get_thumbnail_image`); CapCut = an
   export or window `shot`. Reuse frames across reviewers: grab once per round. Hand every
   reviewer the `qa-report.json` too, so they know what is already proven.
2. **Review fan-out: TWO dimensions, not four (2026-09-02).** Two subagents one tier below the
   session, one per dimension (not per graphic). **Over 10 graphics, split the copy/depiction
   dimension into TWO agents by graphic range and run them concurrently — it is the bottleneck. On
   every round after the first, hand reviewers full in/mid/out frames ONLY for graphics changed
   since the last round, plus ONE mid-frame contact sheet of the unchanged rest**: still a full
   round, just not re-measured where nothing moved.
   - **Copy, plan fidelity and depiction**, the irreducible LLM dimension, prompted exactly as
     before. It alone found the invisible icon on its own plate, the caps on a number-completing
     fragment, the tie hanging below the body, the missing "=" between two totals.
   - **Motion and rhythm adjudication**: receives the QA report and reviews only intent,
     cross-graphic rhythm, density feel and role-tracked entrances; it does NOT re-measure
     anything the report already measured.
   The composition/face/band and timing dimensions are retired from the fan-out: face coverage,
   the band sweep and word-anchor timing are the script's. Each prompt is self-contained: the
   defect-class list, the original request and accepted corrections, the applicable preset requirements,
   the plan JSON, the frame paths, the final transcript slice and ending, the QA report. Include the
   exact written source for prompt demonstrations and the source manifest for real captures. Never
   the whole CLAUDE.md, never this repo's history. **The brief itself is
   `reference/review-pack.md`**, copied to `projects/<job>/hf-graphics/review/PACK.md` with the
   job's paths, fps and band filled in: it POINTS at the defect classes above, it never restates
   them. Findings must carry evidence: graphic id, frame
   path or timestamp, expected vs actual.
3. **Verify.** Each finding gets ONE skeptic (same tier) prompted to refute it from the same
   evidence. The main session adjudicates disputes. Unverified findings are dropped: a
   hallucinated defect that reaches the fix stage burns a render for nothing.
4. **Fix.** The main session fixes verified defects only, part-by-part per the `graphics-build`
   incremental mechanics: edit the one comp, re-render the one part, re-place
   (`place-graphics.py --apply` swaps the versioned file). Never a full re-render for one fix.
   **Fix the root cause everywhere it appears, not the instance reported** (round 2 named
   `g4.html:58` and round 3 re-raised the same thing on its neighbour).
5. **Targeted re-check: MANDATORY, never skipped (see the stop condition).** Re-run the gate on
   the changed graphics only, into a round-scoped report:
   `uv run workflows/graphics-qa.py projects/<job> --ids <changed> --json projects/<job>/hf-graphics/qa-report.round<N>.json`,
   never the shared `qa-report.json`: a targeted run measures only the ids you named, so writing
   it there replaces the full report the gate and the reviewers read. Then ONE agent re-reviews
   only their windows, **CONCURRENTLY with the next full round (2026-09-07: running it alongside
   saved a full round's wall time on a 2h42 run whose loop was 1h41)**, so a bad fix cannot survive
   into the round that ends the loop. Two conditions make the concurrency safe: (a) re-grab the
   changed graphics FIRST, so the round's reviewers and the re-check both read those fresh frames
   and never the pre-fix set; (b) a failed re-check means that round does NOT count as the clean
   round, whatever it reported on that graphic. Reviewers get a changed-since list and must not
   re-measure unchanged comps.

**Stop condition: the script green AND one full round with zero verified findings (2026-09-01, gate added 2026-09-02).** A clean round costs two reviewers plus an evidence grab, and
a second identical fan-out finding what the first missed is a low-probability event, the
reviewers are stochastic, not sharper on a re-run.

**What that shifts, and the one thing to hold onto:** the fixes from the last defective round get
**one** full review, so **step 5 above is load-bearing rather than a nicety.** The targeted
re-check is what still catches a fix that broke its neighbour, and skipping it turns the stop
condition into shipping a repair nobody looked at twice. Run it after every fix batch, without
exception.

**Expected shape: 2 full rounds. Hard cap: 3.** If a third round still finds something, the next
move is a new assertion in `graphics-qa.py`, not a fourth round; stop and report what is open
(something structural is wrong; a human call is needed).

## Final gate: after the loop dries

- Respect the requested finish surface. **A timeline-only/no-export request ends at saved,
  placed and verified.** Otherwise chat-only = final assemble; Resolve/CapCut = the app's export
  with its locked settings; Premiere export runs only when authorized, using its lane recipe
  (AME stays banned). A proof frame or audio QA bounce is not a final video export.
- Re-run the final dialogue dead-air gate on the final saved EDL, timeline-only jobs included
  (command, threshold and the pinned-boundary caveat: `rough-cut` § Final dialogue dead-air gate),
  and re-read the closing paragraph against the raw outro (`rough-cut` § The Edit Philosophy — the
  filmed closure and handoff are protected).
- Read back the finished edit: dialogue matches the final EDL, every placed graphic is online and
  enabled on its intended track at its planned in-out, no unintended gaps or duplicates, final
  duration intact, project saved. A file existing, a placer returning success, or a plan counting
  correctly does not establish that its graphics render on the timeline. HOW per lane:
  [`LANES.md`](../../../LANES.md) § steps 5–8 and that lane's skill. On a lane with no live
  timeline (chat-only) these are N/A and the assemble render is the proof; an assertion a lane
  cannot read back is announced as unverified, per `LANES.md` § When you hit a ⛔ or a ⚠️.
- After SFX placement or any subsequent change, verify actual cue positions and levels against
  the reviewed plan, with no missing or extra cues; interrupted placement needs this same check.
  For affected-ID updates preserve approved cues and levels elsewhere. Verify requested music at
  its sustained entrance and current bed level using the background-music skill. These audio
  checks close after step 6; earlier graphics QA cannot certify future audio placement. Reopened
  or appended material re-enters the affected graphics/SFX checks before being called finished.
- `uv run.claude/skills/rough-cut/scripts/audio-qa.py projects/<job>` where the lane rendered a
  flat cut (it reads `outputs/<job>.mp4` + `transcript/cuts.json`, not the final deliverable — on a
  Premiere lane there is no flat render, so say it was skipped);
  `uv run workflows/face-frame.py <base-cut> --verify <draft>` on the full-tier split-frame explainer
  only (must print ✓ PASS; the basic explainer tier lays cards over the untouched raw and has no crop).
- **Report:** rounds run, found→fixed per round, per-`⚠️` deviations that stand, and the final
  deliverable or saved project linked with its absolute path, and any specific unfinished check.
  Claim only evidence actually gathered; a timeline-only finish reports no export. Then hand off
  for the creator's watch.

## Token efficiency: the rules

- **Every subagent runs one tier below the session** (Fable → Opus, `model: opus`; Opus →
  Sonnet). The main session keeps the creative work: adjudication, fixes, final judgment. Never fan
  out at the session's own tier, `agent` inherits it unless `model` is passed.
- **The script runs first and is free**, and it is why the fan-out is this small.
- Reviewers are per-DIMENSION (2 per round), not per-graphic. Skeptics spawn only per finding,
  so a clean round costs 2 agents and nothing more.
- **Never poll for a subagent to finish.** The harness sends a notification when an agent completes;
  a Bash `until` loop grepping its transcript for a completion marker matched nothing on your-job
  (2026-09-04) and ran to its 10-minute timeout six times, ~20 minutes of dead wait on a run whose
  agents were already done. Launch the agents, do independent work (SFX dry plan, RUN.md, the next
  grabs), and let the notification wake you. There is nothing to wait FOR.
- **A re-check measures the finding's OWN metric, not a proxy.** The g15 bracket re-check passed a
  soft-shadow fix on window max-minus-min luma (which the shadow inflates) while the defect was
  stroke-vs-adjacent-background contrast, so round 2 flagged it again. When a finding names a
  measurement, the re-check repeats THAT measurement on the new frame.
- Grab evidence once per round; don't re-send unchanged frames. Targeted re-checks before full
  rounds keep round count down.
- Lots of graphics (a long-form job, ~10+): orchestrate the fan-out as one Workflow
  (review dimensions → per-finding skeptics as pipeline stages). A handful: plain Agent calls.

## Handoff: where this skill ends

When the loop dries, **step 5 (Graphics) is done and the job moves to step 6 (SFX)** — not
straight to the creator. That order is deliberate: SFX are aligned to graphic beats, so any
graphic this loop retimes would silently orphan its sound if the sound were already laid.
(The handoff is step 6: `uv run workflows/sfx-plan.py projects/<job>` then the lane's placer, or hand-placing from the cut sheet on a lane with none. Never skip it in silence.)

The moment the creator starts calling live adjustments at **step 7**, this loop is over. Those
tweak rounds follow the second-pass rule: edit, render, show, no self-QA frame grabs (the fixes
get called live from the review).

## Not this skill

Reviewing the rough cut — the `rough-cut` skill carries its OWN fresh-eyes second pass
(§ Fresh-eyes second pass: one script-flow + one mechanical reviewer, both one tier below the session's model,
run before the cut ships; added 2026-08-28) — this loop starts after graphics · deciding or building graphics (5a/5b) ·
captions, music, export mechanics · anything in the banned-findings list.
