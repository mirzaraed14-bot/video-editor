#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
d=research/aw-speed-pick-2026-11-13/src
log=research/aw-speed-pick-2026-11-13/yt/batch13.log
P="C:/Users/affan/.cache/video-editor/whisperx-venv/Scripts/python.exe"
S="C:/Users/affan/AppData/Local/Temp/claude/bd0643937bf87bde/839da3b4-2c97-4d47-b3e8-feb69497aaf3/scratchpad/cpu_scout.py"
chk(){ if tail -25 $log | grep -qiE "HTTP Error 429|not a bot|confirm you.re not a bot"; then echo "BOT/429 seen, stopping" >> $log; exit 9; fi; }
for id in nQs6jA11sQo jhKTrZTfofU; do
  echo "== audio $id $(date '+%T')" >> $log
  bash $L youtube yt-dlp -f "bestaudio[ext=m4a]/bestaudio" --no-playlist --write-info-json -o "$d/%(id)s.%(ext)s" "https://www.youtube.com/watch?v=$id" >> $log 2>&1; chk; sleep 45
done
cd research/aw-speed-pick-2026-11-13
for id in nQs6jA11sQo jhKTrZTfofU; do [ -f src/$id.m4a ] && "$P" -I "$S" scout src/$id.m4a >> yt/batch13.log 2>&1; done
echo DONE >> yt/batch13.log
