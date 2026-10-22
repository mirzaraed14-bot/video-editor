# Neon window: LESSONS (lesson → change made → file)

## 2026-10-22 · Review 1 (Marvel IG Short v1.1, `projects/_client-scott-clary/marvel-board-vs-rdj-ig/`)
Affan, verbatim: *"too glowy and i prefer you don't do the grayed out style and at 20 sec the sfx sounds goofy same with 38 sec it
needs to sound expensive"* (with a screenshot of the "$525 million" stage type).

1. **The neon is a hint, not a bloom.** Mark Brazil's measured glow (two blurs at full gain) read "too glowy" on our stage type.
   → Glows cut to about a third: stage hero (20 px, 0.32) + (5 px, 0.28); inline hero (10, 0.35) + (3, 0.3); white type (6, 0.22);
   name card (10, 0.35) + (3, 0.3); credit bar 0.5; diagram line 0.45; the strike ramp starts at 0.4, not 0.25. → `ig/build.py`
   (GLOW_*), README § numbers.
2. **No black-and-white.** The DOAC reference was B&W, but he wants the window in COLOUR: dark and neutral-cool like Mark's studio
   (gamma 1.35, contrast 1.08, saturation 0.85, a slight cool tint; stills gamma 1.15 / sat 0.92; the stage a dark slate). The low-key
   relight (room falling to black from the top) stays, a touch lighter (205/255). → `grade()` in `ig/build.py`, README.
   Consequence found in the frame checks: in colour, red type can sit on a red picture (RDJ's armour, the booking shirt). The dark
   halo behind red type goes up to (16 px, 2.2) and the name card's to (14, 2.4); the caption-band scrim on stills to 0.88.
3. **"Expensive" sound = no electric family, no narrow tones.** The two flagged cues were a neon tube stuttering on (20 s) and a
   "dramatic" short riser (38 s). Measured: their tonal prominence above 1 kHz is 38 dB and 25 dB (a narrow tone, the same thing as
   the 2026-10-08 "cricket" swells); every sound he did not flag measures 8-16 dB. Also out by the standing rule (never electric /
   UI): the neon buzz on the credit and the name card and the fluorescent hum on "lights came on". → Replaced with cinematic
   swells INTO reveals and reverberant impacts ON them: a trailer reverse swell peaking into "10 characters", a low riser peaking
   as the red line reaches 2009 + a soft reverberant impact, a clean sub impact on the credit, a reverberant thud on the name card,
   a big stage-light clunk on "lights came on". → `ig/sound.py`; the check is in README § Sound.
   **Rule from now on:** before a sound goes in, measure its tonal prominence above 1 kHz (p90 of max-bin vs its ±40-bin
   neighbourhood over the loud part); > 20 dB = reject.
