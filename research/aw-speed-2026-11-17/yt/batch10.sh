#!/usr/bin/env bash
# batch10 (17 Nov 2026 ~19:20, pass 3 rework after Affan's "has potential but this sequence isnt it its too dry"): four pulls, one at a time.
#   Ec18vXsDHYU  his own "Hi Me In 3 Years" (2020 message at 15, posted Oct 2023): teen footage OK per Affan's 14 Nov rule
#   nVq2DON5YKw  DaPlug "IShowSpeed Asks Kai Cenat If He Feels Lonely!" (Aug 2026, 920K, 15 s): scouting for the words + source
#   nQs6jA11sQo  Speedy Boykins "iShowSpeed Talks To His 18 Year Old Self *EMOTIONAL*" (30 Sep 2026, 3:51): his stream opening the message
#   155kZGAuCHc  THTOM "iShowSpeed in 3 years.." (27 Sep 2026, 161K, 30 s): freshness check (unread)
cd "/x/Claude Projects/video-editor-client/video-editor" || exit 1
P=projects/_onyx-batch2-2026-10/pace.sh
FLAG=projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED
log=research/aw-speed-2026-11-17/yt/batch10.log
out=research/aw-speed-2026-11-17/src
chk() { [ "$1" -eq 75 ] && { echo "pace.sh says BLOCKED, stopping" >> "$log"; exit 75; }
  if tail -30 "$log" | grep -qiE "HTTP Error 429|not a bot"; then
    echo "$(date '+%F %T') speed-beats batch10: bot check or 429 on $2; YouTube stopped; the hub clears this flag." > "$FLAG"
    echo "BOT/429 on $2: flag set, stopping" >> "$log"; exit 9; fi; }
for id in Ec18vXsDHYU nVq2DON5YKw nQs6jA11sQo 155kZGAuCHc; do
  [ -f "$FLAG" ] && { echo "BLOCKED, stopping ($(date '+%T'))" >> "$log"; exit 75; }
  echo "== $id $(date '+%T')" >> "$log"
  bash $P youtube yt-dlp -f "bv*[height<=1920][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1920]+ba/b" --merge-output-format mp4 \
    --no-playlist --write-info-json -o "$out/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" >> "$log" 2>&1
  rc=$?; chk $rc $id; echo "rc=$rc $(date '+%T')" >> "$log"
done
[ -f "$FLAG" ] && { echo "BLOCKED, stopping ($(date '+%T'))" >> "$log"; exit 75; }
echo "BATCH10 DONE $(date '+%T')" >> "$log"
