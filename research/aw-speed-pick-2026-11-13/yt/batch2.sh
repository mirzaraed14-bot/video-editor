#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
d=research/aw-speed-pick-2026-11-13/src
log=research/aw-speed-pick-2026-11-13/yt/batch2.log
until grep -qE "^DONE|BOT/429" research/aw-speed-pick-2026-11-13/yt/dl.log; do sleep 5; done
grep -q "BOT/429" research/aw-speed-pick-2026-11-13/yt/dl.log && { echo "batch1 hit a block; not running" >> $log; exit 9; }
sleep 40
chk(){ if tail -25 $log | grep -qiE "sign in to confirm|HTTP Error 429|not a bot"; then echo "BOT/429 seen, stopping" >> $log; exit 9; fi; }
echo "== channel uploads $(date '+%T')" >> $log
bash $L youtube yt-dlp --flat-playlist --playlist-end 30 --print "%(id)s | %(view_count)s | %(duration)s | %(title)s" "https://www.youtube.com/@TheStreamerAwards/videos" >> $log 2>&1; chk; sleep 45
echo "== Lost Reality meta $(date '+%T')" >> $log
bash $L youtube yt-dlp --skip-download --no-playlist --print "%(id)s | %(upload_date)s | %(title)s || %(description)s" "https://www.youtube.com/watch?v=FJ42TkMQBd8" >> $log 2>&1; chk; sleep 45
for id in CmpgXX7ZWJU; do
  echo "== audio $id $(date '+%T')" >> $log
  bash $L youtube yt-dlp -f "bestaudio[ext=m4a]/bestaudio" --no-playlist --write-info-json --no-write-subs --no-write-auto-subs -o "$d/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" >> $log 2>&1; chk; sleep 45
done
echo "== search youshaei $(date '+%T')" >> $log
bash $L youtube yt-dlp --flat-playlist --print "%(id)s | %(view_count)s | %(duration)s | %(channel)s | %(title)s" "ytsearch8:IShowSpeed interview mom kicked me out Detroit dad lonely" >> $log 2>&1; chk
echo DONE >> $log
