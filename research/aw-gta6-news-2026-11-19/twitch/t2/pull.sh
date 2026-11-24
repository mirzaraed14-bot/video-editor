#!/bin/bash
cd "$(dirname "$0")"
for ch in kaicenat ishowspeed xqc caseoh_ jasontheween fanum n3on lacy hasanabi agent00 typicalgamer summit1g stableronaldo plaqueboymax jynxzi theburntpeanut clix ohnepixel; do
  timeout 120 yt-dlp --ignore-config --flat-playlist -J "https://www.twitch.tv/$ch/clips?filter=clips&range=24hr" > r-$ch.json 2> r-$ch.err; sleep 4
done
echo DONE > DONE
