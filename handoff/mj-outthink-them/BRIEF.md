# BRIEF: "WHY EVERYONE UNDERESTIMATED MICHAEL JACKSON 😳" (Abundance Wisdom short)

## ▶ STATUS: resume here (2026-10-31 ~18:35): v3 DELIVERED (labels at the bottom, his note on v2) → at his review
- 23. **Labels at the BOTTOM** (his v2 note, beats brief § 4 "top third"): card top y1270 (London y1385 under its band).

## (previous) ▶ STATUS: resume here (2026-10-31 ~18:00): v2 DELIVERED (40.80 s; v1 41.37 s kept beside it) → at his review. Build notes: RUN.md; report: REPORT.md
- v2 = my own QA fix: a 0.56 s pause inside "…I gave you sixty-four | that's a lot of money" tightened (brief rule 1).
- Build-time decisions after the Tella (all in REPORT.md § Flags): Michael + Paul cutaway on "Michael done bought the
  Beatles"; caption line at ~y1135 (meant ~y950-1000: a sign error, kept in v3 because he reviewed v2 and only named the labels); Katherine re-sourced as the
  wide 60 Minutes frame; Bashir lip sync measured in sync (no slip).

## (previous) STATUS (2026-10-31 ~15:45): HIS TELLA 1 RESOLVED → DECISIONS 13-22 → sequence v4 + full code build
- His Tella on the preview = DECISIONS 13-22 below (each note with its Tella time and the preview frame that resolves it).
- Build order: seq v4 (cuts 16 + 17) → HQ Katherine / Joseph stills + Higgsfield (14, 15) → Patrick kit → Stage A →
  Topaz Proteus LDN02 → finish (letterbox 13, Eddie colour / zoom 18-19, BASH slip 20, purple 21, grade, cards, captions)
  → audio → export → § 8 QA → § 9 REPORT → LESSONS + memory.

## (previous) STATUS (2026-10-31 ~13:35): SEQUENCE PREVIEW sent (v3, 45.13 s) → waiting on his OK + "Tella or not?"
- Preview: `X:\Claude Projects\Exports\MJ Outthink Them - SEQUENCE PREVIEW.mp4` (= `seq/preview.mp4`, 1354 f @ 30 fps, -14.4 LUFS,
  rough 9:16 face-tracked crops, labels as plain text, no grade / captions / upscale). In/out table `seq/inout.md`.
- YouTube blocked this PC (12:25); he SnapDownloaded LDN02 ×2 + EDDIE; MATT, BASH and the cover sources were on his drives.
- Open with him: DECISIONS 8–12 below (found on the sources, defaults in the preview).
- His order: on his OK + his answer on a Tella → (Tella: transcribe + frames → DECISIONs) → full code build (Patrick kit).

## DECISIONS (defaults stated to him 2026-10-31 ~12:25; he can override with a word)
0. **Brief version: v3 (his newest file, 10:54), not the v2 I was handed.** v3 vs v2: target ~55 s (52–58), over 60 s → ask
   him before cutting; B1 stops on "music and dancing"; B2 starts on "Every time Beyoncé and Jay-Z"; B3 ends on "ruthless
   businessman" (no specs / hotel; "who's very, very calm" → "very calm" only if clean; optional ≤ 1.5 s adult Katherine /
   Joseph photos); B5 starts on "You gonna sell the Beatles?"; B6 starts "They never thought" (no "but"). Sources and
   ranges are the same, so the locking covers both. (v3's B2 red words still list GANGSTER · SONY'S PUBLISHING: words v3
   removed; only spoken words get coloured.)
1. **Music: none.** His standing rule (`memory/feedback-music-is-his-job.md`; Patrick DECISION 1). The brief's trap
   instrumental at −28 dB and "music out for beat 6" are N/A. Soft swishes stay, 19–23 dB under the voice.
2. **Caption line: HIS height, y≈1060 (~55 %, the lip line)**, not § 6's 62–68 % (Janet review, Kane "his height", Patrick).
   Safe zones of § 6 still hold.
3. **Sources: his drives first (`E:\Bullshit Folder`), then yt-dlp, H.264/avc1 forced.** `Henry/` holds *Living With Michael
   Jackson* parts as fan "4K upscales" (1080p files): compare with the BASH link, use only if the upscale is not a
   face-generation model. MJ + Paul cutaway and the specs still (v2) / Katherine + Joseph photos (v3): sourced here, adult
   only, ≤ 1.5 s each.
