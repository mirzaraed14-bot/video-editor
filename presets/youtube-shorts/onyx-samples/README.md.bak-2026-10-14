# Onyx sample Shorts: THE INSTAGRAM LOOK (minimal motion graphics)

> **AFFAN'S RULES, ALL VIDEOS (review 2, 2026-10-07; verbatim + per-video plan in
> `projects/_onyx-batch-2026-10/REVIEW-2026-10-07.md`). They override anything below that disagrees.**
> 1. Captions keep ONLY `!` `?` and quotation marks: no full stops, no commas, nothing else.
> 2. Caption base position is CONSTANT for the whole video, just under the lips where the face sits; it never moves on a cut
>    (frame the speaker shots consistently instead). The entrance animation is fine.
> 3. The caption entrance must look smooth: the Instagram look's rise tween renders at 60 fps (`ig_build.py` outputs 60/59.94). The
>    YouTube look keeps its measured stepped pop at the source rate (the reference design; MFM is "perfect").
> 4. No instant zoom-in (punch-in cut) on the same camera: one continuous keyframed push-in.
> 5. Transitions (whips) ONLY where the scene/camera/source changes, never between two shots of the same camera.
> 6. Every pop-up / motion graphic has an audible, crisp SFX (high-end minimal podcast vibe; Epidemic Sound).
> 7. Captions: white base + coloured emphasis words (not one colour for everything).
> 8. Never cut a word short at a joint. 9. The hook makes a STRANGER care: who this is and why the story matters to them.
> "Sean Ryan style/format" in Affan's words = `onyx-samples-youtube/` (this look's reference). MFM's sample is the benchmark: "perfect".

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

---

## v2 look downloads note (batch 2, 2026-10-12)

Logged BEFORE each pull (batch-2 download approval, AGENT-BRIEF § Downloads; Epidemic = Affan's own library via the MCP).

| # | File | Source | Size | Why |
|---|---|---|---|---|
| e1 | `assets/sfx/epidemic/tick-glass.wav` | Epidemic SFX 45c94b43-2fb0-4970-98db-cc0fe6ea3678 "User Interface, Click, UI Buttons, Glassy, Touch" (WAV, 96 kHz) | 101,602 B (done) | widget taps / HUD ticks: a glassy tick with body |
| e2 | `assets/sfx/epidemic/blip-data.wav` | Epidemic SFX 7762db67-eb05-432b-8662-a9e448f9cab2 "User Interface, Data, Data Process 03" (WAV, 96 kHz) | 281,236 B (done) | the mono "data blip" under a HUD label typing in |
| e3 | `assets/sfx/epidemic/focus-pull.wav` | Epidemic SFX 0a960941-eb3d-42b6-95c1-4c21a1fd1db1 "Communications, Camera, Lens, Auto Focus, Nikon F4 01" (WAV, 96 kHz) | 315,206 B (done) | the reticle snap / rack focus |

Not downloads (already on this machine, copied, so nothing new was pulled for them):
- **Epidemic SFX from Affan's own library**, pulled 2026-10-08 for `projects/nick-martin-same-night/audio/sfx/` (ids in its
  `fetch.py`), copied into `assets/sfx/epidemic/` under the same names: `thud-low` (e4fa7af5), `thud-thin` (866b9c73), `hit-soft`
  (30e50311), `whoosh-soft` (f040a2a4), `whoosh-med` (36d506f7), `shutter-film` (723aa2bf), `rise-air` (the chirp-free swell),
  `flash-vintage` (ab4f5745), `boom-dark` (d106e784). The names that clash with this kit's files (whoosh-air, whoosh-light, shutter,
  riser) were NOT copied.
- **Fonts (SIL OFL 1.1, Google Fonts families installed in C:\Windows\Fonts)** copied into `kit/fonts/`: IBM Plex Mono Regular /
  Medium / SemiBold (the research's "JetBrains Mono or IBM Plex Mono"), Cormorant Italic VF (a Garamond-family italic: the research's
  EB Garamond Italic role), Unbounded VF (a wide geometric grotesk: the Archivo Expanded role). Each file's name table carries the OFL
  notice.

---

## v2 look (batch 2)

Affan, 2026-10-12: *"minimalistic, so big black bars, because Instagram prefers that cinematic look; caption animations; the video
itself minimalistic but with a LOT of motion graphics: minimalist, high quality, premium, refined… clean crisp sound effects; it should
look like an expensive video."* Built from the measured references in
[references/batch2-style-research.md](references/batch2-style-research.md) (DOAC, YC, Stealth Motion, Mark Brazil, vitalyframes…).
**Opt-in:** a spec with `"look": "v2"`; every v1 job rebuilds byte for byte as before (checked on all six batch-1 specs, LESSONS
2026-10-12). How to build one: [kit/V2-HOWTO.md](kit/V2-HOWTO.md). Demo: `projects/_onyx-batch2-2026-10/kit-demo/`.
All rules at the top of this file still apply (punctuation, ONE caption position, SFX on every graphic, no stray frames, no CTA).

