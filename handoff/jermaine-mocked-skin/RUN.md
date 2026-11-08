# RUN — jermaine-mocked-skin (Abundance Wisdom Short: "Why Michael Jackson's Brother Mocked His SKIN 💔")

## ▶ STATUS: resume here
**2026-11-07 ~23:10: OPENING ADDED on his yes — waiting on his next direction.** Sequence **`Jermaine Jealous - raw cut`** (same sequence, re-laid after a read-back proved it unchanged), ABW10, active, **47.15 s**: V1 26 + A1 26 + V2 5 + 10 markers. Read back = plan: 0 mismatches, no holes (`premiere/readback_v3.json`, `premiere/plan_v3.json`, `premiere/make_v3.py`, `premiere/place_v3.jsx`). Not saved, not exported.
- New clips F1-F6 from `seq_src/diss_458_476_open.mov` (picture as uploaded; left channel to both, the Today lead-in is phase-inverted, corr −0.98; "Perfectly okay, yeah" +6 dB). Motion per shot from YuNet faces. Joints measured frame by frame against the mezzanine (`premiere/exact_cuts_v3.py`): every joint lands on the shot change.
- Mono-sum per line: −23.2, −22.0, −22.1, −21.5, −20.5, −22.6, −22.3, −22.4, −23.8, −24.0 LUFS.
- Words: timeline audio rebuilt from the read-back and transcribed (large-v3 on CPU because another session held the GPU, `proof/seq_v3/asr_cpu.json`): every line in order. Uncertain words to settle by ear at caption time: "went **out** front" (WhisperX on the upload) vs "went **up** front" (the detail's burned-in caption; the CPU pass heard only "went out"), and "**We** put him" (WhisperX, and the context) vs "You put him" (CPU pass).
- `proof/frames_v2/opening.png` = emulated composite of the opening. Its stray-looking frames at clip edges are the emulator (ffmpeg `-ss` lands on the next frame), not the sequence.
- Stage footage at line 1 and at "lead singer first" are two ranges of the same Victory Tour clip (461.64-462.66 and 459.6-460.9).
- The 37 s version is not kept as a sequence: `premiere/place_v2.jsx` rebuilds it into an empty sequence.

## (previous) ▶ STATUS
**2026-11-07 ~22:45: V2 BUILT after HIS REVIEW 1 (BRIEF.md) — waiting on his next direction.** Sequence **`Jermaine Jealous - raw cut`** (bin `Jermaine Mocked Skin`), ABW10, active, 1080x1920, 29.97 fps, **37.07 s**: V1 20 + A1 20 + V2 5 covers + 7 markers. Read back = plan (`premiere/readback_v2.json`, plan `premiere/plan_v2.json`, generator `premiere/make_v2.py`, placed by `place_v2.jsx`). His own edit `Jermaine Mocked Skin - raw cut` (29 clips, `premiere/his_v1.json`) is UNTOUCHED. Not saved, not exported, no captions/SFX/music/grade/zooms/CTA.
- His 13 V1 + 3 V2 clips are re-laid at his in/outs, Scale and Position (they carried no effects, speed 1). His 3-frame hole at 0 closed; C7b/C7c photo in-points slipped to 501.4 (past the source's dissolve ghost).
- New: L3 `_MLtSCBOQbU` 188.22-194.82 (La Toya on camera; 4 pieces, pauses cut; burned-in "LA TOYA JACKSON" lower third crops to "TOYA JACKS" for about 2 s). L4 `eQrYM_RKKpA` 71.48-75.56 (3 pieces). L4 picture: Jermaine close (cover, same show) → Jermaine wide, lips in sync → Michael adult, Victory Tour (cover). Own picture under L4 is a childhood photo and home video, so covered. Snoop Dogg is on set in that shot: it reads as his GGN show, about 2013 (inferred: "Double G News" backdrop, "Reincarnated" promo).
- Audio baked into new mezzanines (originals untouched): UCLA +26 dB (`ucla_official_plus26.mov`, it sits at −47 LUFS), L4 −7 dB (`detail_060_092_minus7.mov`, runs hot, source peak +0.4 dBFS), Today lines left channel to both (`detail_428_496_Lmono.mov`, stereo inverted, corr −0.93). Mono-sum per line now: −21.5, −20.5, −22.6, −22.3, −22.4, −23.8, −24.0 LUFS.
- Checks: rebuilt timeline audio transcribed before the left-channel swap (same in/outs): all 7 lines, in order (`proof/seq_v2/transcript/words.json`). Composite sweep at 2 fps plus every cover edge (`proof/frames_v2/sweep.png`, `key_frames.png`, emulated from the read-back values because Premiere's `frame` failed): no child on screen, no black bars. Sweep was taken before the rebuild; only the photo in-points and audio changed.
- **Open:** title (no skin content left); the photo crop shows two adult men, not necessarily Michael; line 5-6 and L4 are a later show than the 1991 denial (flag below still stands).

## (previous) ▶ STATUS
**2026-11-07 ~21:25: SEQUENCING PASS DONE — waiting on Affan's creative direction.** Nothing saved, nothing exported, no captions/SFX/music/grade/zooms/CTA.
Sequence **`Jermaine Mocked Skin - raw cut`** (bin `Jermaine Mocked Skin`, cloned from his empty `Onyx reaction template (empty)`) in the open
**ABW10.prproj**: 1080x1920, **29.97 fps**, **53.69 s**. V1 25 clips + A1 25 clips (one per spoken stretch, in script order, butt-joined),
V2 3 picture-only covers, 13 markers (one per line, speaker label as placeholder). Read back from Premiere 21:13: V1/A1 starts/ends = plan, 0 mismatches
(`premiere/readback.json`, plan `premiere/plan.json`, in/out table below). The sequence is his ACTIVE sequence (previous: Sequence 45).
Timeline audio rebuilt from the read-back in/outs and re-transcribed (WhisperX large-v3, `proof/seq_audio/transcript/words.json`): every line is there, in order.
A face-centring pass (Motion Position x on 21 clips from YuNet face centres, `premiere/upd.jsx`, values `premiere/upd.json`) was sent at 21:16; the bridge said
"unavailable" but it DID apply: re-read at 21:23, all 21 positions present (`premiere/readback3.json`). Composite check of ten times (emulated from the mezzanines with those
scale/position values, `proof/frames/composite_emulated.png`): faces framed, no black bars, covers in place. Premiere's own `frame` export failed ("ExtendScript execution failed via
CEP evalScript()", QE) so no program-monitor grab was made. Script is LOCKED and was not re-sequenced.

## Things Affan must know (also in the final message)
1. **Provenance of lines 7b/7c and 8.** In the detail's 9:07 upload (`_MLtSCBOQbU`) the whole NBC *Today* interview is there (392-531 s). In it, after
   "That's ridiculous. Who has not had success in my family? We were the Jackson 5. Every song Michael sung on, I sung on. We helped build what's going on right now."
   Jermaine says **"It's not about that. It's about family, Brian."** The lines "They want to forget, but the Jackson 5 is what gave Michael and Janet the platform..."
   and "Michael comes from a family... when he hurts, we hurt" are **not in that interview** (no match in the full transcript). They sit in the detail's 11-min cut
   (`eQrYM_RKKpA` 456-466 and 484-492) under a *different, older-looking Jermaine* (studio, "NEMO HOES / DOUBLE G NEWS TEAM" backdrop) and under Michael b-roll. So the
   detail (and the 2.34M Short, `24sETkh1yQA`, same splice) joins two interviews into one answer to La Toya. I could not identify the second interview. Built as scripted, flagged.
   Real Today answer, if he prefers it: 487.96-498.7 ("...It's not about that. It's about family, Brian. That's the most important thing here.") and the peace lines
   505.1-531.8 ("we've spoken since all this has happened, and we're fine now... I said, Michael, we have to talk because family is very, very important. And I love you.").
2. **Lines 1-5 are not the *Today* anchor.** They come from a taped interview on a red-lit set (a woman interviewer on camera, Jermaine on the same set), which the detail
   cuts with Michael b-roll over lines 1-2. Line 7's lead-in ("on this program last September, your sister La Toya said...") IS the *Today* segment (anchor in New York, Jermaine
   in Sherman Oaks; whisper heard the anchor as "Brian", probably Bryant Gumbel, not confirmed). La Toya's clip is on camera in that segment (confirmed by frame; her lips + the
   "NBC NEWS TODAY" graphic just before).
3. **Words that differ from the script (real words used):** L4 keeps the real tail "as soon as I wanted to" (script ended "...getting to him.") and drops the leading "Basically,"; L5 is "phone
   **calls**" (plural); **L6 keeps La Toya's full sentence**, which ends "...jealous of Michael **or anybody that succeeds in that matter in the family**" (script ended at "Michael": the tail
   widens the claim, so I did not cut it; trim = last 3.3 s); L7 is "**sung**" not "sang", and its ellipsis removes "Who has not had success in my family? We were the Jackson 5."; L8's ellipsis
   removes "He comes from the Jackson family. And". L9 is word-exact ("This is hard." before it is excluded). Length **53.7 s** (script ~50; the two kept tails are +4.6 s).
