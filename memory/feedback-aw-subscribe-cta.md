---
name: feedback-aw-subscribe-cta
description: "Affan 2026-11-03 — every Abundance Wisdom Short carries a subscribe CTA in the AW look: 2 subtle mid prompts in a ~40 s Short + a subscribe end screen (540K → 1M play button); kit = presets/youtube-shorts/abundance-wisdom/cta/"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 0ac70c57-b1cb-4865-b958-7d9d45bd812d
  modified: 2026-11-03T12:12:33.581Z
---

Affan, 2026-11-03: "a universal thing that we are going to be doing in our shorts from now on ... a small call to action to
subscribe because I'm at 540,000 subscribers ... I really want to reach one million ... a subtle CTA that plays along the
video here and there, like if it's a 40 second video two times is fine ... and at the end ... a blank screen ... this cool
animation of telling people to subscribe if they want more ... in our own aesthetic so it doesn't stand out like a sore thumb".

**Why:** the 1M play button matters for his career. A stock YouTube sticker would break the AW look, so the CTA has to read
as part of the video.

**How to apply:** on every AW Short (never Onyx, Scott Clary or other client Shorts):
- Two mid prompts (`aw-cta-mid`, 2.8 s, label band y 1392), placed ~35–45 % and ~70–80 % in. Keep them out of the hook,
  off labels and off the payoff line.
- The end screen (`aw-cta-end`, 4.0 s, black, "Road to 1M") goes after the last line. It shows his gold plaque, the count
  rolling to his number and the tap feeding the plaque. The count is baked in: re-render with `--subs <N>` before a Short ships.
- One soft swish per entrance, the tap silent, cue peak ~15–19 dB under the voice.
- Where everything lives: kit `presets/youtube-shorts/abundance-wisdom/cta/cta.py`, renders in
  `E:\Shorts\Abudance Wisdom Shorts Exports\CTA\`, rules in the AW README § 12.
- Review v1 (2026-11-03): the mid was "nice and subtle" but "slapped on", so it got his red Deep Glow plus a click flare.
  The first end screen (text + button) he "didn't like at all": research the web first, then build ONE scene with phases,
  a non-type visual and a camera move. v2 preview was sent the same day. Harry Diana is the first Short to ship with it.

Related: [[feedback-labels-at-bottom]], [[project-abundance-shorts-automation]], [[feedback-premium-sfx]].
