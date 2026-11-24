# RUN: "Big creators' verdict on GTA 6" (AW Short)

## ▶ STOP 2 STATUS (PC, 24 Nov ~00:20 PKT): DONE and READ BACK. `Streamers Rated GTA 6 - v2` (id `adc7e9fc-7481-4e0c-9638-1d9818035ad0`, 27.633 s, V1-V7/A1-A3) is built; proof = `premiere/READBACK-v2.md`
- v2 picture re-made (15 head-locked Topaz face plates, 6 overlays in HIS slots, MMC T1/T2 transitions baked, AW captions at one base, cards, labels, scoreboard, CTA x2, SFX); A1 (his audio) untouched; his raw cut identical before/after; his active sequence + playhead restored. **Open for Affan:** Higgsfield trophy (placeholder, cost preflight), Moist's eyelid patches (source), "8.8 cut" read from his razor, overlays are 1080p (no H.264 4K), SFX/MMC audio not heard. **Never delete/rebuild v2 either now: any change = a new sequence.**
- (history of this block) was IN PROGRESS: every asset rendered under `premiere/v2/`
- **His edit (read, never touched):** `Streamers Rated GTA 6 - raw cut` (id `912b0f7e...`) is now 27.633 s, 41 clips, razors + scales (`premiere/v2/his_current.xml`, `his_readback.tsv`, `his_edit.json`). His cut keeps lines tight ("GTA 6 does it live up to the hype", Speed without "you should buy it", "I'd rate GTA 6 out of 10", "8.8", "It's right at the 9 mark" already tight at his razor: 59.867-60.550 then 62.250). His V1 gaps = his overlay slots: 1.5-3.267, 4.85-6.517, 7.3-9.15, 12.833-14.417, 17.917-19.417, 23.417-24.967.
- **v2 sequence EXISTS:** `Streamers Rated GTA 6 - v2` (id `adc7e9fc-7481-4e0c-9638-1d9818035ad0`), a clone of his state made under premiere.lock + quiet gate (41 clips = his 41; his sequence read before/after identical; his active sequence + playhead restored). NEVER delete/rebuild `raw cut`; v2 is ours (build window = `premiere/v2/win.py premiere/v2/build.jsx`, waits for him to be idle).
- **Faces (done, offline):** YuNet nose track, face fills 9:16 (nose held at (540,800)), kit Topaz recipe (Chronos + Iris x4 + Proteus 1x) on every piece: `premiere/v2/faces/`; P01 was redone (silent Topaz watermark on the first run; all 15 outputs checked, clean). Speed (cam inset 388x243, face 77 px) and Asmongold (inset 487x412) are limited by the cam resolution: show the 1:1 crops to Affan.
- **Captions (done):** AW engine (Gretaros, white + gold emphasis), ONE base for the whole video (top y~1082, just under the chin of the filled face), 46 captions from his cut's words (forced alignment): `v2/out/captions_v2.mov` (alpha). **Cards (done):** hook, labels x5, 8.8, 10/10, scoreboard, trophy PLACEHOLDER, CTA x2, SFX track.
- **MMC transitions:** `research/aw-gta6-reviews-2026-11-21/MMC-TRANSITIONS.md` (T1 radial zoom-blur + white flash = THE ONE, 13 cuts; T2 tinted flash, 2 cuts). Implemented in `premiere/v2/finalize_clips.py`.
- **Overlays:** sourced by a Sonnet worker into `overlays/` (LOG.md, MANIFEST.json); processed by `premiere/v2/prep_overlays.py`.

