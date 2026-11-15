"""Sun 01:55 v2: apply the cold read's fixes + Affan's framework across hp-cast.md, HP-EXECUTION.md, CLAIMS.md, IG-SEARCH-LOG.md, RUN.md."""
import os
D = r"X:\Claude Projects\video-editor-client\video-editor\research\deep-research-2026-11-14"
os.chdir(D)


def lines(p):
    return open(p, encoding="utf-8").read().split("\n")


def save(p, L):
    open(p, "w", encoding="utf-8").write("\n".join(L))


def block(L, start_prefix, end_prefix, new):
    s = [i for i, l in enumerate(L) if l.startswith(start_prefix)]
    assert len(s) == 1, ("start", start_prefix, len(s))
    e = [i for i, l in enumerate(L) if i > s[0] and l.startswith(end_prefix)]
    assert e, ("end", end_prefix)
    return L[:s[0]] + new.split("\n") + L[e[0]:]


def row(L, prefix, new):
    idx = [i for i, l in enumerate(L) if l.startswith(prefix)]
    assert len(idx) == 1, ("row", prefix, len(idx))
    L[idx[0]] = new
    return L


def sub(s, a, b):
    assert s.count(a) == 1, ("sub", s.count(a), a[:60])
    return s.replace(a, b)


# ---------------- hp-cast.md
p = "hp-cast.md"; L = lines(p)
L = block(L, "## FINAL REPORT", "## Gate tracker (MAX-EFFORT-GATE",
          open(os.path.join("hp-cast", "tools", "final_block_v2.md"), encoding="utf-8").read().rstrip("\n") + "\n")
L = block(L, "## ▶ STATUS", "### Earlier: the downloads were queued", "\n".join([
    "## ▶ STATUS: resume here (01:55 PKT Sun): FINAL v2 written. NOT max effort yet: the stage clip download, the ear-check, a v2 cold read",
    "- **Affan, 01:20 Sun:** keep searching HP with his Paris Jackson method. Confirm a topic with ~12 viral bits, then stitch proven bits",
    "  plus the bits that carry the story. Done for Felton/Draco (`projects/felton-draco-broadway/PITCH.md` v2); Rickman/Snape is the next",
    "  topic (FINAL, \"Next\").",
    "- **The Opus cold read (01:03-01:27) found 11 defects;** all are fixed in v2 (the PITCH lists them).",
    "- **Left:**",
    "  - the hub's download of `DAiOcdPh7wY` (16 s), then probe, frames and audio, then remove the PITCH's \"NOT max effort yet\" line;",
    "  - a cold read of v2, if the meter allows;",
    "  - the ear-check, which is the build's.",
    "### Earlier: gate E, PITCH v1 and the advisor's final read (00:45-01:01 Sun)"]))
L = row(L, "| B. Instagram", "| B. Instagram ≥20 searches, ≥40 reels with numbers | **done** (19:40 Sat; +3 searches and 4 reads 01:32-01:48 Sun) | 26 searches and page loads (18 returned results; 5 phrase refusals, 2 failed renders, 1 with no results); 23 reels and posts read with numbers + 30 grid tiles = 53 | `IG-SEARCH-LOG.md`, rows \"hp-cast\" |")
L = row(L, "| E. Depth on finalists", "| E. Depth on finalists | **done for both, except one file** (v2, 01:50 Sun) | Felton: HSC + debut downloaded and read (row history in § 2a and the gate E results); the Chamber of Secrets film clip is on disk (Draco ≈118.7-120.0 s); the labelled anchor sheet is `proof/anchor_v2.jpg`, with every number in `proof/measures.txt` (music check included). **OPEN:** the stage clip `DAiOcdPh7wY` (the hook and beat 5), waiting on the hub's slot. Rickman: done (card 2). |")
L = row(L, "| G. Variants", "| G. Variants | **done** (v2) | Felton v2: 3 live hooks + 1 dropped, 2 orders, 2 titles + 1 dropped (PITCH v2). Rickman: 2 hooks, 2 orders (§ 2a). |")
L = row(L, "| H. Locked predictions", "| H. Locked predictions | **locked** (Sat 22:10), unchanged | Felton 120K (40K-400K; ~80K is the number I'd defend for v2); Rickman 60K (15K-250K); each with 5K and 5M pre-mortems |")
L = row(L, "| I. Fable advisor", "| I. Fable advisor ×2 | **done**: Sat 19:15 (before the finalists) and Sun 00:58 (on the v1 final; its fixes applied) | |")
L = row(L, "| J. Cold read", "| J. Cold read | **done on v1** (Opus, Sun 01:03-01:27): 11 defects, all fixed in v2. A re-read of v2 is still open (FINAL, first lines) | PITCH v2, \"The cold read's 11 fixes\" |")
L = row(L, "| K. CLAIMS.md", "| K. CLAIMS.md | done: the lane, Rickman, Felton; v2 corrections at 01:55 Sun | `CLAIMS.md` |")
i = [k for k, l in enumerate(L) if l.startswith("## 2a.")][0]
L[i + 1:i + 1] = ["> **Superseded (Sun 01:55) by the FINAL REPORT and `projects/felton-draco-broadway/PITCH.md` v2.** Kept as the trail; where",
                  "> they differ, those two win. hp-films killed its beat B at 22:05, so the \"two Felton Shorts\" flag below is void.", ""]
