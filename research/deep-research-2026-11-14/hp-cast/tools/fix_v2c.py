"""Sun 02:16: the advisor's read of v2 - drop beat 5 (the added line is never named), titles-only topic counts, a fallback title,
honest stamps, a CLAIMS correction. Reports every pattern it can't find instead of stopping."""
import os
D = r"X:\Claude Projects\video-editor-client\video-editor"
os.chdir(D)
PIT = "projects/felton-draco-broadway/PITCH.md"; HC = "research/deep-research-2026-11-14/hp-cast.md"; RUN = "projects/felton-draco-broadway/RUN.md"


def edit(p, pairs):
    s = open(p, encoding="utf-8").read()
    for a, b in pairs:
        if s.count(a) == 0:
            print("MISSING in", p, "::", a[:90]); continue
        s = s.replace(a, b)
    open(p, "w", encoding="utf-8").write(s)


def drop_line(p, startswith):
    L = open(p, encoding="utf-8").read().split("\n"); n = len(L)
    L = [l for l in L if not l.startswith(startswith)]
    if len(L) == n:
        print("NO LINE in", p, "::", startswith[:60])
    open(p, "w", encoding="utf-8").write("\n".join(L))


# ---------------- PITCH.md
drop_line(PIT, "| 5 | Stage clip again, wide |")
drop_line(PIT, "  4. He said the film line once in rehearsal, unplanned, and the director put it back in.")
edit(PIT, [
    ("  5. Asked whether feeling that love night after night", "  4. Asked whether feeling that love night after night"),
    ("| 6 END |", "| 5 END |"),
    ("## The story (one arc: 4 proven bits + 2 that carry it)", "## The story (one arc: 3 proven bits + 2 that carry it)"),
    ("with the trims below; the exact length", "after the trims and with beat 5 dropped: ≈43-48 s; the exact length"),
    ("(Order 1, ≈50-55 s after the trims and with beat 5 dropped", "(Order 1, after the trims and with beat 5 dropped"),
    ("- **Not tied to the ovation:** the confession comes after beat 5, never straight after the ovation. It keeps Josh's \"night after night\"\n  question,",
     "- **Not tied to the ovation:** the confession follows the ovation, but on the HSC picture and with Josh's whole \"night after night\"\n  question kept,"),
    ("the hook is the film shot → HSC beat 2, and beat 5's telling plays over the HSC MCU.", "the hook is the film shot → HSC beat 2."),
    ("The hook's mystery (why is he saying the film line on stage?) pays off at beat 5, then the confession closes.",
     "The line then and now in the first 3 s, the return in his words, and the confession to close."),
    ("film → origin → dwindle → ovation → the stage line and how it got in → the confession.", "film → origin → dwindle → ovation → the stage line → the confession."),
    (" → the ovation → how the line got back in → the confession, each in its own context)", " → the ovation → the confession, each in its own context)"),
    ("| 5 how the line got back in | see beat 1 (same stage moment) | see beat 1 | - |",
     "| (dropped 02:16) how the line got back in | his telling never names the line, and the stage clip's 100 comments don't either | - | so \"Scared, Potter?\" isn't claimed as the line he added |"),
    ("| 6 the confession |", "| 5 the confession |"),
    ("cut before \"Yeah, kind of\" in beat 6", "cut before \"Yeah, kind of\" in beat 5"),
    ("58 videos at 1M+ (79 at 500K+) match Felton/Draco among the 7,102 cached HP videos (`hp-cast/topic_counts.txt`).",
     "46 videos at 1M+ (60 at 500K+) have Felton/Draco in the title among the 7,102 cached HP videos (58 if descriptions count; `hp-cast/topic_counts.txt`)."),
    ("For scale: Radcliffe 45, Rickman/Snape 41, Watson 27, Emma + Tom 17.", "For scale, titles only: Rickman/Snape 29, Radcliffe 23, Watson 14."),
    ("(true per the episode's description: he was cast in 2000; it holds the payoff back)",
     "(true per the episode's own description, \"25 years after first playing Draco Malfoy\"; it holds the payoff back)"),
    ("  - \"Draco's Return Nearly Broke Him\" (runner-up).",
     "  - \"Draco's Return Nearly Broke Him\" (runner-up).\n  - If the ear-check finds the ending light: **\"Draco Never Saw This Coming\"** (his words: \"I would never have believed you\"); it promises no tears."),
    ("plus its read of this v2 (next)", "plus its read of this v2 (Sun 02:13, a third call)"),
    ("## Evidence files", """## The advisor's read of v2 (Sun 02:13), applied
1. **Beat 5 is dropped.** He says "one of the famous lines from the films" and never names it, and the stage clip's 100 comments don't
   say either. So the Short doesn't claim "Scared, Potter?" is the line he added. The hook stands on its own: he says it on stage in the
   production's clip.
2. **The topic counts use titles only:** Felton/Draco 46, Rickman/Snape 29.
3. **A fallback title** that promises no tears.
4. **CLAIMS is corrected,** and the stamps come from the clock.

## Evidence files"""),
])

# ---------------- hp-cast.md
edit(HC, [
    ("- YouTube: 58 videos at 1M+ (79 at 500K+) in the cached set.", "- YouTube: 46 videos at 1M+ (60 at 500K+) with Felton/Draco in the title, in the cached set (58 if descriptions count)."),
    ("- Rickman/Snape passes too, with 41 YouTube videos at 1M+ (see \"Next\").", "- Rickman/Snape passes too, with 29 YouTube titles at 1M+ (see \"Next\")."),
    ("  4. He said the film line once in rehearsal, unplanned, and the director put it back in.\n  5. \"I have to think", "  4. \"I have to think"),
    ("- **Rickman/Snape also passes the 12-bit test,** with 41 YouTube videos at 1M+:", "- **Rickman/Snape also passes the 12-bit test,** with 29 YouTube titles at 1M+ (41 if descriptions count):"),
    ("  - the advisor's read of v2 (next);\n", "  - the advisor's read of v2 is done (02:13, a third call): beat 5 dropped, titles-only counts, a fallback title;\n"),
    ("plus a read of v2 (next)", "plus a read of v2 at 02:13 (a third call; its fixes applied)"),
    ("  - Titles: \"Tom Felton Almost Broke Down\" (pick) and \"Draco's Return Nearly Broke Him\".",
     "  - Titles: \"Tom Felton Almost Broke Down\" (pick) and \"Draco's Return Nearly Broke Him\"; if the ending lands light, \"Draco Never Saw This Coming\"."),
])
edit(RUN, [("cut before \"Yeah, kind of\" in beat 6", "cut before \"Yeah, kind of\" in beat 5")])

with open("research/deep-research-2026-11-14/CLAIMS.md", "a", encoding="utf-8") as f:
    f.write("| Sun 02:16 | hp-cast | CORRECTION to hp-cast's 01:01 and 01:55 rows | The 01:01 rows (stamped 02:05) were written at 01:01. "
            "The topic counts on titles only: Felton/Draco 46 at 1M+ (58 counted descriptions); Rickman/Snape 29 (41). Instagram is 10 distinct bits "
            "at 65K+ from 12 posts, not \"12 bits\". \"Scared, Potter?\" is NOT confirmed as the line Felton added to the play (he never names it), so "
            "that beat is dropped | correction |\n")
print("ok")
