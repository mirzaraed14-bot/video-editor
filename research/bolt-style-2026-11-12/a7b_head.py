import json,numpy as np
from common import *
cuts_raw=json.load(open(OUT+"data/cuts_raw.json"))
tl=json.load(open(ROOT+"/projects/mj-son-step-outside/build/timeline.json"))
res={}
for i in IDS:
    F=json.load(open(OUT+f"data/{i}_faces.json")); rows=F['rows']; W_,H_=F['w'],F['h']
    top={}
    for r in rows:
        if r['faces']:
            f=max(r['faces'],key=lambda f:f[2]*f[3])
            top[r['n']]=(f[0]+f[2]/2,f[1]+f[3]/2,f[2],f[3],f[14])   # cx,cy,w,h,score  (540x960 px)
    g=load_gray(i); n=len(g)
    cl=[round(s['t0']*FPS) for s in tl['shots']][1:] if i=="OURS" else cuts_raw[i]['cuts']
    bounds=list(zip([0]+cl,cl+[n]))
    jc=[]
    for k in cl:
        b=max([m for m in top if m<=k-1],default=None); a=min([m for m in top if m>=k],default=None)
        if b is None or a is None or k-b>6 or a-k>6: continue
        fb,fa=top[b],top[a]
        # skip frames: use 3 frames either side measured at sample grid
        bgd=float(np.mean([np.abs(g[k-1][:, :40].astype(float)-g[k][:, :40].astype(float)).mean(),np.abs(g[k-1][:, -40:].astype(float)-g[k][:, -40:].astype(float)).mean()]))
        hr=fa[3]/fb[3]
        # same camera jump cut: face present both sides, size ratio .7-1.4, centre moved < 25% of frame width, border bg similar
        same= 0.7<hr<1.4 and abs(fa[0]-fb[0])<0.25*W_ and bgd<30
        jc.append(dict(t=round(k/FPS,3),dx_px1080=round(float((fa[0]-fb[0])*2),1),dy_px1080=round(float((fa[1]-fb[1])*2),1),h_before=round(float(fb[3]*2),1),h_after=round(float(fa[3]*2),1),h_ratio=round(float(hr),3),bg_diff=round(bgd,1),same_cam=bool(same)))
    # within-shot drift
    sh=[]
    for a,b in bounds:
        pts=[(m,top[m]) for m in sorted(top) if a+6<=m<=b-4]
        if len(pts)<6 or (b-a)/FPS<0.8: continue
        t=np.array([m/FPS for m,_ in pts]); cx=np.array([p[0] for _,p in pts])*2; cy=np.array([p[1] for _,p in pts])*2; hh=np.array([p[3] for _,p in pts])*2
        slope=np.polyfit(t,np.log(hh),1)[0]
        sh.append(dict(t0=round(a/FPS,2),t1=round(b/FPS,2),n=len(pts),h_px=round(float(np.median(hh)),0),h_pct_frame=round(float(np.median(hh)/1920*100),1),cx_px=round(float(np.median(cx)),0),cy_pct=round(float(np.median(cy)/1920*100),1),
            x_range=round(float(cx.max()-cx.min()),1),y_range=round(float(cy.max()-cy.min()),1),x_std=round(float(cx.std()),1),y_std=round(float(cy.std()),1),face_scale_rate_pct_s=round(float((np.exp(slope)-1)*100),2)))
    allh=[v[3]*2/1920*100 for v in top.values()]; allcy=[v[1]*2/1920*100 for v in top.values()]
    res[i]=dict(face_frames_share=round(len(top)/len(rows),2),face_h_pct_med=round(float(np.median(allh)),1) if allh else None,face_cy_pct_med=round(float(np.median(allcy)),1) if allcy else None,
        face_cx_pct_med=round(float(np.median([v[0]*2/1080*100 for v in top.values()])),1) if top else None,cuts_with_face_both=jc,shots=sh)
    print(i,"face share",res[i]['face_frames_share'],"h%",res[i]['face_h_pct_med'],"cy%",res[i]['face_cy_pct_med'],"cuts w/ face both sides",len(jc),"same-cam",sum(j['same_cam'] for j in jc))
    for j in jc:
        if j['same_cam']: print("   JUMP",j)
    for s in sh[:30]:
        if i=="OURS": print("   shot",s)
json.dump(res,open(OUT+"data/head.json","w"),indent=1)
