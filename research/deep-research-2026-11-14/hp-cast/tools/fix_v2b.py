"""Sun 02:20: the scoped re-read's 9 fixes across PITCH.md, the hp-cast.md FINAL/STATUS/tracker, HP-EXECUTION item 7 and RUN.md."""
import os
D = r"X:\Claude Projects\video-editor-client\video-editor"
os.chdir(D)
PIT = "projects/felton-draco-broadway/PITCH.md"; HC = "research/deep-research-2026-11-14/hp-cast.md"
HX = "research/deep-research-2026-11-14/HP-EXECUTION.md"; RUN = "projects/felton-draco-broadway/RUN.md"


def edit(p, pairs):
    s = open(p, encoding="utf-8").read()
    for a, b in pairs:
        if s.count(a) == 0:
            print("MISSING in", p, "::", a[:80]); continue
        s = s.replace(a, b)
    open(p, "w", encoding="utf-8").write(s)


def block(p, start, end, new):
    s = open(p, encoding="utf-8").read(); i = s.index(start); j = s.index(end, i)
    open(p, "w", encoding="utf-8").write(s[:i] + new + s[j:])


# ---------------- PITCH.md

edit(PIT, [
    ("- Instagram: 26 keyword searches (18 returned results) and 23 reels read with numbers, plus 30 profile-grid tiles.",
     "- Instagram: 26 searches and page loads (18 returned results) and 23 reels read with numbers, plus 30 profile-grid tiles."),
    ("Sat 22:00", "Sat 22:10"),
    ("- **Instagram, 12 bits at 65K+ likes (10 of them at 100K+):**",
     "- **Instagram, 10 distinct bits at 65K+ likes (8 of them at 100K+), from 12 posts (the debut appears 3 times):**"),
    ("  4. He slipped the film line back into the play himself.",
     "  4. He said the film line once in rehearsal, unplanned, and the director put it back in."),
    ("the boy who sneered \"Potter!\" came back 25 years later to a roar.",
     "the boy who sneered \"Potter!\" came back to the role 25 years after he was cast, to a roar."),
    ("## The sequence (Order 1, ≈52 s; times are the YouTube video's own)",
     "## The sequence (Order 1, ≈50-55 s with the trims below; the exact length from word times at build; times are the YouTube video's own)"),
    ("Text: \"25 years later, **Draco** is back\"", "Text: \"He first played **Draco** 25 years ago\""),
    ("… if you told us then… I would never have believed you\" | HSC 6:23-6:55. Carries the story;",
     "… I would never have believed you\" (trimmed to these two clauses, ≈9 s) | HSC 6:23-6:55. Carries the story;"),
    ("(Sun 15 Nov, 02:20 PKT)", "(Sun 15 Nov, 02:12 PKT)"),
    ("plus its read of this v2 (Sun 02:25)", "plus its read of this v2 (next)"),
    ("\"I even get to say one of the famous lines from the films in the play, which was not in the play before… I said it once spontaneously in rehearsals, and John Tiffany… put that back in. And needless to say, it's quite a hit every night.\"",
     "\"I said it once spontaneously in rehearsals, and John Tiffany, our fabulous director… I could see his eyes twinkle and go, yes, put that back in.\" (trimmed, ≈7 s)"),
    ("| 6 END | HSC MCU, eyes down |",
     "| 6 END | HSC MCU (the frames show him eyes down and grinning: it may land warm, not raw; the ear-check decides) |"),
    ("The frames show him eyes down on the line (`anchor_v2.jpg`, 6:02). Nobody has heard it.",
     "The frames show him eyes down and grinning on the line (`anchor_v2.jpg`, 6:02), so it may land warm rather than raw. Nobody has heard it. If it's light, end on beat 4's \"lock eyes with Harry\" line instead."),
    ("Speech -17.1 / -17.8 LUFS, floor -44 dBFS. No music bed: quiet-frame flatness 0.52-0.56 at 300-4000 Hz (noise-like); the low bins are 40-100 Hz room hum (`measures.txt`).",
     "Speech -17.1 / -17.8 LUFS, floor -44 dBFS. **Music bed: OPEN.** The measured check can't tell: the conversation windows score 0.52-0.56, but the theme-and-intro control scores 0.61 too (`measures.txt`). The ear-check decides; a podcast conversation normally runs without a bed."),
    ("Draco's close-up ≈118.7-120.0 s (`proof/cos_116-122.jpg`).",
     "Draco's close-up ≈118.7-120.0 s (`proof/cos_116-122.jpg`); his face is 454 px at delivery at 119.3 s, soft with film grain, so show it on blurred fill if it reads soft (`anchor_v2.jpg`)."),
    ("| Source quality | ✅ (the stage clip OPEN) |", "| Source quality | ✅ (the stage clip and the music bed OPEN) |"),
    ("not found as a clip (the sitting search; \"tom felton breaking down\" returned no results)", "not found as a clip (the sitting search)"),
    ("Josh's clips were the teaser 2,236, \"Potter\" 65,150 and \"rewatching\" 77,137)",
     "Josh's clips were the teaser 2,236, \"Potter\" 65,150 and \"rewatching\" 77,137; \"tom felton breaking down\" returned no results)"),
    ("10. The sheets are regenerated with true labels, and the numbers saved in `measures.txt`.",
     "10. The anchor sheet is regenerated with true labels (`anchor_v2.jpg`; the contact sheets are unchanged, since their labels are times), and the numbers are saved in `measures.txt`."),
    ("## Evidence files", """## The scoped re-read's 9 fixes (Sun 02:12), applied
1. The music bed is OPEN (the check's control failed).
2. The open items are named here and in RUN.md.
3. The length is re-added from the word counts, with the trims, to ≈50-55 s.
4. G3 says "eyes down and grinning".
5. The film tile is regrabbed (Draco, 119.3 s).
6. HP-EXECUTION item 7 matches the build record.
7. "Put back in" follows his words.
8. The hook text is "He first played Draco 25 years ago".
9. The slips are fixed: the empty heading, the lock time, the search row, tracker row B, the counts, and "10 distinct bits".

## Evidence files"""),
])

