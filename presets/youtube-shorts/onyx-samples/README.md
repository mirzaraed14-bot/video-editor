# Onyx sample Shorts: THE INSTAGRAM LOOK (minimal motion graphics)

> **Platform decides the look (Affan, 2026-10-05).** Every sample is built for the prospect's PRIORITY platform:
> - **Instagram-first → this file**: the minimal, card-based, motion-graphics look (the MFM pilot). Affan's verdict on the
>   pilot: *"a classic minimalistic Instagram style"*, fine apart from **too few sound effects in places**.
> - **YouTube-first → `presets/youtube-shorts/onyx-samples-youtube/`**: a separate, maximal B-roll storytelling look, built
>   from the reference Affan chose (Shawn Ryan Show, "Why Shawn Ryan Walked Away From His Dream Farm", 1.03M views,
>   `projects/_ref-yt-shorts-shawn-ryan-farm/`).
> How to pick the platform: PLAYBOOK § 0.

The look of the **sample Shorts Onyx Influence makes for podcast prospects** whose priority is Instagram: a re-edit of one
moment from their show, built to show what a full-time Shorts team would do for them. It is the sales piece. Affan reacts
to it in a separate video, and both are emailed to the host after they say yes to the permission email.

Procedure: [PLAYBOOK.md](PLAYBOOK.md). What jobs taught: [LESSONS.md](LESSONS.md).

**Not Abundance Wisdom.** Nothing from `presets/youtube-shorts/abundance-wisdom/` applies here: no glow bars,
no flashes, no Gretaros, no grade preset, no head lock. Told 2026-10-04: *"another style, not abundance wisdom,
something more minimalistic yet visualistic with motion graphics."*

Status: **v1** (the pilot `projects/mfm-nursery-rhymes/` shipped on 2026-10-05 after 3 QA rounds; Affan approved the look).
Log every change in LESSONS.md.

---

## 1. The idea in one line

**Minimal canvas, moving picture.** One neutral palette and one accent, lots of empty space, and the shot keeps
changing shape: the speaker full-frame, then shrinking into a framed card with words above and below, then
giving the screen to a motion graphic, then back. The change of shape is the energy, so nothing else needs to shout.

## 2. Delivery

| | |
|---|---|
| Canvas | 1080×1920, 30 fps (podcast sources are 24–30 fps; never interpolate) |
| Length | 30–50 s (the hook must land in the first 2 s) |
| Finish | **Fully automatic MP4**, rendered by the chat-only route (HyperFrames + ffmpeg). Affan chose this on 2026-10-04 so the samples keep pace with the yeses. No Premiere step. |
| Safe zone | Everything readable inside y 200 → 1620 (repo rule). |
| Loudness | Speech chain from the rough cut (−17 LUFS pre-limiter, −6 dBFS limiter); music bed at −20 dB under it. |

## 3. The shot grammar: four modes, mixed inside every clip

Told 2026-10-04: *"a good mix of all formats, not just one. For a few seconds just the person talking, then
the next shot can be a visual motion graphic while they get zoomed out into a rectangle, with text above and below."*

| Mode | Picture | Use it for | Length |
|---|---|---|---|
| **FULL** | Speaker fills the frame, face-tracked crop of whoever is talking. Slow push 1.00 → 1.06 over the shot. Captions low. | The hook, opinions, emotion, laughs: anything where the face IS the content. | 1.5–4 s |
| **CARD** | The same video shrinks (one continuous tween, no cut) into a rounded rectangle: 900×900 (1:1) at y 330, radius 36. **Kicker text above** (topic or name, 2–5 words), **key line or number BELOW the card** (y ≈ 1258), captions under it (y 1440), a small grey source line at y 1572. **CARD16** = a 900×506 16:9 card centred in the same zone, for an episode's two-up layout (crop into the speaker's box, never show both boxes or a burned-in label). | Names, deals, numbers, any line worth reading. The default "talking" mode. | 2–6 s |
| **GRAPHIC** | Full-screen motion graphic; the voice keeps running. Speaker bubble: circle, 220 px, bottom-right corner (x 800, y 1380), gold ring. Captions sit above it (y 1278). | The moment a picture explains faster than words: count-ups, logos side by side, a deal stack, a multiplier, a timeline. | 1.5–3 s |
| **SPLIT** | Top half: a graphic that builds while they talk. Bottom half: the speaker. Captions on the seam. | A list or a process the speaker walks through (step 1, 2, 3). | 3–8 s |

