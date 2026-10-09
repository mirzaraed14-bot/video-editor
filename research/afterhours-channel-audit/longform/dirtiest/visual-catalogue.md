# Visual catalogue — "Rockstar's DIRTIEST GTA 6 Moves Yet"

Frame-by-frame dissection of the editing style. Source: `raw/dirtiest.mp4` — YouTube download, 1920×1080,
59.94 fps H.264, 7:45.67 (465.67 s). Uploaded 2026-09-10, 13.6k views, 211 comments (channel V11 in
`X:\Claude Projects\GTA 6\results-log.md`; script `video11-update-compilation-SCRIPT.md`). Cut by: not recorded.

**Evidence** (all in `frames/`): 32 contact sheets at 2 fps (`sheet_001–032.jpg`, every one read);
~85 full-res stills + 9 labelled tiles in `frames/detail/` (`t_coldopen`, `t_cardsA/B/C`, `t_misc`, `t_bw`,
`t_glitches`, `t_stillzoom`); a WhisperX large-v3 word transcript made for this catalogue
(`frames/catalogue-words.json`, same model as the pipeline — the background job's `transcript/words.json`
had not landed when this was written); a face-crop scale track at 4 fps (`frames/catalogue-zoom.tsv`:
every frame matched against the base face frame at 0:24.0 by normalised cross-correlation over 1.0–3.4×);
an ffmpeg `scdet` cut list (129 visual changes after merging); a per-frame duplicate scan at native 59.94
(speed changes) and a bottom-left pixel scan for the subscribe bug. Timecodes are ±0.05 s unless a
boundary was stepped at 1/60 s. **"Looks like"** marks an inference.

---

## 1. The face shot

### Framing and set
- **One locked camera, one position, the whole video.** Medium close-up: head + shoulders, chest cut at
  the bottom edge. Base head height ≈ 36 % of frame height (0:23.6). Face centre x ≈ 0.50 (scan median
  0.50–0.53 across all face runs) — dead centre, generous headroom.
- **Back wall: LED green** `#5ABA75` (lit `#5AC480`), the same green room as RISKIEST, with a
  **lavender/magenta wash** spilling down the upper-left around a small **pink framed print**.
- **`skool` neon** at head height, upper right, mostly hidden behind his head in the base shot (only
  `ool` shows); it becomes the big readable shape in the tight shots.
- **Brown leather armchair** back `#4D1E0E` fills the left third; a **dark monitor bezel** cuts a diagonal
  down the right edge; a **small black stand/tripod** pokes into the bottom-right corner.
- No mic is visible. **Prop: a screwdriver** (black handle, orange band). He holds it like a stage mic
  (1:32–1:36, 2:23–2:30, 4:35), twirls it (1:59–2:03) and points it at the lens (6:26–6:31). He calls it
  out himself at 0:59.5: *"Don't ask me why I have a screwdriver."* (the RISKIEST spatula-mic gag, again).

### Wardrobe
- **Black sleeveless muscle tee** with a tonal print **"GOING ALL IN / EST.21"** and a small patch.
- **Dark smoky-lens glasses** (grey-green tint, dark frames) — not the amber Fuel System pair.
- Watch + bracelet on the left wrist, full beard. No wardrobe change.

### Zoom levels (measured, `catalogue-zoom.tsv`)
| level | crop scale vs base | where |
|---|---|---|
| base | 1.00 | the first frame of almost every face run |
| the push | drifts **1.00 → 1.08–1.13 across a run** (≈ 1–1.4 %/s); e.g. 0:23.5→0:31.2 1.00→1.10, 1:36.9→1:46.6 1.00→1.10, 4:23.5→4:35.7 1.00→1.19 | every run ≥ 4 s |
| cut zoom | **1.16 – 1.60, median ≈ 1.34**, held ≈ 1–2.5 s | ~30 in the video (≈ 3.9/min) |
| biggest | 1.56–1.60 | 2:16.75 (with a slow-down), 2:46.98, 6:24.32 (with a slow-down) |

- **About half the cut zooms ride a hard cut** (the new take arrives already tight: 0:31.18, 2:16.75,
  2:22.43, 2:40.54, 2:45.10, 2:46.98, 3:24.02, 3:28.61, 3:36.23, 3:40.25, 3:47.66, 4:12.69, 5:13.76,
  6:19.61, 6:24.32, 7:31.43); the other half **snap inside a held take** (0:04.9, 0:13.6, 0:51.3, 0:59.3,
  1:18.6, 1:35.9, 1:45.8, 1:52.9, 1:55.3, 2:29.0, 5:05.9, 5:19.9, 5:36.9, 6:13.8, 6:16.4, 7:38.9).
