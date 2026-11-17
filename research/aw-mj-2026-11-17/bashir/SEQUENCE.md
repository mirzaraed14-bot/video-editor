# Bashir card — "Michael Jackson TRUSTED Him" (AW Short) — SEQUENCE TEXT v1.1 (17 Nov 2026, ~20:35 PKT)

**VERDICT: NO PICK. This is a below-bar CARD (centre ≈ 55K, range 12K-500K; the bar is a 150K centre with a 1M top).** It is sent as
text because Affan asked for the sequence. Cold read #1 (`COLDREAD.md`, Sonnet) and the re-read of v1.0 (`COLDREAD2.md`) both said
SEND AFTER FIXES, as a card. Both sets of fixes are applied below; v0.2 is kept as `SEQUENCE-v0.2.md`.

**NOT max effort yet:**
1. William is not downloaded. He has been queued on the shared pace.sh youtube lock since 19:33, behind gta-farewell and speed.
   His in and out times and his frames are open. Taj and ABC 2009 were taken off the queue: they are not in the sequence.
2. No by-ear checks yet (silence rule). Is beat 1 Bashir's own voice, or Take Two's host reading his words? Every quote also needs one
   listen. A pitch test leans towards Bashir (below), but it is not proof. **If it is the host,** the hook is a narrator reading a
   quote: run the **fallback** in Variants (beat 1 relabelled as Take Two's quote, no "SAME MAN").
3. Two tests have not run: the music-bed stem test (it needs the ~80 MB htdemucs download, which needs his OK) and the Iris + Proteus
   anchor test.
4. Instagram returns "No results" for Take Two and Taj, and Jermaine was not searched there.
5. The Fable advisor was called before the draft and on v1.0; the re-read fixes in v1.1 (button, labels, beat 3 text) were not put back to it.

## The arc (one line)
On air, Bashir said he was angry at how Michael's children were made to suffer → on Michael's own camera the same man told him
that relationship was "spectacular" and almost made him weep → who was he? The journalist who had interviewed Princess Diana, and
Michael says Bashir sold himself as "the man that turned Diana's life around" → in 2021 an inquiry found that Diana interview was
obtained with fake documents → Michael: "No matter what you do, there's always somebody that will say something about it."
Shape: setup (the public verdict) → turn (the private praise) → why he was trusted (Diana) → ending (that credential was a
forgery) → the wound, in Michael's voice.

**The viewer gets:** Michael's own camera caught Martin Bashir praising, off air, the parenting he criticised on air, and the Diana
interview that earned Bashir Michael's trust was itself obtained with fake documents (BBC inquiry, 2021).

## Sources (TT = Take Two)
- **TT** = `E:\Bullshit Folder\Henry\The Michael Jackson Interview TAKE TWO_ The Footage You Were Never Meant To See (2003) - 4K UPSCALE.mp4`.
  - Fox, 20 Feb 2003. 1440x1080, a 4:3 upscale of SD, 25 fps, 1.64 Mb/s, AAC 128k.
  - Word times: medium.en with wav2vec2 alignment, run under .asr-lock/gpu.lock, in `asr/tt_*.words.json`.
  - Frames: `proof/tt_*.jpg`.
  - Take Two's red side panel and quote cards sit left of the picture: crop to the picture.
- **STATEMENT** = Michael's written statement, 6 Feb 2003, issued through his London representative (AP via newson6.com, 6 Feb
  2003; Irish Times, 7 Feb 2003; text in `STATEMENTS.md`). Exact words used on screen: "Martin Bashir persuaded me to trust him
  ... and told me that he was 'the man that turned Diana's life around.'" It is not on camera, so it can only be on-screen text.
  BANNED's beat 3 was also a written post.
- **WILLIAM** = `Qyfc1KHJLfI` on "The Royal Family Channel" (20 May 2021, 2:17, 327,505).
  - This is a fan/news channel, NOT the official royal account. ITV News also carries it: `y7qaiP-CwxU`, 951,567.
  - His statement text (`STATEMENTS.md`): "...BBC employees: lied and used fake documents to obtain the interview with my mother" /
    "It is my view that the deceitful way the interview was obtained substantially influenced what my mother said."
  - He never names Bashir.
  - [download and word times pending]
