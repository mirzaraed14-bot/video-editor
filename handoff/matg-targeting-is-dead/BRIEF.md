# matg-targeting-is-dead: Onyx sample Short for Marketing Against the Grain (Kipp Bodnar, Kieran Flanagan) (batch 4)

## ▶ STATUS: resume here
- **YT 2026-10-23 10:07: YT FINAL DELIVERED (tight pacing, 48 fps), awaiting Affan's review.** `outputs/matg-targeting-is-dead.sample-yt.final.mp4`
  = `X:\Claude Projects\Exports\matg-targeting-is-dead.yt.final.mp4` (byte-identical, H.264 High 1080x1920 48 fps, 2484 f, 51.75 s, AAC
  48 k stereo; decode clean; -12.3 LUFS, TP -2.1; 24 cues; proof `outputs/…sample-yt.proof-sheet.jpg`). Built from the v5 spec
  (`yt/work/spec.v5.json` = 24 fps; `yt/spec.json` now carries fps_out 48): v5 picture (`yt/work/picture.whip.v5.mp4`) → Chronos x2 with the
  jump cuts as segment cuts (`yt/work/segs48.txt`, no morph frames: checked at 77/245/993) → `yt_build … final --skip picture`. v5 = v4 +
  the reviewer's fixes (s07b box, `"HEY`, s08 z0 1.2, Kipp z0 1.38). Superseded: v1 (old pacing), v3, v4, v5 drafts in `outputs/`.
  **FOR THE IG BUILD:** Danny says "paid marketing, RIGHT? And so you expect" — the "right?" (raw 225.98-226.18, tight-cut ≈ 8.65-8.85 s)
  is NOT in `transcript/words.json` / the canonical transcript (WhisperX folded it into "marketing."), so a caption built from the
  transcript misses it; YT carries it in the chunk text ("MARKETING RIGHT?"). Transcript left unchanged on purpose (IG was mid-build).
  Taste call for Affan: Kipp s14 is now a tight z0 1.38 (top of his head cut) because the crop is pinned to the frame bottom; the
  alternative is a SPLIT with Kipp on top (LESSONS 2026-10-12, the webcam-face rule).
- **YT 2026-10-23 09:13: v3 (pure remap) + v4 built and QA'd, v5 queued on the render lock (24 fps), then the 48 fps final.**
  `yt/build_spec.py` = the v2 spec pushed through `work/tight/map.json` (MF/MT; `work/tight/check_remap.py`: 0 deviations vs
  `yt/spec.v1-pacing.json`), faces.json remapped (backup `faces.v1-pacing.json`), base_hq = `outputs/…tight.topaz.mov`.
  `…sample-yt.v3.mp4` = the remap; QA (mine + one sonnet reviewer, `yt/work/qa-v3/`, `yt/work/qa-r1/`) fixed in v4/v5: Kipp s14 captions
  ON his lips (his mouth sits at 61 % of his frame and the 9:16 crop is pinned to the frame bottom, so only a zoom lifts it: z0 1.38,
  fy 0.28, r 0.01); Danny s08 lip touching the caption (z0 1.2, fy 0.32); the spoken "right?" after "paid marketing" captioned
  ("ON PAID" + "MARKETING RIGHT?"); the cut pause left `"HEY` 4 frames ("SPECIFICALLY" + `SAY "HEY`); s07b chart box [110, 340, 800, 560]
  (its SOURCE line sat under the captions, labels past x 960). Kept by decision: the hook card's exit runs ~18 f into s04 (t0 locked on
  Danny's first frame; v1 ran 16 f), the 2-row box on s10 (deliberate), the s07a clipping edge, the stack backdrops' short holds.
  FINAL PLAN: v5 picture → `topaz-iris.py yt/work/picture.whip.mp4 yt/work/picture.whip48.mov --no-enhance --no-stab --fps-mult 2
  --segments <shot f0s + 77,245,993>` (GPU lock; the jump cuts inside s03/s05/s13 must be segment cuts) → `build_spec.py --fps-out 48`
  → `yt_build.py … final --skip picture`.
