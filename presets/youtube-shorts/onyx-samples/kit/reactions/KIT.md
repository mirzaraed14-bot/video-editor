# Onyx reaction KIT (frozen 2026-11-23, pilot part 1)

The recipe is `presets/youtube-shorts/onyx-samples/REACTIONS-LEAN.md`; this file is the how. Everything lives in `tools/` (flat, so every sibling import resolves).
`J=projects/<job>` · `KIT=presets/youtube-shorts/onyx-samples/kit/reactions` · `T=$KIT/tools` · run from the repo root, Git Bash, forward slashes. Every `*.sh` takes `--help`; `DRY=1` on prep/mgall3/audchain3/premo3 prints the plan and runs nothing.
cv2 tools (facev3, p2b4_measure, headjump, headlock, mouth) need `PYTHONPATH="X:/Claude Projects/.pylib-cv2"`; numpy/scipy audio tools run on `~/.cache/video-editor/whisperx-venv/Scripts/python.exe` (the scripts pick it).
Shared lock files stay where every other session looks for them: `projects/_onyx-batch2-2026-10/.locks/` (premiere, gpu, youtube) and `projects/_onyx-batch7-2026-11/reactions/.sem` (render slots). Two reaction sessions at most.

## Session order: the exact command lines (steps 1-6)
1. **Prep** (once per recording day; skip if `$J/work/tx.txt` exists):
   `bash $T/prep.sh <job> <obs> <camera> <their-short> <our-yt> [<our-ig>]` then `bash $T/avatar.sh <job> @TheirHandle` and `bash $T/palette.sh <job>`.
   Out: `raw/`, `seq.json`, `work/sync.json`, `transcript/words.json` (WhisperX large-v3, the only large-v3 in the kit), `work/tx.txt`, `work/xplay.txt` (where each file plays), `work/avatar.jpg`, `sfx/`.
2. **Cut** (Opus, one call): reads only `work/tx.txt`, `work/xplay.txt` and the rules; writes `$J/CUT.md` in the shape of `$KIT/CUT-TEMPLATE.md`. Check it: `python $T/spans.py $J $J/CUT.md --fix`.
3. **Cut proof, before any render:**
   `bash $T/cutchain.sh $J [K9 K18 ...]` (CUT.md -> keep.json -> cutbuild EDL -> splice RENDER=0 -> seqmap3 -> syndump -> leakcheck -> endcheck; the K ids drop rows)
   `bash $T/cutproof.sh $J` (pacecheck, silhole at -50 and -40 dB, length <= 180: PASS/FAIL lines)
   `python $T/wholecut.py $J --model medium.en` under `bash $T/lock.sh gpu` and `projects/.asr-lock`; diff `work/wholecut.txt` against CUT.md. A failure is re-cut here.
4. **Build + place:**
   `python $T/build_plan.py $J` (CUT.md beats -> plan.json) · `PYTHONPATH=... python $T/facev3.py $J/plan.json --write`
   `BED_SRC=<bed file> BED_IN=<s> BED_TRIM=-7 bash $T/audchain3.sh $J -24` (beds: `projects/_onyx-batch9-2026-11/reactions/BEDS-b9.md`, audio in the batch-9 job folders and `E:`; rotate, no new searches) -> A1-A6 must pass in `work/audio3-run.log`
   `"$PYW" $T/bleed7.py $J` (a hit > -30 dB: cut the span at a thought boundary; else one `voiceclean7.py` try; else accept >= 28 dB and note it)
   `bash $T/mgall3.sh $J` (one render at a time through `sem.sh`; ffprobe the captions .mov against the length)
   Premiere, one hold, gated through `lanes/premiere/quietgate.py` in the background: `bash $T/premo3.sh $J import,create,addtracks,redo,lay3,screenoff`; then `python $T/dump.py $J/work/dump-layout.json "<sequence>"` -> `python $T/offgrab.py $J --grid 1.5 --edges --sheet`; then P2b once: `p2b4_measure.py $J` -> `p2b4_solve.py $J --write` applied by name, re-dumped. Restore his sequence, save, never export.
5. **Gate:** `bash $T/gate.sh $J [--live]` -> one PASS/FAIL/SKIP line per check (gate A); then Opus gate B reads CUT.md, `work/wholecut.txt`, A's numbers and the offgrab sheets.
6. **One fix round** at the source (re-cut + step-3 proofs, or re-render one overlay under a new name and swap by name), then `gate.sh` again.
   Cost log: `python workflows/session-cost.py --job <job> --since <UTC start> --quiet`.

