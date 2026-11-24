#!/bin/bash
# y.sh <out.json> <endpoint> k=v ... : the aw-gta6-reviews door to yt_api.py (never prints the key)
cd /Users/affanbaig/video-editor; out="$1"; shift
python3 -I research/deep-research-2026-11-14/yt_api.py aw-gta6-reviews "$@" > "research/aw-gta6-reviews-2026-11-21/api/$out"
