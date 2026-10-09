# Visual catalogue — "Your PS5 Pro Won't Fix GTA 6's 30FPS | GTA 6 Extended Look"

Affan Afterhours, uploaded 2026-08-28 — **the channel's first long-form**, ~9.7k views at audit.
Master read: `raw/ps5-pro.mp4` — the YouTube 1080p download, 1920×1080, **60.00 fps** (the other two early videos are
59.94), **8:18.00** (498.0 s).

Evidence: all 34 contact sheets (`frames/sheet_001–034.jpg`, 2 fps); 52 full-res stills in `frames/full/` named by
second; 10–20-fps strips `frames/step_*.jpg` at the boundaries that matter (first insert, the NYT photo, both colour-bar
hits, the first card entrance, the rack-blur card entrances, the two card punch-ins, the Sony segment, the release-date
slate swap, a 4-fps read of the 0:09.8–0:24.6 face run, the ending). Numbers: a scratch run of the facecam preset's own
`style-probe.py` and `slowmo-scan.py` on this file, an ffmpeg scene-change pass (0.15), a card-box tracker (purple/
magenta mask, every 0.6–1 s), and a word-timed scratch transcript (faster-whisper medium.en). The background `probe/` and
`transcript/words.json` had not landed when this was written; they supersede the scratch numbers when they do.
**"Looks like"** marks an inference. Timecodes ±0.1 s.

**One-line read:** a busy, polished, *Fuel-System-grammar* edit — constant snap zooms with four genuine extreme
close-ups, ~20 game-footage runs, **eight designed Vice City quote cards plus two game-branded stat cards**, card
punch-ins, two colour-bar "channel changes", one meme, colour-matte inset diagrams — told in a bright cyan room with no
glasses. Its numbers sit almost exactly on the 170k Fuel System video (`reference/fuel-system`): it looks like the same
hand cut both.

---

## 1. The face shot

### Framing (YuNet, 824 face samples outside overlays)

| | face-box height (fraction of 1080) | |
|---|---|---|
| p10 (base) | 0.336 | head + shoulders, chest cut by the bottom edge |
| median | 0.367 | the base plus the constant push |
| p90 | 0.535 | 1.6× base — a **quarter of all face time is zoomed ≥ 1.25×, a tenth ≥ 1.6×** |
| max | ~1.06 | a 3× extreme close-up (5:04.9) |

- Face centre x **0.517** (dead centre), face top y 0.255 — the whole `skool` sign sits in the headroom above-right.
- **Gradual push: median 8.1 % per held shot = 1.92 %/s** — every held face shot creeps in (Fuel System 1.79 %/s).
- **Snap (cut) zooms:** the detector logs 92 plausible zoom-ins (≥ ×1.1, held ≥ 0.4 s, outside overlays) = 21 per
  minute of face, median **×1.32** (p25–p75 1.22–1.43), held median 0.8 s. Hand gestures inflate that count: a 4-fps
  read of 0:09.8–0:24.6 (`step_0010_zooms.jpg`) shows three clear snaps (0:15.75 ≈ ×1.35, 0:20.0 ≈ ×1.6 with the head
  turned, 0:23.25 ≈ ×1.3) where the detector found six. By eye on the 2-fps sheets at least ~35 (≈ 8 per minute of
  face). Truth is in between; either way it is the densest zooming of the three.
