#!/usr/bin/env bash
# prep.sh <job> <obs file> <camera file> <their-short file> <our-yt file> [<our-ig file>]     (step 1; Haiku/command run, once per recording day, ~$0.2)
#   1. copy (never move) the OBS file into projects/<job>/raw/ and write seq.json (sequence name, OBS, camera + sync json)
#   2. camera<->OBS sync (workflows/sync-dual-audio.py, report only; CPU)
#   3. transcribe ONCE: WhisperX large-v3 through lock.sh gpu + the machine-wide projects/.asr-lock (ONE ASR process). Skipped when transcript/words.json exists.
#      Run it while Affan is NOT in Premiere. This is the ONLY step of the kit that uses large-v3.
#   4. work/tx.txt (tx.py: compact timed lines in OBS seconds) and work/xplay.txt (xplay2: where each given file PLAYS in the OBS audio)
# Env: SEQ_NAME (default "<job> reaction"), BIN ("Onyx reactions"), TEMPLATE ("Onyx reaction template (empty)"), DRY=1 (print the plan, touch nothing).
# Stops at the first non-zero exit and prints the tail of its log. Never debugs.
cd "$(dirname "${BASH_SOURCE[0]}")/../../../../../.." || exit 1
if [ "${1:-}" = "--help" ] || [ $# -lt 5 ]; then sed -n 2,11p "$0"; if [ "${1:-}" = "--help" ]; then exit 0; else exit 2; fi; fi
export PYTHONUTF8=1
j=$1; OBS=$2; CAM=$3; THEIRS=$4; YT=$5; IG=${6:-}
J=projects/$j; T=presets/youtube-shorts/onyx-samples/kit/reactions/tools
SEQ_NAME=${SEQ_NAME:-"$j reaction"}; BIN=${BIN:-"Onyx reactions"}; TEMPLATE=${TEMPLATE:-"Onyx reaction template (empty)"}
b=$(basename "$OBS")
if [ -n "${DRY:-}" ]; then
  echo "DRY prep: copy '$OBS' -> $J/raw/; seq.json (seq '$SEQ_NAME', cam '$CAM'); sync; transcribe $J (skipped if words.json exists); tx.txt; xplay2 on: $THEIRS $YT $IG"
  exit 0
fi
step() { "$@"; rc=$?; if [ $rc -ne 0 ]; then echo "FAILED rc=$rc: $*"; tail -n 5 "$J/work/prep.log" 2>/dev/null; exit $rc; fi; }
mkdir -p $J/raw $J/work $J/transcript $J/sfx $J/audio
[ -f "$J/raw/$b" ] || cp "$OBS" "$J/raw/"
cmp -s "$OBS" "$J/raw/$b" || { echo "copy MISMATCH $b"; exit 3; }
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$J/raw/$b")
python - "$J" "$SEQ_NAME" "$TEMPLATE" "$BIN" "$b" "$CAM" "$DUR" <<'PY'
import json, os, sys
J, seq, tpl, bn, b, cam, dur = sys.argv[1:8]
obs = os.path.abspath(os.path.join(J, "raw", b))
json.dump(dict(sequence=seq, template=tpl, bin=bn, obs=obs, cameras=[dict(path=cam, sync="work/sync.json", obs_from=0.0, obs_to=round(float(dur), 2))], fps=60),
          open(os.path.join(J, "seq.json"), "w", encoding="utf-8"), indent=1)
PY
step uv run workflows/sync-dual-audio.py --camera "$CAM" --mic "$J/raw/$b" --report --json-out $J/work/sync.json > $J/work/prep.log 2>&1
if [ ! -s $J/transcript/words.json ]; then
  if [ -e projects/.asr-lock ]; then echo "another ASR process holds projects/.asr-lock: stop"; exit 4; fi
  echo "$j $(date '+%F %T')" > projects/.asr-lock; trap 'rm -f projects/.asr-lock' EXIT
  step bash $T/lock.sh gpu bash .claude/skills/rough-cut/scripts/transcribe.sh $J >> $J/work/prep.log 2>&1
  rm -f projects/.asr-lock
fi
python $T/tx.py $J > $J/work/tx.txt
: > $J/work/xplay.txt
for f in "$THEIRS" "$YT" $IG; do
  if [ -n "$f" ]; then echo "## $f" >> $J/work/xplay.txt; python $T/xplay2.py "$J/raw/$b" "$f" 0 "$DUR" >> $J/work/xplay.txt 2>&1; fi
done
echo "prep done: $J/work/tx.txt, $J/work/xplay.txt, $J/seq.json ($(wc -l < $J/work/tx.txt) tx lines)"
