---
name: feedback-premium-sfx
description: "Affan 2026-10-08: SFX must feel refined, premium, polished (never goofy) and there should be MORE of them; title-card props stay in shadow"
metadata:
  node_type: memory
  type: feedback
  originSessionId: dba6d668-1b25-43d5-a8b2-d5bc637b60ae
  modified: 2026-10-28T01:50:46.396Z
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

**FIT (Affan 2026-10-26, Scott x Morgan claw v2: "don't sound premium ... in some places the sound effect doesn't even fit the
motion graphic"):** v2 used the YT kit's stock cues (data blips on an LCD menu, glass ticks on a $100 landing, glass pops on a card,
a whoosh on every cut back to the face). Never use the kit's auto cues on a client Short: size each sound to its motion (whip = short
whoosh crested on the cut; a value landing = a hit on its first VISIBLE frame; a wind-up = a riser ending on the landing; cuts back to
the face silent), levels near the Chris Do IG mix. Template: projects/_client-scott-clary/morgan-claw-machine/yt/sound.py + cue_check.py.

**UNDER HIS MUSIC (Affan 2026-10-26, Morgan claw after v3):** "remove the sfx except for the transition ones, once I put music it's
like too much". On a Short he scores himself, the card hits and swells crowd his bed: v4 kept only the whip-cut whooshes. REPEATED
2026-10-28 (Patrón: "crisp premium expensive but subtle ... I'm gonna put a music bed"), so it is now the DEFAULT for Shorts he scores
himself: transition swishes only, short (loud part <= 0.35 s), 19-23 dB under his voice, HP 150 Hz, nothing whose body sits above 6 kHz.
Template: projects/_client-scott-clary/patron-20000-cases/yt/sound.py.

**VARIETY (Affan 2026-10-21, THE LAST SHOW redo, rated the SFX "2 out of 10"):** "this Vegas whoosh air sound effect so many times…
annoying… way more variety… not just spam [one] sound effect again and again". The redo had 293 cues sliced from SAME NIGHT's handful
of samples: whoosh-air (= rise-whoosh.wav) 71×, rise-air 47×, thud-low 37×. So: never build a film's SFX layer from a previous job's
small kit. Source a fresh, wide set per job from Epidemic, with several takes per action class, and rotate them so no sample repeats back
to back and none dominates. Each sound matches what its animation does. Related:
[[feedback-sfx-on-every-graphic]], [[feedback-cinematic-pacing-longform]].

**SUBTLE (Affan 2026-10-27, batch-5 Onyx reactions + reel: "the sound effects sound very very cheap … they don't sound expensive,
premium, refined, subtle … some places they're loud"):** the layers were sliced from earlier jobs' kits (Chris Do / War Dogs / MG:
trailer toms, taiko, heavy thuds, deep whooshes), 38-47 cues per video, hits 5 dB under his voice peak. So: a fresh Epidemic set per
job, soft and airy (gentle swishes, light risers, high-passed soft impacts; still no taps/foley per PHONE BAND), no trailer drums or big booms on a talking reaction,
and every cue clearly under the voice (hits ≥ 8 dB under the voice peak, whooshes far lower); fewer big moments, none louder than the
rest. Lesson: presets/youtube-shorts/onyx-samples/LESSONS.md § 2026-10-27 review.

**SUPERHERO (Affan 2026-10-28, "Shorts cooked" reel, THIRD strike on Onyx SFX: "they sound like they're from a superhero movie ...
each motion graphic of mine has some super powers ... refined premium subtle ... expensive ... belong to the motion graphic"):** lowering
levels (v2) did not fix it because the takes were still Scifi Impact / Ethereal Fantasy Ghost / Fire Reversed / Eerie Metallic / risers /
stingers. For Onyx reels + reactions the palette is ONE family: the soft airy / cloth swishes of the Patrón Short he approved that day
(patron-20000-cases/yt/sound.py), in three sizes (pill/chip = short cloth swish, title/card = light airy, bar/grid/split cut = longer
airy), ONE cue per graphic entrance, crest on the move's fastest frame, silent on text swaps / colour changes / stamps / cuts to the face;
peak 15 dB under the local voice peak and >= 19 LU under. Reject takes by title first (Scifi, Fantasy, Magic, Cinematic, Trailer, Impact,
Riser, Stinger, Hit, Boom, Eerie, Metallic, Fire, Ghost, Ethereal), then measure vs the Patrón slices (tonal p90 <= ~13). Recipe:
projects/shorts-cooked-not-your-fault/work/sfx3_build.py; lesson in onyx-samples LESSONS § 2026-10-28.

**2026-10-28 (AW long-form, BOTH VERSIONS review 2):** "the scrubbing, the writing, the paper sound effects are just a little bit loud…
three, four decibels": paper / pencil / marker / page-turn textures sit ~3.5 dB under the review-1 caps (≈ −22.5 dB vs the voice).
Apply it relative to the live level so his own hand-set levels stay. Quieter beats the phone-band audibility target (AW LESSONS 44).
