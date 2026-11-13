#!/usr/bin/env bash
cd "/x/Claude Projects/video-editor-client/video-editor"
L=projects/_onyx-batch2-2026-10/lock.sh
d=research/aw-speed-pick-2026-11-13/src
log=research/aw-speed-pick-2026-11-13/yt/batch9.log
P="C:/Users/affan/.cache/video-editor/whisperx-venv/Scripts/python.exe"
S="C:/Users/affan/AppData/Local/Temp/claude/bd0643937bf87bde/839da3b4-2c97-4d47-b3e8-feb69497aaf3/scratchpad/cpu_scout.py"
until grep -qE "YT DONE|BOT/429" research/aw-speed-pick-2026-11-13/yt/batch8.log; do sleep 10; done
grep -q "BOT/429" research/aw-speed-pick-2026-11-13/yt/batch8.log && exit 9
sleep 50
echo "== detroit sections $(date '+%T')" >> $log
bash $L youtube yt-dlp -f "bestaudio[ext=m4a]/bestaudio" --no-playlist --download-sections "*1:54:20-1:58:20" --download-sections "*2:02:45-2:22:00" -o "$d/cetc_%(section_start)s.%(ext)s" "https://www.youtube.com/watch?v=cetcKaq5y4s" 2>&1 | tr '\r' '\n' | grep -v "^\[download\]" >> $log
until grep -q "^DONE" research/aw-speed-pick-2026-11-13/yt/batch8.log; do sleep 10; done
cd research/aw-speed-pick-2026-11-13
for f in src/cetc_*.m4a; do "$P" -I "$S" scout "$f" >> yt/batch9.log 2>&1; done
cat scout/cetc_*.scout.txt 2>/dev/null | grep -n -i -E "my mom|my mother|kicked|my dad|father|detroit|started streaming|first stream|room|support|believe|proud|alone|lonely|quit|trophy|trophies|streamer of the year|cry|cried|this is where" > scout/cetc_hits.txt
echo DONE >> yt/batch9.log
