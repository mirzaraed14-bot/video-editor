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
