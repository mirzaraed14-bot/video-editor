# Visual catalogue — "The GTA 6 Leaker's Real Mistake Wasn't The Leak"

Affan Afterhours, uploaded 2026-08-29 (the channel's second long-form, one day after PS5 Pro), ~8k views at audit.
Master read: `raw/leaker.mp4` — the YouTube 1080p download, 1920×1080, **59.94 fps**, **4:31.00** (271.0 s).

Evidence: all 19 contact sheets (`frames/sheet_001–019.jpg`, 2 fps), full-res stills in `frames/full/` (39 frames,
named by second), 20-fps transition strips `frames/step_*.jpg` (cold open, every chapter-card entrance, the whips, the
glitch mascot, the ending). Numbers: a scratch run of the facecam preset's own `style-probe.py` (YuNet face boxes at 5/s)
and `slowmo-scan.py` on this file, an ffmpeg scene-change pass (threshold 0.15), and a word-timed scratch transcript
(faster-whisper medium.en) for what is said at each event. The background `probe/` + `transcript/words.json` had not
landed when this was written; when they do, they supersede the scratch numbers. Anything marked **"looks like"** is an
inference. Timecodes are ±0.1 s. Quotes are the scratch transcript with its obvious mishears fixed ("Cyber League" →
CyberLeek, "paid secret" → trade secret, "key deals" → plea deals, "savior" → serious).

**One-line read:** this is the channel's most *documentary* edit — a scripted, chaptered legal explainer told almost
entirely through **screenshots and clips floating on a pure-white page with a drop shadow**, separated by full-frame
**ACT / CHARGE chapter cards** that slide in with motion blur. There is **no game footage**, no designed quote card, no
meme, and the face barely zooms. Nothing in it matches the facecam README's look; it is a different overlay language.

---

## 1. The face shot

### Framing (YuNet, 837 face samples outside overlays)

| | face-box height (fraction of 1080) | |
|---|---|---|
| p10 | 0.294 | the base is a little WIDER than PS5 Pro / NPC AI (0.336) |
| **median** | **0.323** | |
| p90 | 0.364 | |
| max | 0.424 | the tightest the face ever gets ≈ **1.45× base** — no extreme close-up anywhere |

- **Face centre x = 0.593** — the face sits clearly **right of centre** (PS5 Pro 0.517, NPC AI 0.514). The chair fills
  the left half.
- **Face top y = 0.219** median and the camera is framed HIGH: the neon sign is cut by the top edge so only the
  bottom half of **SKOOL** shows (see `full/t_2.5.jpg`, `t_235.0.jpg`). Less headroom than the other two.
- **Gradual push: almost none** — median 1.8 % per held shot = **0.5 %/s** (PS5 Pro 1.9 %/s). Shots mostly sit still.
- **Cut zooms: few and small.** ~14 plausible zoom-ins over 171 s of face (≈ 5 per minute of face), median ×1.14
  (p25–p75 1.10–1.17), max ×1.5, held a long ~1.9 s. They read as gentle reframes, never as hits. Where they are:
  0:17.5, 1:10.5, 1:35, 2:20, 2:25 (lean-in), 2:38.5 (hands at temples), 2:49.5, 3:00.5, 3:06.5 (hand on chin),
  3:44.5, 4:20.5, 4:28.5.
- **Jump cuts** are the main face rhythm: face runs median 4.8 s, longest 17 s (1:25.5–1:39.8 area; see § 4).
- He looks **off-camera right** (at the monitor, reading) for long stretches: 0:40.5–0:43.5, 0:57–1:04.5, 1:25.5–1:29.5,
  1:49.5, 2:06–2:09, 4:00–4:02.5. The read is visible and left in.

### The set (same room as PS5 Pro, shot at night)

- Wall: grey-lavender `#9691A8` in the light, **teal/blue** lower down, a pink-lavender wash top-left (`#737683` at
  the top edge). The same `skool` neon, the same small pink framed print, black window grille at frame-left edge,
  brown leather armchair, dark monitor at frame-right with a warm lit edge.
- **Lighting is the identifying difference: a warm orange key low from camera-left, deep shadow on the right cheek,
  a dark room.** It looks like an evening shoot with the practicals doing the work. Face frames are dark; the video's
  mean luma 0.316 is only that high because the white-page insets are 29 % "bright" frames.
- Wardrobe: plain **black crew-neck T-shirt**, silver watch on the left wrist + a dark bead bracelet, no glasses.
- Mic: the **red-bodied mic with a black grille top on a desk stand**, lower centre (looks like a HyperX QuadCast-type
  USB mic) — the same mic as PS5 Pro.

### Bugs / lower-thirds / captions / subscribe

None. No captions, no logo, no lower-third, no name strap, **no subscribe animation** anywhere in 4:31 (checked on
every sheet).

---

## 2. Cold open (0:00 – 0:35)

| # | in – out | on screen | said |
|---|---|---|---|
| 1 | 0:00.0 – 0:02.1 | **Illustration, full frame, static:** the CyberLeek mascot (a leek with sunglasses in a blue sci-fi armour suit) standing in front of a pastel vaporwave Vice City skyline (teal sky `#347E97`, pink towers, a helicopter top-left). No text. Looks AI-generated, same art as the chapter cards. | "This guy thinks he's a folk hero," |
| 2 | 0:02.1 – 0:04.2 | Face, base, hand over mouth then open (a ~0.1 s cross-dissolve from the illustration — both visible at 0:02.0) | "manifesto, crypto coin," |
| 3 | 0:04.2 – 0:08.5 | **Inset on WHITE**: a vertical phone video of a curly-haired guy with glasses biting a raw leek outside the ROCKSTAR NORTH building. Inset 920 px wide (48 %), full height, centred slightly right, drop shadow down-right. Hard cut in. | "people biting vegetables outside Rockstar's office because he told them to." |
| 4 | 0:08.5 – 0:12.2 | Face | "Here's what he is actually facing based on federal law." |
| 5 | 0:12.2 – 0:12.5 | **Whip:** the face shot smears sideways (directional blur, ~0.15 s), the next inset arrives smeared and settles (`step_0012_whip.jpg`) | — |
| 6 | 0:12.5 – 0:15.6 | **Inset on WHITE**: a dark ChatGPT-style table "Charge \| Federal Statute \| Maximum Sentence" (Unauthorized computer access 18 U.S.C. § 1030, Theft of trade secrets § 1832, Extortion § 875, Wire fraud § 1343 up to 20 years, Conspiracy § 371). 74 % wide, shrinking slowly. | "Extortion, trade secret theft, possibly wire fraud," |
| 7 | 0:15.6 – 0:19.4 | Face (small zoom ~1.1 at 0:17.5) | "add it all up and you're looking at a theoretical ceiling well past 45 years." |
| 8 | 0:19.4 – 0:20.4 | Whip out of the face | — |
| 9 | 0:20.4 – 0:24.0 | **Found ad clip, full frame:** "Bleap" — a chrome 3D leek figure on black inside a frame of colourful 3D blobs, Bleap logo bottom-centre | "And there's a financial trail sitting in his own crypto token that…" |
| 10 | 0:24.0 – 0:33.2 | Face, 9 s, one gentle reframe | "…might be already pointing straight to his real identity. This is what's publicly reported and what federal law actually says. Let's go through all of it." |
| 11 | 0:33.2 – 0:35.3 | Black frame → **ACT 1 / The 60 Second Recap** chapter card slides in (§ 3b) | (silence) |

Read: the hook is a **spoken thesis + three literal illustrations** (the leek-eater, the charge table, the token ad).
First insert at 0:00, i.e. it opens on an overlay. 28 s of the first 60 s are overlay. It ends its cold open with a
formal "Let's go through all of it" and a chapter card — the register of a documentary, not of the facecam style.

---

## 3. Every overlay, in order

### 3a. Master table

Treatments: **W** = inset on the white page (pure `#FDFDFD` background, soft grey drop shadow to the lower right,
the inset slowly SHRINKS 3–6 % over its hold and drifts a few px), **CH** = full-frame chapter card, **FF** = full-frame.
Widths are the inset's measured box (fraction of 1920).

| # | in – out | dur | kind | what (verbatim text where there is any) | entrance | said over it |
|---|---|---|---|---|---|---|
| 1 | 0:00.0–0:02.1 | 2.1 | FF illustration | CyberLeek mascot, vaporwave skyline | opens | "This guy thinks he's a folk hero," |
| 2 | 0:04.2–0:08.5 | 4.3 | W video, 48 % | leek-biting fan outside Rockstar North (vertical phone clip) | hard cut | "people biting vegetables outside Rockstar's office…" |
| 3 | 0:12.4–0:15.6 | 3.2 | W screenshot, 74→72 % | dark AI table of federal charges/statutes/max sentences | whip | "Extortion, trade secret theft, possibly wire fraud," |
| 4 | 0:20.4–0:24.0 | 3.6 | FF ad clip | "Bleap" chrome-leek crypto ad | whip | "a financial trail sitting in his own crypto token" |
| 5 | 0:33.3–0:35.3 | 2.0 | CH | **ACT 1** / *The 60 Second Recap* | black + blur-slide | (pause) |
| 6 | 0:35.3–0:40.3 | 5.0 | W screenshot, 65→62 % | CyberLeek website (navy, mono font, "CYBERLEEK", "BUY BUILD", "242 / 1000") | hard cut | "August 16th, someone calling themselves CyberLeek starts posting GTA 6 gameplay clips." |
| 7 | 0:44.2–0:50.1 | 5.9 | W video, ~70 % | the leaked gameplay clip **deliberately blurred** to illegibility (a header "THIS VIDEO IS SPED UP, PLEASE WATCH AT…" just readable as a shape) | hard cut | "a clip of the in-game character shooting the word LEEK into a wall…" |
| 8 | 0:54.9–0:57.0 | 2.1 | CH | **CHARGE 1** / *Criminal Copyright Infringement* | blur-slide from left | "18 U.S.C. 2319…" |
| 9 | 1:14.0–1:18.0 | 4.0 | W screenshot, 41→39 % (tall) | X post, **GTA 6 France @GTA_6_France**: "One of the worst heists in video game history. Cyberleek is playing with fire and risking EVERYTHING: Computer hacking & data theft / Massive copyright violation / Attempted extortion on Rockstar Games … In the US, the combined tab can climb to more than 45 years in prison. As a reminder, the 2022 leaker ended up institutionalized for life…" + a GTA V "LEEK" wall image | hard cut | "9 counts, 5 years max. 9 times 5 is 45." |
| 10 | 1:23.4–1:25.4 | 2.0 | CH | **CHARGE 2** / *Civil Damages* | blur-slide | "If a court finds the infringement willful…" |
| 11 | 1:39.8–1:41.9 | 2.1 | CH | **CHARGE 3** / *Extortion* | blur-slide | "CyberLeek's manifesto is based on explicit demand." |
| 12 | 1:44.7–1:49.3 | 4.6 | W screenshot, tall | X post, **GTA 6 Hub**: "Here is an excerpt from the Cyberleek press release… The group presents its 3 'commandments' there: No digital pre-orders / No fake solo DLC / Preserve offline solo content. ⚠ These statements remain to be confirmed." + French document image | whip | "Meet these conditions or more gets leaked." |
| 13 | 1:54.0–1:56.0 | 2.0 | CH | **CHARGE 4** / *Trade Secret Theft* | blur-slide | (pause) → "An unreleased game isn't just copyrighted…" |
| 14 | 2:00.8–2:05.8 | 5.0 | W screenshot, 82→78 % | Google **AI Overview**: "CyberLeek has not been formally charged with trade secret theft or any other crime yet…" (first sentence highlighted in blue), "Legal Exposure and Charges", bullets *Potential Charges / Potential Offenses / Prison Time: …7 to 15 years in federal prison…* | hard cut | "Federal law carries up to 10 years plus fines of $250,000…" |
| 15 | 2:09.6–2:11.6 | 2.0 | CH | **CHARGE 5** / *Wire Fraud* | blur-slide | (pause) |
| 16 | 2:16.4–2:19.4 | 3.0 | W screenshot, 98→96 % | CoinGecko: "CyberLeek CYBERLEEK Price $0.01764 ▲1054.2% (1m)", market cap $12.864M, green spike chart, a yellow Rugcheck warning | hard cut | "a coordinated pump built on false promises to buyers," |
| 17 | 2:31.9–2:34.8 | 2.9 | FF stock photo | black-and-white handshake over a desk with a judge's gavel and papers, slow push | hard cut | "plea deals and concurrent vs consecutive time" |
| 18 | 2:41.1–2:46.5 | 5.4 | W screenshot, ~50 % | AI answer: "…the absolute theoretical maximum ceiling for Cyberleek sits well over 100 years in prison… The Statutory Ceiling Breakdown: Wire Fraud (Up to 20 years per count)… Computer Fraud and Abuse Act… Extortion… Aggravated Identity Theft" | hard cut | "You're looking at a ceiling which could realistically be over 60 to 70 years" (the screenshot says 100 — the line and the evidence disagree) |
| 19 | 2:50.9–2:53.0 | 2.1 | CH | **ACT 3** / *The Financial Trail to Catch CyberLeek* | blur-slide | "Now here's the part that might matter…" |
| 20 | 2:58.9–3:00.7 | 1.8 | W screenshot | article header "**Who is Cyberleek? What we know about the GTA 6 leaker**", red "Features" tag, "By Tyler Wilde, Published 21 August 2026", mascot in a blue ring (looks like PC Gamer) | hard cut | "…stay anonymous with 9 leaks?" |
| 21 | 3:03.3–3:06.3 | 3.0 | FF ad clip | Bleap again: chrome "**$25M**" with the chrome leek leaning on the M | whip | "The token CyberLeek hit a $25 million market cap" |
| 22 | 3:13.8–3:15.9 | 2.1 | CH | **ACT 4** / *Rockstar Legal Roadmap* | dip (face darkens) → card | "Now step by step…" |
| 23 | 3:19.2–3:21.6 | 2.4 | W stock photo | tilted macro of a browser error "This site can't be reached — www.wikipedia.org's server IP address… running Network Diagnostics… PROBE_FINISHED_NXDOMAIN", vignetted | whip | "Copyright takedown requests starting day 1." |
| 24 | 3:21.6–3:29.2 | 7.6 | W screenshot, 90→88 % | article "**Take-Two Interactive files subpoenas against Microsoft, Discord, and X amid ongoing GTA 6 leaks** / Firm is requesting 'any records related to various online accounts involved in posting and sharing leaks'" + GTA 6 still (Jason & Lucia with beers) | cut | "federal subpoenas against Discord and Microsoft filed August 20th…" |
| 25 | 3:39.1–3:42.4 | 3.3 | W screenshot, portrait | Instagram news post: mascot on top, green "NEWS" tag, condensed caps "A GTAFORUMS USER HAS TRACED THE CRYPTO WALLETS LINKED TO GTA VI LEAKER **CYBERLEEK** AND BELIEVES THE TRAIL COULD **LEAD TO THEIR REAL IDENTITY**" (accent words yellow-green) | hard cut | "…the KYC verified wallet. If the trace is actually accurate," |
| 26 | 3:49.7–3:52.3 | 2.6 | W screenshot | BBC article "**Lapsus$: GTA 6 hacker handed indefinite hospital order**", 21 December 2023, Joe Tidy; photo of a boy holding a shark, **face blurred** | hard cut | "…worked before with the previous hacker." |
| 27 | 3:52.3–3:54.3 | 2.0 | CH | **ACT 5** / *The Wildcard* | black + blur-slide | "Here's what could make every number in this video irrelevant." |
| 28 | 3:57.2–3:58.6 | 1.4 | FF animation | the mascot **walking**, on a blue CRT/scan-line "hacker terminal" background with code columns (looks like an AI-animated clip) | whip | "Where is this person?" |
| 29 | 4:02.9–4:07.4 | 4.5 | W screenshot, 93→88 % | article "**The India Connection to the GTA 6 Leak: How Rockstar's Bengaluru Footprint Became Part of a $2.8 Billion Market Shock**", green "CYBER CRIME / TRENDING" tags, GTA 6 key art (Lucia & Jason in bandanas) | hard cut | "…a rumored Rockstar India breach and Russian hackers…" |
| 30 | 4:13.8–4:16.1 | 2.3 | W photo, ~89 % | news photo: Putin at the long Kremlin desk with an official | whip | "Russia doesn't hand over its citizens for…" |
| 31 | 4:23.3–4:26.0 | 2.7 | W illustration | the mascot behind **jail-cell bars** (barred window, keyhole lock, cot) | whip | "…decades of theoretical exposure or" |

**31 overlay events (6.9/min), 28 runs (6.2/min), 37 % of runtime; median overlay 3.0 s; face 63 %.**
Counted by kind: 12 white-page screenshots, 2 white-page videos, 2 white-page photos, 1 white-page illustration,
**9 chapter cards**, 2 ad clips, 1 stock photo, 1 animation, 1 illustration. **Zero game-footage inserts**, zero
designed quote cards, zero memes.

### 3b. The chapter card (9 of them, one template)

- **Art:** the same full-frame illustration every time — the CyberLeek mascot on the right third, the pastel vaporwave
  Vice City skyline behind (teal sky, pink-white towers, a bridge, a helicopter top-left), with a **VHS/CRT texture**
  (visible scan-line grain and chromatic fringing on edges in the 20-fps strips).
- **Type:** left-aligned block, upper-left. Line 1 **"ACT 1" / "CHARGE 1"** in a very heavy condensed sans,
  **white**, cap height ≈ 170 px (~16 % of frame height) — looks like **Anton / Bebas Neue Bold**. Line 2 the title in
  the same family lighter/narrower, mixed case, white with a soft dark shadow ("The 60 Second Recap", "Criminal
  Copyright Infringement", "Civil Damages", "Extortion", "Trade Secret Theft", "Wire Fraud", "The Financial Trail to
  Catch CyberLeek", "Rockstar Legal Roadmap", "The Wildcard"). No accent colour, no number styling.
- **Entrance (measured, `step_0033_act1.jpg`, `step_0055_charge1.jpg`, `step_0352_act5.jpg`):** a cut to **black**
  (1 frame at 0:33.25 / 0:54.90 / 3:52.25), then the card **slides in from the left with heavy horizontal motion blur**,
  black still showing on the right, sharp after **~0.35 s**; the text lands a beat after the art. ACT 4 instead dips
  through a darkened face frame (3:13.5). **Exit: hard cut** to the face.
- **Hold ≈ 2.0 s**, and the narration **pauses or only starts a word** under it ("18…", "If…", "Now…").
- **The run:** ACT 1 → CHARGE 1–5 → ACT 3 → ACT 4 → ACT 5. **There is no ACT 2 card** — looks like the CHARGE cards
  stand in for it, or it was dropped.

### 3c. The white-page inset (the video's main overlay)

- Background **pure near-white** `#FDFDFD` (253,253,253) full frame; the screenshot/clip sits on it as a flat rectangle,
  **square corners**, **soft grey drop shadow offset down-right** (~20–30 px, large blur), no border, no tilt.
- **Size is whatever the source is**: 39 % wide (a tall tweet) to 98 % (the CoinGecko page); usually centred slightly
  right (box centre x ≈ 990–1040). Insets often run off the bottom edge.
- **Motion: a slow scale-DOWN**, measured 1416→1392 px over 2.4 s, 1256→1196 over 4.2 s, 1580→1492 over 4.2 s,
  1736→1688 over 6.6 s — i.e. **−3 to −6 % across the hold** (≈ −1 %/s), a pull-back, never a push.
- Entrance alternates between a **hard cut** and a **whip** (directional-blur smear out of the face, ~0.25 s:
  0:12.2, 0:19.4, 1:44.5, 3:03, 3:19, 3:57.2, 4:13.5, 4:23.0). Exits are hard cuts.
- Nothing is annotated: no arrows, no highlight boxes added by the edit (the blue highlight in the AI Overview is the
  browser's own text selection).

---

## 4. Recurring patterns

- **Say it, then show the document.** Almost every factual sentence gets its receipt: a tweet, an AI answer, an
  article header, a price chart. The overlay is evidence, not B-roll.
- **Chapter rhythm:** a chapter card every ~20–45 s through the middle (0:33, 0:55, 1:23, 1:40, 1:54, 2:10, 2:51, 3:14,
  3:52); between cards the pattern is face → white-page receipt → face.
- **Cut rate** ~18–19 visible changes/min, flat across the video (by minute 21/18/17/19/21) — the most even pacing of
  the three.
- **Face runs are short** (median 4.8 s); the longest stretch without an overlay is **0:57.0–1:14.0 (17 s)**, much of it
  read off the monitor, then 1:25.4–1:39.8 (14.4 s) and 2:19.4–2:31.9 (12.5 s).
- **Repeat assets:** the mascot illustration (cold open + 9 chapter cards + the jail + the glitch), the Bleap ad twice.
- **No game footage at all** in a GTA channel video — GTA 6 appears only inside other people's article images.

## 5. Comedy and emphasis devices

Few — this is the straightest-played video of the three.

| device | where | what |
|---|---|---|
| literal illustration as a gag | 0:04.2 | the leek-biting fan clip on "people biting vegetables" |
| the mascot as a character | 3:57.2, 4:23.3 | the leek walks on a hacker screen on "Where is this person?"; the leek behind bars on "decades… of exposure" |
| on-the-nose photo | 4:13.8 | Putin at his desk on "Russia doesn't hand over its citizens" |
| the gesture | 2:38.5 | hands at temples ("mind blown") under a ~1.25 reframe |

No slow-down is visible on the face (the frame-duplicate scan cannot see the creator's 0.8× speed anyway — 0.8× repeats
only 20 % of frames, under its 35 % threshold), no colour bars, no meme clip, no extreme close-up, no shake.

## 6. Palette and type

- Page white `#FDFDFD`; screenshots are dark-mode UIs (`#1E1E1E`–`#212429` panels, white text).
- Chapter art: teal `#347E97` sky, pastel pinks, the mascot's blue armour and green leaf; CRT grain.
- Type the edit itself sets: only the chapter cards — white heavy condensed caps (Anton/Bebas class) + a lighter
  condensed title line. **No accent colour, no pink, no Vice City gradient** — none of the facecam card system.
- Face frames: warm orange skin key against cool teal/lavender wall, deep shadows.

## 7. Ending (4:16 – 4:31)

4:16.1–4:23.0 face, a ~1.15 reframe at 4:20.5 ("…cyber crimes against Western companies. So the honest answer today,
this could end in a federal prosecution stacking") → 4:23.0 **whip** → 4:23.3–4:26.0 **jail-cell mascot** on white
("decades of theoretical exposure or") → 4:26.0–4:31.0 face, wider, then a jump-cut reframe tighter at 4:28.5
("or it could end in a fully verified name, sitting somewhere no subpoena can ever reach.") → **cold cut on the face,
mid-gesture**. No CTA, no "subscribe", no end card, nothing kept clear for end screens.

## 8. Differences vs README.md and CREATOR-HAND.md

| README / CREATOR-HAND says | Leaker does |
|---|---|
| Game footage is the main overlay, full-frame, sharp, HUD in | **No game footage at all**; the overlays are documents |
| "Nothing is ever an inset" (README); inset over a **colour matte** since 09-30 (CREATOR-HAND) | every document is an **inset on a pure-white page** with a drop shadow — an earlier, different inset look |
| Enters and exits on hard cuts, no transitions | **whips** (directional-blur smears) and **blur-slides from black** on every chapter card |
| Posters: designed 16:9 cards, Vice City art, pink accent, on a quote or a rule | **no posters**; text the edit sets is only the 9 ACT/CHARGE chapter cards (no such device in either doc) |
| Push ~1 %/s (110 preset); cut zooms 121–136 %, ~4–10/min, extremes to 200–350 % | push **0.5 %/s**; ~5 zoom-ins per minute of face at **~114 %**, max ~145 %, no extreme close-up |
| Bright LED room, no dark frames | a **dark, warm-keyed night shoot**; the face sits right of centre, neon cut by the top edge |
| Meme layer: colour bars, Vine boom, memes, cricket | none visible |
| Subscribe bug twice per video (README) | none |
| Ends cold on the face | ✔ same |
| Opens on the face (README) / voice from 0.000 (CREATOR-HAND) | opens on an illustration with the voice already running — matches CREATOR-HAND's looser rule |

**Earlier-era markers:** the night lighting and black tee, the QuadCast-type desk mic (later videos use a lav on a
prop), the white-page insets, chapter cards, whip transitions and the scripted documentary register ("Let's go through
all of it", "Here's where it gets serious") — none of which survive into the shipped Sept timelines CREATOR-HAND reads.
