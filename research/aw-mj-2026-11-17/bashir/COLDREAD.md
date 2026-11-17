# Cold read: Bashir card "Michael Jackson TRUSTED Him" (SEQUENCE.md v0.2), 17 Nov 2026

Judged on the files only (no web, no playback). Frames looked at: every `proof/*.jpg` and `full_*.png` named below. Word times: `asr/*.words.json`. Numbers: `api/*_stats.json`, `api/c_*.json`, `IG.md`.

**VERDICT: SEND AFTER FIXES, as a below-bar evidence CARD, not a pick. V1 as drafted does NOT go.**
The strong part is real: beats 3 and 4 (a journalist's on-air "angry ... suffer" against his own off-air "weep") are first-party, exact and self-proving. Around them the draft staples a Diana story whose link to Bashir is a card we supply, rests on one source it has not downloaded, and prices itself about 1.6x too high.

**PRICE: centre 55K (honest band 40-70K), range 12K to 500K. UNDER the bar (150K centre / 1M top), not close.** The draft's 90K centre and 1.2M top are not supported by the files (finding 7).

---

## Numbered findings

### 1. Shape

**1a. BLOCKER: the Bashir link is not spoken anywhere in the pick's cut.**
- Evidence:
  - Beat 2's chosen span is TT 225.84-234.67 (`asr/tt_215.words.json`): "In 1995, this little-known British journalist caused an uproar when his sensational interview with Princess Diana revealed details of her extramarital affair." The word "Bashir" is not in it. "Martin Bashir" sits in the PRECEDING sentence, 216.89-224.90 ("But who is Martin Bashir and how did he get an exclusive interview..."), which is the draft's "+8 s option".
  - SEQUENCE.md line 86 says "the Bashir-did-Diana's-interview link is spoken by Povich (TT 225.84-234.67)". Only true with the option, which turns V1 into about 48 s.
  - Beat 5 (William) never names Bashir; the draft admits it (line 28: "He never names Bashir").
  - The only spoken "Bashir" in the whole base cut is Jermaine's, in beat 1 (4482.71-4483.51).
- Result: the viewer hears "this journalist ... Diana", then "BBC employees lied", with a card "2021: AN INQUIRY INTO THE DIANA INTERVIEW" in between. The step that makes the Short work, "the man who interviewed Diana forged documents", is our card. That is exactly the "line we supply" the checklist § 4 forbids.
- The earlier cold read (`pass3/COLDREAD-DRAMA.md` § 2.1, 2.5) set the condition itself: D1 passes SHAPE only if William names Bashir; if not, "the Diana half is fact A + fact B and D1 collapses to N1". William does not name him. So by its own test D1 collapses.
- Fix: either (a) make V1 the collapsed arc (beats 3, 4 + the button; Diana as a closing card or dropped), or (b) put Povich's "Who is Martin Bashir ... Diana" sentence (216.89-234.67) in as the spoken link AND find a speaker who ties "fake documents" to Bashir by name (Taj/Sunrise 2021, `mjLoyJ3FPKY`, not yet downloaded; or the Channel 4 / Guardian 2021 pieces). Do not ship a version where the link is only a card.

**1b. MAJOR: hook is paid off by a word echo, not by content.**
- The hook says "trusted". The ending is "When they lie". Michael's "lie" is not about Bashir or Diana's forgery. Context from `asr/tt_3495.words.json`: 3496.43 "They were trying and trying to try to get some crap on Michael that was not true." (a Jackson-camp voice, Jermaine on screen at 58:16, `proof/tt_hurts_3496.jpg`), then 3501.02 "What hurts you most?", 3502.82 "When they lie.", and after the cut 3509.32 "And it hurts me because I know there's children out there who has to hear that crap."
- So the "lies" are the allegations and the press, in Michael's words. The draft's own G-table says "never captioned as about Bashir", but the whole sequence is built so the viewer reads it as about Bashir. That is the editorial join the checklist wants in a speaker's own words.
- Fix: say in the sequence text that beat 6 is a join of ours, and either cut to a button that is about Bashir (not found in the files), or accept the join and take the implied-claim risk (finding 5b).

**1c. MAJOR: beat 5 is not understandable to a stranger.** "BBC employees lied and used fake documents to obtain the interview with my mother" tells a cold viewer: a prince says the BBC lied. Nothing says that Michael's journalist and the BBC's liar are one man, or that William's mother is Diana, unless beat 2 and the card did it. Gate F (viewer understands who/what/why in 5 s from the clip alone) fails for this beat.

**1d. MAJOR: the beat 3 / beat 4 "contradiction" is arguable, and a commenter will say so.** "They are restricted. They are overly protected. I was angry at the way his children were made to suffer" (4325.57-4331.78) and "your relationship with your children is spectacular ... it almost makes me weep" (4334.72-4342.57) are compatible: one is about the restrictions (masks, veils, the balcony), the other about the bond. The full sentence after "weep" (`tt_2185`, 2211.86-2218.01) is "because your interaction with them is just so natural, so loving, so caring". The pairing is Take Two's own (the Jackson camp's: Take Two narration at 4323-4324 "included on Bashir's special", 4332.62-4333.80 "But this was not"). It needs a narrator-free way to show it, or it reads as our spin.
- Also: `asr/tt_4318.words.json` is a bad chunk. It prints "Your relationship with your children is spectacular" at 4325.57-4333.15, where `tt_4323` and the Take Two card (`proof/tt_angry_4318.jpg`, 01:12:05 card) both show "They are restricted ... angry". The draft correctly used `tt_4323`, but the two files disagree and the log does not say so; delete or flag `tt_4318` so the build session does not trust it.

