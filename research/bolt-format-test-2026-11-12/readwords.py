import json,sys
d=json.load(open(sys.argv[1],encoding='utf-8'))
clips=d['clips']
items=clips.items() if isinstance(clips,dict) else [(c.get('clip') or c.get('file') or c.get('name'),c) for c in clips]
for name,c in items:
    ws=c['words'] if isinstance(c,dict) and 'words' in c else c
    print('===',name)
    line=[];start=None;last=None
    for w in ws:
        s=w.get('start');e=w.get('end');t=w.get('w') or w.get('word') or w.get('text') or ''
        if s is None: line.append(t);continue
        if last is not None and (s-last>0.6 or len(line)>=14):
            print(f'[{start:7.2f}-{last:7.2f}] '+' '.join(line));line=[];start=None
        if start is None:start=s
        line.append(t);last=e
    if line:print(f'[{start:7.2f}-{last:7.2f}] '+' '.join(line))
