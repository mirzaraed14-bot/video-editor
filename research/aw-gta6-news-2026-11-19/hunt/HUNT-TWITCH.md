# Twitch hunt: wild face-cam reactions to the GTA 6 Bigfoot encounter (20 Nov 2026, ~20:50)

Silent run (ffmpeg frames and `-f null` only, no playback). Twitch only (yt-dlp, `--ignore-config`, one process at a time under a lock file plus the machine-wide `ps` check). No YouTube, no browser, no VOD pulled beyond two 90 s sections. Everything lives under `hunt/`; paths below are relative to `research/aw-gta6-news-2026-11-19/`.

## Bottom line

**About three distinct clips qualify** (own face cam + the encounter on frame + a real reaction), and **only one is truly wild: Fanum**. Nothing screams or leaves the chair. This is a short list, not ten.

| # | Streamer | Why |
|---|---|---|
| 1 | **Fanum** | Hand clamped over his mouth while the hairy legs stand over him, then a shouted "what is that?" (no profanity in that window). |
| 2 | **Kai Cenat** (one night-chase moment, two clips: "finding skunk ape" 6,571 views and the 60 s "bigfoot hunting") | Stunned, mouth open through the Mr. Mangrove chase; at the effigy "oh my gosh bro" and a hand over his mouth. No profanity, but not loud either. |
| 3 | **summit1g** (one moment, three clips; "???????" has 1,521 views) | The legs at 40-44 s are confirmed, but he is flat: "What the fuck is happening?" Very quiet audio (-29 LUFS). |

HutchMF is a weak fourth (legs and blackout on frame, but he never speaks). Everything else fails a test (section c).

**Coverage caveat (read this).** The yt-dlp lane was held by other sessions' downloads for most of the run (two to three minutes per list), so I did **not** get the full 38 x 3 sweep; section (a) says exactly which lists were pulled. Several lists came back empty or short and **must be treated as failed or unreliable pulls, not as "no clips"**: fanum 24hr is empty although his 7d list holds 20 Nov clips; ishowspeed 7d is empty although yesterday's pull held about 130; kaicenat 7d returned 20 entries against 98 yesterday; adinross returned 0; summit1g 24hr is empty and his 7d was never obtained. The 7d lists for lacy and a second Kai pass were still queued when I stopped (I killed my workers; nothing of mine is still running). The `all` range (all-time top 20 per channel) was skipped on purpose: a two-day-old game cannot be in it. Channels with no fresh list rely on the 19 Nov 24hr lists from the earlier pull (`twitch/r-*.json`), which cover day 1 only, so an undiscovered day-2 clip is possible, especially for the channels marked NOT PULLED.

## (a) Channel log

Lists are yt-dlp flat playlists of Twitch clips, top 150 by views per range. "fresh" = pulled 20 Nov from this run (`hunt/lists/`); "older 24hr" = the 19 Nov pull in `../twitch/` (day 1 only; the Kai 7d there is the 98-clip list). "all" (all-time top 20) was not pulled for anyone. Title grep = bigfoot, big foot, skunk, sasquatch, mangrove, effigy, monster, creature, scream, scared, scary, jumpscare, spooked, wtf, what is that, knocked, passed out, swamp, ape, kirk, drone (plus the misspelling "biggfoot", which I caught by eye). Top-15 most-viewed clips per channel with vague titles were opened as thumbnail contact sheets for every channel that had a list; the sheets I read are in `hunt/sheets/`.

