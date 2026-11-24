import sys
sys.stdout.reconfigure(encoding="utf-8")
base = "X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/"
p = base + "SEQUENCE.md"
s = open(p, encoding="utf-8").read()
i0 = s.index("## 4. Locked prediction"); i1 = s.index("## 5. Variants compared")
s = s[:i0] + """## 4. Locked predictions, side by side (re-locked 19 Nov 20:40 machine clock)
**Why re-locked:** v2's 50K was centred on a stale base, AW's newest-30 median of 50K read on 14 Nov. The live channel, read through the API at 20:30, says otherwise (`api/aw-recent.json`):
- the newest-30 median is **93.5K**;
- the GTA 5 farewell ("Saying Goodbye To GTA 5 💖🥹", posted 18 Nov 11:06) is at **298,365 views in 28 h, about 10.7K/h**, the fastest of the recent Shorts (MJ Best Dad 480K in 65 h, Oldman 330K in 61 h);
- I predicted that farewell at 45K, so my GTA calls have run about 6x low. One data point, but a large miss.

| | **Bigfoot (PICK)** | **Jet theft (runner-up)** |
|---|---|---|
| Most likely | **120K** | **90K** |
| 50 % range | 40K-400K | 30K-300K |
| 1M+ | about 15 % | about 10 % |
| Under 10K | about 8 % | about 10 % |
| For it | the GTA lane is AW's fastest; Instagram shares are growing ~10x faster than the jet's; three big faces; a built-in reversal | YouTube's GTA 6 feed is hottest on it: about 11 % of its videos at 100K+, against about 2 % for Bigfoot |
| Against it | YouTube Shorts are cold on Bigfoot: same-day "streamers found Bigfoot" Shorts sit at 1-2K, and the best Short is 153K | **the PITCH-CHECKLIST § 3 entry tax:** Typical Gamer's own Short of the same moment is at 2.35M, so our compilation re-cuts the clip the feed has already served; only 2 faces; no turn |
| 5K pre-mortem | posted on day 3, after Afterhours' long-form and the clip channels; the small cams read as filler | the feed treats it as a re-upload of Typical Gamer's Short |
| 5M pre-mortem | "that's literally Bigfoot" becomes the comment war under the skunk-ape line, shared like the 226K-share reel | the military-chase spectacle travels to non-gamers like the 15.5M "POV: you stole a jet" reel |

Both are below the 150K bar; see the first line.

""" + s[i1:]
R = [
("- The 16:9 stream frame sits in the 9:16 with a blurred fill. Beat 3 uses README § 13's stacked split (game on top, the cam enlarged below), because summit1g's face is the beat there.",
 "- The 16:9 stream frame sits in the 9:16 with a blurred fill, with every face cam left as an inset at its stream size. **No stacked split:** the anchor test failed it (below)."),
("**Face cams at source:** Fanum about 420 px wide of 1920; summit1g about 680 of 2560; xQc about 370 of 1920. They will be soft when enlarged (no Iris on small faces), so only summit1g's is enlarged.",
 "**Face cams, the anchor test** (`frames/anchor_compare.jpg`, `tools/anchor.py`: the same face region at delivery scale against the approved Prince ABC panels P7 and P8):\n- Faces at delivery: Fanum 67 px wide; summit1g 50 px as an inset, 165 px if enlarged into a split; xQc about 45 px (too small for the detector). Prince: 772-883 px.\n- **Verdict: below the Prince anchor at any enlargement. FAIL for a face-led beat.** The enlarged summit1g split is visibly soft.\n- As small insets, the cams read as \"a streamer reacting\", which is how streamer-reaction Shorts show them (Typical Gamer's 2.35M Short keeps its cam inset). The picture that carries the Short is the game footage (1080p-1440p), not the faces.\n- **This is a source-quality gate failure, named, under the exception.**"),
("| 3 | 0:09.0-0:13.4 | same file 32.9-37.3 (edges to re-measure: the ASR timing is smeared) | Jason drops, the screen blurs, he lies in the plants. **Stacked split:** summit1g's face below |",
 "| 3 | 0:09.0-0:13.4 | same file 32.9-37.3 (edges to re-measure: the ASR timing is smeared) | Jason drops, the screen blurs, he lies in the plants; summit1g's cam inset (no split: the anchor test failed it) |"),
("**Weakest, named first:**\n- The jet beats it on the brief's own YouTube metric.\n- The face cams are small, and the anchor test was not done.",
 "**Weakest, named first:**\n- Below the 150K bar: 120K centre, under the exception.\n- The jet beats it on the brief's own YouTube metric.\n- The face cams FAIL the Prince anchor test; they are used only as small insets."),
("| Source quality | PASS (picture) · WEAK (cams; anchor test not done) · OPEN (audio by ear) |",
 "| Source quality | PASS (picture) · **FAIL (cams vs the Prince anchor: faces 45-67 px at delivery; insets only)** · OPEN (audio by ear) |"),
]
for a, b in R:
    if a not in s: print("MISSING:", a[:70])
    s = s.replace(a, b)
open(p, "w", encoding="utf-8").write(s)
print("ok")
