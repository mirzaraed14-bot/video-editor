# Visual catalogue — "GTA 6's Fuel System Isn't The Problem…This Is"

Frame-by-frame dissection of the editing style. Master: `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\GTA Cars.mov`
— 1920×1080, 60 fps, 6:53.07 (413.07 s), 170k views, the channel's best performer.

Evidence: all 78 post-cut frames in `probe/cuts/`, the segment mid-frames, `probe/summary.md`,
`probe/probe.json`, `slowmo.json`, `transcript/words.json`, plus ~60 extra frames pulled from the
master at 1/10–1/20 s around every graphic boundary. Anything marked **"looks like"** is an inference.

---

## 1. The face shot

### Framing

One camera, one lock-off, one position for the whole video. Everything else is done in post with
scale keyframes.

Measured off the 1,446 face-detector samples that fall inside talking-head segments (box ≈ brow to chin,
fractions of the 1080 px frame height):

| | face-box height | in px |
|---|---|---|
| tightest 10 % of samples | 0.311 | 336 px |
| **median** | **0.354** | **383 px** |
| loosest 10 % | 0.543 | 586 px |
| maximum | 0.719 | 777 px |

- **Base shot = medium.** Head + shoulders, chest cut at the bottom edge, the whole head about half
  the frame height. You can see the chair back, the plant, the neon sign, the monitor edge.
- **Tightest shots are ~2× the base** (0.72 vs 0.31 face-box height) — a genuine extreme close-up
  where the head overflows the top of the frame. Examples: **2:00.20**, **4:07.40**, **4:55.20**,
  **6:07–6:08**.
- **Face centre x = 0.513 median** — dead centre, and it stays centred on the wide shots. The extreme
  close-ups break that: at **4:55.20** the head is shoved to the right third and he is looking out of
  frame left.
- **Face centre y = 0.389 median** — the face sits in the upper-middle. **Headroom: face-box top at
  y = 0.204 median**, i.e. roughly 220 px of wall/neon above the brow. Generous but not empty —
  the neon sign lives in that band.
- The camera is very slightly **below eye line** (you read a touch up at him), lens looks wide-ish
  (the leather chair curves off behind him).

### What changes between jump cuts

Framing changes on **almost every cut**, and often *inside* a cut:

- **Gradual push:** every held face shot ≥ 1.5 s creeps in. Median **+9.5 % scale per shot =
  1.79 %/s**. Nothing sits still.
- **Cut zooms:** **143 step-ins and 134 step-outs** over 6:53. Median step **×1.3**, median hold
  **0.4 s**. These are hard scale jumps *inside a continuous take* — the audio never cuts, the crop
  snaps. Watch **6:04.8 → 6:08.0**: six distinct crop levels in four seconds on one sentence.
- Biggest single step in the video: **×2.57 at 3:09.00** — and it's on *game footage*, not the face.
- A handful of B-roll-sized steps: ×1.88 at 6:39.60, ×2.21 at 5:57.00, ×1.81 at 2:22.20.

### The set

- **Back wall:** plain white/eggshell, washed with a **lavender/magenta LED** (`#D299F4` where the
  light lands). The purple is the single most identifying colour in the room.
- **Neon sign** on the wall behind his right shoulder, at head height: lowercase **"skool"** in tube
  neon, each letter a different colour — cyan `s`, magenta/pink `k`, warm-white `o`, cyan-white `o`,
  orange-red `l`. It sits in the headroom band and is in almost every wide face shot.
- **Framed print** further left on the wall: a small portrait-format piece, pink/orange gradient.
- **Far left:** a window with dark purple-painted burglar bars / grille, plus a sliver of white wall.
- **Chair:** a big **brown leather** armchair/sofa back (`#512B23`), bolster roll visible behind his
  shoulders. It fills the left third of the base shot.
- **Right:** a **plant with round dark-green leaves in a brass/gold pot** on a dark sideboard, and
  the bezel of a **monitor** cutting into the right edge of frame.
- **Mic:** a large condenser on a desk boom in the lower-centre of frame — black body, **bright red
  mesh grille**, red-and-black shock mount, capsule roughly on his sternum line. It is the one
  saturated warm object in a cool-purple room and it is in every single face shot.
- **Lighting:** soft key from camera-front-left (his face is evenly lit, mild shadow on the right
  cheek), purple practical filling the background. Mean frame luma across the video 0.337, 11 % dark
  / 16 % bright — a dim, moody picture overall.

### Wardrobe

Identical for the whole 6:53 — no wardrobe change, no reshoot:

- Plain **black crew-neck t-shirt**, no print, slightly loose.
- **Black-framed sunglasses with amber/orange lenses**, worn indoors the entire video. His eyes are
  visible through them but tinted — this is the face's signature.
- Black hair, full dark beard.
- **Dark brown leather watch** on the left wrist (visible whenever he gestures, which is constantly).
- He holds a small **white/mint vape pen** in his hand through large stretches (2:34, 3:10, 5:13,
  6:33) and gestures with it.

### Bugs, lower-thirds, captions

- **No persistent bug. No logo. No watermark. No lower-third. No name strap.** The frame is completely
  clean 100 % of the time except for the two subscribe animations below.
- **No burned-in captions or subtitles anywhere.** Checked all 78 cut frames plus a 2-second-interval
  sweep of the whole runtime — zero caption frames. (YouTube CC only.)
