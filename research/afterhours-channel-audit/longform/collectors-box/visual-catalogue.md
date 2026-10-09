# Visual catalogue — "GTA 6 Collector's Box DISAPPOINTED Everyone"

Frame-by-frame dissection of the editing style. Master: `raw/collectors-box.mp4` (the YouTube upload, 2026-09-25,
559 views at audit time) — 1920×1080, 59.94 fps, **6:00.74** (21,623 frames).

Evidence: 25 contact sheets at 2 fps covering every second of the runtime (`frames/sheet_001–025.jpg`, 15 s each, all
read), ~50 full-resolution single frames (`frames/full/`), every-frame strips around the colour-bars insert
(`frames/bars_0108_60fps.jpg`), the shake (`frames/shake_0035_10fps.jpg`), two carousel moves, 3:02–3:08 and the ending
(`frames/end_*.jpg`), and the zoom ladder (`frames/zoom_ladder.jpg`). Structure comes from the creator's own Premiere
timeline (`prproj/Sequence-05.summary.txt`, `agg-collectors-box.txt`); two facts the decoded summary does not carry
were read from the raw project XML (`prproj/ABW8.xml`): the **PiP opacity mask** and the **screen recording's frame
size (2560×1440)**. The automated `probe/`, `zoom.log` and `slowmo.log` outputs were read too, but they misread this
format (see §3a). The export lines up with the timeline to the frame (the colour bars sit at 1:07.95–1:08.15 in
both). Speech is quoted from `transcript/words.json` (WhisperX, 1,239 words; quotes are verbatim ASR, lightly unreliable on names — "Mac of the Gator" = Macca the Gator, "chunky the manly" = Chunkee the Manatee). Anything marked **"looks like"** is an inference.

---

## 1. The face shot

### Framing

One camera, one lock-off, one position for the whole video (`C1302.MP4`, 1920×1080 — looks like a Sony file name;
one continuous take, used from source 0:32 to 15:54). Everything else is done with static Motion scales on razor-cut clips.

- **Base shot (100 %) = medium shot.** Head, shoulders and chest to mid-torso; the red mic sits in front of his
  sternum. Measured on the base frame at 0:01.6: **face centre x ≈ 0.58** (≈1,110 px — a little right of centre),
  **brow-to-chin ≈ 300 px (≈0.28 of frame height)**, **top of hair at y ≈ 0.18** (≈195 px). The neon sign sits
  directly above and behind his head, its middle letters hidden by his hair.
- He shifts in the chair between takes, so the base framing wanders by ±100 px (0:42.5: he leans to frame-left with
  the chair filling the left third; 2:16.5: centred-right). It is never re-centred in post.
- Camera at roughly eye level, normal-to-wide lens (the chair back curves away on the left).
- In the screen-share stretches he is **physically reading his monitor**, so most full-face shots there are a 3/4
  profile looking out of frame-right (1:08–1:59, 2:00–2:05, 4:22–4:29, 4:37–4:58), with glances back to the lens
  on the punchlines.

### The set

- **Back wall, two-tone:** the left third is a warm off-white washed **blush pink/magenta** by an LED (measured
  `#887360` in shade, reads as pale blush on screen); the rest is a **pale sage/mint green** (measured
  `#929C7A`–`#8F9C7E`). Not the lavender wall of Fuel System, not the saturated LED green of RISKIEST.
- **YouTube Silver Play Button plaque** on the left wall, upper-left of frame (x ≈ 520–690, y ≈ 40–295 at base),
  lit with a **pink→violet gradient** (`#E260F7` at the hot spot). Present in every wide face shot; reads as a pink
  square at the top-left edge on the 126–157 % zooms.
- **Neon "skool"** on a clear acrylic backer, centred above his head: `s` cyan-blue (`#7FFFFF` core), `k` orange-red,
  first `o` warm white/cream (`#F2EDB8`), second `o` cyan (`#84F6F6`), `l` orange (`#FF9C44`). On cut zooms ≥ 136 %
  only a coloured band of it survives at the top edge.
- **Chair:** dark oxblood leather armchair (`#3F160E`), bolster cushion, filling the left ~40 % of the lower frame.
- **Right side:** a plant with dark green leaves and pale pink/white blossoms right of his head; a black camera bag
  (Lowepro logo visible) on an orange-topped sideboard; a monitor bezel as a black strip on the far right edge.
- **Mic:** black USB condenser with a **red-lit mesh grille** in a red/black shock mount (HyperX-QuadCast-like),
  lower centre-right. The one saturated warm object in the room, in every face shot.
- **Light:** soft warm key from camera-left/front, even on the face; bright, airy background. Mean frame luma on the
  base shot 0.36 (92/255).

### Wardrobe (identical for the whole 6:00)

- Plain **navy/black crew-neck T-shirt** (`#191418`), no print.
- **Olive/khaki-green translucent square frames with amber/orange tinted lenses**, worn indoors the whole video.
- Dark hair, full dark beard.
- **Steel bracelet watch** on his left wrist (frame-right), visible whenever he gestures.

### Cut zooms — what they look like

48 cut zooms (8.0 per minute): **static scale on a razor-cut clip**, anchor centre (Position 0.5:0.5), no keyframes,
no nests. Median **136 %**, p25–p75 **126–144 %**, min 109, max 180; median hold **1.34 s**. The audio never cuts at
a cut zoom that sits inside a continuous take; the crop just snaps.

