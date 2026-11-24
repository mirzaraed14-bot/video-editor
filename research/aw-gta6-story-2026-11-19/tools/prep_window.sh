#!/bin/bash
# prep_window.sh <media file> : probe, 16 kHz mono wav for ASR, a 1-frame-per-5s contact sheet (silent; never plays anything)
set -u
f="$1"; d=$(dirname "$f"); b=$(basename "${f%.*}")
ffprobe -v error -show_entries stream=codec_type,codec_name,width,height,r_frame_rate,bit_rate -show_entries format=duration,bit_rate -of compact "$f" > "$d/$b.probe.txt"
cat "$d/$b.probe.txt"
ffmpeg -v error -y -i "$f" -vn -ac 1 -ar 16000 "$d/$b.wav"
if ffprobe -v error -select_streams v -show_entries stream=codec_type -of csv=p=0 "$f" | grep -q video; then
  ffmpeg -v error -y -i "$f" -vf "fps=1/5,scale=384:-1,drawtext=text='%{pts\:hms}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black" -frames:v 400 "$d/${b}_t%03d.jpg" 2>/dev/null || ffmpeg -v error -y -i "$f" -vf "fps=1/5,scale=384:-1" "$d/${b}_t%03d.jpg"
fi
echo prepped
