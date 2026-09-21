---
name: feedback-editable-captions-in-premiere
description: "@affanwizu captions must be EDITABLE inside Premiere (not a rendered .mov layer), so the creator fixes spellings themselves"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 123ecc4f-c34e-484c-84b1-6417b858da1c
  modified: 2026-09-19T02:41:41.843Z
---

Deliver @affanwizu captions as something the creator can edit in Premiere, never a rendered caption .mov (said 2026-09-19).

**Why:** re-rendering a layer for every spelling fix is slow; they'd rather retype a word themselves. They also want each reel done in ≤ 15 min.

**How to apply:** `build.py <job> --srt --dur <sequence end>` → an .srt caption track they drag onto the sequence at 00:00 and style with the saved "affanwizu yellow" Track Style (settings in `presets/instagram/affanwizu/deep-talks-style.md` § Premiere caption track). On this machine, scripted import into Premiere (importFiles, importMGT, changeMediaPath) was broken on 2026-09-18/19, so a .mogrt route couldn't be automated. Retry importMGT if that gets fixed. Related: [[project-urdu-instagram-captions]], [[feedback-long-term-self-improving]].
