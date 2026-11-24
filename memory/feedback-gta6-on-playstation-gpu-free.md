---
name: feedback-gta6-on-playstation-gpu-free
description: "Affan 2026-11-18: he plays GTA 6 on PlayStation, not this PC, so GPU and CPU work here is fine while he plays; gpu.lock order and the no-parallel-large-v3 rule still apply"
metadata:
  node_type: memory
  type: feedback
  originSessionId: bbab9b11-e865-49c1-b37c-cc374554528c
  modified: 2026-11-18T13:38:46.022Z
---

Affan, 2026-11-18 (Scott hub, while six Scott sessions were starting before the GTA 6 launch): "You can use the GPU because I'm gonna be playing it on Playstation not gonna be playing on this PC".

**Why:** the hub had restricted the sessions to CPU-only work, assuming his GTA 6 play and recording ran on this PC. It doesn't, so that restriction only slowed the work.

**How to apply:**
- His GTA 6 play sessions are no reason to hold back GPU or CPU work on this PC.
- These rules stay:
  - one job at a time on `projects/_onyx-batch2-2026-10/.locks/gpu.lock`;
  - a time-sensitive GTA news Short first ([[feedback-news-shorts-gpu-priority]]);
  - never two large-v3 ASR jobs at once, and never disturb his Premiere ([[feedback-dont-disturb-his-premiere]]).
- **Same message:** he set a 10-hour deadline for the 19-21 Nov Scott content, about 18:38 on 18 Nov to about 04:30 on 19 Nov (GTA 6 came out about 15 hours later). Brief: `projects/_client-scott-clary/research/picks-19-21-nov/BRIEF.md`.