s = "\n".join(L)
s = sub(s, "turn a week ago (23K)", "turn on 12 Nov (24K)")
s = sub(s, "the channel aired it a week ago", "the channel aired it on 12 Nov")
s = sub(s, "Son Saw His Dad AGAIN 445K)", "Son Saw His Dad AGAIN 445K; 455,396 by 14 Nov)")
s = sub(s, "Son Saw His Dad AGAIN\" (445K)", "Son Saw His Dad AGAIN\" (445K; 455,396 by 14 Nov)")
s = sub(s, "**hp-films needs the same file** for its beat B, so it's one download for both.", "(hp-films killed its beat B at 22:05, so this file is hp-cast's alone.)")
s = sub(s, "hold as #1's hook", "hold as candidate 1's hook (Rickman)")
s = sub(s, "same turn as #1 |", "same turn as candidate 1 (Rickman) |")
open(p, "w", encoding="utf-8").write(s)

# ---------------- HP-EXECUTION.md
p = "HP-EXECUTION.md"; s = open(p, encoding="utf-8").read()
s = sub(s, "Session `hp-cast`, 14 Nov 2026. **v1.3, 22:10 PKT**",
        "Session `hp-cast`, 14-15 Nov 2026. **v1.4, Sun 01:55 PKT** (after an Opus cold read: suspect 1 scoped to its evidence, all 8 comments\n"
        "read, item 7 follows the house Iris rule, the limits updated). **v1.3, 22:10 PKT**")
s = sub(s, "Our Snape Short drew \"you are imposing an AI face on two\n     dead men\"", "Our Snape Short drew \"you are imposing an AI face on two\n     dead men\"") if "Our Snape Short drew \"you are imposing an AI face on two\n     dead men\"" in s else s
s = sub(s, "**Comments:** read through the API at 21:45 (3 of the 8 threads counted; see suspect 1).",
        "**Comments:** all 8 read through the API (3 threads Sat 21:45, the 5 replies Sun 01:45); 7 of them argue about whether the picture is AI\n(suspect 1).")
L = s.split("\n")
L = block(L, "- **YouTube pages are still blocked**", "- **No Studio data.**", "\n".join([
    "- **YouTube was blocked until 23:13 Sat** (the hub cleared it).",
    "  - The numbers and comments here come from the Data API, and only our finalists' sources were downloaded.",
    "  - So nobody on our side has watched the first 2 s of the winners. Their openings are judged from titles, descriptions, lengths and the",
    "    same clips on Instagram."]))
