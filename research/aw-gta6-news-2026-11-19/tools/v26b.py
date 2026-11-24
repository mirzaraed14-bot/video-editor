import sys, re
sys.stdout.reconfigure(encoding="utf-8")
base = "X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/"
p = base + "SEQUENCE.md"
s = open(p, encoding="utf-8").read()
# top block
s = s.replace("> - The prediction is re-locked from 90K to **150K: AT the 150K bar**, about a coin flip to clear it. The jet stays below, at 90K.",
 "> - The prediction is re-locked from 90K to **110K: still BELOW the 150K bar**, though closer, with about 40 % to clear it. The jet moves from 90K to 85K.\n> - The exception stays named: you asked for this Short; launch week is a one-time window; the upside tail.")
s = s.replace("> - One correction: the glowing night figure in beat 5 is the quest's effigy (\"Inspect the tree\"), not the live creature.",
 "> - One correction: the glowing night figure (beats 5-6) is the quest's effigy (\"Inspect the tree\"), not the live creature.")
s = s.replace("## 3. The sequence (33.1 s)", "## 3. The sequence (33.5 s)")
lines = s.split("\n"); out = []
for ln in lines:
    if ln.startswith("| 6 | 0:20.9-0:24.5 |"):
        ln = ("| 6 | 0:20.9-0:24.9 | **NEW in v2.6, replaces xQc's \"Run! We're the prey!\" dark-shape beat.** `kai-bigfoothunting-4096145023.mp4` (Kai Cenat's own clip \"bigfoot hunting\", twitch.tv/kaicenat/clip/TrappedSpinelessDugongLitty-k4LDRLXugP8d5cQd, 7 views, created 19 Nov 14:16 PKT, 1920x1080 60), **in-file 54.6-58.6** "
              "| **The effigy close-up fills the frame:** the glowing figure by the tree, with the game's \"The hell is this?\" and the prompt \"Inspect the tree\". Kai's cam shows him alone; he ends with his hand over his mouth "
              "| \"oh my gosh bro\" (55.02-58.46, Kai, ASR) "
              "| **Kai Cenat** · `KAI CENAT · TWITCH` on his cam "
              "| PROVEN: his own clip (`frames/kai-beat-effigy.jpg`, `-cam.jpg`). The same quest is re-upped as \"Kai Cenat Found Bigfoot In GTA 6!\" on YouTube: 139K, about 13.5K/h since upload |")
    elif ln.startswith("| 7 BUTTON | 0:24.5-0:33.1 |"):
        ln = ln.replace("| 7 BUTTON | 0:24.5-0:33.1 |", "| 7 BUTTON | 0:24.9-0:33.5 |")
    out.append(ln)
s = "\n".join(out)
# effigy wording leftovers
s = s.replace("It is the same quest and the same creature Kirk calls \"Mister Mangrove\" (the creature is on frame next to Kirk in beat 5), not the daylight knock-out in beats 1-4.",
 "It is the same quest Kirk calls \"Mister Mangrove\" (the quest's effigy is on frame next to Kirk in beat 5), not the daylight knock-out in beats 1-4.")
s = s.replace("The two are linked by the creature on frame, not by any game text (Afterhours hunt-eggs R3-1f).",
 "The two are linked by the figure's look (the same tree-bodied design in daylight and as the night effigy), not by any game text (Afterhours hunt-eggs R3-1f).")
s = s.replace("beside the same glowing creature", "beside the same glowing figure (the effigy)")
s = s.replace("the shot shows a glowing skunk-like animal in the grass.", "the shot shows a glowing skunk-like animal in the grass (an animal in the night quest; not the figure).")
s = s.replace("and hunted xQc's and Kai Cenat's at night;", "and at night xQc's and Kai Cenat's characters met its effigy and were chased;")
s = s.replace("- **Night:** the glowing figure by the tree (beat 5, and the end of Kai's clip)", "- **Night:** the glowing figure by the tree (beats 5 and 6)")
# Fable reactor condition line
s = s.replace("Since v2.6 Kai Cenat is in the cut (beat 6), so it is 4.",
 "Since v2.6 Kai Cenat is in the cut (beat 6: cam, the effigy and his reaction in one window), so it is 4 under \"the encounter's figure on frame\". Under \"the live creature on frame\", only the daylight figure counts (summit1g, Fanum), and even that is not shown moving.")
