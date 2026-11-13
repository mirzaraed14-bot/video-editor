import json,numpy as np,sys
from common import *
cuts_raw=json.load(open(OUT+"data/cuts_raw.json"))
tl=json.load(open(ROOT+"/projects/mj-son-step-outside/build/timeline.json"))
def cutlist(i):
    if i=="OURS": return [round(s['t0']*FPS) for s in tl['shots']][1:]
    return cuts_raw[i]['cuts']
res={}
for i in IDS:
    s=json.load(open(OUT+f"data/{i}_framestats.json")); n=len(s)
    L=np.array([x['luma'] for x in s]); LP=np.array([x['lap'] for x in s]); D=np.array([x['diff'] for x in s])
    rgb=np.array([[x['b'],x['gr'],x['r']] for x in s])
    out=[]
    for k in cutlist(i):
        if k<12 or k>n-12: continue
        Lb=np.median(L[k-12:k-5]); La=np.median(L[k+6:k+13]); ref=min(Lb,La)
        win=L[k-8:k+9]; Lmin=win.min(); Lmax=win.max()
        depth=ref-Lmin; flash=max(Lb,La)-0 and Lmax-max(Lb,La)
        thr=ref-0.4*depth if depth>12 else -1
        dip_frames=int((L[k-20:k+21]<thr).sum()) if depth>12 else 0
        # dip frames only contiguous around min
        lb=np.median(LP[k-12:k-5]); la=np.median(LP[k+6:k+13]); lapmin=LP[k-8:k+9].min()
        lapratio=lapmin/max(1e-6,min(lb,la))
        base=max(2.0,np.median(D[k-30:k+30]))
        act=[j for j in range(k-6,k+7) if j!=k and D[j]>max(5,3*base)]
        dcol=np.abs(rgb[k-8:k+9]-np.median(np.r_[rgb[k-12:k-5],rgb[k+6:k+13]],axis=0)).max()
        # wide-window dip (smooth fade through dark)
        refw=np.median(np.r_[L[k-45:k-28],L[k+28:k+45]]); w=L[k-28:k+29]; wmin=w.min()
        dip_ratio=float(wmin/max(refw,1e-6)); dipdur=int((w<0.9*refw).sum()) if dip_ratio<0.8 else 0
        pre_blur=float(LP[k-3:k].mean()/max(1e-6,np.median(LP[k-40:k-20]))); post_blur=float(LP[k+1:k+4].mean()/max(1e-6,np.median(LP[k+25:k+45])))
        swell=float(L[k-28:k+29].max()-refw)
        kind="hard"
        if D[k]<8 and dip_ratio<0.6: kind="smooth dip to dark"
        elif post_blur<0.45 and D[k]>=8: kind="hard cut + blur decay"
        elif depth>25: kind="dip"
        elif flash>25: kind="flash"
        elif lapratio<0.5 and len(act)>=3: kind="blur"
        elif len(act)>=3: kind="whip/slide"
        out.append(dict(frame=k,t=round(k/FPS,3),Lb=round(float(Lb),1),La=round(float(La),1),dip_depth=round(float(depth),1),dip_frames=dip_frames,flash_height=round(float(flash),1),lap_ratio=round(float(lapratio),2),n_active_nbr=len(act),color_dev=round(float(dcol),1),kind=kind,dip_ratio=round(dip_ratio,2),dip_dur_frames=dipdur,pre_blur=round(pre_blur,2),post_blur=round(post_blur,2),swell=round(swell,1),diff_spike=round(float(D[k]),1)))
    res[i]=out
    kinds={}
    for o in out: kinds[o['kind']]=kinds.get(o['kind'],0)+1
    print(i,len(out),kinds)
json.dump(res,open(OUT+"data/transitions.json","w"),indent=1)
for o in res['OURS']: print(o['t'],o['kind'],o['dip_ratio'],o['dip_dur_frames'],o['post_blur'],o['swell'],o['flash_height'])