- After a cut zoom the picture returns to the push level, not to 1.00.
- **Two-rung ladders**: 1:52.9 1.08 → 1.28 → 1:55.3 1.41 ("for 25 years robbing a shop was just one
  button / now the corner shop has a plan"); 2:45.10 1.31 → 2:46.98 1.56 ("where does the money go? and
  they gave it four steps").
- **A/B alternation** 3:21–3:41 (the "man who's seen something" rant): 1.00 → 1.38 → 1.10 → 1.41 → 1.00 →
  1.34 → 1.00 → 1.45, a new size every 1.4–3 s on jump cuts.
- Face share **61 %** of runtime, **34 face runs**, median 7.3 s, longest 20.7 s (3:21.0–3:41.7 and the
  7:25.0–7:45.7 close).

### Bugs, lower-thirds, captions
- **No captions, no lower-third, no logo bug, no name strap, no chapter labels.**
- **Canned SUBSCRIBE animation ×5, bottom-left, 8.5–8.6 s each** (pixel-scanned):
  **1:35.2–1:43.8 · 2:38.6–2:47.2 · 4:23.6–4:32.2 · 5:58.1–6:06.6 · 7:12.0–7:20.5**. A white rounded
  bell tile pops in, a **red pill "SUBSCRIBE"** wipes out of it, a cursor clicks, the bell turns blue, the
  pill turns **white "SUBSCRIBED"**, then wipes back. Same asset as Fuel System. Never cued to a line
  ("How crazy is that? Meanwhile…", "until somebody washes it", "is going to produce a man…", "no nagging,
  no guilt", "now it does"); #4 runs over a title card (its tail sits on TELL HER at 6:06), #5 starts over
  game footage and ends on the face.

---

## 2. Cold open (0:00 – 0:59) — the promise stack

Voice starts at 0:00.2 on the face. 18 visual changes in minute 1. No title card, no logo sting.

| # | in – out | dur | on screen | treatment / speed | what's said |
|---|---|---|---|---|---|
| 1 | 0:00.00–0:05.12 | 5.1 | Face, base 1.00 pushing to 1.16 | — | "In GTA 6, the money you steal is worthless. Not low value, it's" |
| 2 | 0:05.12–0:06.14 | 1.0 | **Face snapped to 1.49–1.52**, mid-sentence, inside the same take | **0.8× slow-down** (every 5th frame doubled) | "**worthless.**" |
| 3 | 0:06.14–0:09.13 | 3.0 | **AI illustration**: Jason (white tank) scratching his head over an open duffel of cash on a motel bed, Vice City skyline sunset through the balcony | full frame, slow push | "You can't spend it, you can't put it in the bank." |
| 4 | 0:09.13–0:14.53 | 5.4 | Face 1.00 → push → cut zoom 1.34 at 0:13.6 | — | "And if you die holding it, it's gone. Like it was never yours. Legally it wasn't." |
| 5 | 0:14.53–0:17.15 | 2.6 | GTA 6: beach, yellow umbrellas, banner plane "WHY SIXTY NINE WHEN YOU CAN NINE 1 NINE" | full frame, 1× | "The least strange thing Rockstar told the YouTubers," |
| 6 | 0:17.15–0:17.63 | 0.5 | Game footage with an activity HUD "TARGETS REMAINING 8/12" (looks like a GTA 6 Extended Look shooting challenge) | full frame | "they flew to" |
| 7 | 0:17.63–0:19.80 | 2.2 | **AI illustration**: a Rob-Nelson-like bearded host gesturing to six creators round a table, Scottish saltire, castle in the window, R★ props | full frame, slow push | "Scotland in July" |
| 8 | 0:19.80–0:20.65 | 0.85 | Same shooting challenge, "6/12" | full frame | "where Rob Nelson" |
| 9 | 0:20.65–0:23.51 | 2.9 | Dirt-bike race, HUD "LAP 1/2 · 11/12 · 00:16.92" + minimap | full frame | "played the game in front of them for two and a half hours." |
| 10 | 0:23.51–0:32.67 | 9.2 | Face; push 1.00→1.10; cut zoom 1.31–1.45 on a jump cut at 0:31.18 | — | "But one of them was Italian and his notes got translated this week. So there's a second wave and it's weirder. So here's what's in this video." |
| 11 | 0:32.67–0:33.82 | 1.2 | GTA 6 trailer: shotgun POV into a convenience store | full frame | "Why a corner shop" |
| 12 | 0:33.82–0:35.90 | 2.1 | Trailer: masked robber, camo legs kicking | full frame | "in Vice City has a plan for you." |
| 13 | 0:35.90–0:39.21 | 3.3 | **AI title image "THE QUESTION / ROB NELSON / WOULDN'T ANSWER."** (§3b-1) | full frame, slow push | "The one question Rob Nelson refused to answer on purpose." |
| 14 | 0:39.21–0:40.86 | 1.7 | Trailer: Lucia bench-pressing ("GAINZ" plates) | full frame | "The two numbers the game tracks" |
| 15 | 0:40.86–0:43.36 | 2.5 | Trailer: a man sprints down a dock and dives | full frame | "about your body that you will not enjoy." |
| 16 | 0:43.36–0:46.58 | 3.2 | Trailer: couple in an elevator (woman in a pink dress) | full frame | "And what happens when you lie to your girlfriend in the game?" |
| 17 | 0:46.58–1:00.84 | 14.3 | Face (jump cut 0:52.42), cut zooms 1.22 at 0:51.3 and 0:59.3, screwdriver raised like a mic from 0:52.5 | — | "Although, also in general, because it's very identical. Scarily identical. We start from you with the money and every section gets closer. By the end, it's inside your relationship. Don't ask me why I have a screwdriver. So the corner shop has a" |

The **stack previews four of the nine sections, each with its own picture**, and the third preview is the
section's title image itself (it returns at 2:48 as section 3's card). Section 1 opens at 1:00.8 on the
word "plan" with no re-setup — the claim-first seam fix the results log asked for.

---

## 3. Every overlay, in order

### 3a. Master table

Treatment key: **FF** = full-frame, sharp, HUD left in; **AI** = full-frame AI illustration (slow push
unless noted); **TITLE** = AI title image with headline (§3b); **POSTER** = plain white quote text on a
blurred moving game plate (§3c). Speed: game footage runs at **1×** everywhere — 30 fps sources on the
59.94 timeline (every other frame repeated); no slow-mo on any insert.

| # | in – out | dur | what | treatment | what's said |
|---|---|---|---|---|---|
| 1 | 0:06.14–0:09.13 | 3.0 | Jason over a duffel of cash, motel, VC sunset | AI | "You can't spend it, you can't put it in the bank." |
| 2 | 0:14.53–0:17.15 | 2.6 | Beach, banner plane | FF | "The least strange thing Rockstar told the YouTubers," |
| 3 | 0:17.15–0:17.63 | 0.5 | Shooting-challenge HUD 8/12 | FF | "they flew to" |
| 4 | 0:17.63–0:19.80 | 2.2 | Rob + six creators, Scotland | AI | "Scotland in July" |
| 5 | 0:19.80–0:20.65 | 0.85 | Shooting challenge 6/12 | FF | "where Rob Nelson" |
| 6 | 0:20.65–0:23.51 | 2.9 | Dirt-bike race HUD | FF | "played the game in front of them for two and a half hours." |
| 7 | 0:32.67–0:33.82 | 1.2 | Trailer shotgun POV, store | FF | "Why a corner shop" |
| 8 | 0:33.82–0:35.90 | 2.1 | Trailer masked robber | FF | "in Vice City has a plan for you." |
| 9 | 0:35.90–0:39.21 | 3.3 | **THE QUESTION ROB NELSON WOULDN'T ANSWER.** | TITLE | "The one question Rob Nelson refused to answer on purpose." |
| 10 | 0:39.21–0:40.86 | 1.7 | Lucia bench press | FF | "The two numbers the game tracks" |
| 11 | 0:40.86–0:43.36 | 2.5 | Dock dive | FF | "about your body that you will not enjoy." |
| 12 | 0:43.36–0:46.58 | 3.2 | Elevator couple | FF | "And what happens when you lie to your girlfriend in the game?" |
| 13 | 1:00.84–1:03.38 | 2.5 | **THE CORNER SHOP / HAS A PLAN....** — cashier with a pump shotgun | TITLE (text looks editor-typed, §3b-2) | "So the corner shop has a plan." |
| 14 | 1:07.07–1:09.45 | 2.4 | Jason + Lucia aim pistols at the cashier, wide | AI | "pointed a gun at the cashier." |
| 15 | 1:09.45–1:14.42 | 5.0 | Closer: Jason's pistol, cashier hands up, **comic speech bubble "WE HAVE A / SAFE IN THE / BACK ROOM!"** | AI (bubble baked in) | "The cashier panicked and blurted out that there's a safe in the back room." |
| 16 | 1:19.61–1:22.72 | 3.1 | Jason + Lucia stuffing cash into a black bag at the till | AI | "So now you've got a decision. Either you just take the register and run" |
| 17 | 1:22.72–1:26.15 | 3.4 | Back room: Jason reading a note, Lucia on the safe keypad, Leonida Mart boxes | AI | "or stay. Find a combination inside of the store." |
| 18 | 1:29.41–1:32.28 | 2.9 | The safe explodes, cash flying, both ducking | AI | "Or you can just get impatient and blow the safe" |
| — | 1:35.2–1:43.8 | 8.6 | SUBSCRIBE bug #1 | bottom-left | "How crazy is that? Meanwhile, TGG watched this himself…" |
| 19 | 1:46.57–1:50.89 | 4.3 | **Isometric cut-away map of "LEONIDA MART"**: pink tag **FRONT DOOR** with a pink dashed arrow in, green tag **BACK DOOR** with a green dashed route out, white label **SAFE**, logo top-left "LEONIDA MART / GOOD TIMES CLOSER THAN YOU THINK" | AI (labels baked in) | "so the store has a back door you should know where it is before you walk up front" |
| 20 | 1:56.47–1:59.00 | 2.5 | **YOUR / MONEY IS / DIRTY** — Jason with a cash stack | TITLE + **cut zoom ×1.3 at 1:57.57** | "number two your money is dirty" |
| 21 | 2:03.01–2:05.19 | 2.2 | GTA 6 Extended Look: liquor-store robbery (rapid motion; a flash burst 2:03.29–2:03.52 is in the source) | FF | "the italian creator came out of a robbery with" |
| 22 | 2:05.19–2:07.04 | 1.85 | A man hands a woman something at an open van (a fence) | FF | "big bag of cash and tried to treat" |
| 23 | 2:07.04–2:08.81 | 1.8 | The pair with duffels by a manhole | FF | "it like money but couldn't" |
| 24 | 2:11.93–2:16.75 | 4.8 | Gameplay: damaged grey sedan through palms, **4 wanted stars**, minimap flashing | FF | "they had to drive to a business that launders money before a single dollar could go in the bank" |
| 25 | 2:30.73–2:31.77 | 1.0 | Jason counting cash on a motel bed | AI | "Your wallet has a cap," |
| 26 | 2:31.77–2:36.74 | 5.0 | Jason + Lucia cuffed by Leonida Police, rain, helicopter, cash duffel on the ground, "QuickMart" | AI | "cash on you is just gonna disappear the moment you get arrested, duffel bag loot is worthless" |
| — | 2:38.6–2:47.2 | 8.6 | SUBSCRIBE bug #2 | bottom-left | "…until somebody washes it. Rockstar took the one thing…" |
| 27 | 2:48.03–2:51.44 | 3.4 | **THE QUESTION ROB NELSON WOULDN'T ANSWER.** again (tighter crop) | TITLE (reused) | "number three the question rob nelson wouldn't answer" |
| 28 | 2:53.76–3:00.81 | 7.1 | Leonida cop aiming a pistol at Jason (back to camera), pastel VC street | AI, slow push | "in gta 6 a cop will still warn you before he opens fire gun out he sees it and instead of shooting he tells you to drop it" |
| 29 | 3:06.20–3:10.99 | 4.8 | **"THE ITALIAN CREATOR" and "ROB NELSON"** (handwritten labels) at a Rockstar desk; creator's bubble **"WHAT HAPPENS AT / 6 STARS?"** over six stars, Rob's bubble **"…"**; Italian flag on the sleeve, poster "BIGGER WORLDS BOLDER STORIES" | AI (text baked in) | "the italian creator asked rob nelson directly what happens at six stars" |
| 30 | 3:12.51–≈3:17.8 | 5.3 | **“ESCAPING AT 6 STARS IS EXTREMELY DIFFICULT”** | POSTER, plate = blurred chase | "he said escaping at six is extremely difficult he used the word relentless" |
| 31 | ≈3:17.8–3:21.03 | 3.2 | **“I'M NOT GOING TO DESCRIBE WHAT SHOWS UP”** (plate cut 3:20.62) | POSTER | "and then he said deliberately that he wasn't going to describe what shows up" |
| 32 | 3:41.66–3:43.82 | 2.2 | **Neon "23" (pink) and "87" (teal)** over ghost "?" marks, Jason from behind facing VC | TITLE (no words), near-static | "number four the two numbers you know the" |
| 33 | 3:53.37–4:02.63 | 9.3 | GTA 6 trailer: getaway car interior — bearded man in the back, driver in a red bandana, masked passenger | FF | "the italian creator opened the stats menu and next to health stamina and focus there were two more body fat and sleep quality separate for jason and lucia" |
| 34 | 4:16.67–4:19.13 | 2.5 | Trailer: Jason outside a pink strip-mall market | FF | "on the face skip the gym it's on the body" |
| 35 | 4:19.13–4:22.03 | 2.9 | Trailer: porthole-window laundromat, a couple dancing/fighting | FF | "so the classic gta playthrough awake four days straight" |
| 36 | 4:22.03–4:23.46 | 1.4 | Trailer: masked man with a rifle, low angle out of a car boot (the curved black edge is the source shot) | FF | "eating nothing committing crimes" |
| — | 4:23.6–4:32.2 | 8.6 | SUBSCRIBE bug #3 | bottom-left | "is going to produce a man that finally looks like the person playing him" |
| 37 | 4:35.68–4:38.80 | 3.1 | **Red Dead Redemption 2 key art** (Arthur, revolver, red/yellow sun, logo) | found art, FF, slow push | "It's much faster and less demanding than Red Dead 2." |
| 38 | 4:38.80–4:42.03 | 3.2 | **SHE HAS A LIFE WITHOUT YOU** — Lucia kickboxing a heavy bag | TITLE | "Number 5. She has a life without you." |
| 39 | 4:46.44–4:50.47 | 4.0 | **“EACH CHARACTER HAS THEIR OWN ROUTINE / WHEN YOU'RE NOT CONTROLLING THEM”** (plate cut ≈4:47.5) | POSTER | "Rockstar told the press each character has their own routine when you're not controlling them." |
| 40 | 4:50.47–4:53.14 | 2.7 | **“WHILE YOU'RE Off PLAYING JASON”** | POSTER | "The example they give. While you're off playing Jason," |
| 41 | 4:53.14–4:58.70 | 5.6 | **“LUCIA GOES TO KICKBOXING TRAINING / SO THAT NEITHER CHARACTER FEELS / LIKE A SIDEKICK”** — plate = the kickboxing title image, blurred | POSTER | "Lucia goes to kickboxing training. Their words. so that neither character feels like a sidekick." |
| 42 | 5:06.36–5:09.33 | 3.0 | Laundromat clip again (reuse of #35) | FF | "to break someone's nose. That's why you see her fighting style" |
| 43 | 5:20.14–5:22.54 | 2.4 | **THE COUPLE ICON** — Jason and Lucia back to back, neon double-heart ring | TITLE | "number six the couple icon under your wanted stars" |
| 44 | 5:25.06–5:27.76 | 2.7 | Night drives, red convertible, wanted stars; **2–4-frame RGB-split/blur flash at 5:26.24–5:26.31** between two clips | FF | "it lights up when a witness reports the two of you" |
| 45 | 5:37.97–5:40.77 | 2.8 | **THE LAST THING THEY WANTED** — Lucia angry, Jason hands up | TITLE | "number seven the last thing they wanted" |
| 46 | 5:42.98–5:49.30 | 6.3 | Trailer: Lucia holding up two outfits / Jason at a bulb mirror (cut 5:46.30) | FF | "they said a nagging relationship was the last thing they wanted… lucia texting where are you every 10 minutes" |
| 47 | 5:52.37–5:54.99 | 2.6 | Jason alone on a strip-club sofa, whisky, dancer | AI | "strip club as jason alone fine" |
| 48 | 5:54.99–5:57.91 | 2.9 | Jason + Lucia laughing together in the club | AI | "together as a couple like in the trailer also fine" |
| — | 5:58.1–6:06.6 | 8.5 | SUBSCRIBE bug #4 (tail lands on #49) | bottom-left | "no nagging no guilt total freedom…" |
| 49 | 6:05.73–6:08.10 | 2.4 | **TELL HER / OR DON'T** — Jason's face lit by a phone | TITLE | "number eight tell her or don't" |
| 50 | 6:17.63–6:19.61 | 2.0 | Trailer: Jason + Lucia holding hands, button prompt "HOLD HANDS" | FF | "and if you hide it nothing happens great" |
| 51 | 6:26.24–6:31.40 | 5.2 | **His own face in BLACK & WHITE**, different crop (him left of centre, `skool` white), screwdriver at the lens; **vertical squash distortion 6:29.00–6:29.74** | face, B&W | (role-play voice) "But you hid this information from me. I knew you were hiding something. Piece of shit. I'm gonna go to bed fully clothed tonight." |
| 52 | 6:36.58–6:38.90 | 2.3 | **YOU CAN BREAK UP** — broken heart, Lucia walking away | TITLE | "Number nine, you can break up." |
| 53 | 6:38.90–6:45.07 | 6.2 | **“THEY'LL REMAIN PARTNERS IN CRIME / NO MATTER WHAT, ROMANTIC OR NOT”** (plate cut 6:40.0) | POSTER | "Back in August, Rob Nelson told IGN they'll remain partners in crime no matter what, romantic or not." |
| 54 | 6:45.07–6:48.31 | 3.2 | **“YOU WILL ALWAYS HAVE THE / BENEfIT OF WORKING TOGETHER / AND HAVING EACH OTHER'S BACKS”** | POSTER | "You will always have the benefit of working together and having each other's back." |
| 55 | 6:55.27–≈6:59.2 | 3.9 | **“THEY CAN STOP BEING A COUPLE / THEY KEEP DOING CRIMES TOGETHER / THE STORY CONTINUES”** (plate cut 6:57.53) | POSTER | "They can stop being a couple. They keep doing crimes together. The story continues." |
| 56 | ≈6:59.2–7:01.72 | 2.5 | **“BUT THE RELATIONSHIP / BECOMES....PROFESSIONAL”** | POSTER | "But the relationship becomes... professional" |
| 57 | 7:11.80–7:14.85 | 3.05 | Trailer: Lucia in a red bandana mid-robbery (cut 7:13.15) | FF | "things gta never looked at now it does" |
| — | 7:12.0–7:20.5 | 8.5 | SUBSCRIBE bug #5 | bottom-left | "now it does and here's what gets me rob nelson told ign…" |
| 58 | 7:21.81–7:25.00 | 3.2 | **“VERY SPECIfIC POLITICAL ISSUES / OR MEMES WILL DATE FAST”** | POSTER | "his exact words very specific political issues or memes will date fast" |

**Totals.** 57 overlay rows (≈ 60 clips counting the cuts inside rows 44, 46, 57) in **33 runs
(4.25 runs/min)**, overlay share **39 %**, run median 4.8 s, longest 13.9 s (0:32.7–0:46.6); row 51 is
the B&W face beat, not an overlay. By kind: **24 AI illustrations** (10 title images incl. the reuse + 14
story illustrations), **10 plain-text posters** in 5 runs, **≈ 25 game-footage clips** in 20 rows (GTA 6
trailers / Extended Look gameplay; nothing from GTA V or older), **1 found key art** (RDR2). Reuse: the
QUESTION title (0:35.9 → 2:48.0), the laundromat clip (4:19.1 → 5:06.4).

### 3b. The title images — the video is a numbered list and each item gets a picture

The script is a nine-rung ladder ("number two… number nine"). **Every rung's title is shown as a
full-frame AI illustration with the title in big type**, hard-cut in exactly on the spoken title, held
2.2–3.4 s (median 2.5), slow push, hard-cut out — the cards function as **chapter title cards**. They
look like AI-generated thumbnail-style art: GTA-loading-screen painting (Jason in a white tank, Lucia in
pink), Vice-City sunset palette, the type baked into the art and in several cases **cropped by the top
edge of the frame** (the art was made at another aspect and cut to 16:9). "Number one" is never said —
rung 1's title (THE CORNER SHOP) lands on the last words of the cold open; rung 3 re-uses the
cold-open teaser image.

1. **THE QUESTION / ROB NELSON / WOULDN'T ANSWER.** (0:35.90 and 2:48.03) — Rob-Nelson-like bearded
   man in a black V-neck, smug, hand on chin; an over-the-shoulder interviewer holds an **R★-branded mic**
   and a notepad *"GTA VI? / Release date? / New features? / Vice City? / Online?"*; Rockstar office, VI
   poster, shelf labels "VICE CITY / LEONIDA / A BRIGHTER TOMORROW". Headline top-left, left-aligned,
   three lines ≈ 45 % of the frame width: cream `#FAF3E4` / **hot pink `#EE37A3` "ROB NELSON"** (the
   largest line) / cream, dark outline + drop shadow, a **pink brush-swash underline**. The 2:48 reuse is
   cropped tighter (headline larger, Rob centred).
2. **THE CORNER SHOP / HAS A PLAN....** (1:00.84) — the cashier (mullet, palm-print shirt) drawing a pump
   shotgun from under the counter, CCTV monitor and convex mirror behind. Text right of centre
   (x 0.61–0.87, y ≈ 0.43–0.55), left-aligned, two short lines: white `#FFF7ED` / **red `#E80003`** —
   the exact red of the quote posters, so **this one looks editor-typed** over a text-free illustration.
3. **YOUR / MONEY IS / DIRTY** (1:56.47) — Jason in a motel holding a cash stack, beer, piles of cash,
   billboard "GOOD TIMES / DIRTY MONEY" outside. Stacked left: cream / cream / **pink `#E90C92` "DIRTY"**
   (largest); "YOUR" is cut by the top edge. **The only cut zoom on a card in the video: ×≈1.3 at 1:57.57**,
   into the text and Jason.
4. **23 · 87** (3:41.66) — no words: neon outline numerals, **pink `#E44FA4` "23"** and **teal `#94E6D8`
   "87"**, each over a huge faint "?", Jason from behind facing the skyline. Near-static (98 % duplicate
   frames).
5. **SHE HAS A LIFE WITHOUT YOU** (4:38.80) — Lucia kicking a heavy bag, ghosted Lucias jogging and
   drinking coffee. Headline across the full top width, cream condensed caps, partly behind the bag,
   clipped at the top.
6. **THE COUPLE ICON** (5:20.14) — Jason and Lucia back to back, arms crossed; centre **a neon ring with
   two overlapping hearts (pink + teal) and HUD-style connector lines**. Headline centred at the top,
   peach-cream `#FCE4CD`, letter-spaced, glowing.
7. **THE LAST THING THEY WANTED** (5:37.97) — bedroom row: Lucia mid-rant, Jason hands up. Headline full
   width at the top, clipped.
8. **TELL HER · OR DON'T** (6:05.73) — tight on Jason's worried face lit from below by a phone, purple
   room. Two small white condensed-caps phrases at eye level, one each side of the face (looks
   editor-typed). The SUBSCRIBED pill is still bottom-left for its first 0.9 s.
9. **YOU CAN BREAK UP** (6:36.58) — Lucia walking away, Jason reaching after her by a classic muscle car
   on a pastel deco street, **a broken pink heart** between them. Headline across the top, peach-cream.

**Story illustrations (same art style, no headline)** carry the anecdote beat by beat, 1.0–7.1 s each:
the cash duffel (0:06), the Scotland round table (0:17), the robbery (1:07, 1:09 with a **comic speech
bubble**: white bubble, black outline, black italic caps with **dark-red `#830007` "SAFE" and
"BACK ROOM!"**), the cash grab (1:19), the safe keypad (1:22), the explosion (1:29), the **isometric store
map with FRONT DOOR / BACK DOOR / SAFE labels** (1:46), counting cash (2:30), the arrest (2:31), the cop's
warning (2:53, 7.1 s — the longest), the Italian creator vs Rob with the "WHAT HAPPENS AT 6 STARS?"
bubble (3:06), the strip club alone (5:52) and together (5:54). **An unfilmable anecdote is told as a
storyboard of illustrations**, two to five panels per anecdote.

### 3c. The plain-text quote posters (10, in 5 runs)

Every poster is **a reported Rob Nelson / Rockstar quote, set verbatim in “curly quotes”** at the moment
it is read — never his own opinion.

- **Layout:** full frame; the text block centred horizontally and vertically (centre y ≈ 0.50), 1–3
  lines, centre-aligned, the widest line up to ≈ 92 % of the frame width; cap height ≈ 6–8 % of frame
  height.
- **Type:** heavy condensed sans caps (Anton / Bebas class), **pure white `#FFFFFF` with a soft dark drop
  shadow, no outline**. **One accent phrase per poster in a saturated colour**: red `#E80003`
  (EXTREMELY DIFFICULT · WHEN YOU'RE NOT CONTROLLING THEM · KICKBOXING TRAINING / SIDEKICK · ROMANTIC OR NOT
  · PROFESSIONAL · OR MEMES WILL DATE FAST), **blue `#3EA8FA`** (DESCRIBE WHAT SHOWS UP), **cyan
  `#15FAFA`** (JASON), **green `#11EE0B`** (BENEfIT OF WORKING TOGETHER · THEY KEEP DOING CRIMES
  TOGETHER). Looks like: red = the punch, green = the reassuring "together" lines.
- **Plate:** game footage blurred to mush (wanted stars and the minimap still read as colour blobs),
  **playing at 1×** — the plate moves; the plate **hard-cuts under held text** (3:20.62, ≈4:47.5, 6:40.0,
  6:57.53). #41's plate is the blurred kickboxing title image.
- **Entrances/exits:** hard cut in from the face, hard switch poster-to-poster (the text swaps, the plate
  may continue), hard cut out. No text animation, no grow.
- **Typos/artefacts that shipped:** the font renders "ff"/"fi" as lowercase ligature glyphs —
  **"Off", "DIffICULT", "BENEfIT", "SPECIfIC"**; "BECOMES....PROFESSIONAL" (four dots).

---

## 4. Recurring patterns

- **Cadence.** 129 visual changes (scdet, merged) = **16.6/min**; per minute 18 · 16 · 20 · 18 · 15 · 18 ·
  15 · 9 — even all the way, dropping only in the close. Overlay runs every ~14 s.
- **Which line gets what.**
  - a **section title** → its AI title image, on the exact words;
  - an **anecdote** (what the Italian creator did, what TGG saw) → AI story illustrations, panel by panel;
  - a **Rockstar quote** → a plain-text poster, verbatim, in curly quotes;
  - a **game fact you can show** → GTA 6 trailer / Extended Look footage, full frame, HUD in;
  - **his reaction, joke or opinion** → the face, with cut zooms (and the B&W role-play once).
- **Game footage is GTA 6 only**, full frame, sharp, HUD left in, 1× speed, 1–9 s per clip, usually 1–3
  clips per run. No inset, no matte, no PiP anywhere.
- **Stills always move**: every AI image pushes slowly (some sub-pixel, near-static: 23/87, SHE HAS A
  LIFE, TELL HER).
- **Transitions:** hard cuts only — the exceptions are the B&W switch (a hard cut into a graded take) and
  one 2–4-frame RGB-split blur flash between two night-drive clips at 5:26.24 (looks like a glitch
  transition preset, the only one).
- **Face slow-downs: three, all 0.8×** (every 5th frame doubled at 59.94): **0:05.09–0:06.17 "worthless."**
  (1.1 s, on a 1.49× cut zoom), **2:16.72–2:19.22 "money laundering, ladies and gentlemen"** (2.5 s, 1.52–1.60×),
  **6:24.22–6:26.30 "even bigger problems"** (2.1 s, 1.56×). Each slow-down coincides with the biggest
  cut zooms in the video — **slow-down + max zoom is one move**.
- **Longest stretches without an overlay:** 3:21.0–3:41.7 (20.6 s, the "man who's seen something" rant)
  and the 20.7 s close. Longest without the face: 13.9 s (the cold-open preview montage).

## 5. Comedy and emphasis devices

| t | device |
|---|---|
| 0:05.1 | **Slow-down + cut zoom on the hook word** — "worthless." at 0.8×, face jumps 1.16 → 1.49 inside the take. |
| 0:17.6 | **The anecdote as an illustration** — Rob "playing the game in front of them" drawn as a Rockstar round table in Scotland. |
| 0:59.5 | **The prop self-own** — "Don't ask me why I have a screwdriver." The screwdriver then becomes his mic for the rest of the video. |
| 1:09.5 | **The comic speech bubble** — the cashier blurting "WE HAVE A SAFE IN THE BACK ROOM!" in a comic-book bubble, 5 s, under "the cashier just said it… he shouldn't be robbed, he should be fired." |
| 1:46.6 | **The heist-map gag** — "like an ex, so the store has a back door": an isometric map with FRONT DOOR / BACK DOOR / SAFE labels and escape route. |
| 1:57.6 | **Cut zoom on a title card** — YOUR MONEY IS DIRTY punches ×1.3 a second after it lands. |
| 2:16.7 | **Mock-solemn slow-down** — "money laundering, ladies and gentlemen" at 0.8× on a 1.5–1.6× face. |
| 2:48.0 | **The callback title** — the cold-open teaser image returns as section 3's card. |
| 3:06.2 | **The silent answer** — Rob's speech bubble is only "…" under the creator's "WHAT HAPPENS AT 6 STARS?". |
| 3:12.5–3:21.0 | **Quote poster pair** — the withheld part ("DESCRIBE WHAT SHOWS UP") in blue, the only blue in the video. |
| 3:21–3:41 | **A/B cut-zoom alternation** on the rant (1.00 / 1.38 / 1.10 / 1.41 / 1.00 / 1.34 / 1.00 / 1.45). |
| 4:35.7 | **Found key art as the punchline** — RDR2's cover on "less demanding than Red Dead 2". |
| 4:53.1 | **The poster plate is the joke picture** — "KICKBOXING TRAINING… LIKE A SIDEKICK" set over the blurred kickboxing illustration. |
| 6:19.6–6:26.2 | **Escalation into the role-play** — 1.38–1.45, then 1.56 at 0.8× on "even bigger problems". |
| 6:26.2–6:31.4 | **The B&W role-play** — he plays the girlfriend ("Piece of shit. I'm gonna go to bed fully clothed tonight.") in a desaturated, re-framed take, screwdriver at the lens, with a **vertical squash distortion** (face flattened/widened) 6:29.0–6:29.7, then a hard cut back to colour. |
| 6:59.2 | **The dramatic ellipsis** — "BECOMES....PROFESSIONAL", the pause written into the poster. |
| 7:18–7:21 | Finger to lips "shh" before the final quote poster. |

## 6. Palette and type

| swatch | hex | where |
|---|---|---|
| Set green (LED wall) | `#5ABA75` / `#5AC480` | every face shot |
| Chair brown | `#4D1E0E` | face shot, left third |
| Poster white | `#FFFFFF` | all quote-poster text |
| Poster red | `#E80003` | quote-poster accent (6 of 10), CORNER SHOP "HAS A PLAN…." |
| Poster blue | `#3EA8FA` | "DESCRIBE WHAT SHOWS UP" |
| Poster cyan | `#15FAFA` | "JASON" |
| Poster green | `#11EE0B` | the two "together" lines |
| Title cream | `#FAF3E4` / `#FBF5EF` / peach `#FCE4CD` | title-image headlines |
| Title pink | `#EE37A3` / `#E90C92` | "ROB NELSON", "DIRTY", underline swash |
| Neon pink / teal | `#E44FA4` / `#94E6D8` | 23 / 87 |
| Bubble red | `#830007` | the speech bubble's "SAFE", "BACK ROOM!" |
| Art palette | magenta-violet sunsets, pastel deco, palm silhouettes | all AI art |

Type classes: (1) **heavy condensed caps, white + drop shadow** — the posters and the editor-typed title
text; (2) **heavy condensed caps in cream with pink accent, outline/shadow** — the baked-in title
headlines; (3) **lighter letter-spaced condensed caps with glow** — THE COUPLE ICON / YOU CAN BREAK UP;
(4) **comic italic caps** in the speech bubbles; (5) handwritten labels ("THE ITALIAN CREATOR",
"ROB NELSON", the notepad). No sentence-case serif, no geometric sans — the Fuel System card fonts are
absent.

## 7. Ending (7:25.0 – 7:45.67)

One 20.7 s face run after the last quote poster: jump cuts at 7:31.43 (to 1.34×), 7:33.85, 7:40.13, a
1.19× snap at 7:38.9; he riffs on "skibidi toilet… sigma memes", spreads his arms at 7:40, then the
sign-off "let me know what you guys think… make sure you subscribe to the channel… and I'm out" over a
medium face at ≈1.05×. Last frame (7:45.4) is that medium shot. **No end card, no end-screen space, no
outro graphic, no logo, no fade.** The fifth SUBSCRIBE bug already ran at 7:12–7:20.

## 8. Differences

### vs the preset README (`affan-afterhours-facecam/README.md`)
| README says | DIRTIEST does |
|---|---|
| face on screen ~80 %, overlays are seasoning | **61 %** face; overlays 39 % (33 runs, 4.25/min) |
| overlays almost all game footage; cards 1–1.6/min on quotable punchlines | **24 AI illustrations** (10 chapter-title images + 14 storyboard panels) + 10 quote posters + ≈ 25 game clips. The illustrations are the dominant graphic, and **titles are section headers, not punchlines** |
| posters = 16:9 inset card ~72 %, tilted 1–3°, cream type, pink accent, growing 8–15 % over a blurred plate | **no inset cards at all.** Titles are full-frame art; quotes are plain white text on a blurred moving plate with red/blue/cyan/green accents (the README's "two plain-text posters" kind, but coloured and the house style here) |
| one accent colour (pink `#EE2A9A`), green only for GTA 5 | pink only on the title art; posters rotate **red / blue / cyan / green** |
| cut zoom +25 % (×1.27), ~5/min | **×1.16–1.60, median ≈ 1.34**, ≈ 3.9/min, about half on jump cuts — matches CREATOR-HAND, not the README |
| slow-downs 0.5–0.6× | **0.8× ×3**, each fused with the biggest cut zoom |
| inserts routinely slowed (0.5×–0.03×) | **every insert plays at 1×**; no near-freezes |
| SUBSCRIBE bug twice | **five times**, every ~1.5 min |
| uses GTA V / SA footage for the old games | GTA 6 only; the old game appears once as RDR2 key art |
| only device: hard cut | hard cut + one B&W graded take with a squash distortion + one RGB-split flash |
| meme insert, interview freeze | none; the comedy is carried by illustrations, the bubble and the B&W role-play |

### Cross-check with the measurement job (`report.md`, `probe/summary.md`, landed after this was written)
- **Face 88 % / overlays 12 %** in the job is the face detector counting the AI-illustrated faces (Jason,
  Lucia, Rob) as the face; by shot, the face is 61 % (§1).
- **Zoom steps median ×1.156** in the job is measured step-to-step (from the pushed level); measured from
  the base frame the same zooms sit at ×1.16–1.60, median ≈ 1.34. Both say "big static steps".
- **"10 slowed stretches at ×0.49–0.69"** come from word rate + duplicates and are **not supported by the
  frames**: at 59.94 fps the only regular duplicate patterns on the face are the three 0.8× stretches in
  §4 (period-5 doubling); the flagged spots (0:01.8, 2:09, 2:25, 4:03–4:14, 5:28) have no periodic
  duplicates. Trust the frames (CREATOR-HAND found the same false positives on Game Informer).
- The job's audio check finds **3 chopped words** — a hard cut inside a word with a 12–17 dB drop:
  0:52.40 "identical.", 4:47.40 "press", 5:49.20 "minutes" (not analysed here; the first one sits on the
  "scarily identical" joke).

### vs CREATOR-HAND.md (the creator's own 09-23 → 09-30 timelines)
- **Same:** 0.8× slow-downs on a joke/claim (CREATOR-HAND's number, here already in September);
  static-scale cut zooms at 125–160 %; a +≈10 % push per face run (the "110" preset shape); the voice from
  0.000; ends on the face.
- **Different:** no colour-matte insets (overlays are full frame); no screen-share PiP; no meme clips,
  no colour-bars glitch (visually — audio not analysed here); no fade from/to black; heavy **AI
  illustration** use that the later timelines do not show; five canned SUBSCRIBE bugs; the B&W role-play
  take.
