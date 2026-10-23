# Neon window: Instagram look (rounded window on black + Mark Brazil's type)

**Status: v1.2, 2026-10-22, after Affan's first review** (`LESSONS.md`: colour not B&W, a hint of glow not a bloom, no electric
or narrow-tone sounds). Built for the Scott D. Clary Short "Marvel's board vs Robert Downey Jr." (Instagram variant,
`projects/_client-scott-clary/marvel-board-vs-rdj-ig/`, master in `X:\Claude Projects\Exports\scottclary-marvel-board-vs-rdj-ig.final.mp4`).
Log every review in `LESSONS.md`.

## What the first build's frame checks taught (apply from the start next time)
- **Type over a bright room dies.** A webcam in a white living room needs the low-key relight (room to black from the top and
  edges) before any white or neon type goes over it. Bright stills need the caption-band scrim + the dark halo; a document whose
  own lettering is white and large (a magazine cover) goes on the stage as a whole card, never full-bleed under captions.
- **A word starting ON a block boundary** (26.1499 vs 26.15) lands in both blocks; select words with a 20 ms tolerance, and never
  let a word or stage element appear before its own block / shot (the 1-frame pre-roll otherwise flashes over the previous shot).
- **Playfair's default figures are old-style** ("$525" reads "$5z5"): use the lining copy.
- **A "60p" upload of a webcam is not 60p**: measure duplicate frames first (`ig/motion_check.py`: 57 % frozen steps on Peter's
  cam); double the 30p cut with Topaz Chronos per take (`--fps-mult 2`, ~7 min for 40 s on the 3060 Ti) -> 1.8 %. Never start Topaz
  while another session holds the GPU: `ig/topaz_when_free.sh` waits for it, then rebuilds and recopies by itself.
- **Long Epidemic files** (60-80 s ambiences, 19 s shutter sets) misread the mixer's whole-file peak: slice and peak-normalise
  first, then place by dB under the voice peak; a buzz with sparse pops needs ~5-6 dB under, not 10-12, to be heard.

## What Affan asked for (2026-10-21, his words)
- He picked from 10 clean IG pages, then: *"analyze mark brazil's style frame by frame ... scan his last 10 reels"*.
- Then: *"I want the motion graphics and subtitles style of Mark but in the rounded rectangle aesthetic like this"*, with a
  DOAC reel frame as the reference (`projects/_client-scott-clary/marvel-board-vs-rdj-ig/work/look/reference-rounded-window.png`).
- So: **the frame is DOAC's** (rounded window, black surround) and **the type and motion are Mark Brazil's**. The picture is
  in COLOUR (review 1: *"I prefer you don't do the grayed out style"*), even though the reference frame was B&W (study: `presets/youtube-shorts/onyx-samples/references/markbrazil-study-2026-10-21.md`, frames in
  `markbrazil-shots/`).

