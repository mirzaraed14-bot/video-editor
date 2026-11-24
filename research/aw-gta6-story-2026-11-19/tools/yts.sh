#!/bin/bash
# yts.sh <label> <query> [extra name=value...]  -> search then videos stats, compact lines, saved to api/<label>.json
cd "X:/Claude Projects/video-editor-client/video-editor"
L="$1"; Q="$2"; shift 2
OUT=research/aw-gta6-story-2026-11-19/api
python -I research/deep-research-2026-11-14/yt_api.py gta6-story search part=snippet type=video q="$Q" maxResults=25 "$@" > $OUT/$L.search.json || exit 1
IDS=$(python -I -c "import json,sys;d=json.load(open(sys.argv[1],encoding='utf-8'));print(','.join(i['id']['videoId'] for i in d.get('items',[])))" $OUT/$L.search.json)
[ -z "$IDS" ] && { echo "no results"; exit 0; }
python -I research/deep-research-2026-11-14/yt_api.py gta6-story videos part=snippet,statistics,contentDetails id=$IDS > $OUT/$L.videos.json
python -I - $OUT/$L.videos.json <<'PY'
import json,sys,re
sys.stdout.reconfigure(encoding='utf-8',errors='replace')
d=json.load(open(sys.argv[1],encoding='utf-8'))
rows=[]
for v in d.get('items',[]):
    s=v['snippet'];st=v.get('statistics',{});dur=v['contentDetails']['duration']
    rows.append((int(st.get('viewCount',0)),int(st.get('likeCount',0) or 0),v['id'],s['publishedAt'][:16],dur,s['channelTitle'][:22],s['title'][:90]))
for r in sorted(rows,reverse=True): print(f'{r[0]:>11,} {r[1]:>8,}L {r[2]} {r[3]} {r[4]:>9} | {r[5]} | {r[6]}')
PY
