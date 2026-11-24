import sys
sys.stdout.reconfigure(encoding="utf-8")
base = "X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/"
p = base + "SEQUENCE.md"
s = open(p, encoding="utf-8").read()
TOP = """# AW GTA 6 news Short: "Bigfoot Is In GTA 6 😳" (sequence v2.3, 19 Nov 2026; nothing built)

> **BELOW THE USUAL BAR. Neither moment's locked centre reaches AW's 150K bar.** Bigfoot: 120K (40K-400K). The jet: 90K (30K-300K). Both are re-centred on the channel's live numbers, read at 20:30 (§ 4).
> - **Held strictly to the bar, this route gives NO PICK.**
> - **The exception (PITCH-CHECKLIST), named first, for why Bigfoot is still worth building tonight:**
>   - you asked for this GTA 6 news Short today;
>   - GTA is the channel's fastest lane right now: "Saying Goodbye To GTA 5 💖🥹" has 298K views in 28 h against my 45K prediction, so my GTA calls have run about 6x low;
>   - launch week is a one-time window;
>   - the upside tail is real: about 15 % chance of 1M+.
"""
old_head = s.split("\n", 1)[0]
s = s.replace(old_head + "\n", TOP, 1)
R = [
("v2.2 applies the second cold read (`COLD-READ-2.md`: 10 new items).",
 "v2.2 applies the second cold read (`COLD-READ-2.md`: 10 new items). v2.3 closes the hub's open gate items (20:20-20:45): Instagram per streamer, 6 more YouTube phrasings, the anchor test, Kai, the jet prediction and the bar line."),
]
for a, b in R:
    if a not in s: print("MISSING:", a[:60])
    s = s.replace(a, b)
# NOT max effort block: replace the whole numbered list
i0 = s.index("**NOT max effort yet:**")
i1 = s.index("**What was done:**")
s = s[:i0] + """**NOT max effort yet (only items that can't be done from here):**
1. **Quotes not heard by ear.** The silence rule applies. The streamers' own words come from ASR (Fanum's are also backed by his on-stream captions), and the game's lines are its on-screen subtitles. You hear them first on the Premiere sequence or the Tella.
2. **Reddit, TikTok and X: not read.** The browser tool refused Reddit, and TikTok returned an error page.
3. **Kai Cenat is not placed in his stream.** No Twitch clip of the moment exists (98 clips over 7 days checked), and the hub said not to pull his 19-hour VOD. He stays out of the cut (Q5).

""" + s[i1:]
s = s.replace("- **YouTube:** 12 Data API searches since 18 Nov 10:00 UTC, plus 12 `videos` calls giving exact counts for 570 videos (`api/`).",
 "- **YouTube:** 18 Data API searches since 18 Nov 10:00 UTC, plus 16 `videos` calls giving exact counts for 770 videos (`api/`).\n  - The knock-out and the skunk-ape beat now have 3 phrasings each: \"gta 6 bigfoot knocked out\", \"gta 6 bigfoot attack\", \"gta 6 mr mangrove\"; \"gta 6 skunk ape quest\", \"gta 6 bigfoot not bigfoot\", \"gta 6 skunk ape kirk\".\n  - Best results: SeseGel (Turkish, \"found Bigfoot, a tiger attacked\") 250K at 40.5K/h; GameV \"These Animals Can Actually KILL You\" 100K. Same-day Shorts titled \"Bigfoot is real… and he knocks you out\" sit under 1K.\n  - **Nobody has the \"it's not Bigfoot\" angle in a Short.**\n  - AW's own channel was read via the API (1 channel + 1 playlist + 1 videos call): newest-30 median **93.5K**; the GTA 5 farewell is at **298K in 28 h**.")
open(p, "w", encoding="utf-8").write(s)
print("ok")
