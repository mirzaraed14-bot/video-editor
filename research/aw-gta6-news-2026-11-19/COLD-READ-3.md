# Cold read 3 of SEQUENCE.md v2.4 (short pass, files only)

Checked against: api/rank-all.txt, api/aw-recent.json (recomputed), api/watcher-moments-1907.txt, ig/IG-PASS-1.md, ig/IG-PASS-2-streamers.md, audio/*.txt, twitch/. The anchor_compare.jpg and kai-thumbs were not opened (time). Beat arithmetic (durations sum to 32.3 s; pull-timeline and VOD clock conversions) checks out. 93.5K newest-30 median reproduces exactly from aw-recent.json; the GTA 5 farewell is 298,365 views. The 6.6x, 440K/h, 325K/h, 1.35x, 10x, 229K and 201K figures all recompute.

## Findings, most serious first

1. **First line contradicts § 4 on the GTA 5 farewell.**
   - Line 8 uses "Saying Goodbye To GTA 5 ... 298K in 28 h" as the exception's second reason ("GTA content is doing well on AW right now").
   - Line 128 says it "does not calibrate this format, so it moves neither centre", and it is "another session's story Short".
   - It is also the newest of the 30 videos in the 93.5K median, and it is n = 1.
   - The exception rests on a datum the sequence itself disowns.
   - Fix: delete the bullet, or restate it as "one GTA Short did 298K, which is not evidence for a reaction compilation".

2. **§ 4 "one rule" is applied unevenly in the entry-tax row (line 122).**
   - For Bigfoot, three prior 100K+ Shorts (113-153K) count as a plus.
   - For the jet, a prior 2.35M Short of the same clip is not credited. It is silently treated as saturation (the jet's 5K pre-mortem calls it a "re-upload").
   - The same kind of fact is scored opposite ways, and the net "Bigfoot +" depends on it.
   - Of those three, only the CaseOh fan clip and LazarLazar's Short are anywhere near the pick's format; none is a streamer compilation (§ 1 says the join stayed low).
   - Fix: score the row "even" (prior hits show the moment travels, and also mean the feed has seen it), or name the opposing sign for each side.

3. **Identical 10 % under-10K for Bigfoot is hard to square with line 62.**
   - rank-all.txt shows the same-day streamer-titled Bigfoot Shorts at about 100-2K views (Dropy, Komnt, TurkishProduction, GTA Updates) and the other non-hit Bigfoot Shorts at 20-40K (Ross, Bedirianis, BrenaX, ClipsTycoon, Siidv2). Only 3 clear 100K.
   - The jet has the same percentages with a 11 % vs 2 % topic-heat gap.
   - The tail rows (50 % range 30-300K, 1M+ 10 %, under 10K 10 %) are copied across both columns rather than derived. Under a lognormal centred at 90K they are internally consistent, but P(over the 150K bar) is about 38 % and is never stated.
   - Fix: state P(at or over 150K) once, and say the tail rows are the channel's own spread, not a per-moment estimate.

4. **§ 6 line 163 (weakest-first list): "Instagram was not searched per streamer."**
   - This is a leftover. Pass 2 (ig/IG-PASS-2-streamers.md) searched per streamer, and § 0 and the IG row (lines 29, 170-176) say so.
   - Fix: replace with "Per-streamer Instagram search found no streamer Bigfoot reel (pass 2, likes only, no shares or views read)".

5. **§ 0 line 37 "Fable advisor: 3 calls", then four are listed.** Before-lock 19:28, 19:44, final about 20:07, v2.3 about 20:44. That is 4 (or 3 if the two before-lock calls count as one). Fix: say "4 calls" or "3 sessions".

6. **Fable's condition of at least 4 reactors mid-clip now fails in the cut as built (line 41).**
   - Line 41 says the condition "held at 4 once Kai was confirmed", but Kai is out of the cut (Q5, line 52).
   - In the cut it is 3 with cams (xQc, summit1g, Fanum) plus Brendaniel, who has no cam and whose clip is not checked to be this moment (line 101 admits it).
   - Fix: add "In the cut as pitched: 3 held, Brendaniel's beat voice-only; the 4th depends on Q5."

7. **Line 18 "77 clips since 18 Nov".** twitch/kai-7d.json holds 98 entries and kai-all.json 20. The 77 cannot be reproduced from the file without the date filter. Fix: state "98 in the 7-day list, 77 dated 18 Nov or later", or cite the file.

8. **G4 numbers have no source file named.**
   - "Dropy 1.9K, Komnt 1.5K, TurkishProduction 1.2K, GTA Updates 0.9K" are views.
   - rank-all.txt shows those channels at 0.1-0.2K views/h and 0.00M (rounded) views, so the figures are plausible but not verifiable from the printed columns.
   - The sentence "5 Kai re-ups on Instagram at 0-33 likes" is supported by pass 2 (4 opened, plus the 5-like re-up in pass 1).
   - Fix: add a views column to rank-all.txt or cite the `videos` JSON ids.

9. **Line 50 "now 226K shares on 6.5K followers"** is correct from IG-PASS-1 (226.1K, 6,519). But line 169 reports "spectrexgaming 38.3K likes" as a #gta6bigfoot top result, and pass 1 marks it "not re-read" and "earlier". Fix: add "(earlier read)".

10. **§ 4 first line vs table.** The first line says both centre at about 90K; the table nets 2 jet-plus vs 2 Bigfoot-plus with one even row. That is honest. But § 1 line 58 says "§ 4 centres both at about 90K" while line 49 says the jet wins the metric about 6.6x, which sits next to a 90K centre for Bigfoot. This is acceptable only because item 2 above is cleaned up.

## Not found (checked, clean)
- No leftover 120K or 50K prediction (line 116 mentions v2.3's 120K only as the replaced value).
- No stacked split described as current (lines 77, 153 are "no split" or "cut").
- No "nobody has the angle".
- No lips-captions (line 79 explicitly says they cannot apply).
- G4 reads WEAK in line 180, consistent with line 158 and line 61.
- Kai is excluded from the cut everywhere except the Instagram re-up evidence and Q5.
