# BRIEF: "WHY PATRICK STEWART'S FATHER WAS SO ANGRY 💔" (Abundance Wisdom short)

## ▶ STATUS: resume here (2026-10-31 ~09:40): his Tella 1 on the preview resolved (DECISION 10) → full code build (RUN.md)
- He answered the preview with a Tella (`brief/tella/guide.mp4`, 7:50, transcript `brief/tella/guide.json`, frames
  `proof/tella/`): one cut, five picture/finish notes, "apart from that you can start". Sequence v2 = `seq/edl.py` (61.73 s).
- His words (2026-10-31 ~02:50): "give me the sequence not in Premiere but in a video format so that I can see ... I'm going
  to approve the sequencing and then you're going to do everything yourself. I'm not even going to give the creative
  direction video for this one. I really want to test what you do yourself." + "download everything yourself."
- So the order this time: download → lock ins/outs by ear → **sequence preview MP4** (no Premiere) → his OK → full code
  build with NO Tella direction (my own calls on zooms, transitions, colours, SFX; logged below) → export both folders.
- Source file of this brief: `X:\Claude Projects\Abundance Wisdom\PATRICK-STEWART-EDITOR.md` (v11, 02:45). Background:
  `PATRICK-STEWART-FATHER-CUT.md` (v10, the 4a-bridge flag).

## DECISIONS (defaults stated to him 2026-10-31; he can override with a word)
1. **Music: none.** His standing rule (2026-10-27, Joe; repeated on Kane 10-29): AW code-built shorts ship with NO music bed,
   even when the brief names one; music is his job. § 5's piano bed and beat 6's "fade it out" are N/A. SFX stay (soft
   swishes on transitions, 19–23 dB under the voice).
2. **Sources: downloaded here, plain yt-dlp, H.264 (avc1) forced.** YouTube worked on 2026-10-31. The TNG bridge clip for
   beat 8 has no link in the brief → I source it (drives first, then YouTube), ≤ 1.5 s.
