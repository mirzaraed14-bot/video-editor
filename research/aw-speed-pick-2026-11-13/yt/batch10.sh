#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
d=research/aw-speed-pick-2026-11-13/src
log=research/aw-speed-pick-2026-11-13/yt/batch10.log
chk(){ if tail -25 $log | grep -qiE "HTTP Error 429|not a bot|confirm you.re not a bot"; then echo "BOT/429 seen, stopping" >> $log; exit 9; fi; }
q(){ echo "== search: $1 $(date '+%T')" >> $log; bash $L youtube yt-dlp --flat-playlist --print "%(id)s | %(view_count)s | %(duration)s | %(channel)s | %(title)s" "ytsearch10:$1" >> $log 2>&1; chk; sleep 45; }
echo "== HD full ep childhood 1:34:35-1:35:30 $(date '+%T')" >> $log
bash $L youtube yt-dlp -f "bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1080]+ba/b" --merge-output-format mp4 --no-playlist --download-sections "*1:34:35-1:35:30" -o "$d/hd/QaBBgNjc5Pg_childhood.%(ext)s" "https://www.youtube.com/watch?v=QaBBgNjc5Pg" 2>&1 | tr '\r' '\n' | grep -v "^\[download\]" >> $log; chk; sleep 45
q "ishowspeed i feel alone i need a therapist stream"
q "ishowspeed irl stream in america keystone south dakota"
q "ishowspeed mount rushmore stream day 24"
echo DONE >> $log
