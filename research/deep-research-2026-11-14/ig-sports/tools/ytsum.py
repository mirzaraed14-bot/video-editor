# ytsum.py <json file> [search|videos|channels|playlist]: compact one-line summaries of a yt_api.py answer
import sys as _s; _s.stdout.reconfigure(encoding="utf-8")
import json, sys, re
d = json.load(open(sys.argv[1], encoding='utf-8')); kind = sys.argv[2] if len(sys.argv) > 2 else 'search'
def dur(s):
    m = re.match(r'P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?', s or '')
    if not m: return 0
    d_, h, mi, se = (int(x) if x else 0 for x in m.groups()); return d_*86400+h*3600+mi*60+se
for it in d.get('items', []):
    if kind == 'search':
        print(it['id'].get('videoId'), '|', it['snippet']['channelId'], '|', it['snippet']['channelTitle'][:28], '|', it['snippet']['publishedAt'][:10], '|', it['snippet']['title'][:80])
    elif kind == 'videos':
        st = it.get('statistics', {}); sn = it['snippet']
        print(it['id'], '|', st.get('viewCount'), '|', st.get('likeCount'), '|', st.get('commentCount'), '|', dur(it.get('contentDetails', {}).get('duration')), 's |', sn['publishedAt'][:10], '|', sn['channelTitle'][:24], '|', sn['title'][:70])
    elif kind == 'channels':
        st = it.get('statistics', {}); print(it['id'], '|', it['snippet']['title'][:30], '|', st.get('subscriberCount'), 'subs |', st.get('videoCount'), 'videos')
    elif kind == 'playlist':
        print(it['contentDetails']['videoId'], it['contentDetails'].get('videoPublishedAt', '')[:10])