- **TAJ** = Sunrise `mjLoyJ3FPKY` (24 May 2021, 52,986): pending, not in V1. **ABC 2009** = `Prm2n9HVMRA`: pending, not in V1.
- **Dyson report** (20 May 2021), verified (Press Gazette, The Week):
  - Bashir had fake bank statements mocked up and showed them to Earl Spencer to gain access to Diana.
  - The BBC accepted the findings in full and apologised.
  - Bashir apologised for the forgery but says it had no bearing on Diana's choice.
  - Panorama aired November 1995 (22.8M viewers).

## V1 — the card's sequence (cold read's re-order)
| # | ~s | Label (low) | Words | Source in → out | Picture | Proven / ours |
|---|---|---|---|---|---|---|
| 1 HOOK | 3.2 (6.2 with the lead-in) | none for 0-3 s; then MARTIN BASHIR · HIS 2003 DOCUMENTARY (only if the ear check confirms his voice; else "BASHIR'S DOCUMENTARY, 2003") | "I was angry at the way his children were made to suffer." (lead-in option: "They are restricted. They are overly protected.") | TT **4328.56 → 4331.78** (lead-in from 4325.57) | Michael alone, or Michael and Bashir walking (TT 71:35, adults only). NEVER TT's own picture here (masked children) | Seen half: Take Two's own 2003 pairing |
| 2 TURN | 7.9 | SAME MAN · MICHAEL'S OWN CAMERA | Bashir to Michael: "Your relationship with your children is spectacular. And in fact it almost makes me weep when I see you with them." | TT **4334.72 → 4342.57** (Take Two's replay, clean words; close the 1.56 s hole between "spectacular." 4338.00 and "And" 4339.56), or the first take **2203.85 → 2205.99 + 2208.64 → 2211.62** (quieter bed; cuts out an off-mic "I love you" at 2206.67-2207.80) | Michael in red, alone (TT 36:32-36:57): crop the quote card off | Seen half (same) |
| 3 WHO HE WAS | 10.2 | MICHAEL'S STATEMENT · 6 FEB 2003 (on-screen text while the voice runs) | Voice, Take Two host Maury Povich: "But who is Martin Bashir?" + "In 1995, this little-known British journalist caused an uproar when his sensational interview with Princess Diana revealed details of her extramarital affair." On screen over the "In 1995" sentence, only the fragment of Michael's statement: "...the man that turned Diana's life around." (the full line, "Martin Bashir persuaded me to trust him ... and told me that he was 'the man that turned Diana's life around'", is 19 words over ~21 spoken words in 10 s: too much to read) | TT **216.89 → 218.29** + **225.84 → 234.67** | Bashir photo (TT 3:37) → Diana's Panorama interview (TT 3:49-3:55, frame-in-frame; the BBC original via news at build). Skip TT 3:45-3:47 (boys in the crowd behind Bashir); use the Diana frame only to 3:52 (a tabloid cover enters at 3:53) | The spoken link: Bashir is named in voice and tied to Diana in the next sentence. Michael's own words tie his trust to Diana. The text is OURS (no video quotes it: b11 returned 0 results) |
| 4 REVEAL | 1.5 + ~5 | card: "2021: THE BBC'S INQUIRY INTO BASHIR'S DIANA INTERVIEW" (Dyson named him) → PRINCE WILLIAM · 2021 | "...BBC employees lied and used fake documents to obtain the interview with my mother." Fallback if the list line doesn't cut cleanly: "the deceitful way the interview was obtained substantially influenced what my mother said" | WILLIAM [pending] | William on camera | OURS as a join (2021 news only: Sunrise 52,986, Popcorned Planet 86,502; no Short) |
| 5 BUTTON | 3.6 (+4.3 tail) | MICHAEL · TAKE TWO, 2003 | "No matter what you do, there's always somebody that will say something about it." Optional tail: "And all you want to do is bring some love and some joy, you know?" | TT **4641.57 → 4645.19** (-19.8 LUFS); tail **4661.94 → 4666.28**, joined over a cutaway, never a same-camera jump | Michael in teal, alone (TT 77:08-77:48, `proof/tt_jerk_4620.jpg`); end before the credits at 77:50 | OURS. b20 found only fan clips (241, 172 views); b21 and b22 (Shorts) found 0 results; the line is in none of our cut sheets |

