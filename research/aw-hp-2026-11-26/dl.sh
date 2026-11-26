#!/usr/bin/env bash
# dl.sh <tag> <id> [section] [audio]: ONE paced yt-dlp pull via pace.sh (no cookies/proxies/captions). audio=1 -> bestaudio into idref/ (source identification only, never footage)
cd "/x/Claude Projects/video-editor-client/video-editor"
R=research/aw-hp-2026-11-26; tag=$1 id=$2 sec=${3:-} aud=${4:-}
extra=(); [ -n "$sec" ] && extra=(--download-sections "*$sec")
if [ -n "$aud" ]; then OUT=$R/idref; fmt="ba[ext=m4a]/ba"; else OUT=$R/src; fmt="bv*[height<=1080]+ba[ext=m4a]/bv*[height<=1080]+ba/b[height<=1080]"; fi
echo "[$(date '+%T')] start $tag $id $sec" >> $R/src/queue.log
bash projects/_onyx-batch2-2026-10/pace.sh youtube yt-dlp --no-warnings --no-playlist -f "$fmt" "${extra[@]}" \
  -o "$OUT/%(id)s_$tag.%(ext)s" "https://www.youtube.com/watch?v=$id" > "$OUT/dl_$tag.log" 2>&1
rc=$?; echo "[$(date '+%T')] end $tag rc=$rc" >> $R/src/queue.log
if grep -q -i -E "not a bot|sign in to confirm|HTTP Error 429|HTTP Error 403" "$OUT/dl_$tag.log"; then
  echo "$(date '+%F %T') hp-short (aw-hp-day2): bot page / 429 / 403 on $id ($tag)" > "projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED"
  echo "[$(date '+%T')] BLOCKED flag set" >> $R/src/queue.log; exit 75; fi
exit $rc
