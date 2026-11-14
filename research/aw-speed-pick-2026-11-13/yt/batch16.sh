#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
log=research/aw-speed-pick-2026-11-13/yt/batch16.log
chk(){ if tail -25 $log | grep -qiE "HTTP Error 429|not a bot|confirm you.re not a bot"; then echo "BOT/429 seen, stopping" >> $log; exit 9; fi; }
for id in D5FYQQm7IYs v-CQFdbVgCI ObWG_5dENy0 FWSrzjozAMU h5gQWaeVW00 3FT7fOsUsd4 bcIJJb9-JjA _VSHiZ8G8B8 H81Qnad27jQ m_MxS1uvnYc 12bBWIGNjU4 49LIDsOrWtM x3rRVV6czyA -L8IMvngcpk CY0qWjI8hds P4HHaMkbUi0 D5RP_85y0-Q PbN0vD4cOzQ rjQjlYbcNTg _n7kwq8oZ1Y GdoMvHah58I; do
  echo "== meta $id $(date '+%T')" >> $log
  bash $L youtube yt-dlp --skip-download --no-playlist --print "%(id)s | %(upload_date)s | %(duration)s | %(view_count)s | %(channel)s | %(height)sp | %(title)s || %(description).260s" --print "%(chapters)s" "https://www.youtube.com/watch?v=$id" >> $log 2>&1; chk; sleep 45
done
echo DONE >> $log
