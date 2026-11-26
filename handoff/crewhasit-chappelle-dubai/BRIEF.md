# BRIEF: The Crew Has It x King Bach, "Dave Chappelle denied entry" (Onyx sample)

## ▶ STATUS 2026-11-26: FINAL READY
V1 built in the Scott Clary YouTube style, QC'd, copied to Exports (`crewhasit-chappelle-dubai.yt.final.mp4`, 39.25 s). Not sent: the email session sends it.
RUN.md has the decisions log and the open items.

## The prospect and the yes
- The Crew Has It: Gianni Paolo + Michael Rainey Jr. (Power franchise actors), YouTube 361K subs, Instagram @thecrewhasit 323K followers.
  Weekly 54-70 min episodes, studio set; sponsors in Ep. 107: PrizePicks, Nick's pouches, Hall Pass candy, Square, Uncommon Goods, Hims, Fabletics.
- Yes from Gianni, 2026-11-25 19:41 UTC: "Yes you can use!" (no conditions) for the YouTube Short `-cFtTORhd6U`.

## Platform pick (PLAYBOOK § 0): INSTAGRAM-FIRST
| | YouTube Shorts | Instagram Reels |
|---|---|---|
| Audience | 361K subs | 323K followers |
| Recent median | 13.2K (last 30 days, 10 Shorts); 19.3K (90 days, 34) | ~295K (newest 12 and newest 20 reels) |
| Best recent | 615K (YOUNG THUG HEARD HIS NAME ON POWER, 10-06) | 920K (10-13), 840K (11-03), 660K (11-11, King Bach ranking clip) |
| All-time best | 2.14M, 2.04M, 1.53M (early 2026) | not read |
| THIS clip | 20,976 views / 655 likes / 9 comments (94 s) = 1.6x their 30-day median | 113K views / 1,703 likes / 47 comments (93.5 s) = 0.38x their IG median |
The email named the YouTube Short, but the same cut is on their Instagram, which runs ~20x the YouTube median. Rule 2 decides:
Instagram is the priority platform. On Instagram this clip UNDERPERFORMED (0.38x median; their 14 s King Bach ranking clip from the same
episode did 660K and 4.1 % likes vs 1.5 % here): that gap is the reaction video's strongest line.
Sources: `research/uploads.json` (API, 359 uploads), `research/instagram.md` (reels tab, read 2026-11-26).

## The story (episode V5Hd3n7faRM)
The exact words and times live in SEQUENCE.md (v6, large-v3 slice reads in `work/cpu/slices.log` + `slices2.log`); the CPU-era quotes
that stood here are retired. In one line: in the UAE ("Dubai, Abu Dhabi"), at the F1 race's yacht after-party, they wouldn't let Dave
Chappelle on ("who is he?"); Bach had no pull, left the yacht and hung out with him; Chappelle only knew Bach from a Warriors playoff game
("who is this n**** three rows in front of me?"); Gianni's roast, the episode's own cold open: "I was on the yacht and Chappelle wasn't, and
I was three rows in front of him." Speakers: Gianni asks "He knew who you were?" (on camera in their Short); the hook's "No." is unattributed.

## Their Short (`reference/-cFtTORhd6U-permitted-short.mp4`): 1080x1920, 24 fps, 93.5 s, -16.7 LUFS, peak 0.0 dBFS
Cut from episode 2543.2-2683 (cross-correlation, `work/xcorr.txt`) plus the cold-open copy of Gianni's roast. The n-word is MUTED in
their audio (digital silence 2622.4-2622.7) and starred in the caption ("N**GA").

## Teardown: their Short vs ours
Lives in SEQUENCE.md ("Their Short vs ours"), kept there only so the two never drift.

## Facts check (GATE 5): only his own words go on screen
- ABU DHABI: he says "I was in Dubai, Abu Dhabi" (large-v3, both passes), a host then asks "What was your ass doing in Dubai?" and he says "I was at the F1 race" (the F1 race is in Abu Dhabi; the hosts tease him it was F2/F4, so "F1" stays OFF screen). The Abu Dhabi GP is held at Yas Marina Circuit (background only; "Yas Marina" is NOT on screen: he never says where the yacht was berthed).
- No year: nothing primary dates the party. A National gallery listing King Bach at an Abu Dhabi GP race day came only through a search summary: OFF screen.
- The Warriors playoff game and "three rows behind me": his anecdote, told as his.
- Other tellings: none found (web, YouTube, Instagram). Reposts: WhutClips YouTube "Dave Chappelle Got Turned Away From a Yacht in Dubai" 1,207 views (11-12); @thebfacollective IG repost 126 likes. Fresh everywhere.

## Name-tag credential (checked 2026-11-26)
- KING BACH = the most-followed person on Vine: Guinness World Records "Most followers on Vine", 16,066,791 as of 26 July 2016
  (https://www.guinnessworldrecords.com/world-records/413766-most-followers-on-vine.html); Tubefilter 2015-03-16: passed Nash Grier
  with ~11.33M (https://www.tubefilter.com/2015/03/16/king-bach-most-followed-vine/). Phrase it as a past record ("most-followed person
  on Vine"), never as a live count.
- Chappelle as a Warriors courtside regular (supports the playoff beat; B-roll candidates, other creators' clips, <= 3 s, flag): "Dave
  Chappelle supports the Golden State Warriors" (2015, k-7gtHtYjQo), Chappelle + Chris Rock at Warriors vs Celtics (2022), Sporting News
  "Dave Chappelle and Matthew McConaughey were in the house for Lakers-Warriors" (2023, cvuxSy8d3Yg).
- "that clip again" (2640-2643) is a callback to a running joke at episode 2:26: "He wants the clip, that's what he wants... let's give him
  the clip" (CPU small.en read). Left out of the cut.

## Premise proof (strangers care about "security didn't recognise a star")
YouTube (API, 2026-11-26): J.Lo Denied Entry at Chanel 2.73M (41 s) · Paul McCartney DENIED at Grammy Party (TMZ) 1.86M · Rafael Nadal
stopped by security 1.25M · George Michael Denied Entry To His Own Concert 805K (43 s, 2026-02) · Lewis Hamilton (ESPN) 218K · "When
Rappers DON'T Get Recognized" 32.2M. Instagram premise proof: `research/instagram.md` round 2.

## Downloads (logged)
| File | Source | Size |
|---|---|---|
| `reference/-cFtTORhd6U-permitted-short.mp4` | YouTube, yt-dlp f137+140 | 26.0 MB |
| `source/ep107-V5Hd3n7faRM-audio.m4a` | YouTube, bestaudio | 68.5 MB |
| `source/ep107-rss.mp3` | the show's podcast RSS (megaphone MALM5558950843), same length as YouTube (4233.5 s) | 169.7 MB |
| `work/raw-orig/ep107-sec2510-2695.*` | YouTube section 2510-2695 s, best <= 2160p | pending |


## Fetched stills and clips (builder, 2026-11-26)
| File | Source | Licence | Size |
|---|---|---|---|
| `ref/stills/chappelle.jpg` | Wikimedia Commons "Dave Chappelle at Preamiere of "Dave Chappelle In Real Life" (2) (cropped 2).jpg", Kolby Ari (AirEdits), 2025-08-08, via en.wikipedia Special:Redirect/file | CC BY-SA 4.0 | 1280x1706 (original 1563x2083; sharp at full size, checked) |
| phone shot | the episode's own 4K section (`raw4k/`), Bach holding his phone to the camera at episode ~2652-2656 | the show's footage (permission yes 2025-11-25) | 4K crop |
