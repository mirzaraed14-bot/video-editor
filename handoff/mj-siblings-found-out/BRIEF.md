# BRIEF — "How Michael Jackson's Siblings Found Out He Died 💔" (Abundance Wisdom short, to be built FULLY IN CODE)

## ▶ STATUS: resume here (2026-10-21)
- Resolved from his Tella direction video (`brief/raw/guide.mp4`, 12.6 min, "Video Editing Tutorial and Sequencing Guide";
  transcript `brief/guide_transcript.txt`; every "this" pinned to sequence time by reading his timeline timecode:
  `brief/frames/tc_sheet_*.png`, `strip_*.png`). **His answers 2026-10-21 (bottom): build STARTED; O2/O3 (Janet) and O5 (Jermaine × Michael) wait on his files and are
  slotted in last.**
- **The sequence = HIS edit of ours**: ABW10 "MJ Siblings Found Out - raw cut", 58.25 s, read-only dump
  `seqref/seq_his.tsv` (41 clips; V2 = the overlay slots he marked), his A1 rebuilt `seqref/raw/a1.mov`, transcript
  `seqref/transcript/words.json`, one frame per clip `brief/frames/his_clips.jpg`. He changed our cut: beat 3 = the ABC
  bedside interview (`E:\Bullshit Folder\Henry\'You Are Not Alone'_ Michael Jackson's Childhood Revealed by Brother.mp4`),
  La Toya keeps "I started begging people on the street to drive me because", 2 × "how's he doing", Marlon one "never",
  our V2 cover removed.
- The locked edit brief (`brief/edit-brief.md`) still holds where the direction video is silent; where they differ the
  direction video (newer, his voice) wins and is flagged below.
- Method = `projects/katherine-day-michael-died/` (head lock, Topaz chain + jitter tweak, align_frames, finish.py look,
  captions agent, audio.py). Rules: no AE/Premiere/CapCut in the build, never save/export his projects, silence, X: only,
  no phone copy.

## The plan (sequence seconds = his edit; "→" = transition INTO that block)
| Time | Track | Words | Picture | Zoom | → in |
|---|---|---|---|---|---|
| 0.00–2.38 | V1 La Toya (2 cuts) | "I said, how's he doing? How's he doing? Is he okay?" | La Toya CU, head-locked | **in, ONE layer** | — (frame 1 = her face) |
| 2.38–3.95 | **O1** (V2) | "And my mother, she grabbed the phone" | **Katherine Jackson, 60 Minutes Australia: a silent stare**, letterbox | **in** | purple |
| 3.95–6.97 | V1 La Toya | "and she screamed… He's dead." | CU | **in** | cyan |
| 6.97–14.88 | V1 La Toya (4 cuts) | "And when she did that… my legs got so weak." | CU | **in, ONE layer** | dark green |
| 14.88–16.43 | **O2** (V2) | "My sister Janet calls me." | **Janet Jackson, Piers Morgan interview (~2011, 360p): sad / neutral face**, letterbox | in *(not stated — my call)* | purple |
| 16.43–17.90 | V1 Tito CU | "She asked me, was I driving?" | Tito CU | **out** | cyan |
| 17.90–22.22 | **O3** (V2, 4 cuts) | "And I said, I'm getting ready… Don't get on the freeway." | **Janet (same interview), ONE overlay throughout**, sad/neutral, letterbox; **saturation → 0 from "no," (20.45) to ~21.9, grey to the cut** ("like the previous video"; colour back after the purple dip = the Katherine precedent) | **in, ONE layer, masked with the overlay** | purple |
| 22.22–26.08 | V1 Tito CU (4 cuts) | "I said, Janet, is he dead? And she said, he's gone. And" | CU | **in, ONE layer** | purple |
| 26.08–28.78 | V1 Tito wide (2 cuts) | "I just melted right there. And I pulled over in this parking" | wide two-shot | **in, ONE layer** | dark green |
| 28.78–31.28 | V1 Tito CU | "lot and just cried for like 15 minutes." | CU | **in** | dark green |
| 31.28–32.72 | **O4** (V2) | "There he was laying there." | **his hospital-bed still** (= `../katherine-day-michael-died/raw/mj-morgue-still.webp`, crop x96–1255 y35–1155: **"People v. Murray / SA073164" masked out**), letterbox | **out** | peach (exposure blur) |
| 32.72–35.93 | V1 ABC CU (4 cuts) | "And La Toya was there before us. And he was lifeless." | Jermaine CU, **letterbox** (low quality: "the Jermaine video stays in letterbox") | **in, ONE layer** | purple |
| 35.93–38.05 | V1 ABC wide | "I touched his forehead, his face." | wide (Jermaine + interviewer), letterbox | **in, own layer** | cyan |
| 38.05–42.98 | V1 ABC CU (4 cuts) | "Then I kissed him. I pulled his eye… his eyelids. I just told him" | CU, letterbox | **in, own layer** | purple |
| 42.98–45.88 | **O5** (V2) | "how much I love him. And I'm going to miss you so much." | **Jermaine + Michael together, happy, smiling/laughing (adult — rule 4: no childhood footage)** | **out** | *not named — Q3* |
| 45.88–48.33 | V1 Marlon (2 cuts) | "We would never understand what he endured," | Marlon tight (memorial) | **in, ONE layer** | peach |
| 48.33–52.38 | **O6** (V2, 2 cuts) | "not being able to walk across the street without a crowd gathering around him," | **MJ scared / tense / nervous in public, crowd around him, clean HD** — ONE overlay throughout | out *(not stated — my call)* | purple |
| 52.38–54.40 | **O7** (V2, 2 cuts) | "being judged, ridiculed." | **MJ sad / crying, "way down"** — single overlay | **out** | cyan |
| 54.40–56.12 | V1 Marlon | "How much pain can one take?" | Marlon tight | in *(not stated — my call)* | dark green |
| 56.12–58.25 | **O8** (V2) | "Maybe now, Michael, they will leave you alone." | **MJ alone, smiling / laughing, single shot, in GREY** ("he looks happy but he has passed") | out *(my call)* | cyan |
| 58.25 | — | — | **purple fading out into black** | | |

