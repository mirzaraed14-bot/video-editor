#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
d=research/aw-speed-pick-2026-11-13/src/mom
log=research/aw-speed-pick-2026-11-13/yt/batch17.log
P="C:/Users/affan/.cache/video-editor/whisperx-venv/Scripts/python.exe"
S="C:/Users/affan/AppData/Local/Temp/claude/bd0643937bf87bde/839da3b4-2c97-4d47-b3e8-feb69497aaf3/scratchpad/cpu_scout.py"
chk(){ if tail -25 $log | grep -qiE "HTTP Error 429|not a bot|confirm you.re not a bot"; then echo "BOT/429 seen, stopping" >> $log; exit 9; fi; }
until grep -qE "^DONE|BOT/429" research/aw-speed-pick-2026-11-13/yt/batch16.log; do sleep 15; done
grep -q "BOT/429" research/aw-speed-pick-2026-11-13/yt/batch16.log && exit 9
sleep 45
for id in h5gQWaeVW00 v-CQFdbVgCI FWSrzjozAMU ObWG_5dENy0 _VSHiZ8G8B8 H81Qnad27jQ bcIJJb9-JjA 3FT7fOsUsd4 m_MxS1uvnYc 12bBWIGNjU4; do
  echo "== dl $id $(date '+%T')" >> $log
  bash $L youtube yt-dlp -f "bv*[height<=1080][vcodec^=avc1]+ba[ext=m4a]/bv*[height<=1080]+ba/b" --merge-output-format mp4 --no-playlist --write-info-json -o "$d/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" 2>&1 | tr '\r' '\n' | grep -v "^\[download\] " >> $log; chk; sleep 45
done
echo "YT DONE $(date '+%T')" >> $log
cd research/aw-speed-pick-2026-11-13
for f in src/mom/*.mp4; do id=$(basename $f .mp4); ffmpeg -v error -y -i $f -vn -ac 1 -ar 16000 C:/Users/affan/AppData/Local/Temp/claude/bd0643937bf87bde/839da3b4-2c97-4d47-b3e8-feb69497aaf3/scratchpad/$id.wav 2>/dev/null || ffmpeg -v error -y -i $f -vn -ac 1 -ar 16000 src/mom/$id.wav; w=C:/Users/affan/AppData/Local/Temp/claude/bd0643937bf87bde/839da3b4-2c97-4d47-b3e8-feb69497aaf3/scratchpad/$id.wav; [ -f $w ] || w=src/mom/$id.wav; "$P" -I "$S" scout/mom $w >> yt/batch17.log 2>&1; rm -f $w; done
echo DONE >> yt/batch17.log
