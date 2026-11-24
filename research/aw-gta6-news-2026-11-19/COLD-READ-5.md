# Cold read 5 of SEQUENCE.md v2.7 (changed sections only)

Checked against `UPDATE-2026-11-20-1930.md`, `api/t3/tracked.json`, `api/watcher-moments-now.txt`, `api/t2/tracked.json`. Read-only; no web, no media.

**Numbers that check out:** Marcade 4.42M, lane 502K/h, 19 at 100K+, CaseOh 1.32M (+774K), Kai 331K, jacksepticeye 929K, Foltyn 367K, Typical Gamer 3.74M (about 28K/h since 04:30), Aaron Rheins 1.81M, TmarTn2 6.73M, jet lane 639K/h, six stars 537K to 347K/h, MrBeast Gaming 1.43M, AW farewell 366K at about 51 h, Instagram 15.8M to 16.5M and 16.5M to 16.9M. The "about 55 %" matches a lognormal fitted to the stated 50 % range (60K-550K): P(over 150K) is about 54 %.

## 1. Leftover v2.6 facts outside any history label (contradict v2.7)
- **Line 17 (§ 0, "NOT max effort yet" item 3):** "The 543K CaseOh fan Short was not viewed". It is 1.32M now (evidence: t3 tracked, 1,317,002; § 6 and line 174 already say 1.32M). Fix: change to "The 1.32M CaseOh fan Short".
- **Line 104 (beat 5 source cell):** Kai's YouTube re-up "139K, about 13.5K/h". It is 331K now (t3, 330,587; 139K was the 04:30 reading, t2). Fix: "331K at 19:30 (139K at 04:30)".
- **Line 224 (§ 9 jet runner-up):** "TmarTn2 3.71M, Typical Gamer 3.32M, Aaron Rheins 1.46M; Instagram 16.5M ... lane is cooling (718K -> 602K/h)". All 04:30 or older. At 19:30 it is 6.73M, 3.74M, 1.81M, 16.9M, and the lane is flat or slightly up (602K -> 639K/h), not cooling. Fix: replace with the 19:30 figures and drop "cooling".
- **§ 1 table and bullets (lines 48-60):** labelled a 19 Nov snapshot, which is fair, but the bullet "the jet wins about 6.6x" and "By the brief's literal metric, the jet is the hottest" sit right above "As of v2.7 ... forecast" and now disagree with it (Bigfoot's best Short, 4.42M, beats every jet Short; lanes 502K vs 639K/h). Fix: add one line "At 19:30 the gap is about 1.3x on the lane and Bigfoot has the best Short" or mark the bullets as 19 Nov history.
- The "110K / below the bar / exception / 543K" strings that remain are only in labelled history (line 4 "since v2.6", the v2.6 column on line 139, § 13 on lines 250-270). That is fine.

## 2. The re-lock is not applied evenly to the jet
- **Line 134 (jet join cell):** "still low (best 20K on 19 Nov; not re-read)" sits in a table headed "Factor (measured 20 Nov 19:07-19:35)", and the rule says to move only "for a factor measured since". It is a stale reading used as a measured factor, and it is the only "-" in the jet column that is not today's. The jet is still moved down (85K -> 80K) partly on it. Fix: either re-read it or mark the cell "not measured, no effect" and move the jet only on today's rows (lane up, Shorts slowing, same-footage tax unchanged), which would hold it at about 85K.
- **Lines 132-133, 145-146 (asymmetry):** Bigfoot gets "++" from a single 4.42M upload (Marcade, not a streamer join), while § 4 then discounts comparables as "single uploads". The jet's own comparables (3.74M, 1.81M) get only "+ (lane)" and the Instagram row is "about even" although the jet's reel is the larger one (16.9M vs 16.5M). The two moments are not on one rule. Fix: give the jet's 3.74M and 1.81M Shorts the same "topic heat" credit, or cap Bigfoot's "++" to what the streamer-join rows (CaseOh, Kai) alone support; then say which comparables move which centre.
- **Line 132 (jet lane cell):** "639K/h, mostly TmarTn2's long-form (6.73M)". TmarTn2 is 217K/h of 639K (watcher line 3), about a third. Fix: "led by TmarTn2's long-form (217K/h of 639K)".

## 3. Bar line vs table: consistent, with two caveats
- "ABOVE the 150K bar (180K centre, about 55 % to clear)" matches the table (180K centre, 55 % row, 150K threshold). It is evenly worded for the jet ("stays below, 80K").
- The tail rows run fatter than the stated range implies, in the same direction in both versions. A lognormal through 60K-550K gives about 15 % for 1M+ and about 4 % under 10K (the table says 18 % and 5 %). v2.6's rows had the same lean (12 % vs about 8.5 %), so it is consistent, but say "fat-tailed, by judgment" once. Low priority.
- Line 150's "AW's own GTA 5 farewell ... 366K after 51 h" is right. Minor: line 196 cites "Dropy 1,930", while t2 (04:30) reads 2,090. Say "about 2K".

## One-sentence summary
The numbers in the changed sections are right; fix the three stale v2.6 leftovers (lines 17, 104, 224), and re-apply the 80K jet move on today's rows only so both centres follow the same rule.
