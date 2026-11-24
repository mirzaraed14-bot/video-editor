import sys
sys.stdout.reconfigure(encoding="utf-8")
base = "X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/"
p = base + "SEQUENCE.md"
s = open(p, encoding="utf-8").read()
R = [
("(sequence v2.4, 19 Nov 2026; nothing built)", "(sequence v2.5, 19 Nov 2026; nothing built)"),
(">   - GTA content is doing well on AW right now: \"Saying Goodbye To GTA 5 💖🥹\" has 298K views in 28 h;",
 ">   - GTA isn't penalised on AW: one GTA Short, the story-format farewell \"Saying Goodbye To GTA 5 💖🥹\", has 298K views in 28 h. That is n = 1 and is no evidence for a reaction compilation;"),
("v2.4 applies Fable's review of v2.3: both predictions on one rule, the tried join named as a weakness, absence claims softened, and cold read 3.",
 "v2.4 applies Fable's review of v2.3: both predictions on one rule, the tried join named as a weakness, absence claims softened. v2.5 applies cold read 3 (`COLD-READ-3.md`, 10 items)."),
("(77 clips since 18 Nov; the list may be capped)",
 "(77 of the 98 clips in `twitch/kai-7d.json` are dated 18 Nov or later, timestamp ≥ 1795000000; the list may be capped)"),
("- **Fable advisor:** 3 calls.", "- **Fable advisor:** 4 calls."),
("held at **3** on its own standard (camera, creature and reaction in one clip: summit1g, Fanum, xQc), and at **4** once Kai Cenat was confirmed at 20:10. (My lock message to the hub said 5; that counted HutchMF's aftermath and frizzeyes' reel, and is corrected here.)",
 "held at **3** in the cut on its own standard (camera, creature and reaction in one clip: summit1g, Fanum, xQc). Kai Cenat would make 4, but he is out of the cut. Brendaniel is voice-only, and his clip is not checked to be this exact moment. (My lock message to the hub said 5; that counted HutchMF's aftermath and frizzeyes' reel, and is corrected here.)"),
("| Entry tax (prior 100K+ Shorts of the same moment) | 3 Shorts at 113K-153K (CaseOh fan clip, LazarLazar, DarkViperAU) | Typical Gamer's own Short of the exact clip, 2.35M | Bigfoot + |",
 "| Entry tax (prior 100K+ Shorts of the same moment) | **against Bigfoot:** 3 Shorts at 113K-153K on the creature (CaseOh fan clip, LazarLazar, DarkViperAU); none uses our clips (summit1g, Fanum, xQc) | **against the jet, heavier:** Typical Gamer's own 2.35M Short is the same footage our jet cut would lead with | both taxed; the jet's is the same footage, so Bigfoot + |"),
("| 50 % range | 30K-300K | 30K-300K |", "| 50 % range (the channel's own spread around its median; its newest 30 run 4.5K-561K, not moment-specific) | 30K-300K | 30K-300K |"),
("| Under 10K | about 10 % | about 10 % |",
 "| Under 10K | about 10 % | about 10 % |\n| Clears the 150K bar (under the same spread) | about 40 % | about 40 % |"),
("- Instagram was not searched per streamer.",
 "- Per-streamer Instagram search found no reel of these streamers with Bigfoot (likes and comments read only)."),
("spectrexgaming 38.3K likes;", "spectrexgaming 38.3K likes (earlier read, not re-read);"),
("same-day YouTube \"streamers found Bigfoot\" Shorts: Dropy 1.9K, Komnt 1.5K, TurkishProduction 1.2K, GTA Updates 0.9K,",
 "same-day YouTube \"streamers found Bigfoot\" Shorts: Dropy UzViI0St2ts 1,930; Komnt UYzb7gleBbE 1,511; TurkishProduction nLICuB4kNfk 1,220; GTA Updates fNBGCPtDhPw 874 (exact counts, API 19:22),"),
]
miss = []
for a, b in R:
    if a not in s: miss.append(a[:70])
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
print("missing:", miss)