- **Subscribe animation, twice, bottom-left, unannounced:**
  - **2:34.5 → 2:43.2** (~8.7 s) and **5:40.5 → 5:48.8** (~8.3 s).
  - Canned asset: a white rounded-square tile with a **grey bell** slides/pops in, then a **red pill
    reading "SUBSCRIBE"** in white caps wipes out from behind it left→right. A **mouse cursor** flies
    in and clicks. The bell turns **YouTube blue and rings**, the pill wipes to **white with black
    "SUBSCRIBED"**. It holds ~4 s, then the pill wipes away right→left and the bell shrinks out.
  - Type on the pill is a plain wide grotesque, all caps, no tracking tricks.
  - It plays over whatever happens to be on screen — the second one starts over GTA V gameplay and
    finishes over the face. It is not cued to anything he says.

---

## 2. Cold open (0:00 – 0:30)

Eleven shots in thirty seconds. Cut rate in minute 1 is **15.0/min**, the highest in the video.

| # | in – out | dur | on screen | what's said |
|---|---|---|---|---|
| 1 | 0:00.00 – 0:02.00 | 2.0 s | Face, base medium. Hand raised near his face, then opening out. | "The entire internet is arguing…" |
| 2 | 0:02.00 – 0:03.40 | 1.4 s | **Live-action meme clip**, teal-lit corridor: a man in black tactical gear shoving / arguing with someone in a cheap **Spider-Man costume**, red exit light behind them. **Pillarboxed** — hard black bars left and right, the only non-full-frame insert in the video. | "…whether GTA 6 should have fuel or not." |
| 3 | 0:03.40 – 0:03.80 | 0.4 s | Same clip, **hard punch-in to full width** — the black bars are gone, Spider-Man's mask fills the right half. A 24-frame beat. | (tail of the same line) |
| 4 | 0:03.80 – 0:07.20 | 3.4 s | Face, both hands up and open, framing slowly pushing in. 4 cut-zoom steps inside this one shot (0:04.60 ×1.20, 0:05.40 ×1.73, 0:06.00 ×1.55, 0:06.60 ×1.76). | "Now it does. It's confirmed. And I get it. 25 years of GTA…" |
| 5 | 0:07.20 – 0:09.60 | 2.4 s | **GTA 6 footage**, full frame: chase-cam behind a dark sedan on a palm-lined coastal highway into a low sun, truck and freight in the lane. Sharp, unblurred, radio/HUD widget bottom-left. | "…and now your car needs gas. People are upset. But…" |
| 6 | 0:09.60 – 0:15.40 | 5.8 s | Face, wide. Both hands up and shaping. 4 more cut-zooms inside. | "…I've been going through everything the developers have released this week, and I'm here to tell you, the fuel is…" |
| 7 | 0:15.40 – 0:16.80 | 1.4 s | **GTA 6 footage**: Lucia in a car passenger seat, red bandana mask, gloved hands, sun flare through the windscreen. | "…nothing. The fuel is the least insane thing…" |
| 8 | 0:16.80 – 0:17.80 | 1.0 s | **GTA 6 footage**, tighter on Lucia, flare blowing out the left of frame. | "…Rockstar has done…" |
| 9 | 0:17.80 – 0:19.40 | 1.6 s | **GTA 6 footage**: extreme close on a red car bonnet at a gas-station canopy, camera cranes up to reveal a man aiming a pistol outside a **FOOD MART**. | "…to this game." |
| 10 | 0:19.40 – 0:26.00 | 6.6 s | Face, wide, both hands up in a "calm down" shape. Three cut-zooms. | "Here's what's actually in this video. There's a car in GTA 6 that snitches on you if you drive it too slow. I'll explain." |
| 11 | 0:26.00 – 0:29.60 | 3.6 s | **GTA 6 footage**, very dark: Lucia driving at night looking back over her shoulder, camera drifts to Jason in the passenger seat against a blown-out window. Heavily slowed (≈0.15×). | "There's a fee, an actual fee with a price in the game that…" |
| — | 0:29.60 → | | Back to face; the cold open runs straight into the body with no title card, no logo sting, no music drop visible. | |

**The cold open has no title card and no channel branding at all.** First frame is his face, and the
first insert lands two seconds in.

---

## 3. Every overlay, in order

### 3a. Master list

"Bg cut" = the footage *behind* a held card hard-cuts while the card stays put.

