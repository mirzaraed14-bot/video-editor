# Cold read: MOM-MOMENTS.md (defects only, never taste)

**What was read:** `research/aw-speed-pick-2026-11-13/MOM-MOMENTS.md`, the 268-line version saved at 17:24:29 on 14 Nov. The file changed while
I was reading it (the 17:19 version was replaced), and it was still the 17:24 version when this report was finished. All line numbers
below are for that version.

`SEQUENCE-v2.md` and `RUN.md` in `projects/speed-kicked-out-three-peat/` were updated at 17:50. Every citation to them is to the 17:50
versions.

**Conventions:**
- Paths are relative to `X:\Claude Projects\video-editor-client\video-editor\`.
- **"Scout"** = `research/aw-speed-pick-2026-11-13/scout/52pXQVGHwEE.words.json` (small.en; it uses the fam file's own time base).
- **"Waveform"** = 20 ms and 40 ms RMS and zero-crossing windows, measured on audio decoded from the named mp4 to a wav file. Nothing was
  played. ZCR (zero-crossing rate) separates an "sh" (high) from voiced sounds (low).
- **Shots** were re-measured with the scene-detect command on the fam file, plus stills at 60, 65, 70, 77, 83, 113, 117, 123 and 130 s.

**Skipped, as instructed:** the § 1a planned-surprise block (lines 68-82).

**Totals:** 8 WRONG · 5 MISLEADING · 4 CLAIM-AS-FACT · 18 MINOR.

## WRONG

**1. WRONG: § 1b row A1 (line 93), in-point "~62.2".**
- **The sources:**
  - Scout has "She's" at 63.07.
  - The 62.2 comes from a smeared large-v3 word: `she's@7.20-8.08` (+55 s = 62.20-63.08) in
    `projects/speed-kicked-out-three-peat/mom/asr/fam_55_90.large-v3.txt`.
  - Waveform: "video" stays voiced to ~62.42, there is silence 62.44-62.96, and the "sh" starts at 63.00 (ZCR 0.45-0.55).
  - The research log's own § 8 (`research/aw-speed-pick-2026-11-13.md` line 379) gives "fam 63.07-66.73".
  - `SEQUENCE-v2.md` row 6 (line 19) starts A1 at 62.84.
- **Why it matters:** an in at 62.2 replays the tail of "video", and his own clip already ends there at 62.43.
- **Fix:** in at ~62.85-62.95 (the silence after the 62.81 cut), so A1 sits entirely on the WIDE.

**2. WRONG: § 1b row A3 (line 95), in-point 75.36 opens on "No,", which the quote leaves out.**
- **The sources:**
  - Large-v3 has `no@18.08-20.36 she@20.36-20.74` (+55 s), a smear.
  - Scout has "No," at 75.11-75.51 and "she" at 75.71.
  - Waveform: a voiced, low-ZCR word at 75.34-75.64 ("No,"), a gap at 75.64-75.68, the "sh" at 75.68-75.82, then "told" from 75.92.
  - `SEQUENCE-v2.md` line 40 writes this line as "(No,) she told me to quit."
- **Fix:** in at ~75.66, or quote it as "No, she told me to quit…".

**3. WRONG: § 1c musing row 1 (line 117): the out at 114.35 cuts the last word, "dad.".**
- Scout: "my" 114.21-114.35, then "dad." 114.35-114.55.
- Waveform: voiced at 114.38-114.58.
- **Fix:** out at ~114.60-114.95 ("Shout" starts at 115.02).

**4. WRONG: musing row 2 (line 118): the out at 119.77 adds a word the quote doesn't have, "But".**
- Scout: "on." ends at 118.99, "But" runs 119.49-119.77, then "anyways,".
- Waveform: speech ends ~119.22, silence 119.28-119.64, then "But" at 119.68-119.78.
- **Fix:** out inside the silence, ~119.30-119.60.

**5. WRONG: musing row 3 (line 119): the out at 125.15 cuts "here."**
- Scout: "got" ends at 125.15, "here." runs 125.15-125.43.
- Waveform: voiced to 125.44, silent from 125.48. The WIDE runs to the cut at 125.54.
- Without "here.", the line loses the "and now here we are" it is offered as.
- **Fix:** out at ~125.46-125.52.

