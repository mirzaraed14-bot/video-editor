---
name: feedback-voice-first-mix
description: "Affan 2026-10-08 (SAME NIGHT cold open): the voice must be the loudest thing; music is a bed under it, SFX quiet; measure the balance on HIS timeline and preview it with the real levels"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 2af79f46-b1fb-47c3-827d-40eebd325de0
  modified: 2026-10-08T11:17:30.040Z
---

Affan, reviewing the SAME NIGHT cold-open preview (2026-10-08): the SFX were "too damn loud" and the music "completely
overtaking my voice"; "my voice is the most prevalent, the background music acts as background music, the sound effects
shouldn't be so damn freaking loud."

**Why:** his ABW8 voice clips (Enhanced Speech exports) integrate around -28/-29 LUFS while his music clips sit at 0 dB
(-15/-16 LUFS), so on his own timeline the music plays ~12-14 LU OVER the voice; track faders are 0 dB, no track effects.
I had matched SFX to his Seq 24 camera-flash level (-6.6 dBFS) without measuring that voice: 7 dB over his voice peaks.
My preview also used a flat -9 dB music guess instead of his keyframes, so it did not show the real mix.

**How to apply:** measure the voice first (voice-file clips only, the inserted clips are louder); music bed 12-14 LU under
the voice, swelling only in real voice gaps (titles, cards); SFX peaks ~7-8 dB under the voice PEAK (voice peak ~-15.5
dBFS -> hits ~-23, whooshes ~-31, beds ~-34); fewer cues. Previews replay every clip's real Level/keyframes
(`projects/nick-martin-same-night/preview.py`, `level-music.py`). Related: [[feedback-sfx-on-every-graphic]],
[[feedback-whooshes-too-loud]], [[project-abundance-wisdom-longform]].
