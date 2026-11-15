# Re-read (J): hp-films FINAL + projects/oldman-good-sirius/PITCH.md after the cold-read fixes

15 Nov 2026 ~01:05 PKT, as of the files at ~01:02. A verification pass that judged files only. There was no network, nothing was played, and nothing was edited except this file.

**Read:**
- `coldread.md`, `PITCH.md` (00:52), `RUN.md` (00:53), `hp-films.md` (00:53): line 1, the FINAL block, and the working notes where a fix
  points into them.

**Checked against:**
- `proof/audio_measure.txt`;
- `proof/anchor_1to1.jpg`, viewed, and its `tools/anchor_1to1.py`;
- `meta/api_a1|a2|b3b|b3c|b4a|b4b|b4c` TSV, plus the saved `*_videos.json` descriptions;
- `meta/api_comments_*.json`, `meta/api_extra.err` and `meta/peer_UCf3SpupfoGnXEpgaGRGPbqg.json`;
- `yt_api_log.jsonl`, which is now readable;
- `src/yt/*_sect.scout.txt` and `src/local/hsc2024_full.scout.*`;
- `src/hsc/*.scout.json` coverage;
- ffprobe on both Oldman downloads;
- `IG-SEARCH-LOG.md`, HP-EXECUTION § 7, MAX-EFFORT-GATE, README:101-124 and HUB-BOARD "The bar".