Because the face sits right of centre and the scale is centre-anchored, **every zoom pushes the face further right
and up**. Read off `frames/zoom_ladder.jpg`:

| scale | example | what's in frame |
|---|---|---|
| 100 % | 0:01.6 | medium shot: whole neon sign, plaque, chair top, mic, both arms |
| 109–119 % | 1:49.33 (109), 0:29.53 (118), 1:40.22 (119) | a nudge: chair and plaque still in, neon complete |
| 126–136 % | 0:13.78 (126), 2:00.69 (136) | head-and-shoulders; neon cut by the top edge; at 136 % the top of his hair touches the frame edge |
| 144–157 % | 0:52.74 (144), 4:06.01 (150), 3:38.97 (154), 0:02.75 (157) | close-up: forehead to collarbone, the neon reduced to a coloured strip on the top edge, the hand gestures fill the right third |
| 180 % | **4:49.96** | extreme close-up, the only one: top of head cut, chin a little above the bottom edge, face in the right half, the leather chair a brown wall on the left 40 % — the **broken composition** of the video |

- Mostly **in → out** pairs (zoom, then the next clip is 100 %). Two short ladders: **0:29.53 118 → 0:30.66 151**
  and **0:52.74 144 → 0:53.35 118 → 0:57.51 148**.
- **The one reposition:** **2:42.70–2:43.61 (0.92 s), 147 % with Position x 0.268** — he leans right into the lens,
  out of focus, his face fills the whole frame (glasses across the full width, mouth open); the position shift
  re-centres the leaning face. The line: "It's not cool." — then a hard cut straight into the TimTheTatman clip
  saying the opposite.
- **No gradual push anywhere on the face.** The only scale keyframes in the entire edit are on one screenshot
  (0:05.96, 81→86 %).
- Cut zooms keep firing inside the screen-share sections, but **only on the full-face returns** (1:25.85 112,
  1:30.91 136, 1:40.22 119, 1:49.33 109, 3:38.97 154, 4:24.18 144, 4:28.65 144, 5:22.24 125, 5:30.65 127,
  5:44.56 137). **The PiP itself is never zoomed** — it is 46 % in every one of its clips.

### Bugs, lower-thirds, captions

- **Nothing added on top of the picture, ever.** No logo, no watermark, no lower-third, no name strap, no
  burned-in captions, no subscribe animation (the Fuel System bug does not appear in any of the 721 sampled frames),
  no arrows, circles, highlights or callouts on the screen recording.
- Every piece of type that appears is part of a captured web page or a screenshot (§5).

---

## 2. Cold open (0:00 – 0:30)

13 picture changes in 30 s (26/min); minute 1 as a whole has 29. The open is **not** faster than the body
(minutes 4 and 5 have 37 and 36). Music: ES "Loungin – Scientific" at −21 dB from frame 1, **muted under every cut
zoom** (A2 has gaps exactly over 0:02.75–0:04.69, 0:10.38–0:12.28, 0:19.94–0:21.50, 0:27.89–0:30.66).

| # | in – out | dur | on screen | what's said |
|---|---|---|---|---|
| 1 | 0:00.00 – 0:02.75 | 2.75 s | Face, base. **Fades up from black over ~1.1 s** (a black solid on V5, opacity 100→0; mean luma 16 → 45 → 71 → 91 at 0.0 / 0.1 / 0.5 / 1.1 s, then flat). He is sitting back, one hand resting on the mic arm. | "Rockstar just revealed the GTA 6 collector's" |
| 2 | 0:02.75 – 0:04.69 | 1.94 s | **Cut zoom 157 %**, right hand raised beside his face. Music drops out. **Vine boom at 0:04.29** (−11 dB, the loudest SFX in the video) in the pause after "$400.", on the tail of the zoom. | "box. $400." |
| 3 | 0:04.69 – 0:05.96 | 1.27 s | Face, base, both hands out flat ("spread"). | "The game is not in it." |
| 4 | 0:05.96 – 0:08.24 | 2.29 s | **Screenshot** — the Rockstar Store product gallery: a vertical thumbnail rail (white outline on the first) and the black **Vice City Leonida "VI" box** on a magenta gradient. 1320×1179 px source, **centred on pure black, 81 → 86 %** (≈1,069×955 → 1,135×1,014 px), a slow push (2.2 %/s) — the only push in the video. | "And honestly, that's not even my problem with it" |
| 5 | 0:08.24 – 0:10.38 | 2.14 s | Face, base, fingers interlaced/spread. | "because they called it the collector's box," |
| 6 | 0:10.38 – 0:12.28 | 1.90 s | Cut zoom 146 %, looking down, hands working. | "right? That's exactly what they did" |
| 7 | 0:12.28 – 0:13.78 | 1.50 s | Face, base. | "back in the Red Dead days as well." |
| 8 | 0:13.78 – 0:15.97 | 2.19 s | Cut zoom 126 %, hand to the side of his face. | "My problem is what they did put in it." |
| 9 | 0:15.97 – 0:20.34 | 4.37 s | Face, base, one jump cut at 0:17.58. | "Because I went through every single item and for $400, this box is" |
| 10 | 0:20.34 – 0:21.50 | 1.17 s | Cut zoom 126 %. | "mostly useless." |
| 11 | 0:21.50 – 0:27.89 | 6.39 s | **Screenshot of the store's hero banner + the first face PiP (top-left).** The banner (2481×1194 px at 100 %, so it overfills the frame and is cropped ~280 px each side): Vice City / Leonida comic-panel collage left, *The Goodtime State* script logotype, "VICE CITY COLLECTION" kicker and a three-line blurb right, on deep navy. The face PiP sits over the top-left of the collage (§3b). He is **reading the banner's blurb aloud** ("Quote, …"), so the screenshot is the evidence for the quote — no card is built for it. | "This is how Rockstar describes it. Quote, a premium Grand Theft Auto 6 collectible set featuring all the essentials for a good time." |
| 12 | 0:27.89 – 0:29.53 | 1.63 s | Face, base — he repeats the quoted phrase to camera (the repeat is kept in the cut, as emphasis). | "all the essentials for a good time." |
| 13 | 0:29.53 – 0:30.66 | 1.13 s | Cut zoom 118 %, then straight into **151 %** at 0:30.66 (the first ladder). | "Remember that sentence." |

