# Visual catalogue — "GTA 6's NPC AI Is LITERALLY From The Future"

Affan Afterhours, uploaded 2026-09-08, **~350 views at audit — a flop between hits** (its own callback shows Fuel System
at "148K views · 8 days ago", so it went up a week after the 170k video).
Master read: `raw/npc-ai.mp4` — YouTube 1080p download, 1920×1080, **59.94 fps**, **6:54.69** (414.7 s).

Evidence: all 28 contact sheets (`frames/sheet_001–028.jpg`, 2 fps); 36 full-res stills in `frames/full/` named by
second; strips `frames/step_*.jpg` at 4–20 fps for the B&W shrink (0:05), the first caption-poster (0:55), the face whip
(1:10), the mirror flip (2:37), the colour bars (2:43), the self-callback (4:31), the 4:55 jump, the colour shrink (6:22)
and the ending. Numbers: a scratch run of the facecam preset's own `style-probe.py` and `slowmo-scan.py` on this file,
an ffmpeg scene-change pass (0.15), a card-box tracker, and a word-timed scratch transcript (faster-whisper medium.en).
The background `probe/` and `transcript/words.json` had not landed when this was written; they supersede these numbers
when they do. **"Looks like"** = inference. Timecodes ±0.1 s.

**One-line read:** the same card system as PS5 Pro (the Vice City quote card, now joined by a staircase "explainer"
card and full-width **caption-posters**), cut into a **bright coral room with sunglasses and a boxing-glove mic** — but
with a nearly static face (no push, small snaps, no extreme close-up), more GTA V than GTA 6 on screen, and long
uncovered face stretches, two of them 25–36 s at the back end.

---

## 1. The face shot

### Framing (YuNet, 1,281 face samples outside overlays)

| | face-box height (fraction of 1080) | |
|---|---|---|
| p10 (base) | 0.336 | same base size as PS5 Pro |
| median | 0.375 | |
| p90 | 0.439 | only **1.3× base** — 18 % of face time is at ≥ 1.25×, **0 % at ≥ 1.6×** |
| max | ~0.60 | ≈ 1.6–1.8×, once or twice |

