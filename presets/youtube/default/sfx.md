# SFX — the youtube/default sound design (pipeline step 6)

**WHAT only.** Which sound lands on which motion event, how it is sliced, how loud, and how the
layers stack. Every number here is app-independent. Placing a clip on a timeline is a lane
mechanic: [`LANES.md`](../../../LANES.md) § step 6 (Premiere: `lanes/premiere/place-sfx.py`).

Measured off the one shipped sound design, a hand-placed reference intro: 65 clips, 51
onsets, every one frame-grabbed and level-measured. The machine-readable copy is
[`sfx.json`](sfx.json); [`workflows/sfx-plan.py`](../../../workflows/sfx-plan.py) reads it and
turns the placed graphics into `projects/<job>/hf-graphics/sfx-plan.{json,md}`.

## The law

1. **Events come from the graphics, not from the transcript.** Every registry call a comp makes
   (`pop`, `slam`, `riseIn`, `slideIn`, `slideOut`, `drawOn`, `countUp`, `reveal`), every word of a
   text animation rising in, and every hard cut INTO a full-screen is an event. Cuts back to the
   face are not. Exits (`riseOut`, `exit`) are not. Talking-head stretches with no graphic get
   nothing.
2. **One sound per motion class, the same one every time.** Variation comes from slicing the file
   differently on a run, never from swapping sounds. The WOW is the singleton sting: not in the map, a plan-time
   call, one per piece at most. The bell (`payoff`) and the Impact (slam text, `emphasis`) ARE mapped
   events now — see § Sound follows MEANING.
3. **One-shots are sub-slices of the library file.** Each event class carries its slices in
   `sfx.json`; a run rotates through them so no two adjacent hits play the identical sample.
   Sustained classes (`countUp`, `reveal`) are cut to the event's duration.
4. **Timing is on the element's own onset**, snapped to the frame grid. A slide whoosh starts ON
   the slide start. A cut-in whoosh leads the cut by 2 frames; a riser ends 0.45s before it.
   Layers on one hit land on the same frame.
5. **Levels are class bands on the on-timeline peak**, so the clip level is target minus the
   measured slice peak, whole dB, never above +6. The seven bands and their targets are
   `targets_dbfs` in [`sfx.json`](sfx.json); transient sits at the voice ceiling and everything
   else is placed against it.