| channel | fresh lists pulled (20 Nov) | older 24hr list (19 Nov) | unique clips seen | title grep matches | strong matches (bigfoot/skunk/kirk/swamp/creature...) | note |
|---|---|---|---|---|---|---|
| kaicenat | 24hr=384, 7d=20 | 153 | 435 | 7 | 1 | 7d list returned only 20 entries (98 yesterday): unreliable |
| ishowspeed | 7d=0 | 131 | 129 | 2 | 0 | list came back EMPTY: unreliable, treat as a failed pull |
| xqc | 24hr=150, 7d=150 | 54 | 292 | 7 | 0 |  |
| ludwig | NOT PULLED (lane busy) | 0 | 0 | 0 | 0 |  |
| adinross | 24hr=0 | 0 | 0 | 0 | 0 | list came back EMPTY: unreliable, treat as a failed pull |
| jynxzi | 24hr=150 | 240 | 352 | 4 | 0 |  |
| lacy | 24hr=150 | 0 | 148 | 1 | 0 |  |
| caseoh_ | 24hr=150 | 17 | 158 | 1 | 0 |  |
| summit1g | 24hr=0, 7d=59 | 74 | 121 | 3 | 3 |  |
| fanum | 24hr=0, 7d=99 | 0 | 97 | 1 | 1 |  |
| asmongold | 24hr=0 | 0 | 0 | 0 | 0 | list came back EMPTY: unreliable, treat as a failed pull |
| timthetatman | 24hr=150 | 0 | 145 | 1 | 0 |  |
| sodapoppin | 24hr=141 | 183 | 254 | 0 | 0 |  |
| ohnepixel | 24hr=150 | 379 | 487 | 3 | 0 |  |
| clix | 24hr=150 | 833 | 806 | 0 | 0 |  |
| typicalgamer | 24hr=137 | 314 | 375 | 9 | 2 |  |
| valkyrae | NOT PULLED (lane busy) | 0 | 0 | 0 | 0 |  |
| pokimane | NOT PULLED (lane busy) | 0 | 0 | 0 | 0 |  |
| shroud | NOT PULLED (lane busy) | 0 | 0 | 0 | 0 |  |
| nadeshot | NOT PULLED (lane busy) | 6 | 6 | 0 | 0 |  |
| n3on | 24hr=8 | 0 | 8 | 0 | 0 |  |
| plaqueboymax | 24hr=118 | 9 | 119 | 1 | 0 |  |
| agent00 | 24hr=58 | 153 | 193 | 6 | 3 |  |
| emiru | NOT PULLED (lane busy) | 2 | 2 | 2 | 0 |  |
| mizkif | NOT PULLED (lane busy) | 0 | 0 | 0 | 0 |  |
| hasanabi | NOT PULLED (lane busy) | 394 | 314 | 9 | 7 |  |
| esfandtv | NOT PULLED (lane busy) | 0 | 0 | 0 | 0 |  |
| quin69 | NOT PULLED (lane busy) | 49 | 49 | 2 | 0 |  |
| ninja | NOT PULLED (lane busy) | 0 | 0 | 0 | 0 |  |
| dream | NOT PULLED (lane busy) | 0 | 0 | 0 | 0 |  |
| ranboo | NOT PULLED (lane busy) | 0 | 0 | 0 | 0 |  |
| tommyinnit | NOT PULLED (lane busy) | 0 | 0 | 0 | 0 |  |
| stableronaldo | 24hr=150 | 273 | 397 | 7 | 1 |  |
| jasontheween | 24hr=150 | 236 | 333 | 6 | 2 |  |
| theburntpeanut | 24hr=150 | 66 | 206 | 1 | 0 |  |
| brendaniel | 24hr=8 | 37 | 44 | 3 | 3 |  |
| hutchmf | 24hr=150 | 216 | 314 | 2 | 2 |  |
| swagg | 24hr=83 | 263 | 283 | 2 | 2 |  |

Not pulled this run (lane busy, no fresh list): ludwig, asmongold, timthetatman, sodapoppin, ohnepixel, clix, valkyrae, pokimane, shroud, nadeshot, n3on, plaqueboymax, agent00, emiru, mizkif, hasanabi, esfandtv, quin69, ninja, dream, ranboo, tommyinnit, swagg. Where the table shows an older 24hr count, day 1 was grepped; otherwise the channel is uncovered. Empty or short lists (adinross, ishowspeed 7d, fanum 24hr, summit1g 24hr, kaicenat 7d) are unreliable pulls and must not be read as "no clips"; summit1g 7d and lacy 7d were never obtained.

## (b) Ranked: clips that pass all three tests

