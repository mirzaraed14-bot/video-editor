#!/usr/bin/env bash
# audchain3.sh <job dir> [BED_LIM=-24]: audio3 (stems; bed from $BED_SRC, BED_TRIM=-7, 19 LU under) -> sfxassign3 (cue sounds vs the carved bed, MARGIN=4.3)
#   -> tlsynth7 -> tlmix7 gates (A2_WANT=19 A2_MIN=16 A2_MAX=25); keeps plan.json's mtime (the MG queue compares against it). Output: $J/work/audio3-run.log (tail -n 5 it).
# Env: BED_SRC (default $J/audio/bed.wav; rotate from projects/_onyx-batch9-2026-11/reactions/BEDS-b9.md, no new searches), BED_IN (bed start in the file, s; default 0),
#      BED_TRIM=-7, CLAMP=6, MARGIN=4.3, DRY=1 (print the setup, run nothing).
cd "$(dirname "${BASH_SOURCE[0]}")/../../../../../.." || exit 1; export PYTHONUTF8=1; PYW="$HOME/.cache/video-editor/whisperx-venv/Scripts/python.exe"
if [ $# -lt 1 ] || [ "$1" = "--help" ]; then sed -n 2,6p "$0"; exit 0; fi
J=$1; L=${2:--24}; T=presets/youtube-shorts/onyx-samples/kit/reactions/tools
SEQ=$(python -c "import json;print(json.load(open('$J/seq.json',encoding='utf-8'))['sequence'])"); OBS=$(python -c "import json;print(json.load(open('$J/seq.json',encoding='utf-8'))['obs'])")
BED_SRC=${BED_SRC:-$J/audio/bed.wav}
if [ -n "${DRY:-}" ]; then echo "DRY audchain3: $SEQ  OBS=$OBS  BED_SRC=$BED_SRC BED_IN=${BED_IN:-0} BED_TRIM=${BED_TRIM:--7} BED_LIM=$L"; exit 0; fi
BED_LIM=$L BED_TRIM=${BED_TRIM:--7} CLAMP=${CLAMP:-6} BED_SRC="$BED_SRC" BED_IN=${BED_IN:-0} "$PYW" $T/audio3.py $J --write --obs "$OBS" > $J/work/audio3-run.log 2>&1
MARGIN=${MARGIN:-4.3} "$PYW" $T/sfxassign3.py $J --apply >> $J/work/audio3-run.log 2>&1
python $T/tlsynth7.py $J >> $J/work/audio3-run.log 2>&1
A2_WANT=19 A2_MIN=16 A2_MAX=25 "$PYW" $T/tlmix7.py "$SEQ" $J --cached >> $J/work/audio3-run.log 2>&1
if [ -f $J/work/plan.mtime ]; then touch -d "$(cat $J/work/plan.mtime)" $J/plan.json; fi
echo DONE >> $J/work/audio3-run.log
