import sys
sys.stdout.reconfigure(encoding="utf-8")
base = "X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/"
p = base + "SEQUENCE.md"
s = open(p, encoding="utf-8").read()
R = [
("  - Two more loads by this session at about 20:00-20:10: \"fanum gta 6\", and the Kai Cenat re-up.",
 "  - Loads by this session at about 20:00-20:10: \"fanum gta 6\", and the Kai Cenat re-up.\n  - **Per streamer, pass 2 at 20:19-20:39** (`ig/IG-PASS-2-streamers.md`, about 21 loads, 11 queries) plus 4 more loads by this session at 20:42-20:47: \"xqc skunk ape\", #gta6bigfoot, and 2 posts. Results are in § 6's IG row."),
("| IG first filter | PASS (creature + knock-out) · WEAK (skunk-ape beat) · OPEN (per streamer) |",
 "| IG first filter | PASS (creature + knock-out) · WEAK (skunk-ape beat) · **WEAK (per streamer)** |"),
("Skunk ape: reels of at most 2K likes, plus a 701-like comment \"That's Skunk Ape to us in Florida\" |",
 "Skunk ape: reels of at most 2K likes, plus a 701-like comment \"That's Skunk Ape to us in Florida\". **#gta6bigfoot top reels:** frizzeyes; spectrexgaming 38.3K likes; siidv2 \"Bigfoot CONFIRMED in GTA 6\" **61K likes, 207 comments**; cadaver_x \"GTA 6 is actually a horror game\" (streamer itskreas) 4K likes.\n**Per streamer (2-3 phrasings each):**\n- Fanum: his 5 GTA 6 reels are other moments (a rap about missing GTA 6, 122K likes); \"fanum bigfoot\": No results.\n- summit1g: \"summit1g gta 6\" and \"summit1g bigfoot\": No results.\n- xQc: big GTA 6 reels are other moments (renovating his house, fboy, 117K likes); \"xqc bigfoot\" and \"xqc skunk ape\": No results.\n- Kai Cenat: \"kai cenat bigfoot\" gave 24 tiles, 4 opened, all tiny re-ups (33, 9, 1 and 0 likes). One confirms he was knocked out (\"instantly got KNOCKED OUT\").\n- Brendaniel: one Portuguese compilation (2 likes) crediting his stream among others.\n- **So the moment is proven on Instagram, but the streamers' own Bigfoot clips are not. The join (these streamers + Bigfoot) is fresh, not proven.** |"),
]
for a, b in R:
    if a not in s: print("MISSING:", a[:70])
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
print("ok")