### 2. Quotes vs word times

| Beat | Draft says | Files say | Verdict |
|---|---|---|---|
| 1 | TT 4479.32 → 4483.51, "And he trusted. He trusted Martin Bashir." | `tt_4465`: And 4479.32, he, trusted, 4479.78-4480.30; he trusted 4480.80-4481.35; **1.36 s gap**; Martin 4482.71-4482.97; Bashir ("Bashoor") 4482.99-4483.51; next word "They" starts **4483.53** | Words exact. MINOR: out point is 20 ms before the next word; the line continues "They took this thing back to the studio ... the way this thing was narrated, it was just not fair" (4483.53-4493.65). |
| 2 | TT 225.84 → 234.67 | `tt_215` exact, "In" 225.84, "affair." ends 234.67 | Exact, but "Bashir" absent (1a). Alt in 216.89 exact. |
| 2 text | On screen: "He told me that he was 'the man that turned Diana's life around.'" | Draft's own quote of the statement (SEQUENCE.md lines 24-25): "...and told me that he was 'the man that turned Diana's life around.'" | MINOR/MAJOR: the on-screen text changes the words inside quotation marks and presents them as "Michael's own words". Use the exact clause, or no quotation marks. No file in the folder holds the statement itself. |
| 3 | 4325.57 → 4331.78 | `tt_4323`: They 4325.57 ... suffer. 4331.78 | Exact. Antecedent of "They" is cut (not named until "his children"). Sheet confirms card text. |
| 4 | 4334.72 → 4342.57 | `tt_4323`: Your 4334.72 ... them. 4342.57; **1.56 s hole** 4338.00-4339.56 inside the beat | Exact. The 7.9 s includes a 1.6 s gap; trim it. First-take alt 2203.85-2205.99 + 2208.64-2211.62 exact; cuts out "I love you" 2206.67-2207.80. Who says "I love you" is not established ("off-mic" is an assertion). If it is Bashir, it is the strongest line in the pair and is being cut. |
| 5 | William, pending | no file | NOT CHECKABLE. See finding 3 on wording. |
| 6 | 3501.02 → 3507.00 | `tt_3495`: What 3501.02 ... most? 3501.88; When 3502.82 lie. 3503.54; The lies. 3504.62-3505.24; The complete lies. 3505.88-3506.96 | Exact. Out 3507.00 is 40 ms after "lies." Frame step (`proof/step_3506.56.jpg`) confirms Michael through 3507.08, dissolve to the child by 3507.12; the cut at 3507.00 is safe. |

Anything said in between: only the 1.36 s gap in beat 1 (possible laugh; the ASR gives no word) and the "I love you" in the first take.

### 3. Numbers vs the files