**6. WRONG: § 2a line 144, "If used: audio only (the middle way above) is the safe form."**
- It contradicts the ruling at the top of the same file (lines 32-35: picture IN, framed tight or covered) and `BRIEF.md` § "His ruling
  on minors".
- "The middle way above" is no longer in the file. It was the pre-ruling idea ("minor-era AUDIO under an adult picture"), which the
  research session's own note to the hub says the ruling supersedes (side-session note `aw-speed-pick-2026-11-13.md` lines 22, 36).
- **Fix:** replace the line with the ruling as stated at lines 32-35.

**7. WRONG: § 7 line 247 (and lines 17-18), "Before 16:42, 34 calls in ~67 min came from two sessions."**
- **Three things are missing:**
  - **This session's own earlier calls:** `research/aw-speed-pick-2026-11-13/yt/batch11-14.log` add 12 more lock.sh calls at
    15:39:05-15:56:37 (batch11: 2 audio + 1 search; batch12: 3 meta; batch13: 2 audio; batch14: 1 meta + 3 searches).
  - **The hub's own burst:** `presets/youtube-shorts/abundance-wisdom/HUB.md` lines 24-27 says the hub's channel listing at 16:34
    (~10 page requests in 24 s) "most likely helped trip it".
  - **The build's timing:** the build agent's 9 calls ran 15:46:40-15:59:31 (`projects/speed-kicked-out-three-peat/mom/logs/yt_all.log`),
    not from ~15:35.
- The same "34 / two sessions" figure also went to the hub (side-session note line 31).
- **Fix:** "≥46 lock.sh calls from 15:39 to 16:42, plus the hub's ~10-request listing at 16:34, from three sessions". Add the hub's
  lesson: no channel-listing bursts.

**8. WRONG: § 7 line 262, batch17.sh "waits for a DONE that batch16 never wrote".**
- `yt/batch17.sh` line 9 waits for `^DONE|BOT/429`. Line 10 exits 9 if batch16.log contains BOT/429.
- `yt/batch16.log` ends with "BOT/429 seen, stopping", so batch17 would exit at once and fetch nothing.
- **Fix:** "batch17.sh exits at once (batch16 ended on BOT/429); batch18.sh replaces it."

## MISLEADING

**9. MISLEADING: § 1a lines 63-64 vs lines 83-84. The dad's call "exists only in a fan re-edit".**
- `mom/local/birthday_short.mp4` IS the Abundance Wisdom edit that lines 83-84 warn about:
  - byte-identical (15,693,493 bytes) to the E:\ file, with the AW monogram burned in (`mom/WEB_NOTES.md` lines 81-83, § 3d lines 172-176);
  - RUN.md's ~17:10 entry says the same, and `SEQUENCE-v2.md` line 48 calls it "OUR OWN May 2025 Short".
- Read as written, Affan sees two different edits.
- "Only" is also too strong: it is only true of what's on disk. The original stream is unchecked.
- **Fix:** "On disk, the dad's call exists only in our own AW edit (the repeat-risk file below)".

**10. MISLEADING: § 2 heading, line 125, "Minor-era (16-17): his yes needed, clip by clip".**
- **It contradicts his ruling, three ways:**
  - BRIEF.md: his own 2020-22 mom-house streams are IN, and only other children get flagged.
  - `memory/feedback-minors-rule-hp-film-ok.md` lines 24-27: "He no longer needs a flag for this; just state the year and age once in
    the notes as information."
  - This file's own line 265: "Minors: answered".
- **Fix:** "Minor-era (15-17): IN by his ruling; each clip labelled with date and age; other children flagged".

**11. MISLEADING: line 104, "He cut 'I'm out… not about to stop' in v6 as not deep enough."**
- No file records Affan cutting this line.
- `projects/speed-kicked-out-three-peat/PITCH.md` line 100 ("Cut, and why") records that the pitch dropped it because "it plays without
  the ultimatum before it, so it reads as a non sequitur". `COLD-READ-V6.md` item 7 raised the point.
- His v6 note was about struggle depth in general (research log line 303).
- **Fix:** give the recorded reason. A3-A4 are exactly the ultimatum that line lacked.

