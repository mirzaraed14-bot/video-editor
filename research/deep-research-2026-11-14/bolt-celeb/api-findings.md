# bolt-celeb: the YouTube Data API pass (Sat 14 Nov 2026, 21:40-22:05 PKT; §§ 9-10 added 23:20; corrected after the final cold read and the advisor, clock checked 23:43)

Run through `yt_api.py bolt-celeb` only (README ▶ THE YOUTUBE DATA API). **666 units in all.** By 22:05 it was 462: 3 searches (300) and 162 one-unit
calls (videos, playlistItems, channels); 40 more calls came from the cache, free. Raw JSON is in `work/api/`. Nothing was
downloaded, no youtube.com page was opened, no comments were fetched before § 10. §§ 9-10 then added 2 searches and 4 one-unit calls (3 `videos`, 1 `commentThreads`), 204 units. "x avg" below = views ÷ the channel's lifetime average per
video (lifetime views ÷ video count). Hits skew that average upward, so the multiples are conservative.

## 1. Bolt Motivation: all 803 uploads (`UCy2vByAZhHucf8wV1Lr8hKw`, 3.13M subs; `work/api/bolt_uploads.json`)
- **Median 2.02M per upload.** 2026: 292 uploads, median 1.67M. The latest 60 (17 Oct-13 Nov): median 663K.
- 182 uploads name a famous person (title, description or tags; a crude name list): median 2.0M, the same as the rest (2.02M).
- **The name in the title, re-tested on the full list:** all-time, no difference (named title median 2.0M, n 107; name only in
  the description or tags 1.94M, n 75). **2026 only:** named titles 698K (n 29), hidden names 1.87M (n 32). So hiding the
  name is a 2026 effect, not a rule of his catalogue. This corrects `bolt-shares.md` point 1, which rested on 9 Shorts.
- **No MJ and no Bieber Short in 803 uploads.**
- **His music-star Shorts split by shape:**
  - The star stops for someone at a show: "Adele Stopped Her Show For Him" 15.9M (`GnB-3kHQRVo`, Feb 2026); "Lewis Capaldi
    Finally Finished The Song" 2.99M (Jan 2026); "Billie Eilish & Finneas" 4.2M.
  - The star beats the critics: "She Risked Her Life For One Last Song" (Celine Dion) 387K (Nov 2025); "Billie Eilish
    SILENCED The Entire Internet" 302K (Jan 2026); Drake 200K.
- **The Alzheimer's shape works for him on ordinary people:** "He Forgot Everything But Her…" (a couple married 60 years, 8 Mar
  2026, 57 s) 2.96M.
- The 12 Nov figures have moved: the NFL legend Short is now 10.28M (`W3q6bLmMzIU`).

