#!/usr/bin/env bash
# Spaced YouTube searches through lock.sh (>=60 s apart). Metadata only.
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
out=research/aw-speed-pick-2026-11-13/yt
i=0
while IFS= read -r q; do
  [ -z "$q" ] && continue
  i=$((i+1))
  echo "== [$i] $q $(date '+%T')" >> $out/search.log
  bash $L youtube yt-dlp --flat-playlist --print "%(id)s | %(view_count)s | %(duration)s | %(channel)s | %(title)s" "ytsearch12:$q" >> $out/search.log 2>> $out/search.err
  rc=$?
  echo "rc=$rc" >> $out/search.log
  if grep -qiE "sign in to confirm|429|bot" $out/search.err; then echo "BOT/429 seen, stopping" >> $out/search.log; exit 9; fi
  sleep 45   # lock.sh adds 20 s cool-down => ~65 s apart
done < $out/queries.txt
echo DONE >> $out/search.log