s = s.replace("| **Kai Cenat** (own Twitch clip, v2.6), **xQc, summit1g, Fanum**", "| **Kai Cenat** (own Twitch clip, the night effigy), **xQc** (the night effigy), **summit1g, Fanum** (the daylight figure)")
# G2
s = re.sub(r"\| G2 What's on screen \| PASS \|[^\n]*\n",
 "| G2 What's on screen | PASS | the daylight figure on frame in beats 1-2 and its legs in beat 4; the night effigy in beats 5-6 (\"Inspect the tree\"). The live night creature is never clearly on frame, and is not used |\n", s, count=1)
# G4
s = re.sub(r"\| G4 Freshness \| \*\*PROVEN, with an entry tax\*\* \|[^\n]*\n",
 "| G4 Freshness | **PARTLY PROVEN, with an entry tax** | v2.5's \"tried and stayed low\" is out of date: **2 of about 10** streamer + Bigfoot Shorts broke out overnight. The Kai Cenat fan Short (139K; his quest moment is verified on his own clip). The CaseOh fan Short (543K; title only: **not checked** that it shows this creature, and CaseOh's own \"Bigfoot\" Twitch clip is a mission dialogue). The rest stay low: Keoxer 69.5K, Swagg 47.8K, Poggers 39.6K, Barış 36.7K, same-day compilations about 1-2K. If the 543K Short is the same angle, it is the entry tax. Ours differs: 4 streamers, the black-out, the game's reversal. No AW Short on it |\n", s, count=1)
s = s.replace("- A 543K fan Short has already taken the \"streamer finds Bigfoot\" angle (G4 entry tax).",
 "- Below the 150K bar: 110K centre, about 40 % to clear (the exception is named first).\n- A 543K fan Short may already hold the \"streamer finds Bigfoot\" angle (G4 entry tax; not checked).")
s = s.replace("- At the 150K bar, not above it (150K centre, about 50 % to clear).\n", "")
s = s.replace("- **I pick Bigfoot.** As of v2.6 it is fit AND forecast: § 4 centres it at 150K against the jet's 90K.",
 "- **I pick Bigfoot.** As of v2.6 it is fit, and modestly forecast too: § 4 centres it at 110K against the jet's 85K, inside each other's ranges.")
s = s.replace("- **The cost:** a 543K fan Short (CaseOh) already holds the \"streamer finds Bigfoot\" angle on YouTube. Ours has to read as the bigger version: 4 streamers plus the game's reversal.",
 "- **The cost:** a 543K fan Short (CaseOh, title only, not checked) may already hold the \"streamer finds Bigfoot\" angle on YouTube. Most single-streamer Bigfoot Shorts sit at 37K-70K.")
s = s.replace("2. Build Bigfoot now (§ 4: 150K, at the bar), or hold for something above it?",
 "2. Build Bigfoot under the exception (§ 4: 110K, below the 150K bar, about 40 % to clear), or hold for something above the bar?")
