# Scott D. Clary Shorts: the 1 % ledger

Affan, 2026-11-05: "every short of ours kind of is the same thing over and over again ... not just redo the wheel again and again every single day, just pick out a
different moment, I don't want that. I really want to improve our shorts every single day by 1%."

**The rule.** A new moment is not an improvement. Before a Short is built, the analysis session (Opus) reads `research/effects-catalog/` and `research/shorts-style-radar.md`, adds a radar pass when it has
gone stale, and writes **at least 2 moves this channel has not used yet** here and in the job's BRIEF. The builder (Sonnet) executes them. A move that fails its own test clip gets dropped and logged, never shipped half-working.
After review and at the 7-day read, fill in the verdict: **keep** becomes part of the kit, **kill** goes in the "killed" list and doesn't come back. Results stay in RESULTS.md.

Taste still lives inside the channel: premium, real receipts, no goofy sound, swishes only.

## The ledger
| Short | New this time | Source | Affan's verdict | 7-day read |
|---|---|---|---|---|
| H1 `herjavec-500m-billion` v2 (2026-11-05) | POP grade + stronger sharpen (`workflows/grade-picture.py`) on the whole Short | Radar: our blacks 39 vs 0-13 | Approved with the whole v2 check, 2026-11-05 ("approved and also start the IG build"); no comment on any single move | |
| | Depth type: a giant $1 BILLION BEHIND his head on "I got to get to a billion" **(KILLED at build, see Killed)** | FX-13 | | |
| | Money ladder: $500M → $1.2B → $6B stepping full-screen on his words, then "who cares?" snaps back to his face | FX-71 | Approved with the whole check, no single comment | |
| | His real jet: fast push to the HERJAVEC tail with a hand-drawn circle | FX-55, D2 marks | Approved with the whole check, no single comment | |
| | Colour as story: the family in B&W on "don't love me", full colour on "love me because" (the B&W-to-colour flood was not built) | FX-22 reversed | Approved with the whole check, no single comment | |
| H1 `herjavec-500m-billion` IG variant (2026-11-05, 30 fps check; `ig/`) | Money ladder drawn TO SCALE in the neon window: bars 75 : 180 : 900 px = $500M : $1.2B : $6B, each landing on its spoken word (0 / +1 / 0 frames on the delivered check) | FX-71, IG-native | | |
| | Colour as story in the IG window: the family card in B&W (saturation 0.002), the ski card in full colour from its first frame (0.367); the B&W-to-colour flood on "spend" is built and OFF (`FLOOD_ON`; half the card on that word's frame, measured), his call | FX-22 reversed | | |
| | The jet's deep push warped from the source photo INSIDE the card, a hand-drawn circle riding the same transform (not new to the IG look: Pincus / Harary circles) | FX-55, D2 marks | | |
| H3 `herjavec-unsaved-spreadsheet` (2026-11-08, 30 fps check; Affan's own sequence, cut A as sent) | CRT power-off collapse: the sheet's CRT squashes to a line, then a dot, on "shut the computer down"; the cut lands on his face saying "Anyway." | FX-49 + FX-56 (new here), real-speed test clip viewed before the build | | |
| | The 7 hours -> 2 seconds reprise: an analog clock runs 9 -> 4 beside a filling sheet ("7 HOURS" on "seven"), then the same sheet fills in 2.0 s beside a stopwatch ring ("2 SECONDS" on "two") | FX-73 + FX-77 (new here) | | |
| | (small) a drawn hammer with a scale thud on "hammer." as the last picture, and an alarm clock over a bed for "out of bed" | Bombas B9, FX-77 | | |
| H3 `herjavec-unsaved-spreadsheet` IG variant (2026-11-08, 30 fps check; `ig/`, the neon window) | **Both new moves kept in the IG port, re-composed for the window** (the YT's cards are full 1080x1920 frames; `ig/cards_ig.py` draws them at 1044 x 1044 as pure functions of time): the CRT power-off collapse (the white line is whole 0.9 frames after "down." starts, the dot dies, hard cut to his laughing face; measured on the delivered check) | FX-49 + FX-56 | | |
| | The 7 hours -> 2 seconds reprise in the window: the CRT glides left while the dial (clock / stopwatch ring) and its tag come in on the right, identically in both shots (CRT bounding box 1.1 s in: identical, 0 px; tags +1.6 / +2.3 frames after "seven" / "two"; the ring's arc runs the 2.0 s fill window); the tags are the IG look's red lining Playfair on a dark pill | FX-73 + FX-77 | | |
| | (not new, IG-native) a drawn scene is a pure function of time at window size, so the 60 fps final renders the cards natively and Chronos only touches the cam shots | | | |
| Moshe / Dobrik `moshe-dobrik-coin-flip` (2026-11-09, 30 fps check; Claude's approved pick, funny-test Short 2) | **COIN IRIS** (kit effect `workflows/coin-iris.py`, called through the job's `yt/cards.py`): a gold coin is tossed from below the frame, spinning (motion-blurred, "$" front / star back), flies toward the lens, LANDS face-up, and its rim OPENS like an iris onto the real picture (a gold ring on the expanding edge, the footage pushing out from x1.18 to x1.0). The toss plants the flip on "let's flip" (the coin leaves the top of the frame); the landing pays it off on "We lost the flip" and the iris opens on "He flipped" onto Dobrik's real celebration on "He won". Silent apart from the whip swish. Test clip: `yt/assets/broll/iris.mp4` frames viewed at a 15 fps tiling before the build | FX-16 Portal Zoom with an OBJECT as the frame; learned from **Cleo Abram** (round lens masks as the scene container, "You're Dead. What Next?", 1.1M) + **MrBeast** (a hero object carries every cut, "What's Inside My Briefcase?") | | |
| | A stamped **receipt strip** for the money lines (zigzag paper, typewriter rows, a red worn-ink NO / SOLD stamp, a hand strike-through) with ONLY the numbers he says, over a generic drawn watch (no maker mark) | DOAC / Mark Cuban's spending-review receipt (`eLh-KTuJ1u4`: a red circle and an IMBALANCE stamp on a ledger) | | |
| | (NOT new, Bombas B6 did it; the third-party footage is a few seconds each) REAL vlog footage as receipts: Dobrik's face in the frame-1 split, the watch on his wrist, the bet's handshake, the celebration (muted, a few seconds each, ~8.5 s of 33 s); nothing from the clip's own words or numbers | Bombas B6 (the real event on screen, moving) | | |
| Moshe / Dobrik `moshe-dobrik-coin-flip` IG variant (2026-11-09, 30 fps check; `ig/`, the neon window) | **COIN IRIS in the window** (`ig/cards_ig.py` `WinScene`, the kit effect re-pathed for a 1044 x 1044 stage; `workflows/coin-iris.py` read, never modified): the coin starts inside the window above the caption band and leaves through the TOP edge (the toss, a plant on "let's flip"), the iris version lands on the stage centre (522, 390, r 235) and its rim opens to the window's corner onto the real celebration (a window crop of the vlog read through `cards_ig.FOOT`). Read off the delivered check: landed 27.27 s (the YT's `t_land`), the rim opens 27.50 s on "He flipped", the footage reaches the corner 27.77 s, 11 frames before "won" | FX-16 + Cleo Abram's lens masks + MrBeast's hero object (as the YT) | | |
| | **Receipt strips in the window**: the watch LEFT and the strip RIGHT (the YT stacks them, ~800 px, the stage is ~614), NO stamp in the gap between the label and the figure (first red ink +1.3 / +1.4 frames after "no."), the hand circle round $100,000 (+3.2 after "hundred"), a "STILL DROPPING" tag; the lowest edge stays >= 116 px above the caption top | DOAC / Mark Cuban's receipt (as the YT) | | |
| | (small, IG-native) a **side-by-side frame-1 split inside the window** (Moshe left, the real Dobrik footage right, a 6 px white line that fades out under y 690 so the captions cross a clean picture): a stacked split cannot hold a face in half of a square window | TCO two-up (neon-window LESSONS 2026-10-31 #1) | | |

## Queue (fits a seated podcast, not used yet; pick by what the story needs, never by order)
- **A bespoke graphic world for the one key line** (DOAC): newspaper + halftone cutout of the guest + stacked props (FX-44, FX-19), in place of a photo card.
- **Numbered stages** when a story has steps (Cleo Abram): "1. / 2. / 3." so progress is visible.
- **Two-person stack** when the host's reaction carries it (Hormozi): the listener below, live.
- **Coloured highlight bar** on one caption beat only (Johnny Harris). The caption look itself stays locked.
- **Red word quote** (FX-27) or **Karaoke leader quote** (FX-18) for the one line that should be read twice.
- **Ghost dissolve** (FX-37) between a then and a now of the same person; **Tape morph** (FX-43) for the same.
- **Portal zoom** (FX-16) through a phone or a window into the next scene.
- **Year ghost** (FX-41) when a date matters.
- **Rival colour split** (FX-11) when two people or brands face off.
- **Native 4K master** (Cleo, MrBeast): test on one Short whether a 2160x3840 upload looks crisper after YouTube's encode.

## Killed
- **Depth type (FX-13) on a close talking head, H1 v2, 2026-11-05.** Built and tested end to end: `npx hyperframes@0.8.16 remove-background` made a clean person matte (a smooth silhouette, viewed on 4 consecutive frame pairs at the hair edge (362/363, 372/373, 384/385, 396/397): no gold halo and no flicker between the pairs, only the finest flyaway hairs softened; 0.29-1.2 s a frame on CPU), `work/depth_billion.py` put a gold BILLION between the wall and him (landing on the first "billion", +15 % on the second).
  It fails the readability test: a seated podcast guest with a 9:16 head-tracked crop has his head and hair across x 200-790 of the 1080 frame, so only the two end columns of wall show (~230 px left, ~290 px right) and the word reads "B··ON" (frame 392) or just "ON" (frame 372); the same at three sizes and three heights (y 400-700; lower runs into the mic top). Not shipped.
  **What it needs:** a shot where his head is under ~35 % of the frame width (a wide two-shot, or a guest set further back), or a SHORT word (≤ 4 letters, e.g. "$1B"); the code and the matte step are reusable as they are (`work/depth_billion.py` in the H1 job).
