#!/usr/bin/env python
"""The Abundance Wisdom zoom pass, end to end: AE layer dump -> shots -> face-safe Center XY -> JSX.

One S_BlurMoCurves adjustment layer per footage block (README § 3):
  - direction from the creator's label: AE label 2 (yellow) = pull out, anything else = push in
  - depth from the block length (creator's rule, refined by their comp-06 review, 2026-09-21):
    <= 1.45 s -> 0.85 · <= 2.6 s -> 0.78 · < 5 s -> 0.70 · 5 s+ -> 0.67
  - Center XY from zoom_center.py, checked on the frames at BOTH ends of the block (a face that is not
    head-locked can move during the zoom); the more protective pivot wins
  - the house curve as temporal eases (44x @ 1.7 % out of key 1, 17x @ 2.8 % into key 2)
The JSX is re-runnable: it removes its own previous zoom layers first, one undo group.

usage: python zoom_pass.py <srcmap.tsv> "<comp name>" <work_dir>
  srcmap.tsv: the layer dump (layer, name, label, in, out, startTime, ..., adj, enabled, fx, path)
  writes <work_dir>/shots_*.json, centers_*.json, apply.tsv, zoom.jsx (run it with AfterFX -r)
"""
import csv, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FPS = 60.0
LAYER_NAME = 'Adjustment Layer 29'


def depth(span):
    if span <= 1.45:
        return 0.85      # tiny block: they took a 1.37 s shot from 0.78 to 0.85
    if span <= 2.6:
        return 0.78      # standard 1.5-2.5 s
    if span < 5.0:
        return 0.70      # 3-5 s: they tune this band (one 3 s shot went to 0.80)
    return 0.67          # 5 s+


def main(srcmap, comp_name, work):
    work = os.path.abspath(work)          # AE resolves relative paths from its own install folder
    os.makedirs(work, exist_ok=True)
    rows = [r for r in csv.DictReader(open(srcmap, encoding='utf-8'), delimiter='\t')
            if r['layer'].isdigit() and r.get('adj', '0') == '0' and 'Comp 1' not in r['name']
            and r.get('enabled', '1') == '1']
    # one block per distinct in/out: the creator's "double layers" (a 100 % shot over its 198-229 %
    # twin, the aesthetic) are ONE shot. The face check uses the smallest-scale copy (the visible face);
    # the block pulls out if any of its layers is yellow.
    groups = {}
    for r in rows:
        groups.setdefault((round(float(r['in']), 3), round(float(r['out']), 3)), []).append(r)
    blocks = []
    for key in sorted(groups):
        g = groups[key]
        r = dict(min(g, key=lambda x: float(x['scale'] or 100)))
        r['label'] = '2' if any(x['label'] == '2' for x in g) else r['label']
        r['n_layers'] = len(g)
        blocks.append(r)

    shots = []
    for i, r in enumerate(blocks, 1):
        a, b = float(r['in']), float(r['out'])
        d = 'out' if r['label'] == '2' else 'in'
        s = {'id': i, 'start': round(a, 3), 'end': round(b, 3), 'span': round(b - a, 3), 'dir': d,
             'z_deep': depth(b - a), 'src': r['path'].replace('\\', '/'), 'st': float(r['startTime']),
             'layers': r['n_layers']}
        vals = [float(r[k]) for k in ('scale', 'posX', 'posY', 'anchorX', 'anchorY')]
        if vals != [100.0, 540.0, 960.0, 540.0, 960.0]:     # scaled/moved (a still, a reframed twin)
            s['map'] = vals
        shots.append(s)

    # face check near both ends, 0.1 s INSIDE the block: the frames right at a cut can be soft
    # (Topaz blurs 2-4 frames at every cut), and a blurred face is not detected
    cents = {}
    for end in ('a', 'b'):
        sh = []
        for s in shots:
            inset = min(0.1, s['span'] / 4)
            t = s['start'] + inset if end == 'a' else s['end'] - inset
            sh.append(dict(s, src_time=round(t - s['st'], 4)))
        sp, cp = os.path.join(work, 'shots_%s.json' % end), os.path.join(work, 'centers_%s.json' % end)
        json.dump(sh, open(sp, 'w', encoding='utf-8'), indent=1)
        subprocess.run(['uv', 'run', os.path.join(HERE, 'zoom_center.py'), sp, os.path.join(work, 'frames_' + end), cp],
                       check=True, capture_output=True)
        for c in json.load(open(cp, encoding='utf-8')):
            cents.setdefault(c['id'], []).append(c)

    # <work>/centers.override.json: [{"start": <block start s>, "center_y": <px>, "center_x": <px, optional>, "why": ...}]:
    # whose "face" is not a person (a portrait painting on the podcast wall pulled a wide to y200).
    op = os.path.join(work, 'centers.override.json')
    overrides = json.load(open(op, encoding='utf-8')) if os.path.exists(op) else []
    lines, report = [], []
    for s in shots:
        c = min(cents[s['id']], key=lambda c: c['center'][1])      # lower y = pivot = more protective
        o = [x for x in overrides if abs(x['start'] - s['start']) < 0.02]
        if o:
            c = {'center': [float(o[0].get('center_x', 540.0)), float(o[0]['center_y'])],
                 'why': 'MANUAL: ' + o[0].get('why', 'override')}
        z0, z1 = (s['z_deep'], 1.0) if s['dir'] == 'out' else (1.0, s['z_deep'])
        lines.append('\t'.join(str(v) for v in [s['id'], '%.4f' % s['start'], '%.4f' % s['end'], s['dir'],
                                                '%.3f' % z0, '%.3f' % z1, '%.1f' % c['center'][0], '%.1f' % c['center'][1]]))
        report.append('%2d  %6.2f-%6.2f  %5.2fs  %-3s  Z %.2f -> %.2f  centre y %4d  %s%s' % (
            s['id'], s['start'], s['end'], s['span'], s['dir'].upper(), z0, z1, c['center'][1], c['why'],
            '  [%d layers]' % s['layers'] if s['layers'] > 1 else ''))
    tsv = os.path.join(work, 'apply.tsv')
    open(tsv, 'w', encoding='utf-8').write('\n'.join(lines))

    jsx = open(os.path.join(HERE, 'zoom_pass.jsx.tmpl'), encoding='utf-8').read()
    jsx = jsx.replace('%TSV%', tsv.replace('\\', '/')).replace('%OUT%', os.path.join(work, 'zoom.txt').replace('\\', '/'))
    jsx = jsx.replace('%COMP%', comp_name).replace('%LAYER%', LAYER_NAME)
    open(os.path.join(work, 'zoom.jsx'), 'w', encoding='utf-8').write(jsx)
    print('\n'.join(report))
    print('%d zooms, %d face pivots -> %s' % (len(shots), sum(1 for l in lines if not l.endswith('\t960.0')),
                                              os.path.join(work, 'zoom.jsx')))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
