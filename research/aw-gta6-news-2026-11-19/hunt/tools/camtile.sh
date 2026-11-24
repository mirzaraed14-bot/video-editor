#!/bin/bash
# camtile.sh <clip.mp4> <x> <y> <w> <h> <t0> <dur> <n> <out.jpg>   -> n face-cam frames across [t0,t0+dur] tiled in a row
cd "X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/hunt"
clip=$1; x=$2; y=$3; w=$4; h=$5; t0=$6; dur=$7; n=$8; out=$9
tmp=frames/camtmp; rm -rf $tmp; mkdir -p $tmp
ffmpeg -v error -y -an -ss $t0 -t $dur -i "$clip" -vf "fps=$n/$dur,crop=$w:$h:$x:$y,scale=320:-1" -frames:v $n $tmp/c-%02d.jpg
args=""; i=0; for f in $tmp/c-*.jpg; do t=$(python -c "print(round($t0+$i*$dur/$n,1))"); args="$args ${t}s=$f"; i=$((i+1)); done
uv run -q --with pillow python -I tools/sheet.py "$out" ${10:-6} 320 $args
