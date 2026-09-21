---
name: feedback-creators-hand-is-not-a-bug
description: "On a timeline the creator has hand-edited, a value that deviates from the tool's default is a decision — never \"fix\" it silently"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e1b9cd8c-a044-4294-9e79-318eb202a8a0
  modified: 2026-09-17T00:20:52.227Z
---

The creator edits their own timelines by hand alongside me ("it's not all automated right now i'm
still doing my work"). On any timeline they have touched, **a value that deviates from a tool's
default is a DECISION until proven otherwise.** Do not "fix" it, do not normalise it — ask.

The tell: **a bug is not uniform.** If the same non-default value appears on every clip of a class,
a human put it there.

**Why:** on the Hot Coffee cut every Higgsfield reenactment clip sat at Motion > Scale 96 instead of
100, so the track below showed a few px around all four edges. I measured the edge columns, decided
`setScaleToFrameSize()` was fitting instead of filling, and scaled 59 clips up to 101.5. It was their
look — a colour mat with film grain under the overlay track, reading as a dark red drop shadow.
*"the edge bleed was an esthetic that I gave to every single Higgs field overlay ... I spend so much
time doing that ... everything looks bad."* Hours of their work, deleted by a correctness argument
that was never wrong about the geometry and completely wrong about the intent.

**How to apply:**
- Before changing a look on their timeline, ask: is this value the same everywhere, and is their hand
  anywhere near it? If yes, ask before touching it.
- **Export an FCP XML before ANY batch operation on clip properties.** It is the only way to read
  per-clip Motion scale and colour labels, and therefore the only real undo across a session — a
  guess at "what it was" is not a restore. A clip with no Basic Motion filter is at the default 100,
  and that is a value to restore too, not a blank to fill.
- Restore exactly what was there per clip; never flatten a class to one number.

See [[project-gta-documentary-channel]] and [[feedback-long-term-self-improving]]. The channel-level
version is locked in `presets/youtube/affan-afterhours/README.md` § 1 (THE OVERLAY FRAME) and
`LESSONS.md`.
