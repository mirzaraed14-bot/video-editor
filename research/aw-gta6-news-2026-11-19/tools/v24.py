import sys
sys.stdout.reconfigure(encoding="utf-8")
base = "X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/"
p = base + "SEQUENCE.md"
s = open(p, encoding="utf-8").read()
# 1. top block
i1 = s.index("v2 applies the cold read")
s = """# AW GTA 6 news Short: "Bigfoot Is In GTA 6 😳" (sequence v2.4, 19 Nov 2026; nothing built)

> **BELOW THE USUAL BAR.** Both moments centre at about **90K**, against AW's 150K bar (AW's live newest-30 median is 93.5K).
> - No measured factor separates them (§ 4), so the choice between them is **fit, not forecast**.
> - **Held strictly to the bar, this route gives NO PICK.**
> - **The exception (PITCH-CHECKLIST), named first, for building Bigfoot tonight anyway:**
>   - you asked for this GTA 6 news Short today;
>   - GTA content is doing well on AW right now: "Saying Goodbye To GTA 5 💖🥹" has 298K views in 28 h;
>   - launch week is a one-time window;
>   - the upside tail: about 10 % for 1M+.

""" + s[i1:]
R = [
("v2.3 closes the hub's open gate items (20:20-20:45): Instagram per streamer, 6 more YouTube phrasings, the anchor test, Kai, the jet prediction and the bar line.",
 "v2.3 closes the hub's open gate items (20:20-20:45): Instagram per streamer, 6 more YouTube phrasings, the anchor test, Kai, the jet prediction and the bar line. v2.4 applies Fable's review of v2.3: both predictions on one rule, the tried join named as a weakness, absence claims softened, and cold read 3."),
("3. **Kai Cenat is not placed in his stream.** No Twitch clip of the moment exists (98 clips over 7 days checked), and the hub said not to pull his 19-hour VOD. He stays out of the cut (Q5).",
 "3. **Kai Cenat is not placed in his stream.** None found by title or by first frame in his 7-day Twitch clip list (77 clips since 18 Nov; the list may be capped). The hub said not to pull his 19-hour VOD. He stays out of the cut (Q5)."),
("  - **Nobody has the \"it's not Bigfoot\" angle in a Short.**",
 "  - No \"it's not Bigfoot\" title found in 3 phrasings."),
("  - On the final (about 20:07): its four fixes are applied in v2.1.",
 "  - On the final (about 20:07): its four fixes are applied in v2.1.\n  - On v2.3 (about 20:44): its four blocking fixes are applied in v2.4."),
("- **Cold read:** done (`COLD-READ.md`); every must-fix is applied below.",
 "- **Cold reads:** 1 on v1 (`COLD-READ.md`), 2 on v2.1 (`COLD-READ-2.md`), 3 on v2.4 (`COLD-READ-3.md`). Each one's fixes are applied."),
("| **Famous streamers with the moment on frame, mid-clip** | **Kai Cenat** (on an Instagram re-up of his Twitch stream: his cam, the glowing creature, \"Run! We're the prey! Run!\"), **xQc, summit1g, Fanum** (plus Brendaniel's voice, HutchMF's aftermath, frizzeyes) | Typical Gamer, ohnePixel |",
 "| **Famous streamers with the moment on frame, mid-clip** | **xQc, summit1g, Fanum** (plus Brendaniel's voice, HutchMF's aftermath and frizzeyes; Kai Cenat only on an Instagram re-up, not in the cut) | Typical Gamer, ohnePixel |"),
("- **I pick Bigfoot for this format:**", "- **I pick Bigfoot for this format. This is fit, not forecast: § 4 centres both at about 90K.**"),
("- **The cost:** Bigfoot is cold on YouTube Shorts. Day-1 multi-streamer Bigfoot compilations there sit at 0.9K-1.9K views.",
 "- **The cost:** Bigfoot is cold on YouTube Shorts, and **the streamer + Bigfoot join was already tried today and stayed low**.\n  - About 8 same-day YouTube Shorts sit at 0.9K-1.9K; the exceptions are the CaseOh fan clip (153K) and Swagg's own Short (40K).\n  - 5 Kai Cenat re-ups on Instagram have 0-33 likes.\n  - The faces are a bet. The measured case is the creature's own reach plus the ending."),
("- Captions sit just under the lips, AW rules (F*CK). Game characters' lines are captioned in italics with a small `GTA 6` tag.",
 "- **Captions:** \"just under the lips\" can't apply to 45-67 px insets, so they sit in the band under the game frame (AW labels-low rule: above y1620), AW rules (F*CK). Game characters' lines are in italics with a small `GTA 6` tag."),
("- As small insets, the cams read as \"a streamer reacting\", which is how streamer-reaction Shorts show them (Typical Gamer's 2.35M Short keeps its cam inset). The picture that carries the Short is the game footage (1080p-1440p), not the faces.",
 "- As small insets, the cams read as \"a streamer reacting\". The picture that carries the Short is the game footage (1080p-1440p), not the faces."),
("About 2-3 hours: the AW template, captions, labels, blurs, one split and the CTA.",
 "About 2-3 hours: the AW template, captions, labels, blurs/plates (no split) and the CTA."),
("| G4 Freshness | PASS for our join |", "| G4 Freshness | **WEAK: the join was tried today and stayed low** |"),
("same-day YouTube \"streamers found Bigfoot\" Shorts: Dropy 1.9K, Komnt 1.5K, TurkishProduction 1.2K, GTA Updates 0.9K.",
 "same-day YouTube \"streamers found Bigfoot\" Shorts: Dropy 1.9K, Komnt 1.5K, TurkishProduction 1.2K, GTA Updates 0.9K, plus about 4 more under 1K. Exceptions: CaseOh fan clip 153K, Swagg's own Short 40K. 5 Kai re-ups on Instagram at 0-33 likes. Only our version has the skunk-ape turn."),
("**Weakest, named first:**\n- Below the 150K bar: 120K centre, under the exception.",
 "**Weakest, named first:**\n- Below the 150K bar: about 90K centre, under the exception.\n- The streamer + Bigfoot join was tried today and stayed low (G4)."),
("| IG first filter | PASS (creature + knock-out) · WEAK (skunk-ape beat) · **WEAK (per streamer)** |",
 "| IG first filter | PASS (creature + knock-out) · WEAK (skunk-ape beat) · **WEAK (per streamer; pass 2 read likes and comments only, not shares or views)** |"),
("2. Hold to the 150K bar (no pick tonight), or build under the exception (§ 4: Bigfoot 120K, jet 90K)?",
 "2. Hold to the 150K bar (no pick tonight), or build Bigfoot under the exception (§ 4: both about 90K)?"),
]
for a, b in R:
    if a not in s: print("MISSING:", a[:80])
    s = s.replace(a, b)
