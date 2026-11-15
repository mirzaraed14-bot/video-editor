---
name: feedback-dont-disturb-his-premiere
description: "Affan 2026-11-14: never move his playhead or switch his timeline while he edits in the same Premiere project; offline frames (offgrab.py) instead of window grabs, quietgate.py + QUIET-MODE gate writes on his idle time, no parallel large-v3 ASR (it crashed his Premiere)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 81bec4af-1855-4005-9296-3fd26dffaf18
  modified: 2026-11-14T12:58:53.770Z
---

When Affan edits in the same Premiere project as a Claude batch, nothing may move his playhead or switch his active sequence.

- **QC frames:** come from `projects/_onyx-batch9-2026-11/reactions/offgrab.py`. It rebuilds frames offline from a by-name `dump.py` readback and is proven frame-exact on 1,076 real frames. Window grabs are not used.
- **Gating:** while `lanes/premiere/QUIET-MODE` exists, `lanes/premiere/quietgate.py` (called from `pp.es`) holds every write until he is idle. `lanes/premiere/PREMIERE-PAUSE` is the emergency stop for all bridge calls.
- **Memory:** never run several large-v3 ASR jobs at once. Use medium.en, one at a time via `.asr-lock`, with at least 8 GB of RAM free.
- **Tool locations:** details in `lanes/premiere/lab-notes.md` § 2026-11-14 QUIET MODE.

**Why:** "you are constantly moving the playhead ... do it in your own sequence and let me edit in my own sequence don't disturb me". Later the same day three parallel large-v3 runs (~8 GB each) starved RAM and his Premiere hung and closed ("my premiere is stuck").

**How to apply:**
- Ask whether he is editing before a Premiere-heavy batch. While he is, create QUIET-MODE; delete it when he says he is not editing (as on 2026-11-14 evening).
- Big rebuilds (re-lays) hold Premiere for minutes, so ask when they may run.

Related: [[feedback-affan-exports-himself]], [[feedback-work-in-silence]].
