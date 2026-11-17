# COLDREAD-FORMAT2 — re-read of SEQUENCE.md v1.0 (17 Nov 2026)

**VERDICT: SEND AFTER FIXES, as a card, NOT a pick.** One MAJOR on the beat-4 card (firing / year ambiguity from a single unsaved source), one MAJOR on the beat-6/7 adjacency, and the V1 table still carries dead air and a mis-stated total. All fixes are small. **My price: centre ~70K, band 30-200K, P(>=1M) ~2%. Under the 150K bar.**

Checked against: word-time files, `fTTl4Vaow5Y.fw.txt`, the four sheets, `beats2/SEQUENCE.md` § Facts, `COLDREAD-FORMAT.md`. No web, no audio.

## 1. Beat 4 card (papers sent to Joe's house -> "not easy firing your father")

- **MAJOR: the card is supported by one note, with no saved source, and which firing it describes is unsettled.**
  - Everything for the card is the SEQUENCE.md cell itself ("Yahoo/Insider fetched 17 Nov"). No copy of the page is on disk (grep for "sent to Joe" finds only SEQUENCE.md).
  - The same cell says the Insider text puts the firing "just as Michael became a worldwide superstar" (the line carried in COLDREAD-FORMAT.md's P-A row). That reads as Thriller-era (1983), not 1979.
  - `beats2/SEQUENCE.md` § Facts has Michael dropping Joe as manager in 1979 and the brothers following in 1983, "at Michael's urging" (NYT). It also says the NYT quote of "It's not easy firing your father" sits in the 1983 context, and the NYT page itself was never opened.
  - The card sits right after beats 2-3, whose label says 1979. A viewer joins "1979 / papers sent / not easy firing your father" into one event. The files do not establish that the papers and the quote belong to the 1979 manager firing and not the 1983 one.
  - "Told a biographer" (Taraborrelli 1991) is correctly softened to "MICHAEL, LATER:", but the card never says it is a book quote.
- Not an overclaim: "the papers" (passive, nobody named as sender) and no year. Both are the safest wording available.
- **Fix:** (a) save the Insider page text into `format/` before send; (b) tag the card with its source ("per Insider, citing Taraborrelli"), and put "reportedly" in the first line; (c) keep the year off the card and never let beat 2's "1979" label bleed into it. A dated sentence is not supportable from the files. (d) Ideally open one more source (Taraborrelli excerpt or the NYT page) to settle which firing; if unsettled, say "WHEN HE FIRED HIM".
- Also worth knowing: the card confirms the film ("piece of paper") rather than correcting it. That is fine as a "the movie didn't lie" beat, but the "OURS (answers the film's piece of paper)" label should not become a caption.

## 2. Beats 6-7 against the word times

- **Piers (6):** the question is real and matches the file: 217.92 "But do you have any regrets that you may have been a little bit too tough on some of them?" ends 222.13. Joe: "Well," 223.09; "I'm glad I was tough because look what I came out with." 224.41 -> 227.75-228.21. Sheet_piers_224: Piers on camera 217-221, Joe from 223. Quote is exact.
  - **MINOR:** in/out is 217.92 -> 228.21 = 10.29 s raw. The table says 4.2 + 5.1 = 9.3. That only holds if the 0.96 s gap (222.13 -> 223.09) and the 0.92 s gap ("Well," -> "I'm") are trimmed. Write them in the EDL (223.09-223.49 "Well," can be dropped; start Joe at 224.41, or keep "Well," and trim the gap).
  - **MINOR:** the cut ends on "look what I came out with." The next words (228.37-231.60) are "I came out with some kids that everybody loved all over the world." That is the stronger half of his answer and it is cut. Cutting at 228.21 is defensible, but it makes Joe sound like he is only defending the method. Say so; the call is his.
- **Does the run-in read as a reply across 34 years? Yes, and the labels do not fully stop it.** 1979 beat 7 (83.94 -> 88.10): "Well, he feels that he was strict. I'm glad he said it. Now I'll say it, yes." Right after Joe's "I'm glad I was tough," the two "I'm glad" lines rhyme. The ear hears "Michael responding to his father's 'I'm glad I was tough'". Michael died in 2009; Piers is 2013.
  - **MAJOR:** the on-screen fix (years on screen, never "answers") is necessary and not enough on its own. The adjacency does the work, not the captions. The V1 "viewer gets" paragraph and the arc line already say "both of them answered the same question on camera, decades apart", which is true of the question (too strict?) and not of the order of replies. Keep that wording for the title/description, never "answers each other".
  - Also: "he feels that he was strict" in 1979 refers to something Joe had said. The file shows the ABC doc cutting to a later-era Joe cutaway at 73-75 s (`sheet_1979.jpg` frames 2-3). The 1979 file is therefore itself an ABC re-edit ("MICHAEL JACKSON" bug), not a raw 1979 broadcast. The "1979" label rests on an IG caption (9 Dec 1979) the notes themselves say to "confirm".
- **Better ordering (my pick):** 1 -> 2 -> 3 -> **6 (Joe 2013)** -> 5 (Katherine) -> 4 (card) -> 7 (Michael 1979). Joe's "glad I was tough" lands directly as the real man's own answer to the film's Joe ("look me in the eye"); Katherine's "you can't whoop nobody" and the card sit between him and Michael, so the "I'm glad" rhyme is no longer back to back, and the card's "not easy firing your father" leads into Michael's "yes". If the card sits last-but-one, the 1979/1983 ambiguity in finding 1 is also the last thing the viewer reads before the end. If that worries him, keep the old order but insert a 0.5 s black / SFX break between 6 and 7.
- Alternative already in the file (drop Joe, 1-2-3-4-5-7, ~26 s) is the cleanest on the answer-across-34-years risk. I would run it as the safe version if Joe's 2013 audio is slurred on listening (the file already flags it).

## 3. Quotes and times in the V1 table

All word-time checks below are against the files.

| Beat | Check | Result |
|---|---|---|
| 1 | "I need you to fire Joseph." 142.37 -> 143.63; "You're gonna fire your dad." 148.39 -> 149.21; "How would you like me to do that?" 151.31 -> 152.22; "Quickly." 154.38 -> 154.74 | quotes exact. **MAJOR (dead air):** the table says the 2.2 s hold was "tightened" but the in/out is still 151.31 -> 154.74 (3.43 s) and the 3.4 s in the header equals the untrimmed length. The hold is 2.16 s (152.22 -> 154.38), over his 2 s rule. Fix: write the trim into the table (for example 151.31 -> 152.22 + 153.3 -> 154.74, about 2.3 s) and recompute. |
| 2 | 72.70 -> 74.00 question, "Yes." 75.22-75.62, "No, he's going to kill me." 76.46 -> 78.02 | exact; internal gaps 1.22 s and 0.84 s (under 2 s, but they are laugh/pause; tighten if it drags). 5.3 s ok. The Joe cutaway at 73-75 is already flagged. |
| 3 | 195.10 -> 201.53 "The boy fired me with a piece of paper. A piece of paper, couldn't even be man to man, huh? Look me in the eye and do it." | exact, 6.43 s ok. Internal gap 197.38 -> 198.32 (0.94 s) fine. |
| 4 | card | see 1 |
| 5 | "He's grown." 215.37 -> 216.15; Katherine 224.63 -> 228.98 ("You can't whoop nobody." 224.63-225.88; "You can't beat nobody." 227.80-228.98) | quotes exact. **MINOR (repeat, NOT fixed from the last cold read):** the 1.92 s silence 225.88 -> 227.80 is inside the span. The sheet (`sheet_film_joe`, 224-228) shows Joe listening between the two lines. The table's 0.8 + 4.4 hides it. Also "He's grown" is over Joe's face (215-216 frame is Joe) and Joe's "What'd you say to me?" (216.67-217.33) is dropped, so Katherine's answer has no question. Fix: trim the gap to about 0.4 s (total about 3.7 s), or restore 216.67-217.33. |
| 6 | see 2 | exact; trim gaps |
| 7 | 83.94 -> 88.10: "Well, he feels that he was strict." 83.94-85.34; "I'm glad he said it. Now I'll say it, yes." 85.92 -> 88.10 | exact; 4.16 s ok. |

- **Sum:** 5.5 + 5.3 + 6.4 + 3.0 + 5.2 + 9.3 + 4.2 = **38.9 s**. The header says "≈ 38 s" and the Variants table says "~40 s". After the fixes above (beat 1 -1.1 s, beat 5 -1.5 s) it is about 36.3 s. Use one number.
- Within the 2 s dead-air rule after trims: only the beat 1 hold and the beat 5 gap break it, plus 0.96 s and 0.92 s gaps in beat 6.

## 4. Runner-up 3b "Burn + Joe"

- **The film line is quoted right.** `film_ZVhqwZQSVQ0.words.json`: "Mr. Jackson, your son almost died." 29.62-32.40, then Joe "I know that." 32.60-33.06, "...I know my part." 38.72, **"And the only thing that's going to heal him is by getting back on that stage." 39.38 -> 42.26**, "That's where he lives." 42.52-43.24. The sequence's quote is exact. It joins the doctor's line and Joe's answer; Joe does not answer immediately (about 7 s of "I know that / if that fire had caught his clothes... I know my part" in between). A caption "your son almost died -> Joe" skips that; the film-side cut should keep "I know that."
- **Weaker than the firing on his filter, not stronger.**
  - Firing: 5 film beats at 1.3-6.5M on YouTube plus the real 1979 line (3.79M). That is 2+ beats on the same moment and each on the exact beat in the cut.
  - Burn + Joe: the film side has exactly one beat (Scene Arc 1,053,164, just over 1M). The real side's 4.66M and 2.02M are rehearsal footage, a different moment from the hospital scene. So it has 1 beat on the exact moment, 2 on the real event.
  - The real side never has Joe's words. The real footage is Michael rehearsing, not the father saying "the only thing that will heal him...". The beat is a film line paired with real pictures, so the real Joe/first-party voice is absent, and the format's "real people answer the actors" is not delivered.
  - Against: the burn movie-vs-real join already exists (SLY 6.13M / 4.50M) and our own Short (94K) used the burn lines. Rehearsal quality is unchecked.
  - Instagram: 0 either way (no IG figure for either).
- Fine as the labelled runner-up, no stronger. The note's own phrase "Runner-up worth sourcing" is right. Do not describe it as a "stronger" alternative anywhere.

## 5. Verdict block and gate table

Stated more strongly than the evidence:

1. **"Michael fired his own father as his manager"** (the viewer-gets line) is stated flat. Fine for 1979 in the notes' sources; it conflicts with the Insider timing in finding 1. "Michael fired his father" is supported; "as his manager" in 1979 rests on search summaries of Guardian / Biography.com / Wikipedia (the cell says they were blocked).
2. **"The real Michael answers it on camera"** (Why-this-topic #1). The 1979 line answers a strictness question, not the firing; the cold read already said "Michael's real answer to the firing does not exist in our files". Reword to "the real Michael on his father's strictness".
3. **G5 Facts "PASS with care"** rests on one fetched page. "PASS" is too strong; use "PASS on the quote, OPEN on which firing / year".
4. **G4 Freshness "PASS for the join"**: the "no movie-to-real firing found" is from searches r03/r06; say "none found in our searches". The claim itself is a 995K Short and the 3.68M farewell join exists. OK as written, just not "PASS" without the qualifier.
5. **Source quality "PASS"** while the same cell says Piers audio is -28.5 LUFS and the September notes called Joe's audio slurred: should be "PASS pending a listen". Also the 1979 file is an ABC bug retrospective (needs the crop the notes mention).
6. **Rights**: the cut is Lionsgate film audio + ABC + CNN. "his call" is right.
7. The verdict opening block is honest on bar and Instagram (0). Good. The "farewell as what could beat it" paragraph is fair.
8. "His floor: 2 viral beats" holds for YouTube only; the file states it. Fine.

## Findings list

1. **MAJOR** Beat 4 card: single unsaved source; firing/year unresolved (Insider "superstar" timing vs 1979 label); save the page, add a source tag, keep the year off.
2. **MAJOR** Beats 6-7: the adjacency reads as an answer across 34 years; reorder (6 earlier, card between) or insert a break; keep "answers" out of every caption.
3. **MAJOR** Beat 1: the 2.16 s hold is still inside 151.31 -> 154.74; the "tightened" note is not in the numbers.
4. MINOR beat 5: 1.92 s gap and the missing question (repeat finding).
5. MINOR beat 6: trim two ~0.9 s gaps; ending cut before "kids everybody loved".
6. MINOR total 38.9 s vs "≈ 38" / "~40".
7. MINOR gate words: "answers it", "PASS" on Facts and Source quality.
8. MINOR 3b is weaker than the firing on proof and has no real Joe voice.

## Price

Centre ~70K, band 30-200K, tails 12K-600K, P(>=1M) ~2%. It stays below the 150K bar and the Instagram proof is 0 for both sides. Send as a card with the fixes, not as a pick.
