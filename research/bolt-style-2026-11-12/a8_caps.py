import sys,json,numpy as np,cv2
from common import *
i=sys.argv[1]
g=load_gray(i); n=len(g)
BY0,BY1=(1005,1115) if i=="OURS" else (915,1000)     # full-res band rows (Bolt caption y 941-977 measured above)
r0,r1=BY0//4,BY1//4
band=np.asarray(g[:,r0:r1,:]); mask=band>=225; cnt=mask.reshape(n,-1).sum(1)
ev=[]
for k in range(2,n-14):
    a,b=mask[k-1],mask[k]; uni=(a|b).sum()
    if cnt[k]>=25 and uni and ((a&b).sum()/uni<0.45 or cnt[k-1]<10):
        if ev and k-ev[-1]<9: continue
        ev.append(k)
def text_mask(img):
    mn=img.min(2); white=(mn>=225)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    colr=(hsv[...,1]>150)&(hsv[...,2]>200)
    return white,colr,hsv
nxt=ev[1:]+[n]
settled=[min(e+14,x-2) for e,x in zip(ev,nxt)]
G=grab(i,settled,1080,1920)
rows=[]
for e,s in zip(ev,settled):
    img=G.get(s)
    if img is None: continue
    crop=img[BY0:BY1]; white,colr,hsv=text_mask(crop); tm=white|colr
    rp=tm.sum(1); ys=np.where(rp>5)[0]
    if len(ys)<8: continue
    groups=[];st=ys[0];pv=ys[0]
    for y in ys[1:]:
        if y-pv>10: groups.append((st,pv)); st=y
        pv=y
    groups.append((st,pv)); groups=[q for q in groups if q[1]-q[0]>=16]
    if not groups: continue
    q=max(groups,key=lambda q:rp[q[0]:q[1]+1].sum()); sub=tm[q[0]:q[1]+1]
    xs=np.where(sub.sum(0)>1)[0]
    if len(xs)<30: continue
    h=q[1]-q[0]+1; wd=1;pv=xs[0]
    for x in xs[1:]:
        if x-pv>0.33*h: wd+=1
        pv=x
    cc=int(colr[q[0]:q[1]+1].sum()); 
    rows.append(dict(ev=e,t=round(e/FPS,3),y_top=int(q[0]+BY0),y_bot=int(q[1]+BY0),height=int(h),x_l=int(xs[0]),x_r=int(xs[-1]),width=int(xs[-1]-xs[0]),words=wd,lines=len(groups),colored=bool(cc>40),colpx=cc,
      hue=(float(np.median(hsv[q[0]:q[1]+1][...,0][colr[q[0]:q[1]+1]])*2) if cc>40 else None),white_px=int(white[q[0]:q[1]+1].sum()),
      cx=float((xs[0]+xs[-1])/2)))
json.dump(rows,open(OUT+f"data/{i}_caps_events.json","w"))
print(i,"events",len(ev),"measured",len(rows),"y_top",np.median([r['y_top'] for r in rows]),"y_bot",np.median([r['y_bot'] for r in rows]),"h",np.median([r['height'] for r in rows]),"words",np.median([r['words'] for r in rows]),"colored",np.mean([r['colored'] for r in rows]).round(2),"cx",np.median([r['cx'] for r in rows]),"gap",np.median(np.diff([r['t'] for r in rows])).round(2))
# entrance sheets: choose 4 events spread
pick=[rows[int(len(rows)*q)] for q in (0.15,0.4,0.65,0.85)] if len(rows)>=4 else rows
fr=[];
for r in pick: fr+=list(range(r['ev']-1,r['ev']+7))
G2=grab(i,fr,1080,1920)
ims=[];labs=[];anim=[]
for r in pick:
    y0=max(0,r['y_top']-45); y1=r['y_bot']+45
    s_img=G.get(min(r['ev']+14,len(g)-2)); 
    xl=max(0,int(r['x_l'])-30); xr=min(1080,int(r['x_r'])+30)
    ref=None
    seq=[]
    for f in range(r['ev']-1,r['ev']+7):
        im=G2.get(f)
        if im is None: continue
        ims.append(im[y0:y1,xl:xr]); labs.append(f"t={r['t']:.2f} f{f-r['ev']:+d}")
        white=(im[y0:y1,xl:xr].min(2)>=225)
        ys,xs2=np.where(white)
        seq.append(dict(f=f-r['ev'],px=int(white.sum()),cy=float(ys.mean()+y0) if len(ys) else None,x_l=int(xs2.min()+xl) if len(xs2) else None,x_r=int(xs2.max()+xl) if len(xs2) else None,y_top=int(ys.min()+y0) if len(ys) else None,y_bot=int(ys.max()+y0) if len(ys) else None,lum=float(im[y0:y1,xl:xr].mean())))
    anim.append(dict(event=r,seq=seq))
json.dump(anim,open(OUT+f"data/{i}_caps_anim.json","w"))
w=max(im.shape[1] for im in ims); h=max(im.shape[0] for im in ims)
ims2=[cv2.copyMakeBorder(im,0,h-im.shape[0],0,w-im.shape[1],cv2.BORDER_CONSTANT) for im in ims]
sc=min(1.0,330/w); S=tile(ims2,labs,8,int(w*sc),int(h*sc),lab=14); S.save(OUT+f"{i}_caps.jpg",quality=85); print(S.size)
