#!/usr/bin/env bash
# gate.sh <job dir> [--live]: the single QC gate A (scripts), ONE PASS/FAIL line per check, exit 1 if any FAIL. Gate B (Opus) only starts when this is all green.
#   default (offline): reads the job's saved readbacks (plan.dump = work/dump-*.json, work/tl-read.json, work/offgrab*/REPORT.txt); touches no Premiere, renders nothing.
#   --live           : also asks Premiere (DOM read only, never activates a sequence, never moves the playhead): applyo --verify, and a fresh tlmix7 read. Run it inside the
#                      one Premiere hold of step 4 (quietgate), never in a loop.
# Checks (REACTIONS-LEAN § The single QC gate A):
#   1 applyo --verify = 0              2 tlmix7 A1-A6 (bed 19 LU, min 16, max 25; 3 s windows <= -4.0 dBFS)    3 bleed7 A7 (no played file audible under his talk)
#   4 premcheck6 = 0                   5 claudecheck_o = 0                                                      6 leakcheck = 0
#   7 seam / cover bound (seamcheck)   8 stagecheck: no empty panel frame                                      9 captions from frame 0 to the end (+ .mov length)
#  10 sequence end <= 180.0 s         11 offgrab REPORT.txt: no unmodelled layer
# Output discipline: one line per check, then the tail of the failing tool (3 lines) under a FAIL.
cd "$(dirname "${BASH_SOURCE[0]}")/../../../../../.." || exit 1; export PYTHONUTF8=1
if [ $# -lt 1 ] || [ "$1" = "--help" ]; then sed -n 2,13p "$0"; exit 0; fi
J=$1; LIVE=0; [ "${2:-}" = "--live" ] && LIVE=1
T=presets/youtube-shorts/onyx-samples/kit/reactions/tools; PYW="$HOME/.cache/video-editor/whisperx-venv/Scripts/python.exe"; [ -x "$PYW" ] || PYW=python
SEQ=$(python -c "import json;print(json.load(open('$J/plan.json',encoding='utf-8'))['sequence'])"); rc=0
mkdir -p $J/work/gate
res() { # res <name> <PASS|FAIL|SKIP> <detail> [<tail file>]
  printf '%-4s %-26s %s\n' "$2" "$1" "$3"
  if [ "$2" = FAIL ]; then rc=1; [ -n "${4:-}" ] && tail -n 3 "$4" | cut -c1-200 | sed 's/^/       | /'; fi
}
L=$J/work/gate

# 1 applyo --verify (live readback of the placed sequence)
if [ $LIVE = 1 ]; then
  python $T/applyo.py $J/plan.json --verify > $L/applyo.txt 2>&1; [ $? = 0 ] && res "applyo --verify" PASS "$(tail -n 1 $L/applyo.txt | cut -c1-100)" || res "applyo --verify" FAIL "readback differs from plan" $L/applyo.txt
else res "applyo --verify" SKIP "needs the live Premiere readback (run with --live)"; fi

# 2 tlmix7 A1-A6
if [ $LIVE = 1 ]; then CACHED=""; else CACHED="--cached"; fi
A2_WANT=19 A2_MIN=16 A2_MAX=25 "$PYW" $T/tlmix7.py "$SEQ" $J $CACHED > $L/tlmix.txt 2>&1
bad=$(grep -E "^A[1-6] |   A[1-6] (PASS|FAIL)|A[1-6] (PASS|FAIL)" $L/tlmix.txt | grep -c "FAIL"); got=$(grep -oE "A[1-6] (PASS|FAIL)" $L/tlmix.txt | sort -u | tr '\n' ' ')
if [ -z "$got" ]; then res "tlmix7 A1-A6" FAIL "no verdict lines (tl-read.json missing?)" $L/tlmix.txt
elif [ "$bad" = 0 ]; then res "tlmix7 A1-A6" PASS "$got"; else res "tlmix7 A1-A6" FAIL "$got" $L/tlmix.txt; fi

# 3 bleed7 A7
"$PYW" $T/bleed7.py $J > $L/bleed7.txt 2>&1
n=$(grep -oE "audible under his voice \(z > 5 vs control offsets\): [0-9]+" $L/bleed7.txt | grep -oE "[0-9]+$")
if [ -z "$n" ]; then res "bleed7 A7" FAIL "no verdict (bleed7 crashed)" $L/bleed7.txt
elif [ "$n" = 0 ]; then res "bleed7 A7" PASS "0 kept talk segments with a played file audible"; else res "bleed7 A7" FAIL "$n hit(s): a hit > -30 dB -> cut the span at a thought boundary; else ONE voiceclean7 try; else accept >= 28 dB and note it" $L/bleed7.txt; fi

# 4 premcheck6
python $T/premcheck6.py $J/plan.json > $L/premcheck6.txt 2>&1; p=$?
[ $p = 0 ] && res premcheck6 PASS "$(tail -n 1 $L/premcheck6.txt)" || res premcheck6 FAIL "$(tail -n 1 $L/premcheck6.txt)" $L/premcheck6.txt

# 5 claudecheck_o
python $T/claudecheck_o.py $J/plan.json > $L/claudecheck.txt 2>&1
c=$(grep -oE "EXPOSED Claude-app frames: [0-9]+" $L/claudecheck.txt | grep -oE "[0-9]+$")
[ "$c" = 0 ] && res claudecheck_o PASS "0 exposed Claude-app frames" || res claudecheck_o FAIL "exposed frames: ${c:-no verdict}" $L/claudecheck.txt

# 6 leakcheck
python $T/leakcheck.py $J > $L/leakcheck.txt 2>&1
[ "$(tail -n 1 $L/leakcheck.txt)" = "0 leaks" ] && res leakcheck PASS "0 leaks" || res leakcheck FAIL "$(tail -n 1 $L/leakcheck.txt)" $L/leakcheck.txt

# 7 seam / cover bound
python $T/seamcheck.py $J > $L/seamcheck.txt 2>&1; s=$?
[ $s = 0 ] && res "seam cover bound" PASS "$(head -n 1 $L/seamcheck.txt | cut -c11-120)" || res "seam cover bound" FAIL "$(head -n 1 $L/seamcheck.txt | cut -c11-120)" $L/seamcheck.txt

# 8 stagecheck
python $T/stagecheck.py $J/plan.json > $L/stagecheck.txt 2>&1; s=$?
[ $s = 0 ] && res stagecheck PASS "$(tail -n 1 $L/stagecheck.txt)" || res stagecheck FAIL "$(tail -n 1 $L/stagecheck.txt)" $L/stagecheck.txt

# 9 captions from frame 0 to the end
python - "$J" > $L/captions.txt 2>&1 <<'PY'
import json, os, subprocess, sys
J = sys.argv[1]; P = json.load(open(f"{J}/plan.json", encoding="utf-8")); END = P["end"]; cj = f"{J}/overlays/captions.json"
bad = []
if not os.path.exists(cj): bad.append("overlays/captions.json missing")
else:
    c = json.load(open(cj, encoding="utf-8"))
    if not c or c[0]["t0"] > 0.05: bad.append(f"first caption starts {c[0]['t0'] if c else 'never'} (need 0.0)")
    if c and c[-1]["t1"] < END - 0.5: bad.append(f"last caption ends {c[-1]['t1']} < end {END} - 0.5")
mov = f"{J}/overlays/{P.get('captions_file', 'captions-v3.mov')}"
if not os.path.exists(mov): bad.append(f"{os.path.basename(mov)} missing")
else:
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", mov], capture_output=True, text=True).stdout.strip() or 0)
    if abs(d - END) > 0.15: bad.append(f"captions .mov {d:.2f} s vs sequence {END:.2f} s")
print("; ".join(bad) if bad else f"captions 0.0 -> {c[-1]['t1']} of {END}, .mov {d:.2f} s"); sys.exit(1 if bad else 0)
PY
[ $? = 0 ] && res captions PASS "$(cat $L/captions.txt)" || res captions FAIL "$(cat $L/captions.txt)"

# 10 sequence end <= 180.0
python - "$J" > $L/end.txt 2>&1 <<'PY'
import json, sys
J = sys.argv[1]; P = json.load(open(f"{J}/plan.json", encoding="utf-8")); e = P["end"]; print(f"end {e:.3f} s"); sys.exit(0 if e <= 180.0 else 1)
PY
[ $? = 0 ] && res "sequence end <= 180.0" PASS "$(cat $L/end.txt)" || res "sequence end <= 180.0" FAIL "$(cat $L/end.txt)"

# 11 offgrab REPORT.txt lists no unmodelled layer
R=$(ls -t $J/work/offgrab*/REPORT.txt 2>/dev/null | head -n 1)
if [ -z "$R" ]; then res "offgrab unmodelled" SKIP "no work/offgrab*/REPORT.txt yet (dump.py -> offgrab.py --grid 1.5 --edges --sheet first)"
elif [ "$(sed -n 3p "$R" | tr -d ' ')" = "none" ]; then res "offgrab unmodelled" PASS "none ($(dirname "$R" | xargs basename))"
else res "offgrab unmodelled" FAIL "unmodelled layer(s) in $R" "$R"; fi
[ $rc = 0 ] && echo "GATE A: all green" || echo "GATE A: FAILED (fix at the source, one round)"
exit $rc