"Cam" = the streamer's own face cam, in source pixels. Loudness from `ffmpeg ebur128` over the whole file (I = integrated; TP = true peak). Face-cam proof strips: `hunt/sheets/cam-*.jpg`; frame contact sheets: `hunt/sheets/<clip>.jpg`; speaker-check frames: `hunt/sheets/attr-*.jpg`. **Speaker attribution:** the game prints small subtitles at the bottom ("Ugh... fuck...", "What happened?", "Oh shit! Hey. I found him, he's over here!"), and these clips also carry burned-in captions of the streamer's speech that star out profanity. Every line below was checked against the frame at its timestamp; game lines are marked as NOT the streamer. ASR is faster-whisper medium.en; treat it as a reading aid, not a quote source.

### 1. Fanum "fanum finds out bigfoot is real"
- **URL:** https://www.twitch.tv/fanum/clip/CleverImportantNuggetsCmonBruh-uSYmEMOocVv1V7Cv (clip id 2119485677), 219 views, 11-19 06:00, 60 s.
- **File:** `media/ondisk/fanum-bigfoot.mp4` (1920x1080, 60 fps, 60.03 s). Face proof: `hunt/sheets/cam-fanum-peak.jpg`, `hunt/sheets/cam-fanum-full.jpg`; screen proof: `hunt/sheets/fanum-peak-screen.jpg`.
- **Best window: 27.5-31.5 s** (4 s: hand over mouth, the shouted "what is that?", the hairy legs on screen). Wider cut 25.0-31.5 s. Second window: 3.0-7.4 s (effigy close-up, with the swearing).
- **On screen:** 0-15 s he walks to the effigy; 3-10 s the effigy close-up (game "ZOOM" prompt); 15-24 s the green fog and the player staggering, then down; **24.5-31.5 s the hairy legs and boots stand over the fallen player**; 30-38 s blackout; 38-40 s he wakes by the red truck.
- **His words** (burned-in captions or the absence of a matching game subtitle confirm each): 3.0-4.5 "The hell is this thing?" / 4.8-7.4 "What the fuck am I looking at?" (captions "thing? **** ***" and "**** am I" on screen) / 14.2-15.9 and 17.3-18.0 "Am I getting high?" (game subtitle at those moments reads "Ugh...", so this is him; **drug reference, flag**) / 20.1 "Whoa!" / 22.5 "Jason!" (burned captions; screen black, body down) / **25.3-26.7 "Bro,"** then **"what is that?" ending in a shout at 30.6-31.3 s**, the loudest moment of the window (momentary -8 LUFS; `words.json` smears "what is" across 27.4-31.0, so the 25.3-31.3 segment is one 6 s line with a long silent beat inside it; burned caption "Bro what is" is visible at 30.0 s) / 54.2-56.6 "the he just fucked me" (no game subtitle on screen).
- **NOT him (game subtitles):** 34.4-36.1 "ooohh fuck" is the game's "Ugh... fuck..." on the black screen; 38.4-40.3 "what happened?" is the game's line at the truck.
- **Face:** 19.5-25 s wide eyes, brow furrowed, leaning into the screen; **26.5-30.5 s hand clamped over his mouth, eyes wide, frozen**; 45-50 s turns away, laughing. The strongest expression of the batch.
- **Cam:** about 430 x 240 px (22 % of the width), left edge, x 2-429, y 403-643 (37-60 % down). Dark red room with a neon "V" sign behind him.
- **Overlays to cover:** chat column top right (usernames and messages, readable; includes "BIGFOOT" and "SKUNK APE"), "DEATH COUNTER: 1", "Twitch Subs 7157 / 8,000" at right, minimap bottom left, burned-in captions lower centre ("Jason!", "Bro what is"), the game "ZOOM" prompt (3-10 s).
- **Profanity:** his own: "hell" 3.0, "fuck" 5.6, "fucked" 54-56.6. The game's "fuck" at 35 s. **None inside 27.5-31.5 s.** Drug word: "high" 14-18 s (outside the window).
- **Minors:** none visible. **Loudness:** I -14.6 LUFS, LRA 13.9, TP 0.0 dBFS (touching full scale); loudest 3 s starts at 15.5 s.