4. **Upscale: Topaz Proteus, never Iris** (Iris is face-aware = the brief's banned class). Every Topaz output checked for the
   lapsed-login watermark. **No Higgsfield / AI enhance of any face still without his yes** (his HQ-stills rule vs the
   brief's "no AI faces").
5. **Delivery: 30 fps, −14 LUFS integrated, ≤ −1 dBTP measured on the ENCODED file; warm filmic archive grade on LDN02 +
   BASH, clean on EDDIE + MATT.** Skin R/G measured per source before the finish render (Patrick lesson: his 1.5–1.7).
6. **Catalog pass** only for what the brief leaves open (label motion, caption animation, zooms, transitions).
7. **Words as spoken:** every caption re-ASR'd against the audio (Patrick: "were" was "are"); cut before any other voice
   starts (DJ Vlad, Dodge Woodall); VladTV's bleeps kept; censor rule checked (no drug / self-harm words expected).

8. **Swearing: the VladTV upload is NOT bleeped** (no tone anywhere, `win/bleep.py`); the brief's "[bleep]" came from YouTube's
   caption filter. B5 has "THAT MOTHERFUCKER go right to his trailer" and "the next F***ING day". Default (closest to his
   written words "Go right to his trailer" / "the next [bleep] day"): **cut "that motherfucker"** (clean: dip 9:27.29-.35) and
   **bleep the f-word** with a 1 kHz tone over 9:30.98-9:31.30 (span proven by muting: the word vanishes). Options: keep both
   uncensored (captions F*CK-censored) or cut the f-word too ("the next day").
9. **B3 host on camera:** the podcast cuts to Dodge Woodall 1:47:43.46-1:47:45.86 (`win/cuts.py`), under "He's shrewd behind
   it all" → 1.2 s of Michael in hat + sunglasses (`E:\Bullshit Folder\Henry\Michael Jackson in Public.mp4` @0:52, Paris,
   alone in the foreground). v3's optional photos used: Katherine (Joe doc 11:53, 1.5 s) and Joseph (Joe doc 14:02.5, 0.87 s).
10. **Words by ear differ from the brief:** "Katherine Jackson IS very, very calm" (not "who's"): cut to "Katherine Jackson,
    very calm" (the "is" is a -27 dB 'z', clean). "he had / you've got Joseph Jackson, who was / who's a ruthless
    businessman" and "and my boy / and Paul, come on, say" are unresolved by ear (wav2vec2 ties; settled by the caption
    re-ASR on the final cut). Beat 5's "that's a lot of money" (2nd) and "how do you buy the Beatles" ×2 are KEPT (v3: one
    continuous piece; the brief's "…" elides them). B5 "you gonna sell" is "gonna sell" (no "you" in the audio).
11. **Vlad laughs** between "the girl is mine" (9:41.55-9:42.79) and "your publishing's mine" (9:43.90-9:45.00): the 1.1 s pause
    is cut, so most of it goes; some may sit under "your publishing's mine" (speaker embedding favours Vlad there,
    `win/who.py`). His ear decides. Cut ends 9:44.96, before "this n***a's a gangster" (9:44.98).
12. **Payoff (B6): "them" is audible** (Whisper ×3 on two copies + wav2vec2). The 0.33 s beat "this | performer" is kept whole
    (no jump cut on the push-in; brief rule 1 says ~0.25 s). "That" sits inside the crowd noise at 2:19.00-2:19.23 (mute test).
    LDN02: he pulled 2 copies; copy a "Michael jackson exposes sony.mp4" (640×358, frontal, lit) is the sharpest on his face;
    copy b "...RARE Speech ... Killer Thriller Party (Londra 2002).mp4" (1080p60) is a dark fan camcorder, mostly profile,
    "Stefan Manderioli" watermark. Runtime 45.13 s vs v3's ~55 s estimate (pauses > 0.3 s tightened per rule 1).