## The 24 defects
| # | Status | Evidence |
|---|---|---|
| 1 | FIXED | The prediction is re-locked for v3c: range 10K-600K, centre 40-100K. PITCH § Prediction lists the comparables line by line, including the four the cold read named: 34K/47K, Snape ~23K, non-MJ 12-50K and the calibration overshoots. The 5M pre-mortem uses only v3c content, and "NO PICK" leads FINAL :6. The "finalist" label is a separate problem: see N1 |
| 2 | PARTLY FIXED | The statement is now line 1 of both files, and it says "replaced only when every item is closed". **Unfixed:** PITCH.md has no counts (MAX-EFFORT-GATE item 7: searches per platform and per beat, downloads, advisor calls, cold read). The list also leaves out four open things: the pre-commit advisor gap (12), the Horowitz clips check (5), the voices line (13) and the word-level in/out (8) |
| 3 | FIXED | The Rickman/Snape rows now sit under "Context only, a DIFFERENT promise (rule 2), not counted" (FINAL :39-41; PITCH weak gate 2). b69Bxu02vLo is tagged title-only, unviewed, reading withdrawn. A's own proof is restated, and thin IG is weak gate 2, right after "under the bar". The same rule is applied unevenly elsewhere: see N3 and N4 |
| 4 | FIXED | pAO2y3kqkl0 is labelled "a 242 s clip, not a Short". dLzpf4MYxns (34,426) and the 2026 copies (217,238 / 54,417 / 29,686) are added, and all match api_a1.tsv. The "news headline" pre-mortem is gone. The 79K that came in with the cold read's own fix is a new problem: see N3 |
| 5 | PARTLY FIXED | Beats 3 and 4 now have 3 YouTube phrasings each (a2 + b3b + b3c; b4a + b4b + b4c; yt_api_log.jsonl 00:50:56-00:51:01). Beat 1 and the IG payoff/end-line searches are ACCEPTED-AS-OPEN (C). **Unfixed:** Horowitz's Sep 2026 clips are unread, and they're not named. The on-disk list of his main channel (peer_UCf3…json) starts 30 Sep 2026, after the 14 Sep sitting, and the Clips channel isn't on disk. playlistItems costs 1 unit and isn't one of the 12 capped searches (README:69-71). So "the 2026 pride beat isn't in any Short" (FINAL :44, PITCH G4) still overstates what is only "not found in 2 searches" |
| 6 | PARTLY FIXED; the rest is ACCEPTED-AS-OPEN (E) | **Fixed:** G2 is OPEN and Source quality PARTIAL. anchor_1to1.jpg was rebuilt as asked: a face-centred 9:16 window, Lanczos only, 480 px crops never resized, beside Prince P7/P8 and Bieber, with a verdict. ~1.3 Mb/s matches ffprobe (a 1,271 kb/s video stream), and the Lanczos-only rule is stated. **Open and named:** the film pictures and the zoom-out finish test. **Unfixed:** the VP9 re-fetch wasn't run (it's only offered as an option), and anchor_oldman.jpg is no longer cited but still sits in proof/ unlabelled. **Viewing note:** the 2023 tile is visibly smeared next to P7/P8, so "just below Prince" is generous, though it is far above the approved Bieber tile |
| 7 | FIXED | Horowitz's voice is cut, and the row-3 label carries his question. The cut points exist in the transcripts: in 2023, "Gary… why do you say this?" falls between rows 1 and 2; in 2026, "Yeah?" comes after row 3's last word |
| 8 | PARTLY FIXED | v3c is reordered so the payoff ends the Short, which meets rule 6 on paper. My word count of the four segments gives ~29-35 s, in line with "~33-36 s ±2". **Unfixed:** no word-level alignment and no per-row in/out. The sequence header defers them to the build, but they could run now on the files already on disk |
| 9 | FIXED | "Was Oldman A Good Sirius?" is 5 words and 25 characters, and it names the payoff question. The runner-up is 4 words, and the old title is rejected with its reason |
| 10 | FIXED | The 1,360 comment is quoted in full, with its concession. The 544 and 319 comments are added, along with "he says it of all his work" and the rule "no caption may imply Sirius-only". All match api_comments_*.json |
| 11 | FIXED | G5 reads "Press: THR (its own Short). EW and Variety unconfirmed". G3 and G5 read "PASS on text (by ear OPEN)" |
| 12 | NOT FIXED | There is no "pre-commit advisor" item, and no note that the final call is also the first review. v3c, like A and v3b, was committed with no advisor call (FINAL :16 "2 calls… final call pending"). The statement names only "I (final advisor call)" |
| 13 | PARTLY FIXED | Oldman's Jun 2025 sitting is fetched (src/hsc/oldman_v3_y25.mp3, 00:52) and transcribing (named in E). The 2019 passage was read and :535 corrected. **Unfixed:** there is still no line on the voices considered (Lowden 66K, Radcliffe 2019/2014) and why Radcliffe 2024 wins. :535 now also says "2020 partly transcribed", which is wrong (N6) |
| 14 | PARTLY FIXED | The IG counts are now 37 = 28 + 6 + 3, with reads 46 / 43 / 41, and B is listed as open. **Unfixed:** the two "searches run" tables (:570-577) are still empty, and the RSS count was changed to "8 in full, 1 partly", which the disk contradicts (N6) |
| 15 | FIXED | proof/audio_measure.txt holds every quoted number (0.096 / -31.3, 0.105 / -18.0, 0.147 / -25.0; the RSS 0.098 / -32.1), and PITCH and FINAL cite it. Its windows cover the v3c rows; its row labels are off (H2) |
| 16 | FIXED | The kill now cites the German Shorts at 165.7K and 48.4K. The 301K is tagged "description doesn't match, not viewed" (FINAL :70-71) |
| 17 | FIXED | "All three sources are HSC podcast stages", and "crop above" the TIFF credit. The crop is needed now, because v3c's row 3 shows the 2026 picture |
| 18 | FIXED | "suspect #2", and "no Iris/Proteus on real faces, Lanczos only" in His rules and RUN.md |
| 19 | FIXED | "the 92NY frame in rows 2 and 4", which is correct for v3c |
| 20 | FIXED | "a legend's self-doubt answered with warmth" |
| 21 | FIXED | "wanted to cry", "a moment with Daniel he takes pride in", and no age on screen (G5). "A teenager" in the 5M pre-mortem is true for any Oldman film (Radcliffe was 13-17 in 2003-06), and it isn't a caption |
| 22 | FIXED | "≈ 4-6 %… the Snape build's own share wasn't measured" |
| 23 | FIXED | Lesson 1 now separates the show's feed (Oldman 2023), hp-cast's slice (Oldman 2026) and the video on disk (Radcliffe) |
| 24 | PARTLY FIXED | **Fixed:** the statement is on line 1. **Resolved:** the a1 query can now be checked in yt_api_log.jsonl ("gary oldman mediocre sirius", 21:38:42), though api_a1.tsv still says q=[]. **Unfixed:** the Oldman 2026 face is now one number (388 px, the anchor_1to1 tile), but no frame time is recorded. The Gleeson numbers still differ in the working notes (:441 496,276 / 30,963 vs :506 481.3K / 30.4K); the FINAL avoids them |

**Tally:** 16 fixed, 7 partly fixed (2, 5, 6, 8, 13, 14, 24), 1 not fixed (12).

