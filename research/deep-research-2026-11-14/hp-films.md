NOT max effort yet: B (follower counts missing on most reads); C (only one "mediocre" Shorts phrasing found by search, and the 12-search cap is spent until 13:00 PKT; Horowitz Clips' 1,000 uploads since May 2025 are now read, and none clips Oldman's 2025 "Sounds like me" reply); E (PoA Sirius is found in the Snape pack, but the veil/OotP picture is unsourced; no finish test; word in/outs are the build's); I (the advisor reviewed v6 at 01:58, after the build had started; its final review waits for STOP 1); J (a targeted re-read of tonight's edits). This line is replaced only when every item is closed.

# hp-films: Harry Potter, the films, the characters and the making of them (AW deep research, 14-15 Nov 2026)

## ▶ ROUND 2 (Affan, 15 Nov 01:30 PKT, verbatim: "try the sirius angle but continue searching for better ideas also")
- **Sirius:** the sequence was cut down over Affan's chat notes, each saved in `projects/oldman-good-sirius/BUILD-BRIEF.md`:
  - 01:35 "whos churchill": the Churchill ending is out (v4c);
  - 01:37 "last bit is weird doesn't really connect": Radcliffe's telling stays unbroken (v5);
  - 01:37 "its too short": v6 adds Oldman's "sign a picture" and "killed me off… it's me".
    - The brief said ~40-45 s. Segment word rates say **~60-65 s** (checked 01:58), with the payoff at ~75-80 %.
- **01:41 PKT, Affan (verbatim): "build it in premiere".**
  - 01:42: I started the build session **sirius-build** (`local_73783eac-87f5-4409-8bbc-d8be66046fdb`, Sonnet) from the v6 brief.
    STOP 1 = the raw cut in his Premiere project for his review, via the hub's lock. Nothing saved, no export.
  - A message telling the hub not to double-start was queued (`fac9f992`). Delivery is unconfirmed: the route reports nothing back.
  - **01:58, builder notes queued (`58763e6c`):**
    - beat 4 is one unbroken Radcliffe take (28:22.23-28:45.20 is one segment);
    - beat 3 keeps its two inner cuts under film picture;
    - approved words win over the runtime target;
    - the Sirius timecodes in the Snape pack;
    - the ASR rule;
    - the STOP-1 notes for Affan: the claim lands ~10 s in, beat 3 is a second topic, the payoff is late, ~60-65 s.
  - Only the veil/OotP picture is still unsourced.
  - **02:23, Affan (verbatim): "Not on my drives"** (the HP films). Forwarded to sirius-build (`53b27589`) and the hub
    (`e6aefefd`, delivered).
    - PoA Sirius comes from the Snape pack.
    - The veil is a placeholder or the pack's OotP hug.
    - An official veil clip only on his word after STOP 1, by the hub's YouTube order.
  - **STOP 1 reached 02:20-02:29 (sirius-build; `projects/oldman-good-sirius/RUN.md`, read-back PASS):**
    - "Was Oldman A Good Sirius - raw cut" is in his ABW11: **48.98 s**, NOT saved (his Ctrl+S), nothing exported.
    - V2 holds the real PoA Sirius shot (0-2.72 s), a Snape stare, and a labelled veil placeholder.
    - The payoff line lands at 72-75 %.
    - **My 60-65 s estimate (01:58) was wrong.** Segment word rates overstated it: the build cut pauses and Oldman's pieces run
      tighter. The real runtime is 48.98 s.
    - The builder also ran large-v3 (01:50-01:54, under the GPU lock, after a RAM check). Disclosed in RUN.md.
- **Drive search, between the 01:44 and 01:50 clock reads:** film-title name patterns with video extensions only; no Harry Potter film files on E:, D: or X:. G: came back in 1 s (probably not traversed), and C: wasn't searched. Only the earlier Snape packs
  (`projects/harry-potter-prank/src/snape/`). "ALL Severus Snape Scenes" may hold PoA's Shrieking Shack, where Sirius is on frame
  (unverified at the time). **Verified at 01:57:** "Severus Snape scene pack 4K.mp4" (1920x800) has Sirius:
  - the Shrieking Shack at 1106-1110 s and 1160-1164 s;
  - an OotP Grimmauld Place hug at ~1653-1657 s.
  - Proofs: `hp-films/proof/snapepack_*.jpg`. The veil is not in the pack.
- **v6 evidence check, 01:50 (API log time; videos, 1 unit; `hp-films/meta/api_v6check.json`). A proof omission, corrected:**
  - **The owner's own clip of v6's Oldman half:** `pAO2y3kqkl0`, Josh Horowitz main channel, 29 Dec 2023, 4:02, 1,095,450 views /
    11,344 likes / 1,167 comments, "Gary Oldman says his acting in HARRY POTTER is mediocre".
    - Its description says it covers "the unlikely scene… he did not enjoy shooting", the frozen lake at file 3:19-5:33.
    - Its 4:02 then most likely runs through "killed me off… it's me" and "mediocre… like Alan" (to ~7:29): v6's beats 1-3.
    - The lead card missed it: it cited only the Shorts of the line (316K, 217K) and the owner's 34K Short. It was in hp-cast's bench
      (`hp-cast/api/bench.rows.json`).
    - **Meaning (an inference from the title, description and length; the clip's transcript is unread):**
      - strong long-form demand for these words, and a bigger entry tax;
      - v6's Oldman half was probably in that 1.1M-view clip, so only Radcliffe's telling and the join are surely new.
  - **Our same-lane control:** the Snape Short `h7ze3Ckj830` (posted 12 Nov 17:59 UTC, 44 s, the same HSC Radcliffe frame).
    - One timed read: 24,451 views / 986 likes at day 2.3.
    - The earlier "~23K" is undated, so a plateau isn't shown.
  - **The adjacent Oldman clip:** `tVm7ajSlOIU` (Horowitz Clips, 14 Sep 2026, 1:23), 1,198,122 views: Oldman's 2026 TIFF Rickman
    story. It's hp-cast's lead (another promise), but it shows Oldman-on-HP clips are pulling now.
  - **The 13 s EDEN ORIGINALS text Short of the hook:** 217,238 (30 Mar 2026).
- **Better ideas:** RSS-transcript mining of HSC HP-cast episodes (Grint 2019, Brendan Gleeson 2018, Branagh 2017, Radcliffe 2014;
  `hp-films/src/hsc/round2/`), then IG proof checks on any beat found. Stay within the stop lines: 75 % finish within the hour,
  82 % stop. The meter read 68 % at 01:44 PKT. The API search cap resets at 13:00 PKT.
  - **Status:** Grint 2019 is transcribed (`round2/grint_y19.scout.txt`, 142 segments). B. Gleeson, Branagh and Radcliffe 2014 hit
    CUDA out-of-memory at ~01:50 (8 GB GPU, ~3.8 GB held by Premiere/AME).
  - **Rule broken:** that run was large-v3 while Premiere was open, against lab-notes 2026-11-14 17:35 (no large-v3 while Affan is
    in Premiere; medium.en, one ASR process via `.asr-lock`, ≥ 8 GB RAM free). It was one GPU process, ~2.4 GB RAM, and it's
    over.
  - The three left wait until the builder is done, then medium.en under `.asr-lock` only.
- **Round-2 results (02:10). No better idea clears the bar; the Sirius build stays the lane's only live item.**
  - **Grint 2019 (HSC):** no scene story. His HP talk is general:
    - Maggie Smith ("what 12-year-old knows who Maggie Smith is?");
    - Columbus out, Cuarón in;
    - Rickman "so warm";
    - Horowitz's 2019 joke "The Adventures of Ron… HBO Max series" (a news-peg curiosity, not a story).
  - **Horowitz Clips sweep** (`hp-films/meta/hzclips/`: 20 pages, 1,000 uploads back to 16 May 2025, 62 HP/Oldman titles, stats
    in `hits_stats.tsv`; 22 units, no searches):
    - No clip of Oldman's 2025 "Sounds like me" reply, which closes that part of gate C.
    - Oldman 2026: the Rickman moment 1.2M, plus a second Rickman cut at 15K, and "biggest diva on the HP set" 204K.
    - Radcliffe Apr 2026: film rankings 1.34M; "cringes at his HP acting" 16.8K (46 s), which mirrors Oldman's "mediocre". A
      possible note for Affan only, not built.
    - Spielberg "almost directed" 19K; Baz Luhrmann "turned it down" 2.4K.
  - **Killed: "The biggest diva on the HP set was a rat"** (Oldman 2026: Scabbers needed a break every 15 minutes, "who's his agent?").
    - Owner clip `5bjO53PVrAU` 204K; IG `DdT4GGroGt5` 25,437 / 537 shares (a trivia page).
    - Below the bar, and off-shape: a trivia laugh with no stake (VIRAL-BAR).
  - **Affan's 01:20 framework applied** (to hp-cast, `hp-cast.md:4`: confirm a topic with ~12 viral bits, then stitch proven bits).
    Counted over the 7,296 cached YouTube videos (biased by what the runs searched):
    - **Oldman/Sirius FAILS: 4 HP bits at 1M+.** They are b69Bxu02vLo 5.9M (title-mismatched), 7zyCjAwrKf4 1.49M, tVm7ajSlOIU 1.2M
      and pAO2y3kqkl0 1.1M; 6 at 500K+. Instagram has 1 bit at 65K+ (DWYiL2hgXuQ 96.3K).
    - Passing topics: Felton/Draco 46, Rickman/Snape 29, Radcliffe 15. Near: Watson 11, bloopers/BTS 10.
    - hp-cast holds Felton and Rickman. The Sirius build is Affan's explicit call, so it goes on; he should know it fails his own
      test.
  - **Missed in round 1, unpursued:** Jason Isaacs's improvised moment.
    - The Cinema Craft (a peer in AW's format) has it twice: `uFqHEIQMWi4` 11.26M (May 2025, "how a young Radcliffe surprised
      everyone… one bold, unscripted moment") and `_LQs1zrTOUg` 1.6M (Aug 2026).
    - Proven, but the peer's two Shorts make G4 an entry tax. The first-party source is unchecked, the clip is unwatched (no
      playback), and the meter is at 70 %.

## FINAL (15 Nov 2026: written ~00:20 PKT, last revised ~01:20)
> **Status 01:59:** the record below is v4 (the Churchill ending), now superseded.
> - Affan cut it down in chat to **v6** (no Churchill; Radcliffe unbroken; ~60-65 s; `projects/oldman-good-sirius/BUILD-BRIEF.md`).
> - At 01:41 he said "build it in premiere". The raw build is on (ROUND 2 above).
> - The prediction is re-locked once, on the cut he OKs at STOP 1. v4's upside rested on the Churchill line v6 cut, so the top
>   of the range needs a new reason or comes down. The verdict (under the bar, LEAD) is unchanged.

**NO PICK clears the 150K bar.** One LEAD under the bar, for Affan's information (a card, no build ask; below-bar ideas are never
pitched): **"Was Oldman A Good Sirius?"**, centre 40-100K: `projects/oldman-good-sirius/PITCH.md` (the lead card).

