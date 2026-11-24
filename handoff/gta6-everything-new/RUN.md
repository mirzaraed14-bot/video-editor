# RUN — gta6-everything-new (Affan Afterhours long-form 28, FACELESS)

## ▶ STATUS: resume here
- **State (19 Nov 05:32 PKT): v2 REBUILT after a Premiere crash and SAVED by him (ABW11.prproj 05:32:02, file verified to contain "GTA 28 - Everything New v2"); waiting for his review.** ABW11 › bin "GTA 28 - Everything New" › sequence **"GTA 28 - Everything New v2"** (8:35.6, 1920x1080 60.00 fps, linear compositing off). **629/629 clips verified frame-exact** (readback + END), his active sequence (v1) and playhead restored. **Saved 05:32.** v1 ("GTA 28 - Everything New") is untouched as he reviewed it.
- **v2 = his review notes:** 13 false starts removed (`work/cut/subphrase.py` piece-by-piece ASR → `work/cut/tighten.py`), pauses capped 0.30 s / 0.16 s (VO 535.6 → 512.0 s), face cams unblurred and labelled on the cam (`footage/v2/`, `tag-xqc-*-mid`, `tag-kai-cam`); chat + viewer counts still blurred. Spot composites: `work/preview/v2check/v2check.jpg`.
- **Next action:** his review of v2 → notes → fix at the source → place as a new sequence (never `--rebuild` a sequence he touched). Then phase D + LESSONS.

