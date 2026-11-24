import sys
sys.stdout.reconfigure(encoding="utf-8")
base = "X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/"
p = base + "SEQUENCE.md"
s = open(p, encoding="utf-8").read()
R = [
("(sequence v2.1, 19 Nov 2026; nothing built)", "(sequence v2.2, 19 Nov 2026; nothing built)"),
("v2.1 applies Fable's final review and adds Kai Cenat, confirmed on frame at 20:10.",
 "v2.1 applies Fable's final review and adds Kai Cenat, confirmed on frame at 20:10. v2.2 applies the second cold read (`COLD-READ-2.md`: 10 new items)."),
("8. **No second cold read of v2.1** (MAX-EFFORT-GATE item 5 asks for a re-read after large fixes): see § 12.",
 "8. Cold read 2 (on v2.1) is done and applied; v2.2's small numeric fixes have had no third read."),
("| Instagram, all creator reels we read with a face cam | frizzeyes 226K shares, Clix 3K: about 229K | Typical Gamer 65K, Leopard 80K, itssmro 56K, nixstahh 156K (flying, not a theft), alphavoid 0.4K: about 357K |",
 "| Instagram, all creator reels we read with a face cam | frizzeyes 226K shares, Clix 3K: about 229K | jet-theft reels: Typical Gamer 65K, Leopard 80K, itssmro 56K, alphavoid 0.4K: about 201K. With nixstahh's plane-flying reel (156K; not a theft): 357K |"),
("- **By the brief's literal metric, the jet is the hottest moment of launch day.** It leads YouTube by about 6.6x and Instagram by total creator shares.",
 "- **By the brief's literal metric, the jet is the hottest moment of launch day.** It leads YouTube by about 6.6x and has the bigger top Instagram reel by total views (15.5M against 13.7M). Creator-reel shares are about level (Bigfoot about 229K, jet-theft reels about 201K)."),
("each top reel measured over its own window, Bigfoot gains about 1.3-1.5x the views per hour and about 10x the shares.",
 "each top reel measured over its own window, Bigfoot gains about 1.35x the views per hour (≈ 440K/h against ≈ 325K/h) and about 10x the shares."),
("  - a reaction compilation needs famous faces with the moment on frame: Bigfoot has four of the biggest names (Kai Cenat, xQc, summit1g, Fanum), the jet has two;",
 "  - a reaction compilation needs famous faces with the moment on frame: Bigfoot has three of the biggest names in this cut (xQc, summit1g, Fanum), four if Kai Cenat is added (Q5); the jet has two;"),
("and hunted xQc's (and Kai Cenat's) at night;", "and hunted xQc's at night;"),
("(twitch.tv/fanum/clip/CleverImportantNuggetsCmonBruh-uSYmEMOocVv1V7Cv, \"fanum finds out bigfoot is real\", 66-78 views)",
 "(twitch.tv/fanum/clip/CleverImportantNuggetsCmonBruh-uSYmEMOocVv1V7Cv, \"fanum finds out bigfoot is real\", 56 views in the 16:34 list; 66 at the Afterhours download)"),
("- **Fanum:** his burned-in stream captions (purple, lower centre), the chat panel (top right), the viewer count, \"DEATH COUNTER\" and \"Twitch Subs 7157 / 8,000\". Crop to the game area; our caption plate covers his captions.",
 "- **Fanum:** his burned-in stream captions (purple, lower centre), the chat panel (top right), the viewer count, \"DEATH COUNTER\" and \"Twitch Subs 7157 / 8,000\". Crop away the right-hand quarter of the 1920x1080 frame, which holds chat, counter and goal; keep x 0-1440, which keeps his cam (left, about y 400-650). Our caption plate covers his captions."),
("- **summit1g:** the donation alert \"Khafen: $50.00\" over his cam, and the \"21,256\" count.",
 "- **summit1g:** the donation alert \"Khafen: $50.00\" sits on the cam's top edge, and the \"21,256\" count under it. Cover each with a small plate outside the face, not a blur across it."),
("| 5 | 0:16.8-0:20.9 | `xqc-chase-1370-1500.mp4` = xQc launch VOD 2932113307, ≈ VOD 15:01:09-15:01:13 (file 1419.5-1423.6) |",
 "| 5 | 0:16.8-0:20.9 | `xqc-chase-1370-1500.mp4` (**in-file 49.5-53.6 s**; = pull-timeline 1419.5-1423.6) = xQc launch VOD 2932113307, ≈ VOD 15:01:09-15:01:13 |"),
("| 6 | 0:20.9-0:23.7 | same file, ≈ 1445.0-1447.8 (≈ VOD 15:01:35; re-check ±1 s at build) |",
 "| 6 | 0:20.9-0:23.7 | same file, **in-file ≈ 75.0-77.8 s** (pull-timeline ≈ 1445.0-1447.8; ≈ VOD 15:01:35). Edges to re-measure on the audio at build: the ASR has no words in this window, and an f-word starts at pull-timeline 1448.2 (in-file 78.2), so the out-point must stay before it |"),
("| 7 BUTTON | 0:23.9-0:32.5 | `xqc-kirk-0940-1060.mp4` = VOD file 1032.0-1040.6 (≈ VOD 14:54:42-14:54:51) |",
 "| 7 BUTTON | 0:23.7-0:32.3 | `xqc-kirk-0940-1060.mp4` (**in-file 92.0-100.6 s**; = pull-timeline 1032.0-1040.6; ≈ VOD 14:54:42-14:54:51). 8.6 s holds because it is a two-line dialogue; keep xQc's inset visible |"),
("our frames at 1033.75 and 1036.25 match.", "our frames at in-file 93.5 and 96.5 match."),
("## 3. The sequence (about 32 s)", "## 3. The sequence (32.3 s)"),
("**Order and context, said plainly (cold read item 8):**",
 "**File offsets (for whoever cuts it):**\n- The `xqc-*.mp4` files were stream-copied from the Afterhours pull of VOD 2932113307 (pull start = VOD 14:37:30) at pull-timeline 1370 and 940, so they may start a few frames early on a keyframe.\n- The ASR in `audio/` was cut from the same pull at 1380 and 960.\n- Times marked \"pull-timeline\" are seconds in the original pull; \"in-file\" are seconds in our copies.\n\n**Order and context, said plainly (cold read item 8):**"),
("| Censor | ASK | 2 f-words → F*CK in captions.",
 "| Censor | ASK | 2 f-words → F*CK in captions; one more right after beat 6 (xQc pull-timeline 1448.2) is a hazard for the out-point."),
("Willyrex \"I FIND BIGFOOT in GTA VI\" 521K, from the watcher;",
 "Willyrex \"I FIND BIGFOOT in GTA VI\" 521K, from the watcher store at 19:07, `api/watcher-moments-1907.txt` line 29;"),
("YouTube \"i found BIGFOOT in GTA 6\" 140K and \"I FIND BIGFOOT in GTA VI\" 521K.",
 "YouTube \"i found BIGFOOT in GTA 6\" 140K (`api/`) and \"I FIND BIGFOOT in GTA VI\" 521K (`api/watcher-moments-1907.txt`); the YouTube Short \"KAI CENAT & FANUM FOUND BIGFOOT IN GTA 6\" (874 views)."),
("- **Re-read:** the cold read covered v2's changes from v1. v2.1's changes (this section, the velocity row, the reactor count, the labels) have had no second independent read.",
 "- **Re-read:** cold read 2 (`COLD-READ-2.md`) checked v2.1. Its 10 items are applied in v2.2: the jet shares counted without the plane-flying reel; Fanum's views; in-file seconds and offsets for the xQc beats; the beat-6 f-word hazard; Kai counted only if added; the Willyrex row saved; the Fanum crop and the summit1g alert plate; beat times closed at 32.3 s; 1.35x; cross-file fixes."),
]
miss = [a[:80] for a, b in R if a not in s]
for a, b in R:
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
print("missing:", miss)
# cross-file fixes
r = base + "README.md"
t = open(r, encoding="utf-8").read()
t = t.replace("YouTube Data API (8 searches, `api/s1-8.json`,", "YouTube Data API (12 searches, `api/s1-s12.json`,")
open(r, "w", encoding="utf-8").write(t)
g = base + "ig/IG-PASS-1.md"
u = open(g, encoding="utf-8").read()
if "Correction (main session" not in u:
    u += "\n## Correction (main session, 20:16)\nKai Cenat WAS found on Bigfoot after this pass: Instagram re-up Df5u9Z8ysMb (@nerrd_engineer, 5 likes), with his Twitch cam beside the glowing creature and the subtitle \"Run! We're the prey! Run!\". This pass's \"No Kai/Speed/xQc reaction\" covers only its own grids. xQc's Bigfoot moment is in his VOD (the skunk-ape quest), not on Instagram.\n"
    open(g, "w", encoding="utf-8").write(u)
print("ok")
