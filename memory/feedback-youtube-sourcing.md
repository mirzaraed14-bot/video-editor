---
name: feedback-youtube-sourcing
description: Claude fetches YouTube b-roll itself (yt-dlp is installed and the repo ships it for this); the user does not have to download and bin clips first
metadata: 
  node_type: memory
  type: feedback
  originSessionId: e83a5461-9372-426b-acd3-91eb82cfebd1
  modified: 2026-09-22T07:40:45.066Z
---

Claude downloads the YouTube source clips for a job itself and imports them straight into the Premiere bin. The
user does not have to fetch anything first. Asked on 2026-09-22 while the GTA 6 PC-release job was waiting on
game-footage overlays. This **supersedes** the older "the user downloads, Claude works from the files" split
recorded in [[project-abundance-shorts-automation]] for that channel.

**Why:** `yt-dlp` is installed on this machine and `check-setup.sh` lists it as a project tool for "downloading
reference clips + YouTube research"; `lanes/premiere/lab-notes.md` already carries the format flag for downloads
headed into Premiere. The system was built expecting this. The material in question is official publisher footage
(Rockstar trailers, the Extended Look, old-GTA gameplay) used as short clips under commentary, which is the normal
b-roll diet of this channel per `presets/youtube/affan-afterhours-facecam/`. Downloading is contrary to YouTube's
terms of service, which is the user's call about their own channel, not a reason to hand the task back.

**How to apply:** fetch into `projects/<job>/broll/`, then import into the job's bin the same way the synced master
went in. Premiere cannot read AV1, so always force H.264:
`-f "bv*[vcodec^=avc1]+ba[ext=m4a]/b[vcodec^=avc1]"`. Name what is being pulled before pulling it, so the user can
redirect. When a source is another creator's own video (a podcast, a reaction, a video essay) rather than a
publisher's, say so and keep the clip short — that is a flag, never a refusal. See
[[project-gta-documentary-channel]].
