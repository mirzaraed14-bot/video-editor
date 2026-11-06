# BRIEF: melanin-3-escalators (Onyx batch 7, Melanin Money "3 Escalators To Wealth")

▶ STATUS 2026-11-06, Affan's review 1 applied (`../_onyx-batch7-2026-11/review1.py`, YT look only; picture cuts, MGs and mix NOT rebuilt; old final = outputs/melanin-3-escalators.sample-yt.before-r1.mp4, old spec = yt/spec.json's .before-r1): Captions moved below his lips on the full-face shots (y1092, 19 chunks; his lower lip reaches y984); on splits they stay on the y880 white line because the panels start there, so captions sit at two heights. Hook below (y1340/1445), captions from frame 1. POP grade tuned (grade_look: relight .15, gamma 1.08, bp .04, wp .86, s .30, sat 1.22, skin 1.05), sharpen .55/.40; SPLIT panels restored from the ungraded picture. Re-running yt/build_spec.py would lose this patch: re-run review1.py after it. IG look unchanged. Waiting for his song.

Earlier ▶ STATUS 2026-11-05 22:50: v2 after main's review, both looks re-exported (same names). YT: face from frame 1 under the hook, type beats for the nouns (no stock but the
escalator clip), every graphic a split so captions never touch a label. Both: labels margin >= 72 px (work/margin_check.py), IG captions throughout (stage keeps
160 px free), IG labels bold white sans, SFX full -19.2/-18.7 dB under the voice, cue_check PASS none weak (k2 swish dropped).

## The job
Host George Acheampong (wealth-firm founder), Melanin Money (128K, @MelaninMoney). His yes: "yes". Their Short `reference/NK93HK2_Ex4.mp4`
(61 s, 4.3K views, 1080x1920, 23.976) IS the only source (`source/0000-the-short-itself.mp4`, same file): the clean episode was not found.
Approved beats: `../_onyx-batch7-2026-11/SEQUENCING.md` § 4 (restructure). Viewer gets: the exact order the rich stack business, stocks and
real estate. Title: *You Can't Get Wealthy With Just One Of These*.

## The beats (found by words in the Short, source seconds; cut by `work/cut/`, EDL `transcript/cuts.json`)
| # | Beat | Words (his) | Source s | Cut frames |
|---|---|---|---|---|
| 1 | hook | "It is not an option to be a business owner. It is not an option to be a real estate owner. It is not an option to own stocks. You must own all three." | 22.05-30.35 | 0-199 |
| 2 | what they are | "So there are three escalators to building wealth in America. Real estate, stocks, business ownership." | 0.13-6.56 | 199-353 |
| 3 | the tax tilt | "All of the systems, the tax laws, the incentives, the opportunities are designed to keep these three escalators moving upward." | 7.41-15.08 | 353-536 |
| 4 | the stake | "If you own one of them, you can be rich. If you own all three of them, you can become wealthy." | 15.16-21.73 | 536-694 |
| 5 | mechanism a | "Here's why. Your business makes the income." | 32.70-35.62 | 694-764 |
| 6 | mechanism b | "You invest it in the stock market. Then you borrow against your portfolio in the stock market to then buy real estate. The depreciation from the real estate offset the income in your business." | 37.56-49.02 | 764-1038 |
| 7 | button | "This financial freedom flywheel is what allows our clients to retire three times faster than most other Americans." (cut on "Americans") | 49.20-55.97 | 1038-1200 |

