# Paris Shock Therapy — BRIEF (decisions)

AW Short **"Why Michael Jackson's Daughter Got SHOCK Therapy 💔"**. The locked editor brief is
`X:\Claude Projects\Abundance Wisdom\PARIS-SHOCK-EDITOR.md` (locked 1 Nov 2026). This file records every decision
taken against it, and every question still open for Affan. State and next steps live in [RUN.md](RUN.md).

## Affan's instruction (2026-11-01, verbatim)
"start a session for this short and do the sequencing for premiere and await my direction video"

## HIS DIRECTION 1 (Tella "Video Editing Instructions for Paris Jackson Project", 2026-11-02 ~14:40)
`guide/tella1.mp4` (8:31), transcript `guide/tella1.json`. Every "here / this one" is pinned to HIS timeline by the
program-monitor timecode and the selected clip (`proof/tella_tl_*.jpg`, `proof/tella_tc_trans.jpg`).

**His cut is the spec**: he re-cut the raw sequence in Premiere himself, to **42.40 s**. The read-only dump is
`premiere/his_cut.tsv`; his A1 was rebuilt and re-transcribed (`win/asr_his_a1.json`). Never re-place over it. What he
changed:
- B1: "They … knock" stretch tightened, "I mean, the" and the doubled "it was" removed. Now reads "…I did nine
  sessions in three weeks. The first time I woke up and it was the most sharp pain…".
- B2: the second "like" is gone: "I got very, very close, centimeters away."
- B3: "It was really hard, and" cut, so it now starts "people would tell me to kill myself every day. And I was
  depressed."
- B4: every pause tightened ("completely … not", the syllable before "visit", "me … and").
- Overlay slots are marked by dragging clips up to V2, as he does on every job.

### Overlays (V2 slots, his timeline)
| Slot | Time | Under the words | What he wants |
|---|---|---|---|
| MG | 0:00.0–0:03.9 | "They knock you out … electrocute you" | a small **motion graphic** telling people what this is: the therapy (ECT) she had after the s\*\*cide attempt |
| S1 | 0:03.9–0:05.8 | "I did nine sessions in three weeks" | the **album cover** (*Happiest Day of My Life*, the bite-guard image, the "very disturbing" one). Square art, framed the AW default way (his "full screen" note was about the close-up, below) |
| S2 | 0:20.1–0:21.3 | "And I was depressed" | **video of Paris actually crying**; letterbox only if the quality is low |
| S3 | 0:21.3–0:23.2 | "The side effects are gnarly. I mean, I definitely" | **video of Paris looking "unhinged"**: not dressed properly, looking weird |
| S4 | 0:30.2–0:32.1 | "There were some dark, dark times" | **Paris mourning her dad**. His fallback: the 2009 memorial, her speech and hugging Janet (**she was 11**, see Q1) |
| S5 | 0:34.7–0:36.5 | "I feel like it's still probably there" | **Paris singing in a booth / recording / playing an instrument**, highest quality possible |
| S6 | 0:38.4–0:41.0 | "the louder thing that competes is that I" | a **photo of Michael with his daughter** (**Paris as a child**, see Q1) |

Also, "this won't be letterboxed by the way, this will be in full screen, this one" (Tella 3:12–3:18): his playhead was at
0:10.47, on the On Purpose close-up ("inside of my head"). That close-up stays **full screen, no letterbox**. ET's punch-in
at "I did nine sessions" ("a built-in zoom, we can't do anything about it") is now under S1. Every overlay is picture
only, with its audio muted (brief rule 4: only Paris and Jay are heard).

### Transitions (named out loud per clip: "this will be X fading into this" = at that clip's out)
| # | Cut (his timeline) | From → to | Type (AW README § 7) |
|---|---|---|---|
| 1 | 0:03.90 | "…electrocute you" → S1 album cover | **Purple** (brightness dip to −90) |
| 2 | 0:05.77 | S1 → "The first time I woke up" | **Dark Green** (flash to +30) |
| 3 | 0:10.93 | B1 → Jay's question | **Purple** |
| 4 | 0:15.53 | Jay → Paris "I got very, very close" | **Dark Green** |
| 5 | 0:18.57 | "centimeters away" → B3 | **Purple** |
| 6 | 0:20.13 | "…every day" → S2 crying | **Purple** |
| 7 | 0:21.30 | S2 → S3 unhinged | **Cyan** (Gaussian blur 50 → 0) |
| 8 | 0:23.17 | S3 → "had days" | **Cyan** |
| 9 | 0:30.17 | B4 → S4 mourning | **Purple** |
| 10 | 0:34.70 | "…music was all I had" → S5 singing | **Purple** |
| 11 | 0:38.43 | "…back of my head, but the" → S6 photo | **Purple** |
| 12 | 0:41.03 | S6 → "feel like my dad would be proud" | **Cyan** |
Every other cut is a straight cut.

