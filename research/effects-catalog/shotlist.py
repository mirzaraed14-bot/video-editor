"""Turn work/<code>/effects.json into the shot list for the stills pass.

  python shotlist.py <code>          -> prints the JS list for the browser's __shots(code, list)
  python shotlist.py <code> --local  -> extracts the stills/strips locally from src/<code>.mp4 (when yt-dlp got it)
A MOVE gets 4 frames across [t0, t1] (a strip + the middle frame as the still); otherwise one frame at the peak.
"""
import json, os, re, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))


def slug(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


code = sys.argv[1]
fx = json.load(open(os.path.join(ROOT, 'work', code, 'effects.json'), encoding='utf-8'))
shots = []
for e in fx:
    mv = e.get('move')
    ts = [round(mv[0] + (mv[1] - mv[0]) * i / 3, 2) for i in range(4)] if mv else [e['peak']]
    shots.append({'name': slug(e['name']), 'ts': ts})

if '--local' in sys.argv:
    for s in shots:
        if len(s['ts']) == 1:
            subprocess.run([sys.executable, os.path.join(ROOT, 'tools.py'), 'still', code, str(s['ts'][0]), '--name', s['name']], check=True)
        else:
            subprocess.run([sys.executable, os.path.join(ROOT, 'tools.py'), 'strip', code, str(s['ts'][0]), str(s['ts'][-1]),
                            '--n', '4', '--name', s['name']], check=True)
            mid = s['ts'][len(s['ts']) // 2]
            subprocess.run([sys.executable, os.path.join(ROOT, 'tools.py'), 'still', code, str(mid), '--name', s['name']], check=True)
else:
    print(json.dumps(shots))
