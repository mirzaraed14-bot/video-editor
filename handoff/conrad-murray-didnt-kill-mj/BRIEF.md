# BRIEF: "WHY CONRAD MURRAY SAYS HE DIDN'T KILL MICHAEL JACKSON 😳" (Abundance Wisdom short)

## ▶ STATUS: resume here (2026-10-31 ~18:30): DELIVERED `Conrad Murray Guilty.mov` (49.37 s) after his Tella (DECISIONS 15–24); at his review (RUN.md, REPORT.md)
- Sent: `X:\Claude Projects\Exports\Conrad Murray Guilty - SEQUENCE PREVIEW.mp4` (= `seq/preview.mp4`, 49.23 s, censor
  default ON) + `… SEQUENCE PREVIEW (beat 5 uncensored).mp4` (8 s). In/outs: `seq/inout.md`. What the sources forced:
  DECISIONS 8–14 below (all visible in the preview, all his call).
- His answers so far: DECISION 1 → caption DR*G ADDICT, "drug" audible (no bleep). 8, 10, 13, 14 still open (they can
  come with the Tella).
- His order (2026-10-31): "i want to give a creative direction video on this first before the edit". So: download → lock
  every in/out by ear → **sequence preview MP4** (plain cut, words + order, no Premiere) → **STOP, wait for his Tella** →
  resolve every note here as its own DECISION (Tella time + the frame that resolves it) → only then the full code build.
- When the Tella arrives: `memory/feedback-walkthrough-videos.md` (curl the page, never open it in a browser; m3u8 →
  ffmpeg -c copy → `brief/tella/guide.mp4`; ASR a highpass+dynaudnorm copy) → frames at every "this/here" → DECISION 15+.
