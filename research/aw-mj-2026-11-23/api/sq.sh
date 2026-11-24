#!/bin/bash
# usage: sq.sh <tag> "<query>" [extra params]  -> search + videos stats, compact print
cd "X:/Claude Projects/video-editor-client/video-editor"
tag=$1; q=$2; shift 2
out=research/aw-mj-2026-11-23/api
python -I research/deep-research-2026-11-14/yt_api.py mj-short search part=snippet type=video q="$q" maxResults=25 order=relevance "$@" > $out/$tag.search.json || exit 1
ids=$(python -I -c "import json,sys;d=json.load(open('$out/$tag.search.json',encoding='utf-8'));print(','.join(i['id']['videoId'] for i in d.get('items',[])))")
python -I research/deep-research-2026-11-14/yt_api.py mj-short videos part=snippet,statistics,contentDetails id=$ids > $out/$tag.videos.json
PYTHONIOENCODING=utf-8 python -I -c "
import json
d=json.load(open('$out/$tag.videos.json',encoding='utf-8'))
rows=[(int(v['statistics'].get('viewCount',0)),v['id'],v['snippet']['publishedAt'][:10],v['contentDetails']['duration'],v['snippet']['channelTitle'][:22],v['snippet']['title'][:90]) for v in d.get('items',[])]
for r in sorted(rows,reverse=True): print('%11s %s %s %-9s %-22s %s'%('{:,}'.format(r[0]),r[1],r[2],r[3],r[4],r[5]))
"
