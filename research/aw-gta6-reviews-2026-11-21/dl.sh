#!/bin/bash
# dl.sh: reads dlq.tsv (url<TAB>name<TAB>optional --download-sections arg); one pace.sh call per line; stops on any block.
cd "$(dirname "$0")"; PACE=/Users/affanbaig/video-editor/projects/_onyx-batch2-2026-10/pace.sh
LK=/Users/affanbaig/video-editor/projects/_onyx-batch2-2026-10/.locks
OUT=/Users/affanbaig/video-editor/projects/gta6-reviews-compilation/raw
touch dlq.tsv dl-done.txt
while true; do
  [ -e $LK/youtube.BLOCKED ] && { echo "$(date +%T) youtube.BLOCKED present, stop" >> dl.log; exit 75; }
  line=$(grep -vxFf dl-done.txt dlq.tsv | head -1)
  case "$line" in *twitch.tv*) [ -e $LK/twitch.BLOCKED ] && { echo "$(date +%T) twitch.BLOCKED present, stop before a twitch line" >> dl.log; exit 75; };; esac
  if [ -z "$line" ]; then [ -f STOP ] && exit 0; sleep 10; continue; fi
  url=$(echo "$line"|cut -f1); name=$(echo "$line"|cut -f2); sec=$(echo "$line"|cut -f3)
  case "$url" in *youtube.com*|*youtu.be*) kind=youtube;; *) kind=twitch;; esac
  if [ -n "$sec" ]; then X=(--download-sections "$sec" --force-keyframes-at-cuts); else X=(); fi
  echo "$(date +%T) START $kind $name $sec" >> dl.log
  $PACE $kind yt-dlp --ignore-config --no-update -q --no-warnings --no-playlist -f 'bv*[height<=1080][vcodec^=avc1]+ba/bv*[height<=1080]+ba/b[height<=1080]/b' --merge-output-format mp4 "${X[@]}" -o "$OUT/$name.%(ext)s" -- "$url" >> dl.log 2>&1; rc=$?
  echo "$(date +%T) rc=$rc $name $(ls -la $OUT/$name.mp4 2>/dev/null|awk '{print $5}')" >> dl.log
  echo "$line" >> dl-done.txt
  [ $rc -eq 75 ] && { echo "STOP75" >> dl.log; exit 75; }
  [ $rc -eq 124 ] && { echo "TIMEOUT124 $name (split it)" >> dl.log; }
  tail -5 dl.log | grep -qiE "HTTP Error 403|HTTP Error 429|not a bot|Sign in to confirm" && { echo "STOP403" >> dl.log; exit 75; }
done