- **IG 2026-10-23 10:55: IG FINAL DELIVERED (neon-window look, tight pacing, 48 fps), awaiting Affan's review.**
  `outputs/matg-targeting-is-dead.sample-ig.final.mp4` = `X:\Claude Projects\Exports\matg-targeting-is-dead.ig.final.mp4` (md5-identical;
  H.264 High 1080x1920 48 fps, 2484 f, 51.75 s, AAC 256k; decode clean; -12.2 LUFS, TP -2.3; bed 'Out There' 13.5 LU under the voice;
  26 cues, every slice <= 18.9 dB tonal). QA (`ig/qa.py`) PASS: bars black, no strays, punctuation, every word once; proof
  `outputs/…sample-ig.proof-sheet.jpg`. Same lines and receipts as the YT look (GATE 5): IM8's Beckham + Aryna cards, the Zacks SCR
  strips ($305 -> $301, never the $35.7M line), the $305/$301/$239 chart, IM8's live ads, Meta's targeting panel, the Athletech photo,
  80-20 -> 90-10 landing on Danny's word. Camera plate from the TIGHT 4K Topaz (`ig/tools/wincam.py`), not `ig/work/cam24.mov`
  (no crop is upscaled), Chronos x2 per take (1.7 % near-zero steps). v1 kept for reference (`…sample-ig.v1.mp4`).
- **IG 2026-10-23 10:30: IG v1 drafted + reviewed (one sonnet reviewer, defects only); v2 rendering with the fixes.** v1 =
  `outputs/…sample-ig.v1.mp4` (QA PASS: 2484 f @ 48, bars black, no strays, punctuation + every word once). Reviewer r1 fixed in v2:
  thud-2/3 slices began on 0.16 s of silence (hits 0.2 s late; sound.py now aligns a hit's measured ONSET / a swell's PEAK on the event);
  cues added for note strip 2 + the chart's page turn; markers -12 (their scribble sat in the voice band) and a click on the Gender box;
  'to' / fast runs re-blocked (plan asserts every word reaches full opacity before its block fades); one-line captions + a soft scrim
  over IM8's cards (white jacket); ad cards side by side (no overlap slivers); Meta panel clear of the bug; the leaning 2-up take
  head-locked (`ig/tools/headlock.py`: it jumped 77 px at the cut in from Danny full); the spoken 'right?' after 'paid marketing'
  (raw 225.98-226.18) added to the $33M stack tail. Kept by design: the stack lands '$33 million' whole on '$33'.
- **IG 2026-10-23 08:55: IG BUILDING on the tight cut (fresh IG builder).** Everything re-anchored to WORDS in `ig/plan.py` (cut map,
  layouts, framing, 18 shots, 40 caption blocks, 24 cues; build/sound/qa import it). Camera = `ig/tools/wincam.py`: window crops from
  the TIGHT 4K Topaz (never upscaled; 1080p crops would have been 1.2-1.45x), mouth line 568-595 / face 540-578 px in every speaker run
  (`ig/tools/mouth_check.py`), captions at ONE spot (window y 640), then Chronos x2 per take (27 cuts) -> `ig/work/wincam48.topaz.mov`
  (GPU lock). The old `ig/work/topaz48.log` JSONDecodeError = the kill (take 13 re-run alone: 182/182 frames, OK), not a bug.
