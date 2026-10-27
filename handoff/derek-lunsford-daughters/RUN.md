# RUN — "Why Derek Lunsford Just Wanted His Daughters After Losing Mr. Olympia 💔" (Abundance Wisdom short)

## ▶ STATUS: resume here (2026-10-26 ~19:40) — RAW SEQUENCE PLACED, waiting on his review
- **ABW10 › bin "Derek Daughters" › "Derek Daughters - raw cut"** (clone of "Onyx reaction template (empty)", 1080x1920
  60 fps): **52.27 s**, V1/A1 33 clips, V2 4 picture-only covers, 7 beat markers. Readback (`premiere/readback.tsv`):
  0 flags (every in-point within one source frame, V/A identical, covers where planned). Active sequence restored to
  "Joe Appointment - raw cut" (the other session's, which was active). **Not saved** (he saves).
- His order (AW LESSONS 2026-10-24): he re-edits this raw cut → his direction video → code build. Nothing built yet.
- Open for him: (1) beat 2 — two of the brief's four "Derek only" lines are his WIFE; (2) beat 5's 2.2 s sigh (lock 6 kept
  it, the one exception to the no-gap rule); (3) the cold open's own 0.3 s white flash under "nobody has a chance";
  (4) beat 1's picture is Derek + Andrew Jacked posing B-roll (cropped on Derek); (5) card "BACKSTAGE" — beats 5–7 are a
  hotel-style corridor, not obviously backstage.
- Re-place from scratch: `premiere/clear_ours.js` (this sequence only) → `resolve_beats.py .` → `plan_placement.py .` +
  the splits `DL-PRE_NobodyHasAChance@22.6 @25.667 @27.567 @27.867 JRN_TheJourney2026@4289.035` → set every V2 row's
  `to_src` to null in placement.json (see Log) → `place_sequence.py` → `premiere/place.jsx` → `premiere/readback.js` →
  `premiere/restore_active.js` (edit the name if his active sequence changed).

## Sources (`raw/`, originals in E:\Bullshit Folder\Henry)
| Code | File | Original | Format |
|---|---|---|---|
| DL-PRE | `DL-PRE_NobodyHasAChance.mp4` | `_NOBODY HAS A CHANCE_ Derek Lunsford RAW _ UNFILTERED.mp4` | 1920x1080 30, 55:21 |
| JRN | `JRN_TheJourney2026.mp4` | `The Journey _ 2026 Mr Olympia.mp4` | 1920x1080 23.976, 1:17:46 |
| NW | `NW_HomieGotThird.mp4` | `Nick Walker Trolls Derek Lunsford at Champion Seminar + …mp4` | 1920x1080 29.97, 17:32 |
| IL | `IL_HomieGotThird_alt.mp4` | `NICK WALKER CALLS DEREK LUNSFORD A “WUSSY”…mp4` | 1920x1080 30 (fallback, unused) |
| OL | (placed from the original) | `2026 Mr. Olympia Finals Official Footage.mp4` (= his `_2` download: same title + 4628.85 s) | 1920x1080 29.97, 1:17:09; `raw/OL_Finals_2026.mov` = audio 3985–4015 |
Transcripts: `transcript/words.json` (WhisperX, all four + the OL window; batches in `win/b1..b3`), `transcript/OL_full.txt`
(faster-whisper, whole finals), isolated re-ASR `win/snip/`. Tools: `tools/asr.py`, `tools/f0_words.py`, `tools/crop_sheet.py`.

## Ranges (source seconds; `edl.json` / `placement.json` = the exact frame-snapped values)
| Beat | Src | Timeline | Pieces | Words / notes |
|---|---|---|---|---|
| 1 | DL-PRE | 0.00–6.62 | 21.43–26.85 · 27.10–28.30 | "you're never going to beat me if I have anything to do with it. If I'm still around, if I'm competing every single year, nobody has a chance." Cold open (lock 5). Crop on Derek through the Andrew B-roll (framing.json). |
| 2 | JRN | 6.62–11.77 | 1907.99–1909.26 · 1911.03–1912.98 · 1913.87–1914.89 · 1918.88–1919.79 | Derek "Are you rooting for daddy?" · WIFE "Are you gonna watch daddy this weekend?" · WIFE (likely) "Hi, baby." · Derek "I love you." Dropped: the daughter's "Dada" (1916.5–1916.9) and Derek's "Hiii" (1917.3–1918.1). |
| 3 | OL audio | 11.77–15.62 | 3993.86–3995.46 · 3998.53–3999.86 · 4009.07–4009.99 | "the third place award, … the check for $100,000, … Derek Lunsford." Picture = 3 JRN covers at OL + 112.10 s: 4106.27–4107.89 · 4110.65–4111.98 · 4121.20–4122.13 (top three from behind, crop on Derek, teal trunks; he steps forward on his name). |
| 4 | NW | 15.62–21.78 | 194.59–196.86 · 198.47–202.37 | "I said, homie got third. And he's in his posing routine throwing threes up for third, boy." Cut between: 0.8 s near-silence + a room voice "yeah, that's". Picture: Nick 1.5 s, then OL cover 3562.19–3566.86 (tl 17.12–21.78), "threes" on the 3 sign (OL 3565.0). |
| 5 | JRN | 21.78–28.80 | 4286.95–4293.97 (whole) | "Going from champion to third, just processing. [sigh, 2.2 s] Processing, it sucks." Walking with his wife until 4289.035, then the corridor shot. |
| 6 | JRN | 28.80–49.03 | 4368.99–4372.79 (2 pcs) · 4387.47–4388.87 · 4389.72–4403.76 (6 pcs) · 4405.48–4412.59 (4 pcs) · 4413.37–4414.48 | "Just thinking about my daughters at home. Missing them." / "Your loved ones sacrifice with you. My daughters, even though they're young, maybe don't really know any better, their daddy hasn't really been around as much as he could have been the last two months, and obviously not at all this week." / ADD (runtime was 47.9 s < 50): "Just looking forward to getting back and spending time with them. It's all I can think about, right away when my name was called." |
| 7 | JRN | 49.03–52.27 | 4425.50–4425.94 · 4426.09–4428.89 | "But as soon as I came off stage, I was like, I just want to go be with my daughters." Hard cut after the "s" of "daughters" (4428.86). |
Trims if he wants it shorter: beat 6's first line (−2.2 s), beat 4 (−6.2 s), the beat 6 add (−5.7 s).

## Locks
1. **No child on frame: PASS.** FaceTime 31:37–32:00 = Derek + his wife in bed, the phone's BACK to camera (`proof/jrn_facetime_full.jpg`).
   **Child's voice: the daughter is audible on the call** ("Daddy is in the blocks" 1906.5–1907.9 and "Dada" 1916.5–1916.9,
   pyin 300–475 Hz): both left OUT; Derek's "Are you rooting for daddy?" ends in a rising 230 Hz tail (1909.0–1909.2; WhisperX
   wrote it as "No.", the isolated re-ASR heard nothing there) — kept, for his ear. **Speakers (pyin + lips, `proof/jrn_facetime_lips_1910.jpg`):**
   "Are you gonna watch daddy this weekend?" = his WIFE (237–275 Hz, her mouth moves); "Hi, baby" = most likely his wife (~200 Hz).
   The brief lists all four as Derek's.
