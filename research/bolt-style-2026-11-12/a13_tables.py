import json,numpy as np
from common import *
names={"3ESXVGflnmk":"3ESX (57s)","BZ-IBPeR2BA":"BZ-I (53s)","LvmhfahxDnY":"Lvmh (40s)","S1C7KVnzfDg":"S1C7 (57s)","UcpSXSGBtjc":"UcpS (53s)","zWe7WSLQ3dQ":"zWe7 (32s)","OURS":"**OURS (35s)**"}
cuts=json.load(open(OUT+"data/cuts_raw.json")); tl=json.load(open(ROOT+"/projects/mj-son-step-outside/build/timeline.json"))
ma=json.load(open(OUT+"data/motion_agg.json")); T=json.load(open(OUT+"data/transitions.json")); H=json.load(open(OUT+"data/head.json")); TX=json.load(open(OUT+"data/texture.json"))
def row(cells): return "| "+" | ".join(str(c) for c in cells)+" |"
def med(v): return round(float(np.median(v)),2)
out=[]
# 1 cuts
out.append("### 1. Cuts\n"); out.append(row(["Short","dur s","cuts","cuts/10s","shot len median s","mean","min","max"])); out.append(row(["---"]*8))
rows=[];
for i in IDS:
    n=len(load_gray(i)) ; c=([round(s['t0']*60) for s in tl['shots']][1:] if i=="OURS" else cuts[i]['cuts']); L=np.diff([0]+c+[n])/60
    rows.append((len(c),L)); out.append(row([names[i],round(n/60,1),len(c),round(len(c)/(n/60)*10,2),med(L),round(L.mean(),2),round(L.min(),2),round(L.max(),2)]))
allL=np.concatenate([r[1] for r in rows[:6]]); 
out.append(row(["**Bolt pooled**",round(sum(len(load_gray(i)) for i in IDS[:6])/60,0),sum(r[0] for r in rows[:6]),round(sum(r[0] for r in rows[:6])/(sum(len(load_gray(i)) for i in IDS[:6])/60)*10,2),med(allL),round(allL.mean(),2),round(allL.min(),2),round(allL.max(),2)]))
out.append(f"\nBolt shot-length percentiles p10/p25/p50/p75/p90 (s): {np.percentile(allL,[10,25,50,75,90]).round(2).tolist()}\n")
# 2 motion
out.append("### 2. Camera motion inside shots (registration, 270 px grey, caption band masked)\n")
out.append(row(["Short","shots","static","in","out","clean shots*","clean median rate %/s (IQR)","clean median total %","first/mid/last third %/s (clean median)","ease profile (accel/linear/decel)","pan px/s clean median","|rot| deg clean med","same-dir / alternating adjacent pairs"])); out.append(row(["---"]*13))
for i in IDS:
    a=ma[i]; out.append(row([names[i],a['n_shots'],a['n_static'],a['n_in'],a['n_out'],a['n_clean'],f"{a['rate_clean_med']:.2f} ({a['rate_clean_iqr'][0]:.1f} to {a['rate_clean_iqr'][1]:.1f})",f"{a['total_scale_clean_med']:.1f}","/".join(f"{x:.1f}" for x in a['thirds_clean_med']),f"{a['profile']['accel']}/{a['profile']['linear']}/{a['profile']['decel']}",f"{a['panspeed_clean_med']:.1f}",f"{a['rot_abs_clean_med']:.2f}",f"{a['same_dir_pairs']} / {a['alt_dir_pairs']}"]))
out.append("\n*clean = registration inlier ratio >= 0.95, |rotation| < 0.7 deg, shot >= 0.6 s. Anything else is real camera/subject motion in the footage and cannot be separated from an edit zoom. Direction strings (+ in, - out, 0 static): \n")
for i in IDS: out.append(f"- {names[i]}: `{ma[i]['dir_seq']}`")
# 3 transitions
out.append("\n### 3. Transitions at the cuts\n"); out.append(row(["Short","cuts","hard","dip (smooth fade through dark)","hard cut + blur decay","other flagged*"])); out.append(row(["---"]*6))
for i in IDS:
    k={}
    for o in T[i]: k[o['kind']]=k.get(o['kind'],0)+1
    other=sum(v for kk,v in k.items() if kk in('flash','whip/slide','dip'))
    out.append(row([names[i],len(T[i]),k.get('hard',0),k.get('smooth dip to dark',0),k.get('hard cut + blur decay',0),other]))
out.append("\n*'flash' and 'whip/slide' flags on Bolt were checked against the cut sheets: all are hard cuts inside fast footage (water glare, camera whips in the footage itself), no edit transition. OURS ground truth from timeline.json: purple = brightness dip (BCC -90, 0.333 s in, 0.267 s out) x5, cyan = hard cut + Gaussian blur decaying over 0.7 s x5, green = +30 brightness swell x1, hard x2 (17.167, 31.667).\n")
# 4 head
out.append("### 4. Head stability and face framing (YuNet, every 3rd frame, 540x960)\n"); out.append(row(["Short","frames with face","face height % of frame (median)","face centre y %","same-camera jump cuts found","within-shot face x std / y std px (shots with face>=15% h)"])); out.append(row(["---"]*6))
for i in IDS:
    v=H[i]; s=[x for x in v['shots'] if x['h_pct_frame']>=15 and x['n']>=8]
    out.append(row([names[i],v['face_frames_share'],v['face_h_pct_med'],v['face_cy_pct_med'],sum(j['same_cam'] for j in v['cuts_with_face_both']),f"{med([x['x_std'] for x in s])} / {med([x['y_std'] for x in s])}" if s else "-"]))
out.append("\nSame-camera jump cuts, face before -> after: ")
for i in IDS:
    for j in H[i]['cuts_with_face_both']:
        if j['same_cam']: out.append(f"- {names[i]} t={j['t']}: dx {j['dx_px1080']} px, dy {j['dy_px1080']} px, height x{j['h_ratio']} (px at 1080x1920)")
# 9 texture
out.append("\n### 9. Texture (face crops, inner 60 % of the YuNet box, 1080x1920 frames, ~14 frames/Short with face >= 12 % of frame height)\n"); out.append(row(["Short","Laplacian var","HF noise std (gray-blur1.5)","Sobel","skin hue deg (HSV, YCrCb mask)","skin sat","skin Y"])); out.append(row(["---"]*7))
for i in IDS:
    t=TX[i]; out.append(row([names[i],t['lap_var'],t['hf_noise_std'],t['sobel'],t['skin_hue'],t['skin_sat'],t['skin_Y']]))
open(OUT+"tables.md","w").write("\n".join(out)); print("\n".join(out))