## ▶ STATUS: resume here (PC, 23 Nov ~11:30 PKT): STOP 1 DONE, the raw sequence is in his Premiere. SPEED (beat 2b) PLACED (11:58).
- **Sequence:** `Streamers Rated GTA 6 - raw cut` (id `912b0f7e-369e-4401-b47a-0517b6893c4f`, `ABW11.prproj`, bin `Streamers Rated GTA 6`), 1080x1920 @ 60, **39.867 s** with Speed (34.267 without). V1/A1 = 12 baked mezzanines (Speed 5.2-10.8 s + 8 beats), V2 = 3 gameplay cutaways, 19 markers. Speed = `raw/speed-day1-13500.mp4` 155.88-161.48 (his own day-1 stream), label ISHOWSPEED - DAY 1; placed by a guarded `--redo` (live sequence read back == READBACK first), so the sequence id changed. His active sequence (`Sequence 20`) and playhead restored by id, ticks identical; never saved, exported or played.
- **Proof:** `premiere/READBACK.md` (read-back table, ASR of the placed cut = every word at every edge, levels per beat, head_lock, edges changed from SEQUENCE section 3 and why). Builder: `premiere/` (`beats.py` is the one table; `run_window.py --run | --redo | --readback`).
- **Anchor recipe test (kit recipe, Iris + Proteus on 405x720 crops):** Kai PASS, Moist FAIL (grey painted patches). Moist's grey eyelid patches are in the SOURCE too (the recipe cleans everything else). Both stay on frame-on-blurred-fill per SEQUENCE 2; Kai tight 9:16 + Iris is an option for Affan (files in `premiere/anchor/`).
- **Three edges corrected on the waveform:** beat 1a out 1.30 -> 1.66, beat 6 in 80.50 -> 80.62 (80.50 is inside "explain this?"), beat 8 out 32.00 -> 32.20 (32.00 cut "far" in half). The SEQUENCE Short-time column is stale (hook +1.1 s never rippled).
- **A1 is finished audio** (per-beat gain + limiter baked in, -14 LUFS, -1.6 dBFS ceiling): later stops must not limit again.
- **Kai is not clipped** in the kept windows (peaks -2.2 dBFS), contrary to the "+3.0 true peak" note.
- **Next:** later stops only (hook card, captions, scoreboard incl. SPEED "BUY IT", SFX, CTA, names). Never `--redo` now (he may edit the sequence): any structural change goes into a NEW sequence.

## (history) STATUS (PC, 23 Nov ~09:45 PKT): SEQUENCE v1.2 DONE, WAITING ON AFFAN'S OK. NO BUILD.
- **The pitch:** `research/aw-gta6-reviews-2026-11-21/SEQUENCE.md` v1.2, "Streamers Rated GTA 6 👀", about 32.7 s, **BELOW THE BAR: 110K** (40K-320K, about 42 % over 150K).
  - H1: a CRITICS 99 · USERS 5.6 card + Moist "does it live up to the hype?" → Kai "…8.8" → Asmongold "like a nine" / "game of the year material" → Kai graphics 10/10 / "watching a movie" → Moist "yes, FOR ME".
  - The runner-up is H2/O2, Kai's cliffhanger.
- **Sent to the hub** (`local_3ae3a4cf…`), which relays it to Affan. Four questions are in the file's § 10.
- **On his OK:** ONE build session (Sonnet, xhigh) for STOP 1, the raw Premiere sequence, copying the method of `projects/bigfoot-is-in-gta-6/premiere/` (premiere.lock + quietgate.py; restore his active sequence and playhead; a NEW sequence; no save, export or playback).
  - **The build's first job:** the anchor recipe test (2 s of Kai and Moist through Iris vs Prince). If it fails, they go frame-on-blurred-fill.
  - Edges: SEQUENCE § 3 (PC ASR + RMS), never `CLIPS.md`'s Mac times.
- **Done on the PC:**
  - unpacked the Mac zips;
  - PC ASR of all trims + tight re-runs (`asr/`);
  - pulls: Speed's Short (a MISS → Speed OUT), DarkViperAU's Short (a swap), Moist's intro and outro;
  - frames and the anchor sheets (`frames/`);
  - 10 YouTube searches + 6 videos calls (`research/…/api-pc/`);
  - 11 Instagram loads (`research/…/ig/IG-PC.md`);
  - Metacritic read;
  - 1 Sonnet cold read (all applied); Fable × 2 (the beat set and the final, all applied).