- **Extreme close-ups (the hits):** 1:23.4 (≈ 1.9×, eyes half-shut deadpan after the 600,000 card — "600,000!"),
  1:58.6 (≈ 2.3×, "Yeah, double it."), 3:22.9 (≈ 2.6×, head tilted, face shoved frame-left — "Somebody made them by hand
  one at a time"), 5:04.9 (≈ 3.2×, eyes wide, face pushed right — "Rockstar doubled the map and multiplied the density
  by 11"). Stills: `full/t_83.4.jpg`, `t_118.6.jpg`, `t_202.9.jpg`, `t_304.9.jpg`.
- He reads off the monitor only briefly (1:11–1:12, 7:45–7:48.5); the rest is to lens.

### The set (the bright, cool version of the room)

- Wall **light cyan-blue `#84B1CA`**, a lavender-pink wash top-left (`#878EAA`), the multicolour `skool` neon fully in
  frame above his left shoulder (frame-right), a small pink framed print left of it, black window grille at the frame-left
  edge, brown leather armchair behind/left, dark monitor at frame-right. Even, soft front key; luma 0.329.
- Wardrobe: **black ribbed knit crew-neck sweater**, a thin chain necklace, a steel bracelet watch on the left wrist,
  **no glasses**. Between 1:15 and 3:00 he turns a small black puck in his fingers (looks like a lens cap).
- Mic: **red-bodied desk mic with a black top** on a stand, lower centre (looks like a HyperX QuadCast-type) — only its
  top shows in the base shot.

### Bugs / lower-thirds / captions / subscribe

No captions, no logo bug, no subscribe animation anywhere (checked all 34 sheets). **Two name tags exist** — on the
portrait cut-ins only (§ 3c).

---

## 2. Cold open (0:00 – 0:35) and the hook to 1:17

| # | in – out | on screen | said |
|---|---|---|---|
| 1 | 0:00.00–0:02.25 | Face, base, both hands open | "Right now, around 4,000 videos are" |
| 2 | 0:02.25–0:04.32 | **GTA 6 trailer**, night Vice City street: a man in pink beaten in the road beside a red sports car (`step_0002_first_insert.jpg`) | "going up about GTA 6's extended" |
| 3 | 0:04.32–0:04.95 | GTA 6 Extended Look: Jason outside a "Market" store, daylight | "look." |
| 4 | 0:04.95–0:05.73 | **Streamer clip**: IShowSpeed cheering in his chair, chat overlay, donation alert, a white "61,076,188" counter | "People reacting to" |
| 5 | 0:05.73–0:06.13 | a streamer's GTA gameplay with his webcam top-left | "it," |
| 6 | 0:06.13–0:09.80 | **YouTube search rows** (his own browser, a VPH extension visible) on a heavily blurred game plate: TSG "GTA 6: Extended Look – EVERYTHING YOU MISSED!" (10K views · 3 hours ago · 2.1K VPH) lower-left, then SubscribeForTacos "GTA 6: Extended Look BREAKDOWN" (25K views · 6 hours ago) upper-left; rows ≈ 80 % wide, drop shadow | "everything you missed, every hit in detail, frame by frame breakdown." |
| 7 | 0:09.80–0:24.63 | Face, 14.8 s, push + snaps at 0:15.75, 0:20.0 (big, hand at temple), 0:23.25 | "This is not that video. Because the craziest thing Rockstar said this week wasn't in the extended look at all… a room in Scotland. And almost nobody has done the actual math on it. So here's what we're doing today." |
| 8 | 0:24.63–0:30.00 | GTA 6 Extended Look: a dark candle-lit motel room, door "308", a man with a red bag | "There is a photograph hanging on a wall in a room inside GTA 6 that you will probably never walk into." |
| 9 | 0:30.00–0:35.25 | Face, hand over mouth | "And what Rockstar did to put that photograph there is genuinely unhinged." |
| 10 | 0:35.25–0:39.52 | **Photo inset**: the New York Times building (low angle), ~55 % wide, square corners, centred, over a blurred game plate that hard-cuts at 0:35.72 | "There's a number Rockstar gave to the New York Times that nobody has processed properly." |

Then: 0:39.5–0:57.6 face (18 s, snaps at 0:47.4 and 0:49.8 ×1.5–1.6, 0:55.0) — "an entire office building in Los
Angeles that exists for one job… you're gonna laugh… if you bought a PS5 Pro… I need you to sit down because I've got bad
news." → **0:57.65–0:57.85 SMPTE colour bars, 0.2 s** (`step_0057_bars.jpg`: clean 7-bar test card) → face "By the end of
this video, you're gonna know" → 0:59.5–1:04.9 GTA 6 montage (scooter past a mural, an airboat in the swamp with the
minimap, a guy shooting hoops under a stilt house) "why GTA 6, a $2 billion game, is still 30 FPS." → 1:04.9–1:07.4 PS5
Slim + DualSense product photo on marble, blue backdrop "Why the more expensive consoles don't fix it." → face to 1:17.2
"…It's not a graphics problem at all. So let's start with the number."

