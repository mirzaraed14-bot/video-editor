#!/usr/bin/env bash
# aw-hp-2026-11-23 downloads: one at a time through pace.sh youtube, H.264 first, no cookies/captions/listings.
cd "/x/Claude Projects/video-editor-client/video-editor"
OUT=research/aw-hp-2026-11-23/src
dl(){ local tag=$1 id=$2
  echo "[$(date '+%T')] start $tag $id" >> $OUT/queue.log
  bash projects/_onyx-batch2-2026-10/pace.sh youtube yt-dlp --no-warnings --no-playlist \
    -f "bv*[vcodec^=avc1][height<=1080]+ba[ext=m4a]/bv*[height<=1080][ext=mp4]+ba[ext=m4a]/b[height<=1080]" \
    -o "$OUT/%(id)s_$tag.%(ext)s" "https://www.youtube.com/watch?v=$id" > "$OUT/dl_$tag.log" 2>&1
  local rc=$?; echo "[$(date '+%T')] end $tag rc=$rc" >> $OUT/queue.log
  if grep -q -i -E "not a bot|sign in to confirm|HTTP Error 429|HTTP Error 403" "$OUT/dl_$tag.log"; then
    echo "$(date '+%F %T') hp-short (aw-hp-2026-11-23): bot page / 429 / 403 on $id ($tag)" > "projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED"
    echo "[$(date '+%T')] BLOCKED flag set" >> $OUT/queue.log; exit 75; fi
  [ $rc -eq 0 ] || exit $rc; }
dl rad2026_cringe 2zx_rQpE4Ow
dl rad2026_rankings LcdJXjfpGmo
dl garfield2026_mlim YtDD9nUvicA
echo "[$(date '+%T')] ALL DONE" >> $OUT/queue.log