| # | in – out | dur | kind | line being spoken |
|---|---|---|---|---|
| 1 | 0:02.00 – 0:03.40 | 1.4 s | Live-action meme clip (Spider-Man), **pillarboxed** | "whether GTA 6 should have fuel or not" |
| 2 | 0:03.40 – 0:03.80 | 0.4 s | Same clip, punched to full frame | (same line) |
| 3 | 0:07.20 – 0:09.60 | 2.4 s | GTA 6 — highway chase-cam | "and now your car needs gas. People are upset. But" |
| 4 | 0:15.40 – 0:16.80 | 1.4 s | GTA 6 — Lucia, bandana, pistol | "nothing. The fuel is the least insane thing" |
| 5 | 0:16.80 – 0:17.80 | 1.0 s | GTA 6 — Lucia, tighter | "Rockstar has done" |
| 6 | 0:17.80 – 0:19.40 | 1.6 s | GTA 6 — bonnet → Food Mart holdup | "to this game" |
| 7 | 0:26.00 – 0:29.60 | 3.6 s | GTA 6 — night drive, Lucia → Jason (≈0.15× slow) | "There's a fee, an actual fee with a price in the game that" |
| 8 | 0:36.60 – 0:40.40 | 3.8 s | **Real interview clip** — Rob Nelson (Rockstar), grey beard, black V-neck, white studio behind. Slowed to a crawl (≈0.03×) with a slow push-in, so it reads as a near-freeze reaction shot. | "at the end of the video I'm going to show you a quote from Rockstar's co-head of development mid-gameplay" |
| 9 | 0:59.20 – 1:08.40 | 9.2 s | **GTA V gameplay**, full frame, HUD intact (minimap, "Elgin Ave", ammo counter). One unbroken take: walk to a black classic car at night → smash window → get in → hotwire → drive off. Slowed to ≈0.2× to cover the whole description. | "you see a car, you press triangle… you break the window, hands do the wiggle wiggle hot wire thing… three seconds boom you're out" |
| 10 | **1:21.80 – 1:23.80** | 2.0 s | **TEXT POSTER** — "STEP 1: YOU CHECK AN APP" | "Step 1. You check an app. Before" |
| 11 | 1:47.80 – 1:51.00 | 3.2 s | **GTA 6 preview gameplay** — a guy beside a maroon muscle car, PlayStation prompts **▲ SLIM JIM / ● SMASH WINDOW** in condensed caps, eagle/flag mural and a tow truck behind | "sure you can smash the window, 2013, they haven't removed that, but" |
| 12 | 2:01.40 – 2:05.20 | 3.8 s | GTA 6 — chase-cam behind a red convertible on a suburban street | "old beater, slim jim, random Toyota on the street, fine, reasonable, high-end" |
| 13 | **2:11.60 – 2:18.20** | 6.6 s | **TEXT POSTER** — the Rob Nelson quote. Bg cut at 2:17.60. | "without the key cloner you can smash the window… some vehicles simply cannot be hot wired" |
| 14 | **2:29.00 – 2:34.80** | 5.8 s | **CARD** — neon quote card, KEY CLONER | "you can't just buy a key cloner from day one, these tools unlock by doing jobs for guys called fences" |
| 15 | 2:48.00 – 2:51.60 | 3.6 s | GTA 6 — dark grey coupé parked kerbside, bus passing | "because a lot of cars, especially the high-end cars, will have trackers and" |
| 16 | 2:58.40 – 3:01.00 | 2.6 s | GTA 6 — a man in a tan jacket and a woman at the open back of a van, a bag being handed over (a fence) | "have to unlock by doing even more work for them" |
| 17 | 3:07.40 – 3:10.40 | 3.0 s | GTA 6 — pawn-shop strip ("GADGETS", "WE DO REPAIRS", "JOYERIA EMPEÑOS"), a woman in a yellow dress walking past a red car. Hard **×2.57 step-in at 3:09.00** mid-shot. | "was playing it live in front of a creator, stole a car he liked and" |
| 18 | **3:23.60 – 3:30.35** | 6.75 s | **CARD 1** — IT STAYS QUIET / BEEPING | "top tier tracker in your car you just stole, while you're driving fast it stays quiet, the moment you slow down it starts beeping" |
| 19 | **3:30.35 – 3:35.25** | 4.9 s | **CARD 2** — TOO LONG IT PINGS THE POLICE | "and if you stay slow too long it pings the police to your exact location" |
| 20 | **3:35.25 – 3:38.45** | 3.2 s | **CARD 3** — THE STOLEN CAR REPORTS YOU TO THE COPS | "the stolen car reports you to the cops for driving responsibly" |
| 21 | **3:38.45 – 3:46.40** | 7.95 s | **CARD 4** — TO KEEP SPEEDING | "you are legally required by the car to keep speeding, this is the only vehicle in history that punishes you for obeying the speed limit" |
| 22 | **4:22.40 – 4:29.00** | 6.6 s | **CARD** — LOW ON GAS? Bg cuts at 4:25.40 and 4:26.80. | "steal a random car mid police chase and it's low on gas, that's your problem now, you gambled on a stranger's fuel tank" |
| 23 | **4:37.60 – 4:48.20** | 10.6 s | **CARD** — YOU CANNOT JUST WALK IN AND LIFT. Bg cut at 4:45.60. Longest single card. | "the gyms, you walk up to the front desk, buy a membership, you cannot just walk in and lift, the most wanted criminals in Leonida and they're getting the tour" |
| 24 | 4:49.60 – 4:52.80 | 3.2 s | GTA 6 — a pale primer-coloured muscle car inside a dark workshop | "shop does everything anymore, different shops, different specialties" |
| 25 | **4:59.80 – 5:06.80** | 7.0 s | **CARD** — PROPERTY'S ARE TOO TRACEABLE / GARAGES AND PARKING | "Jason and Lucia are fugitives. Properties are too traceable. The one thing you're allowed to purchase and own are garages and parking." |
| 26 | **5:18.20 – 5:22.00** | 3.8 s | **CARD** — A CRIMINAL / THINK like one | "I think you feel a lot more like a criminal and you have to think like one" |
| 27 | 5:39.20 – 5:40.40 | 1.2 s | GTA V — Franklin shouldering a rifle at an industrial site | "and that's very true, GTA" |
| 28 | 5:40.40 – 5:43.20 | 2.8 s | GTA V — white supercar on a wet neon street at night | "5 had like, if you're viewing it from this context" |
| 29 | 5:43.20 – 5:46.40 | 3.2 s | GTA V — a character shooting hoops under a stilt house | "the amount of things that we have in GTA 6, GTA 5 doesn't have any of this" |
| 30 | 5:56.40 – 6:00.20 | 3.8 s | GTA V Online — the heist planning board, SWAT models round a table with the Los Santos map on it. Heavily slowed (≈0.11×). | *(transcript has no words 5:52.5–6:09.9, though he is visibly still talking — WhisperX dropped this stretch)* |
| 31 | 6:09.80 – 6:13.60 | 3.8 s | **STILL / SCREENSHOT** — a real **YouTube channel page for "TGG"** (verified tick, @TGG_, 2.2M subscribers, 1.1K videos, bio "I like to have fun in GTA Online & Grand Theft Auto 5. GTA 6 News", Subscribe / Community / View channel stats buttons). Dark YouTube UI panel centred on solid black, no crop-in on the browser chrome. Near-frozen with a very slow push. | "One of the creators, Rockstar, flew out to Scotland, watched Rob Nelson play this game for" |

