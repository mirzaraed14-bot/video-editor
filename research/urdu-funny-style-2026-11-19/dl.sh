#!/usr/bin/env bash
# one stream at a time via pace.sh; H.264 mp4; no subs, no cookies
B="/x/Claude Projects/video-editor-client/video-editor"
OUT="$B/research/urdu-funny-style-2026-11-19/src"
for id in 6U5zDE2ypaA lgUUlX1DZpE 9CyIYSM1gO8; do
  if ls "$OUT/$id".mp4 >/dev/null 2>&1; then echo "have $id"; continue; fi
  echo "=== $id $(date '+%T')"
  "$B/projects/_onyx-batch2-2026-10/pace.sh" youtube yt-dlp -S "vcodec:h264,res:1080,fps,acodec:aac" --merge-output-format mp4 --no-write-subs --no-write-auto-subs --no-playlist -o "$OUT/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id"
  rc=$?
  echo "rc=$rc for $id $(date '+%T')"
  if [ $rc -eq 75 ]; then echo "BLOCKED flag, stop"; break; fi
done
echo ALLDONE
