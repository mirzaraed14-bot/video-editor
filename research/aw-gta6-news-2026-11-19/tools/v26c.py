import sys, re
sys.stdout.reconfigure(encoding="utf-8")
base = "X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/"
p = base + "SEQUENCE.md"
s = open(p, encoding="utf-8").read()
def rep(a, b, must=True):
    global s
    if a not in s:
        if must: print("MISSING:", a[:90])
        return
    s = s.replace(a, b)

# top block correction line
rep("> - One correction: the glowing night figure (beats 5-6) is the quest's effigy (\"Inspect the tree\"), not the live creature.",
    "> - **Correction to the picture:**\n>   - The big figures are effigies, branch figures bound to trees that never move: the daylight one in beats 1-2 and the glowing night one in beats 5-6.\n>   - **Bigfoot itself** is on frame only as its **hairy legs standing over the knocked-out player** (beat 4). The same legs appear in summit1g's clip.\n>   - The hook and the button still hold.")
# 2. The pick
s = re.sub(r"- \*\*Moment:\*\* a giant tree-bodied creature waits in GTA 6's Grassrivers swamp\.[^\n]*\n",
 "- **Moment:** GTA 6 has a Bigfoot in its Grassrivers swamp, and the game calls it a skunk ape.\n  - Guides describe it running through the swamp to a giant branch figure bound to a tree, an effigy. Stand in the effigy's green fog and you black out; Bigfoot comes back and stands over you; you wake up nearby (PowerPyx and GTA6 SOL descriptions, `api/v_ids3_*.json`).\n  - A side quest about it has a drone operator named Kirk tell you it is not Bigfoot.\n", s, count=1)
rep("- **Arc:** setup: streamers walk into a monster in the swamp → turn: it blacks them out, then hunts them at night → ending: the game's own character says \"Nope. Skunk ape. Same genus, different species.\"",
    "- **Arc:** setup: streamers walk into a giant figure in the swamp → turn: they black out, and Bigfoot stands over them → ending: the game's own character says \"Nope. Skunk ape. Same genus, different species.\"")
s = re.sub(r"- \*\*The viewer gets:\*\* GTA 6 hid a Bigfoot in its swamp;[^\n]*\n",
 "- **The viewer gets:** GTA 6 hid a Bigfoot in its swamp. Its giant effigy knocks you out, and the real thing stands over you while you're down. Kai Cenat, xQc, summit1g and Fanum all ran into it, and the game insists it's a \"skunk ape\". This is entertainment (VIRAL-BAR gate I), not a money or career stake.\n", s, count=1)
# beats 1, 2, 4 pictures
rep("**The creature fills the frame from frame 1:** bark body, rope at the waist, claws",
    "**The effigy fills the frame from frame 1:** a giant figure of bark and branches bound to a tree with rope, with claws. It never moves (VERIFY-F2)")
rep("He walks up the mangrove path; the creature stands there; the camera pushes in", "He walks up the mangrove path; the effigy stands there; the camera pushes in")
rep("| Blacked out: the creature's huge legs standing over him |",
    "| Blacked out: **Bigfoot's hairy legs standing over him**, Bigfoot itself (PowerPyx: \"Bigfoot comes back to look at you\"). summit1g's clip shows the same legs at 40-44 s with his cam (`frames/legs-4up.jpg`) |")
