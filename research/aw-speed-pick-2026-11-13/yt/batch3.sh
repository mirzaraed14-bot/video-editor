#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
log=research/aw-speed-pick-2026-11-13/yt/batch3.log
chk(){ if tail -25 $log | grep -qiE "sign in to confirm|HTTP Error 429|not a bot"; then echo "BOT/429 seen, stopping" >> $log; exit 9; fi; }
echo "== VOD meta $(date '+%T')" >> $log
bash $L youtube yt-dlp --skip-download --no-playlist --print "%(id)s | %(duration)s | %(upload_date)s | %(live_status)s | %(title)s" --print "%(chapters)s" "https://www.youtube.com/watch?v=ydxPi62euMo" >> $log 2>&1; chk; sleep 45
echo "== search therapist $(date '+%T')" >> $log
bash $L youtube yt-dlp --flat-playlist --print "%(id)s | %(view_count)s | %(duration)s | %(channel)s | %(title)s" "ytsearch10:speed says he needs a therapist feels alone usa tour" >> $log 2>&1; chk; sleep 45
echo "== fan 2026 SOTY short meta $(date '+%T')" >> $log
bash $L youtube yt-dlp --skip-download --no-playlist --print "%(id)s | %(upload_date)s | %(view_count)s | %(channel)s | %(title)s || %(description).300s" "https://www.youtube.com/shorts/M1V5cpbdwtQ" >> $log 2>&1; chk
echo DONE >> $log
