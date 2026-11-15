# Cold read of the FINAL report: bolt-celeb.md (file mtime 23:26 PKT, 14 Nov 2026), files only

Read: the gate (whole), the report (whole), `api-findings.md`, `candidates.md`, `bolt-shares.md`, `narration-table.md`, `amy-diagnosis.md`, `coldread.md`, the raw JSON in `work/api/` (run with `python -I`), `AW-SHORTS-NOW.md`, `CLAIMS.md`, `IG-SEARCH-LOG.md`, `HUB-BOARD.md`, `yt_api_log.jsonl`. No web, no API, no playback.

**Numbers checked: about 90**, against the JSON and logs. Most match exactly. The matches include:
- Bolt: 803 uploads, 2.02M median, 292 uploads in 2026 at 1.67M, latest 60 at 663K, Adele 15.9M, Capaldi 2.99M, Forgot 2.96M, Celine 387K.
- AW: Kanye 22K, Mamdani 9.3K, Police 5.85M and 11.9K (0.2 %), KSI, Winnie, Hollywood BROKE 170K.
- C14: all eight retellings (views, likes, dates, durations), the long-form rows, Spike Lee parts 1-2, the 36.55M and 1.46B official videos.
- Tony × Gaga: all 14 rows plus the 105x, 137x, 65x, 19x, 0.24x and 0.13x multiples, recomputed from `s1_channels.json`.
- Peers: MrWood 6.0K, MJ Forever 46.5K, the detail. 39.2K, Michael Jackson Shorts 3.9K, plus the 390x.
- Instagram: every like and share count I traced into `IG-SEARCH-LOG.md`, and the 130 view-only tiles (20+25+30+30+25).
- API log: the 5 searches and 666 units. The log has 211 `bolt-celeb` rows, of which 171 are uncached (5 searches + 166 one-unit calls = 666 units).

Mismatches and problems follow.

## MUST-FIX

**1. First line and accounting under-report the open items; C and F are marked "done" when they are not.**
- Quote (line 1): "NOT max effort yet: E is open (...). B was closed by the hub's rule at 22 full-count posts, not 40. G and H are complete on card 2 only..."
- Quote (accounting): "**C** done ... the retellings of card 2 and C14" and "**F** done for card 2 (§ 0 table); arcs and gate notes for C14 and cards 3-4."
- What's wrong:
  - Gate item C needs "every finalist beat searched on YouTube or Shorts in at least 3 phrasings". Card 2 has ONE search ("tony bennett lady gaga", `yt_api_log.jsonl` 21:44). Cards 3 and 4 have none (the report says so on the cards). C14 has one retelling search ("michael jackson favela"). Searches 4 and 5 are own-voice hunts, not retelling searches.
  - Gate item B says a block means "NOT max effort for this item". There were freezes and refusals, and 22 of 40 posts. The first line calls B "closed" in prose instead of listing it as open.
  - Gate item F needs a § 0 gate statement with evidence per gate. Only card 2 has one. Cards 1, 3 and 4 have gate notes only.
  - The first line never names C or F, and uses bare letters. Gate item 7 says the first line lists what is NOT done.
- Evidence: `api-findings.md` § 4 ("search 1"), the log rows at 21:44, 21:48, 21:55, 23:18 and 23:19.
- Fix: replace line 1 with: "NOT max effort yet: B (22 of 40 reels read, and Instagram froze or refused 6 searches), C (YouTube proof in 3 phrasings per beat: Tony × Gaga 1, Coachella 0, VMA 0, favela 1 retelling search + 2 own-voice searches), E (no downloads), F (a § 0 gate table for card 2 only), G and H (cards 3-4 have no variants or pre-mortems; the favela card has no script), I and J (on this final: in progress)." Change the accounting of C and F to "partly done" or "open", with the same counts.

**2. The question numbering conflicts with the hub board, and the report attributes Q3 to the hub.**
- Quote: "Opens on his yes (Q3: an SD-origin event as the climax; the hub, 23:14)". Also: "Q1 alone opens nothing."
- What's wrong:
  - `HUB-BOARD.md` Q1 is: "May SD archive carry an MJ Short, the climax included, upscaled and letterboxed? ... it opens MJ's proven legend beats, the Super Bowl 1993 ... and Motown 25". That is the report's Q3.
  - The board's Q3 is "Snape's Studio numbers".
  - The board's 23:14 triage says the legend beats "wait on his answer to Q1", not Q3.
  - The report's own Q1 is a narrower question (a letterboxed SD overlay while the climax is 720p+).
  - Affan sees the board's numbering. If he answers "yes" to the board's Q1, the report says that opens nothing. His Q3 is also a different question on the board.