**12. MISLEADING: § 5 row Cog1cYrpQjw (line 212), "his musing's exact contrast".**
- The reel was posted 11 Feb 2023, 21 months before Club Shay Shay (27 Nov 2024), so it cannot show the musing.
- Its thumbnail is black and its content is unseen. `mom/IG_PROOF.md` line 40 files it under beat B (possibly the birthday call,
  unconfirmed).
- **Same table, row DPPSEnaibnu (line 213):** "his retelling" is read from the title only. IG_PROOF's method (line 15) opened no reel.
- **Fix:** "same mom-vs-dad theme; content unseen". Mark DPPSEnaibnu "by title".

**13. MISLEADING: § 7 lines 243-257. "Wave 1 is scripted … batch18.sh" sits right above the "First" list, but the two differ.**
- **What batch18.sh runs** (lines 49-62):
  - items 1 and 2;
  - Mother's Day only as one clip audio plus one search;
  - then six clips from the "Then" list (C1a, C2, C3, C5, C6, C7 audio).
- **What it skips:**
  - item 4 (a non-gated copy of the birthday stream) and item 5 (the criterion-2 and adult-window searches);
  - the C1 section, C4, C8 and C10.
- It is 12 calls, not 13 (line 244).
- **Fix:** say exactly what batch18 runs and what's left for wave 2.

## CLAIM-AS-FACT

**14. CLAIM-AS-FACT: § 2a line 133, "Turn that stream off!"**
- The two passes disagree on the word that decides criterion 1:
  - large-v3: "Turn that stream off!" (141.40-142.32, `mom/asr/local/E_fireworks_room.large-v3.txt`);
  - medium.en: "Turn that stream out." (`mom/asr/local/fw_118_180.medium.en.txt` 23.42-24.58, +118 s).
- FINDINGS row 1 carries "[or 'out']", and candidates row 18 flags it too.
- **Line 134 has the same issue:** the 4th "I'm sorry" (160.22) and "Oh, my God" (173.98) are large-v3 only. Medium.en hears three
  "I'm sorry" (155.3-158.3) and nothing after.
- **Fix:** write "Turn that stream off [or 'out']!", and mark 160-175 as one pass only.

**15. CLAIM-AS-FACT: § 4 line 192, "Mother's Day 2023: she hangs up."**
- **The only sources:**
  - a clip title (`P4HHaMkbUi0`, `yt/batch16.log` line 98);
  - an IG caption that says she "did NOT pick up" (IG_PROOF line 43). That is a different account from "hung up after he wished her";
  - an X post recorded only in the research log (line 394), with no text, URL or capture.
- Nothing was watched.
- **Fix:** "Mother's Day 2023: a hang-up, per a clip title and fan posts (unwatched)".

**16. CLAIM-AS-FACT: § 2b row notes that come from titles.**
- **C1a "(locates the moment in C1)"** (line 152): inferred from the title and the same upload day.
- **C8 "(his mom on the phone)"** (line 159): no source says "phone". Not the title, not FINDINGS line 59, not WEB_NOTES line 70.
- **C9 "(his own telling at the time)"** (line 160, and again at line 252): unheard, and uploaded Nov 2021, a year after the 2020 kick-out.
- **C2 "(links his live …)"** (line 153): the description links a /live/ URL whose channel is unverified (batch16.log line 53).
- **Fix:** mark each one "by title", and drop "on the phone".

**17. CLAIM-AS-FACT: § 6 line 220. XhvuBBkKLjY, "kids on frame", listed under "Watched and rejected".**
- Only audio was fetched (`mom/src/XhvuBBkKLjY_audio.m4a`), and `mom/frames/` has no Xhvu frames.
- "Kids" comes from speech: "these kids keep playing" (`mom/asr/XhvuBBkKLjY_audio.large-v3.txt` 433.84).
- `mtxFNmt6R-E` is audio-only too.
- **Fix:** "heard and rejected; kids audible, not frame-checked".

## MINOR

**18. MINOR: § 1b, the A1/A2 join (lines 93-94).**
- There is no pause between "online?" and "Because":
  - the waveform is continuous voice from 66.32 to 67.44, with silence only at 67.48-67.84;
  - large-v3 hears a second "blah blah" at 66.54-67.06, so A1's out at ~66.7 lands mid-voice.