- **2026-10-23 08:28: CUT TIGHTENED (Task 1 DONE, `work/tight/READY.json` written for the IG builder).** 11 pauses cut on the raw's
  10 ms envelope (`work/cut_plan.py` TIGHT, measurements per pause in its comments; `work/tight/pauses.py`, `edges.py`, `what.py`):
  57 frames = 2.375 s removed → **51.750 s / 1242 f @ 24**, 25 segments, AMPLIFY_DB 0, every left gap ≈ 0.09-0.115 s of room tone
  (the plateaus inside 5 of them were breaths). Not in the transcript-candidate list but cut: Kieran "$400,000 | dollars" (0.41) and
  "hey, | we're targeting" (0.31); the uncaptioned "right?" after "paid marketing" (in the v1 cut, 225.98-226.18) stays, both its
  pauses cut. LEFT (≤ ~3 frames already): of|$300K, spent|$33, that|your, actually|further, joints $239|Right and L4|L5; candidates
  22.82 / 28.46 / 39.91 are speech on the envelope. Map `work/tight/map.json` (kept old-frame ranges); new base frame-exact vs the
  old through it (PSNR ≥ 50 dB); `outputs/…tight.topaz.mov` = the old Topaz 4K stream-copied through the map (1242 packets
  md5-identical; old `topaz.mov` untouched); transcript 168 words = v1 remapped (old: `outputs/…v1-pacing.json`, base
  `…v1-pacing.mp4`, cuts `transcript/cuts.v1-pacing.json`, spec `yt/build_spec.v1-pacing.py`). audio-qa 24 joints clean, dead-air
  PASS, medium.en re-ASR = v1's reading. New visible jump cuts: s03 top (Danny listening, 3 px), s05 (≈ 5 px), s13 (≈ 9 px base).
  The old builder's v2 build (old pacing) died in yt_picture (ffprobe IndexError on the maroon plate, s16); no v2 file exists.
  Next: remap `yt/build_spec.py` through the map → v3 draft (24 fps) → QA → one sonnet reviewer → final 48 fps.
- **2026-10-23 (later): v1 PACING REJECTED.** Affan: the cut is fine but the pauses are too long; the YT look is quick jump cuts (no speech clipped). The old builder (678k-token context) was stopped; a FRESH builder re-tightens the cut (every silence > ~0.15 s -> 2-3 frames, measured on the envelope; line picks, in-line trims, 'biased | and' and the button ending unchanged), re-slices topaz.mov (and cam48 at 2x) through an old->new frame map instead of re-running Topaz, remaps the spec (shots, 67 captions, 24 SFX) and ships the 48 fps YT final; then a second fresh builder does IG from the tightened cut. `outputs/…sample-yt.v1.mp4` = old pacing, superseded.
- **2026-10-23: YT v1 BUILDING (24 fps draft, `yt/work/build-v1.log`, render lock); IG cam prep running (Topaz 4K -> 1080p
  `ig/work/cam24.mov` -> Chronos x2 `ig/work/cam48.topaz.mov`, GPU lock).** Spec = `yt/build_spec.py` (16 shots: 6 DOC receipts, 2 CHART,
  2 SPLIT, 6 A; 67 caption chunks; 24 fresh SFX cues, auto_sfx off; hook credit lands on Danny's first frame, t0 2.167). Decisions:
  CAC stays "CAC" in the captions (as said; "COST PER CUSTOMER" for a 0.2 s word flashed 0.25-0.37 s, unreadable) and the graphics say it
  in plain words (chart title COST PER CUSTOMER, the highlighted "customer acquisition cost" line); two-up spans are SPLITs (Danny's
  panel on top, white line) because a full-frame crop of a two-up panel shows its beige margin; the webcam faces are big (48 % of the
  frame), so full-frame A shots sit at fy_out 0.27-0.30 to keep the chin above the seam captions; the 80-20 chart is a full-frame CHART
  under Kipp and the flip a SPLIT (chart above the seam, Danny below). Two risers failed the tonal check (34 / 20.7 dB > 20) and were
  replaced (x16-x17). Delivery fps: the final renders at **48 fps** (`--fps-out 48`, Chronos x2 per shot: 60 is not an integer multiple
  of the 24 fps source) so the caption pop is smooth. Next: v1 QA -> fixes -> one sonnet reviewer -> final (48 fps) -> Exports ->
  report -> IG build (`ig/`, copied from the Marvel neon-window kit).
- **The cut** (`work/cut_plan.py`, 14 pinned segments, every boundary measured on the 10/5 ms envelope + slice ASR): **54.125 s / 1299 f @ 24**,
  `outputs/matg-targeting-is-dead.mp4`, AMPLIFY_DB 0 (measured), audio-qa joints clean (2 "ambience holes" = joints placed in -66 dB room tone,
  covered by the bed), dead-air gate PASS. 168 caption words (`outputs/<job>.transcript.json`). WhisperX squeezed every spoken number
  (hook "$300,000, $400,000 dollars a day" stamped 17.5-18.2, really 17.65-20.84), so 25 words are re-timed from the envelope (cut_plan RETIME;
  raw stamps kept in `work/words.whisperx.json`); "biased | and" kept (the [s] ends 393.13, "and" 393.14-393.42), "piece" cut in its [p] closure.
  Re-ASR of the cut (medium.en) reads every line as approved. Trims inside lines: hook from "you're"; "on [0.6 s] paid"; "…on Q2, while still
  remaining at AOV" and "per customer" dropped; L5 from "we don't have to target"; L6 "everyone's biased and | they always think they may be
  smarter than the AI"; L7 "So for example, let's say Arena, right? World number one tennis player | we don't actually have to specifically
  say, hey, we're targeting tennis players"; L8 Kipp two pieces; button "I would say it's 90-10 right now." ends 0.015 s after "now".
- **Topaz DONE** (Iris 2x + FI, 17 takes at every joint + layout cut 0,35,113,198,238,324,333,423,525,738,828,857,910,990,1077,1145,1265):
  `outputs/matg-targeting-is-dead.topaz.mov` 3840x2160, 1299 frames, 15 min.
- **Better than the closest earlier sample (TFTC, also a money story with a chart):** every receipt is the company's own world (IM8's own
  site, IM8's live Meta ads in Meta's Ad Library, the Q2 2026 analyst note hosted on Prenetics' own IR CDN), the numbers chart lands on the
  spoken $239, and the ending FLIPS one chart (80/20 under Kipp → 10/90 under Danny on the button word) instead of ending on a static receipt.

## The job
- Approved pick (Affan 2026-10-19/20, line by line): `projects/_onyx-batch4-2026-10/SEQUENCING.md` § 2 ★ A, "Why Beckham's $400K-a-day
  ad account doesn't use targeting". 9 lines, in order; trimming inside lines only. Guest Danny Yeung (co-founder, IM8, with David Beckham;
  CEO of Prenetics). Hosts Kieran Flanagan (glasses, painting behind) and Kipp Bodnar (white room, wooden beams). Remote recording: full-frame
  singles, a two-up and a three-up layout.
