# PITCH v2 (AW Harry Potter, 26 Nov 2026): the EMMA WATSON angle, on Affan's direction ("try to make a text sequence for the emma watson angle")

**First, the finding Affan most needs: "HATED" is not her word.** The bank title came from a 28.8M GSA Short that is a narrator. In her own words (Nov 2010), the torture scene was "very intense… but I'm really glad with how it came out". A year later she calls the woman who tortured her on screen "a really important mentor" whose every word she wrote down.

**Pick status: at the bar, not over it. Locked centre 150K, conditional on the picture quality of two old sources.** Read this as **"no pick yet"** until the HeyUGuys 2010 footage passes the anchor test.

NOT max effort yet:
1. **Picture (the deciding item):** the hook source, HeyUGuys' Nov 2010 interview, is **640x360** (VP9, 25 fps; `src/jP-p3QM9dWk_heyuguys_watson_v.mkv`, frame `proof/heyuguys_full.png`). Her face is ~120 px tall. It can only run as the house's centred 16:9 box on a blurred twin (~1.7x upscale), never full-frame 9:16, and only after a Topaz test against the Prince-ABC anchor (not run). Audio -28.2 LUFS, clean. The 2011 mentor lines are CONFIRMED in an upload of the DH2 Blu-ray featurette "The Women of Harry Potter" (`j0fBiihIt-8`, 960x720 H.264, picture letterboxed inside it, no watermark; Watson at 113.88-169.76). The Blu-ray itself is the 1080p original.
2. **Bonham Carter's own side** of the scene is not in her four 2010 sit-downs (HeyUGuys, Movies Ireland, ClevverTV, the WB EPK). Also checked: two 2010 on-set clips (Bellatrix only) and the DH2 role-swap featurette (`KUKULvha5Tk`: Helena on playing Hermione-as-Bellatrix; its upload has a burned-in "@TheHPfacts" watermark, and the speaker of "I really liked working with her" is off camera, so it is NOT used). The fan "facts" are NOT used: "she whispered are you OK", "made sure they were on good terms", "the cast thought she was really hurt", "the scream was cut".
3. **Instagram:** Watson keyword phrases return "No results" (5 tried); 16 searches and 22 posts in all. The 3-phrasings-per-beat bar is not met on Instagram.
4. **Ear-check.**
5. **Final advisor + cold read** of v2: pending at the time of writing (see the report).

## The story, first-party only
- **Watson, HeyUGuys exclusive, DH1 junket, Nov 2010, age 20** (`jP-p3QM9dWk`, 2:37-3:32, word-aligned `transcript/jP-p3QM9dWk_heyuguys_watson_0200.words.json`). Q: how intense was the scene where Bellatrix tortures Hermione?
  > "It was very intense to film. I was actually surprised by how affecting I found it, but the way we did it is I agreed with him. I said, look, I'll do it once, and I'll do it for real. And he was like, OK. So he set up two, three different cameras. And then he just said, roll. And then Helena and I basically just, like, free-played for like two minutes. And by the end of it, I was a bit of a state. When he called cut, I couldn't stop crying. It's like quite hard when you get yourself into something like that, when the camera stops rolling, to just click out of it. So it was pretty intense, but I'm really glad with how it came out."
  ("him" = director David Yates, named in the question.) Collider's 4.2M Short is a cut of this same interview.
- **Watson, "The Women of Harry Potter" (DH2 Blu-ray featurette, 2011, age 21)** (`j0fBiihIt-8` 113.88-169.76, `transcript/w1.txt`; frames `proof/sheet_women.png`: Watson in a white blouse, lamp-lit set; before it, BTS of Helena hugging Emma on set):
  > "Helena was also a really important mentor to me on this last movie. She very sweetly invited me over for dinner and we talked about books a lot. And just being a woman… [the public is harder on women]… we talked about how to kind of be able to absorb criticism and flattery… I've never told her this, but after I had my evening with her, I went home and wrote down everything that she said, everything that we shared. And I actually have a book of important encounters to me… I just don't want to forget."