- **The models disagree on "Because" by 0.29 s** (scout 67.35, large-v3 67.06). A stop closure at 67.08-67.12 points to ~67.1, so an
  in at 67.35 likely clips the "Be-".
- "Blah, blah." inside A1 is large-v3 only.
- **Fix:** play A1 into A2 as one piece (~62.9-69.13; SEQUENCE-v2 row 6 now does this), or start A2 at ~67.05.

**19. MINOR: § 1a in-points (lines 52 and 54).**
- **57.84 opens on the end of Adin's "dad"** (large-v3 57.66-57.84):
  - the waveform has Adin to ~57.94, silence at 57.96-58.10, then Speed from ~58.12;
  - medium.en puts "Let" at 58.20 (51.20 + 7 s).
  - **Fix:** in at ~58.05.
- **The head of 23.90-27.12 is uncertain.** The waveform has a voice from ~23.72 under a ring tone. SEQUENCE-v2 row 10 now starts at 25.03,
  leaving out "the other voice's 'No, no way, when we call it' before his line". So the span may open on another speaker.
  - **Fix:** check by ear, and start no earlier than his "my mom's" if that's right.
- Line 56 drops the wouldn't/won't disagreement (candidates row 6).

**20. MINOR: row A4 (line 96).**
- "So I'm like," (81.10-81.70) is on the WIDE.
- 1.7 s of silence follows (81.72-83.40) before "I'm out." (83.44-83.84) on the single.
- The note only says "single from 81.87".
- **Fix:** note both, as row A2 does.

**21. MINOR: § 1c quotes that don't match their spans.**
- **Line 107:** the 6.54-9.94 span is "I'm, like, mom, I was 12 years, I'm, like, mom, I want to be a streamer, she's, like, boy"
  (`mom/asr/QaBBgNjc5Pg_5855.large-v3.txt`). The quote drops words with no ellipsis. The clean in for the quoted words is 8.14.
- **Line 110:** the 28.06-31.72 span is "I moved back, yeah, then I moved back in with my mom for my junior year". For the quoted words,
  the in is 29.40 ("then").

**22. MINOR: lines 122-123, "The last line is the only place where his mom comes round". The scope is unclear.**
- Within the musing table, it holds.
- Across the interview, it doesn't: the full episode has "You know, she even now to this day, she still supports me."
  (`scout/QaBBgNjc5Pg.scout.txt` line 2808, 1:43:57), ~4 s after his own ending clip.
- **Fix:** say "in these lines", or cite both.

**23. MINOR: lines 33-35, "'Not in a weird way': … frame it tight or cover it".**
- It sits under his quote but is this session's reading.
- BRIEF.md, RUN.md and `memory/feedback-minors-rule-hp-film-ok.md` don't record it. The memory says "OK on frame in a normal,
  non-sensitive use".
- Line 36 labels its own rule "not his words"; this bullet doesn't.
- The build's 17:50 SEQUENCE-v2 also plays the argument over the empty room, so only the label is off.
- **Fix:** add "our reading, not his words".

**24. MINOR: line 99, Dazed "prints the same words".**
- Dazed prints "My mom got mad, 'Stop, stop, what are you doing, why are people talking about my son like this?'" (WEB_NOTES line 43).
- That is similar, not the same.
- **Fix:** "a close version".

**25. MINOR: the seen-it check (line 102) misses one line.**
- It omits "she told me to quit or I'm leaving" (`scout/GBvPG_TpMpk.scout.txt` line 12).
- So A3 is a full repeat of our 950K Short, not half of one.

**26. MINOR: § 3 line 185 contradicts § 1b.**
- Line 185: "Only A1-A2 are in-slot and in order".
- Lines 87-88 say A1-A4 "sit IN his slot, in true order". A3-A4 (75-84 s) are in the slot too.
- **Fix:** "A3-A4 are in the slot too, but they repeat our Short".

**27. MINOR: line 41, "everything dated 2021-22 shows him at 16-17".**
- By the file's own rule (line 147), a clip upload date only caps the event date. A 2021 upload can show a 2020 event, when he was 15.
  1-20 Jan 2021 is also 15.
