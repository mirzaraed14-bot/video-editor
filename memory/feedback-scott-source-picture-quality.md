---
name: feedback-scott-source-picture-quality
description: "Scott Shorts built from a soft Zoom/webcam source were rejected (\"how tf can we upload this\"): a pick needs a source-QUALITY check at full size, and a 16:9 Zoom frame is never centre-cropped to 9:16 and sharpened"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 792a7c45-43d8-4ff6-abf8-08b96a0e1730
  modified: 2026-11-20T19:58:06.474Z
---

Karnazes "He Ran 30 Miles Drunk" (YT-2, 20-21 Nov 2026) was built and delivered, then Affan rejected it: "you didn't quality check this video, this is a zoom call and a shitty connection, how tf can we upload this."

**Why:** the sequence gate J only proved real video exists (the HLS has renditions, frames seen). Nobody judged whether the picture was good enough to post. The build then cropped a 608 px sliver out of a soft 1080p Zoom frame and stretched it to 1080 (1.78x up), added the POP grade and stronger sharpen (a hard halo, waxy skin), and the button (the second window, rows 12-13) was smeared and blocky. The only clean frame in the whole Short was a pants-mime shot where the full 16:9 frame was scaled DOWN. Pick and delivery notes called it a "look to judge" when it was a quality defect.

**How to apply:**
- A pick on a webcam, Zoom or remote source gets a **source-quality gate at pick stage**: look at a 100% frame from EACH span (the second span is often worse), and say "Zoom quality" in the sequence if it is one. Score a soft source against the pick. A funny story on bad picture does not clear the bar; say that first.
- **Never centre-crop a Zoom 16:9 frame to 9:16 and sharpen it.** For soft remote sources use the full 16:9 frame as a float window, scaled DOWN, over a blurred fill, with a light grade. Never the POP grade or stronger sharpen on a soft source.
- **QA means viewing full-size frames from every section, ending included**, not just the hook frame. A hook frame at 1 s is the best-looking part. Report picture softness as a defect, never as "taste".
- Related: [[feedback-first-party-hq-bits]], [[feedback-sourced-stills-must-be-hq]], [[feedback-aw-overlays-recognisable-crisp]].
