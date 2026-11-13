#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
d=research/aw-speed-pick-2026-11-13/src
log=research/aw-speed-pick-2026-11-13/yt/batch4.log
chk(){ if tail -25 $log | grep -qiE "sign in to confirm|HTTP Error 429|not a bot"; then echo "BOT/429 seen, stopping" >> $log; exit 9; fi; }
sleep 40
echo "== AW millionaire short $(date '+%T')" >> $log
bash $L youtube yt-dlp -f "bv*[height<=1920][ext=mp4]+ba[ext=m4a]/b" --merge-output-format mp4 --no-playlist --write-info-json -o "$d/aw_own/%(id)s.%(ext)s" "https://www.youtube.com/shorts/GBvPG_TpMpk" >> $log 2>&1; chk; sleep 45
for id in I883j8Wu1kw kD1VVGpA8n0 MFBIqsJSocM; do
  echo "== meta $id $(date '+%T')" >> $log
  bash $L youtube yt-dlp --skip-download --no-playlist --print "%(id)s | %(upload_date)s | %(view_count)s | %(like_count)s | %(title)s" "https://www.youtube.com/shorts/$id" >> $log 2>&1; chk; sleep 45
done
echo "== Speed 2026 SOTY short $(date '+%T')" >> $log
bash $L youtube yt-dlp -f "bv*[ext=mp4]+ba[ext=m4a]/b" --merge-output-format mp4 --no-playlist --write-info-json -o "$d/%(id)s.%(ext)s" "https://www.youtube.com/shorts/M1V5cpbdwtQ" >> $log 2>&1; chk
echo DONE >> $log
