---
name: feedback-affan-exports-himself
description: "On Premiere jobs in his own project (ABW8 reaction videos, 2026-10-07): prepare the sequence only, never run exportAsMediaDirect; he exports himself"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4f6ff510-e01c-4ae4-a5c4-8388b194173e
  modified: 2026-10-07T13:40:16.948Z
---

When I edit sequences inside Affan's own Premiere project (first said on the ABW8 reaction videos, Sequences 33-35,
2026-10-07): **prepare the sequence and stop. Never export.** His words: "no don't export … just prepare the videos
ill export myself."

**Why:** he works in Premiere at the same time. `exportAsMediaDirect` pops an encoding window that blocks his session
(he cancelled the first one by accident, then stopped the second). He'd rather export on his own schedule.

**How to apply:**
- The run ends at "placed + verified on the timeline". Proof comes from DOM readback, the PrintWindow grab
  (`lanes/premiere/window-grab.ps1`) and a source-composited preview, never from an export.
- Keep anything that switches his active sequence (QE calls such as `addTracks` or `audio-polish.py`) to one short
  window. Restore his sequence in a `finally`, and say so beforehand.
- Tell him which sequence to export and which preset to use. The vertical preset is
  `lanes/premiere/premiere-templates/vertical-1080x1920-60-h264-cbr24.epr`.

Related: [[feedback-creators-hand-is-not-a-bug]], [[project-onyx-sample-shorts]].