**No title card, no logo sting, no channel branding.** The first frame is his face fading up; the first insert lands
at 5.96 s.

---

## 3. Every non-face layer, in order

### 3a. How the picture is built (time shares, from the timeline, checked against the frames)

| what the viewer sees | time | share |
|---|---|---|
| full-frame face | 232.3 s | 64.4 % |
| **screen recording + face PiP top-right** | 83.0 s | 23.0 % |
| **screen recording + face PiP top-left** | 27.3 s | 7.6 % |
| screenshot + face PiP top-left | 6.4 s | 1.8 % |
| YouTube clip (TimTheTatman VOD) in a black-bordered window | 6.0 s | 1.7 % |
| screenshots on black, no PiP | 5.6 s | 1.6 % |
| colour bars | 0.2 s | 0.1 % |

- **His face is on screen 96.7 % of the runtime** (full or PiP). The screen recording is **never** shown without
  the PiP.
- 191 visible picture changes = **31.8 per minute**; median shot 1.79 s; longest unbroken shot 8.43 s (2:06.14, the
  sunglasses page with PiP). Per minute: 29 / 32 / 26 / 37 / 36 / 31.
- **No game footage at all.** The B-roll is the Rockstar Store page captured live, five screenshots, one clip of
  another creator's stream, and a test card.
- **Warning on the automated probe** (`probe/summary.md`, run on this master): it reports "face 99 % of runtime in 4
  runs, 3 overlays, 120 cut zooms in, median step ×1.356, hold 0.4 s, 150 cuts = 24.9/min". The face detector counts
  the 46 % PiP as the face, so every screen-share run is read as "face", and head movement inside the small PiP is
  read as scale steps. Its cut count (hard picture cuts only) is usable; its face share, overlay count and cut-zoom
  count are not, for this format. The figures in this catalogue come from the timeline plus the frames. (Its luma:
  mean 0.328; the 2 fps sweep here gives 0.345, <1 % of frames dark, none above 0.5.) Likewise `slowmo.log` lists
  76 "slowed/still runs" — almost all are static web pages and screenshots (a still page duplicates frames); the
  timeline has exactly **one** speed change (5:46.06, 0.1×). `zoom.log` (26 steps in, median ×1.27) undercounts the
  48 cut zooms in the timeline.

### 3b. The screen-share + face-PiP format (new for this channel)

**What the screen recording is.** An OBS capture (`2026-09-25 09-57-16.mp4`) of his own browser on the Rockstar Store
"Grand Theft Auto VI: The Goodtime State – Vice City Collection" page, and later a Google Images search. The file is
**2560×1440, 60 fps** (project XML), placed in the 1080p sequence at **100 %, not scaled to frame** — so the edit
shows only the **centre 1920×1080 (75 %)** of his monitor. That crop is why **no browser chrome ever appears**: no
tabs, no address bar, no bookmarks, no taskbar. The store page is a dark-navy horizontal carousel (one product per
slide: a big render on the left, condensed all-caps headline + body copy on the right), so the 100 % crop fills the
frame like a designed product card.

- **Cursor visible** throughout (arrow, I-beam over the copy, a pointing hand on Google Images) — never hidden,
  never highlighted, no click rings, no zoom-follow. He parks it near the text he is reading (I-beam on "debossed"
  at 3:46.5, on "of" at 1:11).
- **Navigation happens inside the recording:** the site's own horizontal slide animation carries the product changes
  (1:19.1 Macca → hat, 1:51.4 hat → sunglasses, 4:16 stickers → poster, 4:19.6 poster → pins); at 4:02.48–4:05.18
  three quick cuts catch the carousel **sliding backwards** (keychain/mirror overlapping → mirror → sunglasses) as he
  scrolls back. Once (3:05.2) the recording itself navigates to the product page showing the blue
  **"This product is not available in your region."** notice.
- **Sync:** the voice is the OBS file's own audio, and every face clip is locked to it at a fixed 20.35 s offset, so
  **the PiP is the live take recorded while he browsed** (he is looking at his monitor, frame-right). A screen clip
  in true sync would also sit at 20.35 s; most sit within ±1.3 s of that (19.1–20.8 s), i.e. the screen picture is
  nudged a little to land the right slide on the right word, and in places it is cut loose entirely: 2:22.44 reuses
  the 2:06.14 screen in-point (sunglasses held), 2:35.52 is 14.8 s, the 5:13 Google Images clip and the 5:46 freeze
  come from other parts of the recording.

