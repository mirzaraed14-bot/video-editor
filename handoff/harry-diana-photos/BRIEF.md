# Harry Diana Photos — BRIEF (decisions)

AW Short **"Why Princess Diana's Son Asked To See Her Crash Photos 💔"**. The locked editor brief is
`X:\Claude Projects\Abundance Wisdom\HARRY-DIANA-EDITOR.md` (locked 1 Nov 2026; the file was already on disk, identical
to the pasted brief, so it was used as is). This file records every decision taken against it and every question still
open for Affan. State and next steps live in [RUN.md](RUN.md).

## Instruction (2026-11-02, via the orchestrator session)
Same flow as Paris Shock Therapy: "do the sequencing for premiere and await my direction video".

## HIS DIRECTION 1 (Tella "Video Editing Instructions and Overlay Guide", 2026-11-04 ~13:00)
`guide/tella1.mp4` (4:24, https://www.tella.tv/video/affans-video-0kjme74z); transcript `guide/tella1.json` (medium.en:
large-v3 was out of RAM, GPU busy). Every "here" is pinned to HIS timeline by the program-monitor timecode
(`proof/tella_tc_a.jpg`, `proof/tella_tc_b.jpg`).

**He re-cut the raw sequence himself: his cut is the spec** (`premiere/his_cut.tsv`, read-only dump; real source out =
inPoint + duration; never re-place over it). **41.63 s** (was 48.13): he dropped "she would never do this to us, but also"
(B2) and "smiling" (B6), cut the "pictures / showed" pause live, removed my end hold and B4 1-frame fix, and tightened
several heads by 1–4 frames. His A1, rebuilt from `seq_src/` (`win/his_a1.py` → `seqref/a1_his.wav`) and re-ASR'd
(`win/asr_his.json`), holds every word intact, from "the last thing Mummy saw…" to "…wiping away". **He marks every overlay
slot by lifting that V1 shot onto V2**:

| # | His timeline | Words | What he asked for (Tella time) |
|---|---|---|---|
| O1 | 4.43–8.57 | "the pictures showed the reflection of… a group of photographers" | "find pictures of exactly what Harry is describing here… just one overlay, exactly according to Harry's description" (0:31–0:59): photographers taking photos through a (car) window |
| O2 | 14.70–16.40 | "maybe this is all part of a plan" | "an overlay of Harry and Diana together when Harry was little… a happy overlay of them two together" (1:08–1:22) |
| O3 | 21.70–23.20 | "proof that she was injured" | "a picture of her injured… her being dragged into a hospital, or an ambulance, whatever" (1:50–2:07) |
| O4 | 29.13–30.90 | "all I saw was the back of my mom's head" | "Diana's back-of-her-head image, I think it's on the internet already" (2:18–2:40) |
| O5 | 33.97–36.33 | "and there we were shaking people's hands" | "from the memorial footage… Harry and William shaking hands" (2:42–2:58) |
| O6 | 36.33–39.90 | "and the wet hands that we were shaking, we couldn't understand why their hands were wet" | "another shot of Harry and William shaking hands with the people" (3:04–3:16) |

- Zooms and transitions: "you pretty much know what to do" (3:31) → the AW style of the recent builds.
- Quality: "use the highest quality overlay possible… it happened many years ago"; if only low quality exists,
  **letterbox it** (3:48–4:16). Sourced stills and clips also get the Higgsfield upscale (his 2026-11-03 rule).
- Not mentioned → defaults stand: no music, captions at his ~55 % height, labels at the bottom, Cooper's question and
  the Cooper-listening shot kept (he kept both in his cut).

### Conflicts with the locked brief — ASKED, not decided
1. **O2, O5, O6 show Harry and William as children** (O5/O6 are the 1997 walkabout). The brief's hard rule 5 bans exactly
   this ("no 1997 footage of 12-year-old Harry or William"). His Tella is newer and explicit. **Default: follow the Tella.**
