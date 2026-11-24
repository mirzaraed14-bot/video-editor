#!/usr/bin/env bash
# premo3.sh <job dir> <phases>: the Premiere session of a reaction (premiere.lock mkdir/owner/trap, active sequence restored, template project saved; NEVER exports). DRY=1 prints and exits.
#   import = build_seq3 --import (the cleaned-voice OBS file + everything not yet in the bin)      redo = V1/V2/A1 re-placed from cuts.json, razored, overlay tracks cleared (premo.sh redo)
#   lay3   = layout (static face/views) -> window (A1 Amplify + Hard Limiter) -> clipgain6 -> premcheck6 -> overlays (captions, MGs, cues at STATIC levels, plays + bed STEM) -> bedstatic7 -> verify
#   screenoff = razor + disable the screen piece at each handoff (work/screenoff.args)
#   KIT: no Premiere frame grabs anywhere (they moved his playhead): frames come from offgrab.py. No relink/check/grabs phases.
[ "${1:-}" = "--help" ] && { sed -n 2,6p "$0"; exit 0; }
set -u
cd "$(dirname "${BASH_SOURCE[0]}")/../../../../../.." || exit 1     # repo root
J=${1:?usage: premo3.sh <job dir> <phases, comma separated>}; PH=${2:?phases}
KIT=presets/youtube-shorts/onyx-samples/kit/reactions; T=$KIT/tools; T3=$T; R=$T; T7=$T
L=projects/_onyx-batch2-2026-10/.locks/premiere.lock
SEQ=$(python -c "import json;print(json.load(open('$J/seq.json',encoding='utf-8'))['sequence'])")
[ -n "${DRY:-}" ] && { echo "DRY: premo3 would run phases [$PH] on $J (sequence $SEQ); no lock taken, Premiere untouched"; exit 0; }
bash $T/cfree.sh 1501
until mkdir "$L" 2>/dev/null; do echo "waiting for premiere.lock ($(cat $L/owner 2>/dev/null))"; sleep 1; done
echo "reaction builder $J $SEQ $PH $(date '+%F %T')" > "$L/owner"
trap 'rm -rf "$L"; echo "premiere.lock released"' EXIT
export PYTHONUTF8=1
APP=$T/applyo.py
PI=$(python -c "
import sys; sys.path.insert(0,'$T'); from build_seq import es
print(es('(function(){ return app.project.name + \"|\" + (app.project.activeSequence ? app.project.activeSequence.name : \"\"); })()'))")
echo "project|active before: $PI"
case "$PI" in ABW11.prproj*) ;; *) echo "NOT ABW11.prproj: STOP"; exit 9;; esac
ACT=${PI#*|}; [ -n "${ACT_OVERRIDE:-}" ] && ACT="$ACT_OVERRIDE"; echo "$ACT" > "$J/work/active-before.v3.txt"
set -e
if [[ ",$PH," == *,import,* ]]; then python $T3/build_seq3.py $J/seq.json --import; fi
if [[ ",$PH," == *,create,* ]]; then python $T3/build_seq3.py $J/seq.json --create; fi
if [[ ",$PH," == *,addtracks,* ]]; then python $T/addtracks.py "$SEQ" 5; fi
if [[ ",$PH," == *,redo,* ]]; then
  bash $T/cfree.sh 1501
  python $T3/build_seq3.py $J/seq.json --place --clear --nearest
  python $T3/build_seq3.py $J/seq.json --style
  python $T3/build_seq3.py $J/seq.json --verify
  python $T/dump.py $J/work/dump-real.json "$SEQ"
  python $R/syndump.py $J --compare $J/work/dump-real.json || echo "compare: end differs only because the old overlay tracks are still there (cleared by clear6)"
  python $APP $J/plan.json --razor
  python $T/dump.py $J/work/dump-layout.json "$SEQ"
  python $R/clear6.py $J/plan.json
fi
if [[ ",$PH," == *,post,* ]]; then
  bash $T/cfree.sh 1501
  python $APP $J/plan.json --razor
  python $T/dump.py $J/work/dump-layout.json "$SEQ"
  python $R/clear6.py $J/plan.json
fi
if [[ ",$PH," == *,lay3,* ]]; then
  bash $T/cfree.sh 1501
  python $APP $J/plan.json --layout-check
  python $APP $J/plan.json --layout
  python $APP $J/plan.json --window
  python $R/clipgain6.py $J/plan.json
  python $R/premcheck6.py $J/plan.json
  bash $T/cfree.sh 1501
  python $APP $J/plan.json --overlays
  python $T7/bedstatic7.py $J/plan.json
  python $R/clipgain6.py $J/plan.json --verify
  python $APP $J/plan.json --verify
fi
if [[ ",$PH," == *,razor,* ]]; then
  python $APP $J/plan.json --razor
fi
if [[ ",$PH," == *,layout,* ]]; then
  python $T/dump.py $J/work/dump-layout.json "$SEQ"          # screenoff razored V1 after the last dump: re-dump before applying
  python $APP $J/plan.json --layout-check
  python $APP $J/plan.json --layout
  python $APP $J/plan.json --verify
fi
set +e
if [ -n "$ACT" ] && [ "$ACT" != "$SEQ" ]; then python $T/restore_active.py "$ACT"; fi
python -c "
import sys; sys.path.insert(0,'$T'); import apply as A; A.safe_save()"
if [[ ",$PH," == *,screenoff,* ]]; then python $T/screenoff.py $J/plan.json $(cat $J/work/screenoff.args); fi
