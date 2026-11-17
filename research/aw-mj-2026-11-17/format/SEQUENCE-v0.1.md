# Movie ↔ real: "The Day Michael Fired His Father" — SEQUENCE TEXT draft v0.1 (17 Nov 2026, ~23:05 PKT)

**Status: DRAFT, not sent.** Pending:
- the Instagram film-scene read (`IG-FILM.md`);
- Joe's Piers Morgan 2013 question and word times (`beats2/asr/real_piers2013`: queued behind the shared ASR lock);
- Katherine 60 Minutes (queued);
- the text cold read of the topic ranking;
- the final cold read;
- the advisor.

## Why this topic for the format (ranking: `FORMAT-MAP.md` § Scoring)
The firing is the film's most clipped scene, and it's the one where the real people answer the movie on camera:

- **The film:**
  - Crowd reaction "funniest part" 6,506,412.
  - "Crowd Reaction to THIS part" 4,118,584.
  - JoBlo 4,008,251.
  - Scene Arc 2,667,746.
  - Michael Trapson "When Michael Fired Joe Jackson" 1,305,035.
  - Re-up 999,938.
- **Real Michael:** the 1979 "he's going to kill me" clip, 3,790,519.
- **Real Joe:**
  - On being let go: "I was there until the contract expired."
  - On being too strict: "I'm glad I was tough."
- **Nobody has done it as a movie → real story.** r03 "...movie vs real life" Shorts and r06 found side-by-side Joe/Colman comparisons only (DailyTea "Is Colman Domingo the perfect choice for Joe Jackson?" 1,356,511).

## V1 — movie → real → movie → real (≈ 40 s)
| # | ~s | Side · label | Words | Source in → out | Proven / ours |
|---|---|---|---|---|---|
| 1 HOOK | 1.3 + 0.8 + 3.4 | MOVIE · no label 0-3 s, then "THE MOVIE (2026)" | Michael: "I need you to fire Joseph." Lawyer: "You're gonna fire your dad." "How would you like me to do that?" "Quickly." | FILM-F 142.37 → 143.63, 148.39 → 149.21, 151.31 → 154.74 | PROVEN: "The funniest part was when he said to Fire his dad Joe and to make it as quick as possible" 17,002 likes on the 6.5M; "Quickly." 2,902 |
| 2 | 5.3 | REAL · "THE REAL MICHAEL · 1979" | "Do you think your father was too strict?" "Yes." ... "No, he's going to kill me." | 1979 72.70 → 78.02 | PROVEN 3.79M |
| 3 | 6.4 | MOVIE · "THE MOVIE" | Joe: "The boy fired me with a piece of paper. A piece of paper, couldn't even be man to man, huh? Look me in the eye and do it." | FILM-F 195.10 → 201.53 | PROVEN (same scene; "PEAK Karma... piece of paper" 5,503) |
| 4 | ~9 | REAL · "THE REAL JOE · 1980s" | "Like all the kids, when they reach a certain age, you know, they want to do things on their own... As far as managing the kids, I was there until the contract expired." | JOW 1165.1 → 1191.0 (trim the middle; Joe on camera 1170-1185, then B-roll) | OURS (Joe's version) |
| 5 | 0.8 + 4.4 | MOVIE · "THE MOVIE" | Katherine: "He's grown." ... "You can't whoop nobody. You can't beat nobody." | FILM-F 215.37 → 216.15 + 224.63 → 228.98 | same scene |
| 6 | ~3.5 | REAL · "THE REAL JOE · 2013" | "I'm glad I was tough, because look what I came out with." | **Piers Morgan, CNN, 30 Jan 2013, clean file** `H Michael Jackson's Father, Joe Jackson - Piers Morgan Interview January 30, 2013.mkv` (1440x1080): the line found at **224.3** by audio match against the doc (JOW 813.0; score 0.178); Joe on camera 223-228 under the CNN lower third "MY KIDS WERE BROUGHT UP TO RESPECT PEOPLE"; Piers asks the question at ~217-222 (words pending ASR); -28.5 LUFS (quiet: gain at build) (`sheet_piers_224.jpg`) | OURS (Joe's denial lane: 1,485,553) |
| 7 BUTTON | 4.2 | REAL · "THE REAL MICHAEL · 1979" | "Well, he feels that he was strict. I'm glad he said it. Now I'll say it, yes." | 1979 83.94 → 88.10 | OURS: the real son answers the real father |

The pattern is MOVIE, REAL, MOVIE, REAL, MOVIE, REAL, REAL. Michael gets the last word, not Joe. Every film beat is labelled THE MOVIE.
The cut never states a film-only detail as fact, never says "at 21", never calls the 1979 line fear (he laughs), and never presents
Joe's "contract expired" as a lie.

## Variants
| Variant | Order | For | Against | Verdict |
|---|---|---|---|---|
| **V1** | M "fire Joseph… Quickly" → R Michael 1979 "too strict? Yes… he's going to kill me" → M Joe "fired me with a piece of paper" → R Joe "until the contract expired" → M Katherine "He's grown" → R Joe 2013 "I'm glad I was tough" → R Michael 1979 "Now I'll say it, yes" | the most proven moment first (6.5M "funniest part"); every movie line gets a real answer; Michael has the last word | 7 beats in ~40 s; Joe's 1980s line is long (trim); Piers audio is quiet | **lead** |
| V2 | R Michael 1979 cold open → M firing → R Joe contract → M Joe "piece of paper" → R Joe "glad I was tough" → R Michael "yes" | the real man first; the question is the hook | a laughing hook; the proven film moment lands at 6 s | runner-up |
| V3 (short) | M firing → R 1979 → M Joe "piece of paper" → R Joe "until the contract expired" (END) | ~25 s; ends on the twist (the father's version) | Joe gets the last word: the drama cold read's "middle of that fight" risk | third |

## Topic ranking for this format (from `FORMAT-MAP.md` § Scoring; searches r01-r07, 37/42 today)
1. **The firing**: film 6.51M / 4.12M / 4.01M / 2.67M / 1.31M; real 1979 3.79M; real Joe ×2 (ours). 2+ viral beats; 3 collisions; no
   movie→real version found.
2. **Pepsi burn**: proof is the biggest (film 1.25M + Joe-asks 1.05M; real "Burn Center Story" 16.9M, "Hair Caught Fire" 4.0M,
   "Rehearses Just Days After" 4.66M / 2.02M), BUT the movie-vs-real comparison already exists (SLY 6.13M and 4.50M, Slay World 2.57M), and
   the real Katherine/burn-centre lines were our "Burnt Hair" Short (94K). Joe's real voice on the burn: none found.
3. **Nose**: film "GO ON, BIG NOSE." 881K, JoBlo 640K; real "Dad Hated His Nose" 968K, "Oh You're So Black, You Have Such a Big Nose"
   811K: close, but no single beat at 1M+; "you want to die" needs censoring.
4. **Farewell**: film 12.0M + real IG 1.2M likes, but the real tape is the VHS he rejected.
5. **Berry Gordy audition**: film 6.27M; the real audition shows Michael at 9-10 (minors).
