#!/usr/bin/env bash
# measure.sh <ref_dir>... — the facecam preset's standard style measurement, unchanged, per reference folder.
# Same chain that measured fuel-system/ and riskiest/ (2026-09-21): style-probe -> style-set -> style-zoom
# -> slowmo-scan -> transcribe.sh -> style-audio -> style-report. Each stage logs to <ref>/<stage>.log and is
# skipped when its output already exists, so a re-run resumes.
set -u
ROOT="/x/Claude Projects/video-editor-client/video-editor"
W="$ROOT/workflows"
export PYTHONUTF8=1 PYTHONIOENCODING=utf-8
REFS=()
for r in "$@"; do REFS+=("$(cd "$r" && pwd)"); done   # absolute BEFORE the loop cd's into $ROOT
for ref in "${REFS[@]}"; do
  src="$(ls "$ref"/raw/*.mov "$ref"/raw/*.mp4 2>/dev/null | head -1)"
  [ -z "$src" ] && { echo "[$ref] no raw video"; continue; }
  echo "=== $(basename "$ref")  ($src)  $(date +%T)"
  cd "$ROOT"
  [ -f "$ref/probe/probe.json" ] || uv run "$W/style-probe.py" "$src" "$ref/probe" > "$ref/probe.log" 2>&1; echo "  probe  $(date +%T)"
  [ -f "$ref/set.json" ]         || uv run "$W/style-set.py"   "$src" "$ref/set.json"  > "$ref/set.log" 2>&1;  echo "  set    $(date +%T)"
  [ -f "$ref/zoom.json" ]        || uv run "$W/style-zoom.py"  "$src" "$ref/zoom.json" > "$ref/zoom.log" 2>&1; echo "  zoom   $(date +%T)"
  [ -f "$ref/slowmo.json" ]      || uv run "$W/slowmo-scan.py" "$src" "$ref/slowmo.json" > "$ref/slowmo.log" 2>&1; echo "  slowmo $(date +%T)"
  [ -f "$ref/transcript/words.json" ] || bash .claude/skills/rough-cut/scripts/transcribe.sh "$ref" > "$ref/transcribe.log" 2>&1; echo "  words  $(date +%T)"
  [ -f "$ref/audio.json" ]       || uv run "$W/style-audio.py" "$ref" > "$ref/audio.log" 2>&1; echo "  audio  $(date +%T)"
  uv run "$W/style-report.py" "$ref" > "$ref/report.log" 2>&1; echo "  report $(date +%T)"
done
echo "ALL DONE $(date +%T)"
