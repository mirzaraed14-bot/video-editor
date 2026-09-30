---
name: feedback-walkthrough-videos
description: "The user plans to record a Tella/Loom walkthrough per video explaining their vision for the edit; ingest it as transcript + sampled frames and write it to the job's BRIEF.md"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e83a5461-9372-426b-acd3-91eb82cfebd1
  modified: 2026-09-29T21:30:05.586Z
---

From 2026-09-22 the user intends to record a **Tella or Loom walkthrough for each video**, talking through what they
want from that edit, instead of typing the brief. Treat it as the primary brief for the job.

**Why:** they direct rather than execute, they dictate by voice, and a screen recording carries what text cannot —
they scrub their own timeline and point at things. Half of a spoken note is deictic ("this bit", "here", "that
one"), and those only resolve against the picture.

**How to apply:** ingest it, never just skim it.
1. **Audio** → `transcribe.sh` on a job folder gives a word-timed transcript of everything said.
2. **Picture** → sample frames with ffmpeg at each moment they point at something, and actually look at them. Read
   the timecode off their Premiere program monitor / timeline so "this bit here" becomes a clip and a time.
3. **Write it down** → the resolved brief goes in `projects/<job>/BRIEF.md`, and anything that will recur graduates
   into the channel preset's `PLAYBOOK.md` or `LESSONS.md`. Nothing stays only in chat. See
   [[feedback-long-term-self-improving]].

**Getting the file:** yt-dlp has a native `loom` extractor, so a Loom share link is enough. **Tella (solved
2026-09-30):** yt-dlp's generic extractor only gets the 5 s `thumb.mp4` preview. Open the share link in the
built-in browser, press play, read `performance.getEntriesByType('resource')` for the signed
`prod-stream.tella.tv/media/manifest.m3u8?...` URL, then `ffmpeg -i "<that url>" -map 0:v:0 -map 0:a:0? -c copy
guide.mp4` (~1.5 min for 13 min). The creator mutes the screen audio on purpose, so the audio is their direction
only; their timeline timecode (top-left of the timeline panel), read at each narration segment, maps every "here"
to a clip. Overlay slots are marked by dragging the face clips up to V2. Caveat to state honestly: frames are sampled, not watched as motion, so a note
about how a MOVE feels (easing, how a transition reads) needs to be said in words as well as shown.
