# Affan Afterhours: GTA Shorts editing style (evidence file)

Audit date 2026-10-08. Scope: the **editing** of the channel's vertical GTA Shorts (1080×1920, face cam). I compared the three June/July viral winners and three mid-tier hits with the four newest edits (Sep/Oct). Topic, title and upload timing are left out, except where the edit itself carries them.

**How to read this file.** Anything stated plainly was SEEN in a frame, MEASURED by a script, or READ from the creator's Premiere timeline. Anything marked *looks like* is an inference. Timecodes are `s.ss` from the first frame of the exported master.

---

## 0. Sources and matching

No downloads were needed (0 of the 8 allowed). Every analysed short has a local master in `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\`.

**Matching rule:**
- vertical 1080×1920
- duration within ±1 s, and it rounds to the YouTube duration
- file mtime (PKT, UTC+5) a few minutes to a few hours BEFORE the upload timestamp (UTC from the yt-dlp metadata in `../meta/`)
- one frame checked by eye: the creator's face plus GTA content

| # | Short (views) | YouTube id, upload (PKT) | Local master | Length | Exported | Evidence |
|---|---|---|---|---|---|---|
| 01 | Don't Release GTA 6 On PC Please (859 k) | jjI1pFoUlwc, 06-28 12:21 | `son.mov` | 29.65 s (YT 30) | 06-28 10:59 | 1 h 22 before upload. Frame shows creator, GTA mod clips |
| 02 | GTA 6 Will Be On STEROIDS (442 k) | mooEIFZZ9AA, 07-12 17:59 | `gtasax.mov` | 28.75 s (YT 29) | 07-12 17:54 | 5 min before upload |
| 03 | GTA 6 Shouldn't Be Released On PC (281 k) | AxYzZ5A1vKY, 07-04 11:19 | `crop.mov` | 37.15 s (YT 37) | 07-04 09:51 | `con final yt.mov` (37.88 s → 38) rejected on duration |
| 04 | GTA 6 Is Coming On PS4! (42 k) | W7uKM16ijF4, 07-06 00:25 | `broke.mov` | 27.13 s (YT 27) | 07-06 00:02 | 23 min before upload |
| 05 | GTA 6 On MOBILE (41 k) | 6QBTB-OwoWM, 07-03 01:15 | `bc.mov` | 16.62 s (YT 17) | 07-02 22:42 | |
| 06 | GTA 6 DESTROYS FORZA HORIZON 6 (34 k) | y6Fgk0R1pek, 07-01 00:04 | `gta444.mov` | 30.08 s (YT 30) | 06-30 23:57 | `gta4.mov` (10.2 s, 23:55) is an aborted partial export of the same edit |
| 07 | Travis Scott In GTA 6 CONFIRMED!! (2.9 k) | 6PZY1RGH1Qg, 09-15 23:13 | `travis.mov` | 33.92 s (YT 34) | 09-15 23:05 | |
| 08 | GTA 6 Collector's Box Is DISAPPOINTING (1.3 k) | WXUoPBk-yMA, 09-25 16:37 | `Collector.mov` | 61.93 s (YT 62) | 09-25 14:40 | Equals Premiere **Sequence 06** end (61.93) |
| 09 | Vice City / Heat-arena short (**not in the public Shorts list**) | none | `vice.mov` | 38.07 s | 09-25 01:13 | Equals **Sequence 04** end (38.07). *Looks like* never published, or deleted |
| 10 | GTA 6 Not Nominated For Game Of The Year (4.6 k) | V_S4T8KIz9U, 10-01 19:01 | `GOTY.mov` | 38.63 s (YT 39) | 10-01 18:29 | Equals **Sequence 21** end (38.63) |

All masters are H.264, 60 fps, about 24 Mb/s (04 is about 10 Mb/s).

**Where the evidence lives:**
- `frames/<nn_name>/sheet_XX.jpg`: 4 fps sheets with burned timecodes. All of them were read.
- `frames/fullres/`: full-resolution frames, caption crops, 60 fps caption-swap strips, hook strips.
- `audio/*.spec.png`: spectrograms.
- `probe/<nn>.cuts60.json`: cut lists.
- `tools/`: the measurement scripts and the raw visual notes.

---

## 1. House constants (true of all 10)

**Canvas and picture**
- **Canvas.** 1080×1920, 60 fps.
- **Picture.** A 16:9 face-cam frame scaled into a centred horizontal band. It is never a true vertical crop, except the skit (05), which is full-bleed. Black bands sit above and below the picture.
  - On the timelines, face clips are base-scaled 126–128 %. This gives a 1382 px band, 72 % of the frame height, at y 14–86 %.
  - The winners measure 72–85 % (see § 3).

**Persistent title (top black band)**
- One line of white Anton, ALL CAPS (the text is typed lowercase on the timeline and rendered caps). Glyph height is 50–63 px (2.6–3.3 % of 1920). It runs the full length of the video.
- It ends in 1–2 colour emoji: 🥀, 😭🙏, ✌️🥀, 😭.
- On the recent timelines the emoji is a separate PNG sticker on the top track, sitting at the end of the title line:
  - `crying.png`: scale 29 %, at (0.83, 0.17)
  - `rose.png`: scale 37 %, at (0.79, 0.15)
- The title is written as a reaction, not a headline: "ROCKSTAR IS WELL AWARE GNG", "AIN'T NO WAY THIS IS REAL".

**Captions**
- Font and look: Anton, pure white, a thin black outline plus a soft black drop shadow. Seen at full resolution: `frames/fullres/cap_zoom.png`.
- Position: one line, centred horizontally. The caption centre sits at 54–65 % of frame height, just under the chin and lips, and stays at one constant y for the whole video.
- Length: 1–3 words per caption, mean about 2.2. Captions hold 0.6–0.95 s each.
- **Hard swap, with no pop, scale or fade animation.** The 60 fps strips show the next caption appearing whole on one frame (`pop01.png`, `pop10.png`).
- **Text treatment:**
  - Swear words are censored with an asterisk: SH\*T, F\*CK, FCKIN, C\*C\*INE.
  - A read-out comment is put in quotation marks.
  - No full stops or commas; only `?`.
- **Timeline structure:** each caption is its own Essential Graphics text clip on V4, named with its own words. The timelines have 40–90 of them per short.

**Edit**
- **Cut zooms.** The face alternates between the base framing and a punch-in, cut on a sentence beat. There is no keyframed push: the creator cuts to the tighter scale.
- **Opening and ending.** No intro, no outro, no CTA. Every short ends on a cold cut on the last caption.

**Timeline layout** (Sequences 04, 06 and 21)

| Track | Contents |
|---|---|
| V1 | Face, plus full-frame inserts |
| V2 | Adjustment layer across the whole short (its effect is not decoded; *looks like* a grade) |
| V3 | Screenshot cards |
| V4 | Captions |
| V5/V6 | Title |
| V6/V7 | Emoji PNG |
| A1 | Voice. A separate recorder file, `YYYY-MM-DD hh-mm-ss.mp4` |
| A2/A3 | SFX |
| A3/A4 | Meme music |

---

## 2. Per-short catalogue

Caption glyph heights are measured on full-resolution frames: the white-pixel band height including the outline. The cut count is the creator's own edit points from a 60 fps jump-cut detector (`tools/cuts.py`):
- Against ground truth it found Seq 21: 19/19, Seq 04: 20/20 plus 1 internal B-roll cut, and Seq 06: 32/34.
- Cuts inside reposted B-roll clips are excluded by hand.

### 01 · Don't Release GTA 6 On PC Please · 859 k · 29.65 s

- **Set.** Plain mint-green wall, brown leather chair, black tee, no glasses, QuadCast mic lower centre. Daylight look.
- **Title.** `ROCKSTAR IS WELL AWARE GNG ✌️🥀`, y 10–13 %. The picture runs 14–86 % (72 %).

**Hook (0–1.85)**
- 0.00: the creator's head is **down, reading**. He lifts it while saying the viewer's question, captioned in quotes: `"WHY ISN'T GTA 6"` → `"COMING TO PC?"`.
- 1.60: a 0.43 s dip to black.
- 1.85: cut to `I DON'T THINK / YOU REALIZE`.
- 3.02: punch-in, about ×1.4, on the censored `THE SH*T THAT / THOSE PEOPLE / ARE CAPABLE OF`.

**Captions.** All caps, glyph height 70–79 px (3.6–4.1 %), centre about 63 %. There are 26 captions, 2.2 words each, about 0.86 s per caption while he is on screen. Captions are off during the inserts.

**Structure**
- Three times: "I saw [absurd PC mod]". Each time the line is said on a wide shot, then the tight shot, then paid off by a **full-frame black-and-white repost of a viral TikTok mod clip**. The clips keep their watermarks and burned-in text: `@gamingzar`, "This is why GTA 6 is not coming to PC".
- Inserts:

| Time | Insert |
|---|---|
| 5.72–7.17 | B/W photo of a crying/praying man (sad-meme beat), no caption |
| 12.23–14.17 | B/W aircraft-carrier mod |
| 18.10–19.80 | B/W gorilla-throwing-buses clip |
| 22.97–25.27 | B/W Chop/Franklin clip |

- Total: 4 inserts, 7.4 s (**25 % of the runtime**). No cards at all.

**Transitions**
- **9 dips to black** of 0.27–0.43 s, at 1.60, 5.73, 7.17, 11.97, 14.17, 17.70, 19.80, 22.90 and 25.27. That is one at every beat change and around every insert.
- The caption dims with the picture during a dip.

**Zooms.** Five tight shots: 3.02, 10.28, 16.17, 21.57 and 27.35, alternating with the wide one. At 21.57 there is an **extreme punch-in, about ×2.5 on nose and mouth**, for `WALKING / FRANKLIN`.

**Cuts.** 14 edit points, 28/min. Face shots have a median of about 1.9 s.

**Audio**
- Integrated loudness −22.2 LUFS, peak −2.1 dBFS.
- No Vine boom, no sub-bass hits.
- From 1.6 s a quiet sustained tonal bed. *Looks like* a soft melodic music bed: steady tones at about 400–1200 Hz in the spectrogram, about −45 dB.
- The hook (0–1.5) is voice only.

**Ending.** The last line is a punch-in: `WHEN THEY'RE READY / TO ACCEPT / THEIR FATE`. Cold cut at 29.65.

### 02 · GTA 6 Will Be On STEROIDS · 442 k · 28.75 s

- **Set.** Saturated green wall, maroon sleeveless top, no glasses.
- **Title.** Lower-case sentence `who broke Rockstar's heart 😭🙏`, y 11–14 %. The picture runs 15–89 % (74 %).

**Hook (0–3.0)**
- He is **reading off his phone**, eyes down, then looks up.
- Captions run `so it's almost / confirmed that / GTA 6 / will have / fully interactive / malls` over a GTA VI cover card. The card is about 35 % wide, at y 68–88 %, from frame 0.

**Captions.** **Lower/sentence case**: the only winner without All Caps. Glyph height about 85 px including ascenders and descenders, centre about 64 %. 38 captions, 2.3 words each, about 0.76 s per caption. The punchline `GET A JOB` is in caps.

**Devices**
- **Black-and-white tight face** for the stat beat `179 / story missions`, 3.23–6.10. It returns to colour on the next line.
- **Cards**, about 49 % of the runtime:

| Time | Card |
|---|---|
| 0–3.0 | GTA VI cover |
| 6.25–10.0 | B/W screaming-face meme on cyan; *looks like* the "6-7" meme |
| 13.5–16.0 | GTA V cover |
| 22.25–24.4 | GTA V mall screenshot |
| 24.5–27.0 | PS4 product shot |

- No full-frame inserts.

**Transitions.** **5 dips**, at 3.10, 6.10, 10.07, 11.70 and 27.27.

**Zooms.** About 5, at 3.23, 8.85, 10.22, 18.78 and 27.37, each about ×1.3–1.4.

**Cuts.** 14, 29/min.

**Audio.** −16.6 LUFS. No booms. A tonal bed runs the whole short (lines at about 500–1300 Hz).

**Ending.** A 0.25 s dip at 27.27, then a punch-in on `GET A JOB`. Cold end at 28.75.

### 03 · GTA 6 Shouldn't Be Released On PC · 281 k · 37.15 s

- **Set.** Purple/magenta LED wall, maroon sleeveless top, no glasses.
- **Title.** `ROCKSTAR'S BIGGEST ENEMY 🥀`, in a thin band at y 6.6–9.8 %. The picture runs 10.6–89.3 % (79 %).

**Hook**
- Frame 0 has the **head down**, lifting into a direct address: `YO ROCKSTAR / IS SO / DUMB MAN / THEY SHOULD JUST / RELEASE THE / PC VERSION / SAME DAY / AS CONSOLES`.
- The first shot is held **4.68 s with no cut**. The captions carry it.
- 6.43: punch-in, about ×1.35, on the joke `IF I WAS / MENTALLY CHALLENGED`.

**Captions.** Caps, glyph height 63 px (3.3 %), **centre about 54.5 %**, the highest position of the set. 38 captions, about 2.3 words each.

**Structure.** The same "I saw…" engine as 01: `I SAW GODZILLA / THROWING / CARS AT / PEOPLE'S FACES`, `HOMELANDER / COMPLETELY / VAPORIZING A / PASSENGER PLANE`, `AND FRANKLIN / GETTING ROASTED / BY A / CROP DUSTER`.

**Inserts**

| Time | Insert |
|---|---|
| 12.9–13.9 | B/W meme still: man, eyes closed, chain |
| 13.9–14.25 | **Black frame with the caption `THEY KNOW` over it** |
| 21.75–23.25 | B/W mod clip |
| 27.17–29.2 | B/W mod clip |
| 32.15–34.0 | B/W mod clip |

Total 6.4 s (17 %). No cards.

**Flash frame.** At 27.0 and 32.0, a 1–2 frame **deep-fried flash** of his face (blown-out red and white) right before the B/W clip.

**Transitions.** **6 dips**, at 8.43, 12.90, 13.90, 18.17, 29.20 and 34.00.

**Zooms.** 6, at 4.68, 6.43, 11.32, 16.40, 24.65 and 31.00.

**Cuts.** About 19, 31/min.

**Audio.** −19.3 LUFS. No booms. A tonal bed from about 6 s.

**Ending.** `YEAH I THINK / WE SHOULD LET THEM / HAVE THE DECISION / ON THIS ONE`. Cold end at 37.15.

### 04 · GTA 6 Is Coming On PS4! · 42 k · 27.13 s

- **Set.** Lime/olive wall, window bars, black sleeveless top. He holds a PS4 box as a prop.
- **Title.** In quotes, as a viewer comment: `"BRO GTA 6 SHOULD BE ON PS4" 🥀`, y 7–10 %. The picture runs 11–90 % (79 %).

**Hook**
- Head down, reading. Quoted captions `"MAN WHY ISN'T" / "GTA 6 COMING TO" / "PS4"`.
- 1.83: punch-in, about ×1.3, on `HOW ABOUT YOU / SHUT THE / F*CK UP / ALRIGHT?`.
- 3.90: a **Vine-boom-type sub-bass hit**, 2.8 s long, +38 dB over the median sub level. This is the same signature as the timeline's `Vine boom sound effect.mp3`.

**Captions.** Caps, 63 px, centre about 57 %. 34 captions.

**B-roll, cards, memes.** **None.** Pure face plus captions plus cut zooms.

**Zooms.** 5, at 1.83, 6.75, 12.90, 18.88 and 25.75. At 18.88–21.4 there is a **2.5 s tight hold with no caption**: a silent stare.

**Transitions.** 0 dips.

**Cuts.** 13, 29/min.

**Audio.** −18.4 LUFS. A tonal bed. Two smaller bass hits at 1.76 (on the punch-in) and 23.5.

**Ending.** Punch-in, `IN 13 YEARS`. Cold end at 27.13.

### 05 · GTA 6 On MOBILE · 41 k · 16.62 s · skit format

- **Picture.** **Full-bleed 9:16**: no black bands.
- **Title.** Two lines.
  - Line 1 is a coloured persona label: `PS5 PLAYERS` (blue), `XBOX PLAYERS` (green), `PC PLAYERS` (yellow).
  - Line 2 is white: `WHEN GTA 6 RELEASES`.
  - At 4.30 it switches to `MOBILE MFS`.
- **Personas.** Each persona has its own LED colour:

| Time | Persona | Light |
|---|---|---|
| 0–2.57 | PS5 and Xbox | Teal |
| 2.57–4.30 | PC | Green |
| 4.30 onward | Mobile | Red, near silhouette |

- **Captions.** Caps, 63 px, centre about 58 %. The mobile persona whispers search queries: `GTA 6 / MOBILE APK / DOWNLOAD / … / ON SAMSUNG / A-SERIES`.
- **Meme.** 7.93–8.97: a glitchy purple anime clip, letterboxed.
- **Cuts and dips.** 7 cuts (25/min). 0 dips.
- **Audio.** −16.5 LUFS. A dark tonal bed enters with the red persona at 4.3.
- **Ending.** Cold end at 16.62.

### 06 · GTA 6 DESTROYS FORZA HORIZON 6 · 34 k · 30.08 s

- **Title.** **None**: the only short without one.
- **Picture.** 7.5–92.4 % (85 %), the largest face in the set.
- **Set.** Purple LED, olive tank top, no glasses.

**Hook.** `SO I SAW / SOMEONE COMPARING / CARS IN GTA 6 / TO FH6`, with a finger pointing at the lens.

**Captions.** Caps, 74 px (3.9 %), centre about 57 %. About 42 caption changes.

**Visuals**
- 6.5–8.9: a **full-frame split-screen comparison clip**, Forza on top and GTA VI below, 2.4 s, no caption.
- Cards at y 67–90 %, about 70 % wide, about 33 % of the runtime:
  - Xbox One | PS4, 14.25–19.9
  - RAGE logo, 20.0–24.1

**Transitions.** 4 dips, at 6.43, 8.93, 14.17 and 19.97.

**Zooms.** 25.53 punch-in (`GTA 4 DAYS`). From 28.52 to the end, an **extreme ×2.5 mouth close-up** (`FCKIN INSANE`).

**Cuts.** About 10 (20/min); the detector may undercount here.

**Audio.** −20.0 LUFS. A tonal bed. One bass hit at 25.54 on the punch-in.

### 07 · Travis Scott In GTA 6 CONFIRMED!! · 2.9 k · 33.92 s (recent)

- **Set.** The "skool" neon set: pink and blue LED, **sunglasses**, black sleeveless top.
- **Title.** `THIS MAN IS A DIFFERENT BREED 😭🙏`, y 12.6–15.2 %. The picture runs about 14–86 %.

**Hook.** `TRAVIS SCOTT JUST / CASUALLY REMINDED / EVERYONE THAT / THERE ARE LEVELS` with a **photo card on frame 0**: Travis, at y 66–86 %.

**Captions.** Caps, **57 px (3.0 %)**, centre about 61 %. About 41 changes.

**Cards.** 9 different cards, visible in **about 62 % of sampled seconds**: Travis, an Instagram shoe post, a concert photo, the Nolan film, Tom Holland, Zendaya, the Ye album, GTA VI art, MJ.

**Meme.** 3.80 dip, then 4.0–5.17 a B/W grainy smiling close-up, full band. *Looks like* a falling-tone SFX into it (a descending staircase in the spectrogram at 3.5–4.5).

**Zooms.** About 5 (about ×1.3–1.4).

**Cuts and dips.** 13 cuts (23/min). 2 dips.

**Audio.** −17.5 LUFS. Tonal bed. Bass hits at 0.62, 4.60 and 18.32.

**Ending.** `AFTER MICHAEL JACKSON` plus an MJ card. Cold end.

### 08 · Collector's Box Is DISAPPOINTING · 1.3 k · 61.93 s (Sequence 06, ground truth)

- **Set.** The "skool" neon set, sunglasses.
- **Title.** **Two lines**: `GTA 6 COLLECTOR'S BOX` in white, `IS DISAPPOINTING` in **red**.

**Hook.** `THE BIGGEST PROBLEM / WITH THE / GTA 6 / $400 COLLECTOR'S BOX` plus a product card from frame 0.

**Captions.** 90 caption clips. Glyph height **55 px (2.9 %)**, centre about 62.5 %.

**Face clips.** Base scale 126 %, about 12 cut zooms (136–258 %). One is 258 % off-centre for `IT'S THE DAMN SUNGLASSES` (4.07–5.63).

**Cards.** 10 screenshot cards on V3, scale 63–87 %, centred at y 0.76–0.81. 21.7 s, **35 %** of the runtime.

**Speed.** One 0.8× nested slow-mo, 19.45–20.87.

**SFX**
- **Vine boom ×5**, at 5.42, 20.72, 31.23, 33.15 and 52.67, gain −10 dB. My detector re-found all five.
- **TV colour-bars tone ×2** at 32.35 and 40.73, used as a **censor beep** on `C*C*INE SPOON`.

**Music.** `QKThr.mp3` at −6 dB, 0–60.08.

**Loudness.** −14.9 LUFS, **peak 0.0 dBFS**.

**Cuts and dips.** 34 cuts (33/min). 0 dips.

### 09 · Vice City / Heat arena · not public · 38.07 s (Sequence 04, ground truth)

- **Set.** "skool" set, sunglasses.
- **Title.** `THIS GAME'S HYPE IS UNREAL` plus a `crying.png` sticker, y 15.4–18.3 %.

**Hook.** `ROCKSTAR JUST PAID / $975,000 / TO PUT VICE CITY / ON TOP OF / A REAL NBA ARENA` with a small Rockstar-logo card from frame 0.

**Captions.** 40 caption clips, glyph height 56 px, centre about 63 %.

**Face clips.** Base scale 128 %, 7 zooms (145–211 %).

**Visuals**
- 5.75–8.32: full-band news B-roll video (197 %).
- 6 screenshot cards: 14.8 s, 39 %.
- 23.18–24.60: an extreme punch on `THE F*CKING MANHOLE COVERS`.
- 30.27–30.87: a **0.8× slow-mo at 211 %, with no caption**.

**SFX.** One Vine boom at 5.65, on the news-clip entrance.

**Music.** `Marty Gots a Plan` at +4 dB, cut into 4 pieces. It **drops out** during:
- the news clip
- the manhole rant
- the 0.8× beat

**Loudness.** −14.7 LUFS, **peak 0.0 dBFS**.

**Cuts and dips.** 20 cuts (31.5/min). 0 dips.

### 10 · Not Nominated For Game Of The Year · 4.6 k · 38.63 s (Sequence 21, ground truth)

- **Set.** Purple LED plus "skool" neon, black sweatshirt, no glasses.
- **Title.** `AIN'T NO WAY THIS IS REAL` plus a `rose.png` sticker, y 13.3–16.2 %.

**Hook.** `GTA 6 / MIGHT NOT EVEN BE / NOMINATED FOR / GAME OF THE YEAR` with a **GTA VI logo card from frame 0**.

**Visuals**
- 3.02–5.38: a screaming-old-man meme still, full band, with a slow push 140→150 %. *Looks like* the Angry Grandpa meme. A black-video opacity fade sits over it.

**Face clips.** **All 19 face clips at 1.1× speed.** The voice is also at 1.1× on A1.
- Base 128 %.
- 7 zooms, 149–256 %.
- 15.58–18.70: a 256 % extreme close-up with a keyframed pan and **no captions**.
- 21.02–21.65: the face frame shoved off-centre and stretched (pos x 0.11).
- 29.30: a 180 % punch on `I DON'T ACCEPT THAT`.
- 36.75–38.63: a 181 % held stare with no caption, as the ending.

**Captions and cards.** 40 caption clips at 55 px, centre about 59.5 %. 6 cards: 12.2 s, 32 %.

**Music.** `WWE The Undertaker Theme Song` at −9 to −15 dB, in 8 pieces. It **drops out** for:
- 10.33–12.02
- 24.20–25.07
- 29.13–29.97, the "I don't accept that" punch

The bell tolls show as sub-bass hits at 0.5, 3.6, 8.3 and 12.7. No Vine boom.

**Loudness.** −16.1 LUFS.

**Cuts and dips.** 19 cuts (29.5/min). 1 dip.

---

## 3. Side-by-side numbers

| | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 |
|---|---|---|---|---|---|---|---|---|---|---|
| Views | 859 k | 442 k | 281 k | 42 k | 41 k | 34 k | 2.9 k | 1.3 k | — | 4.6 k |
| Length (s) | 29.7 | 28.8 | 37.2 | 27.1 | 16.6 | 30.1 | 33.9 | 61.9 | 38.1 | 38.6 |
| Creator cuts/min | 28 | 29 | 31 | 29 | 25 | ~20 | 23 | 33 | 31.5 | 29.5 |
| Tight-shot zooms | 5 | 5 | 6 | 5 | 1 | 2 | ~5 | ~12 | 7 | 7 |
| Extreme ×2–2.5 punch | 1 | – | – | – | – | 1 (end) | – | 1 | 1 | 1 |
| **Dips to black** | **9** | **5** | **6** | 0 | 0 | 4 | 2 | **0** | **0** | **1** |
| Picture band (% H) | 72 | 74 | 79 | 79 | 100 | 85 | ~72 | 71 | 72 | 72 |
| **Caption glyph px (% H)** | **70–79 (3.6–4.1)** | **~85 lc (4.4)** | **63 (3.3)** | 63 | 63 | **74 (3.9)** | **57 (3.0)** | **55 (2.9)** | **56 (2.9)** | **55 (2.9)** |
| Caption centre (% H) | 63 | 64 | 54.5 | 57 | 58 | 57 | 61 | 62.5 | 63 | 59.5 |
| Full-frame inserts (% time) | **25** | 0 | **17** | 0 | 6 | 8 | 3.5 | 0 | 7 | 6 |
| Card share (% time) | 0 | 49 | 0 | 0 | 0 | 33 | **62** | 35 | 39 | 32 |
| Card on frame 0 | no | yes (cover) | no | no | no | no | **yes** | **yes** | **yes** | **yes** |
| Head-down / reading start | **yes** | **yes (phone)** | **yes** | **yes** | no | no | no | no | no | no |
| Vine booms | 0 | 0 | 0 | 1 | 0 | 0 | 0 (3 hits) | **5** + 2 beeps | 1 | 0 |
| Named meme song | no* | no* | no* | no* | no* | no* | ? | QKThr | Marty | Undertaker |
| Loudness (LUFS / peak dBFS) | −22.2 / −2.1 | −16.6 / −2.6 | −19.3 / −4.3 | −18.4 / −3.6 | −16.5 / −3.6 | −20.0 / −3.3 | −17.5 / −3.8 | −14.9 / **0.0** | −14.7 / **0.0** | −16.1 / −1.8 |

\* The winners all carry a quiet tonal bed; I could not identify it. *Looks like* soft melodic or ambient music, not a recognisable meme theme.

Caption cadence is the same across eras: about 2.2 words per caption and about 0.7–0.9 s per caption (65–80 captions per minute of face time).

---

## 4. What the winners share (01/02/03 vs the recent 07–10), editing only

The cut rate is not the difference: 28–31/min in both groups, and both use cut zooms on sentence beats. What differs:

1. **Shorter.** The winners run 29–37 s (median 29.7 s). The recent four run 34–62 s (median 38.4 s).
2. **The video "breathes" with dips to black.** The winners have 5–9 short dips (0.27–0.43 s) at beat changes and around every insert, about one every 4–6 s. The recent four have 0–2.
3. **Proof is full-frame and black-and-white, not a small card.**
   - 01 and 03 (the two PC winners) put 17–25 % of their runtime into full-frame, desaturated reposts of viral GTA-mod TikToks. Each one pays off an "I saw…" line, with no caption on top, plus a B/W meme still after the setup. They use **no cards at all**.
   - 02 uses cards but adds a B/W face segment for its stat beat.
   - The recent four lean on full-colour screenshot cards under the caption for 32–62 % of the runtime, with full-frame inserts at 7 % or less.
4. **Bigger captions.** Winners' caps measure 63–79 px glyph height (3.3–4.1 % of 1920). 02's lower-case captions reach about 85 px including ascenders. The recent four are all 55–57 px (2.9–3.0 %): about 13–30 % smaller.
5. **The hook opens on the creator, not on a graphic.**
   - In all three winners (and in 04), frame 0 shows the creator **looking down or reading** (a comment, his phone). He lifts into the line, which is often a read-out comment in quotes.
   - The first cut comes at 1.8–1.9 s into a punch-in on the first insult or claim. (In 03 the first shot is held for 4.7 s.)
   - Every recent short opens on a news-style line with a **card already on frame 0**.
6. **A plainer sound bed.**
   - The winners have no recognisable meme song and no Vine boom; the only boom in the set's top six is in 04.
   - The recent four use named meme themes (Undertaker, Marty Gots a Plan, QKThr), up to 5 Vine booms, and a colour-bars censor beep. Two of them peak at 0.0 dBFS.
   - The winners sit at −16.6 to −22.2 LUFS. YouTube normalises loudness, so loudness itself is not the lever, but the busier SFX layer is new.
7. **New devices not seen in any winner:**
   - the 1.1× speed-up on every face clip (Seq 21)
   - two-line coloured titles (Seq 06)
   - long caption-less extreme close-ups (Seq 21, 15.6–18.7)

**Confounds to keep in mind.**
- **Production.** The winners were shot on a different set: a plain green or purple wall, no sunglasses. The recent four use the busier "skool" neon set, and three of them have sunglasses.
- **Timing and topic.** June/July PC-release outrage is a different moment from Sep/Oct news.
- **Sample size.** Three winners against four recent shorts: these are correlations to test, not proven causes.

---

## 5. Recipe: a GTA Short edit for this channel

**Format and framing**
- **Length.** 27–35 s, target 30 s, about 80–95 spoken words. Cut anything that is not the claim, the proof or the punchline.
- **Canvas.** 1080×1920, 60 fps.
- **Face picture.** The 16:9 cam centred, base scale **135–150 %**: a picture band 75–85 % of the frame height, starting at about y 7–11 %. Face centred horizontally. (128 % is the recent default. The 859 k short was at 72 %, so this is a preference, not a rule.)

**Title (V5)**
- One line, white Anton ALL CAPS, glyph height 50–56 px, in the top black band (centre y about 8–12 %), for the full length.
- Written as a reaction or a quoted comment, ending in 1–2 emoji as PNG stickers: 🥀, 😭🙏, ✌️🥀.

**Captions (V4)**
- One Essential Graphics clip per caption.
- Anton, white, thin black outline plus a soft black shadow, **glyph height 63–75 px (3.3–3.9 %)**.
- Centred x, at **one fixed y just under the lips, 55–63 %**.
- 1–3 words (mean 2.2), held 0.6–0.9 s, **hard swap with no animation**.
- Text rules:
  - Censor swears with `*`.
  - Put read-out comments in quotes.
  - Only `?` as punctuation.
  - Captions off during full-frame inserts.

**Hook (0–2 s)**
- The first frame is the creator **looking down or reading**, lifting to the lens on the first word.
- Caption on frame 0. No card on frame 0.
- First cut at **1.6–1.9 s**, into a ×1.3–1.4 punch-in on the first insult or claim.
- An optional single Vine boom (−10 dB) on that punch-in. Use it once, never more.

**Cutting and zooms**
- **Cuts.** 28–31 creator cuts per minute: a face shot every 1.5–2.5 s, never held longer than about 4.7 s.
- **Zooms.** Alternate base and **×1.3–1.4** tight shots, one tight shot per sentence: 5–6 per 30 s. Place **one extreme ×2–2.5 punch-in** (nose and mouth) on the most outrageous word in the last third. Always end on a tight shot.
- **Dips.** A **0.3 s dip to black** (about 18 frames at 60 fps) at each beat change and in and out of every insert: **5–9 per 30 s**. The caption dips with the picture.

**Proof**
- **Inserts (V1).** For "look at this" beats, use **full-frame, desaturated (B/W) gameplay or mod clips**, 1.5–2.3 s each. Use up to 3 per short, each following a setup line. Add a 1–2 frame blown-out "deep-fried" flash of the face before a big one.
- **Meme still.** One B/W meme still (crying or praying man, a stare) of 1–1.5 s right after the setup line, with no caption. Total insert time about 15–25 %.
- **Cards (V3)**, only for things that must be read: a cover, a stat, a product. Bottom-centre, centred at y 0.77–0.80, 35–70 % wide. **Total under 50 % of the runtime, ideally under 35 %.** Not on frame 0 unless it is the game's cover.
- **Stat beat.** Optionally switch the face to black and white for 2–3 s on a number.

**Sound**
- Voice in front.
- One quiet tonal bed (soft melodic/ambient) entering after the hook (about 1.5 s), at least 20 dB under the voice.
- At most one boom.
- No recognisable meme theme as the bed.
- If using a beep, use it only on censored words.
- Master at about −16 to −18 LUFS integrated, true peak ≤ −2 dBFS (two recent masters hit 0.0).

**Speed.** 1.0× by default. The 1.1× speed-up on the latest edit (Seq 21) is unproven: the winners' speed is unknown because there are no project files for them. Reserve 0.8× slow-mo for one deliberate comic beat, if any.

**Ending.** Cold cut on the punchline caption on a tight shot, last caption at most 1.5 s. No outro, no CTA, no held stare without a caption.

---

## 6. Limits

- The winners have no project files. Their speed changes, the bed's identity, the adjustment-layer effect and the exact zoom percentages are inferred from pixels and audio, and are marked as such.
- "Picture band" for the winners is measured from black-band edges on sampled frames, ±1–2 %.
- Cut counts for 06 and 07 come from the detector only. It undercounts small jump cuts in static profile shots by about 5 %.
- The Vice City short (09) has no public view count, so it cannot sit in the views comparison. It still documents the recent editing grammar.
