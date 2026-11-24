# BUILD BRIEF: "Harry Potter Can't Watch Himself", AW Short, STOP 1 (raw sequence in Affan's Premiere)

Approved by Affan on 24 Nov 2026. His words: "As much as I can do to just be his very uncool, unimpressive dad for as long as I can is the goal. no need to put
this and now start the build but make sure the video quality is good for all source material".

- **Job folder:** `projects/radcliffe-cant-watch-himself/`.
- **Research (read-only for the build):** `research/aw-hp-2026-11-23/`. The sequence is `PITCH.md` § v3 (top table), with beat 7 trimmed.
- **Method to copy:** `projects/mj-fired-his-father/premiere/` + `projects/mj-fired-his-father/RUN.md` § STOP 1 (mezzanines, plan.json, create/place/readback,
  `premiere.lock`, `quietgate.py`, his active sequence + playhead restored by id).

## The cut (7 beats, ~32-34 s)
HSC = episode time. The file `src/4PxqJWglmH8_hsc2026_full_3800-5200.mp4` starts at 2280 s, so file time = HSC − 2280.

| # | Words (verbatim) | Source span | Picture |
|---|---|---|---|
| 1 hook | "now I cringe watching myself when I was 18 or 19." | HSC 2707.43-2709.25 | Radcliffe |
| 2 | "Half-Blood Prince is probably the bottom of the bracket for me. And that's my own stuff. That's not the film." (close the 1.4 s pause after "me.") | HSC 2784.09-2788.75 | A Half-Blood Prince film shot of Harry (see Quality § 3), then back to Radcliffe |
| 3 | "I see them at the premiere, and then if I can, I avoid ever watching them again… It's like passing around baby photos of yourself." | Ross `src/bIOkpZKdwQw_ross2021.mp4` 5.67-9.72 + 22.18-23.62 | Radcliffe at ~22 (Ross studio) |
| 4 | "when the films would come out, my mum and dad would just go like, the reviews were good, you don't need to worry about them, they're good, you're fine." | HSC 2627.22-2632.62 | Radcliffe |
| 5 turn | "And honestly, I hadn't watched the Harry Potters until recently… he's really good in those Harry Potter movies." | Garfield `src/YtDD9nUvicA_garfield2026_mlim.mp4` 1331.88-1334.44 + 1337.20-1339.00 (stop before 1344 "controversial") | Garfield. **The host is on screen at ~1334 s and ~1341 s**: cover any host frame with an HP film shot, never show the host |
| 6 | "Thank you, Andrew Garfield. You're awesome… I disagree with him about my performance in Potter, but that's really nice." | HSC 2688.21-2689.63 + 2692.03-2694.85 | Radcliffe |
| 7 END | "there's a world where my son watches the HBO show of Harry Potter now instead of the films, and I'm also sort of happy with that." (close the pause 2471.6→2473.4) | HSC 2470.93-2478.56 | Radcliffe; hard cut on "that." |

- **Edges:** the word edges come from WhisperX medium.en + wav2vec2 (`transcript/*.words.json`). Re-measure each joint on the waveform and its energy, never by
  listening (silence rule). No clipped first or last phoneme.
- **Horowitz is cut everywhere.**
- **Placeholder labels on V3,** per the MJ method: "DANIEL RADCLIFFE · HARRY POTTER", "RANKING HIS OWN HARRY POTTER FILMS", "THE JONATHAN ROSS SHOW",
  "ANDREW GARFIELD · SPIDER-MAN".

## Quality (Affan's explicit ask): every source span checked at FULL SIZE before it goes in
What is on disk now: all spans checked by frame at full size on 24 Nov (`proof/q/`).

| Source | Stream on disk | Read |
|---|---|---|
| HSC Apr 2026 (beats 1, 2, 4, 6, 7) | H.264 1080p59.94, **2.7 Mb/s** (YouTube avc1 299) | a livestream stage camera, sharp enough at 1080 but soft when blown up for 9:16. The "HAPPY SAD CONFUSED" bug sits bottom-right: crop it out |
| Ross ~2011 (beat 3) | H.264 1080p25, 2.0 Mb/s | clean broadcast picture, good |
| Garfield, Hits Radio Mar 2026 (beat 5) | H.264 1080p25, **1.1 Mb/s** (avc1 137) | a good cinema camera, but the lowest bitrate on disk: check the face for blocking at full size |

