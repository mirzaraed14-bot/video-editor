# Cold read (Sonnet), AW IShowSpeed report, 17 Nov 2026

Judged from files only. Checked against `api/*.json`, the run log (`research/instagram-beat-mining/2026-11-17-speed.md`), the scout files, the Club Shay Shay transcript and one frame sheet. All AW upload numbers in TEARDOWN § 2 (views, likes, comments, ages, likes per view) match `api/aw_stats.json`. The 12 searches, 6 Reels tabs, 16 keyword pages, 15 phrasings, 23 reels, 110 grid tiles and 13 downloads all reconcile. The Club Shay Shay quotes match the transcript.

## BLOCKER

1. **BLOCKER. REPORT.md lines 3-4 and 49, CANDIDATES.md #33, README.md STATUS: the tears-to-boots re-telling is "Ftbl Lab 3.3M" is not supported.**
   - REPORT line 49: "Tears → boots: Ftbl Lab ... 3.3M (18 Jul)". The headline (line 3) says both leads are "re-tellings of joins that already ran big (49.9M and 3.3M)".
   - The run log (05:08) calls it the "journey → boots join". The title is "Overtime", which reads as a Speed-and-Ronaldo montage over the years.
   - The only evidence is two comments in `api/comments_MqnU059R2YE.json`: "that boot's worth a million dollars" (17 likes) and "...we all cried that horrible day" (1 like). The top comments there are about singing off tune, the World Cup ending and brand CR7. No frames or audio were checked.
   - The only same-join Shorts that were actually seen are 80.9K (`4LWSuIgygwU`) and 16.1K (`Mf0YRdEmVDg`). The report's own run log row 04:18 says "THE JOIN EXISTS, SMALL".
   - Fix: say the 3.3M is "a Speed-and-Ronaldo montage that includes the boots; whether it shows the tears is unchecked". Lead 2 freshness becomes "ran at 81K, 3.3M montage unchecked". The NO PICK verdict does not depend on this (see the verdict line), but the headline must not assert it.

## FIX

2. **FIX. REPORT.md line 99 and line 96-97: implied cause, and a disputed fact stated as fact.**
   - "The viewer gets: a hero who sees his loudest fan" and the arc "tears. Four days later he opens Ronaldo's own gold CR7 World Cup boots, one of two pairs". This implies Ronaldo answered the tears. Section 7 of the same card says no cause may be claimed (@withalvin__: gift planned before the loss; unverified).
   - "Ronaldo's own ... World Cup boots" is stated flat. Lines 127-128 say "game-worn" is only Speed's words and outlets disagree. The scout ASR (`scout/WGRAVtYFPCo.scout.txt`) has Speed saying "These are samples", and K24 says samples.
   - Fix: "the viewer gets: a fan's grown-up thank you to the hero he cried for" (no "sees"). Replace "Ronaldo's own ... World Cup boots" with "gold CR7 World Cup boots Ronaldo sent him (Speed says Ronaldo wore them in the tournament; outlets disagree)".
3. **FIX. REPORT.md lines 40-41 and CANDIDATES.md #30: a comment is placed on the wrong video.**
   - "Rejected by his mother, Loved by his Father" (67,948 likes) is a comment on the 109.3M video `4PMPoZNDSn8` (`api/comments_4PMPoZNDSn8.json`), not on the 49.9M `Qq1Z14c_RyQ`.
   - REPORT lists it under the 49.9M bullet block, and CANDIDATES #30 lists both as comments on the dad join. TEARDOWN § 5 is correct.
   - Fix: write "(on the 109.3M)" after it in both files.
4. **FIX. REPORT.md line 22 ("Two reels autoplayed muted") vs the run log.** The log documents one: `DfYbDWShy4D` at 04:05. Row 05:21 (`DbBM54Cs8-V`) says muted and paused but not autoplayed. Fix: "one reel (second not logged: say which)" or log the second.
5. **FIX. The run log is missing two searches.** REPORT/README say 12 of 12 searches and the run log "has every search". `api/search_retire_nov.json` (04:05) and `api/search_shay_ronaldo.json` (04:36, empty) have no log row. The log has 10 search rows, and the empty `search_thankyou_nov.json` is the only empty one logged. Fix: add the two rows. Timestamps for several search rows are also 3-7 minutes off the file times (dadbus file 05:08, log 05:15; mom file 05:30, log 05:28), and rows 05:13/05:14/04:59 sit out of order. NIT-level, but the log is called the record.
6. **FIX. Peer medians in the log do not match `api/peers.json`.**
   - Log row 05:12: Nexxo Recaps 6.64M, SpeedShor7s 431K, Ftbl Lab 39K, Live Speedy 18.6K.
   - `peers.json`, median of the 50 newest: Nexxo 6.05M, SpeedShor7s 389K, Ftbl Lab 38.3K, Live Speedy 18.1K. deagzzzshorts 6.54M matches.
   - REPORT line 46: "deagzzzshorts and Nexxo Recaps run medians of 6.5M". Nexxo is 6.05M. Fix: "about 6M and 6.5M", and correct the log row.
