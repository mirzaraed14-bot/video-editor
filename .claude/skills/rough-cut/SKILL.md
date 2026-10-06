---
name: rough-cut
description: "Rough-cuts videos from raw clips, every format (short-form reels and long-form YouTube alike, the universal step 2). Transcribes with WhisperX (large-v3 + wav2vec2 word-level alignment), kills filler + dead air, keeps only the essential lines, stitches with FFmpeg. No captions, no B-roll — just a tight rough cut ready for final polish. Triggers: rough cut, cut this video, trim this, chop this up, rough-cut, make a rough cut, tighten this cut. (Whole-line phrasings — 'edit this video', 'do the whole edit', 'edit the latest project' — belong to `edit-video`, the orchestrator: this skill is step 2 of that line.)"
---

# Rough Cut — Transcript-Driven Edits

Raw talking-head clips into a tight rough cut: you transcribe, you decide the cuts, FFmpeg stitches. The goal is the **shortest reel that still delivers the value.**

## How to Trigger
- **"rough cut [job name]"** → that job folder; **"rough cut"** / **"cut this reel"** with no job named → the newest job folder (a path picks that folder)

---

## Folder Contract

**This skill starts at transcription.** Creating the job folder, copying the raw into `projects/<job>/raw/` (never moving it) and naming the job are step 1, Intake, owned by `edit-video` (layout + naming: CLAUDE.md § Folder Structure and § Job naming). No job folder yet → do intake first; if the content isn't obvious before transcribing, use a provisional folder and rename it before the splice.

Three durable paths get written under `projects/<job>/`: `transcript/words.json` (the canonical transcript), `transcript/cuts.json` (the EDL), `outputs/<job>.transcript.json` (the cut-aligned caption transcript). Scratch lives in `/tmp/video-editor/<job-name>/`, which macOS clears — never depend on anything living solely in `/tmp`.

**Intent is derived, never asked.** If `intent.md` exists, read it. Otherwise read the FULL transcript first and work out the hook (the strongest curiosity/tension line, often filmed mid-take and re-orderable to the front) and the takeaway (the one thing the viewer should leave with), then cut to serve those. No usable dialogue? Sample frames (`ffmpeg -ss <t> -i <clip> -frames:v 1 <out.png>`) and infer the subject + arc from what's on screen. State your read in one line of the report.

---

## The Edit Philosophy (non-negotiable)

**Short and snappy, max value per second.**

Every cut decision runs through this filter: **does this line deliver value?** (if not, kill it) · **is this the tightest version?** (if not, use the shorter take) · **would a viewer skip past this?** (if yes, it's dead).

**RELEVANT IS NOT NECESSARY — the #1 filter (2026-08-28, after a first cut ran
3:32 that should have been 2:00):** "just because it's relevant doesn't mean that it's
necessary... stuff that's like okay, cool, good to know, instead of need to know right now,
is fluff." A line survives only if the viewer NEEDS it right now, for understanding or for the
flow of the script; good-to-know context, how-I'll-do-it teases, second statements of a point
already made and warm-up framing are all relevant and all dead, and a prerequisite aside that sends
the viewer off to do a step the video is about to show anyway — when the two lines around it join
cleanly without it, it goes. (This is not the same as a preamble that sets context or a setup clause
its own next line depends on: those stay.) **The kill rate is an OUTCOME,
never a target (2026-09-04):** emphasis-heavy multi-take footage has landed at 60-75%
killed, a take where the speaker nailed the script might lose 20-30%, and whatever total the
necessity question produces is the right cut. The red flag is a kept line that fails that
question, never "kept more than half". An intro especially is pure momentum
(claim → problem → rules → stakes → go) — every beat that doesn't advance it goes.

**Format is auto-detected from the raw footage, never asked** — resolved at `edit-video` Step 0 and written into RUN.md; probe every clip only when this skill runs alone (`ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 <clip>`): **vertical** (height > width) → short-form, **horizontal** → long-form YouTube. State the detected format in the report.