Found and correct: William 327,505 (`Qyfc1KHJLfI`, 20 May 2021); Taj/Sunrise 52,986 (24 May 2021); ABC upload 279,720; 18,275,995; 4,454,488; 609,430; 347,798; 55,454; Channel 4 253,098; ITV 951,567; Guardian 655,916; Untold MJ 1,324; The Recall 999; Tea With The Airhead 695 (16 Nov 2026); Damn Quotes 115; Popcorned Planet 86,502; SLY 34,631,759; our K*ller 1,214,895 (Jul 2026); Candace Owens 984,588; Celeb Daily 444; GMB 890,849. Comments: 2,075 (`c_TGqCXiYAVLo`), 519 and 317 (`c_mjLoyJ3FPKY`). Every IG number in the gate table matches `IG.md`. AFRAID 167,235 (RESULTS line 101), GANGSTER 88,662 (RESULTS line 38).

Wrong, stale or not in any file:
- **MAJOR: "William = Royal Family channel ... official."** The channel is "The Royal Family Channel" and the description ends "Report by Iain Jones", so the upload is a news report, not a Palace video. "Official" is not supported anywhere in the files. The Guardian (655,916), ITV (951,567) and Fox (433,075, `OmvVPdk_64Y`) carry the same statement and are better-labelled sources.
- **ABC 2009 date "25 Jun 2009":** the file gives upload 5 Aug 2009 (title "ABC NEWS Martin Bashir confessed he lied in Living with Michael Jackson", by a fan account). The ABC News piece itself is `MeEEODRn6Ik`, 26 Jun 2009, 177,992. The 25 Jun date is in no file. (Variant only.)
- **MINOR: stale lane numbers.** `AW-SHORTS-NOW.md` row 40: AFRAID is 176K now (draft: 167K). DISRESPECTFUL is 86K (draft: 80K). La Toya BETRAYED is 19K, 17,412 on RESULTS (draft: 20K).
- **Not in any file (web-only, I cannot verify):** Take Two aired 20 Feb 2003; 1440x1080 / 25 fps / 1.64 Mb/s probe; Panorama 22.8M viewers; the Press Gazette / The Week / AP / Irish Times / Yahoo UK pages; Taj's Insider quote ("welcoming ... Princess Di"); Bashir's apology and "no bearing" line. G5 says PASS on these.
- **MINOR: Granada citation.** "TT 4672.7-4678.5 ... Granada maintained it was fair and honest" has no word file: no `asr/tt_*.words.json` covers 4672 (they stop at 4614.98). The counter-evidence is "shown, never hidden" in the table but appears in none of V1's beats.
- **William's wording (MAJOR):** the draft's beat 5 line "BBC employees lied and used fake documents to obtain the interview with my mother" is not in the folder. The only William words in the files (the `Qyfc1KHJLfI` description) are "the deceitful way the interview was obtained substantially influenced what my mother said ... a major contribution to making my parents' relationship worse and has since hurt countless others." Until the clip is downloaded and the words read, "fake documents" in William's mouth is unverified; if he did not say it, beat 5 has no line.

### 4. Proof honesty

| Beat | Status | Evidence |
|---|---|---|
| 1 Jermaine "he trusted Martin Bashir" | OURS | no Short found (b15, b16) |
| 2 Povich + statement text | OURS; Povich is a narrator | b11: 0 results |
| 3 on air | NOT proven; half-seen | Take Two's own pairing |
| 4 off air | half-seen, and under-counted | see below |
| 5 William | the lane is big (ITV 951K, Guardian 656K, Fox 433K), as a join it is OURS | |
| 6 "When they lie" | OURS | b18, b19 |

- The draft does not oversell the 18.3M / 4.45M lane: it says they are other moments (lines 83, 110) and prices without them. Good.
- **MAJOR: G4 "Freshness PASS" and "Seen half" understate how much of the Take Two material is already out.** In the files and not named in the draft:
  - `0q12VDbW0ug` LEGENDS IN 4K "MICHAEL JACKSON CALLS OUT MARTIN BASHIR FOR CHEATING", 10 s Short, **419,508**, Dec 2024.
  - `GPKE6_YmYrE` Visionary "How Martin Bashir manipulated Michael Jackson (Take Two - Living with Michael Jackson", 78 min, **260,627**, Jun 2021: this is the programme itself.
  - `76wEcQIYiW0` "MARTIN BASHIR IS A LIAR! Michael Jackson TRUTH footage revealed", **106,848**, 2009.
  - `qUSXw2_V4pY` Soul Lounge "When MICHAEL Jackson Went Off on Bashir", **87,665**, Jul 2026.
  - `PAUS4xm_z50` "Exposes Martin Bashir" **55,454** is named but "content unread" while the draft already uses it as proof; its 13 comments (`c_PAUS4xm_z50.json`) include "the best place to put a camera..." and "Thank God they did that video, Bashiar is evil", so it is probably the same own-camera footage.
  - The Take Two own-camera pair (beats 3-4) is likely already clipped; read these before calling it a fresh join. A 55K result on a clean 58 s Take Two Short is also the nearest price anchor for this source.
