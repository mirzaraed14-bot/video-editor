---
name: graphics-plan
description: "Storyboards the graphics for a video BEFORE any are built — the creative-direction step (5a) between the graded cut and the build. Reads the finished-script transcript, builds a narrative beat sheet, probes the footage, then storyboards every graphic (exact copy, placement, timing, motion) and self-reviews the whole plan so the FIRST pass ships at review quality. Outputs graphics-plan.{json,md}. Does NOT create graphics. Triggers: plan the graphics, graphics plan, where should graphics go, ideate graphics, what graphics for this, graphic direction, storyboard the graphics, beat sheet, plan visuals for this reel."
---

# Graphics Plan — beat sheet → storyboard → self-review

**Step 5a of the pipeline.** Rough-cut already produced the finished script (the cut-aligned
transcript). This skill turns that script into a **storyboard**: a beat-by-beat plan of
graphic-or-not, what exactly appears, where, when, and how it moves — *before anything is built*.
The creation step (5b) builds from this plan, captions included on short-form (see § The captions cell). The colour grade is step 4 and
is already on the timeline before this plan is written.

**The bar: one-shot quality.** The plan must be good enough that the build needs no
back-and-forth — every correction the creator would make on a review pass, this skill makes on itself
in Step 4 before you ever sees the plan. A plan that needs "you should have made this a graphic"
afterward is a failed plan, not a draft.

**This skill decides graphics. It does not create them.** No rendering, no HyperFrames, no HTML.

---

## 🔒 STEP 0 — resolve the preset + the tier (before any planning)

**The preset is decided by format, automatically.** Format was auto-detected at intake (horizontal
raw → long-form YouTube; vertical → short-form, explainer vs TikTok/raw read from the content).
Each format has exactly one default preset, and presets are fully independent — read ONLY the
chosen preset's own docs, never another preset's:

| Format | Default preset | Read |
|---|---|---|
| long-form YouTube | `presets/youtube/default/` | its `README.md` + `default-overlay-style.md` + **`creative-moves.md` (the default vocabulary AND § THE DENSITY NUMBERS — the per-minute cadence you plan to)** |
| short explainer | `presets/instagram/explainer/` | its `default-overlay-style.md` |
| TikTok/raw | `presets/tiktok/raw/` | its style doc — **hook card only, plan nothing else** |

**A named preset overrides the default** — "edit this in the Vox style" → `presets/youtube/vox-collage/`
(and its `motion-craft.md` craft layer), "liquid-glass" → `presets/youtube/liquid-glass/`. Only an
explicit name switches presets; nothing else does.

> **"Do a graphics pass" = the BASIC tier. Always. Assume nothing bigger.**

| Tier | Trigger | What it is |
|---|---|---|
| **Basic** ← DEFAULT | "edit this video", "do the graphics", "graphics pass" | the preset's `default-overlay-style.md`: face-clear cards plus its default scenes, captures and prompt demonstrations; 4–7 is the card ceiling, not the whole graphics pass. |
| **Full** | asked for **by name** — "go all out", "full graphics pass", names a look | takeovers, bespoke art, higher density, whatever the named preset's doc says |

**A tier is never inferred from how good the footage is.** An exciting script is not permission to
escalate. When a beat genuinely wants more than the tier allows, note it in the plan in one line
and plan within the tier anyway — upgrading is your call.

**Two things require an explicit ask (one line, at plan time, never mid-build):**
1. **Decorative extended full-frame coverage** — takeovers outside the preset's default vocabulary,
   bespoke art, background replacement. State the total second-count and get a yes unless already
   authorized. Short punch-cuts, real evidence captures and full-screen prompt walkthroughs are
   long-form DEFAULT work: plan them without asking. Required demonstrations last for their spoken
   explanation; track those seconds separately from the decorative coverage budget.
2. **A non-default look** you didn't already name.

---

## Step 1 — the BEAT SHEET (understand the video before decorating it)

```bash
uv run .claude/skills/graphics-plan/scripts/segment-script.py projects/<job> /tmp/video-editor/<job>/beats.json
```

That gives the mechanical grid (sentence beats + timestamps). The beat sheet is what you ADD to it —
read the whole script first and answer, in order:

