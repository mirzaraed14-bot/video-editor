# Abundance Wisdom shorts — fresh-session start (read THIS, not the whole PLAYBOOK)

Written 2026-10-18 when the long working session was retired. One page so a new session starts cheap.

## Ground rules (Affan is on paid usage credits)
- **Quote the cost before each job and stay inside it.** Batch steps into few tool calls; no advisor calls, no subagents
  and no full-size image reads on routine passes; read only the PLAYBOOK section you need.
- **Never save his projects** (ABW8/ABW10 .prproj, ABW9.aep): he saves. **Never export**: he exports himself.
- **Never `app.open` in AE** and never close/restart AE or Premiere. AE scripts run in his open ABW9:
  `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders\ABW9.aep`.
- Captions: max 3 words per layer, about 1 in 3 coloured (`<red>`, `<yellow>`, `<blue>`), no commas or full stops (? ! ok,
  inside the colour tag), interviewer lines italic (`i: `), stacked second line `+`, the f-word censored `F*CK`.
- Creator's edits are decisions. YouTube is blocked on this PC: never bypass it.

## How to run things
- **AE script:** write the .jsx with Python `.replace()` from a template (never sed; in heredocs build backslashes with
  `chr(92)`), copy it to a `.js` and `node --check` it, then
  `powershell -NoProfile -Command "$p = Get-Process AfterFX | ? MainWindowTitle -like '*After Effects*'; Start-Process $p.Path -ArgumentList @('-r','<jsx path>')"`
  (escape `$` as `\$` from bash) and poll for the script's own output file.
- **Premiere (read-only queries):** `node lanes/premiere/premiere-bridge.mjs execute_extendscript "$(python -c "import json;print(json.dumps({'script':open(F).read()}))")"`
  → keep the line starting with `"` and `json.loads` it.
- GPU python: `$HOME/.cache/video-editor/whisperx-venv/Scripts/python.exe`. Others: `uv run -q --with numpy --with pillow ...`.

## Recipes (newest working example = `projects/abw10-comp04/`, see its RUN.md)
| Job | Steps | Templates |
|---|---|---|
| **BlurMoCurves zoom** (~$0.6) | dump the comp → `presets/youtube-shorts/abundance-wisdom/zoom_pass.py <srcmap.tsv> "<comp>" <dir>` (uv: opencv-contrib-python-headless numpy pillow scipy) → run `<dir>/zoom.jsx` → after-dump | `projects/abw10-comp04/zoom/dump04.jsx` (swap comp name + OUT); yellow (2) = pull out |
| **Transitions** (~$0.3) | `python presets/youtube-shorts/abundance-wisdom/transition_pass.py "<comp>" <out.jsx>` → node check → run; log = `<out>.txt` | labels: 10 Purple −90 dip · 16 Dark Green +30 · 4 Pink white flash · 6 Peach exposure blur · 14 Cyan gaussian · 3 Aqua none · others none · last block ignored |
| **Caption export** (~$1–1.5) | read the sequence's **A1 clips** (`projects/abw10-comp04/seqref/a_clips.js`), rebuild A1 audio, transcribe (`.claude/skills/rough-cut/scripts/transcribe.sh <job>`, raw/*.mov) → read words against the audio for mishears → `captions.txt` → flat copy (strip leading `+`) + `flat/transcript/words.json` (fix mishears there) → `presets/youtube-shorts/abundance-wisdom/make_plan.py <flat> --hang 1.0` → `render_caps.py sheet` then `render <out.mov> <audio>` | `projects/abw10-comp04/captions/` (render_caps.py, captions.txt); out = `E:\Shorts\Abudance Wisdom Shorts Exports\Caption Exports\<name>.mov` |
| **Caps clean** (~$0.4) | `find_caption.jsx` (lists caption footage + its comp) → `clean_capcut.py "<file>"` (~5 min) → `verify_clean.py` (worst caption change ≤ 6) → re-point jsx | `projects/abw10-comp04/captions/capcut/` (find_caption.jsx, verify_clean.py, roadster2_replace.jsx: swap id, name regex, CLEAN path, precomp name) |
| **Head lock** (~$1–1.5, 6 layers) | `read_comps*.jsx` → `head_track.py` (all layer indices in ONE call) → `track_sheet.py` → `apply_headlock.py` → AE → `headlock_proof.py` | `projects/mj-skin-son-tyson/headlock/`; profiles: CSRT `head_box_track.py` |
| **Fuchsia letterbox** | `plan_band.py <render> plan.json in:out` → `letterbox.jsx.tmpl` (`projects/ronnie-coleman-truths/letterbox/`) → proof | `projects/mj-skin-son-tyson/letterbox/` (plan79.json, letterbox79.jsx, proof79.py) |
| **Sequencing from a brief** | PLAYBOOK § 0 + `find_quote.py`, `resolve_beats.py`, `plan_placement.py`, `place_sequence.py` | `projects/mj-skin-son-tyson/` (sources.json, beats.json, premiere/) |

Lessons that cost money last time: transcribe the CLEAN A1 dialogue (the mixed render made captions land up to 0.56 s
early); check the words.json schema (`clips[].words[]` with `w`/`start`/`end`) before parsing; caption files named
`<name>2.mp4` in Caption Exports are his CapCut returns (clean those, never the `.mov` we render).

## Open state at handoff (2026-10-18)
- ABW10 Linked Comp 04 (Rogan × Musk Roadster, Sequence 05): zooms, transitions, caption export `roadster.mov`, caps clean
  all DONE in ABW9 — **ABW9 unsaved when last checked: he saves, then exports.**
- MJ short (ABW8 Linked Comp 79 / Sequence 53): letterbox + clean caps restored 2026-10-15; he exports.
- ABW10 Linked Comp 07 (Katherine × Paris Jackson): head lock DONE 2026-10-18 in ABW9 (unsaved); Sequence 07
  caption export `katherine-paris.mov` DONE; state in `projects/abw10-comp07/RUN.md`. Its build comp ABW10 Linked
  Comp 08: zoom pass + transitions + caps clean DONE 2026-10-18 (`projects/abw10-comp08/RUN.md`).