**Target length depends on that format:**
- **Short-form** (9:16 Reels/TikTok/Shorts) → aim **1–2 minutes**, the target *after* ruthless cutting, not permission to ramble. If the value fits in 40s, ship 40s.
- **Long-form** (16:9 YouTube) → **no length cap**, but no cap is not license: the necessity filter still governs. Cut for retention and structure, not to hit a number.

---

## Auto-Kill Rules (always apply)

When building `cuts.json`, automatically remove:

| Kill | Why |
|------|-----|
| Filler words: *um, uh, like, you know, so yeah, basically* (when vestigial) | Dead weight |
| Stutters + false starts: *"I- I was gonna-"* | Breaks flow |
| Restarted takes | Keep the **last** take, kill the rest — you always want the latest take of a repeated line (warmest delivery). Don't compare takes. |
| Emphasis echoes: the same claim re-stated for punch (*"one prompt, one shot, one go... it was literally one prompt..."*) | Keep the STRONGEST single statement of each claim; every echo after it is fluff. A hook montage of restatements collapses to one claim + at most one punch ("One shot."). |
| Silences ≥ 0.65s (MEASURED on the envelope, not read off the transcript) | Dead air. `polish-boundaries.py` splits any interior quiet run ≥ 0.65s whatever the timestamps say — the aligner can stretch a low-probability word across a pause so no inter-word gap exists. Author the transcript-gap split anyway; the polish pass is the net.§ mechanism (8). |
| Tangents + asides that don't serve the hook/takeaway | Viewer time |
| Throat-clears, "okay let me start over" | Production noise |
| Orphan low-prob word before a kept take | A lone low-confidence word (prob ≲ 0.3) with a ≥1s gap right before a kept take is a false start WhisperX half-missed. Kill the fragment and start the segment at the real take; never keep the orphan as its own segment. |
| Preamble before the hook lands | Every reel opens ON the hook |
| Trailing verbal tics after a landed point: *"...5X more usage, okay?"* → cut at "usage" | The point landed; the tic is a ~0.5s tax. Mid-sentence tics are rhythm — keep those. |
| Meta-signposts about the video's own structure: *"so now what I'm going to do is cover..."*, *"you can skip to the next section"*, and how-I'll-do-it teases: *"my plan is to build a preset"* | The content announces itself. All three die — preview, skip-ahead courtesy, AND method tease (2026-08-28: "it's just fluff... obviously I'm gonna explain how I do it later in the video"). |
| Self-referential flexes: *"personally, I'm on the $200 a month plan"* | Status talk, not information. |

**The closing beat is content.** The filmed closure and handoff — the sign-off, the goodbye, the handoff into whatever comes next — is not a disposable meta-signpost: keep it complete unless the user explicitly asks to remove it, and never reduce the closing passage to its final sign-off. Inside that passage the normal rules still apply: pauses, tics, false starts and retakes go, and a repeated sign-off collapses to the last take.

**Preserve the creator's cadence.** Don't surgical-kill every "like" — some are rhythm, some filler. Taste call.

**The keep/kill line (your 2026-07-29 hand pass): persuasion and personality are CONTENT — meta-narration is not.** Objection-handling ("can I do this on the free plan?"), the pitch, the value stretch, the walk-back for budget viewers, section preambles that set context — all of it stays, even in an "essentials only" cut. What dies is talk *about the video*, talk *about the creator's status*, and tics. Cut harder = tighten inside lines before deleting persuasion beats.

---

## The Pipeline

### Transcribe

Find the job folder, then:

```bash
bash.claude/skills/rough-cut/scripts/transcribe.sh <job_dir>
```

WhisperX (large-v3 ASR + wav2vec2 forced alignment) writes true word-level timestamps to the canonical `projects/<job>/transcript/words.json` (plus a scratch mirror under `/tmp`).

**First run builds the venv** at `~/.cache/video-editor/whisperx-venv` (several GB, several minutes) plus the large-v3 + wav2vec2 weights; a `.deps-ok` sentinel rebuilds cleanly after an interrupted install. Later runs start in seconds.

**Hardware is auto-detected:** an NVIDIA GPU (Windows/Linux) runs CUDA float16 behind a fallback ladder (cuda float16 → cuda int8_float16 → cpu int8), so a broken CUDA stack warns and degrades instead of blocking; Apple Silicon stays CPU int8 (locked — GPU torch is flaky there). `WHISPERX_DEVICE=cpu|cuda` overrides. Details: the engineering archive.

