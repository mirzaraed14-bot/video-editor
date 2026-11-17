#!/usr/bin/env bash
# pass 3 rework (17 Nov ~19:25): ASR each batch10 pull as it lands, one at a time, hub gate 6 GB phys / 10 GB commit, medium.en.
cd "/x/Claude Projects/video-editor-client/video-editor/research/aw-speed-2026-11-17" || exit 1
PY=~/.cache/video-editor/whisperx-venv/Scripts/python.exe
for id in Ec18vXsDHYU nVq2DON5YKw nQs6jA11sQo 155kZGAuCHc; do
  n=0; while [ ! -f "src/$id.mp4" ]; do sleep 20; n=$((n+1)); [ $n -gt 120 ] && { echo "gave up waiting for $id"; continue 2; }; grep -q "BLOCKED\|BOT/429" yt/batch10.log 2>/dev/null && { echo "batch10 blocked"; exit 3; }; done
  ASR_PHYS_GB=6 ASR_COMMIT_GB=10 ASR_MODEL=medium.en $PY -I tools/scout_asr.py pass3/scout "src/$id.mp4"
done
echo "REWORK ASR DONE $(date +%T)"