- Look: `presets/youtube-shorts/onyx-samples-youtube/` (Sean Ryan look) + README § 13 devices. Template: `projects/tftc-hospital-bill/`.
- Deliver: `outputs/matg-targeting-is-dead.sample-yt.final.mp4` + `X:\Claude Projects\Exports\matg-targeting-is-dead.yt.final.mp4` (MP4 H.264).

## GATE 5 (facts on screen)
- "Aryna" (the audio says "let's say Arena… world number one tennis player"): IM8's own parent announced on 2025-06-26 "World No. 1 Tennis
  Star Aryna Sabalenka Joins Prenetics' IM8 Health as Global Ambassador and Shareholder" (prenetics.gcs-web.com news release; also SI,
  Athletech News). Confirmed against the audio below before her name goes on screen.
- CAC numbers: the episode is from Sept 2026 ("20 months since launch, Dec 2024"), so Danny's "Q2" = **Q2 2026**. Verified: Zacks SCR note
  "PRE: Company Revenue Growth Accelerates, Raising Price Target" (Brad Sorensen, CFA, 2026-08-18, PDF on Prenetics' own IR CDN s27.q4cdn.com),
  page 3: "Yet customer acquisition cost actually declined slightly, from approximately $305 to $301" and "CAC declined further to approximately
  $239, roughly 21% below Q2 levels" (July). The chart prints $305 / $301 / $239 with that source. Danny's "$33 million on paid marketing" is HIS
  number (the note says $35.7M acquisition marketing): it stays spoken only, and no receipt line with $35.7M is shown or highlighted.
  CAC on screen = "COST PER CUSTOMER" (the chart title). (Earlier note: the Q2 **2025** release prints a H1 CAC of $104: wrong year, not used.)
- Aryna: CONFIRMED. Audio "let's say Arena, right? World number one tennis player, we have [a lot of content / a long contract] with her" + IM8's
  own homepage card "Aryna Sabalenka · World No. 1 Tennis Player · Global Ambassador & Shareholder" + Athletech News 2025-06-26 "Tennis Star Aryna
  Sabalenka Takes Stake in David Beckham's IM8". Captions spell the spoken word "ARYNA"; the clause after "with her" is NOT in the cut (two ASRs
  disagree on it).
