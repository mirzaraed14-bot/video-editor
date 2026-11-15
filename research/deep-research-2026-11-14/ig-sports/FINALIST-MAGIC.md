# Lead working file: "Magic Johnson's Wife Wore WHITE 💔" (ig-sports, 14 Nov 2026)

## ⚠ Cold-read corrections (20:37 PKT): these override anything below that contradicts them
- **Label:** a LEAD under the README bar (a locked centre of 150K), re-derived centre **25-60K** (range 8K-1.5M; the top widened at
  21:56 for the 34.8M / 14.8M Magic-family Shorts, a different angle). Not a pick.
- **Order:** v1 is the lead (Cookie's "It wasn't how he got it… trumped everything" answers Instagram's judgment); v2 (The View
  "leave and let him die") is the runner-up. 2016 and 2021 are two tellings by one speaker, not two eras.
- **Windows:** use only the "Measured word boundaries" table at the bottom; the rough windows in the tables above are segment
  starts (beat 1 opened on Gayle's VO; beat 2 started on "…new drugs"; beat 4 ran into the host's "I have so").
- **The hook:** a ~3 s pause follows "Because of the" in the 1991 clip, so context is NOT in 5 s without a cut; ~42 s needs ~7 jump
  cuts (~56 s untrimmed).
- **Facts:** she SAT beside Jerry Buss (AP caption), she did not stand. He told her days BEFORE 7 Nov (a preseason call-back from
  Utah), so beat 2 is a labelled flashback. The end label over the 2021 two-shot is "2021 · 30 YEARS LATER"; the 35th is the peg.
  "Everyone over 35 remembers" is wrong: the core women (35-44) were 0-9 in 1991.
- **Logos:** the 528x940 crop still shows "INGS"; an "EXCLUSIVE / CBS MORNINGS" tag also sits top-left on every frame. A punch-in
  (~1.3x) or a mask is needed, and the letterboxed 1991 inserts and the two-shot carry both.
- **The View:** host cutaways at ~237-238 s and ~251 s fall inside v2's beats; there is a studio audience (check applause after
  "live."); its anchor test is not done. The `cookie-gma-*` folder names are historical: the clip is The View (dl.log id
  `160920_view_cookiejohnson`); the GMA/Robin Roberts telling was never downloaded.
- **Final lead sequence (hook B, 20:40):** Gayle 409.43-412.22 (white-suit question, over the 1991 shot) → Magic 1991 55.35-65.25
  (cut the ~3 s pause) → Magic 2021 149.15-157.52 (flashback label) → Gayle 431.87-434.21 + Cookie 443.76-452.32 (the "sexual contacts"
  stretch 434.21-443.76 cut out) → Cookie 415.48-428.39 ("…like a future"). ~45 s raw, ~38-40 s after ~5-6 jump cuts.
  Runner-up: hook C with "She Didn't Leave Magic Johnson 💔", ending on "trumped everything" (~30 s).
- **Anchor:** `proof/anchor_strip.jpg` is ⅓-scale whole frames, not 1:1 face crops; its Magic tile is a dissolve frame.


▶ STATUS (Sat 20:00 PKT): source downloaded, transcribed and measured; sequence v1 drafted below. OPEN: YouTube freshness
(the flag set 16:42 blocks every Shorts search), Instagram proof for this exact beat (topic proof only so far), cold read,
advisor call 2. Not a pick yet.

## The source (one first-party broadcaster file holds the whole arc)
- CBS Mornings, Gayle King, "Magic and Cookie Johnson on surviving HIV, stopping the stigma and building an empire" (Nov 2021,
  30th anniversary), downloaded from CBS's own site (not YouTube):
  `src/magic-cbs-2021/magic_cbs_2021.mp4` = **1920x1080, 29.97 fps, h264 3.1 Mb/s, AAC 48 kHz stereo, 10:48.6**.
- Transcript: WhisperX large-v3 + alignment, `src/magic-cbs-tr/transcript/words.json`, readable `src/magic-cbs-tr/transcript.txt`.
- Frames: `src/magic-cbs-2021/sheet_12s.jpg` (whole file), `sheet_396_420.jpg` (the white-suit shots).
  The 1991 press conference is inside the package as archive: Magic at the podium in a dark suit (~0:52-1:03, ~1:12),
  and **Cookie in a white suit beside Lakers owner Jerry Buss (~6:36-6:38, 6:50-6:57)**.
