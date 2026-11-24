#!/usr/bin/env bash
# mgall3.sh <job dir>: step 4 render of the captions layer + every MG of plan.json, each through ONE sem.sh slot at a time (resumable: skips an id whose .mov is newer than plan.json).
# DRY=1 lists what would render and renders nothing.
cd "$(dirname "${BASH_SOURCE[0]}")/../../../../../.." || exit 1; export PYTHONUTF8=1
if [ $# -lt 1 ] || [ "$1" = "--help" ]; then sed -n 2,3p "$0"; exit 0; fi
J=$1; T=presets/youtube-shorts/onyx-samples/kit/reactions/tools; S=$T/sem.sh; mkdir -p $J/work
if [ -n "${DRY:-}" ]; then
  python -c "import json;g=json.load(open('$J/plan.json'))['graphics'];print('DRY mgall3: captions + %d MG: %s' % (len(g), ' '.join(x['id'] for x in g)))"
  exit 0
fi
if ! { [ -s $J/overlays/captions-v3.mov ] && [ $J/overlays/captions-v3.mov -nt $J/plan.json ]; }; then
  bash $S python $T/mgxo.py $J/plan.json --captions > $J/work/captions-v3.log 2>&1
fi
for id in $(python -c "import json;print(' '.join(g['id'] for g in json.load(open('$J/plan.json'))['graphics']))"); do
  f=$J/overlays/mg/$id.mov
  if [ -s $f ] && [ $f -nt $J/plan.json ]; then echo "skip $id"; continue; fi
  bash $S python $T/mgxo.py $J/plan.json --mg --only $id >> $J/work/mgall3.log 2>&1; echo "$(date +%T) $id rc=$?" >> $J/work/mgall3.log
done
echo ALLDONE >> $J/work/mgall3.log