- Template job: `projects/patrick-stewart-father-angry/` (same kind of locked YouTube brief, built in code 2026-10-31).
- Started by session local_3ae3a4cf (parent). Shared notes: `C:\Users\affan\AppData\Roaming\Claude\side-session-notes\local_3ae3a4cf-7107-4cdf-a50e-e1b313072860\`.

## DECISIONS (defaults stated to him 2026-10-31; he can override with a word)
1. **Drug-word censor: CAPTION ONLY, his answers (2026-10-31, after the preview): "do it like dr*g addict", then "Audible,
   caption only".** His standing rule (`memory/feedback-censor-sensitive-words.md`, 2026-10-27) censors audio AND captions;
   on this Short he narrowed it: B5's red caption = **DR*G ADDICT** (asterisk in the word, the AW S*X / F*CK form) and
   **"drug" stays AUDIBLE** — no bleep (`seq/edl.py` BLEEPS = []; the preview file still carries the bleep, the build does
   not). B3 label stays DR. STEVEN SHAFER · ANESTHESIA EXPERT · MURRAY TRIAL, 2011 (the stated default; he didn't object).
2. **Music: none.** His standing rule (`feedback-music-is-his-job.md`; Patrick DECISION 1). § 5's tense pulse, the hard
   stop on "guilty" and the B5 re-entry are N/A. Soft SFX on transitions stay (19–23 dB under the voice).
3. **Caption line: HIS height (y≈1060, ~55 %, on the speaker's lip line)**, not § 6's 62–68 % (Janet v1 at 64 % was moved
   up by his review; Kane he answered "his height"; Patrick DECISION 3). Still inside § 6's safe zones. Style = the AW
   caption engine (1–3 words per caption, colour MIX, README § 8), as on Patrick, for § 6's "word-by-word … recent MJ style".
4. **Sources: his drives first, then yt-dlp with H.264 (avc1) forced** (YouTube worked 2026-10-31). He said "download
   everything yourself" on Patrick.
5. **SD upscale (trial footage, KATPM 360p): Topaz Proteus, never Iris** (Iris is face-aware = the brief's banned AI-face
   class). Every Topaz output checked for the lapsed-login WATERMARK.
6. **Delivery: 30 fps, −14 LUFS integrated, ≤ −1 dBTP measured on the ENCODED file; cool/tense grade B1–5, warm for
   Katherine (B6).** The brief wins over earlier AW defaults (60 fps, −15.3 LUFS).
7. **Catalog pass** (CLAUDE.md learning loop 5) only for what the brief leaves open: label/card motion, caption
   animation, zooms, transitions. The cut itself is locked.

### Found on the sources (sequence preview, 2026-10-31 ~13:10; each shown in the preview, his call)
8. **Beat 5 speakers are not all Murray.** Voice match (`win/who.py`: MFCC GMMs trained on known Hayes / known Murray
   speech from the same 60M recording; LLR Murray−Hayes): "None." +5.1 = MURRAY · "None?" −3.8 = HAYES · "Absolutely
   nothing?" −6.2 = HAYES (she is on camera from 17:27.88) · "Nothing." +2.3 = MURRAY. The brief (from YouTube captions)
   gives all three to Murray. Preview: the brief's words AND Murray's own "Nothing." (0.57 s) so his answer is his; drop
   it with a word (→ 48.66 s). Captions will set Hayes's lines in the interviewer italic.
9. **Beat 1: Hayes is on camera for her whole line** (10:14.08–10:18.72). Brief: frame 1 = Murray's close-up → Murray
   listening, the shot just before (10:10.68–10:14.08) at 0.8x under her line; his denial plays in sync.
10. **Beat 2: the 911 clip opens on an EXTRA MINUTES title card (to 0:02.52) and shows Hayes over Murray's "I had my cell
    phone" and both "Yes".** Preview: B1's Murray shot runs on 0.43 s under her first words (no title frame); Murray
    listening shots (60M 13:08.44, 13:10.40, 13:11.60, mouth closed) under his three answers; "I did not call 911" in sync.
11. **Beat 5 picture ("Murray, tight"):** one continuous Murray listening shot (60M 16:30.76) under her whole question, so
    the AFTER PRISON, 2013 card sits on HIM (first try put it on Hayes's face, caught before sending) → his "None." in sync
    (17:25.31) → "None?" on his reaction → Hayes ~0.9 s over "Absolutely nothing? / Nothing." (= the brief's Hayes
    cutaway, hides the join) → Murray "Michael Jackson … is a drug addict" with a 3-frame dissolve on the trim. **The trim is clean** (`win/join_test.py`: reads "Michael Jackson is a
    drug addict"; the cut at 9:58.72, before "as" at 9:58.75; 9:58.62 clipped it to "Jack").
12. **KATPM copy: Absolutely Definite part 2/5 (`2WOCXNNunfk`, 720p), 3:01.57–3:08.31**, the same broadcast as the 360p
    wh3po5ErEh0 (part 1 doesn't hold the passage). Hard cut 0.09 s after "again"; "but" starts 0.6 s later.
13. **Rule 1 tightened the dramatic pauses** (every pause > 0.30 s → ≤ 0.2 s): Hayes's hook, Shafer's long pauses (27 s of
    source → 14.2 s), Katherine's 1.0 s + 0.8 s. Ask: Katherine's pauses back (+~1.4 s, still ≤ 52 s)?
14. **(→ resolved by DECISION 16)** **SD vs "full bleed, don't punch past ~120 %":** a 9:16 slice of the 360p Shafer footage is 202 px wide (5.3x to fill
    1080); the crop adds 1.24x only to drop CNN's lower third. Build plan: Topaz Proteus (DECISION 5), full bleed as the
    brief says (his AW letterbox for low-quality inserts is the fallback if he prefers it).

### His creative-direction Tella (2026-10-31 ~15:40; `brief/tella/guide.mp4`, 5:13, transcript `brief/tella/guide.json`,
### frames `proof/tella/sheet0.jpg` + `sheet1.jpg`; he plays the SEQUENCE PREVIEW, whose top-left timecode = preview time)
Supersedes the brief and DECISIONS 1–14 where they differ. Each note → what it resolves to.
15. **B2: the reporter stays on screen unless Murray is visibly saying it** (tella 17–72; frames tella 17/24/30 = preview
    6.7–7.6 Murray listening under "I had my cell phone", tella 66 = preview 13.1–13.5 / 15.1–15.5 under the "Yes"es): "if
    the camera shot is not actually at him it's not worth it, you should just keep it at the reporter" · "this is good
    because he's actually saying it" (tella 39–44, preview 9.5 "I did not call 911"). → The three Murray listening covers
    go; the source picture (Hayes) stays under "I had my cell phone" and both "Yes"; Murray only on his in-sync line.
    DECISION 10's covers are void (the B1→B2 title-card cover stays: it is B1's own Murray shot, not a silent face).
16. **Shafer (B3) = LETTERBOX, zoom IN, no head track** (tella 74–78 "this video will be letterboxed because this is very
    low quality", tella 108–112 "this will not be a track by the way because this will be in the letterbox", tella
    282–288 "this part when you letterbox it this will be zoomed in"; frames tella 76 / 104 / 110 / 286 = preview
    15.5–29.6). The IV-demo cutaway (same 360p HLN) letterboxed with it. → AW letterbox (README § 4: 100 % native band +
    198 % twin fill at 43 % + glow bars; Kane O6 recipe), push-in.
17. **Labels = animated motion-graphic lower thirds from the BOTTOM, never top** (tella 78–93 "should be placed at the bottom
    not at the top and it should have like a little nice animation which feels integrated with my whole abundance wisdom
    style, it shouldn't just look separate"; again tella 208–227 + 303–310; frames tella 5 / 258 / 305 = the top labels in
    the preview). → Patrick's lt_card (NAME / hairline / gold line rising in under the caption line over a soft scrim, AW
    glow-bar rule), for all four: CONRAD MURRAY · MICHAEL'S DOCTOR · 2013 / DR. STEVEN SHAFER · ANESTHESIA EXPERT · MURRAY
    TRIAL, 2011 / AFTER PRISON, 2013 / KATHERINE JACKSON · HIS MOTHER · 2012. Above the bottom-20 % safe band.
18. **Verdict (B4) = full bleed ("the quality here is fine"), HEAD-TRACKED, zoom IN** (tella 112–125, 288–293; frames tella
    116 / 123 / 291 = preview 29.6–36.5).
19. **B5: Hayes on screen while Murray's voice would play over a silent Murray; back to Murray "when he's actually saying"**
    (tella 125–178; frames tella 128 / 135 / 150 / 165 / 174 = preview 36.5–41.0: my Murray listening cover + Murray eyes
    closed on "None"): "when he speaks and he is shown like he's silent it's just awkward … better that you just pan the
    camera to the reporter … then you can pan the camera back when he's actually saying" (he then plays "Absolutely
    nothing. Nothing. Michael Jackson is a drug addict"). → B5 picture: Hayes (her own shot, in sync) on "What
    responsibility do you take", Hayes on "For his death? / None. / None?" and on "Absolutely nothing? / Nothing.", Murray
    in sync on "Michael Jackson … is a drug addict". DECISION 11's Murray cover is void. **His "both of them are
    overlapping" (tella 142–155): they are not, in the source or the cut** — Hayes's "death" ends 17:24.93, Murray's "None."
    starts 17:25.39 (0.46 s apart); rule 1 brought it to ~0.2 s. Said in the report.
20. **"You ended it halfway of him saying the name"** (tella 181–191; frames tella 186 / 190 = preview 42.4–43.2): the
    B5 trim clipped "Jackson" (my level-dip override 9:58.72 sat inside the "-son"; ASR join tests fill the word in and
    missed it). → re-measured edge (see RUN); the brief's fallback (keep "as you have realized now") if no clean edge.
21. **Katherine (B6) = LETTERBOX, zoom IN** (tella 203–208 "this Catherine video will also be letterboxed", tella 300–303
    "this Catherine bit will be zoomed in because it will be letterbox"; frames tella 200 / 205 / 305 = preview 44.3–49.2).
    No head track (his Shafer rule for letterboxed shots).
22. **Caption colours: white + ONE accent per caption, gradient, varied through the short: blue, pink, orange, red, green,
    PURPLE** (tella 227–249: "it's not like red only … white and blue, white and pink, white and orange, white and red,
    white and green, white and purple … there shouldn't be two colors"). README § 8 Colour MIX + purple added.
23. **Transitions: my call in his vocabulary** (tella 249–254 "you have basic idea of like how the transitions work").
24. **Zooms: the 60 Minutes parts (B1, B2, B5) ZOOM OUT; letterboxed parts (Shafer, Katherine) and the verdict ZOOM IN**
    (tella 253–303: "this is too zoomed in already … majority of the bits and clips here will be zoomed out instead of zoom
    in … we're going to start with a zoom out here" on B1; "you had your cell phone, this will be zoomed out as well";
    "all of the 60 minutes parts will be zoomed out"; frames tella 258 / 263 / 268 / 276 / 281 / 296). → pull-outs that END
    on the full-bleed frame (z 1.0), BlurMoCurves curve (README § 3), never a push past the native crop on 60M.
- **Not mentioned = stands:** DECISION 8 (Murray's own "Nothing." stays: he played "Absolutely nothing. Nothing." without a
  note), DECISION 13 (pauses tightened per rule 1), DECISION 12 (KATPM 720p part 2), DECISION 1 (DR*G, audible).

## CATALOG PASS (2026-10-31 ~17:50; CLAUDE.md learning loop 5)
Read `research/effects-catalog/CATALOG.md` (FX-01..81) and looked at all 137 reference stills (`proof/catalog/page1-4.jpg`).
**Honest timing note:** this section was written DURING the build (Stage A done, before the finish render), not before the
first edit as the rule asks; it confirmed the moves in use and added none. Next AW job: write it before Stage A.
The look stays HIS (AW README: glow bars, Gretaros captions, purple / cyan / peach transitions, his AE grade layer); the cut
is locked; the catalog only feeds what the brief + his Tella leave open (label motion, caption animation, zooms, transitions).
- **Fits and used:** FX-42 Kin Tag (NAME / role / relation-to-the-subject stack) = the lower thirds (CONRAD MURRAY ·
  MICHAEL'S DOCTOR · 2013, KATHERINE JACKSON · HIS MOTHER · 2012) in his AW form at the bottom (his Tella). FX-58
  Speaker-Coded Subs = his own italic-for-the-interviewer rule (Hayes italic, the subjects upright). FX-48 / FX-14 cold
  plates = the brief's cool, tense B1-5 grade against the warm Katherine ending (FX-79-like grade contrast). FX-40 Slow-Burn
  = the slow push-ins on the letterboxed Shafer and on Katherine. FX-80 hard dip = his purple -90 dips at the scene changes.
- **Fits, not used (why):** FX-27 Red Word Quote / FX-18 Karaoke Quote on "inconceivable" (a full-frame quote would cover
  Shafer on a line the captions already carry). FX-46 / FX-56 CRT Witness for the 360p trial footage (his Tella chose his
  AW letterbox for low quality). FX-54 Dark Headline Card for the verdict (non-spoken text the brief doesn't list; the clerk
  + GUILTY carry it). FX-75 Scorebug Punch-In on CBS's bug (cropped out instead). FX-37 Ghost Dissolve (not his Shorts
  vocabulary).
- **New on this channel / better than the last AW short:** (1) labels as AW glow-rule lower thirds drawn in three parts
  (rule from the centre, name rises, role/year follow), from the bottom, his ask; (2) the picture follows who is VISIBLY
  speaking (his note): the reporter whenever Murray would be a silent face, and a wide two-shot as a shot-size change
  instead of a Hayes-to-Hayes jump; (3) face heights set per same-camera run from MEASURED mouths (open mouths included)
  so the caption line never sits on a lip, and the exposed bottom is a soft vignette fill, not a mirror; (4) caption MIX
  with a sixth accent, purple (his Tella).
- **What the last ones leaned on:** Patrick: restored father stills + an opener card drawn from his head; Kane: full-screen
  4K overlays + green flashes. Here: real footage only (no stills, no AI anything), letterbox only where he said
  (the 360p courtroom and the CNN Katherine).

## HIS BRIEF, VERBATIM (v3, locked 31 Oct 2026)

EDITOR BRIEF: "WHY CONRAD MURRAY SAYS HE DIDN'T KILL MICHAEL JACKSON 😳"
Channel: Abundance Wisdom · Format: YouTube Short, 1080×1920 · Locked: 31 Oct 2026 (v3, Affan's final order)
The creative is locked. Cut it exactly as written. If anything can't be done exactly as written, stop and tell Affan before improvising.
What this Short is: Murray denies it → admits he didn't call 911 → the expert calls that inconceivable → GUILTY → he still takes no responsibility and calls Michael a drug addict → Michael's mother.
Target runtime: ~48s (45–52s), measured on the timeline.
1. HARD RULES (any one broken = redo)

1. Someone is speaking at every moment. No gaps over ~0.25s.
2. Source audio only. No voiceover, TTS, AI voices or AI faces.
3. Exact words only. Trim filler inside a range. One approved join: beat 5 links two answers from the same 60 Minutes interview (see beat 5).
4. Voices allowed: Liz Hayes (60 Minutes), Conrad Murray, Dr. Steven Shafer (court), the court clerk, and Katherine Jackson. No anchors, no narration.
5. No minors on frame. No photos or footage of Michael's children.
6. Never "Demerol" anywhere.
7. Hard cut on "I'll never see my son again." No end card, no music tail.

2. SOURCES (download first)

```
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "60M_Murray_2013.%(ext)s"         https://www.youtube.com/watch?v=Sa2taDu2W5A
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "60M911_Murray_2013.%(ext)s"      https://www.youtube.com/watch?v=M7TZWLflW54
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "SHAF2_Shafer_court_2011.%(ext)s" https://www.youtube.com/watch?v=Xv6vWTkEdU4
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "SHAF_demo_court_2011.%(ext)s"    https://www.youtube.com/watch?v=fcbX7wIbgKU
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "VERD_verdict_2011.%(ext)s"       https://www.youtube.com/watch?v=Z5qT5p6aX00
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "KATPM_Katherine_PiersMorgan_2012.%(ext)s" https://www.youtube.com/watch?v=wh3po5ErEh0
# better copy of KATPM if you can find the passage in it:
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "KATPM_full_p1.%(ext)s"            https://www.youtube.com/watch?v=4wX18Fwft9M