1. **The arc.** What is this video actually about, in one sentence? What are its 2–3 biggest
   moments (the hook, the core reveal/demo, the payoff)? The storyboard is built around these;
   everything else supports them.
2. **Per beat, its narrative role:** `hook` · `promise` · `setup` · `point` · `evidence` ·
   `demo` · `payoff` · `punchline` · `transition` · `aside`. Merge or split the mechanical beats
   freely when the story says so — the grid is a starting point, not a contract.
3. **Per beat, the showables:** every concrete noun the line contains — a number, a name, a
   product, a process, a before/after, a list. These are the graphic candidates. A beat with no
   showable almost never earns a graphic.

**Read the original request and all later corrections alongside the script.** A transcript cannot
tell you the exact written prompt, which of your own pages or accounts a line points at, or whether
the closing lines hand off into another video. Resolve those sources before assigning visuals. Put
each required demonstration and its source in the relevant cell's `content`/`capture`; unresolved
source access is a recorded gap, never silent permission for a generic substitute. Re-run this
mapping after cuts restore or add footage, through the final kept sentence.

Write the roles into the plan (`role` field). The beat sheet IS the first deliverable — a wrong
beat sheet makes every downstream choice wrong.

## Step 2 — look at the footage (never storyboard blind)

```bash
uv run .claude/skills/graphics-plan/scripts/probe-frames.py projects/<job> /tmp/video-editor/<job>/beats.json
```

One frame per beat lands in `projects/<job>/plan-frames/` (regenerable scratch — re-runnable at any
time; `prune.sh` does not remove it. Works from the flat render or, on app-finish jobs, straight from
the raw via the EDL). Actually look at them. They decide:

- **Screen-recording beats already show the thing** — a demo that's on screen needs an annotation
  or nothing, never a card summarizing what's visible. This is the #1 wasted-graphic mistake.
- **Placement** comes from where you actually is in frame (side to place a card, where your head is),
  not from a guess. **A side callout's zone is MEASURED over the beat's whole window**, never read off
  one frame: `uv run workflows/chin-line.py <raw> --edl <cuts.json> --from <start> --to <end> --step 0.1`
  prints the head's extent (ears included, worst frame), the two zones and the side with more room
  (preset § SIDE CALLOUTS). The cell records what it measured as `head`.
- **Gestures** — a point/hold toward one side is an anchor for that beat's graphic.
- **Energy** — a big delivery moment on camera may land harder plain.

## Step 3 — STORYBOARD the graphics (the creative core)

Walk the beat sheet in story order and decide each beat. **Big moves must earn their slot** — a
full graphic gets planned only when:

- it's the **hook** (the hook always gets the strongest visual in the video),
- it's a **payoff/punchline** worth underlining,
- it has a **showable** the frame isn't already showing (stat, name, list, process, artifact),
- it's a **structure beat** a diagram/flow would make instantly clearer.

**Full-screens: the cadence AND the spread (2026-09-10).** 2–3 per minute, spaced across the
whole runtime — never 40 s of runtime without one, and the back half gets its share (three in the
first 41 s and none after is the failure this rule was written on). A payoff LINE gets the bg-light
TEXT punch-cut; an artifact or a process gets the dark one (`creative-moves.md` move 2, the two
references). `validate-plan.py` warns on the gap and the rate.

Leave BIG moves off: connective tissue, transitions, asides, emotional delivery, rhetorical
setup — those land harder on your face. But on long-form, "plain" is bounded by the RHYTHM LAW
(below): a bare stretch gets a text animation. The law gives a FLOOR (something every ~10s, you
2026-08-29); the ENFORCED bound is tighter — no bare stretch over 6s (`creative-moves.md` § THE
DENSITY NUMBERS, warned by `validate-plan.py` and `graphics-qa.py`). **Plan to 6s.** And **never let
two graphics collide on adjacent short beats**: merge them or let one breathe.

**Spend the creativity where it counts.** For the hook and each major payoff, draft **2–3 distinct
options** and keep the strongest (say why in one clause). Ordinary beats get one good idea, not a
brainstorm. Visuals over text everywhere: the motion/footage/data carries the point; words are a
label, a number, or a hook line. Reserve text-forward cards for hook + punchlines, and remember
**captions are the top layer of this same step** (short-form) — don't fill the frame with text a caption will collide with.