**This is the ONE transcription for the entire pipeline — rough cut AND finishing captions.** The canonical `words.json` is **reused forever**: re-running `transcribe.sh` skips WhisperX (`--force` to redo). Nothing downstream transcribes this footage again — the locked caption presets and `graphics-plan` consume the derived `outputs/<job>.transcript.json` instead (see Splice + Handoff).

**Add `--diarize`** to label each word with a speaker: needs `HUGGINGFACE_TOKEN` in env and the pyannote/speaker-diarization-3.1 model accepted on HF.

**Run in background** over 3min of total clip length (`run_in_background: true` + Monitor). CPU timings: ~30s of clip = ~10-20s wall (first run slower, model downloads), ~5min = ~2min; CUDA is several times faster.

### Author the cuts

Read `projects/<job>/transcript/words.json`. Each clip has a `words` array of `{w, start, end, prob}` (plus `speaker` under `--diarize`).

Apply the auto-kill rules and the edit philosophy. Output `/tmp/video-editor/<job-name>/cuts.json` — the path `splice.sh` reads, overwriting the job copy from it (see Gotchas) — in this shape:

```json
{
  "segments": [
    { "clip": "clip-02.mov", "start": 1.24, "end": 4.60, "transcript": "Are you still paying a VA three grand a month" },
    { "clip": "clip-01.mov", "start": 12.20, "end": 18.80, "transcript": "..." }
  ]
}
```

