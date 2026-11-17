#!/usr/bin/env bash
# batch14 (17 Nov 2026 ~23:08, the Darren sequence): two scouting pulls, monium "Old Speed almost came out" (A3LvS9N75uc, 13.5M, 7 s) and "No Darren Watkins, only Speed" (YhRGidNvn94, 9.85M, 11 s), to see the moments and find his own source.
cd "/x/Claude Projects/video-editor-client/video-editor" || exit 1
P=projects/_onyx-batch2-2026-10/pace.sh
FLAG=projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED
log=research/aw-speed-2026-11-17/yt/batch14.log
out=research/aw-speed-2026-11-17/src
chk() { [ "$1" -eq 75 ] && { echo "pace.sh says BLOCKED, stopping" >> "$log"; exit 75; }
  if tail -30 "$log" | grep -qiE "HTTP Error 429|not a bot"; then
    echo "$(date '+%F %T') speed-beats batch14: bot check or 429 on $2; YouTube stopped; the hub clears this flag." > "$FLAG"
    echo "BOT/429 on $2: flag set, stopping" >> "$log"; exit 9; fi; }
for id in A3LvS9N75uc YhRGidNvn94; do
  [ -f "$FLAG" ] && { echo "BLOCKED, stopping ($(date '+%T'))" >> "$log"; exit 75; }
  echo "== $id $(date '+%T')" >> "$log"
  bash $P youtube yt-dlp -f "bv*[height<=1920][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1920]+ba/b" --merge-output-format mp4 \
    --no-playlist --write-info-json -o "$out/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" >> "$log" 2>&1
  rc=$?; chk $rc $id; echo "rc=$rc $(date '+%T')" >> "$log"
done
[ -f "$FLAG" ] && { echo "BLOCKED, stopping ($(date '+%T'))" >> "$log"; exit 75; }
echo "BATCH14 DONE $(date '+%T')" >> "$log"