2. **Three fingers: FOUND, real footage.** OL 59:24.8–59:25.6 (3564.8–3565.6), walking off at the end of his finals routine,
   right hand up in the "3" sign; commentator 59:23.94 "Nice, throwing up three." (`proof/ol_threes_zoom.jpg`, `proof/b4_cover_v3.jpg`).
3. **The call is Derek's: CONFIRMED** by alignment, not by ear: JRN's arena audio = OL's broadcast + 112.10 s (envelope xcorr
   0.755); OL's feed reads "…present it to your third place finisher, Derek Lunsford." (WhisperX + faster-whisper agree), JRN's
   arena copy of the name is crowd-blurred (ASR "Dan Musgrave"). So beat 3 AUDIO = OL (the fallback), PICTURE = JRN.
4. **NW: no host on screen** 3:11–3:22 (Nick at the seminar table); a small "@BODY.BUILDING UPDATED" watermark sits left of his
   mic, outside the 9:16 crop. The swear ("oh, shit", ends 193.28) is before the cut (in 194.59). Nick's words are "I said,
   homie got third" (no "like" in either ASR; onset 194.62 after 1.3 s of quiet). IL unused.
5. **Cold open: KEPT.** No music (its pauses −47…−72 dB vs the interview's −26…−54), no burned-in captions; the same take as
   24:49.9–24:56.8, whose picture is a BTS TV Zoom split-screen. Picture under the line = Derek + Andrew Jacked posing B-roll
   (20.9–27.87, cropped on Derek) and the source's own flash transition 27.57–27.87 (0.3 s white) before "a chance".
6. **Beat 5 sigh: KEPT** — beat 5 placed whole (no tighten): the 1.6 s breath/sigh (4290.2–4291.8, −38…−52 dB, unvoiced) plus
   the repeated "processing, it".

## Checks
- Crops: `proof/crops_v2.jpg` (first / mid / last frame of every row as framed): Derek in every speaking row; framing.json
  fixes the detector's wrong picks (Andrew ×2, his wife, Nick/Samson ×3).
- Words: A1 rebuilt from the readback (`check/a1_rebuilt.wav`, 53.07 s pre-fix) re-transcribed (`check/a1_asr.txt`): the brief's
  words in order; gaps > 0.22 s = crowd under the announcer, comma pauses ≤ 0.34 s, the beat 5 sigh, and the beat 4 room voice
  (cut in the final placement).

## Log
- 2026-10-26 ~18:00: brief received in this side session; yt-dlp blocked (one try); drive search found only OL.
- 18:06–18:18: he downloaded NW, IL, DL-PRE, OL (again) and JRN into Henry; copied to `raw/`; transcribed (WhisperX).
- Locks worked (above); beats.json → resolve_beats → plan_placement (+ splits, framing.json) → crop sheet → place_sequence.
- First placement: beat 3 covers 1 + 3 came out wrong ("end re-pinned to 10.32 / 3831.03"): a cover whose `to` is a NUMBER
  gets `to_src`, and place_sequence re-pins its end from the V1 footage's in-point — meant for a cover ending on the covered
  footage's own cut, wrong for covers synced to another source. Cleared (`clear_ours.js`), `to_src` nulled in placement.json,
  re-placed. Then the re-ASR found "yeah, that's" (a room voice) in beat 4 → beat 4 piece 2 in 198.45, cover re-timed, re-placed.
- Not saved. Active sequence restored after each pass ("Joe Appointment - raw cut").