### 2. Kai Cenat, night chase and effigy (one moment, two clips)
The 22.8 s clip is the 60 s clip's 6.7-29.5 s (the stream counters match, 168,983 to 171,812, and the NPC line lands 6.7 s apart in the two files); only the 60 s clip reaches the effigy.
- **60 s clip "bigfoot hunting":** https://www.twitch.tv/kaicenat/clip/TrappedSpinelessDugongLitty-k4LDRLXugP8d5cQd (clip id 4096145023, clipper ghostyyyyyyyy19), 7 views; file `media/ondisk/kai-bigfoothunting-4096145023.mp4` (1920x1080, 60 fps). Proof: `hunt/sheets/cam-kai-4096.jpg`, `hunt/sheets/cam-kai-4096-peak.jpg`, `hunt/sheets/attr-kai.jpg`.
- **22.8 s clip "finding skunk ape":** https://www.twitch.tv/kaicenat/clip/BoldEncouragingHamJonCarnage-pe0Q59lJ1Zj-4lUY (clip id 2131405255), **6,571 views**, 11-19 03:58; file `hunt/clips/kaicenat-2131405255.mp4` (1280x720, 60 fps). Proof: `hunt/sheets/kaicenat-2131405255.jpg`, `hunt/sheets/cam-kai-skunk.jpg`.
- **Best window: 53.5-58.5 s of the 60 s clip.** On screen: the night effigy up close with the game text "The hell is this? / Inspect the tree" and "ZOOM". Second window: 22-26 s (equals 15.3-19.3 s of the short clip): "Chase Mr. Mangrove" in the fog (HUD text at the bottom), no creature in view.
- **His words:** 29.4-30.7 "No, don't lose him. There's no way." (burned caption "There's no way" at 30.0) / 32.2-33.1 "No, no, no, no." (caption "no I") / 35.4-40.2 "He said don't shoot him." (repeated; caption "him"; he is repeating a quest line) / 41.9 "Oh my god." / 46.4 "Another victim." / **55.0-58.5 "oh my gosh bro"**. At 22.4 and 25.5 s the 60 s clip's ASR hears "Oh my god!" twice; the short clip's ASR hears "Yeah" on the same audio, so the words are **uncertain**, though no game subtitle is on screen then (only the "Chase Mr. Mangrove" HUD line).
- **NOT him:** 16.5-17.5 "It's over here" is the game NPC (subtitle on screen at 16.9 s: "Oh shit! Hey. I found him, he's over here!"). In the short clip that is 9.7-13.2 s, and it has no other speech from Kai.
- **Face:** from 20 s on, eyes wide and mouth open, frozen (stunned, not screaming); **57-58 s hand over his mouth** (`cam-kai-4096-peak.jpg`).
- **Cam:** about 392 x 220 px in the 1080p clip (x 0-392, y 432-652; pink-lit bedroom); about 262 x 150 in the 720p clip (x 0-262, y 285-437). Chat lines run directly under the cam.
- **Overlays to cover:** stream counters right edge (about "173,156 / 16,844,794"), **the whole chat strip under the cam, which includes the line "joeywildinnn: LOOK FOR NIGFOOT" (0-5 s; a slur-like misspelling, must cover) and "KILL THAT BOY" (near 36-37 s, low-res read)**, burned-in captions, the green "Chase Mr. Mangrove" HUD line, minimap.
- **Profanity:** none from Kai; the game subtitle "Oh shit". **Minors:** one person in dark clothes walks across the room behind him at about 23-27 s (partial back/side view; build looks adult against the bed and TV, but **age cannot be confirmed**; crop `hunt/frames/attr/kai-person26.png`). **Loudness:** 60 s clip I -13.2 LUFS, LRA 5.4, TP -0.2, loudest 3 s from 35.8 s; 22.8 s clip I -12.7, TP 0.0.