- **Meter:** weekly 1 % → 5 %, shared with 3 other sessions (Travis, MJ, HP); Fable 0 %.
- **Open (named in the SEQUENCE's § 0):** the anchor recipe test; Instagram at one phrasing per creator; other tellings; quotes not heard by ear.

## (history) STATUS written on the Mac, Mon 23 Nov 2026 ~05:30 PKT, for the PC hand-back at 07:00 PKT)

**Where it stands:** step 1 (research + text sequence) is about 80 % done. **`SEQUENCE.md` does NOT exist yet.** Nothing is built. Nothing has gone to Affan.
- 5 creators' lines were HEARD on first-party files: ASR word times, frames looked at, loudness measured.
- 1 Fable advisor call was made, at the start (21 Nov ~20:05). There is no advisor call on the beat set yet, and no cold read.
- The Mac worker (`dl.sh`) is stopped, with a `STOP` file in the research folder. Start no Mac pulls.

**Affan's ask (21 Nov):** a compilation of big YouTubers and streamers giving their verdict on GTA 6, like Moist Critical's review.
- Positive-leaning.
- Either a separate review video or mid-playthrough talk.
- Big names only.

**The frame the evidence supports:** one question, answered. The live question is "does GTA 6 live up to 13 years of hype?" (critics 99 on Metacritic vs a loud backlash), and the big names answer it one by one. Moist's "yes, it has lived up to my expectations" is the answer and the button.

### 1. VERIFIED (heard on the first-party file; ASR = WhisperX small with word alignment; frames on contact sheets)
Times are in the source video (VOD timecode). Each row's evidence is in the matching section of `research/aw-gta6-reviews-2026-11-21/NOTES.md`, which carries the file-second word times, loudness and the overlays to cover.

| Creator | Source ID | VOD time | Line (verbatim from ASR) | Picture / audio |
|---|---|---|---|---|
| **penguinz0 (Moist)** | YouTube `Bhti3dZCtXM` "Does GTA 6 Live Up to the Hype" (2.75M views, 20 Nov) | 0:20:25.0-0:20:26.4 | "I am having a great time." | Full-frame face cam, his room, 1080p59.94; no overlays |
| | | 0:20:26.7-0:20:34.0 | "This is what I was hoping GTA 6 would be able to achieve with all of this content right at my fingertips." | |
| | | **0:20:45.1-0:20:52.1** | **"So for me, I would say yes, GTA 6 has lived up to my expectations of it thus far."** (a 1 s pause after "So for me,") | -16.7 LUFS, peak -2.5 |
| **Kai Cenat** | YouTube `dSDUAAr-w_g` "BEATING GTA 6 *FINALE*" (Kai Cenat Live) | 7:09:04.0-7:09:06.8 | "the graphics and realism is 10 out of 10." | **Full-screen face cam, NO game on screen** (so no ending spoiler). Cover: viewer count top left, chat top right, sub counter bottom left. 1080p60 |
| | | 7:09:11.1-7:09:18.2 | "It's not as funny or playful as GTA V, but the realism is what kills every other game." | -12.5 LUFS, true peak +3.0 (hot: check for clipping) |
| | | 7:09:20.6-7:09:28.9 | "The map size is crazy. The amount of things you can do is insane. This is a good game, bro. This is a really good game." | |
| | | **7:10:38.8-7:10:42.7** | **"if I had to rate GTA 6 out of 10, I will rate it a 8.8."** | -15.2 LUFS |
| | | 7:10:52.3-7:10:53.4 | "It's right at the nine mark." | |
| | | 7:11:10.7-7:11:12.9 | "It's like, you're literally watching a movie." | -12.8 LUFS |
| **Asmongold** | YouTube `oyHFwPNd_c4` "So I Played GTA 6.." (Asmongold TV, 3.39M) | 8:43:56.2-8:43:58.6 | (reading chat) "What would you rate it?" / "I would rate it like a nine." | Cam inset top left (~485x415 px, face ~140 px wide) over FULL-FRAME gameplay (golden-hour Leonida). Cover chat bottom right. 1080p60 |
| | | **8:44:54.5-8:44:59.5** | **"Is it game of the year material? Yeah, yeah, it definitely is. It definitely is."** | -19 to -23 LUFS: needs a level match |
| | | 8:48:11.1-8:48:18.2 | "would you recommend it to a friend? ... I think it's more than good enough to recommend. Absolutely." | |
| **xQc** | Twitch clip `VivaciousCallousYogurtDxCat-tcAghtrsbnP82HX2` (his own channel, 19 Nov launch night) | clip 0.21-5.60 s | "The actual core missions are genuinely cinema. The story is good," | **Weak picture:** a blurred pause menu + a ~400x320 cam (face ~70 px), his stream's burned-in captions. HEVC, 0.62 Mb/s, -23.8 LUFS. OPTIONAL beat |

**Verified but NOT usable as positive:**
- IShowSpeed, YouTube `OIeLbmyraRQ` (final mission):
  - 5:20:15-5:20:26 "It's not a 10-game, man. It's not a 10-game." (after "he didn't show what the drive was").
  - 5:14:57 "they both just died": an ENDING SPOILER.
  - This is the counter-evidence a commenter could post, so no beat may present Speed as "after finishing".

**Caveats around the used lines (honesty rule: cut a caveat half, never splice a line into saying more):**
- **Moist:** "I don't think it's a perfect game" (0:20:21) and "thus far" (keep it).
- **Kai:** "you could start to feel demotivated" before chapter 1 ends. "This game is ass." (7:09:48) is him voicing a hater: never use it alone.
- **Asmongold:**
  - The story criticism ("kind of fam slop", 8:44:01-8:44:27) and "is the game a 10? ... I could come up with other games that are 10s".
  - "This is my first GTA game that I've ever played" (8:46:08).
- **xQc:** never end on "the world is immersive": his next sentence is "I wasn't well immersed... the frame rate... headache".

### 2. LEADS ONLY (not heard; don't build on them)
- **IShowSpeed** "It's not even a sponsor, bro. It's a good game. It's actually a great game… You should play it."
  - Fan Short `QsI1s_Ptb5s` (98K) quotes it, posted 18 Nov 17:51 UTC.
  - Speed's OWN Short "iShowSpeed's First Look At GTA 6" `1wzzrOvl_Jg` (30 s, 4.07M views) went up at 17:49 UTC, so the line is most likely in his own Short. **Not downloaded:** the Mac pull was killed in the queue.
  - The guessed window in his day-1 VOD (`qSyo5d-dVzA` 4:25:00-4:31:00) was pulled and is a MISS: a robbery mission.
- **IShowSpeed** "This doesn't even feel like a game": somewhere in `qSyo5d-dVzA` 0:00-7:41 (fan Short `eLtHfYBV-cM`, 70K). Time unknown.
- **Kai Cenat** "It's like The Last of Us had a baby with GTA": fan Short `2pq4wLIQDo4` (62K). Day-1 VOD, time unknown.
- **Kai Cenat** realism "increased by 200%", "you got me taking showers every day": `5tdj53ioJ-c` @ 8:30:31 (the fan Short's own source link). Not pulled.
- **Jacksepticeye:** no spoken verdict pinned. `hI4k9ewBEFA` is titled "ABSOLUTE CINEMA"; a viewer comment points at 1:14:54 (a slow-mo shot). Parked.
- **Dropped as negative:** Lacy, TheBurntPeanut, summit1g, Tfue and Jynxzi, plus xQc's 30 fps half.

### 3. Demand and proof so far (YouTube Data API, session `aw-gta6-reviews`, 10 searches on 21 Nov)
- **Single-creator verdict fan Shorts:**
  - xQc 218K (`sRwp_8JIFa4`)
  - Speed 98K (`QsI1s_Ptb5s`) and 70K (`eLtHfYBV-cM`)
  - Kai 62K (`2pq4wLIQDo4`)
  - A re-upload of Moist's review (2:56) got 182K in 13 h (`VtlECqblmO0`)
- **Multi-creator Shorts:** only negative or other angles, VYCE "13 YEARS FOR 30 FPS?! Streamers React" 57K and LoomLoop 38K. Long-form compilations: StreamerTV 26.5K and 57K. **No positive multi-creator verdict Short was found.**
- **Topic heat:** IGN review 8.15M, Moist 2.75M, Asmongold's GTA 6 clips 2.4-4.4M. The backlash runs at the same time (Asmongold's "The GTA 6 backlash is getting out of hand" 665K, WestJett "Already A Disaster" 1.38M).
- **AW own channel (21 Nov):** no GTA 6 Short posted. Newest-30 median 94.7K. GTA 5 farewell 367K.
- **Working read: BELOW THE USUAL BAR** (about 100K centre). NOT locked: lock it in SEQUENCE.md with the Bigfoot § 4 method (`research/aw-gta6-news-2026-11-19/SEQUENCE.md` § 4).

### 4. Draft beat order (a working draft for the advisor, NOT the sequence)
1. Kai "the graphics and realism is 10 out of 10" (hook claim).
2. xQc "genuinely cinema" (optional).
3. Kai "you're literally watching a movie".
4. Speed (only if `1wzzrOvl_Jg` verifies).
5. Asmongold "game of the year material? ... it definitely is".
6. Asmongold "like a nine".
7. Kai "rate it a 8.8 ... right at the nine mark".
8. Moist "I am having a great time. This is what I was hoping GTA 6 would be able to achieve".
9. BUTTON: Moist "I would say yes, GTA 6 has lived up to my expectations".

About 30-34 s. Runner-up to test: Moist's "yes" as the cold-open hook with the others as the proof.

**G2 risk:** the faces are talking heads. Default: cut to each creator's own GTA 6 gameplay under the line (Asmongold's file already has it; Kai's and Moist's would need gameplay pulls from their own videos at build time).

