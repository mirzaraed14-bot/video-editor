import json,numpy as np,cv2,sys
from common import *
cuts_raw=json.load(open(OUT+"data/cuts_raw.json"))
tl=json.load(open(ROOT+"/projects/mj-son-step-outside/build/timeline.json"))
def shot_bounds(i,n):
    if i=="OURS":
        c=[round(s['t0']*FPS) for s in tl['shots']][1:]
    else: c=cuts_raw[i]['cuts']
    return list(zip([0]+c, c+[n]))
mask=np.zeros((H,W),np.uint8)
mask[int(H*.15):int(H*.40)]=255; mask[int(H*.62):int(H*.85)]=255
ctr=np.array([W/2,H/2])
def run(i):
    g=load_gray(i); n=len(g); out=[]
    for si,(a,b) in enumerate(shot_bounds(i,n)):
        a2=a+3  # skip transition frames
        if b-a2<6: out.append(dict(shot=si,f0=a,f1=b,short=True)); continue
        M=np.eye(3); logs=[0.0]; px=[0.0]; py=[0.0]; rot=[0.0]; inl=[]
        for k in range(a2+1,b):
            p0=cv2.goodFeaturesToTrack(g[k-1],300,0.01,5,mask=mask)
            if p0 is None or len(p0)<8:
                logs.append(logs[-1]);px.append(px[-1]);py.append(py[-1]);rot.append(rot[-1]);inl.append(0);continue
            p1,st,_=cv2.calcOpticalFlowPyrLK(np.ascontiguousarray(g[k-1]),np.ascontiguousarray(g[k]),p0,None,winSize=(21,21),maxLevel=3)
            ok=st.ravel()==1
            if ok.sum()<8:
                logs.append(logs[-1]);px.append(px[-1]);py.append(py[-1]);rot.append(rot[-1]);inl.append(0);continue
            A,inm=cv2.estimateAffinePartial2D(p0[ok],p1[ok],method=cv2.RANSAC,ransacReprojThreshold=1.2)
            if A is None: A=np.array([[1,0,0],[0,1,0]],float); inm=np.zeros((ok.sum(),1))
            inl.append(float(inm.mean()))
            S=np.vstack([A,[0,0,1]]); M=S@M
            s=np.hypot(M[0,0],M[1,0]); r=np.degrees(np.arctan2(M[1,0],M[0,0]))
            c2=(M@np.r_[ctr,1])[:2]-ctr
            logs.append(float(np.log(s))); px.append(float(c2[0])); py.append(float(c2[1])); rot.append(float(r))
        t=np.arange(len(logs))/FPS
        L=np.array(logs); T=t[-1]
        tot=np.exp(L[-1])-1
        # thirds
        th=[np.exp(L[int(len(L)*q)])/1 for q in (0,1/3,2/3)]
        def rate(lo,hi):
            lo=int(len(L)*lo); hi=max(lo+1,min(len(L)-1,int(len(L)*hi)))
            return float((np.exp((L[hi]-L[lo])/((hi-lo)/FPS))-1)*100)
        r1,r2,r3=rate(0,1/3),rate(1/3,2/3),rate(2/3,1)
        lin=np.polyfit(t,L,1); res=L-np.polyval(lin,t); r2lin=1-res.var()/max(L.var(),1e-12)
        pan=np.hypot(px[-1],py[-1])*4
        static=abs(tot)<0.015 and pan<10
        out.append(dict(shot=si,f0=a,f1=b,t0=a/FPS,t1=b/FPS,dur=(b-a)/FPS,total_scale_pct=float(tot*100),mean_rate_pct_s=float((np.exp(lin[0])-1)*100),
            r_first=r1,r_mid=r2,r_last=r3,lin_r2=float(r2lin),panx_px1080=float(px[-1]*4),pany_px1080=float(py[-1]*4),pan_px_s=float(pan/T),
            rot_deg=float(rot[-1]),inlier=float(np.mean(inl)) if inl else 0,static=bool(static),
            dir=("static" if static else ("in" if tot>0 else "out")),
            curve=dict(t=[round(x,4) for x in t],logs=[round(x,5) for x in logs],px=[round(x*4,2) for x in px],py=[round(x*4,2) for x in py])))
    return out
if __name__=="__main__":
    i=sys.argv[1]; r=run(i); json.dump(r,open(OUT+f"data/{i}_motion.json","w"))
    print(i,len(r))
    for s in r:
        if s.get('short'): print("  short",s['f0']);continue
        print(f"  {s['t0']:6.2f}-{s['t1']:6.2f} {s['dir']:6s} tot{s['total_scale_pct']:7.2f}% rate{s['mean_rate_pct_s']:6.2f}%/s  thirds {s['r_first']:.1f}/{s['r_mid']:.1f}/{s['r_last']:.1f} pan {s['panx_px1080']:.0f},{s['pany_px1080']:.0f} rot{s['rot_deg']:.2f} inl{s['inlier']:.2f}")
