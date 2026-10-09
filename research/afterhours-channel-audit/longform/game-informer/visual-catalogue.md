# Visual catalogue: "Everything Game Informer Just Revealed About GTA 6" (Affan Afterhours)

6:22.20 · 1920x1080 · 59.94 fps · uploaded 2026-09-30 · 287 views · master `raw/game-informer.mov`.
Read frame by frame on 2026-10-08. Layer identities come from the creator's timeline (`prproj/Sequence-16.summary.txt`,
`agg-game-informer.txt`) and the overlay brief (`projects/gta6-hurricanes/BRIEF.md`, `RUN.md`, `overlays/build.py`). This file says
**how it looks** and **what is said over it**. Timecodes are program time in the master. *Looks like* marks an inference.

**Evidence in `frames/`:** `sheet_001…026.jpg` (2 fps contact sheets, 15 s each, timecode burnt top-left). `f_<m>m<ss.ss>_<label>.jpg`
(195 full-res stills: every slot's in / mid / out and the face frame just before it, every cut zoom, both stretch gags, the cold open,
the last 15 s and the fade). `keyframes_grid_001…022.jpg` (the same stills, 9 per page, labelled). `corner-detail.png` (bottom row =
this video's rounded corners; top row = PC Release for comparison).

**Measurement notes.** Face size = OpenCV face box (forehead to chin) as % of frame height. Inset bounds = edge scan (exact on this
video: every slot measures 144,81 → 1776,999 = **85.0 % × 85.0 %**). Matte colours = the mean and the brightest-10 % mean of the
pixels outside the inset and its shadow, at the slot's in / mid / out frames.

---

## 1. Face framing, set, and how each zoom level reads

**The set (night, dark, saturated).**
- **Wall:** saturated **LED green `#78A44B`** behind the right shoulder (`#6B933F` mid-right), warm olive `#948856` in the upper-left
  corner where a pink/purple wash spills down. Much darker and greener than PC Release's pale sage.
- **Neon:** the same `SKOOL` neon (S blue/pink, K orange, OO cyan/blue with white cores, L orange), top centre-left, **cut by the
  top of frame even at 100 %** (camera is closer/lower than in PC Release). A small pink-lit square box frame upper left.
- **Props:** brown leather armchair behind him; a leafy plant and a dark cabinet frame-right with a **green-LED-lit bottle/vase**;
  the red-grille mic on a stand, lower centre (red-lit grille, black spider mount).
- **Wardrobe:** black crew-neck sweater (`#0E0906`), watch on the left wrist.
- **Light:** warm orange key on the face, everything else falls off. Face shots average ~0.24 luma (62/255); the master's mean is 0.28.

**Framing at 100 %:** medium close-up; face box **31–34 % of frame height**, face centre x ≈ 55 %, y ≈ 36–41 % (slightly right of
centre and higher than PC Release). Chair wings both sides, plant right, mic bottom centre.

| scale | face box (% of frame h) | what it looks like | frames |
|---|---|---|---|
| 100 | 31–34 % | MCU, neon cut at the top, chair wings, mic whole | `f_0m03.40`, `f_2m00.00`, `f_6m15.00` |
| 110 | ~36 % | marginally closer; reads as a jolt more than a framing change | `f_0m09.50`, `f_1m16.80` |
| 124–135 | 37–40 % | CU, neon reduced to colour at the top edge | `f_2m57.00`, `f_3m26.80`, `f_3m38.00` |
| 139–149 | 45–48 % | tight CU, repositioned left (149 at 5:26.6 is shifted to x 0.435) | `f_4m11.80`, `f_5m27.50` |
| 161 | ~46 % (pushed down to y 0.563) | forehead cropped, face low in frame | `f_5m58.50` |
| 203 | ~67 % | big CU (repositioned x 0.354 so the face is centred): brows to beard, clasped hands bottom right | `f_1m32.40` |

Cut zooms: **23 = 3.6/min, median 121 %** (103–203), held ~1.6 s, 15 of them inside nests. The probe's "x1.7–1.9 steps" at 2:30.8–2:33.8,
4:52 and 5:02.8 are **false positives** (hands moving); the frames show plain 100 % framing (`f_2m30.85`, `f_2m32.05`, `f_4m52.10`).
There are **no slow-downs**: no clip has a speed change, and the frame-duplicate check at the report's "slowed stretches" (3:41, 3:52,
4:30, 4:43) finds 0 held frames (PC Release's 0.8x clips show them).

---

## 2. Cold open, beat by beat (0:00–0:44)

| time | picture | said |
|---|---|---|
| 0:00.00–0:03.20 | **C01, the first frame is an overlay**: the Game Informer article page (nav bar, hero image of a seaplane over a stormy turquoise Vice City bay with lightning, blue **EXCLUSIVE** tag, headline *"Exclusive: Grand Theft Auto VI Features Tropical Storms And Hurricanes"*, byline "by Marcus Stewart on Sep 29, 2026 at 12:17 PM"). 85 % inset, rounded corners, on a **magenta/plum** matte; the page slowly pushes in *inside* the fixed frame (the nav bar crops off by 3.1 s). Pop SFX on the entrance. | "So Game Informer's just dropped their big GTA 6 articles" |
| 0:03.20–0:06.12 | Face, 100→105 push | "and it's official that GTA 6 will have hurricanes." |
| 0:06.12–0:07.72 | **C02: four GI screenshots, 0.4 s each, a pop on each**, held dead still: seaplane over the bay → neon night skyline (GAMEINFORMER watermark) → packed beach, US flag, sunbathing couple → golden wetland with heron and deer. **Teal/navy** matte. | "Everyone's posting the screenshots," |
| 0:07.72–0:20.54 | Face nest 110 (12.8 s, 7 jump cuts), hands steepled/explaining; 110 snaps at 0:09.3 and 0:18.5 | "nobody's asking the only question that matters. When a hurricane hits in the middle of Vice City, will it actually do anything? Rockstar hasn't said anything about it, but their games have kind of spoken about this for the past 20 years." |
| 0:20.54–0:27.76 | **C03, the roadmap montage** (plum/navy matte with a rust glow): Game Informer cover art (Jason and Lucia in a bullet-holed pink convertible, the GAMEINFORMER masthead cut off at the top) 3.0 s → San Andreas Santa Maria pier at sunset 1.0 s → GTA IV Coney-style rollercoaster with a blue convertible 1.0 s → GTA V orange supercar on a rain-soaked road 1.15 s → RDR2 rider in a dark rainy forest 1.1 s. A pop on every switch. | "In this video: everything Game Informer actually confirmed, the weather tricks Rockstar has been quietly putting in their games for years that most people never noticed," |
| 0:27.76–0:31.50 | Face, 100→105 push, a wincing grin | "the animal number that is actually smaller than Red Dead 2, and one Vice City detail from 2002" |
| 0:31.50–0:38.64 | **C04**: Vice City Definitive Edition, Tommy walking a rainy sidewalk (Parsons/HOTEL signs), wanted stars top-right and a radar arc bottom-left left in. Indigo matte with teal. | "that tells you Rockstar has been planning storms in this exact city for 24 years. Take a round for that one." |
| 0:38.64–0:44.19 | Face nest 105, then the **145 % snap repositioned down** at 0:39.77 (face fills the lower frame) | "So let's get the facts straight first, because the internet is already making stuff up." |

---

## 3. Overlay master table and the matte palette

**The treatment, identical on all 24 slots:**
- **Fixed inset, exactly 85.0 % of the frame** (1632×918 at 144,81), **rounded corners ~22 px**, a baked soft shadow offset down-right
  (16/24 px, ~70 % alpha; on the dark mattes it reads only as a slightly darker rim). The inset itself never moves or scales.
- **Motion lives inside and behind it:** stills push in slowly inside the frame (C01, C16; C02 deliberately dead still); video plays at
  normal speed; behind it a **slot-specific animated colour matte** (V3) drifts — a slow gradient with grain whose bright spot wanders
  (C01's glow centroid moves from the top centre to the lower middle over 3 s).
- **Trailer letterbox bars are left in** inside the inset (C05, C06, C14, C19); some HUD bits stay (C04 stars and radar arc, C13/C18
  RDR2 core icons and radar arc, C22 health/stars); C08's speedometer and minimap are cropped out.
- **A pop SFX on every entrance and every picture switch inside a slot** (44 = 24 entrances + 20 switches); exits back to the face are
  silent. (Placed at −6 dB clip / −12 dB gain; in a high-pass onset scan of the master they do not stand out from speech sibilance,
  i.e. they sit low.)
- **Entrances/exits are hard cuts.** The matte and the inset appear together on the cut and leave together.

**Matte palette, slot by slot** (measured on the master; "built" = the intended triple in `overlays/build.py`). The shipped mattes are
much darker than the built hex — dark jewel tones, mean luma 2–20 %:

| slot | in–out | dur | what's shown | matte as seen: mean · brightest (where) | built (c0 · c1 · c2, type) | said over it |
|---|---|---|---|---|---|---|
| C01 | 0:00.00–0:03.20 | 3.2 | GI article screenshot (§ 2), slow push | **magenta-plum** `#520E37` · `#861C5C` (top → lower middle) | 3a0a5a · 0b1f4a · b0287a radial | "Game Informer's just dropped their big GTA 6 articles" |
| C02 | 0:06.12–0:07.72 | 1.6 | 4 GI stills × 0.4 s, dead still | **navy-teal** `#081C26` · `#064442` (top) | 12305a · 5a0f4a · 0d5a5a linear | "Everyone's posting the screenshots" |
| C03 | 0:20.54–0:27.76 | 7.2 | GI cover art → SA pier → GTA IV coaster → GTA V rain → RDR2 rain | **plum/navy, rust corner** `#1E0714` · `#430F1D` (rust `#220707` right at 0:24) | 4a0c3c · 102a52 · 7a2a10 spiral | "everything Game Informer actually confirmed, the weather tricks…" |
| C04 | 0:31.50–0:38.64 | 7.1 | VC DE: Tommy walking in rain | **indigo with teal top** `#0E0D2A` · `#0E2D43` | 6a0b55 · 0b4a5a · 2a0b6a radial | "one Vice City detail from 2002… planning storms… for 24 years" |
| C05 | 0:44.19–0:50.52 | 6.3 | trailer pier sunset (letterboxed) → EL sunny highway drive → pink-sky causeway → night skyline | **deep violet-indigo** `#090623` · `#190F46` | 0b1a3a · 0d4a5a · 2a1060 linear | "Leonida gets hurricanes and tropical storms, heavy rain, strong winds, dark clouds, thunder, lightning" |
| C06 | 0:53.69–0:57.74 | 4.1 | EL red van through a toll plaza (sunny) → night pickup in a storm, sparks (letterboxed) | **near-black navy, faint olive-gold** `#040716` · `#272518` | 5a3a08 · 0b2a4a · 12123a radial | "sunny in one part of the map, but the other part is like drenched" |
| C07 | 1:09.04–1:12.19 | 3.2 | EL man in a green back room, respirator round his neck → Lucia ("DON'T TRIP" jacket) entering a store, wanted stars → EL sunny highway | **oxblood/rust** `#250703` · `#3F0C06` | 5a1408 · 3a0a2a · 6a3a08 linear | "whether they affect missions or driving physics" |
| C08 | 1:22.88–1:25.82 | 2.9 | GTA V orange supercar sliding on a wet road (HUD cropped) | **dark slate-teal** `#04141A` · `#0B2531` | 1a2a3a · 0b3a4a · 2a2a3a radial | "in GTA 5 when it rains the roads get slippery" |
| C09 | 1:34.11–1:40.05 | 5.9 | GTA V prologue cutscene (four men in a snowy car) → snow-road drive, minimap | **steel blue-grey** `#111E2A` · `#2B3A48` | 2a4a6a · 0b1a3a · 5a6a7a linear | "And in the snow, at the beginning of GTA 6 in the prologue, it's even worse" (he says 6; the footage is GTA 5's prologue) |
| C10 | 2:04.06–2:06.99 | 2.9 | GTA V rainy night street, telephone pole with "LOST CAT" flyers | **deep forest-teal** `#01160F` · `#06261F` | 0b2a3a · 1a1a3a · 0b3a2a radial | "So in GTA 5, when it rains, pedestrians run for cover." |
| C11 | 2:11.10–2:16.49 | 5.4 | **Rob Nelson quote card** (§ 5) | **dark red left, navy-violet right** `#160312` · `#240C31` (red `#270001` left) | 6a0b14 · 0b1a6a · 2a0a2a linear | "In GTA 6, the police only come after you if someone witnesses the crime or an alarm goes off." |
| C12 | 2:34.07–2:37.34 | 3.3 | RDR2 blizzard on a mountainside, a tiny rider and horse | **dark amber-brown** `#1E0F02` · `#472609` (top) | 4a2a0b · 6a3a14 · 2a1a0b radial | "In Red Dead 2, if you wore light clothes in the snow, your health drained." |
| C13 | 2:41.59–2:44.85 | 3.3 | RDR2 rider in an orange dust storm, radar arc bottom-left | **ochre/mustard brown** `#2F1B02` · `#5A4410` (top) | 6a3a08 · 4a1a08 · 7a5a1a linear | "Snowstorms, dust storms made it hard for you to see." |
| C14 | 2:46.98–2:51.79 | 4.8 | EL Lucia on a pink bed with her phone → trailer Jason bench-pressing at a beach gym (letterboxed) → night street fight → Lucia kickboxing in a cage (letterboxed) | **dark plum** `#16010D` · `#2A071D` (centre; barely moves) | 6a1a3a · 7a3a2a · 3a0b2a radial | "You sleep, you eat, you go to the gym, your body changes based on how much you exercise." |
| C15 | 3:01.75–3:03.32 | 1.6 | **Animal-number card** (§ 5), counting up | **deep green** `#072003` · `#183F05` (top) | 0b3a14 · 2a5a0b · 0b2a2a spiral | "next up, we've got the animal number: over 170 animal species" |
| C16 | 3:18.25–3:20.42 | 2.2 | NME article screenshot: *"'Grand Theft Auto 6' is the most expensive video game ever made, according to analysts"*, standfirst "The team was given 'unlimited financial resources'", by Ali Shutler, key art below; slow push | **crimson-wine** `#1F010C` · `#43061E` (top) | 3a0b0b · 0b0b3a · 5a0b2a linear | "This is the most expensive game ever made," |
| C17 | 3:31.24–3:35.50 | 4.3 | trailer airboat in golden swamp haze → flamingo flock over a marsh → GI wetland screenshot (heron, deer, watermark) | **moss green** `#0B2104` · `#17370E` | 0b3a1a · 0b4a4a · 2a4a0b radial | "will these animals actually attack you and stuff? I think the big ones at least will." |
| C18 | 4:05.01–4:08.48 | 3.5 | RDR2 rider in a grey rainy meadow → night sky, a single lightning bolt | **dark bronze** `#201404` · `#422B0A` (top) | 3a2a0b · 1a1a2a · 5a3a14 linear | "to be fair to Rockstar, the weather can be purely cosmetic" |
| C19 | 4:38.38–4:42.92 | 4.5 | Trailer 2: grey-bearded man in a palm-print shirt by a pickup → shirtless man in cap and shades on a porch → view from the porch over a puddled yard and the pickup (all letterboxed) | **deep violet with magenta** `#0F011E` · `#2A0631`–`#36062D` | 6a2a0b · 5a0b3a · 2a0b4a radial | "Jason is a retired, or like used to be a Navy SEAL" |
| C20 | 4:50.14–4:56.16 | 6.0 | Trailer 1 robbery: bandana-masked Lucia and Jason in a liquor store (Pißwasser sign, $14.99), low-angle close-ups | **maroon-red** (brightest slot) `#2D070F`–`#340A0B` · `#5C121E` | 7a1a2a · 6a3a0b · 2a0b3a linear | "because she was robbing a store alone in the extended look" |
| C21 | 5:08.84–5:12.15 | 3.3 | original Vice City at night in heavy rain, green neon Ocean Drive hotels | **indigo with violet** `#080520` · `#290839` | 0b5a5a · 5a0b5a · 14144a radial | "there was actually interactions with the weather" |
| C22 | 5:14.93–5:21.20 | 6.3 | VC DE heavy-rain drive: red car, then a yellow taxi alongside; health/stars top-right | **magenta drifting to blue** `#260223` → `#0E0C2E` · `#4B0638` / `#151A50` | 6a0b4a · 0b3a6a · 3a0b6a spiral | "the cars would turn on their hazard lights and everybody would stop following the signals" |
| C23 | 5:44.48–5:47.91 | 3.4 | EL/trailer: Lucia skydiving over the Vice City canals | **deep violet, warm orange glow at the exit** `#110324` · `#1C0643` (orange `#501B18`) | 7a0b4a · 7a3a0b · 2a0b5a radial | "not even a month and a half to this game" |
| C24 | 6:01.53–6:09.05 | 7.5 | his own **Hot Coffee** video (bedroom, kid at a glowing CRT, Christmas lights; chapter title "3 / THE FILE NAMES") → its CRT card "SAN ANDREAS · PC / RELEASES IN 3 DAYS▌" (monospace, a pixel tricolour flag) → his **Wolverine** video (Logan vs red ninjas, sparks, burned-in subtitles) | **olive/orange/blue multi** `#201B09`–`#251808` · `#3C3C04` / `#532802` | 7a2a08 · 0b2a6a · 4a5a0b linear | "I tried to make a GTA San Andreas Hot Coffee mod — that flopped. I tried to make a Wolverine video — that flopped." |

**The palette logic** (*looks like*): the matte takes the colour of what the slot shows — green for animals/wetlands (C15, C17), amber
and ochre for Red Dead snow and dust (C12, C13, C18), red/oxblood for robberies and crime (C07, C11, C20), steel blue/teal for rain and
snow (C08–C10), violet/magenta for Vice City nights and trailer shots (C04, C19, C21–C23). No two consecutive slots share a hue.

**Totals:** 24 slots, 23 % of runtime, median 3.4 s, 3.8/min. Longest off-face run 7.5 s (C24). Longest face run 1:40.05–2:04.06
(24.0 s, one nest with a single 103 % nudge at 1:45.6 and a scale reset at 2:01.25 under a **dab** — he throws his arm up and buries
his face in the elbow — on "The next one is the one I actually think matters most").

---

## 4. The creator's own additions

| time | what | how it looks | the line under it |
|---|---|---|---|
| 0:39.77–0:41.80 | **145 % repositioned snap** | face pushed down and filling the lower frame, neon gone | "So let's get the facts straight first" |
| 1:31.91–1:32.89 | **203 % snap**, repositioned | big CU, wide eyes, hands clasped (the biggest zoom of the video) | "blamed it on yourself" |
| 3:57.82–3:59.27 | **stretch gag, Scale Width 446 %** | the face smeared into a wide pancake, `SKOOL` stretched across the top, the mic a wide red band | on the long, trailing "**ohhh**…" of the hiking joke ("Jason and Lucia can go on dates like hiking. Oh, that's gonna be interesting. So you can… oh… what happens after hiking") |
| 4:19.08–4:19.94 | **139 % snap** | grinning CU | "I don't know why I did that" (after a goofy jazz-hands flourish at 4:17.5) |
| 4:21.83–4:22.25 | **stretch gag, Scale Width 443 %**, 0.4 s | same pancake, a hand flapping at the left edge | "but" — a flash between the self-aware aside and "one more thing I forgot to mention" |
| 4:22.3–4:30.5 | no edit treatment: a **real facepalm** on camera | head in hand, then palm over the eyes, eyes off-camera | "where was the tweet? God damn it. Oh my God, I lost it." (then a 123 % snap at 4:30.5) |
| 5:26.56–5:29.66 | **149 % snap**, repositioned left | pained CU | "fancy schmancy weather stuff" |
| 5:58.19–6:00.11 | **161 %**, pushed down (forehead cut) | face low in a tight frame, hands thrown up at the edges | "because I don't know what to make videos on" |
| every cut zoom | **music dropout** (A2 razored out under all 22 cut-zoom ranges) | — (audio) | — |

No memes, no glitch inserts, no cricket, no SUBSCRIBE bug, no slow-downs in this video.

---

## 5. Cards: palette and type

Both built cards follow the poster colour code (cream + hot pink), set in **Inter** (Black / Bold), not a condensed face:

- **C11 Rob Nelson quote card (2:11.1–2:16.5).** Background: a Higgsfield-made Vice City boulevard at night in the rain (pink/cyan
  neon reflections on wet asphalt, palms, a lifeguard tower, a dark car), un-blurred, darkened. Text block upper left, left-aligned:
  kicker **ROB NELSON · CO-STUDIO HEAD, ROCKSTAR NORTH** in tiny pink caps; the quote in **cream `#F6F1DD` Inter Bold, sentence case,
  curly quotes**, four lines: *"The Wanted system in GTA 6 requires / that someone **witness** the crime, / or an **alarm** needs to be set
  off / for it to be reported to the law."* with **witness** and **alarm** in **pink `#F43293`**; a tiny credit "speaking to IGN, August
  2026". Static (no type animation).
- **C15 animal-number card (3:01.75–3:03.32).** Background: the GI wetland screenshot, heavily **blurred and darkened** (heron and
  deer as soft shapes, GAMEINFORMER watermark ghosting bottom right). Centred: kicker **THE ANIMAL NUMBER** (tiny pink caps); a huge
  **cream Inter Black numeral counting up** — 24 (3:01.8) → 127 (3:02.1) → 168 (3:02.5) → 170 (3:02.6) → **170+** (3:03.2), eased so it
  slows near the end; **ANIMAL SPECIES** in cream bold caps beneath.
- **Found type, left as found:** the GI article (black Inter-like headline on white, blue EXCLUSIVE tag), the NME article (black
  grotesque headline, red byline), the Hot Coffee video's own "3 / THE FILE NAMES" chapter type and CRT monospace card, the Wolverine
  subtitles.

---

## 6. Ending (6:09–6:22.2)

After C24 (his two flopped videos) the last face run is one nest, 6:09.05–6:22.20, 100→110 over 13 s, no cut zooms, eyes mostly down
then to the lens: "so I'm just waiting on GTA's news… let me know what type of videos you guys would like on the channel… that's pretty
much it, I'll catch you guys inside the next one." On "next one" he gives a **thumbs-up** (6:21.6) and the picture **fades to black
over the last ~0.5 s** (luma 61 at 6:21.4 → 32 at 6:21.7 → 0 at 6:22.0; the nest's opacity keyframe 100→0). Music (ES "Brooklyn –
Dyalla") runs under it, dropped a further 3 dB from 6:11.6. No end card, no SUBSCRIBE bug.

---

## 7. What this video adds to / contradicts in `presets/youtube/affan-afterhours-facecam/README.md`

**Contradicts**
- **"Nothing is ever an inset… game footage always full-frame."** All 24 inserts are 85 % insets with rounded corners on coloured mattes
  (the creator's own rule in the Tella brief: "edges bleed, never full-frame"). Footage is also partly **de-HUDed** and trailer
  **letterbox bars are kept** inside the inset.
- **"Opens on the face… no title card."** The first frame is the Game Informer article (an overlay), and the first 28 s carry two
  roadmap montages.
- **"End on the face, cold."** It ends on the face, but with a thumbs-up and a **0.5 s fade to black**.
- **The comedy slow-down (1–2 per video).** **None here**; the jokes are carried by cut zooms, two stretch gags and a real on-camera
  facepalm.
- **Card type "heavy condensed grotesque".** The two built cards use **Inter** (Black/Bold), sentence-case for the quote, all caps for
  the number card. The colour code (cream `#F6F1DD` + hot pink `#F43293` accent words) matches the README.

**Adds**
- **Per-slot matte palette** keyed to the slot's subject (green = animals, amber = Red Dead weather, red = robbery, steel/teal = rain,
  violet = Vice City night). Dark jewel tones, ~2–20 % luma, slowly drifting, never the same hue twice in a row.
- **Pop SFX on every overlay entrance and every switch inside a slot** (44), silent exits — the README has no SFX layer.
- **Music drops out under every cut zoom** (22 ranges).
- **Quick-flash stills**: four article screenshots at 0.4 s each with a pop each (C02), and a 1 s-per-game montage (C03).
- **The count-up number card** (C15): a stat that animates to its value on a blurred plate.
- **The self-callback as footage**: his own flopped videos (Hot Coffee, Wolverine) cut in raw, inside the same inset/matte.
- **Calmer face grammar than PC Release**: cut zooms 3.6/min (median 121 %), long slow nests (0.4–1.2 %/s over 8–24 s), 25 face runs,
  the face on screen 77 % of the time.
