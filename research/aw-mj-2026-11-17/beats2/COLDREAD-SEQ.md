# Cold read of SEQUENCE.md v1.1 ("Michael fires his father"), 17 Nov 2026

**VERDICT: SEND AFTER FIXES.** As built it cannot go: beat 8 fails Affan's own 8 Nov source rule. The verdict block is mostly honest, but it overstates Instagram proof, and the 1979 to "fired his father" card chain says more than the files show. With the ending swapped to material already on disk, it goes to him as a card, not a pick, at centre about 90K.

Judged from files only (no web, no playback). Read: SEQUENCE, PAIRS, COLDREAD-PAIRS, the three word files, the 1979 transcript, the four frame sheets, `api/` stats and comments, PITCH-CHECKLIST (head), IG-TOP.

## 1. Quotes and times vs the word files

Checked against `asr/*.words.json` and `fTTl4Vaow5Y.fw.txt`. Every quote is exact and no cut lands mid-phrase.

| Beat | In/out | Check |
|---|---|---|
| 1 | 142.37-143.63 | "I need you to fire Joseph." Exact. |
| 2 | 148.39-149.21 | "You're gonna fire your dad." Exact. **Skipped between beats 1 and 2:** 146.65-147.05 "You're dead." (lawyer). Harmless, but note it is dropped. |
| 3 | 72.70-78.02 | Question 72.70-74.00, "Yes." 75.22, "No, he's going to kill me." ends 78.02. Exact. |
| 4 | 83.94-88.10 | Exact. Skips the interviewer's 79.98-82.42 line ("still worried about that at your age?"), the antecedent of "he feels that he was strict". |
| 6 | 195.10-201.53 + 202.47-204.11 | Joe's quote is exact (ASR "fill my belt", it is "feel"). Two internal pauses are kept: 197.38-198.32 (0.94 s) and 199.99-200.59 (0.6 s). Fine as drama, but the dead-air gate will flag them. |
| 7 | 215.37-216.15 + 221.25-225.88 | Words exact, but **see finding M5**. |
| 8 | 5.68-16.51 | **The table quote starts "I'd like to say", but the in-point 5.68 is "Listen up,".** "I'd like" starts at 6.60. Either quote "Listen up" or move the in-point to about 6.5 (saves 0.9 s). |

**M5 (MINOR): beat 7.**
- Joe's "What'd you say to me?" (216.67-217.33) is dropped, so "I said you can't do it no more" has no antecedent.
- The stated duration is 1.2 + 3.3. The real in/out is 0.78 + 4.63 = 5.4 s.
- At 215-216 the picture is Joe listening (`sheet_film_joe.jpg`). Katherine is on screen only from about 218. The table lays the 220-224 picture over audio from 215.37, so "He's grown" will not sync.
- Fix: put 216.67-217.33 back in, or start the second span at 221.25 and show Katherine on "He's grown" by a cutaway. Then re-time.

## 2. The hook (beats 1-2)

**PASS, with one caveat.** "I need you to fire Joseph." (142.37) followed by "You're gonna fire your dad." (ends 149.21) gives a son firing his father by about 2.2 s.
- **Caveat (MINOR):** nothing names Michael or the film until after 3 s ("none for 0-3 s"). A stranger sees an unlabelled actor in sunglasses. The title carries "Michael Jackson". The first frames should show the 2026 film label small, or a top line "HE FIRED HIS OWN FATHER", to stay honest and not read as real footage.
- Do not shorten the 2.2 s any further.

## 3. The cards