Plus the two **subscribe bug** animations (2:34.5–2:43.2 and 5:40.5–5:48.8) described in §1.

### 3b. The two plain-text posters

Both are **white type straight on top of heavily gaussian-blurred game footage** — no panel, no box,
no background plate of their own.

**#10 — "STEP 1: YOU CHECK AN APP" · 1:21.80 – 1:23.80 (2.0 s)**

- **Copy (exact, one line):** `STEP 1: YOU CHECK AN APP`
- **Layout:** single line, **horizontally centred, sitting on the vertical centre line** of the frame.
- **Colours:** pure white type; thin black outline plus a soft drop shadow so it holds over a bright
  background. Background: GTA V alley footage blurred to mush — you can still read a car, the wanted
  stars top-right and a pink minimap bottom-left through the blur.
- **Typeface class:** heavy **condensed grotesque, all caps**, very tight letter fit, flat terminals.
  Looks like Anton / a United Sans Heavy Condensed.
- No icon, no rule, no number badge.
- **Enters:** hard cut (first frame is full size and full opacity). **Exits:** hard cut back to face.
- **Motion while held:** the whole plate (type + blurred footage) slowly scales up together.

**#13 — the Rob Nelson pull-quote · 2:11.60 – 2:18.20 (6.6 s)**

- **Copy (exact, line breaks as `/`):**
  `"WITHOUT THE KEY CLONER YOU CAN SMASH THE WINDOW / YOU CAN SIT IN THE CAR AND IT WILL NOT START. / SOME VEHICLES SIMPLY CANNOT BE HOTWIRED"`
  (curly double quotes open and close; the second line ends in a full stop, the first does not.)
- **Layout:** three lines, **centre-aligned**, block centred horizontally, its optical centre a touch
  **above** the frame's vertical centre.
- **Colours:** pure white, black outline + drop shadow. No accent colour — this is the only text
  event with **no pink in it at all**.
- **Typeface class:** the same heavy condensed all-caps grotesque as the STEP 1 card.
- **Enters/exits:** hard cut both ends.
- **Motion:** the type creeps up in scale across the hold (measurably bigger at 2:17.9 than at
  2:11.8), and **the footage behind it hard-cuts at 2:17.60 to a completely different blurred scene
  while the text does not move** — the quote is one sustained layer over a cutting plate.

### 3c. The nine designed cards

All nine share the same construction, which is the video's strongest graphic rule:

> A **16:9 inset card with a soft drop shadow**, sitting at a **slight tilt (≈1–3°)**, floating over a
> **heavily blurred plate of game footage**. It **hard-cuts in at full size and hard-cuts out** — no
> fade, no wipe, no slide, ever — and **grows roughly 10–15 % across its hold** (a slow push on the
> card itself). Card art is illustrated/AI-rendered Vice-City neon, never a game screenshot.

---

**#14 · 2:29.00 – 2:34.80 (5.8 s) — "KEY CLONER" neon quote card**

- **Copy:** `"" / You can't just buy a / KEY CLONER from day 1, / these tools are unlocked / by doing jobs for guys / called "fences"`
- **Layout:** the card fills about 72 % of frame width; **inside it a rounded rectangle outlined in a
  glowing pink neon tube**, and inside that the text block, **centre-aligned**, vertically centred.
  A large pink **double-quote glyph sits top-left**, outside the text block, hanging into the corner.
- **Colours:** card background is a Vice City sunset illustration — **electric blue sky `#1035A3` at
  the top grading down to magenta/violet `#571F58`**, palm silhouettes at the corners, a skyline and
  its reflection on water at the bottom. Text **cream-white `#F9F3DF`**. Accent **hot pink `#E7278D`**
  carried by exactly two things: **"KEY CLONER"** and **"fences"** (plus the quote glyph and the
  neon frame).
- **Typeface class:** a **rounded geometric sans, sentence case, semibold** — the *only* card in the
  video that isn't condensed caps. Looks like Poppins / Montserrat SemiBold.
- **Icon/image:** the quote glyph; the palms and skyline are part of the background plate.
- **In/out:** hard cut both ends (verified at 1/10 s: 148.8 = face, 148.9 = full card; 154.7 = full
  card, 154.8 = face).