- **MAJOR: the join already exists as 2021 news.** Sunrise `mjLoyJ3FPKY` (52,986): "Michael Jackson's nephew claims Martin Bashir also deceived singer to secure interview ... just like he did to Princess Diana." That is the first-party-family link the earlier cold read said to look for (§ 2.6 check 1b). The draft acknowledges the video but not that it IS the link and that Taj is the speaker who could carry beat 5.
- **IG per-beat proof is thin.** IG.md ran 7 searches; none for beat 1 (Jermaine), beat 4 ("almost makes me weep") or beat 6 ("when they lie"). The gate needs each beat searched in several phrasings with numbers. The Take Two, JOIN and Taj searches returned "No results" and were not reordered or retried in other phrasings. The judgment comments are 2021 Sunrise and a 2025 calm-Michael Short whose top comment (2,372) is not about Bashir.

### 5. Rules

**5a. Minors, from the sheets.**
- Chosen frames are clean: beat 6 Michael teal 58:20.5-58:26.5 and 3507.00 (`proof/tt_hurts_3500.jpg`, `step_3506.56.jpg`); beat 3's masked children (`tt_angry_4318.jpg` 01:12:02-07 veiled child in purple, 01:12:08-13 balcony silhouette) are correctly replaced; beat 4 Michael in red 01:12:14-21.
- MINOR: beat 1's picture. Adult-only Michael + Bashir walk exists only at about 71:34.5-71:36.9 (`proof/tt_onair_4283.jpg`: 71:33 children running at the Neverland arch, 71:37 onward card + bumper-car and swing children, 71:43-47 children). That is about 2.4 s for a 4.2 s beat: a freeze or slow-mo is needed, or a different picture.
- MINOR: Take Two's red "children at the van" cut sits at 58:27-58:32 straight after beat 6 (child in red). The out at 3507.00 is correct; do not extend.
- MINOR: Diana Panorama window TT 3:49-3:55 (`tt_diana_217.jpg`): the "PRINCESS DI ... The Men... The SEX... The spies who caught her" tabloid cover is burned in from 3:53. Use 3:49-3:52 only. Skip 3:45-3:47 as drafted (boys behind Bashir, the sheet shows them). The window is a small SD picture-in-picture (`full_230.5.png`), soft once scaled; the draft's "BBC original at build" is not sourced yet.

**5b. MAJOR: the Short implies "Bashir deceived Michael", which is the claim the draft says it will not make.**
- The structure is: Michael trusts Bashir -> Bashir's two faces (Take Two's framing) -> Bashir's Diana interview obtained with fake documents -> Michael: "When they lie." Each caption is accurate; the sum says Bashir lied to Michael.
- The only sources for "two faces" and "edited unfairly" are the Jackson camp (Take Two, Jermaine's next sentence "they took a lot of things out ... not fair"). Dyson found deceit toward Spencer/Diana (draft's own G5); no inquiry covers Michael. Bashir's own side (apology for the forgery only; Granada "fair and honest") is in the draft's table and nowhere in the cut.
- Titles: #3 "Michael Jackson Was LIED To" is the same claim by title. Drop it. #1 is the safest; #2 "He Trusted Martin Bashir" is neutral.
- Fix: keep every caption to "said", never "lied to"; put the Granada/Bashir counter-line on screen in the cut or accept this stays a card.

**5c. Allegations lane: still "his call", correctly open.** Add: beat 6's own continuation ("children out there who has to hear that crap") and the 55K Short's comments ("He literally admitted to sleeping with young boys?!") show the comment section goes to the allegations, and `rEkjIrEXQ-w` Megyn Kelly (793,828, 28 May 2026) shows the lane is live in 2026. Name this in the pitch's first lines.

**5d. Captions on "When they lie".** Short-form captions run the whole video; the spoken words are the caption. Nothing wrong with the words. The risk is the label: "MICHAEL · 2003" is fine; any "BASHIR" or "BBC" label on beat 6 would assert the join.