- A "CBS MORNINGS" bug sits bottom-left (y ≈ 0.83-0.88) on every frame; a 528x940 crop from y20 (1.15x punch) clears it.
- Audio, integrated loudness per beat window (ebur128): 1991 announcement -23.0 LUFS (peak -7.4); Magic "toughest thing"
  -28.7 (peak -7.7); Cookie white suit -26.3 (-6.5); Cookie "how he got it" -25.3 (-5.7); Gayle studio lines -15.5 / -16.6.
  Floor between words (100 ms RMS, 5th percentile): -54.0, -57.2, -59.9 dBFS → **no music bed under the sit-down voices**.
- Anchor test (`proof/anchor_strip.jpg`): Cookie 2021 at delivery scale is at or above the Prince ABC panels (PASS); the
  1991 white-suit shot is archive SD, clearly softer → his letterbox-with-blur-fill rule for that 2-3 s insert.

## The words (WhisperX times in the CBS file; to be confirmed against the waveform at build)
| t (s) | Speaker | Words |
|---|---|---|
| 52.4-63.1 | Magic, 1991 (archive) | "Because of the HIV virus that I have attained, I will have to retire from the Lakers." |
| 72.3-77.4 | Magic, 2021 | "At that time, the only thing I knew, if you got AIDS, you died, right?" |
| 120.6-140.1 | Magic | "Oh, I was just devastated… And so I just lost it right there… Am I gonna die? Because I definitely asked him that." |
| 146.3-173.9 | Magic | "But the toughest thing, Gayle, that I had to do was really drive home and tell Cookie. It was hard because I loved her so much and I hated to hurt her. … no greater pressure than driving home to tell her. Even today, it's still the toughest thing I've ever had to do in my life." |
| 174-183 | narration (Gayle VO) | "The Johnsons were married a little over a month… and they had just learned Cookie was pregnant." |
| 395-408 | Cookie | "The stigma with AIDS… they thought you couldn't touch people, you couldn't hug people. And I didn't want people to treat us like we were lepers." |
| 406.4-411.8 | Gayle | "I still remember the press conference. You're sitting there in that white suit. What were you thinking?" |
| 412.9-430.0 | Cookie | "I was thinking, you know, be strong. And I wore that white suit for a reason. I didn't want to wear anything dark or black, because to me, it's what it symbolized. And the white suit to me symbolized, you know, brightness, like a future, basically. You know, positivity." |
| 431.9-451.2 | Gayle → Cookie | "When he told you how he got it, what was your thought?" → "…It wasn't how he got it that was important to me. It was, you're possibly going to die. And that trumped everything." |
| 541.7-554.6 | Magic | "That situation wasn't going to change my attitude… If I was going to die, I was going to die being Earvin Johnson." |
| 563.5-566.3 | Gayle (studio) | "He said most people said he wouldn't last three or four years, let alone 30." |
| 622.6-627.3 | Gayle (studio) | "we just all assumed one of the greatest players is going to die. And he's still here." |

