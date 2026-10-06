---
name: feedback-captions-just-below-lips
description: "Onyx sample Shorts (and talking-head Shorts generally) — captions sit JUST BELOW the speaker's lips, never on them, never far down; the eye shouldn't travel between mouth and text"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4f6ff510-e01c-4ae4-a5c4-8388b194173e
  modified: 2026-10-06T16:13:36.438Z
---

Captions sit conveniently just below the speaker's lips: not on top of the mouth, and not a big distance down the frame.
Affan, 2026-10-06, after watching batch 1 (Rob Dial, Chris Do, Rich Roll, Harbinger): "the distance between the captions and the lips
needs to be shorter… I was constantly moving my eyes up and down… which creates irritation for the viewer."

**Why:** the viewer reads the face and the words together; a fixed caption band far below the mouth makes the eyes ping-pong.

**How to apply:** place captions PER SHOT from the measured mouth position (face landmarks through the shot's crop math): caption top a
small gap under the lower lip, clamped to the safe zone and pushed clear of any card on screen; B-roll / full-screen-graphic shots use the
video's median face-shot position so the text doesn't jump. A fixed `captions.y` is the fallback only. A chunk on screen across a cut must
take each shot's own height ON the cut frame (QA 2026-10-06: otherwise it sits on the other shot's mouth). Kit: `onyx-samples/kit/ig_capy.py`.
Related: [[project-onyx-sample-shorts]].