**Timestamp rules:**
- Trust WhisperX timestamps for WHICH words to keep, not for edges: word STARTS run ~50-100 ms late vs the real acoustic attack, word ENDS run early vs the decay. Exact boundaries are dialed by the refiner (below), not by you.
- **A low-probability boundary tail means the TIMESTAMP is fiction, not just soft (your-job, 2026-08-28).** When a boundary word or its 1-2 neighbors carry prob < 0.3, measure the real edge on the raw envelope with a WIDE window — up to the next raw word, NOT `word.end + 300 ms` — and require a sustained drop before cutting; a capped search lands mid-word and chops the line. Related: a mid-speech "graft" is only legitimate when the adjacent word is KEPT, so a graft against a KILLED region means the measurement failed. **Both are enforced by `polish-boundaries.py` — run it every job; its ⚠ lines are these cases surfacing.**
- **Merged repeats: an immediately repeated word ("However... However,") can collapse into ONE transcript entry spanning every utterance**, so a cut keeping it keeps the stutter. `transcribe.sh` flags long-span words (> 1.0s, and > 0.5s at p < 0.5); the refiner snaps a segment starting on one to the LAST utterance, trims one ending on it to the first, and warns on mid-segment ones (split the range at that word). **On screen-recording footage (OBS) the auto-fix fails SILENTLY** (1 caught of 4 real), so treat every ⚠ long-span word on a boundary as unverified there: measure the raw with a 10 ms RMS envelope, then pin the boundary as explicit start/end + `"no_refine": true`, or the refiner searches from the bogus word end and undoes it. Interior ⚠ words and quiet runs under ~0.3s are fine.§ mechanism (5).
- Start on the first word you want, usually `word.start - 0.03` to `0.08`; end after the last, usually `word.end + 0.04` to `0.10`.
- **Segments must never overlap in the source — a continuous split shares ONE boundary time.** Split a take with nothing removed between the halves and the pads point at each other: `word.end + 0.08` out and `next_word.start - 0.04` in put the SAME frames in both segments, played twice as a 1-15 frame stutter. Write `"end": T` on one and `"start": T` on the other, one shared value in the inter-word gap. Padding is for a real cut, where the pads open outward into different silences. `refine-cuts.py` repairs overlaps and `splice.sh` hard-aborts on survivors, naming YOUR segment numbers.§ mechanism (6).
- Don't cut mid-word; a clipped transition means adjust `cuts.json` and rerender. Segments CAN cross clips in any order.
- **The graft — splice restarts mid-sentence, don't cut at sentence boundaries.** When the speaker restarts a thought ("...we need Claude Code. Okay, we need Claude Code for it to..."), end segment A *through* the repeated phrase in take 1 and start segment B in take 2 *right after* the restated words (at "for it to..."): one continuous sentence, zero duplication. Prefer-last-take governs *full retakes*, the graft governs *mid-thought restarts*.
- **Orphaned connectives — when you kill a line, kill the words that answered it (you caught this on your-job, 2026-08-28).** Rebuttal/contrast frames ("But the reality is...", "That's why...", "So instead...") answer the PREVIOUS sentence, so keeping the counter while cutting the claim leaves a "but" contradicting whatever now sits before it. Re-read the cut sheet as one continuous script and check every segment's FIRST few words: does the connective still refer to something that survived? If not, start the segment after it. Same check on deictics. **And the reverse: a beat that only makes sense WITH its framing clause dies whole when the clause dies.** **The framing clause of a KEPT beat is part of the beat (2026-09-07):** "and after receiving a ton of feedback from my customers, my audience, my community" was killed as good-to-know credibility, and the next line, "I noticed one huge problem...", is its ANSWER, so "I noticed" hung off nothing ("that fucks up the flow"). Before killing any "after / because / from my..." setup, read the line that follows: if it opens with noticed / found / realized / learned / saw, the setup stays. The necessity filter is for echoes, teases and warm-up, never for the cause half of a cause-and-effect sentence.
- **NEVER author extra tail for emphasis — every tail is uniform (RETIRED 2026-08-31, you).** Every boundary is the measured decay + 70 ms, every segment, no exceptions. The old `"air": <sec>` field is gone from `refine-cuts.py` and `polish-boundaries.py`, so a stray `"air"` in an old `cuts.json` is inert. A beat that needs room is a timeline call.§ mechanism (7).
- These pads are a starting point: `splice.sh` runs `refine-cuts.py` first, which measures each boundary word's acoustic onset/offset on the raw and nudges the cut just outside it (in = onset − 40 ms, out = offset + 50 ms), clamped inside the local gap and capped relative to its own word (250 ms lead, 300 ms tail); continuous splits get one shared boundary, joints resolve PAIRWISE. Watch the `[refine]` report — `cut was N ms INTO "word"` lines are clipped attacks it saved. `REFINE=0` disables the pass; `"no_refine": true` pins a segment (an overlap against a pinned side moves the UNPINNED side only). Mechanics: the engineering archive § mechanisms (4) and (6).
- **Refinement is NOT idempotent — repair a shipped EDL with `refine-cuts.py --repair-only`, never a second full pass.** The refiner measures from the authored cut, so a second pass re-measures from the moved boundaries and drifts tails further out (+0.4s observed). `--repair-only` runs ONLY the pairwise joint resolution with zero re-measurement, so only overlapping joints move.

Include the `transcript` field on every segment so the cut sheet reads on its own.

### Splice (EDL-only by default)

**The editing-app finish IS the default (2026-08-28): a bare "rough cut" with no lane named means EDL-only mode + automatic Premiere handoff — NEVER render:**

```bash
RENDER=0 bash.claude/skills/rough-cut/scripts/splice.sh <job_dir>
```

~8 seconds: boundary refine + frame-snap + persisted EDL + corrected canonical transcript, no ffmpeg encode. Nothing on an editing-app path reads the flat MP4. Go straight to the timeline (clients: `capcut` / `davinci-resolve`), then the **audio polish** (step 3, the house chain as clip effects — see `premiere-pro`). The full render below is **only** for the chat-only/HyperFrames lane, never inferred: it runs when a client with no editing app has explicitly said to do it in chat.

```bash
bash.claude/skills/rough-cut/scripts/splice.sh <job_dir>
```

Dials every boundary against the raw audio (`refine-cuts.py` — see Timestamp rules), then writes `outputs/<job-name>.mp4` in a **single FFmpeg filtergraph**: one `trim`/`atrim` per kept segment → `concat` → static gain → limiter, encoded once. Audio rides through **lossless (PCM in-graph)** and is polished **once** on the assembled track (measured amplify from `workflows/voice-gain.py`, kept speech → −17 LUFS pre-limiter → −6 dBFS hard limiter → AAC 256k), **never** per-segment (boundary click-pops). Video and audio trim from the same in/out, so A/V stay locked by construction.