| | v2 numbers (research move) |
|---|---|
| Frame | Pure black bars 510 / 510 px; the picture in a **1044 x 900 window at x 18, y 510, corner radius 64** (Stealth Motion measured 1044 x 899, bars 507 / 514, r 64-80). Alternative: 1080 x 810 at y 555, square corners (Valueclippss). `spec.frame` overrides. The speaker is face-tracked INSIDE the window (the shared engine renders every shot kind at window size: A, B-roll, FIT, SPLIT). A split's seam sits in the window (default 450) with the white line. |
| Finish (in the window only) | Grade contrast 1.12, saturation 0.88, warm 0.025, black lift 0.015 (the job's `grade` wins per key); vignette 22 % from 0.6 of the half-diagonal; mono grain sigma 1.9 code values (a 3 % plate), seeded per frame (sigma 3.8 tripled the file size for no visible gain). `rack`: a pre-blurred (16 px), pre-darkened (42 %) clone crossfaded in under full-window type. `leak`: a warm screen-blended light leak 0 -> 0.9 -> 0 over 0.35 s, on scene changes only. `mood`: B&W + accent tint for the darkest line. |
| Top bar | The hook only, <= 3 s, centred ~ y 365: a mono kicker (who this is) + 2 lines of 62 px Inter Bold that rise out of a mask, one word in the serif accent. |
| Bottom bar | The credit, 26 px mono caps at 55 % white with a short accent dash, at y 1500 (replaces the v1 grey pill). |
| Captions | ONE constant top for the whole video, just under the lips, clamped inside the window (ig_capy measures; `on_seam` puts it on a split seam). `stack` (default): words land on their own word (opacity, x +24, blur 6, scale 1.04 -> 1 in 0.12 s power3.out), lead 54 px Inter Bold, ONE hero per block on its own line at 124 px Cormorant Italic in the accent with a glow; blocks <= 6 words, break on sentence / comma / pause; `cx` centres the block under an off-centre mouth. `word`: one word, mono caps on a translucent box or wide Unbounded caps with a cream gradient. `line`: 58 px chunks rise 40 px from a mask in 0.32 s, the hero word's colour sweeps in on its word (0.22 s). `colors` gives words meaning (green gain, red loss). Only ! ? and quotes (captext.clean). |
| Graphics | Dark glass (gradient 84-88 % black, 1.5 px hairline, 46 px accent glow), mono labels (IBM Plex Mono), serif-italic hero words and numbers (Cormorant / Playfair), wide caps for names (Unbounded). Kinds: `lower3`, `neon` (number that re-rolls), `reticle`, `route` (timeline / map, vertical or horizontal), `widget` (todo / list / progress / notify, cursor taps, hand-drawn ticks), `wordscene`, `titlecard` (RGB split settling over the racked picture), `compare`, `leak`. Entrances blur in and rise (power3.out); objects settle 1.06-1.18 -> 1.00 with no overshoot; lines draw on (power2.inOut); slides carry a directional motion blur; exits 0.14-0.25 s. Full keys: `kit/ig_v2.py` docstring. |
| Layout | Speaker on the right third (`fx_out` ~0.64), side graphics in the window's left side above the caption line; full-window scenes <= 3 s each and <= 25 % of the runtime with >= 1.5 s of face between them; a side card dips out under a full-window scene. |
| Density | >= 3-4 designed events per 10 s (each card entrance and each beat inside a card: a tick, a node, a re-roll, a word); `ig/work/v2-events.json` + the build's report. The demo runs ~7 per 10 s. |
| Sound | One sound per designed event, never per caption word; set by peak under the voice's own peak (ig_build `ES`): lower3 = glass tick + soft whoosh · reticle = lens focus + film shutter (+ a quiet data blip under the label) · neon = a reverberant soft impact on the value; re-roll = an airy swell INTO it + a thin thud · widget = soft whoosh, glass tick per tap / row, `confirm` on the last tick · route = soft whoosh + glass tick per node · wordscene = medium whoosh, a glass tick per word, a thud on the hero · titlecard = medium whoosh + low thud · compare = a soft whoosh per side + a thin thud on the winner · leak = vintage flash + airy swell · split = soft whoosh · hook = soft whoosh + thin thud. Whooshes 15-16 dB under the voice peak (Affan's -10 dB, built in); swells and whooshes are placed so their CREST lands on the event (`ES_PRE`), long tails fade (`ES_DUR`). |
| QA | `kit/ig_qa.py <job> <out.mp4> --sheet`: decode, loudness, every word once, punctuation, one caption y inside the window, a sound on every event, each cue's level against the voice, the density report, a contact sheet. |

**Build:** `python projects/<job>/ig/build_spec.py && python presets/youtube-shorts/onyx-samples/kit/ig_build.py projects/<job> <version> --preview`
(ig_build routes a v2 spec to `ig_window.py` for the picture and `ig_v2.py` for the overlay; the window render is cached between
builds while the shots are unchanged).