**PiP geometry (identical in every PiP clip).** Motion **scale 46 %** (883×497 px), Position **(0.864, 0.164)**
top-right or **(0.049, 0.164)** top-left, plus an **Opacity rectangle mask** that the decoded summary drops — read
from the XML: source x **0.375–0.828**, y **0.146–0.927**, **feather 10**, opacity 100, expansion 0. Net result:

| corner | visible window on the 1920×1080 frame | notes |
|---|---|---|
| **top-right** | x **1548 → 1920**, y **≈2 → 390** → **≈372×388 px** | the mask runs ~28 px past the right edge, so the window is flush to the right edge and top edge; only the left and bottom edges are inside the frame |
| **top-left** | x **0 → 384**, y **≈2 → 390** → **≈384×388 px** | mask runs ~16 px past the left edge; flush to the left and top edges |

- A **near-square (~1:1) window, ~20 % of frame width, ~36 % of frame height, jammed into the corner** — not a
  16:9 inset, not floating with a margin.
- **No border, no stroke, no drop shadow, no rounded corners, no glow.** The two inner edges are slightly soft
  (the 10 px mask feather — measured as an ~8 px luminance ramp at the bottom edge); at viewing size it reads as a
  plain hard-edged rectangle cut out of the camera frame.
- **What's inside the window:** a fixed crop of the base shot — the neon "SK" in its top-left corner, his head and
  shoulders (face ~140 px tall), the red mic at the bottom, a sliver of chair on the left. The plaque and most of the
  chair are masked out.
- **The PiP never moves, scales, fades or animates.** It cuts on and off with hard cuts only. It has jump cuts inside
  it (the face clip is razor-cut with the screen clip; e.g. 5:13.63 / 5:16.72 / 5:18.69 — a 0.40 s PiP clip).
- **Corner choice looks like "keep the page's text clear":** top-right on the store carousel (product copy sits
  below y ≈ 390 on the right; the PiP occasionally kisses the headline, e.g. at 2:55 "LEONIDA KEYS" starts a few px
  below the window); top-left on the hero banner (its text is on the right) and on Google Images (its close button and
  header sit top-right).

**How the edit moves between full face and screen share.** The screen recording runs continuously on a lower track
(V1 in block A, V3 in blocks B–C, V2 in block D) and the face clip on the track above **toggles between 100 %
(covers the screen entirely) and the 46 % masked PiP** at each cut. So:

- every change is a **hard cut**, no transition; the screen has kept rolling underneath when it comes back;
- full-face returns are where the punchlines and cut zooms go (e.g. 1:22.50–1:42.54 is a 20 s full-face stretch
  with three cut zooms while the store page sits underneath unseen);
- typical PiP run **≈4.2 s median** (2.0–10.9 s), typical full-face return 1–5 s;
- the first entry into screen-share is announced by the **0.2 s colour-bars insert** (1:07.95); later entries are
  plain hard cuts.

**Zooms on the screen recording** (cut zooms, not pushes — the same razor-and-scale move as the face):

| at | scale / position | what it does |
|---|---|---|
| 2:53.57 – 2:56.11 | 123 % | crossbody-bag slide enlarged; headline "LEONIDA KEYS CROSSBODY BAG" in pink, the body copy runs off the right edge ("…YKK zipper pull." touches x = 1920) |
| 3:46.11 – 3:48.23 | **168 %**, x 0.255 | punch into the swizzle-spoon copy: "VICE CITY / COLLECTIBLE / SWIZZLE SPOON" fills the left-centre of frame, the spoon handle cut diagonal top-left; Vine boom at 3:48.09, cut to face at 3:48.23 |
| 3:56.42 – 3:57.45 | 143 % | shot-glass slide: the glass fills the left half, "CHUNKEE THE / MANATEE SHOT GLA…" runs off the right edge |
| 5:13.63 – 5:46.06 | **186 %**, x −0.178 | Google Images preview panel blown up to fill the frame: "YouTube · IGN · 3:20" header, ‹ › ⋮ ✕ controls, the IGN thumbnail of the **GTA V Collector's Edition** box (steelbook, blueprint map, Los Santos cap, deposit bag, "DIGITAL CONTENT" stamps), a Google Lens button, "1,280 × 720" label, hand cursor. Visibly soft (looks like a 1,280×720 preview enlarged twice — by the browser panel, then by the 186 %). A 32.4 s clip, seen in three PiP runs with full-face returns between. |
| 5:46.06 – 5:52.12 | 124 %, x 1.005, **speed 0.1×** | the store gallery's VI box image as a **near-freeze** (0.6 s of source over 6 s; only the cursor steps); the recording's left edge lands at x ≈ 342, so the frame-left strip below the PiP is uncovered black |

### 3c. Master table

"PiP-TR / PiP-TL" = screen recording full frame + face PiP in that corner. Durations are the visible run.

