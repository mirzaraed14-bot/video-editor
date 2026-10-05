# affanwiz — THE EDITING STYLE (adopted 2026-10-04, from the next video on)

**The creator, 2026-10-04:** *"We're picking up this editing style from my other channel for our next video."* The
reference is their Affan Afterhours video **"Everything Game Informer Just Revealed About GTA 6"** (YouTube
`EsnIehnZUhs`, published 2026-09-29, 6:22). It was built in this repo as job `projects/gta6-hurricanes/`
(ABW8 · Sequence 16); the published master is `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Weather GTA.mov`
(1920×1080 59.94, 382.2 s), and it is **Sequence 16 exactly as saved** (diffed 2026-10-04: one pop nudged to 0:00,
nothing else changed after our last save).

Every number below is either READ OFF THAT TIMELINE (`reference/game-informer/timeline.json`, read live and read-only)
or MEASURED ON THE MASTER with the style tools (`reference/game-informer/report.md`, `probe/`, `zoom.json`,
`transcript/words.json`, `frames/sheet.jpg`). This file is self-contained on purpose: it is AffanWiz's copy of that
look, so a later change to the Afterhours presets never moves this channel silently.

---

## 1. The shape of the edit

| | measured | the rule |
|---|---|---|
| runtime | 6:22 | |
| visible changes | **25.6 / min** (hard cuts 13.5, same-size jump cuts 10.7, zoom steps 1.7) | ~25 changes a minute, never a still frame for long |
| face on screen | **77 %**, 25 face runs, median 10.6 s, longest 30 s | the face is the meal, ~3/4 of the runtime |
| overlays | **24 slots = 3.9 / min**, median 3.6 s, longest 7.4 s, 26 internal switches | ~4 a minute, 1.5–7.5 s each, never long |
| cut zooms | **22 = 3.5 / min**, median **121 %** (103–203), hold median ~1.4 s (0.7–5.1 s) | § 2 |
| gradual push | on EVERY face run: 100 → 110 across a nest, 100 → 105 on a short clip (0.62 %/s measured) | § 2 |
| speed changes | **none**: every clip at 100 %, nests included | no slow-downs in this style unless asked |
| transitions | none: hard cuts only, every boundary | |
| speech | 196.5 words/min, only 2 pauses ≥ 1 s | cut tight |
| first / last shot | **overlay** (the news article, voice over it from 0:00; face at 3.2 s) / face | open on the artefact the video is about, close on the face |
| grade | none (no adjustment layer); luma 0.28 | the lit room is the look |
| on-screen text | only inside the two built cards (§ 3c) | no captions, no lower-third, no logo, no subscribe bug, no end card |
| master loudness | −17.4 LUFS integrated, LRA 6.9 LU | |

## 2. The face (V1)

The track: **V1 = the face cut** (raw clips + nests), every clip at 100 % speed.

1. **Every face run moves.** A run of ~8 s or more is **nested**, and the nest clip's Scale is keyed **100 → 110,
   linear, first frame to last** (17 nests here, 8.3–24 s long, so 0.4–1.2 %/s). A short run (~3–6 s) is keyed
   **100 → 105** on the raw clip itself. A clip that IS a cut zoom, or a sliver between two zooms, stays still.
2. **Cut zooms** = razor-cut the clip and set a **static Scale** on the piece (inside the nest when there is one:
   14 of the 22 sit inside nests, 8 on V1). Then straight back to 100. Two families:

   | family | scale | lands on (the words under it, from the master) |
   |---|---|---|
   | **emphasis** (17) | **103–135 %**, mostly 110–126 | "only question that matters" · "spoken about this for the past 20 years" · "very very cool" · "storm type thing" · "I'm very very intrigued" · "something that Rockstar told us back in August" · "might be lower because you robbed a store in the hurricane" · "if you think Rockstar wouldn't make the weather cost you something" · "some sort of consequence attached to rough weathers" · "doesn't really matter… 24 hours into the game" · "Quickfire also confirmed" · "gonna have a zoo" · "if that is the case" · "I lost it" · "people are saying that" · "backstory" · "there used to be rain" |
   | **the punch** (5) | **139–203 %**, with Position **re-centred on the face** so it stays in frame (149 % at x 0.435 · 203 % at x 0.354 · 145 % at y 0.607 · 161 % at y 0.563) | "let's get the facts straight first" · "blamed it on yourself" · "I don't know why I did that" · "fancy schmancy weather stuff" · "because I don't know what to make videos on" |

   Emphasis goes on the claim and the adjective that sells it; the big punch goes on the joke and the self-roast.