- Fix: renumber the report's questions so none collides with the board. Tell the hub that the board's Q1 is the report's "SD climax" question. Suggested labels: Q-SD (the board's Q1, opens the legend beats), Q-biopic (the board's Q2), Q-letterbox (the report's narrower Q1) and Q-C14 (drug boss). Change "the hub, 23:14" to "the board's Q1".

**3. Wrong comparison in the C14 prediction.**
- Quote (card 1, item 8): "It sits between AW's no-wound MJ Shorts since October (85-89K) and its MJ median (~119K)."
- What's wrong: centre ~80K is BELOW 85K, so it is not between 85-89K and 119K.
- Fix: "It sits just under AW's no-wound MJ Shorts since October (85K and 89K), discounted for narration, the missing own voice and the September police loser." Or move the centre to ~85-90K and say why.

**4. The "since 2 Oct" MJ stat mixes two sets.**
- Quote (top and Lessons 2): "MJ Shorts since 2 Oct: median ~119K, 6 of 15 at 150K+." `api-findings.md` § 3 adds "(the two newest, 1-2 days old, are left out)".
- What's wrong, from `aw_uploads.json`, Shorts of 60 s or less with "Michael Jackson" in the title, 2 Oct onward:
  - 17 Shorts: median 118,576 (~119K), 6 at 150K+.
  - With the two newest left out (15 Shorts, up to 11 Nov): median 125,332, still 6 at 150K+.
  - So "~119K" belongs to 17, and "6 of 15" excludes the two newest. The pair as written does not match.
- Fix: "median ~119K, 6 of 17 at 150K+ (up to 14 Nov)". Or use the 15 with a median of ~125K.

**5. Mamdani is called "the one narrator-led test", but its narrator share is unknown.**
- Quote: "**Mamdani (21 Aug, AI voiceover, no face, 9.3K) is the one narrator-led test, and it failed.**"
- What's wrong:
  - `narration-table.md` § 1 lists Mamdani's narrator share as "unknown (length 0:48; no word or second split in any file)".
  - It is a no-face political topic, not a celebrity, so it is a weak test of "narration over a celebrity".
  - The report also says "of the published Shorts with a known share, none exceeded ~22 %", which excludes Mamdani. It cannot then be the one narrator-led test.
- Evidence: `narration-table.md` row 1 and observation 4.
- Fix: "Mamdani (21 Aug, AI voiceover, no face; narrator share unrecorded; 9.3K) is the only published AW Short with a voiceover-led look, and it failed. It is a poor test: a political topic with no celebrity face." Delete "narrator-led test".

## SHOULD-FIX

**6. Stale or mixed numbers: `AW-SHORTS-NOW` (16:45, rounded) alongside the API (exact).**
- Examples:
  - "Son 445K" appears repeatedly (W2, closest winner, calibration). The API (`aw_uploads.json`, 10 Nov) says 455,911. The README calibration is the only place "445K" should stay.
  - "Bieber 26K" in L1 and on cards 3-4, but the top summary and card 3 say 27.2K. API: 27,243. The report contradicts itself.
  - "Snape 23K" is 24,076 now, and "Patrick Stewart 13K" is 13,975.
  - "CRUEL father 5.1M" in W1 is 5.155M. The report says 5.2M elsewhere.
  - Bolt's "NFL legend 9.6M" and "Ali 2M" in "What the evidence says" are the 12 Nov figures. The API says 10.28M (the report notes this only in the API paragraph) and the Ali Short is 2.70M.
- Fix: use API values throughout, with one line saying the calibration quotes are the README's. Bolt: NFL ~10.3M, Ali ~2.7M.

**7. "Only MJ clears 150K" and "0 of 9" are overstated, and the nine are not defined.**
- Quote: "on AW today, only MJ clears 150K ... Non-MJ celebrity Shorts: 0 of 9."
- What's wrong:
  - Since 2 Oct, Nick Walker Parents (166.5K, 4 Oct) cleared 150K, and Fitzwater (103.8K) came close.
  - The nine are an unlisted hand-picked set. They are Kanye, Diana, Bieber, Snape, Stewart, Owen Hart, Elon, Kane and Ninja.
  - The set excludes the bodybuilders (Levrone 49.6K, CBum 46.6K, Walker).
  - The report concedes the Nick Walker exception in L1, but the top summary does not.
- Fix: "only MJ and Nick Walker (bodybuilding) clear 150K". List the nine once in a footnote, with the rule "mainstream music, film, TV, royals, HP, tech".

