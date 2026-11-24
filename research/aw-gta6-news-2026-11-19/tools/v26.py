import sys, re
sys.stdout.reconfigure(encoding="utf-8")
base = "X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/"
p = base + "SEQUENCE.md"
s = open(p, encoding="utf-8").read()

# ---- top block
i1 = s.index("v2 applies the cold read")
TOP = """# AW GTA 6 news Short: "Bigfoot Is In GTA 6 😳" (sequence v2.6, 20 Nov 2026; nothing built)

> **What changed since v2.5 (re-check at 04:20-05:10, 20 Nov):**
> - The streamer + Bigfoot Shorts broke out on YouTube overnight.
> - Kai Cenat is now in the cut, from his own Twitch clip.
> - The prediction is re-locked from 90K to **150K: AT the 150K bar**, about a coin flip to clear it. The jet stays below, at 90K.
> - One correction: the glowing night figure in beat 5 is the quest's effigy ("Inspect the tree"), not the live creature.

"""
s = TOP + s[i1:]

# ---- version note
s = s.replace("v2.5 applies cold read 3 (`COLD-READ-3.md`, 10 items).",
 "v2.5 applies cold read 3 (`COLD-READ-3.md`, 10 items). v2.6 re-locks on the 20 Nov 04:30 numbers (`UPDATE-2026-11-20-0430.md`), adds Kai Cenat, and fixes the effigy reading. v2.5 is kept as `SEQUENCE.v2.5.md`.")

# ---- NOT max effort: Kai item
s = re.sub(r"3\. \*\*Kai Cenat is not placed in his stream\.\*\*.*?\n",
 "3. **Kai Cenat's clip read at 1080p on frames and ASR only** (his own Twitch clip, see beat 6). His words, like everyone's, are not heard by ear.\n", s, count=1)

# ---- section 3 heading + cover list
s = s.replace("## 3. The sequence (32.3 s)", "## 3. The sequence (33.1 s)")
s = s.replace("- **xQc:** nothing to cover.",
 "- **xQc:** nothing to cover.\n- **Kai Cenat:** the chat panel under his cam (left, about x 0-400, y 650-800 of 1920x1080) and the two counters on the right (about x 1730-1920, y 520-600). Cover both with plates; his cam stays (about x 0-392, y 432-652).")

# ---- beat rows 5, 6, 7
lines = s.split("\n")
out = []
for ln in lines:
    if ln.startswith("| 5 | 0:16.8-0:20.9 |"):
        ln = ("| 5 | 0:16.8-0:20.9 | `xqc-chase-1370-1500.mp4` (**in-file 49.5-53.6 s**; = pull-timeline 1419.5-1423.6) = xQc launch VOD 2932113307, ≈ VOD 15:01:09-15:01:13 "
              "| Night. **The quest's effigy:** a glowing figure of the creature by a tree (Kai's clip shows the game's prompt \"Inspect the tree\" at the same object). Beside it stands a red-hooded man, Kirk "
              "| \"I'm not hunting him.\" / \"He's hunting me!\" (subtitles) "
              "| Kirk (GTA 6), italic; label `KIRK · THE DRONE OPERATOR (GTA 6)` (the game's map card calls him that; the label is OURS) · `XQC · TWITCH` (inset) "
              "| PROVEN (subtitles + the effigy on frame) |")
    elif ln.startswith("| 6 | 0:20.9-0:23.7 |"):
        ln = ("| 6 | 0:20.9-0:24.5 | **NEW in v2.6, replaces xQc's \"Run! We're the prey!\" dark-shape beat.** `kai-bigfoothunting-4096145023.mp4` (Kai Cenat's own clip \"bigfoot hunting\", twitch.tv/kaicenat/clip/TrappedSpinelessDugongLitty-k4LDRLXugP8d5cQd, 7 views, created 19 Nov 14:16 PKT, 1920x1080 60) in-file 22.2-25.8 "
              "| Night swamp, flashlight. The game's objective on screen: **\"Chase Mr. Mangrove\"**. Kai's cam shows his reaction. The creature itself is not clearly visible in this window "
              "| \"Oh my god!\" (22.44-23.48) … \"OH MY GOD!\" (25.54-25.84) (ASR) "
              "| **Kai Cenat** · `KAI CENAT · TWITCH` on his cam "
              "| PROVEN: his own clip; the moment is also re-upped as \"Kai Cenat Found Bigfoot In GTA 6!\" (139K on YouTube) |")
    elif ln.startswith("| 7 BUTTON | 0:23.7-0:32.3 |"):
        ln = ln.replace("| 7 BUTTON | 0:23.7-0:32.3 |", "| 7 BUTTON | 0:24.5-0:33.1 |")
    out.append(ln)
s = "\n".join(out)

# ---- order note: beat 6 now Kai
s = s.replace("comes about 6 minutes BEFORE beats 5-6 (about 15:01).", "comes about 6 minutes BEFORE beat 5 (about 15:01).")

