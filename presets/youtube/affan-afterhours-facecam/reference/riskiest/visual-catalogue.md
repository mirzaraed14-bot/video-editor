# Visual catalogue — "Rockstar's RISKIEST GTA 6 Move Yet"

Frame-by-frame dissection of the EDITING STYLE, for reproduction.

**Source:** `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Gta gun.mov` · 1920×1080 · 60 fps · 5:32.35 · 35k views (creator's #2 video).
**Evidence:** all 101 cut frames + all 102 segment mid-frames in `probe/`, plus ~70 extra frames pulled with ffmpeg around every transition. Measured numbers from `probe/summary.md` and `probe.json` are treated as given; everything else below was read off the frames.
**Transcript:** present (`../transcript/words.json`, WhisperX, 1124 words) — every overlay is quoted against the spoken line.

> **Data caveat carried through this document.** `probe.json`'s `kind: face|overlay` label is a face-*detector* output, and it fires on GTA characters' faces. Roughly a third of the segments labelled `face` are actually game footage (0:01.60–0:07.00, 0:22.00–0:26.60, 0:39.00–0:43.60, 0:31.60, 2:28.80–2:34.20, 4:17.00, …). Everything in this catalogue is classified **visually**, not from the label. Consequence: the probe's "overlays = 10 % of runtime" is a floor. The true cutaway share, counted by eye, is **76.4 s of 332.35 s = 23 %**.

---

## 1. The face shot

### Framing (measured off `probe.json` face boxes, real face shots only, n=1278 samples)

| | value |
|---|---|
| face-box height | median **348 px of 1080 (32 %)** · p10 313 px · p90 418 px |
| face-box top edge (≈ forehead/hairline) | median **265 px** from the top |
| face centre X | median **1036 px** — i.e. **76 px right of frame centre** |
| face centre Y | median **440 px** — upper-middle, on the upper third |

So: a **medium close-up**, chest-up, subject placed slightly **camera-right of centre** with the neon sign filling the left-of-head negative space. Headroom is generous in the base size (~265 px / 25 % of frame height above the hairline) and collapses to near-zero in the tight sizes.

### The framing ladder (what changes between jump cuts)

There is no locked size. Every jump cut lands on a **slightly different reframe**, and on top of that each held shot **creeps in continuously**: measured gradual push on face shots ≥1.5 s is **median 4.3 % per shot = 0.92 %/s**. Nothing is ever static.

Four working sizes, by face-box height:

- **Wide/base (~300–330 px, 28–31 %)** — chest-up, the leather armchair's rolled arm in frame left, the monitor edge frame right, full "skool" neon visible. e.g. 0:07.00, 0:18.60, 0:33.80, 1:24.80, 3:44.60, 4:53.00.
- **Medium (~350–420 px)** — the default; shoulders cropped, neon partly cropped at the right edge. e.g. 1:16.80, 2:34.20, 3:18.20.
- **Tight (~450–550 px)** — head-and-shoulders, neon cropped to "kool" or "skoo", top of hair near the frame edge. e.g. 1:15.20, 1:19.00, 5:12.60.
- **Extreme (~590–640 px, 55–59 %)** — face fills the frame, hair cropped off the top, only two neon letters survive. **0:11.40–0:12.40** ("Technically *impossible*"), **2:44.40–2:45.00**, and the **final shot 5:29.60–5:32.35**.

`summary.md` counts **66 cut-zooms in / 58 out, median step ×1.195, median hold 0.6 s** — i.e. most jump cuts move the size by ~20 %, and it snaps back out just as often as it pushes in. The three biggest steps inside face runs are ×3.19 at **2:10.40**, ×2.50 at **1:35.60** and ×1.97 at **2:26.20**.

### The set

- **Wall:** a plain light wall washed with a **green LED** (sampled `#5BAC5D` / `#96AD89`), with a **magenta/violet** accent light bleeding in at the upper left. No greenscreen — it is a lit wall.
- **Neon sign:** the word **`skool`**, lowercase, tubed script, each letter a different colour — s cool-blue/white, k red-orange (`#CE604E`), first o warm white/yellow (`#F4DD99`), second o cyan (`#4CBEB4`), l yellow-orange. It sits on the wall **camera-left of his head**, and how much of it is cropped is the fastest read on how tight a given shot is.
- **Framed panel:** a small square framed picture / LED art panel glowing pink-and-green on the wall further left, visible once the shots widen (0:26.60, 2:23.00, 3:05.40, 4:31.40).
- **Chair:** a brown/oxblood **leather armchair** with a fat rolled arm, occupying the lower-left quadrant. He sits back into it for most of the video and leans out of it for emphasis.
- **Frame right:** a large dark **monitor/TV seen edge-on** — only its bezel and angled back panel are in shot, a hard dark wedge that anchors the right side.
- **Frame far-left:** a dark slatted rack / shelving unit, green-backlit. Looks like foliage or cable-managed racking; too dark to call.
- **Behind, lower right:** a green plastic crate and a table with loose objects.
- **Plants:** none clearly identifiable in the set. (The only plant in the video is inside the stock interview clip at 0:48.80, which is not his room.)

### The microphone — the running visual gag

He holds a **wooden cooking spatula / paddle** upright like a handheld stage mic, with a **DJI wireless lav transmitter** (grey foam windscreen, DJI logo legible at 0:12.45) clipped to its top. It is in his hand for essentially the entire video, and he works it like a mic — brings it to his mouth on punchlines, points with it, rests it on his shoulder, chews near it. This is the single most identifiable prop in the video.

### Wardrobe

Plain **black short-sleeve crew/mock-neck tee**, **black shorts** with a white drawstring (only visible in the headless shot at 2:10), a **metal-bracelet watch** on the mic hand, and **black square acetate glasses with orange-red tinted lenses**, never removed. Dark hair, full dark beard. No jewellery beyond the watch.

### Persistent graphics — none

**There is no bug, no logo, no lower-third, no name tag, no chapter title and no subscribe animation anywhere in 5:32.** Checked across ~70 sampled frames spanning every face run.

**There are no captions or subtitles of any kind.** Not burned-in, not styled, not partial. All the text in this video lives inside the four poster cards. (This matches the house rule for long-form: YouTube CC only.)

### Motion / conform note

`slowmo.json` (74 runs) shows **no slow motion anywhere**. What it flags are two different things:
- Every game-footage run reads **~50 % duplicate frames** → the sourced clips are **30 fps conformed onto the 60 fps timeline**, unretimed.
- Four runs read **93–95 % duplicate** → those are **stills**, not video: the R★ card (0:12.47–14.38), the interview portrait (0:48.80–50.65), the GTA 5 weapon wheel (1:09.23–1:11.90), and the thumbnail callback (1:43.28–1:45.20).
- The face cam itself is true 60 fps; its short dup bursts are just him sitting still.

---

## 2. Cold open (0:00–0:30)

**Cut rate: 26 cuts in the first 30 s ≈ 52 cuts/min** (`summary.md` measures the full first minute at 44.0/min against a 18.2/min whole-video average). The cold open is roughly **3× the density** of the body.

**No title card, no hook text, no logo sting.** It opens on his face mid-sentence at frame 1.

| # | TC | Dur | On screen | Spoken |
|---|---|---|---|---|
| 1 | 0:00.00 | 1.6 s | Face, base wide. Spatula-mic raised. | "For 25 years, every GTA character has been carrying a rocket launcher," |
| 2 | 0:01.60 | 0.4 s | **GTA San Andreas** — CJ with a rocket launcher, 5-star wanted, taxi + burning cars, "Harry Gold Parkway" street title burned in | "a sniper rifle," |
| 3 | 0:02.00 | 0.4 s | GTA SA, same rampage, closer | |
| 4 | 0:02.40 | 0.4 s | GTA SA, rocket aimed skyward | |
| 5 | 0:02.80 | 0.4 s | GTA SA, wider | |
| 6 | 0:03.20 | 1.2 s | GTA SA, crosshair on a taxi | "a shotgun," |
| 7 | 0:04.40 | 0.6 s | GTA SA, car explodes in a fireball | |
| 8 | 0:05.00 | 1.2 s | **GTA 5** — night, Michael on a rooftop holding a sniper rifle, near-black frame | "four pistols" |
| 9 | 0:06.20 | 0.8 s | **GTA 5** — Franklin, daylight, shotgun on a police car | "and a minigun" |
| 10 | 0:07.00 | 4.4 s | Face, base wide, slow push | "somewhere on their body. Technically" |
| 11 | 0:11.40 | 1.2 s | **Face, EXTREME close-up** — biggest face of the first minute (599–634 px) | "impossible." |
| 12 | 0:12.60 | 1.8 s | **Rockstar R★ logo card**, full-frame (see §3) | "But that's how it was. And Rockstar" |
| 13 | 0:14.40 | 1.2 s | Face, medium, index finger raised | "just took that away." |
| 14 | 0:15.60 | 1.6 s | **GTA 6** trailer — Jason loading a gun at an open car trunk, Lucia beside him, letterboxed 2.39:1 | "Here's what's in this video. There" |
| 15 | 0:17.20 | 1.4 s | **GTA 6** — night, burning cars, a man face-down on the road with a red backpack | "is now a hard limit on how many guns" |
| 16 | 0:18.60 | 3.4 s | Face, base wide, finger raised | "you can carry. And I'll give you the exact number. And it's smaller. / Then you think," |
| 17 | 0:22.00 | 0.4 s | **GTA 6** — Lucia (red bandana, backwards cap) + Jason walking into a gas-station store | "there's a rule about your second rifle" |
| 18 | 0:22.40 | 0.4 s | same, closer | |
| 19 | 0:22.80 | 0.4 s | same, inside the doorway | |
| 20 | 0:23.20 | 0.4 s | same, inside the shop | |
| 21 | 0:23.60 | 1.4 s | **GTA 6** — shotgun levelled at the clerk, seen partly through the shop's round **convex security mirror**. ⚠ *This circle is a real object in the game footage, not an edit effect — it is easy to mis-log as an iris/spotlight overlay.* | "that is going to change how you walk down the street" |
| 22 | 0:25.00 | 0.8 s | **GTA 6** — Jason vaulting the counter, beer fridges behind | "Not a joke," |
| 23 | 0:25.80 | 0.8 s | **GTA 6** — low angle, Jason mid-vault over the chiller | "literally how you walk" |
| 24 | 0:26.60 | 2.4 s | Face, base wide | "Rockstar removed something that's been in every GTA" |
| 25 | 0:29.00 | 0.4 s | **GTA 6** — first-person-ish over-shoulder, firing on a cop pickup, 4-star | "since 2001" |
| 26 | 0:29.40 | 0.4 s | GTA 6, rounds sparking off the truck | |
| 27 | 0:29.80 | 0.4 s | GTA 6, closer | |
| 28 | 0:30.20 | 0.4 s | GTA 6, truck smoking | |
| 29 | 0:30.60 | 0.4 s | **GTA San Andreas** — red car airborne over an "SFPD" cruiser, helicopter, night | |
| 30 | 0:31.00 | 0.6 s | **early-2000s GTA** (Vice City / SA era) — pink winged sports car, night street | |
| 31 | 0:31.60 | 0.6 s | **GTA Vice City** — low-poly nightclub, a punch being thrown | |
| 32 | 0:32.20 | 1.6 s | **GTA 3** — yellow taxi, "Saint Mark's" street title, a third-party channel watermark visible bottom-right | |
| 33 | 0:33.80 | 5.2 s | Face, base wide | "And most people, myself included, didn't notice it…" |

**The move worth stealing:** the line "*every GTA since 2001*" is cut so that the GTA 6 footage **hard-cuts straight into a 3.2 s retro montage** (SA → Vice City → GTA 3, four clips at 0.4–1.6 s) exactly on the word "2001". The edit does the chronology, not the script.

---

## 3. Every overlay run

**20 runs, 76.4 s total = 23 % of runtime.** Consecutive game clips are recorded as one run with their internal cut count.

Only **six** of the twenty are built graphics. The other fourteen are raw game footage cut in full-frame.

### Inventory

| # | Start–End | Dur | Cuts inside | Kind | Spoken line |
|---|---|---|---|---|---|
| 1 | 0:01.60–0:07.00 | 5.4 s | 8 | Game — **GTA SA** rampage ×6 → **GTA 5** ×2 | "a sniper rifle, a shotgun, four pistols and a minigun" |
| 2 | 0:12.60–0:14.40 | 1.8 s | 1 | **Logo card** — Rockstar R★ (still) | "But that's how it was. And Rockstar" |
| 3 | 0:15.60–0:18.60 | 3.0 s | 2 | Game — **GTA 6** trailer (trunk loadout; night mayhem) | "Here's what's in this video. There is now a hard limit…" |
| 4 | 0:22.00–0:26.60 | 4.6 s | 7 | Game — **GTA 6** gas-station store robbery | "there's a rule about your second rifle… literally how you walk" |
| 5 | 0:29.00–0:33.80 | 4.8 s | 8 | Game — **GTA 6** cop shootout ×4 → **retro GTA** (SA / VC / GTA 3) ×4 | "…in every GTA since 2001" |
| 6 | 0:39.00–0:43.60 | 4.6 s | 8 | Game — **GTA 6** jewellery-store robbery → street escape (green "MARCUS 69" jersey) | "it was right there in front of our eyes and at the end a control change…" |
| 7 | 0:48.80–0:50.60 | 1.8 s | 1 | **Real photo / portrait (still)** — a bearded man in a black V-neck with a lav mic, white kitchen/workshop | "let's start with the number. Rob Nelson, co-head of development" |
| 8 | **0:58.00–1:02.40** | **4.4 s** | 1 | **POSTER 1 — "2 CONCEALED HANDGUNS"** | "you can always have two concealed handguns on you whenever you want" |
| 9 | 1:09.20–1:11.80 | 2.6 s | 1 | **Screenshot (still)** — GTA 5 weapon wheel, German UI | "Remember the GTA V weapon wheel? Eight slots and every slot was a category." |
| 10 | **1:21.20–1:24.80** | **3.6 s** | 1 | **POSTER 2 — "PERSONAL VEHICLE / LOADOUT"** | "Only your personal vehicle carries your entire selected loadout." |
| 11 | 1:35.00–1:38.40 | 3.4 s | 3 | Game — **GTA 6** trailer, sunset carjacking/shootout, letterboxed | "So steal a car mid-mission and your arsenal does not come with you" |
| 12 | 1:43.40–1:45.20 | 1.8 s | 1 | **Own thumbnail callback (still)** — his previous video as a YouTube list row | "Which if you saw my last video, took an app, a tool, a fence and a registration fee to get" |
| 13 | 2:28.80–2:34.20 | 5.4 s | 3 | Game — **GTA 6** Lucia walking a strip mall, pedestrians reacting | "when Lucia was walking in the grocery shop, people were just walking away" |
| 14 | **2:58.60–3:05.40** | **6.8 s** | 1 | **POSTER 3 — "DON'T REACT"** (the only green card) | "in GTA 5 you can pull out a shotgun from nowhere in front of people and they don't react" |
| 15 | **3:29.40–3:35.20** | **5.8 s** | 1 | **POSTER 4 — "STICKINESS / LESS OF A DEFAULT LOCK ON"** | "a little bit of stickiness on the aiming but leaning more towards… less of a default lock on" |
| 16 | 4:17.00–4:18.60 | 1.6 s | 1 | Game — **GTA 6** motel forecourt, Jason + a woman at a muscle car | "one permanently in your hand so the street will be watching you" |
| 17 | 4:28.60–4:31.40 | 2.8 s | 1 | Game — **GTA 5** gameplay, Franklin pistol duel in a scrapyard | "So a setting exists for people to turn it on so they feel like they're in GTA 5 again, 2013 style" |
| 18 | 4:38.40–4:43.80 | 5.4 s | 3 | Game — **GTA 6** trailer, rear-seat POV, Lucia driving, letterboxed | "if you play the game in a harder difficulty… you will get more rewards" |
| 19 | 4:50.00–4:53.00 | 3.0 s | 4 | Game — **GTA 5**, Franklin **sprinting** down Vinewood Blvd, cops | "Since GTA 3 2001, you sprint by mashing X. Tap, tap, tap, tap." |
| 20 | 5:01.40–5:05.20 | 3.8 s | 7 | Game — **Destiny 2**, Guardian fighting a Hive/Vex-type boss in an ice arena | "I used to play a game called Destiny 2. And that's exactly how we used to sprint." |

### Transitions — there is exactly one, and it is the absence of one

**Every single overlay enters on a HARD CUT and exits on a HARD CUT.** Sampled 3–5 frames across all four poster boundaries and the logo card, weapon wheel, portrait and thumbnail: at 57.95 the frame is a clean face shot, at 58.05 the card is already at full opacity and full size. Zero fades, zero wipes, zero slides, zero dips to black, zero whip-pans, zero flash frames, zero zoom transitions. No transition effect appears anywhere in 5:32.

---

### The four poster cards — full spec

All four are built from the **same template**, and the geometry is identical to the pixel:

| measured | value |
|---|---|
| card size at entry | **1390 × 782 px** of 1920×1080 = **72.4 % of frame**, all four cards identical |
| card size at exit | **~1510 × 850 px = ~78.6 %** |
| growth across the hold | **+8 to +9 %**, i.e. a constant **≈2 %/s** push on the card |
| position | **dead centre** (measured centre 481.5/960 and 271.5/270 in a 960-wide proxy) |
| aspect | landscape, ~16:9, rounded corners, hard black outer edge |
| background plate | the **frame behind the card is a heavily blurred, darkened, desaturated plate of game footage** — never the face shot. Border-colour sampling of all four gives warm greys/browns/creams (`#18140F`, `#CDBDA5`, `#2B2E29`, `#3F3326`), nothing like the green face set (`#5BAC5D`). On posters 3 and 4 the plate looks like the card's own hero image blurred up; on poster 1 it is a different GTA 6 interior. |
| motion while held | yes — besides the scale-up the card sits at a **slight off-axis perspective (a few degrees)** that drifts continuously. Edge measurements across a hold oscillate rather than swing one way, so it looks like a **gentle idle float / wobble**, not a single swing. It is never a flat static rectangle. |
| render fps | the card animation reads ~50–58 % duplicate frames → **rendered at ~30 fps** onto the 60 fps timeline |

---

#### POSTER 1 — 0:58.00–1:02.40 (4.4 s)

**Line:** "*you can always have two concealed handguns on you whenever you want*"

**Copy (exact, `/` = line break):**
`YOU CAN ALWAYS HAVE / CONCEALED / HANDGUNS / ON YOU WHENEVER YOU WANT` — with a giant **`2`** set inline at the end of the first line, and **`01`** / **`02`** labelling two tiles on the right.

**Layout:** two-column. Left ⅔ = the text stack, **left-aligned**. Right ⅓ = two stacked rounded tiles, each a dark glass gradient with a glowing white pistol glyph, numbered 01 and 02, separated by a thin vertical rule.

**Card art:** a flat vector Vice-City sunset — vertical gradient deep blue at the top → magenta → peach at the bottom, **black palm-frond silhouettes** in the upper-left, upper-right and lower-left, and a flat **city skyline** silhouette along the bottom edge. Thin white **HUD corner ticks** at the corners and a short white rule at top-centre.

**Colours:** bg blue `#0B37AC` → magenta `#9A2788` → violet `#533488`; the big `2` in hot pink `#EE2A9A`, sitting on a dark-magenta→hot-pink **gradient bar block** that reads like a loading bar; headline in cream `#F7EFDA`.

**Type:** headline `CONCEALED HANDGUNS` in a **heavy condensed grotesque, all caps**, tight tracking, subtle drop shadow (Anton / Archivo Black class). Supporting lines in a **bold condensed sans, all caps, letterspaced**, white. `01`/`02` in a **light wide sans**.

**Icons:** two identical white pistol glyphs with an outer glow.

**Enter/exit:** hard cut / hard cut. **Moves while held:** yes — scales 695→762 px (in a 960 proxy) and drifts in perspective.

---

#### POSTER 2 — 1:21.20–1:24.80 (3.6 s)

**Line:** "*Only your personal vehicle carries your entire selected loadout.*"

**Copy (exact):**
`ONLY YOUR / PERSONAL / VEHICLE / CARRIES YOUR / ENTIRE SELECTED / LOADOUT`

**Layout:** image-left / text-right, text **right-aligned**, hugging the card's right edge.

**Card art:** a photoreal render of a dark grey mid-engine supercar (Ferrari 458-ish) on wet tarmac under a neon-lit gas-station canopy, palms and a violet Vice City skyline behind. Overlaid on it: a **partial radial weapon-wheel arc** at top-centre with three slot tiles (long-gun glyph, pistol glyph, a third icon) and thin magenta connector lines running from the wheel down to the car — a diegetic "this equips from here" diagram. A **GTA VI logo** ("gta" script above a large `VI`, pink/violet gradient, small star) sits bottom-right of the card.

**Colours:** the darkest of the four — `#261E23`, `#1C2233`, `#3E2831`, lifted by a dusty-rose `#655672` and neon-pink highlights; `PERSONAL` in pink `#AB498B` (softer than poster 1's `#EE2A9A` because it sits over the dark render); the rest cream/white.

**Type:** identical stack to poster 1 — heavy condensed caps for `PERSONAL` / `VEHICLE` / `ENTIRE SELECTED` / `LOADOUT`, lighter letterspaced condensed caps for the connectors `ONLY YOUR` / `CARRIES YOUR`.

**Accent word:** **`PERSONAL`** is the only pink word.

**Enter/exit:** hard cut / hard cut. **Moves while held:** yes, 696→748 px.

---

#### POSTER 3 — 2:58.60–3:05.40 (6.8 s) — *the longest graphic in the video*

**Line:** "*in Rob's exact words, in GTA 5 you can pull out a shotgun from nowhere in front of people and they don't react*"

**Copy (exact):**
`IN GTA 5 / YOU COULD PULL OUT A / SHOTGUN FROM NOWHERE / INFRONT OF PEOPLE / AND THEY / DON'T / REACT` — plus a badge reading `Ø / ZERO / REACTION`, and a small superscript zero-mark after `REACT`.
*(Copy is set as `INFRONT`, one word — reproduced as seen.)*

**Layout:** image-left / text-right, text **right-aligned**. The `Ø ZERO REACTION` badge is a rounded pill straddling the seam between image and text, with a thin leader line dropping from it to a small green node dot on the pavement in the photo.

**Card art:** a sunny GTA 5 Los Santos sidewalk — palms, storefronts, ~6 pedestrians, one man mid-frame openly carrying a **shotgun**. Over it, a surveillance HUD: a **translucent green body-box** around the armed man, and small **circular face-tracker rings** (each with a tiny head thumbnail inside) over three pedestrians' heads, joined by hairline leaders. The point of the card is made by the HUD, not the copy.

**Colours:** the odd one out — **green-accented, not pink.** `GTA 5` in pale mint `#A1D7AD`; the tracker boxes and rings green; `DON'T REACT` in cream `#F4EED2` with a green outer glow. Card body is sunlit olive/sage (`#769F96`, `#B7BEA5`, `#AFA48A`).
**Read this as a deliberate colour code: pink/magenta = GTA 6 and the new rules; green = GTA 5 and the old way.**

**Type:** `DON'T REACT` is the largest type in the whole video — heavy condensed caps across two lines. `IN GTA 5` is thin letterspaced caps. Badge numerals/labels in a condensed caps at two sizes.

**Enter/exit:** hard cut / hard cut. **Moves while held:** yes, 697→762 px over 6.4 s (the slowest push, ~1.3 %/s, because the hold is longest).

---

#### POSTER 4 — 3:29.40–3:35.20 (5.8 s)

**Line:** "*a little bit of stickiness on the aiming, but leaning more towards a definitely less of a default lock-on than previous games*" (quoting Rob)

**Copy (exact):**
`A LITTLE BIT OF / STICKINESS / ON THE AIMING` then `BUT LEANING MORE TOWARDS / LESS ᴼᶠ DEFAULT / ᴬ LOCK ON / THAN PREVIOUS GAMES`
— the second block is a nested lockup: `LESS` (huge) with small `OF` and `A` stacked between it and `DEFAULT` / `LOCK ON` (huge), so the small words read as connective tissue inside one big phrase.

**Layout:** image-left / text-right, text **right-aligned**, two separated text blocks with a clear gap.

**Card art:** GTA 6 Ocean Drive at dusk — Jason from behind, walking a neon-lit street, palms, a "NEON" sign. HUD overlay: a large cream **square bracket reticle** locked onto a distant pedestrian on the left, with a **red laser/tracer line** running into it; a smaller round reticle mid-frame; a tiny label box reading **`PREVIOUS GAMES`** at lower-left; thin **magenta swoosh curves** and faint circle-grid decorations in the right half. Thin rounded navy frame with **corner tick marks** and a small pink `+` glyph at bottom-right.

**Colours:** the darkest card — near-black navy `#0F1122` / `#0A0C1B`; accents in a **lighter orchid pink** `#DF6BE1` / `#D26FD4` (on `STICKINESS` and `LESS`), cream `#EFE1C7` (on `DEFAULT LOCK ON`), plus the red laser line.

**Type:** same family throughout — heavy condensed caps at two sizes plus letterspaced light caps for the connectors.

**Enter/exit:** hard cut / hard cut. **Moves while held:** yes, 672→750 px.

---

### The three "found artefact" stills

These are not designed cards; they are **screenshots and photos cut in full-frame as evidence**, each held ~1.8–2.6 s with a slow scale-up and nothing else. All three read ≥93 % duplicate frames — they are stills, not video.

**A. Interview portrait — 0:48.80–0:50.60 (1.8 s).** A real-world video still: a bearded man, greying, in a black V-neck with a lav mic on the collar, seated in a bright white kitchen/workshop, soft daylight, shallow depth of field. It lands on "*Rob Nelson, co-head of development*". **There is no name caption, no label, no attribution of any kind.** It *looks like* a generic stock-interview still used as a stand-in portrait rather than a photo of the actual person — it does not resemble published images of Rockstar's Rob Nelson. Full-frame, no card, no border.

**B. GTA 5 weapon wheel — 1:09.20–1:11.80 (2.6 s).** A frozen GTA 5 screenshot with the radial weapon wheel open, **German UI** ("Schaltflächenbelegung", "Schrotflinte", "Maschinenpistole"). Michael standing on a street. Full-frame, no card, no annotation, no highlight — he just talks over it. Lands on "*Remember the GTA V weapon wheel? Eight slots…*".

**C. Own thumbnail callback — 1:43.40–1:45.20 (1.8 s).** A screenshot of **his own previous video rendered as a YouTube list row**, centred on a **pure black full-frame background** with wide letterbox margins on all four sides. Contents: thumbnail of Lucia's face left, `YOU CAN'T` in white and `STEAL CARS` in red on a black bar; a **red part-watched progress bar** under the thumbnail; duration badge `6:54`; title `GTA 6's Fuel System Isn't The Problem...This Is`; meta `94K views • 5 days ago`; a `⋮` kebab menu. Slow scale-up, hard cut in and out. Lands precisely on "*Which if you saw my last video*".

**D. Rockstar R★ logo card — 0:12.60–0:14.40 (1.8 s).** The only **full-bleed** graphic in the video — it fills the frame edge to edge with no card, no border and no background plate. Diagonal gradient from blue `#2C3EC0` (upper-left) through violet `#7F2096` to hot pink `#EE38A2` (lower-right), with **violet palm-frond silhouettes** in three corners. The white **R★** wordmark sits slightly left of centre with a soft white outer glow. Still image with a slow scale-up. Lands on "*And Rockstar*". No audio sting implied by the visuals; no flash frame.

---

## 4. Recurring patterns

### Poster frequency and hold

Four poster cards in 5:32 = **one every 83 s**, holds **3.6 / 4.4 / 5.8 / 6.8 s** (median **5.1 s**) — three to five times the median held shot (1.3 s). A poster is the longest thing on screen at any given moment; the edit deliberately *stops* for it.

**But they are not spread evenly.** All four fall inside a single 2:37 window (0:58 → 3:35). The first 58 s and **the entire last 1:57 have no poster at all**. The back half is carried purely by game footage and the creator's face.

### What earns which treatment

Sorted by how the edit responds to a line:

- **A verbatim quote or a hard rule → POSTER.** All four posters carry either a direct Rob Nelson quote (3, 4) or a stated game rule with a number in it (1, 2). Nothing else gets a poster. The number or the operative word is the pink one.
- **A claim about what the game shows → GAME FOOTAGE, full-frame.** Fourteen of twenty runs. Whenever he asserts something visible, he cuts to the footage that shows it.
- **A named artefact he can screenshot → the screenshot itself, unannotated.** The weapon wheel, his own thumbnail, the portrait. He does not build a graphic when a real capture exists.
- **A joke, a reaction, an aside, an opinion, a prediction → NOTHING.** He stays on his face. "I trust Rockstar, that's why I'm not raising any fingers", "God damn it Rob", "Talk about real life, these guys are going overboard", "PC ain't seeing GTA 6 till like…" — all played straight to camera with no cutaway.
- **A physical demonstration → NOTHING, deliberately.** 1:55–2:14 is the longest single shot in the first half (18.6 s) and it is him miming how you'd hold a rifle in your off-hand, with no B-roll at all. The comedy is that there is nothing to cut to.

### Full-frame vs inset

**Everything is full-frame. There is not a single picture-in-picture, inset, corner box, split-screen or side-by-side in the video.** Checked across the long face runs at 2:00, 2:25, 2:40, 2:55, 3:10, 3:20, 4:00, 4:25. The only thing that isn't edge-to-edge is the poster card itself, and that is a centred 72 %-of-frame card over a blurred plate — a card, not an inset.

### Motion on stills

Uniform: **everything moves, slowly, always.** Stills get a slow scale-up. Poster cards get a slow scale-up plus a perspective drift. Face shots get a 0.92 %/s push. Nothing in this video is ever locked off for more than a beat.

### Repeated transition devices

There are none. **Hard cuts only, 101 of them, no exceptions.** This is the most rigid rule in the whole edit.

### Shot-length rhythm

`summary.md`: median held shot **1.3 s**, longest **32.4 s**. Cuts per minute by minute: **[44.0, 18.0, 8.0, 7.0, 13.0, 20.4]**. The shape is a **V** — hammer open, decompress hard through minutes 3–4 (the 32.4 s unbroken take at 3:44.60–4:17.00 is the floor), then accelerate back into the close. Minute 5 climbs back to 20.4/min, driven by the sprint montage and the 7-cut Destiny 2 burst.

### The outro (last 30 s: 5:02–5:32)

1. **5:01.40–5:05.20 (3.8 s) — Destiny 2 montage**, 7 clips at 0.4–0.6 s. The fastest cutting in the entire video, faster even than the cold open. Pure energy release on a throwaway personal aside ("I used to play a game called Destiny 2").
2. **5:05.20–5:12.60 (7.4 s)** — face, medium, on the stick-drift joke.
3. **5:12.60–5:13.80 (1.2 s)** — face, tighter.
4. **5:13.80–5:29.60 (15.8 s)** — face, base size, the single longest shot of the outro. The recap: "*so the magic pockets, the lock on, the radar, the sprint, the core fundamentals in short are being changed*".
5. **5:29.60–5:32.35 (2.8 s)** — **face, extreme close-up, pointing directly at camera**: "*what are your thoughts, let me know inside of the comments*". He drops the pointing hand around 5:31.3 and holds a flat stare into lens for the last second.

**The outro has no end card, no subscribe animation, no end-screen placeholder, no logo, no music button, no cut to black.** It ends cold on a held stare, mid-breath. Note that this breaks the usual long-form convention of leaving the right side and bottom clear for YouTube end-screen cards — he leaves nothing clear, because he doesn't use them.

---

## 5. Comedy / emphasis devices you can SEE

| TC | Device | What happens |
|---|---|---|
| **0:11.40** | **Punch to extreme close-up on the punchline word** | Face jumps from base (~320 px) to ~600 px for 1.2 s on the single word "*impossible.*" then cuts away to the R★ card. The cut IS the emphasis. |
| **0:29.40–0:33.80** | **Chronology joke in the cut** | "since 2001" triggers an immediate 4-clip retro montage (SA → VC → GTA 3) at 0.4–1.6 s. The visual does the date. |
| **0:30.60–0:33.80** | **Deliberate low-fidelity contrast** | Retro clips are visibly compressed, soft and 4:3-ish next to the crisp GTA 6 footage either side. Left ugly on purpose. One clip (0:32.20) even carries a **third-party channel's watermark**, un-cropped. |
| **1:43.40** | **Self-referential cutaway** | Cuts to his own previous video's YouTube row, with the red part-watched bar still on it, on the words "if you saw my last video". Plays as a shrug rather than a plug — there's no arrow, no callout, no "link below". |
| **1:55.00–2:13.60** | **The 18.6 s no-B-roll take** | The longest shot of the first half is him physically miming how you'd carry a rifle in your off-hand, with zero cutaways, including a long "I don't know how that works". The void is the joke. |
| **2:10.00–2:11.00** | **Headless frame** | He stands up out of the chair and the camera does not follow: for ~1 s the frame is **his torso, shorts and the spatula-mic with his head cut off above the top edge**, while he keeps talking. `probe.json` logs this as a ×3.19 "cut zoom" — it isn't a zoom, it's him leaving frame. Reads as a deliberate awkward beat. |
| **2:13.60–2:14.40** | **Leaning out of frame** | He leans hard camera-left, face half out of frame, body diagonal across the shot, still miming. |
| **2:26.20** | **Mid-gesture hard cut** | ×1.97 size jump landing inside a hand gesture on "*every cop clocks you*". |
| **2:44.40–2:45.00** | **Double punch-in** | Two cut-zooms 0.6 s apart (×1.389 then ×1.456) stacking into an extreme close-up, on "*you don't know which pedestrian might file a report on your ass*". |
| **2:58.60** | **Green card among pink cards** | Poster 3 breaks the pink palette to mark "this is the OLD game". A colour joke you only get on the fourth viewing. |
| **3:29.40** | **Quote card as the punchline to his own exasperation** | He says "*God damn it Rob*", and the card that follows is Rob's own words, set beautifully. The design politeness against the insult is the gag. |
| **4:50.00–4:53.00** | **Literal-action cutaway, cut on the rhythm** | "*you sprint by mashing X. Tap, tap, tap, tap*" cuts to 4 clips of Franklin sprinting in 3.0 s — the cut rate mimics the button mashing. |
| **5:01.40–5:05.20** | **Over-energetic montage on a throwaway line** | 7 Destiny 2 clips in 3.8 s (the densest cutting in the video) for a one-sentence personal aside. The scale mismatch is the joke. |
| **5:29.60–5:32.35** | **Cold ending on a held stare** | Extreme close-up, points at lens, drops the hand, stares, cut to end. No outro furniture at all. |

**Not found (checked for):** no repeated/stuttered frames, no freeze-frame-with-text, no zoom-punch transitions, no shake/impact frames, no meme cutaways, no sound-effect-driven flash frames, no speed ramps, no slow motion anywhere (`slowmo.json` shows only 30→60 fps conform and still images).

---

## 6. Palette + type summary

### Colours (sampled from the frames, so these are estimates from compressed JPEG — treat as ±5 %)

| Swatch | Hex | Where |
|---|---|---|
| Hot pink / magenta | **`#EE2A9A`** | the `2` on poster 1; the primary accent of the system |
| Orchid pink | **`#DF6BE1`** | `STICKINESS` / `LESS` on poster 4 (the lighter variant used over near-black) |
| Rockstar pink | **`#EE38A2`** | the R★ card gradient low end |
| Electric blue | **`#0B37AC`** / `#2C3EC0` | poster 1 top, R★ card upper-left |
| Violet | **`#533488`** / `#7F2096` | mid-gradient on both, poster 2's dusty rose family |
| Cream / bone (all headline type) | **`#F7EFDA`** — also `#F4EED2`, `#EFE1C7` | every big word on every card |
| Near-black card navy | **`#0F1122`** | poster 4 body |
| Pale mint green | **`#A1D7AD`** | poster 3 only — `GTA 5`, tracker boxes, the `DON'T REACT` glow |
| Set green (wall wash) | **`#5BAC5D`** / `#96AD89` | the room, every face shot |
| Leather brown | **`#885744`** / `#391810` | the armchair, lower-left of every wide face shot |
| Room black | **`#070503`** | frame-left edge, the monitor wedge frame-right |

Overall luma across the video: **mean 0.282, only 3 % dark frames and 8 % bright** — a consistently dim, saturated, neon-lit picture that the bright cards punch out of.

### Type classes — three, total

1. **Heavy condensed grotesque, all caps** (Anton / Archivo Black class), tight tracking, subtle drop shadow. Carries every headline word on every card: `CONCEALED HANDGUNS`, `PERSONAL`, `VEHICLE`, `ENTIRE SELECTED`, `LOADOUT`, `DON'T REACT`, `STICKINESS`, `LESS`, `DEFAULT`, `LOCK ON`. Always cream, except the one accent word per card which is pink (or green on poster 3).
2. **Bold condensed sans, all caps, letterspaced**, smaller, white. Carries every connective line: `YOU CAN ALWAYS HAVE`, `ON YOU WHENEVER YOU WANT`, `ONLY YOUR`, `CARRIES YOUR`, `IN GTA 5`, `A LITTLE BIT OF`, `ON THE AIMING`, `BUT LEANING MORE TOWARDS`, `THAN PREVIOUS GAMES`, `ZERO REACTION`, `PREVIOUS GAMES`.
3. **Light wide sans numerals** — `01` / `02` on poster 1 only.

Plus two **found** typefaces that are not his: the GTA VI wordmark on poster 2, and YouTube's own Roboto UI in the thumbnail callback.

**Casing rule: everything is upper case.** There is no lowercase type anywhere in this video except inside found artefacts (the YouTube row) and the `skool` neon on the wall.

**One accent word per card, and only one.** Poster 1 → `2`. Poster 2 → `PERSONAL`. Poster 3 → `GTA 5` (+ the green glow). Poster 4 → `STICKINESS` and `LESS`. The accented word is always the load-bearing one.
