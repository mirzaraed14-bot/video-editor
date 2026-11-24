import sys,json,glob,re,os,time; sys.stdout.reconfigure(encoding="utf-8", errors="replace")
d=os.path.dirname(os.path.abspath(__file__))
pat=re.compile(sys.argv[1],re.I); n=int(sys.argv[2]) if len(sys.argv)>2 else 40
L=[]
for f in glob.glob(d+'/r-*.json'):
    ch=os.path.basename(f)[2:-5]
    try: j=json.load(open(f,encoding='utf-8'))
    except Exception: continue
    for e in j.get('entries',[]) or []:
        if pat.search(e.get('title') or ''): L.append((e.get('view_count') or 0,ch,e))
L.sort(key=lambda x:-x[0])
for v,ch,e in L[:n]:
    print(f"{v:>8} {ch:14} {time.strftime('%m-%d %H:%M',time.localtime(e['timestamp']))} {e.get('duration',0):4.0f}s | {e['title'][:72]} | {e['url']}")