# ---- what the figure is (new note after order/context block)
s = s.replace("**Order and context, said plainly (cold read item 8):**",
 "**What the figure is, said plainly (new in v2.6):**\n- **Night:** the glowing figure by the tree (beat 5, and the end of Kai's clip) carries the game's prompt \"Inspect the tree\". It is the quest's effigy, an object, not the live creature. The live thing in the night quest is only seen as a dark shape.\n- **Daylight:** our frames don't show the tree-bodied figure (beats 1-2) moving. It stands on the path, the screen blurs, Jason drops at its feet, and he wakes by his truck.\n- An Instagram commenter says it is a statue whose gas knocks you out, and that the skunk ape carries you to your car. That is REPORTED, not verified.\n- **The Short claims only what is on screen** (they find it; they black out; the game says \"skunk ape\"). The hook is the players' own word, Bigfoot.\n\n**Order and context, said plainly (cold read item 8):**")

# ---- section 4 rewrite
i0 = s.index("## 4. Locked predictions"); i5 = s.index("## 5. Variants compared")
s = s[:i0] + """## 4. Locked predictions, side by side (re-locked 20 Nov ~05:00 on the hub's word, from the 04:30 numbers)
**The rule (unchanged):** start from AW's live newest-30 median, 93.5K. Move a moment off it only for a factor measured today.

| Factor (measured) | Bigfoot | Jet theft | Net |
|---|---|---|---|
| **The streamer-compilation join** (API; 19:22 vs 04:30) | **broke out overnight:** the CaseOh fan Short went 153K → **543K** (+390K in about 9 h, about 43K/h); the new "Kai Cenat Found Bigfoot In GTA 6!" is at **139K** (about 26K/h). The 8 low ones stay low | still low: "GTA 6 Sent Fighter Jets After ohnePixel's Stolen Plane" 20K, the rest near 0 | **Bigfoot +, strongly** |
| YouTube lane (watcher interval speed, 19:07 → 04:07) | 124K/h → **204K/h**, rising; 100K+ videos 5 → 10 | 718K/h → 602K/h, cooling; 100K+ 21 → 27 | jet + (still about 3x bigger), but the gap is closing |
| Instagram top reel (~19:40 → ~04:35) | 13.7M → **15.8M** (+2.1M, ≈ 240K/h); shares +31.4K | 15.5M → 16.5M (+1.0M, ≈ 115K/h); shares +2.5K | Bigfoot + (about 2x views/h, about 12x shares) |
| Entry tax (prior 100K+ Shorts of the same beat and angle) | **now heavier:** the 543K CaseOh fan Short is the same angle (a streamer finds Bigfoot). Ours differs: 4 streamers (Kai Cenat, xQc, summit1g, Fanum), the black-out, and the game's \"Nope. Skunk ape.\" reversal | Typical Gamer's own Short of the same footage, now 3.32M | both taxed; the jet's is still the same footage |
| Big faces on frame | **4:** Kai Cenat, xQc, summit1g, Fanum | 2 | Bigfoot + |

| | v2.5 (19 Nov 20:52) | **v2.6 (20 Nov ~05:00)** |
|---|---|---|
| Bigfoot, most likely | 90K | **150K** |
| Bigfoot, 50 % range | 30K-300K | **50K-450K** |
| Bigfoot, 1M+ | about 10 % | **about 15 %** |
| Bigfoot, under 10K | about 10 % | **about 6 %** |
| Bigfoot, clears 150K | about 40 % | **about 50 %** |
| Jet, most likely | 90K (30K-300K) | **90K (30K-300K), unchanged:** its join is still low and its lane is cooling |

**Why 150K and not higher:**
- The closest comparable, one streamer finding Bigfoot on a small fan channel, did 543K in a day.
- AW's own median is 93.5K, and the GTA 5 farewell (a story Short) is at 345K.
- Ours enters behind that 543K Short, on the same angle, with a different cut. The entry tax keeps the centre at the bar rather than above it.

**The bar:** **AT the 150K bar** (centre 150K, about 50 % to clear). The jet stays BELOW (90K). The exception line from v2.3-v2.5 is no longer needed for Bigfoot.
- **5K pre-mortem:** it posts after the CaseOh and Kai fan Shorts have taken the feed's \"streamer finds Bigfoot\" slot, and our cut reads as a re-up.
- **5M pre-mortem:** four of the biggest streamers in one Short, plus the game's own \"Nope. Skunk ape\", becomes the version people share.

""" + s[i5:]

# ---- G2 / G4 rows
s = re.sub(r"\| G2 What's on screen \| PASS \|[^\n]*\n",
 "| G2 What's on screen | PASS | the daylight figure on frame in beats 1-2 and its legs in beat 4; the night effigy in beat 5 (\"Inspect the tree\"); in beat 6 the objective \"Chase Mr. Mangrove\" is on screen, but the creature is not clearly visible |\n", s, count=1)
