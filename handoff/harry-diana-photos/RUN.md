# Harry Diana Photos — RUN

## ▶ STATUS: resume here (2026-11-02 ~16:10)
- **RAW SEQUENCE PLACED in ABW10, NOT saved** (he saves): bin **"Harry Diana Photos"** › **"Harry Diana Photos - raw
  cut"** (id `253ccf59-794c-4036-9454-4c504a1ab05c`). 1080×1920 **30.00 fps** (clone of "Onyx reaction template
  (empty)" set to 30 / display 104), **48.13 s**:
  - V1/A1: 32 clips each (26 speech pieces + 6 crop razors), source audio only.
  - V2: 4 picture-only clips (B6 covers over ITV's 1997 footage, a hold under ITV's fade under "away", and a 1-frame
    crop fix in B4). A2 empty.
  - 6 beat markers (name, label, warning). No grade, captions, upscale or music.
- His active sequence was restored after each window: "Still Here reaction" after v1, and "Paris Shock Therapy - raw
  cut" after v2 (he had switched to it in between). The 1-frame fixes ran without switching.
- **v2 = v1 re-placed** (2026-11-02 ~16:00): the A1 re-ASR of v1 still heard "you know" before "she would never" (B2). In
  moved 8.70 → 9.17 (the real gap between "know" and "she"). Placed only after the read-back showed our sequence
  unchanged since v1 (`premiere/run_replace.py`). v1 files are in `premiere/v1/`.
- **Verified:** `premiere/readback.tsv` vs the measured edges (`win/verify_eff.py`): every piece holds exactly its
  in/out, no gaps. The only deviations are two crop razors one frame late: B6's sits under a cover, B4's is patched by
  `premiere/fix_b4_frame.js`. Picture (`proof/sim_readback.jpg`): only Harry and Cooper; no wreckage, no 1997 footage, no bugs. A1 rebuilt from the
  read-back and re-ASR'd (`win/asr_a1.json`): the brief's words, first words "the last thing…", last "wiping away";
  nothing leaked at any of the 31 joins (no "you know", "Mm-hmm", "Well", "um", "I've seen", narrator or reporter).
  Hard rule 1 (`win/gap_check.py`): the longest quiet run is 0.18 s.
- **WAITING for his Tella direction video.** Nothing else runs before it: no build, grade, captions, Topaz or render.
- When it arrives:
  1. Transcribe it, and sample the frames he points at.
  2. Resolve every note into BRIEF.md.
  3. If he re-cut the sequence, dump HIS sequence read-only; his cut is the spec (never re-place over it).
  4. Do the catalog pass into BRIEF.md (CLAUDE.md learning loop 5).
  5. **Quote the build cost, CTA included** (§ Subscribe CTA below), then do the code build (copy the newest AW build, e.g.
     `projects/conrad-murray-didnt-kill-mj/build/`). Lean mode (usage tight since 2026-11-02): no new agents without asking.
- Open questions for him: BRIEF.md § "Brief vs his standing rules" and § "Decisions taken in the raw cut".

