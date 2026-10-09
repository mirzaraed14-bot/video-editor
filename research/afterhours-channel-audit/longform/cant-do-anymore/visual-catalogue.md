# Visual catalogue — "GTA 5 vs GTA 6: Everything You CAN'T Do Anymore"

Frame-by-frame dissection of the editing style. Source: the YouTube 1080p59.94 H.264 download
`raw/cant-do-anymore.mp4`, 1920×1080, 26,349 frames, **7:19.65 (439.65 s)**. Uploaded 2026-09-12;
17.7k views, 294 comments. It is the channel's 3rd-best long-form, and the README lists it as the reference the
creator dropped.

**Evidence (all in this folder):**

- `frames/sheet_001–030.jpg`: the whole video at 2 fps, 15 s per sheet. All 30 were read.
- `frames/full/*.jpg`: about 85 full-resolution single frames.
- `frames/edges/*.jpg|png`: boundary tiles at every frame (1/60 s) or at 10–20 fps around each graphic
  boundary, plus 2×2 mosaics of the key frames (`m1`–`m13`) and big crops of every text card (`big_*`).
- From the measurement job: `probe/`, `report.md`, `zoom.json`, `slowmo.json`, `audio.json` and
  `transcript/words.json`. All quotes below come from `words.json`.
- My own measurements: a per-frame difference trace (mean abs diff at 96×54), scale matching across every
  face-run event, and background-only scale matching for gradual moves. The scripts live in the session
  scratchpad, not in this folder.

Anything marked **"looks like"** is an inference.

> **Probe caveat, important for anyone reading `report.md`.** The probe reports **face 78 %**. That figure is wrong
> for this video. The face detector fires on the illustrated Jason faces and on the GTA characters, so 12 AI
> illustrations and several stills were counted as "face". Read frame by frame, the face is on screen
> **≈57 % (250 s)** and overlays take **≈43 % (189 s)**. The probe also lists a "zoom burst" at 3:55–4:05. That
> shot is really a slow pull-out, and the box changes come from his hands covering his face. Its zooms at
> 6:59–7:03 are inside game footage. The hard-cut rate, word rate, chopped-word list and slow-down detector are
> sound and are quoted as measured.

---

## 0. The numbers at a glance

