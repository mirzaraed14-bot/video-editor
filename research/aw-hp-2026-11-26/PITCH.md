# PITCH v3 (AW Harry Potter, 26 Nov 2026): the EMMA WATSON angle, on Affan's direction ("try to make a text sequence for the emma watson angle")

**NO PICK: the anchor test is not run, and the hook exists only at 640x360 (face ~120 px).** Her own telling is on camera (HeyUGuys, Nov 2010). Bonham Carter's side was not found on camera. The best Watson version is below, **locked centre 100K (below the 150K bar)**. It gets built only if the 360p box passes a Topaz + Prince-ABC anchor test and Affan accepts it.

**First, the finding Affan most needs: "HATED" is not her word.** The bank title came from a 28.8M GSA Short that is a narrator. In her own words (Nov 2010), the torture scene was "very intense… but I'm really glad with how it came out". In a DH2 featurette she calls Helena Bonham Carter "a really important mentor to me on this last movie", and says that after one dinner with her she "went home and wrote down everything that she said".

NOT max effort yet:
1. **Picture (the deciding item):** the hook source is HeyUGuys' Nov 2010 interview (`jP-p3QM9dWk`). It is **640x360** (VP9, 25 fps; `src/jP-p3QM9dWk_heyuguys_watson_v.mkv`; frames `proof/heyuguys_full.png`, `proof/sheet_heyuguys.png`: black satin top, headband, "HP7 PART 1" backdrop). Her face is ~120 px tall.
   - It can only run as the house's centred 16:9 box on a blurred twin (~1.7x upscale), never full-frame 9:16.
   - It runs only after a Topaz test against the Prince-ABC anchor (not run). Audio is -28.2 LUFS and clean.
   - **Every 2010 telling found is this same interview:** Collider's 4.2M Short is a 608x1080 cut of it. Checked, without the passage: ClevverTV (2:00, 7:04, HD) and IGN's cast video (HD). **Not pulled:** TIME's HD "10 Questions" (`7XK6FYKDzXc`, reader questions), which might hold an HD telling.
2. **Bonham Carter's own side of the scene: not found on camera.** Checked:
   - her four 2010 sit-downs (HeyUGuys, Movies Ireland, ClevverTV, the WB EPK);
   - two 2010 on-set clips (about Bellatrix only);
   - the DH2 role-swap featurette (`KUKULvha5Tk`: its upload has a burned-in "@TheHPfacts" watermark, and the speaker of "I really liked working with her" is off camera, so it is NOT used).

   **Fan "facts" NOT used** (no first-party source):
   - "she whispered are you OK";
   - "made sure they were on good terms";
   - "the cast thought she was really hurt";
   - "the scream was cut";
   - a comment in `c_twHLFlqZ8T8` (3,688 likes) saying Yates called cut the first time and Emma asked to keep going. It is fan-attributed, and it conflicts with her "I'll do it once".
3. **Film insert (beat 2):** no clean HD source of the torture frames is verified yet. Movieclips' official `R2zNRrOXbPY` is the escape clip (3:42), and it may not hold them. `twHLFlqZ8T8` is a 49 s user upload.
4. **Instagram:** Watson keyword phrases return "No results" (5 tried); 16 searches and 22 posts in all. The 3-phrasings-per-beat bar is not met on Instagram.
5. **Ear-check;** the featurette's recording date (uploaded 13 Nov 2011, the DH2 home-video month; she was 20-21).

**Done:**
- Fable advisor on Watson v1 and on v3 (its checks applied);
- 2 cold reads: Sirius, and Watson v2 (5 blocking + 7 minor, applied in v3; v3 itself has not had a re-read);
- word-level alignment of every beat (WhisperX medium.en + wav2vec2).

## The story, first-party only
- **Watson, HeyUGuys exclusive, DH1 junket, Nov 2010, age 20** (`jP-p3QM9dWk` 2:37-3:32; `transcript/jP-p3QM9dWk_heyuguys_watson_0200.*`). Asked how intense the scene "where Bellatrix tortures poor Hermione" was, and how open David Yates was to her suggestion:
  > "It was very intense to film. I was actually surprised by how affecting I found it, but the way we did it is I agreed with him. I said, look, I'll do it once, and I'll do it for real. And he was like, OK. So he set up two, three different cameras. And then he just said, roll. And then Helena and I basically just, like, free-played for like two minutes. And by the end of it, I was a bit of a state. When he called cut, I couldn't stop crying. It's like quite hard when you get yourself into something like that, when the camera stops rolling, to just click out of it. So it was pretty intense, but I'm really glad with how it came out."
- **Watson, "The Women of Harry Potter" (DH2 Blu-ray featurette; upload `j0fBiihIt-8`, 960x720 frame with a **960x536** picture inside the letterbox (cropdetect), no watermark; `transcript/w1.*`; frames `proof/sheet_women.png`):**
  > "Helena was also a really important mentor to me on this last movie. She very sweetly invited me over for dinner and we talked about books a lot… It was such a big evening for me… I've never told her this, but after I had my evening with her, I went home and wrote down everything that she said, everything that we shared. And I actually have a book of important encounters to me, and I write down things that they say… I just, I don't want to forget. So Jo has a page too."
