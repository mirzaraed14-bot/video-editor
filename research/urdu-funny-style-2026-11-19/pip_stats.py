import json,numpy as np,sys,collections,statistics as st
label=sys.argv[1]; splits=[float(s) for s in sys.argv[2:]]  # segment boundaries in seconds
o=json.load(open(f'meas/{label}_pip.json'))
W,H=480,270
t=np.array([a[0] for a in o]); x=np.array([a[1] for a in o]); y=np.array([a[3] for a in o]); xs=np.array([a[2] for a in o]); ys=np.array([a[4] for a in o])
w=(W-x)/W; h=y/H; ok=(xs>12)&(ys>6)
bounds=[0]+splits+[t[-1]+1]
tc=lambda s:f"{int(s//60)}:{s%60:04.1f}"
for a,b in zip(bounds,bounds[1:]):
    m=(t>=a)&(t<b)&ok
    if m.sum()<10: continue
    base=np.median(w[m]); baseh=np.median(h[m])
    print(f'segment {tc(a)}-{tc(b)}: PiP baseline width {base:.3f} height {baseh:.3f} (n={m.sum()})')
    # enlarged intervals: w > base+0.07 for >=3 frames (0.6 s at 5fps)
    big=(w>base+0.07)&ok&(t>=a)&(t<b)
    iv=[];s=None
    for i in range(len(t)):
        if big[i] and s is None: s=i
        if (not big[i]) and s is not None:
            if i-s>=2: iv.append((t[s],t[i-1]+0.2,float(w[s:i].max())))
            s=None
    print(f'  enlarged intervals: {len(iv)}; per min {len(iv)/((min(b,t[-1])-a)/60):.1f}')
    if iv:
        d=[e-s for s,e,_ in iv]; mx=[m for *_,m in iv]
        print(f'  duration median {st.median(d):.1f}s range {min(d):.1f}-{max(d):.1f}; peak width median {st.median(mx):.2f} max {max(mx):.2f} (x baseline {st.median(mx)/base:.2f})')
        print('  at',[tc(s) for s,e,_ in iv][:40])
