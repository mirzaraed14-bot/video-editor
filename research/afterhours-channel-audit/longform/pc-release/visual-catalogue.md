# Visual catalogue: "GTA 6 Is Coming To PC Sooner Than Everyone Thinks" (Affan Afterhours)

5:15.70 · 1920x1080 · 60.00 fps · uploaded 2026-09-23 · 1.1k views · master `raw/pc-release.mov`.
Read frame by frame on 2026-10-08. The layer identities come from the creator's own timeline (`prproj/PC-release-Seq24.summary.txt`,
`agg-pc-release.txt`); everything below says **how it looks** and **what is said over it**. Timecodes are program time in the master.
Anything marked *looks like* is an inference, not a measurement.

**Evidence in `frames/`:** `sheet_001…022.jpg` (2 fps contact sheets, 15 s each, timecode burnt top-left). `f_<m>m<ss.ss>_<label>.jpg`
(153 full-res stills at every overlay entrance/exit, meme, zoom extreme, ladder rung, slow-down, the cold open and the last 15 s).
`keyframes_grid_001…017.jpg` (the same stills, 9 per page, labelled). `corner-detail.png` (overlay corners, A top row vs B bottom row).

**Measurement notes.** Face size = OpenCV face box (forehead to chin) as % of frame height. Inset size = edge scan of the inset's
bounding box (reliable on the flat-colour cards, ±3 % on busy footage). Colours = medians of the pixels, 8-bit hex.

---

## 1. Face framing, set, and how each zoom level reads

**The set (bright, warm, daylight-ish).**
- **Wall:** pale sage/cream green, washed out by a bright key: `#C7C78D` (behind the right shoulder) to `#DAD7A4` (the mid-right
  wall). It is **not** the saturated LED green of the Game Informer video, and not the lavender of Fuel System. Upper-left corner
  falls off warm `#9A8059`.
- **Neon:** `skool` script neon, top centre, slightly left of his head: `s` blue/pink, `k` pink, `oo` cyan with white cores, `l`
  orange. At 100 % the whole word sits clear above his hair. A **pink/magenta-lit square box frame** on the wall, upper left.
- **Props:** brown leather armchair behind him (`#4E2317`), headrest at shoulder height; a leafy plant behind the right shoulder; a
  dark monitor edge cutting into frame right; a black/grey backpack with an orange item on the desk lower right; the **red-grille
  mic on a desk stand** in the lower centre (red-lit grille, black shock mount) that he talks over.
- **Wardrobe:** navy crew-neck T-shirt (`#141011` in shadow), steel watch on the left wrist, bead bracelet on the right.
- **Luma:** face shots average ~0.45 (115/255) — this is the brightest of the channel's sets; the master's mean is 0.40.

**Framing at 100 %:** medium close-up, chest up. Face box ≈ **28–31 % of frame height**, face centre at x ≈ 50 % (range 43–55 %),
y ≈ 44–48 %. Generous headroom with the neon above the hair; chair wings visible both sides; monitor edge right.

