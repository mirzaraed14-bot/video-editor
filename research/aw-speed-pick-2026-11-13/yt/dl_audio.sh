#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
d=research/aw-speed-pick-2026-11-13/src
log=research/aw-speed-pick-2026-11-13/yt/dl.log
for id in ZQu2g8VUs6g 52pXQVGHwEE 8AKJH_chWQQ auSbPov16vA fox09o3r2SU QaBBgNjc5Pg; do
  echo "== $id $(date '+%T')" >> $log
  bash $L youtube yt-dlp -f "bestaudio[ext=m4a]/bestaudio" --no-playlist --write-info-json --no-write-subs --no-write-auto-subs -o "$d/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" >> $log 2>&1
  echo "rc=$?" >> $log
  if tail -20 $log | grep -qiE "sign in to confirm|HTTP Error 429|not a bot"; then echo "BOT/429 seen, stopping" >> $log; exit 9; fi
  sleep 45
done
echo DONE >> $log
