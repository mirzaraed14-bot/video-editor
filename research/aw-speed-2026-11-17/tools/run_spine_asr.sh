#!/usr/bin/env bash
# One clip per run, 8 GB headroom (advisor #2), medium.en for the words that go to captions. Waits for each file to exist.
cd "/x/Claude Projects/video-editor-client/video-editor/research/aw-speed-2026-11-17" || exit 1
PY=~/.cache/video-editor/whisperx-venv/Scripts/python.exe
for id in 3YVIjJyNLNM hMCusTW14xI MSizEHlSsTs; do
  while [ ! -f "src/$id.mp4" ]; do sleep 30; done
  ASR_PHYS_GB=8 ASR_COMMIT_GB=8 ASR_MODEL=medium.en $PY -I tools/scout_asr.py scout_medium "src/$id.mp4"
done
echo "SPINE ASR DONE $(date +%T)"
