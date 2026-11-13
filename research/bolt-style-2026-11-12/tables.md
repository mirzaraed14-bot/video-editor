### 1. Cuts

| Short | dur s | cuts | cuts/10s | shot len median s | mean | min | max |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 3ESX (57s) | 57.4 | 19 | 3.31 | 2.48 | 2.87 | 1.15 | 6.23 |
| BZ-I (53s) | 53.4 | 22 | 4.12 | 1.72 | 2.32 | 1.07 | 10.42 |
| Lvmh (40s) | 40.0 | 24 | 6.01 | 1.62 | 1.6 | 0.75 | 2.65 |
| S1C7 (57s) | 56.6 | 25 | 4.42 | 1.86 | 2.18 | 1.17 | 4.85 |
| UcpS (53s) | 52.6 | 20 | 3.8 | 1.27 | 2.5 | 0.75 | 11.22 |
| zWe7 (32s) | 32.0 | 9 | 2.81 | 2.89 | 3.2 | 1.45 | 5.78 |
| **OURS (35s)** | 34.9 | 13 | 3.72 | 2.35 | 2.49 | 1.2 | 5.6 |
| **Bolt pooled** | 292.0 | 119 | 4.08 | 1.88 | 2.34 | 0.75 | 11.22 |

Bolt shot-length percentiles p10/p25/p50/p75/p90 (s): [0.91, 1.45, 1.88, 2.6, 4.03]

### 2. Camera motion inside shots (registration, 270 px grey, caption band masked)

| Short | shots | static | in | out | clean shots* | clean median rate %/s (IQR) | clean median total % | first/mid/last third %/s (clean median) | ease profile (accel/linear/decel) | pan px/s clean median | |rot| deg clean med | same-dir / alternating adjacent pairs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3ESX (57s) | 20 | 3 | 14 | 3 | 12 | 2.52 (1.6 to 3.2) | 5.3 | 2.3/2.5/2.4 | 0/7/0 | 6.4 | 0.05 | 8 / 5 |
| BZ-I (53s) | 23 | 2 | 10 | 11 | 9 | 4.04 (-0.4 to 6.0) | 6.3 | 0.6/4.0/2.1 | 2/3/0 | 23.3 | 0.26 | 4 / 14 |
| Lvmh (40s) | 25 | 1 | 19 | 5 | 15 | 4.51 (2.9 to 5.0) | 3.0 | 1.1/5.2/2.9 | 2/6/1 | 3.5 | 0.07 | 14 / 8 |
| S1C7 (57s) | 26 | 3 | 8 | 15 | 4 | -4.22 (-7.2 to -1.2) | -17.0 | 15.3/4.2/1.5 | 0/0/2 | 22.6 | 0.25 | 13 / 6 |
| UcpS (53s) | 21 | 1 | 11 | 9 | 3 | 3.97 (1.9 to 6.0) | 2.7 | 3.2/4.4/5.4 | 0/0/0 | 11.4 | 0.14 | 12 / 6 |
| zWe7 (32s) | 10 | 1 | 8 | 1 | 8 | 1.64 (1.5 to 1.7) | 4.7 | 1.7/1.7/1.6 | 0/6/0 | 1.8 | 0.10 | 6 / 1 |
| **OURS (35s)** | 14 | 0 | 12 | 2 | 1 | 10.24 (10.2 to 10.2) | 26.4 | 28.8/3.6/18.6 | 0/0/1 | 44.7 | 0.21 | 9 / 4 |

*clean = registration inlier ratio >= 0.95, |rotation| < 0.7 deg, shot >= 0.6 s. Anything else is real camera/subject motion in the footage and cannot be separated from an edit zoom. Direction strings (+ in, - out, 0 static): 

- 3ESX (57s): `++++-0++0+-+-++++0++`
- BZ-I (53s): `+--+--++--+-+0+-0+-+-+-`
- Lvmh (40s): `++-+++++-++--++++++-+++0+`
- S1C7 (57s): `---+-0++0+-----++-0-----++`
- UcpS (53s): `+-+++++++------0-++-+`
- zWe7 (32s): `++++++-0++`
- **OURS (35s)**: `+++++++++-+-++`

