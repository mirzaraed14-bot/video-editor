# CUT.md template (the Opus cut call writes `$J/CUT.md` in exactly this shape; build_plan.py and keepjson.py read it)

▶ STATUS: (cut call: one line)  ·  Better than the last: ___  ·  Predicted length: ___ s  ·  Bed: <BEDS-b9.md row, file start s>

## K table
| K | span (OBS raw seconds) | words | rule |
|---|---|---|---|
| K1 | 41.17-44.18 | "Gentlemen, today we are going to be reviewing ..." (the only "Gentlemen" at the start) | NEVER |
| K2 | 46.78-49.44 + 55.31-57.82 | "They've been kind enough ..." (last take) | NEVER |
| K3 | PLAY theirs file 0.00-9.70 (= OBS 79.09-88.79, ≈9.7 s) | THEIR Short, its own audio, from "..." through "..." | keep |
| K4 | 89.32-99.84 | "..." | keep |

Rules the table must obey (spans.py checks the word edges): a span starts on a word START and ends on a word END; PLAY rows carry `(= OBS a-b ...)`;
the rule column is `NEVER` (do not drop), `keep`, or `OUT` (listed for reference only); `DROP 2nd` style notes go in the rule text; drop-in-order is the K ids you
pass to `cutchain.sh` when the cut runs over 3:00. Run `python $KIT/tools/spans.py $J $J/CUT.md --fix` and it prints the predicted length.

## Files
theirs = projects/<job>/reference/short-XXXX.mp4
yt = <our YouTube sample file>
ig = <our Instagram sample file, optional>
handle = @TheirChannel
avatar = work/avatar.jpg
view = <cx>,<cy>,<z>

(`view` is the ONE static screen view he is talking about, in source px: centre x, centre y, zoom. It sits in the top panel for the whole video; measure it once on the prep contact sheet. Crop out the Claude app, browser chrome, the taskbar and his own facecam inset.)

## Beats
| K | layout | menu item | exact copy |
|---|---|---|---|
| K1 | FACE | channel_card | Their Channel ; @TheirChannel ; 835K subscribers@43.12 |
| K2 | SPLIT | side_by_side | theirs:THEIR SHORT ; yt:OUR EDIT |
| K3 | SPLIT | play_card | theirs |
| K4 | SPLIT | pointer_mark | THE TITLE@89.3 ; 1700,1240 |

MENU (the only items; 8-12 graphics per reaction; one soft SFX cue per entrance, exits silent; entrance = `slab`, no overshoot):
`channel_card` (real avatar, on the hook) · `cred_cards` (2-3 over the intro) · `play_card` (one per play; the K row must be PLAY) · `side_by_side` (theirs-vs-ours) ·
`number_card` (number shown on their screen) · `pointer_mark` (1-2). Copy grammar: `;` separates items; `text@raw` anchors an item at OBS second `raw`.
cred_cards: first item = the label (its `@raw` = when the gold rule draws), then chips `CHIP@raw`. number_card: `value|LABEL@raw ; value|LABEL@raw` (value = seconds, `1:27`, or text).
Card copy is his own words, ≤ 5, kind. Censor drug and self-harm words in the captions.