rep("PROVEN: the creature = the 13.7M / 226K-share reel", "PROVEN: the same figure as the 13.7M reel (now 15.8M)")
# swap beats 5 and 6 (game order: inspect first, then Kirk)
lines = s.split("\n")
i5 = next(i for i, l in enumerate(lines) if l.startswith("| 5 | 0:16.8-0:20.9 |"))
i6 = next(i for i, l in enumerate(lines) if l.startswith("| 6 | 0:20.9-0:24.9 |"))
b5 = lines[i5].replace("| 5 | 0:16.8-0:20.9 |", "| 6 | 0:20.8-0:24.9 |")
b6 = lines[i6].replace("| 6 | 0:20.9-0:24.9 |", "| 5 | 0:16.8-0:20.8 |")
b6 = b6.replace("**NEW in v2.6, replaces xQc's \"Run! We're the prey!\" dark-shape beat.**", "**NEW in v2.6, replaces xQc's \"Run! We're the prey!\" dark-shape beat; placed before Kirk, as in the game.**")
b6 = b6.replace("\"oh my gosh bro\" (55.02-58.46, Kai, ASR)", "\"oh my gosh bro\" (55.02-58.46, Kai, ASR; edges to re-measure)")
lines[i5] = b6; lines[i6] = b5
s = "\n".join(lines)
rep("comes about 6 minutes BEFORE beat 5 (about 15:01).", "comes about 6 minutes BEFORE beat 6 (about 15:01).")
rep("(the quest's effigy is on frame next to Kirk in beat 5)", "(the quest's effigy is on frame next to Kirk in beat 6)")
rep("- **Night:** the glowing figure by the tree (beats 5 and 6)", "- **Night:** the glowing figure by the tree (beats 5 and 6)")
# figure note rewrite
s = re.sub(r"\*\*What the figure is, said plainly \(new in v2\.6\):\*\*\n(- .*\n){4}",
 """**What the figure is, said plainly (new in v2.6, settled after Fable's final call):**
- **The big figures are effigies.**
  - PowerPyx's "Search for Tree Effigies" guide: "They look like stick figures bound to trees."
  - Afterhours' VERIFY-F2: summit1g's daylight figure "never moves".
  - At night the game prompts "Inspect the tree".
- **Bigfoot itself:** guides say it runs through the swamp to an effigy, you pass out in the green fog, and "Bigfoot comes back to look at you".
  - On our frames that is its hairy legs standing over the player: Brendaniel 55-58 s, summit1g 40-44 s.
  - Streamers' glimpses of it running (Lacy, Swagg, Agent00) aren't readable on frame and aren't used.
- **The Short claims only what is on screen:** they find the figure; they black out; Bigfoot's legs stand over them; the game says "skunk ape". The hook is the players' own word, Bigfoot.
""", s, count=1)
# G2 / G5 / Shape / reactor lines
s = re.sub(r"\| G2 What's on screen \| PASS \|[^\n]*\n",
 "| G2 What's on screen | PASS | Bigfoot itself as its hairy legs over the player (beat 4); the daylight effigy in beats 1-2; the night effigy in beats 5-6 (\"Inspect the tree\") |\n", s, count=1)
s = re.sub(r"\| G5 Facts \| PASS, with the context in § 3 \|[^\n]*\n",
 "| G5 Facts | PASS, with the context in § 3 | In the released game (Twitch launch streams). **Bigfoot itself on frame in 2 independent streams** (its legs: summit1g, Brendaniel); its effigies in 5 (Fanum, summit1g, Brendaniel by day; xQc, Kai Cenat by night). The daylight encounter is free roam; the night scenes are a side quest. The quotes are the game's subtitles or the streamers' own words (ASR). \"Bigfoot\" is the players' word, corrected by the game |\n", s, count=1)
rep("| Shape | PASS (comic F1) | a belief named (Bigfoot) → physical proof (it blacks them out) → the \"owner\" corrects it |",
    "| Shape | PASS (comic F1) | a belief named (Bigfoot) → physical proof (they black out; its legs stand over them) → the \"owner\" corrects it |")
rep("so it is 4 under \"the encounter's figure on frame\". Under \"the live creature on frame\", only the daylight figure counts (summit1g, Fanum), and even that is not shown moving.",
    "so it is 4 under \"the encounter on frame\" (effigies included). Under \"Bigfoot itself on frame, with a cam\", only summit1g holds (its legs at 40-44 s); Brendaniel shows it too, but without a cam. **The hub's call:** Kai is in on the effigy only.")
rep("| **Kai Cenat** (own Twitch clip, the night effigy), **xQc** (the night effigy), **summit1g, Fanum** (the daylight figure)",
    "| **Kai Cenat** (own Twitch clip, the night effigy), **xQc** (the night effigy), **summit1g** (the daylight effigy + Bigfoot's legs), **Fanum** (the daylight effigy)")
