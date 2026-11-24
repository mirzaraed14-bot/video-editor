import json,sys,statistics as st,collections
f=sys.argv[1]
d=json.load(open(f,encoding='utf-8'))
V=d['video'][0]; dur=V[-1]['end']-V[0]['start']
L=[r['end']-r['start'] for r in V]
def pct(a,p):
    a=sorted(a); 
    if not a: return None
    i=(len(a)-1)*p; lo=int(i); hi=min(lo+1,len(a)-1); return a[lo]+(a[hi]-a[lo])*(i-lo)
tc=lambda t:f"{int(t//60)}:{t%60:05.2f}"
print(f"{f}: runtime {dur:.2f}s ({tc(dur)}), V1 clips {len(V)}, cuts/min {(len(V)-1)/dur*60:.1f}")
print(f"clip len median {st.median(L):.2f} mean {st.mean(L):.2f} p25 {pct(L,.25):.2f} p75 {pct(L,.75):.2f} min {min(L):.2f} max {max(L):.2f}; <1s {sum(1 for x in L if x<1)}; <0.6s {sum(1 for x in L if x<0.6)}; >5s {sum(1 for x in L if x>5)}")
# per-minute cut counts
bym=collections.Counter(int(r['start']//60) for r in V)
print('cuts by minute:',[bym[i] for i in range(int(dur//60)+1)])
print('first 60s edit points:',sum(1 for r in V if 0<r['start']<60))
# source span / keep ratio
media=collections.Counter(r['name'] for r in V)
print('media',dict(media))
for nm in media:
    rs=[r for r in V if r['name']==nm]
    print(' ',nm,'source in-range',round(min(r['in'] for r in rs),1),'-',round(max(r['out'] for r in rs),1),'kept',round(sum(r['end']-r['start'] for r in rs),1),'s')
# source jump (how much removed between consecutive clips from same media)
gaps=[]
for a,b in zip(V,V[1:]):
    if a['name']==b['name']:
        gaps.append(b['in']-a['out'])
fwd=[g for g in gaps if g>0.0001]
print(f"consecutive same-source: continuous (gap<0.05s) {sum(1 for g in gaps if abs(g)<0.05)} / {len(gaps)}; jumps fwd {len(fwd)} median skipped {st.median(fwd) if fwd else None:.2f}s; backward {sum(1 for g in gaps if g<-0.05)}")
# zooms
Z=[]
for r in V:
    for c in r.get('fx',[]):
        if c['display']=='Motion':
            p=c['params']; Z.append((r,p))
print('Motion clips (static scale/pos):',len(Z))
if Z:
    sc=[p.get('Scale') for r,p in Z if isinstance(p.get('Scale'),(int,float))]
    ln=[r['end']-r['start'] for r,p in Z]
    print(f" zooms/min {len(Z)/dur*60:.1f}; scale median {st.median(sc):.0f} p25 {pct(sc,.25):.0f} p75 {pct(sc,.75):.0f} min {min(sc):.0f} max {max(sc):.0f}")
    print(f" hold median {st.median(ln):.2f}s p25 {pct(ln,.25):.2f} p75 {pct(ln,.75):.2f} min {min(ln):.2f} max {max(ln):.2f}; total zoomed {sum(ln):.1f}s = {sum(ln)/dur*100:.1f}% of runtime")
    print(' scale bands: <=125:',sum(1 for s in sc if s<=125),'126-150:',sum(1 for s in sc if 126<=s<=150),'151-200:',sum(1 for s in sc if 151<=s<=200),'>200:',sum(1 for s in sc if s>200))
    print(' sorted scales',sorted(int(s) for s in sc))
    # positions
    pos=[p.get('Position') for r,p in Z]
    xs=[];ys=[]
    for q in pos:
        if isinstance(q,str):
            x,y=q.split(':'); xs.append(float(x)); ys.append(float(y))
    print(f" pos x median {st.median(xs):.2f} y median {st.median(ys):.2f}; x range {min(xs):.2f}-{max(xs):.2f} y range {min(ys):.2f}-{max(ys):.2f}")
    # zoom adjacency: how many zoomed clips are directly preceded by non-zoom
    isz=[any(c['display']=='Motion' for c in r.get('fx',[])) for r in V]
    runs=0; cur=0; runlens=[]
    for z in isz:
        if z: cur+=1
        else:
            if cur: runlens.append(cur)
            cur=0
    if cur: runlens.append(cur)
    print(' consecutive zoom runs (lengths):',collections.Counter(runlens))
    # what precedes: gaps (clips between zooms)
    idx=[i for i,z in enumerate(isz) if z]
    gp=[b-a-1 for a,b in zip(idx,idx[1:])]
    print(' clips between zooms median',st.median(gp),'dist',collections.Counter(gp).most_common(8))
    print(' zoom times:',[tc(r['start']) for r,p in Z][:80])
# keyframed Transform
for r in V:
    for c in r.get('fx',[]):
        if c['display']=='Transform':
            p=c['params']
            print('Transform clip',tc(r['start']),tc(r['end']),'scale kf',p['Scale']['kf'],'pos kf',[(t,v) for t,v in p['Position']['kf']])
# non-main media on V1
for r in V:
    if 'TV colour' in r['name']: print('colourbars V1',tc(r['start']),round(r['end']-r['start'],3),'in',r['in'],'out',r['out'])
for ti,tr in enumerate(d['audio']):
    for r in tr:
        if 'Don' not in r['name'] and 'Escape' not in r['name'] and 'Backrooms 2nd' not in r['name']:
            print('audio extra A%d'%(ti+1),r['name'][:50],tc(r['start']),round(r['end']-r['start'],3),'gain',r.get('gain_db'),'speed',r.get('speed'),'in',r['in'])
# audio gains
for ti,tr in enumerate(d['audio']):
    g=[r.get('gain_db') for r in tr if r.get('gain_db') is not None]
    if g: print(f'A{ti+1} gain_db n={len(g)} values',collections.Counter(round(x,1) for x in g).most_common(12))
