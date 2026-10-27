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

## 2026-10-23 · Review 1 of the War Dogs IG Short (`projects/_client-scott-clary/war-dogs-fake-office/`, "it's good but…")
Affan: no head tracking at all in this video; no captions for the duration the hook text is up ("the first 3-4 seconds look so
cluttered: the captions, the text box, the podcast tag"); the sound under the counter climbing to $300,000,000 "should be something
else, a lot more subtle, minimalistic… a weird sound effect… definitely lower in volume".

1. **No head tracking.** The eye-locked crop (per take, smoothed) is out: ONE fixed frame for the whole video, anchored on his median
   eye position (846, 341 in 1080p), the approved pushes zooming toward that fixed point. → `ig/build.py` (EX0/EY0, `cam_frame`).
   This overrides the 2026-10-19 head-steady-across-cuts lock for this look until he says otherwise.
2. **The hook card owns the screen.** While the hook text (and the name tag) is up, there are NO captions; they start on the first
   word after it ("War Dogs" at 3.3 s). → BLOCKS in `ig/build.py`. Apply from the start next time: a hook card = a caption pause.
3. **A climbing number gets a breath, not a riser.** The clean "build-up" riser under the counter read as weird and loud. → a slow,
   broadband dark airy swell (`wd-swell-dark-airy.wav`, Epidemic 0ea4c198; 14.8 / 10.3 dB tonal) at 15 dB under the voice peak
   (~10 dB lower than the riser), its slice ending on the swell's peak as the number lands; the landing boom unchanged. → `ig/sound.py`.
Patched, not re-rendered: `build.py --patch` re-rendered only the cam shots and the hook (0-200, 560-700, 930-1005, 1540-1610,
2545-2670 at 60 fps), the rest of the picture passed through.
- 2026-10-24 (Brad Lea Ferrari IG, in-studio multi-camera, 30p source -> 60 fps Chronos): (1) a FIXED frame per take, placed so the head doesn't jump at joints (<= 9 px drift), beats head tracking on studio shoots; (2) push-ins (10-15 % within ~0.9 s) anchor on the MOUTH so the lips stay above the caption spot; (3) hold the zoom at 1.00 while type sits above the head (it touched the hair); (4) watch the speaker leaning down at a close-up's first cut (lips dropped under the captions: start the shot half a line later); (5) Epidemic files rejected by the narrow-tone check: phone-buzz, riser-dramatic, riser-reverse-layers; a small reused set repeats (pen stroke 5x, low boom 4x): source a wider set per job.

## 2026-10-25 · Chris Do "$150 sneaker" IG Short (`projects/_client-scott-clary/chris-do-sneaker-pricing/ig/`, Affan: "make the style and everything 1% better this time")
What it did better than the War Dogs IG (the BRIEF's § IG variant has the full list):
1. **The hook is Mark's stage shot**: the whole webcam frame small at the window bottom (`hookstage_frame`), the promise in the dark
   band above, the mono credit beside his head; no captions under it (they start on the first word after, 2.65 s).
2. **Mouth-anchored fixed frame per take**: every cam shot puts his median mouth at window y 590 and the pushes zoom ON it, so the
   caption top keeps a measured gap under the lips at every zoom (`lips_check()` asserts >= 20 px; tightest 43 px).
3. **One object that returns and evolves** (Mark's floating artifact cards, Brad's receipt): the sneaker lit with its price -> inside a
   floating sponsored-ad card -> beside its $150 fake -> lit again on "a different kind of buyer". The marker ring + FAKE are drawn
   strokes, never a font or a stamp.
4. **A number that climbs is a hand-drawn line chart** (Mark 10-23), point by point on each spoken number, under a quiet airy breath.
5. **Sound measured three ways** before it goes in: tonal prominence (<= 20 dB), the slice starts on its measured attack (envelope
   events listed per file), and `ig/cue_check.py` (premix - voice = the SFX alone) proves each crest lands on its frame and every cue's
   50 ms loudness sits >= 3 dB under the voice beside it (worst -6.4 dB). First pass had four cues as loud as the voice (a stinger,
   two thuds, the landing): lowered 3-5 dB; transients measuring 14-18 dB under (card slide, tag tap, chart dot) raised, since
   "quiet ticks read as none".
Caught by the 60 fps frame check, the proof sheet and the review pass (all fixed before delivery):
- **A floating card under the show bug**: the 640 px ad card at y 40 ran its corner under SUCCESS STORY. -> card at 90 % with its top
  at y 92 (bug bottom 74), all its marks scaled with it (AS). Rule: anything near the top of the window starts below y 80.
- **A hero phrase wider than a line orphans its neighbour**: "different kind of buyer" in red Playfair was > 620 px, the layout
  cannot split inside a red run, so "a" sat alone on line 1. -> hero = "different" (the stressed word). Rule: a red hero is one or
  two words; check every block's line count before rendering.
- **A drawn mark must arrive with its object**: on the callback the pair's FAKE was drawn at full strength while the shoes and prices
  were still fading in (0.35 s), so it floated alone under the burn. -> `hand_stroke(..., alpha=)` and `draw_fake_word(..., alpha=p)`;
  patched 962-1000, 1824-1850. Gotcha: `hand_stroke`'s own loop rebinds `a` to a point, so a fade argument named `a` is clobbered
  (the first patch died at the first drawn frame): it is `alpha`.
- **Every drawn stroke gets a sound, even a repeat**: the FAKE re-written under the pair's $150 (16.18-16.58) was silent, only the card
  slide 0.15 s earlier had one. -> the marker `write` slice again at 16.18, 9 dB under (24 cues).

## 2026-10-25 · Review 1 of the Chris Do IG Short: "the sound effects need to sound expensive and premium"
1. **Cheap = what a phone plays.** Measured: v1's cinematic hits (deep thud, airy hit, soft stinger, low thud) sat 25-41 dB down in
   300 Hz-6 kHz, so on a phone they vanished and only the foley came through: 8 soft taps, marker squeaks, pencil strokes, a card
   slide. -> One cinematic family only (trailer impacts, a hall tom, taiko, a reverberant impact, reverse swells, deep and clean
   whooshes, single soft deep thuds); no taps, no foley. -> `ig/sound.py` v2.
2. **Split the crack from the weight.** Every hit is HIGH-PASSED (70-150 Hz) before it is peak-normalised, so its crack, not its sub,
   sets its level; the weight is ONE sub-boom layer under the big moments (hook, the landing number, the callback).
3. **Check in the phone band, cue by cue.** `ig/cue_check.py` now renders each cue ALONE at the mixer's gain and reports it against the
   voice beside it, full band (>= 3 dB under, plus the whole SFX bus) and in 300 Hz-6 kHz (WEAK below -20 dB). v2: loudest -5.2,
   none weak. Also re-run the tonal test on the final SLICES: a trailer swell passed as a file (18.3) but its peak slice measured 20.2.
4. **A hit is placed by its attack, a swell by its crest.** Three hits had been placed by their 5 ms peak and started 100-140 ms early.
5. **Repeats get pitch steps, never the same sample 5x.** The thread's five thuds: his asks step up (0.94 -> 1.0 -> 1.06), the
   client's "Yes" sits low (0.89), each a dB louder; and check a "single" library hit is not a double (cd2-thuds-deep is 2 hits each).

## 2026-10-26 · Morgan "claw machines are rigged" IG Short (`projects/_client-scott-clary/morgan-claw-machine/ig/`, "start the ig variant")
What it did better than the Chris Do IG: Mark Brazil's CURRENT hook (checked @markbrazil 10-26: white bold sans, the promise words on a
flat red box), his camera floating as a card; transitions carry the motion (3 burns, one blue-edged; a red ink bleed into the $ card,
FX-15; a 0.3 s settle-in push on every other cut into B-roll or a card; hard silent cuts back to his face) and the only sound; the
cards are catalog moves (FX-28 dossier readout + FX-35 blur-isolate rows + FX-69/74 "1 in 20" marks; FX-11 $ split + FX-24 dashed arc
to a notched tag); the bunny returns (FX-79). The catalog pass is in the job's BRIEF.
1. **B-roll at exactly 60 fps, not x2.** Stock is 23.976 / 25 / 29.97: Chronos x2 gives 47.95 / 50 / 59.94. -> Topaz's tvai_fi with
   fps=60 on each span used (+0.5 s), frames mapped by TIME (`ig/tools/broll60.py`); qa.py measures frozen steps per shot (worst 4.3 %).
2. **A tight face crop wants a 4K plate.** Zoom 1.46-1.72 from a 2560 plate upscales his face 6-25 %. -> each cam shot as its own 4K
   Chronos plate (`ig/tools/cam4k.py`, 239 source frames, a few minutes); the 2560 plate only feeds the small hook card.
3. **A joint he turns through is ONE Chronos take.** As separate takes the cut gets no in-between frame and the take's last frame is a
   clone: his eyes stalled, then jumped 32 px (median 9). One take: no stall, 17 px across. (The YT's smooth_through, IG side.)
4. **Measure the head on the EYES.** YuNet's mouth corners move with speech (+-10 px): the same frames re-encoded flipped a joint
   verdict. qa.py now steps the eye midpoint across each in-shot joint against the median step around it.
5. **Frame 0 is the preview.** The hook faded in from black, so IG's first frame was dim text. -> the whole hook (title, red box, cam
   card) on frame 0; the tag decode and the bunny pop keep the motion.
6. **An ink bleed is bright and wet, never a dark splat.** First pass: the blot inherited the dark stage (maroon) and a spiky edge
   (high-frequency noise). -> low-frequency organic edge, 22 px smoothstep feather, a thin white rim, bright red that holds to 60 % of
   the transition then clears; its radius reaches past the window corners (880 > 800 px).
7. **A floating object never covers his face**: the payoff bunny sat on his cheek at 300 px; in a tight close-up it goes in the free
   top corner (905, 300) at 250 px.
8. **No fire, no crackle under a burn.** A light-leak burn suggests a flame sound, but Epidemic's "burn up / flare" files crackle (6 and
   4 sharp onsets, > 8 dB in 15 ms, after the crest) or hiss (62 % above 4 kHz): the foley texture that reads cheap on a phone. -> clean
   whooshes rising into the cut; the check (count onsets after the crest + the share above 4 kHz) runs on every slice before it goes in.