rep("| Big faces with the encounter on frame | 4 (Kai Cenat, xQc: night effigy; summit1g, Fanum: daylight figure) | 2 |",
    "| Big faces with the encounter on frame | 4 (Kai Cenat, xQc: night effigy; summit1g: daylight effigy + Bigfoot's legs; Fanum: daylight effigy) | 2 confirmed (Typical Gamer, ohnePixel); Fanum's \"crash-lands a jet on a city street\" and 2 Agent00 jet clips are in the 04:30 list, not checked |")
s = re.sub(r"Only Typical Gamer and ohnePixel are on frame\. Its clips are on disk; no sequence is written for it\.",
 "2 streamers confirmed on frame (Typical Gamer, ohnePixel); Fanum's and Agent00's jet clips in the 04:30 list are not checked, and the lists look capped. Its clips are on disk; no sequence is written for it.", s, count=1)
# censor row: drop the 1448.2 hazard
rep("2 f-words → F*CK in captions; one more right after beat 6 (xQc pull-timeline 1448.2) is a hazard for the out-point.",
    "2 f-words → F*CK in captions (the 1448.2 hazard went with the dropped xQc beat).")
# sources + anchor
rep("| alternates | `hutch-bigfoot.mp4` (HutchMF aftermath, 2560x1440), `summit-findsbigfoot.mp4` | |",
    "| `kai-bigfoothunting-4096145023.mp4` | Kai Cenat, \"bigfoot hunting\" (beat 5), -13.2 LUFS, LRA 5.4 | 1920x1080 60 |\n| alternates | `hutch-bigfoot.mp4` (HutchMF aftermath, 2560x1440), `summit-findsbigfoot.mp4`; summit1g 40-44 s (Bigfoot's legs, with his cam) | |")
rep("- Faces at delivery: Fanum 67 px wide; summit1g 50 px as an inset, 165 px if enlarged into a split; xQc about 45 px (too small for the detector). Prince: 772-883 px.",
    "- Faces at delivery: Fanum 67 px wide; summit1g 50 px as an inset, 165 px if enlarged into a split; xQc about 45 px (too small for the detector); Kai Cenat's cam is about 392 px wide of 1920, so his face is about 70 px (not run through the detector). Prince: 772-883 px.")
# section 0 counts and open list
rep("- **Fable advisor:** 4 calls.", "- **Fable advisor:** 5 calls.")
rep("  - On v2.3 (about 20:44): its four blocking fixes are applied in v2.4.",
    "  - On v2.3 (about 20:44): its four blocking fixes are applied in v2.4.\n  - On v2.6 (20 Nov about 04:39): its blocking point was what the figure is; it is settled and applied above. Its non-blocking items are applied too: beat order, sources, censor row, counts, beat-5 edges, the Instagram file.")
rep("- **Cold reads:** 1 on v1 (`COLD-READ.md`), 2 on v2.1 (`COLD-READ-2.md`), 3 on v2.4 (`COLD-READ-3.md`). Each one's fixes are applied.",
    "- **Cold reads:** 4 in all: v1 (`COLD-READ.md`), v2.1 (`-2`), v2.4 (`-3`), v2.6 (`-4`). Each one's fixes are applied.")
rep("3. **Kai Cenat's clip read at 1080p on frames and ASR only**",
    "3. **The 543K CaseOh fan Short was not viewed** (title only; nothing from YouTube, per the hub).\n4. **Kai Cenat's clip read at 1080p on frames and ASR only**")
rep("- **YouTube:** 18 Data API searches since 18 Nov 10:00 UTC, plus 16 `videos` calls giving exact counts for 770 videos (`api/`).",
    "- **YouTube:** 22 Data API searches since 18 Nov 10:00 UTC (4 in the 20 Nov re-check), plus 21 `videos` calls, giving exact counts for about 970 videos (`api/`, `api/t2/`).")
rep("  - Instagram: 4 paced loads, no block.", "  - Instagram: 4 paced loads, no block (`ig/IG-RECHECK-0435.md`).")
s += "- **Fable's final review of v2.6** (04:39) applied:\n  - the figure settled: effigies, plus Bigfoot's legs;\n  - beats 5 and 6 swapped into the game's order;\n  - the jet faces reworded (2 confirmed, others not checked);\n  - the censor row, sources, anchor line, counts and Instagram file updated.\n"
open(p, "w", encoding="utf-8").write(s)
print("ok")