**Rhythm rules (v0):**
- **Open on FULL** with the hook line, then switch within 2 s.
- The mode changes every **2.5–5 s**. Never hold one mode past 6 s.
- **Never two GRAPHICs in a row**: return to the face (FULL, CARD or SPLIT) in between.
- Every switch lands **on a word boundary**, ideally the stressed word.
- **End on CARD** with the payoff line in the bottom text slot.
- **No CTA** and no Onyx branding on the sample itself (repo rule: no sales asks inside a video). The show's own name may appear as a kicker.

## 4. Motion

- **One easing family:** expo-out for entrances (fast start, soft landing), expo-in for exits. 0.35–0.5 s per move.
- **Window morphs: power3.inOut, 0.55 s** (expo.inOut squeezed the change into 2 frames and read as a cut; QA 2026-10-05).
  A morph that also changes speaker starts 0.18 s before the camera cut. Graphics enter only once the window has landed.
- **FULL ↔ CARD is a morph, not a cut**: the video wrapper tweens position, size and corner radius together.
- **Type rises in**, masked: each line slides up 40 px from behind a mask with a slight stagger. Type never pops or bounces.
- **Objects (logos, icons, chips) pop:** scale 0.85 → 1.0 with a tiny overshoot.
- **Numbers count up** in place (0 → $3,000,000,000), ~0.8 s, a tick sound on the last digits.
- Large slides **of graphics** get motion blur. **Window morphs don't**: a uniform blur pulse on a face reads as a focus
  fault, not motion (decided on the pilot, 2026-10-05).
- No glows, flashes, grain, shakes or neon. Minimal means the motion carries it.

## 5. Type and colour

| | |
|---|---|
| Font | One grotesk family, two weights (Regular for captions/body, Bold/Black for numbers/kickers). v0 pick: **Inter** (bundled in `assets/fonts/`: Regular, Bold, Black); revisit after the pilot. |
| Captions | 2–4 words / ≤ 22 characters per chunk (one line at 66 px), sentence case (a chunk that opens a sentence is capitalised), white, **active word in the accent colour**. Numbers stay with their unit; a chunk never ends on "to/for/the/and…". **Positioned JUST BELOW THE SPEAKER'S LIPS, per shot** (Affan, 2026-10-06: *"the distance between the captions and the lips needs to be shorter… I was constantly moving my eyes up and down"*): `kit/ig_capy.py` maps the measured mouth landmarks through each shot's crop and puts the caption top ~0.075 × face height under the lip line (on the chin, never on the lips); B-roll and full-screen graphics use the video's median face-shot position; cards push it clear. The old fixed bands (FULL 1330, CARD 1440, GRAPHIC 1278, SPLIT 922) are the fallback only. **A dark pill backs every caption during a window morph.** A caption ends at a speaker-changing cut, and leaves when a morph starts if its words are done. Around a morph into or out of the bubble, a caption waits ≤ 0.15 s so the window is mostly out of the band (a brief edge overlap under the pill is accepted). Run the whole video (repo rule). |
| Kicker | All caps, letter-spaced 0.18em, 34 px, 70 % opacity. |
| Big number / key line | 96–140 px Bold, accent or white. |
| Canvas | Off-black `#0E0E0E` (default) or off-white `#F2EEE6` (light shows). One per clip. |
| **Accent** | **ONE colour per podcast, taken from the show's own branding** (logo or thumbnails). It shows we built it for them. Logged per job in BRIEF.md. |

## 6. Sound

- Soft whoosh on every **entrance** (a switch away from the face), peak on the switch, low level. ~~Returns to the face are silent~~ → **Affan, 2026-10-05: "there aren't sound effects enough in places"**: the pilot's density (21 cues in 33.6 s, 0.6/s, with several 2–4 s silent stretches) is too sparse. Next sample: a sound on EVERY visual event (returns to the face included, softer), caption-chunk ticks on punch words, and no stretch over ~1.5 s without a designed sound. **Measured against the YouTube reference (2026-10-05):** it has almost NO sound
  effects (silent transitions, one chime) and still feels full, because a continuous music bed runs ≈ 13.6 LU under the voice from the first
  frame to the last (`presets/youtube-shorts/onyx-samples-youtube/` README § 8). The pilot had no bed. So the likely fix here is **a bed plus
  more SFX**, not more SFX alone. Affan picks.
- Small tick on count-up landings; a **single-hit** pop on object pop-ins (slice library files to one hit, since some hold several). No sub-drops or sustained impacts.
- One music bed at −20 dB, no ducking (repo default), picked to fit the show's tone.
- The speaker's voice is the star: nothing masks a word.

## 7. Open questions for Affan (resolve on the pilot)

1. Inter, or a different font family?
2. Dark canvas by default, or match each show's brand (light vs dark)?
3. Speaker bubble during GRAPHIC: always, sometimes, or never?
4. Music bed: always, or only when the show uses music in its own Shorts?
