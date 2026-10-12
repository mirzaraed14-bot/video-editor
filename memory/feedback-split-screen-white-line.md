---
name: feedback-split-screen-white-line
description: "Affan's split screens always have a white line between the two halves, and the captions sit ON that line from the first frame of the video (the base caption position is the split line)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4f6ff510-e01c-4ae4-a5c4-8388b194173e
  modified: 2026-10-12T00:12:30.933Z
---

Every split screen Affan makes has a **white separator line** between the two halves ("it just feels nice, it feels organized").
The captions sit **on that line**, between the two boxes, never inside the top or bottom person's box. He sets the BASE caption
position for the whole video to the split line, so when a split arrives 5–10 s later the captions are already exactly on it and
never move. Said 2026-10-12 about the batch-1 Sean Ryan-format samples, which had no line ("the one thing I just don't like").

**Why:** the line makes the split read as a designed layout instead of two videos stacked; captions on the seam belong to both
halves and never cover a face.

**How to apply:** in the YouTube "Sean Ryan" Onyx look (`presets/youtube-shorts/onyx-samples-youtube/`) and anywhere he splits the
frame: draw a white line on the seam, and anchor the caption baseline/centre to the seam y for the WHOLE video (full-frame shots
included). This is the split-format form of [[feedback-captions-just-below-lips]]: one constant position, and in a split format that
position is the line. Related: [[project-onyx-sample-shorts]].