### 5. THE EXACT NEXT STEP (PC)
1. Re-download (list below). Re-run ASR and frames, and confirm the VOD times above. Same windows, same IDs: the times should hold.
2. Pull Speed's own Short `1wzzrOvl_Jg` (30 s). If "it's actually a great game… you should play it" is in it, Speed is a beat (label it day 1, never "after beating it"). If not, Speed is OUT.
3. Fable advisor on the beat set and the order (call 2 of the gate).
4. Write `research/aw-gta6-reviews-2026-11-21/SEQUENCE.md`:
   - The MAX-EFFORT statement goes first, with the open items named in the first line.
   - Beats with exact in/out points.
   - 2 hooks x 2 orders, with the runner-up named.
   - The PITCH-CHECKLIST § 0 gate table.
   - A locked prediction (centre + range, 5K and 5M pre-mortems).
   - "BELOW THE USUAL BAR" first if under 150K.
   - A "Defaults I took" block.
5. A Sonnet cold read of the final; apply the fixes; then a Fable advisor final.
6. Send the text to Affan through AW - Main. Build only after his OK. Where the raw goes is AW - Main's and Affan's call: this file makes no claim about ABW11's state. Build with the AW kit and reuse it.

### 6. PC MUST RE-DOWNLOAD (footage is never copied between machines; all age-checked on 21 Nov: no `ytRating`)

