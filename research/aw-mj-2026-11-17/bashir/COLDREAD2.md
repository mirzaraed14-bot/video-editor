# Cold read 2: Bashir card (SEQUENCE.md v1.0), 17 Nov 2026

Files only (no web, no playback). Checked: `asr/tt_215`, `tt_4323`, `tt_4620` word times; frames `tt_angry_4318`, `tt_jerk_4620`, `tt_diana_217`; `STATEMENTS.md`; `api/b20-b22`.

**VERDICT: SEND AFTER FIXES, as a below-bar card (centre 55K, range 12K-500K). Most fixes are text-only; the ear check on beat 1 needs one listen.**

## Findings

### 1. New hook (beat 1, TT 4328.56-4331.78)
Words exact (`tt_4323`: I 4328.56 ... suffer. 4331.78). It pairs with beat 2 far better than v0.2's "he trusted".

1a. **MAJOR: the V3 fallback does not hold up.** If the voice is the host's, SEQUENCE says "lead with V3". V3 (William cold open) still contains beats 1 and 2, so the "SAME MAN" label is false in V3 too. V3 also needs William, who is not downloaded, so the fallback has no source today. Fix: state the host-case rule: drop beat 1 and the "SAME MAN" label (or the pair), and make the ear check a gate that blocks the label.
1b. **MAJOR: the voice evidence is weak and the label rule rests on it.** Frame `tt_angry_4318` 01:11:58 shows Take Two using "Voice Of Martin Bashir" on a documentary-narration quote, and plain "Martin Bashir" on the "restricted" card at 01:12:04-13; the plain-label-means-host reading is not borne out by the frames. The pitch test (96 Hz vs host 120-125) is plausible but weak. v1.0 does make the label conditional, which is honest: keep that, and do not ship the label before the listen.
1c. **MINOR: cold-viewer read.** "his children" with Michael alone and no antecedent reads as a charge of cruelty against Michael for the first 3 s. The cut-off sentence ("They are restricted... overly protected", 4325.57-4327.91) is what narrows it to restrictions. The payoff at ~3.2 s reverses it. It is his call (allegations lane); say so in the hook note.
1d. **MINOR (open from read 1): picture.** Adult-only Michael + Bashir walk is ~2.4 s for a 3.2 s hook; a freeze or another shot is needed, not stated in v1.0.

### 2. Beat 3 (Povich splice + statement text)
Words exact: "But who is Martin Bashir?" 216.89-218.29 (Bashir 217.89-218.29); "In 1995, ... affair." 225.84-234.67 (`tt_215`). The 7.5 s cut between them removes "and how did he get an exclusive interview with one of the most reclusive pop stars", which is fine: "this little-known British journalist" reads as the answer.

2a. **Spoken link: FIXED.** "Martin Bashir" and "journalist... Princess Diana" are both in voice, one sentence apart. Residual: see 5a.
2b. **On-screen quote is exact** against `STATEMENTS.md`. The ellipsis hides "that his would be an honest and fair portrayal of my life": the omitted clause is Michael's complaint, not a favourable fact, and the ellipsis is shown. Acceptable. Label it a written statement via his representative, not speech.
2c. **MAJOR: text over voice is not readable in 10 s.** 19 words on screen against ~21 spoken words, carrying different information (voice: journalist, Diana, affair; text: persuaded me to trust him). Fix: show only "the man that turned Diana's life around." plus the attribution over the "In 1995" sentence; or fade the first half in over 217.89-218.29 and hold it through the gap.
2d. **MINOR: picture.** TT 225.84-229 is 3:45.8-3:49, the crowd shot with boys (`tt_diana_217` 3:45-3:47); v1.0 skips it but does not say what covers ~4 s. Diana window 3:49-3:55: the tabloid cover ("TRUTH ABOUT HER LOVE AFFAIR") sits over it from 3:53, so use 3:49-3:52.