4. **Pauses:** every gap inside a speaker > 0.35 s is cut, joints keep ~0.16 s (no gap > 0.25 s): L2 (0.64), L3 (0.64), L4a (0.44, 0.55), L4b (1.78, 0.48), L7c (0.54, 1.02), L8b (0.78), and
   **L9 (0.92, 1.24, 0.46: his solemn reading; call it back if he wants the weight)**. These are same-camera jump cuts.
5. **Pictures:** the detail's own cut shows **minors** under L7b/L7c (1970s Jackson 5 stage, 448-459 s) and **babies** under L8a (484-485.9 s). Replaced: V2 C7b/C7c = the adult brothers photo
   (1991, from the 9:07 upload 499-511 s) and V2 C8a = the older-Jermaine shot (reuse). L1/L2 picture is Michael b-roll (Bad era), as the detail cut it, not Jermaine's face. L8a after 485.85 and L8b
   are adult Michael b-roll (podium + flag, pointing). L7c's own picture is the older Jermaine from 458.96 (lip sync with the audio NOT verified; the audio may not be his). I looked at the first and last
   frame of every V1 clip and sheets at 0.5-1 fps of the picture windows; **a full frame-by-frame minors sweep of every clip was not run**.
6. **Line 9:** the official UCLA channel upload (`LVaEaDty5_Y`, max 854x476, no logo, darker than the detail's brightened copy) is used, not the detail's logo copy; Jermaine is small in the
   wide shot (4x upscale to fill the height). The statement continues at 140-146 s: "...And may Allah be with you, Michael, always." (earlier "not found in any transcript": it exists).
7. Audio is not level-matched between sources (different lines come from different uploads); nothing mixed.

## Sources (everything in `src/`, originals kept as downloaded; metadata `src/meta-*.json`)
| id | what | downloaded | used |
|---|---|---|---|
| `_MLtSCBOQbU` | the detail, "Jermaine Addresses ... DISS TRACK" 9:07 | **3840x2160 VP9**, 717 MB | L1-L5 (392-426 s), photo covers (499-511 s) |
| `eQrYM_RKKpA` | the detail, "Jermaine Jackson on Jealousy, Rivalry..." 11:00 | **3840x2160 VP9**, 770 MB | L6, L7a-c, L8a-b, C8a (428-496 s) |
| `LVaEaDty5_Y` | UCLA official, "Michael Jackson statement by Jermaine Jackson" 3:14 | **854x476 H.264** (best offered), 11 MB | L9 (65-75.4 s) |
| `tG-xOuIHUxk` | the detail's 595K Short | 720x1280 H.264 (burned-in captions + title) | audio reference only |
| `24sETkh1yQA` | the detail's 2.34M Short | 720x1280 AV1 | reference only (same splice) |
| `pjec7YVuhfo` | "Jermaine talks about Word to the Badd" 1:15 | 1280x720 H.264 | not used |
| local E: | Siblings (1080p60 = the same upload as `drcN-XJoWUc`), 2 other Jermaine files | not re-downloaded | Siblings scanned for line 9 (found at 507.7-520.4); the two others do not hold our lines |
`drcN-XJoWUc` itself was NOT downloaded: its line 9 is replaced by the official upload.
H.264 mezzanines for Premiere (Premiere cannot read VP9): `seq_src/detail_428_496.mov` (4K, crf 14, PCM), `seq_src/diss_388_512.mov` (4K, crf 14, PCM), `seq_src/ucla_official.mp4` (remux, copy).
Search results: `src/search-*.txt`.

## In/out table (source = original upload clock; sequence 29.97 fps, tl = timeline seconds)
| clip | tl | source (upload) | words |
|---|---|---|---|
| L1.1 | 0.000-3.604 | `_MLtSCBOQbU` 392.039-395.627 | Jermaine, the words are you changed your shade. Was your color wrong? |
| L2.1 | 3.604-4.605 | 395.627-396.658 | Do you resent the manner |
| L2.2 | 4.605-8.742 | 397.139-401.283 | in which your brother has changed his look so as to minimize his black features? |
| L3.1 | 8.742-11.678 | 401.363-404.286 | Reconstructed, been abducted, don't know who you are. |
| L3.2 | 11.678-14.748 | 404.766-407.809 | Did you feel that way? That he didn't know who he was? |
| L4a.1 | 14.748-17.484 | 408.870-411.593 | I felt that he was missing something. He wasn't |
| L4a.2 | 17.484-18.285 | 411.873-412.674 | communicating. |
| L4a.3 | 18.285-20.854 | 413.067-415.643 | And what was very hurting to me |
| L4b.1-3 | 20.854-23.156 | 419.494-420.089 / 421.709-422.670 / 422.990-423.740 | I wasn't / getting to him / as soon as I wanted to. |
| L5 | 23.156-24.825 | 423.740-425.410 | You mean he wasn't returning your phone calls? |
| L6 | 24.825-31.732 | `eQrYM_RKKpA` 435.684-442.589 | La Toya, on camera |
| L7a | 31.732-32.766 | 443.070-444.110 | That's ridiculous. |
| L7b | 32.766-35.135 | 450.777-453.158 | Every song Michael sung on, I sung on. |
| L7c.1-3 | 35.135-41.675 | 457.761-459.162 / 459.542-460.803 / 461.663-465.545 | They want to forget, but / the Jackson 5 / is what gave Michael and Janet the platform to do what they did. |
| L8a | 41.675-43.644 | 484.272-486.213 | Michael comes from a family. |
| L8b.1-2 | 43.644-45.479 | 489.536-490.256 / 490.877-491.977 | when he / hurts, we hurt. |
| L9.1-4 | 45.479-53.687 | `LVaEaDty5_Y` 65.016-65.696 / 66.457-68.739 / 69.820-71.241 / 71.541-75.364 | My brother, / the legendary king of pop, Michael Jackson, / passed away on Thursday, / June 25th, 2009 at 2:26 p.m. (HARD CUT at 53.687) |
V2 covers: C7b 32.766-35.135 and C7c 35.135-36.336 (photo, `_MLtSCBOQbU` from 499.6), C8a 41.675-43.277 (`eQrYM_RKKpA` from 461.0, older Jermaine).
Motion (all native-pixel scales): 4K full-frame 88.9 %; 4:3 *Today* box (L6, L7a) 96.8 %; photo 107.1 % (y 0.6026); UCLA 403.4 %. Position x set per clip from YuNet face centres (`premiere/faces.json`).
Edge frames: `proof/edges/edges.png` (first/last frame of every V1 clip, centre crop, before the face-centring pass).

## Premiere state / how to resume
- Lock: `premiere/plock.sh take "<why>"` ... `release` (mkdir lock). Scripts run through `lanes/premiere/premiere-bridge.mjs execute_extendscript` (see `premiere/*.jsx`, `/tmp` helper not kept).
- `premiere/create_seq.jsx` (ran 21:11), `premiere/place.jsx` (generated by `make_place.py` -> `make_jsx.py`; ran once, REFUSES a second run), `premiere/readback.jsx`, `premiere/upd.jsx`.
- **Bridge quirk seen today:** when Premiere is busy (another session's import, or a modal) the bridge says "MCP Bridge is not running / bridge_unavailable" even though the script DID run (first place run).
  Always read back before re-sending. Never re-send place.jsx (it refuses when the sequence has clips; to redo, delete the sequence's clips by hand or build a new sequence name).
- An "Import Files" modal that hung for ~1 min was on screen at 20:58 with the *MJ Showed His Mother* sequence active: that is the sibling session (mj-showed-his-mother), not this job (our only earlier calls were read-only).
- YouTube spacing slip: the UCLA official download started ~25 s after the preceding search request (rule: >= 60 s). No bot check followed. All other requests >= 60 s apart.

## Log
- 20:20 metadata for 4 ids; 20:25-20:40 downloads (eQrYM 4K, tG, 24sE); local WhisperX of the E: copies; 20:42 official UCLA found via search + downloaded; 20:47-20:56 three searches for the Today original,
  none better than the detail's 9:07 upload (which holds the Today interview in 4K); downloaded it + `pjec7YVuhfo`.
- 21:05-21:10 mezzanines, segments (`premiere/segments.py`, word-level, gaps > 0.35 s cut), plan (`premiere/make_place.py`).
- 21:11 sequence created; 21:12 clips placed; 21:13 readback + audio rebuild + re-transcription = script; 21:16 face-centring sent (unverified).