- **In 2b, the same rule isn't applied:**
  - C1a "16" (line 152) and C12 "17" (line 163) are clip channels, so they should read "≤16" and "≤17";
  - C12's "15 days before his 18th" is the upload date, not the event date.

**28. MINOR: § 2b, missing IDs and channels (lines 151-162).**
- **No video IDs on C1-C9**, so § 7 can't be run from this file. The IDs are:
  - C1 `D5FYQQm7IYs`, C1a `bcIJJb9-JjA`, C2 `H81Qnad27jQ`, C3 `_VSHiZ8G8B8`, C4 `_n7kwq8oZ1Y`;
  - C5 `12bBWIGNjU4`, C6 `ObWG_5dENy0`, C7 `m_MxS1uvnYc`, C8 `3FT7fOsUsd4`, C9 `v-CQFdbVgCI`.
- **C10 and C11 show "?" for channels the logs have:**
  - `S_8w_i4dUd8`: Speedy Boykins, 195K. `FcReds3MZew`: NoLimitPlug, 7.9K (`mom/logs/yt_all.log`).
  - `3mGXgbHV3YY`: ExowsPlug. `aChw3aOVpNs`: Speedy Boykins (`yt/batch15.log` lines 31 and 38).

**29. MINOR: § 4, line 197 and lines 203-204.**
- **"Two uploads … where he turns on her":** the logs have only one, `vS1w9DbfE1I`. The other Mother's Day upload, `x4QLNdUfyR4`
  (11 views), is titled "speed mum lost her heart" (batch15.log lines 68 and 77).
- **"The only lead is C7":** by title, C6 "Mom Tells Him To Get Stop Streaming" fits the same reading.

**30. MINOR: the header, lines 19, 24 and 25.**
- **Line 19:**
  - Medium.en covers only the call (7-84 s) and the fireworks argument (118-180 s).
  - The fam A-line and musing times come from the 13 Nov small.en scout, the source behind findings 3-5.
  - Xhvu and mtxF have no frame sheets.
- **Line 24:** C2's original is identified (`t-RMVq_6hTQ`); it just hasn't been fetched.
- **Line 25:** "No search yet" contradicts line 203 ("no text source, across both sessions' web searches"). Say "no YouTube search yet".

**31. MINOR: the criteria are never defined in the file.**
- Here, "criterion 3" is the birthday call (line 44) and "criterion 2" is mom telling him to shut the stream (lines 25 and 203). That
  matches BRIEF.md's bullet order.
- The research log's STATUS block (`aw-speed-pick-2026-11-13.md` lines 13-16) numbers them differently: the birthday call is 2, and
  "feel bad, kept going" is 3.
- **Fix:** list the three criteria at the top of the file.

**32. MINOR: § 6 line 224, "Sept 2025 family/hometown streams (no mom lines)".**
- The sources say "no mom-rejection lines" (FINDINGS line 31) and "no mom-story telling" (research log § 5).
- The transcripts do have mom lines:
  - `scout/CmnDmFYeRow.scout.txt` [0:19:00.3], his dad by context: "Because your mama used to be mad at me."
  - `scout/KCOIJjpLk1M.scout.txt` [0:03:54.2]: "My mom lived right around the corner."
- **Fix:** "no mom-rejection lines".

**33. MINOR: § 6 line 227, `GdoMvHah58I` "he wakes her up yelling".**
- The title goes on: "and crying (ENDS STREAM)" (batch15.log line 63). That is the shape of his criterion 1.
- **Fix:** move it next to the "second look" pair, not under "comic".

**34. MINOR: facts and numbers with no record in any source file except this session's own log line.**
- the Speedy Reports X quote (line 193; research log line 394 has neither text nor URL);
- "565K" for the $100K-allowance post (line 232; IG_PROOF line 88 gives no count);
- `DLYTxF6oPml` and its 328K (line 214): only in research log § 8, with no poster or date. Its Beat cell says "(no caption)", next to a
  quoted caption;
- "~2:51:00" and "Sportskeeda" for the 23 Jul 2023 police call (lines 200-201; WEB_NOTES line 27 has TheSportsRush only);
- `rjQjlYbcNTg` tied to the Sept 2025 off-mic talk (line 230): its date was never read, because batch16 stopped first.

