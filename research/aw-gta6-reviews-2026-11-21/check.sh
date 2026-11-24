#!/bin/bash
# check.sh <raw file name without .mp4> [sheet fps]: probe + contact sheet + whole-file loudness + ASR (silent, ffmpeg -f null only)
cd /Users/affanbaig/video-editor; R=research/aw-gta6-reviews-2026-11-21; f=projects/gta6-reviews-compilation/raw/$1.mp4
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,bit_rate:format=duration -of csv=p=0 "$f"
ffmpeg -v error -y -i "$f" -vf "fps=${2:-1/10},scale=384:-1,tile=6x${3:-14}" -frames:v 1 "$R/sheets/$1.jpg"
ffmpeg -v info -nostats -i "$f" -af ebur128=peak=true -f null - 2>&1 | grep -E "^\s+(I|Peak):" | tail -2
shasum -a 256 "$f" | cut -c1-16
bash projects/_onyx-batch2-2026-10/lock.sh gpu $HOME/.cache/video-editor/whisperx-venv/bin/python -I $R/asr.py "$f" 2>/dev/null | grep -v "^        \["