- Face centre x **0.514**, face top y 0.263: centred, the `skool` sign above-right.
- **Gradual push: median 3.1 % per held shot = 0.32 %/s** — effectively static (PS5 Pro 1.92 %/s, Fuel System 1.79).
- **Snap zooms:** 33 plausible zoom-ins = **7.6 per minute of face**, median **×1.19** (p25–p75 1.13–1.24), held a long
  **1.6 s**. The biggest ≈ 1.6× at 1:19.2–1:20.6 ("…NPCs notice it and react. In GTA 5 you could drop a grenade at
  someone's feet") and ≈ 1.5× at 3:00–3:03 (pointing up, "You can throw dog shit at people"). **No extreme close-up
  anywhere.**
- **Reading off the monitor, left in:** the face turns 3/4 to frame-right and reads at 1:55.5–2:03.5, 2:06,
  2:31.5–2:37, 3:17–3:27.5, 4:45–4:55.5, 5:25.5–5:36, 6:30–6:34 — about **50 s of the runtime is visibly read**.
- Jump cuts on gestures; one **face-to-face whip** (1:10.95–1:11.25, a 0.3 s sideways smear between two takes,
  `step_0110_whip.jpg`) on "Oh, and they notice objects too."

### The set (the warm, late look)

- Wall washed **coral-red `#FF643A`–`#FF5B65`** with **hot pink/magenta** at the top-left, the multicolour `skool` neon
  frame-right of the head, a small framed print top-left (white with a red emblem — looks like a YouTube play-button
  plaque), brown leather sofa behind, dark monitor at frame-right. Bright, high-key: mean luma 0.375, 43 % "bright"
  frames, 3 % dark.
- Wardrobe: **maroon crew-neck T-shirt**, **red-framed round sunglasses with blue-tinted lenses** (mirror-glare at
  times), a black-strap watch on the left wrist.
- **The mic is a prop:** a **gold-and-black VENUM boxing glove** held upright like a handheld mic, a **DJI-style lav with
  a fuzzy windscreen clipped on top** (`full/t_362.0.jpg`) — the same "lav on a prop" gag as the README's spatula
  (RISKIEST).

### Bugs / lower-thirds / captions / subscribe

No logo, no lower-third, no name strap, no subscribe animation (all 28 sheets). **But there is on-screen text that is
not a card:** three full-width **caption-posters** (§ 3c) that set the spoken sentence over blurred footage.

---

## 2. Cold open (0:00 – 0:45)

| # | in – out | on screen | said |
|---|---|---|---|
| 1 | 0:00.0–0:05.8 | Face, base, holding the glove-mic; a ~1.2× snap at 0:04 | "In GTA 5, pedestrians were furniture. You could walk past a cop holding a shotgun and" |
| 2 | 0:05.8–0:07.1 | **The face shot desaturated to black-and-white and shrunk to ~80 %, centred on black** (`step_0005_bw.jpg`) — a "this is the old way" tag | "and he'd nod at you." |
| 3 | 0:07.1–0:12.7 | **GTA V**: a shirtless robber in a 24/7 store, clerk hands up | "You could rob a store in front of 40 people. Not one of them did anything but scream." |
| 4 | 0:12.7–0:16.1 | Face | "GTA 6 gave every single NPC a brain because" |
| 5 | 0:16.1–0:20.6 | **Key-art card**: "GtA6 HAS / 600,000 / NPCs" in a Pricedown-style face with a purple→pink gradient fill, over the official Lucia & Jason gas-station key art; ~82 % wide, drop shadow, over a blurred GTA V plate | "600,000 of them and every single one is handmade." |
| 6 | 0:20.6–0:24.1 | Face, a ~1.3× snap at 0:21.8 | "NPCs are handmade! Here's what's in this video." |
| 7 | 0:24.1–0:30.6 | **GTA V** Michael/FIB rooftop gun standoff → **GTA 6** a woman at an open car trunk → GTA 6 a man in sunglasses arguing on a brick street | "What happens when you point the gun at the wrong pedestrian? And why you're gonna start putting bodies in the trunk of your car?" |
| 8 | 0:30.6–0:37.3 | Face | "Let's start at the beginning, before the crime. Walk down the street with a rifle on your back? Fine, nobody cares. Take it in your hand." |
| 9 | 0:37.3–0:40.9 | **GTA 6 Extended Look**: a masked woman in yellow walks into a pawn shop ("WE DO REPAIRS"); two NPCs edge away | "Rob Nelson described exactly what happens, and we saw that." |
| 10 | 0:40.9–0:45.7 | Rob Nelson quote card (§ 3b #1) | read verbatim |

Read: voice from 0.000 on the face; the **first picture is GTA V** (0:07), the first GTA 6 image is static key art
(0:16), the **first GTA 6 gameplay arrives at 0:27.5**. The "what's in this video" is two items in six seconds. 34 s of
the first 60 s are overlay, so the open is not visually thin — it is backward-looking (GTA 5) and promise-light.

---

## 3. Every overlay, in order

### 3a. Master table

**G6** GTA 6 footage · **G5** GTA V footage · **C-VC** Vice City quote card · **C-EX** staircase explainer card ·
**CP** caption-poster · **FF** other full frame. All game footage full-frame, sharp, HUD left in.

| # | in – out | dur | kind | what | said over it |
|---|---|---|---|---|---|
| 1 | 0:05.8–0:07.1 | 1.3 | face device | B&W shrunken face on black | "and he'd nod at you." |
| 2 | 0:07.1–0:12.7 | 5.6 | G5 | 24/7 robbery | "You could rob a store in front of 40 people…" |
| 3 | 0:16.1–0:20.6 | 4.5 | key-art card | "GtA6 HAS 600,000 NPCs" | "600,000 of them and every single one is handmade." |
| 4 | 0:24.1–0:30.6 | 6.5 | G5 → G6 ×2 | rooftop standoff; trunk; argument | "point the gun at the wrong pedestrian… bodies in the trunk" |
| 5 | 0:37.3–0:40.9 | 3.6 | G6 | pawn-shop walk-in, NPCs move away | "Rob Nelson described exactly what happens" |
| 6 | 0:40.9–0:45.7 | 4.8 | **C-VC** | Nelson #1 | verbatim |
| 7 | 0:45.7–0:49.1 | 3.4 | FF found clip | a young YouTuber in a white headset, navy Tommy Jeans tee, green screen, grinning to camera | "The YouTuber who got flown out to Rockstar North watched it happen." |
| 8 | 0:55.8–1:02.4 | 6.6 | **CP** | "That's exactly how a real person responds…" (§ 3c) over blurred jewellery-store → street footage | verbatim |
| 9 | 1:03.5–1:06.9 | 3.4 | G5 | Vespucci beach panic | "The GTA 5 pedestrians were literally like a screaming cartoon." |
| 10 | 1:12.8–1:17.3 | 4.5 | **C-VC** | NYT / drop something | verbatim |
| 11 | 1:28.7–1:36.1 | 7.4 | **C-EX** | "REPORT THE CRIME" (§ 3b) | verbatim, card builds nothing — all text on at once |
| 12 | 1:42.0–1:45.1 | 3.1 | G5 | Sandy Shores trailer park fight, a dog | "not the cops, the guy walking his dog." |
| 13 | 1:49.0–1:52.7 | 3.7 | icon panel | black rounded panel ~82 % over a blurred street, **four red neon-ringed icons**: two people, a coat hanger, a head-and-shoulders bust, a car (the witness-description icons) | "That's how you get those icons so that police can actually try…" |
| 14 | 2:04.0–2:05.8 | 1.8 | FF meme | **black-and-white** stock reaction: a man with both hands on his head, mouth open | "…her car and call the police with it." |
| 15 | 2:19.2–2:22.0 | 2.8 | G6 | old man with a shotgun outside the FOOD MART | "some pedestrians are carrying. It's America." |
| 16 | 2:25.9–2:31.4 | 5.5 | **C-VC** | pet dogs | verbatim |
| 17 | 2:43.15–2:43.33 | 0.2 | FF | **colour bars, VHS-damaged** (tearing, noise — not PS5 Pro's clean card) | "And I — need to tell you the dog thing." |
| 18 | 2:49.2–3:00.2 | 11.0 | **CP** | the dog-bag sentence (§ 3c) over four changing blurred plates (a Rockstar livestream with chat, beach umbrellas, a village, a dirt-bike trail) | verbatim |
| 19 | 3:11.4–3:17.2 | 5.8 | G6 | low-angle palms and towers, blue sky — static | "…why there was a whole f—ing building reserved for just NPC animations" |
| 20 | 3:28.0–3:35.8 | 7.8 | G6 | masked man in a car back seat → the cap-wearing shooter and the flipping police truck (**the same clip as PS5 Pro 7:05**) | "TGG watched Rob get into a three star gunfight… The NPCs who were far away ran away." |
| 21 | 3:42.1–3:46.7 | 4.6 | **C-VC** | TGG | "In TGG's words, they were afraid of their lives." |
| 22 | 3:56.1–4:01.2 | 5.1 | G6 | Trailer 2: Jason & Lucia's van in an alley | "…so they just hid behind the car." |
| 23 | 4:02.7–4:08.2 | 5.5 | **C-VC** | Nelson "instantly" | verbatim |
| 24 | 4:22.6–4:30.3 | 7.7 | **CP** | "Every NPC is handcrafted…" over blurred driving footage | verbatim |
| 25 | 4:31.6–4:32.8 | 1.2 | **self-callback** | his own YouTube row: Fuel System thumbnail (Lucia, "YOU CAN'T STEAL CARS", 6:54, red watched-bar), "GTA 6's Fuel System Isn't The Problem...This Is / 148K views · 8 days ago", ~70 % wide, **over a blurred copy of his own face shot** (`step_0431_callback.jpg`) | "in previous videos." |
| 26 | 4:33.7–4:41.1 | 7.4 | **C-EX** | "HEIGHT AND BODY TYPES" (§ 3b) | verbatim |
| 27 | 5:16.6–5:19.1 | 2.5 | G5 | Michael with a rifle on a balcony at dusk (cutscene) | "You're not the only criminal in the game." |
| 28 | 5:22.2–5:25.6 | 3.4 | G6 | night convertible, intersection explosion (**PS5 Pro 6:23 again**) | "Rubeus hit a massive traffic jam caused by a crashed car and" |
| 29 | 5:36.3–5:39.5 | 3.2 | G5 | FIB rooftop shootout cutscene, a headshot | "It's not like it was inside of a story mode, inside of a mission" |
| 30 | 5:48.2–5:56.8 | 8.6 | G5 | desert highway gameplay: a car hits a pedestrian, a fistfight, "Steal the RV" mission text, minimap | "For 25 years, bodies in GTA games have just evaporated… Nothing happened." |
| 31 | 6:02.5–6:10.7 | 8.2 | **C-EX** | "LUCIA PUTS CORPSES IN THE TRUNK." (§ 3b) | verbatim |
| 32 | 6:22.6–6:24.6 | 2.0 | face device | **colour** face shot shrunk to ~80 % on black (`step_0622_shrink.jpg`) | "oh, GTA 6 is dead. They're just doing too much." (an imagined viewer) |
| 33 | 6:25.1–6:30.1 | 5.0 | G5 | Vespucci beach, a car ploughing through sunbathers | "You can still drive down the beach, run everyone over on day one." |

**32 overlay events (4.6/min) in 29 runs (4.2/min), 37 % of runtime; median run 5.1 s; face 63 %.**
Text screens: **6 quote cards + 3 explainer cards + 1 key-art card + 3 caption-posters = 13 (1.9/min, ≈ 77 s of
reading)**. Game footage: **GTA V 8 runs ≈ 35 s, GTA 6 7 runs ≈ 32 s** — more old game than new on screen, two GTA 6
clips recycled from PS5 Pro. No portrait, no screenshot, no colour matte.

### 3b. Cards

**C-VC — the Vice City quote card (6), the PS5 Pro template unchanged:** blue `#0427B5` → magenta → hot-pink panel,
palms, skyline with a setting sun, an inner rounded **neon-line frame**, white heavy sans in sentence case, accent words
in **hot pink, CAPS**, big pink “ ” marks, "- ROB NELSON / ROCKSTAR" attribution under a thin rule. 75–81 % wide at
entry, **growing ~1 %/s** (tracked 78→82 % over 3.8 s, 81→85 % over 4.8 s), centred, hard cut in and out, over blurred
moving game footage. The type face shifts card to card (a geometric bold on some, a narrower humanist bold on others) —
looks like each card is generated as an image, not typed from one template. Verbatim (typos kept):

1. 0:40.9 — "if you've got one in your hand, people don't like it and they react and start **MOVING AWAY FROM YOU.**" ·
   - ROB NELSON / ROCKSTAR
2. 1:12.8 — "rockstar told the **NEW YORK TIMES** that if you drop something **NPC** notice it and react" · - ROB NELSON /
   ROCKSTAR *(a paraphrase in quote marks, attributed to Nelson)*
3. 2:25.9 — "you can't just **PET DOGS** anymore. You have to ask the owner. Some dogs **BARK** and **REFUSE**" · - ROB
   NELSON / ROCKSTAR
4. 3:42.1 — "they were afraid of **THEIR LIVES**" · - TGG *(no quote marks, centred)*
5. 4:02.7 — "the whole point was to get past the old GTA where they forget about you **INSTANTLY**" · - ROB NELSON
6. (the 600k key-art card at 0:16.1 is a different design: Pricedown-style "GtA6 HAS 600,000 NPCs" on official art)

**C-EX — the staircase explainer card (3), new in this video:** a full-bleed illustrated night scene (looks
AI-generated) inside a card ~80–95 % wide over a blurred plate. Copy is **stepped down the card in alternating sizes** —
a small cream condensed kicker ("SOMEONE NEEDS TO"), a big cream condensed line ("REPORT"), with **one pink accent**
(`#AB3174`-ish dusty pink on the dark art) — and thin pink leader lines/arrows tie the words to picture details.
1. 1:28.7 — "SOMEONE NEEDS TO / **REPORT** THE CRIME *(pink)* / USUALLY BY / **PHONE** / OR IF YOU SET AN / **ALARM OFF** /
   OR YOU STEAL A VEHICLE WITH A / **TRACKER**" — a man on a phone with pink signal rings, a store alarm, a car pinging a
   tracker.
2. 4:33.7 — "THEY COME IN A FULL RANGE OF / **HEIGHT AND BODY TYPES** / THEY POST ON THE / **IN-GAME SOCIAL MEDIA** *(pink)* /
   AND YOU CAN / **GO TO ANYWHERE** / THEY POST IT FROM" — a crowd on a neon Vice City street (O'Grady's Bar & Grill),
   body-type silhouettes, a phone mock-up of a "VCE_Vibes" post.
3. 6:02.5 — "LUCIA PUTS CORPSES IN THE **TRUNK.** *(pink)* / YOU CAN HIDE / **BODIES IN CAR BOOTS** / YOU CAN ALSO **HIDE
   YOURSELF** *(pink)* IN ONE." — Ocean View Motel at night, Lucia at an open trunk, a hologram body-in-trunk diagram, a
   framed trunk close-up.

### 3c. The caption-poster (3) — text with no card

- The spoken sentence set **full width, centred, in white heavy condensed caps (Anton/Bebas class) with a dark soft
  shadow**, 3–4 lines, cap height ≈ 45 px, sitting in the **upper-middle band (y ≈ 0.37–0.70)**, **3–4 accent words in
  violet-magenta `#D100F6`** (a different, bluer pink than the cards).
- Over **soft-blurred, still-moving game footage** that may hard-cut behind it (the 11-s one changes plate four times).
- All text on at once on a hard cut (`step_0055_poster_in.jpg`), no animation, hard cut out.
- Verbatim: "THAT'S EXACTLY HOW A **REAL PERSON** RESPONDS / THEY'RE NOT PANICKING / THEY'RE **LEAVING** QUIETLY SO THEY
  DON'T DRAW **YOUR ATTENTION**" (0:55.8) · "AN **NPC** WALKS THEIR DOG THE DOG DOES ITS BUSINESS / THE OWNER PICKS IT UP IN A
  **LITTLE BAG** YOU CAN HIT THE OWNER / THEY **DROP** THE BAG AND YOU PICK UP THE BAG / YOU CAN THROW AT **PEOPLE**" (2:49.2) ·
  "EVERY NPC IS **HANDCRAFTED** NOT GENERATED / WITH AN **ENTIRE** OFFICE IN LOS ANGELES DEDICATED / TO JUST **PEDESTRIANS**"
  (4:22.6).

---

## 4. Recurring patterns

- **Quote → card, comparison → GTA V.** Every Nelson/TGG/Rockstar line is a card; every "in GTA 5…" line is a GTA V clip.
  The NPC behaviours themselves (walking away calmly, the leash wrapping an arm, picking up the hat, hiding behind cars,
  remembering you) are **told in type, not shown** — only the pawn-shop clip (0:37) shows one.
- **Face runs:** median 6.5 s but a long tail — **4:41.1–5:16.6 = 35.6 s** with no insert and only nudges (the Rob
  bug-testing story and the "10 years ahead of the industry" line, which PS5 Pro had set as two cards), 6:30.1–6:54.7 =
  24.6 s (the close), 2:05.8–2:19.2 = 13.4 s, 1:52.7–2:04.0 = 11.3 s (read off the monitor).
- **Cut rate:** probe 11.9 cuts/min, the lowest of the three (by minute 15/13/14/11/13/11/5.5); scene-change pass ≈ 22
  visible changes/min. The last minute is the emptiest.
- **Words:** 187/min, no pauses ≥ 1 s; delivery repeats left in ("and and it wraps", "It's literally, it's literally
  everyone. It's literally everyone.").
- **Slow motion:** the duplicate-frame scan reads ≈ 0.5× on most game inserts and card plates (as in PS5 Pro — consistent
  with 30-fps sources on a 59.94 timeline as much as with deliberate slow motion); no face slow-down is measurable
  (0.8× is below the scan's threshold).

## 5. Comedy and emphasis devices

| device | where | spec |
|---|---|---|
| **B&W shrink** | 0:05.8 | face desaturated, ~80 % on black, 1.3 s: the GTA 5 cop "nod" |
| **colour shrink** | 6:22.6 | the same shrink in colour, 2.0 s, for an imagined viewer's voice ("GTA 6 is dead") |
| **mirror flip** | 2:37.25–2:41.3 | the face shot **flipped horizontally** for 4 s (the `skool` neon reads backwards, `step_0237_mirror.jpg`), head turned, on "Holy graphics. Rockstar built leash physics for…" — looks like a "second voice" gag |
| **VHS colour bars** | 2:43.15 | 0.2 s damaged bars as the turn into "I need to tell you the dog thing" |
| **B&W shock meme** | 2:04.0 | 1.8 s stock reaction |
| **the named YouTuber** | 0:45.7 | 3.4 s of the person being cited, grinning, as a reaction shot |
| **self-callback** | 4:31.6 | his own 148K Fuel System row on a blur of his own face, 1.2 s |
| **face whip** | 1:10.95 | 0.3 s smear between two face takes |
| **wider jump** | 4:56.25 | a jump to a slightly wider frame, head tilted back, mimicking "the co-head of development taking notes" |

No extreme close-up, no card punch-in, no zoom ladder.

## 6. Palette and type

- Room: coral `#FF643A`/`#FF5B65`, hot-pink top-left, maroon tee, red sunglasses, gold glove — the warmest, brightest set.
- Quote cards: blue `#0427B5` → magenta/pink, accent hot pink; explainer cards: dark night art, cream condensed type,
  dusty-pink accent `#AB3174`; caption-posters: white condensed caps, accent **violet-magenta `#D100F6`**; key-art card:
  purple→pink Pricedown.
- Three text systems in one video (sentence-case quote card / cream condensed staircase / white condensed caption).

## 7. Ending (6:30 – 6:54.7)

6:30.1 hard cut from the GTA V beach to the face for the last **24.6 s**, no inserts, one small snap: "Nelson's entire
pitch is that you have more freedom, not less… But this is a bit confusing. So we'll have to play the game on our own
to understand all of these details. So in short, when Rob said there's a whole world that's watching you, it's not just
cops. It's literally, it's literally everyone. It's literally everyone. Do let me know what your thoughts are inside of
the comments." Arm sweep at 6:48.7, points at lens at 6:50.7, finger raised at 6:53.0, **cut on the base face**
(`step_0645_end.jpg`). No end card. The only spoken CTA of the three videos.

## 8. Differences vs README.md and CREATOR-HAND.md

| doc says | NPC AI does |
|---|---|
| Push ~1 %/s via the 105/110 preset | **0.32 %/s** — no push to speak of |
| Cut zooms median 121–136 %, 4–10/min, extremes 160–360 % | ×1.19 median, 7.6/min of face, **no extreme**, held long (1.6 s) |
| Overlays: game footage first, GTA 6 Extended Look/trailers; old games only when the line is about them | ✔ the rule held (GTA V on "in GTA 5…" lines) but the script leans on GTA 5 so often that **GTA V outnumbers GTA 6 on screen**; two GTA 6 clips reused from PS5 Pro |
| Posters: verbatim quote or numbered rule; held 3–7 s; ~72 %; grow; hard cuts | ✔ quote cards behave so (4.5–5.5 s, 75–85 %, grow ~1 %/s); explainer cards and caption-posters are extra text systems the README does not have |
| No captions / no other text | **three caption-posters** — the spoken line typeset over blurred footage |
| Nothing is an inset; inset over a colour matte since 09-30 | insets only on blurred plates (the callback sits on a blur of the face itself) |
| Two long graphic-free stretches per video | ✔ two — but 35.6 s and 24.6 s, both in the last third, much of it read off the monitor |
| The prop mic (spatula, RISKIEST) | ✔ a boxing glove with the lav on top |
| Colour-bars glitch (CREATOR-HAND) | ✔ once, VHS-damaged variant |
| Subscribe animation twice | none |
| Ends cold on the face | ✔, after a spoken comment CTA |

**Era markers:** this is the first of the three in the later look — coral wall, sunglasses, lav on a prop, maroon tee —
but it still uses the August card system (Vice City quote cards) rather than CREATOR-HAND's colour-matte insets, and its
face grammar is far flatter than the creator's later timelines (no nests/presets visible, no ladders, no extremes).