## New errors from the rewrite
### Blocking: in FINAL, PITCH or RUN
1. **N1, the 150K-bar wording breaks the house rule.** The rewrite labels a below-bar idea a "finalist" and pitches it, in four
   places:
   - FINAL :6 "The lane's best finalist, under the bar and offered for Affan's call";
   - card :19 "(finalist, UNDER the bar)… PITCH-track";
   - PITCH.md :10 "PITCH… for Affan's call" and :14-15 "this text, his OK, then the raw build";
   - RUN.md lines 1 and 4 ("finalist under the bar… offered for Affan's call").

   The rules say otherwise:
   - README:111: "below-bar ideas are never pitched";
   - README:114: "Under it = a LEAD";
   - MAX-EFFORT-GATE:90-91: a PITCH is only for an idea that clears the bar;
   - memory no-below-bar-pitches: it is "a bench line";
   - the hub's precedent, HUB-BOARD:26-27: "NO PICK. One lead: …".

   The range top of 600K also misses the bar's "top reaches 1M+" half (README:112-113). "Finalist" is carried over from the cold read's
   own fix 1.2, which was written for the AT-the-bar case.
2. **N2, the payoff proof is mislabelled.** PITCH Proof gives "the payoff 47K (the owner's) and 15.7K". WREU59HfMpM's own description
   (api_b3b_videos.json) is about the Oldman-Radcliffe bond and Felton's jealousy, not the last-day question. It is bond proof.
3. **N3, the proof is selective in two directions, both against the standard used for b69Bxu02vLo and the 301K:**
   - **Over-counted:** the "mediocre" 79K (zDxiMCq8hjM) appears in PITCH weak gate 3, the Proof row and the comparables. It is ET's "Gary
     Oldman Reflects on Being Part of the 'Harry Potter' Phenomenon" (Aug 2025); its title and description have no "mediocre", and it
     wasn't viewed.
   - **Not weighed:** the bond-promise Shorts from the rewrite's own searches. The IG bond reels count as proof, but none of these do,
     and they are missing from freshness and from the upside comparables. Payoff freshness itself holds: no saved title or description
     shows the last-day question outside 8qn-er0UfPI.
     - ZT-z59SSL6w, 165,467: b3c's only hit, also in a2; its description is "a mentor to Daniel Radcliffe off-screen";
     - zXYxe3BKBrY, 232,601: the official HP channel, "Daniel Radcliffe on working with Gary Oldman";
     - uWa1iBhQ5pk, 346,467: "Godfather off screen";
     - MU_w8a7Oj_o, 211,327;
     - 7zyCjAwrKf4, 1,489,079: a "backstage clip", content unknown.
4. **N4, rule 2 is applied unevenly to the fan edits.** 3CBY39D2rbY (623K) and BqXqigoPqFI (194K) are Sirius-death "sadness edits" set
   to music (their descriptions name Lil Peep/XXXTENTACION and Lana Del Rey). That is a different promise, and AW can't make the format
   (no music bed). Yet they count in Proof, in the FINAL table, in the upside comparables and in the 5M pre-mortem. They are context,
   like the Rickman rows.
5. **N5, "12 API searches" overstates the freshness evidence.** FINAL :44 and PITCH G4 base "nothing joins…" on 12 searches, but five
   were for other leads or hooks (a3, a4, b1, b2, c1). Only 7 bear on v3c's beats. PITCH Proof also still says "the end beat: none
   found (3 phrasings)", though in v3c the 2026 pride beat is the turn (row 3) and the end is Radcliffe's payoff.
6. **N6, the RSS count doesn't match the disk.** FINAL :15 says "8 transcribed in full, 1 partly", and :535 says "2020 partly
   transcribed". radcliffe_v3_y20.scout.json spans 0-3,589.4 s of a 3,591.3 s wav (161 segments, no gap over 20 s), and
   radcliffe_v1_y14 has no transcript at all. The true count: 8 full, 1 untranscribed (2014), and 2025 in progress.
7. **N7, "Cold read: 1 (24 defects, all applied)" (FINAL :17) is untrue.** Item 12 isn't applied, and parts of 2, 5, 6, 8, 13, 14 and
   24 aren't.
8. **N8, the 2-source facts.** G5's "two sources each" counts two copies of one recording. Radcliffe's video and Horowitz's Short title
   are the same 2024 sitting, so the last-day question rests on Radcliffe's telling alone. E asks for 2 independent sources, and E
   doesn't name this. Oldman's 2025 sitting may close it.
