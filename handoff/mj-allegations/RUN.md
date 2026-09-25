# RUN — mj-allegations ("Don't treat me like a criminal")

▶ **TRANSITIONS (2026-09-24): DONE in ABW8 Linked Comp 06** — 8 from the creator's labels
(Purple dips at 2.55, 8.10, 44.27 · Dark Green +30 at 29.90, 33.52, 38.47 · Peach uni.Exposure at
13.92, 41.83), read back from AE, above the zoom layers. Undo group "Abundance Wisdom transition pass
(Claude)", project NOT saved. `transitions/transitions.jsx` re-runs cleanly.
⚠ The creator relabelled blocks for transitions (incl. former yellow pull-outs), so **the zoom
directions now live in `zoom/apply.tsv`, not in the labels — never re-run zoom_pass.py from labels.**

▶ **ZOOM PASS (2026-09-24): DONE in ABW7.aep → ABW8 Linked Comp 06** (the creator said "08"; 06 is
the comp with the Topaz render `hurt_stab_chr2_iris3_prob4.mov` and the labels). 11 × S_BlurMoCurves
("Adjustment Layer 29"), undo group "Abundance Wisdom zoom pass (Claude)", project NOT saved.
Plan + frames + preview: `zoom/` (apply.tsv, zoom-preview.jpg). Pivots: blocks 1 (y593), 5 (y357),
6 (y680). **Flagged:** the Topaz render blurs 2–4 frames at every cut (stabilisation, by elimination).

▶ **CAPTIONS (2026-09-23, night): SRT READY, caption track NOT yet on Sequence 03** — the Premiere
MCP Bridge stopped mid-job; one call, `captions/import_srt03.jsx` (importFiles +
`seq.createCaptionTrack(item, 0)`) once the creator clicks Start Bridge again.
- `captions/outputs/seq03-captions.srt` — **66 captions, max 3 words** (creator's rule for this
  job), wall-to-wall 0.05 → 49.233 s, no commas/full stops. Styling guide: `captions/caption-colours.md`.
- Built from the LIVE A1 (`captions/brief/seq03_tracks.txt`) by `timeline_words.py`: the job's
  per-source transcript moved onto the sequence clock, no re-transcription — except Sawyer 974.77,
  outside the old extract, transcribed once as `raw/sawyer974.mp4` (offset 960) and merged into
  `transcript/words.json` (backup: `words.before-sawyer974.json`).
- Dropped one edge fragment: "it" at 46.368 (39 ms, left by the cut before "It is of loving").
- Italic (14): Bashir 2.61–6.25, and the police remarks Michael quotes (14.49–16.62, 26.86–29.96).

▶ **STATUS (2026-09-23, night): HEAD LOCK APPLIED in AE project ABW7 — 21 of 22 Iris clips, proven.
AE project NOT saved yet (undo group "Head lock (Claude)"). Next: the creator answers the two
questions below, saves, renders the stab comp → Topaz.**

- Comps: **ABW8 Linked Comp 02** (layers 1–16 = clips 0–15) and **ABW8 Linked Comp 03** (layers
  1, 2, 4, 5, 6 = clips 19, 20, 22, 23, 24; comp starts at sequence 38.4667). Map: `headlock_map.json`.
- Per layer: Anchor Point keyed on EVERY 60 fps frame (linear, 2,513 keys total) from `track.json`,
  Position untouched; Motion Tile Output Height 340 / Width 100 / Mirror Edges on.
- Read back from AE: key count = layer length × 60 on all 21; AE's source times and anchor values
  match the track to 0.0000 s / 0.1 px. Proof sheet (all 21, locked vs unlocked, detector-free):
  `headlock_proof.py` → every layer holds the nose on its first-frame point.
- Not tracked: the 3 Violet Katherine clips (33.55–38.47, as asked); **comp 03 layer 3** (Sawyer
  close-up, 41.80–44.23, Scale 100 = letterboxed) — waiting on the answer below.

**Open for the creator**
1. Comp 03 L3 at Scale 100 (letterboxed) — intended? Yes → lock it without Motion Tile (the bands
   stay clean). No → scale to fill like the rest and lock it (track is already computed, clip 21).
2. **Comp 02 L8 (12.58–13.92, "One time I asked to use the restroom.")** is the 60 Minutes WIDE shot:
   Michael sits at the top-right corner of the broadcast frame, outside the crop — the viewer sees the
   dark room behind Ed Bradley. The lock follows Michael whatever the framing, but at 266.8 % his
   nose would land at y≈191 if slid into frame, so this shot needs a scale-down or a different take.
3. Note: the last frame of comp 02 L3 (6.2333) is the broadcast's own one-frame dissolve into the
   next shot (Bashir → Michael, source 25.20). The track is smooth through it; flagged only because it
   is a ghost frame.

Restore points: `brief/ABW8_copy.prproj` (Premiere, saved 20:37); AE = undo "Head lock (Claude)".

*(earlier)* The creator re-cut the sequence (82.55 → 49.23 s, 25 clips + a parked full 60 Minutes
clip at 69.08 s, music added) — measured in LESSONS 2026-09-23 (recut).

