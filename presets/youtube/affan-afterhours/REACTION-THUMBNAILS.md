# REACTION-THUMBNAILS.md: face-cam REACTION thumbnails in the KSI+ style (@KSIplus)

The thumbnail half of `REACTION-STYLE.md`. It is the same format (Affan Afterhours face-cam reaction / talk videos) and the same rule: copy KSI+'s grammar exactly, with Affan's own face.

## ▶ STATUS: v1 written 2026-11-24. Read this block first.

| | |
|---|---|
| State | **v1, buildable.** The grammar is MEASURED on 72 KSI+ thumbnails. The builder works and is tested once (`gta6-npc-organic` test, blue + pink). **His face comes from his own cam frames, no photo shoot (his call, 24 Nov; § 10).** **Watch first (his rule, 24 Nov; § 10b): no thumbnail before the video's cut exists and has been watched; the card is a freeze frame of the interaction, the face is his reaction to that same moment.** GTA 41 (`gta6-npc-organic`): built 24 Nov from the raw after a full silent watch (alligator reel), then CONFIRMED against the edit session's cut the same day: card, face and quote are all frames of the cut (`X:/Claude Projects/GTA 6/thumbnails/gta41-npc/README.md`, `cut-proof.jpg`). **His review (24 Nov): purple background + a frame where he is laughing** → final `gta41-alligator-purple-laugh` (§ 13). |
| Scope | Thumbnails for Afterhours **face-cam reaction / talk videos** (first: `gta6-npc-organic`). Not scripted VO videos, play videos or Shorts. |
| His words (23 Nov) | *"also train yourself on the thumbnails in another session as well"*, after *"I want the style to be exactly in this channel style"* (FEEDBACK.md 2026-11-23). He sent 4 screenshots of 10 KSI+ thumbnails with outlier scores. |
| Evidence | `X:/Claude Projects/GTA 6/research/ksiplus-thumbnails-2026-11-23/`. **`findings.md`** holds every number and its source. `table.md` / `classify.csv` has one row per thumbnail. Also `refs/` + `refs-older/` (72 full-size thumbnails), `refs-from-affan/` and `meas/` (the recovered template, the font match, zooms). |
| Tool | **`X:/Claude Projects/GTA 6/thumbnails/reaction-kit/make_reaction_thumb.py`** (`cutout` / `build job.json` / `compare`). Test job: `reaction-kit/test-npc/` (two `job-*.json` files, outputs, `compare-vs-ksi.jpg`). |
| Gaps | (1) **The test face is a cringe frame** from the 20 Nov pose session (C1489); KSI's are open-mouth laughs. The real one comes from the NPC recording via `pick` (§ 10). (2) The quote speaker in the test is inferred; it was not checked with sound. (3) KSI+'s newest reaction thumbnails (Nov) moved to a different layout, and its biggest specials use a centred face, not the card (§ 0). (4) The sky is procedural, not a photo. (5) Nothing has been tested on HIS channel's CTR yet. |

**Label key:**
- MEASURED: read off pixels by a script, or off full-size 1280×720 frames.
- READ: classified by eye on sheet tiles.
- INFERRED: reasoned.