1. **Re-fetch the best stream for each SPAN, then compare.**
   - YouTube's VP9/AV1 1080p (or 1440p/2160p if the upload has it) is usually cleaner than avc1 at the same height. Precedent: the winner's `oldman-good-sirius`
     fetched AV1 2160p.
   - Fetch through `bash projects/_onyx-batch2-2026-10/pace.sh youtube yt-dlp ...`, one at a time, each into a NEW empty dir.
   - Only the needed sections, with a few seconds of handle each:
     - HSC 2465-2795;
     - Ross 0-30;
     - Garfield 1325-1345.
   - Format: `-f "bv*[height<=2160]+ba[ext=m4a]/b"`, then make sure it decodes (ffprobe plus one frame).
   - No cookies, proxies, `--extractor-args`, captions, comments or listings. A bot page, 429 or 403 means stop, write `youtube.BLOCKED`, and tell the hub.
2. **Keep the better file per span, by measurement plus eyes.** Pull the same frame from both files at full size. Compare a face crop by eye and by a sharpness and
   blocking number (e.g. Laplacian variance on the face box). Keep the winner. Note it in RUN.md with the proof image.
3. **Half-Blood Prince film shot (beat 2) and the cover for Garfield's host frames.**
   - Nothing for HBP is on disk.
   - Find an OFFICIAL or "4K" scene upload of a Harry close-up from Half-Blood Prince (the films' own picture, young cast OK).
   - Check it is real 4K or clean 1080p, not an upscale: no halos, no plastic skin.
   - One or two fetches, as in item 1.
4. **Mezzanines exactly as the MJ method** (`make_mezz.py`: H.264 crf 12 + PCM 48 kHz, CFR at the sequence's rate, a source-frame boundary), so Premiere never
   meets a yt-dlp file. 25p sources (Ross, Garfield): no frame blending; flag any judder.
5. **Framing:**
   - 9:16 face-centred: one static Motion per clip (YuNet centres), as in the MJ STOP 1.
   - Report the blow-up factor per clip. A 1080p 16:9 source cropped to 9:16 is ~1.78x.
   - **Lanczos only. NO Topaz / Iris / Higgsfield on any real face here** (soft-source rule).
   - If a clip looks soft at full size after the best stream, say so in the report with the image; do not "fix" it with AI.
6. **Audio:**
   - Level-match the three sources to one level (Garfield is quiet, about +12 dB).
   - Static gain plus a look-ahead limiter, as in the MJ method. Never dynamic loudnorm.

## Safety and limits (from the hub's rules; all still in force)
- **Premiere:**
  - only inside `premiere.lock`, after `quietgate.py` says he is idle;
  - a NEW sequence only (a clone of "Sequence 02"; name "Harry Potter Can't Watch Himself - raw cut");
  - restore his active sequence and playhead by id, and compare before and after;
  - **no save, no export, no playback**; never move his playhead.
- **Silence:** never play audio or video; ffmpeg `-f null` only.
- **Content:** censor drug, self-harm and suicide words (none are expected in these spans).
- **GPU:** one ASR job at a time under `.asr-lock` / `gpu.lock`, never a parallel large-v3.
- **Files:** media on X:.
- **Hub files:** do not edit `HUB.md`, `LESSONS.md`, `RESULTS.md`, `IDEAS.md`, `RESULTS-TRACKER.md` or memory; the hub merges.
- **Stop point:** **STOP after the sequence is placed and READ BACK (PASS).** Wait for Affan's Tella. No STOP 2 work (captions, SFX, grade, head lock) before his OK.

## Report (RUN.md ▶ STATUS + the final message)
- the sequence name and id, the clip count, and the runtime;
- the quality table (stream kept per span, blow-up factor, proof images);
- what was NOT checked (no listening);
- the downloads used;
- the weekly meter.