- (Backup) **DH2 press conference, Jul 2011** (`T6K1KLmbfU8`, SD): her best memory is "getting to work with Helena Bonham Carter, both when she tortured me and… playing me essentially".

**Arc (one relationship, Emma and Helena):** she chose to play the torture scene "once, and… for real" → after "cut" she couldn't stop crying → the same woman, Helena, was her mentor on the last film, and after one dinner Emma wrote down everything she said.
**The viewer gets:** the actress in the scene that left Emma Watson unable to stop crying was also her mentor. After one dinner with her, Emma went home and wrote down everything she said.

## The sequence (Variant A)
Word edges are WhisperX on the files named. Ends are the END of the last word.

| # | Voice (low label) | Words | Source, time | Picture |
|---|---|---|---|---|
| 1 (hook) | Emma Watson, 2010 | "I said, look, I'll do it once, and I'll do it for real." | HeyUGuys 176.28-179.94 | Watson in the house box. Labels: "EMMA WATSON · HERMIONE" + "THE BELLATRIX TORTURE SCENE" (gives "it" its context in second 1) |
| 2 | Watson | "And then he just said, roll." | 184.81-186.39 | cut on "roll" to the film: Bellatrix over Hermione on the Malfoy Manor floor, ~2 s of the scream (film audio; HD source OPEN) |
| 3 | Watson | "Helena and I basically just, like, free-played for like two minutes. By the end of it, I was a bit of a state." | 188.25-192.22 + 194.34-197.34 (pauses closed) | Watson; label "HELENA BONHAM CARTER (BELLATRIX)" on "Helena" |
| 4 | Watson | "When he called cut, I couldn't stop crying." | 198.86-201.50 (drop the false start "I couldn't," 197.38) | Watson |
| 5 (turn) | Watson (voice-over), DH2 featurette | "Helena was also a really important mentor to me on this last movie. She very sweetly invited me over for dinner." | `j0fBiihIt-8` 113.96-120.92 | **in the featurette this line is VOICE-OVER** over its own BTS: Helena hugging Emma on set (file 114-116), the two with Yates (117-118), Emma on camera only at ~119-120 (`proof/sheet_women_beats.png`). Use that BTS; skip the film frame at 113 (burned-in "Half-Blood Prince" caption). Label "DEATHLY HALLOWS PART 2 · BEHIND THE SCENES" |
| 6 (payoff, end) | Watson (on camera, white blouse, the whole window) | "after I had my evening with her, I went home and wrote down everything that she said." (+ optional: "And I actually have a book of important encounters to me.") | 145.46-149.91 (+ 152.46-153.22 + 155.14-157.28, pause closed) | Watson; hard cut on "said" (or on "to me") |

- **Runtime (word edges):** 3.7 + 1.6 + 2.0 (film) + 7.0 + 2.6 + 7.0 + 4.5 = **28.4 s; 31.3 s with the book line.**
- **Left out on purpose:**
  - "I just don't want to forget": in the source it is about everyone in her book, not only Helena;
  - "So Jo has a page too": it pulls in Rowling and the dispute;
  - the being-a-woman passage: a second topic;
  - all the fan lore (above).
- **Censor:** none. If the "Mudblood" arm shot appears in the film insert, flag it to Affan.
- **Minors:** Watson was 19-20 filming DH1 and 20-21 in the interviews.

## Variants compared
| | Hook | Beats | Why not first |
|---|---|---|---|
| **A (recommended)** | "I'll do it once, and I'll do it for real" | 1-6 | 360p source |
| B | "When he called cut, I couldn't stop crying" | 4 → 2 → 3 → 5 → 6 | the same line as Collider's 4.2M Short: "seen it" in second 1 |
| C (ending alt) | as A | 1-4 → the press-conference "best memory… both when she tortured me" | SD only, and lighter than the notebook |
| D (picture-first) | 1.5 s of the scream, then beat 1 | 2 → 1 → 3-6 | gives instant context, but opens on a film clip, not her face (H1) |