**8. The "decays" lesson (L2, Lessons 6) over-reads two data points.**
- Quote: "A frame fed twice decays on AW too: police-and-MJ went from 5.85M (May) to 11.9K (Sep)."
- What's wrong:
  - AW's other September MJ Shorts include Drug Addiction 10.8K (5 Aug), Dead Body DECOY 9.8K (19 Aug) and Lisa Marie FAKE 17.7K (21 Sep).
  - So the 11.9K fits "scandal or rumour MJ Shorts were low before October" at least as well as "police decays".
  - That also bears on C14's drug-boss twist, which is the same family. The card does not weigh this against the retellings.
- Evidence: `aw_uploads.json`.
- Fix: say "n=2, confounded: MJ rumour and scandal Shorts in Aug-Sep ran 10-18K", and add that C14's twist belongs to that family. Keep it as a hypothesis in L2, not a lesson.

**9. The "no download" reasoning does not say what the lift would be.**
- Quote: "I can't say that one file would genuinely lift it past 150K" and "What would move it toward 150K, all four together".
- What's wrong:
  - The hub's exception turns on whether ONE download could lift a lead past 150K. The report never says what the centre becomes if all four conditions are met.
  - The reasons given (Q4 open, children in the footage) are things a download cannot fix, so they answer a different question.
  - Evidence the report leaves out: both Spike Lee parts carry the UPLOADER's description "Spike Lee delivers a keynote in Brazil including about the making of Michael Jackson's they don't care about us" (`s4_spike_parts.json`). Part 2 (`BHYmFzijQHI`) also carries the tag "Michael Jackson Santa Marta". The report cites only a comment, and names Part 1 as the file to test.
- Fix: add one line, "if all four are met, centre ~X K". Add the uploader description and the Part 2 tag. State whether Part 2 is the better first file. The no-download call looks defensible, but it should rest on that number.

**10. The cold-read bookkeeping is wrong.**
- Quote: "an independent Opus cold read on the 20:25 version (`bolt-celeb/coldread.md`, 21 findings, all applied)."
- What's wrong:
  - `coldread.md` says it read the report "saved 19:41" (the file was last written at 20:09).
  - It never names a model.
  - "21 findings" is correct.
- Fix: "on the 19:41 version (file written 20:09)". Drop "Opus" unless the log shows it.

**11. The API cap numbers do not match the log.**
- Quote: "all callers together have used 39 of 95."
- What's wrong: `yt_api_log.jsonl` has 42 uncached searches on 14 Nov across all callers (ig-mj 9, hp-cast 8, ig-icons 8, hp-films 7, ig-sports 5, bolt-celeb 5). The last three are ig-mj searches at 23:24, before the 23:30 save.
- Also: `api-findings.md` still opens with "462 units: 3 searches (300) and 162 one-unit calls", while its last line says 666 units and 5 searches. Update the header.
- Fix: "42 of 95 by the 23:24 log". Make the api-findings header 666 units, 5 searches, 166 calls.

**12. The "Shorts" peer medians use an unstated 180 s rule, and "narration isn't the lift" is over-read.**
- Quote: "MJ Forever ... last-6-months Shorts median is 46.5K", "the detail. 39.2K", and "Narration isn't the lift."
- What's wrong:
  - The medians use every upload of 180 s or less. By the 60 s rule AW uses, the detail. has NO Shorts in the last six months. MJ Forever has 4, with a median of 28K.
  - AW's ~119K is a 6-week window of 17 Shorts, and AW has 542K subs. The comparison is across different windows, different audiences and different lengths.
  - Two peers cannot show that narration is not the lift.
- Fix: state "uploads of 180 s or less" in the table header. Soften to "the narrated MJ peers' medians are low (28-47K), though not directly comparable to AW's window".

**13. The all-time MJ stat counts long videos.**
- Quote (`api-findings.md` § 3): "MJ Shorts: median 143K, 35 of 71".
- What's wrong: the 143K median only appears when 70 MJ uploads of ANY length are included (34 at 150K+). MJ Shorts of 60 s or less: 67-71 items, median ~168K, 34-36 at 150K+. Labelling the 143K figure as "MJ Shorts" understates the base.
- Fix: "MJ Shorts (60 s or less) median ~168K, ~35 of ~70 at 150K+" or relabel it as "all MJ uploads".

**14. The 738K Short is described both ways.**
- Quote (§ 0 G4 row): "the 6-8 s and 17 s clip reposts (261K, 15K, 738K) didn't [win]".
- What's wrong: `api-findings.md` § 4 gives the 738K Short 1.6x its channel's average, so it did beat its channel. Only 261K (0.24x) and 15K (0.13x) fell below.
- Fix: "the 6-8 s reposts (261K, 15K) fell below their channels' averages; the 17 s repost did 738K (1.6x)".

