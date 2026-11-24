#!/bin/bash
# clipsheet.sh <name> [cols] : 12 frames evenly + sheet, loudness
cd "X:/Claude Projects/video-editor-client/video-editor/research/aw-gta6-news-2026-11-19/hunt"
n=$1; f=clips/$n.mp4
d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $f)
mkdir -p frames/$n; rm -f frames/$n/s-*.jpg
ffmpeg -v error -y -an -i $f -vf "fps=12/$d,scale=480:-1" frames/$n/s-%02d.jpg
args=""; i=0; for fr in frames/$n/s-*.jpg; do t=$(python -c "print(round($i*$d/12,1))"); args="$args ${t}s=$fr"; i=$((i+1)); done
uv run -q --with pillow python -I tools/sheet.py sheets/$n.jpg ${2:-4} 480 $args
echo "dur=$d $(ffprobe -v error -select_streams v -show_entries stream=width,height,r_frame_rate -of csv=p=0 $f)"
python -I tools/loud.py $f
