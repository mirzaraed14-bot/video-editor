import json,re,sys
# usage: grepw.py <clipname> <regex> [ctx_seconds]
w=json.load(open('projects/aw-mj-scan-2026-11-13/transcript/words.json',encoding='utf-8'))
clip=[c for c in w['clips'] if c['clip']==sys.argv[1]][0]
ws=clip['words']; ctx=float(sys.argv[3]) if len(sys.argv)>3 else 12
txt=[(x.get('start'),x.get('w','')) for x in ws]
pat=re.compile(sys.argv[2],re.I)
hits=[t for t,wd in txt if t is not None and pat.search(wd)]
done=-1e9
for h in hits:
    if h<done: continue
    seg=[wd for t,wd in txt if t is not None and h-ctx<=t<=h+ctx]
    print('@%.1f: %s\n'%(h,' '.join(seg)))
    done=h+ctx
