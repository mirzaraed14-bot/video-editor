"""Offset between the RSS audio and a downloaded YouTube section, by FFT cross-correlation of 30 s snippets.
usage: python -I xcorr.py <rss.wav> <section.mp4> <rss_start_s> [<rss_start_s> ...]  -> per snippet: file time where it starts, z-score"""
import subprocess, sys, numpy as np
SR = 8000
def pcm(src, ss=None, t=None):
    cmd = ['ffmpeg', '-v', 'error'] + (['-ss', str(ss)] if ss is not None else []) + (['-t', str(t)] if t else []) + ['-i', src, '-vn', '-ac', '1', '-ar', str(SR), '-f', 's16le', '-']
    return np.frombuffer(subprocess.run(cmd, capture_output=True).stdout, np.int16).astype(np.float32)
rss, sec = sys.argv[1], sys.argv[2]
y = pcm(sec); y -= y.mean()
for st in map(float, sys.argv[3:]):
    x = pcm(rss, st, 30); x -= x.mean()
    n = 1 << int(np.ceil(np.log2(len(y) + len(x))))
    c = np.fft.irfft(np.fft.rfft(y, n) * np.conj(np.fft.rfft(x, n)), n)[:len(y)]
    k = int(np.argmax(np.abs(c))); z = (abs(c[k]) - np.abs(c).mean()) / np.abs(c).std()
    print('rss %7.1f s -> file %8.2f s  (file - rss = %+8.2f s, z=%.0f)' % (st, k / SR, k / SR - st, z))