3. **The music drops out under every cut zoom** (§ 4). That is part of the zoom, not a separate decision.

## 3. The overlays (V3 matte + V4 overlay)

### 3a. The frame — every overlay, no exceptions
| element | value |
|---|---|
| **inset** | **85 %: 1632 × 918**, centred (x 144, y 81), **rounded corners 22 px**. The picture **fills** the inset (scale-to-cover, centred crop), so the matte shows evenly on all four sides ("edges bleed"). |
| **cleanup first** | crop off HUDs, minimaps, watermarks and burned-in subtitles before the cover-scale (margins used: game HUD l/t/r/b 10/6/6/16 %, a watermark 4/8/8/4 %) |
| **drop shadow** | baked into the overlay: the same rounded rect, black at **~69 % (175/255)**, offset **+16 x / +24 y**, Gaussian blur **26 px**. (Premiere's Drop Shadow is near-invisible on a dark matte.) |
| **file** | ProRes 4444 with alpha, 59.94, one clip per slot on **V4**, Motion untouched (100 %, centred) |
| **matte** | its own clip per slot on **V3**, **a different palette every time** ("don't just create one colour matte, keep a variety"): a 3-colour animated gradient in dark jewel tones (channels mostly ≤ `0x7a`, one accent up to `0xb0`, e.g. `3a0a5a / 0b1f4a / b0287a`), drifting slowly (ffmpeg `gradients` n=3, speed 0.012, type radial / linear / spiral, seed per slot), temporal grain (`noise=alls=5:allf=t`), vignette `PI/4.5`. The palette nods to the content: amber and brown under a dust storm, greens under the animals, blues and teals under rain. |
| **inside a slot** | the picture changes on the creator's own block edges (24 slots → 44 pictures); video runs at 100 %. |
| **stills** | a slow **eased 5 % push** over the hold (cosine ease). **A rapid run of stills (≤ ~1 s each) does NOT move** (the creator, 2026-09-30: four 0.4 s screenshots pushing was "too flashy… very jarring"). |

### 3b. What goes in them
23 of the 25 overlay runs are **video**: GTA 6 footage (the Extended Look first, then the trailers), old-game footage
(Vice City, San Andreas, GTA 4/5, Red Dead 2 from YouTube, crisp 1080p) wherever the line names it, and **the
creator's own earlier videos as the outro callback** ("Hot Coffee mod… that flopped / Wolverine video… that
flopped"). Stills: the news article itself as the cold open, a quick flash-run of the article's screenshots, an
article headline as proof of a claim. Every screenshot clean and sharp; **Higgsfield-enhance when soft** (README § 1a).

### 3c. The two built cards (2 in 6:22: earned, not routine)
Both live INSIDE the same 85 % frame on their own matte, set in **Inter** (Black / Bold), cream `#F6F1DC` with ONE
accent colour, hot pink `#FF2D95`:
- **The quote card** (5.4 s): a Higgsfield background with no text (a neon Vice City street at night, blurred), the
  quote in Inter Black ~52 px cream with **the load-bearing words in pink**, a small pink caps kicker (name · title),
  an attribution line in cream at ~75 % ("speaking to IGN, August 2026"). Lines rise in staggered (0.35 s eased,
  0.09 s apart), the card pushes 4 % over the hold. **The quote is verified against two sources first.**
- **The number card** (1.6 s): blurred footage behind, a pink caps kicker ("THE ANIMAL NUMBER"), the number huge in
  Inter Black ~260 px cream with a soft shadow, a label under it ("ANIMAL SPECIES", Inter Black ~55 px) rising in
  at 0.9 s.

## 4. The sound

| track | what | level |
|---|---|---|
| **A1** voice | the creator's Enhance-Speech voice, no other effects | clip 0 dB |
| **A2** music | **Epidemic Sound beds, one per section, ~2 min each**: *Loungin* (Scientific) 0:00–2:16 · *First Born* (Timothy Infinite) 2:34–4:17 · *Brooklyn* (Dyalla) 4:22–end. Chill, beat-driven, no vocals. The first bed enters at 0:00 already 11 s into its track (no intro). **A music-free gap before each new song** (17.6 s and 5.1 s). Ends with the video, no fade. | clip 0 dB; measured **~12.5 dB under the voice** (pauses with music −30 dBFS RMS vs speech −17.6) |
| A2, under every cut zoom | **the music is lifted** for the zoomed block (22 drop-outs here): razor in and out, no fades, the bed plays on from where it would have been | silence = room tone (−45 dBFS) |
| **A3** pops | Epidemic **"Cartoon, Pop, Mouth, Finger"** (0.40 s, transient 4 ms in) on **every overlay entrance AND every internal switch** (44 = 24 + 20), never on the exit back to the face, at most 3 a second. Alternate on file: "UI Click Select 01". | clip −6 dB (−6 dBFS peak) |

## 5. What changes for AffanWiz (vs README § 1a, job 1)

| | AffanWiz job 1 (§ 1a) | **this style, from the next video** |
|---|---|---|
| overlay size | fit INSIDE 1700 × 972 (88.5 %), whole picture | **FILL a 1632 × 918 inset (85 %)**, cover-crop, **22 px rounded corners** |
| matte | one seamless plum/teal matte the length of the sequence | **a different animated gradient per overlay** |
| shadow | 100 %, spread 10, offset 16/20, blur 24 | **~69 %, offset 16/24, blur 26** |
| overlay SFX | none | **a pop on every entrance and switch** |
| face pushes | the creator's | every run: nest 100→110 / short clip 100→105 |
| music under zooms | out under every punch-in (127 %) | the same rule, every cut zoom |

**Kept from § 1a:** the Higgsfield enhancement rules, and the **tiny-overlay exception**: a crop too small to fill the
inset without blowing past ~2× (a view-count badge, a one-line crop) still goes **960 px wide, centred, on its own
matte with the shadow**. The reference has no such overlay, so this is an inference, flagged for the creator's first
review.

## 6. Definition of done for a draft in this style

- visible changes ≥ ~25 / min; face ~75–80 %; overlays ~4 / min, 1.5–7.5 s, none longer unless it is the evidence
  (measure the draft export with `workflows/style-probe.py` + `style-report.py`, the tools that measured the reference);
- every face run has its push; cut zooms ~3–4 / min, emphasis 103–135 %, the punch 139–203 % re-centred;
- every overlay: 85 % inset, filled, rounded, shadowed, on its OWN matte, a palette not used by its neighbours;
- a pop on every overlay entrance and internal switch, none on exits; music out under every cut zoom, a gap
  before every new bed;
- no transitions, no slow-downs, no captions, no grade; opens on the subject's artefact, closes on the face.

## 7. Where the tools are (the proven pattern, job-local)

`projects/gta6-hurricanes/overlays/build.py` (SLOTS → mattes + ProRes overlays + the two cards) · `overlays/place.py`
(V3/V4 placement, refuses if V2 moved) · `overlay-sfx.py` (the pops) · **`lanes/premiere/music-dropouts.py`** (the drop-outs, V1 + nests, pushes excluded;
finds exactly the reference's 22 ranges). A new job copies the overlay pattern and changes only its SLOTS.
