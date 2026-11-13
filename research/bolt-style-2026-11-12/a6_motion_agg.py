import json,numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import *
agg={}
for i in IDS:
    M=[s for s in json.load(open(OUT+f"data/{i}_motion.json")) if not s.get('short')]
    for s in M:
        s['clean']=bool(s['inlier']>=0.95 and abs(s['rot_deg'])<0.7 and s['dur']>=0.6)
    dirs=[s['dir'] for s in M]
    same=sum(1 for a,b in zip(dirs,dirs[1:]) if a==b and a!='static'); alt=sum(1 for a,b in zip(dirs,dirs[1:]) if a!=b and 'static' not in (a,b))
    def stats(S,key): 
        v=[x[key] for x in S]; return (float(np.median(v)),float(np.percentile(v,25)),float(np.percentile(v,75))) if v else None
    clean=[s for s in M if s['clean']]; cz=[s for s in clean if s['dir']!='static']
    prof={'accel':0,'linear':0,'decel':0}
    for s in cz:
        if abs(s['total_scale_pct'])<2 or s['dur']<1.0: continue
        a,c=abs(s['r_first']),abs(s['r_last'])
        r=c/max(a,0.05); prof['accel' if r>1.4 else 'decel' if r<0.7 else 'linear']+=1
    agg[i]=dict(n_shots=len(M),n_static=sum(s['dir']=='static' for s in M),n_in=sum(s['dir']=='in' for s in M),n_out=sum(s['dir']=='out' for s in M),
        n_clean=len(clean),clean_in=sum(s['dir']=='in' for s in cz),clean_out=sum(s['dir']=='out' for s in cz),
        same_dir_pairs=same,alt_dir_pairs=alt,
        rate_all_abs_med=float(np.median([abs(s['mean_rate_pct_s']) for s in M if s['dir']!='static'] or [0])),
        rate_clean_med=float(np.median([s['mean_rate_pct_s'] for s in cz] or [0])),rate_clean_iqr=[float(np.percentile([s['mean_rate_pct_s'] for s in cz] or [0],25)),float(np.percentile([s['mean_rate_pct_s'] for s in cz] or [0],75))],
        panspeed_clean_med=float(np.median([s['pan_px_s'] for s in clean] or [0])),panspeed_all_med=float(np.median([s['pan_px_s'] for s in M])),
        rot_abs_clean_med=float(np.median([abs(s['rot_deg']) for s in clean] or [0])),profile=prof,
        thirds_clean_med=[float(np.median([abs(s[k]) for s in cz] or [0])) for k in('r_first','r_mid','r_last')],
        total_scale_clean_med=float(np.median([s['total_scale_pct'] for s in cz] or [0])),
        dir_seq=''.join({'in':'+','out':'-','static':'0'}[d] for d in dirs))
    # plot
    fig,ax=plt.subplots(3,1,figsize=(14,9)); 
    for s in M:
        t=np.array(s['curve']['t'])+s['t0']+3/FPS; sc=(np.exp(np.array(s['curve']['logs']))-1)*100
        c='tab:green' if s['clean'] else 'tab:gray'
        ax[0].plot(t,sc,color=c,lw=1.6); ax[0].axvline(s['t0'],color='k',lw=.3)
        ax[1].plot(t,s['curve']['px'],color='tab:blue',lw=1); ax[1].plot(t,s['curve']['py'],color='tab:red',lw=1)
        ax[2].bar(s['t0']+s['dur']/2,s['mean_rate_pct_s'],width=max(s['dur']*.8,.15),color=c)
    ax[0].set_ylabel("cum. scale % (per shot)"); ax[1].set_ylabel("pan px@1080 (blue x, red y)"); ax[2].set_ylabel("mean rate %/s")
    ax[0].set_title(f"{i}: green = clean digital-type drift (inliers>=.95, |rot|<.7), grey = footage motion / unreliable"); ax[1].set_ylim(-600,600)
    plt.tight_layout(); plt.savefig(OUT+f"{i}_motion.png",dpi=70); plt.close()
    json.dump(M,open(OUT+f"data/{i}_motion_flagged.json","w"))
json.dump(agg,open(OUT+"data/motion_agg.json","w"),indent=1)
for i,a in agg.items(): print(i,{k:(round(v,2) if isinstance(v,float) else v) for k,v in a.items() if k not in('rate_clean_iqr',)})