7. **FIX. REPORT.md lines 46-47 (base rate) vs the predictions.**
   - "every non-MJ Short ran 12-66K" is true only for the last 20 uploads. AW's own Speed Shorts did 368K, 950K and 44K.
   - Then Lead 1's predicted centre is 70-140K and Lead 2's is 60-130K. Both sit above anything non-MJ in the window, including the best one (65.8K at 2 days), yet the text says neither lead has a new element strong enough.
   - Fix: add one sentence on why Speed leads are predicted above the non-MJ base rate (Speed's 368K/950K) or lower the centres. State which base the centre is built on.
8. **FIX. REPORT.md line 52: "Son 543K (against a 4M Short of the same picture)".** I found no 4M competitor in this folder, the run log or `research/aw-mj-pick-2026-11-13.md`. Fix: cite the source or delete the parenthesis.
9. **FIX. CANDIDATES.md #2: "Shorts on it ≤ 214K".** REPORT and the run log have `KK3tJr7byqQ` at 604K (`api/stats_thankyou_nov2.json`: 604,103). Fix: "≤ 604K".
10. **FIX. REPORT.md line 96: quote not checked against his own Short.**
    - "Ronaldo, I love you. I'm so sorry that you lost the World Cup" is from HITC via `WEB-MOMENTS.md`. The ASR of the tears Short `hMCusTW14xI` died on a memory error (`tools/asr_hMCusTW14xI.log`), and the run log says "no words caught" for the E: copy. README/DRAFT attribute it to his Short.
    - WEB-MOMENTS says "fights tears". REPORT says "cries live".
    - Fix: "(HITC's transcript of his stream; not heard in the Short)" and "fights tears".
11. **FIX. Plain words (REPORT.md top and Counts).** A non-technical creator will stall on: "locked centre", "join" (used about 20 times, "the same join", "tears → boots join"), "first-party", "the spine words are a light-model scout, not yet the medium.en pass (RAM was held by Media Encoder)", "counts lost their K/M suffix", "grid tiles", "pace.sh", "the hub merges my run log", "youtube.lock / .asr-lock", "template rule 3", "freshness FAIL", "gates".
    - Also "4 refused" is wrong: those four phrasings returned "No results" (run log), nothing was refused.
    - Fix: "a centre of 150K+" → "a Short that most likely gets 150K+ views (and could reach 1M+)"; "join" → "same story told the same way"; "first-party" → "Speed's own"; "spine words … medium.en" → "the exact words are from a quick, rough transcript, not the careful one (the computer ran out of memory)"; "refused" → "found nothing".
12. **FIX. REPORT.md Lead 1 arc and § 9: tone against Speed's own words.** "One story: the parent who showed up" frames the mother as the parent who did not. The report flags the risk (lines 86-87) but the card text still sets it up. Fix: "One story: a dad who would not miss it." Keep "his mother on a trip with his little sisters" in Speed's words only.

## NIT

13. NIT. REPORT.md line 73: "about twenty more on the bus beat, most 11-108K". `api/stats_dadbus.json` shows roughly half of them under 11K (1.4K, 1.3K, 0.8K, etc.). Say "most 1K-108K".
14. NIT. REPORT.md Lead 2 has no "Flags" line. Lead 1 flags Jamal. The run log (04:24) notes Ronaldo's kids on frame in his retirement video (not in the current Lead 2). Add "Flags: none in the planned beats; Ronaldo's kids if his retirement video is used".
15. NIT. README.md STATUS still says "Next: Fable final → independent cold read → fixes". Five advisor calls are done and this is the cold read. Update after fixes.
16. NIT. REPORT.md line 28: "Main suspects" lists four. Line 138 says "the teardown's five suspects" (H1-H5). Say "five" or list H5.
17. NIT. TEARDOWN.md H1 omits "Speed's own 748K (2026 win)" for the kick-out story in `research/aw-speed-pick-2026-11-13.md` line 155. It weakens "already worn out". Add one line.
18. NIT. CANDIDATES.md #2: "(11 days)". The 5 Nov Ronaldo video is 12 days old on 17 Nov (6 Nov is 11). Say "12 days".
19. NIT. REPORT.md opens with the verdict. The max-effort rule says the message opens with what was done. Add a one-line "what was done" (searches, reels, downloads, 5 advisor calls) before NO PICK, or accept that the Counts block does it.
20. NIT. `PITCH.md` appears only in README line 14, already marked "since renamed". Fine. No stale file references in REPORT, TEARDOWN or CANDIDATES.

Checked and clean: every date, and Speed's ages (21 Jan 2005): 15 at the 2020 kick-out, 16-17 in 2021-22, 19 at Club Shay Shay, 18 at the 2023 meeting. Jamal (16) is flagged on Lead 1 and in the candidates. The caption read of `Qq1Z14c_RyQ` matches `proof/sheet_Qq1Z14c_RyQ.jpg` ("Where's your mom?", "She's on a trip", "My little sisters", "I wish my mom would've came", "Travel 12 hours", "Dad always by his side"). The report states it is fan-edit captions, not a transcription.

**Verdict holds: yes, because** every route to the 150K bar fails on numbers that do check out: AW's non-MJ Shorts ran 12-66K, both leads' own predicted centres (60-140K) are under 150K, and Lead 1's join is a verified 49.9M. Finding 1 weakens one stated reason for Lead 2 but not the conclusion.