Dropped (their order's fluff): "Think about it", "You take that income from your business", "You must own all three if you truly want to be wealthy",
"Do this now and enjoy the rest of your life sooner". Kept as spoken (flag): "So" before "there are", "the systems," and "Then ... in the stock
market ... then" (no clean gap: 20-60 ms; a trim would add a jump cut inside a split). 50.05 s vs the ~48 s in the sequencing.
"faster" IS in the audio and in WhisperX this time (54.09 s in the source).

## Framing (the burned captions)
Their pills sit at y 1355-1448 of the 1080x1920 file (checked on a strip sheet every 0.67 s: pill top never above y 1352). BOTH looks sample
only source rows 0-1330: `work/base_clean.mp4` = rows 0-1330 at native scale, 120 px of mirrored backdrop above and a blurred reflect below
(1450+), so no pixel of a caption can reach the screen on any frame, any zoom. The IG window crops from the unpadded cut at rows < 1330.

## Teardown: their Short -> ours (Affan's talking points)
| Axis | Their Short | Ours |
|---|---|---|
| Hook (0-3 s) | opens on a definition, "So there are three escalators to building wealth in America" (no stake, no tension) | opens on his hardest line from the middle, "It is not an option to be a business owner. ... You must own all three": a rule with a threat in it, with one claim card |
| Who/what/why by 5 s | not clear: a man on a couch and a pill caption; the show name is a sign half cropped by the frame | claim card + his name low once ("George Acheampong / host, Melanin Money") + the three nouns shown |
| Captions | yellow-on-white pill, 3-4 words, covers his chest, wipes at a constant place | our caption system under his chin (YT: Anton caps, white + gold wipe; IG: Inter, one line), theirs removed from the picture |
| Pacing | 61 s, one angle, no cut, no visual for any of the five ideas, "think about it" and a 5 s outro | 50 s, a new picture every 1-3 s, face never bare over 4 s, cuts on the ideas, no outro |
| Visuals | none: the mechanism (the whole value) is only spoken | three escalators that rise on "real estate, stocks, business ownership", and THE FLYWHEEL builds node by node on his words and spins: business -> stock market -> borrow against the portfolio -> real estate -> depreciation offsets the income -> business |
| Ending | "Do this now and enjoy the rest of your life sooner": an instruction, no button | ends on "retire three times faster than most other Americans" over the loop, cut on "Americans" |
| Sound | raw room | voice -12 LUFS, soft swishes on every graphic entrance, no bed (Affan lays it) |

## Catalog pass (CLAUDE.md rule 5; lean mode, a sample)
`research/effects-catalog/CATALOG.md` read for the moves that fit a one-speaker Short on one couch (not the 137 doc stills, which are long-form
documentary): FX-73 Chart Reprise Push-In (the flywheel returns full-screen at the button), FX-71 Funnel Count (the 1 -> 3 count on the stake),
FX-58 Speaker-Coded Subs (gold wipe on the payoff chunks), FX-68 Data-Point Clipping (the nouns as cut-out chips), FX-23 Pointer Tag (the name tag).
New to this channel: a loop that BUILDS itself on the words, escalators that rise. Last video leaned on receipts/stills; this one has none.

## Better than the last one of its kind
Their sample's value (the mechanism) was a spoken list; ours draws the five-step loop on the exact word of each step and reprises it as the
button. Hook is the mid-speech rule instead of the opening definition. Face max 4 s bare, steady 2.5 %/s drift, pops settle 1.10.

## Downloads (all non-YouTube; logged before the pull)
| File | Source | Size | Use |
|---|---|---|---|
| mixkit 14529 (airport escalator) | mixkit.co free stock (Mixkit licence) | 6.3 MB 720p (1080p denied) | YT B-roll "escalators" |
| mixkit 15064 (house key + tablet on a desk) | mixkit.co | 10 MB 720p | YT B-roll "real estate" |
| mixkit 45661 (candlestick chart on a tablet) | mixkit.co | 3.8 MB 720p | YT B-roll "stocks" |
| mixkit 4451 (shop street at dusk) | mixkit.co | 87 MB 1080p | YT B-roll "business owner" |
| mixkit 206, 47006, 30873, 10161, ... | mixkit.co previews pulled to choose (work/mix/) | < 2 MB each | not used unless listed above |

NEEDS-YOUTUBE: none.