| File name used on the Mac | Source | Section |
|---|---|---|
| `moist-review-1220.mp4` | `https://www.youtube.com/watch?v=Bhti3dZCtXM` | `*20:20-21:10` |
| `kai-finale-25000.mp4` | `https://www.youtube.com/watch?v=dSDUAAr-w_g` | `*6:56:40-7:10:00`; only ~7:07:00-7:10:00 is needed (face-cam verdict), so pull `*7:06:50-7:10:00` |
| `kai-rating-25790.mp4` | `https://www.youtube.com/watch?v=dSDUAAr-w_g` | `*7:09:50-7:11:30` (or merge with the row above: `*7:06:50-7:11:30`) |
| `asmon-review-31410.mp4` | `https://www.youtube.com/watch?v=oyHFwPNd_c4` | `*8:43:30-8:53:30`; only 8:43:50-8:45:05 and 8:48:05-8:48:25 are used |
| `xqc-verdict-clip.mp4` | `https://www.twitch.tv/xqc/clip/VivaciousCallousYogurtDxCat-tcAghtrsbnP82HX2` | whole clip (33.7 s) |
| `speed-firstlook-short.mp4` (NEW, never pulled) | `https://www.youtube.com/shorts/1wzzrOvl_Jg` | whole Short (30 s) |

- **Not needed again:** `speed-final-18600` (`OIeLbmyraRQ` 5:10-5:24, negative, evidence only) and `speed-day1-15900` (`qSyo5d-dVzA` 4:25-4:31, a miss).
- Format used on the Mac: `-f 'bv*[height<=1080][vcodec^=avc1]+ba/bv*[height<=1080]+ba/b[height<=1080]/b' --merge-output-format mp4 --force-keyframes-at-cuts`, one pace call per line.

