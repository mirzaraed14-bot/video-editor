#!/usr/bin/env bash
# Phase E (ig-mj, 15 Nov 03:05), the hub's 02:35 grant for Affan's "go all out" arc: our own 5.1M "On His CRUEL Father" (Jd7STI2SpWM),
# then the 1979 interview (fTTl4Vaow5Y). One at a time through pace.sh (180 s apart), <=1080p, no cookies; HLS first (DASH 403'd here
# before), DASH as the fallback. Bot page / 429 -> flag + stop. Transcripts wait until no other fw2.py run is active (mkl_malloc).
. "/x/Claude Projects/video-editor-client/video-editor/research/deep-research-2026-11-14/ig-mj/tools/common.sh"
FMT='bv*[protocol^=m3u8][height<=1080][vcodec^=avc1]+ba[protocol^=m3u8]/b[protocol^=m3u8][height<=1080]/bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/b[height<=1080]'
quiet() { local free=0 cap=$(( $(date +%s) + 1200 )); while [ $free -lt 20 ] && [ "$(date +%s)" -lt "$cap" ]; do [ -f "$FLAG" ] && exit 75; if [ -d "$LOCKDIR" ]; then free=0; else free=$((free+5)); fi; sleep 5; done; }
one() {
  local id=$1 out=$2
  [ -f "$FLAG" ] && { echo "$(date '+%F %T') BLOCKED flag present, not requesting $id" >> "$log"; exit 75; }
  quiet; mkdir -p "$out"
  echo "== E $id $(date '+%F %T')" >> "$log"
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
one Jd7STI2SpWM "$P/Jd7STI2SpWM"
one fTTl4Vaow5Y "$P/fTTl4Vaow5Y"
asr_free; post "$P/Jd7STI2SpWM/Jd7STI2SpWM.mp4"
asr_free; post "$P/fTTl4Vaow5Y/fTTl4Vaow5Y.mp4"
echo "PHASE E DONE $(date '+%T')" >> "$log"
