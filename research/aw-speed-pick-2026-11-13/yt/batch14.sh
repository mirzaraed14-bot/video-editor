#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
log=research/aw-speed-pick-2026-11-13/yt/batch14.log
chk(){ if tail -25 $log | grep -qiE "HTTP Error 429|not a bot|confirm you.re not a bot"; then echo "BOT/429 seen, stopping" >> $log; exit 9; fi; }
q(){ echo "== search: $1 $(date '+%T')" >> $log; bash $L youtube yt-dlp --flat-playlist --print "%(id)s | %(view_count)s | %(duration)s | %(channel)s | %(title)s" "ytsearch10:$1" >> $log 2>&1; chk; sleep 45; }
echo "== meta Hi Me In 3 Years $(date '+%T')" >> $log
bash $L youtube yt-dlp --skip-download --no-playlist --print "%(id)s | %(upload_date)s | %(view_count)s | %(duration)s | %(channel)s | %(title)s" --print "%(formats.-1.height)s x %(formats.-1.width)s" "https://www.youtube.com/shorts/Ec18vXsDHYU" >> $log 2>&1; chk; sleep 45
q "ishowspeed stream august 2023 viral incident chat laughing be a real human being"
q "ishowspeed full stream august 18 2023"
q "ishowspeed reacts to going viral accidentally mental toll stream cries"
echo DONE >> $log
