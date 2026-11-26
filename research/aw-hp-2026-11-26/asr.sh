#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
if [ -e projects/.asr-lock ]; then echo "projects/.asr-lock held: $(cat projects/.asr-lock)"; exit 4; fi
echo "aw-hp-day2 $(date '+%F %T')" > projects/.asr-lock; trap 'rm -f projects/.asr-lock' EXIT
bash projects/_onyx-batch2-2026-10/lock.sh gpu "$HOME/.cache/video-editor/whisperx-venv/Scripts/python.exe" research/aw-hp-2026-11-26/asr.py "$@"
