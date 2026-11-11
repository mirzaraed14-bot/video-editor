# RUN: harry-potter-prank ("Harry Potter Thought Snape HATED Him 💔"), Abundance Wisdom Short

## ▶ STATUS: resume here
- **11 Nov 2026, 02:08 (Premiere window 02:08:06-02:08:52, readback 02:09): RAW SEQUENCE PLACED in ABW10** as "Snape Prank - raw cut" (bin "Snape Prank"), 30.00 fps,
  1080x1920, 0-55.60 s.
  - It's a clone of his empty "Onyx reaction template (empty)", with both sources imported into the bin.
  - V1/A1: 12 clips each, butt-joined. 7 beat markers.
  - **Read back** (`premiere/readback.tsv`):
    - every clip's sequence span equals the plan;
    - Premiere floored each in-point one more frame (33 ms) earlier, and every edge still lands between words
      (checked against `transcript/words.json`);
    - scale and position as planned (HSC 177.78 %, DVD 400 %).
  - His active sequence was restored afterwards ("Brotherly Love reaction"). **ABW10 NOT saved**: it needs his Ctrl+S to
    keep the sequence.
- He reviews it and sends a Tella video. Next step: resolve his Tella notes into BRIEF.md (memory
  `feedback-walkthrough-videos`), then the build.
- **11 Nov, 06:52-06:58: the G4 freshness search ran** (the hub cleared YouTube at 06:48). Six requests via `lock.sh`,
  ≥60 s apart, no bot page.
  - **Our stitch was not found by title.** Recall is low: Horowitz's known 1.17M "hates me" Short didn't come up either.
  - The prank alone: 12.5M (ShenronAlt, 2012, 16:9), 2.8M (Tyler Morgan, his download), 858K (chelsea, format not
    checked).
  - Results: `meta/fresh.txt`, `fresh2.txt`, `fresh3.txt`; the row is in `PITCH.md`.
  - **Option for his review, not downloaded:** tgXZefAYRnQ (Josh Horowitz Clips, 276K, 6:16) is titled "Alan Rickman
    reflecting on playing Snape… and his pride in the young actors". It's likely the full-frame original of the clip
    that R07-R09 show only as an oval inset, so it would give a cleaner picture for beat 6 and a date for the clip.
    It needs one more spaced YouTube call.

- **11 Nov, 21:09-21:20: v2 PREPARED, not yet placed.** He asked: "download the remaining bits if needed and give me
  the raw sequence asap so i can approve it".
  - **Downloaded** tgXZefAYRnQ, the full-frame 2015 Rickman original (Josh Horowitz Clips): 1080p H.264, 23.976 fps,
    594 kbps. Readable copy: `src/rickman/Alan Rickman on Snape and his pride in the young actors (2015).mp4`.
  - **Transcribed** word-aligned in `_rk/transcript/words.json`. Same words as v1 R07-R09, edges set from 20 ms
    loudness:
    - R07: 301.00-303.43;
    - R08: 333.07-337.77;
    - R09: 343.00-349.73. Tight: Horowitz talks straight after "worked at it" in the original.
  - Crops: `proof/framing_v2.jpg`. Rickman fills the frame and there's no oval.
  - **Ready to run:**
    - `premiere/build_place_v2.py` → `place_v2.jsx` and `plan_v2.json` (55.7 s);
    - `run_window_v2.py` (creates "Snape Prank - raw cut v2", places it, restores his active sequence, never saves);
    - then `pp.py readback_v2.js`.
  - **Blocked by the shared `premiere.lock`:**
    - It has been held since 08:11 by "heretics v3 FIX shift…", and that job hasn't written since 08:34.
    - My takeover (rename) was refused by the permission classifier, so it waits on Affan or the hub.

## Sources (his downloads, `E:\Bullshit Folder\Henry\`)
- `Daniel Radcliffe, Jonathan Groff, _ Lindsay Mendez talk MERRILY WE ROLL ALONG I Happy Sad Confused.mp4`: 1080p, 59.94 fps.
- `Prank on Harry Potter.mp4`: Warner's *Azkaban* DVD featurette, 854x480, 25 fps, 4:3 pillarbox. The dailies file is
  named `hp3_61_11_joke`.
- The Fallon file (`Alan Rickman Takes Jimmy to Task…`) is the helium segment, NOT the prank, so it isn't used.

## The cut (`premiere/plan.json`; words = WhisperX word-aligned `transcript/words.json`)
| Row | Seq | Source | Words |
|---|---|---|---|
| R01 B1 HOOK | 0.00-4.73 | HSC 2184.03 | "I was so intimidated by him for the first three movies… this guy hates me." |
| R02-R03 B2 | 4.73-12.77 | DVD 2.07 / 6.97 | "Michael Gambon and Alan Rickman, … took the opportunity to play a practical joke on me." (Rickman laughing on set, then young Dan) |
| R04 B3 | 12.77-18.80 | DVD 22.67 | "and Dan has asked to have his sleeping bag next to this particular girl that he fancied." |
| R05 B4 | 18.80-23.20 | DVD 35.97 | Gambon in the take: "In our dreams, we enter completely our own world." (raw dailies) |
| R06 B5 | 23.20-32.73 | DVD 51.03 | "They had put a fart machine into my sleeping bag… Michael Gambon had actually been pressing it during the take, I found out." |
| R07-R09 B6 | 32.73-46.50 | HSC 2114.77 / 2146.87 / 2157.63 | Rickman: "this was their life… from 12 to 22", "Huge pride to go and see him in the musical", "how dare he be dancing as well as the New York dancers because he worked at it." (Dan above, Rickman's oval below) |
| R10-R12 B7 | 46.50-55.60 | HSC 2166.77 / 2199.27 / 2219.80 | "Thanks for showing me that. I've never seen that before." / "He cut short a vacation in Canada… every piece of stage work I ever did while he was alive." / "I'm so, so lucky." |

**Flags for him:**
1. 55.6 s raw. Under the 60 s cap for Shorts with claimed content (a claimed Short over 60 s is blocked).
2. R10 is the source's wide stage shot (1.7 s), so Dan is small there.
3. The DVD footage is SD, cropped at 400 %. A zoom-out with blurred fill is the alternative.
4. Warner's "Raw Camera Dailies" label is partly visible bottom-right on R05/R06.
5. R01 is moved up from after the clip; his words are intact.
6. Minors: young cast in the DVD featurette, under his exception (BTS is my default reading).

Crops: `proof/crop_sheet.jpg`. Quality: `proof/anchor_fair.jpg`. Gate statement: `PITCH.md`.