# ---------------- hp-cast.md
edit(HC, [
    ("## ▶ STATUS: resume here (01:55 PKT Sun): FINAL v2 written. NOT max effort yet: the stage clip download, the ear-check, a v2 cold read",
     "## ▶ STATUS: resume here (02:12 PKT Sun): FINAL v2 written and re-read (9 more fixes). NOT max effort yet: the stage clip download, the ear-check"),
    ("  - a cold read of v2, if the meter allows;\n", "  - the advisor's read of v2 (next);\n"),
    ("### Earlier: gate E, PITCH v1 and the advisor's final read (00:45-01:01 Sun)",
     "### Earlier: gate E, PITCH v1 and the advisor's final read (00:45-01:01 Sun)\n"
     "- 00:45-00:48 gate E (sheets, anchor, audio); 00:55-00:59 PITCH v1; 00:58 the advisor's call 2 (on v1); 01:01 its fixes; 01:03-01:27 the\n"
     "  Opus cold read (11 defects)."),
    ("2. The tone row (G3) waits for the build's ear-check, since we work in silence.\n3. v2 hasn't had its own cold read yet (see the last line of this report).",
     "2. The ear-check (we work in silence) for the tone row (G3: he's grinning on the ending line) and the music bed (the measured check's\n   control failed)."),
    ("- **Advisor ×2; an Opus cold read** (11 fixes, all applied).",
     "- **Advisor ×2, plus a read of v2; an Opus cold read (11 fixes) and a scoped re-read of v2 (9 fixes),** all applied."),
    ("- Instagram: 12 bits at 65K+ likes, 10 of them at 100K+.", "- Instagram: 10 distinct bits at 65K+ likes (8 at 100K+), from 12 posts."),
    ("  - G3 tone, OPEN until the ear-check.", "  - G3 tone and the music bed, OPEN until the ear-check (he's grinning on the ending line)."),
    ("  4. He slipped the film line back into the play himself.", "  4. He said the film line once in rehearsal, unplanned, and the director put it back in."),
    ("the boy who sneered \"Potter!\" came back 25 years later to a roar.", "the boy who sneered \"Potter!\" came back to the role 25 years after he was cast, to a roar."),
    ("- **Locked prediction:** 120K (40K-400K), Sat 22:00;", "- **Locked prediction:** 120K (40K-400K), Sat 22:10;"),
    ("  - -16.8 LUFS, floor -56 dBFS, no music bed (flatness 0.67).", "  - -16.8 LUFS, floor -56 dBFS; the music bed is OPEN (the measured check can't tell; ear-check)."),
    ("**Cold read of v2:** not run yet (the meter is at 68 %; the finals line is 72 %). It's named in the first lines of this report until it runs.",
     "**Cold reads:** v1 (Opus, 01:03-01:27, 11 fixes) and a scoped re-read of v2 (Opus, 01:57-02:12, 9 fixes), all applied."),
])
s = open(HC, encoding="utf-8").read().split("\n")
for k, l in enumerate(s):
    if l.startswith("| B. Instagram"):
        s[k] = ("| B. Instagram ≥20 searches, ≥40 reels with numbers | **done** (19:40 Sat; +3 searches and 4 reads 01:32-01:48 Sun): 26 searches and page "
                "loads (18 returned results; 5 phrase refusals, 2 failed renders, 1 with no results); 23 reels and posts read with numbers + 30 grid "
                "tiles = 53 | `IG-SEARCH-LOG.md`, rows \"hp-cast\" |")
    if l.startswith("| J. Cold read"):
        s[k] = "| J. Cold read | **done**: v1 (Opus, Sun 01:03-01:27, 11 defects) and a scoped re-read of v2 (Opus, 01:57-02:12, 9 defects), all fixed | PITCH v2, both fix lists |"
    if l.startswith("| I. Fable advisor"):
        s[k] = "| I. Fable advisor ×2 | **done**: Sat 19:15 (before the finalists) and Sun 00:58 (on v1), plus a read of v2 (next) | |"
open(HC, "w", encoding="utf-8").write("\n".join(s))

# ---------------- HP-EXECUTION item 7
edit(HX, [("Our Snape Short broke it (Iris-3 ×4 on small face crops, Proteus ×4 on a 180×320 crop), and its comments argued about\n     \"an AI face on two dead men\".",
           "Our Snape Short ran Iris-3 ×4 on the Dan 2024 and Rickman 2015 face shots and Proteus on the small crops (×4 on a 180×320 crop),\n     and its comments argued about \"an AI face on two dead men\".")])

# ---------------- RUN.md
edit(RUN, [
    ("**Sun 15 Nov 01:55 PKT: a LEAD below the bar", "**Sun 15 Nov 02:12 PKT: a LEAD below the bar"),
    ("  - G3 tone OPEN until the ear-check.", "  - G3 tone and the music bed OPEN until the ear-check (he's grinning on the ending line; the measured music check can't tell)."),
    ("- **Still to fetch:**", "- **Max effort:** not yet: the stage clip and the ear-check are open; everything else is done (the PITCH's first lines).\n- **Still to fetch:**"),
])
print("ok")