**M2 (MAJOR): "THAT SAME YEAR, HE FIRED HIS FATHER AS HIS MANAGER."** The card says things the files do not settle.
- **The files contradict each other.** PAIRS (lines 43-44 and 58-60) says sources vary 1979/1983, that "the '1979, at 21' version is a blog claim: don't use it", and "use 1983". SEQUENCE v1.1 reverses this on the strength of the Guardian obit (via inkl), Biography.com and Wikipedia. It does not record the reversal or open the contest. Any of 1979/1983 on screen without both pages saved in the job is an unverified claim about a named person.
- **"THAT SAME YEAR" implies a sequence.** The interview was filmed on 9 Dec 1979 (an IG caption, per the file, "confirm"). If Michael left his father's management when his contract ended at 21 (Aug 1979, per PAIRS), the firing came months BEFORE the interview. Then "he's going to kill me" is not followed by the firing.
- **Fix:** card = "1979: HE DROPPED HIS FATHER AS MANAGER", or "IN 1979, HE LEFT HIS FATHER'S MANAGEMENT". Drop "that same year". Save the Guardian and Biography.com pages (and a NYT page that actually opens) into `api/` or a `facts/` file before sending.
- **Beat 5's picture is not 1979 Joe.** In `sheet_1979.jpg` the Joe cutaway (frames 2-3: wood panelling, suit, an older face) is a much later Joe, not 1979 footage. It is also mid-speech with no audio under it, with the ABC bug on it. Over a card about 1979 this implies the wrong year. The sheet has no timestamps, so "~75 s" is not verified. Fix: no face; use type on the black plate, or label it "JOE JACKSON, LATER".
- **Film-only claims:** the cards are correct. Every film beat is labelled THE 2026 FILM. Branca's "first job" and the lawyer's scene are not asserted. No card says Joe was at the stadium or that the brothers did not know. Good.
- **The arc line "why: he was afraid of him" (the label "WHY") is not what the 1979 interview says** (see M3).

## 4. Honesty of the verdict block

**M1 (MAJOR): the Instagram proof is overstated.**
- The file says "only 1 of 3 on Instagram". The 1 is the REAL Dodger tape (`DUrkSxtjZbT` 1.2M likes). The cut does not show that moment full-frame; it fails his ≥720p rule and is at most a 2 s optional insert.
- The film farewell has no Instagram number. The 1979 clip on IG is `Cl9IHmXJ3aT` at 23K (under 65K). The firing scene has 10 likes.
- PAIRS' own rule says "a lane's numbers do not count for a beat they don't contain".
- **Honest count as built: Instagram 0 of 3. YouTube 3 of 3, but only 2 are buildable at spec: the firing 4.0M and the 1979 line 3.79M.** The 12.0M (`1IEe8hdYv1o`) is beat 8, which fails the source rule. Under his first filter (Instagram), this sequence has no proof.
- Also unmentioned: `cNN3cSzT1aQ` "When Michael Fired Joe Jackson", 1.3M, 1:40 (in `p01_fired_stats.json`). It is a title-level near-duplicate that nobody read. Source and content are unknown; add it to freshness.

**B1 (BLOCKER): beat 8's source.** The file states it plainly, but not in the headline. The headline lists only two FAILs, not this third one.
- `1IEe8hdYv1o` is a 24 s fan upload by Music Central, 480x854, -11.2 LUFS. It is a re-cut of another channel's upload (checklist § 2) and fails the ≥720p rule. The HD copy is "queued", not on disk.
- The words "Y'all have been wonderful" differ from the real tape ("You all been wonderful"), so this really is the film.
- It cannot ship as built.

**Film-dialogue share (MINOR, miscounted).** The file says "about 30 s of ~38 s". Summing the actual in/out:

| Beat | Seconds |
|---|---|
| 1 | 1.26 |
| 2 | 0.82 |
| 6 | 6.43 + 1.64 = 8.07 |
| 7 | 0.78 + 4.63 = 5.41 |
| 8 | 10.83 (9.9 if trimmed to "I'd like") |
| **Film audio** | **26.4 s** |

