#!/usr/bin/env bash
# normalize-sections.sh — apply the HOUSE audio chain to every source recording in a job, as
# normalized copies, and verify nothing shifted in time. The Resolve lane's step 3.
#
#   usage: normalize-sections.sh <job_dir>
#          DRY=1 normalize-sections.sh <job_dir>            measure only, render nothing
#          AMPLIFY_DB=12 normalize-sections.sh <job_dir>    override the measured gain
#
# The chain is the same one every lane runs (LANES.md § step 3; unified 2026-09-04, the user's call):
#   gain = whatever puts the KEPT speech at -17 LUFS integrated, measured by workflows/voice-gain.py
#   from transcript/cuts.json against raw/  →  hard limiter at -6 dBFS  →  320k AAC.
# One gain per job dir (a section sub-job with its own transcript gets its own measurement).
#
# Writes normalized copies to <job_dir>/audio-normalized/. NEVER touches the raws.
# Swap them into Resolve afterwards with replace-clips.py — see README.md.
#
# Locks (full rationale in README.md):
#   · -c:v copy          video is stream-copied, so the picture stays bit-identical
#   · level=disabled     alimiter auto-level otherwise defeats the measured static gain
#   · latency=1          compensates the limiter's own lookahead so nothing moves in time
#   · 320k AAC           downstream-bitrate lock: never re-encode voice below 256k
#   · NEVER loudnorm     dynamic normalization pumps
#
# Bash 3.2 clean (stock macOS) and Linux clean — no mapfile, no associative arrays.
set -euo pipefail

JOB="${1:?usage: normalize-sections.sh <job_dir>}"
OUT="$JOB/audio-normalized"
CEIL="0.501"             # -6.0 dBFS, the house limiter ceiling (splice.sh uses the same value)
REPO="$(cd "$(dirname "$0")/../../.." && pwd)"
VOICE_GAIN="$REPO/workflows/voice-gain.py"

[ -d "$JOB" ] || { echo "no such job dir: $JOB" >&2; exit 1; }
mkdir -p "$OUT"

# every raw recording in the job: the top-level raw/ plus each section's raw/
SRCS=$({ find "$JOB/raw" "$JOB/sections" -type f -name '*.mp4' -path '*/raw/*' 2>/dev/null || true; } | sort)   # sections/ may not exist; under set -e that must not abort
[ -n "$SRCS" ] || { echo "no raws found under $JOB" >&2; exit 1; }

measure() {   # $1=file -> "I LRA PEAK"  (whole file, for the readback columns only)
  ffmpeg -nostdin -hide_banner -i "$1" -af ebur128=peak=true -f null - 2>&1 \
    | sed -n '/Summary:/,$p' \
    | awk '/^ *I:/{i=$2} /^ *LRA:/{l=$2} /^ *Peak:/{p=$2} END{print i, l, p}'
}

probe() {     # $1=file -> "dur vframes aframes astart"
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$1")
  v=$(ffprobe -v error -select_streams v:0 -show_entries stream=nb_frames -of csv=p=0 "$1")
  a=$(ffprobe -v error -select_streams a:0 -show_entries stream=nb_frames -of csv=p=0 "$1")
  s=$(ffprobe -v error -select_streams a:0 -show_entries stream=start_time -of csv=p=0 "$1")
  echo "$d $v $a $s"
}

# gain for one job dir: voice-gain.py on the kept ranges, or the AMPLIFY_DB override.
# Prints "GAIN KEPT_LUFS".
job_gain() {  # $1=job dir (the one holding raw/ + transcript/cuts.json)
  if [ -n "${AMPLIFY_DB:-}" ]; then echo "$AMPLIFY_DB override"; return; fi
  [ -f "$1/transcript/cuts.json" ] || { echo "no transcript/cuts.json under $1 — run rough-cut first, or set AMPLIFY_DB" >&2; exit 1; }
  if command -v uv >/dev/null 2>&1; then j=$(uv run "$VOICE_GAIN" "$1" --json); else j=$(python3 "$VOICE_GAIN" "$1" --json); fi
  printf '%s' "$j" | python3 -c 'import json,sys; d=json.load(sys.stdin); print(d["gain_db"], d["lufs"])'
}

echo "house chain: measured gain -> kept speech -17 LUFS pre-limiter, hard limiter -6 dBFS   out: $OUT"
printf "\n%-26s %9s %7s %9s %8s  %s\n" SECTION KEPT_LUFS GAIN OUT_LUFS OUT_PEAK CHECK
fail=0
last_dir=""; GAIN=""; KEPT=""
echo "$SRCS" | while read -r src; do
  [ -n "$src" ] || continue
  name=$(basename "$src" .mp4)
  jobdir=$(cd "$(dirname "$src")/.." && pwd)
  if [ "$jobdir" != "$last_dir" ]; then
    set -- $(job_gain "$jobdir"); GAIN="$1"; KEPT="$2"; last_dir="$jobdir"
  fi

  if [ "${DRY:-0}" = "1" ]; then
    printf "%-26s %9s %+7s %9s %8s  %s\n" "$name" "$KEPT" "$GAIN" - - "dry-run"
    continue
  fi

  dst="$OUT/$name.mp4"
  ffmpeg -nostdin -v error -y -i "$src" -c:v copy \
    -af "volume=${GAIN}dB,alimiter=level_in=1:level_out=1:limit=${CEIL}:attack=5:release=50:level=disabled:latency=1" \
    -c:a aac -b:a 320k "$dst"

  # DRIFT GATE — duration, video frames, audio frames and audio start must all match.
  # An AAC re-encode can shift audio a frame via encoder priming; that would break sync
  # across every cut, and it is invisible until someone watches the whole video.
  if [ "$(probe "$src")" = "$(probe "$dst")" ]; then chk="OK"; else chk="*** DRIFT ***"; fail=1; fi
  set -- $(measure "$dst")
  printf "%-26s %9s %+7s %9s %8s  %s\n" "$name" "$KEPT" "$GAIN" "$1" "$3" "$chk"
done

echo
if [ "${DRY:-0}" = "1" ]; then
  echo "dry run — nothing written. Re-run without DRY=1 to render."
else
  echo "OUT_LUFS is the whole file (dead air included); the kept speech sits at -17. OUT_PEAK should read about -6.0."
  echo "Any *** DRIFT *** line above means DO NOT REPLACE that file — investigate first."
  echo "Next: replace-clips.py to swap them into the Resolve timeline."
fi