*(earlier)* sequenced into ABW8 / Sequence 03 (82.55 s). Waiting on the creator: beat 6 attribution,
arrest footage for beat 3, drop candidates.

| | |
|---|---|
| Channel / preset | Abundance Wisdom → `presets/youtube-shorts/abundance-wisdom/` |
| Brief | `E:\Claude Projects\Abundance Wisdom\ALLEGATIONS-CUT.md` → **SEQUENCING DRAFT 3** (and its NEVER list) |
| Project | Premiere `ABW8.prproj` → **Sequence 03** (1080×1920, 60 fps), bin **MJ Hurt** |
| Scope | first job where Claude SEQUENCES (the creator used to). Everything after stays as agreed. |

## Sources

| key | file | fps | note |
|---|---|---|---|
| neverland | `C:\Users\affan\Videos\Michael Jackson Neverland Statement 1993 Ai Digital Remastered 4K 60Fps.mp4` | 60 | **not in the bin** — found on disk, imported into MJ Hurt |
| bashir16 | `LIVING WITH MICHAEL JACKSON PART 16 4K Upscale.mp4` | 50 | the sheet's "BASHIR 10/10" is a different upload; quote found at 0:21 |
| sawyer | `…PRIMETIME Interview (1995) 4K UPSCALE.mp4` | 29.97 | same upload as the sheet |
| katherine | `Katherine Jackson Interview Piers Morgan 2012 Part 1.mp4` | 29.97 | quote at **11:02**, not the sheet's 9:36; no burned-in subs |
| sixtymin | `Michael Jackson - 60 Minutes Interview.mp4` | 30 | full copy; the sheet's times were from an excerpt |
| **arrest** | — | — | **missing everywhere on this machine** |

## The cut on the timeline (V1 + A1, 17 clips, 10 markers)

| beat | tl | words |
|---|---|---|
| 1 hook | 0.00–2.85 | "Don't treat me like a criminal, because I am innocent." |
| 2 Bashir *(drop #1)* | 2.85–8.50 | "The world needs a man who's 44, sleeping in a bed with children." / "No, no, you're making it all wrong." |
| 3 arrest | 8.50–11.50 | **3 s gap held — no source** |
| 4 shoulder | 11.50–19.17 | "They manhandled me very roughly. My shoulder is dislocated, literally. It's hurting me very badly." |
| 5 restroom | 19.17–33.48 | "Once I went in the restroom, they locked me in there for like 45 minutes." / "one of the policemen came by the window and he made a sarcastic remark. He said, does it smell good enough for you in there?" / "And I just simply said, it's all right. It's okay." |
| 6 "his wife" ⚠ | 33.48–44.45 | Sawyer "maybe this is true," / **Elizabeth Taylor** "No way. Absolutely not. Never? Never. I know Michael's heart. I know his mind and his soul." |
| 7 Elizabeth Taylor | 44.45–57.32 | "He was my friend. He was alone. He was totally alone." / "if they'd planned an assassination, they couldn't have done it any better. It almost broke his heart." |
| 8 Katherine | 57.32–66.27 | "It just hurt because I know Michael didn't do those terrible things. But then I say there are so many wicked people. Why are they doing this to him?" |
| 9 hurting *(drop #2)* | 66.27–71.70 | "I wanted the public to know that I was okay, even though I was hurting." |
| 10 end | 71.70–82.55 | "if I am guilty of anything," / "It is of loving children of all ages and races." / "I love you very much, and may God bless you all. I love you. Goodbye." |

Framing: every clip scaled to **fill the frame height** (the creator's habit, from their AE head-lock
comps) and slid sideways onto the face. Two camera cuts inside a quote were split into separate clips
so each shot gets its own crop (Bashir → Michael at 25.23; 60 Minutes close-up → wide at 509.80);
both splits are sample-continuous.

## Checks run

- **NEVER list:** hook ends on "innocent." before the strip-search passage; Taylor cut on "heart."
  before the painkiller narration; no settlement, no suicide question, no "slit my wrists".
- **Frame check, every segment** (6 frames each; the Bashir beat at 12 fps): **no child on screen**
  (the hand at 25.1 s is Michael's own, taped finger); Elizabeth Taylor **is** on camera in beat 7;
  60 Minutes spans are his close-up — the last 1.8 s of beat 4 is the broadcast's own wide two-shot
  (him and Ed Bradley), not the wrist photo.
- **Every cut edge** read back from Premiere and checked against the words and against measured
  audio energy (the aligner's boundaries were wrong at four edges).

## Open for the creator

1. **Beat 6 is misattributed in the cut sheet.** It's Elizabeth Taylor, not Lisa Marie.
   Real Lisa Marie, on camera, close-up: **SAWYER 21:51–22:10** — Sawyer: "Would you let your son,
   when he grows up and is 12 years old, do that?" / Lisa Marie: "You know what, if I didn't know
   Michael, no way. But I happen to know who he is and what he is… I know that he's not like that."
   (the question is about sleepovers — ad-sensitive, their call).
2. **Beat 3 arrest footage** isn't on this machine.
3. **Drop candidates** are marked: #1 Bashir (5.65 s), #2 "even though I was hurting" (5.43 s) →
   ~71.5 s with both out.
4. **Project is unsaved.**