# section 4 rewrite
i0 = s.index("## 4. Locked predictions"); i5 = s.index("## 5. Variants compared")
s = s[:i0] + """## 4. Locked predictions, side by side (re-locked 20 Nov ~05:20 on the hub's word, from the 04:30 numbers; cold read 4 applied)
**The rule (unchanged):** start from AW's live newest-30 median, 93.5K. Move a moment off it only for a factor measured today, and apply each row to both moments.

| Factor (measured) | Bigfoot | Jet theft | Effect on the centre |
|---|---|---|---|
| The streamer-compilation join (API; 19:22 vs 04:30) | **2 of about 10 broke out:** Kai Cenat fan Short 139K, verified moment; CaseOh fan Short 543K, title only, unchecked. The rest: Keoxer 69.5K, Swagg 47.8K, Poggers 39.6K, Barış 36.7K, compilations about 1-2K. **Median of the 6 single-streamer Shorts ≈ 59K** | still low: best 20K, the rest near 0 | Bigfoot + (small); jet − (small) |
| YouTube lane (watcher interval speed, 19:07 → 04:07) | 124K/h → 204K/h, rising; 100K+ videos 5 → 10 | 718K/h → 602K/h, cooling, but still about 3x Bigfoot's; 100K+ 21 → 27 | jet +; Bigfoot + (rising) |
| Instagram top reel (~19:40 → ~04:35) | 13.7M → 15.8M (≈ 240K/h); shares +31.4K | 15.5M → 16.5M (≈ 115K/h); shares +2.5K | Bigfoot +; jet − |
| Entry tax (prior 100K+ Shorts of the same beat and angle) | the 543K CaseOh Short, if it shows this creature (unchecked) | Typical Gamer's own 3.32M Short of the same footage our cut would use | jet −− (certain, same footage); Bigfoot − (possible) |
| Big faces with the encounter on frame | 4 (Kai Cenat, xQc: night effigy; summit1g, Fanum: daylight figure) | 2 | Bigfoot + (a bet, not measured) |

**Net:** Bigfoot moves modestly up from the median. The jet moves slightly down: its lane lead is offset by a certain same-footage entry tax and a join still at 0-20K.

| | v2.5 (19 Nov 20:52) | **v2.6 (20 Nov ~05:20)** |
|---|---|---|
| Bigfoot, most likely | 90K | **110K** |
| Bigfoot, 50 % range | 30K-300K | **40K-350K** |
| Bigfoot, 1M+ | about 10 % | **about 12 %** |
| Bigfoot, under 10K | about 10 % | **about 7 %** |
| Bigfoot, clears 150K | about 40 % | **about 40 %** |
| Jet, most likely | 90K (30K-300K) | **85K (30K-280K)** |

**Why not higher:** the median single-streamer Bigfoot Short is about 59K. Only the 543K Short supports a higher centre, and it is one upload, title only.

**The bar:** **still BELOW the 150K bar** (110K centre, about 40 % to clear); the jet is further below (85K). **Held strictly, still no pick.** The exception, named first: you asked for this Short today; launch week is a one-time window; the upside tail (about 12 % for 1M+).
- **5K pre-mortem:** it posts after the Kai and CaseOh fan Shorts have taken the feed's \"streamer finds Bigfoot\" slot, and it reads as a re-up.
- **5M pre-mortem:** four of the biggest streamers in one Short, plus the game's own \"Nope. Skunk ape\", becomes the version people share.

""" + s[i5:]
# section 13 additions
s = s.replace("- **Kai's frames** (`frames/kai-1080-sheet.jpg`, `frames/kai-4up.jpg`), checked against the hub's four conditions:",
 "- **Kai's frames** (`frames/kai-1080-sheet.jpg`, `frames/kai-4up.jpg`, beat window `frames/kai-beat-effigy.jpg` and `-cam.jpg`), checked against the hub's four conditions:")
s = s.replace("  - creature on frame: only the \"Chase Mr. Mangrove\" objective in beat 6, and the effigy at 50-58 s;",
 "  - creature on frame: the night effigy fills the frame in the beat window (54.6-58.6), with his reaction in the same window;")
s = s.replace("  - minors: none on frame.",
 "  - minors: none on frame. A second person (an adult by size) stands behind Kai in his cam at about 12-17 s, outside our window; at 54.6-58.6 he is alone.")
s += "- **Cold read 4** (`COLD-READ-4.md`, 9 items) applied:\n  - the re-lock moves from 150K to 110K, with every row applied to both moments and the comparables' median shown;\n  - the CaseOh 543K is marked title-only;\n  - Kai's beat moved to his effigy window, which also removes the clipped last word;\n  - the effigy wording made consistent;\n  - Kai's Short rate corrected (about 13.5K/h average since upload; the watcher's last interval read 26K/h);\n  - the second person in Kai's cam is noted.\n"
open(p, "w", encoding="utf-8").write(s)
print("ok")
