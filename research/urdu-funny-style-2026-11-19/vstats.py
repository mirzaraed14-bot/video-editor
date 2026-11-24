import sys,re,statistics as st,collections,json
vid=sys.argv[1]; dur=float(sys.argv[2])
sc=[float(m.group(1)) for m in re.finditer(r'pts_time:([\d.]+)',open(f'meas/{vid}_scene.txt').read())]
print(f'{vid}: scene hits {len(sc)} over {dur:.0f}s = {len(sc)/dur*60:.1f}/min')
bym=collections.Counter(int(t//60) for t in sc); print(' by minute',[bym[i] for i in range(int(dur//60)+1)])
iv=[b-a for a,b in zip(sc,sc[1:])]
if iv: print(f' interval median {st.median(iv):.2f}s; <0.5s {sum(1 for x in iv if x<0.5)}; >5s {sum(1 for x in iv if x>5)}')
txt=open(f'meas/{vid}_ebur_M.txt').read()
M=[(float(a),float(b)) for a,b in re.findall(r'pts_time:([\d.]+)\s*\nlavfi.r128.M=(-?[\d.inf]+)',txt) if b not in('-inf',)]
v=[b for a,b in M if b>-70]
print(f' momentary LUFS: median {st.median(v):.1f} p10 {sorted(v)[int(len(v)*.1)]:.1f} p90 {sorted(v)[int(len(v)*.9)]:.1f} max {max(v):.1f}; frac of time >-14 {sum(1 for x in v if x>-14)/len(v)*100:.1f}%')
# 1-s buckets max M
b1=collections.defaultdict(list)
for a,b in M: b1[int(a)].append(b)
sec={k:max(x) for k,x in b1.items()}
med=st.median(sec.values())
# peaks: seconds with max M > med+8, merged within 6s
cand=sorted([k for k,x in sec.items() if x>med+8],key=lambda k:-sec[k])
peaks=[]
for k in cand:
    if all(abs(k-p)>8 for p,_ in peaks): peaks.append((k,sec[k]))
print(f' median sec-max M {med:.1f}; peaks (>{med+8:.0f}):',[(f"{p//60}:{p%60:02d}",round(x,1)) for p,x in sorted(peaks)][:60])
json.dump({'peaks':sorted(peaks),'median':med},open(f'meas/{vid}_peaks.json','w'))
