---
name: feedback-no-stray-frames-at-overlays
description: "Affan 2026-10-09: no single stray frame of face at any overlay edge — every overlay lands on a V1 cut or butts the next overlay"
metadata:
  type: feedback
---

Affan's review of GTA video 22 (Tella walkthrough, 2026-10-09): "for literally one millisecond you can see my face even
though the viewer is not supposed to see my face… I need you to fix this in all of the overlays." The cause was mine: the
plan ended back-to-back graphics 0.02 s early (one frame at 59.94) and never snapped graphic edges onto V1 cuts.

**Why:** a one-frame flash of the face (often an un-zoomed shot between a zoom and a graphic) reads as a glitch.

**How to apply:** every graphic edge within a few frames of a V1 cut lands ON the cut; neighbouring graphics butt with
gap 0 (never `next.start - 0.02`); gate before placing: no gap < 0.8 s between graphics, no face sliver < 0.3 s at a
graphic edge, re-checked on the timeline readback. If an insert's media is short, his fill is a 98–99 % slow-mo. And
when he has re-cut the draft himself, read his timeline first and rebuild from it ([[feedback-creators-hand-is-not-a-bug]]).
Related: [[project-gta-documentary-channel]].
