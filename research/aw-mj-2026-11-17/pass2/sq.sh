#!/usr/bin/env bash
# sq.sh <tag> <query> [extra params...]: search (100 u) + videos (1 u), print top 15 by views
set -e
cd "X:/Claude Projects/video-editor-client/video-editor/research/aw-mj-2026-11-17/pass2"
mkdir -p api
tag=$1; q=$2; shift 2
python -I ../../deep-research-2026-11-14/yt_api.py mj-beats search type=video q="$q" order=viewCount maxResults=50 part=snippet "$@" > api/$tag.json
ids=$(python -I -c "import json;d=json.load(open('api/$tag.json',encoding='utf-8'));print(','.join(i['id']['videoId'] for i in d['items']))")
python -I ../../deep-research-2026-11-14/yt_api.py mj-beats videos part=snippet,statistics,contentDetails id=$ids > api/${tag}_stats.json
echo "== $tag: $q $*"
python -I ../show.py api/${tag}_stats.json | head -15