- **Motion:** grows ~12 % across the 5.8 s.

---

**#18 · 3:23.60 – 3:30.35 (6.75 s) — "IT STAYS QUIET / BEEPING"**

- **Copy:** `TOP TIER TRACKER IN YOUR CAR / WHILE YOU'RE DRIVING FAST` → `IT STAYS QUIET` … `THE MOMENT YOU SLOW DOWN IT STARTS` → `BEEPING`
- **Layout:** a **diagonal split** runs top-right to bottom-left across the card. The "quiet" copy is
  **top-left, left-aligned**; the "beeping" copy is **bottom-right, left-aligned but pushed right**,
  with "BEEPING" set enormous and breaking almost the full card width.
- **Colours:** night Vice-City boulevard illustration, deep navy `#171327` ground, warm street-lamp
  amber, a black coupé centre with red tail-lights. Cream-white type. Accent **hot pink** on
  **"YOU SLOW DOWN"** only. "BEEPING" is cream with a **magenta glow** and a **ghost/echo duplicate of
  the word sitting under it**, offset down and clipped by the card edge — a deliberate "ringing" artefact.
- **Typeface class:** condensed grotesque caps throughout; the kickers set small and letterspaced,
  the payoff words set huge.
- **Icons:** a grey **tracker fob** rendered twice — once beside "IT STAYS QUIET" (inert), once on
  the right **ringed by concentric pink sonar arcs** (transmitting). The two fobs are the argument.

**#19 · 3:30.35 – 3:35.25 (4.9 s) — "TOO LONG / IT PINGS THE POLICE"**

- **Copy:** `AND IF YOU STAY SLOW / TOO LONG / IT PINGS THE POLICE / TO YOUR EXACT LOCATION`
- **Layout:** headline block **top-left, left-aligned**; the kicker `TO YOUR EXACT LOCATION`
  **bottom-right, right-aligned**. Mixed sizes inside one line — "IT" tiny, "PINGS" huge, "THE" tiny,
  "POLICE" medium, so the line reads as a ransom-note rhythm.
- **Colours:** magenta/violet night street with palms and Art-Deco facades, a big **pink concentric
  ping ring** rising from the road in the centre. Cream type. Accent **hot pink** on **"EXACT"** only.
- **Typeface:** condensed grotesque caps.
- This card carries the most visible **tilt** of the nine — a clear couple of degrees.

**#20 · 3:35.25 – 3:38.45 (3.2 s) — "THE STOLEN CAR REPORTS YOU"**

- **Copy:** `THE STOLEN CAR / REPORTS YOU TO THE COPS / FOR DRIVING / RESPONSIBLY`
- **Layout:** the whole block **top-left, left-aligned**, occupying the left 45 % of the card.
- **Colours:** wet night street, deep navy, a magenta-lit sedan with headlights on at the bottom
  right. Cream type. Accent **hot pink** on **"REPORTS YOU"**.
- **Icons:** a small pink **broadcast/wifi glyph top-right** with a dotted line running down to a
  street pole — the car "calling out". A **Rockstar R★ logo bottom-right** of the card.
- Shortest of the four, and the punchline word "RESPONSIBLY" is the last line.

**#21 · 3:38.45 – 3:46.40 (7.95 s) — "TO KEEP SPEEDING"**

- **Copy:** `YOU ARE LEGALLY REQUIRED BY THE CAR / TO KEEP SPEEDING / THIS IS THE ONLY VEHICLE IN HISTORY / THAT PUNISHES YOU / FOR / OBEYING THE SPEED LIMIT`
- **Layout:** four stacked left-aligned blocks down the left half, alternating tiny kicker / big
  payoff / tiny kicker / big payoff. The last line is inset behind a **thin pink corner-bracket frame**.
- **Colours:** dusk skyline, pink/orange sky, a magenta supercar receding at the right. Cream type,
  accent **hot pink** on **"THAT PUNISHES"**.
- **Icons:** a large **pink speedometer arc** behind "TO KEEP SPEEDING"; a small grey **SPEED LIMIT
  sign** graphic sitting in the last line, in place of a bullet.
- **Card-to-card transitions in this run are all hard cuts, one frame to the next** (verified at
  1/20 s at 210.35, 215.25 and 218.45). Each new card **resets to its smaller start size and grows
  again**, so the run reads as four separate slams, not one long graphic.

---

**#22 · 4:22.40 – 4:29.00 (6.6 s) — "LOW ON GAS?"**

- **Copy:** `STEAL A RANDOM CAR MID POLICE CHASE / AND IT'S… / LOW ON GAS? / THAT'S YOUR PROBLEM NOW / you gambled on a STRANGER'S FUEL TANK`
- **Layout:** everything **left-aligned, flush to a left margin**, stacked down the full height of the
  card. "LOW ON GAS?" is the largest thing on any card in the video.
- **Colours:** Vice City neon night street, purple/magenta ground `#2C1A4E` over near-black `#1F0E28`,
  cyan and pink neon bars at the left, wet reflections. Type **cream `#F6F1DC`**; accent **hot pink
  `#C92D87`** on **"PROBLEM NOW"** only.
