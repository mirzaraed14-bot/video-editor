---
name: feedback-first-party-hq-bits
description: "Affan 2026-11-07: a Short's beat needs high video and audio quality from a first-party voice (family, the subject, an on-camera eyewitness); bad far-away audio is out however strong the words; new bits are shown on the timeline for his OK before any build"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 295c30a8-6088-41ae-9463-ba352f8a763c
  modified: 2026-11-08T16:48:26.737Z
---

Tella 1 on What Michael Jackson Showed His Mother: he cut a fire inspector's account (640x480, audio over a still) and Tito's podcast audio: "the audio is very bad... we will have to compensate with video overlays". He wants first-party sources (Katherine, Joe, brothers, sisters, the subject himself is "amazing", the kids, anyone first-hand) at high video quality.

**Why:** a rare line loses to a clear one; weak audio forces overlays to carry the beat.

**2026-11-08, stricter:** he rejected the built "Why MJ Gave Away $5 Million" Short (1984 VHS news, press-conference and brothers footage, Getty and uploader watermarks): "the footage is too bad... the audio is horrendous". New parameter for every idea: **check each source's video and audio quality during research, before scripting.** Every beat needs real **≥720p** footage (not a VHS rip upscaled; check with ffprobe, or a `yt-dlp -F` format list plus a frame look) and clean, close audio. A story whose key beats only exist in 80s/90s SD archive fails, however proven the demand. Log the resolution per beat in the script table.

**How to apply:** when picking beats, reject low-quality audio even for strong words. Keyword-scan the local long docs first (`projects/mj-showed-his-mother/win/scan_all.py`, small.en, minutes for 26 files): Take Two gave Karen Faye and real hospital video that YouTube search missed. When he asks for new bits, put them on the timeline as a v2 sequence beside his cut and STOP for his approval prompt before building. Related: [[feedback-sequencing-before-edit]], [[feedback-walkthrough-videos]].
