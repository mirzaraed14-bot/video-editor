# Measure white-text rows: find horizontal bands where many near-white pixels with dark neighbours occur.
import sys, glob, os
import numpy as np
from PIL import Image
for p in sorted(glob.glob(os.path.join(sys.argv[1], '*.png'))):
    im = np.asarray(Image.open(p).convert('RGB')).astype(int)
    H, W, _ = im.shape
    white = (im[:,:,0] > 235) & (im[:,:,1] > 235) & (im[:,:,2] > 235)
    # black band detection: rows fully near-black
    rowmean = im.mean(axis=(1,2))
    black_rows = rowmean < 6
    # find video band: first/last non-black rows
    nb = np.where(~black_rows)[0]
    top, bot = (nb[0], nb[-1]) if len(nb) else (0, H-1)
    cnt = white.sum(axis=1)
    rows = np.where(cnt > W*0.01)[0]
    # group into bands
    bands = []
    if len(rows):
        s = rows[0]; prev = rows[0]
        for r in rows[1:]:
            if r - prev > 6:
                bands.append((s, prev)); s = r
            prev = r
        bands.append((s, prev))
    out = []
    for a, b in bands:
        if b - a < 12: continue
        cols = np.where(white[a:b+1].sum(axis=0) > 0)[0]
        out.append(f"y {a}-{b} ({a/H*100:.1f}-{b/H*100:.1f}%, h={b-a}px={((b-a)/H*100):.1f}%) x {cols[0]}-{cols[-1]} (w={(cols[-1]-cols[0])/W*100:.0f}%)")
    print(os.path.basename(p), f"video band rows {top}-{bot} ({top/H*100:.1f}-{bot/H*100:.1f}%)")
    for o in out: print("   ", o)