- **Typeface classes:** *three* on one card — heavy condensed caps for "LOW ON GAS?" and "THAT'S
  YOUR PROBLEM NOW"; a **lighter condensed caps** for the top kicker; and an **italic serif** for
  `you gambled on a` (looks like Playfair Display Italic), which then hands back to condensed caps
  for "STRANGER'S FUEL TANK" mid-line.
- **Icon:** a **fuel gauge** at the right of the "LOW ON GAS?" line — white arc, `E` marked at both
  ends (a deliberate joke), red needle pinned to empty, small pink pump-nozzle glyph.
- **Motion:** grows ~12 % across the hold; the plate behind it **cuts twice** (4:25.40, 4:26.80) from
  a blue-grey blur to a blown-out orange sunset blur while the card does not move.

---

**#23 · 4:37.60 – 4:48.20 (10.6 s) — "YOU CANNOT JUST WALK IN AND LIFT"**

- **Copy (headline):** `YOU CANNOT / JUST WALK IN / AND LIFT`
- **Copy (body paragraph, verbatim including its errors):** `the gyms you walk up to the front desk buy a / membership you cannot just walk in and lift the / MOST WANTED CRIMINALS in leoonida are getting a tour / and they're SIGNING UP LIKE EVERYONE ELSE`
- **Copy (UI labels):** `01 FRONT DESK` · `02 BUY A MEMBERSHIP` · `GYM MEMBERSHIP`
- **Layout:** headline **left, left-aligned, upper-middle**; the body paragraph directly under it in
  small type; two grey **"membership card" rectangles** float on the right side, each with a small
  dumbbell glyph, connected by thin hairlines to labelled hotspots — an imitation UI walkthrough.
  Thin horizontal rules with tick marks run between the label points.
- **Colours:** a dim gym render — concrete, dark timber, an "OCEANVIEW ELITE FITNESS" reception desk
  with two figures at it, magenta LED strip on the far wall, a pink/purple sunset through glass doors
  at the left. Type cream; accent **hot pink** on **"AND LIFT"**, **"MOST WANTED CRIMINALS"** and
  **"SIGNING UP LIKE EVERYONE ELSE"**.
- **Typeface classes:** condensed caps headline; the body paragraph is a **plain default-looking
  grotesque** (looks like Arial/Helvetica) — visibly less designed than the rest of the card; small
  letterspaced caps for the UI labels.
- **Motion:** the biggest growth of any card — noticeably larger at 4:48 than 4:37.6 (≈15 %). Bg cuts
  at 4:45.60.

---

**#25 · 4:59.80 – 5:06.80 (7.0 s) — "PROPERTY'S ARE TOO TRACEABLE / GARAGES AND PARKING"**

- **Copy:** `JASON AND LUCIA ARE FUGITIVES` / `PROPERTY'S ARE / TOO TRACEA BLE` … `THE ONE THING YOU'RE / ALLOWED TO PURCHASE / AND OWN` / `GARAGES / AND PARKING`
  *(Both errors are on screen: "PROPERTY'S" for "properties", and "TRACEABLE" broken as `TRACEA BLE`
  with a space in the middle.)*
- **Layout:** a **hard diagonal split** from lower-left to upper-right. Left/upper block
  **left-aligned** with a thin rule under the kicker; right/lower block: tiny **right-aligned** kicker
  next to a big **left-aligned** payoff, pinned to the bottom-right corner.
- **Colours:** the left half is a desaturated **near-black architectural model** of villas and
  condos with faint blueprint linework; the right half is a **parking garage glowing hot orange and
  magenta** from inside. Near-black ground `#13131F`, cream type `#EAE9E1`. Accent **hot pink** on
  **"FUGITIVES"**, on **"TOO"** (which also carries a short pink underline), and on **"AND"** (also
  underlined pink).
- **Typeface:** condensed grotesque caps throughout, two weights.
- The dark/lit diagonal split *is* the argument — dead property on one side, the one thing you can
  own lit up on the other.

---

**#26 · 5:18.20 – 5:22.00 (3.8 s) — "A CRIMINAL / THINK like one"**

- **Copy:** `i think you feel alot more like` / `A CRIMINAL` / `and you have to` / `THINK` / `l i k e   o n e`
  *(lowercase "i", and "alot" as one word, both on screen.)*
- **Layout:** the whole text block **left-aligned on the left third** of the card, stacked
  small-big-small-huge-small. "like one" is heavily **letterspaced**. A thin vertical hairline runs
  down the left of the block, with small **crosshair/registration ticks** either side of "and you
  have to" — a subtle print-layout detail.
- **Colours:** an illustrated **noir detective desk** — near-black navy `#030619`, a warm desk lamp
  pooling amber light on a map covered in red string lines, a coffee cup, phone, keys, glasses,
  banknotes, a silhouetted figure's hand bottom-right, and a **window onto a pink/cyan Vice City
  skyline** top-right. Type cream `#F6F1DC`; **the big words carry a thin magenta/pink outline** and
  a dark drop shadow rather than a solid pink word — this is the one card where the accent is a
  *stroke*, not a fill.
- **Typeface classes:** condensed grotesque caps for "A CRIMINAL" and "THINK"; a **light serif** for
  the three small lines (looks like a transitional/slab serif — PT Serif or Roboto Slab Light).
- The only card whose headline is a lowercase sentence.

### 3d. What the cards have in common

- **Every card's headline is the sentence he is saying at that exact moment**, transcribed near
  verbatim. The poster is not a summary or a label — it's the audio, set in type.