## Gate statement (PITCH-CHECKLIST § 0)
| Gate | Result | Evidence |
|---|---|---|
| **Weak, first: source quality** | OPEN, leaning FAIL for full-frame | hook 640x360 (box only, Topaz + anchor, NOT run); featurette picture 960x536; film insert HD source OPEN |
| **Weak, first: H1 (a harsh self-verdict)** | not this engine | her verdicts are warm. The engine here is the turn from the scene to the mentor, not the self-verdict that won for Oldman |
| G1 Quotable image | PASS | "I'll do it once, and I'll do it for real"; "I went home and wrote down everything that she said" |
| G2 What's on screen | OPEN | the film scene's clean HD source is not verified; the featurette's own BTS of the two women is in hand |
| G3 Tone | OPEN (by ear) | 2010: animated; featurette: soft |
| G4 Freshness | not found (scanned); entry tax on beats 3-4 | Collider's 4.21M Short ran beats 3-4 of this interview; GSA's narrated 28.8M ran the story. Searches s32-s34 (the hook line; the mentor/notebook lines) **returned zero results at all, so no files were saved**: that is weak evidence, not proof of absence. s35 (uncapped, "emma watson on helena bonham carter") shows none in its top 25. The two biggest HP Short channels were scanned upload by upload (GREEN SCREEN ANIMATION and HogwartsFandom, 1,000 each): their Helena/Emma Shorts are the role swap, chaos and injuries; **none uses the mentor or notebook lines** |
| G5 Facts | PASS on text; by ear OPEN | every line is hers: beats 1-4 and 6 on camera; beat 5 is her voice-over in the featurette (a featurette can splice audio under b-roll: ear-check). "Him" is Yates (named in the question). Chronology: "this last movie" = DH2. Nothing puts the dinner before or after the DH1 scene, so no caption may say "after"/"later". The fan lore is excluded. Last 12 months: the Rowling dispute (2025) is not touched |
| Judgment | PASS | the comments hold that it was real ("her screams were so raw that the other actors actually got worried" 33,193 likes; "Emma's acting is everything in this scene" 21,123) and that Helena cared ("Helena felt so bad… kept checking on her" 17,054; "Helena confronted Emma to make sure they were still in good terms" 40,871). Emma's own words confirm the closeness |
| Shape | PASS | one relationship: the cost → the same woman as mentor → a picture to end on (she wrote it all down) |
| Proof | PASS for the scene; **beats 1, 5 and 6 have no proof of their own** | YouTube: GSA 28.82M / 615K likes; scene upload `twHLFlqZ8T8` 7.53M; Movieclips `R2zNRrOXbPY` 9.35M; Collider 4.21M; "Scene Made The Cast Uncomfortable" `PlW5pQx2DqM` 2.49M; HBC & Watson role swap "Ultimate Duo" `bNYt1mKShvA` **38.2M** (narrated; it shows the pair travels). Instagram: Watson-as-Hermione `DbdtfctTu4G` **530K likes / 6,984 comments** (Jul 2026); "She Was Screaming…" `DNBQ5qDMvAW` 56K |
| His rules | PASS | title ≤5 words; no censor words; 2 SUBSCRIBE prompts at build |
| **Why it's interesting enough** | | the actress in the scene that left her unable to stop crying was her mentor, and Emma wrote down everything she said after one dinner |

## Title (≤5 words)
**"Bellatrix Was Emma Watson's MENTOR 🥹"** (5 words; true as worded: Helena, who played Bellatrix, was her mentor on DH2). Alternatives:
- "Emma Watson Did It ONCE 💔";
- "Bellatrix Made Emma Watson CRY 💔" (looser: she cried after "cut", in a scene she chose to play for real).

## Locked prediction (26 Nov ~07:50 PKT): centre 100K at day 7, range 20K-700K. Below the bar
- **Base:** the closest winner is Oldman "MEDIOCRE" (661K: HD, a harsh self-verdict). The closest loser is Snape (37K: SD and upscaled faces, warm "he cared" shape).
  - This Watson version matches the loser on picture (360p, upscaled) and on shape (warm).
  - It matches the winner on face power (Watson, first time on AW) and on proof (the lane's biggest story).
  - v1 was 120K; the picture news since (360p, face ~120 px) moves it down to 100K.
- **Up:**
  - the lane's most-proven story (28.8M; 38.2M for the pair);
  - Watson's first time on AW (530K-like Instagram nostalgia, Jul 2026);
  - a hook line not seen as a Short;
  - a turn in her own words.
- **Down:**
  - 640x360 hook footage (the Snape loser's comments attacked soft and restored faces);
  - the warm verdict (not the H1 engine);
  - beats 3-4 already ran as a 4.2M Short;
  - one voice.
- **Biggest failure:** the boxed 360p picture looks old and soft, and viewers swipe.
- **5K pre-mortem:** soft faces plus "seen it" on "couldn't stop crying".
- **5M pre-mortem:** "the actress from that scene was her mentor" travels with everyone who flinched at that scream.

## Backups (one line each; detail in BANK.md)
- **Sirius Part 2**, "Oldman's FAVOURITE Sirius Scene": all sources on disk, 1080p; locked 150K; needs Affan's same-face answer (`PITCH-sirius-backup.md`). **This is the only HD-ready option at the bar.**
- **Felton Broadway:** below the bar.
- **Felton "slimy git":** unlocked lead.

## Questions for Affan
1. The only on-camera copy of Watson's 2010 telling is 640x360. OK in the boxed layout after Topaz, or HD only? If HD only, the Watson Short is dead and the Sirius backup is the HD-ready alternative.
4. Hook A ("I'll do it once, and I'll do it for real": fresh, no proof of its own) or hook B ("When he called cut, I couldn't stop crying": the proven 4.2M line, so "seen it")? His proven-bits rule favours B.
2. Is a same-face Sirius Part 2 a repeat? (still open)
3. Film audio of the scream, with its score, at beat 2?
