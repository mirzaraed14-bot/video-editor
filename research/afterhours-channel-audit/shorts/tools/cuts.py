import sys, subprocess, json
import numpy as np
video = sys.argv[1]; out = sys.argv[2]
W, H = 135, 240
p = subprocess.Popen(['ffmpeg','-v','error','-i',video,'-map','0:v:0','-vf',f'fps=60,scale={W}:{H}','-f','rawvideo','-pix_fmt','gray','-'], stdout=subprocess.PIPE, bufsize=10**8)
frames = []
while True:
    b = p.stdout.read(W*H)
    if len(b) < W*H: break
    frames.append(np.frombuffer(b, np.uint8).reshape(H, W).astype(np.float32))
F = np.stack(frames)
r0, r1 = int(0.17*H), int(0.52*H)   # head region, above the caption line
reg = F[:, r0:r1, :]
d = np.abs(np.diff(reg, axis=0)).mean(axis=(1,2))
# also histogram-ish: mean luma change
n = len(d)
cuts = []
for i in range(n):
    lo, hi = max(0, i-8), min(n, i+9)
    nb = np.concatenate([d[lo:i], d[i+1:hi]])
    base = np.median(nb) if len(nb) else 1
    score = d[i] / (base + 0.5)
    if d[i] > 4.0 and score > 3.0:
        t = (i+1)/60
        if cuts and t - cuts[-1][0] < 0.12:
            if d[i] > cuts[-1][1]: cuts[-1] = (t, float(d[i]), float(score))
            continue
        cuts.append((t, float(d[i]), float(score)))
json.dump({'n_frames': len(F), 'cuts': cuts}, open(out, 'w'))
print(len(cuts), ' '.join(f'{c[0]:.2f}' for c in cuts))
