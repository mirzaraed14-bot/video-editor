---
name: feedback-absence-claims-full-res
description: "Never script \"it isn't in the footage\" from thumbnails or sampled frames; check at full res frame by frame, else say \"I couldn't find it\""
metadata:
  node_type: memory
  type: feedback
  originSessionId: ad672385-8a50-4e9b-b9c0-9ea2d990c3d2
  modified: 2026-11-18T18:51:46.912Z
---

A script line that says something is NOT shown ("the limbs aren't in the footage", "that part isn't in the clip") must be checked at full resolution, frame by frame (0.25 s steps), before it goes in. "TOO SMALL" or "NOT SEEN" in a thumbnail frame log (384 px tiles, 2.5 s apart) means "can't judge", never "absent". If the check can't be done, the line says "I couldn't find it".

**Why:** 18 Nov 2026, GTA 6 Video A (streams-2026-11-18): the script said IGN's review footage didn't show heavy weapons taking limbs off. Affan watched the review and saw it clearly; he had already recorded the whole voice-over and lost trust in the whole script. The claim came from FRAMELOG.md rows marked TOO SMALL. A 1080p quarter-second check showed it at 2:12:10.5 and 2:12:31.25. He said he can record at most twice.

**How to apply:** before any script ships, grep it for negative claims (isn't, not in, not shown, no footage, neither, haven't seen) and re-verify each at full resolution. Positive claims follow the existing frame-verify rule. Pairs with [[feedback-max-effort-every-asset]] and [[feedback-no-false-completion-line]].
