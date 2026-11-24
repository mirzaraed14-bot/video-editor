#!/bin/bash
cd "$(dirname "$0")"
D="X:/Claude Projects/video-editor-client/video-editor/projects/_onyx-batch9-2026-11/reactions/.asr-lock"
until mkdir "$D" 2>/dev/null; do sleep 10; done
PY="$HOME/.cache/video-editor/whisperx-venv/Scripts/python.exe"
bash "X:/Claude Projects/video-editor-client/video-editor/projects/_onyx-batch2-2026-10/lock.sh" gpu "$PY" -I "X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/tools/asr_words.py" "$@"
rc=$?
rmdir "$D"
echo "asr rc=$rc $(date +%T)"