```

* Export every range with ±3s handles.
* The timestamps come from YouTube captions and can drift 1–2s. Lock every in/out point by ear.

3. THE SEQUENCE (cut exactly in this order)
BEAT 1: HOOK (60M) · ~5s

* Source: 60M · ~10:14 → ~10:20
* Words: HAYES: "Michael Jackson died because you killed him." / MURRAY: "I did not kill Michael Jackson."
* Start exactly on "Michael Jackson died…" and end on "…kill Michael Jackson." Nothing after it.
* Picture: frame 1 is Murray's close-up (1080p). Crop out the 60 Minutes bug (bottom left).
* On screen: label CONRAD MURRAY · MICHAEL'S DOCTOR · 2013
* Red words: YOU KILLED HIM · I DID NOT KILL MICHAEL JACKSON

BEAT 2: HIS OWN ADMISSION (60M-911) · ~8s

* Source: 60M-911 · ~0:02 → ~0:12
* Words: HAYES: "You had your cell phone…" MURRAY: "I had my cell phone." HAYES: "You didn't call 911?" MURRAY: "I did not call 911." HAYES: "You called his assistant?" MURRAY: "Yes." HAYES: "To call security?" MURRAY: "Yes."
* End on the second "Yes."
* Picture: Murray close-up. A cutaway to Hayes is OK on her questions.
* Red words: I DID NOT CALL 911 · TO CALL SECURITY

BEAT 3: THE EXPERT (SHAF2, court) · ~14s

* Source: SHAF2 · ~0:40 → ~1:07
* Words: "That is so egregious that I actually find it difficult to even comprehend… that you could have a patient who has arrested, and you call and you leave a voice message for someone. It's just inconceivable to me."
* Start on "That is so egregious." End on "inconceivable to me."
* Picture: Shafer on the stand. IV-demo cutaways (SHAF_demo ~0:46–3:30) are OK over the first half. Confirm by eye that the speaker is Shafer (the prosecutor addresses him as "Dr. Shafer" at 0:00).
* On screen: label DR. STEVEN SHAFER · PROPOFOL EXPERT · MURRAY TRIAL, 2011
* Red words: SO EGREGIOUS · LEAVE A VOICE MESSAGE · INCONCEIVABLE

BEAT 4: VERDICT (VERD) · ~6s

* Source: VERD · ~0:33 → ~0:47
* Words: "We the jury… find the defendant Conrad Robert Murray guilty of the crime of involuntary manslaughter."
* Trim "in the above entitled action". End on "involuntary manslaughter."
* Picture: the courtroom, and Murray if he's on screen.
* Music: hard stop on "guilty".
* Red words: GUILTY · INVOLUNTARY MANSLAUGHTER

BEAT 5: STILL NOTHING (60M, two answers joined) · ~9s

* Source: 60M · ~17:17 → ~17:28, then ~9:56 → ~10:01
* Words: HAYES: "What responsibility do you take for his death?" / MURRAY: "None. None. Absolutely nothing." / MURRAY: "Michael Jackson… is a drug addict."
* Piece 2: cut from his line "Michael Jackson, as you have realized now, is a drug addict" down to "Michael Jackson… is a drug addict," as Affan wrote it. If the trim inside the line isn't clean, keep "as you have realized now".
* The join: both answers are from the same 2013 interview. Hide the jump with a 2–3 frame crossfade or a 0.5s cutaway (Hayes listening).
* Picture: Murray, tight.
* On screen: small card AFTER PRISON, 2013 (top third, ~1.5s). It's true: the interview aired a month after his release.
* Red words: NONE · ABSOLUTELY NOTHING · DRUG ADDICT

BEAT 6: ENDING (KATPM) · ~6s

* Source: KATPM (wh3po5ErEh0) · ~1:46 → ~1:53
* Words: "…for a person's life, four years in jail is not enough. I'll never see my son again."
* Start on "for a person's life." HARD CUT on "again," before "but he can get out…"
* Picture: Katherine (Piers Morgan Tonight, 2012), the tightest crop, slow push-in. Crop out the CNN lower-third and bug. If the 360p copy is too soft, find the same passage in the Absolutely Definite 5-part upload.
* On screen: label KATHERINE JACKSON · HIS MOTHER · 2012
* Music out completely. Dry.
* Red words: NOT ENOUGH · I'LL NEVER SEE MY SON AGAIN

4. PICTURE

* 1080×1920, 30 fps, full-bleed vertical crop on each speaker. No letterbox, no blurred fill.
* Grade: cool and tense for beats 1–5. Warm for Katherine (beat 6).
* Trial footage is SD: sharpen lightly, match the grain, don't punch past ~120%.
* Labels: small, top third, ~2s, only on each speaker's first appearance.

5. AUDIO

* −14 LUFS integrated, true peak ≤ −1 dBTP. Level-match the courtroom audio.
* Music: a low, tense pulse at about −30 dB under beats 1–3, a hard stop on "guilty", a low re-entry under beat 5, and out for beat 6.
* 2–4 frame crossfades on every dialogue cut.

6. CAPTIONS

* Word-by-word, burned in, in the recent MJ style, at ~62–68% of frame height. Red words as listed.
* Safe zones: no text in the bottom ~20% or right ~12%.

7. EXPORT

* H.264 (≥20 Mbps) or ProRes 422 .mov, 1080×1920, 48 kHz.
* File: `Conrad Murray Guilty.mov` → `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders`

8. QA CHECKLIST (tick every box before export)

* [ ] Order: hook → 911 → Shafer → GUILTY → "None… drug addict" → Katherine.
* [ ] Frame 1 is Murray; the first words are "Michael Jackson died because you killed him."
* [ ] No anchors or narration. No children on frame. "Demerol" appears nowhere.
* [ ] Katherine says four years; hard cut on "again."
* [ ] No CNN lower-third.
* [ ] Runtime ~48s (45–52s).
* [ ] −14 LUFS, true peak ≤ −1 dBTP.

9. REPORT BACK TO AFFAN

1. Final runtime.
2. The exact in/out points per beat.
3. Which KATPM copy you used.
4. Whether the beat 5 trim to "Michael Jackson… is a drug addict" was clean.
5. Anything that didn't match this brief.
