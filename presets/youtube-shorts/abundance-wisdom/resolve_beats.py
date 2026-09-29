#!/usr/bin/env python
"""beats.json (word anchors) + transcript/words.json -> edl.json (word-exact source in/out, timeline slots).

Each segment is [clip, first words, last words]. The first words are matched anywhere in the clip,
the last words after them. Edges get a small breath of padding, clamped so a cut never reaches into
the neighbouring word (that is how a "cut hard on heart" stays out of the painkiller line).
Timeline slots are laid back to back on the 60 fps grid. A beat may carry "cover": picture-only V2
inserts [{clip, src_in, from, to}] (see the code), written to edl.json "covers".

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


_AUDIO = {}


def rms_db(job, clip, a, b, hop=0.01):
    """10 ms RMS (dBFS) of raw/<clip>.* between clip-local a and b."""
    if clip not in _AUDIO:
        raw = [f for f in os.listdir(os.path.join(job, 'raw')) if os.path.splitext(f)[0] == clip][0]
        pcm = subprocess.run(['ffmpeg', '-v', 'error', '-i', os.path.join(job, 'raw', raw), '-ac', '1', '-ar', '16000',
                              '-f', 's16le', '-'], capture_output=True, check=True).stdout
        import numpy as np
        _AUDIO[clip] = np.frombuffer(pcm, np.int16).astype(float)
    import numpy as np
    x, sr, n = _AUDIO[clip], 16000, int(hop * 16000)
    i0, i1 = int(a * sr), int(b * sr)
    frames = [x[k:k + n] for k in range(i0, i1 - n + 1, n)]
    return [20 * np.log10(np.sqrt(np.mean(f ** 2)) / 32768 + 1e-9) for f in frames]


def tighten(job, clip, a, b, cfg, hop=0.01):
    """Split [a, b] at every measured pause, keeping keep_tail after the sound and keep_lead before
    the next. A pause = a run below (the segment's 10th-percentile floor + margin_db) long enough to
    remove at least min_remove. The creator cuts these at sequencing (LESSONS 2026-09-23 recut)."""
    db = rms_db(job, clip, a, b, hop)
    if not db:
        return [(a, b)], []
    whole = [d for d in rms_db(job, clip, 0, len(_AUDIO[clip]) / 16000, 0.05) if d > -120]
    floor = sorted(whole)[len(whole) // 10]               # the clip's room tone, not a speech dip
    thr = floor + cfg.get('margin_db', 6)
    tail, lead, minrm = cfg.get('keep_tail', 0.10), cfg.get('keep_lead', 0.06), cfg.get('min_remove', 0.13)
    runs, k = [], 0
    while k < len(db):
        if db[k] < thr:
            s = k
            while k < len(db) and db[k] < thr:
                k += 1
            runs.append((a + s * hop, a + k * hop))
        k += 1
    pieces, cur, cut = [], a, []
    for s, e in runs:
        if s <= a + 1e-6 or e >= b - 1e-6:          # a pause at the segment edge is the edge's business
            continue
        if (e - s) - tail - lead >= minrm:
            pieces.append((cur, s + tail))
            cur = e - lead
            cut.append(round((e - s) - tail - lead, 3))
    pieces.append((cur, b))
    return pieces, cut


def main(job, fps=60.0):
    spec = json.load(open(os.path.join(job, 'beats.json'), encoding='utf-8'))
    beats, tcfg = spec['beats'], spec.get('tighten')
    removed = []
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
            pieces, cut = (tighten(job, clip, src_in, src_out, tcfg) if tcfg and override.get('tighten', True)
                           else ([(src_in, src_out)], []))
            removed += cut
            # a camera cut in a piece's silent head/tail becomes its edge (else a 1-2 frame flash of
            # the other shot). sources.json "cuts" = camera cuts in SOURCE time (scdet).
            cam = [c - off for c in meta[clip].get('cuts', [])]
            spoken = [(w['start'], w['end']) for w in ws[i:j + 1]]
            quiet = lambda a, b: not any(s < b and e > a for s, e in spoken)
            for pi, (p_in, p_out) in enumerate(pieces, 1):
                for c in cam:
                    if p_in - 0.02 < c < p_in + 0.15 and quiet(p_in, c):
                        p_in = c
                p_in = snap_up(p_in + off, sfps) - off
                dur = math.ceil((p_out - p_in) * fps - 1e-6) / fps
                for c in cam:
                    if p_in + dur - 0.2 < c < p_in + dur + 1e-4 and quiet(c, p_in + dur):
                        dur = math.floor((c - p_in) * fps + 1e-6) / fps
                text = ' '.join(w['w'] for w in ws[i:j + 1] if p_in - 0.05 <= w['start'] < p_out)
                first_piece = si == 1 and pi == 1
                edl.append({'beat': b['n'], 'seg': si, 'piece': pi, 'name': b['name'], 'clip': clip,
                            'source': meta[clip]['source'], 'card': b.get('card') if first_piece else None,
                            'drop_candidate': b.get('drop_candidate'), 'src_fps': round(sfps, 4),
                            'warning': b.get('warning') if first_piece else None,
                            'src_in': round(p_in + off, 4), 'src_out': round(p_in + off + dur, 4),
                            'tl_in': round(t, 5), 'tl_out': round(t + dur, 5), 'text': text,
                            'match': [round(s1, 2), round(s2, 2)]})
                t += dur

    # A beat's "cover": a picture-only insert on V2 over the beat's own footage (placement drops its
    # audio), e.g. a listener's face when the source never cuts to them. from/to are source times of
    # the beat's clip ('start'/'end' = the beat's edges); the end rounds UP to the timeline grid so the
    # covered shot never shows through for a frame.
    covers = []
    for b in beats:
        rows = [e for e in edl if e['beat'] == b['n'] and not e.get('placeholder')]
        for k, cv in enumerate(b.get('cover', []), 1):
            def tl_of(x, up):
                if x == 'start':
                    return rows[0]['tl_in']
                if x == 'end':
                    return rows[-1]['tl_out']
                for e in rows:
                    if e['clip'] == b['segments'][0][0] and e['src_in'] - 1e-4 <= x <= e['src_out'] + 1e-4:
                        v = (e['tl_in'] + x - e['src_in']) * fps
                        return (math.ceil(v - 1e-6) if up else math.floor(v + 1e-6)) / fps
                sys.exit('cover %d of beat %d: %s is not inside the beat' % (k, b['n'], x))
            a, z = tl_of(cv['from'], False), tl_of(cv['to'], True)
            cm = meta[cv['clip']]
            if 'fps' not in cm:
                cm['fps'] = source_fps(cm['source'])
            s_in = snap_up(cv['src_in'], cm['fps'])
            covers.append({'beat': b['n'], 'cover': k, 'clip': cv['clip'], 'source': cm['source'],
                           'src_fps': round(cm['fps'], 4), 'src_in': round(s_in, 4),
                           'src_out': round(s_in + z - a, 4), 'tl_in': round(a, 5), 'tl_out': round(z, 5),
                           'to_src': cv['to'] if isinstance(cv['to'], (int, float)) else None})

    json.dump(meta, open(os.path.join(job, 'sources.json'), 'w', encoding='utf-8'), indent=1)
    out = os.path.join(job, 'edl.json')
    json.dump({'fps': fps, 'duration': round(t, 4), 'segments': edl, 'covers': covers},
              open(out, 'w', encoding='utf-8'), indent=1)
    for e in edl:
        if e.get('placeholder'):
            print('B%-2d        %6.2f-%6.2f  [PLACEHOLDER %.1fs — %s]' % (e['beat'], e['tl_in'], e['tl_out'],
                                                                   e['tl_out'] - e['tl_in'], e['name']))
            continue
        print('B%-2d s%d %-9s src %8.3f-%8.3f  tl %6.2f-%6.2f  %4.2fs  %s' % (
            e['beat'], e['seg'], e['clip'], e['src_in'], e['src_out'], e['tl_in'], e['tl_out'],
            e['tl_out'] - e['tl_in'], e['text'][:70]))
    for c in covers:
        print('B%-2d V2 %-9s src %8.3f-%8.3f  tl %6.2f-%6.2f  %4.2fs  [cover, picture only]' % (
            c['beat'], c['clip'], c['src_in'], c['src_out'], c['tl_in'], c['tl_out'], c['tl_out'] - c['tl_in']))
    if removed:
        print('\ntightened: %d pauses removed, %.2fs total (%s)' % (
            len(removed), sum(removed), ', '.join('%.2f' % r for r in sorted(removed))))
    print('\ntotal %.2fs -> %s' % (t, out))


if __name__ == '__main__':
    main(sys.argv[1])