- **Watson, DH2 press conference, Jul 2011** (`T6K1KLmbfU8`, SD), asked for her best memory of the whole experience: "getting to work with Helena Bonham Carter, both when she tortured me and… playing me essentially, and we had so much fun." (Backup beat.)

**Arc:** she agreed to do the torture scene once, for real → she couldn't stop crying after "cut" → the woman who did it to her became her mentor, and she wrote down every word Helena said.
**The viewer gets:** the actress who tortured Hermione until Emma Watson couldn't stop crying is the mentor whose every word Emma wrote down in her book of important encounters.

## The sequence (Variant A)
Word edges from WhisperX (medium.en + wav2vec2) on HeyUGuys `jP-p3QM9dWk`.

| # | Voice (low label) | Words | Source, time | Picture |
|---|---|---|---|---|
| 1 (hook) | Emma Watson, 2010 | "I said, look, I'll do it once, and I'll do it for real." | HeyUGuys 176.28-179.62 | Watson (pixie cut, junket backdrop). Label "EMMA WATSON · HERMIONE" |
| 2 | Watson | "And then he just said, roll." | 184.81-186.01 | cut on "roll" to the film: Bellatrix pinning Hermione to the Malfoy Manor floor, ~2 s of her scream (film audio) |
| 3 | Watson | "Helena and I basically just free-played for like two minutes. And by the end of it, I was a bit of a state." | 188.25-191.86 + 194.34-196.96 (close the two pauses) | Watson; label "HELENA BONHAM CARTER = BELLATRIX" on "Helena" |
| 4 | Watson | "When he called cut, I couldn't stop crying." | 198.86-201.08 (drop the false start "I couldn't," 197.38) | Watson |
| 5 (turn) | Watson, 2011 | "Helena was also a really important mentor to me on this last movie. She very sweetly invited me over for dinner." | `j0fBiihIt-8` 113.88-~120 | Watson 2011; insert the featurette's own BTS of Helena hugging Emma on set (frame `proof/sheet_women.png` #1) |
| 6 (payoff, end) | Watson, 2011 | "after I had my evening with her, I went home and wrote down everything that she said… I just don't want to forget." | `j0fBiihIt-8` ~142-~168 ("after I had my evening with her" ≈142; hard cut before "so Jo has a page too" ≈168) | Watson; hard cut on "forget" |

- **Runtime:** 3.3 + 1.2 + 2 (film) + 6 + 2.2 + 6 + ~9 ≈ **30 s.**
- **Order is hers:** the 2010 lines are in her order. The 2011 lines come a year later (DH2 featurette); the label carries "A YEAR LATER".
- **Left out on purpose:**
  - "Jo has a page too": Rowling, which drags in the Rowling dispute;
  - the being-a-woman passage: a second topic;
  - all the fan lore (above).
- **Censor:** none. If the "Mudblood" arm shot appears in the film insert, flag it to Affan.
- **Minors:** Watson was 19-20 filming DH1 and 20-21 in the interviews.

## Variants compared
| | Hook | Beats | Why not first |
|---|---|---|---|
| **A (recommended)** | "I'll do it once, and I'll do it for real" (no Short of this line found, s32) | 1-6 | old SD junket footage |
| B | "When he called cut, I couldn't stop crying" | 4 → 2 → 3 → 5 → 6 | the same line as Collider's 4.2M Short: "seen it" in second 1 |
| C (ending alt) | as A | 1-4 → the 2011 press-conference "best memory… both when she tortured me" | lighter, and SD-only; the mentor ending lands harder |