## 2. Peers: every upload, exact
| Channel | Subs | Uploads | Shorts median, all (uploads of 180 s or less) | Shorts median, last 6 months (180 s or less; n) | Best Shorts |
|---|---|---|---|---|---|
| MrWood (narrated celebrity "hidden stories") | 154K | 821 | 11.5K | **6.0K** (97) | Stallone's wife 13.1M; 9.8M; 8.4M |
| MJ Forever (narrated MJ facts and listicles) | 335K | 568 (264 Shorts) | 76.6K | **46.5K** (22) | "How Drug Lord Helped Michael Jackson Shoot His Music Video" 29.9M (Feb 2024); "How Michael Jackson wrote Billie Jean" 3.46M (Mar 2026) |
| the detail. (MJ documentaries; Shorts are people's own words) | 791K | 693 (328 Shorts) | 36.7K | **39.2K** (26) | Culkin 8.2M; "16 years ago we lost a King" 8.0M; 2026: father's control 1.4M, no contact with family 1.0M, "Real Story Behind… Billie Jean Motown 25" 789K |
| Michael Jackson Shorts | 33.1K | 62 | 9.6K | 3.9K (36) | Moonwalk 6.6M (2021) |

Narrated MJ and celebrity Shorts are hit-driven: the typical one lands at 6-47K, with rare multi-million outliers. This replaces
the unconfirmed "the detail.'s narrated Shorts top out at 15-66K" (its last-6-months Shorts median is 39.2K).

## 3. AW's own base, exact (`UCbLhNRQjyvNTqluyjKiJ8jw`, 542K subs, 282 uploads; `work/api/aw_uploads.json`)
- **Since 2 Oct:**
  - MJ Shorts (60 s or less): median ~119K, 6 of 17 at 150K+ (to 14 Nov). Without the two newest (1-2 days old): median ~125K, 6 of 15.
  - Non-MJ celebrity Shorts outside bodybuilding (Kanye, Ninja, Elon, Harry Kane, Patrick Stewart, Diana, Owen Hart, Bieber, Snape): none of 9 reached 150K. They landed at 12.5-35.1K, median 22K. Bieber's "Painful Upbringing"
    (9 Nov) is 27.2K.
  - Bodybuilding, the exception: Nick Walker's Parents 166.5K (4 Oct), Fitzwater 103.8K, Levrone 49.6K, CBum 46.6K,
    Lunsford 16.8K.
  - All 11 AW MJ Shorts of August-September, split by register (a confound for the police-and-MJ reading in § 10):
    - tabloid-claim: Drug Addiction REVEALED 10.8K, Dead Body DECOY 9.8K, Lisa Marie FAKE? 17.7K; the police Short (11.9K) sits
      with them;
    - family and wound: BANNED His Own Birthdays 6.02M, Kids Didn't Know Their MOM 628K, Daughter Had NO Idea 566K, Son
      SURPRISED Jaafar 283K, AFRAID Of 176K, DISRESPECTFUL Interview 87K, FORCED To Mask His Kids 77K.
    A rumour title can still win as a wound: "This Rumor BROKE Michael Jackson" did 6.63M (22 Jun).
- **March to September 2026, non-MJ Shorts did clear 150K:**
  - KSI 1.69M (Jun); Winnie Harlow 1.17M (Aug); Messi vs Ronaldo 439K; Stan Lee 380K and 159K; Speed 368K; Biggie/Tupac 230K.
  - "Hollywood BROKE Justin Bieber" 170K (30 May).
  - Monthly non-MJ medians ran 33-95K.
  - So the 12-35K band is the last six weeks, not a permanent ceiling. It is still the current state.
- **All-time:**
  - MJ Shorts (60 s or less): median 168K, 34 of 67 at 150K+. Counting MJ uploads of any length: 143K, 34 of 70.
  - AW's MJ hits are MJ-wronged or family stories, in his own voice, from archive: "Biggest Misunderstanding" 10.4M, "This
    Rumor BROKE Michael Jackson" 6.6M, "BANNED His Own Birthdays" 6.0M, "Police HUMILIATED Poor Michael Jackson" 5.85M, "On His
    CRUEL Father" 5.2M, "MTV Humiliated Michael Jackson To Tears" 1.47M.
- **Repeat check:** AW has no Short on the favela shoot (titles, descriptions and tags searched).

## 4. Card 2 (card 1 before 23:30), Tony Bennett × Lady Gaga, on YouTube Shorts (search 1: "tony bennett lady gaga", short, by views)
Retellings of 90 s or less (the API's "short" means under 4 minutes, so music videos were dropped). Subscriber counts are from
`work/api/s1_channels.json`.

| Id | Channel (subs) | Date | Length | Views | x avg | Angle (title) |
|---|---|---|---|---|---|---|
| `oq6YaA6oia4` | Gaga Shorts (498K) | 13 Jul 2022 | 26 s | **26.9M** | 65x | "This moment was so moving" |
| `VzFltxDWuxk` | 도플리 dobby playlist (118K) | 4 Jan 2025 | 51 s | **9.69M** | 19x | "the amazing stage he gave while suffering severe dementia" (Korean) |
| `XT5z0Ms7KZA` | Gaga Daily (431K) | 14 Jul 2022 | 29 s | 9.58M | 3x | "When Lady Gaga met Tony Bennett" (angle unclear) |
| `rT8Cr7AvH1U` | Billboard Nigeria (159K) | **23 May 2026** | 52 s | **6.95M** | **105x** | "At 95 and battling Alzheimer's, Tony Bennett sang every word…" |
| `n_-mxFGKuwQ` | Golden Arrival (24.4K) | **28 Oct 2025** | 6 s | **4.80M** | **137x** | "Tony Bennett Remembered Lady Gaga One Last Time" |
| `AbRMj5EqXqc` | 音のひとくち (97.9K) | 28 Jun 2026 | 54 s | 2.93M | 1.2x | "the brightest memory dementia couldn't stop" (Japanese) |
| `dqmAtDfFNqw` | 재즈기자 Jazz Editor (405K) | 5 May 2022 | 60 s | 2.44M | 12x | "the singer leaving the last stage of his 95 years" (Korean) |
| `WSTscZ6nZSU` | Gaga Shorts (498K) | 26 Aug 2024 | 59 s | 1.71M | 4x | "Lady Gaga talking about Tony Bennett" |
| `eBzTzOh6Ufg` | Gaga Shorts (498K) | 9 Feb 2023 | 58 s | 1.02M | 2.4x | "Lady Gaga moved by Tony Bennett!" |
| `fjmKI7EppXY` | Oro Hits (87.6K) | 13 Mar 2025 | 27 s | 914K | 28x | "beautiful moments" (Spanish) |
| `ujm5_p5KrDE` | ArchiveHeist (36.1K) | 12 Jul 2026 | 17 s | 738K | 1.6x | "HE REMEMEBERED LADY GAGA" |
| `Il3qkw-A3lo` | Noemi Cermenati (183) | 7 Oct 2021 | 82 s | 401K | 13x | the 60 Minutes re-upload (card 1's source) |
| `O9wCXecWM2g` | Vinylfiles (42.5K) | 31 Jul 2026 | 8 s | 261K | 0.24x | "He Remembered Her" |
| `KomPn6CVx7k` | Moments That Matter (23.2K) | 6 Jun 2026 | 6 s | 15K | 0.13x | "Forgot Her Name but Recognized Her" |

**Reading:**
- A repeat winner across languages and years. In 2025-26, two small channels (24K and 159K subs) did 4.8M and 6.95M with it,
  at 137x and 105x their averages.
- Two mid-2026 clip reposts (6-8 s, no story) did 15K and 261K, below their channels' averages.
- **The 6.95M (Billboard Nigeria, 23 May 2026) carries the same caption text as the @femalequotient Instagram reel (21 May
  2026, 1.7M likes / 61K shares):** "Even when memory fades, music has a way of finding its way back in", plus the Northwestern
  Medicine line. One telling won on both platforms in the same week.
- No retelling's audio or picture was checked (no downloads), so whether any already ends on "my friend saw me" is still open.

Official 60 Minutes uploads (`work/api/card1_ids.json`):
- `cIMuacCUgGY`, "Anderson Cooper on witnessing Tony Bennett's final act in 2021": 21 Jul 2023, 3:27, HD, 198K.
- `BGl37mA0v-8`, the rehearsal promo: 39 s, HD, 70.5K.
- `ZACgW7hltyw`, "Lady Gaga on when a loved one has Alzheimer's": 1:52, HD, 343K.

## 5. C01 Thriller (search 2: "john landis thriller jehovah's witness destroy", by relevance)
- In 2026, at least seven Shorts tell "he tried to destroy Thriller": 33.4K (`lNJjgLKGgJs`, Oct), 29.6K (`CfO0Qe1ds4M`, Aug),
  27.2K (Japanese, Nov), 8.6K (Spanish), 73, 34 and 11 views. **Ceiling ~33K.**
- No John Landis on camera surfaced in the top 50.
- **Verdict: the KILL stands, now with numbers.**

## 6. C14 They Don't Care About Us, the favela shoot (search 3: "michael jackson favela", short, by views)
| Id | Channel | Date | Length | Views | Title or angle |
|---|---|---|---|---|---|
| `Uv08NEFnBnY` | Zunorama | 4 Sep 2025 | 10 s | **40.1M** | "Michael Jackson Got Unexpected Protection In Brazil While Making A Music Video" |
| `M-PosTnbqK8` | MJ Forever (335K) | 13 Feb 2024 | 51 s | **29.9M** | "How Drug Lord Helped Michael Jackson Shoot His Music Video" |
| `XoJ72JcB1jY` | Бизнес Люди (Russian) | **6 Jun 2026** | 78 s | **18.5M** | "the police refused to protect him, but Michael Jackson still went to the most dangerous place in Brazil" |
| `QlEU76xhpKI` | Buaya darat8 (Indonesian) | **10 Feb 2026** | 7 s | **11.9M** | "Brazil's government banned it, but this MJ video was still shot in the favela" |
| `avuHwo59U64` | MAR Channel (Indonesian) | 12 Dec 2024 | 58 s | 9.1M | "the story of MJ shooting in the most dangerous place in the world" |
| `PdYGxyEh1KQ` | Andy Jiang | 22 Mar 2024 | 59 s | 6.4M | "They Filmed This on a DRUG Lord's Territory" |
| `R738rFzNByA` | Absurd daily (Indonesian) | 1 Sep 2025 | 54 s | 6.3M | "when the police wouldn't secure it, the cartel was ready to back it" |
| `RC-Y9T5rll4` | HE Xperience (Spanish) | 23 Mar 2024 | 57 s | 4.25M | "the drug trafficker who helped MJ record his music video" |

Also in the results: `0q-Qe6E3wRo` "NUNCA FAÇA NA FAVELA DO SANTA MARTA" (17.6M, Nov 2025). Its topic isn't confirmed, so it isn't
counted.

**Reading:**
- Eight confirmed retellings at 4.25M-40.1M, from Feb 2024 to Jun 2026, in English, Russian, Indonesian and Spanish.
- The English ones date from 2024 to Sep 2025. No 2026 English retelling made the top 50, where the lowest entry is 3.9M.
- Official sources:
  - "They Don't Care About Us (2020)" (`PoEa9bzeTu0`, Michael Jackson channel, 7:18, flagged HD, 36.6M). Whether it is a new
    film transfer or an upscale is unknown until the file is checked.
  - The Brazil version (`QNJL6nfu__Q`) is SD (1.46B).
- The story's facts were not checked here (see the report's card).

## 7. Official MJ footage and its HD flags (`work/api/mj_official_inventory.txt`; michaeljacksonVEVO 138 + Michael Jackson 159 items)
- **Native 4K:** Thriller (`sOnqjkJTMaA`), Beat It (`oRdxUFDoQe0`), and the Beat It 4K Short (`SrtYzwQbkyk`).
- **Official "Upscaled" HD:** Remember the Time, Don't Stop 'Til You Get Enough, Rock With You, Give In To Me, Will You Be
  There, Who Is It, In the Closet, Jam, She's Out of My Life, Black or White (full).
- **HD, origin unknown:** They Don't Care About Us (2020); Human Nature (Apr 2026).
- **SD on the official channels:**
  - Videos: Billie Jean, Smooth Criminal, Bad, They Don't Care About Us (Brazil and Prison versions), Earth Song, Scream, Man In
    The Mirror, Dirty Diana, You Are Not Alone, Black or White (shortened), Ghosts.
  - Concerts: Live in Bucharest, Live at Wembley 1988.
  - Also the This Is It music video.

## 8. Instagram, to close B (one Reels grid, per the hub at 21:37)
- @fboy Reels tab: 25 tiles, 367K-9.1M, median ~1.5M.
- A repeat load of @boltmotivation was my error: it is the empty account already logged at 17:35.
- Both are logged in `IG-SEARCH-LOG.md`.

## 9. C14's own voice (search 4: "Michael Jackson Santa Marta", 4-20 min, HD only; `work/api/s4_santa_marta_medium.json`)
The length and HD filters keep the Shorts retellings out, so the features, talks and local reports come through. All 50
results are flagged HD.
- **Long-form retellings run from 2021 through 2026:**
  - Meteoro Brasil, "QUANDO O COMANDO VERMELHO PROTEGEU MICHAEL JACKSON" (`bdgDMk-UFfs`, 13:29, 409K, Feb 2021);
  - Jackson Diary (`-jayO_EsPPA`, 15:29, 207K, Oct 2024, Spanish);
  - Understanding Michael Jackson (`Si4lGKZ7hqw`, 9:42, 104K, Oct 2022);
  - Flipper (`tUcdj88ud7Q`, 12:04, 88K, Apr 2026, Spanish);
  - English pieces from 2026 at 1-8K: `ulKaWYGNstw` (Feb), `YCFd4FfJ7FA` (May), `OM6hS30zi7w` (Sep).
- **Own voices found (none verified; nothing downloaded):**
  - Residents, in Portuguese, HD: "Memórias da visita de Michael Jackson ao Santa Marta" (`3xZrGNx3HaE`, 10:27, 56.9K,
    26 Jun 2019), a video report by a PUC-Rio journalism class. Also "Rolé em Santa Marta" (`XsiatLdH55E`, 9:57, 810 views,
    Nov 2016), whose description says "we talked with residents".
  - Salvador, not Santa Marta: Jornal Nacional's special on the people who took part in the Salvador shoot (`R5IaR8JfhLA`,
    4:06). It's a 2025 re-upload of Globo; the original date is unknown.
- **Facts the descriptions give (retellings, not primary sources):**
  - Rio's tourism secretariat tried to stop the shoot in Santa Marta and failed; without the authorities' support, the
    Comando Vermelho protected him (Meteoro Brasil).
  - A judge tried to ban the shoot; the statue was later vandalised (`7RZjJja9Tlw`, Jun 2026).

## 10. Spike Lee (search 5: "Spike Lee Michael Jackson Brazil", any length; `work/api/s5_spike_lee_mj.json`)
Follow-up calls:
- `videos` on both parts of his talk (`s4_spike_parts.json`);
- one `commentThreads` on Part 1, to check what the talk covers (`s4_spike_comments.json`).

Findings:
- **His own account, flagged HD, unverified:** his keynote at Rio Innovation Week (Nov 2022), filmed by a travel-vlog
  channel, the Brazil Show.
  - Part 1: `TXV8VXXnnN4`, 14:04, 981 views, 18 Nov 2022, "Michael Jackson in Brazil – The Untold Story (Spike Lee's Vision)".
  - Part 2: `BHYmFzijQHI`, 15:24, 406 views, "Behind the Scenes in Bahia".
  - A comment under Part 1 says the talk covers "working with Michael Jackson the video The[y] Don't Really Care About Us".
  - Unknown until downloaded: whether he tells the Santa Marta permission story, and how the picture and the sound hold up.
- **1996 voices, SD-origin:**
  - the MTV making-of (`n4z0YSPhnUk`, 13:33, SD, 445K, a 2010 fan upload);
  - AP Archive, "BRAZIL: MICHAEL JACKSON IN DONA MARTA SLUM FILMING NEW VIDEO" (`bxLEcM-4Hi4`, 2:59, SD, 310K).
- **Other Spike Lee interviews on MJ, none checked for the favela story:** CBS 2009 (`POjJrOooh1Q`, 23:39, SD, 200K);
  Venice 2012, Bad 25 (`3QX7apebWaE`, 13:50, HD, 75K); The Hollywood Reporter 2016 (`eQpGCEklXpM`, HD, 22.9K); CBS Mornings
  2016 (`SlvcVlZDgUU`, HD).
- **A different MJ beat surfaced: "Spike Lee reveals MJ's real voice"** (logged as C42).
  - Shorts: `2Qqi9p-DkN0` 3.90M (Jul 2025, Spanish), `mvebwGEFF6E` 2.20M (Aug 2024), `094P2w_WsdA` 1.46M (Jun 2025),
    `4BySr8glNe0` 348K (Apr 2025).
  - Spike Lee is on camera in HD, e.g. Boardroom, `iySHEsc_Emg`, 32K, May 2025.
- **Numbers refreshed:** the official 2020 video `PoEa9bzeTu0` 36.55M; the Brazil version `QNJL6nfu__Q` 1.46B (SD).
- **AW's own police-and-MJ Shorts** (`aw_uploads.json`; both are the arrest-and-search lane by their tags):
  - "Police HUMILIATED Poor Michael Jackson": 5.85M (28 May 2026);
  - "The Police Did THIS To Michael Jackson": 11.9K (24 Sep 2026), 0.2 % of the first.

**Units:** five searches and 166 one-unit calls in total, 666 units. All callers: 42 of 95 searches by the log at 23:43.
