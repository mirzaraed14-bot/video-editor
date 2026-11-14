#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
log=research/aw-speed-pick-2026-11-13/yt/batch15.log
chk(){ if tail -25 $log | grep -qiE "HTTP Error 429|not a bot|confirm you.re not a bot"; then echo "BOT/429 seen, stopping" >> $log; exit 9; fi; }
q(){ echo "== search: $1 $(date '+%T')" >> $log; bash $L youtube yt-dlp --flat-playlist --print "%(id)s | %(upload_date)s | %(view_count)s | %(duration)s | %(channel)s | %(title)s" "ytsearch12:$1" >> $log 2>&1; chk; sleep 45; }
q "ishowspeed calls his mom on his birthday adin ross house no answer"
q "ishowspeed 18th birthday adin ross mom call"
q "ishowspeed mom comes in angry shut the stream off what is he doing"
q "ishowspeed sad after mom leaves room almost crying stream"
q "ishowspeed mom yells at him stream cries 2021"
q "ishowspeed phone call mom hangs up sad stream"
q "ishowspeed mom told him to stop streaming sad but kept going"
q "ishowspeed mom turns off his power internet stream"
echo DONE >> $log