Read: the hook is a **77-second promise list** ("There is a photograph… There's a number… There's an entire office…
And if you bought a PS5 Pro…"), each item illustrated as it is named, then a colour-bar hit, then the thesis. **First
insert at 2.25 s, GTA 6 footage from the first insert.** 18 s of the first 60 s are overlay.

---

## 3. Every overlay, in order

### 3a. Master table

Kinds: **G** game footage (full frame, sharp, HUD left in), **C-VC** Vice City quote card, **C-GM** game-branded stat
card, **I** inset (photo/screenshot/portrait) over a blurred plate, **M** colour-matte inset, **FF** other full frame.

| # | in – out | dur | kind | what (verbatim text where any) | said over it |
|---|---|---|---|---|---|
| 1 | 0:02.25–0:04.95 | 2.7 | G×2 | GTA 6 trailer street beating; Jason at the Market | "…videos are going up about GTA 6's extended look." |
| 2 | 0:04.95–0:06.13 | 1.2 | FF stream ×2 | IShowSpeed reacting; a streamer's gameplay | "People reacting to it," |
| 3 | 0:06.13–0:09.80 | 3.7 | I | two YouTube search rows (TSG, SubscribeForTacos) on blurred plate | "everything you missed… frame by frame breakdown." |
| 4 | 0:24.63–0:30.00 | 5.4 | G | motel room 308 | "There is a photograph hanging on a wall in a room…" |
| 5 | 0:35.25–0:39.52 | 4.3 | I | NYT building photo, blurred plate | "There's a number Rockstar gave to the New York Times…" |
| 6 | 0:57.65–0:57.85 | 0.2 | FF | **colour bars** | "By" |
| 7 | 0:59.47–1:04.87 | 5.4 | G×3 | scooter/mural, airboat, basketball | "why GTA 6, a $2 billion game, is still 30 FPS." |
| 8 | 1:04.87–1:07.38 | 2.5 | FF photo | PS5 Slim + controller on marble, blue backdrop | "Why the more expensive consoles don't fix it." |
| 9 | 1:17.20–1:22.30 | 5.1 | **C-VC** | " **GTA 6 has over 600,000 NPC animations** " — R★ tile, "ROCKSTAR GAMES → THE NEW YORK TIMES" | "Rockstar told New York Times that GTA 6 has over 600,000 NPC animations." |
| 10 | 1:29.57–1:33.15 | 3.6 | **C-GM** | "**GtA 5: 55,000 npc animations**" (GTA V card) | "GTA 5, 2013, 55,000 animations." |
| 11 | 1:33.15–1:36.25 | 3.1 | **C-GM** | "**RDR 2: 300,000 NPC ANIMATIONS**" (Red Dead card) | "Red Dead Redemption 2, 2018, around 300,000." |
| 12 | 1:38.73–1:43.32 | 4.6 | G×4 | RDR2: snow, Arthur leading a horse, Valentine | "That's the game where snow left footprints. Where mud stuck to your coat." |
| 13 | 2:02.13–2:08.73 | 6.6 | G×3 | GTA 6 rooftop bar (Extended Look), interior, older couple | "Animation isn't a texture. Animation isn't a building… a thing a person does." |
| 14 | 2:14.02–2:17.57 | 3.6 | I portrait | **Aaron Garbut** headshot + name tag | "This is Aaron Garbut. He is the co-studio head of Rockstar North." |
| 15 | 2:20.30–2:23.38 | 3.1 | G×2 | GTA 6 liquor-store robbery ("Rough Seas Smoothest Rum $10.99") | "…one of the actual people running the studio on the record." |
| 16 | 2:26.53–2:32.93 | 6.4 | **C-VC** | Garbut quote 1 (§ 3b) | read verbatim |
| 17 | 2:44.67–2:56.35 | 11.7 | **C-VC** | Garbut quote 2 (§ 3b); plate hard-cuts dark interior → bright windows at 2:46.7 | read verbatim |
| 18 | 3:00.95–3:03.88 | 2.9 | FF | animated **GTA VI logo** building on dark navy | "…sitting there and watching the extended look," |
| 19 | 3:05.10–3:11.38 | 6.3 | I screenshot | **his own notes** in a dark text editor, three **red arrows** added at "black culture tatoos", "everyone has a personality", "every place has its own culture"; the list includes "holy shit insane difference from gta 5" and "fkin ai vids", unredacted | "I wrote everything has a personality. I wrote every place has its own culture. I wrote down the tattoos." |
| 20 | 3:27.12–3:31.72 | 4.6 | G×2 | aerial over a Vice City rooftop + mural; rooftop party | "an entire office in Los Angeles dedicated to NPCs" |
| 21 | 3:38.07–3:38.27 | 0.2 | FF | **colour bars** (same clean card) | "No," → "look, I know how I sound right now." |
| 22 | 3:44.45–3:45.92 | 1.5 | I portrait | **Berkay Dursen** photo + name tag | "This is Berkay Dursen," |
| 23 | 3:45.92–3:49.03 | 3.1 | G | rooftop couple, "HOLD HANDS" prompt | "a developer at IO Interactive… crowd systems." |
| 24 | 3:54.28–3:57.20 | 2.9 | **C-VC** on black | "Atleast **10 years** ahead of the industry" – BERKAY DURSEN; **punch-in** at 3:55.9 | "At least 10 years ahead of the industry." |
| 25 | 3:59.10–4:05.95 | 6.9 | **C-VC** | Berkay quote 2 (§ 3b) | read verbatim |
| 26 | 4:16.60–4:26.97 | 10.4 | G×5 | night tower, woman taking a selfie in a car, pool party, drift race (PROGRESS HUD) | "Anybody can make a beautiful street. Rob Nelson…" |
| 27 | 4:26.97–4:39.62 | 12.7 | **C-VC** | Rob Nelson map quote, **rack-blur + fade in**, **punch-in** at 4:38.3 | read verbatim |
| 28 | 4:48.72–4:52.67 | 4.0 | G×2 | Vice City skyline silhouette at sunset; boat | "only so much attention that you can put…" |
| 29 | 4:56.43–5:00.45 | 4.0 | G×2 | a Rockstar livestream clip (chat panel, "LIVE 53k", "VIEW LIVESTREAM"); beach with a banner plane | "Every open world… has had to pick one: big or dense." |
| 30 | 5:10.40–5:16.12 | 5.7 | **C-VC** | " **GTA 6 is currently running 30 fps ON EVERY CONSOLE** " – ROB NELSON / ROCKSTAR | "Rob Nelson confirmed GTA 6 is currently running 30 frames per second on every console." |
| 31 | 5:29.30–5:31.90 | 2.6 | FF meme | a man in a Lakers #23 jersey in a kitchen slamming a gaming laptop shut (handheld phone video) | "it's the console, PS5 is six years old." |
| 32 | 5:38.18–5:41.33 | 3.2 | **M** | flat **green matte `#0B925A`**, a small cut-out PS5 Slim + controller on white with a drop shadow; then a cut-out Sony APU die photo ("SONY INTERACTIVE ENTERTAINMENT INC CXD90044GB") | "Your console has two brains. You've got this GPU." |
| 33 | 5:41.33–5:47.77 | 6.4 | G×2 | strip club (Jason throwing cash); street race (LAP 1/2, position counter) | "The GPU draws the picture, lighting, reflections…" |
| 34 | 5:47.77–5:49.57 | 1.8 | **M** | flat **plum matte `#8A006A`**, a photo of the APU on a green PCB, drop shadow | "You've got the CPU." |
| 35 | 5:49.57–5:56.60 | 7.0 | G | a guy in a green #69 jersey running with a bag, hopping on a motorbike (wanted stars) | "The CPU runs the world where every single person is…" |
| 36 | 6:04.72–6:17.43 | 12.7 | FF promo | **Sony PS5 Pro reveal** (black console, light-speed streaks, blue burst) → **Marvel's Wolverine** trailer (blood, motorbike, snow) → white PS5 + DualSense studio shot (`step_0602_sony.jpg`) | "So the PS5 Pro is a GPU upgrade… The CPU barely moved…" |
| 37 | 6:23.17–6:35.90 | 12.7 | G×3 | night convertible + intersection explosion; a woman on a rooftop edge then skydiving; couple on a night runway by a private jet | "…physics on land, at sea and in the air… lands on the half of the console that was never struggling." |
| 38 | 6:41.10–6:57.65 | 16.6 | G → **C-VC** | red convertible on a highway (MIO truck), **blurs over 6:43.0–6:43.7**, then the Digital Foundry card fades in (`step_0641_cardblur.jpg`) | "Digital Foundry looked at this properly…" read verbatim |
| 39 | 7:05.48–7:14.50 | 9.0 | G | shootout: a guy in a cap fires from behind a car, a police truck flips | "Every single one of those 600,000 animations is a cost…" |
| 40 | 7:25.85–7:32.33 | 6.5 | I slate | the trailer end slate (GTA VI logo, "COMING 2025", R★) in a black box ~92 % wide over a blurred plate, **hard-swapped at 7:29.9 to "MAY 26, 2026"** (`step_0730_slate.jpg`) | "December 2023, we get the trailer. They say 2025… pushed to May 2026" |
| 41 | 7:32.33–7:36.22 | 3.9 | I screenshot | X post, Rockstar Games @RockstarGames, X.com: "Hi everyone, Grand Theft Auto VI will now release on Thursday, November 19, 2026. We are sorry for adding additional time…" | "Pushed again to November 19th, 2026." |
| 42 | 7:48.98–7:51.88 | 2.9 | G | **GTA V** first-person shooting | "GTA V shipped with a full first person mode." |
| 43 | 7:55.30–8:02.92 | 7.6 | I screenshot | Google AI answer: "Grand Theft Auto 6 is confirmed to be a single-player experience at launch." + "Launch Details" bullets | "Every official description of this game says the three words: single player experience." |

**46 overlay events (5.5/min) in 33 runs (4.0/min), 46 % of runtime; median run 5.7 s; face 54 %.** 18 game runs
(~20 if the montage pieces are split), 10 cards (8 Vice City + 2 game-branded), 4 screenshots, 2 portraits, 2 colour
mattes, 2 colour-bar hits, 1 meme, 1 Sony promo segment, 1 logo animation, 1 slate. **Six cards are quotes, four are
numbers** — every card is a sentence he is saying, set in type.

### 3b. Card detail

**Template C-VC — the Vice City quote card (8 cards: 600k, Garbut ×2, Berkay ×2, Nelson ×2, Digital Foundry)**

- **Card:** a 16:9 landscape panel with very slightly rounded corners and a hard edge, **drop shadow down-right**, no
  tilt. Background art: **deep royal blue `#0427B5` at the left → magenta-purple `#4E0060`–`#80006D` → hot pink at the
  lower right**, palm silhouettes on both edges, a Vice City skyline with a setting sun and water reflections along the
  bottom. Inside it, a **second rounded rectangle drawn as a thin neon line** (pink-violet glow, ~3 px, radius ≈ 40 px)
  inset ~5 % — the text lives inside that frame.
- **Type:** **white, heavy geometric grotesque, sentence case** (Poppins/Montserrat ExtraBold class — not condensed),
  left-aligned, tight leading, 4–10 lines. **Accent phrase in hot pink `#E70C89`–`#EA1EB1`**, same weight, sometimes in
  CAPS ("ON EVERY CONSOLE", "NOT A CROWD", "ALL OF THEM"). **Oversized pink typographic quote marks** “ ” open and close
  the block. Attribution: "- NAME" in pink caps over a smaller muted-pink "ROCKSTAR" / "ROCKSTAR NORTH", under a thin
  rule; the Garbut and 600k cards instead carry a **pink-purple R★ app-icon tile** + name block bottom-right.
- **Size & motion (tracked):** 600k 66 → 71 % wide over 5.4 s; Garbut 2 71 → 82 % over 11 s; Berkay 2 76 → 79 % over
  6.2 s; 30 fps 81 → 88 % over 4.8 s; DF 75 → 86 % over 12 s — **centred, growing ~1–2 %/s, nothing on the card
  animates.** Plate = heavily blurred game footage, still moving, may hard-cut behind the card (Garbut 2 at 2:46.7,
  Berkay 2 at 4:00.9). **Exception: the Berkay "10 years" card sits on pure black** (89 % wide, no plate).
- **Entrance:** hard cut (600k, Garbut ×2, Berkay ×2, 30 fps) — or a **rack-blur**: the game shot under the line blurs
  out over ~0.6 s, then the card **fades in over ~0.3–0.4 s** while semi-transparent (Nelson map 4:26.3, DF 6:43.0–6:44.1).
  **Exit:** hard cut.
- **Card punch-ins (a device):** 3:55.9 the "10 years" card snaps to ~250 % so "10 years / ahead of / the industry" fills
  the frame for 1.3 s; 4:38.3 the Nelson card snaps to ~300 % on "…los santos. And my own playthrough I think took me
  around 80 hours." for 1.35 s (`full/t_236.3.jpg`, `t_278.5.jpg`).
- **Verbatim text (typos kept):**
  1. 1:17 — "GTA 6 / has over / **600,000** / NPC animations" · R★ ROCKSTAR GAMES → THE NEW YORK TIMES
  2. 2:26 — "Every room in the game somebody thought about this who's sitting there, what they're drinking. **The marks
     that are left on the table**" · AARON GARBUT / ROCKSTAR NORTH
  3. 2:44 — "The pictures on the wall will have people that are in that room with their tattoos on their arms and their
     family behind them. **The whole thing has been made and built and photographed and placed in this random room**" ·
     AARON GARBUT / ROCKSTAR NORTH
  4. 3:54 — "Atleast **10 years** ahead of the industry" · - BERKAY DURSEN *("Atleast" sic)*
  5. 3:59 — "GTA 6 is simulating every single **character** NOT A CROWD **individuals..** **ALL OF THEM** at the same
     time" · - BERKAY DURSEN
  6. 4:27 — "The map is twice the size of GTA 5 three times the size of RDR2 **Vice city on it's own is double the size
     of los santos.** And my own playthrough I think took me around **80 hours.**" · - ROB NELSON / ROCKSTAR *("it's" sic)*
  7. 5:10 — "GTA 6 is currently running **30 fps ON EVERY CONSOLE**" · - ROB NELSON / ROCKSTAR
  8. 6:44 — "The crowd simulation in this game is **in order of magnitude harder** than the most demanding simulation
     games on console. The vehicle physics across grounds sea and air are the kind of expense that normally forces a
     game **down to 30 frames**" · - DIGITAL FOUNDRY *("in order of", "grounds" sic)*

**Template C-GM — the game-branded stat card (2 cards, a comparison run with card 1)**

- **GTA 5 (1:29.6):** "GtA 5: / **55,000** / npc animations" in a **Pricedown-style** GTA face, white with a black
  outline; "55,000" in a **yellow-green gradient `#CDD95C`→`#98AE2B`** with a dark outline; Franklin from behind on the
  Del Perro pier holding a money bag, the GTA V logo bottom-left, an R★ tile bottom-right. ~73 % wide over a blurred GTA V
  plate.
- **RDR 2 (1:33.2):** "RDR 2: / **300,000** / NPC ANIMATIONS" in a condensed western display face, cream + **red
  `#AE0003`**, Arthur aiming a revolver, a red-orange sun, a line of riders, stars. ~73–76 % wide over a blurred plate.
- **Hard cut card to card**, no face between: 600k (pink) → 55k (green) → 300k (red). The **colour code is per game** —
  the same "GTA 5 = green" the README found in Fuel System.

### 3c. Other inset treatments

- **Portrait cut-in with a name tag (2):** a portrait-format headshot centred full height, the side bars filled with a
  **blurred, enlarged copy of the same photo**, and the name in **white heavy condensed caps (Anton/Bebas class) with a
  dark shadow**, centred low on the photo: "AARON GARBUT" (2:14), "BERKAY DURSEN" (3:44). The only name straps in the three
  videos.
- **Found screenshots on a blurred plate (4):** YouTube rows, his notes (with three hand-placed **red arrows**), the
  Rockstar tweet, the Google AI answer — square corners, drop shadow, ~55–92 % wide, over defocused game footage.
- **Colour-matte inset (2):** a small product/chip cut-out with a drop shadow, centred on a **flat full-frame colour**
  (green `#0B925A`, plum `#8A006A`) — the earliest sighting of the matte idea CREATOR-HAND records from 09-30.
- **The slate swap (7:25.9 → 7:29.9):** two trailer end slates boxed in black over a blurred plate, the date hard-swapped
  in place — the edit "says" the delay.

---

## 4. Recurring patterns

- **Show the noun.** Each item of the promise list, each number and each named person gets its picture the moment it is
  said (the motel room for "a photograph on a wall", the NYT building for "the New York Times", Garbut's face for "This
  is Aaron Garbut").
- **Card runs:** 600k → 55k → 300k (1:17–1:36, three numbers, ~11 s with one 7-s face beat), Garbut 1 → Garbut 2,
  Berkay 1 → Berkay 2 — quotes are split into two cards around a face reaction ("The marks that are left on the table."
  repeated to camera; "That's not the unhinged part. This is.").
- **Game runs are long and slowed-looking:** median overlay run 5.7 s; the 4:16.6 night montage and the 6:23–6:36 run
  each carry 10–13 s. The duplicate-frame scan reads ≈ 0.5× on most GTA 6 inserts — consistent with either 0.5× slow
  motion or 30-fps trailer footage on a 60-fps timeline; it cannot tell which.
- **Cut rate:** probe 13.9 cuts/min (by minute 11/15/16/18/8/14/18/14), scene-change pass ≈ 29 visible changes/min
  including the snap zooms. Longest face stretch 18.8 s; face runs median 6.3 s.
- **Words:** 190/min, zero pauses ≥ 1 s.

## 5. Comedy and emphasis devices

| device | where | spec |
|---|---|---|
| **colour-bar channel change** | 0:57.65, 3:38.07 | clean SMPTE bars, 0.2 s, on the turn from the hook into the promise ("By the end of this video") and from the Garbut section into "No, look, I know how I sound right now" |
| **extreme close-up** | 1:23.4, 1:58.6, 3:22.9, 5:04.9 | 1.9–3.2×, two of them off-centre (broken composition), on "600,000!", "Yeah, double it", "made them by hand", "multiplied the density by 11" |
| **card punch-in** | 3:55.9, 4:38.3 | the quote card itself snaps to 250–300 % on its last words |
| **the reaction meme** | 5:29.3 | 2.6 s laptop-slam clip as "the Internet" saying "it's the console" |
| **self-receipt** | 3:05.1 | his own raw notes, swearing left in, red arrows on the three lines he quotes |
| **the date swap** | 7:29.9 | COMING 2025 → MAY 26, 2026 on the same slate |
| **repeat-to-camera** | 2:33 | reads the card's pink line again to lens: "The marks that are left on the table." |

## 6. Palette and type

- Room: cyan `#84B1CA` + lavender, warm neon, black sweater, red mic.
- Cards: royal blue `#0427B5` → magenta `#80006D`/`#4E0060`, accent **hot pink `#E70C89`–`#EA1EB1`**, white text;
  game cards green `#CDD95C`/`#98AE2B` (GTA 5) and red `#AE0003` (RDR 2); mattes green `#0B925A`, plum `#8A006A`.
- Type: card body = heavy geometric sans, sentence case; name tags = heavy condensed caps; GTA 5 card = Pricedown-style;
  RDR2 card = western condensed. No captions.

## 7. Ending (8:03 – 8:18)

8:02.9 hard cut from the Google AI answer to the face for the last **15.1 s**, no inserts: "nobody at Rockstar said a word
about online. Now, was it worth it? 12 years later, over a billion dollars, close to two billion, photographs in rooms
you'll probably never walk into, playing at 30 frames per second. On November 19th, we'll find out ourselves." Snaps at
8:12.5 (≈ ×1.5) and **8:17.0 (≈ ×1.4), which is the last frame** — the video **cuts out on a zoomed face**, no
CTA, no end card, nothing reserved for end screens (`step_0809_end.jpg`).

## 8. Differences vs README.md and CREATOR-HAND.md

| doc says | PS5 Pro does |
|---|---|
| ~20–25 visible changes/min; cut zooms +25 %, ~5/min (README) / 121–136 % median, 4–10/min (CREATOR-HAND) | consistent: median ×1.32, dense (8–21 per minute of face), four 1.9–3.2× extremes — **closest of the three to Fuel System's grammar** (push 1.92 %/s vs Fuel 1.79; detector 196 snap-ins vs Fuel 143) |
| Face ~80 % of runtime (README); 73 % (CREATOR-HAND) | **54 %** — the most overlay-heavy of all measured videos |
| Overlay runs ~4 s, 3–4/min | 4.0 runs/min but median **5.7 s**, several 10–17 s runs |
| Posters ~72 % of frame, grow 8–15 %, hard cut in/out, Anton/League Gothic condensed caps in cream `#F6F1DC`, one pink word | the card is a **different template**: blue→magenta Vice City panel with an inner neon frame, **white sentence-case geometric sans**, a whole pink *phrase*, pink quote marks; 66–89 % wide, grows 1–2 %/s ✔; two fade/rack-blur entrances ✘; card punch-ins (not in either doc) |
| Card colour code pink = GTA 6, green = GTA 5 | ✔ and extended: **red = RDR 2** |
| No lower-thirds, no name tags | **two name tags** on portrait cut-ins |
| Nothing is ever an inset (README) / inset over a colour matte since 09-30 (CREATOR-HAND) | insets on blurred plates throughout; **two flat colour mattes already on 08-28** |
| Colour-bars glitch is the creator's (CREATOR-HAND, PC/CB) | ✔ present twice, clean SMPTE bars, 0.2 s |
| Subscribe animation twice (README) | none |
| Ends cold on the face | ✔ (on a snap zoom) |

**Earlier-era markers:** cyan wall, black knit sweater, no sunglasses, desk-stand mic — the later look (coral wall,
sunglasses, a lav on a prop) is not here yet. The Vice City quote-card template (blue→pink, inner neon frame, white
geometric sans) and the per-game stat cards are this era's card system; it carries into NPC AI unchanged.
