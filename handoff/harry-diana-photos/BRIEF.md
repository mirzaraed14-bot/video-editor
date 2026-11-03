# Harry Diana Photos — BRIEF (decisions)

AW Short **"Why Princess Diana's Son Asked To See Her Crash Photos 💔"**. The locked editor brief is
`X:\Claude Projects\Abundance Wisdom\HARRY-DIANA-EDITOR.md` (locked 1 Nov 2026; the file was already on disk, identical
to the pasted brief, so it was used as is). This file records every decision taken against it and every question still
open for Affan. State and next steps live in [RUN.md](RUN.md).

## Instruction (2026-11-02, via the orchestrator session)
Same flow as Paris Shock Therapy: "do the sequencing for premiere and await my direction video".

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
