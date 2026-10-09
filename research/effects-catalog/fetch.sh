#!/usr/bin/env bash
# Reference clips for the effects catalog: first 10 min of one video per channel, H.264. Reference only, never used in an edit.
cd "$(dirname "$0")"
while IFS=$'\t' read -r code id ch title; do
  [ -f "src/$code.mp4" ] && { echo "skip $code"; continue; }
  echo "=== $code $ch"
  yt-dlp --no-playlist -f "bv*[vcodec^=avc1][height<=1080]+ba[ext=m4a]/b[vcodec^=avc1]" --merge-output-format mp4 \
    --download-sections "*0-600" -o "src/$code.%(ext)s" "https://www.youtube.com/watch?v=$id" 2>&1 | grep -E "ERROR|Merger" || true
  [ -f "src/$code.mp4" ] || { echo "FAILED $code (stopping this pass)"; exit 1; }
done < sources.tsv
echo "=== done"