2. **O3 "her injured / dragged into a hospital":** no such photo can be shown. Any photo of Diana injured is a crash photo
   (hard rule 6, a platform risk, and the brief's own "we describe, never show"). **Default: the ambulance and the
   Pitié-Salpêtrière hospital exterior from the night's news footage, with Diana not visible.**
3. **O4 "the back of her head":** the image Harry describes IS the crash photo. **Default: a pre-crash photo**, e.g. her
   in the back of the car leaving the Ritz that night: the back of her blonde head between bodyguard Trevor Rees-Jones
   and driver Henri Paul, taken minutes BEFORE the crash (60 Minutes broadcasts it at 3:03.5–3:06.8,
   `proof/m60_carphoto.jpg`; source a higher-resolution copy). Never the crash photo.
4. **Subscribe CTA** (not in the Tella): on his 41.63 s cut, mid 1 fits at ~16.0–18.8 (38–45 %: "I had huge amounts of
   hope" + Cooper's question, on face cam, no overlay). Mid 2's 70–80 % window (29.1–33.3) is all O4 + "slumped" + B6's
   label. **Default: ~26.3–29.1 (63–70 %, "…lying half dead on the backseat of the car")** unless he picks another spot.
   End screen: hard cut from "away" (his cut now ends on ITV's own 0.28 s dip to black) into the 4.0 s "Road to 1M".
   **His current subscriber count** goes into the end screen.

### HIS GO (2026-11-04): "Yes, defaults, build"
All six defaults above taken: children OK in O2/O5/O6 (his Tella over the brief's rule 5); O3 = ambulance / hospital
exterior, Diana never visible; O4 = the pre-crash Ritz photo; CTA mid 1 ~0:16.6, mid 2 ~0:26.2, end screen hard-cut in
after "away" (README § 12 now says the same, Affan 2026-11-04). No subscriber count given: the end screen keeps 540,000
(yesterday's number) and is re-rendered the moment he sends a new one. Higgsfield upscales approved within the quote.

### HIS REVIEW 1 (Tella 2 "Video Editing Review and Feedback", 2026-11-04 ~15:30, on v1)
`guide/tella2.mp4` (3:04, https://www.tella.tv/video/affans-video-f84b51a9), transcript `guide/tella2.json`, frames
`proof/tella2_sheet.jpg` (he plays v1 in a player). Fix ONLY these:
1. **"Why is the camera wiggling so much"** (0:02, the opening Harry shot; "the wiggle camera needs to be fixed"): the head
   lock followed every frame (sigma-3 smoothing). → One anchor per shot (its median nose; head level across cuts) where the
   head stays put; a slow follow (sigma 12 frames) only where the head really travels (Cooper turning). `build/smooth_track.py`.
2. **The 0.43 s Harry flash** between Cooper's "…in the pictures?" and the cameramen (0:04.0–0:04.43; "two milliseconds …
   use this person, slow him down … so that when he speaks we directly go into the cameraman bit"). → Cooper's shot runs
   0.8x from 0:02.9 to 0:04.43 and cuts straight to O1 when Harry starts "The pictures showed".
3. **Zooms "too intense … the curve is too strong … too poppy … I want a smooth, subtle zoom in which looks elegant …
   eased in"** (shown on "Mainly proof"). → Every block is ONE push-in, ~4 %/s capped at 8 %, on a sine ease in-out
   (`zoom_curve: ease`), never the front-loaded AW table, never a pull-out.
4. **The Road to 1M end screen "looks absolutely horrendous and cheap … skip this until you come up with a better one, but
   I don't need a better one for this video … fade out this video".** → No end screen; the picture fades to black over the
   last 0.6 s (41.03–41.63). The end screen is OFF for future Shorts too until a new design is approved.
5. **Subscribe prompts "at 21 seconds and 35 seconds".** → mids at 0:21.0 and 0:35.0.
Unchanged: the cut, overlays, captions, grade, labels, mix levels.

### HIS REVIEW 2 (text, 2026-11-04 ~17:15, on v2)
"You're missing the plot ... analyze how my Shorts do zoom ins and outs ... all my shorts have a zoom which basically acts as
a transition zoom ... it starts strong, it loses its intensity, but it picks up its intensity at the end of the shot so that
... it directly goes into the next clip, and obviously the next clip will have the same intensity, so it feels like it's
zooming in to the next shot ... do frame by frame analysis ... the short looks fine, although there are some weird artifacts
because of the Topaz ... you have to fix these things before I publish it."
1. **Zooms = his transition zoom, measured** (`win/his_zoom.py` on ABW6 03, ABW8 34, ABW8 39, Martin Final; numbers in
   `win/hiszoom/`): start +30..+65 %/s, middle +2..+9 %/s, end +15..+30 %/s into the cut, totals +15..+45 %, ~80 % push-ins,
   pull-outs come in runs (never flip-flopping), and EVERY cut restarts at 1.00, same-camera jump cuts included (4 of 4
   joints: −13, −13, −28, −13 % size steps). v1 had his curve but pulled out on 8 of 23 blocks (the reversals he heard as
   "poppy"); v2's sine ease removed the transition. → v3: one push-in per shot on README § 3's table, v1's depths
   (+16..+25 %), no start faster than his fastest (~70 %/s) on the 0.37 / 0.70 s jump-cut pieces, O3 held (the AP clip
   zooms +92 % by itself).
2. **Topaz artifacts:** the raw Topaz files are clean; his PRE sharpen bands + Sharpen 40 turn their smooth surfaces into a
   painted look (O1 faces, O3 ambulance, O5/O6 crowd faces, dark halos on the ITV5/ITV10 Harry shots). → soften before the
   grade (`pre_blur`) + grain on those shots, picked from test frames (`work/v3test/`).
Unchanged: the cut, overlays, captions, transitions, CTA, grade, labels, mix.

### HIS REVIEW 3 (text, 2026-11-04 ~19:45, on v3)
"If the shot is the same you will not introduce a new zoom layer on it. You literally did it in the first few seconds when
Harry says 'yep' ... it just looks weird if we're zooming in and then we zoom out and then zoom again on the same shot ...
when the shot changes to another person or to an overlay, that's when you introduce another zoom layer, not when they finish
their sentence." → a same-camera jump-cut run (same source + setup) is ONE zoom layer: 0–2.90 (through "yep"),
23.20–29.13, 31.83–33.97 (ITV). 20 layers (was 24). Everything else as v3.

### CATALOG PASS (2026-11-04, BEFORE the build; CLAUDE.md learning loop 5)
Read `research/effects-catalog/CATALOG.md` (FX-01..81) in full and looked at all 137 reference stills
(`projects/conrad-murray-didnt-kill-mj/proof/catalog/page1-4.jpg`). The look stays HIS (AW glow bars, Gretaros captions,
his purple / dark green / cyan transitions, his AE grade); his cut and his six V2 overlay slots are the spec. The catalog
only feeds what he left open ("zooms and transitions, you know what to do") and the overlay treatment.
- **Fits and used:**
  - **FX-40 Slow-Burn Portrait** on O4: the pre-crash Ritz photo (the back of her head in the car) held with a slow AW
    push-in, no text, under "all I saw was the back of my mom's head".
  - **FX-29 Float Frame / FX-08 Black Table Tiles**, archive never full-bleed: every 4:3 archive overlay (1987 ITN, the
    1997 walkabout) goes in his AW letterbox band (his Tella: "if the footage is really low quality, letterbox it").
  - **FX-42 Kin Tag**, the bottom labels: PRINCE HARRY · DIANA'S SON (B1, after the hook, on Harry) and ITV · 2023 (B6).
  - **FX-80 Black-Beat Ident:** B6 (ITV) opens on ITV's own fade up from black, kept as the chapter turn into the ending;
    no extra transition on it.
- **Fits, not used (why):**
  - **FX-27 Red Word Quote** on "half dead on the backseat": it would cover his face on the line that has to land on him.
  - **FX-43 Tape Morph** (little Harry → adult Harry at O2 → B3): needs two stills matched on the eyes; O2 is moving
    archive and B3 is synced speech.
  - **FX-37 Ghost Dissolve** into O2: his transitions are dips and flashes; a 1–2 s double exposure would eat the 1.7 s slot.
  - **FX-22 Red Isolate / FX-49 Scanline Skin** on the archive: not his Shorts vocabulary (as on Paris).
- **New on this channel / better than the last AW Short:**
  1. The first AW Short with the subscribe CTA (two mid prompts + the Road to 1M end screen).
  2. The first non-Jackson mega-celebrity: two broadcasters (60 Minutes 29.97 fps, ITV 720p 25 fps) graded into one look.
  3. Archive picked by the BEST copy, not the first: 60 Minutes' 1080p transfer of the 1997 walkabout instead of ITV's
     720p, every window frame-stepped clear of bugs, lower thirds and the crash footage.
- **What the last ones leaned on:** Paris: six overlays + the ECT explainer graphic + his named transitions. Conrad: real
  footage only, letterboxed court. Kane: full-screen 4K overlays.

### OVERLAYS PICKED (2026-11-04; every one muted, picture only, all in his AW letterbox band)
| Slot | His timeline | Source | Window | Why |
|---|---|---|---|---|
| O1 | 4.43–8.57 | Smithsonian Channel, *Diana and the Paparazzi* (`qRB5UFJLVV0`, 720p) | 123.20–127.33 (ends before its promo card at 127.67) | the paparazzi pack, cameras up: "a group of photographers taking photographs" |
| O2 | 14.70–16.40 | ITN, Mallorca 1987 (his drive `E:\Bullshit Folder\Drake987- 'Bye!'…`, 1080 pillarbox SD) | 49.35–51.05 | Diana with little Harry (2) on her lap, both smiling; ITN logo cropped out |
| O3 | 21.70–23.20 | AP Archive, first reports 31 Aug 1997 (`e40n9H3SVdY`, 360p) | 92.60–94.10 | the SAMU de Paris ambulance with blue lights, at the hospital; no car, no Diana, every wreck frame out |
| O4 | 29.13–30.90 | 60 Minutes (raw 60M) | still at 184.5 | the PRE-crash Ritz photo: the back of her head between Rees-Jones and Henri Paul; FX-40 slow push-in |
| O5 | 33.97–36.33 | 60 Minutes "found out" upload (his drive, 1080 pillarbox SD) | 70.25–72.62 | Kensington walkabout 1997: Charles, William, Harry shaking hands across the barrier |
| O6 | 36.33–39.90 | same | 76.70–80.27 (a frame before its next shot) | hands + a woman wiping tears, then William and Harry shaking hands at the barrier |
Each is the exact played crop (square, native pixels), upscaled by Higgsfield (Topaz video 2160p ×5, bytedance image 4K ×1;
27 credits) and lanczos'd to 1080. Rejected: AP night tunnel footage (the car is in it), a Getty-watermarked flash clip,
The Crown's crash scene (drama + crash), his drive's `xxDianaLastYear5` (a crash photo), ITV's 720p walkabout (60M's
transfer is sharper, its logo outside the picture).

## Sources (decided 2026-11-02)
| Key | File | What it is |
|---|---|---|
| 60M | `raw/60M_Harry_2023.mp4` | 60 Minutes (CBS), "Prince Harry refused to accept Princess Diana's death for years", uploaded 9 Jan 2023 (`NtJzkpy-Rcs`). H.264 1920×1080 29.97, 227.5 s. yt-dlp format 270+140 (avc1, the best there is) |
| ITV | `raw/ITV_Harry_2023.mp4` | ITV News, "Prince Harry speaks of 'guilt' he felt after Diana's death in latest ITV trailer", 7 Jan 2023 (`7rMzHiegIKA`). H.264 **1280×720 25 fps**, 133.9 s. yt-dlp 232+140: **720p is the best YouTube has** |

- His drives: `E:\Bullshit Folder\Drake\` already holds the same 60 Minutes upload (same length and bitrate, a different
  download). The fresh yt-dlp copy is used; it is no worse. No ITV copy on his drives.
- Premiere gets `seq_src/*.mov` (H.264 CRF 12 + PCM 48 k, whole files, so ±3 s handles are automatic). ITV stays at its
  native 25 fps inside the 30 fps sequence.

## Picture hazards found in the sources
- **60M 43.3–59.0 s: the wrecked Mercedes** (crash-scene images, hard rule 6). Beat 3 ends just before it; never on screen.
- 60M 99.7–102.8: the tunnel at night WITH cars; 153.3–155.9 tunnel with a car; 155.9–159.7 tunnel interior, no car.
- 60M 175.1–178.9: adult Harry + William (fine, adults); 183.5–186.8 Diana's car photo (never).
- **ITV 30.5–47.12 and ~59.2–76.0: 1997 footage (flowers walkabout, children Harry + William)** — hard rule 5 (frame-
  stepped: the walkabout fades to black 46.88–47.12 and Harry fades up 47.16–47.64; the 1997 run ~59.2–75.04 dissolves
  into the wide 75.04–76.00). Beat 6's words over it get V2 covers of adult Harry from the same ITV interview.
- Bugs: 60 MINUTES top-left (x ≤ ~0.08, y ≤ ~0.09); ITV NEWS top-right (x ≥ ~0.88). Both outside a face crop.

## Decisions taken in the raw cut (all flagged to Affan)
1. **Runtime 48.13 s, under the brief's ~60 s (56–64 s).** The brief's own words, with every pause over ~0.25 s cut (hard
   rule 1), run ~48 s; its per-beat estimates (14/13/3/14/4/14 s) are source ranges before trimming. Nothing was
   added to pad it. Ways to add length if he wants it: Harry's "Yeah, hope." before B3 (+0.6 s); keep Harry's pauses (B6
   "I cried once, … at the burial" had 1.0 s; against rule 1); or a line the brief left out (60M "Years. Many, many
   years.", ITV "Everyone thought and felt like they knew our mum…").
2. **B1 starts exactly on "the last thing Mummy saw"**: the cut sits in the 5 ms "t" closure of Cooper's "that". The
   QA box's first words are met (A1 re-ASR: "the last thing…").
3. **B1: "Mm-hmm" and a "Well, the—" false start trimmed.** Harry says "Well, the— [0.4 s] the pictures showed": "Well,
   the" is one voiced run with no gap, so the line starts "The pictures showed…" (exact words otherwise). His "Yep"
   (the brief writes "Yeah"; ASR hears both) is kept.
4. **B1 ends on "through the window"**: "and the reflection of the window was them" is dropped (the brief allowed it;
   it starts 60 ms after "window").
5. **B2:** "Part of, you know," and the second "part of" are trimmed (the brief's ellipses). Under "I just refused to
   accept that she was gone" 60 Minutes cuts to **Cooper listening** (2 s): kept (synced, allowed person); the brief
   says "Picture: Harry", so cover it with a Harry shot if he wants Harry only.
6. **B3 ends 10 ms before 60 Minutes cuts to the crash wreckage** (43.277). Only the breath after "hope" is lost.
7. **B4 includes Cooper's "Why did you want to see it?"** (clean: the narration ends 0.4 s before it; a mouth click
   is left out). One razor removes it (−1.0 s) if he'd rather start on "Mainly proof".
8. **B6:** "um" (between "once" and "at"), "and I go into detail… to our mother", and "I've seen the videos, right? I
   look back over it all." are trimmed. "smiling" runs straight into "I've" with no silence, so that cut sits on the
   "ng" tail (A1 re-ASR: clean). HARD CUT on "away".
9. **B6 picture:** ITV plays 1997 footage of the boys under "And there we were… smiling" and under the first half of "the
   wet hands…" → V2 covers of adult Harry from the same ITV interview (lip-mismatched placeholders, like Paris). The
   synced picture is kept where it exists: the CU for "I cried once at the burial" (after ITV's own fade-up from black)
   and the wide for "…tears that they were wiping away". ITV fades to black under "away", so the last 0.33 s is a hold
   of the wide's last clean frame (the cut stays hard).
10. **Optional inserts not placed:** the tunnel exterior (B4) and adult Diana "over 'our mother'" (B6). "our mother" is
    in a part the brief itself trims, so that insert has no anchor.
11. **30 fps sequence** (his template is 60 fps), cloned then set to 30.00 fps NDF. The crops are rough fill-height crops
    on the face. Both bugs are outside every crop. ITV's lower-third "'HARRY: THE INTERVIEW', ITV1" shows at the bottom
    of "at the burial".
12. **Labels** are in the beat markers only (B1 "PRINCE HARRY · DIANA'S SON", B6 "ITV · 2023"), to be built as cards
    at the bottom.

## Brief vs his standing rules — OPEN, for his answer in the Tella
- **Music:** the brief asks for a soft piano at −30 dB under B1–4, out from B5. His rule (2026-10-27): music is his job,
  and AW code builds ship with no bed. **Default: no music.** The raw has none.
- **Caption height:** the brief says 62–68 % (y1190–1306). His height is ~55 % (y940–1130, just under the lips), and
  footage is never lifted for it (2026-10-31). **Default: his height.**
- **Labels:** the brief gives no position. His rule (2026-10-31) puts them at the BOTTOM (card top ~y1260–1280, under
  the captions, above y1620). **Default: bottom.**
- **Runtime** (decision 1): 48 s vs the brief's ~60 s.
- **B2 Cooper listening** (decision 5) and **B4 Cooper's question** (decision 7): keep or change?
- **Words to settle by ear** (the captions follow the audio): B1 "Yep" vs "Yeah"; B5 "mom's" (ASR also hears "mum's").
- **Subscribe CTA (his rule 2026-11-03; this is the first Short to ship it):** (a) the brief's hard rule 7 says "No end
  card", but the CTA adds a subscribe end screen. **Default: hard cut from "away" straight into the end screen.** (b) The
  second mid prompt's 70–80 % slot falls on B5 "the back of my mom's head". Keep it there, or move it earlier to B4's tail
  (~64–70 %)? Details: RUN.md § Subscribe CTA.

## Hard limits checked (raw)
- No crash photos or crash-scene images on screen: 60M's wreckage (43.28–59.03) and Diana's car photo (183.5–186.8)
  are never used; B3's out is 10 ms before the wreckage. ✔ (`proof/sim_readback.jpg`)
- No 1997 footage of child Harry or William on screen: every span under Harry's words is covered on V2. The covered
  clips still sit on V1 underneath (deleting a cover would show them). ✔
- Only adult Diana: no Diana footage is used at all. ✔
- Clip edges: 60M and ITV were frame-stepped at every used edge (cuts, dissolves, fades). No promo frames, no narrator
  frames, and no reporter audio (A1 re-ASR). ✔