## Subscribe CTA (Affan 2026-11-03: this is the FIRST Short to ship it; part of the build, not before his Tella)
- Spec: `presets/youtube-shorts/abundance-wisdom/README.md` § 12. Kit (built, don't redesign): `presets/youtube-shorts/
  abundance-wisdom/cta/cta.py` (`rgb, a = cta.frame('mid'|'end', u, cy=1392)`, premultiplied float32). Renders:
  `E:\Shorts\Abudance Wisdom Shorts Exports\CTA\` (`aw-cta-mid-30.mov` 2.8 s ProRes 4444 alpha, `aw-cta-end-30.mov` 3.5 s, `aw-cta-mid-
  sfx.wav` / `aw-cta-end-sfx.wav`, crest on frame 0). He was reviewing the Conrad preview on 2026-11-03: **use whatever
  is in that folder at build time** (design changes come through the orchestrator and get re-rendered there).
- **v2 (after his review of v1, 2026-11-03 17:23–17:27, README § 12 rewritten):** the mid prompt is the same size, slot,
  2.8 s and `cta.frame('mid', …)` call, now with his red Deep Glow and a flare on the click. The END SCREEN is replaced by
  "Road to 1M", **4.0 s** (was 3.5): his gold play-button plaque flips in on a light streak, the count rolls to the
  subscriber number on "ROAD TO 1,000,000", the button is tapped, the count ticks +1, and sparks fly into the plaque.
  **Pad the end WAV to 4.0 s** in the mix.
- **The subscriber count is baked into the end screen: ask him for N in the cost quote** (540,000 on 2026-11-03), then
  re-render before shipping: `uv run -q --with numpy --with pillow --with opencv-python-headless python presets/youtube-
  shorts/abundance-wisdom/cta/cta.py render --only end --fps 30 --subs <N>` (or set `cta.SUBS` / `cta.FPS` in code).
- Mid prompt ×2 at ~35–45 % and ~70–80 %; never in the 0–5 s hook, over a label card or another low-band graphic, in the
  last 3 s, or on the payoff line. Centre y 1392, moved (cy) off a glow bar or a mouth. Sound: the mid WAV's peak ~15–19 dB
  under the local voice peak (Conrad: −12.6 dB on the WAV); the end WAV −15.6 dB. No music under the end screen.
- Provisional slots on the 48.13 s raw (re-place them on whatever cut his Tella leaves):
  - Mid 1 ≈ 0:16.9–0:19.7 (35–41 %): B2 "she would never do this to us… part of a plan". No label there.
  - Mid 2 ≈ 0:33.7–0:36.5 (70–76 %): this lands on B5 "All I saw was the back of my mom's head…". There's no other
    slot in 70–80 % (B6 from 0:37.20 carries the ITV · 2023 label, and the end is the payoff). It's a grim line for a
    subscribe pill: **ask him**, or slide it to ~0:30.9–0:33.7 (64–70 %, B4's tail).
  - End screen: appended after "wiping away" (4.0 s in v2). **The brief's hard rule 7 says "No end card"**; his 2026-11-03 rule adds one.
    Default: HARD CUT from "away" straight into the end screen's black (keeps the hard cut), and confirm with him.

## Job facts
- Brief (locked, his words): `X:\Claude Projects\Abundance Wisdom\HARRY-DIANA-EDITOR.md` (already on disk from 1 Nov; used as is).
  Decisions: [BRIEF.md](BRIEF.md).
- Instruction (via the orchestrator session): same flow as Paris Shock Therapy, "do the sequencing for premiere and await
  my direction video".
- Export (later): `Harry Diana Photos.mov` → `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders` + identical copy in
  `X:\Claude Projects\Exports\`. Never C:, no phone copy unless asked.
- House rules: never save or export his Premiere project; never close Premiere or AE; work in silence; no Fable agents;
  one heavy GPU job at a time (check `nvidia-smi`).
- **Premiere is shared (3 sessions in ABW10, 2026-11-02): every Premiere window takes the ONE shared lock**
  `projects/_onyx-batch2-2026-10/.locks/premiere.lock` (lab-notes 2026-11-02). Built in: `premiere/plock.py`; `pp.py`
  takes it per call, `run_window.py` / `run_replace.py` hold it for the whole window. Never overwrite a file Premiere has
  imported (a re-render gets a new name); `lanes/premiere/dialog-watch.py` closes import-failure modals, so run no closer.
  The v1 window (15:30) and the v2 re-place ran WITHOUT the lock, before the rule; v1's place.jsx collided with the Onyx R2
  builder (bridge drop) but landed in full, and v2 was placed and read back complete.

## Pipeline
| # | Step | Status |
|---|---|---|
| 1 | Intake: 60M + ITV via yt-dlp (H.264) → `raw/`; `seq_src/` H.264 CRF 12 + PCM 48 k (native 29.97 / 25 fps) | ✅ |
| 2 | Words (WhisperX) + edges by ear-proxy (`win/snip*.txt`, `win/fine.py`) + picture edges (`win/fstep25.py`, per-frame luma) | ✅ 48.13 s |
| 2b | Raw sequence in ABW10 (30 fps), read-back verified, A1 re-ASR | ✅ v2 |
| 2c | His Tella direction | ⏳ waiting |
| 3–8 | Code build → export → QA → REPORT | pending (quote first) |
| — | Music | default none (his rule); the brief asks for a piano: open question |

## The cut (actual, from the read-back; source = each upload's own clock)
| Beat | Timeline | Source in → out (pieces) | Words |
|---|---|---|---|
| 1 | 0:00.00–0:11.00 | 60M 1:20.60–1:23.13 · 1:24.67–1:25.03 · 1:25.87–1:27.40 · 1:29.23–1:31.50 · 1:31.73–1:32.47 · 1:33.07–1:34.80 · 1:35.00–1:36.83 | Cooper: "the last thing Mummy saw on this earth was a flashbulb." Harry: "Yep." Cooper: "That's what you saw in the pictures?" Harry: "The pictures showed the reflection of… a group of photographers taking photographs through the window." |
| 2 | 0:11.00–0:19.60 | 60M 0:00.23–0:01.93 · 0:03.50–0:04.73 · 0:04.97–0:07.17 · 0:09.17–0:10.73 · 0:11.53–0:13.43 | Cooper: "You didn't believe she was dead?" Harry: "For a long time. I just refused to accept that she was gone. She would never do this to us, but also… maybe this is all part of a plan." |
| 3 | 0:19.60–0:21.33 | 60M 0:41.53–0:43.27 | "I had huge amounts of hope." |
| 4 | 0:21.33–0:34.07 | 60M 1:01.50–1:03.73 · 1:03.83–1:05.77 · 1:06.27–1:07.93 · 1:08.13–1:13.67 · 1:13.97–1:15.33 | Cooper: "Why did you want to see it?" Harry: "Mainly proof. Proof that she was in the car. Proof that she was injured. And proof that the very paparazzi that chased her into the tunnel were the ones that were taking photographs of her lying half dead on the backseat of the car." |
| 5 | 0:34.07–0:37.20 | 60M 1:47.80–1:49.73 · 1:49.97–1:51.17 | "All I saw was the back of my mom's head, slumped on the back seat." |
| 6 | 0:37.20–0:48.13 | ITV 0:47.20–0:48.13 · 0:48.73–0:50.07 · 1:05.20–1:06.33 · 1:06.87–1:08.80 · 1:11.90–1:12.63 · 1:12.93–1:17.80 | "I cried once, at the burial. And there we were, shaking people's hands, smiling. And the wet hands that we were shaking, we couldn't understand why their hands were wet, but it was all the tears that they were wiping away." HARD CUT |

V2: B4 1-frame crop fix (60M frame 2032) at 0:27.07 · B6 cover 0:39.47–0:42.53 = ITV Harry CU 0:55.00 (over the boys,
1997) · B6 cover 0:42.53–0:46.40 = ITV Harry CU 1:20.73 (over the walkabout + its dissolve) · B6 hold 0:47.80–0:48.13 =
ITV frame 1937 (the wide's last clean frame, over ITV's fade to black under "away").

## How it was built (re-run recipe)
```
python premiere/make_beats.py                                   # sources.json, beats.json, framing.json (effective edges)
python ../../presets/youtube-shorts/abundance-wisdom/resolve_beats.py . --fps 30              # -> edl.json
uv run ../../presets/youtube-shorts/abundance-wisdom/plan_placement.py . --fps 30 60M_Harry_2023@6.973633 60M_Harry_2023@86.953533 60M_Harry_2023@62.529133 60M_Harry_2023@63.663600 60M_Harry_2023@67.834 ITV_Harry_2023@76.04
python ../../presets/youtube-shorts/abundance-wisdom/place_sequence.py . "Harry Diana Photos - raw cut" "Harry Diana Photos" premiere/place.jsx
python premiere/run_window.py      # first time: state → his active → create_seq.js → place.jsx → restore his
python premiere/run_replace.py     # re-place: only if unchanged since premiere/v1/readback.tsv → clear_ours.js → place.jsx → restore
python premiere/pp.py premiere/fix_b4_frame.js ; python premiere/pp.py premiere/readback.js > premiere/readback.tsv
python win/verify_eff.py ; python win/verify.py ; uv run --with pillow python win/sim.py --readback proof/sim_readback.jpg
<gpu python> -I win/asr_a1.py ; uv run --with numpy python win/gap_check.py
```
**Re-place only if he has NOT edited the sequence** (`run_replace.py` checks that itself).
On a re-place, pass the TRUE cut `60M_Harry_2023@67.801067` (not 67.834) and skip `fix_b4_frame.js`: place_sequence already
re-pins razors from the in-points Premiere actually holds, so the one-frame-later split was what put the B4 razor a frame late.

## Notes for the build
- 60M: 60 MINUTES bug top-left; ITV: ITV NEWS bug top-right. Both outside the face crops. ITV's lower-third
  "'HARRY: THE INTERVIEW', ITV1" shows at the bottom of B6 "at the burial" (0:38.13–0:39.47): crop/push-in past it.
- ITV is 720p 25 fps (the best on YouTube): B6 needs the upscale most. The B6 wide (Harry seated, 0:46.40–0:47.80) is
  the softest shot.
- B6 opens on ITV's own fade-up from black (0:37.20–0:37.63).
- 60M's B4 has a medium shot (0:23.50–0:27.07 on the timeline) between close-ups.