- **Hard cut in, hard cut out, always.** Zero fades, dissolves, wipes or slides anywhere in the video.
- **The plate behind every card is game footage blurred to abstraction.** Full-frame game inserts are
  always sharp with the HUD left in; card backdrops are always defocused. That contrast is what tells
  you which mode you're in.
- **One accent colour, one or two words.** Hot pink `#E7278D`/`#C92D87`, never more than two phrases
  per card, always on the punch word.
- **Cream, not white.** Card type is `#F6F1DC`–`#F9F3DF`. The two plain-text posters are the exception
  — those are pure white with a black outline.
- **The card grows; nothing else about it moves.** No parallax, no element animation, no text reveal.

---

## 4. Recurring patterns

**Cadence.** 78 hard cuts = **11.3 per minute**, median held shot **3.6 s**, longest **24.0 s**
(1:23.80 – 1:47.80, the "check an app" explanation). By minute: **15 · 7 · 12 · 8 · 15 · 14 · 7.9** —
front-loaded in the hook, spiking again around the gym/property run, and dropping off hard in the
closing minute.

**Poster rate.** 11 text events (2 plain-text posters + 9 designed cards) across 6:53 = **1.6 per
minute**. Counting them as runs (a card run of four counts once) it's **8 runs = 1.16/min**.
Typical designed-card hold **3.2 – 7.0 s (median ≈ 5.8 s)**; the outlier is the gym card at 10.6 s.
The two plain-text posters hold 2.0 s and 6.6 s.

**Overall share.** Face on screen **79 % of runtime in 18 runs** (median run 13.3 s); overlays
**21 %**, median 3.1 s.

**Which line gets what.**
- **A designed card** goes on a *quotable declarative punchline* — a numbered step's payoff, or a
  Rockstar quote. If the sentence would survive as a tweet, it gets a card.
- **Full-frame game footage** goes on a line describing an *action or a place* — "you break the
  window", "the gyms", "mod shops", "different specialties". Something showable.
- **Nothing at all** — face only — gets the argument, the asides and the opinion. Two long graphic-free
  stretches prove it: **3:46.40 – 4:22.40 (36 s, five face shots, zero graphics)** while he sets up
  the registration fee, and **6:13.60 – 6:53.07 (39.5 s)**, the entire close.