**Every `graphic:true` beat is a complete storyboard cell** — the build must need zero guesses:

- **`kind`** — from the vocabulary below, **`template`** — which of the preset's templates it uses (basic tier).
- **`copy`** — the EXACT on-screen words/numbers. Not "a stat card about the revenue" — `"$4,700 / mo"`.
- **`region` + side** — from the Step-2 frame, inside the format's safe zones. **On long-form,
  anything CENTERED under your head goes in THE LOW BAND** (`presets/youtube/default/default-overlay-style.md`
  § THE LOW BAND): the whole stack fits between the measured chin floor and the bottom margin,
  and a two-line block is therefore SMALLER and LOWER than a one-liner. Record the measured band in
  the plan as `low_band {top, bottom, chin_measured}` — it is what `graphics-qa.py` holds every
  under-the-face overlay to; omitted, the gate falls back to the 2026-08-31 shoot's 765/1030. A
  `callout-L` / `callout-R`
  cell carries `head` (`{left, right, frame}` from `chin-line.py --edl` over ITS window — copy
  chin-line's own `frame`, which normalises a 4K measurement into the authoring frame), sits on the
  side with more room, and is as wide as that room (cap 620); `validate-plan.py` fails a callout cell
  without a measured head. Full-screens have no face to clear.
- **`start` / `end`** — snapped to word timestamps: in ON the word that names the showable (not the
  sentence start), out before the next thought begins. 2–5s on screen for a CARD; a card that overstays reads as a mistake.
  A SCENE that depicts an unfolding process runs as long as the process does (the shipped chat
  ping-pong graphic holds 8.6s) — the limit there is the beat, not the clock. **Name the anchor
  word and its transcript time in `content` for every cut-in and word-synced entrance** ("cut in
  ~30 ms before 'one' 4.41"): the hook on your-job was first computed off "shot," because the
  phrase was read as a unit; the validator warns on a cut-in that leads no word. **A READABLE graphic needs more:** if the beat shows something the
  viewer is meant to read or screenshot (a prompt, a command, code, a config, a quote), the slot
  must fit a **2–3s hold of the COMPLETE content** on top of its reveal — say so in `content` and
  size the slot for it, or flag `⚠️` that the text is too long for the beat. For a prompt walkthrough,
  `source_artifact` names a job-relative UTF-8 file containing the complete original written artifact — copy
  the original text into the job folder (`assets/`) when it lives outside it; `copy` matches that file in
  full, and any readable cell whose words come from a written artifact names it (the validator checks both).
  `content` names the source provenance and maps spoken anchors to the actual highlighted
  clauses. Its full-screen slot covers the entire explanation, not merely the minimum hold
  (`creative-moves.md` § 4d).
- **`content`** — one tight paragraph: what's on screen, the hierarchy, the hero element, and the
  motion (what animates, in what order). Written so the build step can build it without asking.
- **`reason`** — why this beat earns it (the second pass reads these).
- **`phases` + `visuals`** (full-screen / punch-cut cells only) — a full-screen is a SCENE
  (`creative-moves.md` move 2 § A FULL-SCREEN IS A SCENE, you 2026-09-10): `"phases"` lists at least
  two visual beats with comp-relative times (`[{"at": 0, "what": "the wall is back, struck through"},
  {"at": 1.83, "what": "racks out under the type"}]`), `"visuals"` names at least one element that
  is not type (a picture, an artifact, a prop, a diagram, a UI), and `content` names the camera move
  and, when type lands over the scene, the rack focus. `validate-plan.py` fails the cell without them.
- **`bg`** (full-screen / punch-cut cells only) — ALWAYS written on a full-screen cell
  (`validate-plan.py` fails it otherwise); `"dark"` unless the visual reads better light (2026-09-10; no rotation). It is not decoration: it
  drives locked render flags (**bg-dark = `STEP_FPS=12` + the glow pass; bg-light = neither**).
- **`push_in`** (long-form A-roll beats) — `true` where the footage should push in on the
  emphasized phrase (numbers: the preset README § Emphasis push-in; when to reach for it: `creative-moves.md` move 5). This is a
  DEFAULT move, so plan it rather than waiting to be asked, but ration it: **2–3 per minute of
  runtime, spread** — none closer than ~7 s, no long stretch without one, on the beats carrying the
  strongest claims (`creative-moves.md` § THE DENSITY NUMBERS owns the figure; `validate-plan.py` prints the rate).
  Pick them from the SCRIPT — the line that lands the claim, the reveal, the stakes — and pair each
  with the text animation of that phrase. Everything else stays still; a push-in on every emphasis
  reads as a wobble.
- **`entrance`** (`text-animation` cells only) — omit for the default rise; `"slam"` by name for the
  punchline that has to hit. **Never `pop`/`punch`: type never pops**
  (`presets/youtube/default/animations.md` § TEXT NEVER POPS); `validate-plan.py` fails the cell.

| Kind | Use it for |
|------|-----------|
| `screen-rec` | the thing actually working — a demo, the agent running, a folder, an app state, a click (real footage with real continuous motion — a scroll, a navigation, a UI action — not a card and not a still given a move). No file yet → the cell carries `capture` and the BUILD records it (§ THE CAPTURE GATE below) |
| `b-roll` | illustrative motion footage over a claim (generate one with your AI-video tool if none exists) |
| `screenshot` | the real artifact — a post, a report, a DM (zoom/pan/annotate it, never park it). No file yet → `capture` with `"still": true` (a covered-window grab, the app is never fronted) |
| `diagram` / `flow` | how it works — steps/pipeline, drawn ON as you talk |
| `data-viz` | numbers in motion — a chart drawing in, a count-up, a ranking |
| `stat-callout` | a single number as a beat — counted up / popped, never static |
| `icon-row` / `list` | a set of things, revealed in sequence |
| `quote` / `comment` | a comment, tweet, DM, testimonial |
| `lower-third` | a name / title / label (long-form) |
| `kinetic-title` | hook + punchlines only — the words ARE the payoff |
| `text-animation` | long-form's default sprinkle — word-synced emphasis text in the low band (the rhythm-law filler; uncounted against the card budget) |
| `punch-cut` | long-form default: hard cut to a short full-screen graphic on a locked background at a power phrase, hard cut back (creative-moves move 2) |
| `annotation` | arrow/highlight/circle pointing at something already on screen |
| `enacting-overlay` | the line is about the FOOTAGE itself (recorded, filmed, captured, live) — add capture UI (viewfinder brackets, a REC dot, a timecode) so the untouched shot reads as that thing, plus a text animation for the words. Purely additive, face never covered, no transform on the footage. Model: g20 |

**🔒 THE CAPTURE GATE (2026-09-11) — a screen capture is PLANNED, never improvised, and TEXT IS NEVER
CAPTURED.** A beat gets a `screen-rec` / `screenshot` cell with `capture` when the line points at a real
thing on your screen that IS the evidence and cannot be re-typed: a folder tree, an app's state, a click
you describes making, a timeline filling up, a page that exists. The build records exactly that (Stage 2)
and the comp builds it as a scene to the preset's look (`default-overlay-style.md` § SCREEN-REC SCENES:
straight frame, label and arrow on the label's side, bg-light) — never parked full-frame. It does
NOT apply when the content is words: a prompt, a command, a config, a quote is REBUILT word for word from
the exact written source as a graphic (house type, highlight phases, the readable hold), because a screenshot of a
chat window gets none of that. A list of tool NAMES is a card, not four screen grabs. And a beat whose
footage already IS a screen recording needs an annotation or nothing (Step 2). When a line names a
specific real destination — a page, an account, a product, a place something is downloaded from — the
capture is THAT destination itself; a generic badge, a stock icon or a public marketing page for the
same brand is not it. The cell says what to capture and what happens during the take:

```json
"capture": {"source": "url", "target": "https://github.com/heygen-com/hyperframes", "action": "the repo landing page, the README scrolling slowly through the take", "scroll": 900, "dark": true, "seconds": 6}
"capture": {"source": "app", "target": "Finder", "action": "the repo root in list view, presets/ expanded", "still": true}
```

`source` is `url` (a page: recorded HEADLESSLY by `workflows/page-record.mjs`,
never through your live browser — a `scroll` in px and `dark` ride in the cell) or `app` (a running app's
biggest window, `index` for another, recorded on screen by `workflows/screen-record.sh`); `seconds` is the
take (recordings only); `still` makes it a screenshot cell's grab.
A page behind a login is planned as `source: "app"` with the browser as `target` and the real URL
stated in `action`; the build records it (`graphics-build` § Stage 2). A redirect to a sign-in or
sales page is not evidence of the real thing.
`validate-plan.py` fails a `screen-rec` / `screenshot` cell that has neither an `asset` already in the job
folder nor a `capture`.

**Density — long-form youtube/default runs the RHYTHM LAW (2026-08-29): at least one
visual event every ~10 seconds, no bare stretches — and the enforced bound is tighter, no bare
stretch over 6s (`creative-moves.md` § THE DENSITY NUMBERS). Plan to 6s.** Big moves (punch cuts, cards, charts, props)
on the beats that earn them; **text animations fill every gap** that would otherwise sit empty — they
are the always-available default. A stretch where the script DESCRIBES something visual gets
CONTINUOUS graphics for its whole run (30s of visual storytelling = 30s of visuals). The 4–7
budget still scopes the CARD count per intro/section; pops and creative moves ride on top,
uncounted. Short-form keeps 4–7 per section; TikTok/raw: exactly the hook card. Full-tier
densities live in the chosen preset's own doc.

**Long-form structure beats** are part of the plan too: the section title cards, the cold-open, and
chapter boundaries come from `presets/youtube/default/README.md` — the storyboard places graphics
AROUND that structure (a section's cards cluster early in the section where its claim lands).

**Safe zones (short-form, never break):** open the preset you are on — the bands are its style doc's
(explainer § Placement; TikTok/raw § THE LOOK), not restated here. **Long-form has NO
platform safe bands (retired 2026-08-27):** the rules are never cover the face or important
on-screen content, 80 px breathing room at the frame edge, 60 px between a side callout and the
head (ears included, measured per window — preset § SIDE CALLOUTS), right side + bottom clear
during an actual end-screen window, and every under-the-face overlay inside THE LOW BAND (measured per
shoot with `workflows/chin-line.py` — spec in the preset's `default-overlay-style.md`).

## Step 4 — SELF-REVIEW (run the review pass the creator would otherwise run)

Re-read the finished storyboard top to bottom as a reviewer, not the author. Fix everything below
BEFORE writing the plan — these are the exact corrections past first passes needed:

1. **Missed requirements/showables** — compare the original request, later corrections and full
   kept script to the storyboard, not merely the storyboard to itself. Every required prompt,
   real named destination and closing beat has the right content and full time coverage?
   Any number, name, list or artifact got no graphic and no `reason` for staying plain?
2. **Wasted graphics** — any card restating what the frame already shows (screen recordings!), or
   summarizing instead of showing?
2c. **A line about the footage itself given a CARD?** "I recorded this", "I filmed the whole
   thing", "this is live" — those want an `enacting-overlay` (capture UI over the untouched
   shot + a text animation), which enacts like a scene at a card's cost. See
   `default-overlay-style.md` § the overlay that enacts.
2b. **Card where a SCENE was needed** — for every `graphic:true` beat, does the line state a
   fact/number/name (card) or describe an action/process/back-and-forth (scene that shows it
   happening)? A card on an action beat narrates instead of depicting. The tell is decoration
   shaped like data — a meter with no scale, a bar with no metric. See
   `presets/youtube/default/default-overlay-style.md` § CARDS NAME, SCENES ENACT.
2d. **A real thing on your screen given a drawn stand-in, or words given a screenshot?** A folder, an
   app state, a click, a page that exists wants a `capture` cell (§ THE CAPTURE GATE); a prompt,
   command or quote is rebuilt verbatim from its written source as a graphic. For a prompt
   walkthrough, verify complete text, continuous full-screen coverage and spoken-clause highlights.
3. **Rhythm** — graphics evenly clumped or breathing with the story? A payoff needs a beat of air
   after it, not a new CARD on top of it, and no two cards butt end-to-end. **Text animations are
   exempt** — they are the connective tissue that keeps the ~10s floor, and they legitimately run
   back to back. Check the plan against `creative-moves.md` § THE DENSITY NUMBERS — that table is
   the one home of the figures, and `graphics-qa.py` and `validate-plan.py` enforce it. Review
   dark full-screen scenes across the whole runtime, including new/restored outro footage; a
   cluster of light recordings does not replace the preset's dark scene vocabulary.
4. **Variety** — three of the same template in a row reads as a stamp. Vary template, side, and
   scale across neighbors.
5. **Timing** — does each `start` sit on the word that earns it? Does anything overstay?
6. **Copy** — labels are short and in your voice (no marketing speak, no em dashes in authored
   copy); source artifacts retain their complete text, punctuation and case. **Case depends on what the copy IS:** captions and
   text animations stand in for speech and keep the lowercase-casual register; a LABEL inside
   a graphic (card title, nameplate, eyebrow, axis) is not speech and takes title case.
   A leading article drops only when the label NAMES a thing ("Claude Video Editor", never
   "the claude video editor") — in a short descriptive label the article is part of the
   phrase and stays ("The Goal", the eyebrows THE BUILD / THE RULES). Test: answers "what
   is this thing called?" → drop it; answers "what is this number/row?" → keep it
   (default-overlay-style.md § Copy case, you 2026-08-31).
7. **Scope** — count per section within tier, zero unplanned full-frame, overlays never cover the face,
   captions zone clear (short-form).
7b. **The band** (long-form) — every under-the-face cell sits inside the low band, and no cell
   is sized as if it had the whole frame. If a beat's copy needs two lines, the plan says two
   lines and expects smaller type; it does not ask for big type AND two lines.
8. **The two asks** — full-frame seconds + non-default look, each stated in one line if present.

Revise the plan, then output. If a beat is genuinely 50/50, keep your call and flag it `⚠️` — one
flag you can answer beats a timid plan.

## Step 5 — write the plan + report

**The gate (2026-09-02): a plan that fails this is not PRESENTED.** The order is: write
`projects/<job>/graphics-plan.json` → run the validator → fix and re-run until it exits 0 → then
write `graphics-plan.md` and report.

```bash
uv run .claude/skills/graphics-plan/scripts/validate-plan.py projects/<job>
```

It asserts what the build and the review loop otherwise pay for later: every text-animation cell
STARTS on the first word of its own copy (word − 0.08, within 0.15s, not the sentence, not a guess);
every full-screen edge within 8 frames of a `cuts.json` boundary sits ON it to the frame (off by
one flashes the outgoing shot, g2, g11 and g7 all shipped that way; an edge far from any cut is a
cut back mid-take and passes); a cell flagged `"readable": true` holds ≥ 3.0s; a text-animation
cell longer than 8.0s FAILS (a start anchored to the wrong occurrence of its first word, g11,
2026-09-04); no em dash in copy;
text animations keep the lowercase register; ids unique, fields present; and it prints the density
block against § THE DENSITY NUMBERS. Write the copy AS IT WILL BE SPOKEN for text animations (the
builder matches the transcript verbatim; a filler mid-phrase is skipped automatically, a
paraphrase is not).

The two reviewed artifacts in the job folder:

- **`projects/<job>/graphics-plan.json`** — machine-readable, consumed by the build (schema below).
- **`projects/<job>/graphics-plan.md`** — the storyboard for your review, and what the second pass
  edits: the arc line, the beat sheet, then per-graphic cells (`# · time · line · role · template ·
  copy · placement · motion · why`), plain beats listed with their reasons.

Report tight: **the preset + tier**, the arc in one line, beats total / graphics count,
**face-covered seconds**, the 2–3 strongest cells, any `⚠️` flags, and the explicit asks if any.

### `graphics-plan.json` schema

```json
{
  "job": "your-job",
  "format": "short-explainer",
  "tier": "basic",
  "preset": "<the chosen preset's style-doc path>",
  "compositor": "premiere",   // the app finish; "resolve" | "capcut" | omit = chat-only
  "duration": 136.56,
  "arc": "one sentence: what the video is and its biggest moment",
  "face_covered_seconds": 0,
  "low_band": {"top": 773, "bottom": 1030, "chin_measured": 703, "note": "chin-line.py sweep of the raw: lowest jaw y703, floor = chin + 70"},   // long-form: the MEASURED band, what graphics-qa.py holds every under-face overlay to; omit on short-form
  "beats": [
    {
      "id": 1, "start": 0.05, "end": 5.03,
      "line": "I just built this Claude skill that can predict exactly what you need to post to go viral.",
      "role": "hook",
      "graphic": true,
      "kind": "kinetic-title",
      "template": "label card",
      "region": "top-half",
      "copy": "predict what goes VIRAL",
      "content": "Hook title, hero word 'VIRAL' in a royal boxed chip that stamps in last; two-line stack, stepped entrance.",
      "phases": [{"at": 0, "what": "the two-line stack rises in"}, {"at": 1.2, "what": "'VIRAL' stamps into its chip, stack racks back"}],
      "visuals": ["the royal chip prop behind the hero word"],   // full-screen/punch-cut cells: ≥2 phases, ≥1 non-type visual
      "bg": "dark",            // full-screen/punch-cut cells (long-form); omit on short-form
      "entrance": "slam",      // text-animation cells only; omit = rise. never "pop"
      "push_in": false,        // long-form A-roll only; omit on short-form
      "part_of": "g8",         // continuation cells only: a graphic split for BUILD reasons is planned as part cells, the stem cell carrying the scene fields and each continuation carrying "part_of", validated as ONE graphic
      "source_artifact": "assets/original-prompt.txt", // required on any readable cell whose words are a written artifact; omit only for authored labels and captured files, copy must match this complete file
      "readable": false,       // true when the viewer is meant to READ it (prompt, code, quote): the slot must hold ≥ 3.0s
      "capture": {"source": "url"|"app", "target": "https://…"|"Finder", "action": "what happens during the take", "seconds": 5, "scroll": 900, "dark": true, "index": 1, "still": false},   // screen-rec / screenshot cells with no file yet: the build records it (§ THE CAPTURE GATE); or "asset": "assets/x.png" for a file already in the job
      "reason": "the hook — must open on the strongest visual in the video"
    },
    {
      "id": 2, "start": 5.17, "end": 6.49,
      "line": "And yeah, it works.",
      "role": "punchline",
      "graphic": false,
      "reason": "delivery beat — lands harder on your face, air after the hook"
    }
  ]
}
```

Keep `graphic:false` beats in the array (with `role` + `reason`) so the plan is a complete map of
the script — the second pass needs the plain beats too.

---

### The captions cell (short-form presets, on by default — 2026-09-04)

Captions are a graphic of this step, not a pass. On `instagram/explainer` and `tiktok/raw` the plan
carries ONE extra cell spanning the whole cut, and the build lays it on the top graphics track like
any other overlay (long-form never has one — YouTube CC):

```json
{ "id": "captions", "start": 0, "end": <plan.duration>, "graphic": true, "kind": "captions",
  "region": "captions", "content": "the preset's locked caption layer (explainer: centered on the seam · tiktok/raw: low under the face), built by the preset's caption builder (tiktok/raw: build.py --alpha; explainer: the job copy of build.py with ALPHA = True, then its printed render command)" }
```

`validate-plan.py` keeps it out of the density, overlap and anti-stale maths; the lane's placer derives
its row from `hf-graphics/captions/renders/captions-alpha.mov` onto a track above every other overlay
(which track is the lane's business: [`LANES.md`](../../../LANES.md) § step 5); `sfx-plan.py` ignores
it (captions are silent). Every other cell still plans AROUND the caption zone — that rule did not move.

## Handoff

The plan feeds **step 5b: the `graphics-build` skill owns the whole build** — it builds each
`graphic:true` beat at its `start`/`end` in its `region` per `template` + `copy` + `content`,
renders, places, and QAs. **On an app finish** set
`"compositor"` so the build knows the target: `"premiere"` (alpha overlays on the preset's graphics track + baked
footage moves, per the `premiere-pro` skill), `"capcut"` (`lanes/capcut/capcut-bridge.py`), or `"resolve"`
(the `davinci-resolve` skill § Step 5). `b-roll`/`motion-graphic` beats with no real
footage go through your AI-video tool, then composite like any part. Then the **second pass** adjusts.

This skill does ONE thing: decide the graphics. It never renders.