9. **N9, the statement wording.** C says "the Data API quota is spent until 13:00 PKT", but only the 12-search cap is spent; 1-unit
   calls still work (README:69-71).

### Hygiene: working notes, proof labels, outside the lane (non-blocking under the brief's carve-out)
- **H1, the 5 new searches aren't in the working notes.** The notes still read "7 of my 12 searches used" (:157) and "5 searches are
  left in reserve" (:192), and the requests table (:574-576) is empty. The b3b/b3c/b4a/b4b/b4c queries and results exist only in meta/
  and yt_api_log.jsonl.
- **H2, the proof files mix v3b and v3c row numbers.** anchor_1to1.jpg labels "Radcliffe 2024 row 3" beside "Oldman 2026 (v3c row 3)".
  audio_measure.txt calls Oldman 2026 "row 4" and Radcliffe "row 3".
- **H3, the ▶ STATUS resume block (:92-106) wasn't rewritten.** It still says "v2 sequence… centre of 100-250K" and "No cold read yet".
  The notes also still label v3b "RECOMMENDED" (:347) and v3 "runner-up" (:373), with no "superseded" marker. A cold resume would start
  from the wrong state.
- **H4, the IG-log caption correction can't be checked from files.** IG-SEARCH-LOG.md:332 (00:53, marked as a correction) gives
  DWYiL2hgXuQ's caption "as read on the page that night". No on-disk capture of that caption exists (ig_rows.txt, 21:16, holds only the
  letters/terrified text), and it cites a "20:09 row" that is at 20:08. Working notes :380 lean on it; FINAL and PITCH don't.
- **H5, the rule-12 framing.** PITCH's v3b note credits v3b with ending "in the subject's own voice (rule 12)", which implies v3c
  doesn't. By the rule's text (HP-EXECUTION:240, "the person's own voice"), v3c passes on Radcliffe's line. Reword the note.
- **H6, the header times.** The FINAL says "~01:05" but hp-films.md was written at 00:53. The PITCH says it was "re-locked ~01:00" but
  was written at 00:52.
- **H7, for the hub:** HUB-BOARD.md:24 still shows "PITCH: 'Oldman Called His Sirius MEDIOCRE'… center 100-250K".

## v3c against the rules
| Rule | Result | Evidence |
|---|---|---|
| Two voices (rule 5) | PASS | Oldman and Radcliffe; Horowitz is cut |
| Labels (rule 5; "labels low") | PASS on paper | Low labels on rows 1 and 3. Radcliffe is introduced by his face, and the Voices line says "each labelled" |
| Payoff placement (rule 6) | PASS on paper | The payoff row starts at ~62 %, with a hard cut ~2 s after "wanted to cry". Unproven until the word-level in/out |
| Title ≤ 5 words, names the payoff (rule 4) | PASS | 5 words, 25 characters |
| One topic (rule 1) | PASS | The title, frame 1 and last line are all Oldman's Sirius |
| Minors | PASS | Teen Radcliffe appears only in film footage, and the Snape shot has no students |
| Censor | PASS | No drug, self-harm or suicide words in the four rows |
| Picture (rule 7) | OPEN, named | The film shots are unsourced, and Oldman 2023 is soft |
| 150K bar wording | **FAIL** | N1 |

## Verdict
(a) **The statement line is accurate but not complete.** It omits the pre-commit advisor gap (v3c was never put to the advisor),
Horowitz's unread Sep 2026 clips, the voices line, the word-level in/out (it can run now) and E's second independent source for the
last-day question. It also overstates the quota block, and the FINAL's "24 defects, all applied" is untrue.

(b) **The disclosure is honest; the label and format are not compliant.** "NO PICK" comes first, and the centre, comparables and weak
gates are all named first. But README:111/114 and MAX-EFFORT-GATE:90-91 make a 40-100K idea with a 600K top a LEAD, as a CARD that is
never pitched. It should read "NO PICK. One lead: Was Oldman A Good Sirius? (centre 40-100K)" in FINAL, PITCH.md and RUN.md, with no
OK-to-build ask.

(c) **One more short, targeted re-read is needed,** run after Oldman's 2025 transcript is read. That transcript is the only open item
that could change the sequence itself. Re-read the edited lines only (N1-N9, the unfixed parts of 2, 5, 6, 8, 12, 13, 14, and the
statement line). As of the files at ~01:02, no conclusion changes, so no new cold read is needed.
