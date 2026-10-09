# per short: picture band (edge strips), caption timeline (changes, empty share), at 10 fps
import sys, subprocess, json
import numpy as np
R = sys.argv[1]
CAP = {'01_dont-release-pc':(1165,1275),'02_steroids':(1165,1285),'03_shouldnt-release-pc':(1005,1088),'04_ps4':(1050,1130),
       '05_mobile':(1075,1158),'06_forza':(1047,1142),'07_travis':(1127,1204),'08_collectors-box':(1162,1238),'09_vice-city':(1177,1253),'10_goty':(1103,1178)}
out = {}
for item in sys.argv[2:]:
    name, f = item.split(':')
    W, H = 1080, 1920
    p = subprocess.Popen(['ffmpeg','-v','error','-i',f'{R}/{f}.mov','-vf','fps=10','-f','rawvideo','-pix_fmt','rgb24','-'], stdout=subprocess.PIPE, bufsize=10**8)
    tops, bots, masks = [], [], []
    a, b = CAP[name]
    while True:
        buf = p.stdout.read(W*H*3)
        if len(buf) < W*H*3: break
        fr = np.frombuffer(buf, np.uint8).reshape(H, W, 3)
        g = fr.mean(axis=2)
        strip = np.concatenate([g[:, :24], g[:, -24:]], axis=1).mean(axis=1)
        rows = np.where(strip > 3)[0]
        if len(rows): tops.append(rows[0]/H); bots.append(rows[-1]/H)
        band = fr[a:b, 40:1040]
        m = (band > 232).all(axis=2)
        masks.append(m)
    # caption changes
    changes, empty = 0, 0; prev = None; segs = []
    cur_start = 0
    for i, m in enumerate(masks):
        n = m.sum()
        if n < 300: empty += 1; state = None
        else: state = m
        if prev is None and state is None: pass
        elif prev is None or state is None: changes += 1
        else:
            x = np.logical_xor(prev, state).sum() / max(1, np.logical_or(prev, state).sum())
            if x > 0.35: changes += 1
        prev = state
    dur = len(masks)/10
    out[name] = dict(dur=dur, top=float(np.median(tops)), bot=float(np.median(bots)), cap_changes=changes, cap_empty_share=empty/len(masks))
    print(f"{name:24s} dur {dur:5.1f}  picture {np.median(tops)*100:4.1f}%..{np.median(bots)*100:4.1f}% (h {(np.median(bots)-np.median(tops))*100:4.1f}%)  caption changes {changes:3d} ({changes/dur*60:4.0f}/min, mean hold {dur*(1-empty/len(masks))/max(1,changes/1):.2f}s)  no-caption share {empty/len(masks)*100:3.0f}%")
json.dump(out, open(sys.argv[0].replace('layout.py','layout.json'),'w'), indent=1)