It also writes **`outputs/<job-name>.transcript.json`** — the cut-aligned caption transcript, the kept words remapped through `cuts.json` by `export-transcript.py`: timestamps rebased to the edited timeline, **zero re-transcription.** This is what finishing/captions/graphics consume.

**Spelling/brand fixes happen HERE, once.** `export-transcript.py` applies [`transcript-corrections.json`](../../../transcript-corrections.json) as it writes the canonical transcript: `auto` entries (non-word mishears + brand/name casing) swap silently, `flag` entries (real words that might be mishears, e.g. `cloud`) print for eyeballing. Because this is the one source of truth downstream reads, the fix propagates everywhere. The raw `words.json` is untouched; per-video one-offs go in `projects/<job>/corrections.local.json` (same `{auto,flag}` shape, merged on top). Watch the splice log for `auto-fixed:` and `⚠ REVIEW`. Rationale: the engineering archive.

**The full render runs 15-45s per 60s of output — background it.** `RENDER=0` is ~8s, foreground.

### Polish the boundaries (ALWAYS, every job — added 2026-08-28)

```bash
uv run.claude/skills/rough-cut/scripts/polish-boundaries.py <job_dir>
bash.claude/skills/rough-cut/scripts/splice.sh <job_dir>     # RENDER=0 on app-finish jobs
```

The refiner leaves two classes of boundary unmeasured: dead-air kills between adjacent transcript
words are classified "continuous split" and skipped, and its absolute thresholds clip soft decays or
count breaths as tails. This re-derives EVERY boundary peak-relative (local floor, threshold
`max(floor+10dB, peak−28dB)`, decay capped at word.end+300ms, uniform out = decay+70ms /
in = onset−40ms on every segment), widens the search on low-probability boundary words, sweeps every
segment's interior and splits any quiet run ≥ 0.65s, and pins everything. Run the FIRST splice with
`RENDER=0` on every lane, chat-only included — the real render belongs AFTER this step. Already
hand-pinned (`no_refine`) segments are left untouched, which makes the step idempotent. **Heed its ⚠
lines** — clipped words, merged repeats, possible flubbed takes; each gets verified (slice-ASR the
span — see § Fresh-eyes second pass — or fix the boundary by hand) before the cut ships. Then re-run
splice.sh to consume the pinned EDL.§ mechanisms (7) and (8).

### Final dialogue dead-air gate (required before handoff and after EDL changes)

Run `uv run workflows/dead-air-qa.py <job_dir> --json <job_dir>/transcript/dead-air-qa.json` against the final saved EDL, including pinned segments. This read-only check uses the original dialogue audio, so music and SFX cannot conceal a pause. It bridges brief room-noise spikes and measures across edit joints. Every flagged ≥0.65s run must be checked acoustically and corrected if it is dead air. `no_refine` protects a measured boundary; it does not prove a pause was reviewed or intentionally retained.

Also inspect transcript gaps ≥0.65s as independent review candidates. A quiet detector passing, timeline clips being contiguous, and an export decoding successfully are separate checks; none is a substitute for reviewing the actual pacing. After a repair, rerun this gate and verify live V1/A1 source ranges match the audited EDL. Never declare the rough cut clean from timeline contiguity alone.

### Transcript QA (auto, every run)

The static dictionary only fixes mishears it knows. This catches the **new** ones — names/brands WhisperX mangled. **Run it every job, right after splice:**

```bash
uv run.claude/skills/rough-cut/scripts/scan-transcript.py <job_dir>
```

(Windows has no system wordlist — the scan reports nothing there, so skip this step.)

It compares every word against a 235k-word English wordlist (+ inflection stripping) and the dictionary, printing only the **suspects**. Clean transcript → empty; otherwise a short list with context: `higsfield  ×1  …built it on higsfield and pushed to…`.

**Judge each suspect in context:** single token, recurring name/brand (`higsfield → Higgsfield`) → [`transcript-corrections.json`](../../../transcript-corrections.json) `auto`, fixed everywhere forever · one-off → `projects/<job>/corrections.local.json` · **multi-token mishear** ("higs field" → "Higgsfield") → **never** auto-apply (it changes word count and breaks per-word timestamps), flag it · already-correct proper noun → skip.