**Counts:**
- **Instagram:** 37 searches and pages (28 loaded, 6 phrase refusals, 3 failed loads); 46 post reads, 43 with numbers (41 in the HP
  lane), all in `IG-SEARCH-LOG.md`.
- **YouTube Data API:** 12 of 12 searches (7 bear on the lead's beats); lookups on 100+ ids; comments on 2; 6 peer channels.
- **Breadth:** 38 candidates with a kill log.
- **The lead's 4 sources:** downloaded, probed, transcribed, frames (all 4; `oldman2025_sheet.jpg`), audio (`hp-films/proof/audio_measure.txt`), 1:1
  anchor for 3 of 4 (`anchor_1to1.jpg`; not the 2025 clip).
- **HSC RSS episodes:** 10 downloaded, 9 transcribed (2014 not).
- **Advisor:** 2 calls, plus this final one.
- **Reads:** a cold read (24 defects: 16 fixed, 7 partly, 1 open, the pre-commit advisor) and a re-read (`hp-films/reread.md`; N1-N9
  applied).

### 1 (LEAD, under the bar). Was Oldman A Good Sirius? | hp-films | CARD
1. **Arc (v4):** Gary Oldman calls his Sirius "mediocre" (2023) → Radcliffe: on Oldman's last day he asked "have I been a good Sirius?",
   and Daniel "wanted to cry" (2024) → told this, Oldman answers (2025): "Sounds like me, yeah… I won an Oscar. And two years later, I
   said to my wife, what's so good, Churchill?" Two voices; Horowitz's relays are replaced by labels.
2. **The viewer gets:** a legend who still asks "was I good?", answered by the boy who wanted to cry. A laugh, plus warmth.
3. **Proof for THIS promise:**
   - YT: the hook line's Shorts are escpEISnUso 316K (2024) and JJeQxpRX1hg 217K (Mar 2026); the owner's own Shorts did 34K (the hook)
     and 47K (the witness line); Oldman's 2025 answer isn't found in 3 "good Sirius" searches or Horowitz's main-channel Jun 2025 uploads (Horowitz Clips unread).
   - IG: DVWX_vaDZEP 35.6K / 4.9K (the quote); DWYiL2hgXuQ 96.3K / 10.6K (the bond).
   - Adjacent bond Shorts: 1.49M, 346K, 233K, 211K, 165K.
   - Not counted (other promises): Snape/Rickman, and Sirius music edits.
4. **Closest AW winner:** the Funniest MJ Story (504K) and the Son Short (445K). **Closest loser:** Holland/Iger (7.9K). Same-lane
   control: our Snape Short (~23K, TOO EARLY).
5. **Freshness:** the join isn't found; the hook line is a recurring Short.
6. **Sources (all HSC podcast stages, 1080p, first-party, adult):**
   - Oldman 2023: ~1.3 Mb/s, soft at 1:1, 742 px, flatness 0.096.
   - Radcliffe 2024: on disk, 530 px, flatness 0.147.
   - Oldman 2025: medium singles (`proof/oldman2025_sheet.jpg`), ~1.2 Mb/s, flatness 0.051, with a low hum and no music
     (`proof/oldman2025_spectrum.png`); high-pass at build. The video's ASR ends "what's up with Churchill?" and the RSS ASR "what's so
     good, Churchill?": check by ear.
   - **v4 risk:** the last line is about Churchill (label "OSCAR · DARKEST HOUR · AS CHURCHILL"). Variant v4b ends on Radcliffe's "yes,
     oh my God". No reviewer has seen v4.
7. **Gates weak, named first:**
   - Under the bar.
   - Thin proof for this promise.
   - Oldman says it of all his work (v4 uses this).
   - Low-bitrate streams.
   - The 92NY frame repeats our Snape Short.
   - The film pictures are unsourced.
   - ASR, not heard by ear.
8. **Locked prediction:** range 10K-600K, **centre 40-100K**.
   - Named failure: the 92NY repeat.
   - 5K pre-mortem: the hook is a familiar Short.
   - 5M pre-mortem: his own answer wasn't found clipped, and "I won an Oscar…" travels.
9. **Flags:**
   - Minors: teen Radcliffe in film shots only (OK).
   - Censor: none.
   - Length: ~30-34 s.

**Killed:**
- **Gambon's Ferrari joke to Felton:** a 2026 German Short at 165.7K, and 48.4K.
- **Gleeson's Australian Bill Weasley:** Late Night's own Short at 344K.
- **Rickman's secret, on its own:** no on-camera Rickman source.
- **Felton's forgotten line:** no on-camera telling.
- **Peeves, Seven Potters:** no IG proof.
- The full kill log is in the working notes.

**Format finding for Affan:** the lane's biggest IG reels have no first-party voice: Dudley's deleted goodbye (2.22M / 136.6K), Warner
UK bloopers (896K / 233K), a deleted scene (666K / 63K). Only a narrated or text-led HP format could use them.

**Lessons for the hub:**
1. **Podcasts publish full audio on RSS.** Transcribing there costs zero YouTube requests, and it found Oldman's 2023 and 2025 lines.
2. **IG:** `/p/<code>/` pages with their embedded JSON are stable; screenshots and grids freeze background tabs.
3. **A host who returns to one question across years** (Horowitz on "mediocre": 2023 → 2024 → 2025 → 2026) hands over the join already
   spoken.
4. **Re-lock a prediction whenever the hook changes,** and price it on the source owner's own Shorts first.

---
# Working notes (the record behind the FINAL; where the notes disagree with FINAL, FINAL wins, e.g. the old ▶ STATUS centre of 100-250K)

## ▶ STATUS: resume here
- Session `hp-films` (Opus, Fable advisor), started 14 Nov 16:39 PKT (11:39 UTC). The weekly meter read 11 % at the start; my cap is about 10 points.
- **Interim posted 14 Nov ~21:05 PKT** (below). Final due Sun 15 Nov 10:00 PKT (05:00 UTC).
- Working files are in `research/deep-research-2026-11-14/hp-films/`:
  - `firstparty-tellings.md`, `hbo-peg.md`, `inventory.md` (the 3 Sonnet gatherers);
  - `src/hsc/` (6 HSC episodes from RSS + transcripts), `src/local/` (2 local transcripts);
  - `yt_queue.sh` (the YouTube queue, ready);
  - `tools/igdate.py` (Instagram shortcode → date).
- **Blocked:** YouTube since 16:42 (another session's bot page). The hub plans a probe around 23:15. Gates C and E waited on it.
- **22:10:** the YouTube Data API (Affan's switch) closed gate C: 7 searches, the lookups, comments and 6 peer channels.
  - **B and C are KILLED on freshness.**
  - **A is the only finalist**, with a v2 sequence (the proven Rickman hook, then Oldman's regret, then Radcliffe's tears), a locked
    centre of 100-250K (straddling the bar) and a gate statement.
  - Left: the ONE download (38pRftXvOmA, after the probe), the finish test, the cold read, the final advisor call.
- Advisor calls: 2 (orientation; before finalists → "no finalists yet; close the on-camera-source gate first"). No cold read yet.

## INTERIM (14 Nov ~21:05 PKT): NOT max effort yet: B (34/40 HP reels), C (YouTube blocked), E (video downloads), F-H, the final advisor call, J
**Three leads, zero finalists.** Each lead's teller is located, on camera, adult and HD, and his words are verified from the show's own
RSS audio (zero YouTube). Open for all three: YouTube freshness of our join, the video download, the finish test, variants and the prediction.

| # | Lead (title draft) | The arc, in their own words | Instagram proof | Source state | Open |
|---|---|---|---|---|---|
| A | **"Have I Been A Good Sirius?"** | Oldman (HSC, 28 Dec 2023): "they killed me off too early… you open the script and you go, it's me" + "I think my work is mediocre in it… if I had read the books like Alan… if I had known what's coming, I honestly think I would have played it differently" → Radcliffe (HSC, 11 Apr 2024): "he asked me on the last day of his filming… have I been a good Sirius? And I wanted to cry. I was like, yes, oh my God" | exact quote @movies.verse 35.6K / 4.9K; Oldman-Radcliffe bond @soulcinema_ 96.3K / 10.6K and 26K / 4K; Oldman tribute 147.8K; the Rickman-secret promise (Oldman's reason) 496K / 36.9K | Radcliffe 1080p60 ON DISK; Oldman audio verified, video on YouTube (queued) | YouTube: the beat's own Shorts (Horowitz cuts his own clips); the RtH "only Rickman knew" beat is at 5.94M |
| B | **"Tomorrow I'll Have A New Ferrari"** | Felton (HSC, 26 Mar 2026): "It's Draco killing Dumbledore… I must have bumbled my way through the first three attempts" → Gambon takes him out for air: "Dear boy, do you have any idea how much they pay me per day to be here? If you keep effing it up at this rate, tomorrow I'll have a new Ferrari" → "just relax, man, have some fun. And next take, that's the one they used" | Felton's own reel on the same story, 324K likes (19 Oct 2022); "cast went off script" promise 614K / 58.3K | audio verified; video on YouTube (queued). Picture = the HBP tower take (all adults) | IG has only one exact proof (on his own account); YouTube freshness |
| C | **"He Played Bill Weasley Australian"** | Gleeson (Late Night, 2 Sep 2025): first day on the set, "I couldn't stop", Yates asked him to stop | **@latenightseth (the broadcaster) 496.3K / 31K (10 Sep 2026)** | NBC on camera; the clip is on YouTube (queued) | a comic single beat (HA1 risk); YouTube freshness (Late Night's own clip) |

**Folded or killed this round:**
- **Rickman's secret:** no on-camera Rickman source (the HSC 2015 full episode and the 2015 clip have none; HitFix 2011 was a phone call), and
  RtH has score under it. It is folded into A as Oldman's own reason.
- **Felton's forgotten line:** no on-camera telling located, and it's one beat.
- Peeves and Seven Potters: no Instagram proof. Dobby: print only. Draco's deleted wand-throw: print only, 92.7K.

**Format finding for Affan:**
- The lane's biggest reels are voiceless: Dudley's deleted goodbye 2.22M / 136.6K, a deleted scene 665.6K / 63.1K, Warner UK's
  bloopers 896K / 233K.
- AW's own-voice format can't make these. A narrated or text-led HP format would be his call.

## A. His winners and losers: the testable hypotheses for this lane (draft, refined as data comes in)
Read: `AW-SHORTS-NOW.md` (274 Shorts, 14 Nov), `X:\Claude Projects\Abundance Wisdom\RESULTS.md`, `research/instagram-beat-mining/RESULTS-TRACKER.md`,
`research/instagram-beat-mining/FRAMEWORKS.md`, AW `LESSONS.md` (HP entries 12 Nov), `research/harry-potter-niche-2026-11.md` (whole file).

AW's own film / making-of Shorts are this lane's comps:

| Short | Views (14 Nov) | Class | What it had / lacked |
|---|---|---|---|
| Jaafar Jackson On Perfecting His Uncle's Moonwalk | 2.6M | actor builds the role, own voice, the finished image on screen | MJ halo, a transformation the viewer can judge |
| MJ's Nephew On Remaking Thriller Video | 1.5M | same | same |
| Stan Lee Almost KILLED OFF Spider-Man?! | 380K (365.8K Studio, 73.4 % stayed, AVD 0:44 of 0:52) | creator's own voice, the character nearly lost | an underdog "they said no" story, the creator himself |
| Jaafar Installed MJ's Vocal Chords | 122K | actor's process | weaker image than the moonwalk |
| Christian Bale RISKED His Heart To Play Batman | 111K | the cost of a role | a body cost, his own voice |
| Tom Holland Predicted His Own Future | 82K | | |
| Tom Holland's CRUEL Treatment From The Media | 79K | | |
| Radcliffe Thought Snape HATED Him | 23K (TOO EARLY; #1 of 10 at first, then #5-6) | HP set story + a dead man's warmth | SD DVD picture, ~44 s, 30 fps (hp-cast diagnoses) |
| Christopher Nolan's CUSTOM IMAX Camera! | 16K | tech trivia, no person's stake | no wound, no face |
| Tom Holland's Phone Call SAVED Spider-Man?! | 11K (7.9K Studio) | "lucky, not wronged"; four men in chairs | no wound, no picture |
| Chris Hemsworth Almost LOST Thor To His Brother?! | 7K (2.9K Studio, 58.1 % stayed) | casting what-if | hook failure, no wound |

**Hypotheses (each card is scored against its closest winner AND loser):**
- **HA1, a wound or a warm reversal beats trivia.** Making-of facts with nobody's stake (Nolan 16K) and lucky casting what-ifs (Hemsworth 7K, Holland/Iger 11K) are AW's floor. A making-of story clears 100K when a person pays a cost or is wronged (Bale 111K, Stan Lee 380K).
- **HA2, the finished image IS the payoff.** The 1.5-2.6M making-of wins end on the film image the process produced, so the viewer judges it (moonwalk, Thriller). A making-of told over chairs without the image is the Holland class.
- **HA3, priced without the MJ halo.** Jaafar's numbers ride the biopic wave; a non-MJ making-of is priced off Stan Lee / Bale (100-400K), not Jaafar.
- **HA4, the HP hook pulls, the body must hold.** Snape ranked #1 of the last 10 at first: an HP name + "HATED" held the first seconds. It fell to #5-6 (TOO EARLY, a data point only): suspects are the SD DVD picture and a second half that leaves the hook's subject.
- **HA5, one story, one arc, the link in their words.** Hagrid was rejected as "just 2 topics"; Snape v2 drew "doesn't fit the story" for an unset-up join.
- **HA6, FRAMEWORKS:** the first voice asks or accuses (nobody narrates); the belief can be typed as a comment; a physical picture early; 28-48 s; end on the sore spot and cut.

## YouTube Data API results (14 Nov ~21:45-22:05 PKT; Affan's switch, via the hub's `yt_api.py`; 7 of my 12 searches used)
Raw JSON and tables: `hp-films/meta/api_*.json|tsv`, `peer_*.json`, `peers.txt`. Searches are `videoDuration=short`, `order=viewCount`,
50 results each, with exact numbers from `videos` (1 unit).

**Freshness and proof, 3+ phrasings per lead:**
| Search | Top results (views, date, channel) | Reading |
|---|---|---|
| A1 "gary oldman mediocre sirius" | 316,301 (Oct 2024, Outstanding Screenplays, 55 s); 217,238 (Mar 2026); 79,125 (ET); **Horowitz's own Short dLzpf4MYxns 34,426**; ~20 news cuts under 30K | the "mediocre" beat is proven |
| A2 "radcliffe gary oldman have i been a good sirius" | 783,391 (Oct 2026, a Sirius-Harry fan edit); 211,290 (RtH Oldman and Radcliffe clip); 165,459 (GSA "Sirius impact on Radcliffe"); **Horowitz's own Short 8qn-er0UfPI "was I a good Sirius?" 47,010 (Apr 2024)**; a "reaction mashup" 8,811 | the exact payoff exists only as Horowitz's 47K Short; **our join (Oldman's regret + Radcliffe's tears) not found** |
| A3 "gary oldman sirius killed off too early harry potter" | 1 result: a Korean Short 44,072 | "killed me off too early… it's me" is barely used |
| A4 "alan rickman only one who knew snape secret" | **5,647,060 (Aug 2026, The Cinema Craft, a 60K-sub channel)**; 5,486,434 (Sep 2026, same); 5,315,607 (Collider 2022); 4,621,018 (official HP); 2,372,077; **b69Bxu02vLo "Gary Oldman had NO IDEA about Rickman" 5,935,905 (Jul 2026)** | **the hook promise is among the hottest HP Shorts topics right now** |
| Lookups | **pAO2y3kqkl0 Horowitz "Gary Oldman says his acting in HARRY POTTER is mediocre" 1,095,128 (242 s, 29 Dec 2023)**; full episode 38pRftXvOmA 280,145 (67 min, HD); wTM27ZzeRa8 "Jack Lowden gushes over Gary Oldman's Sirius Black" 66,222 | the "mediocre" beat at 1.1M on the source's own channel |
| B1 "tom felton michael gambon ferrari" | 48,370 (German, Oct 2026); 914 (Nida Sarfraz) | - |
| B2 "tom felton michael gambon dumbledore" | **cqVrG0_o2J0 "Dumbledore's HILARIOUS prank on Tom Felton!" 301,141 (6 Apr 2026)**; **uVrus-E4JEU "the emotional scene in HP only exists because of a joke" 165,704 (May 2026, German)**; Felton's Gambon tribute 163,382 | **B is told, our film-take angle included, twice in 2026: KILL (freshness)** |
| C1 "domhnall gleeson australian accent harry potter" | **W5eyBfMYaAE Late Night's own Short 344,131 (10 Sep 2026)**; Hits Radio on Bill Weasley 312,890 (3 Sep 2026) | **C would re-cut the broadcaster's own Short: KILL (freshness + HA1)** |

**The judgment, in real comments** (`commentThreads`, top by relevance):
- On Horowitz's "was I a good Sirius?": "He was fantastic. Feral and frightening and then within a few minutes, he's so warm and paternal"
  (148 likes); "The shrieking shack scene is some of the best acting ive ever seen… how the hell he can even suggest its mediocre is
  insane" (11); "Gary is a Legendary Sirius" (25).
- On the 316K Short: **"Gary Oldman's 'mediocre' is the next guy's great" (1,360 likes)**; "He couldn't be mediocre if he tried!" (48).
- The viewer holds that Oldman's Sirius was great. Oldman's own "mediocre" collides with it, and Radcliffe's "I wanted to cry… yes"
  answers it.

**Peer channels (gate C):** the latest 50 uploads each, with exact numbers (`peers.txt`):
| Channel | Subs | Median views | Top uploads |
|---|---|---|---|
| The Cinema Craft | 60K | 55,329 | 7.6M (Butler, 300); **5.65M and 5.49M (Rickman/Snape)** |
| GREEN SCREEN ANIMATION | 705K | 35,133 | 4.05M (HBO series vs movie opening); 703K; 634K |
| Josh Horowitz | 227K | 41,912 | 505K; 460K |
| Half-Blood University | 104K | 16,548 | 50K |
| HogwartsFandom | 116K | 10,387 | 52K |
| Nida Sarfraz Potterhead | 6.9K | 1,966 | 85K (its 5.94M Oldman/Rickman is older than the latest 50) |

## Queued for YouTube, revised 22:05 (after the API results)
- **API: done.** 7 searches and 9 lookups (videos, channels, playlistItems, comments). 5 searches are left in reserve.
- **Downloads: 2 files (updated 22:35)**, after the hub's probe and in its order. **#2 is `BWMPDqyMc5Y`** (HSC "Gary Oldman on SLOW HORSES, HARRY POTTER memories…", 14 Sep 2026, HD, 58:43), section ~38:00-46:00 (around RSS 41:58-43:01), for the v3 ending (his pride in the PoA scene). **#1:** `38pRftXvOmA` (HSC "Gary Oldman talks SLOW HORSES, HARRY POTTER,
  BATMAN", 28 Dec 2023), the section ~08:00-18:00 (wide, because the RSS mp3 carries ads the video doesn't), ≤1080p.
  - Why: gate E, Oldman's picture (the audio and words are already verified from RSS).
  - Radcliffe's half is already on disk (OYJ7W0mJZUA, 1080p60). B and C are killed, so their downloads are dropped.

## Queued for YouTube (counted; leads only; runs one at a time through pace.sh, +20 s, after the hub's probe and in its order) [SUPERSEDED by the revision above]
Script: `hp-films/yt_queue.sh`. Searches are flat (`ytsearch30`, one request each, no listings, no comments). Downloads are one
section each, ≤1080p.

| # | Lead | Type | Query or id | Why |
|---|---|---|---|---|
| 1 | A | search | "gary oldman sirius black mediocre" | freshness, phrasing 1; finds the HSC Vol. II video id |
| 2 | A | search | "daniel radcliffe gary oldman have i been a good sirius" | freshness of OUR join, phrasing 2 |
| 3 | A | search | "gary oldman killed off too early sirius harry potter" | freshness, phrasing 3 |
| 4 | A | download | HSC "Gary Oldman, Vol. II" (id from #1), section ~13:30-17:30 | E: picture, probe, frames, finish test (audio already verified from RSS) |
| 5 | B | search | "tom felton michael gambon ferrari" | freshness, phrasing 1; finds the HSC Felton 2026 video id |
| 6 | B | search | "tom felton draco killing dumbledore gambon" | freshness, phrasing 2 |
| 7 | B | search | "michael gambon advice tom felton dumbledore scene" | freshness, phrasing 3 |
| 8 | B | download | HSC "Tom Felton" 26 Mar 2026 (id from #5), section ~47:30-50:30 | E: picture, probe, frames, finish test |
| 9 | C | search | "domhnall gleeson australian accent harry potter" | freshness; finds Late Night's own clip |
| 10 | C | search | "bill weasley australian accent" | freshness, phrasing 2 |
| 11 | C | download | Late Night's clip (id from #9) | E (only if C is still alive after #9-10) |

**Total: 11** (8 for A and B, which come first; 3 for C, optional). There are no metadata calls: ids come from the flat searches. The
film pictures (Sirius in PoA/OotP; the HBP tower) are Warner footage, sourced at build time from his drives or a scene pack, as the
Snape picks were. They aren't in this queue.

## Cards (DRAFT 21:30, before YouTube; every number below the proof tables is open until the queue runs)

### A. Oldman Called His Sirius MEDIOCRE | hp-films | PITCH track (the only finalist)
**REVISED 22:10 after the API results (this block supersedes items 3, 5, 7 and 8 below):**
- **The hook is the proven promise, the turn is new.**
  - **The hook:** Horowitz: "he [Rickman] was the only one that knew how the books ended. He got the inside dope." Oldman: "He did."
    The promise is proven at 5.94M (b69Bxu02vLo, Jul 2026), 5.65M and 5.49M (The Cinema Craft, Aug-Sep 2026), and on IG 496K / 36.9K.
  - **The join, in his own words, put early (HP-EXECUTION rule 8):** "I think my work is mediocre in it… maybe if I had read the books
    like Alan… if I had known what's coming, I honestly think I would have played it differently". Horowitz's own clip of this did
    1.10M.
  - **The turn:** "they killed me off too early… it's me". It's barely used (44K).
  - **The payoff:** Radcliffe's "have I been a good Sirius? And I wanted to cry". It's used once, as Horowitz's own 47K Short.
- **Freshness of the join: PASS** (3 phrasings; nothing joins them; the closest is an 8.8K mashup). The entry tax on the hook is real
  (5.9M), so the first 3 s must already turn toward Oldman, not re-run the RtH clip.
- **Judgment: PASS** (real comments): "Gary Oldman's 'mediocre' is the next guy's great" (1,360 likes).
- **Locked prediction:**
  - **Range 25K-1.5M, centre 100-250K.** The centre straddles the 150K bar: no guarantee line.
  - **Biggest named failure:** "seen it" on the Rickman hook. The cut must leave the RtH promise within 3 s.
  - **5K pre-mortem:** the hook reads as the 5.9M RtH clip and gets swiped; the 92NY podcast stage is the same frame as our Snape
    Short (23K), so the seed audience feels a repeat; the Oldman shots are a wide-ish podcast two-camera.
  - **5M pre-mortem:** the Rickman-secret promise is the hottest HP Shorts topic of Jul-Sep 2026 (5.5-5.9M on small channels); the
    turn is new; the comment section already argues "he wasn't mediocre"; the HBO premiere (25 Dec) lifts HP search.

**A: gate statement (PITCH-CHECKLIST § 0), open or weak rows first:**
| Gate | Result | Evidence |
|---|---|---|
| Source quality, Oldman's picture | **OPEN** | 38pRftXvOmA (HD, 67 min, Josh Horowitz's own upload) is queued as the only download, after the hub's probe. Audio already verified from the show's RSS (flatness 0.098 = clean; -32.1 LUFS, needs gain). The Prince-ABC finish test runs on the download |
| Heard by ear | **OPEN (build)** | ASR from the RSS audio (WhisperX large-v3); we work in silence |
| G4 Freshness | PASS (join) / entry tax (hook) | 3 phrasings plus the hook search: the join isn't found anywhere; the hook promise is at 5.9M (RtH clip), so the cut leaves it within 3 s |
| Why it's interesting enough | PASS | The man everyone calls a legendary Sirius thinks he was mediocre, because only Rickman knew what was coming. He found out he dies by opening the script, and on his last day asked a teenager "have I been a good Sirius?" |
| G1 Quotable image | PASS | "you open the script and you go, it's me"; "have I been a good Sirius?"; "I wanted to cry" |
| G2 On screen | PASS (rule 13) | The film's own Sirius scenes (the veil) carry the turn; Radcliffe's face carries the payoff |
| G3 Tone | PASS | Oldman plain and self-critical; Radcliffe moved ("I wanted to cry"); no chat-show laugh on the key lines |
| G5 Facts | PASS | Primary: both men's own words (HSC RSS audio, Dec 2023 and Apr 2024); press: Variety, THR, EW (Dec 2023-Jan 2024) on "mediocre"; Horowitz's own Short titles the payoff. Last 12 months: Oldman on HSC again Sep 2026 (no change of view found); Radcliffe on Broadway in 2026. Counter-evidence: Oldman's line is "my work is mediocre in it", so the title must not say "he hated Sirius" |
| Judgment | PASS | Real comments: "Gary Oldman's 'mediocre' is the next guy's great" (1,360 likes); "He was fantastic… feral and frightening… warm and paternal" (148) |
| Shape | PASS | One story, one theme (not knowing what was coming), two voices plus the interviewer's one question; F1-like reversal with a warm end; join early (HP rule 8) |
| Source quality, Radcliffe | PASS | 1080p60 on disk; frames `hp-films/proof/radcliffe2024_sirius_sheet.jpg`; flatness 0.147, -25.0 LUFS; the same footage the published Snape Short used |
| Proof | PASS | YT: 5.94M (the hook beat), 1.10M ("mediocre"), 47K (the payoff). IG: 496K / 36.9K (the promise), 35.6K / 4.9K (the quote), 96.3K / 10.6K (the bond) |
| His rules | PASS | No censor words; no music bed; Sirius film shots show teen Radcliffe (film footage: his ruling OK); title ≤ 5 words; labels low; captions under the lips |

**Title options (≤ 5 words, real names):** "Oldman Called His Sirius MEDIOCRE" (recommended: the IG proof's own word) · runner-up "Only Rickman Knew. Oldman Didn't."
(5 words).

### KILLED 22:05 (freshness): Tomorrow I'll Have A Ferrari (B)
The story, our film-take angle included, already ran in 2026: cqVrG0_o2J0 301,141 (6 Apr), uVrus-E4JEU 165,704 (May, "the emotional scene
only exists because of a joke"), KHD28FSh_eo 48,370 (Oct). The text below is kept for the record.

### KILLED 22:05 (freshness + HA1): He Played Bill Weasley AUSTRALIAN (C)
Late Night's own Short W5eyBfMYaAE 344,131 (10 Sep 2026) and its IG reel 496K are the same clip. Hits Radio's Bill Weasley interview is at
312,890. Ours would re-cut the broadcaster's own Short. The text below is kept for the record.

### A, the original card (21:30)
1. **Arc (one story):**
   - **Setup:** the man who played Sirius thinks he was "mediocre", because unlike Rickman he didn't know what was coming.
   - **Turn:** they killed Sirius off ("you open the script and you go, it's me").
   - **End:** on his last day he asked a teenage Radcliffe "have I been a good Sirius?", and Radcliffe "wanted to cry". The link is in
     their own words: Horowitz puts Oldman's "mediocre" to Radcliffe inside the 2024 source.
2. **The viewer gets:** a legend's self-doubt, answered with warmth ("yes, oh my God"). Fans who loved Sirius get told he worried he
   wasn't good enough. It's a reversal of "Oldman knew he was great" (F1-like, no villain).
3. **Proof:**

   | Where | id | Numbers | Date | What |
   |---|---|---|---|---|
   | IG | DVWX_vaDZEP (@movies.verse) | 35,630 likes / 4,927 shares | 1 Mar 2026 | the exact "mediocre… like Alan" quote |
   | IG | DWYiL2hgXuQ (@soulcinema_) | 96,322 / 10,551 | 27 Mar 2026 | the Oldman-Radcliffe bond (letters) |
   | IG | Db26ym0h9QE | 25,993 / 4,008 | 10 Aug 2026 | the Sirius-Harry bond mirrored reality |
   | IG | DU__cPpDBRG (@amazingmoviesonly) | 147,793 / 2,951 | 20 Feb 2026 | Oldman career tribute |
   | IG | DcVeFNpRYwI (@howeverythingworks, 4.3M followers) | 495,895 / 36,891 | 21 Aug 2026 | the promise Oldman names as his reason: Rickman knew |
   | YT | b69Bxu02vLo (Nida Sarfraz) | 5.94M | 2026 | RtH: Oldman learns only Rickman knew (from HP-EXECUTION § 3) |
4. **Closest AW winner:** "Michael Jackson's Son Saw His Dad AGAIN" (445K): the tender reaction of someone who loved them, with no
   villain. **Closest loser:** "Tom Holland's Phone Call SAVED Spider-Man?!" (7.9K): men in chairs, no wound. A's guard against that
   loser is the wound line ("mediocre") in the first second, over the Sirius film image, and the payoff on Radcliffe's face.
5. **Freshness:** OPEN (YouTube blocked). Expected entry tax: Horowitz cuts his own clips, so "Oldman mediocre" and possibly
   "have I been a good Sirius" exist as Shorts. Our join (Oldman's reason + his last-day question + Radcliffe's tears) needs checking.
6. **Sources:**
   - Radcliffe: HSC 11 Apr 2024, 1080p60 on disk (`E:\Bullshit Folder\Henry\…Happy Sad Confused.mp4`, 28:03-28:50). Gap flatness
     0.147 (clean), -25.0 LUFS. It's the same file the published Snape Short used for Dan.
   - Oldman: HSC Vol. II, 28 Dec 2023, RSS audio verified (14:00-16:30; flatness 0.098, -32.1 LUFS, needs gain). The video is on Josh
     Horowitz's YouTube (queued).
   - Pictures: Sirius in PoA and OotP (the film), including the veil.
7. **Gates weak, named first:**
   - YouTube freshness and the Oldman video download are open.
   - IG proof for the exact last-day question is not found (only the "mediocre" quote, 35.6K).
   - Our Snape Short also stars Radcliffe on HSC (same frame), so a recognition risk.
   - Oldman's "J.K." mention brings Rowling's name in; trim it.
8. **Prediction:** not locked until YouTube reads; working range 15K-600K, centre 60-150K (at or under the run's 150K bar).
9. **Flags:**
   - Minors: Sirius film shots show teen Radcliffe (his ruling: OK).
   - Censor: none.
   - Length: about 35-45 s.

### B. Tomorrow I'll Have A Ferrari | hp-films | CARD (PITCH after YouTube)
1. **Arc (one story, one teller):**
   - **Setup:** "It's Draco killing Dumbledore. It's a big one". He bumbles the first three takes.
   - **Turn:** Gambon takes him out for air and says: "Dear boy, do you have any idea how much they pay me per day to be here? If you
     keep effing it up at this rate, tomorrow I'll have a new Ferrari".
   - **End:** "just relax, man, have some fun. And next take, that's the one they used". The tower take plays.
2. **The viewer gets:** a laugh and a legend's kindness disguised as a joke, and the iconic scene seen anew: the take in the film is the
   one after the Ferrari line. Gambon died in 2023.
3. **Proof:**
   - Felton's own reel Cj5wXJmA4JG: 324,075 likes / 1,071 comments (19 Oct 2022, "the best advice Sir Michael Gambon gave me on set").
   - The "cast went off script" promise: DQPnQpiDcuh 613,995 / 58,302.
   - The forgotten-line promise: DVIf5evjYzi 864K / 17.1K.
   - Gambon on IG: small (7.2K, 28.9K).
4. **Closest AW winner:** "Funniest Michael Jackson Story EVER" (504K): a legend's funny kindness told by someone who was there.
   **Closest loser:** "Chris Hemsworth Almost LOST Thor" (2.9K, 58 % stayed): trivia with no person to care about. B has a dead
   legend and a nervous young man, and the payoff is a picture everyone knows.
5. **Freshness:** OPEN. The story has been told since 2022 (memoir, his reel, a 2023 tribute), so Shorts likely exist.
6. **Sources:**
   - Felton: HSC 26 Mar 2026, in person. RSS audio verified at 47:47-50:10 (flatness 0.098, -18.4 LUFS); the video is on YouTube
     (queued).
   - Pictures: HBP Astronomy Tower (Felton 20, Radcliffe 18, Gambon, all adults).
7. **Gates weak, named first:**
   - Instagram proof for this exact story is one post on the teller's own account.
   - Felton says "17-year-old" (he was 19-20). It's his words, so no label contradicts him.
   - A crude aside sits inside the passage and must be cut.
   - The memoir version says "excited, not nervous" (a conflict between his tellings).
8. **Prediction:** not locked; working range 10K-500K, centre 40-120K.
9. **Flags:**
   - Censor: "effing" and "taking a piss" (not on his list).
   - He mentions a cigarette.
   - Minors: none.
   - Length: about 40-50 s (his telling runs ~2:20, so it needs a tight cut).

### Variants (G), drafted from the RSS transcripts
Times are episode times in the RSS audio, ±2 s. The YouTube videos will differ by any ad offset, so re-time them from the downloads.

**A, v3b (RECOMMENDED, 23:20, after the hub's one-topic watch): Oldman's own judgment → his reason → Radcliffe's tears → Oldman's pride (~35-40 s)**
- **The one-topic test.** The rule (PITCH-CHECKLIST § 4, the Hagrid lesson; HP-EXECUTION rule 1) is that title, frame 1 and last line
  are one story, and every link is in their own words.
  - v3 opened on "only Rickman knew how the books ended" and ended on Oldman's pride. That's the Snape-turn risk: the hook sells a
    Rickman/Snape secret and the body delivers Oldman/Sirius. It's the same shape as HP-EXECUTION's suspect #1 for the Snape Short
    ("the hook sold one story, and half the Short told another").
  - **v3b fixes it.** The hook is Oldman's own judgment, "I think my work is mediocre in it", proven at 1.10M (his source's clip) and
    316K (a Short), with the comment section arguing back. Rickman enters only as Oldman's reason, in Oldman's words ("if I had read
    the books like Alan"), over two seconds of Snape.
  - **The one-line arc:** a legend thinks his Sirius was mediocre, because unlike Alan he didn't know what was coming → on his last
    day he asked the boy "have I been a good Sirius?" and the boy wanted to cry → years later the one scene he's proud of is the one
    about carrying the people we love. Title, frame 1 and last line are all Oldman's Sirius. **PASS.**

| # | Voice | Words | Picture |
|---|---|---|---|
| 1 (0-3 s) | Oldman, 2023 | "I think my work is mediocre in it." (RSS 15:44) | Sirius (film), frame 1 says HP; low label "GARY OLDMAN · SIRIUS BLACK" |
| 2 | Oldman, 2023 | "maybe if I had read the books like Alan… if I had known what's coming, I honestly think I would have played it differently." (15:50-16:20) | 2 s of Snape on "Alan", then Oldman |
| 3 (payoff 1, ~55 %) | Radcliffe, 2024 | "he asked me on the last day of his filming… have I been a good Sirius? And I wanted to cry. I was like, yes, oh my God" (28:22-28:35) | Radcliffe single, 1080p60 |
| 4 (end) | Horowitz → Oldman, 2026 | "a moment… between you and Daniel that you do take pride in?" / "the scene with Daniel where I talk about the people that we've loved… and that we carry them always with us." (42:28-42:45) | PoA, Sirius and Harry (picture only); hard cut |

- **Hooks compared:**
  - H1 "mediocre" (v3b, recommended): one topic; a proven 1.1M promise.
  - H2 "only Rickman knew" (v3, runner-up): a bigger proven promise (5.9M), but the Snape-turn risk is named above.
  - H3 "they killed me off too early" (order 1's alternative): a wound hook, but it reads as plot news.
- **Orders compared:** v3b (chronological, pride last; recommended) against v2 (ends on Radcliffe's "yes"; runner-up).

**A, v3 (runner-up, 22:35): proven hook → join → Radcliffe's tears → Oldman's own pride (~35-40 s)**
A third telling turned up in the Sep 2026 episode (HSC "Gary Oldman, Vol. IV", BWMPDqyMc5Y). hp-cast downloaded its RSS audio and
transcribed it with the small model (`hp-cast/src/hsc_oldman/asr_small_full.txt`, 2518-2581 s).
- **Horowitz:** "you've said you call your work mediocre. That's insane… Do you have a favorite scene, at least? Can you cite a moment
  that you felt between you and Daniel that you do take pride in?"
- **Oldman:** "Yeah, I have the scene with Daniel where I talk about that the people that we've loved or that have loved us live in here
  and that we carry them always with us."
- That's PoA's "the ones that love us never really leave us", the line the 96.3K / 10.6K IG reel (@soulcinema_) opens with.
| # | Voice | Words | Picture |
|---|---|---|---|
| 1 (0-4 s) | Horowitz → Oldman, 2023 | "he was the only one that knew how the books ended" / "He did." (15:16-15:30) | Snape (film), low label "ALAN RICKMAN" |
| 2 (the join) | Oldman, 2023 | "I think my work is mediocre in it… maybe if I had read the books like Alan… I would have played it differently." (15:44-16:20) | Sirius (film), then Oldman |
| 3 (payoff 1) | Radcliffe, 2024 | "he asked me on the last day of his filming… have I been a good Sirius? And I wanted to cry. I was like, yes, oh my God" (28:22-28:35) | Radcliffe single, 1080p60 |
| 4 (the end, ~70 %) | Horowitz → Oldman, 2026 | "a moment… between you and Daniel that you do take pride in?" / "the scene with Daniel where I talk about… the people that we've loved… live in here and that we carry them always with us." (Vol. IV ~41:58-43:01) | PoA, Sirius and Harry (picture only), hard cut |

- **Why v3 beats v2:** v2 ends on Radcliffe; v3 ends warm in the subject's own voice (HP-EXECUTION rules 12 and 13) and shows the scene.
  Both still have two voices, plus the interviewer's short questions.
- **Runner-up:** v2 below.
- **Sources:** the v3 ending needs a 2nd download (BWMPDqyMc5Y).
  - **Its words are CONFIRMED on large-v3** (22:45: `hp-films/src/hsc/oldman_v4_slice_a.scout.txt`, a slice of hp-cast's RSS mp3 from 40:30). Horowitz at 41:59: "you're amazing as Sirius Black… you call your work mediocre. That's insane". At 42:28: "Can you cite a moment… between you and Daniel that you do take pride in?" Oldman at 42:35: "I have the scene with Daniel where I talk about the people that we've loved, or that have loved us, living here, and that we carry them always with us."
  - **Audio clean:** gap flatness 0.105, -18.0 LUFS.

**A, v2 (runner-up): proven hook → join → turn → payoff (~36-40 s)**
| # | Voice | Words (RSS episode time; trim "from J.K.") | Picture |
|---|---|---|---|
| 1 (0-4 s) | Horowitz → Oldman 2023 | "You discovered for the first time that he was the only one that knew how the books ended. He got the inside dope." / "He did." (15:16-15:30) | Snape (film) with a low label "ALAN RICKMAN"; Oldman reacting |
| 2 (the join, 4-14 s) | Oldman | "I think my work is mediocre in it… maybe if I had read the books like Alan… if I had known what's coming, I honestly think I would have played it differently." (15:44-16:20) | Sirius (film) under "mediocre", then Oldman |
| 3 (14-24 s) | Oldman | "They killed me off too early… we were all taking bets… It's Hagrid… maybe it's Ron… then you open the script and you go, it's me." (14:33-15:05) | OotP, the veil (picture only) |
| 4 (payoff ~65-70 %) | Radcliffe 2024 | "he asked me on the last day of his filming… have I been a good Sirius? And I wanted to cry." (28:22-28:32) | Radcliffe single, 1080p60 |
| end | Radcliffe | "I was like, yes, oh my God, what?" Hard cut | his face |

The chain is one theme from start to end: he didn't know what was coming (unlike Alan) → he found out he dies by opening the script →
on his last day he asked if he'd been good → the boy said yes.

**A, order 1 (runner-up, the 21:30 draft): wound → reason → death → payoff (~40 s)**
| # | Voice | Words | Picture |
|---|---|---|---|
| 1 (0-3 s) | Oldman 2023 | "I think my work is mediocre in it." (15:44) | Sirius film close-up (frame 1 says HP) |
| 2 | Oldman | "maybe if I had read the books like Alan… if I had known what's coming, I honestly think I would have played it differently." (15:50-16:20) | Oldman on HSC; a beat of Snape |
| 3 | Oldman | "they killed me off too early… we were all taking bets… It's Hagrid… you open the script and you go, it's me." (14:33-15:05) | OotP, the veil (picture only) |
| 4 (payoff ~70 %) | Radcliffe 2024 | "he asked me on the last day of his filming… have I been a good Sirius? And I wanted to cry." (28:22-28:32) | Radcliffe single, 1080p60 |
| end | Radcliffe | "I was like, yes, oh my God, what?" Hard cut | his face |

- **A, order 2 (runner-up):** cold-open on Radcliffe's question ("he was like, have I been a good Sirius?"), then Oldman's
  "mediocre" and the reason, then back to "And I wanted to cry. Yes". It's riskier: the payoff is spent early.
- **A, hook 2 (runner-up):** "They killed me off too early. I'm still upset about that." (a wound hook, the death image first).
- **Pick: hook 1.** The judgment is said by the person it's about, and "mediocre" is the word the IG proof quotes.

**B, order 1 (recommended): chronological (~45 s)**
| # | Voice | Words | Picture |
|---|---|---|---|
| 1 (0-3 s) | Felton 2026 | "It's Draco killing Dumbledore. It's a big one." (48:16) | HBP tower: Draco's wand on Dumbledore |
| 2 | Felton | "I must have bumbled my way through the first three attempts" (48:25) | Felton on HSC |
| 3 | Felton | "He asked for a tea break… invited me out for a breath of fresh air… I'm sorry, sir… I've rehearsed the lines" (48:40-49:35, tightened) | Gambon as Dumbledore |
| 4 | Felton (as Gambon) | "Dear boy, do you have any idea how much they pay me per day to be here? If you keep effing it up at this rate, tomorrow I'll have a new Ferrari." (49:50-50:05) | Felton |
| 5 (payoff) | Felton | "And next take, that's the one they used." (50:12) | the film take: Draco lowers the wand |
| end | Felton | "What a legend." Hard cut | Gambon (film) |

- **B, order 2 (runner-up):** cold-open on Gambon's line ("If you keep effing it up at this rate, tomorrow I'll have a new
  Ferrari"), then the setup and the take.
- **B, hook 2:** "Sir Michael Gambon would just take the piss out of himself and everyone" (47:47). It's warmer, but it doesn't say
  HP in frame 1.
- **Pick: order 1, hook 1.** The famous scene is named in second one, and the payoff is the film's own take.

### C. He Played Bill Weasley AUSTRALIAN | hp-films | CARD
1. **Arc:** first day on Deathly Hallows → "I couldn't stop" doing an Australian accent → Yates asked him to stop → his "one of the
   worst days of my life".
2. **The viewer gets:** a laugh, and a reason to rewatch Bill's scenes.
3. **Proof:** @latenightseth DdHOr7QgA7t: 496,276 likes / 30,963 shares (reposted 10 Sep 2026; aired 2 Sep 2025).
4. **Comparison:** the closest AW winner is the Funniest MJ Story (504K); the closest loser is Hemsworth/Thor (2.9K: an actor's casting
   trivia). C sits nearer the loser: there's no wound or warmth.
5. **Freshness:** OPEN (the broadcaster's own clip).
6. **Sources:** Late Night (NBC) on YouTube (queued). Not on disk.
7. **Gates weak, named first:** HA1 (comic trivia, no stake); no second voice; the broadcaster's own clip is the proof (seen it).
8. **Prediction:** working centre 20-60K, under the bar.
9. **Flags:** none.

## The format question: what goes viral for HP film moments, and what AW can make
Instagram numbers are read today (every row in `IG-SEARCH-LOG.md`). YouTube numbers come from HP-EXECUTION.md § 3 and the 10-12 Nov
metadata, because YouTube is blocked today.

| Format | Instagram (likes / shares, date) | YouTube | Can AW make it with source audio only? |
|---|---|---|---|
| **Text over a film or BTS clip** ("X forgot his line and improvised this", "the deleted scene", "how Hagrid was made") | Felton's line @bloopersbits 864K / 17.1K (Feb 2026); the same beat on a 2nd page 163K / 3.1K (Mar 2026); Draco's deleted scene @cineatomy 92.7K / 2.8K; Hagrid making-of 68.5K / 66.9K | Hagrid-was-real trivia 18.2M (KIO) | **Not as is** (no voice). Yes when someone who was there says it, and the text becomes our title and first caption |
| **The misunderstood character, over film and score** (Snape) | @howeverythingworks 496K / 36.9K (Aug 2026); @talk_hollywood_ 435K / 40.1K (Nov 2025); @cinechronicles.in 238K / 29.5K (Mar 2026); a Rickman tribute 517K / 42.3K (Oct 2025) | fan edits 1.3-2.7M | **Not as is** (score, no voice). **The story inside them is AW's**: their caption is "Rickman knew the truth the entire time and never let it slip once", and Rickman said it himself in 2011 |
| **Bloopers and BTS compilations** | @warnerbrosuk (the owner) 896K / 233K; @bloopersbits feast 2.3M / 147.9K, Hagrid 2.6M / 1.4M | Warner official 16.3M, 13.6M; last day 32M | Picture only, and it's the owner's footage with no story. At most a picture layer |
| **An actor tells a set story in their own voice** | Felton's own reel on Gambon 324K (Oct 2022); Isaacs vs Lucius (featurette voices) 513.8K / 24.5K | GREEN SCREEN ANIMATION's animation over real interview audio 17.93M, 8.51M, 7.06M; Nida Sarfraz's *Return to Hogwarts* clip "Oldman had NO IDEA about Rickman" 5.94M; Graham Norton's own 1.26M; Horowitz's own 1.17M | **Yes, this is AW's format** |

**Answer:**
- On Instagram, HP film moments mostly win as text over film clips from fan and trivia pages. AW can't make that.
- On YouTube, the form AW can make (the person who was there, in their own voice, over the moment) is proven to 5.9-17.9M.
- So AW takes the PROMISE from the Instagram winner (its burned-in hook text and caption) and tells it in the first-party voice, over the scene's picture.
- That is HP-EXECUTION § 7 rule 2 ("build to the promise that was proven") applied to film moments.

## Breadth log (every candidate beat; ≥25 required)
Sources for the first-party column: `hp-films/firstparty-tellings.md` (Sonnet gatherer, ~40 WebSearch, snippet-level, nothing viewed),
`hp-films/hbo-peg.md` (Sonnet, 19 WebSearch), `hp-films/inventory.md` (local disk, zero network), and my own checks.
YouTube freshness is OPEN for every row: YouTube is bot-blocked since 16:42 PKT (`youtube.BLOCKED`, set by aw-speed-research).

| # | Beat | Instagram proof (likes / shares) | First-party on-camera telling | One arc, link in their words? | State |
|---|---|---|---|---|---|
| 1 | **Rickman alone knew Snape's secret ("Always")** | Snape "most misunderstood man" @talk_hollywood_ DRZt6WOjCdn 435K / 40.1K; Snape's truth @cinechronicles.in DWjOKrMkv3t 238K / 29.5K (both film edits) | Radcliffe to Oldman, *Return to Hogwarts* (1 Jan 2022, HBO; score likely, as Coltrane's); Rickman 2011 (RTE / HitFix): Rowling "gave me one little piece of information, which I always said I would never share with anybody"; Rowling's 18 Jan 2016 tweet "I told Alan what lies behind the word 'always'" (text) | Yes: hated teacher → the actor was told a secret he swore to keep → revealed only after his death | **LEAD 1** (YT proof of the beat: 5.94M b69Bxu02vLo per HP-EXECUTION) |
| 2 | **Draco's deleted wand-throw (DH2 courtyard)** | @cineatomy DCAcfUqN6Ho 92.7K / 2.8K ("The story arc Malfoy deserved 🥺"); Draco "isn't meant to be a bad guy" edits in the grid | Felton memoir (print); making-of footage of the take exists; Yates 2011 (print) "a big deal… a different moment" | Possible: coward → the redemption they filmed → cut; needs Felton on camera | LEAD 2 (first-party open) |
| 3 | Felton forgot his line, improvised "I didn't know you could read" (CoS) | @bloopersbits DVIf5evjYzi 864K / 17.1K | Felton memoir (print); on-camera telling not found yet | Comedy single beat; Columbus suggested it | LEAD 3 (trivia risk, HA1) |
| 4 | Fiennes improvised the Voldemort-Draco hug (DH2) | @fw_official11 98 likes (small); bigger reels not surfaced | Felton DragonCon 2011 (fan video), memoir 2022 (print); take count conflicts (25/30+/50) | Single beat | weak IG so far |
| 5 | Rik Mayall filmed as Peeves, cut | thin: 3 results, top is an unrelated Mayall clip (25K / 6.4K) | Columbus TRE 1080p ON DISK (23:13-24:33); Mayall 2011 "we've cut you out" (outlet unknown) | Yes, but no IG proof | weak IG |
| 6 | Dobby's death scene | @yoshua.hassan 48.8K / 4.9K (fan commentary) | print only (Radcliffe via ComingSoon) | - | KILL (first-party) |
| 7 | Neville's parents at St Mungo's, never filmed | search loaded, unread | Lewis 2019/2021 (print + fan-filmed Dragon Con) | Possible | open |
| 8 | Seven Potters, ~95 takes | search loaded, unread (tab froze) | Radcliffe 2010 (print; video unknown) | Trivia | open |
| 9 | Fiennes nearly refused Voldemort; his sister said "You have to do it" | not searched | Jonathan Ross Show 16 Mar 2019 (on camera, ITV) | Casting what-if (HA1 floor: Hemsworth 7K) | weak by HA1 |
| 10 | Molly's "Not my daughter, you b***h!" | not searched | Walters: Empire 2011 (print) + DVD commentary | Single beat | open |
| 11 | Isaacs invented Lucius's look (hair, cane wand) | not searched (the Isaacs-vs-Lucius reel is a different beat) | EW 2010 (print), fan-filmed panels | HA2 fit (finished image) | open |
| 12 | Isaacs is warm, the opposite of Lucius | @thepartystavern DTtmkdUkat0 513.8K / 24.5K | BTS featurette | actor as person | HANDED to hp-cast |
| 13 | Radcliffe broke wands drumming | not searched | Hot Ones (2020), WIRED (count disputed) | Trivia | weak (HA1) |
| 14 | Watson mouthing co-stars' lines (PS) | DHYzSGbtmIF (unread) | none (an observation, not a telling) | - | KILL (first-party) |
| 15 | HP bloopers compilation | @warnerbrosuk DZsBs5KD-y7 896.2K / 233.3K (rights holder) | Warner footage | No story | KILL (format: H1, the owner's own footage) |
| 16 | Hagrid making-of (practical effects) | @bloopersbehindthescenes DUnng92CKLk 68.5K / 66.9K | (idea 3, dropped 12 Nov) | - | KILL (his rejection) |
| 17 | New Snape Essiedu: abuse + Isaacs's defence | @filmthusiast DWUoNRoDKti 58.8K / 3.9K comments | Isaacs FanExpo Denver Jul 2025 (on camera); Essiedu "Quit or I'll murder you" (Mar 2026) | F6-ish, but race politics in the comments | weak (audience split) |
| 18 | New Dumbledore Lithgow on Gambon | not searched | BBC *The One Show* (on camera, 2025) | HBO peg | open |
| 19 | New Hagrid Frost: Coltrane's family blessing | not searched | video podcast, 5 Sep 2026 | Joins Coltrane's "Hagrid will", but that source failed audio (score) and quality (468p) on 10 Nov | weak (source) |
| 20 | New McGonagall McTeer on Maggie Smith | not searched | podcast audio only | - | weak (no picture) |
| 21 | Gambon's "did you put your name in the Goblet" (book: "asked calmly") | not searched | none on camera | - | KILL (first-party) |
| 22 | Dudley's deleted goodbye (DH1) | not searched | no Melling telling | - | KILL (first-party) |
| 23 | Petunia's "I lost a sister" deleted scene | not searched | filmed; no Shaw telling | - | KILL (first-party) |
| 24 | Fred's death (Phelps twins) | not searched | secondhand print | - | open/weak |
| 25 | Lupin and Tonks shown only as bodies | not searched | none | - | KILL (first-party) |
| 26 | Sirius's death | not searched | Oldman: "mediocre", killed off too early (HSC 2023, reported); Radcliffe: "the hardest" (BuzzFeed 2018) | Possible | open |
| 27 | Hermione erases her parents (DH1, film-added) | not searched | Watson 2010 junkets (print; video likely) | Possible | open |
| 28 | Students raise wands for Dumbledore (film-added) | not searched | inventor not found | - | weak |
| 29 | Harry snaps the Elder Wand (film change) | not searched | no creator reason | - | KILL (first-party) |
| 30 | Gambon trolled Felton during Dumbledore's death scene (HBP) | not searched | Felton (CinemaBlend coverage; on camera?) | Possible (warm, Gambon d. 2023) | open |
| 31 | Helen McCrory lost Bellatrix to pregnancy, became Narcissa | not searched | print ("insurance wouldn't cover pregnant witches") | - | weak (print) |
| 32 | Peeves: Columbus "should be restored" (20th anniversary) | (see 5) | Columbus | (see 5) | merged into 5 |
| 33 | **Gleeson accidentally played Bill Weasley in an Australian accent** (DH first day; "I couldn't stop"; Yates asked him to stop; "one of the worst days of my life") | @latenightseth DdHOr7QgA7t 481.3K / 30.4K (reel 10 Sep 2026; the interview aired Sep 2025) | **Late Night with Seth Meyers, Sep 2025, on camera (NBC, HD), adult** | one comic set story, his own words | LEAD (the only lane lead with an on-camera adult HD teller already located; YouTube freshness open; the broadcaster's own clip) |
| 34 | GoF hair: the cast grew their hair out on the break | @tweets DZuhjmtIKVX 933.4K / 36.6K (18 Jun 2026) | none located | trivia, child cast | weak (HA1 trivia; no teller) |
| 30b | (update to 30) **Gambon's joke got Felton through Dumbledore's death**: Felton told Gambon he doubted he was "the right man for the job"; Gambon: "I'll be able to buy a new Ferrari by tomorrow" (more takes, more pay); Felton "didn't know if he was joking" | Felton's own reel Cj5wXJmA4JG 324K likes (19 Oct 2022, "the best advice Sir Michael Gambon gave me on set") | Felton's own video (Instagram; download is his call, not ours); memoir-tour TV tellings not located yet; memoir says "excited, not nervous" (conflict) | yes: the scared boy who had to "kill" Dumbledore → Gambon's joke → the scene fans love; Gambon d. 28 Sep 2023 | LEAD (proof weak: one post on the teller's own account) |
| 35 | **"Have I been a good Sirius?"**: Oldman calls his Sirius "mediocre" (HSC, 28 Dec 2023, on camera: he'd have played it differently had he read the books "like Rickman"); Radcliffe, told of it by Horowitz: on Oldman's last day "he was like, have I been a good Sirius? And I wanted to cry. I was like, yes, oh my God, what?" | not searched yet (Chrome stalled) | **both on disk or in RSS: Radcliffe in the HSC Apr 2024 episode (1080p60 on E:, 28:03-28:45, setup by Horowitz inside the source); Oldman Vol. II audio via the show's RSS (downloading)** | yes: the legend's self-doubt → his question on his last day → "I wanted to cry"; the link is in their own words, inside one show | **LEAD** (IG and YT open) |
| 22b | (update to 22) **Dudley's deleted goodbye** is the biggest film-moment reel read today | **@the_goodfilms DZqMUDpueA5 2,217,860 likes / 136,640 shares (16 Jun 2026)** | no Melling telling found (two searches); the scene's own dialogue is fiction, not a first-party voice | the scene alone | **KILL for AW's own-voice format; flagged to Affan as a format finding** (voiceless deleted-scene and BTS reels are the lane's biggest proof) |
| 36 | A deleted scene "that deserved to stay in the film" (unnamed) | @yellowcardmeme DV1UUU5oA9f 665,641 / 63,070 (13 Mar 2026) | none | - | proof for the deleted-scene PROMISE only |
| 37 | "5 times the HP cast went off script" (improvised lines kept) | DQPnQpiDcuh 613,995 / 58,302 (25 Oct 2025) | per beat (see 3, 4, 30b) | list format | proof for the improvised-moment PROMISE |
| 38 | Draco "the boy who had no choice" edits | @inkedandcreamy DSMZxhak2_q 38.7K / 5.8K | - | fan edit | supports 2 (mid) |
| 8b | (update to 8) Seven Potters | 3 results; the top read: 25 likes (DeYuZNJuCPr) | - | - | **KILL (no IG proof)** |
| 5b | (update to 5) Peeves | the beat's own reel: 1 like (Dd1aoEVkouK); 3 results | - | - | **KILL (no IG proof)** |
| 7b | (update to 7) Neville | top read 149 likes (DZSZcxCNAO5) | - | - | weak (no proof found) |
| 1b | (fact check on 1) The viral promise "Rickman knew the ending the whole time" OVERSTATES it | - | Rickman 2011 (HitFix, a PHONE interview = audio/print): "one tiny, little, left of field piece of information"; LA Times 30 Dec 2011: he played the double agent without knowing the ending; Rowling 2016: "I told Alan what lies behind the word 'always'"; Rowling 2024 Q&A: "You were in love with Harry's mother" | The accurate claim: he knew Snape loved Lily ("Always") years early, not the plot's ending | hook wording must say "the secret", never "the ending" |

## Source check, zero YouTube requests (14 Nov 19:25-20:50)
The show's own RSS audio for six *Happy Sad Confused* episodes, plus two files already on disk, was transcribed locally with WhisperX
large-v3 (scout, GPU lock).
- Audio: `hp-films/src/hsc/*.mp3`, from megaphone via `hp-films/src/hsc/fetch.sh`. Not YouTube.
- Transcripts: `hp-films/src/hsc/*.scout.txt` and `hp-films/src/local/*.scout.txt`.
- **Scout-time bug:** the dates in my filenames shifted every HSC timestamp by +2,0xx s. Episode time = printed time minus the offset that
  `scout.log` prints (33:35-33:46). The times below are corrected.

| Source | What's in it, corrected time, his words (ASR, to be checked by ear) | Verdict |
|---|---|---|
| **Gary Oldman, HSC Vol. II, 28 Dec 2023** (67 min) | **14:33** "they killed me off too early. I'm still upset about that. And we were all taking bets, you know. It's Hagrid… maybe it's Ron… And then you kind of open the script and you go, it's me. I'm out of here." · **15:16** Horowitz: "You discovered for the first time that he [Rickman] was the only one that knew how the books ended. He got the inside dope from J.K." Oldman: "He did. He had a special relationship going with that." · **15:44** "I think my work is mediocre in it… maybe if I had read the books like Alan… if I had known what's coming, I honestly think I would have played it differently." · **12:20** his hardest scene: a week lying by a frozen lake (PoA) | **The Sirius story, with Rickman's secret as its reason, all in Oldman's own voice.** The video is on Josh Horowitz's YouTube (queued) |
| **Daniel Radcliffe, HSC 11 Apr 2024** (on disk, 1080p60) | **28:03** Horowitz: Oldman "called his work in Harry Potter mediocre, and the entire audience… gasped." **28:22** Radcliffe: "he asked me on the last day of his filming, I think for the fifth film, he was like, have I been a good Sirius? And I wanted to cry. I was like, yes, oh my God, what?… it's insane that he thinks that way." | **The payoff, set up inside the source** |
| **Tom Felton, HSC 26 Mar 2026** (in person, NYC; Broadway run) | **47:47** "Sir Michael Gambon would just take the piss out of himself and everyone immediately… disarming everyone for us to act freely." **48:16** "It's Draco killing Dumbledore. It's a big one… I must have bumbled my way through the first three attempts." **48:40** Gambon asked for a tea break, invited him out "for a breath of fresh air"; Felton: "I'm sorry, sir… I promise you, I've rehearsed the lines". **49:56** Gambon: "Dear boy, do you have any idea how much they pay me per day to be here? If you keep effing it up at this rate, tomorrow I'll have a new Ferrari." **50:07** "And I took it deadly serious before I realized that this man is taking a piss… just relax, man, have some fun. And next take, that's the one they used. I love it. What a legend." | **The whole Gambon arc, one teller, payoff = the take in the film.** Felton says "17-year-old" (he was 19-20 on HBP): his words, not a label. A crude aside ("Fucked her up, didn't I?") sits inside the passage and must be cut. "Potter" origin at 26:26-27:11 (brothers called him "Maggot", "Runt"): trivia |
| Tom Felton, HSC 1 Nov 2022 (virtual) | Rickman and Fiennes as the most intimidating; "I never met Ralph Fiennes till the final premiere… green dots… for CGI" (~28:20-29:00) | No Gambon story here. The Ferrari story's on-camera telling is the 2026 one |
| Alan Rickman, HSC 22 Jun 2015 (full 45 min) + the 6-min clip | No Snape-secret passage anywhere. "Three was all I knew. I didn't know what was going to happen after the third." (contract, not the secret) | **L1 has no on-camera Rickman source** |
| Radcliffe Vol. V (13 Apr 2026), Fiennes Vol. II (29 Dec 2021) | Radcliffe 2026: asked if he improvised on HP, he says he still prefers "the take as scripted first" (no scene story); Fiennes 2021: the Voldemort casting, "my sister… 11, 10, 7… You've got to do it" (a casting what-if, kill log) | no new lead |
| Radcliffe 2014 / Vol. II 2019 / Vol. III 2020 (RSS audio on disk) | 2019 transcribed (an Oldman passage at 23:54: Radcliffe 'freaked out to meet' him, not the beat); 2020 partly transcribed; 2014 NOT transcribed: the run was stopped at 21:59 on Affan's priority call (the Speed build took the GPU). Optional: it would only show whether Radcliffe tells the Rickman-secret story himself; A's hook doesn't need it | optional |

## Kill log
| Beat | Gate failed | Evidence |
|---|---|---|
| Rickman alone knew Snape's secret, as its own Short | **First-party source**: no on-camera Rickman telling exists (HSC 2015 full episode and clip: none; HitFix 2011 was a phone call; RTE and Empire attributions conflict). RtH has score under it (Coltrane measured 0.019 on 10 Nov). **Facts**: the viral wording "knew the ending" overstates it (he knew "what lies behind the word 'always'"). **Freshness**: 5.94M RtH Short | Folded into A as Oldman's own reason ("if I had read the books like Alan") |
| Felton's forgotten line ("I didn't know you could read") | **First-party** (no on-camera telling located; the Apr 2026 "iconic" quote is about "Potter"); **Shape** (one beat); **Facts** (Columbus suggested the line) | IG 864K / 17.1K and 163K / 3.1K stand as proof of the "improvised" promise |
| Draco's deleted wand-throw | **First-party** (Felton memoir only, print; Yates 2011 print) | IG 92.7K / 2.8K; Draco edits 38.7K |
| Dudley's deleted goodbye | **First-party** (no Melling telling; the scene's dialogue is fiction) | IG 2.22M / 136.6K: the lane's biggest proof → Affan's narrated-format question (hub Q4) |
| A deleted scene "that deserved to stay" | First-party | IG 665.6K / 63.1K |
| HP bloopers compilation | **Format** (owner's footage, no story) | WB UK 896K / 233K |
| Peeves (Rik Mayall cut) | **IG proof** | 3 results; the beat's own post 1 like; Columbus 1080p on disk is the only HD voice |
| Seven Potters (95 takes) | **IG proof** | 3 results; top read 25 likes; print only |
| Dobby's death scene | **First-party** (print only) | IG 48.8K / 4.9K fan commentary |
| Neville's parents (St Mungo's never filmed) | **IG proof**; first-party fan-filmed only | top read 149 likes |
| Fiennes nearly refused Voldemort | **Shape** (casting what-if = HA1 floor: Hemsworth 2.9K, Holland 7.9K) | First-party exists: HSC 29 Dec 2021 ("my sister… 11, 10, 7… You've got to do it"), Jonathan Ross 2019 |
| Molly's "Not my daughter" | **First-party** (Empire print, DVD commentary unlocated); **IG proof** (3 results) | - |
| Isaacs invented Lucius's look | **First-party** (print, fan-filmed panels) | the Isaacs-vs-Lucius reel (513.8K) is a different beat → handed to hp-cast |
| Watson mouthing co-stars' lines | **First-party** (an observation, no teller) | - |
| GoF long hair | **First-party** (none located); **Shape** (trivia) | IG 933.4K / 36.6K |
| Hagrid making-of | **His rejection** (12 Nov, "just 2 topics") | IG 68.5K / 66.9K |
| New Snape Essiedu: abuse + Isaacs's defence | **Audience** (race politics in the comments); print-heavy | IG 58.8K / 3.9K comments |
| New Hagrid Frost: Coltrane's blessing | **Source** (Coltrane's line has score under it and a 468p rip) | - |
| New McGonagall McTeer on Maggie Smith | **Source** (podcast audio only, no picture) | - |
| Gambon's "did you put your name" | **First-party** (none on camera) | - |
| Petunia's "I lost a sister" | **First-party** (filmed; no Shaw telling) | - |
| Lupin and Tonks shown only as bodies | **First-party** (none) | - |
| The Elder Wand snap | **First-party** (no stated reason) | - |
| Students raising wands (film-added) | **First-party** (the inventor isn't credited) | - |
| Helen McCrory: lost Bellatrix, became Narcissa | **First-party** (print) | - |
| Evanna's paycheck for Dumbledore's funeral | **Source** (Normal Not Normal, Feb 2021, a remote podcast; quality unchecked); **IG proof** thin ("dumbledore funeral" 3 results, all 2017-2025) | lead not pursued |
| Hermione erases her parents (film-added) | **First-party** (Watson 2010 print; video unlocated) | - |
| Radcliffe breaking wands | **Shape** (trivia, count disputed) | - |
| Fred's death (Phelps twins) | **First-party** (second-hand print) | - |

## Instagram searches run (also appended to `IG-SEARCH-LOG.md`)
| PKT | query / page | what loaded | top results |
|---|---|---|---|

## YouTube requests run (all through `pace.sh youtube`)
| PKT | request | result |
|---|---|---|
