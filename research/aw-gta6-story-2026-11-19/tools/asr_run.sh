#!/bin/bash
# asr_run.sh <wav> [offset] : one ASR job under the machine-wide .asr-lock + gpu.lock, commit headroom >= 10 GB first.
set -u
ROOT="/x/Claude Projects/video-editor-client/video-editor"
ASR="$ROOT/projects/_onyx-batch9-2026-11/reactions/.asr-lock"
GPU="$ROOT/projects/_onyx-batch2-2026-10/.locks/gpu.lock"
me="$$ aw-gta6-story asr (medium.en)"
take() { while ! mkdir "$1" 2>/dev/null; do sleep 10; done; echo "$me $(date '+%F %T')" > "$1/owner"; }
release() { for d in "$GPU" "$ASR"; do grep -q "aw-gta6-story asr" "$d/owner" 2>/dev/null && rm -rf "$d"; done; }
trap release EXIT
take "$ASR"; take "$GPU"
commit=$(powershell -NoProfile -Command "[int]((Get-Counter '\Memory\Commit Limit').CounterSamples.CookedValue/1MB - (Get-Counter '\Memory\Committed Bytes').CounterSamples.CookedValue/1MB)")
echo "commit headroom ${commit} MB"
if [ "${commit:-0}" -lt 10000 ]; then echo "ABORT: commit headroom < 10 GB"; exit 3; fi
"$HOME/.cache/video-editor/whisperx-venv/Scripts/python.exe" "$ROOT/research/aw-gta6-story-2026-11-19/tools/asr_words.py" "$1" "${2:-0}" 2>&1 | grep -v -i -E "warning|lightning|torchaudio|pyannote|deprecat" | tail -6
