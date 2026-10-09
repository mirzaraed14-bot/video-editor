# Visual catalogue — "GTA 6: The Most COMPLEX Crime System Ever Made (REVEALED)"

Frame-by-frame dissection of the editing style. Source: `raw/crime-system.mp4` — YouTube download,
1920×1080, 59.94 fps H.264, 6:06.18 (366.18 s). Uploaded 2026-09-03, 10.7k views (channel V6 in
`X:\Claude Projects\GTA 6\`; core points `video6-never-forgets-core-points.md`). Cut by: not recorded.

**Evidence** (all in `frames/`): 25 contact sheets at 2 fps (`sheet_001–025.jpg`, every one read);
~70 full-res stills + 8 labelled tiles in `frames/detail/` (`t_coldopen`, `t_cardsA`, `t_qentry`,
`t_misc1`, `t_hud`, `t_collage`, `t_zoomcheck`, `t_end`); a WhisperX large-v3 word transcript made for
this catalogue (`frames/catalogue-words.json`; the background job's `transcript/words.json` had not landed
when this was written); a **zoom proxy track** (`frames/catalogue-lens-zoom.tsv`: the distance between his
red lens centres, 4 fps — a background-matching scan was unreliable on this video's LED-lit wall, so the
glasses are the ruler); an ffmpeg `scdet` cut list (108 visual changes after merging); a per-frame
duplicate scan at native 59.94 (speed changes); a bottom-left pixel scan for a subscribe bug; card
bounding boxes measured at entry and exit. **"Looks like"** marks an inference.

---

## 1. The face shot

### Framing and set
- **One locked camera, same room as DIRTIEST and RISKIEST**, framed a little wider: medium shot, head
  ≈ 30 % of frame height at the widest (4:07), chest and both arms in, the chair back and the monitor
  fully in frame. Face centre x ≈ 0.50.
- **Back wall: saturated LED green** `#6DD87D` with a **lavender/pink wash** around the small framed print
  upper-left of his head. The **`skool` neon sits above his head**, fully readable in the base shot (in
  DIRTIEST it hides behind his head).
- **Brown leather armchair** `#543125` left third, **dark monitor bezel** right third, a dark window grille
  at the far left edge.
- No mic on a stand; a **small round teal/green device clipped at the chest** (looks like a wireless lav
  transmitter). At times he handles a small white object (0:41, 4:16, 5:29 — looks like a phone or note).

### Wardrobe
- **Maroon sleeveless tee** `#4D0414` with the tonal **"GOING ALL IN / EST.21"** print (the same tee
  design as DIRTIEST, other colour).
- **Red-orange-lensed glasses** (lens `#B81500`, black frames) — the "red shades" look.
- Watch on the left wrist, bracelets, full beard. No change through the video.

### Zoom levels (lens-distance proxy, `catalogue-lens-zoom.tsv`; widest = 1.00)
| level | relative size | where |
|---|---|---|
| base | 1.00–1.10 | most face runs (he leans, so ±10 % is body movement, not editing) |
| cut zoom | **≈ 1.30–1.62**, held 0.7–3.5 s | ≈ 17 in the video (≈ 2.8/min) |
| biggest | 1.60–1.62 | 1:07.63 "how stupid **the old world was**", 4:04.93 "one more **state I haven't told you about**" |

- **Almost every cut zoom arrives on a hard cut** (the new take is already tight) and lasts one phrase:
  0:11.99 "Here's what's in this video." · 0:32.35 "the whole time." · 0:52.50 "cold-blooded. That's at
  the end…" · 1:07.63 "the old world was." · 1:13.99 "massacre." · 1:44.79 "His exact words," · 1:48.17
  "**persistent memory.**" · 2:26.81 · 3:12.11 (→ 1.62 at 3:15.3) · 3:21.07 · 3:29.56 · 3:36.57 "There are
  four classifications." · 4:04.93 · 5:09.9 (inside the take, 1.12 → 1.42) · 5:21.67 · 5:40.62 "Just like
  your ancestors did in GTA 5, 4, 3," · **6:04.53 "You're just not anonymous anymore."** (the last shot).
- **Gradual push: not measurable / looks like none.** Runs that hold still (5:11.8–5:17.9, 5:25.2–5:33.5,
  4:06.0–4:11.9) stay within ±3 % — the 110 %-per-run drift seen in DIRTIEST is absent here.
- Face share **62 %**, **31 face runs**, median 7.8 s, longest 18.6 s (4:59.3–5:17.9).
- **No face slow-downs.** The duplicate scan finds no 0.8× (or any) speed change on the face; the
  irregular duplicates at 3:30–3:34, 5:21–5:25 and 5:53 are him holding still.

### Bugs, lower-thirds, captions
- **No captions, no lower-third, no logo bug, no name strap.**
- **No SUBSCRIBE animation** at all (bottom-left scanned at 10 fps — zero hits; DIRTIEST has five).

---

## 2. Cold open (0:00 – 1:00.9) — the promise stack

**It opens on game footage, not the face**: the voice is running from frame 0 over a GTA 6 strip-club
clip. 23 visual changes in minute 1 (the fastest minute). No title card, no logo sting.

| # | in – out | dur | on screen | what's said |
|---|---|---|---|---|
| 1 | 0:00.00–0:02.47 | 2.5 | GTA 6 trailer: a man in a plaid shirt throwing cash at a pole dancer, button prompt "THROW" bottom-right | "GTA 6 does something that no" |
| 2 | 0:02.47–0:04.80 | 2.3 | Race gameplay: white touring car, HUD "LAP 1/2 · 10/16 · 00:19.64" + minimap (looks like GTA 6 Extended Look) | "GTA has ever done before." |
| 3 | 0:04.80–0:09.39 | 4.6 | Face, finger up; jump cut 0:08.19 | "It remembers everything. Whole world remembers you. Not just the police officer." |
| 4 | 0:09.39–0:11.99 | 2.6 | Trailer: motel lot, man in a black tank and a woman in a lilac dress by a classic car | "Random people on the street, they remember you." |
| 5 | 0:11.99–0:13.40 | 1.4 | **Face, cut zoom ≈ 1.5 on a hard cut** | "Here's what's in this video." |
| 6 | 0:13.40–0:16.37 | 3.0 | Face, back to base | "The cops in this game don't just chase you anymore." |
| 7 | 0:16.37–0:17.78 | 1.4 | Trailer: Lucia and a partner in bandana masks in a liquor store ("$14.99"), then outside "Food Mart" | "They remember your face," |
| 8 | 0:17.78–0:18.68 | 0.9 | Trailer: Lucia holding up two outfits | "your outfit," |
| 9 | 0:18.68–0:20.90 | 2.2 | Gameplay: a man in black walks up to a parked red car | "Your car, you guys probably know about this already." |
| 10 | 0:20.90–0:23.31 | 2.4 | Face | "Now this is something that you don't know. Who you were with." |
| 11 | 0:23.31–0:26.40 | 3.1 | Gameplay: shoot-out behind a car, police cruiser, 4 wanted stars (cuts 0:24.32, 0:25.02) | "And escaping doesn't mean forgetting, because there are tiers" |
| 12 | 0:26.40–0:28.00 | 1.6 | **HUD magnifier #1** (§3c): the top-right HUD of the same footage — 4 stars, 4 heat icons, "39 221", rifle — blown up on a black panel over the blurred footage | "of stars now." |
| 13 | 0:28.00–0:35.97 | 8.0 | Face (cut zoom 1.31 at 0:32.35) | "I'm gonna explain everything, I'll show you exactly what I mean, because it's on your screen the whole time. The game will now also keep a psychological profile." |
| 14 | 0:35.97–0:38.99 | 3.0 | **Collage**: four slanted portrait panels of GTA 6 characters (official character-art stills), slow push | "There are four classifications it can put you in." |
| 15 | 0:38.99–0:48.78 | 9.8 | Face (jump cut 0:47.76) | "Most people haven't seen the names yet. And then there's the thing I actually made this video for. There is a state in GTA 6 from which you can never come from. And when you hear" |
| 16 | 0:48.78–0:52.50 | 3.7 | **Rockstar logo card**: white R★ with a soft glow on a blue → magenta gradient with palm-frond silhouettes, slow push | "Rockstar's reasoning on why they did this, it's honestly a little cold-blooded." |
| 17 | 0:52.50–1:00.88 | 8.4 | Face: cut zoom 1.41 on "cold-blooded. That's at the end", back to base 0:55.02 | "…I promise it is worth it. Because here's the sentence which explains this whole game. Comes from Rob Nelson, co-head of development at Rockstar." |
| 18 | 1:00.88 → | | **Quote card #1** "This is a world THAT'S NOW WATCHING YOU" — the body starts on the thesis | |

Every promise in the stack gets its own picture **on the noun**: face → masks, outfit → the outfit
clip, car → the car, tiers of stars → the HUD itself, four classifications → four faces, Rockstar → the
logo.

---

## 3. Every overlay, in order

### 3a. Master table

Treatment key: **FF** = full frame, sharp, HUD left in; **QUOTE** = the neon Rob Nelson quote card (§3b);
**HUD** = HUD magnifier inset (§3c); **WHITE** = inset on a pure-white page (§3d); **ART** = found key art /
logo, full frame, slow push. Game footage plays at **1×** (30 fps sources on the 59.94 timeline); no
slow-mo on any insert.

| # | in – out | dur | what | treatment | what's said |
|---|---|---|---|---|---|
| 1 | 0:00.00–0:02.47 | 2.5 | Strip club, cash throw (GTA 6 trailer) | FF | "GTA 6 does something that no" |
| 2 | 0:02.47–0:04.80 | 2.3 | Race HUD gameplay | FF | "GTA has ever done before." |
| 3 | 0:09.39–0:11.99 | 2.6 | Motel couple | FF | "Random people on the street, they remember you." |
| 4 | 0:16.37–0:17.78 | 1.4 | Masked pair, liquor store → Food Mart (2 clips) | FF | "They remember your face," |
| 5 | 0:17.78–0:18.68 | 0.9 | Lucia's two outfits | FF | "your outfit," |
| 6 | 0:18.68–0:20.90 | 2.2 | Man walks to a red car | FF | "Your car, you guys probably know about this already." |
| 7 | 0:23.31–0:26.40 | 3.1 | Shoot-out, 4 stars (3 clips) | FF | "And escaping doesn't mean forgetting, because there are tiers" |
| 8 | 0:26.40–0:28.00 | 1.6 | **HUD magnifier #1** — stars / heat icons / ammo / rifle | HUD | "of stars now." |
| 9 | 0:35.97–0:38.99 | 3.0 | Four-character slanted collage | ART | "There are four classifications it can put you in." |
| 10 | 0:48.78–0:52.50 | 3.7 | Rockstar logo card | ART | "Rockstar's reasoning on why they did this, it's honestly a little cold-blooded." |
| 11 | 1:00.88–1:03.66 | 2.8 | **“This is a world THAT'S NOW WATCHING YOU”** | QUOTE | "This is a world that's now watching you." |
| 12 | 1:09.02–1:11.14 | 2.1 | **Key-art split**: GTA V cover trio (Michael, Trevor, Franklin) left · RDR2 Arthur with revolver right, diagonal seam | ART | "Red Dead Redemption 2 and GTA 5." |
| 13 | 1:14.67–1:18.18 | 3.5 | **GTA V**: tank on the Fort Zancudo runway, attack helicopter, 5 stars, explosion | FF | "Full three block helicopter and tank massacre. And then" |
| 14 | 1:18.18–1:20.30 | 2.1 | **GTA V**: dark sedan in a tunnel garage driving toward the light, 4 stars | FF | "drive into an alley, sit there" |
| 15 | 1:28.79–1:32.68 | 3.9 | **GTA V**: Michael taking a phone selfie in front of a run-over pedestrian | FF | "So the GTA V world has the memory of a goldfish. It remembers absolutely nothing." |
| 16 | 1:42.05–1:44.79 | 2.7 | **“lose the cops and then they FORGET ABOUT YOU INSTANTLY”** | QUOTE | "They wanted to get past the era where lose the cops and then they forget about you instantly." |
| 17 | 1:55.03–≈1:56.5 | 1.5 | GTA 6 official key art (Jason and Lucia, guns drawn, on a dock), sharp | ART | "This game has been in development for" |
| 18 | ≈1:56.5–1:57.47 | 1.0 | **Same art blurred + "13 YEARS"** in huge white condensed caps, centred (hard switch, no animation) | ART + text | "13 years, right?" |
| 19 | 2:02.49–2:04.89 | 2.4 | Gameplay: a woman in a "DON'T TRIP" leather jacket walks into a convenience store, wanted HUD | FF | "First, someone has to actually see your crime." |
| 20 | 2:04.89–2:07.13 | 2.2 | Liquor store: a man in a cap grabs the clerk | FF | "Cops don't magically know anymore." |
| 21 | 2:10.58–2:14.58 | 4.0 | A man in a hoodie and shades filming someone on his phone | FF | "Which means every random pedestrian is now an actual pair of eyes." |
| 22 | 2:19.74–2:26.81 | 7.1 | Gameplay: a woman parks a red convertible, walks to a pawn shop (ZEKES GADGETS / WE DO REPAIRS / JOYERIA EMPEÑOS), pulls up a bandana; two bystanders watch and leave | FF | "and we saw that in the extended look when Lucia was walking into the store you could see two people they saw her holding the gun and they walked away" |
| 23 | 2:38.09–2:46.27 | 8.2 | **“there's a row of little icons. those are called HEAT INDICATORS. …”** (plate cuts 2:39.76, 2:41.53) | QUOTE | "there's a row of little icons those are called heat indicators and every single one is a fact the police currently remember about you" |
| 24 | 2:46.27–2:52.36 | 6.1 | **HUD magnifier #2** — the four heat icons alone on a black panel (plate cut 2:50.0) | HUD | "they've seen your face icon they know your outfit there's an icon for that too they know your car that's an icon also" |
| 25 | 3:01.23–3:08.07 | 6.8 | Gameplay: bandana-masked woman throws a molotov, the car goes up in flames, 4 stars | FF | "…change your clothes burn your car we saw that in the extended look so you have to go and physically delete all of your evidence" |
| 26 | 3:08.07–3:12.11 | 4.0 | **HUD magnifier #3** — sky crop with power lines, six stars (2 grey, 4 red) and three heat icons | HUD | "and when you lose the cops they don't vanish they turn red" |
| 27 | 3:16.90–3:19.15 | 2.3 | **Social-post infographic "GTA VI / CRIMINAL PROFILE / SYSTEM"** (carousel slide "3/5") | WHITE | "it's called criminal profile you've" |
| 28 | 3:22.64–3:25.37 | 2.7 | Gameplay: Jason petting a dog in a dim room, prompts SCOLD / PET / … | FF | "when jason pets a dog or robs a store" |
| 29 | 3:33.85–3:36.57 | 2.7 | **Found webcam clip of the YouTuber TGG** (white headset, Tommy Jeans tee, green screen), smiling; no name label | FF (found) | "TGG, he got this directly from Rob Nelson." |
| 30 | 3:40.30–3:43.51 | 3.2 | The four-character collage again | ART (reuse) | "are Professional, Aggressive, Violent and Psycho." |
| 31 | 3:49.96–3:53.65 | 3.7 | The "DON'T TRIP" woman walking the store aisles (same source as #19) | FF | "Do you rob a store with restraint and control? In and out, nobody heard." |
| 32 | 3:55.74–3:59.19 | 3.5 | **GTA V**: fighter jet dogfight, explosions | FF | "Either you can be the dumbass just shooting every block, robbing shit," |
| 33 | 4:11.94–4:15.02 | 3.1 | **GTA V**: yellow convertible ploughing through pedestrians on the Vespucci boardwalk | FF | "cruelty, randomly running people over, causing mayhem in buildings," |
| 34 | 4:26.13–4:32.27 | 6.1 | The dog-petting clip again (longer) | FF (reuse) | "you can't just pet a random dog for five minutes and lose all your stars or get all that good karma" |
| 35 | 4:42.55–4:46.27 | 3.7 | **RDR2 gameplay** (Arthur brawling on a mountain ledge) as a small inset | WHITE | "In that game, you could play 60 hours and be a complete monster." |
| 36 | 4:55.38–4:59.32 | 3.9 | GTA Online key art: a man in a suit and sunglasses lying on a bed of cash, champagne, clown mask | ART | "Rockstar looked at this and were like, no, no, no, no, not this time." |
| 37 | 5:17.90–5:21.67 | 3.8 | Trailer: masked crew with rifles in the back of a car | FF | "You can't just terrorize everyone and get away with it." |
| 38 | 5:33.50–5:40.62 | 7.1 | Gameplay: jewellery-store hold-up, then the robber with a duffel jumps on a motorbike pillion and rides off (cut 5:35.92) | FF | "So like, you can still run over every single person in the whole game. And it will be completely fine." |
| 39 | 5:48.40–5:51.12 | 2.7 | Gameplay: sedan with passengers shooting out of the windows, 4 stars | FF | "this brand new mode where everything is being tracked. Or" |
| 40 | 5:51.12–5:53.47 | 2.4 | GTA 6 footage: a woman with a backpack leaping off a tower over Vice City | FF | "can just go back, switch to the classic GTA version." |
| 41 | 5:54.87–6:00.61 | 5.7 | **“you still have as much FREEDOM as you had before, … JUST A BIT MORE CHOICE”** (plate cut 5:57.36) | QUOTE | "You still have as much freedom as you had before. And there's no right or wrong way to play the game. Just a bit more choice." |

**Totals.** 41 rows (≈ 46 clips) in **31 runs (5.1 runs/min)**, overlay share **38 %**, run median 3.8 s,
longest 14.3 s (2:38.1–2:52.4, quote card + HUD magnifier). By kind: **4 quote cards**, **3 HUD magnifiers**,
**2 white-page insets**, **7 found art/logo stills** (collage ×2, R★, key-art split, GTA 6 key art, 13
YEARS, GTA Online art), **1 found webcam clip**, **≈ 28 game clips** (GTA 6 trailers / Extended Look;
**GTA V ×5 for "the old world"**). Reuse: the collage (0:36 → 3:40), the dog clip (3:22 → 4:26), the
"DON'T TRIP" store clip (2:02 → 3:50).

### 3b. The four Rob Nelson quote cards — one template

All four are the same template, the family of Fuel System's KEY CLONER card:

- **Geometry (measured):** a 16:9 inset, **dead centre** (box centre 0.500 / 0.500), **no tilt**, **no
  growth** — the bounding box is identical at entry and exit on all four. Size: #1 **1376×768 (71.7 % of
  frame width)**; #2–#4 **≈ 1532–1557×854–868 (≈ 80 %)**. Soft dark drop shadow.
- **In/out:** hard cut both ends (1:00.85 face → 1:00.90 full card; 1:03.65 face; 1:42.00 face → 1:42.07
  card; 2:46.20 card → 2:46.30 HUD magnifier, card-to-card hard).
- **Plate:** game footage **blurred to abstraction and still playing**; it hard-cuts behind the held
  card (2:39.76, 2:41.53, 5:57.36). Convenience-store interiors for #1–#2, shopfronts for #3, a dark
  interior then a bright glass lobby for #4.
- **Card art:** a diagonal gradient, **electric blue top-left** (`#0626A0`, lighter `#4929C7`) → **magenta
  bottom-right** (`#A70088`, glow `#E6589F`); a Vice City skyline silhouette with a pink setting sun and
  water reflection along the bottom; palm silhouettes at both side edges; an **inner rounded rectangle
  drawn as a pink-violet neon tube**, inset ≈ 6 % from the card edge.
- **Type:** a rounded geometric sans, bold (Poppins / Montserrat class). The set-up words in **white
  sentence case** `#FEFDFF`, the load-bearing phrase in **hot-pink caps** `#E032B0`–`#E432B3`. Pink
  quote glyphs: “ hanging at the top-left of the block, ” after the last word. Attribution under a thin
  pink rule, bottom-left inside the frame: **"- ROB NELSON"** small pink caps, **"ROCKSTAR"** tiny below.
- **Copy (exact, `/` = line break):**
  1. 1:00.88–1:03.66 (2.8 s), left-aligned: `This is a world / THAT'S NOW / WATCHING YOU`
  2. 1:42.05–1:44.79 (2.7 s), left-aligned: `lose the cops / and then they / FORGET ABOUT / YOU INSTANTLY`
  3. 2:38.09–2:46.27 (8.2 s), centred: `there's a row of little icons. / those are called / HEAT INDICATORS. / and every single one is a fact. / THE POLICE CURRENTLY REMEMBER / ABOUT YOU`
  4. 5:54.87–6:00.61 (5.7 s), centred: `you still have as much / FREEDOM as you had before, / and there's no right or wrong / way to play the game. / JUST A BIT MORE CHOICE`
- **What earns one:** a Rob Nelson line read out verbatim (#1, #2, #4 are introduced as his words — "the
  sentence which explains this whole game. Comes from Rob Nelson", "Nelson said it straight", "Nelson said
  it flat out"). **#3 is the creator's own explanation set as a Rob quote** (looks like a mis-attribution;
  the line is his narration).

### 3c. The HUD magnifier (new device, ×3)

**The game's own HUD, cropped from the footage that just played, blown up on a centred inset over a
blurred copy of that footage** — "it's on your screen the whole time", shown.
1. **0:26.40–0:28.00** — black rounded panel ≈ 62 % wide (1188×743 measured) centred: **four white stars,
   four red-ringed heat icons (faces / hanger / person / car), "39 221" ammo, a rifle icon**. The blurred
   plate keeps playing (the minimap flashes blue → red behind it).
2. **2:46.27–2:52.36** — black panel ≈ 70 % wide: **the four heat icons alone**, red neon rings
   `#CD1C34`, white glyphs; the plate cuts at 2:50.0. Follows the HEAT INDICATORS card card-to-card.
3. **3:08.07–3:12.11** — a light-blue sky crop ≈ 72 % wide with power lines: **six stars, two grey + four
   red, and three heat icons** — "they don't vanish, they turn red".

Hard cut in, hard cut out, no border graphics, no arrows, no labels.

### 3d. The white-page insets (×2)

A source picture **on a pure white full-frame page with a soft grey drop shadow**, slow push — the only
white frames in this video and in DIRTIEST.
- **3:16.90–3:19.15 — "GTA VI / CRIMINAL PROFILE / SYSTEM"**: a portrait social-carousel slide (≈ 38 % of
  the frame width, ≈ 91 % of its height): "GTA VI" logo (white GTA, gradient VI), an airboat in a swamp
  photo, then on black: *"GTA 6 introduces a new Criminal Profile system that evaluates how you behave as
  a criminal."* and five icon rows — *"NOT honor. It evaluates how you behave as a criminal." · "Robbing a
  store successfully without killing anybody and escaping cleanly RAISES your Criminal Profile." ·
  "Excessive violence LOWERS your Criminal Profile." · "There isn't a traditional meter on-screen. Jason &
  Lucia's profile info is available in a dedicated menu tab." · "Your criminal profile can be PERMANENTLY
  RUINED after specific actions."* — pink keywords, page number "3/5". Cut in raw, uncredited.
- **4:42.55–4:46.27 — RDR2 gameplay** (Arthur in a fist-fight on a cliff, RDR2 radar bottom-left) as a
  16:9 inset ≈ 64 % wide, centred slightly high, shadow falling down-right.

### 3e. Found art and the 13 YEARS slam
- **Character collage** (0:35.97, 3:40.30): four slanted parallelogram panels side by side — a long-haired
  man in white, a man in a cap and khaki tank ("DNIDA"-style print), a woman in aviators leaning on a
  ledge, a grinning man in a bucket hat and green floral shirt. Slow push. Shown for "four
  classifications" and again for their names.
- **R★ logo card** (0:48.78): white R★ with glow on the same blue → magenta gradient as the quote cards,
  palm fronds; slow push 3.7 s.
- **Key-art split** (1:09.02): GTA V cover art | RDR2 key art, diagonal seam, slow push.
- **13 YEARS** (1:55.03–1:57.47): the GTA 6 Jason-and-Lucia key art sharp for 1.5 s, then a **hard switch
  to the same art blurred with "13 YEARS"** in huge white condensed caps (Anton class), dead centre, ≈ 40 %
  of the frame width. No animation.
- **GTA Online art** (4:55.38): the man on the bed of cash. Slow push.

---

## 4. Recurring patterns

- **Cadence.** 108 visual changes (scdet, merged) = **17.7/min**; per minute 23 · 20 · 15 · 20 · 15 · 13 —
  front-loaded, softening into the argument.
- **Which line gets what.**
  - a **Rob Nelson quote** → the neon quote card, verbatim;
  - **"it's on your screen"** → the HUD magnifier (the game UI, cropped and enlarged);
  - **a list** → one clip per item (face / outfit / car in 4.5 s at 0:16.4–0:20.9);
  - **the old games** → GTA V gameplay and GTA V / RDR2 key art (1:09–1:32, 3:55, 4:12, 4:42) —
    chronology by footage;
  - **a named source** → the source itself, raw (the TGG webcam clip, the social infographic);
  - **opinion, the argument, "I want to be fair here"** → the face (the 18.6 s run 4:59–5:18 and the
    11.8–12.8 s runs around it carry the "shattered profile" explanation with almost no pictures).
- **Game footage**: full frame, sharp, HUD in, 1×, 1–7 s per clip. **No inset/PiP for gameplay except the
  RDR2 white-page inset**; no colour matte anywhere.
- **Every still moves** (slow push on collage, logo, key art, infographic); quote cards and HUD
  magnifiers are static over a moving blurred plate.
- **Transitions:** hard cuts only. No dissolve, wipe, whip, glitch or flash anywhere.
- **Reuse is normal**: three sources appear twice.

## 5. Comedy and emphasis devices

| t | device |
|---|---|
| 0:00 | **Open on a strip-club clip with the voice already running** — the hook line is over footage, the face arrives at 0:04.8. |
| 0:16.4–0:20.9 | **The list acted out** — "your face, your outfit, your car": a cut per noun. |
| 0:26.4 | **The HUD magnifier** — "it's on your screen the whole time" answered by blowing up the HUD. |
| 0:36.0 | **Four faces for four classifications.** |
| 1:07.6 | **Cut zoom 1.60 on the insult** — "how stupid the old world was." |
| 1:14.7 | **Literal B-roll** — "helicopter and tank massacre" over a tank shooting at a helicopter in GTA V. |
| 1:28.8 | **The goldfish selfie** — Michael grinning into a phone in front of a run-over pedestrian under "the memory of a goldfish". |
| 1:48.2 | **Cut zoom on the key phrase** — "persistent memory." (after "hold on to that phrase"). |
| 1:56.5 | **The number slam** — "13 YEARS" smashed onto the blurred key art. |
| 2:28.5 | Arms crossed in an X (no edit device, the gesture carries it) on "even when you haven't done anything criminal". |
| 3:55.7 | **"The dumbass just shooting every block"** → a GTA V jet dogfight. |
| 4:12.0 | **"Randomly running people over"** → a convertible through the boardwalk crowd. |
| 4:26.1 | **The dog clip returns** as the punchline to "you can't just pet a random dog for five minutes". |
| 4:42.6 | **RDR2 on a white page** — the old game framed like an exhibit. |
| 6:04.5 | **The thesis on a cut zoom** — "You're just not anonymous anymore." tight, and the video ends there. |

## 6. Palette and type

| swatch | hex | where |
|---|---|---|
| Set green (LED wall) | `#6DD87D` | every face shot |
| Shirt maroon | `#4D0414` | wardrobe |
| Lens red | `#B81500` | the glasses (the zoom ruler) |
| Chair brown | `#543125` | face shot |
| Card blue | `#0626A0` / `#4929C7` | quote card + R★ card gradient |
| Card magenta | `#A70088` / `#E6589F` | quote card + R★ card gradient |
| Quote pink | `#E032B0` – `#E432B3` | quote accent phrases, quote glyphs, attribution |
| Quote white | `#FEFDFF` | quote set-up words, 13 YEARS |
| Heat-icon red | `#CD1C34` | HUD magnifier rings (the game's own UI) |
| Page white | `#FFFFFF` | the two white-page insets |

Type classes: (1) **rounded geometric sans bold** (Poppins / Montserrat class) — white sentence case +
pink caps, the quote cards; (2) **heavy condensed caps** (Anton class) — "13 YEARS" only. Every other
letter on screen is the game's or the found artefact's own.

## 7. Ending (6:00.61 – 6:06.18)

Quote card #4 hard-cuts out at 6:00.61 to a base face: "Nothing is stopping you from being a psycho.
You're exactly free as you've always been." **Hard cut at 6:04.53 to a tight crop (≈ 1.4)** for the last
line, "You're just not anonymous anymore." — the thesis, said once, and the video stops on that tight
face at 6:06.18. **No sign-off, no subscribe ask, no end card, no end-screen space, no fade.**

## 8. Differences

### vs the preset README (`affan-afterhours-facecam/README.md`)
| README says | CRIME SYSTEM does |
|---|---|
| opens on the face | **opens on game footage**, face at 0:04.8 |
| face ~80 % | **62 %**; overlays 38 % in 31 runs (5.1/min) |
| posters: 16:9 inset ~72 %, tilted 1–3°, cream condensed caps, one pink accent, **grow 8–15 %** | the quote cards are 72–80 % insets but **untilted, static (0 % growth)**, in a **rounded geometric sans, white sentence case + pink caps** — the Fuel System KEY CLONER variant is the house template here |
| cards on a quotable punchline or quote | cards **only** for Rob Nelson quotes (4); the "13 YEARS" slam is the one typeset number |
| cut zoom +25 %, ~5/min, two thirds inside a held shot | **≈ ×1.3–1.6, ≈ 2.8/min, nearly all on a hard cut** |
| push ~1 %/s on every face run | **looks like none** |
| 1–2 face slow-downs | **zero** |
| inserts slowed as a matter of course | **every insert at 1×** |
| SUBSCRIBE bug twice | **none** |
| nothing is ever an inset | three new inset kinds: **HUD magnifier**, **white page**, the quote card |
| ends cold on the face | same — and on the thesis line, without a sign-off |

### vs CREATOR-HAND.md (the creator's own 09-23 → 09-30 timelines)
- **Same:** cut zooms as static jumps of 130–160 %; no slow-down when the script has no comic beat ("zero
  is fine"); ends on the face; voice from 0.000 with an overlay at frame 0 (as Game Informer, 09-30).
- **Different:** no nest push (CREATOR-HAND's 105/110 presets don't show here); no colour matte (the
  09-30 inset rule), but the inset idea is already present in three forms; no meme clip, no colour-bars
  glitch, no fade; the found-source raw cut-in (TGG clip, the social slide) anticipates CREATOR-HAND's
  "raw found artefacts" at 81–86 %, but here on a white page.