## Gate statement (PITCH-CHECKLIST § 0)
| Gate | Result | Evidence |
|---|---|---|
| **Weak, first: source quality** | OPEN, leaning FAIL for full-frame | HeyUGuys 2010 is 640x360 (face ~120 px): box only, Topaz + anchor test needed. The 2011 lines: 720p featurette upload (Blu-ray is 1080p) |
| **Weak, first: H1 (a harsh self-verdict)** | not this engine | her verdicts are warm. The engine here is the reversal (villain → mentor), not the self-verdict that won for Oldman |
| G1 Quotable image | PASS | "I'll do it once, and I'll do it for real"; "I went home and wrote down everything that she said" |
| G2 What's on screen | PASS | the Malfoy Manor scene itself (official Movieclips `R2zNRrOXbPY` HD, 9.35M, to check for the torture frames) + DH2 BTS of the two women |
| G3 Tone | OPEN (by ear) | 2010: animated; 2011: soft, reflective |
| G4 Freshness | PASS on the join; entry tax on beat 4 | Collider's 4.21M Short already ran beats 3-4 of this same interview, and GSA's narrated 28.8M ran the story. **No Short found of the hook line (s32) or of the mentor/notebook lines (s33-s35; s33/s34 returned nothing).** Prior virality is proof (his 11 Nov rule) |
| G5 Facts | PASS on text; by ear OPEN | every line is hers, on camera. "Him" is Yates (named in the question). The fan lore is excluded. Watson's last 12 months: the Rowling dispute (2025) is not touched; "Jo" is cut |
| Judgment | PASS | the comments hold that it was real ("her screams were so raw that the other actors actually got worried" 33,193 likes; "Emma's acting is everything in this scene" 21,123) and that Helena cared ("Helena felt so bad… kept checking on her" 17,054; "Helena confronted Emma to make sure they were still in good terms" 40,871). We confirm it in Emma's own words |
| Shape | PASS | one relationship (Emma and Helena): the cost → the reversal → a picture to end on (the notebook) |
| Proof | PASS (huge) | YouTube: GSA 28.82M / 615K likes; scene upload `twHLFlqZ8T8` 7.53M; Movieclips `R2zNRrOXbPY` 9.35M; Collider 4.21M; "Scene Made The Cast Uncomfortable" `PlW5pQx2DqM` 2.49M; HBC & Watson role swap "Ultimate Duo" `bNYt1mKShvA` **38.2M** (narrated; it proves the pair travels). Instagram: Watson-as-Hermione `DbdtfctTu4G` **530K likes / 6,984 comments** (Jul 2026); "She Was Screaming…" `DNBQ5qDMvAW` 56K |
| His rules | PASS | title ≤5 words; no censor words; 2 SUBSCRIBE prompts at build |
| **Why it's interesting enough** | | Bellatrix made her cry for real, and then became the mentor whose every word she wrote down |

## Title (≤5 words)
**"Bellatrix Became Emma Watson's MENTOR 🥹"** (5 words). Alternatives:
- "Emma Watson Did It ONCE 💔";
- "Bellatrix Made Emma Watson CRY 💔".

## Locked prediction (26 Nov ~06:55 PKT): centre 150K at day 7, range 30K-1M. AT the bar, only if the picture passes
- **Up:**
  - the lane's most-proven story (28.8M, 38.2M for the pair);
  - Watson's first time on AW (530K-like Instagram nostalgia in Jul 2026);
  - a fresh hook line;
  - a real reversal in her own words.
- **Down:**
  - 2010 junket footage at 640x360 (the Snape loser's comments attacked soft and restored faces);
  - the warm verdict (not the H1 engine);
  - beats 3-4 already ran as a 4.2M Short;
  - one voice.
- **Biggest failure:** the 2010 picture looks old and soft, and viewers swipe.
- **5K pre-mortem:** soft SD faces plus "seen it" on "couldn't stop crying".
- **5M pre-mortem:** "Bellatrix → mentor" is a reversal everyone who flinched at that scream wants to share.

## Backups (one line each; detail in BANK.md)
- **Sirius Part 2**, "Oldman's FAVOURITE Sirius Scene": all sources on disk, 1080p; locked 150K; needs Affan's same-face answer. `PITCH-sirius-backup.md`.
- **Felton Broadway:** below the bar.
- **Felton "slimy git":** unlocked lead.

## Questions for Affan
1. The 2010 HeyUGuys hook footage is 640x360 (box layout only, after Topaz). OK, or HD only? If HD only, the hook moves to the film scene and the Short opens on beat 4's line from Collider's cut, which is the same 360p source, so it dies.
2. Is a same-face Sirius Part 2 a repeat? (still open)
3. Film audio of the scream (with its score) at beat 2?