3. **Caption line: HIS height (y≈1060, ~55 %, on the speaker's lip line)**, not § 6's 62–68 %. Janet v1 was built at the
   brief's 64 % and his review moved it up ("all of these things are placed too low just because the captions are placed
   too low"); Kane (10-29) he answered the same question with "his height". Still inside § 6's safe zones.
4. **AMN09 upscale: Topaz Proteus (prob-4), no Iris** (Iris is face-aware = the brief's banned face-restoration class) +
   light grain + desaturated archive grade. Every Topaz output checked for the lapsed-login WATERMARK.
5. **Delivery: 30 fps, −14 LUFS integrated, ≤ −1 dBTP (measured on the ENCODED file), grade cold/desat on beats 1–3 →
   warming from beat 4 → warmest 7–8**, as the brief says (earlier AW builds: 60 fps master, −15.3 LUFS; brief wins).
6. **Catalog pass** (CLAUDE.md learning loop) only for what the brief leaves open: label/card motion, caption animation,
   zoom groups, transitions. The cut itself is locked.
7. **Order: sequence preview as a video file** (his instruction above), then the build without asking again.
8. **Picture that can't be done as written** (found on the sources, shown in the preview, his call): see RUN.md § STATUS.
   Runtime with every word kept = 73.5 s (> 72 s max): default keep the words; option drop "my father. Understand him,".
9. **Words as spoken** (rule 3 + "caption only what's spoken"): B7 "because he JUST made me angry", "HE'S one of the people";
   B8 starts "He would have loved" (his "And" dropped). Build check (2026-10-31): B5 is "soldiers ARE being told", not the
   brief's "were" (YouTube captions): the snippet re-ASR and the final-mix re-ASR both hear "are", wav2vec2 scores
   'are' 0.47 vs 'were' 0.32 (`win/were_are.py`); caption = ARE. B8 ends 15 ms BEFORE wav2vec2's "Picard" end
   (1626.761): Rich Roll's "mm-hmm" starts at 1626.77 (rule 4), so the cut lands before it; runtime 61.67 s.
10. **His Tella 1 on the sequence preview (2026-10-31 morning; `brief/tella/guide.mp4`, his player time = preview time).**
    Each note → what it resolves to. Supersedes the brief where they differ.
    - **Length** (tella 4–26): "preferably less than 60 seconds, but if it's not possible I guess we can still do it"
      (over a minute, his song choice for the Short gets blocked). → his cut below takes 73.53 → 61.73 s. Tightening every
      joint to the MEASURED acoustic edge was tried (`seq/edl.edgetest.py`): 61.9 s, the speech fills the joints, so the
      verified preview pads stay. Under 60 needs ~1.8 s more WORDS (not his call yet): the report says which.
    - **The cut** (tella 215–299, 355–367; preview 0:45–0:57): "this whole bit ... from 45 seconds all the way to ... a
      semi-skilled labourer with no authority at all ... resume it from ... this I realise now must have been very painful
      for him." → B6 = "And this I realise now must have been very painful for him" only ("weekend alcoholic ... no
      authority at all" gone, with its two covers).
    - **Father, not Patrick, on that line** (tella 320–333, frame = preview 0:58 COVER LW 332.64): "for this part you need to
      use his father's, not his overlay" → B6 now covers on Alfred's smiling portrait (WDY3 145, freed by the cut), 2.73 s
      (over the brief's ≤ 2 s per Alfred photo, like B3's 3.3 s he saw and passed).
    - **Opener** (tella 37–99, frame = preview 0:04, B1 LW listening): "put a zoom-out layer, and while it is zooming out it
      fades in saturation as well, so it starts to get grey" + "a motion graphic in my own style aesthetic ... integrated
      ... originates from his head ... tells the viewer he just passed away ... Sir Patrick Stewart, passed away October
      something". → B1: slow zoom-out with a desaturation to grey, and the AW-style card drawn out from his head: SIR PATRICK
      STEWART / PASSED AWAY 28 OCTOBER 2026 (replaces the label "· ON HIS FATHER"). **Overrides brief rule 6 for this one
      card only, on his word: the death, no cause, no illness.** Date checked: Deadline + Just Jared 28 Oct, THR
      "Wednesday" = 28 Oct 2026, announced Thu 29 Oct; "yesterday" would be false on the publish day, so the date.
    - **The regiment photo** (tella 107–139, frame = preview 0:17, B3 LIFE 45): "needs some serious upscaling ... find what
      his face actually looks like ... enhance this image according to that reference so that this face actually looks
      clean and clear" → Higgsfield face restore of Alfred with his clean portraits (WDY2 side-cap, WDY3 smiling) as
      references; checked full size for rewritten badges / other men's faces.
    - **Comicpalooza** (tella 164–172, frame = preview 0:41, `B5 CP 239.36` tag): "this will be in a letterbox format,
      because his face is so low, so you can just drag it up" → B5 in the AW low-quality letterbox (Kane O6 recipe: native
      size, band lifted until his face clears the caption line, twin fill + glow line).
    - **Captions** (tella 366–381): "a lot of coloured captions, not just one colour caption, like I've told you before"
      → README §8 Colour MIX, every accent family used, gradient fills; QA counts distinct accents.
    - **All father images through Higgsfield first, then the whole video through Topaz** (tella 382–413): "Topaz doesn't
      really do a good job of scaling pictures".
    - **Topaz smoothness** (tella 413–465): "use jittery motion with the number of passes set at two, or just below three
      ... with recent videos I have been seeing some jitter ... the last Harry Kane video ... I could feel the jitter ... I
      want very smooth videos (Bolt Motivation)". → `tvai_stb … reduce=2` (= "Reduce jittery motions", 2 passes; his own
      2026-10-10 export log carries exactly that). Also checked: 25p sources conformed by plain frame repeats BEFORE
      Chronos so its duplicate-replace fires; still push-ins rendered sub-pixel (no 1-px stair steps).
    - "All the other things, pretty much you nailed the head on that one" → the rest of the sequence stands.

11. **His note on v1 (2026-10-31 ~12:45, chat):** "because he just made me angry and fearful when he was around ---
    remove this and it will be under 60" → B7 = "my father. Understand him, | And he's one of the people I miss now"
    (PBS 3:44.21-3:49.28 out, with its regiment-photo cover) → **57.77 s**. He chose this line over the one I offered
    ("my father. Understand him,"): the brief's "angry and fearful" red words go with it.

