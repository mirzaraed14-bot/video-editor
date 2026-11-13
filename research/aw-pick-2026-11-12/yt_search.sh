#!/usr/bin/env bash
# Spaced YouTube searches for the AW pick run (12 Nov). One request per >=65 s through lock.sh youtube.
# Each query -> yt/<slug>.txt with "id | duration s | views | channel | title" for the top 40 results. Stops on any failure;
# a 429 / bot page writes the BLOCKED flag. Usage: yt_search.sh "query one" "query two" ...
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
FLAG=projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED
D=research/aw-pick-2026-11-12/yt
for q in "$@"; do
  slug=$(echo "$q" | tr ' ' '_' | tr -cd 'A-Za-z0-9_'); out="$D/$slug.txt"
  [ -s "$out" ] && continue
  enc=$(python -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")
  log=$(mktemp)
  bash $L youtube yt-dlp --no-warnings --flat-playlist --playlist-end 40 --print "%(id)s | %(duration)s | %(view_count)s | %(channel)s | %(title)s" "https://www.youtube.com/results?search_query=$enc" >"$out" 2>"$log"
  rc=$?; echo "$(date '+%T') [$q] rc=$rc lines=$(wc -l <"$out")" >> "$D/../search.log"
  if [ $rc -ne 0 ]; then
    cat "$log" >> "$D/../search.log"
    if grep -qiE "429|not a bot|confirm you|Sign in to confirm|Too Many Requests" "$log"; then
      [ -f "$FLAG" ] || echo "429/bot AW-pick-2026-11-12 search [$q] $(date '+%F %T')" > "$FLAG"; exit 2; fi
    exit 1
  fi
  rm -f "$log"; sleep 45
done
echo "$(date '+%T') done" >> "$D/../search.log"