# 4. predictions
i0 = s.index("## 4. Locked predictions"); i1 = s.index("## 5. Variants compared")
s = s[:i0] + """## 4. Locked predictions, side by side, on one rule (re-locked 19 Nov ~20:50 machine clock; replaces v2.3's 120K / 90K)
**The rule:** start from AW's live newest-30 median, **93.5K** (API, 20:30, `api/aw-recent.json`). Move a moment off it only for a factor measured today.

| Factor (measured) | Bigfoot | Jet theft | Net |
|---|---|---|---|
| YouTube topic heat (share of its videos at 100K+) | 5 of 225 (2 %) | 21 of 194 (11 %) | jet + |
| Entry tax (prior 100K+ Shorts of the same moment) | 3 Shorts at 113K-153K (CaseOh fan clip, LazarLazar, DarkViperAU) | Typical Gamer's own Short of the exact clip, 2.35M | Bigfoot + |
| The streamer-compilation join, tried today | about 8 Shorts at 0.9K-1.9K; exceptions 153K and 40K | about 5 at 0-20K ("GTA 6 Sent Fighter Jets After ohnePixel's Stolen Plane" 20K) | even |
| Instagram share velocity (top reel, its own window) | +41.5K shares in about 5.7 h | +3.1K in about 4.3 h | Bigfoot + |
| Instagram top-reel views | 13.7M | 15.5M | jet + |

These offset, and none is measured strongly enough to move one moment far from the other. **So both centre at the median.** The pick is fit (a reversal ending; three big faces on frame), not forecast.
- The GTA 5 farewell (298K in 28 h) is another session's story Short. It shows GTA content isn't penalised on AW; it does not calibrate this format, so it moves neither centre.

| | **Bigfoot (PICK)** | **Jet theft (runner-up)** |
|---|---|---|
| Most likely | **90K** | **90K** |
| 50 % range | 30K-300K | 30K-300K |
| 1M+ | about 10 % | about 10 % |
| Under 10K | about 10 % | about 10 % |
| 5K pre-mortem | it lands like today's streamer-Bigfoot Shorts (1-2K); the small cams read as filler | the feed treats it as a re-upload of Typical Gamer's 2.35M Short |
| 5M pre-mortem | "that's literally Bigfoot" becomes the comment war under the skunk-ape line, shared like the 226K-share reel | the military-chase spectacle travels to non-gamers like the 15.5M "POV: you stole a jet" reel |

Both are below the 150K bar; see the first line.

""" + s[i1:]
open(p, "w", encoding="utf-8").write(s)
print("ok")