s = re.sub(r"\| G4 Freshness \| \*\*WEAK: the join was tried today and stayed low\*\* \|[^\n]*\n",
 "| G4 Freshness | **PROVEN, with an entry tax** | v2.5's \"tried and stayed low\" is out of date. Overnight the CaseOh fan Short went 153K → 543K and a Kai Cenat fan Short reached 139K, so the join works. The 543K Short is the same angle, which is the entry tax. Ours differs: 4 streamers, the black-out, and the game's reversal. The same-day multi-streamer compilations (Dropy 1,930 etc.) are still low. No AW Short on it |\n", s, count=1)
s = s.replace("- The streamer + Bigfoot join was tried today and stayed low (G4).",
 "- A 543K fan Short has already taken the \"streamer finds Bigfoot\" angle (G4 entry tax).")
s = s.replace("- Below the 150K bar: about 90K centre, under the exception.", "- At the 150K bar, not above it (150K centre, about 50 % to clear).")

# ---- section 1 bar lines
s = s.replace("- **I pick Bigfoot for this format. This is fit, not forecast: § 4 centres both at about 90K.**",
 "- **I pick Bigfoot.** As of v2.6 it is fit AND forecast: § 4 centres it at 150K against the jet's 90K.")
s = re.sub(r"- \*\*The cost:\*\* Bigfoot is cold on YouTube Shorts, and \*\*the streamer \+ Bigfoot join was already tried today and stayed low\*\*\.\n(  - .*\n){3}",
 "- **The cost:** a 543K fan Short (CaseOh) already holds the \"streamer finds Bigfoot\" angle on YouTube. Ours has to read as the bigger version: 4 streamers plus the game's reversal.\n", s, count=1)
s = s.replace("| **Famous streamers with the moment on frame, mid-clip** | **xQc, summit1g, Fanum** (plus Brendaniel's voice, HutchMF's aftermath and frizzeyes; Kai Cenat only on an Instagram re-up, not in the cut) | Typical Gamer, ohnePixel |",
 "| **Famous streamers with the moment on frame, mid-clip** | **Kai Cenat** (own Twitch clip, v2.6), **xQc, summit1g, Fanum** (plus Brendaniel's voice, HutchMF's aftermath, frizzeyes) | Typical Gamer, ohnePixel |")
s = s.replace("  - a reaction compilation needs famous faces with the moment on frame: Bigfoot has three of the biggest names in this cut (xQc, summit1g, Fanum), four if Kai Cenat is added (Q5); the jet has two;",
 "  - a reaction compilation needs famous faces with the moment on frame: Bigfoot has four of the biggest names in this cut (Kai Cenat, xQc, summit1g, Fanum); the jet has two;")
s = s.replace("and hunted xQc's at night;", "and hunted xQc's and Kai Cenat's at night;")

# ---- runners-up
s = re.sub(r"- \*\*Jet theft from the military base, fighter jets chasing:\*\*[^\n]*\n",
 "- **Jet theft from the military base, fighter jets chasing:** still the biggest by raw YouTube views (TmarTn2 3.71M, Typical Gamer 3.32M, Aaron Rheins 1.46M; Instagram 16.5M, 82.7K shares), but its lane is cooling (718K → 602K/h) and its streamer join is still low. Only Typical Gamer and ohnePixel are on frame. Its clips are on disk; no sequence is written for it.\n", s, count=1)
s = re.sub(r"- \*\*Six stars:\*\*[^\n]*\n",
 "- **Six stars: the next news candidate, noted only.** It is rising fastest: 313K → 537K/h, 18 videos at 100K+, MrBeast Gaming \"How Long Can You Survive 6 Stars In GTA 6?\" 114K in 2.4 h, Caylus, Willyrex 1.46M. Kai Cenat's clips say he hit six stars on stream; the HUD is NOT checked on frame. Nothing is started on it (the hub raises it with Affan).\n", s, count=1)

# ---- Q5
s = re.sub(r"5\. Kai Cenat did the same night quest on stream\.[^\n]*\n",
 "5. (Answered in v2.6: Kai Cenat is in, from his own Twitch clip; beat 6.)\n", s, count=1)

s += """
## 13. Added in v2.6 (20 Nov 04:20-05:10)
- **The re-check:** `UPDATE-2026-11-20-0430.md`.
  - API: 4 searches + 5 `videos` calls; 22 of 30 searches used.
  - Instagram: 4 paced loads, no block.
  - Twitch: 18 channels' clip lists, 13 thumbnails; 3 clips pulled at 720p, then Kai's at 1080p.
- **Kai's frames** (`frames/kai-1080-sheet.jpg`, `frames/kai-4up.jpg`), checked against the hub's four conditions:
  - cam visible: pass (named on the build);
  - creature on frame: only the "Chase Mr. Mangrove" objective in beat 6, and the effigy at 50-58 s;
  - chat and counters: covered (§ 3);
  - minors: none on frame.
  - The ASR is in `audio/kai-bigfoothunting.txt`.
- **IShowSpeed's "BIGFOOT" clips are NOT this moment:** a farm shootout with hazmat NPCs and a helicopter crash, no creature (`frames/t2-sheet-ishowspeed-1067453935.jpg`).
"""
open(p, "w", encoding="utf-8").write(s)
print("ok")