**5e. Jermaine's grin (tone).** Confirmed on the frames: `proof/tt_trusted_4466.jpg` 01:14:31-52, `tt_jermaine_4468.jpg`, `full_4481.png` (wide smile at 4481) show him smiling or laughing through "he trusted, he trusted". Covering with Michael + Bashir fixes the picture but the audio may carry the laugh in the 1.36 s gap (4481.35-4482.71). If beat 1 survives at all, cut the gap and listen.

**5f. Take Two music bed (PITCH-CHECKLIST § 2): unresolved.** Speech -19 to -22 LUFS with the bed 8-10 dB under (draft lines 50, 82); the checklist lists "music under the voice" as a fail. The stem test is blocked on an 80 MB htdemucs download. Nothing in the files shows it works. Until it does, beats 1-4 and 6 all carry Fox's score; AW ships with no music of ours.

**5g. Source sharpness (`proof/anchor_bashir.jpg`).** The anchor compares RAW Michael/Jermaine crops against the approved Prince panel AFTER the recipe, which is not the rule (finish a 2 s test with the build's recipe, compare 1:1). Even raw, Jermaine is clearly softer than Prince; Michael's crops are in the same range but soft. The source is an SD broadcast, 4:3, with the picture only about 65 % of the frame once the red side panel is cropped, then a 9:16 crop: very little real resolution. The Iris + Proteus test was NOT run. "Above the Bieber phone shot" is the bar for a failed shot, not a pass.

### 6. Hook: beat 1 and the variants

- Beat 1 as drafted ("And he trusted. He trusted Martin Bashir.") is not a claim a stranger cares about in 3 s:
  - The name "Martin Bashir" starts at 3.39 s into the 4.19 s beat (4482.71 minus 4479.32), after the 3 s window; "he" has no antecedent unless a picture or the title supplies Michael.
  - It states a fact the audience already holds (draft pre-mortem: "the first 3 s carry nothing new"), by a smiling brother, with no stake and no loop.
  - The sentence that gives it stakes ("they took a lot of things out and the way this thing was narrated, it was just not fair", 4483.53-4493.65) is cut.
- V2 (William cold open): the line is a real claim, but the hook's topic is Diana, the payoff's topic is Michael: the Diana v1.1 failure (`pass2/coldread-diana.md` finding 4, same pattern). And William does not name Bashir.
- V3 (off-air "weep" cold open): a praise line, not a claim, as the draft says.
- **What I would send:** a re-ordered V3: open on beat 3 in Bashir's voice ("I was angry at the way his children were made to suffer": a journalist's accusation, a stake a stranger holds in 3 s), then beat 4 ("spectacular ... weep"), then the Diana turn only if a spoken link exists, then "When they lie". It is the only version in which the opening claim and the answer are both first-party and in the Take Two pairing's own words. It is also the N1 arc, which is where D1 collapses anyway. Caveat: the pairing is Take Two's (already clipped at 55K / 419K, 5g, 4), and the hook becomes allegation-adjacent audio.
- If Affan insists on V1, replace beat 1 with beat 1's own next sentence ("they took a lot of things out") only after a listen, and put "Michael" on screen in the first frame.

### 7. Price