### Lip sync ("it's a bit unsynced … sync it with the lips", said twice)
**Measured: the ET On Purpose clip's audio is ~0.20 s (6 frames) LATE against her lips.**
- Two mouth measures agree (`win/lipsync.py` darkness, `win/lipsync_mesh.py` FaceMesh inner-lip gap): +229 ms raw on
  4 shots, against a +30…65 ms natural lead on RTT.
- A bilabial strip confirms it (`proof/bilabial_ect2*.jpg`). At "sharp pain" her lips close 0.2 s before the audio
  silence and open 0.21 s before the next vowel.
- The offset is the same on the raw mp4 and the `seq_src` copy (+7.0 frames weighted), so it isn't a decoder artefact.
  It is also on Jay's shot (+7.6 f, weaker r 0.19).
- Red Table Talk is in sync.
- **Build fix:** every ECT piece, Jay included, takes its picture **6 frames (0.200 s) earlier** than its audio. Prove it
  on the built file with a bilabial strip, and adjust to 5 or 7 frames only if that strip says so.

### Defects the build fixes (not taste); re-derive every V1 picture edge AFTER the slip
- **Re-derive edges after the slip.** It moves every ECT picture edge 0.2 s earlier, so frame-step each one again
  (`win/focus.py`, `win/fstep.py`) and hold the last or first clean frame wherever ET's own cut, graphic or blur shows.
  Known from the slip:
  - **B2 head:** picture 8.30 is about 6 frames of ET's previous shot, so hold Jay's frame 255 for ~6–7 frames, not 1.
  - **B4 "had days" head:** picture 50.467 sits inside ET's album-art dissolve (50.28–50.65), so hold the first clean
    frame (1518).
  - **B1 / B4 tails** now end before ET's flash (39.84) and blur (60.127), so those holds are likely moot. Check them.
- **B3's head** carries a word fragment (the tail of "and", heard as "Like"). Move the in-point a few frames to "people",
  measured.
- **Pauses:** his cut's longest quiet run is 0.28 s ("louder … thing", mid-phrase). Everything else is ≤ 0.23 s
  (`seqref/his_a1.wav`).

### Premiere access (shared ABW10, orchestrator 2026-11-02)
Every Premiere window is wrapped in the shared lock (`projects/_onyx-batch2-2026-10/.locks/premiere.lock`: mkdir with a
15 s retry, `owner` file, remove when done). Never overwrite an imported file. Don't run your own dialog closer
(`lanes/premiere/dialog-watch.py` does it). Full rule in RUN.md § Job facts.

### HIS ANSWERS (2026-11-02, with "Yes, build it")
- **Q1: "Use the childhood shots".** S6 is a photo of Michael with young Paris, and S4 may use the 2009 memorial (her
  speech, hugging Janet). This overrides the brief's rule 5 for these two slots only. No other minors appear (Willow is
  still never shown).
- **Q2: "Caption only".** The caption reads K\*LL MYSELF EVERY DAY (red), and the word stays audible, as on the Conrad
  Short. S\*\*CIDE is caption-only too.
- **Build go:** given, at the ~7–10 % quote.

### HIS REVIEW NOTE 1 (2026-11-03, on v1)
"both these images need to run through a serious higgsfield upscale before making it into the video". He sent finished
frames of **S3** (the paparazzi walk, "ARE GNARLY") and **S6** (the red-curtain photo, "THAT COMPETES").
- **S6:** Higgsfield `upscale_image` bytedance 4K (2 credits). 1259×1080 → 4096×3522, lanczos down to the played size
  (1217 px, scale 1.0) → `assets/mj_paris_redcurtain_hf.png`.
- **S3:** Higgsfield `upscale_video` Topaz 2160p 9:16 (5 credits) on the exact played crop (608×1080, x 686, source
  84.9–87.6 s of HDAIpjrL3X0). It came back 2160×3840 HEVC at 30 fps, then went lanczos to 1216×2160 H.264 →
  `dl/hf/S3_stroll_topaz_1216x2160.mp4`.
