"""Lay the per-cue PNGs (render_cues.mjs) on a caption job at the .srt switch times (frame-snapped by build.py).

usage: python assemble.py <job dir> <cue dir> <out.mp4>            burned preview over the job's cut (h264, audio copied)
       python assemble.py <job dir> <cue dir> <out.mov> --alpha    a transparent full-frame layer (QuickTime Animation, RGBA)
                                                                   for the creator's V2 at 00:00
"""
import glob, json, os, re, subprocess, sys
job, var_dir, out = sys.argv[1:4]; alpha = '--alpha' in sys.argv
m = json.load(open(os.path.join(var_dir, 'cues.json'), encoding='utf-8')); Y0 = m['params']['bandY']
name = os.path.basename(os.path.normpath(job))
srt = open(os.path.join(job, f'{name}.srt'), encoding='utf-8').read()
cut = os.path.join(job, 'raw', f'{name}-cut.mp4')
f = lambda s: int(s[:2]) * 3600 + int(s[3:5]) * 60 + int(s[6:8]) + int(s[9:]) / 1000
ts = [(f(a), f(b)) for a, b in re.findall(r'(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)', srt)]
assert len(ts) == len(m['cues']), (len(ts), len(m['cues']))
assert abs(ts[0][0]) < 1e-6, 'first cue must start at 0'
dur = ts[-1][1]
lst = os.path.join(var_dir, 'concat.txt')
with open(lst, 'w') as fh:
    fh.write('ffconcat version 1.0\n')
    for (a, b), c in zip(ts, m['cues']):
        fh.write(f"file '{os.path.basename(c['file'])}'\nduration {b - a:.4f}\n")
    fh.write(f"file '{os.path.basename(m['cues'][-1]['file'])}'\n")
fps = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate', '-of', 'csv=p=0', cut],
                     capture_output=True, text=True).stdout.strip() or '60'
if alpha:
    cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'lavfi', '-i', f'color=c=black@0.0:s=1080x1920:r={fps}:d={dur},format=rgba',
           '-f', 'concat', '-safe', '0', '-i', lst,
           '-filter_complex', f'[1:v]fps={fps},format=rgba[c];[0:v][c]overlay=0:{Y0}:format=rgb:shortest=0:eof_action=pass,format=argb[v]',
           '-map', '[v]', '-c:v', 'qtrle', '-t', f'{dur:.3f}', out]
else:
    cmd = ['ffmpeg', '-v', 'error', '-y', '-i', cut, '-f', 'concat', '-safe', '0', '-i', lst,
           '-filter_complex', f'[1:v]fps={fps},format=rgba[c];[0:v][c]overlay=0:{Y0}:format=auto:shortest=0:eof_action=pass[v]',
           '-map', '[v]', '-map', '0:a', '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-c:a', 'copy',
           '-t', f'{dur:.3f}', out]
subprocess.run(cmd, check=True); print('->', out)
