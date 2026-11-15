---
name: feedback-news-shorts-gpu-priority
description: "Affan 2026-11-14: a time-sensitive Short (news goes stale) outranks research jobs on the shared gpu.lock; ask the holder to pause, never kill its process"
metadata:
  node_type: memory
  type: feedback
  originSessionId: dec16bd1-a318-4369-9e17-87b685db610b
  modified: 2026-11-14T17:06:28.437Z
---

Affan, 14 Nov 2026, while the Speed Short's final render waited ~40 min behind a deep-research session's transcription on the shared
`projects/_onyx-batch2-2026-10/.locks/gpu.lock`: "you're on priority bruv, override and tell it to wait for you instead, we need to get
this short out otherwise the news will get stale."

**Why:** a news-driven Short loses its value by the hour; research transcriptions can re-run later at no cost.

**How to apply:**
- When a delivery render for a time-sensitive Short is blocked by a research or batch job on gpu.lock, message the holding session
  (find it from the lock's owner line + `ps -ef`) asking it to stop its GPU job and wait. Then queue your render with a 1 s lock
  poll so it wins the moment the lock frees, and hold the lock through all the remaining GPU steps in one script.
- Do NOT kill another session's process: the permission system blocks it (2026-11-14), and asking worked within ~3 min.
- Tell the paused session when the lock is free again.
- Related: [[feedback-dont-disturb-his-premiere]] (the other shared-machine rule), [[feedback-build-dont-block-on-questions]].
