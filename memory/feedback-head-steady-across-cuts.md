---
name: feedback-head-steady-across-cuts
description: Affan 2026-10-19 — on same-camera jump cuts the speaker's head must not move up/down or change size; premium bar, he notices
metadata:
  type: feedback
---

On a speaker shot cut with jump cuts on ONE camera, the head must stay at the same height and size across every cut. Affan: "whenever
there's a cut and the camera angle stays the same the person moves up and down ... it just doesn't look seamless it just looks jarring
... his face shouldn't be moving up down with the cuts it should still be constant."

**Why:** he edits as a premium editor and catches a 20-40 px jump at a cut; to him it reads as sloppy.

2026-10-20 follow-up: he means real head TRACKING (the AW head lock: the face pinned on every frame, not only matched at cuts), and the
push-ins must match the Shawn Ryan reference (linear ~8-14 %/s). Kit: `head_track=True`, A `fy_out` 0.32 (eye line), `r` per second.

**How to apply:** on every Short built from his jump-cut sequences (Scott Clary and Onyx samples), turn on the kit's chained eye head
lock (`head_lock` = joints snapped by `workflows/cut-frames.py`, A shots at z0 1.2) and check eye-line close-ups with a guide line before
delivery. Related: [[feedback-no-same-camera-punch-ins]].