### 3. summit1g, the legs (one moment, three clips)
- **Primary URL:** "???????" https://www.twitch.tv/summit1g/clip/PunchyGlutenFreeCheesecakeNinjaGrumpy-FgCJzHC4BNv_XGNH (clip id 3737810682), **1,521 views**, 11-19 05:15, 60 s; file `hunt/clips/summit1g-3737810682.mp4` (1280x720, 60 fps, I -29.6 LUFS, TP -8.3).
- **Same moment, other clips:** "Bigfoot jumpscare" (1 view) https://www.twitch.tv/summit1g/clip/MistyWittyWormDatBoi-ZrvAwNzMJzIFRn3g and "BigFoot Got 1G" (78 views) https://www.twitch.tv/summit1g/clip/DelightfulDullNikudonFutureMan-Zn3yTuneaQWjQv6u. The 2560x1440 copy `media/ondisk/summit-bigfootjumpscare.mp4` (60 s; I -29.2 LUFS, LRA 14.5, TP -6.9) is what I used for ASR, loudness and the face strip (`hunt/sheets/cam-summit-jump.jpg`). Beats line up with the 720p clip (burned caption at 35 s, legs at 40 s, blackout 45-50 s); expect up to about 3 s of offset between the copies.
- **Best window: 33.0-44.5 s** (his line, then the legs at 40-44 s).
- **His words:** 33.1-37.3 "What the fuck is happening?" (the burned caption at 35 s reads "*** **** is"). That is the only line of his in the window.
- **NOT him (game):** "Ugh... fuck..." on black at about 45 s, 47.0 "My dad?", 50.5 "What do you mean?", 58.5 "What happened, man?" (the game's subtitle "What happened?" is on screen at 50 s).
- **Face:** turns to the camera with raised brows at 34-38 s, mouth open at 40-42 s. A mild, puzzled reaction, nothing wild.
- **Cam:** about 683 x 384 px (27 % of width), x 0-683, y 698-1082 in the 1440p copy.
- **Overlays:** donation alert "Khafen: $50.00" above the cam, counter "21,256" at its bottom-left, minimap, burned-in captions (profanity already starred out).
- **Profanity:** "fuck" at 33-37 s. **Minors:** none.

### Weak pass, listed for completeness: HutchMF "Bigfoot"
- https://www.twitch.tv/hutchmf/clip/SuaveObedientDinosaurWutFace-yTi5OgHG_rYyjRLD, 96 views, 30 s. File `media/ondisk/hutch-bigfoot.mp4` (2560x1440). The legs, the blackout and the truck wake-up are all on frame, and his cam is visible (framed box, about 675 x 380, x 13-688, y 597-977, with a "nimblzzz 12807" widget below). But **he never speaks** (ASR found no speech; I -30.9 LUFS, TP -12.8) and his face stays calm (`hunt/sheets/cam-hutch-test.jpg`). The "Ugh... fuck..." and "What happened" on screen are the game's. Fails the reaction test.

## (c) Rejected, with the reason

| Clip | Reason |
|---|---|
| Brendaniel "BIG FOOT REAL" (1,623 v) and "Bigfoot sighting in GTA VI" | Effigy and legs on frame, loud audio (-13.5 LUFS), but **no face cam in the clip** (chat only). |
| summit1g "summit finds bigfoot HOLY!!!" (45 v, 19.8 s) | Drive to the spot only: truck, a bloody patch, the weapon wheel. The encounter is not on frame. His "What the f-" (caption "the f ****") is over the weapon wheel. |
| Typical Gamer "skunk ape" and "kirkcall" (1 v each) | Only the "Have you seen Skunk Ape? CALL KIRK" flyer and an ATM. Calm face, no creature. |
| CaseOh "Jump Scare" (41 s) | A car chase, not Bigfoot. His other clips are not the encounter. |
| Jynxzi "jump scare" (6,879 v) | Highly expressive face cam, but the scene is a kitchen NPC, not the encounter. His list has no Bigfoot title. |
| Lacy VOD, 6:38:42 "Is that fucking Bigfoot" (90 s section pulled, `hunt/clips/vod-lacy-6h38m30.mp4`) | He walks through the swamp, then something far off. No creature on frame, and his cam is a small strip (top left, about 26 % wide x 20 % tall). Chat says "dino". Not the effigy or the legs. |
| Lirik VOD 3:17:10 "My god, is that Bigfoot?" (90 s section, `hunt/clips/vod-lirik2-3h16m50.mp4`) | Airboat in the swamp; **no face cam in the VOD at all**. |
| xQc VOD sections (`media/ondisk/xqc-*`) | The speech is game dialogue (Kirk, "Mr. Mangrove"); xQc himself is quiet (-27 to -29 LUFS) and his 7d/24hr clip lists have no Bigfoot title. xQc "Nope right out!" (4 v) is an office scene. |
| Lacy, JasonTheWeen, Swagg, Agent00, HasanAbi, Speed "bigfoot" clips | Already checked by the hub: titled, but no encounter on frame. Not re-opened. |
| Kai "WTF" / "HEY WTF YOOO!" / "o0mg" and the other vague top clips of Kai, xQc, Speed, Typical Gamer, Jynxzi, Lacy, CaseOh, Hutch, Hasan, Stable, Fanum | Thumbnails read on contact sheets (`hunt/sheets/new-*.jpg`, `old-*.jpg`, `x1-all.jpg`): nudity scenes, clubs, radio, driving, bank, boat. No swamp, no effigy. (A thumbnail is one frame; a clip with a vague title and an unlucky first frame could still hide an encounter.) |

## (d) VOD keyword hits (read-only index; transcript text, never a quote source)

From `X:/Claude Projects/GTA 6/research/vo-slate-2026-11-19/tools/kw.py` over the big-VOD transcripts (times are VOD time, h:mm:ss; the VOD chunks on disk are audio only, so no frames were possible). Full list: `hunt/vod-hits.txt`.

| Streamer | VOD time | Line |
|---|---|---|
| **lacy** (VOD 2932194507) | 6:38:42-6:39:11 | "What is that? / Is that fucking Bigfoot / Is that Bigfoot? / I lost him." then 6:39:27 "is that normal, or is that like a glitch? Did I just find a rare Easter egg?" (checked: not the effigy) |
| **lirik2** (VOD 2933880721) | 3:17:10 | "What the fuck is that? Oh. My god, is that Bigfoot?" (airboat; no cam) |
| **lirik2** | 3:21:35-3:21:51 | NPC jokes: "I'm a Sasquatch, but I know how to fucking use tech breach... Even Bigfoot's got a phone" |
| **lirik2** | 4:04:16-4:04:20 | "What a day, I'm at a Sasquatch. Passed out, woke up. Not sure what the Sasquatch did" (the blackout; a recap, no reaction heard) |
| **xqc** | 14:53:49-14:54:53 | Kirk: "skunk ape... Mr. Mangrove ... You're saying I saw Bigfoot / Nope, skunk ape, same genus, different species" |
| **xqc** | 15:04:38 | "Like Kirk has a fucking quest" |
| **jasontheween** | 5:51:29 | "I saw Bigfoot" (after a bee sting) |
| **jasontheween2** | 12:04:20-12:04:48 | Kirk's voicemail: "skunk ape hunter... skunk ape information" |
| **jasontheween2** | 12:21:50 | "I've got a big foot ... got caught him yet or no" |
| **stableronaldo** | 1:09:59 | "they call him mr mangrove" (the game's intro speech) |
| **xqcgta5b** | 5:57:32 | "there's a sasquatch trying to get in this grandeur here" (GTA 5, unrelated) |

## Files made

`hunt/HUNT-TWITCH.md` (this file) and, under `hunt/`: `lists/` (every clip-list JSON), `thumbs/`, `sheets/` (contact sheets, face-cam strips, speaker-check frames), `clips/` (downloaded clips and the two VOD sections), `frames/`, `asr/` (wav, txt, word-timed JSON for the on-disk and new clips), `tools/` (scripts), `vod-hits.txt`, `logtable.md`, `loud-known.txt`, `assemble.sh` (rebuilds this file from `hunt-head.md` + `hunt-body.md` + the log table).