Then re-apply (instant, timings + cuts untouched):

```bash
bash.claude/skills/rough-cut/scripts/reapply-corrections.sh <job_dir>
```

**Hard rule:** only auto-apply **single-token, whole-word** swaps — the dictionary mechanism enforces this, which is why it can never shift a timestamp or alter a cut. Unsure? Flag it.

### Fresh-eyes second pass (ALWAYS, every job — 2026-08-28)

The author grading their own cut is why first cuts ship flaws. Before reporting (and before the
timeline replay on app-finish jobs), fan out **two subagents one tier below this session's model**
(the ladder and the inherit trap: `edit-review` § Token efficiency), one pass, not a convergence
loop (that's `edit-review`'s territory):

1. **Script-flow reviewer.** Input: the cut sheet's transcript column as ONE continuous prose
   script (+ this skill's taste rules, self-contained in the prompt). Finds only: orphaned
   connectives, dead deictic antecedents, echoes kept more than once, fluff (good-to-know vs
   need-to-know-NOW), a beat stripped of its framing clause, meta-signposts / method teases (excluding the protected closure/handoff),
   momentum breaks, and a missing or chopped ending against the raw closing passage. Findings must quote the exact lines.
2. **Mechanical reviewer.** Input: the polish-boundaries ⚠ list, the transcript, the words.json
   probabilities. Verifies every ⚠ by slice re-ASR — extract the boundary's raw-audio span (±4s)
   with ffmpeg, transcribe it independently (`uvx --from mlx-whisper mlx_whisper --model
   mlx-community/whisper-large-v3-turbo`), diff what was said against what the cut keeps. Catches
   fictional tails, missing sentence completions, and flubbed takes (an alignment-collapse cluster
   + an untranscribed speech burst nearby = a bad take to kill, not a boundary to fix).

Launch both in the background and do not poll for them (the harness notifies on completion; a grep
loop never matches and burns its whole timeout). Main session adjudicates: mechanical defects get
fixed (boundary moved, take killed, graft moved), flow findings are judgment calls decided against
the taste rules, and only the CHANGED segments get re-checked. Then report. Why this pass exists: the engineering archive.

### Report back

Show the creator: the detected format + the hook/takeaway you inferred (one line, where a wrong read
gets corrected), final duration vs raw total, and the cut sheet. On the default (`RENDER=0`) lane
report the segment count, `transcript/cuts.json`, `outputs/<job>.transcript.json` and the timeline
the EDL was replayed onto — **there is no flat MP4, do not report one.** Only the chat-only /
HyperFrames lane reports `outputs/<job>.mp4`.

```
✂️ ROUGH CUT DONE

📊 3:47 → 0:48 (79% cut)  ·  33 segments
📁 projects/<job-name>/transcript/cuts.json  →  replayed onto <timeline>
   (chat-only lane instead: projects/<job-name>/outputs/<job-name>.mp4)

CUT SHEET:
1. [clip-02 @ 1.24-4.60] "Are you still paying a VA three grand a month"
2. [clip-02 @ 4.95-8.10] "to do shit Claude Code can do for free"
...
```

Flag a weak segment: **"⚠️ segment 3 is borderline — consider killing."**

### Learn from the hand pass (Premiere-finish jobs)

When the creator hand-adjusts the cut on the Premiere timeline, **diff their edit against the EDL and fold the delta back into taste** — their trims ARE the ground truth this skill approximates:

```bash
node lanes/premiere/premiere-bridge.mjs diff-edl projects/<job>/transcript/cuts.json [more cuts.json...]
```

It matches every timeline clip to its EDL segment by source overlap and prints deletions, boundary trims/extensions (with the words at each moved boundary), grafts, and new material. Recurring pattern → a new Auto-Kill row or timestamp rule here; one-off → the job's notes. The 2026-07-29 rules came from exactly this diff. After a hand pass the **timeline is the source of truth** — never re-replay the EDL over it.

---

## Gotchas

- **A raw whose audio starts later than its video cuts in the wrong place (2026-10-06).** `transcribe.sh`, `refine-cuts.py` and `polish-boundaries.py` all read the audio as a plain file (time 0 = the first audio sample), but `splice.sh` trims on container time. yt-dlp `--download-sections` files start the video on the keyframe before the section and the audio later: offsets of 0.05–4.9 s on batch 1, so every cut landed that much EARLY in the speech (clipped word ends, kept fragments). **Check at intake** (`ffprobe -show_entries stream=codec_type,start_time`) and, if the starts differ, normalise before transcribing: `ffmpeg -i in.mkv -map 0:v:0 -c:v copy -map 0:a:0 -af "aresample=async=1:first_pts=0" -c:a flac out.mkv` (pads the audio with silence to time 0; sync unchanged, verified by cross-correlation). Keep the download in `work/raw-orig/`. A job already transcribed on an offset raw needs `transcribe.sh --force` after the fix.
- **A stammer can hide INSIDE the word stamps (2026-10-06, Rollo).** WhisperX stretched "call" over an "It's uh…" false start and put "it." on a cut-off syllable, so the transcript showed no gap and the cut kept ~1.4 s of stammer + dead air at a segment's tail (QA found it as uncaptioned audible speech). Slice-ASR the LAST ~1.5 s of every kept segment, not just the joints, and distrust any word far longer than its syllables ("It's" stamped 0.66 s). Fix the words' times in `words.json` and re-splice; don't caption the filler.
- **`-c copy` alone desyncs A/V on arbitrary cut points** — `splice.sh` trims and concats in one filtergraph, encoding once. Never "optimize" to stream copy.
- **Don't auto-snap cuts to silence.** WhisperX word alignment is the unlock; silencedetect snapping moves chosen boundaries into filler words or awkward pauses. (The refiner and `polish-boundaries.py` are NOT this: they keep the chosen word fixed and only dial the cut against its measured acoustic edge, clamped inside the local gap.)
- **Whisper can mishear.** Cross-check before killing a line — "Claude" becomes "cloud" and the line looks wrong when it's fine.
- **`splice.sh` reads `/tmp/video-editor/<job>/cuts.json`, NOT `transcript/cuts.json`**, then overwrites the job copy with what it spliced. Re-cutting an already-cut job replays the STALE `/tmp` EDL and silently clobbers the new cut sheet. Write the new cuts to the `/tmp` path (delete `cuts.refined.json` + `cuts.snapped.json` alongside it) first.
- **Transcribe.sh auto-skips** when `projects/<job-name>/transcript/words.json` exists. Use `--force` only if the raw footage actually changed.
- **Multi-section jobs: each newly filmed section runs as its own sub-job under `projects/<job>/sections/<name>/`** (raw symlinked from the parent's `raw/`, its own `transcript/` + `outputs/`). This exists because of the auto-skip above: point a new section's transcribe at the main job dir and it silently reuses the WRONG `words.json`/`cuts.json`. (Same nesting the clipper uses.)
- **Clip order in `cuts.json` = final order in the reel.**
- **Questions are a last resort, not a step.** Intent comes from the transcript (or sampled frames on a visual-only edit), format from the clips' aspect ratios. Never ask for those; infer, state your read in the report, let the creator correct it. Ask only when something is genuinely undecidable, and then one question, one sentence.

---

## Handoff

A restored or appended passage changes the final transcript and duration: refresh the canonical cut-aligned transcript, then send the affected window back through graphics planning/build, SFX, and final verification. A dialogue repair is not a finished passage while its required visuals or sounds are missing.

The cut lands on the finish surface; the line continues in `edit-video` (repo-root `CLAUDE.md` has the eight-step flow).

**Transcribe-once is a contract, not a convenience.** Everything downstream reads the canonical `outputs/<job>.transcript.json` — including the locked caption builders ([explainer](../../../presets/instagram/explainer/captions-style.md), [tiktok/raw](../../../presets/tiktok/raw/tiktok-raw-style.md)), which never re-transcribe.

This skill does ONE thing: cut the reel to the essential lines (audio is normalized as part of the cut). No captions, B-roll, zoom effects, or vertical reframing.
