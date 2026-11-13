#!/usr/bin/env bash
# Source downloads for an AW pick (12 Nov). Usage: dl_src.sh <outdir> <id>...  One request per >=65 s through lock.sh youtube.
# H.264 <=1080 preferred, best otherwise. Stops on any failure; a 429 / bot page writes the BLOCKED flag. Nothing is played.
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh; FLAG=projects/_onyx-batch2-2026-10/.locks/youtube.BLOCKED
OUT=$1; shift; mkdir -p "$OUT"; LOG=research/aw-pick-2026-11-12/dl_src.log
for id in "$@"; do
  if ls "$OUT/$id".* >/dev/null 2>&1; then continue; fi
  t=$(mktemp)
  for try in 1 2; do
  bash $L youtube yt-dlp --no-warnings --no-playlist -f "137+140/bv*[vcodec^=avc1][height<=1080]+ba[ext=m4a]/bv*[height<=1080]+ba/b" --merge-output-format mp4 -o "$OUT/%(id)s.%(ext)s" -- "https://www.youtube.com/watch?v=$id" >"$t" 2>&1
  rc=$?; echo "$(date '+%T') $id try$try rc=$rc $(grep -m1 -oE 'ERROR.*' "$t" | cut -c1-160)" >> $LOG
  if [ $rc -ne 0 ] && grep -q "Requested format is not available" "$t" && [ $try -eq 1 ]; then sleep 60; continue; fi
  break; done
  if [ $rc -ne 0 ]; then
    if grep -qiE "429|not a bot|confirm you|Sign in to confirm|Too Many Requests" "$t"; then
      [ -f "$FLAG" ] || echo "429/bot AW-pick-2026-11-12 download $id $(date '+%F %T')" > "$FLAG"; echo "$(date '+%T') BOT/429 flag written" >> $LOG; exit 2; fi
    if grep -qiE "unavailable|not available in your country|private|removed|copyright" "$t"; then rm -f "$t"; sleep 45; continue; fi
    exit 1
  fi
  rm -f "$t"; sleep 45
done
echo "$(date '+%T') done $OUT" >> $LOG