| # | in – out | dur | what it is | framing / treatment | what's said |
|---|---|---|---|---|---|
| 1 | 0:00.00 – ~0:01.1 | 1.1 s | black solid fading out | fade from black over the first face shot | "Rockstar just revealed" |
| 2 | 0:05.96 – 0:08.24 | 2.29 s | screenshot: store gallery (thumbnail rail + VI box) | centred on black, 81→86 % push | "And honestly, that's not even my problem with it" |
| 3 | 0:21.50 – 0:27.89 | 6.39 s | screenshot: "The Goodtime State / Vice City Collection" hero banner | 100 %, overfills frame (cropped L/R); **PiP-TL** | "This is how Rockstar describes it. Quote, a premium Grand Theft Auto 6 collectible set featuring all the essentials for a good time." |
| 4 | 0:39.76 – 0:41.16 | 1.40 s | screenshot: the VI box product photo (1000×683) | 100 %, centred on black (x 460–1460, y 198–881), static | "It's a collector's box." |
| 5 | 0:58.81 – 0:59.73 | 0.92 s | screenshot: GTA VI standard cover art (727×883) | 100 %, centred on black, static | "you have the standard the" |
| 6 | 0:59.73 – 1:00.74 | 1.02 s | screenshot: GTA VI **Ultimate Edition** cover (747×917) | 100 %, centred on black, static — a two-step flip, standard → ultimate | "ultimate and then you" |
| 7 | 1:07.95 – 1:08.15 | 0.20 s | **SMPTE colour bars** (12 frames) + sine tone | full frame, hard cut in and out, off a 135 % cut zoom | "in the box so" |
| 8 | 1:08.15 – 1:10.87 | 2.72 s | (screen starts underneath, covered by full face looking at his monitor) | face 100 % | "so we have 11 items i'm gonna be honest about every single one" |
| 9 | 1:10.87 – 1:12.92 | 2.05 s | store: **MACCA THE GATOR FIGURE** | PiP-TR | "first we've got this mecha the gator figure" |
| 10 | 1:14.67 – 1:17.91 | 3.24 s | store: Macca figure | PiP-TR (face jump cut 1:16.73) | "this is good it's a cool figurine uh he's smoking a blunt" |
| 11 | 1:19.06 – 1:22.50 | 3.43 s | carousel slides Macca → **NEW ERA 9FORTY SNAPBACK HAT** | PiP-TR | "then we have this cap i guess it looks cool right" |
| 12 | 1:42.54 – 1:46.49 | 3.95 s | store: snapback hat | PiP-TR | "my problem with this cap is like you have to wear it to show it off and" |
| 13 | 1:51.38 – 1:57.25 | 5.88 s | carousel slides hat → **OAKLEY FROGSKINS SUNGLASSES** | PiP-TR; **Vine boom 1:53.05** (−15 dB) | "then we have the oakley frog skins Okay, so this is the biggest problem, right? In this collector's box. By far." |
| 14 | 2:06.14 – 2:14.57 | 8.43 s | store: sunglasses (held) | PiP-TR — longest shot in the video | "up $160, by the way, of this whole price point. The $400 price point. Imagine what else you guys could have gotten with this." |
| 15 | 2:22.44 – 2:25.36 | 2.92 s | store: sunglasses (same screen in-point as #14) | PiP-TR | "Wearing these damn sunglasses doesn't show that." |
| 16 | 2:35.52 – 2:40.18 | 4.66 s | store: sunglasses | PiP-TR, 3 clips | "40% of the price point went into this pair of sunglasses. I do not agree with this." |
| 17 | 2:42.70 – 2:43.61 | 0.92 s | (face lean-in, 147 % repositioned) | §1 | "It's not cool." |
| 18 | 2:43.61 – 2:49.60 | 5.99 s | **YouTube clip — TimTheTatman stream VOD** ("THE NEW $400 GTA 6 COLLECTOR BOX…"): the store page with **$399.99**, "COMING SOON", Pre-Order Now, the full "Collection includes" list, his chat and his facecam with a "TOP DONATION" label | scale **84 %** → a 1,613×907 window centred on black (153 px L/R, 86 px top/bottom borders), clip audio up; no PiP of Affan | "Oh, these are actual Vice City Oakleys. Yo, am I crazy that this may be worth it, chat? I'm actually intrigued." |
| 19 | 2:53.57 – 3:00.16 | 6.59 s | store: **LEONIDA KEYS CROSSBODY BAG** | PiP-TR; first 2.54 s at 123 % | "Leonida Keys cross body bag. Again, not a good addition. It looks cool. No, not a collector's edition thing." |
| 20 | 3:03.23 – 3:07.72 | 4.49 s | crossbody bag → at 3:05.2 the recording navigates to the product page: VI box + "**This product is not available in your region.**" | PiP-TR (on V5) | "not that black box, this box, right? If we had a pink case" |
| 21 | 3:19.27 – 3:22.00 | 2.74 s | store: **MACCA THE GATOR MAGNETIC MIRROR** | PiP-TR; **Vine boom 3:19.63** | "A mirror, a Mac of the Gator, magnetic," |
| 22 | 3:25.57 – 3:28.78 | 3.21 s | store: mirror | PiP-TR | "If you're paying 400 clamorous," |
| 23 | 3:31.54 – 3:34.26 | 2.72 s | store: mirror | PiP-TR | "a good, you know, money spent decision." |
| 24 | 3:35.33 – 3:37.53 | 2.21 s | store: **VICE CITY RAZOR BLADE KEYCHAIN** | PiP-TR | "then we have this razor blade keychain" |
| 25 | 3:44.54 – 3:48.23 | 3.69 s | store: **VICE CITY COLLECTIBLE SWIZZLE SPOON** | PiP-TR; 3:46.11 punch to **168 %** on the copy; **Vine boom 3:48.09** | "looks like a spoon vice city collectible swizzle spoon" |
| 26 | 3:50.01 – 3:52.43 | 2.42 s | store: swizzle spoon | PiP-TR | "i genuinely thought that that was a coke" |
| 27 | 3:54.30 – 4:05.18 | 10.87 s | **CHUNKEE THE MANATEE SHOT GLASS** (143 % at 3:56.42) → spoon (4:00.84) → carousel sliding back, keychain/mirror (4:02.48) → mirror → sunglasses (4:03.26) | PiP-TR, 7 clips | "chunky the manly shot glass a shot glass imagine if we remove that you know if we extracted the price of this in this the mirror and the Oakley sunglasses" |
| 28 | 4:14.74 – 4:21.96 | 7.22 s | **LEONIDA KEYS STICKER PACK IN STASH BAG** → **DOUBLE-SIDED SOUVENIR POSTER WITH MAP OF LEONIDA** (4:16.76) → **LEONIDA KEYS ENAMEL PIN SET IN METAL TIN** (4:19.66) | PiP-TR | "sticker pack I guess that's fine map is very cool I like the map, map is nice. And then we have this metal pin set. So" |
| 29 | 4:29.75 – 4:32.02 | 2.27 s | store: crossbody bag again | PiP-TR (a callback to #19) | "even this cross body bag, if I'm being honest." |
| 30 | 5:13.63 – 5:19.09 | 5.46 s | **Google Images — IGN thumbnail of the GTA V Collector's Edition** | 186 %, **PiP-TL** | "and let's look at the GTA 5 collector's edition what they offered us blueprint map very nice tap" |
| 31 | 5:24.32 – 5:29.35 | 5.02 s | same | 186 %, PiP-TL | "you've got you got the the big box the big black box the exclusive artwork steelbook" |
| 32 | 5:31.55 – 5:42.29 | 10.75 s | same | 186 %, PiP-TL (5 PiP clips, one 0.57 s) | "uh you have the security deposit bag the key there as well and then you got stun plane trials the digital content outfits custom characters special ability boost i believe it was like 25 but yeah like" |
| 33 | 5:46.06 – 5:52.12 | 6.06 s | store gallery: the VI box, **0.1× near-freeze** | 124 %, PiP-TL | "If this box costed $250, right? Adjusting with inflation. It shouldn't go up like, okay, $270." |

### 3d. Screenshots — treatment

- **Native pixel size, centred on pure black, no frame, no shadow, no blur plate** (#2, #4, #5, #6). Only #2 moves
  (81→86 %); the rest are dead still. Durations 0.9–2.3 s. #5→#6 is a back-to-back flip (standard cover → Ultimate
  Edition cover) with no gap.
- The wide hero banner (#3) is the exception: 100 % of a 2481 px-wide grab, so it overfills and reads as full-bleed,
  and it carries the PiP.
- They are raw Windows Snipping Tool grabs (`Screenshot 2026-09-25 …png`) — soft where they were small, uncleaned.

---

## 4. Recurring patterns and comedy/emphasis devices

| device | what it is | where | the line it lands on |
|---|---|---|---|
| **Vine boom in the pause after the key noun** | the boom's transient sits at the clip head (in-point 0.30 s); it is dropped into the breath right after the word that carries the joke, usually on or a beat before a hard cut | **0:04.29** (−11 dB) in the pause after "$400." on the 157 % zoom, cut to base 0.4 s later · **1:53.05** (−15) on "Okay," after "oakley frog skins", sunglasses in the PiP · **3:19.63** (−12) right after "A mirror," 0.36 s into the mirror slide · **3:48.09** (−12) right after "…swizzle spoon", 0.14 s before the cut from the 168 % punch to the face · **4:51.16** (−12) on "come on", exactly on the cut out of the 180 % ECU | 0:04 "box. $400. The" · 1:53 "we have the oakley frog skins Okay, so this is the" · 3:19 "look at this now. A mirror, a Mac of the" · 3:48 "spoon vice city collectible swizzle spoon" · 4:51 "a magnetic mirror come on" |
| **Bass-boost + shake on the mocked reaction** | Sapphire **S_Shake** (amp 1, freq 73, stillness 0.7) on a 133 % face clip for the whole 2.65 s, with heavy directional motion blur — most frames are a smear, a sharp frame every ~0.4–0.5 s; no black edges show (looks like the 133 % gives the overscan). "Bass boosted sound effect" at −27 dB, music muted. It plays under him **imitating the internet's outrage** | **0:34.98 – 0:37.64** | "on social media that, oh, the game is not in it. Oh my God." |
| **Word-synced flip** | two cover screenshots cut exactly on the edition names | standard cover at 0:58.81 ("standard" 0:59.18), Ultimate cover at 0:59.73 ("ultimate" 0:59.80) | "right you have the standard the ultimate and then you have" |
| **Channel-change test card** | 12 frames of SMPTE bars + sine tone, hard in/out, in the gap between two sentences | **1:07.95**, the hinge from the cold-open argument into the item-by-item screen-share | "things man in the box so we have 11 items" |
| **Lean-in → someone else's stream** | he lunges at the lens on "It's not cool." (147 %, re-centred, out of focus) then hard cut to TimTheTatman saying the opposite on the same store page | **2:42.70 → 2:43.61** | "Tim the Tatman's video. He saw it was cool. It's not cool. Oh, these are actual Vice City Oakleys." |
| **The 180 % ECU** | the tightest crop of the video, face shoved right, chair filling the left, on the most absurd item; Vine boom on the cut out | **4:49.96 – 4:51.16** | "a magnetic mirror" |
| **Punch into the page copy** | a 168 % / 143 % / 123 % cut zoom on the store page so the product name is huge while he reads it out | 3:46.11 ("vice city collectible swizzle spoon"), 3:56.42 ("a shot glass"), 2:53.57 | 3:46 "vice city collectible swizzle spoon" · 3:56 "a shot glass" |
| **The carousel acts the list** | three 0.8–1.9 s screen clips catch the carousel sliding back to each item as he names it | 4:02.48 mirror ("the mirror" 4:02.82), 4:03.26 sunglasses ("Oakley" 4:03.94) | "in this the mirror and the Oakley sunglasses" |
| **Muted words** | a word is cut out of the voice track (A1 gaps, 0.17–0.45 s), the picture runs straight through it, **no bleep tone**; music plays through the hole if a bed is running, otherwise it is digital silence. Looks like swear censoring | 3:22.52 "what the [—] is going on?" · 3:45.09 "this looks like a [—] spoon" · 3:51.95 (clips the end of "coke") · 4:01.61 "in this [—] the mirror" · 4:25.57 "a [—] spoon" | — |
| **The near-freeze** | 6 s of the box image at 0.1× under the closing price argument | 5:46.06 – 5:52.12 | "If this box costed $250, right? Adjusting with inflation. It shouldn't go up like, okay, $270." |
| **Callback** | the crossbody bag slide returns 1.5 min after its first showing, as he lists the items he'd cut | 4:29.75 | "and even this cross body bag, if I'm being honest. And" |
| **Zoom ladders** | consecutive cut zooms without a 100 % in between | 0:29.53 118 → 151; 0:52.74 144 → 118 → 148 | "problems with it because when you call it gta 6 collector's edition now it's in the game in the game line right" |
| **Music drop on the punch** | the music bed is razored out under almost every cut zoom and SFX hit (A2/A4 gaps line up with 0:02.75, 0:10.38, 0:34.98, 0:46.60, 0:57.51, 1:25.85, 1:53.05, 3:03.23, 3:12.86, 3:19.27, 3:30.31, 3:56.42, 4:34.72, 4:49.96, 5:29.35) — the voice lands dry | throughout | — |

Not present: no slow-down on the face, no meme clip, no reaction GIF, no subscribe bug, no captions, no cards.

**Where the voice comes from:** A1 is `2026-09-25 09-57-16 Audio Extracted.wav` (162 clips) — the **OBS recording's own
audio track**, not the camera's. Camera and OBS ran together for the whole session; the voice edit follows the OBS
file and **every one of the 180 face clips is locked to it at the same 20.35 s offset** (lip sync is never broken).
The screen *picture* is the only thing that gets slipped (§3b).

---

## 5. Palette and type

**The editor adds no type at all.** Everything legible on screen is captured:

- **Rockstar Store carousel** (the dominant non-face look, ~31 % of runtime): background a deep navy/indigo gradient
  (`#111123` → `#23223E`, lighter toward the top-left). Headlines in a **tall condensed grotesque, all caps** (Bebas /
  Druk-condensed class), two to three lines, each product in its own tint: Macca figure peach `#F7C592`, crossbody
  bag pink `#EF8BB2`, sunglasses and spoon pale lime `#E0F992`, keychain and poster lavender `#D79FF7`, sticker
  pack pink `#F694B1`, pin set salmon `#F6AA9B`, shot glass peach. Body copy in a rounded geometric sans,
  sentence case, a paler tint of the same hue (`#DCB3C6` under Macca, `#B7AEDB` under the bag).
- **Hero banner:** *The Goodtime State* in a white connected script with a pink outline (`#FBF9FB` fill), kicker
  "VICE CITY COLLECTION" in widely letterspaced pink caps `#EC8FB1`, blurb lavender `#DAC4F3`.
- **Gallery / box shots:** magenta gradient `#420F33` (dark corner) → `#D9569C` (hot corner), the black box with
  the white "VI" palm logo.
- **Rockstar Store product page / TimTheTatman clip:** black page, white Inter-like sans ("Grand Theft Auto VI: The
  Goodtime State – Vice City Collection", "$399.99"), pill buttons, a pink "COMING SOON" tag; the region notice is a
  blue bar `#254B7C` with white text.
- **Google Images:** dark-grey Google UI, white Roboto, the cream/green dollar-bill art of the GTA V Collector's
  Edition.
- **Colour bars:** standard SMPTE (white, yellow, cyan, green, magenta, red, blue; PLUGE row).

The video's overall palette is therefore **two worlds hard-cut against each other**: the bright, warm room (sage
`#929C7A`, blush, cyan/orange neon, oxblood chair, red mic) and the dark navy + hot-pink/magenta Vice City store.

---

## 6. Ending (last 15 s: 5:45.7 – 6:00.74)

| in – out | on screen | what's said |
|---|---|---|
| 5:44.56 – 5:46.06 | Face, cut zoom 137 %, one palm up, wincing. | "is good. This is nice, right?" |
| 5:46.06 – 5:52.12 | Store gallery VI box at 0.1× (near-still), **PiP-TL**; he gestures in the PiP. Music (Take a Ride, −27 dB) ends at 5:52.12. | "If this box costed $250, right? Adjusting with inflation. It shouldn't go up like, okay, $270." |
| 5:52.12 – 5:54.29 | Face, base, palm up, then a wide-open-mouth mugging face with a hand behind his head (5:53.0) — music is gone; **the last 8.6 s are dry voice.** | "And this is the box. I wouldn't have" |
| 5:54.29 – 5:55.17 | Cut zoom 111 %, hand raised beside his face. | "no problem with" |
| 5:55.17 – 5:57.47 | Face, base, palms pressed/rubbed together. | "it. The only problem is that this costs $400. So" |
| 5:57.47 – 5:59.59 | Face, base (jump cut), talking to the lens, hands low. | "yeah, I just wanted to yap about this." |
| 5:59.59 – 6:00.74 | **Cut zoom 129 %, cut exactly on "Make"** (5:59.62); he throws a **thumbs-up** on "sure to subscribe" (5:59.8–6:00.3), drops it, and holds a flat look into the lens for the last ~0.3 s. The only call to action in the video is this spoken line. **Last frame is his face — hard cut to end, no fade, no end card, no subscribe ask on screen, no space left for end-screen elements.** | "Make sure to subscribe." |

---

## 7. What differs from the face-cam preset (`presets/youtube/affan-afterhours-facecam/README.md`)

1. **The main overlay is a screen share with a face PiP — the preset says "Nothing is ever an inset, a PiP or a split
   screen."** Here 116.7 s (32 %) of the runtime is a browser capture or screenshot with a ~372×388 px corner PiP
   (scale 46 %, rectangle opacity mask, feather 10, no border/shadow), cut on/off by toggling the face clip between
   100 % and 46 %.
2. **Face visibility is higher, not lower:** full face 64 % (preset ~80 %), but face visible full-or-PiP **96.7 %**.
   There is no stretch at all without his face except screenshots/YT clip/bars (≈12 s total).
3. **No game footage.** The preset's "game footage is the main overlay … ~4 s, 3–4 runs a minute" does not apply. The
   B-roll is the store page (live capture), screenshots, another streamer's VOD, a test card.
4. **No cards / posters / typeset sentences** (preset 1–1.6 per minute). The store page's own product typography
   does the job a card would (big condensed caps on dark navy), and it is never re-typeset.
5. **No gradual push on the face** (preset ~1 %/s on a nest). No nests either. Cut zooms are static scales on
   razor-cut clips.
6. **Bigger and more frequent cut zooms:** 8.0/min (preset ~5), median **136 %** (preset +25–27 %), p25–p75
   126–144 %, up to 180 %; median hold 1.34 s (preset ~1 s). Two zoom ladders.
7. **Cut zooms on the B-roll too:** 123 %, 143 %, 168 % and 186 % punches on the screen recording.
8. **Faster overall, flat open:** 31.8 visible changes/min (preset ~20–25), but the cold open is *not* faster than
   the body (29 changes in minute 1 vs 37 in minute 4); the preset's 1.5–2.5× opening burst is absent.
9. **New emphasis devices:** Sapphire S_Shake + bass-boost SFX under a mocked reaction (0:34.98), the 12-frame
   colour-bars "channel change" (1:07.95), a lean-in into a hard cut to another creator's stream (2:42.70), a 0.1×
   near-freeze on a still web image (5:46), screenshots cut on the exact word (0:58.81/0:59.73), and **muted words**
   (five 0.17–0.45 s holes cut out of the voice, no bleep, picture uninterrupted — looks like swear censoring). The
   Vine boom is used ×5, always in the breath right after the key noun (the preset README names no SFX).
10. **Music behaviour:** three ES tracks at −21/−24/−27 dB, **cut out under nearly every cut zoom and SFX hit**, and
    stopped for the last 8.6 s — not a flat continuous bed.
11. **Opening:** a ~1.1 s fade up from black (preset: "first frame is his face", cut in hard). Still no title card,
    logo or branding.
12. **Screenshots on black at native size**, mostly static, 0.9–2.3 s (preset: found artefacts full-frame with a slow
    scale, 1.8–2.6 s). One raw clip of another creator shown windowed at 84 % on black.
13. **No subscribe animation** (Fuel System had two). No slow-down on the face (preset: 1–2 per video).
14. **Set & wardrobe deltas:** two-tone sage/blush wall (not lavender `#D299F4` or LED green `#5BAC5D`); a YouTube
    Silver Play Button plaque on the wall; the neon sits directly above his head; olive-green frames with amber lenses;
    steel bracelet watch; red-grille HyperX-style mic on a shock mount, no spatula prop.
15. **Same as the preset:** no captions, no lower-thirds, no logo bug, no end screen, ends cold on the face (with a
    cut zoom and a thumbs-up), screenshots unannotated, inserts on hard cuts only.