### 3. Button (beat 5, TT 4654.77-4666.28)
3a. **Words exact** (`tt_4620`). Frames `tt_jerk_4620` 01:17:08-48: Michael in teal, alone, no children; credits start 77:50, so the out at 77:46.3 is clear. Internal pauses 4656.19-4657.15 and 4660.46-4661.94 (~2.5 s of the 11.5 s): tighten.
3b. **"OURS" is supported:** b20 returns 241 / 179 / 172 views; b21 and b22 return empty.
3c. **MAJOR: it still implies Bashir is the "jerk".** The "lie" echo is gone, but "some jerk, some mean-spirited person to try to bring you down" lands straight after the William forgery card and Michael's trust statement. Michael's actual context is general ("Do you sometimes despair of human nature?" 4622.88, then "no matter what you do, there's always somebody that will say something about it" 4641.57-4645.19). "Nothing in the cut says Bashir lied to Michael" is true of captions, not of effect. Fix: either name it in the pitch as a deliberate join (not "never implied"), or end on "No matter what you do, there's always somebody that will say something about it", which accuses nobody.
3d. **MINOR: "MICHAEL · 2003".** 2003 is Take Two's air date, not necessarily when the interview was filmed; use "MICHAEL JACKSON" or "TAKE TWO · 2003".

### 4. First-read BLOCKER/MAJOR status
| First-read item | Status in v1.0 |
|---|---|
| 1a BLOCKER: Bashir link not spoken | **Mostly fixed** (Povich names him); the forgery link is still carried by a card, see 5a |
| 1b MAJOR: hook paid off by word echo | **Fixed** (new hook, "jerk" button); an implied join remains, see 3c |
| 1c MAJOR: William beat not understandable | **Partly fixed**: beat 3 text and the card help, but the card names neither Bashir nor the BBC |
| 1d MAJOR: contradiction arguable | **Partly fixed**: sharper pair, but "restricted" still cut and "opposite" overclaimed, see 5b |
| 3 MAJOR: William "official" | **Fixed** (line 39: fan/news channel) |
| 3 MAJOR: William's words unverified | **Open**: Yahoo text only, download pending |
| 4 MAJOR: Take Two clips already out (419,508 / 260,627 / 87,665) | **Open**: listed in G4, contents still unread |
| 4 MAJOR: join already exists as 2021 news | **Acknowledged** (G4), not used |
| 5b MAJOR: implies Bashir deceived Michael | **Partly fixed**: title clean, effect remains, see 3c |
| 5f: Fox music bed under voice | **Open** (named, stem test not run) |
| 5g: source sharpness / recipe test | **Open** (named) |
| 6 hook not a claim | **Fixed** |
| 7 price 90K to 55K | **Fixed** |
| 8 gate items and "NOT max effort yet" opening | **Fixed** (opens honestly); items themselves open |
| Flag `asr/tt_4318.words.json` as bad | **Not done** |
| AFRAID 176K / DISRESPECTFUL 86K / La Toya 17K | **Not done**: v1.0 still says 167K / 80K / 19K |

### 5. New defects
5a. **MAJOR: the Bashir-to-forgery step is carried by a card, not by any voice.** Povich ties Bashir to Diana; William never names Bashir or the BBC; the beat 4 card "2021: AN INQUIRY INTO THAT DIANA INTERVIEW" does not say whose. The Dyson findings do name Bashir (fake bank statements shown to Spencer), so naming him in the card is sourced fact. Fix: "2021: BBC INQUIRY INTO BASHIR'S DIANA INTERVIEW", sourced to Dyson.
5b. **MAJOR: "the viewer gets" and G1 claim Bashir said "the opposite of what he aired".** Angry at the children's suffering and almost weeping at their bond are, by v1.0's own line 79, compatible. "SAME MAN" is fine; "opposite" is not. Reword to "said two things" or keep the "restricted" context in the cut.
5c. **MINOR: beat 2 still has the 1.56 s hole (4338.00-4339.56) and the unresolved "I love you" (2206.67-2207.80, speaker unknown);** both were in read 1 and are not carried over.
5d. **Length:** hook 3.2 + beat 2 7.9 + beat 3 10.2 + beat 4 ~6.5 + beat 5 11.5 = ~39 s; after the pause trims it lands near 35 s.
5e. **Numbers:** every figure I could test is in the files (b20 241/172, IG table, William 327,505, ITV 951,567, beat durations). Web-only, not in any file: Panorama 22.8M viewers, Take Two's 20 Feb 2003 date and probe values, Press Gazette / The Week / AP / Irish Times / Yahoo pages. "7 likes" and the 20 Nov 1995 anniversary come from `IG.md`.