## The numbers (1080 x 1920, 60 fps)
| Element | Value |
|---|---|
| Window | **1044 x 1044 at x 18, y 438, corner radius 48**, anti-aliased; outside it pure `#000`, nothing ever drawn there |
| Picture | **Colour**, dark and neutral-cool (Mark's studio): cam gamma 1.35, contrast 1.08, saturation 0.85, tint R 0.985 / B 1.025, then a low-key relight (the room falls to black from the top 42 %, up to 205/255, and outside a radial vignette centred at 0.63 of the height) so type reads over a bright room. Stills: gamma 1.15, contrast 1.06, saturation 0.92, vignette + the caption band darkened (bottom 42 %, up to 88 %). One eased push 1.00 → 1.06 per still, never a punch-in |
| Stage | Mark's dark set, built: near-black slate with a soft top light (radial, 57 → 5 luma, tint 0.93 / 0.98 / 1.06). Used for the big-type beats only; never a fake studio with the speaker in it |
| Captions | Inter Bold **46 px**, white `#FDFFFF` + a faint white halo (r 6, 0.22) + dark halo (r 12) for stills; centred; **one fixed spot just under the lips for the whole video** (block top y 1322, line pitch 58, max line 560 px, balanced 2-line split that never breaks the hero phrase). Words appear on their spoken word with a 4-frame fade (0.35 / 0.6 / 0.82 / 0.95 / 1) |
| Caption hero | ONE phrase per block in **Playfair Display Black Italic 62 px, pure red `#FF0505`**, a hint of glow (10 px 0.35 + 3 px 0.3; review 1: "too glowy" at full gain), dark halo (16 px, 2.2) so it holds on a red picture. It cuts in fully formed and the glow strikes: 0.4 / 0.8 / 0.6 / 1.0 / 0.9 / 1.0 over 6 frames |
| Stage type | Lead-in Inter 46 px white, left x 72 (window); giant red Playfair Black Italic fitted to 900 px (≤ 156 px; single words up to 330 px), glow 20 px 0.32 + 5 px 0.28; tail Inter 40 px. The stack IS the caption on those beats (no duplicate line at the bottom) |
| Numbers | Lining figures: `ig/fonts/PlayfairDisplay-Italic-VF-lnum.ttf` (the font's own `lnum`, made by `ig/lnum_font.py`; this PIL has no libraqm). Old-style figures made "$525" read "$5z5" |
| Credit tag | Mark's mono tag, 0 → 3.1 s: red bar 6 x 154 px + glow, IBM Plex Mono 34 px (role) / 64 px (name); the bar flickers on (1,0,1,1,0,1,1), the text decodes left to right from random capitals, then decodes out |
| Name card | Wide-tracked red caps (Inter Bold 60, tracking 44 px) across the chest, letters flickering on in random order, all steady by ~0.32 s; dark halo (14 px, 2.4) because the chest can be red |
| List swap | White lead word fixed, red Playfair names flicking every 6 frames with a 2-frame scramble, landing on the total |
| Diagram | One white hairline axis, Playfair Italic labels, a red line + glowing dot climbing it |
| Light-leak burn | ONLY where the source changes, 3 per Short: 10 frames of orange → red → yellow wash over the outgoing shot, the cut, 8 frames of red vertical streaks on the incoming one |
| Show bug | The reference's white label box ("SUCCESS STORY", Inter Bold 26 on `#F5F5F5`), inside the window's **top-right** (bottom-left collides with 2-line captions) |
| Sound | One designed SFX per graphic event, peak-normalised slices, placed in dB under the voice peak: hits and impacts 6-7, clicks 8, swells 8, whooshes 16. The palette is cinematic only: swells and risers that PEAK INTO a reveal (slice ends on the peak), reverberant impacts/thuds ON it, airy whooshes on burns, an analog shutter on stills. **Never** the electric family (neon buzz, fluorescent hum, tube flicker) or anything tonal: measure tonal prominence above 1 kHz first, > 20 dB = reject (review 1: the rejected cues measured 25 and 38 dB, accepted ones 8-19). No bed (Scott). Mix -12 LUFS, -2 dBTP via `yt_mix.py` |

## Affan's standing rules that override Mark
Captions only `! ?` and quotes · one constant caption position · white line on any split · SFX on every graphic ·
every picture sharp (no shallow-focus softness on name cards) · no bed / no CTA on Scott jobs · work in silence.

## How to build the next one
Two kits to copy, by source:
- **Webcam / remote guest** → the Marvel job's `ig/` (`projects/_client-scott-clary/marvel-board-vs-rdj-ig/`): fixed crop, room relight.
- **In-person studio camera** → the War Dogs job's `ig/` (`projects/_client-scott-clary/war-dogs-fake-office/ig/`, 2026-10-23): the
  cam is EYE-LOCKED per take (faces.json eye centre, smoothed sigma 12 frames inside each take, never across a joint, so the head
  never jumps at a jump cut; eyes at window (522, 420), the frame's top edge melting into black above the head), with the approved
  quick pushes as zoom keys; `--fps 30` renders a quick check on the 4K Topaz base; photos of real people below the window's size
  play as sharp PANELS at or under native size over a blurred copy (Affan: no Topaz on faces); cards restyled in code (counter,
  checklist with red ticks, a white Craigslist artifact card, hairline figures).
Rewrite only the beat plan at the top of `build.py` (SHOTS, LEAKS, BLOCKS, the stage beats) and `sound.py` (CUES; a FRESH Epidemic
set per job, each slice tonal-checked). Cam at 60: if the source repeats frames or is 30p, double the 30p cut with Topaz Chronos
per take: `workflows/topaz-iris.py <cut30> ig/work/cam60.topaz.mov --fps-mult 2 --no-enhance --no-stab --segments <30p joints>`
(the 4K base scaled to 2560x1440 keeps detail for the pushes; ~30 min for 45 s while sharing the GPU), **wrapped in
`projects/_onyx-batch2-2026-10/lock.sh gpu`** (sessions share one GPU; two Topaz jobs at once can run out of VRAM), then
`ig/motion_check.py`. Then `python ig/build.py --frames ...` for checks, `python ig/build.py`, `python ig/sound.py --mux`,
`python ig/qa.py outputs/<job>-ig.final.mp4 60`.
