---
name: feedback-head-steady-across-cuts
description: "Affan 2026-10-19 — on same-camera jump cuts the speaker's head must not move up/down or change size; 2026-11-04: Shorts = head TRACKING, no micro-pause jump cuts on his face"
metadata:
  node_type: memory
  type: feedback
  originSessionId: d3d74054-8117-4f44-bcac-6f8a02738576
  modified: 2026-11-05T12:49:26.126Z
---

On a speaker shot cut with jump cuts on ONE camera, the head must stay at the same height and size across every cut. Affan: "whenever
there's a cut and the camera angle stays the same the person moves up and down ... it just doesn't look seamless it just looks jarring
... his face shouldn't be moving up down with the cuts it should still be constant."

**Why:** he edits as a premium editor and catches a 20-40 px jump at a cut; to him it reads as sloppy.

2026-10-20 follow-up: he means real head TRACKING (the AW head lock: the face pinned on every frame, not only matched at cuts), and the
push-ins must match the Shawn Ryan reference (linear ~8-14 %/s). Kit: `head_track=True`, A `fy_out` 0.32 (eye line), `r` per second.

2026-10-20 Tella feedback: but CALM. "Too poppy": no bouncing, no size-following, no cut zooms, no tiny in-and-out pops. Zoom only
on emphasis, eased in and back out (he liked the zoom-out on the last line and a quick zoom-in right after a whip). Splits: no tracking.

**How to apply:** on every Short built from his jump-cut sequences (Scott Clary and Onyx samples), turn on the kit's chained eye head
lock (`head_lock` = joints snapped by `workflows/cut-frames.py`, A shots at z0 1.2) and check eye-line close-ups with a guide line before
delivery. Related: [[feedback-no-same-camera-punch-ins]].

**2026-11-04, AffanWiz Short 2 review 2 ("the camera … snaps with my head … my face will be in the middle"):** the chained lock (the
"How to apply" line above) moves the crop at EVERY pause trim, so a YouTube-tight face shot with micro-cuts reads as a jumping camera.
On code-built Shorts: `head_track` + `head_edge_pin` 12 (not the chained lock), and no pause trim on his face unless it removes >= 0.3 s
(a real pause at a face line's start goes onto the scene change). Gate the background steps, not only the eyes (AffanWiz ENGINE).

**2026-11-05, Scott H1 review 1 ("this tiny silence ... very tightly cut with jump cuts"):** on Scott client Shorts the pause limit is gone: every quiet run >= 0.08 s closes, also on the face. He heard a 0.41 s hole we'd kept to avoid face cuts. Keep the head steady with `head_track` + `head_lock`; don't keep pauses for it. The AffanWiz rule above stays for his own face.

**Long-form Premiere version (CA-010, 2026-11-03, his "Yes, add it"):** static Scale/Position per V1 piece, no keyframes, solved so the eyes
match across every visible same-scale jump cut; one base scale per run between full-frame graphics (≤ ~111 % on 1080p), his cut zooms kept
≥ 1.15× the base, side cards' ear clearance held. Tool + method: `projects/viral-clip-method/work/head_steady.py`, AffanWiz LESSONS
(CA-010 after the hand-off). Build it at the face pass, not after: the brief rule went unapplied in the first CA-010 draft.