### 3. Transitions at the cuts

| Short | cuts | hard | dip (smooth fade through dark) | hard cut + blur decay | other flagged* |
| --- | --- | --- | --- | --- | --- |
| 3ESX (57s) | 19 | 19 | 0 | 0 | 0 |
| BZ-I (53s) | 22 | 19 | 0 | 2 | 1 |
| Lvmh (40s) | 24 | 18 | 0 | 0 | 6 |
| S1C7 (57s) | 25 | 18 | 0 | 0 | 7 |
| UcpS (53s) | 20 | 20 | 0 | 0 | 0 |
| zWe7 (32s) | 9 | 9 | 0 | 0 | 0 |
| **OURS (35s)** | 13 | 4 | 5 | 4 | 0 |

*'flash' and 'whip/slide' flags on Bolt were checked against the cut sheets: all are hard cuts inside fast footage (water glare, camera whips in the footage itself), no edit transition. OURS ground truth from timeline.json: purple = brightness dip (BCC -90, 0.333 s in, 0.267 s out) x5, cyan = hard cut + Gaussian blur decaying over 0.7 s x5, green = +30 brightness swell x1, hard x2 (17.167, 31.667).

### 4. Head stability and face framing (YuNet, every 3rd frame, 540x960)

| Short | frames with face | face height % of frame (median) | face centre y % | same-camera jump cuts found | within-shot face x std / y std px (shots with face>=15% h) |
| --- | --- | --- | --- | --- | --- |
| 3ESX (57s) | 0.42 | 16.7 | 56.5 | 0 | 59.5 / 73.3 |
| BZ-I (53s) | 0.41 | 39.0 | 30.4 | 1 | 22.95 / 22.5 |
| Lvmh (40s) | 0.67 | 17.7 | 41.8 | 0 | 52.6 / 35.5 |
| S1C7 (57s) | 0.52 | 6.5 | 37.5 | 0 | 138.65 / 239.65 |
| UcpS (53s) | 0.42 | 17.6 | 34.5 | 0 | 30.3 / 52.3 |
| zWe7 (32s) | 0.39 | 27.0 | 37.9 | 0 | 5.4 / 16.1 |
| **OURS (35s)** | 0.91 | 41.2 | 32.1 | 2 | 35.5 / 18.4 |

Same-camera jump cuts, face before -> after: 
- BZ-I (53s) t=7.017: dx 0.3 px, dy -54.6 px, height x1.105 (px at 1080x1920)
- **OURS (35s)** t=17.167: dx -82.9 px, dy -1.8 px, height x1.012 (px at 1080x1920)
- **OURS (35s)** t=31.667: dx -27.2 px, dy 37.2 px, height x0.938 (px at 1080x1920)

### 9. Texture (face crops, inner 60 % of the YuNet box, 1080x1920 frames, ~14 frames/Short with face >= 12 % of frame height)

| Short | Laplacian var | HF noise std (gray-blur1.5) | Sobel | skin hue deg (HSV, YCrCb mask) | skin sat | skin Y |
| --- | --- | --- | --- | --- | --- | --- |
| 3ESX (57s) | 22.6 | 2.27 | 1.54 | 10.0 | 0.38 | 158.0 |
| BZ-I (53s) | 30.47 | 3.06 | 1.87 | 14.0 | 0.37 | 155.5 |
| Lvmh (40s) | 52.75 | 4.31 | 2.23 | 17.0 | 0.46 | 136.0 |
| S1C7 (57s) | 128.92 | 5.56 | 2.67 | 16.0 | 0.31 | 153.5 |
| UcpS (53s) | 11.67 | 1.73 | 1.25 | 14.0 | 0.32 | 143.0 |
| zWe7 (32s) | 343.98 | 8.62 | 5.28 | 16.0 | 0.37 | 129.0 |
| **OURS (35s)** | 37.56 | 2.9 | 2.65 | 6.0 | 0.35 | 134.0 |