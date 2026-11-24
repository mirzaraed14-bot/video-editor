#!/bin/bash
cd "$(dirname "$0")"; . ./yt.sh; cd lists
A="xqc summit1g fanum lacy caseoh_ brendaniel hutchmf typicalgamer jasontheween theburntpeanut stableronaldo jynxzi adinross n3on agent00 clix plaqueboymax asmongold timthetatman sodapoppin ohnepixel swagg"
B="kaicenat ishowspeed"
P2="ludwig shroud valkyrae pokimane emiru mizkif hasanabi esfandtv quin69 nadeshot ninja dream ranboo tommyinnit"
run() { ch=$1; rng=$2; out="r-$ch-$rng.json"; [ -s "$out" ] && return
  YT_LOW=1 yt --flat-playlist --playlist-end 150 -J "https://www.twitch.tv/$ch/clips?filter=clips&range=$rng" > "$out" 2> "r-$ch-$rng.err"
  [ -s "$out" ] || rm -f "$out"; }
for ch in $A; do run $ch 24hr; done; echo "A-24hr done $(date +%T)" >> ../pull.log
for ch in $A; do run $ch 7d; done; echo "A-7d done $(date +%T)" >> ../pull.log
for ch in $P2; do run $ch 24hr; done; echo "P2-24hr done $(date +%T)" >> ../pull.log
for ch in $P2; do run $ch 7d; done; echo "P2-7d done $(date +%T)" >> ../pull.log
for ch in $B $A $P2; do run $ch all; done
echo ALLDONE >> ../pull.log
