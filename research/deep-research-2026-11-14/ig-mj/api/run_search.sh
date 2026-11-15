#!/usr/bin/env bash
# run_search.sh <tag> <query> [extra name=value...] : one API search + one videos lookup, compact table out
set -u
cd "X:/Claude Projects/video-editor-client/video-editor"
tag=$1; q=$2; shift 2
D=research/deep-research-2026-11-14/ig-mj/api
python -I research/deep-research-2026-11-14/yt_api.py ig-mj search part=snippet type=video q="$q" maxResults=50 "$@" > $D/s_$tag.json || exit $?
ids=$(python -c "import json;d=json.load(open('$D/s_$tag.json',encoding='utf-8'));print(','.join(i['id']['videoId'] for i in d.get('items',[]) if i.get('id',{}).get('videoId')))")
[ -z "$ids" ] && { echo "no ids"; exit 0; }
python -I research/deep-research-2026-11-14/yt_api.py ig-mj videos part=snippet,statistics,contentDetails id=$ids > $D/v_$tag.json || exit $?
python research/deep-research-2026-11-14/ig-mj/api/show.py "$D/v_$tag.json"; exit 0
PY_UNUSED=1
import json,sys,re
d=json.load(open(sys.argv[1],encoding='utf-8'))
rows=[]
for it in d.get('items',[]):
    s=it['snippet']; st=it.get('statistics',{}); dur=it.get('contentDetails',{}).get('duration','')
    m=re.match(r'PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?',dur); secs=(int(m.group(1) or 0)*3600+int(m.group(2) or 0)*60+int(m.group(3) or 0)) if m else 0
    rows.append((int(st.get('viewCount',0)), it['id'], secs, s.get('publishedAt','')[:10], s.get('channelTitle','')[:20], s.get('title','')[:75]))
rows.sort(reverse=True)
for r in rows[:15]: print(f"{r[0]:>10,} {r[1]} {r[2]:>4}s {r[3]} {r[4]:<20} | {r[5]}")
print('n=',len(rows))
PY