**15. Card numbers do not agree across files.**
- What's wrong: the report calls Tony × Gaga card 2 and the favela C14 card 1. `candidates.md` says "C28 ... LEAD (card 1)" and "C40 ... (card 2)". `api-findings.md` § 4 is headed "Card 1, Tony Bennett × Lady Gaga". A reader who follows a cross-reference lands on the wrong card.
- Fix: relabel in `candidates.md` and `api-findings.md`: Tony × Gaga = card 2, Coachella = card 3.

**16. The first line is too long and jargon-heavy for Affan, and "NO PICK" comes late.**
- What's wrong:
  - The opener is four dense lines of "E", "B", "G", "H", "C14" and "hub's rule" before "NO PICK." appears at line 9.
  - The gate wants the status line first and "no pick" first thereafter.
  - Other shorthand a reader must decode: "LEAD", "the bar", "own voice", "the Prince ABC anchor", "Topaz chain", "Content ID", "mute test", "AW factor".
- Fix: line 1 = the gate-form status, spelling out each open item in words (see finding 1). Line 2 = "NO PICK." Then the counts. Define "C14" as "the favela card" at first use. Add a one-line key for LEAD (below the 150K bar) and own voice (a real person speaking on camera).

## NIT

**17.** Two facts in the C14 arc are not in any file. The "statue, there since 2010" has no support. "the police won't guarantee his safety" rests on a retelling's title. The "Olympic bid" is supported, by the AP description (12 Feb 1996: "chances of playing host to the 2004 Olympics"). That AP text also calls the "no primary source has been read" line into question. Fix: source or cut the 2010, and cite AP for the bid.

**18.** Card 3 names "the Oct 2026 Sahara Ray overdose reports". `hd-inventory.md` L107 says Daily Mail-sourced, unconfirmed, and "Do not use as a hook... ties drugs". Naming a private person's alleged overdose in a Bieber card is unnecessary. Say "unrelated overdose reports about an ex" or drop it.

**19.** The "hidden names win in 2026" statistic (1.87M for n 32 against 698K for n 29) rests on a "crude name list" that is not saved, so it cannot be reproduced. The report itself says it is a 2026 effect. Add "(crude list, n about 30 each, not causal)".

**20.** The Instagram counts: the log has 23 post pages. The report says 22 full counts plus 2 partial, which is 24. Two logged pages are partial (B9TaW5bj4Zt and DKAFNfVxdD_). Say 21 full plus 2 partial of 23 pages, or recount.

**21.** The C14 prediction is stamped "22:05", but `CLAIMS.md` (22:02) already states "centre ~80K". Say "22:02, re-checked 23:25".

**22.** Card 4 uses Nick Walker "Got HUMILIATED" (644K, 30 Sep) as the closest winner "same shape", while the report calls bodybuilding "a confounder". Add "(bodybuilding lane; discount)" on that line.

**23.** Narration is counted in words for Bolt and the card 2 script (41 %) and in seconds for AW (≤22 %). The report flags it once. Repeat the unit on the target line "40-55 %" so it is not read against AW's 22 %.

## Checks that passed

- **Numbers and ranking:** the ranking matches the centres (C14 80K, Tony 35K, Coachella 30K, VMA 25K, with the Super Bowl card conditional and unranked).
- **Card format:**
  - The 9 items are in the gate's order on cards 1-4.
  - The statement "MAX EFFORT DONE" is NOT typed.
  - Every card names the gates failed or weak BEFORE the prediction.
  - Cards 1 and 2 carry a 5K and a 5M pre-mortem and a runner-up; the Super Bowl card is "not locked".
- **Hub rules:**
  - The "no download" decision follows the hub (23:14) instruction (no download unless one file clearly lifts a lead past the bar), subject to finding 9.
  - The MJ legend beats ARE listed as "opens on his yes".
- **Ledgers:**
  - CLAIMS was updated for every beat.
  - Every candidate has a verdict (42 logged).
  - The 130 view-only tiles, the 5 searches, the 666 units and the narrator word count (43 of ~105 = 41 %) all recompute.

## Verdict

**NO PICK stands.**
- Every lead's centre is below 150K by the evidence in the files: C14 ~80K, Tony × Gaga ~35K, Coachella ~30K, VMA ~25K.
- No lead is mis-ranked. C14 is first on the YouTube proof and last on the AW record; that tension is handled honestly.
- Nothing in the files supports a higher centre. The closest honest upside is C14, and the report names the four conditions that would lift it. Finding 9 asks for a number for that case.

**The fixes are not large enough to need a full re-read.**
- The five MUST-FIXes are edits to wording and numbers in the first line, the accounting, the question labels and the Mamdani, "between" and 119K sentences.
- They do not move any centre or the verdict.
- Because the first line and the question labels change, a short re-check of just those passages is enough, not a fresh cold read.