- "$300,000-400,000 a day" = Kieran quoting what Danny told them off camera (spoken only / as said).

## Download log
| # | File | Source | Size | Why |
|---|---|---|---|---|
| v1 | `work/raw-orig/fIgLRgCC30s_full.mp4` | Affan's own download of the whole episode (`E:\Bullshit Folder\Henry\How-I-Grew-SnapYT.App.mp4`, copied, original untouched); YouTube fIgLRgCC30s, 1920x1080 24 fps, 31:25 | 365.5 MB | the source |
| v2 | `raw/fIgLRgCC30s_A.mkv` | LOCAL derivative of v1: stream copy 40.500 → 611.458 s | ≈ 115 MB | the raw clip the EDL cuts from |
| m1 | `yt/assets/audio/ES_Out There - Out To The World.wav` (+ its DRUMS stem, to subtract for a drumless bed) | Epidemic Sound recording a227905b-d133-4d32-92c3-ce285bc0b1f8 "Out There", Out To The World (dark ambient, suspense, pulses, 99 bpm, 2:47), `mcp__epidemic-sound__DownloadRecording` WAV FULL + DRUMS; not used by any earlier sample (grep of every BRIEF/spec 2026-10-22) | ≈ 30 + 30 MB | the bed (13.5 LU under the voice) |
| x1-x15 | `yt/assets/sfx/<name>.wav` | Epidemic Sound SFX, `DownloadSoundEffect` WAV, none used before in this repo (grep 2026-10-22): 073cf199 Whoosh Soft Airy · fe174b5e Whoosh Airy Tonal Cinematic 01 · 87214551 Whoosh Airy Medium Ghost Tonal · 89724499 Whoosh Airy Clean Short Crisp · 240e5b47 Boom Cinematic Hit Low · 41839644 Boom Cinematic Big Deep Reverberant · 2f0a40ab Boom Cinematic Deep Impact · d0ba83c3 Impact Low Deep Thuds · 6d82b75c Boom Low Hit · 3a908c02 Shutter Release Nikon F4 02 · c65951a5 Shutter Release Nikon F4 01 · 3e3e1af7 Paper Thick Turn Page · a836c16e Marker Writing Circle · da68334f Riser Reverse Build Up Tonal 01 · e73cb6c2 Trailer Swell Reverse 01 | ≈ 0.2-2 MB each | a fresh, varied set: every graphic gets its own sound |
| r1 | `yt/assets/broll/doc-im8-home.png` | https://im8health.com/ (IM8's own homepage, "co-founded with David Beckham"), `workflows/page-record.mjs` still, no login | ≈ 2-8 MB | the hook's receipt: whose ad account this is |
| r2 | `yt/assets/broll/doc-prenetics-q2.png` | Prenetics' own news release "Prenetics Announces Second Quarter 2025 Financial Results with IM8 on Track to Achieve $100M Annual Recurring Revenue by Year's End" (2025-09-12; prenetics.gcs-web.com / SEC EX-99.1), page-record still | ≈ 2-8 MB | "Q2, we spent $33 million…": the public Q2 report he cites (highlight = the headline only; the $ numbers stay his) |
| r3 | `yt/assets/broll/doc-sabalenka-im8.png` | Prenetics news release 2025-06-26 "World No. 1 Tennis Star Aryna Sabalenka Joins Prenetics' IM8 Health as Global Ambassador and Shareholder" (prenetics.gcs-web.com) and/or Sports Illustrated "Aryna Sabalenka Adds Her Muscle to IM8 as Ambassador & Shareholder" (si.com), page-record stills | ≈ 2-8 MB | "let's say Aryna, world number one tennis player" |
| r4 | `yt/assets/broll/doc-ads-manager-audience.png` | Jon Loomer, "Advantage+ Audience vs. Original Audiences" (jonloomer.com): his screenshots of Meta Ads Manager's audience controls (Age 18-65+, Gender), page-record still | ≈ 2-8 MB | "we don't have to target men and women, 18 to 65" (a red box on the age row) |
| r5 | `yt/assets/broll/doc-im8-ads-*.png` | ConvertFlow, "The $120M Meta Ads Strategy IM8 Uses" (convertflow.com/blog/im8-meta-ads-strategy): its screenshots of IM8's real Meta ads, page-record still (crops) | ≈ 2-8 MB | "you let your creatives do the targeting": the real creatives |
| r1 (done) | `yt/assets/broll/doc-im8-home.png` 2560x24862 | https://im8health.com/ full-page still 2026-10-22 (the "Trusted by the world's best" cards: David Beckham "Co-Founder of IM8 Health"; Aryna Sabalenka "World No. 1 Tennis Player · Global Ambassador & Shareholder") | 25.6 MB | hook DOC + the Aryna DOC |
| r2 (done) | `work/dl/zacks-pre-q2-2026.pdf` → `yt/assets/broll/doc-zacks-pdf_p0.png`, `_p2.png` (300 dpi renders, pymupdf) | https://s27.q4cdn.com/906368049/files/News/2026/Zacks_SCR_Research_08182026_PRE_Sorensen.pdf (Prenetics' IR CDN; Zacks SCR, 2026-08-18) | 0.5 MB PDF | the Q2 receipt + the CAC lines |
| r3 (done) | `yt/assets/broll/doc-sabalenka-athletech.png` | https://athletechnews.com/tennis-star-aryna-sabalenka-david-beckham-im8 (2025-06-26), viewport still | 1.9 MB | back card of the Aryna DOC |
| r4 (done) | `yt/assets/broll/doc-meta-ad-targeting.png` | https://www.facebook.com/business/ads/ad-targeting (Meta's own "Audience ad targeting" page: the "Create new audience" panel, Age / Gender / Detailed targeting), full still, no login | 4.4 MB | "we don't have to target men and women, 18 to 65" (box mark on the targeting rows; the panel's example age reads 25-60: Meta's illustration, not a claim) |
| r5 (done) | `yt/assets/broll/doc-adlibrary-im8.png` | https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=US&q=%22IM8%22&search_type=keyword_exact_phrase&media_type=all (Meta Ad Library, public, no login), viewport still 2026-10-22: IM8 Health / IM8 Global / IM8 Health Global (David Beckham video) / a creator partnership ad | 1.5 MB | "Q2 … paid marketing" and "you let your creatives do the targeting" |
| x (tried, not kept) | — | prenetics.gcs-web.com (Access Denied), si.com (CSS blocked), sec.gov (automated-tool block: not bypassed), jonloomer.com (unstyled), convertflow.com (DNS), marketbeat.com (redirected), scr.zacks.com HTML (a modal dims the top; the PDF replaced it) | — | — |
| x16-x17 | `yt/assets/sfx/riser-cine-build.wav`, `riser-reversed-hit.wav` | Epidemic SFX c0b19a7b "Riser, Build, Suspenseful, Cinematic" + fcce71b9 "Riser, Cinematic Hit, Reversed, Distorted" (WAV); previews `work/dl/prev/*.mp3` measured first | ≈ 1 MB each | replace "Riser … Tonal 01" (da68334f, tonal prominence 34 dB) and "Trailer Swell Reverse 01" (e73cb6c2, 20.7 dB): the neon-window LESSONS rule (> 20 dB above 1 kHz = a narrow tone = reject); the new ones measure 15.3 / 15.1 dB (deleted the rejected files) |
