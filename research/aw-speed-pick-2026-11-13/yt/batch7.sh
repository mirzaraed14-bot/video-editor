#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
log=research/aw-speed-pick-2026-11-13/yt/batch7.log
chk(){ if tail -25 $log | grep -qiE "HTTP Error 429|not a bot|confirm you.re not a bot"; then echo "BOT/429 seen, stopping" >> $log; exit 9; fi; }
q(){ echo "== search: $1 $(date '+%T')" >> $log; bash $L youtube yt-dlp --flat-playlist --print "%(id)s | %(view_count)s | %(duration)s | %(channel)s | %(title)s" "ytsearch10:$1" >> $log 2>&1; chk; sleep 45; }
m(){ echo "== meta: $1 $(date '+%T')" >> $log; bash $L youtube yt-dlp --skip-download --no-playlist --print "%(id)s | %(upload_date)s | %(view_count)s | %(duration)s | %(channel)s | %(title)s || %(description).250s" "https://www.youtube.com/watch?v=$1" >> $log 2>&1; chk; sleep 45; }
q "ishowspeed lonely no friends covid"
q "ishowspeed my mom always supported me"
q "ishowspeed dad interview moved to detroit"
q "ishowspeed mom interview speaks about son"
q "jon youshaei ishowspeed interview"
q "ishowspeed moved in with his dad detroit shorts"
m v-CQFdbVgCI
m -RYIL98FSTo
m rAlQjjRJ_JQ
m KCOIJjpLk1M
echo DONE >> $log
