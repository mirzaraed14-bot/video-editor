# Onyx reactions: the LEAN recipe (2026-11-23)

**Affan, 2026-11-23:** "Samples can be heavy using sonnet as execution, reactions have to lean down." The week asks for 30 reactions, so
each one is built in **ONE fresh Sonnet session**, target **≤ $18 API-priced (0.8 % of the week)**. Batch 9 measured **$106 a reaction
(≈ 4.8 %)** with `workflows/session-cost.py` (split under "No longer done"). A reaction goes to ONE prospect with the approval ask.
**Fixed, never cut:** max 3:00 · his WHOLE credential intro · the V3 sound spec (`projects/_onyx-batch7-2026-11/REACTIONS-V3.md`
A1-A7 + V3.1: voice loudest, bed 19 LU under and OUT under every play, SFX ~12 dB under) · no insulting hook, their best moment plays ·
one build, one review, one fix round, deliver · never move his playhead, never parallel ASR · he exports himself · silence (never play media).

## Models
- **Session = Sonnet, effort high** (recipe execution, not creative). The launcher starts it and names the job in the first prompt.
  **Advisor OFF for this session** (`/advisor`), or never call it: at 100-300K context one Fable call costs $1-4 uncached. This is an
  exemption from Affan's "Fable as advisor for basically everything", on his 11-14 "do it quick … sent to 1 person" and his 11-23 words. APPROVED by Affan 2026-11-23 ("Yes, all three": the kit pilot capped at $60, no per-reaction catalog pass, no Fable advisor on reactions). Samples keep the full process.
- **Opus, 2 calls only** (Agent tool, `model: "opus"`, fresh context): the CUT (step 2, effort high) and the QC (step 5, effort medium).
- **Haiku** only for the day's prep (step 1, a pure command run). No other subagents, no Fable agents, no workflows.

## Step 0, once: the kit (guard)
Paths: `J=projects/<job>`, `KIT=presets/youtube-shorts/onyx-samples/kit/reactions`.
If `$KIT/KIT.md` is missing, **this session is the KIT PILOT**:
- `mkdir $KIT/.pilot`. If it already exists, another pilot is running: stop and tell the launcher.
- Freeze the kit, then build this reaction with it.
- Log it as `kit pilot`, cap **$60** for both; over that, stop and report.

The freeze reuses, it does not re-derive:
- Copy `projects/hpp-brad-pitt-f1-reaction/tools/`, the last batch-9 build (ABW11 create/addtracks, pacecheck, stagecheck, segasr).
  Add Lunch Table's `p2b4_measure.py`/`p2b4_solve.py` + `silhole.py`. Reference, not copy: `projects/_onyx-batch7-2026-11/reactions/tools7/`,
  `_onyx-batch9-2026-11/reactions/offgrab.py`, `_onyx-batch-2026-10/reactions/tools/dump.py`, `lanes/premiere/quietgate.py`.
- Replace every hard-coded job path/name with `$J` + `seq.json`. Grep `hpp-brad-pitt|High Performance|C1465|02-17-37`: 0 hits.
- ONE data-driven `build_plan.py` that reads the beats table of `$J/CUT.md`, instead of a hand-written beat list per job.
- Strip every Premiere grab: `lay3` ends in `--grab-only` when `work/grab-times.txt` exists, and that moves his playhead.
  `grep -E 'grab-only|--grab'` over the kit must return 0.
- `wholecut.py --model medium.en` (it hard-codes large-v3 today).
- One `gate.sh $J` that runs all of gate A and prints one PASS/FAIL line per check.
- Fixed MENU kinds (step 4) with type sizes baked in (labels 48-64 px, main 64-110 px, never < 40). One entrance, `slab`, no overshoot.
- The SFX palette = batch 9's clean Epidemic originals, copied into `assets/sfx/onyx-reactions/`. That folder is gitignored; `$KIT` is
  not, so audio never goes there.
- KIT.md lists the bed files by path (BEDS-b9 beds, in the batch-9 job folders).
- `prep.sh` (step 1) and `KIT.md`: ≤ 1 page, the exact command line of steps 1-6.

## Steps (rewrite `$J/BRIEF.md` ▶ STATUS at each step; BRIEF ≤ 30 lines)
1. **Prep (Haiku, once per recording day, ≈ $0.2; if `$J/work/tx.txt` is missing the session runs it for its own job).**
   `bash $KIT/prep.sh <job> <obs> <camera> <their-short> <our-yt> [<our-ig>]`:
   - copy (never move) the OBS file into `raw/`, `sync-dual-audio.py`;
   - transcribe ONCE with WhisperX large-v3 (CLAUDE.md), under the GPU lock, while Affan is NOT in Premiere; one ASR process on the
     machine (`.asr-lock`);
   - `work/tx.txt` (`tx.py`: compact lines with OBS times), the play map (`xplay2`: where each file plays), the avatar (og:image).
   - Stop at the first non-zero exit and report the tail. Never debug.
