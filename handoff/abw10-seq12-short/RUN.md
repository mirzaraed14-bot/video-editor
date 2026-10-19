# abw10-seq12-short — ABW10 · Sequence 12 (captions only)

▶ **STATUS: v2 DELIVERED 2026-10-20 (v1 was wrong, see below), waiting on the creator's review.**
Deliverable: `projects/abw10-seq12-short/abw10-seq12-short.srt` (28 cues, first at 00:00:00,000, 0 → 40.583 s, 60 fps grid).
`caption_qa.py` PASSES. Next: drag the .srt into ABW10 · Sequence 12 at 00:00, apply **"affanwizu yellow"**, baseline **y1385**.

## What went wrong in v1 ("bruv what are these shitty captions")
1. **Every clip on A1 is speed-changed (1.1x and 0.8x)**, and Premiere's `trackItem.inPoint` on a speed-changed clip is the
   real source in point DIVIDED by the speed (the 0.8x clip read in=250.04 s on a 215.7 s file; real = 200.03 s).
   `sequence_reference.py` pulled the wrong stretch of the take for every clip: 9.4 s of speech instead of 33.6 s, so v1
   captioned a quarter of the reel with the wrong words. **Fixed in the tool:** it reads `getSpeed()`, uses in × speed, plays
   the audio through `atempo` at the clip's speed, and aborts if a clip comes back short.
2. **The first cue sat at 4.13 s** (v1 started with an empty `@0.00 |`), and Premiere lays an .srt's FIRST CUE at the drop
   point, so every caption landed 4.13 s early. **Fixed:** v2 starts at 00:00:00; build.py now warns on any first cue after 0.
3. The picture rebuild gave each still ONE frame (so the frames under every later time were wrong and the chin read y1330).
   **Fixed:** stills are looped for their timeline length. Re-measured chin y1270 → baseline y1385.

## The job
- 1080×1920 60 fps. V1: 15 clips of `X:\Recordings\PBU\C1379.MP4` (118 %, punch-ins to 356 %) + 4 stills: the webp face
  (11.87), Siccîn 2's nun (14.30), Dabbe's commode scene (22.15), The Medium's night-vision shot (28.12). V4: two screenshots
  under "conjuring insidious". A1 voice; A2 the Undertaker theme; A3 a gunshot (neither in the transcript).
- Speech 33.6 s. Captions OFF over the four silent stills (11.87–13.36, 14.30–15.95, 22.15–23.28, 28.12–29.62).
- Film names resolved by re-decoding ur + en and checking the stills: **conjuring, insidious, siccin 2, dabbe the possession,
  the medium**. English kept English: horror movies, surface level, tutorial, **ball knowledge** (the slang), turkish, asian,
  commode, browser, type, thinking, screen ke through.
- The 0.2 s at 11.55 is a cut-off syllable before the still (the full "siccin 2" is at 13.38): left under the previous line.

## Better than the last one (CLAUDE.md learning loop § 5)
First reel with speed-changed clips: the rebuild now plays every clip at its own speed, so a sped-up or slowed reel is
transcribed exactly as it sounds in Premiere.
