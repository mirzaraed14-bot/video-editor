#!/usr/bin/env bash
# cutproof.sh <job dir>: the step-3 proofs that need no ASR. Every line is PASS/FAIL.
#   pacecheck (talk pauses <= 0.30 s, head/tail air <= 0.12 s) · silhole (no hole > 0.30 s at -50 and -40 dB on the cut voice) · length <= 180 s
cd "$(dirname "${BASH_SOURCE[0]}")/../../../../../.."; export PYTHONUTF8=1
J=${1:?usage: cutproof.sh <job dir>}; T=presets/youtube-shorts/onyx-samples/kit/reactions/tools; rc=0
o=$(python $T/pacecheck.py $J 2>&1); last=$(echo "$o" | tail -n 1); { echo "$last" | grep -q "^0 gaps" && ! echo "$o" | grep -q "air head"; } && echo "PASS pacecheck: $last" || { echo "FAIL pacecheck: $last"; echo "$o" | head -n 3; rc=1; }
for db in -50 -40; do
  o=$(python $T/silhole.py $J $db 2>&1); n=$(echo "$o" | grep -c "bounce "); [ "$n" = 0 ] && echo "PASS silhole $db dB: no hole > 0.30 s" || { echo "FAIL silhole $db dB: $n hole(s)"; echo "$o" | grep "bounce " | head -n 3; rc=1; }
done
L=$(python -c "import json;m=json.load(open('$J/work/seqmap.json'));print(round(max(p+b-a for a,b,p in m['map']),2))")
python -c "import sys;sys.exit(0 if $L<=180.0 else 1)" && echo "PASS length: $L s <= 180" || { echo "FAIL length: $L s > 180"; rc=1; }
exit $rc