Total ≈ 33 s (≈ 37 s with the tail).
- The button is Michael's answer to off-camera questions from the interviewer: "Do you sometimes despair of human nature?"
  (4622.88) and "Can you ever do anything that's right?" (4633.70).
- It is general and is never captioned or labelled as being about Bashir. Placed after the forgery card it still reads as a
  comment on him: that is our join, named as one.
- Nothing in the cut says Bashir lied to Michael. Runner-up button: "There's always some jerk, some mean-spirited person to try to
  bring you down" (4654.77-4660.46): more emotional, but it puts an epithet on a living man by placement.

**Whose voice is beat 1?** Take Two labels beat 2's card "Voice Of Martin Bashir" but beat 1's plain "Martin Bashir"; the plain
style also sits on the Primetime quote Povich introduces with "We'll quote directly" (810.6) and on the Newsday quote he reads
(4598). Median pitch (torchaudio, scratchpad wavs): beat 1 ≈ 96 Hz; Povich narration 120-125 Hz in three samples; Bashir off air
(Take Two) 105-108 Hz; Bashir's questions in the documentary 118-129 Hz (short samples, rising questions). It is lower than every
Povich sample, so it leans to Bashir's own narration, not the host. Weak evidence: the ear check decides.

**Context read around every line:**
- **Beat 2** is from Bashir's FINAL interview. Take Two's narration places it "long after the incident with the baby on the Berlin
  hotel balcony" (TT 2185.05-2191.32). That answers the comment "he was only angry about the balcony".
- **Beat 1** sits in Take Two's own on-air-vs-off-air segment (4270-4343). Take Two introduces it as "This comment about Michael's
  method of raising children was included on Bashir's special" (4319.85-4324.19).
- **Beat 5** follows Michael's answer to "Can you ever do anything that's right?": "No... no matter what you do, there's always
  somebody that will say something about it" (4633.70-4647.35).
- **The contradiction is arguable** (cold read). "Restricted, overly protected" and "a spectacular relationship" can both be true.
  The sharp pair is "made to suffer" against "almost makes me weep", which is why the hook starts at "I was angry".

**Audio** (ebur128 on each beat; RMS in the gaps between words):
- Take Two carries a MUSIC BED under every line.
- Speech: -19.8 (b1 hook) / -20.1 (b1 with the lead-in), -20.7 (b2 replay), -20.4 (b2 first take), -19.9 (b3 "But who is Martin
  Bashir?") and -20.3 (b3 1995 sentence), -20.7 (b5 button) LUFS.
- Gaps: b3's splice point -33.1 dB; b5 -29.9 and -27.1 dB (Take Two's last seconds before the credits: the bed does not swell
  above the rest).
- The gaps sit at -23 to -30 dB RMS, so the bed is ~8-10 dB under the voice. B2's first take is the cleanest (-30.4).
- PITCH-CHECKLIST § 2 lists music under the voice as a fail, so a stem-separation test is needed before the build. The local demucs
  venv has no htdemucs weights: that's an ~80 MB official download and needs his OK.
- AW Shorts ship without our music (his job), so Fox's score would sit under his.

