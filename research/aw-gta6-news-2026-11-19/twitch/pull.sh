#!/bin/bash
# Twitch top-24h clip LISTS (no media), one channel at a time, 4 s apart. aw-gta6-news, 19 Nov.
cd "$(dirname "$0")"
for ch in kaicenat ishowspeed xqc jasontheween lacy fanum caseoh_ n3on typicalgamer ohnepixel clix theburntpeanut summit1g agent00 stableronaldo plaqueboymax jynxzi sketch zoil cdawgva duke marlon tfue nadeshot hasanabi sodapoppin moistcr1tikal lirik emiru brendaniel swagg hutchmf coachboop chiblee extraemily quin69 asmongold tarik shroud; do
  [ -s r-$ch.json ] && continue
  timeout 120 yt-dlp --ignore-config --flat-playlist -J "https://www.twitch.tv/$ch/clips?filter=clips&range=24hr" > r-$ch.json 2> r-$ch.err
  sleep 4
done
echo DONE > DONE