**35. MINOR: minors details.**
- **"His brother Jamal is 16"** (line 36) comes from a Sept 2025 remark, "the most 16 year old room ever" (research log line 288). He is
  most likely 17 now, still a minor.
- **Camden "stays off frame"** (lines 237-238) is stricter than the ruling as recorded: BRIEF.md says other children are "flagged to him
  before use".

## Checked, no defect
- **§ 1a:**
  - **The clip:** date and age (21 Jan 2023, 18). Lit Central, uploaded 24 Jan 2023, 95 s, 1920x1080 60 fps, 3.76 Mbps video.
  - **The call:** every quote in the table matches large-v3 word for word; 44.68, 67.14 and 80.76-82.88 also agree with medium.en.
  - **On frame:** Speed and Adin, plus an adult man behind them at 22.5-58.5, and no children (overview sheet).
  - **Around it:** the dad-call quotes match `birthday_short` large-v3; the IG numbers (1.9M on 5,341 followers); the repeat-risk file
    facts.
- **§ 1b:**
  - **Words and times:** "My mom seen the video" 61.39-62.37, A2's out 69.13, A3's out 80.45, A4 81.17-83.81 (within slop); A3's
    ellipsis.
  - **Shots:** every boundary re-measured (56.43, 62.81, 67.69, 73.87, 81.87, 84.63, 86.34, 111.28, 115.16, 120.62, 125.54, 133.76), and
    every single/WIDE label correct.
  - **Around it:** recorded Nov 2024 at 19; GBvPG 950K / Dec 2024; "hate comments" is new to our audience.
- **§ 1c:** D2 6.54-9.94 and D1 28.06-31.72 are both on Speed's single (sheets). The musing words match the scout word for word; row 4's
  times and all four shot labels are right.
- **§ 2a:**
  - **The clip:** 4 Jul 2022, age 17, at his mother's house. 1080p60, ~1.52 Mbps. Path and copy are as described.
  - **The audio:** the other quoted words agree across both passes. "Ma" is backed by the press headline.
  - **The picture:** Speed on frame 134-147.5, empty room from 148, no other child (`A_fireworks_05s_01.jpg`).
  - **Since:** his World Cup line (HITC, via WEB_NOTES) and the 44K Short.
- **§ 2b:**
  - **Against `batch15/16.log`:** every upload date, length, channel and view count. Examples: C1 6402 s = 1:46:42; C9 214 s; 8.7M, 2.1M,
    2.3M.
  - **Ages:** all computed from 21 Jan 2005. "D5RP_85y0-Q is not in my logs" is true.
- **§ 3:** the 2020 move (Wikipedia and Dazed via WEB_NOTES); "a thousand subs, two thousand subs" (fam 90.43-93.59); his sophomore/junior
  quote (52pXQVGHwEE 4:26-4:41; full episode 40:14-40:30); the dated list. He also says "I was sixteen. I was a junior" (52pXQVGHwEE
  4:03-4:05), which supports ~2021-22.
- **§ 4:** the "MOTHERS DAY ❤️" stream, 14 May 2023, 214 min (TheTVDB via WEB_NOTES); `P4HHaMkbUi0` 3.9K, uploaded 15 May 2023; the
  23 Jul 2023 police call (TheSportsRush).
- **§ 5:** `DI6UXATMaP6` 2.0M views / 233K likes; `DNOcSYhs5aC` 1.9M on 5.3K; `Cog1cYrpQjw` 333K likes, 11 Feb 2023; `DPPSEnaibnu`
  242K on 5.3K.
- **§ 6:** the wrong-person items; the "IG claims with no press"; the privacy note. Club Shay Shay full episode 1:10:27-1:10:48 has his
  remark about the leaked wedding pictures.
- **§ 7:** the `youtube.BLOCKED` flag exists (16:42:17). batch18.sh refuses to run while it's set (batch18.log 17:24:19), sets it again on
  a bot check, and logs age gates. Its calls are ≥65 s apart (45 s sleep + lock.sh's 20 s cool-down). `queue.txt` holds 22 calls. The
  "First" list adds up to ~11.
- **Minors:** his quote and where it's recorded (BRIEF.md, RUN.md, memory); "siblings flagged" as the build's default; adult from
  21 Jan 2023; moved out ~late Aug/Sept 2023.