## Variants
| Variant | Order | For | Against | Verdict |
|---|---|---|---|---|
| **V1** (if beat 1 is Bashir's voice) | on air "made to suffer" → off air "makes me weep" → who he was (Povich + Michael's statement) → William 2021 → "there's always somebody that will say something about it" | the hook is a judgment about Michael, voiced and then answered by the same man (the BANNED shape); the 2021 reveal lands late; the button is a wound, not an accusation | Bashir is unnamed until beat 3; beat 1's voice is unconfirmed; 40 s of SD Take Two | **send (as the card)** |
| V2 | Jermaine "And he trusted. He trusted Martin Bashir." (TT 4479.32 → 4483.51) → 3 → 1 → 2 → 4 → "What hurts you most?" "When they lie. The lies. The complete lies." (TT 3501.02 → 3507.00) | a family voice; a TRUSTED → LIE loop | "Martin Bashir" lands at 3.39 s after a 1.36 s gap, "he" has no antecedent, and Jermaine grins on Fox. "When they lie" follows talk of the police searching for "crap on Michael that was not true" (3496.43), so ending on it implies Bashir lied to Michael | runner-up |
| **Fallback** (if beat 1 is the host's voice) | V1's order; beat 1 labelled "BASHIR'S DOCUMENTARY, QUOTED BY TAKE TWO"; beat 2 labelled "BASHIR · MICHAEL'S OWN CAMERA" (no "SAME MAN") | keeps the order and the honest attribution | the hook becomes a narrator reading a quote: weaker | run only if the ear check says host |
| V3 | William 2021 cold open → Povich (216.89 → 234.67) → statement → 1 → 2 → 5 | the strongest single line first; rides the Diana wave | opens as a royal story: the hook's topic is not the payoff's (the Diana v1.1 failure); needs William's download | third |
| Buttons | "somebody that will say something about it" (V1) vs "some jerk... bring you down" vs "When they lie..." (V2) | — | "jerk" puts an epithet on Bashir by placement; the lie-echo points "lie" at Bashir and Michael | "somebody... say something" |

**Other voices searched (gate item 1):**
- **Uri Geller** (who brought Bashir to Michael): no video on YouTube (b13, 0 results).
- **Earl Spencer** naming Bashir on camera: nothing above 2K (b14). The Diana side lives in 2021 news: Channel 4 News 253,098, ITV
  951,567, Guardian 655,916.
- **Taj Jackson** (2021): Sunrise 52,986 [download pending].
- **Jermaine** (2003, inside Take Two): moved to V2.
- **Bashir himself**, ABC 2009 (279,720): "never saw any wrongdoing" [pending; not used].
- **Proven Bashir-lane moments on disk, checked for beat 1:**
  - "Didn't Prince get poked in the eye?" (`asr/lw11` 98.13), the 4.45M Short's moment.
  - "I've seen Blanket... his mother was probably white" (`asr/lw15` 167.57), likely the 18.3M's.
  - Both are about his children (minors on frame in the proven Shorts), and neither is an on-air-vs-off-air contradiction.
- **Bashir news in the last 12 months:** none found (web, 17 Nov).

**Per-beat YouTube searches (b15-b19, 17 Nov ~19:50):**
- **Jermaine:** b15 "Jermaine Jackson Martin Bashir" found no Short of his Fox line (the GMB 2019 Jermaine at 890,849 is about the
  allegations). Also b16 "he trusted Martin Bashir Michael Jackson" and b04.
- **On air / off air:** b08; b10 (0 results); b17 "almost makes me weep" (one 444-view news clip).
- **The "When they lie" button:** b18 "what hurts you most when they lie" found nothing. b19, Shorts only, "the lies the complete lies"
  found nothing for the line. Neighbours from b19:
  - SLY "GRAMMYS WERE LYING" 34,631,759.
  - OUR "Michael Jackson's K*ller Caught LYING" 1,214,895 (Jul 2026).
  - Candace Owens "They lied to us about Michael Jackson." 984,588.

**The join is starting to appear, at tiny numbers:**
- "He Destroyed Michael Jackson With a Camera — Then Did the Exact Same Thing to Princess Diana" (The Untold MJ, Jul 2026, 28 min):
  1,324.
- "Michael Jackson Trusted Him — Then the Interview Aired" (The Recall, Jul 2026, 14 min): 999.
- "Beware Immediate Empathy #michaeljackson #martinbashir #princessdiana" (16 Nov 2026, 2:37): 695.
- "#DamnQuotes Michael Jackson Martin Bashir persuaded me to trust him..." (2023, 10 s, the statement as text): 115.

None reaches 100K, so there's no entry tax. The title "Michael Jackson TRUSTED Him" does overlap The Recall's (999).

## Gate statement (PITCH-CHECKLIST § 0) — FAILED / WEAK FIRST
| Gate | Result | Evidence |
|---|---|---|
| **The bar** | **FAIL: under the bar** | centre ≈ 55K (below) |
| Source quality | **FAIL until fixed** | Take Two (beats 1, 2, 3 and 5) is an SD upscale with Fox's MUSIC BED ~8-10 dB under every line (gap RMS -23 to -30 dB against speech at -19 to -22 LUFS). The stem test needs the htdemucs weights (his OK). Raw anchor (`proof/anchor_bashir.jpg`): Michael (red and teal shots) sits below the approved Prince ABC panels and above the approved Bieber phone shot. That compares raw crops against a processed Prince panel; the recipe test (Iris + Proteus) was NOT run. Minors: none on the chosen frames |
| Proof (per beat) | **WEAK: no beat is PROVEN** | The lane is proven, but on other moments: LEGENDS IN 4K "BASHIR WAS WRONG ABOUT BLANKET" 18,275,995 and "MARTIN BASHIR LIES ABOUT PRINCE..." 4,454,488; "Tired Of Bashir" 609,430; ALMJ "Interview Moments with Martin Bashir" 347,798. Our on-air/off-air pair is Take Two's own 2003 pairing. The button, the statement and the William-to-Michael join: no Short found. **Instagram** (`IG.md`: 32 loads, 7 searches + 5 reorders, 21 posts read, 0 blocks): the Diana Panorama half is huge (@thewindsorcrown DZ6shYfhD8F 1.3M likes / 90.7K shares, 22 Jun 2026, a 20K-follower account; @historysurfeit DKck_lqhfZK 1.1M / 99.2K shares, 3 Jun 2025, 202K followers; @untold.histories_ 284.4K). The Michael-documentary half is mid (@satninmina_ 44.1K / 4.1K shares; @michaeljacksonism 33.3K / 5K; @the._desk 28.1K / 7.7K, "The interview that changed everything"). The 2021 deceit half is small (@accesshollywood, William, 13.4K). Take Two and Taj: "No results". Instagram joins: one caption with 7 likes (@mjj.evidence DZXnX_gxAnR, 9 Jun 2026: "He did it with Princess Diana and Michael Jackson") and one comment on the 1.1M Diana post: "Martin bashir killed diana and michael both..." |
| G4 Freshness | PASS for the join, WEAK for the halves | No Short joins Bashir's Diana deceit to Michael (b01, b02, b03, b12 with the Shorts filter; b11 found 0 results for the statement line). The join exists only as 2021 news (Sunrise 52,986, with Taj; Popcorned Planet 86,502: "It wasn't just the Princess Diana interview that Martin Bashir was deceitful over...") and tiny 2026 uploads (≤ 1,324). Take Two-style material is already out (by title, content unread): LEGENDS IN 4K "MICHAEL JACKSON CALLS OUT MARTIN BASHIR FOR CHEATING" 419,508 (10 s, Dec 2024, tagged #livingwithmichaeljackson, so possibly the documentary, not Take Two); "MARTIN BASHIR IS A LIAR! Michael Jackson TRUTH footage revealed" 106,848 (2009); Soul Lounge "When MICHAEL Jackson Went Off on Bashir Martin" 87,665; the full Take Two re-upload 260,627 (content known: the full show); "Exposes Martin Bashir" 55,454 |
| Judgment | WEAK-PASS: confirms more than it reverses | The belief is held: "I HATE The interviewer Martin Bashir for exploiting Michael Jackson!" 2,075 likes (on the 18.3M); "Notice both the victims of Bashir were soft spoken, gentle hearted people..." 519 and "Martin Bashir needs to be investigated for the Michael Jackson interview too" 317 (Sunrise 2021). For the fan audience it is vindication, not a reversal. For the Diana audience it reverses "the interview of the century" (William) |
| Shape | PASS, narrowly | One spine: Bashir's word. The link is now spoken: Povich names Bashir (216.89-218.29) and ties him to Diana in the next sentence (225.84-234.67), and Michael's own written words tie his trust to Diana. William's line never names Bashir and works only because beat 3 sets it up. The cold read called the earlier draft's link "a card we supply" (fixed) |
| G3 Tone | PASS in V1 | Jermaine, who grins on Fox (`proof/tt_jermaine_4468.jpg`), is out of V1. Michael's button is quiet and hurt |
| G5 Facts | PASS | Dyson (20 May 2021): fake bank statements shown to Earl Spencer, and a full BBC apology (Press Gazette, The Week). Michael's statement, 6 Feb 2003 (AP via newson6; Irish Times 7 Feb). William's words (full statement, Yahoo UK). All in `STATEMENTS.md`. Counter-evidence is shown, never hidden: Bashir apologised for the forgery but says it had no bearing on Diana's choice, and Granada "maintained that it was a fair and honest portrayal of the man" (TT 4672.7-4678.5). Quotes heard by ear: NOT done (silence rule); the build session hears them |
| G1 Quotable image | PASS | "it almost makes me weep when I see you with them" against "I was angry at the way his children were made to suffer"; "fake documents" |
| G2 On screen | PASS | Michael's own camera (the thing itself), William on camera, Diana's Panorama interview |
| His rules | OPEN: the allegations lane is his call | The cut carries no allegation words (no bed, no Gavin, no "dangerous place", no "criminal"). But the HOOK is now a charge against Michael's parenting, "I was angry at the way his children were made to suffer", heard first and captioned before beat 2 answers it: his call. The documentary IS the allegations documentary and comments may go there. The hook is a claim only; title ≤ 5 words; no censor words; no minors on frame; ≤ 60 s. The button is general and never captioned as about Bashir. Never say or imply in text that Bashir deceived or lied to Michael: that's an unverifiable claim about a living man |
| Why interesting | — | Michael's own camera caught Bashir praising off air what he criticised on air, and the Diana interview that got Bashir in the door was a forgery job |

## Our channel (repeats and neighbours)
- **AFRAID** ("This Is What Michael Jackson Was AFRAID Of", Sep: Oprah → Sawyer → Bashir's questions → Joe): 167,235 lifetime
  (RESULTS line 101). It used Bashir's questions only, none of this card's lines (BASHIR-CUT, "Affan's cut", 9 Sep).
- **Disguised GANGSTER** (1 Nov, one Bashir "Peter Pan" line): 88,662-89,559. **DISRESPECTFUL Interview** (Walters): 80,011.
  (AFRAID and DISRESPECTFUL numbers are from RESULTS.md's lifetime snapshot, not re-read today.)
- **BASHIR-CUT draft 2** (9 Sep) used "When they lie" as its hook, plus the 2009 ABC line. Affan shipped his own montage instead
  (AFRAID), so the contradiction and "When they lie" are unbuilt.
- **Closest winner:** AFRAID 167K (same villain, same lane). **Closest losers:** GANGSTER 89K (a Bashir line in a business story) and
  La Toya BETRAYED 19K (a betrayal title, Nov).

## Title (≤ 5 words, 21-40 chars)
1. **"Michael Jackson TRUSTED Him 💔"** (4 words, 27 chars). It overlaps The Recall's 999-view long-form title.
2. "He Trusted Martin Bashir" (24 chars).

Dropped: "Michael Jackson Was LIED To", because it says outright what the cut must not claim. Never "Bashir LIED To Michael".

## Locked prediction (re-locked after the cold read)
**Centre 55K, range 12K-500K: UNDER the bar (150K centre / 1M top).** This is the cold read's price, taken over my 90K draft.
- Our MJ Shorts since 1 Oct (AW-SHORTS-NOW): Police 11K, Lisa Marie 17K, La Toya BETRAYED 19K, Doctor 27K, Electrocuted 33K, Masks 76K,
  Gangster 89K. The median is ≈ 27K and none reached 150K.
- AFRAID's 167K (same villain) was September.
- The lane's 18.3M and 4.45M are other moments and don't lift it.
- 1M+ would need the Panorama-anniversary peg, a clean source and the spoken link all at once. The cold read puts that near 3 %.

Pre-mortems:
- **5K:** Take Two's SD picture, red side panels and Fox score read as an old documentary. Fans already think Bashir is a villain, so
  the first 3 s carry nothing new.
- **5M:** the "Bashir lied" lane (18.3M) meets a fact most fans don't know (the Diana interview was a forgery job) and gets shared as
  vindication. The Diana × Michael wave carries it outside the fan base.

## Flags
- **Minors:** none on the chosen frames.
  - Take Two's masked children under beat 1's audio are replaced.
  - TT 3:45-3:47 (the crowd) is skipped.
  - V2's "When they lie" goes out at 3507.00, before a child appears at 3507.12.
  - Beat 5's span (77:08-77:48) is Michael alone.
- **Censor:** none.
- **Length:** ≈ 33-37 s.
- **Allegations lane:** his call; the cut carries no allegation words.
- **Peg:** Panorama aired in November 1995 (22.8M viewers). The exact day and any anniversary peg are unverified.