| | this video (17.7k) | how measured |
|---|---|---|
| length | 7:19.65 | ffprobe |
| hard cuts | **175 = 23.9/min** (cold open 25/min; by minute 25 · 31 · 24 · 18 · 25 · 18 · 22 · 36.6) | report.md |
| visible changes | 32.1/min (cuts 23.9 + zoom steps 5.0 + reframes 4.4) | report.md |
| face on screen | **≈57 %**, in 37 runs, median run 6.0 s, longest 23.0 s (2:22.09–2:45.06) | frame-by-frame (the probe's 78 % is wrong, see above) |
| overlays | **47 content overlays + 3 colour-bar stingers**, ≈43 % of runtime, 35 runs = **4.8 runs/min**, median run 5.1 s | frame-by-frame |
| text-bearing graphics | 9: 4 inset quote cards, 4 full-frame illustrated text cards, 1 plain-text caption. That is 1.2/min. One more inset has no text: the radar blow-up | frame-by-frame |
| AI-style illustrations | **12** (8 with no text + the 4 text cards), 64 s = **15 % of runtime** | frame-by-frame |
| cut zooms in (face) | **38 = 5.2/min of runtime** (9.1 per minute of face). Median **×1.21** (p25–p75 1.16–1.29), max ×1.40; median hold 1.36 s. 30 are pure crop snaps inside a take, 8 ride a jump cut. Cut zooms out: 19 | scale-matched at every event |
| gradual push | **none**. Shots are static or **pull out** at 1.0–1.5 %/s. The report gives −0.38 %/s | background-only scale matching |
| words/min | 205.3; pauses ≥ 1 s: 1 | report.md |
| chopped words at cuts | 4 (2:45.60, 2:47.60, 6:42.20, 7:01.20) | report.md |
| slowed audio | 1 (5:52.40, "millions", pitch ×0.82) plus 4 punch-and-slow face beats (§5) | audio.json + frame cadence |
| mean luma | 0.418. Brighter than Fuel System (0.337) | probe |
| first / last shot | face / face, no fade either end | per-frame luma |

---

## 1. The face shot

### Framing

One camera and one position, with **two lighting setups** (see "The set"). Everything else is done with crop
steps in post. Measured from the 1,187 face-detector samples that fall inside true face runs. The box runs brow
to chin and is given as a fraction of the 1080 px height:

| | face-box height | px |
|---|---|---|
| loosest 10 % | 0.349 | 377 |
| **median** | **0.382** | **413** |
| tightest 10 % | 0.463 | 500 |
| maximum | 0.608 (4:55.80, top of the staircase zoom) | 657 |

- **Base shot = medium.** Head and shoulders, with the chest cut by the bottom edge. The leather chair back
  fills the lower-left third. The "skool" neon sits top-centre-right, overlapping or just right of his head. It is
  usually cropped at the top edge.
- **Face centre x = 0.535.** He sits slightly camera-right of centre. **Face centre y = 0.414; face-box top
  y = 0.218.** About 235 px of wall and neon sit above the brow. The pink and beige halves of the video measure
  the same (median 0.381 vs 0.385), so the camera never moved between sessions.
- **Zoom tightness levels:**
  - **Base** ×1.0.
  - **Standard cut zoom** ×1.16–1.29 (median ×1.21). Report zoom-level share: 1.0–1.2 → 863 samples,
    1.2–1.4 → 209, 1.4–1.6 → 39, 1.6–1.8 → 20.
  - **Biggest single steps** ×1.40, at 1:05.22 and 2:29.15.
  - **Tightest level reached** ≈×1.6–1.65, on the staircase at 4:55.75: ×1.28 → ×1.12 → ×1.15.
  - There is no ×2 extreme close-up anywhere. The tightest shots still show the neon and the shoulders.
- **No gradual push-in.** A clean 3.3 s shot (1:24.3 → 1:27.6) matches at exactly ×1.000 on the background. The
  long shots move the *other* way:
  - The first shot opens ≈12 % tight and eases out by 0:01.7 (probe face box −12.5 %).
  - The 12.6 s shot 3:53.12–4:05.71 pulls back continuously: ×0.985, ×0.970, ×0.970, ×0.975, ×0.980, ×0.990
    per 2 s. That is −1.5 %/s, easing to −0.45 %/s at the end, so it looks like an eased keyframe. It starts
    about ×1.3 tighter than where it ends. The probe misread this shot as a "zoom burst".
  - 7:05.1–7:11.1 pulls out at a steady **−1.5 %/s**: ×0.970 for each of three 2 s steps, match error ≤ 6.
    The report's −0.38 %/s is the whole-video average.
  - **The slow move in this video is a pull-out, not a push-in.**
- **One mirrored shot.** At **1:32.21–1:33.33** the frame is flipped horizontally and cropped tight (≈×1.4).
  The neon reads backwards ("looʞs"), on "now. I don't know why people are upset". It looks like a fake second
  angle made by flipping the same take.

### The set (two looks in one video)

**Look A: pink LED, 0:00–5:46.0, plus one pick-up at 5:55.62–5:58.51.**

- **Back wall:** white wall flooded with a **pink/magenta LED**. Lit wall measures `#F5A5CB`–`#FF9AD7` and
  falls to deep magenta toward the bottom of frame.
- **"skool" neon** in lowercase tube letters:
  - `s` pink/cyan, `k` orange-yellow, `o` blue-white, `o` cyan-white, `l` orange-red.
  - It sits behind and right of his head in the headroom band.
- **A white square plaque with a red YouTube play icon** hangs on the wall just left of the neon. It looks like a
  YouTube Silver Play Button. This is new against Fuel System, which had a pink/orange framed print there.
- **Chair:** big brown leather armchair behind him (`#52131C` under the pink light).
- **Frame right:** a dark grey door or wall edge, and a dark sideboard whose top catches red/orange light.
- **Frame left:** a strip of black metal shelving or grille in the wider crops.

**Look B: warm-white, 5:46.0–7:19.65.**

- The LED is off, or white. The wall goes **warm beige** (`#E4AC93` / `#C98B62`) with a dark warm vignette in
  the corners. The neon and plaque are unchanged.
- The cut into Look B is a **whip-blur transition**: 5:45.98–5:46.30, on "Here's the last one".
- **The edit cuts back to a pink take** for one shot, 5:55.62–5:58.51, on "This is the first game that says you
  don't get shit". Two sessions are intercut, and the colour mismatch was left in.

**Lighting:**

- Soft key from camera-front-left.
- Picture is bright: mean luma 0.418, 68 % "bright" samples.
- No dark, moody frames.

### Props and wardrobe (identical in both looks)

- **No microphone in frame.** Fuel System had a red-grille condenser; it is gone here. A **small square wireless
  transmitter** is clipped mid-chest on the t-shirt and shows in every shot. It looks like a DJI Mic.
- **Dark charcoal crew-neck t-shirt**, plain (`#1A0E09`–`#3A3632` depending on the light).
- **Black square-framed glasses with orange/amber lenses**, worn the whole video.
- Black hair and a full dark beard.
- **Black watch with a braided black band** on the left wrist.
- 6:38–6:47 he holds a small **white stick**. It looks like a vape or lip balm, and he gestures with it.
- Body language is constant hand-talking: steepled fingers, a phone mime at the ear (3:46.4, 5:12–5:13.5), and
  a "flexing" pose (7:05).

### Bugs, lower-thirds, captions

- **None.** There is no logo, watermark, lower-third, name strap, burned-in caption or progress bar.
- **There is no subscribe animation anywhere.** All 30 sheets were checked. This is a difference from Fuel
  System, which showed one twice.
- Text appears only on the 9 text graphics listed in §3, and inside game HUDs.

---

## 2. Cold open (0:00 – 1:06.90)

The first 30 seconds, then the rest of the intro through the first colour-bar stinger. **No title card, no logo
sting, no channel branding.** The first insert lands at 3.37 s. The intro promises "one of 10 things", and item
1 starts at 1:06.90 straight after a TV colour-bar glitch. Cut rate in minute 1 is 25/min.

| # | in – out | dur | on screen | what's said |
|---|---|---|---|---|
| 1 | 0:00.00 – 0:03.37 | 3.4 s | **Face, Look A.** Opens ≈12 % tight and eases out by ~1.7 s. Hands pressed together, then chopping. | "In GTA 6, you can't see the cops on the mini-map." |
| 2 | 0:03.37 – 0:07.24 | 3.9 s | **INSET radar card.** A GTA V minimap blown up: black radar, red blips, white player arrow, "N", green/blue/yellow bar, blimp + "F" icon. Thin dark-grey frame, square corners, ≈80 % of frame. Sits over a **blurred plate of the GTA V red-car clip that follows**. Card grows ×1.04. Hard cut in and out (7.224 card → 7.241 face). | "The little blue dots with the vision cones you've been dodging since 2013," *(the radar shows red dots and no cones)* |
| 3 | 0:07.24 – 0:09.73 | 2.5 s | **Face.** At **0:08.54 snaps ×1.26** with a slight slow-down (frame holds every 7th frame, ≈0.85×). | "Rockstar deleted them on purpose." |
| 4 | 0:09.73 – 0:15.15 | 5.4 s | **GTA V gameplay**, full frame, HUD intact: minimap, white stars and cash. A red sports car with a smashed rear window, chase-cam through a military base that looks like Fort Zancudo. Three shots (cuts 0:12.30, 0:12.76). Real speed, 60 fps source. | "The GTA 5 Escape was a game of cones. Blue dots, little triangles of vision," |
| 5 | 0:15.15 – 0:23.09 | 7.9 s | **Face.** 0:16.82 snap ×1.18 ("boom, you're done"), 0:17.45 out, 0:19.52 jump cut to hands-at-mouth. | "stay dark for 30 seconds, boom, you're done. So it wasn't close to real life. Rob Nelson, the man who runs Rockstar North, said it out loud," |
| 6 | 0:23.09 – 0:28.93 | 5.8 s | **ILLUSTRATED CARD "FOCUS."**, full frame (§3c). Hard cut in (23.073 face → 23.090 card). | "you can't just play the game and avoid the little cones anymore. This time, you have to use focus." |
| 7 | 0:28.93 – 0:30.40 | 1.5 s | **Face.** | "that's the replacement" |
| 8 | 0:30.40 – 0:34.28 | 3.9 s | **INSET QUOTE CARD, Rob Nelson #1** (§3b). Hard cut out (34.268 card → 34.284 face). | "his words depending on the wanted level you have to think more" |
| 9 | 0:34.28 – 0:42.88 | 8.6 s | **Face.** 0:37.49 jump + zoom ×1.26 ("and we can't use it"), 0:38.72 out, 0:40.09 snap ×1.28 ("10 things we are going to be discussing"), 0:41.56 out. | "so 12 years of instinct that we have all developed and we can't use it and this is just one of 10 things … because here's the pattern" |
| 10 | 0:42.88 – 0:47.98 | 5.1 s | **SPLIT key art**, full frame. Left: GTA V trio with rifles on an orange sky (official art). Right: Lucia and Jason on a Vice dock, illustrated (looks like fan or AI art). A thin white vertical divider at x ≈ 984. Pulls back ×0.96. | "almost everything that made gta 5 gta 5 the stuff you do without thinking" |
| 11 | 0:47.98 – 0:55.92 | 7.9 s | **Face.** 0:50.52 out step. **0:53.02 snap ×1.28 plus slight slow (≈0.87×)** on "with consequences". **0:54.354–0:54.538: TV COLOUR BARS**, 11 frames of noisy SMPTE-style bars, in the 1.0 s pause after the line. Then face again. | "has a rule attached in gta 6 not new features it's just old habits with consequences / 9" |
| 12 | 0:55.92 – 1:00.96 | 5.0 s | **ILLUSTRATION, no text**, full frame. Jason in a white tank top staring at his phone, a sweat drop on his face, the phone glow lighting it, purple bokeh. Pulls back ×0.94. | "more from mildly annoying to what some people will say this literally changes the whole game." |
| 13 | 1:00.96 – 1:06.72 | 5.8 s | **Face.** 1:01.93 jump cut. **1:05.22 jump + zoom ×1.40** into a take that is visibly **soft**. It looks like he leans inside the focus distance, and the punch magnifies the softness. | "And the last one is why GTA 5 players inside of this comment section are going to be furious." |
| 14 | 1:06.72 – 1:06.90 | 0.18 s | **TV COLOUR BARS**, 11 frames. Marks the start of item 1. | — |
| 15 | 1:06.90 → | | Face; the body begins. | "Tapping X to sprint." |

In the first 30 s, the inserts come at 3.4 s, 9.7 s, 23.1 s and 30.4 s. Of 30 s, 12.7 s is graphics.

---

## 3. Every overlay, in order

### 3a. Master table

"Pulls back" means the image scales *down* across its hold (zoom-out), and "grows" means it scales up. Both are
measured on matched first and last frames. Speed comes from frame-duplicate cadence. In "every other frame
doubled", a 30 fps source at 1× and a 60 fps source at 0.5× cannot be told apart from the picture alone. Every
entrance and exit below is a **hard cut**: a single-frame difference spike of 55–123, with the frames on either side back at plate-motion level. The
exceptions are the three whips listed after the table.

| # | in – out | dur | what | treatment | speed / motion | what's said |
|---|---|---|---|---|---|---|
| 1 | 0:03.37 – 0:07.24 | 3.87 | GTA V radar blown up (red blips, player arrow, health/armour bar) | **inset ≈80 %**, grey frame, square corners, over the blurred GTA V red-car plate | card grows ×1.04; plate plays | "The little blue dots with the vision cones you've been dodging since 2013," |
| 2 | 0:09.73 – 0:15.15 | 5.42 | GTA V: red car with smashed rear window driving through a military base, 3 shots | full frame, sharp, HUD | 1.0× | "The GTA 5 Escape was a game of cones. Blue dots, little triangles of vision," |
| 3 | 0:23.09 – 0:28.93 | 5.84 | **Illustrated text card "FOCUS."** | full frame | static art, pulls back ×0.96 | "…avoid the little cones anymore. This time, you have to use focus." |
| 4 | 0:30.40 – 0:34.28 | 3.88 | **Quote card: Rob Nelson #1** | inset 80 % over the blurred GTA V red-car plate | grows ×1.04 | "his words depending on the wanted level you have to think more" |
| 5 | 0:42.88 – 0:47.98 | 5.10 | Split key art: GTA V trio vs GTA 6 Lucia & Jason | full frame, white divider | pulls back ×0.96 | "almost everything that made gta 5 gta 5 the stuff you do without thinking" |
| — | 0:54.35 – 0:54.54 | 0.18 | **TV colour bars** | full frame | 11 frames | (pause after "consequences") |
| 6 | 0:55.92 – 1:00.96 | 5.04 | Illustration: Jason staring at his phone, sweating | full frame | pulls back ×0.94 | "more from mildly annoying to … changes the whole game." |
| — | 1:06.72 – 1:06.90 | 0.18 | **TV colour bars** | full frame | 11 frames | (between "furious." and "Tapping X") |
| 7 | 1:08.52 – 1:13.29 | 4.77 | GTA V: Michael (grey coat) walks through a pier café's picnic benches and out to a red car at a pump. **Chopped into ~8 jump cuts 0.15–0.5 s apart**, so the walk reads as a fast-forward | full frame, HUD | 1.0× pieces | "Since San Andreas 2004 every GTA player has won by hammering X." |
| 8 | 1:19.28 – 1:24.18 | 4.90 | **Quote card "- FAN"** | inset 80 % over the blurred GTA V red-car plate | grows ×1.05 | "Actual fan quote. It's been tradition to tap since San Andreas. I'm honestly a little disappointed." |
| 9 | 1:36.73 – 1:42.79 | 6.06 | **Quote card "- ROB NELSON / ROCKSTAR"** | inset 80 % over the blurred GTA V street plate | grows ×1.06 | "YouTuber TGG watched Rob play for hours. You scroll stations one at a time, like 2002." |
| 10 | 1:44.52 – 1:47.74 | 3.22 | GTA V radio wheel, night drive (station logos, "Soulwax FM / Daniel Avery / Naive Reception", "Del Perro") | full frame. **The source carries a thin blue→magenta gradient border.** It looks like a clip taken from another channel | near-still; selection hops every ~0.5 s (looks ≈0.2×) | "You open the wheel, you can just skip, skip, skip, choose whatever you want." |
| 11 | 1:56.88 – 1:59.90 | 3.02 | GTA V: black muscle car with white stripes tumbling end over end at an intersection, landing on its wheels ("Power St"), ~3 shots | full frame, HUD | every other frame doubled (≈0.5×) | "nothing. You do quadruple flips and you still land on four wheels." |
| 12 | 1:59.90 – 2:08.11 | 8.21 | **Plain-text caption "ROB NELSON SAYS THE DRIVING…"** over heavily blurred GTA 6 jewellery-robbery footage. The **plate hard-cuts at 2:03.26** to the street/motorbike shot while the text holds | full-frame plate, text centred | text static; plate ≈0.5× | "Rob Nelson says the driving has been completely rebuilt from the ground up. The weightiness and feel of GTA 4 with the accessibility of GTA 5." |
| 13 | 2:16.19 – 2:22.09 | 5.90 | GTA V mega-ramp: a red off-roader with bull horns drops down a giant half-pipe above the city and launches into the sky. 1 internal cut | full frame, HUD | 1.0× | "Whipping cars off of normal ramps and they just start to fly. That's kind of a little unrealistic." |
| 14 | 2:45.06 – 2:48.84 | 3.78 | GTA V: Michael walks to the red car at a gas station, opens the door, gets in and drives off. **4 jump cuts.** Same recording as #7 | full frame, HUD | 1.0× pieces; **voice chopped too** ("GTA" 2:45.60, "yours" 2:47.60) | "GTA 5 you walk up, press triangle, it's yours forever, boom done." |
| 15 | 2:49.99 – 2:55.49 | 5.50 | **Illustrated text card "SCAN it."** | full frame | pulls back ×0.97 | "you have to scan it, a phone app that shows the security level of the car, the tool you need, the tracker." |
| 16 | 3:03.97 – 3:10.09 | 6.12 | **Illustrated text card "CERTAIN SPEED"** | full frame; the top line starts clipped by the frame edge | pulls back ×0.95 | "And if you steal one with a tracker, you have to keep it at certain speed because if you slow down" |
| — | 3:16.45 – 3:16.63 | 0.18 | **TV colour bars** | full frame | 11 frames | (before "for 12 years ladies and gentlemen") |
| 17 | 3:20.67 – 3:24.09 | 3.42 | GTA V weapon-wheel screenshot (Pistol .50, 3/8) on a grey sky | full-frame still | grows ×1.04 | "with each weapon archetype having its own five guns" |
| 18 | 3:24.09 – 3:25.21 | 1.12 | GTA V screenshot: Franklin with an RPG, pink clouds | full-frame still | — | "rocket launcher" |
| 19 | 3:25.21 – 3:25.94 | 0.73 | GTA V screenshot: Trevor firing a minigun at night | full-frame still | — | "minigun" |
| 20 | 3:25.94 – 3:26.72 | 0.78 | GTA V screenshot: Franklin aiming a pistol, close | full-frame still | — | "pistols" |
| 21 | 3:28.84 – 3:33.91 | 5.07 | **Illustrated text card "That doesn't work here."** | full frame | pulls back ×0.95 | "in gta 5 you can pull out a shotgun from nowhere in front of people and they don't react that doesn't work here" |
| 22 | 3:47.76 – 3:53.12 | 5.36 | GTA V: Michael fires a rifle from behind a lattice at Sheriff cruisers on a coast road, 5 stars | full frame, HUD | 1.0× | "You pull L2, the game finds a head for you, you just press R2, repeat until the mission ends." |
| 23 | 4:05.71 – 4:15.00 | 9.29 | GTA 6 gameplay with HUD (pink/blue flashing minimap, 4 stars, heat icons, ammo "25 268"). Looks like preview capture. A man in a grey cap fires a rifle over a car hood; a police pickup flips. ~6 cuts in the last 3 s | full frame, HUD | ≈0.5× | "And the guns apparently have weight now. TGG watched Rob tap firing through a whole rifle shootout. Hold the trigger like it's GTA 5 and you're spraying palm trees." |
| 24 | 4:27.97 – 4:32.04 | 4.07 | GTA 6 trailer: a black Mercedes sedan pulls out; cut ~4:29.5 to a black sedan backing into a garage entrance; the camera drifts to the street | full frame | ≈0.5× | "30 seconds in an alley, and the entire police department develops amnesia." |
| 25 | 4:38.11 – 4:45.77 | 7.66 | Illustration: Jason peeking round a wall at police cruisers on an Art-Deco street | full frame | pulls back ×0.93 | "rob nelson on exactly that we wanted to get past that thing … where you could lose the cops instantaneously and then they forgot about you" |
| 26 | 4:48.42 – 4:50.66 | 2.24 | **HUD blow-up:** four stacked strips, each a 6-star wanted row (2 grey + 4 red; 4 dark + 2 white; 4 grey + 2 outlined ×2) over blurred street crops | full frame | pulls back ×0.97 | "so you have the stars and then you have something called" |
| 27 | 4:50.66 – 4:53.23 | 2.57 | **HUD blow-up:** five maroon heat icons (CCTV, two heads, coat hanger, head, pistol), "13  80", pistol icon, over a blurred white interior. Pixel-soft, so it looks like a crop scaled up hard | full frame | pulls back ×0.97 | "heat icons showing that the police know" |
| 28 | 4:59.32 – 5:00.83 | 1.51 | GTA 6 screenshot (official): Lucia holding up two hangers | full-frame still | pulls back ×0.98 | "change your clothes you have to" |
| 29 | 5:00.83 – 5:02.79 | 1.96 | Photoreal still: Lucia aiming a pistol at Jason on a marina. Looks AI-generated | full-frame still | — | "separate from lucia you have to" |
| 30 | 5:02.79 – 5:05.47 | 2.68 | GTA 6 screenshot: masked Lucia watches a car burn in a parking garage; HUD stars + heat icons top right | full-frame still | — | "burn that car like how we saw in the extended look" |
| 31 | 5:15.15 – 5:17.85 | 2.70 | Photoreal still: Jason, face cut, behind a chain-link fence, police lights. Looks AI-generated | full frame | pulls back ×0.98 | "gta 6 you are a permanent suspect" |
| 32 | 5:19.52 – 5:23.36 | 3.84 | GTA V screenshot: Michael on a balcony over the Los Santos skyline | full frame | pulls back ×0.95 | "the entirety of los santos property was the reward for getting rich" |
| 33 | 5:26.69 – 5:34.03 | 7.34 | Illustration: Jason in a garage with an orange McLaren, a blue Bentley and a grey muscle car; Vice sunset through the door | full frame | pulls back ×0.95 | "you can buy garages, a storage garage for a few thousand bucks, steal a $50,000 car and stash it there." |
| 34 | 5:38.27 – 5:42.46 | 4.19 | GTA 6 trailer frame: Lucia and Jason in bandanas aiming pistols, low angle, sun flare | full frame | **near-frozen** (looks ≈0.1×, reads as a still) | "Because Jason and Lucia … are on the run. They are fugitives." |
| 35 | 5:48.85 – 5:55.62 | 6.77 | Illustration: a man in a suit and sunglasses lying on a bed of cash, champagne bottle, clown heist mask | full frame | pulls back ×0.95 | "Every GTA since 2002 ended in the same way. Complete the story, millions in the bank, looking out of the balcony, you own the whole city." ("millions" is **slowed**, pitch ×0.82) |
| 36 | 6:08.92 – 6:12.92 | 4.00 | Illustration: Jason outside the SUNSET MOTEL holding a few bills, rusty beater car | full frame | pulls back ×0.96 | "So you cannot progress without committing crimes first for a little bit of money." |
| 37 | 6:17.08 – 6:21.10 | 4.02 | Illustration: Jason robbing a convenience store at gunpoint, cash bag, terrified clerk | full frame | pulls back ×0.94 | "until you hit certain cash goals. You have to go rob something to keep going." |
| 38 | 6:24.57 – 6:27.45 | 2.88 | Photoreal still: Jason in a bandana and yellow sunglasses pointing a pistol at the lens in a store ("COLD DRINKS"). Looks like official art | full frame | pulls back ×0.98 | "that can, according to TGG's words, can shatter" |
| 39 | 6:31.34 – 6:34.44 | 3.10 | Illustration: a man in a white suit at a desk behind stacks of cash, LS sunset, plane | full frame | static | "In GTA 5, you are a god with a big fat wallet." |
| 40 | 6:34.44 – 6:38.18 | 3.74 | Illustration: Jason in a Vice apartment, duffel of cash, hand on head | full frame | static | "In GTA 6, you're a rich person with a crime record." |
| 41 | 6:42.22 – 6:44.17 | 1.95 | **Quote card "- TGG / ROCKSTAR"** | inset 80 % over a blurred GTA street plate (grey road, a figure in yellow) | grows ×1.01 | "Does this change what GTA is?" (the voice chops "thinking." at 6:42.20) |
| 42–46 | 6:47.67 – 6:56.52 | 8.85 | **GTA 6 trailer montage, 5 clips:** cave diver (1.61 s), Lucia on a bench press (1.55), a man sprinting down a pier and diving (2.59), binocular POV on a window (1.73), a kayaker (1.37) | full frame | ≈0.5× | "It changes what it can be for people who want to engage with it that way. You still have as much freedom as you had before and every one of these systems steps back if you ignore it" |
| 47 | 6:58.32 – 7:04.94 | 6.62 | GTA 6 trailer: jewellery-store robbery; cut 7:00.55 to a robber in a green MARCUS 69 jersey running out and hopping on a motorbike. **Same footage as the blurred plate under #12** | full frame | ≈0.5× | "crimes do everything like gta 5 style there's just going to be i believe a permanent crime record of you" |

**Three whip-blur transitions between face takes.** These are the only non-cut transitions:

| t | dur | what | what's said across it |
|---|---|---|---|
| 1:53.23 – 1:53.51 | ≈0.28 s (17 frames) | The outgoing take smears and slides sideways with heavy directional blur; the incoming take slides in blurred and settles. Looks like a whip-pan preset | "I don't know why they did this." → "In GTA 5, everyone knows this…": the **driving section** starts |
| 3:46.13 – 3:46.41 | ≈0.28 s | Same whip, landing on him with a phone mimed at his ear | "…that's gonna be in your car." → "What was GTA 5's combat like?": the **aiming section** starts |
| 5:45.98 – 5:46.30 | ≈0.32 s | Same whip, and **the set changes from pink to warm-white across it** | "…you can understand why they did that." → "Here's the last one": the **final section** starts |

### 3b. The inset quote card (one template, used 4×: 0:30.40, 1:19.28, 1:36.73, 6:42.22)

- **Geometry, measured at 1:39.5:**
  - The card is a hard-edged 16:9 rectangle at x 193–1726, y 111–967: **1533×856 px, 79.8 % × 79.3 % of the
    frame**, dead centre.
  - **No tilt.** The top edge sits at y = 111 at x 300, 960 and 1600.
  - **Square outer corners** with a soft dark drop shadow, strongest bottom-right.
  - Inside is a second, **rounded rectangle drawn as a glowing neon tube** in violet-pink (`#A75BD9` core with a
    magenta bloom), inset about 7 % from the card edge.
- **Card art:**
  - A **Vice City sunset gradient**: deep electric blue `#052A9C` top-left → violet `#251252` mid → purple
    `#5B0093` lower-left → hot pink `#E3207E` bottom-right.
  - Black palm-frond silhouettes on the left and right edges.
  - A **city skyline with a setting sun and its reflection on water** along the bottom-right.
- **Plate behind:** GTA V gameplay, **gaussian-blurred to mush** and playing. It is the red-car clip on cards
  #4 and #8, and blurred GTA street shots on #9 and #41. The plate is not darkened.
- **Type:**
  - **Rounded geometric sans, bold, sentence case**, pure **white `#FEFFFA`**. Looks like Poppins Bold or
    Montserrat Bold.
  - **One pink accent phrase**: `#DB35A5` / `#E1196E` / `#D832A6`.
  - Rob Nelson and TGG cards: text **left-aligned**, with a **violet double-quote glyph `“`** (`#9B53D9`) hung
    top-left and a closing `”` after the last word.
  - FAN card: text **centred, no glyphs**.
- **Attribution:** a thin violet hairline rule (`#85439D`), then **"- NAME"** in small bold caps. Below that,
  the Rob/TGG cards carry a tiny letterspaced **"ROCKSTAR"** in dim violet.
- **Copy, exact (line breaks as `/`):**
  - **#4, 0:30.40:** `“ depending / on the / WANTED LEVEL, / you have to / think more ”` · `- ROB NELSON` /
    `ROCKSTAR`. Accent: WANTED LEVEL.
  - **#8, 1:19.28:** `It's been tradition to tap / since SAN ANDREAS, i'm / honestly a little / disappointed` ·
    `- FAN`. Accent: SAN ANDREAS and "- FAN". Note the lowercase "i'm".
  - **#9, 1:36.73:** `“ watched ROB / play for hours, / you scroll stations / one at a time, / like it's 2002. ”` ·
    `- ROB NELSON` / `ROCKSTAR`. Accent: ROB. **Misattributed:** he says "YouTuber TGG watched Rob play for
    hours", so these are TGG's words.
  - **#41, 6:42.22:** `“ does this change / what GTA is? ”` · `- TGG` / `ROCKSTAR`. Accent: GTA. TGG is a
    YouTuber, so the template's "ROCKSTAR" sub-label was left in.
- **In/out:** hard cut both ends.
- **Motion:** the card grows 4–6 % over its hold, ≈1 %/s. Nothing on it animates.
- **The radar inset (#1)** uses the same 80 % geometry and blurred-plate idea, with a GTA HUD element in place
  of the quote art.

### 3c. The four full-frame illustrated text cards

All four share one construction. It differs from both the inset cards above and the Fuel System cards:

> A **full-bleed 16:9 AI-style illustration**: cel-shaded GTA-loading-screen art in the Vice palette, with Jason
> as the protagonist. The **headline typography is baked into the art** (it looks like it was generated with the
> image). There is no plate, no inset, no frame and **no tilt**. It **hard-cuts in at about 104 % and pulls back
> to about 100 %** over the hold, so the first frames clip the outer text. Hard cut out.

The evidence that the type was generated with the image: its glow and colour sit inside the scene lighting,
letterforms are slightly irregular, there are misspellings in the scene signage, and the copy paraphrases the
script rather than matching it.

**#3 · 0:23.09 – 0:28.93 (5.8 s): "FOCUS."**

- **Copy:**
  - `You can't just play the game / and avoid the digital cones anymore.` (small condensed, white)
  - `This time you have to use` (bold condensed, white)
  - `FOCUS.` (huge **pink italic heavy condensed** `#EB429C`, dark drop shadow, a pink swoosh underline)
  - He says "little cones"; the card says "digital cones".
- **Layout:** the text block is left-aligned in the centre-right of the frame. Jason crouches on the left third
  with a **pink targeting reticle circle around his head**.
- **Art:**
  - A rain-soaked neon gas station at dusk, pink/orange sky and palms.
  - A **cop with a flashlight throwing a translucent pink vision cone** across the ground, and a **CCTV camera
    with a red light and a pink cone**. The literal "vision cone" is the joke.
  - A vertical "MOTEL" sign, a "SAME CITY BIGGER OPPORTUNITIES" poster, a "COLD DRINKS COLDER TOMORROW" crate.
- **Motion:** pulls back ×0.96.

**#15 · 2:49.99 – 2:55.49 (5.5 s): "SCAN it."**

- **Copy:** `You have to` / `SCAN it.` / `A phone app that showed the / security level of the car, the tool you
  need, / the TRACKER`
  - "You have to" is cream `#FDFBE1` heavy sans.
  - **"SCAN"** is huge **pink `#ED21B4` extra-bold extended sans**. It looks like Archivo Black or Montserrat
    Black; "it." is cream.
  - The body is cream condensed bold, with **"TRACKER" in pink**.
  - He says "shows"; the card says "showed".
- **Layout:** headline top-centre-right. Jason in a blue palm-print shirt holds a phone ("SCANNING…") on the
  left. A **grey muscle car with a pink scan-grid and corner brackets** sits centre.
- **UI panel:** on the right, glowing pink, with a car outline, **SECURITY LEVEL** (a segmented pink bar),
  **TOOL YOU NEED** (wrench + device) and **TRACKER** (map pin + puck with signal arcs). A hairline connects the
  panel to the car.
- **Setting:** a pink "OCEAN" neon on the right, Vice sunset street.
- **Motion:** pulls back ×0.97.

**#16 · 3:03.97 – 3:10.09 (6.1 s): "CERTAIN SPEED"**

- **Copy:** `AND IF YOU STEAL ONE / WITH A TRACKER, / YOU HAVE TO KEEP IT AT A / CERTAIN SPEED`
  - Heavy condensed caps with slightly rough, brushy edges. It looks like a comic/brush condensed face.
  - Cream `#F2ECDE`. **Pink `#EB2BAA` on "TRACKER" and "CERTAIN SPEED".**
- **Layout:** top-left. The first line is clipped by the top-left frame edge at the entrance, then the pull-back
  reveals it.
- **Art:**
  - Over-the-shoulder POV of Jason driving at dusk.
  - A **phone UI bottom-left**: 7:24, TRACKER DETECTED, VEHICLE SECURITY bar, TRACKER ACTIVE, TOOL NEEDED /
    ADVANCED TOOL.
  - A pink **speedometer reading 65 MPH**, a pink location-target ring over the car ahead, a police helicopter
    with a searchlight.
  - A green highway sign "VICE CITY / Leonida", rendered misspelt (reads like "Leeniida").
- **Motion:** pulls back ×0.95.

**#21 · 3:28.84 – 3:33.91 (5.1 s): "That doesn't work here."**

- **Copy:**
  - `In GTA five, you can pull out a / shotgun from nowhere in front / of people and they don't react.`
    Cream bold condensed, with **pink on "shotgun" and "don't react."**
  - `That doesn't / work here.` Huge heavy grotesque, mixed case. **"That" in cream `#FCF7D9`; "doesn't work
    here." in pink `#EF4BAD`.**
  - A pink brush stroke underneath, and a dark soft backing glow behind the text block.
- **Layout:** the text block is top-right, right of centre.
- **Art:**
  - Jason in a white tank top with a pump shotgun, centre-left.
  - **Panicking pedestrians** with hands up on both sides.
  - A police car with lights, an "OCEAN HOTEL" vertical neon, palms, sunset.
- **Motion:** pulls back ×0.95.

### 3d. The plain-text caption (#12 · 1:59.90 – 2:08.11, 8.2 s)

- **Copy, exact:** `ROB NELSON SAYS THE DRIVING HAS BEEN COMPLETELY REBUILT / FROM THE GROUND UP / THE
  WEIGHTINESS AND THE FEEL OF GTA IV / WITH THE ACCESSIBILITY OF GTA V`
- **Type:**
  - **Heavy condensed grotesque caps**, looks like Bebas Neue or Anton, **pure white `#FFFEFC`**.
  - No black outline is visible; a faint soft shadow only.
  - **Accent in violet-magenta `#D700F4` / `#BD00D7`** on **ROB NELSON**, **GTA IV** and **ACCESSIBILITY**.
    Fuel System's plain posters had no accent at all.
- **Layout:** four centred lines; the block sits slightly below the frame's vertical centre.
- **Plate:** GTA 6 trailer footage blurred to abstraction. It is the jewellery robbery that returns sharp at
  6:58. The plate **hard-cuts at 2:03.26** to the street/motorbike part while the text does not move. On the
  **first frame (1:59.903) the plate is less blurred than on the next**. It looks like the blur starts one frame
  late, a one-frame trim slip.
- **In/out:** hard cut (1:59.886 game → 1:59.903 caption; 2:08.095 caption → 2:08.111 face).
- **Motion:** the text holds static; no push measured.

### 3e. The eight untexted illustrations

#6 phone (0:55.92), #25 peek (4:38.11), #33 garage (5:26.69), #35 cash bed (5:48.85), #36 motel (6:08.92),
#37 store robbery (6:17.08), #39 white-suit desk (6:31.34), #40 apartment (6:34.44).

- **Same art style throughout:** cel-shaded GTA-cover style, heavy outlines, Vice sunset palette of
  pink/orange/violet. Jason in a white tank top and olive cargo pants is a recurring character.
- **Treatment:** full bleed, no text, no plate, hard cut in and out, pull-back of 4–7 % over the hold.
- **Hold:** 3.1–7.7 s, median ≈4.0 s.
- **The last section (6:08–6:38) is a five-image illustrated story:** motel and petty cash → convenience-store
  robbery → (photoreal Jason pointing a gun) → the GTA 5 "god with a fat wallet" → the GTA 6 "rich person with a
  crime record". The illustrations act out the script line by line.

### 3f. Found stills

- **The split key art (#5).**
- **The GTA V weapon wheel plus three GTA V screenshots (#17–#20).** These are a 4-image run, and the last three
  cut on single words.
- **Two HUD blow-ups (#26, #27).**
- **GTA 6 official screenshots and trailer frames (#28, #30, #34, #38).**
- **Two photoreal stills that look AI-generated (#29, #31).**
- **One GTA V screenshot (#32).**
- **How they are treated:** full frame, unannotated, hard cut in and out. The weapon wheel grows ×1.04; the
  others pull back 2–5 %. Holds are 0.7–3.8 s.

### 3g. Game footage

- **Full frame, sharp, HUD left in:** GTA V minimap/stars/cash/street names; GTA 6 pink minimap, stars and heat
  icons.
- **15 clips, ~65 s in total.**
- **Two GTA V clips are chopped into jump-cut fast-forwards** (#7 the sprint walk, #14 the car theft), and #14
  chops the voice with them.
- **GTA 6 footage always plays with every other frame doubled** (≈0.5× or a 30 fps source). GTA V footage plays
  at 1.0× from a 60 fps source.
- **Never inset, never PiP, never split** with the face. The only split screen is the key-art still (#5).

---

## 4. Recurring patterns

**Cadence.**

- 23.9 hard cuts/min overall, by minute **25 · 31 · 24 · 18 · 25 · 18 · 22 · 36.6**. The last partial minute
  is high because of the montage.
- Overlay count by minute: **6 · 7 · 3 · 7 · 6 · 7 · 12 · 0**.
- 2:00–3:00 is the quietest: one caption, one ramp clip and a 23 s face run.
- 6:00–7:00 is the densest: the illustrated story plus the trailer montage.
- **The last 14.7 s have no graphics.**

**Structure = a numbered list of 10.** "This is just one of 10 things". The topic boundaries are marked
visually:

| item | starts | marked by |
|---|---|---|
| 1 cops off the minimap / cones | 0:00 | cold open |
| 2 tap-to-sprint | 1:06.90 | **TV colour bars** (1:06.72) |
| 3 radio wheel | 1:35.4 | cut zoom ×1.18 on "There is no radio wheel" |
| 4 driving weight | 1:53.5 | **whip** |
| 5 stealing cars (scan / tracker) | 2:38.8 | face, on "The verb the game is named after" |
| 6 weapon wheel | 3:16.63 | **TV colour bars** |
| 7 aim assist | 3:46.4 | **whip** |
| 8 wanted / heat | 4:20.8 | spoken "Up next", cut zoom ×1.28 |
| 9 property | 5:15 | the "permanent suspect" still |
| 10 money gates | 5:46.3 | **whip + the set change**, "Here's the last one" |

A fourth stinger (0:54.35) closes the intro. So **3 colour-bar stingers and 3 whips = 6 dividers**, and every
one sits at a section seam.

**Which line gets what.**

- **Inset quote card:** a quoted sentence attributed to a named person (Rob Nelson, TGG, "FAN"), set near
  verbatim.
- **Full-frame illustrated text card:** the item's rule stated as a punchline ("You have to SCAN it", "keep it
  at a CERTAIN SPEED", "That doesn't work here", "you have to use FOCUS"). These are paraphrased, and the
  illustration acts the rule out.
- **Plain-text caption:** a long reported quote with three key terms highlighted.
- **Untexted illustration:** a hypothetical or narrative beat no footage exists for: Jason staring at his phone,
  hiding from cops, the garage stash, the "ending rich" fantasy, the motel/robbery/apartment story.
- **Found still:** a named thing being listed (weapon names, HUD elements, specific GTA 6 screenshots).
- **Game footage:** an action described in GTA V ("you walk up, press triangle", "you do quadruple flips",
  "repeat until the mission ends"), or GTA 6 shown as evidence ("the guns have weight", the freedom montage).
- **Face only:** opinions ("I'm actually a fan of this", "I hope it's not like very real"), the jokes'
  set-ups, transitions and the close.

**Inset vs full frame.**

- Insets are **only the 80 % quote/radar cards** on blurred gameplay.
- Everything else is full bleed: game footage, illustrations, stills and the caption plate.
- No PiP, no split with the face, no colour matte or solid background behind any footage.

**Motion on graphics.** There are two opposite moves, used consistently:

1. **Inset cards grow** about ≈1 %/s (×1.04–1.06 over 4–6 s).
2. **Full-frame stills and illustrations pull back** about ≈1 %/s (×0.93–0.98). They enter slightly over-scaled.
   This is the inverse of Fuel System's "card push".

The face matches the second move: static, or slowly pulling out.

**Speed on B-roll.**

- GTA 6 clips: every other frame doubled (≈0.5×).
- GTA V clips: 1.0×.
- The GTA 6 trailer frame at 5:38: near-frozen.
- Stills and illustrations: static with the scale move only.
- **No 0.03×-style frozen reaction shot.**

**Transitions.**

- **Hard cut everywhere**, verified at single-frame level on every graphic boundary.
- **Exceptions:** 3 TV-colour-bar stingers (11 frames each, identical asset) and 3 whip-blur transitions
  (≈17–19 frames each).
- No dissolves, no fades (the first and last frames have flat luma), no slides and no animated text.

**Reuse.**

- The GTA V red-car clip appears as B-roll (0:09.7) and as the blurred plate under 2 of the 4 quote cards and the
  radar card.
- The Michael gameplay recording supplies both #7 and #14.
- The GTA 6 jewellery robbery is the caption plate (2:00) and the penultimate insert (6:58).

---

## 5. Comedy and emphasis devices you can see

| t | device |
|---|---|
| **0:08.54, 0:53.02, 4:36.33, 5:57.04** | **Punch-and-slow.** A cut zoom (×1.22–1.28) plus a slight slow-down on the punchline. The picture repeats a frame every 6–7 frames (≈0.85–0.87×) and the speech in those windows runs 8–13 chars/s against 14.3 average. The lines: "them on purpose.", "with consequences", "oh, a law-abiding citizen here." (sarcasm), "says you don't get shit." (profanity left in, on the one pink pick-up shot inside the beige section). This is the face slow-down, at ≈0.85×. That is milder than the preset's 0.5–0.6×; check by ear. |
| **0:54.35, 1:06.72, 3:16.45** | **TV colour-bars stinger**, 11 frames of noisy SMPTE bars as a hard "channel change" between sections. 0:54.35 lands in the only ≥1 s pause of the video, right after "with consequences". |
| **1:05.22** | **Punch ×1.40 into a soft, out-of-focus take** on "are going to be furious", straight into the bars stinger. |
| **1:08.52 – 1:13.29** | **Jump-cut fast-forward on gameplay**: Michael's walk chopped every 0.15–0.5 s on "every GTA player has won by hammering X". The cutting acts out the button-mashing. |
| **1:32.21 – 1:33.33** | **Mirrored tight shot**, flipped horizontally with the neon backwards, on "I don't know why people are upset". It fakes a second camera. |
| **1:53.23, 3:46.13, 5:45.98** | **Whip-blur** between takes at section changes. 3:46 lands on him miming a phone call. |
| **2:22.09 – 2:45.06** | **The longest face run (23 s)** carries a riff with nothing to cut to: "Maybe Jason has to call in some pedestrians to help him out to flip the car over". Four cut zooms inside it (2:29.15 ×1.40 on "flip it back", 2:33.95, 2:36.77, 2:41.24). |
| **2:45.06 – 2:48.84** | **"Boom done" theft chopped to bits.** Picture and voice are jump-cut together ("GTA" and "yours" chopped mid-word) on "you walk up, press triangle, it's yours forever, boom done". |
| **3:24.09 – 3:26.72** | **One still per word**: "rocket launcher" (1.1 s), "minigun" (0.7 s), "pistols" (0.8 s). A mimic cut. |
| **3:28.84** | **The literal illustration**: shotgun-wielding Jason surrounded by panicking pedestrians on "they don't react / that doesn't work here". |
| **0:23.09** | **Pun in the art**: the "FOCUS" card's cop casts a literal pink vision cone, illustrating "the little cones". |
| **4:54.14 → 4:55.01 → 4:55.75** | **Staircase zoom on a spoken list**: ×1.28 on "your face, your outfit", ×1.12 on "your partner", ×1.15 on "your car". It climbs to ≈×1.65, then snaps back out (4:56.26, ×0.82). |
| **4:48.42 – 4:53.23** | **HUD blow-ups** on "you have the stars and then you have something called heat icons". The game UI is enlarged to fill the frame. |
| **5:52.40** | **Slowed word** "millions" (pitch ×0.82, 0.45 s) under the man-on-a-bed-of-cash illustration. |
| **6:08.92 – 6:38.18** | **Illustrated story run**: five images act out "commit crimes → cash goals → rob something → crime record", ending on the GTA 5 / GTA 6 pair: a god with a fat wallet vs a rich person with a crime record. |
| **6:47.67 – 6:56.52** | **Freedom montage**, 5 trailer clips at ≈0.5× under "you still have as much freedom as you had before". |
| throughout | **On-screen copy errors shipped:** the 1:36 quote attributed to Rob Nelson though it is TGG's; TGG labelled "ROCKSTAR"; "digital cones" for "little cones"; "showed" for "shows"; "Leonida" misspelt in the TRACKER art; lowercase "i'm" on the FAN card; the radar card shows red dots while he says "blue dots". |
| — | **No freeze frames on the face.** Every face slow-down still moves. |

---

## 6. Palette and type summary

### Palette

| swatch | hex | where |
|---|---|---|
| Hot pink (accent) | **`#ED21B4` / `#EB2BAA` / `#EF4BAD` / `#EB429C`** | the accent words on the 4 illustrated cards |
| Quote-card accent pink | **`#DB35A5` / `#E1196E` / `#D832A6`** | one phrase per quote card |
| Violet-magenta | **`#D700F4` / `#BD00D7`** | the accent words on the plain-text caption |
| Pure white | **`#FEFFFA` / `#FFFEFC`** | quote-card body type; caption type |
| Cream | **`#FDFBE1` / `#F2ECDE` / `#FCF7D9`** | illustrated-card type |
| Card gradient, blue | **`#052A9C`** | quote card top-left |
| Card gradient, violet | **`#251252` / `#5B0093`** | quote card middle and lower-left |
| Card gradient, pink | **`#E3207E`** | quote card bottom-right, sunset |
| Neon frame / glyph | **`#A75BD9` / `#9B53D9`** | quote-card inner tube and quote marks |
| Rule | **`#85439D`** | attribution hairline |
| Set, pink LED wall | **`#F5A5CB` – `#FF9AD7`** | Look A (0:00–5:46) |
| Set, warm wall | **`#E4AC93` / `#C98B62`** | Look B (5:46–7:19) |
| Leather chair | **`#52131C`** (pink light) / **`#492B1B`** (warm light) | behind him |
| Lens orange | ≈ `#E0603A` | his glasses |

The graphic system is **pink on a blue→violet→pink Vice sunset**, white type on the inset cards, cream on the
illustrations, and one violet-magenta exception on the caption. The room's magenta LED in Look A matches the
cards, so face and graphics feel like one palette. Look B breaks that.

### Type classes

1. **Rounded geometric sans, bold, sentence case, white.** Quote cards. Looks like Poppins Bold or Montserrat
   Bold. The attribution is small bold caps, and "ROCKSTAR" tiny and letterspaced.
2. **Heavy condensed grotesque caps, white with violet accents.** The 2:00 caption. Looks like Bebas Neue or
   Anton.
3. **Heavy italic condensed.** "FOCUS.", pink with a swoosh underline. Its kickers are a lighter condensed
   (Oswald class).
4. **Extra-bold extended sans.** "SCAN", looks like Archivo Black or Montserrat Black. Paired with a heavy sans
   kicker and a condensed bold body.
5. **Brushy / comic condensed caps.** "AND IF YOU STEAL ONE / … CERTAIN SPEED".
6. **Heavy grotesque, mixed case.** "That doesn't work here.", over a bold-condensed mixed-case kicker.
7. **Generated UI micro-type inside the art.** SECURITY LEVEL, TOOL YOU NEED, TRACKER DETECTED, ADVANCED TOOL.

**Treatments:**

- Illustrated-card type sits *in* the art. It has scene-matched glow, pink brush underlines and dark backing
  glows.
- Quote-card type is flat white, no shadow, on the gradient.
- The caption is flat white with a faint shadow.
- No outlines anywhere, no kinetic type, no word-by-word reveals.

---

## 7. Ending (6:44.17 – 7:19.65)

- **6:44.17 – 6:47.67:** face, Look B. "Rob said no. His words, I don't think it changes what GTA is."
- **6:47.67 – 6:56.52:** five-clip GTA 6 trailer montage. Then face (6:56.52 – 6:58.32).
- **6:58.32 – 7:04.94:** jewellery robbery → MARCUS 69 motorbike getaway. This is the last graphic. "…a
  permanent crime record of you".
- **7:04.94 – 7:19.65: 14.7 s of pure face, Look B, warm wall.**
  - He opens on a flex pose with fists up at 7:05.
  - The frame drifts out slowly.
  - **Cut zoom ×1.19 at 7:12.45** on "what's it going to be for", then out at 7:13.48.
  - Words: "now the biggest one for me personally is just the mini map … if we cannot find the cops if we cannot
    find the enemies what's it going to be for that's going to be the video guys hopefully you guys enjoy let me
    know what you guys think in the comments catch you guys inside of the next one".
- **Last frame (7:19.6):** medium shot, hands on the desk, looking at the lens.
  - No fade: luma is flat 101–104 to the end.
  - No end card, no subscribe button, no end-screen placeholder, no logo, no music button.
  - Nothing is held clear on the right or bottom.
  - The close is a spoken CTA ("let me know … in the comments") over the bare face, and the cut to black is the
    file's end.

---

## 8. Differences vs the face-cam preset README

### What this 17k video does that the preset does not say (or says the opposite of)

1. **Face share is ≈57 %, not ~80 %.**
   - Overlays fill ≈43 % of the runtime: 47 overlays in 35 runs (4.8 runs/min, median run 5.1 s).
   - The longest face run is 23.0 s. The close is 14.7 s.
   - There are no 36–40 s graphic-free stretches like Fuel System's.
2. **AI-style illustrations are a main B-roll type:** 12 of them, 64 s, 15 % of runtime.
   - 8 have no text.
   - 4 have the headline baked into the art, all full frame.
   - The preset only knows typeset inset cards, game footage and found stills. (The preset's § 5 mentions
     Higgsfield stills only as "an option for a line no footage can show".)
3. **There are two card systems, and neither matches the preset template.**
   - **Inset quote card:** 80 % of frame, not 72 %. **No tilt.** Square outer corners plus an inner neon
     rounded tube. **White rounded geometric sans, sentence case**, not cream heavy condensed caps. Quote
     glyphs and an attribution line. Grows ~1 %/s.
   - **Full-frame illustrated text card:** no inset, no plate, no tilt. **Pulls back** ~1 %/s.
4. **No gradual push-in.**
   - Face shots are static or slowly **pull out** (−1.0 to −1.5 %/s measured at 3:53–4:05, eased; a steady
     −1.5 %/s at 7:05–7:11).
   - The first shot opens ~12 % tight and eases out.
   - The preset says ~1 %/s push-in on every nest.
5. **Cut-zoom steps are smaller and held longer:** median ×1.21 (p25–p75 1.16–1.29), max ×1.40, hold median
   1.36 s. The *rate* matches: 5.2/min of runtime against the preset's ~5. 30 of 38 are pure snaps inside a
   take; 8 ride a jump cut.
6. **Six section dividers that are not hard cuts:**
   - 3 **TV colour-bar stingers** of 11 frames (0:54.35, 1:06.72, 3:16.45).
   - 3 **whip-blur transitions** of ≈0.3 s (1:53.23, 3:46.13, 5:45.98).
   - The preset says "the hard cut" is the only transition device.
7. **The video is a numbered list of 10**, and the dividers fall on the item seams.
8. **Punch-and-slow on the face, ≈0.85×, 4 times**, each riding a ×1.22–1.28 snap (0:08.54, 0:53.02,
   4:36.33, 5:57.04). The preset specifies 0.5–0.6×, 1–2 per video. One audio-only slow-down, "millions" at
   5:52.40 (×0.82), sits under an illustration.
9. **Staircase zoom on a spoken list** (4:54.14 / 4:55.01 / 4:55.75, to ≈×1.65).
10. **Mirrored shot** as a fake second angle (1:32.21–1:33.33).
11. **Mimic cutting on gameplay:** GTA V clips are jump-cut into fast-forwards (1:08.5, 2:45.1), with the
    voice chopped along with the picture. Single-word still montages (3:24–3:26).
12. **HUD blow-ups as graphics:** the radar inset at 0:03.4, the wanted-star strips and the heat icons at
    4:48–4:53.
13. **A plain-text caption with accent colour:** violet `#D700F4` on three phrases. Fuel System's plain posters
    had none.
14. **Two lighting setups intercut.** Pink LED for 0:00–5:46, warm-white for 5:46–7:19, with a pink pick-up
    spliced into the warm section (5:55.6–5:58.5). The preset describes one lit back wall per video.
15. **The set has no microphone in frame**; a small clip-on transmitter sits mid-chest. There is a **YouTube Play
    Button plaque** next to the neon. The preset's props are the red-grille mic or the spatula lav.
16. **No subscribe animation at all.** The preset says twice per video, bottom-left.
17. **GTA 6 footage is consistently frame-doubled** (≈0.5×), while GTA V plays 1.0×. There are no extreme
    0.03–0.15× reaction freezes; the nearest is the near-frozen trailer frame at 5:38.
18. **Plates and footage are reused.** One GTA V red-car clip sits under 3 cards (the radar and 2 quote cards) and appears as B-roll. One
    jewellery robbery is both the caption plate and a late insert.
19. **Copy errors shipped:** a misattributed quote (1:36), a wrong "ROCKSTAR" sub-label on TGG, "digital cones",
    "showed", a misspelt "Leonida", and a radar showing red dots against "blue dots". The preset mentions typos;
    this adds factual attribution errors.
20. **Brighter picture:** mean luma 0.418, against Fuel System's 0.337.

### What the preset says that this video does not do

1. **Face ~80 % of the runtime, overlays as "seasoning":** not here. The face is 57 %.
2. **Gradual push ~1 %/s on every face nest:** absent. The move is static or a pull-out.
3. **Cards tilted 1–3°, ~72 % of frame, cream heavy condensed caps, growing 8–15 %:** quote cards are flat
   (0°), 80 %, white rounded sans, growing 4–6 %. The illustrated cards are full frame and pull back.
4. **"The hard cut, only":** there are 3 colour-bar stingers and 3 whips.
5. **Slow-downs at 0.5–0.6×, 1–2 per video:** the face slow-downs here are ≈0.85×, 4 of them.
6. **Two long graphic-free stretches (36 s and a 39.5 s close):** the longest is 23 s, and the close is 14.7 s.
7. **Subscribe animation twice:** none.
8. **The zoom burst** (six crop levels in 4 s): none. The probe's "burst" at 3:55–4:05 is a slow pull-out
   misread. The nearest is the 3-step staircase.
9. **The near-frozen reaction clip of a real person** (Rob Nelson at 0.03×): none. Rob Nelson is never shown;
   he exists only as quote cards and a caption.
10. **The meme insert:** none. There is no live-action found clip at all; the "found" material is game footage,
    official stills and AI images.
11. **Cut zooms of ×1.27 median with occasional ×1.5–×2.6 hits:** the median is ×1.21 and the max ×1.40, with
    no ×2 close-up.

### What matches the preset (for completeness)

- Opens on the face. First insert at 3.4 s. No title card, logo or branding.
- Ends cold on the face with no end screen and nothing kept clear.
- Game footage is always full frame and sharp with the HUD left in. Never inset, PiP or split with the face.
- Card headlines are the sentence being said: quote cards near verbatim, illustrated cards paraphrased.
- Every card and overlay enters and exits on a hard cut. No text animation.
- No captions, lower-thirds, logo bug or name tags.
- Speech density is similar: 205 vs 211 words/min, with one pause ≥ 1 s.
- Cut-zoom rate is about 5 per minute.
- The "skool" neon set, the leather chair, orange-lens glasses and a dark tee.
