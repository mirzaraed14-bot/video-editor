#!/usr/bin/env python
"""beats.json (word anchors) + transcript/words.json -> edl.json (word-exact source in/out, timeline slots).

Each segment is [clip, first words, last words]. The first words are matched anywhere in the clip,
the last words after them. Edges get a small breath of padding, clamped so a cut never reaches into
the neighbouring word (that is how a "cut hard on heart" stays out of the painkiller line).
Timeline slots are laid back to back on the 60 fps grid.

usage: python resolve_beats.py <job_dir> [--fps 60]
"""
import json, math, os, re, subprocess, sys
from difflib import SequenceMatcher

LEAD, TAIL, GUARD = 0.06, 0.10, 0.03


def source_fps(src):
    out = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
                          'stream=r_frame_rate', '-of', 'csv=p=0', src], capture_output=True, text=True).stdout.strip()
    n, d = out.split('/')
    return float(n) / float(d)


def snap_up(t, fps):
    """Premiere FLOORS an in-point to the source's frame grid; pre-snap it UP so the floor
    lands exactly here and the head never grows into the previous word."""
    return math.ceil(t * fps - 1e-6) / fps + 1e-4


def norm(w):
    return re.sub(r'[^a-z0-9]', '', w.lower())


def match(words, phrase, after=0):
    target = [norm(w) for w in phrase.split() if norm(w)]
    toks = [norm(w['w']) for w in words]
    n = len(target)
    bi, bs = None, -1.0
    for i in range(after, len(words) - n + 1):
        s = SequenceMatcher(None, target, toks[i:i + n]).ratio()
        if s > bs:
            bi, bs = i, s
    return bi, bs, n


def snap(t, fps):
    return round(t * fps) / fps


def main(job, fps=60.0):
    beats = json.load(open(os.path.join(job, 'beats.json'), encoding='utf-8'))['beats']
    words_all = {os.path.splitext(c['clip'])[0]: c['words']
                 for c in json.load(open(os.path.join(job, 'transcript', 'words.json'), encoding='utf-8'))['clips']}
    meta = json.load(open(os.path.join(job, 'sources.json'), encoding='utf-8'))

    edl, t = [], 0.0
    for b in beats:
        if not b['segments']:
            dur = snap(b.get('placeholder_seconds', 0), fps)
            edl.append({'beat': b['n'], 'seg': 0, 'name': b['name'], 'placeholder': True,
                        'card': b.get('card'), 'tl_in': round(t, 5), 'tl_out': round(t + dur, 5)})
            t += dur
            continue
        for si, seg in enumerate(b['segments'], 1):
            clip, first, last = seg[:3]
            override = seg[3] if len(seg) > 3 else {}
            ws = words_all[clip]
            off = meta[clip].get('offset') or 0
            if 'fps' not in meta[clip]:
                meta[clip]['fps'] = source_fps(meta[clip]['source'])
            sfps = meta[clip]['fps']
            i, s1, n1 = match(ws, first)
            if first == last:
                j, s2 = i + n1 - 1, s1
            else:
                j0, s2, n2 = match(ws, last, after=i)
                j = j0 + n2 - 1
            if min(s1, s2) < 0.8:
                sys.exit('weak match (%.2f / %.2f) for beat %d seg %d: %r ... %r' % (s1, s2, b['n'], si, first, last))
            prev_end = ws[i - 1]['end'] if i > 0 else 0.0
            next_start = ws[j + 1]['start'] if j + 1 < len(ws) else ws[j]['end'] + 1.0
            src_in = max(ws[i]['start'] - LEAD, prev_end + GUARD) if i > 0 else max(0.0, ws[i]['start'] - LEAD)
            src_out = min(ws[j]['end'] + TAIL, next_start - GUARD)
            # measured edges (audio RMS) beat the aligner's soft word boundaries
            if 'in' in override:
                src_in = override['in'] - off
            if 'out' in override:
                src_out = override['out'] - off
            src_in = snap_up(src_in + off, sfps) - off
            dur = math.ceil((src_out - src_in) * fps - 1e-6) / fps
            text = ' '.join(w['w'] for w in ws[i:j + 1])
            edl.append({'beat': b['n'], 'seg': si, 'name': b['name'], 'clip': clip,
                        'source': meta[clip]['source'], 'card': b.get('card') if si == 1 else None,
                        'drop_candidate': b.get('drop_candidate'), 'src_fps': round(sfps, 4),
                        'warning': b.get('warning') if si == 1 else None,
                        'src_in': round(src_in + off, 4), 'src_out': round(src_in + off + dur, 4),
                        'tl_in': round(t, 5), 'tl_out': round(t + dur, 5), 'text': text,
                        'match': [round(s1, 2), round(s2, 2)]})
            t += dur

    json.dump(meta, open(os.path.join(job, 'sources.json'), 'w', encoding='utf-8'), indent=1)
    out = os.path.join(job, 'edl.json')
    json.dump({'fps': fps, 'duration': round(t, 4), 'segments': edl}, open(out, 'w', encoding='utf-8'), indent=1)
    for e in edl:
        if e.get('placeholder'):
            print('B%-2d        %6.2f-%6.2f  [PLACEHOLDER %.1fs — %s]' % (e['beat'], e['tl_in'], e['tl_out'],
                                                                   e['tl_out'] - e['tl_in'], e['name']))
            continue
        print('B%-2d s%d %-9s src %8.3f-%8.3f  tl %6.2f-%6.2f  %4.2fs  %s' % (
            e['beat'], e['seg'], e['clip'], e['src_in'], e['src_out'], e['tl_in'], e['tl_out'],
            e['tl_out'] - e['tl_in'], e['text'][:70]))
    print('\ntotal %.2fs -> %s' % (t, out))


if __name__ == '__main__':
    main(sys.argv[1])
