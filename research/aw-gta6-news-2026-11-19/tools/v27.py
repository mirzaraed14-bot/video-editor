import sys, re
sys.stdout.reconfigure(encoding="utf-8")
base = "X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/"
p = base + "SEQUENCE.md"
s = open(p, encoding="utf-8").read()
miss = []
def rep(a, b):
    global s
    if a not in s: miss.append(a[:70]); return
    s = s.replace(a, b)
i1 = s.index("v2 applies the cold read")
s = """# AW GTA 6 news Short: "Bigfoot Is In GTA 6 😳" (sequence v2.7, 20 Nov 2026; nothing built)

> **NOW ABOVE THE 150K BAR.** Re-locked on 20 Nov 19:30 numbers: Bigfoot **180K** (50 % range 60K-550K, about 55 % to clear 150K). The jet: 80K.
> - **Why it moved since v2.6** (110K, below the bar): Bigfoot is now proven on YouTube Shorts.
>   - Its lane is at 502K/h, with 19 videos at 100K+.
>   - Marcade's Bigfoot Short is at 4.42M.
>   - Streamer reactions are real hits: the CaseOh fan Short is at 1.32M, Kai Cenat's at 331K, and jacksepticeye's "WAS THAT BIGFOOT??" at 929K.
> - **The "below the bar" exception is gone.**
> - **The cut is unchanged since v2.6**, including the correction that the big figures are effigies and Bigfoot itself is its legs over the player.

""" + s[i1:]
rep("v2.6 re-locks on the 20 Nov 04:30 numbers", "v2.7 (20 Nov ~19:45) re-locks on the 19:30 numbers (`UPDATE-2026-11-20-1930.md`); numbers only, the cut is unchanged; v2.6 is kept as `SEQUENCE.v2.6.md`. v2.6 re-locks on the 20 Nov 04:30 numbers")
rep("  - On v2.6 (20 Nov about 04:39):", "  - **No Fable call on v2.7:** numbers only, the cut is unchanged since Fable call 5 (the hub's ruling; weekly usage past 84 %).\n  - On v2.6 (20 Nov about 04:39):")
rep("- **I pick Bigfoot.** As of v2.6 it is fit, and modestly forecast too: § 4 centres it at 110K against the jet's 85K, inside each other's ranges.",
    "- **I pick Bigfoot.** As of v2.7 it is fit AND forecast: § 4 centres it at 180K against the jet's 80K.")
rep("- **The cost:** a 543K fan Short (CaseOh, title only, not checked) may already hold the \"streamer finds Bigfoot\" angle on YouTube. Most single-streamer Bigfoot Shorts sit at 37K-70K.",
    "- **The cost:** a 1.32M fan Short (CaseOh, title only, not viewed) may already hold the \"streamer finds Bigfoot\" angle on YouTube.")
rep("- Below the 150K bar: 110K centre, about 43 % to clear (the exception is named first).\n- A 543K fan Short may already hold the \"streamer finds Bigfoot\" angle (G4 entry tax; not checked).",
    "- The CaseOh fan Short (1.32M, not viewed) may already hold the \"streamer finds Bigfoot\" angle (G4 entry tax).")
rep("2. Build Bigfoot under the exception (§ 4: 110K, below the 150K bar, about 43 % to clear), or hold for something above the bar?",
    "2. Build Bigfoot now? (§ 4: 180K, above the 150K bar, about 55 % to clear.)")
s = re.sub(r"\| G4 Freshness \| \*\*PARTLY PROVEN, with an entry tax\*\* \|[^\n]*\n",
 "| G4 Freshness | **PROVEN, with a heavy entry tax** | The streamer + Bigfoot join now works on YouTube (API, 20 Nov 19:30): CaseOh fan Short **1.32M** (title only, not viewed), Kai Cenat fan Short **331K**, jacksepticeye \"WAS THAT BIGFOOT??\" 929K (long-form, not checked on frame), FoltynGaming \"I KILLED BIGFOOT\" 367K. The topic itself: Marcade's Bigfoot Short at **4.42M**. Entry tax: the CaseOh 1.32M Short is the same angle. Ours differs: 4 streamers, the black-out with Bigfoot's legs, and the game's reversal. The 19 Nov multi-streamer compilations (Dropy 1,930 etc.) were not re-read. No AW Short on it |\n", s, count=1)