6. **Three SFX tracks by layer depth** (the roles `primary` / `layer2` / `layer3`, which are A2 /
   A3 / A4 on this preset's track map and map by role on a lane laid out differently)**:** the
   primary track carries the first sound of every event; a sound
   that would OVERLAP a different sound still ringing on a track goes a layer down (layer 2, then
   layer 3) so both play out, while the same sound repeating on top of itself stays on one track and truncates
   (the reference's machine-gun pops). An identical sound within 2 frames is a doubling and is
   dropped. Music takes the `music` role's own track (A5 here), opt-in. No fades on any SFX clip, every clip hard-trimmed to its slice.
7. **Density follows the graphics.** The reference intro ran 1.25 events/s inside the graphics
   span. A plan that sounds every registry event lands near that on its own; it never needs
   padding, and it is then thinned by the two rules in § Density before it is laid; step 7 is taste
   on top of that.

## The map

**Event → sound → why. The level, the slice and any frame offset for every row live in
[`sfx.json`](sfx.json)** — that file is what the planner reads, so read it there rather than
keeping a second copy in sync here.

| event | sound | why |
|---|---|---|
| `pop` (a free-standing object appears) | Pop 1 | the object's own snap |
| `slam` (an object stamps) | Metal Pop | heavier landing, so a heavier transient |
| `riseIn` (a card, panel, row or label rises) | **Simple Whoosh 1, the SECONDARY whoosh** | the whoosh for anything that RISES into place |
| `slideIn` / `slideOut` and any scene move | **Simple Whoosh 2, THE PRIMARY whoosh** | the whoosh for anything that MOVES across the frame |
| `drawOn` (a strike, an arrow, an underline) | Pencils & Markers | a real marker on paper is the stroke's sound |
| `countUp` (a number stepping) | UI Data Loading | a bed under a machine counting |
| `reveal` (text typing on) | Keyboard Typing | real typing at a real level, not a texture |
| `flash` (spelled `flicker` in older specs) | **Neon Flicker** (paired) | the sound IS the strobe: one at its START, nothing on the landing |
| word on a RISE text animation | Scissors | the snip carries the word without a transient per line |
| a RED word (negation) | **Error Buzz** (paired) | a negative beat sounds negative |
| ~~word on a POP text animation~~ | ~~Pop 1~~ | RETIRED 2026-09-10: type never pops (animations.md § TEXT NEVER POPS); the Pop is an object sound |
| word on a SLAM text animation | **Impact** | it lands on the settle; the run truncates itself and the last word rings |
| TYPE in a hand comp (an element whose OWN text is words) | rise → Scissors · slam → **Impact** | the text sounds follow the words into full-screens and cards, read off the markup; a label inside a node/row/chip stays with its surface (whoosh) |
| `emphasis` (a script-critical word, named in the comp or a hand row) | Impact | the word that has to hit; it loses its scissors |
| `row-tick` (a `pop` inside a list/card graphic) | Lighter | a switch clicking on, not an object |
| `payoff` (a COMPLETION state: the finished node, a check, 100 %, the green state — read off the markup, or a hand entry) | Bell Ding | the reward; replaces the pop / slam / row-tick the element would have made |
| `rec` (a RECORDING STARTS: the REC badge of a camera UI, named `data-sfx="rec"` in the comp) | Camera Beep & Shutter, the beep at 5.33 | approved by ear on g24 (2026-09-10); replaces the badge's pop |
| `gunshot` (NAMED: a literal shot, bullet holes) | Gunshot | the literal prop |
| `processing` (NAMED: software working) | UI Data Loading | the bed under a scrub / render / think span |
| `click` (NAMED: a cursor action in a software scene) | Mouse Click | the cursor arriving on its target |
| cut INTO a full-screen | Whoosh Short 2 | the cut's own sound; **dropped when a flash opens the full-screen** |
| the FIRST full-screen of the job | + Riser 2 | the piece's one build-up, whoosh or not |
| title card (section boundary) | Genius Intro Sound | the section's signature |
| `riseOut`, `exit`, cut back to face, push-in, an annotation's arrow | silent | nothing leaves with a sound |

### 🔒 Sound follows MEANING before mechanism (2026-09-10)

The event map above is the default, not a law. When a graphic SHOWS something — completion,
success, the green state, a check, 100 % — the sound represents that, and the mechanical entrance
sound steps aside. you, on the 'Postable Edit' node that popped: *"why isn't the postable edit
card a ding sound? … the reason you went with the pop is because that's the standard default sfx
for a pop animation … sfx aren't always so hard and fast like that."* `sfx-plan.py` reads the
completion signal off the comp (a completion class — `hi`, `done`, `check`, `success` —, completion
words in the element's own text, a green fill or stroke on it or inside it, a green CSS rule it
satisfies, or an explicit `data-sfx="payoff"`) and rings the bell instead; `data-sfx="pop"` opts
an element out. **The palette is the DOCUMENTED map, and only that (2026-09-10, after the
chat-bubble blips: "so fucking heinous … you shouldn't try to go out and find sound effects
yourself because you really don't have the ability to actually listen to what it sounds like").**
The freedom is in WHERE a documented sound goes, not in which files exist: a pop that shows
completion takes the bell, a slam takes the Impact, a negation the Error Buzz, a software scene its
processing bed and clicks — every one of them named in this table with where it belongs and how it
is sliced, and approved by ear. Nothing outside the table is ever placed, however apt the filename:
`assets/sfx/` holds 130 files and the map documents the ones that have been heard. Name a
documented event where the element is authored — `data-sfx="<event>"` swaps the element's
mechanical sound for any event in `sfx.json` (`emphasis`, `gunshot`, `processing`, `click`
included); `data-sfx="none"` silences an element — or in a hand row for a timing the parser cannot
bind. The planner refuses `data-sfx-file` and a hand row's `file` with a warning. A new sound
enters the palette one way: you listens, then it gets a row here and an entry in `sfx.json`.
A marker rides a REGISTRY event on that same element (its `pop`, `riseIn`, `slam`, `slideIn`…): a
prop that moves on a plain tween or a node that arrives inside a scene's slide takes a hand row
instead — g16's processing bed and bell did (2026-09-10).

### 🔒 Density (2026-09-10)

Every event makes a sound, but not every sound survives. Two rules thin the plan, both in
`sfx.json` (`stamp_owns_beat_s`, `max_per_second`) and applied by `sfx-plan.py` before layering:

1. **The stamp owns its beat.** A slam / Impact carries the beat alone: the same graphic's other
   transients within ±0.6 s of it — the scissors of the words around the stamped word, the marker
   stroke of an underline under it, a pop — are dropped. The cut-in and the scene changes
   (`slideIn` / `slideOut`, structure rather than accent) stay; beds and hand entries stay.
2. **Three sounds a second, no more,** across all graphics in a rolling second — where a RUN of one
   sound from one graphic (the scissors of a text animation's words, a wall's machine-gun pops)
   counts once: the pile-up is different sounds from different graphics landing together. The
   lowest-priority source in an over-full second goes (the newcomer on a tie): marker < word <
   rise/slide < pop < slam < cut-in < Impact / character stings. Beds (typing, loading) are textures
   and are not counted; a source with a hand entry in it is never dropped.

Earned on your-job: a 2 s stretch at 1:45 carried seven sounds — a 1.6 s Impact under
three scissors, a pencil scratch, the REC furniture's pop on the cut back and the next line's snip —
and you called it ("there's too many, it's too much going on"). After the rules: the Impact, the
pop, the snip. `sfx-plan.md` lists every drop under *dropped by the density rules*.

**The whoosh roles (2026-09-03):** Simple Whoosh 2 is the primary, on anything that MOVES
across the frame (slides, scene changes, a panel carrying off). Simple Whoosh 1 is the secondary,
on anything that RISES into place. Whoosh Short 2 is the cut-in only. Other whooshes in the
library are for other animation types as they come up, one whoosh per type.

**Paired sounds (a sound that IS an animation's sound, never swapped):** `flash` (`flicker` in an older spec) ↔ Neon Flicker,
red word ↔ Error Buzz, list row ↔ Lighter, slam text ↔ Impact. `assets/sfx/Mac SFX 01–24.wav` are
the individual pieces of the old "Mac & Computer Sound Effects" file (index beside them); Neon
Flicker was 10, Error Buzz was 02; the rest are unassigned until they get used.

**Named calls (in the comp with `data-sfx`, or a hand entry):** an emphasis Impact on an especially
important word (styling alone, serif or italic, does NOT trigger it: scissors is fine on most
emphasis words), a payoff bell, a gunshot, a software scene's processing bed and clicks. They go
in `projects/<job>/hf-graphics/sfx-hand.json` as `{gid, event, at | word, dur?, level_db?, drop?}`;
`drop` removes the automatic events the hand entry replaces (the pops under a gunshot or a bell).

**Read off the timeline, not guessed (your-job, 2026-09-03):** every fixed level and frame
offset in `sfx.json` is the value placed by hand on the reference job. Reading the shipped
timeline back against the plan is how the next batch of hand edits becomes the next batch of rules
(the readback is per lane: [`LANES.md`](../../../LANES.md) § step 6). **Order matters: after the
creator's hand pass, read the diff BEFORE any re-place** — re-placing overwrites the hand edits the
diff exists to capture.

Sounds still unmapped and when to reach for them by hand: `Japanese WOW` on the one reveal of a
piece; `Slap` on a physical bump; `Deep Whoosh 4` + `Deep Whoosh 3` a second later on a big
drop-out-and-launch; `Analogue Camera Snap` when the prop IS a camera; `Paper Turn` when the surface
IS paper (the vox look, not this one).

**Graphics revisions:** run the lane's `--diff` first and fold every approved hand edit upstream (`sfx.json` / `sfx-hand.json`) so a rescore reproduces it. A bare re-run of `sfx-plan.py` REWRITES `sfx-plan.{json,md}` and prints the graphic IDs whose rows changed; when the approved plan carries edits that live nowhere upstream, run `--candidate` instead (parks `sfx-plan.candidate.{json,md}` beside it) and merge only the affected IDs by hand, preserving every unaffected row, level, slice and track. Remove the exact stale affected timeline clips, then apply and verify. After an interruption, read back all SFX before resuming: completion requires zero missing, extra or drifting cues, even when apply adds nothing.

## Definition of done

`sfx-plan.json` written and reviewed as a cut sheet (`sfx-plan.md`), unresolved parser/source warnings resolved with source fixes or explicit hand entries, every row placed on the
lane's SFX tracks at its planned frame with its planned level, **read back with zero missing, extra or drifting cues**, and a frame grab at
a sample of onsets showing the event the sound sits on. Runs AFTER the step-5c defect loop dries
(a graphic retimed later orphans its sound); follow the incremental revision procedure above after any graphic moves.
