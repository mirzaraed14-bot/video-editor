import sys, re
sys.stdout.reconfigure(encoding="utf-8")
p = "X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/SEQUENCE.md"
s = open(p, encoding="utf-8").read()
miss = []
def rep(a, b):
    global s
    if a not in s: miss.append(a[:70]); return
    s = s.replace(a, b)
rep("about 55 % to clear 150K). The jet: 80K.", "about 55 % to clear 150K). The jet: 85K, unchanged.")
rep("The 543K CaseOh fan Short was not viewed", "The 1.32M CaseOh fan Short was not viewed")
rep("on YouTube: 139K, about 13.5K/h since upload |", "on YouTube: 331K at 19:30 on 20 Nov (139K at 04:30) |")
rep("against the jet's 80K.", "against the jet's 85K.")
rep("The jet stays below (80K).", "The jet stays below (85K).")
s = re.sub(r"- \*\*Jet theft from the military base, fighter jets chasing:\*\*[^\n]*\n",
 "- **Jet theft from the military base, fighter jets chasing:** still big at 20 Nov 19:30. TmarTn2 6.73M, Typical Gamer 3.74M (its growth slowing to about 28K/h), Aaron Rheins 1.81M; Instagram 16.9M; the lane is flat at 639K/h (602K/h at 04:00). 2 streamers confirmed on frame (Typical Gamer, ohnePixel); Fanum's and Agent00's jet clips are in the 04:30 list, not checked. Its clips are on disk; no sequence is written for it.\n", s, count=1)
rep("**The bar, said plainly:**", "**At 20 Nov 19:30** the gap has closed: the lanes are 502K/h (Bigfoot) against 639K/h (jet), about 1.3x, and Bigfoot has the single best Short (4.42M). The bullets below are the 19 Nov history.\n\n**The bar, said plainly (19 Nov):**")
rep("| Topic heat on Shorts | **Marcade's Bigfoot Short 4.42M**; lane 204K → **502K/h**; 100K+ videos 10 → **19** | Shorts slowing: Typical Gamer 3.74M (about 28K/h since 04:30), Aaron Rheins 1.81M; lane 639K/h, mostly TmarTn2's long-form (6.73M) | Bigfoot ++; jet + (lane), − (its Shorts are slowing) |",
    "| Topic heat on Shorts | Marcade's Bigfoot Short 4.42M; lane 204K → 502K/h; 100K+ videos 10 → 19 | Typical Gamer 3.74M and Aaron Rheins 1.81M, both slowing (Typical Gamer about 28K/h since 04:30); lane 639K/h, led by TmarTn2's long-form (217K/h of it) | Bigfoot + (rising); jet + (bigger lane and Shorts), − (slowing) |")
rep("| still low (best 20K on 19 Nov; not re-read) | Bigfoot ++; jet − |", "| not re-measured since 19 Nov (best was 20K) | Bigfoot ++; **jet: no effect** (not measured today) |")
rep("| 15.8M → 16.5M (+0.7M) | 16.5M → 16.9M (+0.4M) | about even |", "| 15.8M → 16.5M (+0.7M) | 16.5M → 16.9M (+0.4M) | even: the jet's reel is larger, Bigfoot's grows faster |")
rep("| Jet, most likely | 85K (30K-280K) | **80K (25K-260K)**: its Shorts are slowing and its join is still low |",
    "| Jet, most likely | 85K (30K-280K) | **85K (30K-280K), unchanged:** its bigger lane is offset by slowing Shorts and the certain same-footage tax |")
rep("| Bigfoot, under 10K | about 7 % | **about 5 %** |", "| Bigfoot, under 10K | about 7 % | **about 5 %** (the tails are fat by judgment; a lognormal through 60K-550K gives about 15 % and 4 %) |")
rep("Dropy 1,930 etc.", "Dropy about 2K etc.")
s += "- **Cold read 5** (`COLD-READ-5.md`) applied to v2.7:\n  - stale v2.6 figures updated (CaseOh 1.32M, Kai 331K, the jet runner-up line);\n  - § 1 marked as 19 Nov history;\n  - the jet held at 85K: no move on an unmeasured factor, and its comparables get the same topic credit;\n  - TmarTn2 \"led by\", not \"mostly\";\n  - the tails labelled as judgment;\n  - Dropy \"about 2K\".\n"
open(p, "w", encoding="utf-8").write(s)
print("missing:", miss)
