---
name: feedback-aw-subscribe-cta
description: "Affan 2026-11-03 — every Abundance Wisdom Short carries a subscribe CTA in the AW look: 2 subtle mid prompts in a ~40 s Short (540K → 1M play button); the end screen is OFF since 2026-11-04 ('horrendous and cheap'); kit = presets/youtube-shorts/abundance-wisdom/cta/"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 0ac70c57-b1cb-4865-b958-7d9d45bd812d
  modified: 2026-11-05T13:09:45.600Z
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
- (PAUSED since 2026-11-04, see below.) The end screen (`aw-cta-end`, 4.0 s, black, "Road to 1M") went after the last line. It shows his gold plaque, the count
  rolling to his number and the tap feeding the plaque. The count is baked in: re-render with `--subs <N>` before a Short ships.
- One soft swish per entrance, the tap silent, cue peak ~15–19 dB under the voice.
- Where everything lives: kit `presets/youtube-shorts/abundance-wisdom/cta/cta.py`, renders in
  `E:\Shorts\Abudance Wisdom Shorts Exports\CTA\`, rules in the AW README § 12.
- Review v1 (2026-11-03): the mid was "nice and subtle" but "slapped on", so it got his red Deep Glow plus a click flare.
  The first end screen (text + button) he "didn't like at all": research the web first, then build ONE scene with phases,
  a non-type visual and a camera move. v2 preview was sent the same day. Harry Diana is the first Short to ship with it.
- 2026-11-04 (Owen Hart Wife): "do add the call to action at the end". The end screen goes on even when a locked brief
  says "hard cut, no end card": hard cut on the last word straight into its black, and the runtime limit counts to the
  last word.
- **Later on 2026-11-04 (Harry Diana review): END SCREEN OFF on every Short, which supersedes the Owen line above.** The
  Road to 1M end screen "looks absolutely horrendous and cheap ... skip this until you come up with a better one, but I
  don't need a better one for this video ... fade out this video". The mid prompts stay; he placed them himself at 21 s and
  35 s of 41.6 s. Shorts end as their brief says (Harry: a 0.6 s picture fade). Two end concepts are now rejected. A third
  is built only when he asks, and approved from a real-speed clip before it touches a Short.
- **2026-11-05 (La Toya v2): "Keep it under the bar".** On a Short whose bottom bar sits at y1470, the pill stays under the bar (solid y1544-1620, `mid_dy` 190) rather than moving up onto her chin. A few frames of contact with the growing bar at a shot's end, and the cursor dipping below y1620, are accepted. README § 12.

Related: [[feedback-labels-at-bottom]], [[project-abundance-shorts-automation]], [[feedback-premium-sfx]].