### HIS TELLA 1 on the sequence preview (2026-10-31 ~15:20, https://www.tella.tv/video/affans-video-9iz53z7t)
Files: `brief/tella/guide.mp4` (4:47, his voice + the preview's sound), transcript `brief/tella/guide.json` / `asr.log`,
Tella-second → preview-time map read off the preview's burned tag (`brief/tella/f/labels*.png`, 1 / 2 / 4 per s).
He did NOT comment on: the bleep (DECISION 8 default stands), v2 vs v3 (v3 stands), Vlad's laugh (moot, 17), runtime.
13. **London 2002 (B1 + B6) = AW letterbox** (tella 6-12 at preview 0.3-3.97 "this footage will be letterbox, this is too
    low quality, 100 % letterbox, not in this format"; tella 252 at 40.07 "again this will also be letterboxed"). → README § 4
    look: Proteus-upscaled LDN02 a at 100 % in a band (mask x -60→1188), 198 % / 43 % twin fill, glow bars; band placed so his
    lips clear the caption line (Kane O6 rules: twin ≥ 2·max(cy,1920-cy)/band_h, zoom pivoted on the band centre).
14. **Katherine photo "absolutely horrendous"** (tella 25-37 at 14.90 = cover JOEDO 713): "should be a much higher quality
    picture … also enhanced by Higgsfield". → source a real high-quality adult Katherine portrait, check full size, Higgsfield
    enhance (his explicit yes for this still), then a 1.5 s cover as before. DECISION 4's "no Higgsfield without his yes" is
    answered for B3's two photos only.
15. **Joseph photo same** (tella 43-61 at 17.17 = cover JOEDO 842.5): "what is that image … get a higher quality image and
    then enhance that, this is too pixelated". → same as 14 (an adult Joe Jackson portrait, stern / businessman).
16. **Cut "He's shrewd behind it all"** (tella 160-176 at 12.27-13.40 = the Paris cover): "remove this bit, I don't even know
    what this guy is saying". → B3 = "People think he's like this clown with the makeup, with the red lipstick. | Two sides to
    him, you've got Katherine Jackson, very calm and loving, he had Joseph Jackson, who was a ruthless businessman." The
    Paris cover goes with it ("lipstick" ends 6463.20, before the host-cam cut 6463.46, so no cover is needed).
17. **Cut "the girl is mine / your publishing's mine", straight into the payoff** (tella 105-114 and, decisively, 247-251:
    "remove this, the girl is mine bit, the publishing is mine, directly go into this" with "this" @251.6 = preview 40.07, B6
    LDN). → B5 ends on "…I gave you sixty-four. That's a lot of money." then B6 "They never thought…".
18. **Eddie's colour concept: desaturated when he does MICHAEL's voice, full colour as himself and as Paul** (tella 90-99 at
    34.3-34.5 "decrease the saturation"; 203-233 at 22.30-25.30 "when he's pretending to be Michael the colours are faded out
    … when he is himself fade the colours back in … fade back out when he is Michael again … when he's pretending to be Paul,
    just keep the colours"). Voices measured by pitch + story (`win/pitch.py`, Eddie's own 80-130 Hz): MICHAEL = "gonna sell
    the Beatles? How much you selling for?" · "Wow, that's a lot of money" · "You said sixty, I gave you sixty-four. That's a
    lot of money."; PAUL = "Oh, I don't know, you know, about sixty million" · "How do you buy the Beatles?" ×2 (250-400 Hz);
    EDDIE = "Every time Beyoncé…" · "Go right to his trailer … Michael done bought the Beatles" · "And my boy come on and say".
    Saturation eases in the pauses between lines, never mid-word.
19. **Eddie's zoom concept** (tella 258-281 and 90-95): "when you're putting overlays I normally do zoom outs, other than that I
    just normally zoom in; when he's pretending to be Michael, while it is zooming in you do a subtle zoom out, then zoom back
    again when he's himself". → Eddie runs on a slow push-in; each MICHAEL span eases into a subtle pull-back, the next
    Eddie / Paul line eases back into the push (keyframed, never an instant punch-in: no-same-camera-punch-ins).
20. **Bashir "No, I am Peter Pan": "his lips are not actually synced with the audio, sync it properly"** (tella 182-186 at
    19.67). Measured (`win/plosive_check.py`, 23.976 fps tiles over a 5 ms energy strip; proofs `proof/bash_plos_0/1/2.png`,
    preview `prev_plos_1.png`), 7 events: "No" (the /n/ murmur 104.23, lips part 104.31-104.35 on the vowel), "am/Peter"
    closure 104.81-104.94 vs audio 104.86-104.94 (release 1 tile late), "Pan" closure 105.13-105.25 vs 105.12-105.26, and in
    "I'm Peter Pan in my heart" (108.4-109.3) "Peter" release 108.61-108.65 vs burst 108.63, "Pan" 108.86-108.90 vs 108.89,
    "my" lips shut 109.07-109.15. **The source is IN SYNC within one frame (42 ms) and the offsets disagree in sign, so NO
    slip** (a blind −1 frame slip could make the picture lead). The probable thing he saw: "You don't want to grow up?" is
    Bashir OFF CAMERA over Michael's still, closed mouth (the documentary's own shot), which reads as a voice not matching
    the lips. Build: keep the shot, let the caption carry the question; re-measure "Peter Pan" on the ENCODED file (the
    23.976 → 30 conversion and Topaz can move frames). Told to him in the report; his ear decides on the final.
21. **Purple dip at the London → Eddie cut (preview 6.23)** (tella 137.7 "do a purple" at 10.40, then he scrubbed back and said
    "fade in on this" @141.7 while landing on Eddie's first frame 6.27). Purple = his label 10: brightness dip to −90 and back
    (README § 7, −0.333 / cut / +0.267 s).
22. **Transitions and zooms are mine by his rules** (tella 255-271: "you pretty much know my transition rules at this point,
    so do them yourself, and same with the zoom in and zoom outs"): transitions only on scene changes (README § 7 colours),
    overlays zoom out, everything else zooms in, no same-camera punch-ins.

### CATALOG PASS (scoped, DECISION 6: only what the brief + his Tella leave open; `research/effects-catalog/CATALOG.md`)
- **Used:** FX-14 *Painted Sky Worlds* (near-monochrome plates) → the Michael-voice desaturation on Eddie (his own concept,
  DECISION 18; held at 0.22, colour back on Eddie / Paul); FX-29 *Float Frame* (archive never fills the screen) → the AW
  letterbox for London 2002, Joe and the Michael + Paul photo (his Tella "letterbox"); FX-80 *Black-Beat Ident* (dips to
  black at chapter turns) → his purple −90 dips on the beat changes (London → Eddie, Matt → Bashir, Eddie → payoff);
  FX-40 *Slow-Burn Portrait* → the parent photos held still with a slow zoom-OUT (his overlay rule).
- **Not this time:** FX-37 Ghost Dissolve / FX-38 Hard Push (his transition code is the colour set, README § 7), FX-22 Red
  Isolate (no red story element), any type-over-picture move (captions carry the words; the brief keeps cards small).
- **Better than the last AW short (Patrick, 2026-10-31):** the voice acting is SHOWN, not just heard (colour + zoom follow
  whose voice Eddie is doing), every cover is a real HQ picture (no SD frames), and the low-res London stage footage is
  head-locked inside its band with a smoothed follow instead of a hard lock (no shake from a 115 px face).

## HIS BRIEF, VERBATIM (v2, as handed to this session)

EDITOR BRIEF: "WHY EVERYONE UNDERESTIMATED MICHAEL JACKSON 😳"
Channel: Abundance Wisdom · Format: YouTube Short, 1080×1920 · Locked: 31 Oct 2026 (v2, Affan's sequence)
The creative is locked. Cut it exactly as written. If anything can't be done exactly as written, stop and tell Affan before improvising.
What this Short is: Michael opens with "they thought my mind is always on music and dancing" → a comedian, his bodyguard and Michael himself show both sides (the kid and the shark) → Michael closes it: "…but they never thought that this performer would outthink them."
Target runtime: 64–70s (hard max 72s), measured on the timeline.
1. HARD RULES (any one broken = redo)

1. Someone is speaking at every moment. No gaps over ~0.25s.
2. Source audio only. No voiceover, TTS, AI voices or AI faces.
3. Exact words only. Trim filler inside a range. Never splice to change meaning. One approved split: Michael's London sentence is cut in two, with the setup in beat 1 and the payoff in beat 6.
4. Voices allowed: Michael, Eddie Griffin, Matt Fiddes, and Martin Bashir (one question). No DJ Vlad, no Dodge Woodall (interviewers).
5. No minors on frame. Bashir's documentary is full of children; use only Michael alone. No Michael's-kids footage.
6. Keep VladTV's bleeps as they are. Don't un-bleep or add swearing.
7. Hard cut on "outthink them." No end card.

2. SOURCES (download first)

```
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "LDN02_MJ_London_2002.%(ext)s"  https://www.youtube.com/watch?v=WRFU2SyCCF8
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "LDN02_alt1.%(ext)s"            https://www.youtube.com/watch?v=kIieKGjc6Xs
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "LDN02_alt2.%(ext)s"            https://www.youtube.com/watch?v=hc2U9SklOZU
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "EDDIE_Griffin_VladTV.%(ext)s"  https://www.youtube.com/watch?v=FvuGC-euvE0
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "MATT_Fiddes_Dodge.%(ext)s"     https://www.youtube.com/watch?v=9zj9iE7NSTo
yt-dlp -f "bv*[height<=2160]+ba/b" --merge-output-format mp4 -o "BASH_PeterPan_2003.%(ext)s"    https://www.youtube.com/watch?v=WiMgVPJxLDc

```

* Export every range with ±3s handles.
* The timestamps come from YouTube captions and can drift 1–2s. Lock every in/out point by ear.
* Use the sharpest of the three LDN02 copies (they're all old fan footage, so pick the best).

3. THE SEQUENCE (cut exactly in this order)
BEAT 1: HOOK (LDN02, Michael)

* Source: LDN02 · two pieces: ~3:54 → ~4:04, then ~2:10 → ~2:17
* Words: "…I own half of Sony's publishing…" / "…they really thought that my mind is always on music and dancing, and it usually is…"
* Stop on "and it usually is", before "but they never thought…" (that's beat 6).
* Don't include "and I'm leaving them, and they're very angry at me".
* Picture: Michael at the mic, tight; frame 1 is his face. Upscale cleanly (no face-generation models).
* On screen: label MICHAEL JACKSON · LONDON, 2002
* Red words: HALF OF SONY'S PUBLISHING · MUSIC AND DANCING

BEAT 2: EDDIE GRIFFIN

* Source: EDDIE · ~8:57 → ~9:10
* Words: "…you know what's gangster? 'I own Sony's publishing.' Every time Beyoncé and Jay-Z make a song, Michael was getting a check."
* Start on "you know what's gangster" (drop "let me put it like this"). Stop on "getting a check", before "I bought the Beatles" (that's beat 5).
* Picture: Eddie Griffin (VladTV). Crop out the VladTV bug. Keep Vlad out of frame.
* On screen: label EDDIE GRIFFIN · COMEDIAN, MICHAEL'S FRIEND
* Red words: GANGSTER · SONY'S PUBLISHING · GETTING A CHECK

BEAT 3: MATT FIDDES

* Source: MATT · ~1:47:35 → ~1:48:01
* Words: "…people think he's like this clown with the makeup, with the red lipstick. He's shrewd behind it all… Two sides to him. You got Katherine Jackson, who's very, very calm and loving. You had Joseph Jackson, who's a ruthless businessman. And I see that guy put the specs on, he'd be like, 'We're doing this deal. I'm not paying for that hotel…'"
* Start on "people think he's like this clown". Keep the whole "two sides" sentence. "Ruthless businessman" is said about Joseph, so don't cut Katherine/Joseph out to make it sound like it's about Michael. You may trim "he's a clever dude, you can see that". End on "I'm not paying for that hotel" (or "make sure they know I'm coming" if it fits).
* Picture: Matt Fiddes (podcast). Crop out the host. Optional ≤1.5s still of Michael in sunglasses or business attire over "put the specs on" (adult Michael only).
* On screen: label MATT FIDDES · MICHAEL'S BODYGUARD
* Red words: SHREWD BEHIND IT ALL · RUTHLESS BUSINESSMAN · PUT THE SPECS ON

BEAT 4: THE KID (BASH)

* Source: BASH · ~1:43 → ~1:47
* Words: BASHIR: "…you don't want to grow up?" / MICHAEL: "No. I am Peter Pan."
* Hard out on "Peter Pan." No "You're Michael Jackson" and no "I'm Peter Pan in my heart."
* Picture: Michael alone (green shirt).
* On screen: label MICHAEL JACKSON · 2003
* Red words: I AM PETER PAN

BEAT 5: EDDIE GRIFFIN, THE BEATLES

* Source: EDDIE · ~9:10 → ~9:44
* Words: "I bought the Beatles… Michael walks up: 'You gonna sell the Beatles? How much you sell 'em for?' 'Oh… 60 million.' 'Wow, that's a lot of money.' Go right to his trailer, get his people on the phone. Paul don't find out till the next [bleep] day Michael bought the Beatles… 'How can you buy the Beatles?' 'You said 60, I gave you 64.'… The girl is mine, your publishing's mine."
* Drop "why I'm doing the video with the Beatle? That's gangster, right?" if you need time. End on "your publishing's mine."
* Lock the words by ear; the captions are rough here.
* Picture: Eddie. Optional ≤1.5s cutaway of Michael and Paul together (Say Say Say or The Girl Is Mine era, adults) over "The girl is mine".
* Red words: 60 MILLION · THE NEXT DAY · I GAVE YOU 64 · YOUR PUBLISHING'S MINE

BEAT 6: PAYOFF (LDN02, Michael)

* Source: LDN02 · ~2:17 → ~2:31
* Words: "…but they never thought that this performer, myself, would outthink them."
* ⚠️ Lock the last word by ear. The captions read "out think, yeah" (heavy crowd noise). If "them" isn't clearly audible, caption only what you hear ("…would outthink…") and report it.
* Picture: Michael, the tightest crop of the video, slow push-in.
* Music out for this beat.
* Red words: OUTTHINK THEM
* HARD CUT on the last syllable. ≤0.3s of the crowd roar, then black.

If you're over 72s, cut in this order

1. Beat 5: drop "why I'm doing the video with the Beatle? That's gangster" (−3s), then "'Wow, that's a lot of money'" (−2s).
2. Beat 3: drop the "I'm not paying for that hotel" quote and end on "put the specs on" (−3s).
3. Beat 2: drop "'I own Sony's publishing'" (it's said in beat 1) (−2s).

4. PICTURE

* 1080×1920, 30 fps, full-bleed vertical crop on each speaker. No letterbox, no blurred fill.
* Grade: the London 2002 and Bashir footage is old and soft. Grade it warm and filmic so it reads as archive, not as a mistake. Eddie and Matt are clean, modern podcasts.
* Don't punch the low-res sources past what fills the frame.
* Labels: small, top third, ~2s, only on each speaker's first appearance.

5. AUDIO

* −14 LUFS integrated, true peak ≤ −1 dBTP. Level-match. LDN02 is a live room, so give it a light de-noise.
* Music: a confident, low hip-hop/trap instrumental at about −28 dB from beat 2, ducking under speech. Kill it for beat 6.
* 2–4 frame crossfades on every dialogue cut.

6. CAPTIONS

* Word-by-word, burned in, in the recent MJ style, at ~62–68% of frame height. Red words as listed.
* Safe zones: no text in the bottom ~20% or right ~12%.

7. EXPORT

* H.264 (≥20 Mbps) or ProRes 422 .mov, 1080×1920, 48 kHz.
* File: `MJ Outthink Them.mov` → `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders`

8. QA CHECKLIST (tick every box before export)

* [ ] Order: London (setup) → Eddie → Matt → Bashir ("I am Peter Pan" only) → Eddie (Beatles) → London (payoff).
* [ ] Matt's "ruthless businessman" sentence is complete (Katherine/Joseph included).
* [ ] No DJ Vlad or Dodge Woodall audio. No children on frame.
* [ ] Hard cut on "outthink them."
* [ ] Runtime ≤72s.
* [ ] −14 LUFS, true peak ≤ −1 dBTP.

9. REPORT BACK TO AFFAN

1. Final runtime.
2. The exact in/out points per beat (and which LDN02 copy you used).
3. Whether "them" is audible in beat 6.
4. Any trims used.
5. Anything that didn't match this brief.

## HIS BRIEF v3 (newest file on disk, 10:54)
Verbatim snapshot: `brief/MJ-OUTTHINK-EDITOR.v3.md` (his research notes + fact audit: `brief/MJ-OUTTHINK-CUT.md`, still
the v2 table). Differences from v2 are DECISION 0 above.