Transitions = his colour rule (purple dip to black, cyan Gaussian blur, dark green exposure, peach exposure blur). Each
call was pinned by the timecode at the moment he named it (he names it while the incoming clip plays).

## Look
- Head lock on every face shot ("not properly head tracked nor in proper position — make sure you do that"); overlays NOT
  head-locked. Letterbox = his AW band (440–1484, twin 198 % @ 47 %, glow bars), as on Katherine.
- **Grade: NOT heavily saturated.** "In the previous video she looks very red… check saturation on each video layer so it
  looks natural, not out of place" (he let Katherine slide, not again). Measure per-source saturation/skin hue and level
  them before the shared grade.
- Topaz his chain; the jitter tweak only where measured jittery (LESSONS 2026-10-20).
- Captions: his AW style at the ABW10 height (Katherine `caption_shift` −62), Fable agent; interviewer lines italic (none here).
- SFX: his whoosh/hit family on transitions + overlay entrances, a **fresh, varied** Epidemic set (memory: never one whoosh
  ×71); levels = his measured gains.

## Overlay sources
| Slot | Need | Local file | State |
|---|---|---|---|
| O1 | Katherine silent stare | `E:\Bullshit Folder\Drake\Katherine Jackson on Michael's Changing Face… 60 Minutes Australia.mp4` (stare scan exists: `../katherine-day-michael-died/build/scan/`) | ✅ (a different stare than the Katherine hook) |
| O2/O3 | Janet, Piers Morgan interview, sad/neutral | none (only Katherine's + Joe's Piers Morgan interviews are local) | ❌ **he downloads** |
| O4 | hospital-bed still | his Higgsfield image = Katherine's `raw/mj-morgue-still.webp` | ✅ |
| O5 | Jermaine + Michael adult, laughing | none found (Jackson 5 / Ed Sullivan = childhood, banned) | ❌ **he downloads** (or OK to search `Private Home Movies`) |
| O6 | MJ scared in a crowd, HD | `Henry\Michael Jackson in Public.mp4`, `Living With Michael Jackson` 4K parts (Vegas/Berlin crowds) | 🟡 to pick (no children in frame) |
| O7 | MJ sad / crying | `Lonely\Michael Jackson Neverland Statement 1993 … 4K 60FPS.mkv`, Oprah 1993 4K, Living With MJ | 🟡 to pick |
| O8 | MJ smiling alone (grey) | Oprah 1993 4K (a different moment from Katherine's O3), `Lonely\…Pushed Into The Pool… (HD)` | 🟡 to pick |

## Open questions (sent 2026-10-21) → his answers the same day
1. Janet × Piers Morgan file (O2/O3) — YouTube refuses this PC.
2. Jermaine × Michael together (O5): his file, or OK to search the local `Private Home Movies`?
3. The transition INTO O5 (42.98) was not named (he named purple at 38.05, wide → CU): purple?
4. Zoom directions he didn't state: O2 in, O6 out, Marlon 54.40 in, O8 out — OK?
5. Ending: the brief says hard cut on "alone", the video says purple fade to black → fade (video wins)?
6. Brief items the video didn't mention: piano bed −30 dB under beats 1–4? lower thirds (name · relation)? (Katherine had neither.)
7. Tito's picture runs ~0.25 s AHEAD of his voice on 7 clips of his edit (V1 22.22–28.78 + 16.43) — deliberate sync fix?
8. Marlon's two visible stretches (45.88–48.33, 54.40–56.12) carry the CBS weather crawl: crop it out (zoom past ~115 %)?

**Answers (Affan, 2026-10-21):** 3 → **purple** into O5. 4 → **yes** to the default zooms (O2 in, O6 out, Marlon 54.40 in, O8 out).
5 → **fade to black** (purple). 7 → **deliberate: he synced Tito's picture** (keep his V1 in-points exactly). Saturation plan
(ramp from "no," 20.45, grey to the 22.22 dip, colour back after) → **correct**. Not answered → defaults stand: no music bed; **lower thirds ADDED on his OK 2026-10-21** (name · relation, ~2 s), Marlon zoomed past the CBS crawl, per-source saturation levelled. Still owed by him:
the Janet × Piers Morgan file (O2/O3) and a Jermaine × Michael adult clip (O5).

## What this short does better than the last one (Katherine "day Michael died") — the every-video-better rule
- **Colour:** skin levelled per source AND per overlay before the grade, measured on graded frames (skin HSV-sat 0.53-0.56,
  R/G ~1.6) — Katherine shipped at 0.64-0.71 / R/G 2.3-2.7 ("she looks very red", his note). Re-checked after Topaz.
- **Sound:** a fresh, varied Epidemic SFX set (4 whooshes rotated, never back to back, + 2 low hits on the peach cuts), every
  take passed a narrow-tone ("cricket") check — Katherine used one whoosh slice on every transition. Per-speaker loudness
  matched (Tito +4.6 dB) to the brief's -14 LUFS / <= -1 dBTP.
- **Steadiness:** the jitter tweak chosen per same-setup run by MEASUREMENT (default vs tweak, nose-patch jitter), only where it
  wins (J1 run, M2).
- **Framing hygiene:** burned-in broadcast graphics kept out by measured framing (CBS crawl, ABC banner mostly), and the
  letterboxed Jermaine framed so captions clear his face.
