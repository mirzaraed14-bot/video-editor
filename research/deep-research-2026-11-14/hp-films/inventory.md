# HP films: local inventory (2026-11-14)

Gatherer: local disk only, zero network, nothing played (ffprobe and file reads only). Probe: `ffprobe -v error -show_entries stream=codec_type,width,height,r_frame_rate:format=duration,bit_rate -of compact`.
Paths: `E:` drive files shown with their E: path; project files shortened to `projects/<job>/...` under `X:\Claude Projects\video-editor-client\video-editor\`.

Caveats:
- "Who is on camera" is inferred from filenames, transcripts and info.json. Nothing was watched and no diarization was run.
- `*.scout.txt` timestamps are relative to the scouted window. The HSC window starts at 30:00 of the episode, so absolute = relative + 30:00. Proof: `projects/harry-potter-prank/RUN.md` says `raw/hsc_dan.mp4` is 2183-2223 s of the E: file and `hsc_2070` has offset 2070 s, and the Rickman tape (rel 0:05:06) lands at 35:06. The Columbus transcripts (`tre_*`) are already absolute.

## 1. Media files

The keyword sweep of E: and X: (depth <= 5, skipping node_modules, .git, Windows, caches) found only the files below outside the HP project folders. There is no Return to Hogwarts file, and no Dobby, Hallows, Goblet or Phoenix material anywhere.

### 1a. Outside the project folders
| path | res | fps | dur (s) | kbps | what it is |
|---|---|---|---|---|---|
| E:\Bullshit Folder\Henry\Daniel Radcliffe, Jonathan Groff, _ Lindsay Mendez talk MERRILY WE ROLL ALONG I Happy Sad Confused.mp4 | 1920x1080 | 59.94 | 3347.9 | 2475 | HSC podcast, Radcliffe on camera |
| E:\Bullshit Folder\Henry\Alan Rickman Takes Jimmy to Task for His Impersonation.mp4 | 1920x1080 | 29.97 | 137.9 | 1700 | Fallon, Rickman banter (no film story) |
| E:\Bullshit Folder\Henry\Harry Potter Behind The Scenes- The Making of Hagrid.mp4 | 1920x1080 | 23.976 | 487.0 | 3456 | Collider BTS "Making of Hagrid" (same file as idea3 src/making) |
| E:\Bullshit Folder\Henry\Prank on Harry Potter.mp4 | 854x480 | 25 | 76.8 | 459 | Radcliffe's sleeping-bag fart-machine prank (480p) |
| E:\Bullshit Folder\Henry\Prisoner of Azkaban - Page 394, Severus Snape (HQ).mp4 | 1920x1080 | 29.97 | 152.0 | 1104 | Snape scene clip |
| E:\Bullshit Folder\Henry\Severus Snape scene pack 4K.mp4 | 1920x800 | 23.976 | 2657.6 | 971 | Snape scenes, 2.4:1 crop (not real 4K) |
| E:\Bullshit Folder\Henry\Wizard Duel_ Severus Snape vs Gilderoy Lockhart _ Harry Potter and the Chamber of Secrets.mp4 | 1920x1080 | 23.976 | 132.2 | 1502 | Chamber of Secrets duel scene |
| E:\Bullshit Folder\Henry\ALL Severus Snape Scenes [1080p+Logoless] (NO BG Music).mp4 | 1920x1080 | 29.97 | 26.0 | 4203 | only 26 s despite the title |
| E:\Bullshit Folder\Henry\Secrets Revealed! Hagrid - HARRY POTTER WIZARD'S COLLECTION BONUS DISC.mp4 | 480x270 | 29.97 | 78.7 | 437 | Hagrid bonus-disc BTS (480p) |
| E:\Bullshit Folder\Canelo\Harry Potter and the Half-Blood Prince  Dumbledore's Farewell - Soundtrack Extended.mp3 | audio | | | | score only |
| E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\Harry Potter Thought Snape HATED Him.mov (copy in X:\Claude Projects\Exports\) | 1080x1920 | 30 | 43.9 | 46396 | our finished Short (Radcliffe on Rickman) |

Keyword hits that are not Harry Potter, ignore: Henry\Prince Jackson x2, Henry\je te laisserai des mots (Patrick Watson), Drake\Prince Harry x4, Michael Jackson Jaafar featurette, Telegram and Shorts mp3s (prince, PRINCE OF DARKNESS).

### 1b. Project folders, source media only
Renders, proofs, topaz chunks and bake files are omitted (they sit in `renders/`, `proof/`, `work/`, `outputs/`).

| path | res | fps | dur (s) | kbps |
|---|---|---|---|---|
| projects/harry-potter-niche/src/coltrane/pudHrUqy2I0.mp4 | 854x468 | 26 | 37.9 | 339 |
| projects/harry-potter-niche/src/lastday/DknJ6__GcTM.mp4 | 640x480 | 25 | 81.7 | 673 |
| projects/harry-potter-niche/src/lastday/FfCsVPJsw-E.mp4 | 1280x720 | 23.976 | 316.1 | 600 |
| projects/harry-potter-niche/src/lastday/Tb7GKZGmIRE.mp4 | 1920x1080 | 23.976 | 183.3 | 2176 |
| projects/harry-potter-niche/src/newboy/jo9Pcia-YuQ.mp4 | 1920x1080 | 30 | 44.4 | 2099 |
| projects/harry-potter-prank/raw/dvd_0.mp4 | 320x180 | 25 | 76.8 | 78 |
| projects/harry-potter-prank/raw/hsc_2070.mp4 | 320x180 (black) | 25 | 170.0 | 73 |
| projects/harry-potter-prank/raw/hsc_dan.mp4 | 1920x1080 | 59.94 | 40.0 | 12584 |
| projects/harry-potter-prank/src/rickman/tgXZefAYRnQ.mp4 (+ same-named long copy) | 1920x1080 | 23.976 | 375.1 | 727 |
| projects/harry-potter-prank/_rk/raw/rickman.mp4 | 1920x1080 | 23.976 | 375.1 | 727 |
| projects/harry-potter-prank/src/snape/ (4 files, same as 1a Snape files) | 1080p / 1920x800 | 24-30 | 26-2658 | 971-4203 |
| projects/harry-potter-prank/tella1/guide.mp4 | 1920x1080 | 30 | 342.1 | 1026 |
| projects/harry-potter-idea2/src/wbfeast/n4qSSAk8g2I.mp4 | 1080x1920 | 23.976 | 20.5 | 4044 |
| projects/harry-potter-idea2/src/wbsweets/jqcux1cXw60.mp4 | 1080x1920 | 23.976 | 48.7 | 3337 |
| projects/harry-potter-idea3/src/tre/AZGH_imo_3g.mp4 | 1920x1080 | 25 | 3113.7 | 2140 |
| projects/harry-potter-idea3/_rk/raw/tre_1500.mp4 (cut of the above) | 1920x1080 | 25 | 90.0 | 4670 |
| projects/harry-potter-idea3/src/making/TvB_0vYEyO8.mp4 | 1920x1080 | 23.976 | 487.0 | 3458 |
| projects/harry-potter-idea3/src/bonus/wEm4aBjgYlQ.mp4 | 480x270 | 29.97 | 78.7 | 440 |
| projects/harry-potter-idea3/src/hboteaser/SJVmeJaS44s.mp4 | 1920x1080 | 23.976 | 157.2 | 1713 |
| projects/harry-potter-idea3/src/headtour/jQmfa-YWoNU.mp4 | 1920x1080 | 59.94 | 75.7 | 5117 |
| projects/harry-potter-idea3/src/yerawizard/nnD8FKXzIGs.mp4 | 1920x1080 | 23.976 | 862.5 | 1345 |
| projects/harry-potter-idea3/src/wbtruth/yC4ImdeBtQs.mp4 | 360x640 | 23.976 | 105.2 | 511 |
| projects/harry-potter-idea3/src/set2025/double_closeup_jayjlevans.mp4 | 576x1024 | 30 | 51.5 | 930 |
| projects/harry-potter-idea3/src/set2025/leaky_clicknews.mp4 | 1280x720 | 23.976 | 54.4 | 1485 |
| projects/harry-potter-idea3/src/set2025/photo_frost_crowd.mp4, photo_walk.mp4 | 1080x1920 | 30 | 6.0 each | 610-700 |

Notes: `dvd_0` and `hsc_2070` are 320x180 scouting stubs (hsc_2070 has a black picture and real audio; RUN.md line 50). `hsc_dan.mp4` is the real 1080p60 HSC picture (2183-2223 s of the E: file).

## 2. Project folder listings (src, raw, meta, transcript)

### harry-potter-niche
- src/coltrane: pudHrUqy2I0.mp4 (Return to Hogwarts "Hagrid will", 468p rip), info.txt
- src/lastday: DknJ6__GcTM.mp4 (AP 2010 Radcliffe wrap), FfCsVPJsw-E.mp4 (Off Camera), Tb7GKZGmIRE.mp4 (Wizarding World cast goodbye), info.txt
- src/newboy: jo9Pcia-YuQ.mp4 (AP, Nov 2026, new HP advice), info.txt
- meta/: ids.txt, ids2.txt, ids3.txt, meta.txt to meta7.txt, offcamera_shorts.txt, probe.sh to probe7.sh, subs/ (jHPrkTmj6FU and y6FRGXLHsSw .en and .en-orig .vtt)
- transcript/: ap2010, ap2026, offcamera, wbgoodbye (each .scout.json, .scout.txt, .wav)
- no raw/ folder

### harry-potter-prank
- raw/: dvd_0.mp4, hsc_2070.mp4, hsc_dan.mp4
- src/rickman: tgXZefAYRnQ.mp4, "Alan Rickman on Snape and his pride in the young actors (2015).mp4", info.txt
- src/snape: ALL Severus Snape Scenes, Prisoner of Azkaban Page 394, Severus Snape scene pack 4K, Wizard Duel Snape vs Lockhart
- meta/: fresh.txt, fresh2.txt, fresh3.txt (YouTube search lists for the prank), snape_find.sh, snape_find.txt
- transcript/: fallon, hsc_30-00-40-00, prank (.scout.json, .scout.txt, .wav), words.json (dvd_0 and hsc_2070 word timing); also captions/transcript/words.json and _rk/transcript/words.json (Rickman 2015)
- other: tella1/guide.mp4, outputs/ (finished Short v1 and final), renders/, proof/, premiere/, work/

### harry-potter-idea2
- src/wbfeast: n4qSSAk8g2I.mp4 (WB "BTS of the Hogwarts welcome feast"), info.txt
- src/wbsweets: jqcux1cXw60.mp4 ("Magical sweets in the Gryffindor dormitory"), info.txt
- meta/: hp_official_shorts.txt, s.txt, search.sh
- transcript/: wbfeast, wbsweets (.scout.json, .scout.txt, .wav)
- no raw/ folder

### harry-potter-idea3
- src/tre: AZGH_imo_3g.mp4 + info.json + dl.log (The Rest Is Entertainment, Chris Columbus, 28 Aug 2025)
- src/making: TvB_0vYEyO8.mp4 (Collider "Making of Hagrid"); src/bonus: wEm4aBjgYlQ.mp4 (Muggle-V Hagrid bonus disc); src/headtour: Hagrid's Animatronic Head; src/hboteaser; src/yerawizard ("Yer a wizard, Harry" scene); src/wbtruth; src/set2025 (4 videos, 7 stills)
- _rk/raw/tre_1500.mp4, _rk/transcript, _rk/transcribe.log
- meta/: dl.log, dl.sh, probe.sh, probe.txt, probe2.sh, probe2.txt, s.txt, s2.txt, s3.txt, search.sh, search2.sh, tw/ (5 tweet json files)
- transcript/: bonus, collider_315-390, tre_0-1770, tre_1770-3114 (each .scout.json, .scout.txt, .wav), tre_hagrid_1512-1584.wav, scout.log, scout2.log
- no raw/ folder

## 3. Film-scene, character and how-it-was-made passages

Format: timestamp | speaker | quote (<= 25 words) | what it is about.

### A. Chris Columbus, The Rest Is Entertainment
File: `projects/harry-potter-idea3/src/tre/AZGH_imo_3g.mp4` (1080p25). Transcripts: `transcript/tre_0-1770.scout.txt` and `tre_1770-3114.scout.txt`, absolute timestamps. Scanned end to end.

| ts | speaker | quote | about |
|---|---|---|---|
| 17:09-17:57 | Columbus | "my daughter, Eleanor... kept telling me to read this book... I finally read it, and I fell in love with it." | how he got film 1 (Warner "bake-off") |
| 18:21-18:50 | Columbus | "they sent me the Harry Potter script... on red paper... if it's on red, you cannot photocopy it." | the red script he rewrote with camera directions, for free |
| 19:15-19:41 | Columbus | "Two and a half hours with her in Scotland... she said, that's exactly the same way I saw the film." | meeting J.K. Rowling, getting the job |
| 20:37-21:00 | Columbus | "it took 160 days to shoot the first film. And we did the first two back to back." | shoot length, why he left after film 2 |
| 21:43-22:58 | Columbus | "we agreed that we would cast the family as well as the kids" | casting Radcliffe, Watson, Grint; protecting the kids from fame |
| 23:13-24:33 | Columbus | "I was obsessed... with this character, Peeves... Rik Mayall came in and did an amazing sort of reading as Peeves." | Peeves filmed, CGI never worked, cut from film 1 |
| 25:15-26:20 | Columbus | "Martin Bayfield... played Hagrid with a giant sort of fake rubber Hagrid head that we sometimes replaced with CGI." | Hagrid = Bayfield + animatronic head; the new HBO Hagrid wears "exactly the Hagrid costume that we designed" |
| 49:17-50:41 | Columbus | "I was basically the acting coach for those three kids... I've been Harry Potter. I've been Hermione. I've been Ron." | off-camera line reading for Harris, Smith, Rickman; why film 1 has so many cuts; film 2 allowed a tracking shot |

Not HP: Mrs Doubtfire improv 34:24-37:38, Good Will Hunting 47:44-49:17, Thursday Murder Club.
Existing derived cut: `_rk/raw/tre_1500.mp4` (90 s, 25:00-26:30) and `transcript/tre_hagrid_1512-1584.wav`.
Not checked: framing and who is on screen (podcast table, two hosts plus guest).

### B. Happy Sad Confused with Daniel Radcliffe
File: `E:\Bullshit Folder\Henry\Daniel Radcliffe, Jonathan Groff...mp4` (1080p60). Transcript: `projects/harry-potter-prank/transcript/hsc_30-00-40-00.scout.txt`, window 30:00-40:00, absolute = relative + 30:00. Scanned end to end; the scout stops at about 40:11 absolute, so the rest of the episode is unscouted.

| ts (abs) | speaker | quote | about |
|---|---|---|---|
| 33:17-34:15 | Radcliffe | "coming from sort of the Potter films... do I belong here?... because I'm Harry Potter?" | career after Potter (personal, no scene) |
| 35:06-37:21 | Alan Rickman (2015 archive tape shown on the podcast) | "they were doing it 52 weeks. It was this was their life... from 12 to 22" | Rickman on the kids growing up on the films |
| 36:26-37:21 | Radcliffe | "I was so intimidated by him for the first three movies... this guy hates me... He cut short a vacation in Canada to come and see me in Equus." | Rickman/Snape as intimidating, then mentor. `hsc_dan.mp4` covers 36:23-37:03; the last 18 s of the story are outside it |

The rest of the scouted window is Broadway chat and a BetterHelp ad (37:45-38:47); no other scene stories.

### C. "Prank on Harry Potter"
File: `E:\Bullshit Folder\Henry\Prank on Harry Potter.mp4` (480p). Transcript: `projects/harry-potter-prank/transcript/prank.scout.txt` and `words.json`.

| ts | speaker | quote | about |
|---|---|---|---|
| 0:00-0:50 | Radcliffe (voice) | "They had put a fart machine into my sleeping bag... Michael Gambon had actually been pressing it during the take" | Azkaban Great Hall sleeping-bag scene prank (Gambon, Rickman, Cuaron) |

### D. Alan Rickman 2015 interview (Josh Horowitz Clips)
File: `projects/harry-potter-prank/src/rickman/tgXZefAYRnQ.mp4` (1080p, 375 s). Word timing: `_rk/transcript/words.json`, seconds.

| ts | speaker | quote | about |
|---|---|---|---|
| 0:00-1:15 | Rickman | "I think it gave me a bit of a structure to the year because I was only shooting at seven weeks a year" | what Potter did to his career |
| 2:06-2:56 | Rickman | "Mike Newell and I had done a film called Awfully Big Adventure and Alfonso Cuaron and I had done... a series for Showtime" | history with the HP directors |
| 3:21-3:46 | Rickman | "by the time we finished, we were on a piece of old grass with this kind of green stuff all around us" | films moved from location to green screen/CGI |
| 4:11-4:36 | Rickman | "Rafe and I always knew was the kind of refuge, because we both had very strong disguises" | being recognised by kids (Rafe = Ralph Fiennes) |
| 4:36-5:50 | Rickman | "as much as I was doing it and the rest of us for seven weeks, they were doing it 52 weeks" | the kids growing up, Radcliffe in the musical |

### E. Fallon
`E:\Bullshit Folder\Henry\Alan Rickman Takes Jimmy to Task...mp4`, transcript `fallon.scout.txt`, 0:00-1:55: impersonation banter, no film story.

### F. Hagrid, how it was made
| source | ts | speaker | quote | about |
|---|---|---|---|---|
| `idea3/src/bonus` (480p), `transcript/bonus.scout.txt` | 0:01-0:53 | crew voices | "The heads are air-cooled... we pump cool water around Martin's body." | Hagrid suit cooling, "Team Hagrid" |
| `idea3/src/making` Collider 1080p, `transcript/collider_315-390.scout.txt` | 5:15-6:30 | narrator (Collider voiceover, not cast) | "Martin Bayfield, a 6 foot 10 inch former rugby player who was hired as Coltrane's body double." | Bayfield in costume, platform shoes, little CGI |

Only 5:15-6:30 of the 487 s Collider video was transcribed.

### G. Short clips
- `idea2 wbfeast` (1080x1920, 20 s, WB): 0:00-0:34, crew "one, two, three, action. The food appears." Hogwarts feast being set; no named speaker.
- `idea2 wbsweets` (1080x1920, 49 s, WB): 0:01-0:34, cast reactions at the Gryffindor sweets set ("Look at his face"); no named speaker.
- `niche wbgoodbye` (Tb7GKZGmIRE, 1080p, 183 s): 0:13-2:44, last-day speeches (Rickman and Thewlis, Coltrane, the Bellatrix actress, Rupert, Emma). Quote: "There'll never be a frame of any of these films that I don't look at and connect immediately to a memory." Last days, not a scene.
- `niche ap2010` (640x480): 0:32 Radcliffe on the DH2 wrap, "Me, Rupert and Emma and most of the crew were crying quite a lot." `ap2026` (1080p): Radcliffe on new-Harry advice. `offcamera` (720p): fame and drinking. All personal, not film scenes.

## 4. Previously logged HP film-scene leads in research/*.md
Keywords: deleted scene, improvis*, Dobby, Always, Neville, Sirius, Fred, Lupin, Hedwig, Draco, Voldemort hug, Peeves, Dudley. Paths are under `research/`. The `deep-research-2026-11-14/hp-films/*.md` files were being written by another gatherer at the same time.

| lead | file:line |
|---|---|
| Gambon + Rickman fart-machine prank on Radcliffe (Azkaban); IG 291K and 88.6K shares; source Radcliffe 2014 Reddit AMA; footage origin (G5) still OPEN | `harry-potter-niche-2026-11.md:508-559` |
| "Snape Farts" 293K and "Harry Potter Fart" 44K, unchecked | `harry-potter-niche-2026-11.md:624-625` |
| Hagrid was two men (Bayfield + animatronic); Columbus voice at AZGH_imo_3g 25:15-26:20; 1080p Collider re-cut as best picture | `harry-potter-niche-2026-11.md:645-695` |
| Coltrane "Hagrid will" joined to the new Hagrid; killed (score under voice, 468p) | `harry-potter-niche-2026-11.md:76,155,215-242,307` |
| Dumbledore vs Voldemort duel BTS (competitors 13M-2.7M; no actor tells a duel story) | `harry-potter-niche-2026-11.md:43,92-100,148,231` |
| Voldemort BTS 5.5M (Y0kCTU3haVA) | `harry-potter-niche-2026-11.md:170,393` |
| Fiennes "too scary for children" 1.26M (spent) | `harry-potter-niche-2026-11.md:158` |
| "No on-camera first-party telling found for Columbus, Davis, Phelps" (superseded by our Columbus transcript) | `harry-potter-niche-2026-11.md:639` |
| Radcliffe + Oldman on Rickman knowing Snape's ending (Return to Hogwarts, 1 Jan 2022) | `deep-research-2026-11-14/hp-films/firstparty-tellings.md:7,23` |
| Felton on Fiennes' improvised Voldemort hug (DragonCon 2011; memoir) | `firstparty-tellings.md:9,24` |
| Rik Mayall cut as Peeves | `firstparty-tellings.md:12,36` (first-party source on disk: Columbus 23:13-24:33) |
| Phelps twins on Fred's death; Matthew Lewis on St Mungo's/Neville; Helen McCrory | `firstparty-tellings.md:16,27` |
| Harry Melling's cut Dudley scene; Fiona Shaw deleted DH scene (no first-party video found) | `firstparty-tellings.md:28-29` |
| Radcliffe and Toby Jones on Dobby actor (print only) | `firstparty-tellings.md:25` |
| Jason Isaacs; Gary Oldman on HSC podcast | `firstparty-tellings.md:41,32` |
| HBO series: no on-record new-cast quote about Snape's "Always"; child-cast warning | `hp-films/hbo-peg.md:17,50` |

No Sirius, Lupin or Hedwig lead exists in any research md. The only "Always" hit is the HBO gap line above.

## 5. On disk in HD (>= 720p) with a clean on-camera teller
1. Columbus on Peeves/Rik Mayall (23:13-24:33), Hagrid/Bayfield head (25:15-26:20), acting coach off camera (49:17-50:41), red script and Rowling (18:21-19:41): `projects/harry-potter-idea3/src/tre/AZGH_imo_3g.mp4`, 1080p25.
2. Radcliffe on Rickman's intimidation (36:26-37:21): HSC file on E:, 1080p60; the cut `projects/harry-potter-prank/raw/hsc_dan.mp4` covers 36:23-37:03.
3. Rickman 2015 on the kids, directors, green screen (see D): `projects/harry-potter-prank/src/rickman/tgXZefAYRnQ.mp4`, 1080p24, 727 kbps.
4. Only below the bar: the sleeping-bag prank (480p, Radcliffe voice over footage) and the Hagrid suit/cooling (480p crew voices; the 1080p Collider has a narrator, not a cast teller).
