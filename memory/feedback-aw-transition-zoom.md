---
name: feedback-aw-transition-zoom
description: "Affan 2026-11-04 (Harry review 2) — AW Shorts zoom is a TRANSITION zoom: one push-in per shot, strong start, drift, speeds up into the cut, next shot starts strong again; never a sine ease, never push/pull flip-flops"
metadata:
  node_type: memory
  type: feedback
  originSessionId: ab7670dd-012b-4bf6-896b-d0e0f3d896f6
  modified: 2026-11-04T13:08:18.137Z
---

AW Shorts zoom = his transition zoom: every SHOT CHANGE (new person / camera / overlay) starts a new layer at 1.00 that pushes IN on the README § 3
table (35 % of the move in the first tenth, drift, 18 % in the last tenth), so the speed-up at the end of one shot runs
straight into the strong start of the next. Measured frame by frame on his own finals (ABW6 03, ABW8 34/39, Martin): start
+30..+65 %/s, middle +2..+9 %/s, end +15..+30 %/s, ~80 % push-ins, pull-outs only in runs.

**Same camera = same layer (his review 3, 2026-11-04):** a run of jump cuts on one person/camera keeps ONE zoom layer;
v3 restarted it at each jump cut ("zooming in, then out, then in again on the same shot ... looks weird").

**Why:** Harry v1 had his curve but pulled out on 8 of 23 shots, so the zoom reversed at the cut ("too poppy, too
intense"); v2 swapped to a smooth sine ease and he said "you're missing the plot ... it acts as a transition zoom".
"Eased in / smooth / subtle" in a review means no reversals and no stacked zooms, not a different curve.

**How to apply:** `presets/youtube-shorts/abundance-wisdom/README.md` § 3 (transition-zoom table); check each overlay clip's
own camera move first (`projects/harry-diana-photos/win/his_zoom.py`) and hold a clip that already zooms; gate a render
with `win/zoom_gate.py` (all IN, no flips). Shots under ~1.1 s get +2..+16 % (start ≤ ~45 %/s); shots over ~2.5 s keep the same start/end SPEEDS
(Harry `finish.py long_curve`), the table stretched over 4 s ends too slow. This AW rule does not
override [[feedback-no-same-camera-punch-ins]] / [[feedback-head-steady-across-cuts]] on Onyx / Scott face brands.
Related: [[project-abundance-shorts-automation]].
