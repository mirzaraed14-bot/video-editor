---
name: feedback-premium-sfx
description: "Affan 2026-10-08: SFX must feel refined, premium, polished (never goofy) and there should be MORE of them; title-card props stay in shadow"
metadata:
  node_type: memory
  type: feedback
  originSessionId: dba6d668-1b25-43d5-a8b2-d5bc637b60ae
  modified: 2026-10-25T03:58:21.269Z
---

Affan on SAME NIGHT cold open v2 (2026-10-08): the magic-shimmer SFX on the Sandow lift was "so goofy… I want this video
to have that refined premium polished feel… I'm all for sound effects, I think there should be MORE sound effects, it's
just that they should feel premium and refined". Also: the FX-12 title's floating props were too prominent; darken them
so the text is the focus. And: "I don't have all day just to correct this intro" — carry lessons through the whole video.

**Why:** a cartoonish or "magic" sound breaks the documentary register instantly; refinement is the brand.

**How to apply:** the palette is cinematic: reverse-cymbal swells INTO reveals, low reverberant thuds ON them, soft airy
whooshes on dissolves/entrances, analog shutters on freezes, low booms/drones under weight. Never: magic/twinkle/shimmer
spells, UI glitches, electric sparks, keyboard typing, cartoon/meme sounds, and anything that TRILLS: the reverse-cymbal swells cym-swell / cym-swell-short and riser-eerie are narrow ~2.5 kHz bursts he heard as "a cricket" (2026-10-08); swells are now chirp-free risers (Epidemic rise-low / rise-air / rise-whoosh). Check a new swell's spectrogram for a narrow pulsing tone before it goes on. Many cues, each quiet under the voice
([[feedback-voice-first-mix]]). Picks + IDs: projects/nick-martin-same-night/audio/sfx/fetch.py.

**A measurable test (2026-10-22, Marvel IG review: "at 20 sec the sfx sounds goofy, same with 38 sec, it needs to sound
expensive"):** the two flagged sounds (a neon tube flickering on, a short "dramatic" riser) measured 38 and 25 dB tonal prominence
above 1 kHz (max FFT bin vs its ±40-bin neighbourhood, p90 over the loud part); every accepted cinematic sound measured 8-19 dB.
Reject anything > 20 dB before it goes in, and keep the electric family (neon buzz, fluorescent hum) out entirely. Recipe:
presets/instagram/neon-window/LESSONS.md.

**PHONE BAND (Affan 2026-10-25, Chris Do IG: "the sound effects need to sound expensive and premium"):** the cinematic hits in
v1 had almost nothing in 300 Hz-6 kHz (25-41 dB down), so on a phone they vanished and only the taps and foley (marker, pencil, card
slide) came through: that is what read cheap. Fix: no taps/foley in a premium Short; high-pass every hit (70-150 Hz) before
normalising so its crack sets its level, and carry the weight with one sub-boom layer under the big moments. Check each cue ALONE in the
phone band (`projects/_client-scott-clary/chris-do-sneaker-pricing/ig/cue_check.py`: WEAK below -20 dB vs the voice), re-run the tonal
test on the final slices, place hits by their attack (not their peak), pitch-step repeats.

**VARIETY (Affan 2026-10-21, THE LAST SHOW redo, rated the SFX "2 out of 10"):** "this Vegas whoosh air sound effect so many times…
annoying… way more variety… not just spam [one] sound effect again and again". The redo had 293 cues sliced from SAME NIGHT's handful
of samples: whoosh-air (= rise-whoosh.wav) 71×, rise-air 47×, thud-low 37×. So: never build a film's SFX layer from a previous job's
small kit. Source a fresh, wide set per job from Epidemic, with several takes per action class, and rotate them so no sample repeats back
to back and none dominates. Each sound matches what its animation does. Related:
[[feedback-sfx-on-every-graphic]], [[feedback-cinematic-pacing-longform]].
