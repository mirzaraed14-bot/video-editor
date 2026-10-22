# BRIEF — Katherine Jackson, "the day Michael died" (Abundance Wisdom short, built FULLY IN CODE)

## ▶ STATUS: resume here (2026-10-20)
- Brief resolved from his Tella direction video (`brief/raw/guide.mp4`, 15.5 min; transcript `brief/guide_transcript.txt`;
  each comment pinned to sequence time in `brief/comments_by_seqtime.txt`). **All 5 questions ANSWERED 2026-10-20 (bottom);
  build started — progress in `RUN.md`.** Still owed by him: the morgue still in `raw/`.
- The test (his words): "I'm experimenting with you making this from scratch inside of Claude." No AE / Premiere / CapCut
  in the build: the code engine from `projects/aw-code-trial-parents/` (head lock, Topaz headless, AE look, captions +
  CapCut model). His AE vocabulary (BlurMoCurves, transition colours) is just how he describes it.
- He says it is the kind of short "going viral right now on my channel": very sad, painful.

## Input
- **ABW10 → Sequence 13** (read-only, `seqref/seq13.txt`): 1080×1920, 47.87 s, every clip from
  `E:\Bullshit Folder\Drake\Katherine Jackson on Michael's Changing Face and the Scandals _ 60 Minutes Australia.mp4`.
  RAW: not resized, not locked, no music. Clean A1 dialogue `seqref/a1.wav`, transcript `seqref/transcript/words.json`.
- Shots (contact sheet `brief/clips_sheet.jpg`): **R** = the reporter, **K1** = Katherine close (doll background),
  **K2** = Katherine's second setup (later in the interview).

## The plan (sequence seconds; "→" = transition INTO that shot, by his colour rule)
| # | Time | Shot | Words | Zoom (one layer per row) | → in | Notes |
|---|---|---|---|---|---|---|
| H | 0.00–1.77 | **K stare (new)** | "On the day Michael died, where were you?" (reporter VO) | in | — | HOOK: replace the reporter shot with a moment where Katherine stares, silent (I find it in the source) |
| 1 | 1.77–2.62 | R | "I came home and" | in | purple (dip to black) | |
| 2 | 2.62–4.20 | K1 (2 cuts) | "their father called me" | in, ONE layer 2.62–5.93 | cyan | |
| O1 | 4.20–5.93 | **Joe Jackson overlay** | "…and he said" | overlay zooms OUT | purple | letterbox; NOT head-locked; slow-mo only frame-interpolated/blended |
| 3 | 5.93–7.93 | R | "can't you come down to the hospital?" | in | — | |
| 4 | 7.93–13.52 | K1 (4 cuts) | "I went down … to tell me" | in, ONE layer | purple | "four bits, same shot": no transitions between them |
| 5 | 13.52–15.67 | R | "And I said, well, where's Michael?" | out | purple | |
| 6 | 15.67–20.75 | K1 (3 cuts) | "…visit him … took me to a room" | out, ONE layer | cyan | |
| 7 | 20.75–22.07 | R | "…a room. So finally," | in | dark green (exposure) | |
| 8 | 22.07–31.17 | K1 (4 cuts) | "did he make it? … no, he didn't make it." | in, ONE layer | dark green | **saturation ramps to 0 (full grey) over "And Frank finally said slowly, no, he didn't make it" (27.3→30.9)**, held grey to the 31.17 cut, colour back after the purple dip (his answer); the grade (sharpen, Looks, etc.) stays |
| 9 | 31.17–34.02 | K1 | "I don't know what happened after that. I guess I must have blacked out" | out (its OWN layer, same shot) | purple | |
| 10 | 34.02–35.27 | R | "or screamed or something" | out | cyan | |
| O2 | 35.27–37.13 | **MJ photo overlay (letterbox)** over K2 | "In that morgue where Michael was" | overlay zooms OUT | purple | his still of MJ; he offered an enhanced Higgsfield version |
| 11 | 35.27–38.73 | K2 (2 cuts) | "…I couldn't go." | in, ONE layer | — | |
| 12 | 38.73–40.15 | R | "You didn't want to see Michael?" | out (my call) | dark green | |
| 13 | 40.15–45.38 | K2 (2 cuts) | "Not that way, no. I wanted to remember him when he was smiling and we was alive." | in, ONE layer (my call) | cyan | |
| O3 | 41.58–45.38 (his answer) | **MJ smiling overlay (letterbox)** | "I wanted to remember him when he was smiling and we was alive" | overlay zooms OUT | purple | highest-quality footage of MJ smiling/laughing; one clip runs the whole bit |
| 14 | 45.38–46.72 | R | "And you have no regrets about that?" | in (own layer) | purple | |
| 15 | 46.72–47.87 | K2 | "No, I don't." | in (own layer) | cyan | **ends on a fade out** |

All footage: head-locked, centred (face not drifting left/right), resized by me; overlays NOT head-locked.
Captions: his AW style (Gretaros, max 3 words, colour words, deep glow, drop shadow, wiggle); reporter lines italic.
Topaz: his settings; on jittery shots raise interpolation a few points and lift the 2nd stabilisation pass slightly, never 3
passes (LESSONS 2026-10-20).

## Open questions (sent to him 2026-10-20) → ANSWERED 2026-10-20
1. Grey after "no, he didn't make it": **colour RETURNS after the purple dip at 31.17** (grey only 27.3→31.17).
2. MJ smiling overlay: **covers the WHOLE V2 clip 41.58–45.38** (from "I wanted to remember him"), purple dip into it.
3. Files: **morgue still = he drops his enhanced Higgsfield version into `raw/`** (build the rest first, slot it in
   last). Joe Jackson + MJ smiling: picked by me from the local E: files (no objection): Joe =
   `E:\Bullshit Folder\Henry\EXCLUSIVE LEAK- Joe Jackson's FULL Interview.mp4` or the Piers Morgan 2013 interview
   (`Canelo/` .mp4, `Henry/` .mkv); MJ smiling = `Henry/Michael Jackson - Private Home Movies (Full Version).mp4`,
   the Living With MJ 4K parts (`Henry/`, `Drake/`), Ed Sullivan Jackson 5 (`Drake/`).
4. Music: **none.**
5. SFX: **yes, his usual** on transitions/overlays (no music bed).

Cost quoted 2026-10-20 before the build: ≈ $10–11, ceiling $13 (Opus, this session, no subagents).
