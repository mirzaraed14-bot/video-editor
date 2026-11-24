---
name: feedback-live-research-until-recording
description: "After a game's release, a script stays live until Affan records; keep researching, merge only frame-confirmed finds at his \"I'm home\" signal"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4d087bf4-26ea-4e15-8e2c-2613df13c84b
  modified: 2026-11-18T17:32:09.840Z
---

After GTA 6 unlocked (18 Nov 2026), Affan: "new stuff is just going to come out literally every second… we cannot build the script 1 hour earlier than I record something… just keep on searching up to the point when I say that I'm back at my house."

**Why:** in a launch window, a script frozen an hour early is already stale; he wants the most up-to-date version possible when he reads.

**How to apply:**
- Keep a STABLE checked version for him to read.
- Log new finds append-only (source, time, label).
- At his "I'm home" / "ready to record" signal, merge only the frame-confirmed finds that beat an existing line.
- Put "what changed" at the top and run an independent check on the changed lines.
- Verify every on-screen quote on the full-quality video BEFORE he reads; the VO can't be changed later.

Same night, Video A also went **faceless (VO only)**: "that gameplay is just so powerful… my face is going to be a distraction". So a gameplay-led launch explainer needs picture coverage for every second of voice. That was his call for this video, not yet a channel rule.

Related: [[feedback-sequencing-before-edit]], [[project-gta-documentary-channel]], [[feedback-max-effort-every-asset]]

**The miss that made this a hard gate (Affan, 19 Nov 2026, after GTA 29 "Bigfoot Secrets" was fully edited):** one
YouTube search by him found three eggs the script lacked: the Kraken (Robbin Rams), Jason's UFO abduction (Dan Allen
Gaming) and iShowSpeed's Red Hulk (478K in 4 h). Our own watcher had logged all three BEFORE he recorded at 17:03 (UFO 12:06,
Kraken 13:04, Red Hulk clips 15:27); the script research never read the watcher, and its METHOD banned "YouTube requests of
any kind" (the block is on yt-dlp DOWNLOADS, not on the Data API), so it saw only Twitch VODs + articles and could not see a
YouTube-only streamer like Speed. The watcher itself lacked Speed's own upload (only reuploads). "I can't trust you anymore."
- **Gate, every egg/secret script:** right before he records AND again before the edit starts, run fresh YouTube Data API
  searches (date + viewCount order, since launch) plus the watcher DB, cluster by topic, and show him the ranked topic list
  with the script's beats marked in/out. A big topic missing from the script blocks recording until he decides.
- The edit session also checks this before cutting; it never takes a script as final on trust.
- **Guides too (hub, 19 Nov evening, first applied to the "$1M" money route):** the gate covers every guide or list video.
  Cluster the store's titles by METHOD (treasure, robberies, car sales, hideouts, hunting and so on).
  Mark each method IN (proven on a frame), OUT (with a reason, e.g. glitches, a closed casino) or GAP against the stages, and keep the gaps open until they are checked.
  The store's view counts include pre-launch speculation, so label each title pre- or post-launch.
  Regex clusters need a sanity read: "Method" matches "meth".