2. **Cut (Opus, one call, ≈ $1-2).** Reads ONLY `tx.txt`, the play map and the rules below. Writes `$J/CUT.md`:
   - the K table in `spans.py` format;
   - beats `| K | layout | menu item | exact copy |`;
   - the plays, the bed, and the predicted length.

   Sonnet never re-decides it.
   **Rules:**
   - **Keep:** the intro verbatim, "today we are going to be reviewing" to "let's get into it" (last clean take); every verdict and
     compliment; every point's setup line.
   - **Never:** cut a fact midway (a number, count, name, list or payoff, or a word that flips the meaning).
   - **Takes and ends:** the last take of a repeated line; end lines on their point; cut a stat aside as one unit.
   - **Hook and plays:** the hook is their channel tag, never a critique; their best moment plays with their own voice.
   - **Drop in order:** tangents, restarts, secondary critiques; fillers and false starts always go. Aim for 2:45-2:55.
   - **Text:** censor drug and self-harm words in the captions; card copy is his own words, ≤ 5, kind.
3. **Cut proof BEFORE any render (Sonnet, scripts).** `keep.json` from CUT.md (`keepjson.py`) → `$KIT/cutchain.sh`, the
   `cutbuild` chain batch 9 actually ran on HPP (Opus ruling 2026-11-23; cutv3 was On-That-Note-only); `cutproof.sh` runs the proofs below. Every proof must pass:
   - `pacecheck`: talk pauses ≤ 0.30 s, head and tail air ≤ 0.12 s;
   - silencedetect on the cut voice at −50 and −40 dB: no hole > 0.30 s;
   - ONE whole-cut ASR (`wholecut.py --model medium.en`, allowed while he edits; `.asr-lock`), diffed word by word against CUT.md:
     every K word heard, no doubled word or take, one "Gentlemen", no filler;
   - ≤ 180 s.

   A failure is re-cut HERE: batch 9's re-cuts after placement were most of its fix rounds.
4. **Build + place (Sonnet, kit commands).** These defaults are fixed, never re-decided:
   - **Layout:** SPLIT all through. A card or the static screen view he is talking about sits in the top panel, his face in the bottom,
     and the captions on the seam (y 1038). A FACE beat only where `facev3` puts the lips ≤ y 965 at scale ≤ 150.
     The top panel is never empty. Crop out the Claude app, browser chrome, the taskbar and his own facecam inset. No push-ins or
     keyframes. Plays open on their play card with the screen off (`screenoff`).
   - **MENU, 8-12 graphics, nothing else:** a channel card (real avatar) on the hook; 2-3 credential cards over the intro; a play
     card per play; one theirs-vs-ours side-by-side; 2-4 number cards (the number shown on their screen); 1-2 pointer marks.
     One soft SFX cue per entrance; exits are silent.
   - **Sound:**
     - `BED_TRIM=-7 bash $KIT/audchain3.sh -24`, with the bed rotated from `projects/_onyx-batch9-2026-11/reactions/BEDS-b9.md` (no new searches);
     - `sfxprep3` + `sfxassign3 --apply` (`MARGIN=4.3`);
     - `tlsynth7`, then `A2_WANT=19 A2_MIN=16 A2_MAX=25 tlmix7 --cached`: A1-A6 must pass before Premiere;
     - `bleed7`: a hit > −30 dB → cut the span at a thought boundary; else one `voiceclean7` try; else accept ≥ 28 dB and note it.
   - `facev3 --write`. Render `mgall3` through `sem.sh` (one render at a time). ffprobe the captions `.mov` against the length.
   - **Premiere** (the open project, template "Onyx reaction template (empty)", `premiere.lock` released by absolute path, QUIET-MODE
     as the launcher set it, gated steps through `quietgate.py` in the background):
     - ONE hold for `premo3.sh $J import,create,addtracks,redo,lay3,screenoff`. Never its `grabs`/`check` phases (they move his playhead).
     - Then `dump.py` by name → `offgrab.py --grid 1.5 --edges --sheet`.
     - Then P2b ONCE: `p2b4_solve` on those frames with the hard cover bound (every split face top ≤ seam − 2), applied by name,
       re-dumped. Residuals are judged by eye.
     - Restore his sequence, save. Never export.
5. **The gate (once; see below).**
6. **One fix round (Sonnet, ≤ 40 min).** Only the listed defects, at their source:
   - a cut defect → re-cut + the step-3 proofs;
   - an overlay → re-render that one file under a new name, swap it by name.

   Then gate A again, and Sonnet looks at the fixed spans' offgrab frames. No second QC, no rebuild of the look. Leftovers go into the delivery note.