**Inset vs full frame.** Game footage is **always full-frame and always sharp**, with the game's own
HUD left untouched (GTA V minimap and street names, GTA 6's PlayStation button prompts). The only
inset picture in the video is the **designed card** itself. The only pillarboxed insert is the
**Spider-Man meme clip at 0:02.00**, and it is punched to full width 1.4 s later.

**Motion on stills.** There are effectively no static frames. Three devices, applied everywhere:
1. **Gradual push on every face shot** — median +9.5 % per shot, 1.79 %/s.
2. **Cut zooms** — 143 in / 134 out, median step ×1.3, median hold 0.4 s, applied to the face *and*
   to game footage (×2.57 at 3:09.00).
3. **Card push** — every card grows 10–15 % over its hold.
Two inserts are near-frozen on purpose: the **Rob Nelson interview clip (0:36.60, ≈0.03×)** and the
**TGG channel screenshot (6:09.80, ≈0.07×)** — both drift slowly instead of sitting dead.

**Speed ramps on B-roll.** Game footage is routinely slowed: the 9.2 s GTA V theft take runs at
≈0.2×, the night-drive insert at ≈0.15×, the heist-board insert at ≈0.11×. Most short GTA 6 inserts
sit at ≈0.5× of a 60 fps timeline, i.e. they play at half speed or are 30 fps sources conformed up.

**Transition device.** There is exactly one: **the hard cut.** No dissolves, no wipes, no whip pans,
no zoom transitions, no flash frames, no glitch stingers, no sound-driven shake. Verified at 1/10 –
1/20 s on all eleven graphic boundaries and both ends of the card run.

**The last 30 seconds (6:23 – 6:53).** Pure talking head. Five face shots (cuts at 6:28.40, 6:33.00,
6:34.60, 6:50.60), each with its own push and several cut zooms. **No end card, no subscribe button,
no end-screen placeholder, no outro graphic, no logo, no music button, and nothing held clear on the
right or bottom for YouTube end-screen cards.** The video simply stops on his face mid-thought —
"we'll find out November 19 what people have to say" — and the last frame is a medium close-up.

---

## 5. Comedy and emphasis devices you can see

| t | device |
|---|---|
| **0:02.00** | **The Spider-Man meme insert.** 1.4 s of an unrelated live-action comedy clip dropped on "whether GTA 6 should have fuel or not", with black pillars still on it. No setup, no payoff, never referenced again. The second-shot punch-in at **0:03.40** (0.4 s, full width) is the button on it. |
| **0:36.60** | **Rob Nelson held as a reaction shot.** His interview clip is slowed to ≈0.03× — he's frozen mid-half-smile for 3.8 s while the narration promises the quote that closes the video. Reads as a smug freeze, not as B-roll. |
| **0:59.20 – 1:08.40** | **The theft take stretched to 0.2×** so the "wiggle wiggle hot wire thing" plays out in comic slow motion over a description that keeps saying how *fast* it used to be. |
| **1:08.40** | Hard cut in on **both hands already raised mid-gesture** — the cut lands inside the movement, not before it. This happens constantly (0:19.40, 4:29.00, 5:52.60 are the clearest). |
| **2:00.20** | **Extreme close-up on "they WILL come."** Face fills the frame top to bottom, index finger raised into the shot. The framing *is* the emphasis. |
| **3:09.00** | **×2.57 hard step-in on game footage** mid-shot on "stole a car he liked" — the biggest single scale jump in the video, and it's thrown at a walking-past-a-pawn-shop plate, which makes it funnier. |
| **3:23.60 – 3:46.40** | **Four escalating punchline cards fired back to back**, each a hard cut, each resetting to a smaller size and growing again — a 23-second slide deck of jokes, ending on "FOR OBEYING THE SPEED LIMIT" with a tiny SPEED LIMIT sign as the bullet. |
| **4:07.40** | Extreme close-up, face pushed left, finger jabbing at the lens on "not anymore." |
| **4:55.20** | **The best reaction cut in the video.** On "Rob Nelson literally compared it to hair salons — *what the*—", the frame snaps to an extreme close-up with his head shoved into the **right third**, looking out of frame left, mouth open. Composition breaks on purpose. |
| **5:57.00** | ×2.21 hard step-in on the heist-board footage. |
| **6:04.80 – 6:08.00** | **A zoom burst:** six crop levels in four seconds inside one continuous take (steps at 6:04.80, 6:05.00, 6:05.60, 6:06.00, 6:06.80, 6:07.20, 6:08.00), several held only 0.2 s. The audio never cuts. |
| **6:09.80** | **The screenshot as a callback punchline** — the actual TGG channel page shown instead of naming the creator, held near-frozen for 3.8 s. |
| throughout | **On-screen typos left in** — "PROPERTY'S ARE TOO TRACEA BLE", "alot", "in leoonida". Not gags, but they're part of the texture and they ship. |
| — | **No freeze frames on the face.** Checked the high-duplicate candidates at 1:34, 1:39, 2:40, 5:36 and 6:36 at 15–20 fps: he is still moving and speaking in all of them. The near-freezes in this video are on inserted footage only. |

---

## 6. Palette and type summary

### Palette

| swatch | hex | where it lives |
|---|---|---|
| Hot pink / magenta | **`#E7278D`** (also `#C92D87`) | the single accent — one or two words per card, the neon frame, underlines, sonar rings, the speedometer arc |
| Cream off-white | **`#F6F1DC`** / `#F9F3DF` | all card type. Warm, never pure white |
| Pure white | **`#FFFFFF`** | the two plain-text posters only, with a black outline |
| Near-black plum | **`#1F0E28`** / `#171327` | the dominant card ground on the night cards |
| Near-black navy | **`#13131F`** / `#030619` | the ground on the property and "THINK" cards |
| Mid violet | **`#2C1A4E`** / `#212750` | card mid-tones, wet street reflections |
| Electric blue | **`#1035A3`** | the Vice City sky on the KEY CLONER card |
| Magenta-purple glow | **`#571F58`** / `#512650` | neon bloom inside the card art |
| Set lavender | **`#D299F4`** | the lit back wall of the room — the face shot's signature colour |
| Leather brown | **`#512B23`** | the armchair behind him |
| Mic red | **`#7A1219`**-ish | the mic grille, the one warm object in the room |

The whole thing is a two-colour system: **hot pink on near-black, cream for the words.** Blue and
violet only ever appear as *illustration*, never as type colour.

### Type classes

1. **Heavy condensed grotesque, all caps** — the workhorse. "STEP 1: YOU CHECK AN APP", the Rob
   Nelson quote, "LOW ON GAS?", "BEEPING", "IT STAYS QUIET", "YOU CANNOT JUST WALK IN", "GARAGES AND
   PARKING", "TO KEEP SPEEDING", "A CRIMINAL", "THINK". Looks like **Anton** or a United Sans /
   League Gothic-class heavy condensed.
2. **Lighter condensed caps, letterspaced, small** — the kickers above and below every payoff line
   ("TOP TIER TRACKER IN YOUR CAR", "THIS IS THE ONLY VEHICLE IN HISTORY", "THE ONE THING YOU'RE
   ALLOWED TO PURCHASE AND OWN"). Looks like **Oswald** / a condensed grotesque at light weight.
3. **Rounded geometric sans, sentence case, semibold** — the KEY CLONER card only. Looks like
   **Poppins** or Montserrat SemiBold.
4. **Italic serif** — `you gambled on a` (LOW ON GAS card). Looks like **Playfair Display Italic**.
5. **Light serif, roman** — `i think you feel alot more like`, `and you have to`, `l i k e  o n e`
   (THINK card). Looks like a transitional/slab serif — **PT Serif** or Roboto Slab Light.
6. **Small letterspaced caps, plain grotesque** — UI-style labels on the gym card (`01 FRONT DESK`,
   `GYM MEMBERSHIP`).
7. **Plain default sans** — the gym card's body paragraph. Looks like **Arial/Helvetica**, and it
   reads as the one un-art-directed element in the video.

Treatments: card type is **cream with a dark drop shadow**; on the THINK card the two big words also
carry a **thin magenta outline**. The two plain-text posters are **white with a black outline plus a
drop shadow** so they survive a bright blurred plate. "BEEPING" gets a **magenta glow and a ghosted
echo duplicate**. No text animation, no reveal, no kinetic type anywhere — type is typeset, cut in,
and pushed.
