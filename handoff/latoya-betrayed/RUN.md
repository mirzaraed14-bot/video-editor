# La Toya Betrayed — RUN

## ▶ STATUS: resume here (2026-11-04 23:05): v1 DELIVERED, waiting for his review
- **File:** `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\LaToya Betrayed.mov` = `X:\Claude Projects\Exports\LaToya
  Betrayed.mov` = `outputs/LaToya Betrayed.mov`, sha256 0579ac3f321ebcdc…
  - H.264 1080×1920 30 fps, 1435 frames, 47.83 s, 32.3 Mb/s, PCM 48 kHz.
  - −14.0 LUFS / −1.6 dBTP; export QA PASS.
  - Report (B8): [REPORT.md](REPORT.md).
- **Built from:** `renders/finish.mp4` (chunks; chunk 1000 retried once after a MemoryError) + `renders/mix.wav`, CTA mids at
  17.60 (lowered 100 px off the CL band's glow bar, timeline `cta.mid_dy`) and 34.10. No end screen.
- **QA:**
  - `proof/final_asr.txt`: his cut word for word, no banned word, no Dr. Drew, no narration;
  - `proof/final_edges.jpg`: 31 cuts; the only blends are the broadcast's own 1–2 frame dissolves around Barbara's
    listening shot, plus our transition dips;
  - `proof/final_sweep_2fps.jpg`: no watermark, bug or child;
  - `proof/cta_check.jpg`.
- **Recipe** (from the job folder; GPU steps under `../_onyx-batch2-2026-10/.locks/gpu.lock`):
  1. `python build/topaz_faces.py`
  2. `python build/make_timeline.py`, then `python build/fit_y.py` (AFTER every make_timeline), then
     `$PY build/finish.py centers`
  3. `uv run --with opencv-python-headless --with numpy --with scipy python build/stage_a.py track` (only on new shots), then
     `smooth_track.py`, then `fit_y.py`
  4. `python build/dialogue.py`; `$PY build/stage_a.py render renders/stageA.mov`
  5. `python captions/make_words.py`, `make_plan.py`; `uv run --with numpy --with pillow --with fonttools --with scipy python
     captions/render_caps.py render renders/caps_code.mov`; `$PY captions/capcut_pass.py renders/caps_code.mov
     renders/caps_capcut.mov`
  6. `bash build/render_chunks.sh`
  7. `python build/mix.py renders/mix.wav`
  8. `python build/export_cta.py renders/finish.mp4 renders/mix.wav "outputs/LaToya Betrayed.mov"`
  9. QA as above.

## ▶ (earlier) STATUS 2026-11-04 ~21:50: CODE BUILD RUNNING (his 4 answers: "Yes, all four")
- **Done:**
  - catalog pass (BRIEF § CATALOG PASS, appended);
  - Topaz Proteus x2 face excerpts (`renders/Ra|Ta|Ca|Cb|Da|Db.mov`, `build/topaz_faces.py`);
  - overlays:
    - Higgsfield: Gordon still and Gordon + La Toya still at 4K (`assets/*_hf.png`); Tel Aviv, 1980s, 2005 walk and
      2005 point via Topaz 2160p (`dl/hf/*_up.mp4`), each re-cropped above the CL watermark / HLN bar, true aspect
      restored;
    - checked at full size against the originals (`proof/hf_check1.jpg`, `hf_check2.jpg`): real faces, not waxy;
  - closet = Unsplash OnIGr3hBSdA (free licence, 2000×3000);
  - `build/make_timeline.py` (his re-cut + DD picture slip 0.16 s + per-source bands) → `build/fit_y.py` (one face height
    per setup; watermark / HLN rows always below the band) → `finish.py centers`;
  - `renders/dialogue.wav`, `renders/caps_code.mov` (2869 f), `renders/mix.wav` (−14.00 LUFS, −1.60 dBTP; CTA mids 17.60 / 34.10).
- **Running / next:**
  - `renders/stageA.mov` (GPU, under gpu.lock);
  - `captions/capcut_pass.py renders/caps_code.mov renders/caps_capcut.mov`;
  - `finish.py stills` check;
  - `bash build/render_chunks.sh` → `renders/finish.mp4`;
  - `python build/export_cta.py renders/finish.mp4 renders/mix.wav "outputs/LaToya Betrayed.mov"`;
  - QA: `win/final_edges.py`, `win/asr_file.py`, the B7 boxes;
  - copies: E: Final Renders + X: Exports;
  - REPORT (B8), LESSONS.
- Higgsfield credits: balance read 981 before and after the 2 stills + 4 clips (charges not shown yet: re-check).

## ▶ (earlier) STATUS 2026-11-04 ~20:30: HIS REVIEW 1 IS IN → BUILD NEXT (4 picks asked)
- **His Tella** (`guide/review1.mp4`) is resolved in [REVIEW-1.md](REVIEW-1.md). "Apart from that everything is fine." **He
  also re-cut our sequence in ABW10** (48.03 s): `premiere/his1/readback.tsv` (also `premiere/readback.tsv` now).
  **HIS CUT IS THE SPEC: never re-place over it.** Our last placement is kept in `premiere/v1/readback.tsv`. Re-ASR of
  his A1 is in `win/asr_his1.json`. He cut "I think if I were Michael" (B5) and "I love you. He goes, no, I love you more"
  (B6), and extended the end through "about this". Both kept as decisions; he's asked to confirm.
- **Measured:** Dr. Drew's picture runs ~0.16 s AHEAD of its audio (bilabials). In the build, slip every DD picture 4
  source frames later. The 20/20 copies are in sync. His end (457.767) touches a sound at ~457.62, probably Dr. Drew's
  "Hey, Chris": end at ~457.55.
- **Sourcing (2026-11-04):**
  - Every Jack Gordon photo online is watermarked Alamy / Getty stock: never stripped. Use 20/20's own Gordon frames
    (TT 10–13.5 Gordon alone smiling; TT 16–19.99 / CL 445–449 Gordon + La Toya photo) + Higgsfield 4K.
  - "Michael-Jacksons-Siblings-SnapYT.App.mp4" is a *the detail.* compilation (lock 7: out).
  - Michael + La Toya footage that exists: CL 355.0–358.5 (1980s, smiling and talking, 480p) and DD 417–431 (2005).
  - Michael smiling video: Grammy Legend 1993 (his restored file, ~476 / ~596 s) → desaturate + letterbox.
  - 1993 Tel Aviv press conference: TT 20.0–25.4 (720p).
- **Asked him (defaults in brackets):**
  1. the two word cuts [keep his cut];
  2. Gordon = 20/20's own frames upscaled [yes];
  3. closet = a real stock photo of a dark, luxurious wood closet, no people [real stock; AI-generated only on his word];
  4. Michael + La Toya overlays = the 1980s 20/20 clip (happy, talking) for the B5 slot and the first B6 slot, Dr.
     Drew's 2005 footage for the second B6 slot [yes].
- **NEXT on his answers:**
  - the style-catalog pass into BRIEF.md (CLAUDE.md learning loop 5);
  - copy the Owen/Harry kit (`projects/owen-hart-wife/build/` + `captions/`, Harry's v4 zoom grouping) and drive it from
    `premiere/his1/readback.tsv`;
  - picture: letterbox (picture ≈ 1366–1506 px tall) + one static head anchor per shot;
  - one zoom layer per shot change;
  - grade per source;
  - house captions;
  - low labels: 1993 card on the hook, Gordon lower third, A CALLER · 2012;
  - mid CTA ×2, no end screen;
  - Higgsfield (stills 4K at 2 credits each, Topaz test clip first);
  - −14 LUFS / ≤ −1 dBTP;
  - `LaToya Betrayed.mov`, B7 QA, B8 report.

## ▶ (earlier) STATUS 2026-11-04 ~18:20
- **RAW CUT PLACED in ABW10, NOT saved** (he saves). Bin **"LaToya Betrayed"** › **"LaToya Betrayed - raw cut"**, a
  clone of "Onyx reaction template (empty)" set to 30.00 fps (display 104), 1080×1920. **51.43 s.**
  - V1/A1: 28 clips each, source audio only. V2: 7 picture-only overlays. 6 beat markers.
  - His active "Sequence 41" was restored after every window.
  - Placed 3 times: v1, then the Gordon photo in-point (15.0 → 16.0), then the slowed reaction re-rendered without the
    source's dissolve. Each re-place ran only after `run_replace.py` confirmed the sequence was unchanged since the last
    read-back.
- **Verified:**
  - `win/verify_eff.py`: every V1/A1 clip holds exactly the measured in/out (0.0 ms); no gaps.
  - A1 rebuilt from the read-back and re-ASR'd with medium.en (`win/asr_a1.json`): the brief's words in all 6 beats, plus
    the caller's "And" before "I wondered" and La Toya's "And" before "he says" (both glued on, kept: § Raw cut).
  - `win/gap_check.py`: longest quiet run 0.08 s.
  - Picture (`proof/sim_readback.jpg`): adults only, no Playboy-era footage, frame 1 = her 2009 face.
- **Lock 1 proof:**
  - TT out 25.20: re-ASR to 25.20 and 25.233 hears "…accused Michael." ("of being a pedophile" from ~25.22; to 25.32 it
    hears "Michael of").
  - "Yes" in 26.4333: re-ASR from 26.40 hears only "Yes" (no "-phile"), so a 2-frame crossfade is safe on both sides.
  - DD in 401.0667: "molester" ends ~400.64; re-ASR of 400.0–401.0667 hears "child molester." and nothing after it.
  - CL: Barbara's "pedophile" (~509) is 7 s after our last CL out (502.0667).
  - Captions/cards in the build never carry it.
- **WAITING for his check of the raw cut** (§ Questions for his check). Then the code build, after the CLAUDE.md
  learning-loop-5 catalog pass in BRIEF.md: copy the newest AW build kit (`projects/paris-shock-therapy/build/` or
  Owen's if built by then); per-source grade (TT cooler ↔ CL warmer); house captions; low cards; mid CTA ×2, no end screen;
  one Topaz pass (Higgsfield, test clip first) + 4K stills; crop above the watermark and every bug; −14 LUFS /
  ≤ −1 dBTP; `LaToya Betrayed.mov`; B7 QA; B8 report.

## ▶ (earlier) STATUS 2026-11-04 ~17:30
- **Brief is v2** (his `X:\Claude Projects\Abundance Wisdom\LATOYA-BETRAYED-EDITOR.md`, re-locked 17:05 after a
  source-quality pass): [BRIEF.md](BRIEF.md) is a byte-identical copy. v1 (12:12) is kept as [BRIEF-v1.md](BRIEF-v1.md),
  history only: **never cut from v1.** v2 drops all of Jensen! 2008, which is 240p everywhere online. Beats 1–4 are now 20/20
  2009 (TT = Nine 720p for the hook; CL = ABC 480p 4:3 with a churchoflatoya.com watermark for the closet / puppet /
  threat), and beats 5–6 are Dr. Drew 2012 (DD 720p). Tel Aviv b-roll is gone; there are 3 photos.
- **No end screen** (orchestrator, 2026-11-04: he rejected Road to 1M in the Harry Diana review): hard cut on "cried
  together", as the brief says. The two mid prompts stay. No sub count needed.
- **His downloads ARRIVED 17:08–17:09** in `E:\Bullshit Folder\Henry`: TT, CL, DD, PR. All are the v2 brief's uploads, at
  the expected resolution (§ Intake check). No photos yet. Not yet copied into the job, transcribed or placed. ABW10
  untouched, no Premiere lock taken, no GPU used.
- **WAITING** on his answers (§ Open questions; he hasn't said "defaults" yet). Then: copy to `dl/` → words → raw cut
  in ABW10, using the Owen Hart method (`projects/owen-hart-wife/` RUN.md § Re-run recipe, `win/asr_plan.py`,
  `premiere/run_replace.py`).

## Intake check (2026-11-04 ~17:15, ffprobe + frames: `proof/intake_sheet.jpg`, `proof/intake_cl_vs_pr.jpg`)
| key | his file (`E:\Bullshit Folder\Henry\`) | stream | notes |
|---|---|---|---|
| TT | LaToya explains why she accused her brother in the early 90´s, September 2009, 20-20.mp4 | H.264 1280×720, **24.715 fps** (9101 frames / 368.3 s), AAC 44.1 k | ✓ clean; "9 · 50 years" bug bottom right. 0:26 = the tight reaction shot (frame 1); 0:34 = the wide two-shot. Odd frame rate: conform it at intake (seq_src, native fps) and check lip sync. |
| CL | La Toya Jackson on 20-20 - September 11, 2009 - Part 1 of 3.mp4 | H.264 720×480 (SAR 1:1), 29.97, 9:29.5 | ✓ the ABC capture. **The real picture is only 536×404** at (90,38) inside black borders (cropdetect), true 4:3, so nothing is stretched. The watermark runs ~y378–419, right on her chin in close-ups. The clean area is y38–~375 (337 px), which gives a 9:16 crop of 190×337, ≈ 5.7× to 1920 (120 % past the full-picture crop; within the brief's ~125 %). Soft, but natural. |
| DD | LaToya Jackson on Dr. Drew  (07-06-2012).mp4 | H.264 1280×720, 25 fps, 10:13 | ✓ HLN; the HLN DrDrew bug + lower-third supers ("ON THE PHONE: JANE California") across the bottom ~20 %: crop above them. |
| PR | MICHAEL JACKSON - 1-3 HD - BARBARA WALTERS & LA TOYA.mp4 | H.264 1280×720, 30 fps, 6:25.7 | Fallback only. Has the abc bug. At the same 9:16 face crop, TV scan lines show on her skin, the colour is pink and the highlights bloom: **CL is the better picture** (`proof/intake_cl_vs_pr.jpg`), so v2's call holds. CL→PR offset ≈ −248 s. |

## Job facts
- AW Short "Why Michael Jackson's Sister BETRAYED Him 💔". La Toya lane. Creative locked: cut exactly as written;
  anything that can't be done as written → stop and ask him, never improvise.
- Method = the Owen Hart Short (`projects/owen-hart-wife/`, raw cut 2026-11-03/04): answer the brief's conflicts with his
  standing rules → raw cut in ABW10 for his check → full build. Older example: `projects/mj-skin-son-tyson/`.
- Delivery: 1080×1920, 30 fps, −14 LUFS, ≤ −1 dBTP, `LaToya Betrayed.mov` →
  `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders` (+ copy in `X:\Claude Projects\Exports\`). Never C:, no phone copy.
- House rules: never save or export ABW10; every Premiere window takes `projects/_onyx-batch2-2026-10/.locks/premiere.lock`;
  never touch the Owen Hart bin/sequence; never kill another session's processes; work in silence (ffmpeg `-f null` only);
  lean mode (no agents without asking; builders Sonnet, never Fable); **YouTube is blocked on this PC: never bypass it**
  (no yt-dlp, not even `-F`; the brief's B2 yt-dlp lines are his source list, never run them; the downloads are his).
- Lock 1: "pedophile" / "child molester" must never be audible or on screen: TT ~0:25, **CL ~8:26** (right after our beat-4 out)
  and DD ~6:38. Prove it from words.json around every in/out and crossfade. Lock 3 (v2): **no Barbara narration** in beats 2–4.
- Grade reference: earlier La Toya Shorts `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\toya.mov` and
  `toya yt final.mov`. v2 B3: grade-match TT (cooler) to CL (warmer).
- Build notes from his Harry Diana review (AW LESSONS 2026-11-04): zooms are ONE smooth, subtle eased push-in per block
  (~4 %/s, max 8 %, sine in-out, no pops); no per-frame head-lock wiggle (one anchor per shot, slow follow only where the
  head really travels); no sub-0.5 s shot between a reverse and an overlay.

## Sources (v2 B2), his downloads, MP4 / H.264 (not AV1), highest quality
| key | what | link | expected | need |
|---|---|---|---|---|
| TT | 20/20 2009, Nine rebroadcast (Dee Grimes) | https://www.youtube.com/watch?v=Z8d4M3SRRYE | 720p25 | B1 hook |
| CL | 20/20 2009, ABC capture, Part 1 of 3 (Church Of La Toya) | https://www.youtube.com/watch?v=UpTnvwxRyW8 | 480p30 4:3, watermark | B2–B4 |
| DD | Dr. Drew HLN 2012 (LunaJo/Jolanda) | https://www.youtube.com/watch?v=9LWo0e1b7gE | 720p25 | B5, B6 |
| PR | 20/20 "1/3 HD" (paradiseresort), filmed off a TV | https://www.youtube.com/watch?v=85HUHa9puGI | 720p30 | last-resort B2–B4 only |
- Photos (real, adults only, highest resolution): Jack Gordon with La Toya (early–mid 1990s); adult Michael 1993; adult
  La Toya with adult Michael (2003–05, no children). Backup for Michael 1993: frames from
  `E:\Bullshit Folder\Skin Michael\Michael Jackson - Oprah Winfrey Interview (1993) 4K 50Fps Upscale(1).mp4` (AI upscale:
  waxy check) or `E:\Bullshit Folder\Michael Jackson Super Bowl 1993 [SNIPPETS IN HD].mp4` (1080p25).

## Source search (2026-11-04, v1 sources): none on his drives
- Searched E:\ (all), X:\, D:\, G:\My Drive, C:\Users\affan\{Downloads,Videos,Desktop} for toya / jensen / drew / walters /
  20_20 / gordon / tel aviv / the v1 YouTube IDs. Not usable (lock 7, compilations): *the detail.* files
  (`E:\Bullshit Folder\Lonely\`, `C:\Users\affan\Videos\`), the 68-min "Chronology [1991-2020]" (`Lonely`).
  `E:\Bullshit Folder\Henry\La Toya Jackson Opens Up on Michael's Death.mp4` (176 s, 360p) is not DD.
- v2's new IDs (UpTnvwxRyW8, 85HUHa9puGI) not searched by ID; nothing named "20/20" or "Walters" + La Toya was found.
- His quality question: v2's own audit answers it (every upload checked by eye). The web outside YouTube has no official
  ABC / HLN copy.
- Higgsfield balance 1,042 credits (2026-11-04).

## Cost quote (sent; unchanged by v2)
- ≈ 7–9 % of the weekly cap (≈ $150–200) in this session, lean: raw cut ≈ 2–3 %, build + render + QA + report ≈ 5–6 %.
- Higgsfield (only on his yes): 3 photos × `upscale_image` 4K = 6 credits; ONE Topaz pass on the played 9:16 crops of the
  SD footage (≈ 60 s, Paris rate 5 credits / 2.7 s, unproven) → up to ≈ 110 credits, one test clip first. v2 B3: "any
  upscaling … done once … no AI face 'enhance' that changes her features" → no face-recovery model; compare her face
  to the original before using it.

## Open questions (update sent 2026-11-04 ~17:30, defaults in brackets)
1. Downloads: TT, CL, DD (+ PR fallback). [into E:\Bullshit Folder\Henry]
2. Photos: OK for me to download the 3 from Google Images myself, check adults only, and upscale them? [yes]
3. Music: none (his rule; his Owen answer). [none]
4. CTA: mid pills ×2 only (no end screen). They sit at y1392, so they avoid the hook card, the Gordon lower third, the
   "A CALLER · 2012" card and all of B6; exact slots set on the real cut. [yes]
5. Captions + cards: house look, one constant base just under the lips; labels/cards LOW (top ~y1260–1280, bottoms above
   y1536), not the brief's top third / 62–68 %. [house look]
6. CL watermark: crop above it (forehead to lips, v2 lock 2); where a shot can't be cropped clear, a soft blur band (the
   captions stay at their constant base, so they won't always sit on the band). [yes]
7. Upscale: one Topaz pass, no face-recovery model, checked against her real face, up to ~110 credits, test clip first. [yes]
8. Stop after the raw cut in ABW10 for his check. [yes]

## Decisions
**Affan, 2026-11-04 ~17:20 (his words): "Yes, start it"**, answering "Start the raw cut with the defaults?". So every
default in § Open questions holds:
1. no music;
2. mid CTA ×2, no end screen;
3. house captions + low cards;
4. watermark: crop above it, otherwise a soft blur band;
5. I source the 3 photos from the web myself (adults only), Higgsfield 4K upscale (6 credits);
6. one Topaz pass on the SD footage, no face-recovery model, test clip first (up to ~110 credits);
7. stop after the raw cut in ABW10 for his check.

## Pipeline
| # | Step | Status |
|---|---|---|
| 0 | Brief saved (v2), sources searched, quote + questions sent | ✅ 2026-11-04 |
| 1 | Intake (his downloads → `dl/`, `seq_src/`, `raw/`; ffprobe resolutions) | ✅ 2026-11-04 17:24 |
| 2 | Words + edges, raw cut in ABW10, read-back, A1 re-ASR, gap check | ✅ 51.43 s, 18:15 |
| 2c | His check of the raw cut | ⏳ waiting |
| 3–8 | Code build (catalog pass into BRIEF, grade, captions, labels, mid CTA ×2, upscale) → render → B7 QA → B8 report | pending |

## The raw cut (actual, from the read-back; source = each upload's own clock)
| Beat | Timeline | Source in → out (pieces) | Words (A1 re-ASR) |
|---|---|---|---|
| 1 | 0:00.00–0:07.53 | TT 22.600–25.200 · 26.433–27.000 · 32.700–37.067 | "During the time of your marriage, you accused Michael—" / "Yes." / "Gordon gave me this piece of paper, and he says, 'Read this.' He says, 'You better say this. You say this.'" |
| 2 | 0:07.53–0:17.17 | CL 449.067–451.300 · 451.500–454.300 · 454.467–457.033 · 457.267–459.300 | "He would lock me in the house no matter what. He would close the closet door and say, 'Don't leave that closet.' Do you know I would stay in the closet for eight hours and not leave? Because that's how well-trained I was." |
| 3 | 0:17.17–0:22.80 | CL 482.600–483.600 · 483.867–485.000 · 485.167–487.567 · 487.867–488.967 | "'I tell you what to do. I'm your puppeteer. I pull the strings and you act.' And guess what? I did it, Barbara." |
| 4 | 0:22.80–0:32.43 | CL 490.433–491.700 · 491.967–493.067 · 493.467–495.000 · 495.433–496.300 · 496.567–497.733 · 497.867–498.333 · 498.533–500.967 · 501.267–502.067 | "I was too afraid, because he promised if I did anything out of the ordinary that he would kill me. And he took it a step further. He said, 'And if you don't believe me, I will do it to your brother as well.' And I believed him." |
| 5 | 0:32.43–0:39.70 | DD 401.067–404.967 · 405.233–408.600 | (caller) "And I wondered how you were able to make amends with him after that. I think if I were Michael, I'm not sure if I could ever forgive that." |
| 6 | 0:39.70–0:51.43 | DD 418.067–420.467 · 420.633–425.000 · 425.133–426.167 · 452.667–453.567 · 453.700–456.733 | "When I finally got a chance to talk to him about it, and he says, 'You don't even have to tell me.' He says, 'I know, I know you. You're my sister. I love you. I know your heart.'" / "I love you. He goes, 'No, I love you more.' And we just hugged, and we cried together." HARD CUT |

- Pauses over ~0.25 s closed to ~0.1–0.2 s at measured quiet runs (B2 ×3, B3 ×3, B4 ×7, B5 ×1, B6 ×3). The only trim inside a range is the
  brief's "I didn't know any better". Nothing else dropped: 51.4 s is under 60, so none of the "If over 60s" options are used.
- Kept (glued to the next word, not separable without clipping it): the caller's "And" before "I wondered" (the brief
  starts on "I wondered"; the reason, the accusation word, is out), and La Toya's "And" before "he says" (Owen precedent).
- Words to caption by ear in the build: B1 "He says" (heard "He said / He says / He goes" by different passes); B6a
  "got a chance" (medium.en) vs "had a chance" (first pass). The A1 re-ASR says "got".

V2 (picture only):
- B1 0:00.00–0:03.17: her tight reaction (TT 25.47–26.58, the only take, 1.1 s) slowed ×2.88, `seq_src/TT_react_slow2.mov`.
  Frame 1 = her 2009 face under Barbara's question and her "Yes".
- B1 0:03.17–0:04.60: the 1990s Jack Gordon + La Toya photo (TT 16.0, 20/20's own) over "Gordon gave me this piece of
  paper". The crop holds Gordon only (side by side; § Lessons). Build: pan Gordon → La Toya.
- B1 0:06.83–0:07.53: TT two-shot (34.3) over the source's dissolve to Barbara at the end of "You say this".
- B3 0:17.17–0:18.17: her close-up (CL 485.4, brief "~8:05") over 20/20's Playboy-era B-roll under "I tell you what to do".
- B4 0:30.23–0:31.63: Michael, Grammy Legend Award 24 Feb 1993 (his file, 584.0) over "I will do it to your brother as well".
- B5 0:36.57–0:38.10: Michael, Oprah 10 Feb 1993 (his file, 92.0, AI upscale) over "if I were Michael, I'm not sure".
- B6 0:48.67–0:50.23: La Toya arm in arm with Michael, 2005 (DD 418.6 still) over "I love you more, and we just hugged";
  back to her for "and we cried together".

V1 picture worth knowing:
- B2 opens on the broadcast's Gordon photo (the hook's photo, again) dissolving into the stylised 1980s portrait (brief:
  keep the portrait).
- B4 shows the two-shot (cropped to her) under "because he promised / if I did anything", and Barbara LISTENING for ~1 s
  under "and he took it a step further" (the broadcast's own cut).
- B6a is Dr. Drew's own B-roll of La Toya with Michael (2005, adults; walking arm in arm, then La Toya + Janet + Michael
  close, crop on Michael), because HLN cut away from her there. The brief wanted her face.
- Raw-cut crops show the churchoflatoya.com watermark, the 9 bug, the HLN supers and a "GETTY IMAGES" credit (DD B-roll,
  top). The build crops above all of them.

### Child / content sweep (10 fps, FULL frame, since the build may pan)
- `proof/cc_dd_6a_10fps.jpg` covers DD 417.9–426.3: the walk (La Toya, Michael, adult bodyguards), the dissolve, the close
  shot (La Toya, Janet, Michael), and the start of the dissolve into the pointing shot. Adults only.
- `proof/cc_cl_449.jpg` covers CL 449.0–451.4 (Gordon photo → portrait): adults.
- `proof/cc_cl_482.jpg` covers CL 482.6–502 at 3 fps. The Playboy-era frames run 482.6–~483.4, entirely under the B3 V2
  cover (482.6–483.6); the rest is her close-up, the two-shot, and Barbara listening.

### Crossfade margins for the build (2–4 frame crossfades; nothing banned may come back in)
- TT "Michael" out 25.20: proven to 25.233 (+1 frame). Use a crossfade that ENDS at the cut, or ≤1 frame past it.
- TT "Yes" in 26.4333: proven from 26.40 (−1 frame). "-phile" decays to ~26.415.
- CL B2 in 449.0667: Barbara's "influence" ends ≤ 448.88, so up to ~5 frames back is safe.
- DD B5 in 401.0667: a soft "yeah" sits at 400.80–401.06. Its phone-band HF share is −30.6 dB, between the caller's −35 and
  Dr. Drew's −26: unclear whose it is, possibly Dr. Drew, which hard rule 4 forbids. The crossfade must START at the cut,
  never before 401.0667.
- DD B6 in 418.0667: "Michael" ends ~418.04. Up to ~0.5 frame back.
- CL last out 502.0667: "I had…" from 502.13. ≤1 frame past.
- DD hard cut 456.7333: no crossfade (hard cut), and "about" from ~456.72 → re-ASR to 456.7333 hears only "together".

### Questions for his check (defaults in brackets)
1. B6a: Dr. Drew's own footage of La Toya with Michael under "when I finally got a chance … I know your heart" (her face
   isn't in the source there) [keep it].
2. The hug still is from that same footage (the only shot where both faces fit a vertical frame) [keep it].
3. The Gordon photo shows twice: under the hook's "piece of paper", and for ~1 s at the start of the closet line (20/20's
   own picture) [keep it].
4. Barbara's 1 s listening shot in B4 [keep it].
5. The two glued "And"s [keep them].
6. Frame 1 is her only reaction take (1.1 s) slowed ~2.9× so it sits under Barbara's whole question and her "Yes" (the
   brief names entry as the biggest risk) [keep; the build re-times it smoothly].
7. The Gordon photo crop holds Gordon only (the photo is side by side). Build: slow pan Gordon → La Toya inside full-bleed
   [pan].
8. Runtime 51.4 s, not the brief's ≈60–63 s: every word of the brief is in; the difference is the closed pauses (hard
   rule 1) [fine].
9. The caller's audio is usable (A1 re-ASR word-perfect), so beat 5 stays and the brief's fallback isn't needed.

### Re-run recipe
```
python premiere/make_beats.py                                                     # sources.json, beats.json, framing.json
python ../../presets/youtube-shorts/abundance-wisdom/resolve_beats.py . --fps 30  # -> edl.json
uv run ../../presets/youtube-shorts/abundance-wisdom/plan_placement.py . --fps 30 TT_2020_Nine_2009@35.0 DD_DrDrew_2012@420.9
python ../../presets/youtube-shorts/abundance-wisdom/place_sequence.py . "LaToya Betrayed - raw cut" "LaToya Betrayed" premiere/place.jsx
SNIP_DEVICE=cpu FW_MODEL=small.en <whisperx-venv python> -I win/asr_plan.py      # re-ASR the PLAN before Premiere
python premiere/run_replace.py     # re-place ONLY if unchanged since premiere/v1/readback.tsv (first time: run_window.py)
python premiere/pp.py premiere/readback.js > premiere/readback.tsv && cp premiere/readback.tsv premiere/v1/
python win/verify_eff.py ; python win/verify.py ; uv run --with pillow python win/sim.py --readback proof/sim_readback.jpg
SNIP_DEVICE=cpu FW_MODEL=medium.en <whisperx-venv python> -I win/asr_a1.py ; uv run --with numpy python win/gap_check.py
```