## CATALOG PASS (2026-10-31, before the build; CLAUDE.md learning loop rule 5)
Read `research/effects-catalog/CATALOG.md` (FX-01..81) and looked at all 137 reference stills (contact sheets, 4 pages).
The look itself stays HIS (AW README: glow bars, Gretaros captions, purple / cyan / peach transitions, his AE grade layer):
he asked for the opener "in my own style aesthetic so it doesn't stand out like a sore thumb".
- **Fits and used:** FX-23 Pointer Tag / FX-42 Kin Tag → the opener: a line drawn OUT of his head into the name card
  (in AW glow-bar form, not LEMMiNO's box). FX-40 Slow-Burn Portrait → every Alfred photo held on a slow creep, never a
  cut-in. FX-14 / FX-48 near-monochrome cold plates → B1 drains to grey on the zoom-out, B1-3 cold. FX-80 hard dip →
  the hard cut to black on "Picard".
- **Fits, not used (and why):** FX-34 / FX-45 one highlighted phrase on the newspaper (the WDY2 close-up is the real
  paper and 2.7 s: a highlight there is a new non-spoken text the brief's rule 8 forbids). FX-37 Ghost Dissolve
  between Alfred and Patrick (his transition vocabulary is the AW four; a ghost would be a new move he hasn't asked for
  on a short). FX-43 Tape Morph young → old Alfred (glitch on a tribute = wrong tone).
- **New on this channel / better than the last AW short:** (1) the father photos are restored faces (Higgsfield, his
  references), not soft broadcast frames; (2) the opener card is drawn from the subject's head, tracked through the
  zoom-out; (3) Topaz stabiliser jitter passes 2 (his ask after Kane's jitter), Chronos on exact 25p repeats;
  (4) captions: 37 of 88 coloured (1 in 2.4) across all six accents, the most varied MIX yet.
- **What the last ones leaned on:** Kane: full-screen 4K overlays + green flashes on jump cuts; Katherine: band-C lift.
  Here: no green flashes (tribute tone), letterbox only where the source forces it (CP, the face-filling smile photo).

## HIS BRIEF, VERBATIM (v11)

# EDITOR BRIEF: "WHY PATRICK STEWART'S FATHER WAS SO ANGRY 💔"
**Channel:** Abundance Wisdom · **Format:** YouTube Short, 1080×1920 · **Locked:** 30 Oct 2026 (v11, Affan's order + full beat 6) · **⏱ URGENT: publish within 24–48h** (Patrick Stewart died 28 Oct 2026)

The creative is locked. Your job is to cut it exactly as written. **If anything can't be done exactly as written, stop and tell Affan before improvising.**

**Target runtime: ~66–70s (hard max 72s), measured on the timeline.**

---

## 1. HARD RULES (any one broken = redo)
1. **Someone is speaking at every moment.** No gaps over ~0.25s. Tighten Patrick's pauses, but keep the emotion.
2. **Source audio only.** No voiceover, TTS, AI voices or AI faces.
3. **Exact words only, in Affan's order below.**
4. **Only Patrick's voice.** No narrators, hosts, the PBS reporter, Rich Roll, his brother Trevor, or the fan.
5. **No minors on frame.** No childhood or youth photos (WDYTYA and the PBS B-roll have them). Adults only: Patrick and Alfred in uniform.
6. **Nothing about Patrick's own illness or death** on screen.
7. **Hard cut on "Picard."** No end card, no music tail.
8. **Caption only what's spoken.** The only non-spoken text is the labels and cards listed below.

---

## 2. SOURCES (download first)
```
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "LIFE_Stewart_BBC_Lifeline_CombatStress.%(ext)s" https://www.youtube.com/watch?v=65kGcX4DO6E
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "AMN09_Stewart_Amnesty_speech.%(ext)s"            https://www.youtube.com/watch?v=Xi_27bpIb30
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "WDY2_Stewart_WDYTYA_shellshock.%(ext)s"          https://www.youtube.com/watch?v=Em8Mfiben_k
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "CP_Stewart_Comicpalooza_2013.%(ext)s"            https://www.youtube.com/watch?v=TqFaiVNuy1k
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "LW_Stewart_LooseWomen_2018.%(ext)s"              https://www.youtube.com/watch?v=QQ9oIl1q69c
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "PBS_Stewart_NewsHour_2023.%(ext)s"               https://www.youtube.com/watch?v=dg2PDrJ7EYo
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "RR_Stewart_RichRoll_2023.%(ext)s"                https://www.youtube.com/watch?v=EkTUXuHQLvs
# extra Alfred photo only (NO audio from this one; the emotional lines in it are his brother's)
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "WDY3_Stewart_WDYTYA_brother.%(ext)s"             https://www.youtube.com/watch?v=2k1eTwBiuj4
```
- Export every range with **±3s handles**.
- **The timestamps come from YouTube captions and can drift 1–2s. Lock every in/out point by ear.** The words win over the timestamps.

---

## 3. THE SEQUENCE (cut exactly in this order)

### BEAT 1: LIFE · ~0:34 → ~0:41
- **Words:** "I was seven years old when I first saw him hit my mother, and it happened frequently throughout my childhood."
- **Picture:** Patrick to camera, tight; frame 1 is his face. **Crop out the "BBC one" bug (top left) and the combatstress.org.uk / phone lower-third (right).**
- **On screen:** label **SIR PATRICK STEWART · ON HIS FATHER**
- **Red words:** SEVEN YEARS OLD · HIT MY MOTHER

### BEAT 2: AMN09 · ~2:16 → ~2:48
- **Words:** "…if my mother had… picked up a knife… against my father, I would have held her hand as she did it. I would have locked the door while she carried it out. That's how bad it was."
- Skip the garbled ~2:20–2:28 and **cut "or any other weapon"**. Tighten the long pauses to ~0.2s.
- **Picture:** 360p, so crop, then upscale with a standard upscaler (**no face-generation or face-restoration models**). Add light grain and a desaturated archive grade.
- **On screen:** label **AMNESTY INTERNATIONAL UK**
- **Red words:** HELD HER HAND · LOCKED THE DOOR

### BEAT 3: LIFE · ~0:41 → ~0:56
- **Words:** "I never understood why he was so volatile at home… but it was only two years ago I discovered that my father had suffered from post-traumatic stress disorder."
- **Cut "while in his military career he had been a superstar".** Stop before "a debilitating psychological condition…"
- **Picture:** Patrick to camera.
- **Red words:** I NEVER UNDERSTOOD WHY · POST-TRAUMATIC STRESS DISORDER

### BEAT 4: WDY2 · ~1:56 → ~2:13 (Patrick reads his father's 1940 newspaper report)
- **Words:** "He has been in France three months, and seen a great deal of the recent hard fighting, coming through many bombing and machine-gunning attacks… The brutality of the Germans against civilian refugee children has left a deeper impression than anything else of his experiences."
- Drop "no rest for three weeks…" and everything after "his experiences".
- **Picture:** **⚠️ This is critical: the viewer must know "He" means his father.**
  - **Open the beat on the Alfred-in-uniform portrait** (WDY2 ~2:20) with the card **HIS FATHER'S NEWSPAPER REPORT · 1940** (top third, ~2s), *before or on the very first word*.
  - Then Patrick reading on camera (cap and scarf), and the newspaper close-ups (~2:00).
  - **No children on screen;** they're only in the text.
- **Grade:** start warming here.
- **Red words:** BOMBING AND MACHINE-GUNNING · REFUGEE CHILDREN

### BEAT 5: CP · ~4:00 → ~4:07
- **Words:** "And basically soldiers were being told, 'Pull yourself together, get a grip on yourself, and get out there and be a man.'"
- **Start on "And basically"**, after "In 1940 it was just shell shock."
- **Picture:** Patrick at the mic. **Keep the fan (an abuse survivor) out of frame.**
- **Red words:** PULL YOURSELF TOGETHER · BE A MAN

### BEAT 6: LW · ~2:05 → ~2:24 (one continuous piece, no splice)
- **Words:** "…he was a weekend alcoholic, and it was partly brought about because of his transformation from regimental sergeant major to basically a semi-skilled labourer with no authority at all… and this I realise now must have been very painful for him."
- **Start on "he was a weekend alcoholic"**, after the host's "can you tell us some of what he did". **End on "painful for him"**, before "and he was also suffering…". You may tighten Patrick's own pauses; don't drop any words.
- No host audio.
- **Picture:**
  - Patrick on the Loose Women set, tight. **Crop the ITV bug and the "My domestic violence story" lower-third.**
  - Over "regimental sergeant major", 1.5s of **Alfred in uniform** (WDY3 ~2:24 has a good one, picture only).
  - ⚠️ **Avoid the Loose Women logo wipe at ~2:22**; cover it with Patrick's close-up or the Alfred photo.
- **Music:** fade it out across this beat.
- **Red words:** REGIMENTAL SERGEANT MAJOR · NO AUTHORITY AT ALL · I REALISE NOW · VERY PAINFUL FOR HIM

### BEAT 7: PBS · ~3:42 → ~3:57
- **Words:** "…my father. Understand him, because he made me angry and fearful when he was around… And he is one of the people I miss now."
- **Start on "my father."** Nothing about therapy before it. **Cut "because I would like him to read the book".**
- **Picture:**
  - Patrick on camera for "…angry and fearful when he was around". **⚠️ Never a laughing frame here** (he's laughing around 3:51).
  - **⚠️ Never the PBS B-roll at ~3:56** (an old group photo).
  - Over "And he is one of the people I miss now": **Alfred in uniform**, slow push-in. Hold ~0.3s, then go straight into beat 8.
- **Red words:** ANGRY AND FEARFUL · ONE OF THE PEOPLE I MISS NOW

### BEAT 8: RR · ~27:00 → ~27:06
- **Words:** "He would have loved Next Generation… particularly that I was Captain Picard."
- Start on "would have loved" (drop his leading "and"). **No Rich Roll audio** (cut his question and Patrick's "yes, yes he did" before it).
- **Picture:** Patrick (cropped off Rich Roll's shoulder), then **≤1.5s of Captain Picard on the TNG bridge** on "Captain Picard".
- **Red words:** CAPTAIN PICARD
- **HARD CUT on "Picard."** Black, no music, no tail.

---

## 4. PICTURE
- **1080×1920, 30 fps**, full-bleed vertical crop on Patrick. No letterbox, no blurred fill.
- **Grade:**
  - Beats 1–3: cold and desaturated.
  - Beat 4 onward: warming.
  - Beats 7–8: warmest.
- Don't punch the 1080p sources past ~130%.
- **Labels:** small, top third, ~2s.
- **Archive limits:** ≤2s per Alfred photo, ≤1.5s TNG.

## 5. AUDIO
- **−14 LUFS integrated, true peak ≤ −1 dBTP.**
- Level-match all sources. AMN09 and CP are room mics, so give them a light de-noise and de-reverb.
- **Music:** one soft, sad piano bed at about −30 dB under beats 1–5, swelling slightly at beat 4. **Fade it out across beat 6; beats 7–8 play dry.**
- 2–4 frame crossfades on every dialogue cut.

## 6. CAPTIONS
- Word-by-word, burned in, in the same style as the recent channel Shorts, at ~62–68% of frame height. Red words as listed.
- Caption exactly what's said.
- **Safe zones:** no text in the bottom ~20% or right ~12%.

## 7. EXPORT
- H.264 (≥20 Mbps) or ProRes 422 .mov, 1080×1920, 48 kHz.
- File: **`Patrick Stewart Father.mov`** → `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders`

## 8. QA CHECKLIST (tick every box before export)
- [ ] Beats 1 → 8 in Affan's order; frame 1 is Patrick's face.
- [ ] Beat 4 opens on Alfred's portrait plus the "HIS FATHER'S NEWSPAPER REPORT · 1940" card.
- [ ] Only Patrick is heard.
- [ ] No childhood or youth photos; no PBS B-roll; no laughing face under "angry and fearful".
- [ ] No BBC/ITV bugs, lower-thirds or phone numbers visible.
- [ ] Hard cut on "Picard."
- [ ] Beat 6 is one continuous piece, from "weekend alcoholic" through "painful for him".
- [ ] Runtime ≤72s.
- [ ] −14 LUFS, true peak ≤ −1 dBTP.

## 9. REPORT BACK TO AFFAN
1. Final runtime.
2. The exact in/out points used per beat (file + timestamps).
3. Whether the beat 3 → 4 switch reads clearly with the portrait and card (if not, say so; the 4a bridge line is the fix).
4. How AMN09 looks after the upscale.
5. Anything that didn't match this brief.