**How tight each zoom level reads (measured on the master; nests add up to +10 % on top of a clip's own scale):**

| scale | face box (% of frame h) | what it looks like | frames |
|---|---|---|---|
| 100 | 28–31 % | chest-up MCU, full neon, chair wings, monitor edge | `f_0m04.80`, `f_3m48.00`, `f_5m00.80` |
| 110 | 35–36 % | top of the neon starts to clip; mic still whole | `f_2m21.80`, `f_3m49.20` |
| 120 | 37–39 % | neon cut through the letters; shoulders fill the width | `f_2m23.40`, `f_3m49.90` |
| 130 | ~40 % | close-up; neon only as colour at the top edge | `f_3m50.80` |
| 136–143 | 42–44 % | chin to crown fills ~half the frame, mic head at the bottom edge | `f_0m18.40`, `f_3m45.50` |
| 150–160 | 49–50 % | tight CU, hair touches the top edge | `f_1m52.60`, `f_1m35.90` |
| 167–183 | ~52 % (measured at 172) | tight CU, forehead starts to crop | `f_3m20.50`, `f_4m00.90`, `f_4m17.40` |
| 201–215 | 62–67 % | big CU: forehead to beard, a hand at the edge, nothing of the room but blur | `f_1m07.50`, `f_4m59.50` |
| 294 / 356 | face no longer fits (detector fails) | **ECU**: eyes to beard (294) / eyes and open mouth fill the frame, forehead gone (356) | `f_0m24.60`, `f_4m30.20` |

Cut zooms snap on a cut, are held ~1.3 s (median), and come back on the next cut. Two carry a reposition (201 at 1:07.3 shifted to
0.577/0.619 so the face stays centred; 294 at 0:24.5 shifted up to 0.354).

---

## 2. Cold open, beat by beat (0:00–0:42)

| time | picture | said |
|---|---|---|
| 0:00.00–0:01.89 | **FACEPALM meme**, inset (~88 % wide) on the dark matte with a drop shadow, shrinking 132→127. Four shots inside it: two uniformed cops and a blonde woman (*looks like* The Naked Gun 33⅓ Oscars scene), a TV control room, an audience in black tie all palming their foreheads (two angles). **First shot of the video is not the face.** | "So the internet has officially decided" |
| 0:01.89–0:04.72 | **cue2**: AI synthwave Vice-City boulevard (wet neon road, pink sunset, skyline, a dark sports car's red tail-lights, palms). Enters at ~95 % wide, ends ~87 %. Text **COMING TO PC 2028** (white geometric heavy caps, *looks like* Montserrat ExtraBold, soft shadow) top centre, fading in 2.1→2.4 s. | "GTA 6 is coming out on PC in 2028." |
| 0:04.72–0:06.62 | Face 100→105 push (2.6 %/s), hand raised palm-out | "Like, it's done. It's settled." |
| 0:06.62–0:09.14 | **"THE FIVE STAGES OF GRIEF"** wojak chart (white table, serif small-caps title, Denial / red Anger / Bargaining / Depression / Acceptance, right column empty): a tall narrow screenshot (~42 % wide × 89 % high) centred on the matte, shrinking 151→140 | "PC players have gone through all five stages of grief." |
| 0:09.14–0:10.99 | **The chart punch (Nested Sequence 129, 281 %)**: hard cut into the bottom two rows only, **Depression / Acceptance** filling the left two thirds, the white table bleeding off right and top. No matte visible. | "Now they're sitting at acceptance." |
| 0:10.99–0:18.23 | Face nest 110 (7.2 s, four jump cuts): hands thrown up, then the arm flung out frame-left pointing at an imaginary calendar, eyebrows up | "Got a little calendar on the wall, crossing off days, 700 and something to go. And I'm here to tell you, I think," |
| 0:18.23–0:20.92 | **Slow-down 0.8x + 136 %**, leaning into the lens | "ladies and gentlemen, everybody is wrong." |
| 0:20.92–0:24.49 | **Collage card**: six vertical AI panels, each labelled at the foot in white condensed caps with a tiny lilac year: GTA III 2001 (grey rain, elevated rail) · VICE CITY 2002 (neon deco) · SAN ANDREAS 2004 (lowrider, palms) · GTA IV 2008 (Brooklyn bridge, sleet) · GTA V 2013 (LA freeways) · RED DEAD 2 2018 (mountains, horses). Enters ~95 %, shrinks to ~87 %. | "And I'm not guessing. Rockstar's own history kind of proves it." |
| 0:24.49–0:25.46 | **294 % ECU** (eyes to beard, hand blur right) | "So here's the plan." |
| 0:25.46–0:28.39 | Face nest 105, 114 snap at 0:27.7 | "First, I'll show you where this 2028 thing even comes from." |
| 0:28.39–0:32.98 | **Interview clip**: a bald man in an olive jacket at a podcast boom mic (*looks like* an ex-developer interview), inset on the matte | "Because, spoiler alert, nobody at Rockstar has said this, not even once." |
| 0:32.98–0:38.04 | **Three-game run** (one clip each, hard cuts): GTA IV street with the **"RTX REMIX by xoxor4d" watermark left in** · GTA V Franklin and Lamar in an alley, **minimap + "KVG" watermark left in** · RDR2 Arthur riding through Valentine, minimap | "Then there's a pattern in Rockstar's last three games that literally nobody talks about." |
| 0:38.04–0:42.13 | Face nest 105 (head down, hand at ear), 116 snap at 0:41.0 | "…everybody's mind is stuck on GTA 5 and how it took 19 months." |

Note: the 0:28.4–0:38.0 interview + three-game run is **in the master but not on the decoded Seq24 V2/V3** (V1 there is face,
colour-labelled Rose). *Looks like* it was added after the decoded snapshot, or sits on a track the decoder did not read.

---

## 3. Overlay master table

**The treatment, identical on every insert (A has no exceptions except the two full-frame glitch memes in § 4):**
- **Inset, not full frame.** The picture sits on V3 at 85–95 % of the frame and **shrinks over its hold** (95→87, 90→85, 85→80,
  i.e. −0.5 to −2.8 %/s). The shrink is the motion: it reads as the card slowly settling back into the matte, the opposite of a push.
  Stills that are not 16:9 (the grief chart, the calendar plate, Mike York) simply sit smaller in the middle.
- **Square corners** (no rounding) and a **soft dark drop shadow down-right** (Premiere Drop Shadow, 80 % opacity, 135°, distance 30,
  softness 40) — visible as a ~20 px dark smear off the bottom and right edges (`corner-detail.png`, top row).
- **The matte (V2 `overlay-matte.mp4`)**: near-black blue-violet base `#06060C` with two very soft, slow blooms — **magenta
  (brightest ~`#5B2648`) drifting top-left, teal (~`#0A1C20`) bottom-right** — plus a faint vignette and grain. Only a 3–10 % border of
  it is ever visible, and the border widens as the inset shrinks. Each instance starts at a different in-point, so consecutive inserts
  do not show the same frame of it. Under the 4:36.9 GTA V logo the matte is razored into six pieces that all restart at the same
  in-point: *looks like* a barely visible hiccup of the glow every ~1.2 s.
- **Entrances and exits are hard cuts.** No slide, no fade on the inset itself; motion-graphic text fades in inside the card.
- **Game footage keeps its HUD and other people's watermarks** (RTX Remix, KVG, minimaps, ammo counters, a mod menu).

| # | in–out | dur | what's shown | inset (start→end, % of frame width) | said over it |
|---|---|---|---|---|---|
| 1 | 0:00.00–0:01.89 | 1.9 | FACEPALM meme (4 shots, § 2) | ~88 % (scale 132→127) | "So the internet has officially decided" |
| 2 | 0:01.89–0:04.72 | 2.8 | cue2 AI synthwave card + **COMING TO PC 2028** | 95→87 | "GTA 6 is coming out on PC in 2028." |
| 3 | 0:06.62–0:09.14 | 2.5 | Five Stages of Grief chart (portrait) | 42 % w × 89 % h, 151→140 | "…all five stages of grief." |
| 4 | 0:09.14–0:10.99 | 1.9 | the chart at **281 %**, Depression/Acceptance rows (no matte) | full bleed | "Now they're sitting at acceptance." |
| 5 | 0:20.92–0:24.49 | 3.6 | Rockstar-history collage, 6 labelled AI panels | 95→87 | "Rockstar's own history kind of proves it." |
| 6 | 0:28.39–0:32.98 | 4.6 | interview clip, bald man at boom mic | ~92 % (footage 4:3-ish inside) | "nobody at Rockstar has said this, not even once" |
| 7 | 0:32.98–0:38.04 | 5.1 | GTA IV (RTX Remix wm) → GTA V alley (KVG wm) → RDR2 Valentine | ~90 % | "a pattern in Rockstar's last three games" |
| 8 | 0:42.13–0:47.35 | 5.2 | **mg1** "FOUR DAYS AGO / THE CEO SPOKE" | 95→87 | "The CEO of Take-Two said something four days ago that PC players should be very happy about." |
| 9 | 0:54.34–0:58.38 | 4.0 | **plate**: dark AI room, wall calendar with the month **blurred out**, pink/teal neon city through a rainy window, a plant, a black cat figurine | ~90 %, 130→120 | "at the very end, I'm giving you the exact month I think it comes out on PC" |
| 10 | 1:22.17–1:24.93 | 2.8 | **cue10** synthwave card (mirrored layout) + **RUMOURED PC 2028 ?** | 94→88 | "The 2028 thing mostly comes from people doing maths" |
| 11 | 1:41.53–1:45.91 | 4.4 | GTA IV still: blue muscle car at a toll barrier | ~90→88 | "GTA 4: console April 2008, PC in December, about seven months, not bad." |
| 12 | 1:45.91–1:52.43 | 6.5 | GTA V still: Michael in a suit striding across a downtown plaza | ~90→86 | "GTA 5: console September 2013, PC April 2015, about 19 months." |
| 13 | 1:56.45–2:00.20 | 3.8 | RDR2 gameplay: Arthur in a dark lamplit interior, rifle up (warm amber) | 88→84 | "Red Dead 2… came out October 2018, releases on PC November 2019" |
| 14 | 2:24.48–2:27.63 | 3.2 | GTA V official gameplay video: Simeon yelling at Franklin in the PDM office, then the trailer's own black card **"AN INTRODUCTION / TO THE WORLD OF"** | ~85 % | "So GTA 5 came out at the end of a generation." |
| 15 | 2:31.38–2:35.24 | 3.9 | GTA 6 Extended Look: Jason, Lucia and a dreadlocked man storming a graffiti-covered green-lit apartment | 90→85 | "GTA 6 is built for modern hardware from day one." |
| 16 | 2:39.23–2:43.20 | 4.0 | Strauss Zelnick on stage (navy sweater, white trousers, blue "iicon" backdrop) | 90→85 | "now what the CEO said. Four days ago, September 17th, Take-Two had their shareholder meeting." |
| 17 | 2:45.20–2:47.93 | 2.7 | **mg2** "STRAUSS ZELNICK / CEO, TAKE-TWO" | 90→87 | "Strauss Zelnick is the CEO of Take-Two" |
| 18 | 2:55.69–3:03.87 | 8.2 | **mg3** quote 1 **"MORE AND MORE IMPORTANT"**, hard switch at ~2:59.8 to quote 2 **"A MEANINGFUL AUDIENCE"** | 90→85 | "he said PC is, I'm quoting him, more and more important. And… they launch on platforms for which there's a meaningful audience." |
| 19 | 3:16.00–3:20.23 | 4.2 | GTA V Online modded lobby: a cop-uniform player T-posing in the sky over LS, then the **2TAKE1 mod menu** (cyan/black) and chat spam | ~90 % | "hackers, right? Or it's gonna ruin the game for everyone, modding, etc." |
| 20 | 3:21.50–3:24.52 | 3.0 | Mike York webcam still (cap, headphones, purple-lit shelf, thumbs-up) | ~75 % (scale 85, no move) | "an ex-Rockstar developer, Mike York, he actually worked there" |
| 21 | 3:24.52–3:27.81 | 3.3 | **mg4** "01 / PLAYSTATION / SELLS THE MOST" | 85→80 | "number one, PlayStation sells the most" |
| 22 | 3:34.21–3:37.05 | 2.8 | **mg5** "EVERY PERSON HAS / A DIFFERENT PC" | 85→81 | "his words, every single person has a different PC" |
| 23 | 4:01.56–4:05.03 | 3.5 | **mg6** "10 OR 20 / DIFFERENT SETUPS" | 85→80 | "York says they test on, his words, 10 or 20 different setups" |
| 24 | 4:14.02–4:17.14 | 3.1 | RDR2: Arthur in a mud-street fist-fight in Valentine, minimap | ~90 % | "Red Dead had the exact same problem and they solved it within a year." |
| 25 | 4:22.55–4:23.53 | **1.0** | **mg7** "01 / MONEY" (cut while its text is still fading in) | 85→84 | "number one is money" |
| 26 | 4:36.89–4:44.15 | 7.3 | GTA V logo key art (logo over a white Range Rover street shot) | ~80→75 (129→122) | "GTA 5… has sold over 230 million copies across every console known to man" |
| 27 | 4:56.85–4:59.18 | 2.3 | console concept render: matte-black PS5-style console + pad, magenta fog left, teal fog right | ~88 % (126, static) | "when the PS6 comes out, they're gonna launch it with that." |

Rows 6, 7, 19 and 24 are on the master with the same matte + shadow treatment but are **absent from the decoded V2/V3**.

**Totals:** 27 non-face pictures in 23 runs (memes and the glitch excluded), ~22 % of runtime, median ~3.5 s. Longest off-face stretch:
1:41.5–1:52.4 (the two console-history stills back to back, 10.9 s).

---

## 4. The creator's own additions

| time | what | how it looks | the line under it |
|---|---|---|---|
| 0:00.00 (1.9 s) | **FACEPALM meme** | inset on the matte like any overlay, 4 shots of crowds facepalming | "So the internet has officially decided" |
| 0:09.14 (1.9 s) | **Nested Sequence 129 at 281 %** | the grief chart punched to its last two rows, full bleed | "Now they're sitting at acceptance." |
| 1:01.80 (0.2 s, 12 frames) | **SMPTE colour bars + sine tone** | full-frame bars, no matte — a "signal lost" flash; *looks like* a mock broadcast cut right after the swear | lands straight after "roast the shit out of me." (the swear itself is in the 0.8x slow-down) |
| 2:10.78 (1.2 s) | **horizontal stretch, Scale Width 928 %** | after a 0.2 s 146 % snap on "right?", his face smeared into a wide pancake, the neon a streak, the mic grille a red band | "The PS3, guys," (the fat PS3) |
| 2:15.15 (0.5 s) | **"house exploding #meme#"** | a 4:3 SD clip, **full frame with black pillarbox bars, no matte**: a farmhouse blowing apart in a fireball | on "living room." of "the console that sounded like it's going to take off in your living room" — then a 151 % snap |
| 3:56.65–4:00.56 (3.9 s) | **Awkward Cricket SFX** (−15 dB) | played over one **held 1x wide shot** (3:55.5–4:00.7): dead-pan stare into the lens, eyes flick away, tiny shrug. No zoom, no overlay — the 4.3 s silence is the joke | after "…refuses to upgrade. You know who you are." → (crickets) → 172 % snap on "1080 Ti user." |
| 4:11.72 (1.2 s) | **stretch, Scale Width 266 %** (inside nest 124) | wide, squat face, neon stretched | "the, the complexity takes some time" |
| 4:32.74 (1.5 s) | **stretch, Scale Width 248 %** | squat face, brow knotted, hand flapping | "We're not so different." |
| 1:04.6, 3:05.5, 5:06.3 (8.4 s each) | **SUBSCRIBE bug ×3** | bottom-left: bell icon → red SUBSCRIBE pill (~3.7 s) → a cursor clicks → grey SUBSCRIBED with a blue bell → collapses. Rides on top of whatever is under it, including the 201 % zoom at 1:07.3 and the 149/138 % zooms at 3:06 / 3:09 | #1 "Someone had to say it first, right? The thing is, no one said it." · #2 "Now this is the one I actually think is the biggest deal" · #3 "will be released. Now make sure to tell me in the comments…" |

**The extreme cut zooms (what 201 / 215 / 294 / 356 are):**
- **294 %, 0:24.49–0:25.46:** ECU, eyes to beard, on "So here's the plan." — the hinge into the roadmap.
- **201 %, 1:07.30–1:08.60** (inside nest 115, repositioned): big CU, deadpan, on "The thing is, no one said it." (subscribe bug riding over it).
- **356 %, 4:29.79–4:31.15:** the tightest frame on the channel — eyes and open mouth fill the screen, forehead cut — on
  "You're gonna buy a PS5, right?"
- **215 %, 4:59.18–5:00.22:** big CU, a knowing half-smile, on "I don't think so, because" (rebuttal of the PS6 rumour).
- Others ≥150: 158 "and everybody knows it" (1:21.3) · 156 "the famous one" (1:52.4) · 160 "2028" (1:35.5, slowed) · 167 "that's
  not the main reason" (3:20.2) · 172 "1080 Ti user" (4:00.7) · 174 "is your impatience" (4:48.0, slowed) · 183 "now before the
  comments come for me" (4:17.1, mock-stern stare).

**The zoom ladders** (four consecutive hard cuts, each +10 %, each on the next item of a list):
- **3:48.95–3:55.47:** 110 (0.8x) "Shaq," → 120 "a toddler," → 130 "fit your uncle with a weird toe," → 140 "fit the guy who's still
  running a graphics card from 2016 and refuses to upgrade." Face box 35 → 37 → 40 → 42 %. Then back to 1x wide for the cricket.
- **5:01.47–5:06.99:** 110 "November" → 120 "2027 is when" → 130 "PC version of GTA 6" → 140 "will be released". The video's verdict
  is delivered as a ladder; he closes his eyes and rubs his brow on the 120 rung. Face box 31 → ~37 (hand over face) → 39 → 42 %.

**The 0.8x slow-downs on the face (11 clips, 8 moments), each with Maintain Pitch on; visible as a periodic held frame:**

| time | dur | zoom | line |
|---|---|---|---|
| 0:18.23 | 2.7 s | 136 | "Ladies and gentlemen, everybody is wrong." |
| 1:01.08 | 0.9 s | 110 (in nest) | "the shit out of me." (then the colour bars) |
| 1:09.54 | 1.6 s | 110 | "bro, I heard this and that." (mimicking a friend) |
| 1:12.87 | 1.8 s | 110 | "oh, everyone is going viral." (mimicking) |
| 1:31.21–1:36.35 | 5.1 s, 4 clips | 110 → 110 → 130 → 160 | "okay, add a year and a half… oh… **2028**." — he looks down counting on his hands, then snaps up to the lens at 160 on "2028" |
| 3:45.21 | 2.0 s | 143 | "Making a game for PC" (hands miming a shoe) |
| 3:48.95 | 0.7 s | 110 | "Shaq," (ladder rung 1) |
| 4:48.04 | 1.4 s | 174 | "is your impatience." |

---

## 5. Motion graphics and cue cards: palette and type

**mg1–mg7 (one template).** A 16:9 card with a **diagonal gradient**: slate `#2C2B38` top-left, **magenta `#7C1B4E`** top-right,
**deep teal `#184548`** bottom-left, plum-slate `#302A38` centre. Type is **Montserrat** (geometric, wide): headline Montserrat Black
caps in white `#F6F4FA`; a second line in Montserrat Bold/SemiBold caps in **teal `#37DFDD`** or **hot pink `#FF2E93`**; a numeral
kicker ("01") in pink Black; a **short teal underline rule** (~15 % of the card width) centred under the block. Everything centred.
Motion: the card cuts in blank, the text **fades up over ~0.3–0.5 s** (*looks like* it settles a few px downward into place), the rule
draws out after it; the card itself shrinks with the overlay scale. No exit animation.

| mg | text (exact) | colour of line 2 |
|---|---|---|
| mg1 | FOUR DAYS AGO / THE CEO SPOKE | teal |
| mg2 | STRAUSS ZELNICK / CEO, TAKE-TWO | pink (lighter weight, Medium) |
| mg3 | "MORE AND MORE / IMPORTANT" → "A MEANINGFUL / AUDIENCE" | teal → pink (straight double quotes, the closing quote in the accent colour) |
| mg4 | 01 / PLAYSTATION / SELLS THE MOST | pink "01", teal line 3 |
| mg5 | EVERY PERSON HAS / A DIFFERENT PC | small white line 1, **large teal** line 2 (inverted hierarchy) |
| mg6 | 10 OR 20 / DIFFERENT SETUPS | pink |
| mg7 | 01 / MONEY | pink "01" |

**cue2 / cue10 (AI cards).** Photoreal synthwave Vice City: rain-wet boulevard, hot pink/magenta sky, cyan and pink neon towers, palm
silhouettes, a dark 80s sports car's red tail-lights. White Montserrat ExtraBold caps across the top third, a soft dark shadow, fading
in over ~0.5 s: **COMING TO PC 2028** and **RUMOURED PC 2028 ?** (space before the "?" as shipped).

**Collage + plate.** The collage labels are a **condensed** white caps face (*looks like* Bebas Neue/Oswald) with a tiny lilac year;
the calendar plate has no type (the calendar page is deliberately blurred).

**Colour language of the whole video:** magenta + teal on near-black (matte, mg cards, cue cards, the console render all share it).

---

## 6. Ending (5:00–5:15.7)

5:00.2 face 1x "because this is my call" → the **verdict ladder** 110/120/130/140 ("November / 2027 is when / PC version of GTA 6 /
will be released", 5:01.5–5:07.0) → nest 110 (5:07.0–5:15.7) with the **third SUBSCRIBE bug** running 5:06.3–5:14.7 bottom-left
while he asks for comments ("Are you as a PC player going to wait, or are you going to be like me…") and points off-frame; a 123 %
snap at 5:11.1, a **135 % snap at 5:14.1** on "catch you guys inside at the next one", a flat stare, **hard end on the face** — no
fade (luma flat at 115/255 to the last frame), no end card, no music sting visible.

---

## 7. What this video adds to / contradicts in `presets/youtube/affan-afterhours-facecam/README.md`

**Contradicts**
- **"Nothing is ever an inset, a PiP or a split screen"; game footage "always full-frame and sharp".** Here *every* insert is an inset
  (85–95 %) on an animated magenta/teal matte with a drop shadow. Only the two glitch memes are full frame.
- **Cards grow 8–15 % over the hold; cream condensed type over a blurred game plate.** Here cards **shrink** (−0.5 to −2.8 %/s), sit on
  a flat magenta/teal gradient, use **Montserrat** (geometric, not condensed), white + teal `#37DFDD` + pink `#FF2E93`, a centred
  underline rule, and the type **fades in**. Seven of them (1.3/min), on facts and quotes, not only verbatim tweetable lines.
- **Slow-downs 1–2 per video at 0.5–0.6x.** Here **eight moments / 11 clips, all exactly 0.8x**, mostly on mimicked dialogue and the
  punchline that follows.
- **Cut zooms ~5/min at +25 %.** Here **10.1/min, median 130 %**, p75 149, with ECU extremes at 294 and 356.
- **"Opens on the face."** The first frame is the facepalm meme (as in Game Informer, which opens on the article).
- **The SUBSCRIBE bug "twice per video".** Here **three times**, 8.4 s each, the last one under the outro CTA.
- **"Do not clean up old-game footage"** holds — but the set note does not: the wall here is **pale sage/cream `#C7C78D`–`#DAD7A4`**,
  not lavender or LED green.

**Adds (new devices to name in the README)**
- **The zoom ladder:** 110→120→130→140 on four consecutive hard cuts, one rung per list item; used for an absurd list (3:49) and for the
  video's verdict (5:01).
- **The stretch gag:** Scale Width only (248 / 266 / 928 %), 1–1.5 s, on a word about something fat or clumsy (the PS3).
- **The glitch insert:** 0.2 s SMPTE bars with tone right after a swear; a 0.5 s pillarboxed explosion on "take off in your living room".
- **The cricket beat:** a cricket SFX over a held 1x wide shot and a 4.3 s silence, then a big snap (172 %) on the payoff.
- **The chart punch:** a meme chart shown small, then punched to 281 % into the one row the line names.
- **The slow-down chain:** four 0.8x clips stepping 110→110→130→160 while he counts on his fingers, landing on the number.
- **Overlay scale presets on V3:** 95→87 (cue cards, collage, mg1), 90→85 (footage, mg2–3), 85→80 (mg4–7), statics for stills that
  must not move (Mike York 85, console 126).