- **S3 still blew out under his grade:** the sunlit source runs hot, and his PRE sharpen bands crunch it. It now gets a
  pre-grade level (gain 0.66, gamma 1.08, pre-blur 1.0), on the precedent of Patrick's AMN09 (0.62 / 1.1). His grade
  itself is untouched.
- Credits: 1,072.75 → 1,065.75 (7 spent).

### CATALOG PASS (2026-11-02 ~19:30, BEFORE Stage A; CLAUDE.md learning loop 5)
Read `research/effects-catalog/CATALOG.md` (FX-01..81) and looked at all 137 reference stills
(`projects/conrad-murray-didnt-kill-mj/proof/catalog/page1-4.jpg`). The look stays HIS: AW glow bars, Gretaros captions,
purple / dark green / cyan transitions, his AE grade. The cut and the overlay slots are his. The catalog only feeds what
the brief and his Tella leave open: the ECT motion graphic, label motion, zooms and overlay framing.
- **Fits and used:**
  - **FX-72 / FX-70**, the single glowing line on black and the one-stroke mark: the ECT motion graphic's rule draws out
    from the centre as one glow line that jolts into a pulse spike (the "electro" stroke). It is drawn in his AW glow-bar
    stack, not the reference's orange.
  - **FX-42 Kin Tag** (name / role stack): the AW bottom labels (PARIS JACKSON · MICHAEL'S DAUGHTER, RED TABLE TALK ·
    2021).
  - **FX-33 Dust Void Drop / FX-08**, one artifact isolated and held: the album cover in his AW letterbox.
  - **FX-40 Slow-Burn Portrait:** the closing photo of Michael with young Paris, held 2.7 s with a slow AW push-in under
    "the louder thing that competes".
  - **FX-80 hard dip:** his purple −90 dips.
- **Fits, not used (why):**
  - **FX-27 Red Word Quote** on "kill myself every day": the brief makes it a red caption already, and a full-frame quote
    would cover her face.
  - **FX-43 Tape Morph** (young Paris to adult Paris at the S6 → B5 cut): it needs two stills matched on the eyes, his
    slot is a photo, and the hard cut on "proud" ends on her face.
  - **FX-46 / FX-56 CRT Witness** for the 2016 Instagram clip: his rule for low quality is the AW letterbox.
  - **FX-22 Red Isolate / FX-49 scanline skin** on the archive: not his Shorts vocabulary.
- **New on this channel / better than the last AW short:**
  1. The first animated EXPLAINER graphic in an AW code build. Earlier builds had labels and Patrick's opener card.
  2. Lip sync measured and corrected on the source: ET's audio is 0.2 s late, so every ECT picture is slipped 6 frames.
     No earlier short measured source A/V offset.
  3. Six real overlays that mix full screen and letterbox by source quality (his rule). Each window is frame-stepped
     clear of burned-in subtitles, bugs and channel logos.
  4. Freeze frames hidden under his flashes, wherever the slip exposes one of ET's own cuts.
- **What the last ones leaned on:**
  - Conrad: real footage only, the letterboxed courtroom, three-part lower thirds.
  - Patrick: restored stills and an opener card.
  - Kane: full-screen 4K overlays and green flashes.

### OVERLAYS PICKED (2026-11-02; every one muted, picture only)
| Slot | His timeline | Source | Window | Framing |
|---|---|---|---|---|
| MG | 0:00.20–0:03.60 | code-drawn | n/a | bottom card, see below |
| S1 | 3.90–5.77 | album cover *Happiest Day of My Life*, Apple 2000×2000 (long-form `hf-graphics/assets/img/ch6/`) | still | AW letterbox (still) |
| S2 | 20.13–21.30 | Paris's own Instagram video, Sept 2016 (age 18), via Inside Edition `N1Kf8jaqYO0` (720p) | ~8.6 s, wiping tears | AW letterbox (low quality, his rule). The band stops above Inside Edition's burned-in subtitles |
| S3 | 21.30–23.17 | X17 paparazzi, 2025 anniversary walk, via `HDAIpjrL3X0` (1080p60) | ~85.5 s close-up: messy hair, distressed | full screen, inside the inner vertical video (X17 / channel logos are in the pillars, out of frame) |
| S4 | 30.17–32.10 | 2009 memorial, his drive's CBS feed (`E:\Bullshit Folder\Henry\Michael Jackson Memorial Service…`, 1080p60) | ~9542.5 s, Paris crying at the mic (Q1: childhood OK) | full screen, crop on Paris (CBS lower third gone by 9539) |
| S5 | 34.67–36.47 | *teenage drama*, 101.9 KINK PNC Live Studio Session, Aug 2026, `5leMepqnrZg` (1080p) | ~25.3 s, close-up singing at the mic with guitar | full screen (no PNC logo in the close-up) |
| S6 | 38.37–41.03 | photo of Michael with young Paris (red curtain, his glove), frame of slideshow `5TCjs1NJU2I` (1259×1080 photo area) | still | AW letterbox (scale < 1, no upscale) |
Overlay starts follow HIS V2 clips (S5 34.6667, S6 38.3667), and each transition sits on the overlay's first frame.