### 7. OPEN BLOCKERS AND GAPS
- **Instagram:** NOT run for any beat. The Mac's Instagram is not signed in (`instagram.BLOCKED`, a logged-out wall). On the PC, run the Instagram proof per beat (his first filter) before the sequence goes out, or name "Instagram NOT run" in the first line.
- **YouTube API on the PC:** the session name `aw-gta6-reviews` was added to `yt_api.py`'s SESSIONS on the Mac only. Add it on the PC too (default cap 12). It used 10 searches on Pacific 21 Nov.
- **Max-effort gate still open:** the per-beat proof in 3 phrasings is met only for xQc, Speed and Kai (2-3 each); Moist has 2 and Asmongold 1. There is no "other tellings" pass for Asmongold or Moist. Variants, both advisor calls on the beat set and final, and the cold read are not done.
- **Speed:** unverified (see § 2). If he drops out, the cut is Kai, Asmongold, Moist and (optionally) xQc.
- **Kai's audio** peaks above 0 dBFS. Check for source clipping before the level match.

### 8. Files (light; safe to copy to the PC: no footage)
- `research/aw-gta6-reviews-2026-11-21/`:
  - `NOTES.md`: all evidence, with file-second word times.
  - `api/`: raw API answers.
  - `asr/*.txt|json`: transcripts, Mac file seconds.
  - `sheets/`: contact sheets.
  - Helper scripts: `y.sh`, `cs.sh`, `ct.py`, `vt.py`, `check.sh`, `asr.py`, `dl.sh` (Mac paths).
- `projects/gta6-reviews-compilation/raw/`: Mac footage only, ~1.35 GB. Do not copy it; re-download it.

## Job facts
- Owner: an editor session under "AW - Main" (`local_e8efcca5-9b6b-4d28-a46e-170b923835b6`), started 21 Nov ~19:50 PKT at Affan's request.
- Format: an AW Short, 1080x1920, 60 fps, 30-40 s, code-built finish.
- Constraint: built in one pass from fresh first-party pulls; nothing copied from another job's renders.

## Log (PKT, written on the Mac)
- 21 Nov ~20:00: research started (API session `aw-gta6-reviews`).
- 21 Nov ~20:05: Fable advisor call 1. It said: hear every line before writing beats; re-check Speed's post-finish verdict and Asmongold's own words.
- 21 Nov 20:06-21:16: 7 pulls (YouTube 6, Twitch 1; the xQc clip was held until AW - Main's "Twitch probe passed" at 20:20). All heard. Asmongold turned out POSITIVE; Speed's post-finish take turned out NEGATIVE.
- 21 Nov 21:18: the Speed First Look Short was queued; the worker was later terminated before its turn (not downloaded).
- 23 Nov ~05:30: STATUS rewritten for the PC hand-back at AW - Main's request. No new pulls.
- 23 Nov ~07:05: packed for the PC at Affan's request in `~/Documents/Claude Projects /Mac-handoff/AW/gta6-reviews-pack/`: `gta6-reviews-research.zip` (notes, API, transcripts, sheets, RUN.md, HANDOFF-PC.md; no footage, no wavs) + `gta6-reviews-verdict-clips.zip` (6 lossless verdict trims, ~146 MB, CLIPS.md inside). The PC continues from HANDOFF-PC.md.
- 23 Nov 08:15-09:45 (PC): research finished; SEQUENCE.md v1 → cold read → v1.1 → Fable final → v1.2; sent to the hub.
- 23 Nov ~10:40 PKT: Affan asked for Speed and for 'GTA 6' in the hook. Hook v1.3 done. Speed leads found via the API (SEQUENCE § 13); downloads wait on youtube.BLOCKED.

- 23 Nov ~11:30 (PC): STOP 1 built (build session): anchor recipe test, edges set on RMS + forced alignment, 11 mezzanines + 3 cutaways, sequence created in ABW11 under premiere.lock, one corrected rebuild (beat 6 in-edge), read back + ASR of the placed cut; `premiere/READBACK.md`.
- 23 Nov ~11:58 (PC): Speed beat 2b placed in the sequence (guarded rebuild), 39.867 s; READBACK section 10.
- 24 Nov ~00:20 (PC): STOP 2 built in v2 under lock + gate (37 placements verified, A1 identical to his, his raw cut untouched), READBACK-v2.md.
