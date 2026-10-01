# /// script
# dependencies = ["opencv-python-headless", "numpy"]
# ///
"""Pre-check sheet for the head lock: every tracked layer at start / middle / end, in the creator's own
crop (the layer's scale + position), with the tracked nose as a dot. The dot must sit on the SPEAKER's
nose, and the nose inside the crop. usage: uv run track_sheet.py <job_dir> [out.jpg]   (PLAYBOOK § 2 step 2)"""
import json, subprocess, sys, cv2, numpy as np
job = sys.argv[1]; out = sys.argv[2] if len(sys.argv) > 2 else job + '/brief/track_sheet.jpg'
T = json.load(open(job + '/track.json', encoding='utf-8'))
tiles = []
for k in sorted(T, key=int):
    c = T[k]; sc = c['scale'] / 100; W, H = c['W'], c['H']
    strip = []
    for f in (0, c['frames'] // 2, c['frames'] - 1):
        t = c['src_in'] + f / 60.0
        # the frame AE shows: the last one starting at or before t
        raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', '%.3f' % (t - 3), '-t', '3.3', '-copyts', '-i', c['source'], '-an', '-vf',
                              'select=between(t\\,%.4f\\,%.4f)' % (t - 0.06, t + 1e-4), '-fps_mode', 'passthrough',
                              '-f', 'rawvideo', '-pix_fmt', 'bgr24', '-'], capture_output=True, stdin=subprocess.DEVNULL).stdout
        im = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3)[-1]
        big = cv2.resize(im, (round(W * sc), round(H * sc)))
        x0 = round(big.shape[1] / 2 - c['pos'][0] * 1080); y0 = round(big.shape[0] / 2 - c['pos'][1] * 1920)   # the layer's own position
        fr = np.zeros((1920, 1080, 3), np.uint8)
        sx0, sy0 = max(0, x0), max(0, y0)
        crop = big[sy0:y0 + 1920, sx0:x0 + 1080]
        fr[sy0 - y0:sy0 - y0 + crop.shape[0], sx0 - x0:sx0 - x0 + crop.shape[1]] = crop
        nx, ny = c['nose'][f]
        px, py = round(nx * sc - x0), round(ny * sc - y0)
        cv2.circle(fr, (px, py), 14, (0, 0, 255), -1); cv2.circle(fr, (px, py), 20, (255, 255, 255), 3)
        cv2.line(fr, (540, 0), (540, 1920), (0, 255, 0), 2)
        strip.append(cv2.resize(fr, (180, 320)))
    s = np.hstack(strip)
    cv2.putText(s, 'clip %s %.2f-%.2f' % (k, c['tl_start'], c['tl_end']), (4, 312), 0, 0.5, (0, 255, 255), 2)
    tiles.append(s)
while len(tiles) % 5:
    tiles.append(np.zeros_like(tiles[0]))
cv2.imwrite(out, np.vstack([np.hstack(tiles[i:i + 5]) for i in range(0, len(tiles), 5)]))
print('wrote', out)
