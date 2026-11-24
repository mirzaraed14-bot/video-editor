#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
OUT=research/aw-hp-2026-11-23/src
dl(){ local tag=$1 id=$2 sec=$3; local extra=(); [ -n "$sec" ] && extra=(--download-sections "*$sec")
  echo "[$(date '+%T')] start $tag $id $sec" >> $OUT/queue.log
  bash projects/_onyx-batch2-2026-10/pace.sh youtube yt-dlp --no-warnings --no-playlist \
    -f "bv*[vcodec^=avc1][height<=1080]+ba[ext=m4a]/bv*[height<=1080][ext=mp4]+ba[ext=m4a]/b[height<=1080]" "${extra[@]}" \
    -o "$OUT/%(id)s_$tag.%(ext)s" "https://www.youtube.com/watch?v=$id" > "$OUT/dl_$tag.log" 2>&1
  local rc=$?; echo "[$(date '+%T')] end $tag rc=$rc" >> $OUT/queue.log
  if grep -q -i -E "not a bot|sign in to confirm|HTTP Error 429|HTTP Error 403" "$OUT/dl_$tag.log"; then
    echo "$(date '+%F %T') hp-short (aw-hp-2026-11-23): bot page / 429 / 403 on $id ($tag)" > "projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED"
    echo "[$(date '+%T')] BLOCKED flag set" >> $OUT/queue.log; exit 75; fi
  [ $rc -eq 0 ] || exit $rc; }
dl hsc2026_full_3800-5200 4PxqJWglmH8 "00:38:00-00:52:00"
dl ross2021 bIOkpZKdwQw ""
echo "[$(date '+%T')] ALL DONE 2" >> $OUT/queue.log
