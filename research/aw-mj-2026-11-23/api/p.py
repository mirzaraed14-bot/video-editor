import json,sys
for tag in sys.argv[1:]:
    d=json.load(open(tag+'.videos.json',encoding='utf-8'))
    print('==',tag)
    rows=[(int(v['statistics'].get('viewCount',0)),int(v['statistics'].get('likeCount',0) or 0),v['id'],v['snippet']['publishedAt'][:10],v['contentDetails']['duration'],v['snippet']['channelTitle'][:20],v['snippet']['title'][:95]) for v in d.get('items',[])]
    for r in sorted(rows,reverse=True)[:22]:
        print(('%11s %8s %s %s %-8s %-20s %s'%('{:,}'.format(r[0]),'{:,}'.format(r[1]),*r[2:])).encode('ascii','replace').decode())