## Tools frozen (`$T`), what each does: in -> out
| Group | Tool | In -> Out |
|---|---|---|
| prep | `prep.sh` `avatar.sh` `palette.sh` `tx.py` `xplay2.py` `lock.sh` `sem.sh` `cfree.sh` | files -> raw/, seq.json, words.json, tx.txt, xplay.txt, avatar.jpg, sfx/ ; the lock/semaphore/disk guards |
| cut | `spans.py` `keepjson.py` `cutbuild.py` `cutchain.sh` `seqmap3.py` `syndump.py` `leakcheck.py` `endcheck.py` `pausefloor.py` `tight6.py` `author3.py` | CUT.md K table -> keep.json -> transcript/cuts.json -> work/seqmap.json, work/dump-syn.json (the offline sequence) |
| cut proof | `cutproof.sh` `pacecheck.py` `silhole.py` `wholecut.py` | cuts.json -> PASS/FAIL (pauses, holes, length); work/wholecut.txt (medium.en diff) |
| plan | `build_plan.py` `facev3.py` | CUT.md beats + seqmap + dump-syn -> plan.json ; lips-to-seam framing written into plan.json |
| menu kinds | `kindsmenu.py` `kinds7.py` `mgx6.py` `mgx7.py` `mgx.py` `mgxo.py` `overlays.py` `geom.py` `mouth.py` `pp.py` `preview.py` `viewpatch.py` `planlib.py` `captext (kit/)` | plan.json -> overlays/captions-v3.mov + overlays/mg/<id>.mov |
| render | `mgall3.sh` | plan.json -> every MG + the captions layer, one `sem.sh` slot at a time, resumable |
| audio | `audchain3.sh` `audio3.py` `audio6.py` `sfxprep3.py` `sfxassign3.py` `tlsynth7.py` `tlmix7.py` `tlread7.py` `bleed7.py` `voiceclean7.py` `bedstatic7.py` `bedride6.py` `clipgain6.py` | bed + OBS voice + plan cues -> stems, SFX picked from the palette, A1-A6 verdicts, A7 bleed |
| Premiere | `premo3.sh` `applyo.py` `apply.py` `applyx.py` `build_seq.py` `build_seq3.py` `addtracks.py` `screenoff.py` `clear6.py` `restore_active.py` `relink7.py` `premcheck6.py` `unface6.py` | the open project, template "Onyx reaction template (empty)": place, window, overlays, readback. No frame grabs anywhere; no export |
| frames + P2b | `dump.py` `offgrab.py` `p2b4_measure.py` `p2b4_solve.py` `headjump.py` `headlock.py` `facex6m.py` | by-name DOM dump -> offline frames, REPORT.txt ; head size/place solved once with the cover bound |
| gate | `gate.sh` `seamcheck.py` `stagecheck.py` `claudecheck_o.py` (+`claude-ref.npy`) `premcheck6.py` `leakcheck.py` | one PASS/FAIL line per check of gate A |
SFX palette: `assets/sfx/onyx-reactions/` (gitignored: 26 batch-9 clean Epidemic originals in `src/`, the 26 prepped `v3x-*` slices, `slices.json`); `palette.sh` copies it into `$J/sfx/`.
Menu (build_plan.py): `channel_card` `cred_cards` `play_card` `side_by_side` `number_card` `pointer_mark`; type sizes are baked into `kindsmenu.py`/`kinds7.py` (labels 48-64, main 64-110, nothing under 40); one entrance, `slab`.
Dropped from the batch-9 set (job-local or superseded): hpp/otn kinds, premo.sh/prem6.sh, swap/retry/lk scripts, segasr (per-segment ASR), sfxassign3h, cutv3, audio7, p2b (v1).

## Pilot part 2: still to prove (needs a recorded reaction)
- `prep.sh` for real: seq.json shape, sync, large-v3 under both locks, `xplay2` windows over a whole OBS file (untested here: no recording).
- A real CUT.md through `spans.py` -> `cutchain.sh`: `cutbuild.py` now detects fillers (`uh um er ...`) and counted numbers by pattern instead of batch-9's hard-coded word indices; check on a fresh transcript. `cutchain.sh` follows batch 9's cutbuild chain, not the recipe's author3/polish/tight6/cutv3 wording (cutbuild replaced those for a fresh cut); decide which the recipe means.
- `build_plan.py` renders: only the plan JSON was proven (fixture from HPP). Render one still per kind through `mgxo.py --still` to see the bumped type sizes (`kinds7.ours_pill` 48, `otn_hook` name 48, `title_strip` 40, scorecard heads 40) fit; `kindsmenu` internals still carry some fixed sizes that were not touched. Set the `view` numbers on a real contact sheet, and the avatar via `avatar.sh`.
- `audchain3.sh` with a rotated bed (`BED_SRC`, `BED_IN`): A2 depends on the bed; `sfxassign3.py` one-cue-per-graphic path (batch 9 used the multi-cue variant).
- `premo3.sh` live: the `import,create,addtracks,redo,lay3,screenoff` hold with the grab phases removed; `screenoff` needs `work/screenoff.args` (not written by any kit tool yet: derive it from the play spans).
- `gate.sh --live` (`applyo --verify`, a fresh `tlmix7` read), and `seamcheck.py`: the recipe's seam formula with the crop term can never pass (the crop pins the visible top at the seam), so the kit checks the uncropped layer top <= seam - 2 plus the visible top <= seam + 1; confirm that is the intended rule.
- `p2b4_measure.py`/`p2b4_solve.py` on a new job (they were Lunch Table's; now take `<job>` and read the camera from seq.json; `CAM_FPS` env if the camera is not 59.94).
- `voiceclean7` -> `relink7.py` (the relink phase was removed from `premo3.sh`: it hard-coded a file name; run `relink7.py <item> <path>` by hand under the lock).
- Cost of a full session on the kit against the $18 target.