i0 = s.index("## 4. Locked predictions"); i5 = s.index("## 5. Variants compared")
s = s[:i0] + """## 4. Locked predictions, side by side (re-locked 20 Nov ~19:45 on the hub's word, from the 19:30 numbers; v2.7)
**The rule (unchanged):** start from AW's newest-30 median, 93.5K (API, 19 Nov 20:30; not re-read). Move a moment off it only for a factor measured since, and apply each row to both moments. Sources: `api/t3/`, `api/watcher-moments-now.txt`, `UPDATE-2026-11-20-1930.md`.

| Factor (measured 20 Nov 19:07-19:35) | Bigfoot | Jet theft | Effect on the centre |
|---|---|---|---|
| Topic heat on Shorts | **Marcade's Bigfoot Short 4.42M**; lane 204K → **502K/h**; 100K+ videos 10 → **19** | Shorts slowing: Typical Gamer 3.74M (about 28K/h since 04:30), Aaron Rheins 1.81M; lane 639K/h, mostly TmarTn2's long-form (6.73M) | Bigfoot ++; jet + (lane), − (its Shorts are slowing) |
| The streamer-compilation join | **works:** CaseOh fan Short 1.32M, Kai Cenat fan Short 331K, jacksepticeye 929K | still low (best 20K on 19 Nov; not re-read) | Bigfoot ++; jet − |
| Entry tax (same beat and angle) | the CaseOh 1.32M Short (title only, not viewed) | Typical Gamer's own 3.74M Short of the same footage | both −; the jet's is certain |
| Instagram top reel (~04:35 → ~19:35) | 15.8M → 16.5M (+0.7M) | 16.5M → 16.9M (+0.4M) | about even |
| Big faces with the encounter on frame | 4 (Kai Cenat, xQc, summit1g, Fanum) | 2 confirmed | Bigfoot + (a bet) |

| | v2.6 (20 Nov ~05:20) | **v2.7 (20 Nov ~19:45)** |
|---|---|---|
| Bigfoot, most likely | 110K | **180K** |
| Bigfoot, 50 % range | 40K-350K | **60K-550K** |
| Bigfoot, 1M+ | about 12 % | **about 18 %** |
| Bigfoot, under 10K | about 7 % | **about 5 %** |
| Bigfoot, clears 150K | about 43 % | **about 55 %** |
| Jet, most likely | 85K (30K-280K) | **80K (25K-260K)**: its Shorts are slowing and its join is still low |

**Why 180K and not higher:**
- The comparables now run to 1.32M and 4.42M, but they are single uploads.
- The CaseOh Short is an unviewed same-angle entry tax.
- Ours posts on day 3 or later, when the feed may have moved on.
- AW's own GTA 5 farewell, its best GTA Short, is at 366K after 51 h.

**The bar: ABOVE the 150K bar** (180K centre, about 55 % to clear). **The exception line is retired.** The jet stays below (80K).
- **5K pre-mortem:** it posts after the moment peaks, and the feed treats it as another re-up of the CaseOh and Kai fan Shorts.
- **5M pre-mortem:** four of the biggest streamers, Bigfoot's legs over them, and the game's own "Nope. Skunk ape" become the version people share, riding the same wave as the 4.42M Short.

""" + s[i5:]
s = re.sub(r"- \*\*Six stars: the next news candidate, noted only\.\*\*[^\n]*\n",
 "- **Six stars: the next candidate, not started.** It has cooled since 04:00 (537K → 347K/h), though MrBeast Gaming's Short is at 1.43M. Kai Cenat's six-star HUD is not checked on frame.\n", s, count=1)
open(p, "w", encoding="utf-8").write(s)
print("missing:", miss)
