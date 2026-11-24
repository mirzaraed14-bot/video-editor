# vt.py <json...>: one line per video (id, channel, title, date, duration, views, likes, comments, age rating)
import json,sys
for f in sys.argv[1:]:
    d=json.load(open(f))
    for v in d.get('items',[]):
        s=v['snippet'];st=v.get('statistics',{});c=v.get('contentDetails',{})
        vid=v['id'] if isinstance(v['id'],str) else v['id'].get('videoId')
        print(vid,s['channelTitle'][:20],'|',s['title'][:75],'|',s['publishedAt'][:16],c.get('duration',''),'v',st.get('viewCount'),'l',st.get('likeCount'),'c',st.get('commentCount'),'AGE' if c.get('contentRating',{}).get('ytRating') else '')