Px are at **1280×720** (YouTube's size). The builder draws at 2560×1440 and downsamples.

## ★ DEFAULT BUILD (one value per element; change on his note only)

| element | build exactly this |
|---|---|
| layout | **CARD**: his face cut-out on the left over a cloud sky, the clip card on the right on a flat colour |
| canvas | 1280×720 + 1920×1080 jpg, from one 2560×1440 master (Lanczos down, never up), plus a `_notext` copy of both (on GTA 28 he added the text himself) |
| background | sky on the left (the accent mixed 55 % → 96 % toward white, soft clouds, a white glow behind his head; since his GTA 41 note "tone it down just a little" the glow is `sky_glow` 0.24 and the sky tops out at `sky_max` 0.90, KSI measured .35/.96), blending to the **flat accent** by x≈700. The strip under the card's shadow (y696–720) is flat top to bottom and runs ×0.77 at x690 → ×0.99 at x1260 |
| accent | **Purple `#B330FC`**, his pick on GTA 41 (§ 11 #2): KSI+'s own purple, measured #AF2EFA–#B732FF on `3MqnIRIKlOY` (25 Oct, 2.18M). Blue `#0090FF` and pink `#FF2E9A` stay in the builder |
| card | outer **x490–1247, y27–683 (758×657)**, white **11 px** border, outer radius **25 px** (inner 14) |
| card shadow | the card shape, **+12 px straight down**, hard edge, ×0.65 multiply on whatever is under it |
| card picture | ONE freeze frame of the interaction he reacted to, **taken from the video's own cut after watching it** (§ 10b), cover-cropped to 736×635. A two-panel split (8 px white line) when the moment is a before/after. Mild punch: contrast ×1.08, saturation ×1.12, light unsharp |
| his face | cut-out on the left. **Eye midpoint at (304, 285), eye-to-eye 146 px** (YuNet, median of 43 KSI faces). The crown touches or leaves the top edge. Head over the card's border, **body behind the card** |
| expression | **open-mouth laugh / scream** (KSI's 26 of 44). Shock is second (7). Never a ponder face or smirk (§ 6). **Source: a frame of his own recording**, found with `pick` (§ 10) |
| face prep | plain white balance to a neutral-light skin ratio, levels, saturation ×1.04, a 1 px matte pull-in. **No sharpening, micro-contrast or S-curve on his face** (his own rule: a stacked grade "looks AI"). **His cam frame gets a Higgsfield enhance first, then Lanczos DOWN only** (his ask on GTA 41, 24 Nov; § 10, with the identity check) |
| text | ONE real line from the clip in **quotes**: Poppins ExtraBold Italic, cap height **52 px**, fill **`#F4FE05`**, **5 px black stroke** + hard black shadow (+2, +4), ×0.97 horizontal (the builder renders cap 54 so the yellow-fill probe reads 52, as on KSI), 1–2 lines, 2–7 words, in the card's **bottom band** (last baseline y637, centred) or **top band** (first cap top y61, right-aligned at x1224) |
| pointer | a short arc from the quote toward the speaker's mouth: 8 px fill + 5 px black outline, round caps, ≤110 px, stopping ≥30 px short of the mouth. Only when the speaker is on screen |
| second line | optional: a WHITE set-up quote before the yellow punchline (KSI's two-line dialogue) |
| never | the title's words, a logo, a channel name, a border around the whole thumbnail, emoji rain, an arrow + a pointer on one speaker |

---

## 0. What was read (MEASURED / READ)

- **72 KSI+ long-form thumbnails** were read, 1 Apr to 22 Nov 2026, all at full 1280×720 `maxresdefault`. They include all 10 from his screenshots.
- **Three families:**
  - **CARD** (44, median 735K views): the main reaction thumbnail from Apr to Aug (≈43 of ≈47 clip-watching uploads). **His 10 screenshots are all CARD.**
  - **BLEED** (5, median 494K): full-bleed clip with his face huge on one side (4 of 5 on the right). There is no card or accent colour. It uses the same yellow quote + pointer. **Only 7–20 Nov.**
  - **OTHER** (23): staged photo shoots, collabs, collages, centred faces with emoji rain. **At least 6 are clip-reaction uploads with a non-card thumbnail**, among them KSI+'s biggest: Try-Not-To-Laugh specials with a centred face + 😂 rain or a guest (1.88M, 1.58M, 1.07M) and the Most Viewed TikToks group photo (1.04M). The card is the everyday reaction format; the specials get a bespoke shoot.
- **KSI+'s newest reaction uploads use BLEED.** CARD was last used on 25 Oct (2.18M, purple). With 5 young videos, the switch isn't proven to be deliberate, so CARD is the default. BLEED is his call (§ 11 #1).

## 1. The grammar on one card

| | KSI+ CARD (MEASURED unless marked) |
|---|---|
| left 37 % | his head, big: the eyes on the 40 % line, the crown cut by the top edge, the shoulders off the bottom; clean cut-out edge, no outline; a bright cloud sky behind |
| right 59 % | a white-bordered rounded card holding the clip's funniest moment, close enough to read faces |
| colour | one flat saturated accent around the card (blue on 37 of 44), the same hue tinting the sky |
| words | the clip's own funniest line in quotes, yellow with a thick black edge, in the card's top or bottom band, plus a short pointer to whoever said it |
| what never changes | the card's place, size, border, radius and shadow are pixel-identical across thumbnails (one template file: the pixels under the card are byte-identical on three thumbnails) |

## 2. The template (MEASURED; findings § 3)

- **Card outer box:** x490–1247, y27–683 (758×657, aspect 1.154).
  - Median of 42 detections: top 27, bottom 683, right 1247.
  - Left 490 from the clean refs (490 / 492 / 489).
  - Margins: right 32, top 27, bottom 36.
- **Border** 11 px white (10–12). **Corner radius** 25 px outside.
- **Shadow:** a hard band, the card shape shifted 12 px down. It reads #005EA7 on the blue (×0.65) and #1B5E93 over the sky. There is none on the right or the top.
- **Flat accent:** #0090FF top to bottom right of x≈690. The top strip is still sky-light (#8CCCFC) at x500–600.
- **Sky:** soft white clouds on light blue.
  - At x480: #BBDEF8 (top), #F4FBFF (white glow at y240–300, behind his head), #8DC7F5 (bottom).
  - Over x470–700 it blends into the flat colour.
- **Bottom strip** (y696–720, under the shadow band): flat top to bottom, darker toward the left (#0671C3 at x690 ×0.77, #007DDA at x900, #018FFD at x1260).
- **Two-panel split:** the card's inside is cut by an 8 px white line (x864–871), with equal halves.
- **Non-blue cards recolour the whole template, sky included:**
  - magenta #FF3FB9 → sky #FCD6EF
  - violet #D200FF → #F2CBFA
  - orange #E78431 → #F9A55C
  - The builder's sky = `mix(accent, white, t)` reproduces the measured magenta sky within a few levels.

## 3. His face (MEASURED on KSI; findings § 4)

- **Where:**
  - YuNet face box median x84 y126 w349 h432 (p25–p75: w 334–361).
  - **Eye midpoint (304, 285); eye-to-eye 146 px** (133–155).
  - The head's right edge at x≈465–475, so the head stays left of the card's border.
  - The crown is cut 0–60 px by the top edge.
- **Layer order:** KSI's 3/4-turned shoulders only graze the card's lower-left. **Affan's frontal shoulders would cover a third of the card**, so the builder draws his body BEHIND the card and his head OVER it. The head zone is a tombstone around the face box, ±0.72 face-widths, down to the chin.
- **Expression** (CARD, READ):
  - laugh / scream 26
  - shock (wide eyes, open mouth, hands on cheeks) 7
  - spit-take 5 (all on Try-Not-To-Laugh videos)
  - ponder (hand on chin / finger to temple) 4
  - smirk 1
  - The head is turned 3/4 toward the card or looks at the camera, often tilted.
- **Look:** bright, punchy, neutral-to-warm skin, sharp eyes. KSI's are posed photos, far sharper than a cam frame (INFERRED).
- **His prep, in this order:**
  1. Cut-out: `make_reaction_thumb.py cutout` = `npx hyperframes@0.8.16 remove-background` (u2net_human_seg, local, weights already cached).
  2. Check the hair and shoulder edge at full size over blue AND white.
  3. White balance on the skin (G/R→0.80, B/R→0.66, 80 % strength) + levels.
  4. Saturation ×1.04 only. **No sharpening, micro-contrast or S-curve** on his face by default (memory `feedback-thumbnails-proven-formats`, AffanWiz face rules: a stacked grade "looks AI asf"). `face_contrast` / `face_sharpen` exist as job options, off.
  5. A 1 px matte pull-in against the wall-colour fringe.
  6. A Lanczos resize to the eye-to-eye target, from the Higgsfield-enhanced frame (§ 10; his ask, 24 Nov). Other real people's faces: no AI upscaler unless he asks (memory `feedback-sourced-stills-must-be-hq`).
  7. The builder prints the resize factor. **Above ×1.5 at 1920 the face goes soft:** ask for a closer or 4K photo instead.

## 4. The card's picture (READ)

- **What it shows:** the clip's funniest moment, cropped tight on faces or the action. Famous faces win when they are in the clip.
- **The source's own on-screen text stays:** a game subtitle, a news lower-third, a handwritten sign.
- **GTA version:** a face-level frame of the NPC moment, from his OWN capture where possible. An overhead gameplay angle with tiny figures reads weakly at phone size (the test proved it, § 9).
- **Streamer clips:** crop the streamer's face cam, chat, counters and burned-in captions OUT of the card. If a face cam must stay, it stays visible with the streamer's name on it, never blurred (memory `feedback-streamer-facecams-labelled`).
- **Sourced stills:** checked at full size before use (memory `feedback-sourced-stills-must-be-hq`). Nothing graphic: no blood, no bodies.

## 5. The text (MEASURED on 3 refs, READ on the rest; findings § 5)

- **The quote** is the clip's own words, on 24 of 44.
  - Yellow `#F4FE05`, black outline ≈5 px, hard black drop shadow ≈(+2, +4).
  - Cap height 52 px, line pitch 70 px.
  - Title Case or sentence case. ALL CAPS only on a short shout ("TURN IT OFF!").
  - Curly marks (“ ”).
- **Font:** **Poppins ExtraBold Italic**, the closest free match. At KSI's cap height it is 706 px wide on "Bro Forgot To Wipe" vs his 684, so it is squeezed ×0.97. Montserrat is 13–17 % too wide and has a different g.
  - The font file sits in `reaction-kit/fonts/` (OFL).
  - KSI's real font is unknown.
- **Placement:**
  - The bottom band (last baseline y637, centred) or the top band (cap top y61, right-aligned at x1224).
  - Never mid-card. The median of 37 thumbnails shows yellow only at y60–110 and y530–640.
- **Two-line dialogue:** a WHITE set-up quote + a YELLOW punchline quote. It is on 3 of the top 13 (4 of the top 15).
- **Pointer** (15 of 44): a short arc, or a straight stroke, from the quote toward the speaker's mouth, with the quote's fill and a black outline.
- **Used rarely:**
  - asterisk action captions (*SLAPS*): 6
  - curved arrows: 5
  - labels (-1000 AURA, LEAKED): 9
  - a plain caption without marks: 2
  - emoji: 2
  - No text at all: 7.
- **Never the title:** 0 of 44 quotes repeat the title. The only exceptions are 2 series labels.

## 6. What the high performers do differently (CARD, n=44; correlational, small n; findings § 2)

1. **Topic beats the thumbnail.** Try-Not-To-Laugh videos run at a median of 1.24M; everything else runs at 647K. 6 of the top 10 are TNTL.
   - KSI+'s biggest reaction hits include **non-card** thumbnails: TNTL specials with a centred face and emoji rain (1.88M, 1.07M), a centred spit face with a guest (1.58M), a group photo (1.04M). A big special gets its own shoot; the card is the weekly format.
2. **A loud face.**
   - Laugh 790K, shock 638K, spit-take 1.35M (a TNTL device).
   - The 5 quiet faces (ponder / smirk) are all in the bottom half: 354K / 406K.
   - The same holds inside each era, TNTL excluded: Apr–May 873K loud vs 664K quiet; Jun–Oct 479K vs 338K.
3. **The speaker quote with a pointer.**
   - Pointer: median 1.06M (n=15). No pointer: 655K (n=29).
   - Inside eras the gap shrinks (Apr–May 1.06M vs 794K, n=7/11; Jun–Oct 479K vs 466K). It helps a little; it is not the driver.
4. **Two panels** (before/after): median 1.04M (n=11) vs 647K. This is partly TNTL.
5. **The bottom 8** are 3 ponder faces, 3 labels instead of a clip line, and 2 quotes with no pointer.
6. **The month confounds everything.** Apr–May ≈1.03M median vs Jun–Jul ≈450K: KSI+ cooled, so the splits above are hints, not laws.
7. **His screenshot scores agree:**
   - The 3.5x (Hardest TNTL) is a spit-take with a two-panel card.
   - The 1.4x (Celebrity Fan) is a laugh, Drake, and a yellow quote.
   - The 0.9x pair are a smirk and a plain Robot shout.

## 7. Copy vs adapt (it's KSI's brand; Affan's face)

- **Copy exactly:**
  - the CARD layout and every template number in § 2
  - the face zone and eye point
  - the expression rule
  - the quote style, font size, colours, stroke and pointer
  - the bands
  - "a real line from the clip, never the title"
- **Adapt:**
  - his face (his own photo)
  - the body behind the card (his frontal shoulders)
  - our own procedural clouds, never KSI's sky photo
  - Poppins, the closest free match, in place of KSI's unknown font
  - no headphones unless he wants the prop
- **The blue is a performance device, not KSI's brand mark:**
  - 7 of 44 CARD thumbnails use another accent.
  - Non-blue medians: magenta 1.20M (n=2), purple 2.18M (n=1), orange/red 551K–786K.
  - KSI+ itself used near-hot-pink #FF3FB9 ("Sus Streamer Moments", 1.14M).
  - So switching to the channel's hot pink `#FF2E9A` stays inside the grammar. It is still **his one-line decision** (§ 11 #2). Both builds exist in the test folder.

## 8. Rules that still apply

- **Why a non-gaming channel's format:** GTA thumbnails normally copy gaming-niche formats only (memory `feedback-thumbnails-proven-formats`, GTA 28). He named KSI+ himself for this format, and the standing pattern is "when he names one, build it".
- **Beside the talk list's two thumbnail ideas** (`research/npc-organic-2026-11-23/TALK-LIST.md` § THUMBNAILS): concept A (one NPC + a short line) is the card's picture + quote without his face. Concept B (his face right, the couch woman left, an arrow) is close to KSI+'s November BLEED look. For this video, the KSI+ card is the default; A and B stay his alternatives.
- **No hedging in the text:** the quote is said flatly, as the clip says it (memory `feedback-no-hedging-confirmed-facts`).
- **The quote is real and its speaker verified:**
  - Read the line on a frame and hear who says it before the pointer goes on.
  - No invented lines.
  - Censor words per `feedback-censor-sensitive-words`.
- **His face: the Higgsfield enhance he asked for (24 Nov), then an identity check at full size** (§ 10). Other real people's faces stay Lanczos-only unless he asks. Sourced stills are checked at full size.
- **Streamer face cams stay visible and labelled, never blurred.** Crop them out of the card where possible.
- **Spoiler-free and nothing graphic** (the talk list's own rule for this job).
- **Nothing on C:** outputs go in the job's thumbnail folder; the delivered copy goes in `X:\Claude Projects\Exports\`.
- **Work in silence:** frames only, no playback.

## 9. How to build (the tool)

**Step 0: watch the cut first (§ 10b).** The commands below run only after the edit session's files are in and the moment is chosen.

```
cd "X:/Claude Projects/GTA 6/thumbnails/<job>/"
uv run ../reaction-kit/make_reaction_thumb.py pick <synced-camera.mp4> -o frames/  # his laugh / shock frames + frames/sheet.jpg
uv run ../reaction-kit/make_reaction_thumb.py cutout frames/<chosen>.png -o face.png # check the edge at full size
uv run ../reaction-kit/make_reaction_thumb.py build job.json                     # -> <out>_1280x720.jpg + _1920x1080.jpg
uv run ../reaction-kit/make_reaction_thumb.py compare <out>_1280x720.jpg <KSI ref 1> <KSI ref 2> -o compare.jpg
```

**`job.json`** (paths relative to the json):

```
{
  "face": "face.png",
  "face_wb": "skin",
  "panels": [
    {"clip": "still.png", "crop": [x0, y0, x1, y1]}
  ],
  "quotes": [
    {"text": "Line one|line two", "color": "yellow", "band": "bottom", "align": "center",
     "speaker": [x, y], "pointer": "arc", "panel": 0}
  ],
  "accent": "blue",
  "out": "name"
}
```

**Options:**
- **face:** `face_flip`, `face_size` (×, default 1.0), `face_offset` [dx, dy], `body_behind_card` (default true), `head_width`, `chin_margin`, `face_contrast` (1.0), `face_saturation` (1.04), `face_sharpen` (0 = off).
- **notext:** default true (also writes `<out>_notext_*.jpg`).
- **panels:** a second panel = the split. `crop` is in source px and is grown to the panel's aspect.
- **quotes:**
  - a second quote with `"color": "white"` = the set-up line
  - `band`: `top` / `bottom` / a y value
  - `align`: `center` / `right` / `left` / an x value
  - `speaker`: in the clip's SOURCE px
  - `pointer`: `arc` / `straight` / `none`, with `bend` ±
  - `marks`: `curly` / `straight` / `none`
  - `dx` / `dy`
- **emoji:** `[{"char": "😭", "xy": [x, y], "size": 80}]`. This is Windows' flat Segoe set, not KSI's Apple-style 3D, so prefer none.
- **accent:** `purple` / `blue` / `pink` / `magenta` / `violet` / `orange` / any hex.

**What the builder does NOT draw:** caption boxes, curved arrows, the BLEED layout, labels with their own backgrounds. A plain caption, a label or an asterisk line (*SLAPS*) is a quote with `"marks": "none"` and `"pointer": "none"`; arrows and boxes are added by hand if a job needs them.

**The test** (`reaction-kit/test-npc/`):
- His face: C1489 at 211.0 s (20 Nov pose session; eye-to-eye 150 px, so Lanczos ×0.97 at 1280 and ×1.46 at 1920).
- Measured on the output with the same probes as KSI: card border y27–37 / 673–683, x489–500 / 1237–1247; shadow #005CA5 (KSI #005EA7); strip #007AD8 at x900 (KSI #007DDA); eyes (305, 284), eye-to-eye 143; cap 53.
- The card: Kai Cenat's "somebody stole his car" Twitch clip at 8.0 s, from `research/npc-detail-2026-11-20/clips/`. The NPC thief is inside Lucia's car.
- The quote is the game subtitle on that frame: "Hey, hey, stay back!".
- The crop keeps Kai's face cam, chat, counters, minimap, HUD and burned-in captions outside the card.

**Differences left vs KSI** (from `compare-vs-ksi.jpg`):
1. His expression is a cringe, not an open-mouth laugh. No such frame exists on disk; the real one comes from the NPC recording (§ 10).
2. His head is frontal and upright; KSI's is turned 3/4 toward the card and often tilted.
3. The card's picture is an overhead shot with small figures; KSI's are close faces.
4. The quote's speaker (the thief) is inferred, not heard.
5. Our clouds are softer and less defined than KSI's sky photo.
6. At 1920 his face is a ×1.46 Lanczos upscale; KSI's are native photos.
7. KSI wears headphones and a bandana that add head mass. His head reads a little smaller at the same eye-to-eye distance (`face_size` 1.05–1.10 closes it if he wants).

## 10. His face = his own cam frames (his call, 24 Nov 2026: "Use cam frames")

No photo shoot. The face is a frame of the reaction recording itself.

1. **Find the moments:** `make_reaction_thumb.py pick <file> -o frames/`.
   - Run it on the prep's **synced** file (the DJI audio muxed onto the camera picture). His camera's own mic track is often silent (C1489: median −95 dB).
   - It takes his loudest moments (laughs, shouts), 4 s apart, from the audio. The audio is decoded to numbers, never played.
   - At each moment it grabs 3 frames and keeps the one with the biggest, most frontal, sharpest face (YuNet + a Laplacian).
   - On a silent track it falls back to even sampling. A GATED mic (GTA 41's DJI on the camera track: silence between words, median −83 dB, but speech peaks) is NOT silent: since 24 Nov the test is the 95th percentile (< −60 dB = no voice), so its laughs and shouts are found.
   - Out: full-res PNGs + `frames/sheet.jpg`, labelled with the time, the eye-to-eye px and the Lanczos factor at 1280 and 1920.
   - Tested 24 Nov: C1489 (silent track → even sampling, 16 frames, 8 s); C1490 (real audio → 24 loud moments, 12 frames, 32 s).
2. **Choose from the sheet by eye.** The score can't see an open mouth. Pick a big laugh or shock (§ 6), the mouth clear of the mic and hands, frontal or turned toward his left (the card side).
3. Then `cutout` → check the edge at full size → `build` (§ 9).

**Quality:**
- At his usual framing, eye-to-eye is 96–165 px in a 1080 frame (C1489 / C1490), so the face is ×0.9–1.5 at 1280 (fine) and ×1.3–2.3 at 1920 (soft above ×1.5).
- **Enhance the chosen FULL frame in Higgsfield** (`upscale_image` bytedance 4K, 2 credits flat, 1920×1080 → 4096×2304). His ask on GTA 41 (24 Nov): "my face is very low quality ... generate it through Higgsfield ... keep all the detail everything the same".
  - Then compare it with the real frame at 3–4× zoom: moles, teeth / braces, eyes, glasses. Put back anything it changed, from the real frame, feathered (GTA 41: it erased a cheek mole and invented a smeared front tooth; `thumbnails/gta41-npc/watch/hf_fix_353.py`).
  - Run cutout, matte clean-up, mic and hair fixes on the enhanced frame (scripts scale by width / 1920). The face then goes DOWN in the build (×0.57 at 1280, ×0.86 at 1920), never up.
  - When a frame is too soft even so, pick another; the 1280 file is what YouTube shows in the feed.
- **The one blocker:** in C1490's setup the desk mic covers his mouth in every frame, and a cut-out with a mic over the mouth is unusable. The recording ask in `REACTION-STYLE.md` § 13 now says so in one line.
- His coloured set light (pink / purple) is fixed by the skin white balance (the test shows it).

## 10b. Watch the video first (his rule, 24 Nov 2026)

His words (24 Nov, about GTA 41): *"communicate with the editor session to really watch the video because I don't want you to create a thumbnail when you haven't even watched the video and you don't know what the context is ... grab a freeze frame of the interaction as well but grab a freeze frame of me as well ... don't just blindly make the thumbnail"*.

**No thumbnail goes to him before the video's cut has been watched and confirms the moment.** A DRAFT may be built from the raw first, but only after a full silent watch of the raw (every clip as frame sheets + his transcript + the clips' own subtitles); it is labelled a draft until the cut confirms it. The order:

1. **Ask the video's edit session for the cut.** Use `SendMessage` to the session named in the JOBS.md row. Ask for three files it already makes, by path:
   - the camera↔screen offsets;
   - the reel / clip map (screen in/out and crop box per clip);
   - the EDL (`cuts.json`) of what survived.
   Don't ask it for a render. Its RUN.md carries a line saying the thumbnail session is waiting. The files appearing are the signal; a reply may not come.
2. **Watch it, in silence.** Read the transcript of the kept spans, and sample every kept clip as ffmpeg frame sheets (never playback). Note what each clip IS (what the NPC does), where he reacts hardest, and what he says about it.
   - The camera transcript is HIS voice only. It says where he reacted, not what the NPC did or said.
   - GTA 41's tools (copy per job): `thumbnails/gta41-npc/watch/cut_sheet.py` walks the edit's `work/plan.json` on timeline time (the reel with his face box for clip rows, the camera for cam rows); `watch/cut_proof.py` composes the cut's own frames at the card, face and quote moments with the edit's `work/comp.py`, as the proof sent with the thumbnail.
3. **Choose ONE moment that is in the cut:** the interaction he reacted hardest to, and the one a stranger understands in one glance.
   - **The card = a freeze frame of THAT interaction**, from the screen recording. Clean of the platform's UI (handle, caption, buttons, progress bar) and the sharpest frame around the beat.
   - **His face = a freeze frame of his reaction to that same moment.** Camera time = screen time + the edit session's offset; run `pick --from/--to` around it.
   - A sensitive clip the edit blurs (GTA 41: the Cobain clerk) is never the thumbnail.
4. **The quote is a line that is really in the clip:** read off its on-screen text, or confirmed in the clip's own audio. Never invented, never from his transcript unless it is HIS line.
5. **Be ready by the edit's delivery.** He exports within minutes of it.

**A reel as the card source** (GTA 41: Instagram reels in a 2560×1440 OBS capture of Chrome):
- Measure the usable gameplay px of the reel window at full size before choosing. A few hundred px is soft in a 736×635 card.
- A soft source changes the frame or the layout (a two-panel split). It never gets an AI upscale without his OK.
- A streamer face cam inside a reel stays visible (labelled, never blurred), as in the edit.

## 11. His decisions (build the DEFAULT until he answers)

1. **Layout:** the CARD look of his screenshots (Apr–Aug), or KSI+'s November full-bleed look? DEFAULT: **CARD**. (A big special can get its own shoot, as KSI's TNTL specials do.)
2. ~~Accent: blue or pink?~~ **ANSWERED 24 Nov (GTA 41): "make the background purple instead of blue".** Purple `#B330FC` (KSI+'s own, § 7) is the DEFAULT from now until he says otherwise.
3. ~~The thumbnail photo~~ **ANSWERED 24 Nov: cam frames, no shoot** (§ 10). So headphones = whatever he wears on the recording.

## 12. Not proven yet

- Whether this grammar lifts HIS CTR. KSI's numbers are correlational, small-n and confounded by topic and month.
- Whether KSI+'s November BLEED look is a lasting switch (n=5).
- The real thumbnail: GTA 41 is built, confirmed against its cut (§ 10b) and redone after his review (purple, laugh); a paid upscale of the soft game frame is his call.
- KSI's exact font and sky photo. Poppins and procedural clouds are the stand-ins.

## 13. Lessons

Log his review notes of every reaction thumbnail here as *note → change → file*, and in `LESSONS.md`.

**GTA 41, first real build (24 Nov; job folder `X:/Claude Projects/GTA 6/thumbnails/gta41-npc/`, README ▶ STATUS):**
- **A 3/4-profile face fools the auto size.** Eye-to-eye is foreshortened (96 px), so the default drew his head ×1.4 too big. Set `face_size` by eye against KSI's head (0.72 here), with the crown at the top edge and the face clear of the card.
- **His desk mic sits beside his chin in every frame.** It is painted out with a sloped shoulder (`watch/remove_mic.py`; polygon per frame). The chair's ghost in the matte is dropped by keeping the main alpha blob (`watch/clean_alpha.py`).
- **Purple set light + skin WB = blue hair.** Neutralise only dark, blue-leaning pixels in the WB'd space (`watch/hair_neutral.py`); skin untouched.
- **The card picture and the quote can come from the same reel moment.** The gator rears up exactly as the subtitle says it needs a hot dog. Read the reel's subtitles at full size (`watch/band_sheet.py`) before choosing the frame.
- **Tinted glasses:** his eyes read through the tint, but less than KSI's bare eyes. Not a rule; noted for him.
- **Judge the card at FEED size (168×94 and 320×180), not at 1280.** The begging gator (head up, belly to camera) won at 1280 and turned into a brown blob at 168 px; the face-on gator (eyes, teeth) read instantly, and was 3× sharper by Laplacian. Face-on became the build; the begging one is kept as `alt-begging-blue`.
- **The card source can be soft** (a 648 px reel in a screen capture: ×1.47 at 1280, ×2.2 at 1920). Lanczos is the default; a Higgsfield upscale of a GAME frame is allowed by the sourced-stills rule (the Lanczos-only rule is for his real face), but it costs credits, so it is his call.


**GTA 41, his review (24 Nov): "make the background purple instead of blue and pick a frame where im laughing"**
- **Purple, not blue** → added `purple` `#B330FC` to the builder (KSI+'s measured purple) and made it the default (§ 11 #2) → `reaction-kit/make_reaction_thumb.py` `ACCENTS`, job `gta41-npc/job-purple-laugh.json`.
- **A laughing frame, not the shock "Whoa!"** → face = C1498 cam 353.00. It is in the cut (row S023, tl 2:16): he laughs at the hot-dog part, 6 s after the quote line. Picked from dense bursts of every kept span of the reel by eye, then by Laplacian; open mouth, eyes visible through the tint, turned toward the card → `face/face_353.00_hair.png`, `face_size` 0.64, `face_offset` [30, −5].
  - **The expression default in § 3 already said laugh first** (KSI's 26 of 44). I took the shock face because it read clearest; he put the default back. Pick the LAUGH first; shock only when no laugh exists in the moment.
- **The mic paint-out is per frame.** In the laugh frame the mic stands right of his shoulder, so it is cleared to transparent, not painted as shirt (`watch/remove_mic_353.py`). `watch/hair_neutral.py` now takes the frame's WB gains as an argument (printed by `build`).

**GTA 41, his second review (24 Nov): "my face is very low quality ... generate it through Higgsfield ... keep all the detail everything the same"; "zoom my face a bit more ... not a lot of my torso"; "the white flash in the background, tone it down just a little bit"**
- **Face enhanced in Higgsfield** (2 credits) → the full frame went in; at 3–4× it had erased his cheek mole and invented a smeared front tooth, both put back from the real frame → `face/hf/`, `watch/hf_fix_353.py`. The face now goes DOWN in the build (×0.57 / ×0.86), so 1920 is as sharp as the card.
- **More face, less torso** → `face_size` 0.64 → 0.78 (`face_offset` [34, 11]): the crown at the top edge, the ear in frame, the glasses ~25 px clear of the card, the shirt only at the bottom. For his 3/4 cam frames start at 0.78.
- **White glow toned down a little** → new job keys `sky_glow` / `sky_max` in the builder, now defaulting to 0.24 / 0.90 (was .35 / .96).
- **His hand:** in the laugh frame his hand is up by the mic, which falls behind the card, so it can't show. To show a hand, pick a frame where it is near his face (left of x≈490 on the canvas).