## Second telling, downloaded (20:10): The View, ABC, Sep 2016 (her memoir tour), served at goodmorningamerica.com/video/42228948
- `src/cookie-gma-2016/cookie_gma_2016.mp4` = **1280x720, 29.97 fps, 6:35** (ABC's own player, not YouTube). Transcript
  `src/cookie-gma-tr/transcript.txt`. Frames `src/cookie-gma-2016/sheet_236_260.jpg`: clean single close-ups of Cookie;
  bugs bottom-left (The View) and bottom-right (abc, #VIEW20) fall outside a 9:16 crop on her face.
- Audio, "two things" window (247.5-260.3 s): -24.3 LUFS, peak -8.0; floor p5 -52.9 dBFS (studio, no bed).
- The lines (WhisperX):
  - 0.2-21.7, Magic 1991 (archive, the same press conference): "Because of the HIV virus that I have attained, I will have to
    retire from the Lakers. My wife is fine. She's negative… I plan on going on, living for a long time…"
  - 128.5-165.7, Cookie: "I was at home about to watch him on a game… he called me… 'I'm on my way home and I have to tell you
    something'… my mind was going through all kinds of crazy things, like, oh my God, we just finally got married… Does he want
    a divorce?"
  - 214.1-241.9, host → Cookie: "…you were waiting behind closed doors as he had to let the other women… know" → "he had to set
    himself in a room and call people… over a 10-year period, so it was quite a few people… that was not a good feeling. I
    didn't like it."
  - **247.8-260.0, Cookie: "At that time, I felt I was facing two things. You either stay here and help him live, or leave and
    let him die. And I chose to help him live."**
- This is the judgment ("leave") and the reversal in HER words, five years before the CBS sit-down: the join across eras.

## Sequence v2 (supersedes v1 as the lead), ~42 s
| # | Source, t | Who | Words |
|---|---|---|---|
| 1 | CBS 52.4-63.1 (or View 0.2-7.8) | Magic, 1991 | "Because of the HIV virus that I have attained, I will have to retire from the Lakers." |
| 2 | CBS 146.3-157.0 | Magic, 2021 | "The toughest thing… was really drive home and tell Cookie… I loved her so much and I hated to hurt her." (card: JUST MARRIED · SHE WAS PREGNANT) |
| 3 | View 231.1-241.9 | Cookie, 2016 | "he had to set himself in a room and call people… over a 10-year period, so it was quite a few people… that was not a good feeling." |
| 4 | View 247.8-260.0 | Cookie, 2016 | "I felt I was facing two things. You either stay here and help him live, or leave and let him die. And I chose to help him live." |
| 5 | CBS 408.4-430.0 | Gayle → Cookie, 2021 | "You're sitting there in that white suit. What were you thinking?" → "I wore that white suit for a reason… dark or black… the white suit to me symbolized… brightness, like a future." Over the 1991 white-suit shot, hard cut on "future" to the 2021 two-shot; card: 35 YEARS LATER, HE'S STILL HERE |
- Runner-up order (v1): replace 3-4 with CBS 431.9-451.2 ("When he told you how he got it…" → "It wasn't how he got it…
  you're possibly going to die. And that trumped everything."). v2 wins: "help him live, or leave and let him die" is the
  viewer's judgment said aloud by the person it is about (the BANNED Birthdays mechanic), and it adds a second era.
- Beat 3 is the risk line (it names the other women): keep it only if the hook test says the judgment needs installing; else
  cut to 4 directly (~34 s).

## Instagram: what the proof is for (read 17:45-20:07)
- The autumn-2026 Magic wave is about **how he got it** (his off-court life → HIV): @thebucketzco 200,358 likes / **179,174
  shares** (28 Sep), @fullpossession 51,515 / **32,306 shares** (6 Oct, career bio), @showtimelakerss 944 / 1,309 shares
  (29 Sep). So Instagram proves the JUDGMENT the Short reverses ("he slept around and got HIV"), not the white-suit beat.
- The couple: @magicjohnson's birthday post to Cookie, 115,124 likes / 14,051 comments (20 Jan 2026).
- The white-suit beat itself: **not found** in "magic johnson cookie" (24 posts; 4 opened, junk or off-beat),
  "magic johnson wife", "magic johnson press conference", "magic johnson story", "karl malone magic johnson"
  ("ANGRY AS HELL at Karl Malone", 109 likes / 259 shares). Refused: "magic johnson hiv", "cookie johnson magic".
- The judgment in public: "people openly told her to leave" (EssentiallySports, from her 2016 memoir *Believing in Magic*);
  Magic: "I don't know of many women who would have stayed in this situation" (Essence 2016). Reported, not raw comments.

## Other tellings (searched 20:00)
- **GMA, ABC, Sep 2016 (Robin Roberts)**, Cookie: "I mean, I fell to my knees… We both fell on our knees and we started
  crying" (as quoted by HuffPost). NOT downloaded. What the goodmorningamerica.com/video/42228948 URL actually served is a
  different ABC telling: **The View, Sep 2016** (see "Second telling" above; the `cookie-gma-*` folder names are historical).
- OWN *Super Soul Sunday* (2016, Oprah) and Apple TV+ *They Call Me Magic* (2022): named from summaries, not probed.
- PBS Frontline (2012): not found on pbs.org.

## Facts (G5)
- Press conference: Thu 7 Nov 1991, Great Western Forum; he wore a dark suit (The Root, ESPN, the CBS archive itself).
- Married September 1991 (CBS: "a little over a month" before; other outlets: "45 days" / "six weeks"): a card says
  **"MARRIED 6 WEEKS"** only if two sources agree at build, else "JUST MARRIED".
- Cookie was pregnant; she and the baby tested negative (CBS narration + Magic in the sit-down).
- 35 years: his X post on 7 Nov 2026, "still here and thriving" (theGrio, 8 Nov 2026).
- Last 12 months: no controversy found (Forbes billionaire 2026; Rose Parade grand marshal 1 Jan 2026; Knicks stake talk;
  Lakers commentary). The counter a commenter posts ("he cheated / slept with hundreds") is IN the Short: Cookie answers it.

## Sequence v1 (order C1: the event → the hardest thing → her reversal → the picture), ~40 s
| # | t in CBS file | Who | Words (trimmed) | Picture |
|---|---|---|---|---|
| 1 | 52.4-63.1 | Magic, 1991 | "Because of the HIV virus that I have attained, I will have to retire from the Lakers." | the podium (archive SD, letterboxed on blur) |
| 2 | 146.3-157.0 | Magic, 2021 | "The toughest thing… that I had to do was really drive home and tell Cookie. It was hard because I loved her so much and I hated to hurt her." | his close-up; card low: JUST MARRIED · SHE WAS PREGNANT |
| 3 | 431.9-434.6 + 443.8-451.2 | Gayle → Cookie | "When he told you how he got it, what was your thought?" → "It wasn't how he got it that was important to me. It was, you're possibly going to die. And that trumped everything." | Cookie close-up (crop clears the bug) |
| 4 | 408.4-411.8 | Gayle | "You're sitting there in that white suit. What were you thinking?" | 1991: Cookie in white beside Jerry Buss |
| 5 | 414.9-430.0 | Cookie | "I wore that white suit for a reason. I didn't want to wear anything dark or black, because to me, it's what it symbolized. And the white suit to me symbolized… brightness, like a future." | 1991 white suit → hard cut to the 2021 two-shot; card: 35 YEARS LATER, HE'S STILL HERE |
Hard cut on "a future". No narrator, no music (his job), 2 subscribe prompts mid.

## Variants (gate G)
- **Hook A (chosen): the 1991 announcement** in his own voice. Context in 5 s (who, what, the stakes), the moment everyone
  over 35 remembers.
- **Hook B: Gayle's "You're sitting there in that white suit. What were you thinking?"** over the 1991 shot (mystery first),
  then the announcement. Runner-up: stronger curiosity, weaker context (gate F: a stranger doesn't yet know who she is).
- **Hook C: "When he told you how he got it, what was your thought?"** (installs the judgment in 3 s, the advisor's
  suggestion). Kept as the A/B alternative if freshness shows the white suit already ran as a Short.
- **Order O1 (above):** event → wound → reversal → picture. **Order O2:** white-suit question → event → wound → reversal →
  the answer last (the mystery closes at the end). O1 wins because the reversal ("trumped everything") lands before the
  payoff picture, so the ending is the image, not an explanation.
- Titles (5 words max): "Magic Johnson's Wife Wore WHITE 💔" (chosen) / "She Didn't Leave Magic Johnson 💔".

## Closest AW winner and loser
- **Winner:** "Michael Jackson's Mother Refused To See His Body" (1.9M): a woman's choice at the worst moment, explained in her
  own voice; and "Winnie Harlow Was Called A COW" (1.1M), the one in-era non-MJ 3/3 Short, a face women place.
- **Loser:** "Why Princess Diana's Son Thought She Was ALIVE" (28K, 73.7 % stayed): the most famous face, a family wound in
  the son's own voice, still at the floor; and "Why Patrick Stewart's Father HIT His Mother" (13K). In-era non-MJ family
  wounds sit at 9.5-63K (median ~26K); 2 of 13 passed 100K.
- What differs here: the judgment (he slept around and got HIV) is live on Instagram this autumn (3 pages, 179K / 32K / 1.3K
  shares) and the wife answers it in one sentence on camera; Diana's and Patrick's had no judgment to reverse (MAGIC-FACTOR
  part 1). What is the same: a non-MJ face in front of the MJ audience.

## Gate statement (PITCH-CHECKLIST § 0), weak gates FIRST
| Gate | Result | Evidence |
|---|---|---|
| G4 Freshness | **OPEN** | YouTube flagged BLOCKED since 16:42 (not by me): no Shorts search for "magic johnson wife white suit", "cookie johnson white suit", "magic johnson hiv wife". CBS may have posted this moment as its own Short: check first |
| Judgment | **PARTIAL** | the judgment is live on Instagram (the how-he-got-it reels above) and reported ("people openly told her to leave", her memoir); not yet read in raw comments |
| Source quality | PASS with one insert below the anchor | CBS 1080p first-party, clean floor (-54 to -60 dBFS), anchor ≥ Prince for the 2021 sit-down; the 1991 white-suit and podium shots are archive SD → letterbox on blur, 2-3 s each |
| G1 Quotable image | PASS | "I wore that white suit for a reason" + the white suit on film |
| G2 What's on screen | PASS | the 1991 press conference itself, Cookie in white beside Jerry Buss |
| G3 Tone | PASS | composed sit-down, no laughter in the chosen windows |
| G5 Facts | PASS (dates pinned at build) | CBS + theGrio + The Root/ESPN; "6 weeks" vs "a little over a month" handled by the card wording |
| Shape | PASS | F1 + a physical mystery, one arc: event → the hardest thing → her reversal → the picture |
| Proof | topic only | Instagram 179,174 / 32,306 / 1,309 shares (the judgment); the beat itself unproven on Instagram; YouTube OPEN |
| His rules | PASS | ≤ 60 s (~40 s), no music, no minors on frame (the baby was not yet born), no censor words in the cut ("sexual contacts" is outside the trim) |
| Why interesting | the most famous HIV announcement in history had a message standing next to him that nobody read: his wife's white suit | |

**The viewer gets:** why Magic Johnson's wife wore white the day everyone thought he would die, and that she was right.

## Locked prediction (against the in-era non-MJ base rate, not the business era)
**15K-1.2M, centre 70-150K.** Named biggest failure: the MJ-majority feed meets a non-MJ face and an old news story and
swipes it like Diana (28K). **5K pre-mortem:** the first frame is 1991 SD news, "HIV" in the first line reads as a 35-year-old
headline, the feed refuses it (Winkler's 26 % feed signature). **5M pre-mortem:** the white suit is a picture women
screenshot; "it wasn't how he got it" starts a comment war (forgive vs leave) that shares like BANNED Birthdays did.

## Measured word boundaries for sequence v2 (WhisperX word times, 20:20; these supersede the rough windows above)
| # | File | In → out (s) | First word → last word | Note |
|---|---|---|---|---|
| 1 | CBS | 55.35 → 65.25 | "Because" → "Lakers" | starts after Gayle's VO "A tragic ending to a magical career" (52.4); 1991 archive |
| 2 | CBS | 149.15 → 157.52 | "But the toughest thing" → "hurt her" | the earlier window started on "…new drugs coming down the pipeline" (medicine): out of the cut; ", Gayle," can be trimmed |
| 3 | View | 231.70 → 240.82 | "he had to set himself in a room" → "good feeling" | optional beat |
| 4 | View | 250.47 → 259.69 | "At that time, I felt" → "help him live." | **the host says "I have so much respect…" from 259.71: hard cut exactly on "live."** (20 ms of air) |
| 5a | CBS | 409.43 → 412.22 | "You're sitting there in that white suit" → "thinking?" | Gayle |
| 5b | CBS | 415.48 → 428.39 | "And I wore that white suit" → "like a future" | cut on "future" (drop "basically") |
| 4 (lead order) | CBS | 431.87 → 434.21, then 443.76 → 452.32 | "When he told you how he got it… what was your thought?" → "It wasn't how he got it… trumped everything" | the 434.21-443.76 stretch ("probably through sexual contacts… blood transfusions") is cut out |
Raw speech v2 = 9.9 + 8.4 + 9.1 + 9.2 + 2.8 + 12.9 = 52.3 s; with pause trims ~44 s; without beat 3 ~36 s (≤ 60 either way).
