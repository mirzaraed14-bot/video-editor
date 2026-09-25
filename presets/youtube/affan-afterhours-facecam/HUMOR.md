# HUMOR — how Affan makes a line funny

Measured off the creator's own finished edit of `gta6-pc-release` (2026-09-22, shipped), by diffing their final
Premiere timeline against the rough cut that was handed to them. Everything here is a number read out of the
project file, not an impression. Source: `projects/gta6-pc-release/premiere-backup/ABW6-FINAL-shipped.prproj`.

**The thesis in one line: the comedy is in the TIMING, not the material.** The jokes are already in the script.
What the edit does is hold the funny word a beat too long, and chop the serious claim into pieces. Nothing is
added. Nothing is decorated. The edit just changes the speed at which a sentence arrives.

---

## 1. Slow motion is the punchline marker — and it is ALWAYS exactly 80 %

Ten slow-downs in the video. **Every single one is 80 %.** Not 79, not 75, not a ramp. One value, used ten times.

| # | at | length | the line under it |
|---|---|---|---|
| 1 | 0:18 | 2.69s | "ladies and gentlemen, everybody is wrong." |
| 2 | 1:09 | 1.60s | "Bro, I heard this and that." |
| 3 | 1:12 | 1.82s | "oh, everyone is going viral?" |
| 4 | 1:31 | 0.75s | "okay." |
| 5 | 1:31 | 1.40s | "Add a year and a half." |
| 6 | 1:33 | 2.17s | "Oh, shit." |
| 7 | 1:35 | 0.82s | "shit. 2028." |
| 8 | 3:45 | 1.97s | "Making a game for PC" |
| 9 | 3:48 | 0.65s | "Shaq." |
| 10 | 4:48 | 1.44s | "is your impatience." |

**What they land on.** Read the right-hand column and the rule is obvious: a slow-down goes on **the moment a
joke lands or a claim drops**, never on a fact. Not one of these ten is on a date, a number, a name or an
explanation. The video is full of dates and numbers and none of them are slowed.

**Four in a row is allowed.** Rows 4–7 are one continuous run: *"okay." → "Add a year and a half." → "Oh, shit."
→ "shit. 2028."* The whole comic build of the maths gag runs in slow motion, roughly five seconds of it. This is
the single most distinctive thing in the edit and the preset's "1–2 per video" badly understates it.

**The punch word gets its own clip, slowed, alone.** "Shaq." is a 0.65 s clip. "shit. 2028." is 0.82 s. The
word that lands is cut away from the sentence around it and held.

## 2. The biggest claim gets chopped into staccato

The video's central line was one clip in the rough cut. They cut it into **four**:

> "November 2027 is" (1.69s) · "when" (0.77s) · "PC version of GTA 6" (2.22s) · "will be released." (0.85s)

A single word, "when", gets its own 0.77 s clip. Compare this to how the jokes are treated and the grammar is
symmetrical: **a joke is slowed down, a claim is cut up.** Both are ways of making a sentence take longer to
arrive. Neither adds anything on screen.

Seventeen of the rough cut's segments were split further this way. The others are all the same shape: the setup
runs at length, then the last few words get their own short clip.

## 3. Where they deliberately do NOT do anything

The whole GTA 4 / GTA 5 / Red Dead date recital is left alone at normal speed with ordinary-length clips. So is
the entire CEO section. So is the Mike York explanation. **Information is delivered flat and fast**, which is
exactly what makes the slowed moments read as jokes. The contrast is the mechanism.

## 4. The rhythm it produces

| | |
|---|---|
| runtime | 315.7 s |
| clips on V1 | 127 |
| cut rate | **24.1 / min** |
| median clip | 1.77 s |
| shortest | 0.20 s |
| clips under 1 s | 26 |
| clips under 0.6 s | 4 |

---

## 🔴 This CORRECTS the preset — three numbers were wrong

`PLAYBOOK.md` and `README.md` were measured off two reference videos, not off the creator's own edit. On their
own work:

| | preset said | actually measured |
|---|---|---|
| slow-downs per video | 1–2 | **10** |
| speed | 0.5–0.6x | **0.8x, every time** |
| what gets slowed | "slow the inserts, not the face" | **8 of 10 are the FACE**; only 2 sit on an overlay |

0.6x was too slow and too rare. **Use 0.8x, and budget around ten of them**, clustered on the comic runs rather
than sprinkled evenly.

## How to apply this next time

1. Read the script for the two or three places a joke actually lands. Those get 80 % slow-downs, and if one of
   them is a build (setup, setup, punch), slow the WHOLE run, not just the last line.
2. Isolate the punch word onto its own clip before slowing it. Under a second is normal.
3. Find the video's single biggest claim and cut it into three or four staccato pieces at natural word breaks.
4. Leave every date, number, name and explanation completely alone.
5. Never invent a joke in the edit. Nothing here is a graphic, a sound effect or a zoom gag. It is all speed.

**Still unmeasured:** the cut-zoom scale values and their hold lengths. Premiere 25.0 stores keyframes as encoded
parameter blobs in the `.prproj` and the live project has moved on to `ABW8`, so the zoom magnitudes could not be
read this pass. The zooms live INSIDE the nested sequences (19 nests on V1), matching the creator's own
description: "cut zooms inside the nested sequence, then nest it up and zoom it again." Get these next time by
reading keyframes off the LIVE project while it is open, or by measuring an export with
`workflows/style-zoom.py`.
