---
name: reference-icarus-track
description: The 'Icarus' soundtrack Affan means = Tony Ann (Ampersand) piano, E:\C shit\Telegram Desktop\...; the subtle ducking-free bed recipe used on Herjavec H1 (music/mix_icarus.py); licence unverified
metadata:
  type: reference
---

"The Icarus soundtrack, it's on this machine" = `E:\C shit\Telegram Desktop\Tony_Ann_–_ICARUS_Official_Visualizer_Piano_Deep_Sad_Thoughtful.m4a` (title tag "Tony Ann – ICARUS (Official Visualizer)", artist tag "Ampersand", 199.8 s, steady ~-13 dBFS RMS, sustained entrance at 2.58 s by `workflows/music-onset.py`). It looks like an artist release, not a library track: **licence not verified**, say so when it goes on a post.

Used 2026-11-06 under both Herjavec H1 Shorts (IG + YT variants, [[project-scott-clary-shorts-guarantee]] context) at his explicit ask, as a SUBTLE bed that stays out of the voice: `projects/_client-scott-clary/herjavec-500m-billion/music/mix_icarus.py <video> <out>` copies the picture, carves the bed (high-pass 110 Hz, low-pass 12 kHz, -3 dB at 800 Hz, -5 dB at 2 kHz), sets ONE flat gain by measurement (voice >= 10 dB over the bed on 90 % of speaking frames, full band and 300-3400 Hz; landed 21 LU under the mix, -19 dB gain), no ducking (it pumps), -1.5 dBFS limiter. Reuse it for any Scott Short he wants scored: change only the video / out paths; the constants are `START_UNDER` and `MIN_RATIO`. Overrides "no music bed" only when he asks (AW Shorts: no bed, see [[feedback-music-is-his-job]]). Not listened to: the balance is measured, not heard.

**His verdict on the first level (2026-11-06): 'music should be 7 dB louder, its too low'.** The measured 21 LU under the mix (voice >= 10 dB over the bed on 90 % of speaking frames) was too faint for him; the shipped level is 14 LU under (gain -12 dB on this track: `mix_icarus.py <video> <out> 14`), where the voice is only 5.7 dB over the bed on the quietest 10 % of speaking frames and the median is 14.7 dB. Next time start at ~14 LU under and say the overlap numbers instead of 21. A re-upload to Drive = overwrite the SAME file name on G: (same file id, the link stays).
