# Batch 2 style research: the "expensive" Instagram look (2026-10-12)

Affan's direction for the next 4 Instagram-look samples (2026-10-12, condensed): *minimalistic, big black bars (Instagram
prefers that cinematic look), caption animations (Scott D. Clary's channel has ideas), a minimal video but with a LOT of
refined, premium, high-quality motion graphics, more and more refined than before, clean crisp sound effects, it should look
like an expensive video.* Standing rule: never lock one style; every video beats the last one.

**Method.** Reel IDs, follower and view counts came from Affan's logged-in Chrome (profile grids, read-only, through JS: no
likes, follows or saves). Frames came from each reel's own `<video>` element in the app's built-in browser (logged out),
drawn to a canvas: 12-21 frame contact sheets, crops at source resolution, and 1/30 s strips around caption changes.
Letterbox bars were **measured** on the decoded frames (first/last rows with mean luma < 12-14 of 255, scaled to 1080x1920).
Caption sizes are estimates from crops at a known scale (±10 %). Audio was not reviewed (SFX notes are guidance, not
measurement). Instagram never showed a challenge or rate-limit page; one post was unavailable logged out (skipped).
Key frames: `references/batch2-shots/` (30 files, numbered as cited below).

---

## (a) Accounts studied

| # | Account | Reel(s), views | What it does best |
|---|---|---|---|
| 1 | [@scottdclary](https://www.instagram.com/scottdclary/) (2.1M followers) | [DSxkgsrDiOu](https://www.instagram.com/reel/DSxkgsrDiOu/) 4.9M (pinned, street interview) · [DeUrYfpROsN](https://www.instagram.com/reel/DeUrYfpROsN/) 111K (collab w/ @scaramucci, 69 s) · DSJm5QOjfIl 2M | Clean single-cam talking head, white label-box title over the hook, small white bold sentence-case captions mid-frame (y ≈ 1075). **Captions HARD-CUT**: the bright-pixel count in the caption band steps in one frame, no entrance animation. Shot 26. |
| 2 | [@successstoryshortsofficial](https://www.instagram.com/successstoryshortsofficial/) (704 followers) | [DdRTfaAlAXZ](https://www.instagram.com/reel/DdRTfaAlAXZ/) 47.7K | Heavy **bold serif** captions (white, black outline), 2-4 words on 2 lines, **semantic colour words**: green "math", red "debt". Hard cuts. Shot 27. |
| 3 | [@successstorypodcast](https://www.instagram.com/successstorypodcast/) (118K) | [DeFpUPmEWh0](https://www.instagram.com/reel/DeFpUPmEWh0/) 92.3K | **Condensed all-caps** (Anton/Bebas class), cap height ≈ 88 px, low (y ≈ 1500-1600), size varies per chunk; the emphasis word is a **silver gradient**, not a colour. Hard cuts. Shots 28-29. |
| 4 | [@steven](https://www.instagram.com/steven/) (Diary of a CEO, 5.2M) | [DdQj0LWOBI0](https://www.instagram.com/reel/DdQj0LWOBI0/) 3.8M (104 s) · [Dc-ho1qgyyK](https://www.instagram.com/reel/Dc-ho1qgyyK/) 10.1M (103 s) | **The caption-animation benchmark.** Word-by-word additive build into a left-aligned typographic stack: small caps lead-in, heavy hero line, one word in a classical serif; red for danger words, yellow for the host's lines, serif lowercase for connectors ("which is"). Hook = stacked split with a **glowing pink-red seam** and the title in black label boxes ON the seam. Cinematic guest title cards (cut-out guest + glitch/RGB-split name; a skyline title sequence). B&W-on-speaker mood shift for a dark line. Dark, desaturated grade. Full-bleed (no bars). Shots 01-07. |
| 5 | [@ycombinator](https://www.instagram.com/ycombinator/) (751K) | [Ddm2MeazX5B](https://www.instagram.com/reel/Ddm2MeazX5B/) 99.2K (112 s); grid: DdkPondNkk4 443K, Dd-UbipBDlm 142K | **The refined-graphics benchmark.** One word per caption in MONOSPACE caps on a translucent grey box at frame centre; mono lower-third stack (orange initial tab, orange company label, name on a translucent box); HUD graphics: a satellite map drifting under thin grid lines with a **corner-bracket reticle**, drones as orange line-art over dark terrain with thin laser lines, mono one-word labels in bracket frames over b-roll. Shots 08-11. |
| 6 | [@stealthmotionn](https://www.instagram.com/stealthmotionn/) (editor, 1.6K followers) | [DQjboTjCGjU](https://www.instagram.com/reel/DQjboTjCGjU/) **512K** (Chris Williamson footage, 33 s) · [DQ7C35tCC_R](https://www.instagram.com/reel/DQ7C35tCC_R/) 266K (Robert Greene, 47 s) | **The letterbox benchmark.** Measured: bars **507 / 514 px**, picture **1044 x 899** (x 22-1066), **rounded corners** (r ≈ 64-80 px), pure black bars (luma 0). Second reel: bars 450 / 458 (picture ≈ 1080 x 1012). Kinetic lowercase stacks INSIDE the window beside the face ("this is / **what** / hard / *feels* / like"), mixed weights, yellow serif italic hero word, soft glow; words fade-slide in over 3-4 frames. Film-clip inserts in the same rounded window. Shots 12-15. |
| 7 | [@valueclippss](https://www.instagram.com/valueclippss/) (clip page, **500 followers**) | [DduL9v2zjwz](https://www.instagram.com/reel/DduL9v2zjwz/) **729K** (37 s); same page 991K, 791K, 547K | Proof the plain bars format travels: measured bars **555 / 555**, picture **1080 x 810 (4:3)**, square corners. ONE word per caption, wide-tracked geometric bold caps (≈ 70 px), white-to-cream vertical gradient, at the window centre on the chin line, **partly behind the speaker** (depth matte). No graphics. Shots 16-17. |
| 8 | [@markbrazil](https://www.instagram.com/markbrazil/) (Mark Mastrandrea, Open Residency podcast, 94.7K) | [DRkNaS3DldC](https://www.instagram.com/reel/DRkNaS3DldC/) **1.8M** (37 s) · DMIeizEseFK 987K · DP_yUcvjXie 555K · [DaNtjGHt3MR](https://www.instagram.com/reel/DaNtjGHt3MR/) (edited by @xalmanedit) | **The "expensive" benchmark.** Dark grey studio, one accent (red). Giant **serif-italic numbers and words with neon bloom** ("$7 million" → "$95 million", "No Television.", "reinvent") between small white lead-in / tail lines; **mono lower-third with a glowing red bar**; tiny sentence-case captions at chest height; wide / close stacked split; warm bloom and orange light-leak transitions. Shots 18-22. |
| 9 | [@vitalyframes](https://www.instagram.com/vitalyframes/) (motion designer) | [DSk_Y-ljpaS](https://www.instagram.com/reel/DSk_Y-ljpaS/) 8.3K likes (11 s) | **iOS-widget UI language**: a Notes-style to-do card (yellow header with date and time, soft blue outer glow) whose items tick off with a hand-drawn strike-through, a cursor hand that taps, a toggle switch, a Books widget ("49 % complete", weekday progress rings) that collapses into the app icon. Shots 23-25. |
| 10 | [@yp.motionstudio](https://www.instagram.com/yp.motionstudio/) | [DYnW0cCIlry](https://www.instagram.com/reel/DYnW0cCIlry/) 26.4K likes (9 s) | Type-only beat scene: one lowercase word at a time, black / white canvas flips on the beat, the hero word scales up. A model for a 3-5 keyword "word scene". |

Also reused from earlier studies (LESSONS): @colinandsamir (real artefacts on a clean canvas), @aliabdaal (graphics in the band
above the head), @chriswillx (title box over the hook), @thedankoe (thin-line geometry on black).
**Checked and not used:** @hubermanlab (full-frame, no captions), @lexfridman (older full-frame reels), @tombilyeu
(Hormozi-style captions), @highperformance (label boxes, no bars), @codiesanchez (white label boxes), @imangadzhi (no recent
reels), and the editor "before/after" showcase pages the keyword search returned (busy, template-y).

**On Scott D. Clary specifically:** none of his three accounts animates captions (every change measured as a one-frame hard
cut). What his pages contribute is **caption styling**: colour that carries meaning (green good / red bad), a silver-gradient
emphasis word, and the confidence to set captions in a serif or a condensed face. The animation ideas below come from DOAC,
Stealth Motion, Mark Brazil and YC.

---

## (b) The moves, ranked (adopt in this order)

Notation: times at 30 fps unless stated (our overlay renders at 60, README rule 3, so a 0.12 s entrance is 7 frames). Easing
names are GSAP's. "Kit" = `presets/youtube-shorts/onyx-samples/kit/`; the picture engine is
`presets/youtube-shorts/onyx-samples-youtube/kit/yt_picture.py` (ig_build runs it with `--dir ig`).

### LETTERBOX / FRAME

**1. The rounded cinematic window on black (Stealth Motion 512K; Valueclippss 729K-991K).**
Looks like: the podcast picture in a wide window, pure black above and below, nothing in the bars by default.
Numbers: window **1044 x 900 at x 18, y 510** (bars 510 / 510; measured reference 1044 x 899, bars 507 / 514), corner radius
**64 px**, bars `#000000`. Alternative "4:3 square-cornered": 1080 x 810 at y 555 (Valueclippss, measured). The window sits
inside the repo's 200 → 1620 safe band. Face: eyes on the window's upper third (y ≈ 810), hair top ≥ 40 px under the window top.
Build: a new shot kind **`LB`** in `yt_picture.py`: run `render_A` with `out_h = 900` (the crop math already supports a
panel height, see SPLIT's `panel_h`), paste it into a black 1080 x 1920 frame at y 510 and apply a rounded-rect alpha mask
(anti-aliased, radius 64). B-roll and FIT get the same window (`render_B` into 1044 x 900). Spec: `"frame": {"y": 510, "h": 900,
"inset": 18, "radius": 64}` so every shot kind inherits it. `ig_capy.py` must clamp the caption block inside the window
(y ≤ 1410 − block height − 24).

**2. The bars become a designed stage, used sparingly.**
Top bar: the hook title for the first ≤ 3 s only, centred at y ≈ 400 (inside the safe band: y ≥ 200), 64-72 px, then the bar
goes back to pure black. Bottom bar: one credit / lower line at y ≈ 1500, 28 px mono, white at 55 %. Type MAY break out of the
window's side edge (Stealth Motion's "you'll wonder" overruns the right edge) but never into the face.
Build: `ig_overlay.py` cards already take `y`; add a `"zone": "topbar" | "window" | "bottombar"` helper that converts to px from
`spec.frame`, and move `credit` to the bottom bar by default.

**3. Shape changes inside the window (our FULL ↔ CARD idea, kept but upgraded).**
(a) **Stacked split** in the window: wide shot top / close bottom (Mark Brazil), or host top / guest bottom with a **glowing
seam**: a 3 px line in the accent with a 12-16 px bloom at 60 % (DOAC hook, shot 06), the hook title in black label boxes ON
the seam. (b) A rare **break-out to full-bleed** (black window grows to 1080 x 1920 in 0.55 s power3.inOut) only for a
full-window graphic scene, then back. Build: SPLIT exists in `yt_picture.py` with `line {w, rgb}`; add `glow` and the window
mask; the seam title is an existing `label` card with `"box": "black"`.

### CAPTIONS (three animation modes; one per video, chosen to fit the speaker)

All modes keep Affan's rules: only `! ?` and quotes, white base + coloured emphasis, ONE constant base position per video
(README rules 1, 2, 7). The block anchors at a fixed x / y for the whole video; size variation happens INSIDE the block, the
block itself never moves.

**4. Mode `stack`: the word-by-word typographic stack (DOAC 3.8M / 10.1M, Stealth Motion 512K, Mark Brazil 1.8M).** Best fit
for opinion and story clips.
Looks like: words appear exactly on their spoken word and accumulate into a 2-4 line, left-aligned block; one hero word per
block is set big in a contrasting face; the block clears together and the next one starts.
Numbers: sizes estimated from DOAC crops (shots 02-04): lead-in line **52-56 px** Inter Bold caps or lowercase, white; hero
line **78-96 px** heavy caps (DOAC), up to **110-130 px** for a serif-italic hero word (Playfair Italic, bundled); numbers
**110-150 px**. Positions are proposed for our window (DOAC's block starts at x ≈ 200 on a full-bleed frame): line gap 0.92 em,
block left x = window x + 72 (≈ 90 px), max width 760 px. Per-word entrance (Stealth Motion strip, shot
14: a word lands in 3-4 source frames): **opacity 0 → 1, x +24 → 0, blur 6 → 0 px, scale 1.04 → 1.00, 0.12 s power3.out**;
the hero word gets 0.18 s and a glow (`text-shadow: 0 0 18px <accent>99, 0 0 4px <accent>`). Block exit: opacity → 0 and
y → −16 over 0.14 s power2.in, ending 0.03 s before the next block's first word. Block = ≤ 7 words; break on sentence end, a
pause ≥ 0.35 s, or a speaker change (`captions.breaks`). Emphasis: ONE hero per block (not 37 highlighted words per clip).
Build: `ig_captions.py` gains `"mode": "stack"`: it groups words into blocks, keeps each word's own start time
(`"words": [[t, "text", "lead"|"hero"|"body"]]`), and picks the hero from `hl` (first `hl` word in the block, else the longest
content word). `ig_overlay.py` renders one span per word with its own `tl.fromTo` at `q(t − 0.03)` and a per-role class
(`.lead`, `.hero`, `.hero.serif`); `ig_capy.py` places the block top at the constant lip line (the hero's extra height grows
downward).

**5. Mode `word`: one word at a time (YC 99K-443K, Valueclippss 729K).** Best fit for fast talkers and data-heavy clips.
Looks like: a single word, all caps, centred on the speaker's chin line inside the window.
Numbers: YC variant: **monospace caps 40-44 px**, white on a translucent box `rgba(40,40,40,0.55)`, padding 6 x 14, radius 4,
letter-spacing 0.04 em. Valueclippss variant: **wide geometric bold caps ≈ 70 px**, letter-spacing 0.06 em, a vertical gradient
fill white → `#E9E1D2`. Entrance (both measured as near-instant): **opacity 0 → 1 over 2 frames, scale 1.06 → 1.00 over
0.10 s power2.out, no overshoot** (the look's rule: type never pops or bounces). A word holds until the next one; a word shorter
than 0.18 s merges with its neighbour. Emphasis = the accent colour on the box (YC) or a solid accent fill (Valueclippss).
Optional **behind-the-speaker** depth (shot 17): the caption layer sits under a per-frame person matte of the window; a premium
touch for the hook only (expensive to build; see `workflows/behind-text.py` for the CapCut recipe, and media-use background
removal for the matte).
Build: `ig_captions.py` `max_words: 1` + the merge rule; `ig_overlay.py` new styles `.cap.mono` and `.cap.wide`; needs a
monospace font (below).

**6. Mode `line`: masked line rise plus a colour sweep on the hero word (our current rise, upgraded).** Best fit for calm,
slower speakers (Rich Roll, Bryan Johnson).
Looks like: 2-4 word chunks rise out of a mask; when the hero word is spoken, its colour sweeps in from left to right.
Numbers: rise 40 px under an overflow mask, **0.32 s power3.out** (today: 14 px in 0.16 s, too small to read as designed);
hero sweep: `clip-path: inset(0 100% 0 0) → inset(0 0 0 0)` of an accent-coloured duplicate over the white word, **0.22 s
power2.inOut**, starting at the word's own time; exit 0.14 s fade. Emphasis semantics from Scott's Shorts page (shot 27):
green `#3DDC84` for good / gain, red `#FF4D4D` for bad / loss, the show accent otherwise; or the silver gradient
(`linear-gradient(180deg, #FFFFFF, #9A9A9A)`) of Success Story Podcast (shot 29) when the show has no colour.
Note: this is the one mode not seen frame-for-frame in a reference (the sweep is a refinement of our rise); 4 and 5 are.
Build: `ig_overlay.py` (the rise already exists; add the mask height, the duration and a `.sweep` duplicate per `hl` word timed
from the word list).

### MOTION GRAPHICS (the vocabulary: dark, glowing, thin, one accent)

**7. Neon serif number / hero phrase (Mark Brazil 1.8M, shots 20 and 22).**
A small white lead-in line ("Where my business went from", 44-48 px Inter Medium), a giant serif-italic number in the accent
(**130-160 px**; measured cap height ≈ 96 px on shot 20; Playfair Italic at its bold weight, bloom `0 0 24px <accent>B3, 0 0 6px <accent>`), a small tail line ("in revenue").
Words appear per word; the number fades and slides 20 px in over 0.10 s, then **re-rolls to its second value** (digit roll 0.45 s
power2.inOut) when the speaker says it ("$7 million" → "$95 million"). Lives in the window's negative space beside / above the
head, never over the mouth. Build: new card `neon` in `ig_overlay.py` (reuse the `number` count-up for the roll; add serif
and glow CSS and `lead` / `tail` lines).

**8. Monospace lower-third with a glowing bar (Mark Brazil, YC; shots 21 and 10).**
Name in mono caps **44 px** white, role **30 px** at 80 %, a **6 x 120 px accent bar** with glow to the left. Animation: the bar
draws down 0.25 s power2.out, then the name reveals left → right (clip-path, 0.35 s linear), role 0.1 s later; hold
2.5-3 s; exit fade 0.2 s. YC variant: an accent tab with the initial letter in a white square. Replaces today's grey credit
pill. Build: new card `lower3`; font: add a monospace (below).

**9. HUD reticle and mono label (YC, shot 11).**
Four corner brackets (stroke 3 px, arms 28 px, white or accent) snap around a subject, icon or region: **scale 1.18 → 1.00 and
opacity 0 → 1 in 0.20 s power3.out**, a mono label types in under it (2 characters per frame), a 1 px crosshair line may run
through the frame edge to edge. Use on a b-roll still, a map, a product, or a face in a wide shot ("this guy"). Build: new card
`reticle` (SVG, `target: [x, y, w, h]` in window px).

**10. Map with drift, route and pin (YC map, shot 11).**
A dark satellite / map still filling the window, drifting 3 % per second (one keyframed push, no punch-ins: README rule 4), thin
vertical grid lines at 25 % white, a route line drawing on (`stroke-dashoffset`, 0.8 s power2.inOut), a pulsing pin
(ring scale 1 → 2.2, opacity 0.6 → 0, 1.2 s loop), the place name in mono. Build: new card `map` (needs a sourced map still,
checked at full size per the HQ-stills rule).

**11. iOS-widget card driven by a cursor (vitalyframes, shots 23-25).**
A rounded (**40 px radius**) widget, 760-860 px wide, white or dark glass, a soft outer glow in the accent (`0 0 40px <accent>40`);
content: a to-do list, a Books-style progress widget, a calendar day, a stocks line, a messages thread. A cursor glides in
(0.40 s power2.inOut), taps (scale 0.92 → 1.00, 0.12 s), items tick with a **hand-drawn strike-through** (SVG path draw 0.25 s)
or a ring fills. This is how our existing diegetic cards (`notify`, `call`, `check`, `rules`, `receipt`) should look and move:
glass and glow instead of paper and drop shadow. Build: a shared `cursor` element plus a `widget` card with `layout: "todo" |
"progress" | "day" | "stocks"`; restyle the existing cards to this language.

**12. Cinematic guest title card (DOAC, shots 01 and 07).**
2.5-4 s, early in the clip (after the hook): the guest cut out (background removed) at the bottom of the window over a dark,
motion-blurred plate (a darkened, blurred, slit-scanned copy of the source or a sourced texture), the NAME in extended / heavy
caps **90-110 px** with a **2 px RGB split that settles to 0 over 0.30 s**, the role line at 36 px, a slow push 1.00 → 1.04.
Build: new card `titlecard` (full window); cutout from media-use background removal; RGB split = three stacked text layers
(R, G, B at screen blend) offset ±3 px → 0.

**13. Light-leak / bloom transition, at scene changes only (Mark Brazil, shots 18-19).**
A warm overexposure: a radial white → amber gradient at screen blend, **opacity 0 → 0.9 → 0 over 0.35 s**, peaking on the cut.
Use only where the camera, source or scene changes (README rule 5), so it replaces a whip, never a same-camera cut. Build: new
card `leak` (CSS radial gradient + `mix-blend-mode: screen`) placed by `ig_build.py` at shot boundaries that change source.

**14. Mood shift: black-and-white speaker with an accent-tinted ground (DOAC DdQj0LWOBI0 at 12.2-13.2 s, shot 01).**
For the darkest line of the clip, 1.5-3 s: speaker to B&W, background tinted toward the accent at 25 %, the caption hero word in
the accent. Build: `grade.bw` already exists per shot in `yt_picture.py`; add `tint {rgb, a}` (a multiply over the frame, or over the
background when a person matte exists).

**15. Word scene: 3-5 keywords on black (yp.motionstudio).**
A full-window black scene where one lowercase word replaces the last on each beat, 0.3-0.5 s per word, the hero word scaled 1.6x;
words rise 24 px in 0.12 s. For a spoken list ("food, alcohol, stress, late nights, light"). Build: new card `wordscene` (full
window), word times from the transcript.

### PACING / DENSITY

**16. A designed event every 2.5-3.5 s, plus continuous captions.**
Measured on the references' contact sheets: DOAC 3.8M has captions in 20 of 21 samples and a non-face visual (title sequence,
b-roll, mood shift) in 7 of 21 (≈ 33 % of runtime); Mark Brazil 1.8M has a hero-type block in 5 of 18 samples, the lower-third in
3, a wide or split in 6; Stealth Motion 512K has a hero stack in 4 of 18 and film inserts in 5 (≈ 28 %). Our Rich Roll final has
**6 card entrances in 46.5 s (1.3 per 10 s)**, one of them (`rules`) held 16 s.
Target: **3-4 designed graphic events per 10 s** (a card or widget entrance, a hero phrase or number, a lower-third, a reticle,
a map, an insert, a transition, or a row / item inside a card); a full-window graphic ≤ 3 s and ≤ 25 % of runtime in total;
always ≥ 1.5 s of face between two full-window graphics; no single card on screen longer than 6 s without a new beat inside it.

### FINISH

**17. A deliberate dark grade, glow on type only, grain you can barely see.**
Bars pure `#000` (measured 0 on Stealth Motion). Picture: contrast 1.10-1.14, saturation 0.85-0.90, slightly lifted shadows
(black 0.015), warm highlights (`warm` 0.02-0.03); a 22 % vignette INSIDE the window (radial, feathered from 60 % of the
diagonal); monochrome grain 3 % (Instagram's encoder removes more, and heavy grain turns to mush). Bloom only on the accent type
and the seam line. Keep the source sharp: the window shows the source at ≈ 1.0x on a 1080p podcast (1044 px wide), so no upscale
artefacts, and Topaz interpolation stays as today. Build: `grade` keys `contrast`, `sat`, `warm`, `black` exist in `yt_picture.py`;
add `vignette {a, r}` and `grain {a}` (per-frame noise seeded by frame index, so renders stay deterministic).

**Fonts to add** (all SIL OFL, from Google Fonts; a download, so log it in the job BRIEF first, per the batch rules):
**JetBrains Mono** (or IBM Plex Mono) for lower-thirds, HUD labels and the `word` mono mode; **EB Garamond Italic** (DOAC's
serif accent; Playfair Italic, bundled, works meanwhile); a wide grotesk, **Archivo Expanded / SemiExpanded**, for the
Valueclippss-style `word` mode and title-card names. Inter stays the body face.

---

## (c) What our current Instagram look does that looks cheap next to these

Compared against `projects/richroll-sleep-rules/outputs/richroll-sleep-rules.final.mp4` (shot 30) and `ig/build_spec.py`.

1. **The 9:16 full-bleed crop.** A 16:9 podcast cropped to 9:16 and pushed in (z0 up to 1.8) gives a huge, soft face and kills the
   set. Every "expensive" reference keeps a wide window on black (1044 x 900, 1080 x 810) and the original framing.
2. **One caption voice.** Inter 600 at 60 px, white + yellow, a 14 px rise in 0.16 s: that is what auto-caption apps produce. The
   references run two or three sizes, a second typeface for the hero word, and per-word timing.
3. **Emphasis everywhere means emphasis nowhere.** 37 `hl` words in a 46 s clip; the references light ONE word per block.
4. **Paper cards with drop shadows** (receipt, check, list) pasted over the chest read as templates. The references use dark
   glass, neon type and thin HUD lines that live in the picture's negative space.
5. **Too few graphic events, held too long**: 1.3 entrances per 10 s, a 16 s list card. The references change something every
   2-3 s.
6. **The grey credit pill at the top** reads as a watermark. The references do a proper name lower-third once.
7. **The hook title** (PT Serif, white with a drop shadow, over the face) is weaker than DOAC's black label on a glowing seam or a
   giant hero word.
8. **No finish**: contrast 1.04 only, no vignette, no bloom, hard cuts everywhere. Every reference has a deliberate dark grade, and
   its scene changes get a flash or a leak.
9. **Captions stuck to the chin regardless of the design**: correct per Affan's rule, but with nothing else typographic on
   screen the picture looks empty. The stack mode keeps the constant anchor and fills the window with type hierarchy.

---

## (d) Proposed v2 look (one page)

**Canvas.** 1080 x 1920, 60 fps overlay (README rule 3). Pure black bars **510 px top and bottom**; the picture lives in a
**1044 x 900 window at x 18, y 510, radius 64**. Alternate per show: 1080 x 810 square-cornered at y 555. The top bar carries the
hook title for ≤ 3 s, the bottom bar a 28 px mono credit at y ≈ 1500 (55 % white). The window can split (wide / close or host /
guest, with a 3 px glowing accent seam) and, once or twice per clip, open to full-bleed for a graphic scene (0.55 s power3.inOut).

**Grade.** Contrast 1.12, saturation 0.88, warm 0.025, black lift 0.015, a 22 % vignette inside the window, 3 % mono grain. One
accent per show (from its branding, as today) plus white; red `#FF4D4D` / green `#3DDC84` only when the words mean loss or gain.

**Captions.** Default **`stack`** (move 4): words land on their spoken word with a 0.12 s fade + 24 px slide + 6 px de-blur
(power3.out); lead-in 52-56 px Inter Bold, hero 96-130 px Inter Black or Playfair Italic in the accent with a glow; ≤ 7 words per
block, one hero per block; block anchored at ONE constant x / y per video just under the lips, inside the window. Alternates:
**`word`** (move 5: one mono or wide word at a time, 2-frame fade + 1.06 → 1 settle) for fast or data-heavy talkers; **`line`**
(move 6: 40 px masked rise 0.32 s + hero colour sweep 0.22 s) for calm speakers. Only `! ?` and quotes; the run is continuous.

**Graphic vocabulary** (pick 5-7 per clip, never all): neon serif number / hero phrase (7) · mono lower-third with glowing bar (8)
· HUD reticle + mono label (9) · map with route and pin (10) · iOS-widget card with cursor taps and hand-drawn ticks (11) ·
cinematic guest title card with RGB-settle (12) · light-leak at scene changes (13) · B&W mood shift (14) · word scene (15) · glowing
seam split for the hook (3). Entrances come from one family: type and cards slide / rise with power3.out 0.12-0.35 s, objects
settle 1.06-1.18 → 1.00 with no overshoot, lines draw on with power2.inOut; exits are 0.14-0.20 s fades or a 16 px rise-out. Glow
on accent type and lines only; no drop shadows on type; no paper textures unless the object IS paper.

**Density target.** **3-4 designed events per 10 s** on top of continuous captions (a 45 s clip ≈ 14-18 events); a full-window
scene ≤ 3 s, ≤ 25 % of runtime in total, ≥ 1.5 s of face between two of them; no card holds past 6 s without a new beat inside it;
open with the face plus the hook title inside 0.5 s, the lower-third by ~4 s, the first big graphic by ~6 s.

**SFX (crisp, premium, never goofy).** One sound per designed EVENT, never per caption word (a tick on every word turns into
typing noise). Pairings from the Epidemic kit (`assets/sfx/epidemic/`): lower-third = `click` + `whoosh-air` (whoosh 10 dB down,
Affan 2026-10-08); reticle snap = `shutter`; widget taps and ticks = `click`, `confirm` on the last tick; hero number landing
= `hit` (trimmed to its transient, at the kit's calibrated level: 3 dB under the voice peak, since quiet SFX read as none); its re-roll = `riser` (short) into the second value; seam split
and title card = `whoosh-light` into `hit`; light-leak = `whoosh-air` + a soft swell; map route = a low `whoosh-light`. Never
cartoon pops, magic sparkles or trills; no sub-drops. **The kit lacks the premium middle:** pull 4-6 more Epidemic files before
the batch (a soft cinematic boom, an airy swell, a film-flash transition, a glassy UI tick, a mono "data blip" for HUD labels,
a camera focus pull) and add each one's measured lead-in to `ig_build.ES_LEAD`. Keep a continuous bed 13-17 LU under the voice
(as on Rich Roll) so the gaps between events never read as dead air.

**What this sample must do better than the last one (for each job's BRIEF).** Bars + window (new), per-word stack captions with a
hero word (new), ≥ 3 designed events per 10 s (was 1.3), dark glass / neon graphics instead of paper cards, a real lower-third,
a finishing grade with vignette and grain, and leaks only on scene changes.
