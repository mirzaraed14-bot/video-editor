#!/usr/bin/env bash
# His Tella review of the raw cut -> word-timed transcript (faster-whisper medium.en; Premiere is open, so no large-v3).
set -u
ROOT="/x/Claude Projects/video-editor-client/video-editor"
ASR="$ROOT/projects/_onyx-batch9-2026-11/reactions/.asr-lock"
GPU="$ROOT/projects/_onyx-batch2-2026-10/.locks/gpu.lock"
me="$$ mj-beats review1 guide (medium.en)"
take() { while ! mkdir "$1" 2>/dev/null; do sleep 10; done; echo "$me $(date '+%F %T')" > "$1/owner"; }
release() { for d in "$GPU" "$ASR"; do grep -q "mj-beats review1" "$d/owner" 2>/dev/null && rm -rf "$d"; done; }
trap release EXIT
take "$ASR"  # CPU job: the ASR lock only (the GPU lock is for GPU work)
cd "$ROOT/research/aw-mj-2026-11-17/format/review1"
"$HOME/.cache/video-editor/whisperx-venv/Scripts/python.exe" -I - guide.wav guide.words.json <<'PY' 2>&1 | grep --line-buffered -v -i -E "warning|deprecat"
import json, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from faster_whisper import WhisperModel
m = WhisperModel('medium.en', device='cpu', compute_type='int8', cpu_threads=8)
segs, _ = m.transcribe(sys.argv[1], beam_size=5, word_timestamps=True, language='en', vad_filter=True)
out = []
for s in segs:
    out.append({'start': round(s.start, 2), 'end': round(s.end, 2), 'text': s.text.strip(),
                'words': [{'w': w.word.strip(), 'start': round(w.start, 2), 'end': round(w.end, 2)} for w in s.words]})
    print(f'[{s.start:6.1f}-{s.end:6.1f}] {s.text.strip()}', flush=True)
json.dump(out, open(sys.argv[2], 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
PY
