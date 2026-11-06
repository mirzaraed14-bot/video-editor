---
name: feedback-steady-drift-zoom
description: "Affan 2026-11-04 (Scott client Shorts, Herjavec check): every face-cam shot carries a steady slow push-in ON TOP of the pop zooms, never hold-then-pop; plus his cut notes (drop a host's repeated question word, close pauses over ~0.4 s, check who says an interjection)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: b91b78ad-4977-4979-b54c-80fc96be1991
  modified: 2026-11-04T07:37:13.430Z
---

On the Herjavec check v1 Affan said the face cams of Robert and Scott were "relying on instant zooms ... pop zooms in and then that's it": he wants "some subtle consistent zoom ... constantly zooming in on top of the pop zoom" on every face cam.

**Why:** a face cam that sits still between pops reads static on a phone; the slow push keeps it alive while the pop still marks the emphasis (see [[feedback-face-cam-max-4s]]; it replaces the old "no punch-ins, one keyframed push" caution in [[feedback-no-same-camera-punch-ins]] for the Scott kit).

**How to apply:** in the YouTube kit every A shot gets `drift` (fraction per second, kit/yt_picture.py render_A, default 0); Herjavec used 0.025 (2.5 %/s), pops settle at 1.10 so drift x pop stays <= ~1.2 (hair top >= ~160 px), and ramp-only zoomkeys are dropped (they double up). Same review also: a host's repeated question word is cut ("what was harder ... What was scarier?" -> end on "business?"); after the tight pass list output gaps over 0.2 s and close any over ~0.4 s (an inhale + reverb tail survived the -42 dB pass, 0.73 s); a short interjection ("That's your scariest?") is the HOST's voice, so cyan: check the raw frame for who is on camera. Details in presets/youtube-shorts/onyx-samples-youtube/LESSONS.md (2026-11-04) and scott-clary/ENGINE.md overrides. See [[project-scott-clary-shorts-guarantee]].

## Moved from the MEMORY.md index (2026-11-06)
Affan 2026-11-04 (Scott Herjavec check): every face-cam shot pushes in steadily (`drift` 2.5 %/s) ON TOP of the pop zooms; also drop a host's repeated question word, a host's interjection is cyan (the ~0.4 s pause limit went 11-05, see head steady); 2026-11-05: POP grade + stronger sharpen on every Scott Short (ENGINE § Channel overrides)