- Real Michael: 5.32 + 4.16 = 9.48 s (the file's 9.5 s is right).
- Cards and Joe cutaway: about 3.7 s.
- Total about 39.6 s, not 38. Film audio is about 67 % of the Short, not about 79 %. The correction helps the case slightly, but the headline numbers should be right.

**Other honesty points**
- **Rights FAIL names only Lionsgate.** The 1979 file is an ABC special re-air with an ABC bug and a "MICHAEL JACKSON" bug in frame. The ABC audio is also a Content ID match. Name it, even though the 1979 Shorts at 3.79M and 2.29M exist.
- **The file contradicts itself.** The verdict says "NO PICK", but the variants table says "pick (as the card)". Say "card, not a pick" in both places.
- **The "not max effort yet" list omits the Fable advisor** (twice), which the max-effort gate requires. Add it.

## 5. Minors, censor words, living people

- **Minors: none.** The 1979 Michael is 21. The film spans are adults. I did not check every frame of the Joe cutaway (assumed adult).
- **Censor words:** "kill me" is hyperbole, not self-harm or drug content, so the censor rule does not apply. "Belt" and "whoop" are film dialogue about corporal punishment and are fine. If the Short gets reviewed for ad safety, the "kill me" and "belt" pair is the soft spot. Not a blocker.
- **Katherine is alive (96).** Beat 7 puts "You can't whoop nobody" in an actress's mouth. It is labelled THE 2026 FILM, which is enough. Do not add a card that says she "stood up to him". The label "KATHERINE" with a film actress's face is acceptable only with "THE 2026 FILM" on it, and it must stay on screen for the whole beat.
- **La Toya:** not used. Good.
- **Joe (d. 2018):**
  - The only content about him is film dialogue, and the quotes are labelled.
  - Never say "abusive" in our words (the "abusive" in the comments is theirs).
  - The arc's "Joe's fury" is the film's depiction, so keep it in the film label.
- **Unverifiable:** "(he started at 5)" appears in the shape paragraph. No card carries an age, which is correct. Keep it that way.

**M3 (MAJOR): the 1979 line is a joke about answering on camera, not a statement of fear.**
- The transcript has "Yes." and then "No, he's going to kill me." with Michael laughing (`sheet_1979.jpg`, every frame).
- Beat 4 then says "Now I'll say it, yes", so the exchange is "yes he was strict, I won't say so, he'd kill me (joking), ok I'll say it."
- Earlier in the same interview (43.21-53.17) he calls his father "always wonderful" and says "strong parents are very important".
- The viral uploads (3.79M, 163K) read it as fear. The sequence uses that reading as the "WHY", with no source tying fear to the firing.
- **Fix:** do not call the 1979 beat "why". Drop the WHY label. Keep both beats 3 and 4 (with the pair as the only way to show he says "yes"). Keep the beat 3 label as MICHAEL · 1979 INTERVIEW, and do not add a caption that reads a mood onto it.

## 6. A better ending than beat 8

**Yes, and it is already on disk: the real "Now I'll say it, yes" (1979, 85.92-88.10) as the final line.**
- **Order:**
  1. Hook, beats 1-2: film "fire Joseph", "fire your dad" (about 2.2 s).
  2. Film Joe: "The boy fired me with a piece of paper... gonna feel my belt" (beat 6).
  3. Film Katherine: "He's grown." / "You can't whoop nobody" (beat 7, fixed per M5).
  4. Card "IN 1979, HE DROPPED HIS FATHER AS MANAGER" (per M2) on a plain plate.
  5. The real 1979: "Do you think your father was too strict?" "Yes." "No, he's going to kill me." Then 83.94-88.10 "Well, he feels that he was strict. I'm glad he said it. Now I'll say it, yes."
- **Why it is better:**
  - Every source is already on disk at 1080p with clean audio. It passes the ≥720p rule and drops the beat 8 BLOCKER.
  - The real Michael speaks last, which is the strongest first-party moment. The film is the act, the real voice is the payoff.
  - It ends on his own "yes": his side of the father story, the only thing in the file that is truly his.
  - Total about 30 s. Film share falls to about 55 % and the real voice rises to about 32 %.
- **The cost:**
  - YouTube viral beats become 2 (4.0M + 3.79M). That still meets his "at least 2".
  - The 12.0M beat is lost, and the Instagram count stays 0.
  - The tone WEAK on the 1979 clip stays (she is laughing).
- **Option B, simpler:** end on beat 7's "You can't whoop nobody." and cut beat 8. It is about 27 s, all on disk at 1080p, all film, so first-party share is lower than the file's 24 %. I prefer the 1979 ending because Michael speaks last.
- **Not recommended:** the real Dodger VHS as an ending (he rejected that family on 8 Nov). Also not `xOnrLJuXt5w` (480p, 403).

## 7. Price and agreement

- **Centre 90K, range 40-220K, tails 15K-800K.**
- The file's 120K centre assumes the 12.0M farewell. If beat 8 moves out, the "film clips plus 3 actors" read gets stronger, and the "fired his father" claim is already a 995K text Short and a 999K film re-up.
- The father lane is the second in a row, and the Dad Short is at 57,295 at about 17.5 h.
- **I agree with NO PICK under the 150K bar.** I would send it only as a card, with the beat 8 swap and the M1/M2/M3 fixes written first. I would not call it a pick.