Evidence set (all from the files):
- Bashir-lane on our channel: AFRAID 176K now (Sep, Affan's cut, his best of the lane); GANGSTER 89K (one Bashir line, Nov 1); DISRESPECTFUL 86K (Walters, Sep).
- Our MJ Shorts since 1 Oct (`AW-SHORTS-NOW.md`): Police 11K, Lisa Marie 17K, La Toya BETRAYED 19K, Doctor 27K, Electrocuted 33K, Masks 76K, Gangster 89K. Median about 27K; two of seven reached the high 80s; none reached 150K. (Older 142K-244K MJ Shorts are Sep/Oct and come from emotional family stories, not interviewers.)
- The source's own proof: a Take Two Short at 55K; a 419K "calls out Bashir for cheating" Short (LEGENDS IN 4K, Dec 2024); the 2021 join news at 53K-86K. The 18.3M and 4.45M are different moments with the children on frame (draft says so; correct).
- Source drag: SD, side-panel crop, Fox bed, no recipe test; MAX-EFFORT items open (William not downloaded).
- Upside not in the draft: IG.md's own table says the 1.3M @thewindsorcrown post is a "20 Nov 1995 Panorama anniversary" post; today is 17 Nov, so a 20-21 Nov post would be on the anniversary. The draft says the peg is "unverified". TEMPLATE-birthdays § 3 says liveness beat lifetime views. That is real upside, but only if the build is finished in three days with sources that are not yet downloaded.

My price: **centre 55K, range 12K-500K.** The draft's centre of 90K needs a hit-rate the last seven MJ Shorts did not show; the 1.2M top is borrowed from our unrelated K*ller "LYING" Short (a different, resolved story) and the lane's 18.3M. 1M+ here needs the anniversary peg, a clean source and a spoken link all at once: I put it near 3 %. UNDER the bar by a wide margin. By PITCH-CHECKLIST's exception it can only go as a card with the failure named first, and "source quality" is the line Affan said he would reject on.

5K pre-mortem: add "the Take Two own-camera pair was already clipped (419K/55K)" and "the Diana half reads as a history card to a MJ-fan feed". 5M pre-mortem: keep, but name the 20 Nov anniversary as the only plausible lift.

### 8. MAX-EFFORT-GATE items still open

1. **Research per beat:** Instagram not searched for beats 1, 4, 6 (and Jermaine's line); Take Two / JOIN / Taj IG searches ("No results") never retried; other tellings of beat 6's "lies" answer not searched (the teaser at 2676 is a different cut of the same answer: "They're lies. They're complete lies."); the 419K / 260K / 107K / 88K Bashir uploads above not read.
2. **Download, transcribe, frames, audio, quality gate:** William (`Qyfc1KHJLfI`, or the Guardian/ITV/Fox copy), Taj (`mjLoyJ3FPKY`) and ABC 2009 are NOT downloaded, transcribed or framed; the Diana picture is unsourced; the stem test and the Iris + Proteus recipe test are NOT run; quotes NOT heard by ear.
3. **Variants:** done (V1-V3), but V2 and V3 share five of six beats; there is no second beat set, only second orders.
4. **Fable advisor twice:** the status line (line 4) lists "advisor ... final advisor" as open. NOT done.
5. **Independent cold read of the FINAL version:** this file is it, on a draft v0.2 that still has open sources. Apply fixes, then re-read, because the fixes (the arc) are large.
6. **Channel checklist:** the § 0 statement exists and is honest (it names FAIL), but G5 says PASS on web-only facts and the verdict line "goes here once priced" is empty.
7. **Opening statement:** the message must open "NOT max effort yet: <items 1, 2, 4, 5>". It cannot open with the max-effort statement.

---

## Ranked fix list

1. **Decide the arc.** Collapse to N1 (beats 3, 4, 6, about 20 s) with Diana as a closing card or dropped; or keep Diana only with a spoken Bashir-by-name link (Taj/Sunrise, Channel 4/Guardian 2021). (1a, 1c)
2. **Download and read William, Taj and the Diana picture;** use ITV/Guardian/Fox copies; verify "lied and used fake documents" in his own words or drop it. (3, 8)
3. **Run the source tests:** stem separation for the Fox bed and the Iris + Proteus recipe on a 2 s beat-4 and beat-6 crop, against the approved Prince panel. A fail kills it per Affan's 10 Nov rule. (5f, 5g)
4. **Check the already-out Take Two clips** (419,508, 55,454, 260,627, 87,665) for beats 3-4 and re-write G4 from what they contain. (4)
5. **Replace the hook** (re-ordered V3, or a V1 hook with the name and Michael in the first 3 s). (6)
6. **Rewrite beat 6 and the title for the implied claim:** no "LIED To" title; say in the sequence text that "When they lie" is about the allegations and the press in Michael's own context, and put the Granada/Bashir counter-line in or keep it a card. (1b, 5b)
7. **Fix the on-screen statement quote** to the exact clause; label Povich as narrator. (2)
8. **Re-price to 55K (range 12K-500K),** update AFRAID 176K / DISRESPECTFUL 86K / La Toya 19K, state the 20 Nov anniversary as the only lift and whether it can be hit. (3, 7)
9. **Close the gate items:** Instagram for beats 1, 4, 6; the two Fable advisor calls; open the message with "NOT max effort yet". (8)
10. **Housekeeping:** flag `asr/tt_4318.words.json` as unreliable; trim the 1.36 s gap (beat 1) and 1.56 s gap (beat 4); beat 1 picture needs a freeze past 71:36.9; resolve who says "I love you" at 2206.67; crop the tabloid cover at Diana 3:53.
