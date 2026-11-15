# Cold read: hp-films FINAL + projects/oldman-good-sirius/PITCH.md (J)

An independent cold reader, working from files only. No network, nothing played. The audio, Instagram (IG), YouTube (YT) and image claims
were checked against the evidence files on disk. Files read:
- `PITCH.md` and `RUN.md` (mtime 00:19), and `hp-films.md` (mtime 00:20);
- the rules: MAX-EFFORT-GATE, PITCH-CHECKLIST, HP-EXECUTION § 7, and the run's README / HUB-BOARD;
- the evidence:
  - `src/yt/*_sect.scout.{txt,json}` and `src/local/hsc2024_full.scout.*`, read in full;
  - in `src/hsc/`, the logs and a spot-read of four transcripts (Oldman v2, the Oldman v4 slice, Radcliffe 2019 and 2020);
  - `meta/api_*.tsv|json`, `api_lane_ids.json`, `peers.txt` and both comment files;
  - the 83 hp-films rows of `IG-SEARCH-LOG.md`;
  - the 5 proof JPGs (not the `_af.png` / `_fa.png` scratch frames), the 2 anchor tools and both download logs;
  - `CLAIMS.md` and `AW-SHORTS-NOW.md`.
- `yt_api_log.jsonl` could not be read (permission denied), so the a1 query string is unverified (item 24).

Line numbers are as of those mtimes. Each one carries a short quoted anchor in case lines shift. About 40 claims were spot-checked. The
matches are listed after the defects.

## Defects, most severe first

### 1. The 150K bar and the prediction: "ONE pick" is not what the files support
- **Where:**
  - `hp-films.md:15` ("ONE pick… No other idea clears the bar");
  - `hp-films.md:56-59` and `PITCH.md:61-73` (locked prediction);
  - origin: `hp-films.md:231-237` ("REVISED 22:10", the v2 card).
- **Wrong 1:** the centre of 100-250K was locked at 22:10 for **v2, whose hook was the Rickman promise**. v3b (23:20) dropped that hook,
  but the prediction was never re-locked.
- **Wrong 2:** the 5M pre-mortem still banks the dropped promise:
  - `PITCH.md:70-71` "the Snape/Rickman promise is the hottest HP Shorts topic… Oldman gives it a human turn";
  - `hp-films.md:59` "the hottest HP promise of 2026".
- **Wrong 3:** no comparable is given for 100-250K. README:112-115 requires "State every center against it, **with the comparables it
  rests on**", and says a center under 150K is a LEAD, with "no pick" first.
- **The comparables the files themselves give all point lower:**
  - the same-lane control, the Snape Short, is 23K (`AW-SHORTS-NOW.md:59`);
  - recent non-MJ Shorts sit at 12-50K (`PITCH.md:9`);
  - the source owner's own Shorts of the two key lines did **34,426** (dLzpf4MYxns, the hook line, `api_a1.tsv`) and **47,010**
    (8qn-er0UfPI, the payoff), on a 227K-sub channel;
  - the house calibration overshot 2 of 3 times: Burnt Hair 300-800K → 83K, La Toya 300-700K → 19K (README:115).
- **Wrong 4:** a centre of 100-250K is not "150K or more". "No other idea clears the bar" implies that this one does.
- **Fix:**
  1. Re-lock the prediction for v3b as it stands, naming the comparables line by line (with the four above among them). Write a 5M
     pre-mortem that uses only what v3b contains.
  2. Relabel the result line: "No pick clears the bar. One finalist AT the bar: Oldman/Sirius (centre X, comparables Y)". That is the
     ig-icons wording on HUB-BOARD:26. Or "no pick" first if the re-locked centre lands under 150K.

