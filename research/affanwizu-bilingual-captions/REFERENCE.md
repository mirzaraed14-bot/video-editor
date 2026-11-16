# @affanwizu bilingual captions: the reference, measured (2026-11-16)

Affan, 2026-11-16: change the caption strategy to the format of
[appleby's reel Dfsmt8HNSDg](https://www.instagram.com/reel/Dfsmt8HNSDg/): two layers, the native script on top and the
spoken language under it. For him: **Urdu script on top, Roman Urdu below**, built from our yellow style, both layers
"a little bit glowy". Everything else stays the same. First test: ABW11 Sequence 09 (`projects/abw11-seq09-short/`).

## The reference (read in his Chrome, muted and paused, measured off canvas frames at 1080×1920)

- **Account:** appleby (@applesgotit), musician, 213k followers. The bilingual look is a NEW series (first 2026-11-09):
  DfhrzG4S66j 162k (11-09) · Dfm7HiGSt69 69.6k (11-11) · DfphbEty-2W 13.8k (11-12) · **Dfsmt8HNSDg 211k (11-13, the one
  he sent; 18.4k likes, 418 comments, 1,017 reposts, 948 shares)** · Dfx6NQ6tM6B 50.9k (11-15). His best older reels
  use a text hook on top instead: DX2IbJMOYCr 2.7m, DRvkU92jU5q 826k.
- **Content:** song lyrics. Top = Chinese translation (simplified, a plain sans), bottom = the English lyric (a Times-like
  serif). 13.8 s, 1080×1920, loops.

| | Measured |
|---|---|
| Layout | two lines, both centred on x540, never wrapped; the top line is the BIG one |
| Top line (Chinese) | ink y1233-1295 (62 px tall → ~66 px font); width 380-620 px (35-57 % of the frame) |
| Bottom line (English serif) | cap top y1308, baseline ~y1339 (cap height 31 px → ~47 px font), descenders to y1347 |
| Gap | 13 px of ink between the lines (tight, reads as one block) |
| Block position | ink y1233 → y1347, centre ~y1290 (67 % down the frame), below the chest line |
| Size ratio | top : bottom ≈ 1.4 : 1 |
| Colour | both lines the same warm cream, core **rgb(249,244,214) ≈ #F9F4D6** |
| Glow | same-colour halo, NO dark shadow, NO stroke, NO box. Luminance above the background: +38 at 4 px from the ink, +23 at 8, +15 at 12, +8 at 16, +4 at 20, gone by ~24 px (top and bottom line alike) → a soft two-layer glow (tight ~5 px + wide ~18 px) |
| Motion | none: both lines cut on together and cut off together, no fade, no rise (checked frame by frame at 30 fps on three switches: the first frame of a new line is already at full brightness, max luma 252-254) |
| Timing | 6 lines in 13.8 s, each held 1.2-3 s (lyric lines); a line holds until the next one; one empty stretch (10.5-11.4 s, instrumental) |

## This machine (2026-11-16)
- No Nastaliq font installed: only Arial, Calibri, Cascadia, Courier New, Microsoft Sans Serif, Segoe UI, Tahoma and
  Times New Roman cover the Urdu letters (U+06CC, U+0679), all Naskh-style. Candidate: Noto Nastaliq Urdu (OFL),
  `github.com/google/fonts/raw/main/ofl/notonastaliqurdu/NotoNastaliqUrdu[wght].ttf`, 690,304 bytes; install only with his OK.

## The adaptation (proposal, 2026-11-16, before the first test)

- **Top:** Urdu script in a Nastaliq face (Noto Nastaliq Urdu). Size fitted by MEASURED INK HEIGHT on his frames, not the
  1.4 ratio (Nastaliq runs taller and deeper than a CJK line at the same point size).
- **Bottom:** Roman Urdu, our current line (Ubuntu Light 48, spellings per `presets/instagram/affanwizu/roman-urdu.md`).
- **Colour:** our gold #FFD700 on both lines (his "use our yellow caption style"), glow in the same gold; the black hard
  shadow goes (the reference has none).
- **Cues:** unchanged: ≤ 5 words, same switch times, both layers switch together. The Urdu line is WRITTEN from the
  corrected Roman cue (never lifted from words.json, which carries Whisper's misreads: سنگنگ, فالا, چیٹی, no "theek hai").
- **His English (56 of 241 words on Seq 09; whole cues like "to attach themselves") is HIS DECISION:** Urdu letters
  (ڈیفینیٹلی دیئر از سمتھنگ رانگ), an Urdu translation like the reference does (تو یقیناً کچھ غلط ہے), or Latin kept in the top line.
  Proposed default: loanwords inside Urdu sentences in Urdu letters (پرسنل برانڈ ہے), whole English sentences translated.
  Digits stay as on the Roman line (250, 1 لاکھ).
- **Position:** one base per video. The block has to clear his LOWEST chin, not the median: on Seq 09 the chin reaches
  y1193 (66.3 s, median y1094), so the Urdu ink starts ~y1205 and the Roman baseline lands ~y1340, which is where the
  reference block sits (ink y1233-1347) and far above the y1620 safe band.
- **Premiere (UNTESTED on his version; the sources are 2021-24 forum threads):** only one caption track shows at a time
  (Adobe staff: by design). Routes to test: (1) one caption track, each caption with TWO text blocks sharing its timing
  (stays a caption; unknown whether an import can create the second block); (2) two .srt → two caption tracks →
  "Upgrade Caption to Graphic" (PR 23.1+) → stacked editable text; glow = the style's Shadow (gold, distance 0, blur);
  (3) the Urdu line as a rendered transparent layer (browser engine shapes Nastaliq correctly), Roman stays an .srt:
  breaks his editable-captions rule for the top line, so his call. Open risk on 1-2: Nastaliq shaping in Premiere's text
  engine (forum reports of distorted words with Jameel Noori Nastaleeq).
- **The test is a real-speed clip of his fastest stretch, not stills** (reference lines hold 1.2-3 s, his ~0.9 s).
  The glow was measured over a dark background only: show it with and without a faint black shadow.

## Decisions and first test (2026-11-16)
- **His call:** the top line is what he says, in Urdu letters; his English words are spelled in Urdu letters (ڈیفینیٹلی دیئر از سمتھنگ رانگ); nothing is translated. Bottom line = Roman Urdu as before.
- **Font:** Noto Nastaliq Urdu installed for his user (his OK), copy at `assets/fonts/NotoNastaliqUrdu-wght.ttf`.
- **Glow fit (gold over a flat L40 plate, luminance excess):** `0 0 3px rgba(255,215,0,0.4), 0 0 16px rgba(255,215,0,0.85), 0 0 28px rgba(255,200,0,0.5)` ≈ d4 34 · d8 21 · d12 11 · d16 5.5 against the reference scaled to gold (31 · 19 · 12 · 6.5 · 3.2).
- **Geometry on Seq 09 (footage band y420-1500):** Urdu 72 px baseline y1328 (ink tops y1176-1268, widest 869 px), Roman 48 px baseline y1420.
- **Preview:** `projects/abw11-seq09-short/outputs/bilingual-test/` A Ubuntu Light · B Times New Roman (reference serif) · C Ubuntu + faint black shadow. Renderer `projects/abw11-seq09-short/work/bilingual/render_cues.mjs`.

## His notes on the first real job (Seq 10, 2026-11-16 evening)
- On the v1 layer placed in his Premiere: **"too glowy, I want a subtle glow like how that guy had."** Cause: Premiere's linear
  compositing (~3x the halo of the sRGB preview over a dark shirt), not the fit. Fixed with `bilingual/linfix.py`; the glow
  numbers above stay.
- **"add drop shadow as well and make the urdu portion small and do all caps on english ones":** the yellow style's hard
  shadow back on, Urdu 72 → 48 px (now the SMALLER line, the reverse of the reference's big top line), Roman line ALL CAPS.
