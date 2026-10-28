---
name: feedback-work-in-silence
description: "Affan 2026-10-20: never make sound on his machine while working; a hidden built-in-browser YouTube tab played audio for 20+ minutes and he was disturbed"
metadata:
  node_type: memory
  type: feedback
  originSessionId: ca11365e-c88c-4196-8400-a7f96c6e5dbd
  modified: 2026-10-19T20:25:15.418Z
---

Work in silence. On 2026-10-20 a hidden tab in the Claude app's built-in browser pane sat on YouTube (F062siQfzps, "Admitted to
Hospital 4 Weeks Out") and played aloud for 20+ minutes while subagents ran. Affan: "can't you just work in silence, why do I have
to be disturbed". A VLC window from another session (a Scott Clary final) was also open.

**Why:** he edits and records on this machine, so any sound from a session interrupts him, and he can't tell which session made it.

**How to apply:**
- Never play audio or video aloud: no ffplay, VLC or `start <file>`, and never Premiere playback for checking.
- Measure with ffmpeg to files or to `-f null` only.
- Never leave a YouTube or other autoplaying page open in the built-in browser or Chrome. For facts use WebSearch/WebFetch, and close any media tab you open at once.
- 2026-10-28, again: opening his Tella share link in the built-in browser autoplayed it with sound ("bruv why can i hear it"). Never open a video page (Tella, Loom, YouTube) in a browser to fetch it: curl the page HTML for the stream URL ([[feedback-walkthrough-videos]]).
- Put the silence rule in every subagent brief.
- If he hears sound, check the built-in browser tabs (`tabs_context`, then pause the media with JS) and the running players first.

Related: [[feedback-usage-budget]].