**ECT motion graphic copy** (only what is said on camera; Jay names "the ECT therapy" and "a particular suicide attempt"):
`ECT` (white) / pulse glow rule / `ELECTROCONVULSIVE THERAPY` (gold) / `AFTER A S**CIDE ATTEMPT` (small).
It sits at the bottom label position (top y≈1262, under the caption line), and it fades out before the purple dip at 3.57.
The B1 label PARIS JACKSON · MICHAEL'S DAUGHTER moves to 6.05 s, after the S1 → B1 dark green flash, so the two cards never
stack in the 0–3 s hook.

### Questions for Affan (asked 2026-11-02)
- **Q1 — minors:** the brief's hard rule 5 is "no minors on frame, no childhood photos or footage of Paris". S6
  (Michael with his daughter) can only be Paris as a child, and so is S4's memorial fallback (she was 11). Use them
  anyway, or Michael alone for S6 (an adult photo) and adult footage only for S4?
- **Q2 — "kill myself":** censor it (audio + caption, or caption only), or leave it as the brief's red caption?
- Defaults unless he says otherwise:
  - no music (his rule; the Tella didn't mention it), captions at his ~55 % height, labels at the bottom;
  - ET's music bed stays under the RTT lines;
  - "suicide" becomes S\*\*CIDE in the captions only.

## Sources (decided 2026-11-02)
| Key | File | What it is |
|---|---|---|
| ECT | `raw/ECT_ET_OnPurpose_2026.mp4` | ET 19 Aug 2026 (`Qg9AG0nM58M`), clips of *On Purpose with Jay Shetty*. H.264 1920×1080 29.97, 81.7 s. Copied from `E:\Bullshit Folder\Henry\`, MD5 = the long-form's `broll/04` |
| RTT | `raw/RTT_ET_RedTable_2021.mp4` | ET 17 Jun 2021 (`pfADUCKKF0c`), *Red Table Talk*. H.264 1920×1080 29.97, 169.1 s. Henry copy, MD5 = long-form `broll/08` |

- **No better On Purpose copy exists.** The full episode is still not on YouTube (Jay Shetty Podcast channel: no Paris
  episode, 2 Nov). Every repost is ≤ 1080p and derived: TCP (`id_HQ2n_Tp8`) is stock footage, *MJ Unfiltered*
  (`TNgiEpbHHq0`) is commentary with zoomed crops. Both are kept in `dl/` and unused.
- **Format:** both used files are already H.264 (no AV1, no yt-dlp needed for them). Premiere gets `seq_src/*.mov`
  (H.264 CRF 12 + PCM 48 k, whole files, so ±3 s handles are automatic).
- **No cleaner Red Table Talk** either (fan uploads only; ET's 1080p is the best).

## Decisions taken in the raw cut (all flagged to Affan)
1. **Beat 3 = the brief's FALLBACK** ("It was really hard … I was depressed"). "…a lot of pressure" can't start clean
   (the "a" is fused to "and"). The words before "tell me" are quiet under ET's music: 3 of 4 re-listens hear
   **"people would tell me"**, 1 hears "let people tell me", and ET's captions said "totally". "kill myself every day"
   is clear in every pass. The long-form's lock 3 judged the same line not clean. Adding "a lot of pressure" back
   costs +1.2 s.
2. **Beat 4 keeps her FULL sentence**: "The side effects are gnarly. I mean, I definitely had days… completely not in my
   head at all. I'd have, you know, friends visit me, and I don't remember even seeing them." The brief's "gnarly …
   I'd have" would splice twice inside running speech: no silence at "gnarly/I mean" (under ET's music) and none at
   "all/I'd". So it isn't a clean cut. Exact words, and the brief's 0:50–0:59 range. The short version is NOT a
   one-move lift: it needs razors at timeline ~0:25.82 (source 0:50.02, after "gnarly") and ~0:30.42 (source 0:55.45,
   before "I'd"), which are exactly the two unclean joins. It saves ~4.6 s, so it runs ~42.9 s, under the 44 s floor.
3. **Beat 2:** she says "very, very close, like, [at,] like… centimeters away". The stutter is trimmed to ONE "like",
   and the 0.74 s pause is cut ("Trim filler"; rule 1). Whether that pause should breathe is his call.
4. **Pauses:** every gap over ~0.25 s is cut to ~0.2 s (Jay's 1.2 s, "out … strap" 0.66, "days …" 1.06, "day … And"
   0.9, beat 5's "some … dark, … dark" and "the … louder"). Nothing else is trimmed. Whole-output check on the assembled
   A1 (`win/gap_check.py`): the longest quiet run is **0.28 s** (mid-phrase, B5 "louder … thing", src 2:15.96). All
   others are ≤ 0.22 s.
5. **V2 covers (picture only)**, because ET's picture under the words can't be shown:
   - B3: ET's undated Instagram photo (long-form rule: never shown) and a Willow reaction → two Paris RTT close-ups.
   - B4 head: ET's album-art graphic → the On Purpose wide (Paris + Jay), then a Paris CU from another angle.
   - B5: three Willow reaction shots plus ET's "Thriller" card → three Paris RTT close-ups.
   - B1/B4 tails and B2's first frame: one-frame-exact HOLDS of the last clean frame, under ET's flash and blur
     transitions.
   - Covers come from unused Paris shots and are lip-mismatched by nature (mostly her looking down). They are
     placeholders for his direction.
6. **30 fps sequence** (his template is 60 fps): it was cloned, then set to 30.00 fps NDF. The rough fill crops follow
   faces. The two-shot under the Thriller card is slid right to keep the card out.

## Brief vs his standing rules — OPEN, for his answer in the Tella
- **Music:** the brief asks for a soft sad piano at −30 dB under B1–4. His rule (2026-10-27) is "music is his job":
  AW code builds ship with no bed. **Default: no music** unless he says otherwise. The raw has none.
- **ET's own music bed** is baked into the source audio under all of RTT (B3, B5) and under "The side effects are
  gnarly" (B4). It can't be removed by cutting; flag only.
- **Caption height:** the brief says 62–68 % (y1190–1306). His height is ~55 % (y940–1130, just under the lips), never
  lifting footage for it (2026-10-31). **Default: his height.**
- **Labels:** the brief calls for two: B1 "PARIS JACKSON · MICHAEL'S DAUGHTER" and B3 "RED TABLE TALK · 2021". It gives
  no position; his rule (2026-10-31) puts labels at the BOTTOM (card top ~y1260–1280, above y1620). In the raw they are
  in the beat markers only, not on-screen text. They are built as cards in the code build.
- **"Dry" ending:** the brief wants beat 5 "music out completely. Dry." But ET's music bed runs under ALL of the RTT audio,
  beat 5 included, so the ending can't be dry as cut. Only vocal isolation at build time could remove it. **Ask: try
  isolation, or keep ET's bed?**
- **V1/A1 only:** the raw also has V2. It holds 10 picture-only covers and holds (A2 empty), with V1/A1 untouched
  underneath, because ET's own picture under those words can't be shown.
- **Censoring:** "suicide" (Jay, B2) gets S\*\*CIDE in the captions only, audio as spoken (brief, matching his Conrad
  choice). **"kill myself" (B3)** falls under his rule to censor self-harm in audio AND captions, yet the brief makes
  KILL MYSELF EVERY DAY a red caption. **Ask: censor it (audio + caption, or caption only), or leave it?**
- **Words to settle by his ear** (the captions follow the audio):
  - B1: "**inside** of my head" (every ASR pass) vs the brief's "in the side of my head".
  - B1: "woke up **and** it was" (the "and" is spoken).
  - B3: "people would tell me" vs "they'd" vs "totally".
  - B4: a short unidentified syllable between "friends" and "visit" (kept).
- Brief typo: "aris on On Purpose" (beat 1) = Paris.

## Build (after his Tella, not before)
Code build per the AW flow (Stage A head lock, Topaz Proteus/Chronos as needed, finish.py grade/cards/captions, mix −14
LUFS / ≤ −1 dBTP on the encoded file, `.mov` to Final Renders + `X:\Claude Projects\Exports\`, §8 QA, REPORT.md).
Quote the cost first (recent builds: ~4–6 % of the weekly cap).
