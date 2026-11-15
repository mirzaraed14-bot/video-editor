"""02:05 fixes after the advisor's final read: hp-cast.md FINAL block, status, rows G/I, gate E paragraph; RUN.md; HP-EXECUTION item 7; CLAIMS rows."""
import os
D = r"X:\Claude Projects\video-editor-client\video-editor\research\deep-research-2026-11-14"
os.chdir(D)


def edit(p, pairs):
    s = open(p, encoding="utf-8").read()
    for a, b in pairs:
        n = s.count(a)
        assert n == 1, (p, n, a[:70])
        s = s.replace(a, b)
    open(p, "w", encoding="utf-8").write(s)


FINAL = open(os.path.join(D, "hp-cast", "tools", "final_block.md"), encoding="utf-8").read()
p = "hp-cast.md"
s = open(p, encoding="utf-8").read()
i, j = s.index("## FINAL REPORT"), s.index("## Gate tracker (MAX-EFFORT-GATE")
s = s[:i] + FINAL + "\n" + s[j:]
open(p, "w", encoding="utf-8").write(s)

edit(p, [
    ("- **Felton PITCH:** `projects/felton-draco-broadway/PITCH.md` + `RUN.md`. New since 22:15: the official clip's top comments\n"
     "  (\"HE'S TRYING SO HARD NOT TO SMILE\", 8,766 likes) give the Judgment row; he reverses it in his own voice (\"…to prevent myself\n"
     "  from breaking down\"). Hook D and the title \"Draco Wasn't Hiding A Smile\" follow from it.",
     "- **Felton, a LEAD below the bar** (locked 120K, under 150K), written up as a full PITCH: `projects/felton-draco-broadway/PITCH.md` +\n"
     "  `RUN.md`. The Judgment row is OPEN: viewers read a smug grin, and he reverses the persona but not the moment (\"For me, not really\").\n"
     "  Pick: Hook A + Order 1, title \"Tom Felton Almost Broke Down\" (Hook D dropped at 02:00 after the advisor)."),
    ("| G. Variants | **done** (22:10; +2 Felton hooks at 01:15) | Felton: 4 hooks (A-D), 2 orders, pick D + Order 1, title pick changed to \"Draco Wasn't Hiding A Smile\" after the comments (PITCH); Rickman: 2 hooks, 2 orders (§ 2a) |",
     "| G. Variants | **done** (22:10; +2 Felton hooks at 01:15) | Felton: 4 hooks (A-D), 2 orders. Pick A + Order 1, title \"Tom Felton Almost Broke Down\"; D was dropped at 02:00 because his words don't tie his tears to the ovation (PITCH). Rickman: 2 hooks, 2 orders (§ 2a) |"),
    ("| I. Fable advisor ×2 | 1 of 2 done (19:15, before the finalists) | |",
     "| I. Fable advisor ×2 | **done**: 19:15 (before the finalists) and 01:50 Sun (on the final; its fixes are applied: Hook D dropped, Judgment OPEN, Iris scoped, CLAIMS rows) | |"),
    ("- **Judgment evidence** (API comments on `Ug1vk4ve2h8`, 1 unit):",
     "- **The viewers' reading** (API comments on `Ug1vk4ve2h8`, 1 unit). He reverses the persona, not the moment: asked about the ovation, he\n"
     "  says \"For me, not really\".\n"
     "  - \"Love that smug smirk he gave to Potter, he finally outshined him\" 4,226 likes;"),
])

edit(os.path.join("..", "..", "projects", "felton-draco-broadway", "RUN.md"), [
    ("# RUN: felton-draco-broadway (AW Short candidate, \"Draco Wasn't Hiding A Smile\")",
     "# RUN: felton-draco-broadway (AW Short lead, \"Tom Felton Almost Broke Down\")"),
    ("  - no Topaz Iris on faces; Lanczos only (the HSC faces pass the anchor test raw);",
     "  - Lanczos only: the HSC faces pass the anchor test raw, so no Topaz is needed (Iris is for the hub to settle; see PITCH flags);\n"
     "  - never claim his tears were at the ovation: asked about it, he says \"For me, not really\";"),
])

edit("HP-EXECUTION.md", [
    ("   - **Never run Topaz Iris on a real face, and never Proteus ×4 on SD.** Our Snape Short drew \"you are imposing an AI face on two\n"
     "     dead men\", and Affan called the Speed Short's Iris passes \"pasty AI-ish\" (14 Nov). Chronos alone (frame timing, no new\n"
     "     detail) passed his review.",
     "   - **Never Proteus ×4 on SD. Our recommendation: skip Iris on a real face wherever Lanczos passes the anchor test.**\n"
     "     - Our Snape Short drew \"you are imposing an AI face on two dead men\".\n"
     "     - Affan called the Speed Short's Iris letterboxes \"pasty AI-ish\" (14 Nov), and the fix was Chronos only.\n"
     "     - **A conflict for the hub to settle:** PITCH-CHECKLIST §2's anchor recipe (the Son ABC recipe) uses Iris 1.0, and the approved\n"
     "       Prince panels are Iris-finished."),
])

with open("CLAIMS.md", "a", encoding="utf-8") as f:
    f.write("| Sun 02:05 | hp-cast | HP cast as people (the lane) | NO PICK: nothing clears the 150K-center / 1M-top bar; 2 leads below it | no pick |\n")
    f.write("| Sun 02:05 | hp-cast | Tom Felton: Broadway Draco ovation (`Ug1vk4ve2h8`) + HSC 26 Mar 2026 confession (`pSWIM3Tc9y0`) | "
            "LEAD below the bar (locked 120K, ~60K re-based); full PITCH at projects/felton-draco-broadway/PITCH.md; Judgment OPEN "
            "(his tears aren't tied to the ovation: \"For me, not really\"); shares one download with hp-films beat B | lead |\n")
    f.write("| Sun 02:05 | hp-cast | Gary Oldman on Rickman's set visitors (TIFF, `tVm7ajSlOIU`) | LEAD card below the bar (60K); "
            "G4: our sequence exists (Horowitz 1.2M) | lead (card) |\n")
print("ok")
