import sys, subprocess, wave, os
import numpy as np
R, A = sys.argv[1], sys.argv[2]
for item in sys.argv[3:]:
    name, f = item.split(':')
    W, H = 90, 160
    p = subprocess.run(['ffmpeg','-v','error','-i',f'{R}/{f}.mov','-vf',f'fps=30,scale={W}:{H}','-f','rawvideo','-pix_fmt','gray','-'], capture_output=True)
    F = np.frombuffer(p.stdout, np.uint8).reshape(-1, H, W).astype(np.float32)
    lum = F[:, int(0.2*H):int(0.8*H), :].mean(axis=(1,2))
    n = len(lum); dips = []; i = 0
    while i < n:
        lo, hi = max(0, i-30), min(n, i+30)
        ref = np.median(lum[lo:hi])
        if lum[i] < 0.6 * ref and ref > 25:
            j = i
            while j < n and lum[j] < 0.75 * ref: j += 1
            if (j - i) <= 15: dips.append((i/30, (j-i)/30))
            i = j + 1
        else: i += 1
    # f0
    w = wave.open(os.path.join(A, name + '.wav')); sr = w.getframerate()
    x = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32)/32768
    FR, HOP = int(0.04*sr), int(0.01*sr); lo_, hi_ = int(sr/320), int(sr/75)
    rms = np.array([np.sqrt(np.mean(x[k*HOP:k*HOP+FR]**2)) for k in range((len(x)-FR)//HOP)])
    thr = np.percentile(rms, 60)
    f0s = []
    win = np.hanning(FR)
    for k in np.where(rms > thr)[0][::2]:
        fr = x[k*HOP:k*HOP+FR]*win; fr = fr - fr.mean()
        ac = np.correlate(fr, fr, 'full')[FR-1:]
        if ac[0] <= 0: continue
        seg = ac[lo_:hi_]; m = int(np.argmax(seg)) + lo_
        if ac[m]/ac[0] > 0.5: f0s.append(sr/m)
    print(f"{name:24s} dips {len(dips):2d}: " + ', '.join(f'{t:.2f}({d:.2f}s)' for t, d in dips) + f"   | median f0 {np.median(f0s):.0f} Hz (n={len(f0s)})")