L = block(L, "1. **The picture read as AI", "2. **The hook sold one story", "\n".join([
    "1. **Viewers read the faces of the two late actors as AI (new in v1.3, scoped in v1.4; the only direct viewer evidence we have).**",
    "   - **The comments:** all 8 are read (the API: 3 threads Sat 21:45, the 5 replies Sun 01:45). 7 of the 8 argue about whether the picture is AI.",
    "     - \"have some respect, you are imposing an AI face on two dead men\" (12 Nov, 2 likes). Under it: \"half this content is ai…\" and \"you",
    "       dont see the mangled faces\".",
    "     - The other side: \"This short isnt ai (neither voices nor videos), but youtube puts an ai upscale folter on each YT video…\" (13 Nov,",
    "       6 likes), and two replies blaming YouTube's upscaling. One reply asks \"Whats the Ai part\".",
    "   - **What the build did** (`projects/harry-potter-prank/RUN.md`, `REPORT.md`):",
    "     - Topaz Iris-3 ×4 on the face shots of Dan 2024 (the opening frame) and Rickman 2015;",
    "     - the Gambon shots got Proteus, not Iris (REPORT.md);",
    "     - Proteus ×2 plus a 0.5× Chronos slow-mo on the hook's Snape close-ups;",
    "     - Proteus ×2-×4 on the SD featurette and the dailies, and Proteus ×4 on the 612 % push (a 180×320 crop).",
    "",
    "     Its own notes say Iris \"invents a waxy face\" on small crops, and that Proteus ×4 once turned the dailies \"plastic\".",
    "   - **The quality cliff belongs here (v1.2's suspect 2):** 0-4.7 s is HD, then a 480p 4:3 picture for 51 % of the runtime. The",
    "     Instagram prank reels ran the same SD untouched, sold as the real take, and it didn't stop them.",
    "   - **Why it may cost views:** a viewer who thinks the faces are fake stops trusting the story, and these are the faces of two actors who",
    "     have died. It's a suspect, not a proven cause (§ 6).",
    "   - **The house rules already cover it:**",
    "     - stills (14 Nov): never upscale a real person's face from a soft source; Lanczos only;",
    "     - footage (LESSONS, 14 Nov, the Speed review): \"Iris only where a face is large in frame. A wide or a downscale gets no generative",
    "       enhancement.\" Affan called the Speed Short's Iris letterboxes \"pasty AI-ish\", and the fix was Chronos only. That's a related",
    "       complaint about the same family of tools, this time from the creator.",
    "   - **Test:** a retention step in the first 2 s or at 4.7 s, and the comment mix as views grow. Eight comments are a tiny sample."]))
L = block(L, "7. **No quality cliff in the first 10 s", "8. **If each half", "\n".join([
    "7. **No quality cliff in the first 10 s, and no AI faces.** SD stays at 25 % of the runtime or less, unless the whole Short IS that",
    "   footage and is sold as the real take.",
    "   - **Follow the house rule (LESSONS, 14 Nov, Speed): \"Iris only where a face is large in frame. A wide or a downscale gets no generative",
    "     enhancement.\"** Our Snape Short broke it (Iris-3 ×4 on small face crops, Proteus ×4 on a 180×320 crop), and its comments argued about",
    "     \"an AI face on two dead men\".",
    "   - Never Proteus ×4 on SD. Use Lanczos, show SD smaller and honest (framed, as the real take), or find an HD source.",
    "     PITCH-CHECKLIST §2's anchor recipe runs Iris 1.0 on large faces, which the rule allows.",
    "   - Check the faces at full size before export."]))
save(p, L)

# ---------------- CLAIMS.md and IG-SEARCH-LOG.md
with open("CLAIMS.md", "a", encoding="utf-8") as f:
    f.write("| Sun 01:55 | hp-cast | CORRECTION: the Felton lead, v2 | Rebuilt on Affan's 01:20 framework (topic test passed: 58 YouTube bits at 1M+, 12 Instagram bits at 65K+). The hook is the stage \"Scared, Potter?\" (IG 1,218,486 likes / 189,314 shares; YT 3,669,646). The 01:01 row's hp-films beat B link is void (beat B was killed at 22:05). The \"his tears\" wording is withdrawn: he says he stops himself breaking down | lead (v2) |\n")
    f.write("| Sun 01:55 | hp-cast | Rickman / Snape (the topic) | Passes the 12-bit test on YouTube (41 at 1M+). A stitched \"scariest teacher, kindest man\" is the next HP build to research. Not yet claimed for a build | lead (topic) |\n")
