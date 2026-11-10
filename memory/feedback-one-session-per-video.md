---
name: feedback-one-session-per-video
description: "Affan 2026-10-23..11-09: he sends a raw recording path to the channel's editor session and wants a NEW session started for that video; the editor session dispatches with a self-contained brief and doesn't edit it itself"
metadata:
  type: feedback
---

When Affan sends a recording path ("X:\Recordings\Afterhours\C1453.MP4 — start a new session for this"), the session
he sends it to is a dispatcher. It does not edit the video itself. It:
1. Probes the file.
2. Settles the channel from the content (the folder is not the channel).
3. Finds the last video of the same kind, the bar this one has to beat by 1 %.
4. Spawns one fresh session per video with a self-contained brief.

He clicks to start it, and the new session runs on its own from there.

**Why:** a fresh context per video keeps each edit clean and cheap. He asked "can i send the recording here and you
start it yourself?" and has used it for every video since. Other sessions run alongside, so a brief must stand
alone.
**How to apply:** the brief carries:
- the raw path + probe;
- his words verbatim;
- the files to read first;
- the bar to beat;
- a stated default for every open question, so the session builds v1 and delivers it, with the questions in the delivery
  note ([[feedback-build-dont-block-on-questions]]);
- his standing constraints.

When he names another session ("ask that particular session"), find it with ListAgents, cite the evidence for the pick,
and let the new session ask it. Log every dispatched job in the channel's job log (Afterhours: `JOBS.md`, see
[[project-gta-documentary-channel]]; AffanWiz: `presets/youtube/affanwiz/JOBS.md`, see [[project-affanwiz-channel]]). Related: [[feedback-long-term-self-improving]], [[feedback-every-video-better-than-last]].
