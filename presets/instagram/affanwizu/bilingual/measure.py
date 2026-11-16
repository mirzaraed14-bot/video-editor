"""Ink boxes of both lines for every rendered cue: Urdu = ink above the gap row, Roman = below; reports the tightest gap and the widest line."""
import json, sys, numpy as np
from PIL import Image
m=json.load(open(sys.argv[1]+'/cues.json',encoding='utf-8')); P=m['params']; Y0=P['bandY']
split=P['urBase']+ (P['roBase']-P['urBase'])*0.5 - Y0   # rough row between the baselines
res=[]
for c in m['cues']:
    a=np.array(Image.open(c['file']))[...,3]>200
    # Roman ink: rows below the Roman cap line region; Urdu: rows above Roman cap top
    ro_cap=P['roBase']-Y0-int(P['roSize']*0.75)
    ro=a[ro_cap:]; ur=a.copy(); 
    # columns of the roman line's own extent
    r_rows=np.where(ro.any(1))[0]; r_cols=np.where(ro.any(0))[0]
    # urdu = all ink minus roman's x-extent rows below cap: use text widths from the page for x, ink rows above ro_cap for top
    u_rows=np.where(a[:ro_cap].any(1))[0]
    # urdu bottom: lowest ink row whose columns fall OUTSIDE the roman extent or above ro_cap
    lowest_ur = u_rows.max() if len(u_rows) else None
    # descenders that dip into the roman band: ink rows >= ro_cap where columns are outside the Roman x-extent
    dip=a[ro_cap:, :].copy(); dip[:, r_cols.min():r_cols.max()+1]=False if len(r_cols) else dip[:, :]
    res.append(dict(i=c['i'], t=c['t'], ur_top=Y0+u_rows.min(), ur_low=Y0+lowest_ur, ro_top=Y0+ro_cap+r_rows.min(), ro_bot=Y0+ro_cap+r_rows.max(), urW=round(c['urW']), roW=round(c['roW']), ro=c['ro']))
for k in ['ur_top','ro_bot','urW','roW']:
    v=[r[k] for r in res]; print(k, 'min', min(v), 'median', int(np.median(v)), 'max', max(v))
print('widest urdu:', sorted(res,key=lambda r:-r['urW'])[:3])
print('highest urdu ink:', sorted(res,key=lambda r:r['ur_top'])[:3])
