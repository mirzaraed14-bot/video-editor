#!/usr/bin/env bash
# Phase C (ig-mj, 15 Nov 00:20): ONE retry each of the two HTTP-403 downloads (DASH format 137 refused), now HLS-first
# (270 avc1 1080p + 234 audio, chunked m3u8). Waits for phase B's Gary download to finish, then for the YouTube lock to be
# free 60 s before each request (pace.sh let two holders overlap at 00:14), then pace.sh as usual. Transcribes after phase B.
. "/x/Claude Projects/video-editor-client/video-editor/research/deep-research-2026-11-14/ig-mj/tools/common.sh"
FMT='bv*[protocol^=m3u8][height<=1080][vcodec^=avc1]+ba[protocol^=m3u8][language^=en]/bv*[protocol^=m3u8][height<=1080][vcodec^=avc1]+ba[protocol^=m3u8]/b[protocol^=m3u8][height<=1080]/bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]'
quiet() { local cap=$(( $(date +%s) + 1800 )) free=0; while [ $free -lt 60 ] && [ "$(date +%s)" -lt "$cap" ]; do if [ -d "$LOCKDIR" ]; then free=0; else free=$((free+5)); fi; sleep 5; done; }
dlh() {  # $1 = id, $2 = folder
  local id=$1 out=$2
  [ -f "$FLAG" ] && { echo "$(date '+%F %T') BLOCKED flag present, not requesting $id" >> "$log"; exit 75; }
  quiet
  mkdir -p "$out"
  echo "== RETRY-HLS $id $(date '+%F %T')" >> "$log"
  bash $L youtube yt-dlp --no-playlist --no-cookies --no-cookies-from-browser --no-write-comments --sleep-requests 15 \
    -f "$FMT" --merge-output-format mp4 --write-info-json --no-progress \
    -o "$out/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" >> "$log" 2>&1
  local rc=$?
  echo "rc=$rc $(date '+%T')" >> "$log"
  [ $rc -eq 75 ] && { echo "pace.sh says BLOCKED, stopping" >> "$log"; exit 75; }
  if tail -40 "$log" | grep -qiE "HTTP Error 429|Too Many Requests|not a bot|Sign in to confirm"; then
    echo "$(date '+%F %T') ig-mj: bot check or 429 on $id; YouTube stopped; the hub clears this flag." > "$FLAG"
    echo "BOT/429 on $id: flag set, stopping" >> "$log"; exit 9
  fi
}
until grep -q "^== post research/deep-research-2026-11-14/ig-mj/dl/8Ys5IngU6wg" "$log"; do [ -f "$FLAG" ] && exit 75; sleep 10; done
P=projects/mj-son-red-armband/sources
dlh ESeXvAeuokU "$P/ESeXvAeuokU"
dlh snMguJ8UuyI "$P/snMguJ8UuyI"
w=0; until grep -q "^PHASE B DONE" "$log" || [ $w -gt 3600 ]; do sleep 15; w=$((w+15)); done
post "$P/ESeXvAeuokU/ESeXvAeuokU.mp4"
post "$P/snMguJ8UuyI/snMguJ8UuyI.mp4"
echo "PHASE C DONE $(date '+%T')" >> "$log"
