---
name: feedback-subtle-transitions
description: "Affan 2026-11-14 Skool VSL: no push-through / zoom-through transitions between graphics (\"going in and popping out\"); soft dissolves through the plate; no punch-in push at a CTA, head centred and fully in frame"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 9962ea41-ec9b-41f6-bf73-3dd41869f47c
  modified: 2026-11-13T21:10:08.592Z
---

His Tella review of the Skool VSL (2026-11-14):
- **The 12-frame push-throughs between three consecutive full-screens:** "too dynamic, it's going in and then it's popping out… I was going for a more subtle look… search up other transition effects, something which feels more expensive".
  - Replaced with a soft dissolve through the shared plate. Outgoing content fades over 18 frames (scale 1 → .985). Incoming content fades in over 0.45 s (scale 1.02 → 1, expo.out). The plate scale is continuous across the cut.
- **The CTA push-in (×1.10 on top of a 1.21 head-lock base):** "why am I going down and then zooming in… my face should be in the middle… my head is going up out of the frame".

**Why:** dynamic zooms read cheap on a premium sales video. A zoom that crops his head breaks the face frame.

**How to apply:**
- Between full-screens, use a dissolve or dip through the plate. Never a scale-3/5/6 push-through. Pick alternatives from `research/effects-catalog/CATALOG.md` (FX-37 Ghost Dissolve family).
- On face spans, no fast emphasis push where he gives an instruction (CTA).
- Test the head on the TRANSFORMED frame: the measured hair top keeps headroom (`projects/skool-vsl-2026-11/work/plan/gen_v1.py` head test + `hair_top.py`).
- Do not size-match jump cuts by interocular distance: it swings with head yaw, about 9 % scatter.

Related: [[feedback-no-same-camera-punch-ins]], [[feedback-head-steady-across-cuts]], [[feedback-natural-speech-whole-lines]].