7. **Deliver + log.**
   - BRIEF ▶ STATUS = PREPARED.
   - Report to the launcher: sequence, exact length, gate A numbers, residuals. He exports himself to `X:\Claude Projects\Exports\`.
   - His later notes: one fix session, only what he named; the lesson goes in `LESSONS.md`.

## The single QC gate
- **A, scripts (`bash $KIT/gate.sh $J`), all green before B:**
  - `applyo.py --verify` 0;
  - placed `tlmix7` A1-A6 (bed 19 LU, min 16, max 25; every 3 s window ≤ −4.0 dBFS) + `bleed7` A7;
  - `premcheck6` 0, `claudecheck_o` 0, `leakcheck` 0;
  - the seam check from the readback, as `seamcheck.py` does it (Opus ruling 2026-11-23): the UNCROPPED layer top ≤ seam − 2 and the visible (cropped) top ≤ seam + 1;
  - `stagecheck`: no empty or black top-panel frame at a butt;
  - captions from frame 0 to the end;
  - sequence end ≤ 180.0 s;
  - offgrab `REPORT.txt` lists no unmodelled layer.
- **B, Opus, one fresh call (≈ $1-2).** Reads ONLY CUT.md, the whole-cut ASR text, A's numbers and the offgrab sheets. It fails
  objective defects only:
  - **cut:** C1-C3, the intro whole, verdicts kept, the hook kind;
  - **picture:** captions on lips, two camera images, a frame edge or black band, desktop/Claude app/chrome, an empty panel, text
    < 40 px or cut off, a number card that disagrees with their screen, a head jump that reads as a jump.

  It returns numbered defects with times, or PASS. A static held page is NOT a defect (V3 P2: views stay static).

## No longer done, and why
- **A per-reaction Opus planner** with a 40 KB PLAN.md and the full catalog pass (CATALOG.md + 137 stills), $26 a reaction → one Opus
  cut call on the compact transcript. The catalog pass is done ONCE, in the kit's menu. This is an exemption from CLAUDE.md loop 5
  (APPROVED by Affan 2026-11-23, "Yes, all three", relayed by the hub); BRIEF keeps one line, "better than the last: ___".
- **An Opus hub steering builders** ($16) → none; the launcher only starts sessions.
- **Builder shifts** that each re-read four briefs, copy and hand-patch ~50 tools and write a 250-line `build_plan.py` ($23) → one
  session on the frozen kit.
- **Main's frame looks, fresh-eyes reviewers and fix rounds 1-4** ($41) → one gate, one fix round. "Phases every 1-4 s" and other
  taste calls are not defects.
- **Fable advisor calls** ($16) → none; Opus judges the cut and the QC.
- **Job-local kinds, per-reaction entrance signatures, per-graphic stills, new SFX and bed searches** → the kit menu, the palette, the bed rotation.
- **P2b re-solve loops chasing 3 % / 15 px** → one solve with the cover bound (memory: "reactions fast, not perfect").
- **Premiere frame grabs** (they moved his playhead), per-segment ASR and play-stem ASR → offgrab, and one whole-cut ASR.
- **The max-effort gate is not triggered:** no sequence goes to Affan before a reaction build.

## What the fresh session reads
- **Only:** the launch prompt (job, OBS, camera, their Short, our sample file(s), prospect, sequence name), this file and `KIT.md`.
  CLAUDE.md and memory load themselves.
- **Never:** REACTIONS-V3/V2, RECIPE-V3, the R7/R9 briefs, LESSONS, PLAYBOOK, CATALOG, other jobs' PLAN/BRIEF/RUN, or kit source
  (only a failing command's lines).
- **Output discipline:**
  - every command `| tail -n 5`; never a whole JSON or transcript;
  - images only at gate B (Opus) and for the fixed spans (Sonnet);
  - at most 2 reaction sessions at once (GPU, `sem.sh`, the Premiere lock, ≥ 3 GB free RAM).

## Cost log
- Last command: `python workflows/session-cost.py --job <job> --since <this session's start, UTC> --quiet`. It sums this session,
  its Opus subagents and any advisor. Check that the `sessions` list in its line is this session only; a launcher that named the job
  would inflate it.
- Append one row to JOBS.md § Cost log: `| date | job | reaction (lean) | length | % | $ | gate: n defects, fix y/n | note |`.
- The % is at $22 per %. The 11-23 meter check read ≈ $27 per %, so the log errs high.
- **Stop rule:** a reaction over $25 (≈ 1.1 %) → stop before the next one and tell the launcher where it went (the script's per-agent lines).