| | | |
|---|---|---|
| format | long-form YouTube 16:9, FACELESS VO over streamer gameplay | VO only (no camera); footage 1920x1080 60 fps (Twitch) / 30 fps (IGN) |
| lane | Premiere | brief: ABW10 › new sequence "GTA 28 - Everything New" (see Flags: ABW11 is the open project) |
| preset | `presets/youtube/affan-afterhours/EDITOR.md` + facecam `CREATOR-HAND.md` / `HUMOR.md` CORE grammar only (no face numbers) | NOT `youtube/default` |
| raw | `raw/TX01_MIC034_20261118_233332_orig.wav` (784.98 s, body) + `raw/TX01_MIC035_20261118_235544_orig.wav` (140.34 s, titles / IGN fix / first-jobs beat / conclusion); 48 kHz mono f32 | originals untouched in `X:\Recordings\Afterhours\` |
| script | `X:\Claude Projects\GTA 6\research\streams-2026-11-18\VIDEO-A-SCRIPT.md` (v1.8) + `VIDEO-A-READ-ALOUD.md` + `VIDEO-A-VO-ASSEMBLY.md` + pickups | footage in/outs: `verify/VERIFY.md` wins over the script table |
| constraints | silence (ffmpeg -f null / frames only) · nothing on C: · no Fable agents, Sonnet executors · never move his playhead · he exports (never exportAsMediaDirect) · mute ALL streamer audio · never show streamer face/chat/viewer counts · source tag on every clip · no nudity · gore = fast cut or blur · on-screen quotes exact | |
| started | 2026-11-19 00:05 PKT | he plays GTA 6 at 09:00 PKT |

## Steps
| # | Step | Status | What it produced / why not |
|---|------|--------|----------------------------|
| 1 | Intake | done | both WAVs copied to `raw/` (sizes match originals) |
| 2 | Rough cut (VO assembly) | done (1 joint report pending) | per-burst faster-whisper + wav2vec2 realign (`work/cut/bursts-rec*.json` → `transcript/words.json`; WhisperX original kept as `words.whisperx.json`); 133 segments, VO 8:54 + 8 × 0.2 s colour bars; polish-boundaries + measured tail fixes (numerals collapsed); dead-air gate PASS; slice re-ASR of every segment (`work/cut/slice-asr.json`); fresh-eyes completeness pass: 1 fix (seg 50 → last take) |
| 3 | Audio polish | done (baked) | `workflows/voice-gain.py` on the kept speech: −23.8 LUFS → **+7 dB** into a −6 dBFS limiter (ffmpeg alimiter, latency-compensated), baked into `audio/vo/rec1-polished.wav` / `rec2-polished.wav` (A1 plays these; the raws stay untouched). Assembled VO measures −18.3 LUFS, peak −5.6 dBFS, 1.2 % of samples touch the limiter. Baked rather than Premiere clip effects: one deterministic file, nothing to drop on a rebuild |
| 4 | Color grade | skipped | channel rule: no grade (facecam PLAYBOOK step 4); the streamers' own game capture is the look and the evidence |
| 5 | Graphics | placed (V2-V7), verified | 8 section titles (1/7…7/7 + reviewers), 8 counter chips, 51 source-tag spans (xQc / Kai Cenat / IGN's review, 'not footage of this claim' on reviewer fill, 'radio audio', 'early errand'), 20 quote/reviewer cards, 8 labels (REPORTED / HEARD / UNVERIFIED), 34 pointer boxes from measured tooltip boxes, 21 static cut-zoom punch-ins (his razor + static scale), 8 colour-bars turns. PIL → ProRes 4444 alpha; statics as long qtrle movs |
| 6 | SFX | placed (A2-A5), verified | 113 cues from `work/plan_audio.py`: A3 graphics layer (title whoosh + low hit, card pop, label/pointer tick, bars static), A4 picture-synced game feel (sirens, radio static, cash, phone taps, keypad, plunger, nail gun, car pass-bys), A5 quiet city ambience under the drive montages; levels from measured true peak |
| + | Music | placed (A6), verified | A6: Loungin (open + close), First Born, Take a Ride, Brooklyn, Weeping Cherry Tree, On Cruise Control, El Camino a Madrid; −31 LUFS under the open/close, −34 under explanation; out at each bars turn and the first 1.5 s of every cut zoom; 31 click-free runs in `audio/music-cut/` |
| 7 | Review | **waiting on him** | on ABW11 03:09:57, 553/553 verified |
| 8 | Export | — | his (never exportAsMediaDirect) |

## The bar to beat
Newest long-form `gta6-complete-guide` (6 Nov, 9:14, 105 views), face-cam. This one is the channel's first faceless,
gameplay-led long-form: the bar is retention through the picture (brand-new GTA 6 gameplay wall to wall, the evidence on screen for every line).

## Flags
- **Project:** ABW10 is not open in Premiere; ABW11 is (43 sequences, his live project, also used by the Urdu Editor). Precedent: CA-015 built in ABW11 because ABW10 wasn't open.
- Job files are written in the MAIN checkout (`projects/` is gitignored), per the brief.

## VO assembly (what the recordings actually held)
- **Rec 1** = the whole body AND the section titles 3-6 inline ("Number three, your phone tracks you", …, "Now what the reviewers say"); titles 1-2 were recorded as pickups after title 3 ("Number two, the cops know what you look like", "Number one, in your neighborhood, there are rules"), placed at their sections. Asides to "Claude" (253-276 s, 748-759 s) and the wrong cockpit/limbs line (730.99 s on) are dropped.
- **Rec 2** = the corrected IGN sentence, the "Seven things" line, the first-jobs beat (no spoken title) and a conclusion with a subscribe ask. **No section titles** (the assembly map expected them there).
- **Order:** the jobs beat is the 7th thing, placed AFTER "Number six, your car holds your guns" (not after money as the pickup sheet suggested), so his spoken numbers stay true; on-screen counters 1/7…7/7.
- **Kept ad-libs (his):** "…and iShowSpeed" (unverified that Speed streamed it: never tagged or shown), "so make sure that you subscribe", "I'm gonna make guides, I'm gonna make a what-if series explaining what is different from GTA 5", and the conclusion. No `[YOUR LINE]` reactions were recorded.
- **Opening last line:** Rec 1 "But for now this is what the first players found on the game's own screens." + Rec 2 "Seven things, then…" (Rec 2's own read has a stray "and on"; Rec 1's "But" bridges his what-if ad-lib).

## Delivery note (final, 19 Nov 03:20 PKT)
**Defaults taken (each is one word to change):**
1. **Project:** built in **ABW11** (the project open in Premiere) as a new sequence + bin "GTA 28 - Everything New" (1920x1080, 60.00 fps; **linear compositing switched OFF** on this sequence so the scrims/shadows read as designed). ABW10 was not open, and opening it would have swapped the project in front of him. **Unsaved: Ctrl+S.**
2. **Structure:** his titles were in Rec 1 (not Rec 2). The first-jobs beat is the **7th thing, after the car**, so his spoken "Number five / Number six" stay true; counters read 1/7…7/7; the jobs beat has no spoken title (on-screen title only).
3. **His ad-libs kept:** "…and iShowSpeed" (not verified that Speed streamed it; no Speed footage or tag is shown), "make sure that you subscribe" (opening and conclusion), "I'm gonna make guides… a what-if series…", and his whole conclusion ("10 out of 10… game of the year"). The script said no sign-off/no ask; his recording wins.
4. **No `[YOUR LINE]` reactions were recorded**, so nothing was padded: runtime ≈ 8:59 (above the 8:00 mid-roll floor).
5. **Date-bound lines:** "it releases for me about nine hours from now" and "I'm nine hours away" are only true if it goes up before his 09:00 unlock.
6. **Spoken vs screen:** he says "his locker" (the popup says LOCKUP) and "towards" (card shows the game's "toward"); cards always carry the game's exact text.
7. **Gore (IGN I3a):** a **fast cut**, the shot ends 0.35 s after the burst begins (2:12:10.467 → out 2:12:10.817), no slow-mo, no blur. The scoped shot (I3b) is not used.
8. **Covers:** every streamer cam, chat and viewer count is a baked frosted-blur panel in the footage masters (`footage/QA.md` per clip). Shop/menu rows keep the game card visible (cam-only cover). K5/K6 (violence in the street) are shown as tooltip crops on a dark matte.
9. **Profanity / nudity:** the clerk clip ends before the expletive subtitle (it appears at 2:58:18.18 on the frames, not 2:58:19.5 as VERIFY said); the card shows only "…as long as it's under a thousand…" plus an UNVERIFIED label on the link; tenant and sink subtitles and the "fck" text notice are blurred; every nudity / boxers window is cut before its first flagged frame.
10. **Audio:** no streamer audio anywhere (the footage masters carry no audio stream). Voice = static +7 dB into a −6 dBFS limiter, baked into `audio/vo/*-polished.wav` (swap in his own Enhance Speech bounce if he wants). Music = his four Epidemic beds (Loungin, First Born, Take a Ride, Brooklyn) + Weeping Cherry Tree, On Cruise Control, El Camino a Madrid, one per section, out at each colour-bars turn and for the first 1.5 s of every cut zoom. SFX from Epidemic.
10b. **Mix:** VO −18.3 LUFS mono; as Premiere sums it to both channels the full mix reads about −15.3 LUFS (his masters ≈ −17), music ~18 LU under the voice. Ride A1 or the master if it feels hot.
10c. **K9 (salon):** the price row is hidden under the chat blur (chat words showed in ~70 % of frames); "Not enough cash" stays readable.
11. **Clearance** (his call, unchanged): the whole picture is xQc's, Kai Cenat's and IGN's broadcasts, credited on screen; credit and muting are not permission.
12. **Not this session's job:** title, thumbnail, export (he exports).
12b. **Bin housekeeping:** the GTA 28 bin also holds the unused 96 kHz `audio/sfx/*.wav` items beside the `audio/sfx48/` ones with the same names (an import before the restart); safe to delete. If any music bed sounds wrong or silent, tell me: it would be re-imported under a new name.
12c. **Not machine-verified inside Premiere:** the in-app frame grabs failed after his restart, so how the overlays look in Premiere is verified by the offline composite + his eyes; every graphic item reads the same alpha interpretation as his shipped overlays.
13. Housekeeping: a stray `X:\tmp_vo_lines.txt` (a transcript dump of mine, at the drive root) is safe to delete; the permission check blocked me from deleting it.

## Premiere log
- 02:27:59 backup `premiere/backup/ABW11.prproj.20261119-022759.bak` (3.53 MB, the file as saved on disk).
- 02:28 pilot window 1: bin "GTA 28 - Everything New" created, 15/38 files imported, then the bridge dropped (bridge_unavailable) → stopped before creating anything; his active sequence ("Sequence 15") and playhead (ticks 1955923200000) verified unchanged. Retry-on-ping added to `run_window.py`.
- 02:30 held: free commit 0.5 GB / free RAM 1.2 GB (three other sessions rendering Shorts; Premiere 2.8 GB). No Premiere writes until commit ≥ 6 GB (the 14 Nov crash condition).
- 03:02 he saved + restarted Premiere (31 GB private freed); SFX resampled 96/192 kHz -> 48 kHz (`audio/sfx48/`) to lighten the import.
- 03:07 build attempt: imports 209/209 OK, then the placement scripts (34-41 KB) exceeded Windows' 32 KB command line -> chunked to 40 rows per call.
- 03:08-03:09:57 `--rebuild`: 16 placement calls, all "laid N/N"; readback 553/553 match, END = planned end; his active sequence + playhead unchanged. In-window `frame` grabs failed host-side (QE exportFramePNG after the restart): not retried.

## Final QA (offline composite of the placed plan, 03:20 PKT; `work/preview/final/preview-final.mp4`, `QA-round2.md`)
- Clean: no face / chat / viewer count / nudity; one source tag on every gameplay clip, never over game text; all 21 zooms without black edges and with their evidence whole (except K12, below); 8 section turns correct; zero same-track SFX overlaps; V1 gap-free; fade ends fully black.
- Mix: full −15.3 LUFS (VO summed to both channels), true peak −4.0 dBTP, LRA 3.2; music −33.5 LUFS (18.2 LU under the voice); SFX peaks 10.9 dB under the voice peak.
- Minor, left as is (his timeline, his review first): K12 zoom (≈307.6-311.7) crops the money HUD (the VO there is about the withdraw menu, which is whole); the q-K10a card (≈326.9-330.8) covers the clerk's "For you? Oh yeah," subtitle (the card IS the quoted line); the F11 pointer's top edge grazes the "Unlike" row (≈248.9); K7b's price row is half-cut in the source; the V7 tag stays bright over the last ~0.2 s of the closing fade.
- 04:22 Premiere restarted again (crashed once while reopening); 04:35-04:37 v2 window: 42 import batches of 5 (commit 35 → 24 GB over 21 new H.264 masters: ~0.5 GB each), 16 placement calls all laid N/N, readback 629/629 + END; v1 and his playhead restored.
- 05:27 Premiere crashed and lost the unsaved v2; 05:29-05:31 v2 rebuilt from the plan (`run_window.py --run`), readback 629/629 + END, his active sequence + playhead restored. My scripted save was refused by the permission classifier: HE must press Ctrl+S.
- 05:32:02 he pressed Ctrl+S; the saved ABW11.prproj (3.99 MB) contains the v2 sequence (read-only gunzip check).
