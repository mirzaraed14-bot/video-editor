import json,numpy as np,cv2
from common import *
tl=json.load(open(ROOT+"/projects/mj-son-step-outside/build/timeline.json"))
tot=0;lb=0
for s in tl['shots']:
    d=s['t1']-s['t0']; tot+=d
    if s.get('kind')=='overlay' and not s.get('full'): lb+=d
print("ours shots keys:",[(s['id'],s['kind'],s.get('full'),s.get('lb')) for s in tl['shots']])
out={}
for i in IDS[:6]:
    J=json.load(open(BOLT+i+"_frames.json"))['rows']
    bh=np.array([r['band'][1]-r['band'][0] for r in J]); boxed=bh<0.8
    tops=[r['band'][0] for r,b in zip(J,boxed) if b]; bots=[r['band'][1] for r,b in zip(J,boxed) if b]
    out[i]=dict(boxed_share=round(float(boxed.mean()),2),top_med=round(float(np.median(tops)),3) if tops else None,bot_med=round(float(np.median(bots)),3) if bots else None)
    # twin vs box sharpness on up to 6 boxed frames
    fr=[int(r['t']*60) for r,b in zip(J,boxed) if b][::max(1,len([1 for b in boxed if b])//6)][:6]
    if fr:
        G=grab(i,fr,1080,1920); lt=[];lp=[];lr=[];ll=[]
        for f,im in G.items():
            g=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY).astype(np.float32)
            lt.append(cv2.Laplacian(g[20:250],cv2.CV_32F).var()); lp.append(cv2.Laplacian(g[400:1500],cv2.CV_32F).var())
            lr.append(g[20:250].mean()/max(1,g[400:1500].mean()))
            # logo: brightest blob near y 1450-1560 centre
            seg=g[1380:1600,440:640]; ll.append(float((seg>235).sum()))
        out[i].update(twin_lap_var=round(float(np.median(lt)),1),pic_lap_var=round(float(np.median(lp)),1),twin_over_pic_luma=round(float(np.median(lr)),2),logo_white_px_1380_1600=round(float(np.median(ll)),0))
    print(i,out[i])
out['OURS']=dict(letterbox_shot_share=round(lb/tot,2),band=tl['letterbox']['band'],twin_scale=tl['letterbox']['twin_scale'],twin_opacity=tl['letterbox']['twin_opacity'])
print(out['OURS'])
json.dump(out,open(OUT+"data/layout.json","w"),indent=1)
