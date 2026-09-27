#!/usr/bin/env python
# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless"]
# ///
"""edl.json -> placement.json: timeline rows with the creator's framing.

Framing matches the creator's own sequences: every landscape source is scaled to FILL the
1080x1920 frame height (their AE head-lock comps show e.g. a 640x360 source at 546 %), and the
crop is slid sideways onto the face so the review pass never shows half a head. Where a segment
contains a camera cut, it is split at the cut so each shot gets its own crop.

usage: python plan_placement.py <job_dir> [split source_time ...]
       splits are given as clip@seconds, e.g. bashir16@25.20 sixtymin@509.80
"""
import json, os, subprocess, sys, tempfile
import cv2

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))   # wherever the repo lives (was hard-coded to E:)
MODEL = os.path.join(REPO, 'assets', 'models', 'face_detection_yunet_2023mar.onnx')
FW, FH, FPS = 1080, 1920, 60.0


def probe(src):
    out = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
                          'stream=width,height', '-of', 'csv=p=0', src], capture_output=True, text=True).stdout
    w, h = out.strip().split(',')[:2]
    return int(w), int(h)


def face_x(src, t, tmp):
    p = os.path.join(tmp, 'f.png')
    subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y', '-ss', '%.3f' % t, '-i', src,
                    '-frames:v', '1', p], check=True)
    img = cv2.imread(p)
    if img is None:
        return None
    h, w = img.shape[:2]
    det = cv2.FaceDetectorYN_create(MODEL, '', (w, h), score_threshold=0.6)
    det.setInputSize((w, h))
    _, faces = det.detect(img)
    if faces is None or len(faces) == 0:
        return None
    f = sorted(faces, key=lambda f: -f[2] * f[3])[0]
    return float(f[0] + f[2] / 2)


def snap(t):
    return round(t * FPS) / FPS


def main(job, splits):
    edl = json.load(open(os.path.join(job, 'edl.json'), encoding='utf-8'))
    split_at = {}
    for s in splits:
        clip, t = s.split('@')
        split_at.setdefault(clip, []).append(float(t))

    rows, markers, dims = [], [], {}
    tmp = tempfile.mkdtemp()
    # sources.json "border": [top/bottom, left/right] px baked into a source (a channel's frame) —
    # scale past it and keep the crop inside it. framing.json "overrides": [{clip, at, face}] sets the
    # face x (0-1 of the source width) for a piece the detector can't read (profiles, listeners, wides).
    srcmeta = json.load(open(os.path.join(job, 'sources.json'), encoding='utf-8'))
    fpath = os.path.join(job, 'framing.json')
    overrides = json.load(open(fpath, encoding='utf-8'))['overrides'] if os.path.exists(fpath) else []
    for e in edl['segments']:
        if e.get('seg') in (0, 1) and e.get('piece', 1) == 1:
            m = 'B%d %s' % (e['beat'], e['name'])
            notes = [e['warning']] if e.get('warning') else []
            if e.get('card'):
                notes.append('Card: ' + e['card'])
            if e.get('drop_candidate'):
                notes.append('DROP CANDIDATE #%d' % e['drop_candidate'])
            if e.get('placeholder'):
                notes.append('SOURCE MISSING — arrest footage is not in the bin. %.1fs slot held.' % (e['tl_out'] - e['tl_in']))
            markers.append({'t': e['tl_in'], 'name': m, 'comment': ' | '.join(notes)})
        if e.get('placeholder'):
            continue
        src = e['source']
        if src not in dims:
            dims[src] = probe(src)
        W, H = dims[src]
        bt, bl = srcmeta.get(e['clip'], {}).get('border', [0, 0])
        scale = FH / (H - 2 * bt) * 1.0005               # fill the height, a hair over to kill edge lines
        pieces = [(e['src_in'], e['src_out'])]
        sfps = e.get('src_fps') or FPS
        for cut in sorted(split_at.get(e['clip'], [])):
            if pieces[-1][0] < cut < pieces[-1][1]:
                a, b = pieces.pop()
                # a split inside ONE continuous source must land on BOTH grids (the source's frames
                # and the 60 fps timeline) or Premiere's flooring skips/repeats a sliver of audio.
                k = int(-(-(cut - a) * FPS // 1))
                for _ in range(60):
                    c2 = a + k / FPS
                    if abs((c2 - 1e-4) * sfps - round((c2 - 1e-4) * sfps)) < 0.02:
                        break
                    k += 1
                pieces += [(a, round(c2, 5)), (round(c2, 5), b)]
        tl = e['tl_in']
        for pi, (a, b) in enumerate(pieces):
            t_out = e['tl_out'] if pi == len(pieces) - 1 else snap(tl + (b - a))
            manual = [o for o in overrides if o['clip'] == e['clip'] and a <= o['at'] < b]
            fx = manual[0]['face'] * W if manual else face_x(src, (a + b) / 2, tmp)
            cx = FW / 2 if fx is None else FW / 2 - (fx - W / 2) * scale
            half = (W / 2 - bl) * scale
            cx = max(FW - half, min(half, cx))            # keep the frame covered (and the border out)
            rows.append({'beat': e['beat'], 'seg': e['seg'], 'piece': pi + 1, 'clip': e['clip'],
                         'source': src, 'src_in': round(a, 4), 'src_out': round(b, 4),
                         'tl_in': round(tl, 5), 'tl_out': round(t_out, 5),
                         'scale': round(scale * 100, 3), 'pos': [round(cx / FW, 5), 0.5],
                         'face': None if fx is None else round(fx / W, 3), 'face_manual': bool(manual)})
            tl = t_out

    json.dump({'fps': FPS, 'rows': rows, 'markers': markers, 'duration': edl['duration']},
              open(os.path.join(job, 'placement.json'), 'w', encoding='utf-8'), indent=1)
    for r in rows:
        print('B%-2d s%d.%d %-9s tl %6.2f-%6.2f  src %8.3f-%8.3f  scale %6.2f%%  posX %.3f  face@%s' % (
            r['beat'], r['seg'], r['piece'], r['clip'], r['tl_in'], r['tl_out'], r['src_in'], r['src_out'],
            r['scale'], r['pos'][0], r['face']))
    print('%d clips, %d markers, %.2fs' % (len(rows), len(markers), edl['duration']))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2:])
