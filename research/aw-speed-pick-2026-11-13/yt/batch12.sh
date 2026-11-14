#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
log=research/aw-speed-pick-2026-11-13/yt/batch12.log
chk(){ if tail -25 $log | grep -qiE "HTTP Error 429|not a bot|confirm you.re not a bot"; then echo "BOT/429 seen, stopping" >> $log; exit 9; fi; }
for id in nQs6jA11sQo jhKTrZTfofU B_FCc7hyLWM; do
  echo "== meta $id $(date '+%T')" >> $log
  bash $L youtube yt-dlp --skip-download --no-playlist --print "%(id)s | %(upload_date)s | %(view_count)s | %(duration)s | %(channel)s | %(title)s || %(description).350s" "https://www.youtube.com/watch?v=$id" >> $log 2>&1; chk; sleep 45
done
echo DONE >> $log
