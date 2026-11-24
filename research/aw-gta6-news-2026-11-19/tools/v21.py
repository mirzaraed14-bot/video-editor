import sys
sys.stdout.reconfigure(encoding="utf-8")
p = "X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/SEQUENCE.md"
s = open(p, encoding="utf-8").read()
R = [
("# AW GTA 6 news Short: \"Bigfoot Is In GTA 6 😳\" (sequence v2, 19 Nov 2026; nothing built)",
 "# AW GTA 6 news Short: \"Bigfoot Is In GTA 6 😳\" (sequence v2.1, 19 Nov 2026; nothing built)"),
("v2 applies the cold read (`COLD-READ.md`: 8 must-fix, 13 should-fix); v1 is kept at `SEQUENCE.v1.md`.",
 "v2 applies the cold read (`COLD-READ.md`: 8 must-fix, 13 should-fix). v2.1 applies Fable's final review and adds Kai Cenat, confirmed on frame at 20:10. v1 is kept at `SEQUENCE.v1.md`."),
("6. **Kai Cenat lead unchecked:** a YouTube Short titled \"KAI CENAT & FANUM FOUND BIGFOOT\" (874 views) and a tiny Instagram reel (\"Kai Cenat meets the skunk ape\"). Kai's VOD 2932305259 was not searched.",
 "6. **Kai Cenat's moment is not located in his VOD yet.** He IS on frame with the creature; see § 1. His VOD 2932305259 is 19 h long and was not pulled."),
("7. **frizzeyes' 13.7M reel** was frame-checked but not downloaded.",
 "7. **frizzeyes' 13.7M reel** was frame-checked but not downloaded.\n8. **No second cold read of v2.1** (MAX-EFFORT-GATE item 5 asks for a re-read after large fixes): see § 12."),
("  - Our own pass, 19:30-20:05, about 21 loads (`ig/IG-PASS-1.md`): the lead reels re-read for growth since 14:00; 6 searches; 5 posts opened.",
 "  - Our own pass, about 19:30-19:47, about 21 loads (`ig/IG-PASS-1.md`): the lead reels re-read for growth since 14:00; 6 searches; 5 posts opened.\n  - Two more loads by this session at about 20:00-20:10: \"fanum gta 6\", and the Kai Cenat re-up."),
("- **Fable advisor:** twice before the lock (19:28, 19:44). Its three conditions held. The final call is next.",
 "- **Fable advisor:** 3 calls.\n  - Before the lock (19:28, 19:44), with three conditions:\n    - the 11.2M reel is this creature: held;\n    - no Kai or Speed on the jet: held;\n    - at least 4 reactors hold mid-clip: held at **3** on its own standard (camera, creature and reaction in one clip: summit1g, Fanum, xQc), and at **4** once Kai Cenat was confirmed at 20:10. (My lock message to the hub said 5; that counted HutchMF's aftermath and frizzeyes' reel, and is corrected here.)\n  - On the final (about 20:07): its four fixes are applied in v2.1."),
("| **Instagram top reel, views/h over the last ~5.5 h** (two reads, ~14:00 and ~19:45) | **@frizzeyes: +2.5M views (~450K/h), +41.5K shares; now 13.7M on 6.5K followers, 226K shares** | @leopardstealth: +1.4M (~250K/h), +3.1K shares; now 15.5M on 10.3K, 80K shares |",
 "| **Instagram top reel, views/h, each over its own window** (first read: Bigfoot by 14:01, jet by 15:26; second read: both by 19:47) | **@frizzeyes: 11.2M → 13.7M = +2.5M in about 5.7 h (≈ 440K/h); shares +41.5K (≈ 7.3K/h); now 226K shares on 6.5K followers** | @leopardstealth: 14.1M → 15.5M = +1.4M in about 4.3 h (≈ 325K/h); shares +3.1K (≈ 0.7K/h); now 80K shares on 10.3K |"),
("| **Famous streamers with the moment on frame, mid-clip** | **xQc, summit1g, Fanum** (plus Brendaniel's voice, HutchMF's aftermath, frizzeyes) | Typical Gamer, ohnePixel |",
 "| **Famous streamers with the moment on frame, mid-clip** | **Kai Cenat** (on an Instagram re-up of his Twitch stream: his cam, the glowing creature, \"Run! We're the prey! Run!\"), **xQc, summit1g, Fanum** (plus Brendaniel's voice, HutchMF's aftermath, frizzeyes) | Typical Gamer, ohnePixel |"),
("- **Bigfoot is hotter on Instagram right now:** its top reel is gaining about 1.8x the views per hour and about 13x the shares.",
 "- **Bigfoot is hotter on Instagram right now:** each top reel measured over its own window, Bigfoot gains about 1.3-1.5x the views per hour and about 10x the shares."),
("  - a reaction compilation needs famous faces with the moment on frame: Bigfoot has three of the biggest names, the jet has two;",
 "  - a reaction compilation needs famous faces with the moment on frame: Bigfoot has four of the biggest names (Kai Cenat, xQc, summit1g, Fanum), the jet has two;"),
("The game has a side quest about it, in which a hunter tells you it is not Bigfoot.",
 "The game has a side quest about it, in which a drone operator named Kirk tells you it is not Bigfoot."),
("- **Arc:** setup: streamers walk into a monster in the swamp → turn: it blacks them out → ending: the game's own hunter says \"Nope. Skunk ape. Same genus, different species.\"",
 "- **Arc:** setup: streamers walk into a monster in the swamp → turn: it blacks them out, then hunts them at night → ending: the game's own character says \"Nope. Skunk ape. Same genus, different species.\""),
("- **The viewer gets:** GTA 6 hid a Bigfoot in its swamp; it knocked out xQc, summit1g and Fanum's characters; and the game insists it's a \"skunk ape\".",
 "- **The viewer gets:** GTA 6 hid a Bigfoot in its swamp; it blacked out summit1g's and Brendaniel's characters and hunted xQc's (and Kai Cenat's) at night; and the game insists it's a \"skunk ape\"."),
("| Kirk (GTA 6), italic; label `KIRK · SKUNK-APE HUNTER (GTA 6)` · `XQC · TWITCH` (inset, no split) | PROVEN (subtitles + creature on frame) |",
 "| Kirk (GTA 6), italic; label `KIRK · THE DRONE OPERATOR (GTA 6)` (the game's map card calls him that; the label is OURS) · `XQC · TWITCH` (inset, no split) | PROVEN (subtitles + creature on frame) |"),
("| **Fanum** · `FANUM · TWITCH` · card THEY FOUND `BIGFOOT` IN GTA 6 | PROVEN: the creature = the 13.7M / 226K-share reel |",
 "| **Fanum** · `FANUM · TWITCH` · card THEY FOUND `BIGFOOT` IN GTA 6 (OURS) | PROVEN: the creature = the 13.7M / 226K-share reel |"),
("| Jason and Kirk (GTA 6), italic | PROVEN: VERIFY-F (Afterhours) read the subtitles exactly; our frames at 1033.75 and 1036.25 match |",
 "| Jason and Kirk (GTA 6), italic | PROVEN words: VERIFY-F (Afterhours) read the subtitles exactly; our frames at 1033.75 and 1036.25 match. **Placing it last is OURS** (see the order note) |"),
("- **Jet theft from the military base, fighter jets chasing:** the hottest on YouTube (Typical Gamer 2.35M; TmarTn2 160K/h). On Twitch only Typical Gamer and ohnePixel are on frame. It is also beat 5 of the Afterhours long-form.",
 "- **Jet theft from the military base, fighter jets chasing:** the hottest on YouTube (Typical Gamer 2.35M; TmarTn2 160K/h). On Twitch only Typical Gamer and ohnePixel are on frame. It is also beat 5 of the Afterhours long-form. **Its clips are on disk (`media/ondisk/tg-*`, `tw-*`), but no sequence is written for it:** about 30 minutes if you choose it."),
("5. Should we check Kai Cenat's VOD for a Bigfoot moment before the build? If he has one, he goes in as the biggest face.",
 "5. Kai Cenat did the same night quest on stream. Shall the build locate it in his VOD (one paced Twitch pull) and put him in beats 5-6 in place of xQc, keeping xQc for the button?"),
]
miss = [a[:70] for a, b in R if a not in s]
for a, b in R:
    s = s.replace(a, b)
s += """
## 12. Added in v2.1 (Fable's final review, 20:07-20:12)
- **Kai Cenat, CONFIRMED on frame** (Instagram re-up Df5u9Z8ysMb by @nerrd_engineer, 5 likes, 58 s; caption "Kai ran into the skunk ape in GTA 6", credit twitch.tv/kaicenat).
  - At 20 s: his Twitch cam beside the same glowing creature, with the subtitle "Oh God...".
  - At 44 s: a chase with the subtitle "Run! We're the prey! Run!".
  - Viewer count on screen: about 170K.
  - **Source for the build:** his VOD 2932305259 (19 h 11 min); the time is NOT located yet.
- **A possible xQc line of his own:** the ASR has "You see there, too, guys?" at VOD file 1432.3-1433.3. There is no subtitle on frame at 1432.3, and the shot shows a glowing skunk-like animal in the grass. ASR-only, not used.
- **OURS, named:** the hook card; Kirk's label; placing the skunk-ape talk last.
- **Re-read:** the cold read covered v2's changes from v1. v2.1's changes (this section, the velocity row, the reactor count, the labels) have had no second independent read.
"""
open(p, "w", encoding="utf-8").write(s)
print("missing:", miss)
