---
name: feedback-thumbnail-watch-first
description: "Never build a video's thumbnail blind; get the cut from its edit session, watch it, then use a freeze frame of the actual moment + his reaction to it"
metadata:
  node_type: memory
  type: feedback
  originSessionId: df6628ed-c2e6-4faa-91a1-65de40459f81
  modified: 2026-11-23T23:03:26.972Z
---

Affan, 24 Nov 2026 (GTA 41 NPC reactions): *"communicate with the editor session to really watch the video because I don't
want you to create a thumbnail when you haven't even watched the video ... grab a freeze frame of the interaction as well but
grab a freeze frame of me as well ... don't just blindly make the thumbnail"*.

**Why:** a thumbnail made from the style alone misses what the video is about; the moment that sells it is only known after
watching the cut.

**How to apply:**
- A thumbnail session asks the video's EDIT session (SendMessage, name from the JOBS.md row) for the files it already makes:
  camera↔screen offsets, the clip map, `cuts.json`. Never a render for us. The files appearing are the signal.
- Watch in silence (transcript of kept spans + ffmpeg frame sheets), then pick ONE moment that is in the cut.
- Card = freeze frame of that interaction from the video's own footage; face = his reaction to the same moment
  (camera time = screen time + offset, `make_reaction_thumb.py pick --from/--to`). Quote = a line really in the clip.
- Ready by the edit's delivery (he exports within minutes).
- His face = a LAUGH first (his GTA 41 note, 24 Nov: "pick a frame where im laughing"); shock only if the moment has no laugh.
  Find the peak with a 0.2 s burst, not a 0.5 s sheet. Accent purple #B330FC since that note (spec § 11 #2).
- Spec: `presets/youtube/affan-afterhours/REACTION-THUMBNAILS.md` § 10b. Related: [[feedback-thumbnails-proven-formats]],
  [[feedback-gta-own-style-only]], [[feedback-sourced-stills-must-be-hq]].
