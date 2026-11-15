#!/usr/bin/env bash
# Phase F (ig-mj, 15 Nov 08:30 PKT), for Affan's own pasted sequence (Paris's red 2012 interview): the HD Part 01 (9Cnw4Hn6KL0, the
# on-disk copy's video stream stops at 417 s) and ppb fan's Part 2 (CAI0wqlsL3Q, SD, his screenshot). Same terms as phase E: one at a
# time through pace.sh, <=1080p, no cookies, HLS first. Bot page / 429 -> flag + stop. Part 2 gets a CPU transcript (medium.en).
. "/x/Claude Projects/video-editor-client/video-editor/research/deep-research-2026-11-14/ig-mj/tools/common.sh"
FMT='bv*[protocol^=m3u8][height<=1080][vcodec^=avc1]+ba[protocol^=m3u8]/b[protocol^=m3u8][height<=1080]/bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/b[height<=1080]'
quiet() { local free=0 cap=$(( $(date +%s) + 1200 )); while [ $free -lt 20 ] && [ "$(date +%s)" -lt "$cap" ]; do [ -f "$FLAG" ] && exit 75; if [ -d "$LOCKDIR" ]; then free=0; else free=$((free+5)); fi; sleep 5; done; }
one() {
  local id=$1 out=$2
  [ -f "$FLAG" ] && { echo "$(date '+%F %T') BLOCKED flag present, not requesting $id" >> "$log"; exit 75; }
  quiet; mkdir -p "$out"
  echo "== F $id $(date '+%F %T')" >> "$log"
  bash $L youtube yt-dlp --no-playlist --no-cookies --no-cookies-from-browser --no-write-comments --sleep-requests 15 \
    -f "$FMT" --merge-output-format mp4 --write-info-json --no-progress -o "$out/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" >> "$log" 2>&1
  local rc=$?; echo "rc=$rc $(date '+%T')" >> "$log"
  [ $rc -eq 75 ] && { echo "pace.sh says BLOCKED, stopping" >> "$log"; exit 75; }
  if tail -40 "$log" | grep -qiE "HTTP Error 429|Too Many Requests|not a bot|Sign in to confirm"; then
    echo "$(date '+%F %T') ig-mj: bot check or 429 on $id; YouTube stopped; the hub clears this flag." > "$FLAG"; echo "BOT/429 on $id: flag set" >> "$log"; exit 9
  fi
}
asr_free() { while ps -ef 2>/dev/null | grep -v grep | grep -q "fw2.py"; do sleep 10; done; }
P=projects/mj-the-dad-he-never-had/sources
one 9Cnw4Hn6KL0 "$P/9Cnw4Hn6KL0"
one CAI0wqlsL3Q "$P/CAI0wqlsL3Q"
asr_free; post "$P/CAI0wqlsL3Q/CAI0wqlsL3Q.mp4"
echo "PHASE F DONE $(date '+%T')" >> "$log"
