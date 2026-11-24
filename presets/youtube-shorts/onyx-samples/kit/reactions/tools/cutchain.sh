#!/usr/bin/env bash
# cutchain.sh <job dir> [K9 K18 ... = rows to drop]: step 3, the cut BEFORE any render.
#   keepjson (CUT.md K table -> keep.json) -> cutbuild (EDL from words + 10 ms envelope) -> splice RENDER=0 -> seqmap3 -> syndump (offline sequence dump) -> leakcheck -> endcheck
# then the proofs: bash $KIT/tools/cutproof.sh <job>   (pacecheck, silhole at -50/-40 dB, <= 180 s; the whole-cut ASR is a separate command, see KIT.md)
set -e; cd "$(dirname "${BASH_SOURCE[0]}")/../../../../../.."; export PYTHONUTF8=1
J=${1:?usage: cutchain.sh <job dir> [K-rows to drop]}; shift || true
T=presets/youtube-shorts/onyx-samples/kit/reactions/tools; S=.claude/skills/rough-cut/scripts
mkdir -p $J/work
python $T/keepjson.py $J $J/CUT.md "$@"
python $T/cutbuild.py $J | head -1
RENDER=0 bash $S/splice.sh $J > $J/work/splice.log 2>&1
python $T/seqmap3.py $J | head -1
python $T/syndump.py $J | tail -1
python $T/leakcheck.py $J
python $T/endcheck.py $J 2>&1 | grep -v "PLAY\|seg2[0-9] \(START\|END\)" | tail -12