with open("IG-SEARCH-LOG.md", "a", encoding="utf-8") as f:
    for r in [
        "| 01:32 | hp-cast | keyword \"tom felton happy sad confused\" | grid of 24 | joshuahorowitz DWUt9bzES68 / DWeXt_0Ecae / DWbaDQZEd0M / DV37gi6kbTe; fan DdgZF0zCu4j (\"INTERVIEW 2026 HAPPY SAD CONFUSED…\"); the rest untitled |",
        "| 01:33 | hp-cast | keyword \"tom felton breaking down\" | no results | - |",
        "| 01:37 | hp-cast | an in-page read of the search API | refused by the permission layer; not retried (the /p/ method used instead) | - |",
        "| 01:38 | hp-cast | post @joshuahorowitz DWUt9bzES68 | /p/ embedded JSON | 2,236 likes / 71 comments / 143 shares; 25 Mar 2026; the HSC episode teaser |",
        "| 01:39 | hp-cast | post @joshuahorowitz DWeXt_0Ecae | /p/ embedded JSON | **77,137 likes / 1,314 comments / 5,340 shares**; 29 Mar 2026; \"Tom Felton isn't rewatching HARRY POTTER for a good reason\" |",
        "| 01:40 | hp-cast | post @joshuahorowitz DWbaDQZEd0M | /p/ embedded JSON | **65,150 likes / 486 comments / 7,105 shares**; 28 Mar 2026; \"Tom Felton on the creation of his iconic 'Potter!'\" |",
        "| 01:47 | hp-cast | keyword \"tom felton scared potter\" | grid of 5 | DRC5XI-kYEX, DRDNRDCiWvH, DRkHquBEkaW, DVIf5evjYzi, DRD8MINDwnV |",
        "| 01:48 | hp-cast | reel @cursedchildus DRC5XI-kYEX | /p/ embedded JSON | **1,218,486 likes / 4,368 comments / 189,314 shares**; 14 Nov 2025; \"The 'Scared, Potter?' heard around the wizarding world\" |"]:
        f.write(r + "\n")

# ---------------- RUN.md (rewritten)
open(os.path.join("..", "..", "projects", "felton-draco-broadway", "RUN.md"), "w", encoding="utf-8").write("""# RUN: felton-draco-broadway (AW Short lead, "Tom Felton Almost Broke Down"), v2

## ▶ STATUS: resume here
**Sun 15 Nov 01:55 PKT: a LEAD below the bar, written up as a full PITCH v2 by research session `hp-cast` (PITCH.md). It is not a pick.**
- **Gates:**
  - locked 120K, under the 150K bar; ~80K is the number I'd defend;
  - Judgment OPEN (he reverses the persona, not the ovation moment);
  - G3 tone OPEN until the ear-check.
- **Building it is Affan's call.** Nothing is built.
- **Sources:**
  - Downloaded via pace.sh, in `research/deep-research-2026-11-14/hp-cast/src/`:
    - `yt_felton_hsc/`: HSC `pSWIM3Tc9y0`, sections 0:00-13:00 and 25:30-33:00, 1080p23.976;
    - `yt_felton_debut/`: `Ug1vk4ve2h8`, 1080p25.
  - On disk: the film clip `projects/harry-potter-prank/src/snape/Wizard Duel_ … Chamber of Secrets.mp4`, 1080p (Draco ≈118.7-120.0 s).
  - Intake copies them into `raw/` (never move them).
- **Still to fetch:** the stage clip `DAiOcdPh7wY` (16 s), for the hook and beat 5, in the hub's order. Fallback: Hook B, all on disk.
- **Constraints for the build:**
  - Lanccos only, no Topaz: the faces pass the anchor test raw (house rule: Iris only where a face is large in frame);
  - never tie his "breaking down" line to the ovation (asked about it, he says "For me, not really"); keep Josh's whole "night after
    night" question;
  - skip the debut clip's 0-5 s; Felton's face is 138 px at delivery in a full-height crop;
  - cut before "Yeah, kind of" in beat 6;
  - ear-check every line (the research worked in silence).
- Premiere untouched.
""".replace("Lanccos", "Lanczos"))
print("ok")