### 2. The statement line understates what is open, and PITCH.md has none
- **Where:** `hp-films.md:4` ("NOT max effort yet: J… and I… this line is replaced when both are done"); `PITCH.md:1-4` ("Status:
  sequence in text for Affan's OK"); `RUN.md:4` ("Waiting for Affan's OK on the sequence").
- **Wrong:** only J and I are named. Items 1, 5, 6 and 11-15 below are also open:
  - **C / item 1:** per-beat phrasings;
  - **E:** the anchor test is invalid, other tellings are unchecked, facts lack 2 sources, and the audio has no file;
  - **item 2:** the film pictures are not sourced, framed or quality-gated;
  - **I:** there was no pre-commit advisor call on A or v3b;
  - **H:** the prediction was not re-locked;
  - **B:** follower counts are missing.

  Replacing line 4 once J and I land would type a false MAX EFFORT DONE (MAX-EFFORT-GATE.md:93-101; memory
  no-false-completion-line).
- **Wrong in PITCH.md:**
  - it opens with no max-effort statement at all, against MAX-EFFORT-GATE item 7 (:44-53) and PITCH-CHECKLIST:19 ("The pitch then
    opens with the max-effort statement");
  - it presents the sequence for his OK, against item 7: "the sequence is not presented as final".
- **Fix:**
  1. Make line 1 of PITCH.md and line 4 of hp-films.md read: "NOT max effort yet: C (per-beat YouTube/Instagram phrasings), E (anchor
     test, other tellings, 2-source facts, audio file), item 2 (film pictures), I (pre-commit advisor), H (re-lock for v3b), B
     (followers), J/I final".
  2. Add the counts line under it.
  3. Change "this line is replaced when both are done" to "replaced only when every item above is closed".

### 3. The proof table sells a promise the cut doesn't make, and leans on a withdrawn reading
- **Where:**
  - `hp-films.md:30-31, 34-35` (the b69Bxu02vLo, 0wMBtQXDl2M, DcVeFNpRYwI and DWavjdgkqGq/DU1Al7DEv0s rows);
  - `PITCH.md:13-15` ("The rest of the stitch is strongly proven… Snape's 'Always' 525K… 'Only Rickman knew' is at 5.9M");
  - `PITCH.md:50`;
  - `hp-films.md:42, 163, 455, 470, 536`.
- **Wrong 1:** v3b keeps Rickman to 2 s, inside Oldman's sentence. That is the right call: the one-topic test passes in the cut. But
  5.9M, 5.6M, 496K, 525K and 471K are all proof for the Rickman/Snape-secret promise, and HP-EXECUTION.md:216-217 (rule 2) says
  "Proof doesn't transfer to a different promise". The bait-and-switch has moved out of the sequence and into the proof table and the
  5M pre-mortem.
- **Wrong 2:** b69Bxu02vLo's content is unverified, yet the report states it as fact.
  - Its own description (`api_lane_ids.json`) reads: "Watch Gary's face change as he becomes Sirius in a second…".
  - HP-EXECUTION v1.3 (:7, :75) withdrew the "Oldman learns only Rickman knew" reading at 22:10. It was never viewed.
  - Yet it is still called "the reason's promise" (:30), "the RtH 'only Rickman knew' beat" and "Nida Sarfraz's *Return to Hogwarts*
    clip" (:455), and "5.94M RtH Short" (:536).
  - `hp-films.md:163` lists it among the **A4 search** results, but it is not in `api_a4.tsv`. It comes only from the
    `api_lane_ids.json` lookups.
- **Fix:**
  1. Move the five Rickman/Snape rows out of A's proof table into a "context: a different promise (rule 2)" note.
  2. Tag b69Bxu02vLo as "title only; description doesn't match; not viewed; reading withdrawn in HP-EXECUTION v1.3", and move it from
     the A4 row to "lookups".
  3. Restate A's own proof as:
     - the hook: 316K, 217K (Mar 2026), 79K Shorts, plus IG 35.6K / 4.9K;
     - the payoff: 47K (Horowitz's own Short);
     - the end beat: none found (item 5).
  4. Make "Instagram proof is thin" the first weak gate (PITCH-CHECKLIST:38: "No Instagram proof makes an idea a weak contender").

### 4. The hook's proof is selective: "1.10M" is a 4-minute clip, and the owner's own Short of the line did 34K
- **Where:** `hp-films.md:27` (pAO2y3kqkl0 row); `PITCH.md:13, 50`; `hp-films.md:364` ("a proven 1.1M promise").
- **Wrong 1:** pAO2y3kqkl0 is 242 s, not a Short. Its description is "Gary Oldman discusses the unlikely scene from HARRY POTTER he did
  not enjoy shooting" (the frozen lake), per `api_lane_ids.json`.
- **Wrong 2:** omitted from the PITCH and the FINAL table:
  - Horowitz's own 60 s Short of exactly "My work is mediocre" (dLzpf4MYxns): **34,426**;
  - three 2026 Shorts of the line: 217,238 (30 Mar, 13 s), 54,417 (31 Jul) and 29,686 (16 Aug), all in `api_a1.tsv`.
- **Wrong 3:** the 5K pre-mortem calls "mediocre" "a news headline from 2023". The files show it was re-cut through 2026.
- **Fix:**
  - Label 1.10M "242 s clip (not a Short)".
  - Add the dLzpf4MYxns 34,426 row and the 2026 copies.
  - Restate the entry tax as "the hook line is a recurring Short (316K 2024, 217K Mar 2026); the owner's own Short did 34K".

### 5. Per-beat search coverage falls short of item 1 / C, and the end beat's IG proof has no source
- **Where:** `hp-films.md:41-42, 160-163, 188` ("5 searches are left in reserve"); `hp-films.md:33, 376` ("opens on 'the ones who love
  us'"); `PITCH.md:50` (G4).
- **Wrong 1, YouTube:** MAX-EFFORT-GATE:23 and :73-74 ask for **every finalist beat** searched in at least 3 phrasings. v3b has:

  | Beat | Searches |
  |---|---|
  | Beat 1, "mediocre" | 1 (a1) |
  | Beat 3, Radcliffe's payoff | 1 (a2) |
  | Beat 4, Oldman's 2026 pride | **0** |

  a3 is a cut beat (H3) and a4 is the Rickman promise, so neither counts for v3b. "3+ phrasings" was counted per lead, not per beat.
  Five searches sat in reserve.
- **Wrong 2:** G4 says the join, "Oldman's pride" included, "is found nowhere", but no search contained the pride beat.
- **Wrong 3, the 2026 clips:** Horowitz clips the 2026 sitting:
  - 3_qDzFnIiZM, 16 Sep 2026, 14.5K (`api_lane_ids.json`);
  - tVm7ajSlOIU, 1.2M, on Josh Horowitz Clips (HP-EXECUTION.md:85).

  Whether the "pride" passage was cut is unchecked.
- **Wrong 4, Instagram:**
  - No hp-films IG search uses a Radcliffe phrasing ("radcliffe oldman", "good sirius") or the end line ("the ones that love us"). The
    Oldman searches are: "gary oldman sirius black", "gary oldman mediocre", #siriusblack, plus two refused phrases.
  - Horowitz's own IG, @joshuahorowitz, wasn't checked for the Apr 2024 payoff clip.
  - The claim that DWYiL2hgXuQ "opens on 'the ones who love us'" has **no supporting row**. `IG-SEARCH-LOG.md:266` records only
    "letters… terrified… extremely sweet", and no other file in the run folder contains the phrase.
- **Fix:**
  1. Three phrasings each for beats 1, 3 and 4 needs 7 more searches (2 + 2 + 3). Only 5 remain before the 13:00 PKT quota reset, which
     comes after the 10:00 final.
     - Spend those 5 on beat 4 ×3 (e.g. "gary oldman favorite harry potter scene daniel", "the ones that love us never really leave us
       sirius") and beat 3 ×2.
     - Keep C named as open for beat 1, or run its 2 after 13:00.
  2. Read Horowitz Clips' Sep 2026 uploads by `playlistItems` (1 unit).
  3. Run IG searches for the payoff and the end line.
  4. Delete "opens on 'the ones who love us'" at :33 and :376, or log the read that shows it.

### 6. "Source quality PASS" and "G2 PASS" are premature
- **Where:** `PITCH.md:48` (G2), `PITCH.md:54` (Source quality), `PITCH.md:80-81` ("Film pictures NOT sourced"),
  `hp-films.md:48`.
- **Wrong 1, the film pictures:** they carry about 40-50 % of the runtime and none is sourced, framed or probed:
  - frame 1 (Sirius);
  - 2 s of Snape in row 2;
  - all of row 4 (PoA, "picture only").

  So G2, the Source-quality gate and HP rule 7 can't be checked. Rule 7 (HP-EXECUTION.md:227-233) allows SD at 25 % of the runtime or
  less and no Iris. The Snape Short's SD/DVD picture is v1.3's suspect #1 (HP-EXECUTION.md:125-144).
- **Wrong 2, `anchor_oldman.jpg` fails as proof:**
  - It takes a **centred** crop (anchor_oldman.py:18).
  - The Oldman 2023 tile reads "(no face found: full frame)".
  - The "RADCLIFFE HSC 2024… face 156px" tile shows a chair, not a face: a false detection at t=1700 s.
- **Wrong 3, `anchor_full.jpg` measures size, not sharpness:**
  - It holds no approved tiles.
  - Its tiles are resized to 480×480, so they are not 1:1 at delivery scale.
  - Face px is size, not sharpness.
  - PITCH-CHECKLIST:87-93 asks for a finish test with the build's recipe, 1:1 crops at delivery scale beside Prince P7/P8 and Bieber,
    and a verdict. None was given.
- **Wrong 4, the 2023 bitrate:** Oldman 2023 is format 299 (H.264 1080p59.94, stream 1,413 kb/s per
  `dl_oldman2023_0800-1800.log`; the file is about 1.4 Mb/s with audio). It is planned as the row-2 close at ×1.78, with no finish
  test.
- **Wrong 5:** v1.3's rule "no Iris on a real face" means the anchor recipe (Iris 1.0 + Proteus) has to change. The pitch doesn't say
  how.
- **Fix:**
  1. Mark G2 and Source quality "OPEN (film pictures unsourced; anchor test not run)".
  2. Source the PoA, OotP and Snape shots, and probe and frame-sheet them.
  3. Rebuild one anchor sheet. Use head-locked crops at delivery scale and the planned finish (Lanczos only), with Oldman 2023,
     Radcliffe 2024, Prince P7/P8 and Bieber side by side, and write the verdict: "at/above Prince", "just below" or "clearly below".
  4. Try a VP9 fetch (e.g. format 303) of 38pRftXvOmA against the 1.4 Mb/s H.264.
  5. Drop or label `anchor_oldman.jpg` as a failed detection.

### 7. A third, unnamed voice (rule 5)
- **Where:** `PITCH.md:35` (row 4: "Josh Horowitz → Oldman… PoA, Sirius and Harry (picture only)"); `PITCH.md:53` ("2 voices + 1
  interviewer question… PASS").
- **Wrong:**
  - HP-EXECUTION.md:223-224 (rule 5) says "Two voices at most… Every voice is introduced by its face or a low label before it speaks,
    and no voice goes unnamed".
  - Horowitz is a third voice, and in row 4 he speaks over film picture with no face and no label.
  - That is the Snape Short's suspect #3 ("a voice the viewer can't place", HP-EXECUTION.md:155-158).
- **Fix:** choose one, and say so in the Shape row:
  - cut the question and let Oldman's "I have the scene with Daniel where I talk about…" stand; or
  - show Horowitz's face with a low label for the question, and name the rule-5 exception.

### 8. Payoff placement (rule 6), and a runtime the stated windows don't support
- **Where:** `PITCH.md:29` ("~35-40 s"), `PITCH.md:33-35` (windows), `PITCH.md:53` ("payoff ~55 %").
- **Wrong 1:** rule 6 (HP-EXECUTION.md:225-226) says "the payoff by about 60-70 %… and the end within about 3 s of the payoff line".
  - The payoff (row 3) is followed by all of row 4: 45:07-45:30, 23 s raw, at least 13 s trimmed. The end is far more than 3 s after
    the payoff.
  - If row 4 is counted as the payoff instead, it lands above 90 %.
  - Rule 12 (warm end in his voice) was chosen over rule 6 without saying so.
- **Wrong 2:** the stated windows sum to about 67 s raw (row 1 ~2 s, plus 29 s, 13 s and 23 s). "35-40 s" and "~55 %" assume about
  30 s of trims that no in/out points show.
- **Context:** the scout files are segment-level only, so the timestamps can be checked only to the segment (all match; see below).
- **Fix:**
  1. Run a word-level alignment on the three sections.
  2. Give in/out points per row, the computed runtime and the payoff %.
  3. State the rule-6 deviation and why rule 12 wins, or reorder.

### 9. The title names the setup (rule 4), and it's the 2023 trade headline
- **Where:** `PITCH.md:1` and `hp-films.md:256` (title "Oldman Called His Sirius MEDIOCRE"); `PITCH.md:58` ("title ≤ 5 words" PASS).
- **Wrong:**
  - HP-EXECUTION.md:220-222 (rule 4) says "Name the payoff or the secret, not the setup".
  - "Called… MEDIOCRE" is the setup. That is the pattern v1.3 blames in "Radcliffe Thought Snape HATED Him" (:163-168).
  - It is also the Dec 2023 news line: THR's own Short, "Gary Oldman Calls His 'Harry Potter' Performance 'Mediocre'"
    (`api_a1.tsv`).
  - The word count passes (5).
- **Fix:** offer a payoff-naming title within 5 words, e.g. his own question, "Was Oldman A Good Sirius?". Alternatively, keep the
  current title and write the rule-4 exception with its reason.

### 10. The judgment quote is trimmed, and G5's counter-evidence is incomplete
- **Where:** `PITCH.md:27, 52`; `hp-films.md:22, 173` ("Gary Oldman's 'mediocre' is the next guy's great", 1,360); `PITCH.md:51`
  (G5 counter-reading).
- **Wrong 1, the quote:** the 1,360-like comment reads in full **"It's far from his best role but** Gary Oldman's 'mediocre' is the
  next guy's great" (`api_comments_escpEISnUso.json`).
- **Wrong 2, the concessions:** on the same Short, 544 likes say "not knowing what happens next probably kept him from nuancing". On
  8qn-er0UfPI the top comment (319) says the problem was that he "wasn't given much material".
- **Wrong 3, the counter-reading:** G5 covers only "hated". In the same passage Oldman says it of all his work:
  - Horowitz: "this is not unique to your career";
  - Oldman: "I'd put it all on a fire and burn it and do it all again" (`38pRftXvOmA_sect` 07:29-07:57 = video 15:29-15:57);
  - Oldman: "I'm terrible in that movie" (video ~16:58).
- **Fix:**
  - Quote the comment in full.
  - Add both counter-points to G5.
  - Add the build rule: "no caption implies the doubt is Sirius-only".

### 11. G5 press sources, and the by-ear PASS
- **Where:** `PITCH.md:51` ("also in Variety, THR and EW"); `hp-films.md:249`; `PITCH.md:49, 51` (G3, G5 PASS).
- **Wrong 1, the press:**
  - THR is supported: its own Short is in `api_a1.tsv`.
  - EW appears only as a 40-view aggregator title ("Dig Dig Talk… - Entertainment Weekly News", `api_a1.tsv:27`).
  - Variety has no file in the run folder. `firstparty-tellings.md:32` cites comicbookmovie.com instead.
- **Wrong 2, by ear:** PITCH-CHECKLIST:61 defines G5 as including "by ear". The working gate's separate "Heard by ear | OPEN" row
  (`hp-films.md:243`) was dropped from the PITCH. G3 (tone) was judged from ASR text alone.
- **Fix:**
  - Write "press: THR (its own Short); EW and Variety unconfirmed", or log the articles.
  - Mark G3 and G5 as "PASS on text; by ear OPEN (build)".

### 12. The pre-commit advisor call happened before there was a finalist
- **Where:** `hp-films.md:102` ("before finalists → 'no finalists yet…'"), `hp-films.md:12`.
- **Wrong:** item I (MAX-EFFORT-GATE:86) and item 4 (:36-38) require the advisor before committing to the finalist and the sequence.
  Neither commit had an advisor call:
  - A was committed at 22:10;
  - v3b was chosen at 23:20.
- **Fix:** list "I: pre-commit advisor on A/v3b" as open. Or record that the final-report call is also the first advisor review of
  this finalist and sequence.

### 13. Other tellings and other voices are incomplete (E)
- **Where:** `hp-films.md:531` ("Radcliffe 2014 / Vol. II 2019 / Vol. III 2020… NOT transcribed"), `hp-films.md:82-83` (lesson 3,
  "2023 → 2024 → 2026"), `hp-films.md:164` (Lowden).
- **Wrong 1, Oldman's 2025 sitting:**
  - Oldman's HSC sitting of 12 Jun 2025 (X_m_ksn2rMk, 78 min) is in `api_lane_ids.json`. Its description lists "Hogwarts houses".
  - The run folder holds no transcript or note of it (searched `.md`, `.txt` and `.tsv`).
  - In 2026 Horowitz calls it "our ongoing debate about the quality of your work in Harry Potter that we've had over the years"
    (BWMPDqyMc5Y sect 06:37+).
  - The 2025 sitting may hold Oldman's reply to Radcliffe's 2024 story: the join, in their own words.
- **Wrong 2, Radcliffe's other sittings:** `radcliffe_v2_y19.scout.txt` and `radcliffe_v3_y20.scout.txt` **exist**, contradicting
  :531.
  - 2019 has an Oldman passage at [0:23:54]: "the first person I remember… was Gary Oldman… freaked out to meet somebody".
  - `radcliffe_v1_y14` has no transcript.
- **Wrong 3, another voice:** Jack Lowden on Oldman's Sirius (wTM27ZzeRa8, 66K) is a voice that was found but never weighed.
- **Fix:**
  - Fetch the Vol. III RSS audio and transcribe it around the HP section.
  - Read the 2019 passage.
  - Correct :531.
  - Add one line on the voices considered and why Radcliffe 2024 wins.

### 14. Counts that don't match the files, plus gate B's follower counts
- **Where:** `hp-films.md:7-8, 11, 566-572`.
- **Wrong 1, Instagram searches:** the IG log has 83 hp-films rows: **37** search/page rows plus 46 reads, not 38.

  | Result | Rows |
  |---|---|
  | Loaded | 28 (27 distinct; one is a re-shot of "draco malfoy misunderstood") |
  | Phrase refusals | 6 |
  | Failed loads | **3** (the first "seven potters", @wizardzworld, @howeverythingworks) |

  The report says 10 refused or failed. The reads (46 / 43 / 41) match.
- **Wrong 2, the RSS audio:** "9 podcast episodes' audio from RSS, all transcribed": 8 of 9 were transcribed (there is no
  `radcliffe_v1_y14.scout.*`).
- **Wrong 3, the report's own tables:** the "Instagram searches run" and "YouTube requests run" tables are empty.
- **Wrong 4, gate B (MAX-EFFORT-GATE:70-72):** B asks for the account's followers on each read. Most of the 43 reads have none. The hub
  held ig-sports to exactly that ("most follower counts unread", HUB-BOARD:27). Several reads that lifted B past 40 are tiny posts (2,
  448, 869, 905 likes).
- **Fix:**
  - Correct the counts to 37 / 28 / 6 + 3 and 8 of 9.
  - Point the empty tables to `IG-SEARCH-LOG.md`.
  - Add the followers for A's IG proof accounts (@movies.verse, @soulcinema_ and the two Snape pages), or list B as open.

### 15. The audio numbers have no measurement file
- **Where:**
  - `hp-films.md:44-47`;
  - `PITCH.md:54` (flatness 0.096 / 0.105 / 0.147; -31.3 / -18.0 / -25.0 LUFS);
  - `RUN.md:10`.
- **Wrong:** no file in `hp-films/` or the run folder holds these measurements. Other lanes save them; for example
  `ig-mj/dl/8Ys5IngU6wg/8Ys5IngU6wg.probe.txt` keeps its ebur128 output.
- **Fix:** save the ebur128 summary and the gap-flatness windows per source (e.g. `hp-films/proof/audio_measure.txt`) and cite it.

### 16. The B kill cites a 301K Short whose own description is a different beat
- **Where:** `hp-films.md:66` ("already a 2026 Short, at 301K and 166K"), `hp-films.md:260`.
- **Wrong:**
  - cqVrG0_o2J0's description (`api_lane_ids.json`): "Before filming, Gambon would jokingly act confused about his role". That is the
    "taking the piss" bit from the same sitting, not the Ferrari take. It was not viewed.
  - The Ferrari story's own Shorts are German (165,704 and 48,370), plus Nida's 914.
  - B's centre (40-120K) is under the bar either way, so the "no other idea clears" conclusion is unaffected.
- **Fix:** cite 166K (German, the same angle) and 48K as the kill evidence, and tag the 301K as "description doesn't match; not
  viewed".

### 17. The TIFF source description is wrong twice (moot for v3b, but stated as fact)
- **Where:** `PITCH.md:17-18` ("Two of the three sources are podcast stages… a burned-in 'Footage Provided by TIFF' credit outside the
  9:16 crop"), `RUN.md:11`.
- **Wrong 1:** all three sources are HSC podcast stages: two at 92NY, one at TIFF.
- **Wrong 2:** in `proof/oldman2026_sheet.jpg` the credit spans source x ≈ 36-944 px at the bottom of every tile (measured on all 12
  tiles). A centred 9:16 crop is x 656-1264, so the tail of the credit sits inside it.
- **Why it's moot:** v3b shows no 2026 picture.
- **Fix:** write "All three are HSC podcast stages". For the credit, write "inside a full-height 9:16 crop; crop above it or avoid the
  2026 picture".

### 18. Stale suspect numbering, and v1.3's real suspect #1 is unaddressed
- **Where:** `PITCH.md:16` and `hp-films.md:347` ("HP-EXECUTION suspect #1… the hook sold one story").
- **Wrong:** in v1.3 that is suspect #2 (HP-EXECUTION.md:145). Suspect #1 is now "the picture read as AI" (:125), which the pitch never
  addresses (see item 6).
- **Fix:**
  - Write "suspect #2".
  - Add a line: "no Iris/Proteus on faces; Lanczos only (rule 7)".

### 19. The named failure doesn't fit v3b's frame 1
- **Where:** `hp-films.md:57` ("frame-1 fatigue after the Snape Short"); `PITCH.md:66` ("frame-1 fatigue (the Snape Short's look)").
- **Wrong:** v3b's frame 1 is the Sirius film image (`PITCH.md:32`). The 92NY repeat first appears with Oldman in row 2, and Dan's
  92NY frame in row 3. `PITCH.md:63-64` words this correctly.
- **Fix:** write "the 92NY frame at rows 2-3 reads as a repeat of the Snape Short".

### 20. The Shape row's theme belongs to v2
- **Where:** `PITCH.md:53` ("one theme (not knowing what was coming)").
- **Wrong:** that theme ran through v2's "killed me off… it's me" beat, which v3b dropped. v3b's end beat is pride in a scene, not
  foresight.
- **Fix:** write "one theme: a legend's self-doubt, answered with warmth (Radcliffe, then his own pride)".

### 21. Wording that would mislead if it reached a caption
- **Where:** `PITCH.md:50` ("Radcliffe's tears"); `PITCH.md:24, 59` and `hp-films.md:19, 353` ("the one scene he's proud of");
  `PITCH.md:23` and `hp-films.md:19` ("teenage").
- **Wrong:**
  - Radcliffe says he "wanted to cry", not that he cried.
  - Oldman was asked for "a moment… between you and Daniel that you do take pride in", not for his one proud scene.
  - "Teenage" rests on Radcliffe's hedge "I think for the fifth film" (`hsc2024_full` 28:22).
- **Fix:**
  - Write "wanted to cry".
  - Write "asked for a moment with Daniel he's proud of, he names…".
  - Add to G5: no caption says he cried, says "only scene", or gives an age.

### 22. The cost is called "measured", but it was quoted
- **Where:** `PITCH.md:84` ("the Snape build's measured cost").
- **Wrong:** `projects/harry-potter-prank/BRIEF.md:16` re-quoted it from reference-usage-costs, and `REPORT.md:59` says "I cannot give
  my own share".
- **Fix:** write "≈ 4-6 % (the house estimate for a code-built AW Short; the Snape build's share wasn't measured)".

### 23. Lesson 1 overstates what the RSS feed found
- **Where:** `hp-films.md:79` ("it found all three of A's lines").
- **Wrong:**
  - The Radcliffe line came from the on-disk video (`src/local/hsc2024_full`).
  - The 2026 line came from hp-cast's RSS slice.
  - The RSS feed found Oldman 2023.
- **Fix:** write "it found Oldman's 2023 lines; Radcliffe's came from the video on disk, the 2026 line from hp-cast's RSS slice".

### 24. Minor items
- **Oldman 2026 face size:** 405 px (`anchor_full.jpg`) against 382 px (`anchor_oldman.jpg`). Pick one and name the frame.
- **The Gleeson reel's numbers differ:**
  - 496,276 / 30,963 in `IG-SEARCH-LOG.md:286` and `hp-films.md:437`;
  - 481.3K / 30.4K in `hp-films.md:502`.
- **The a1 query isn't recorded:** `meta/api_a1.tsv` has the header `q=[]`, so the a1 phrasing can't be confirmed from hp-films'
  files.
- **The statement isn't on line 1:** MAX-EFFORT-GATE:93/100 asks for it on the report's first line, but it sits on line 4, under the
  H1 and the FINAL header.

## Rule dispositions (item e)
| Rule | Result | Note |
|---|---|---|
| Minors | PASS | Teen Radcliffe appears only in PoA/OotP film footage, which his 10 Nov ruling allows (README:102). All three interview sources are adults. Pick a Snape shot without students |
| Censor | PASS | There are no drug, self-harm or suicide words in the v3b lines. "Killed me off" is only in H3 and isn't on the list |
| Title ≤ 5 words | PASS on count, FAIL on rule 4 | Item 9 |
| More than two voices | **FAIL** | Horowitz is a third voice, unnamed over the film picture (item 7) |
| Music under voice | PASS on paper | No bed; the film is picture only. The flatness numbers have no file (item 15) |
| Payoff placement | **FAIL, unstated** | The end comes far more than 3 s after the payoff, and the runtime isn't demonstrated (item 8) |
| One topic | **PASS in the cut** | Title, frame 1 and last line are all Oldman's Sirius, and "like Alan" is his own reason over 2 s. The Rickman bait now lives in the proof table and the 5M pre-mortem (items 1 and 3) |
| 150K bar | **Not cleared as stated** | The centre straddles the bar, was inherited from v2 and has no comparables (item 1) |

## Checked and matched (not defects)
- **Quotes, all at segment level** (the scout JSONs have no word timings):
  - Row 1 and row 2: the `38pRftXvOmA_sect` segments 06:43.78-07:13.19 and 07:14.09-07:28.72 = video 14:43.8-15:28.7. "Mediocre in
    it" and "maybe if I had read the books like Alan… played it differently" both fall inside.
  - Row 3: `hsc2024_full` 28:22.23-28:45.20 contains "he asked me on the last day… have I been a good Sirius? And I wanted to cry. I was
    like, yes, oh my God". The local file is the 55:48 YouTube video (inventory.md:17), so its times are video times.
  - Row 4: `BWMPDqyMc5Y_sect` 07:06.68-07:39.86 = video 45:06.7-45:39.9. It contains Horowitz's question and Oldman's "the people that
    we've loved, or that have loved us, living here, and that we carry them always with us".
  - H3: 13:32.8-14:14.2.
- **The RSS offset fix holds.** Oldman v2's printed time minus 33:43 gives 14:33 / 15:00 / 15:16 / 15:44 / 16:14. The RSS runs about
  60.5 s ahead of the video. The 2026 slice puts the question at 42:28 and the answer at 42:35.
- **YouTube numbers all match:**
  - escpEISnUso 316,301 / 11,457 (3 Oct 2024);
  - 8qn-er0UfPI 47,010 / 2,079 (16 Apr 2024);
  - pAO2y3kqkl0 1,095,128 / 11,342 (29 Dec 2023), 4.8× of 227K;
  - b69Bxu02vLo 5,935,905 / 69,220 (16 Jul 2026), 6,930 subs, 857×;
  - 0wMBtQXDl2M 5,647,060 / 135,199 (11 Aug 2026), 94×;
  - f3pRVmGE--w 5,486,434;
  - a3 44,072;
  - a2 783,391 / 211,290 / 165,459 / 8,811;
  - 38pRftXvOmA 280,145 (67 min);
  - wTM27ZzeRa8 66,222;
  - the published dates of BWMPDqyMc5Y (14 Sep 2026) and OYJ7W0mJZUA (11 Apr 2024);
  - the B and C kill numbers 301,141 / 165,704 / 48,370 / 344,131 / 312,890;
  - all six peer rows (subs, medians, top uploads).
- **Comments:** all five quoted comments and their like counts match (1,360; 148; 48; 25; 11).
- **Instagram reads match:**
  - DVWX_vaDZEP 35,630 / 4,927 (1 Mar 2026);
  - DWYiL2hgXuQ 96,322 / 10,551 (27 Mar 2026);
  - DcVeFNpRYwI 495,895 / 36,891 (21 Aug 2026), 4.3M followers, 0.12;
  - DWavjdgkqGq 525,493 / 56,026 and DU1Al7DEv0s 471,494 / 60,138;
  - Dudley 2,217,860 / 136,640; WB UK 896.2K / 233.3K; the deleted scene 665,641 / 63,070;
  - the reads 46 / 43 / 41.
- **Formats:**
  - 38pRftXvOmA is format 299, H.264 1080p59.94, for 480-1080 s;
  - BWMPDqyMc5Y is format 616, VP9 1080p23.98, for 2280-2760 s;
  - Radcliffe is 1920×1080 at 59.94 fps (inventory.md:17; prank PITCH:10).
- **Faces in `anchor_full.jpg`:** 748, 759, 405, 528 and 530 px as quoted. Prince 772/883 and Bieber 125 are in `anchor_oldman.jpg`.
- **Comparables and context:**
  - AW comparables: Son Saw His Dad AGAIN 445K, Holland 11K (7.9K Studio), Snape 23K;
  - HBO premiere 25 Dec 2026 (`hbo-peg.md:8`);
  - K: hp-films' claims are in `CLAIMS.md` (lines 18-23, 33, 40-41, 47). The 2026 end beat (RSS 42:28) is a different passage from
    hp-cast's Rickman card (RSS 44:40-46:10).

## Verdict
The "one pick" is honestly disclosed but mislabelled. The weak gates are named first, there is no guarantee line, and the v3b cut
genuinely passes the one-topic test. But its centre straddles the bar. It was locked for the Rickman-hook v2 and never re-locked when
v3b dropped that hook, and it rests on no stated comparable. The comparables the files do give point lower: Snape 23K, recent non-MJ
12-50K, and 34K and 47K for the owner's own Shorts of the two key lines. Most of its proof is for a promise the cut deliberately doesn't
make. Under README:112-115 that makes it a finalist at (or under) the bar, not a pick that clears it, so "No other idea clears the bar"
should read "no idea clears the bar; one finalist at it". "NOT max effort yet" is the correct first line, but its list (J and I only)
is incomplete. Also open are per-beat search coverage (beat 4 unsearched, 5 searches unused), the anchor test and film pictures, other
tellings including Oldman's 2025 sitting, the 2-source facts and audio file, the pre-commit advisor, the re-lock for v3b and the
follower counts. The stated plan to replace the line once J and I land would type a false MAX EFFORT DONE. PITCH.md itself carries no
statement line and asks for his OK, so as written it would reach him looking final.
