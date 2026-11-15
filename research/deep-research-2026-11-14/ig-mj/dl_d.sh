#!/usr/bin/env bash
# Phase D (ig-mj, 15 Nov 00:24), on the hub's 00:20 terms: ONE retry each of the two HTTP-403 clips with the HLS formats
# (-f 270+234; ESeXvAeuokU's audio IDs carry a language suffix, so its original-English track is 234-20), plain yt-dlp, default
# clients, one at a time through pace.sh, only after hp-cast's pid 168436 has exited and the lock has been free 60 s.
# A second 403 = that clip is unavailable (no more formats). Bot page / 429 = flag + stop.
. "/x/Claude Projects/video-editor-client/video-editor/research/deep-research-2026-11-14/ig-mj/tools/common.sh"
quiet() { local free=0; while [ $free -lt 60 ]; do [ -f "$FLAG" ] && exit 75; if [ -d "$LOCKDIR" ]; then free=0; else free=$((free+5)); fi; sleep 5; done; }
while kill -0 168436 2>/dev/null; do sleep 10; done
echo "$(date '+%F %T') phase D: pid 168436 gone" >> "$log"
one() {  # $1 id, $2 folder, $3 format
  local id=$1 out=$2 fmt=$3
  [ -f "$FLAG" ] && { echo "$(date '+%F %T') BLOCKED flag present, not requesting $id" >> "$log"; exit 75; }
  quiet
  mkdir -p "$out"
  echo "== RETRY $id -f $fmt $(date '+%F %T')" >> "$log"
  bash $L youtube yt-dlp --no-playlist --no-cookies --no-cookies-from-browser --no-write-comments --sleep-requests 15 \
    -f "$fmt" --merge-output-format mp4 --write-info-json --no-progress \
    -o "$out/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" >> "$log" 2>&1
  local rc=$?
  echo "rc=$rc $(date '+%T')" >> "$log"
  [ $rc -eq 75 ] && { echo "pace.sh says BLOCKED, stopping" >> "$log"; exit 75; }
  if tail -40 "$log" | grep -qiE "HTTP Error 429|Too Many Requests|not a bot|Sign in to confirm"; then
    echo "$(date '+%F %T') ig-mj: bot check or 429 on $id; YouTube stopped; the hub clears this flag." > "$FLAG"
    echo "BOT/429 on $id: flag set, stopping" >> "$log"; exit 9
  fi
  [ $rc -ne 0 ] && echo "UNAVAILABLE $id (second failure; no more formats, per the hub)" >> "$log"
}
P=projects/mj-son-red-armband/sources
one ESeXvAeuokU "$P/ESeXvAeuokU" "270+234-20"
one snMguJ8UuyI "$P/snMguJ8UuyI" "270+234"
post "$P/ESeXvAeuokU/ESeXvAeuokU.mp4"
post "$P/snMguJ8UuyI/snMguJ8UuyI.mp4"
echo "PHASE D DONE $(date '+%T')" >> "$log"
