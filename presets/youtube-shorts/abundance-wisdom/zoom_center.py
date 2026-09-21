#!/usr/bin/env python
# /// script
# requires-python = ">=3.10"
# dependencies = ["opencv-python-headless"]
# ///
"""Work out S_BlurMoCurves Center XY per shot so a push-in never rides the face out of frame.

The creator's rule (2026-09-21): the face often sits high in frame, so zooming about the frame
centre pushes it further up until it crops. The zoom origin is then moved onto the face — but
only on the shots that need it.

Geometry: a point p maps to p' = p*k + o*(1 - k) when zooming by k about origin o.
Keeping the hair top at >= MARGIN therefore needs   o <= (hair_top*k - MARGIN) / (k - 1).
If the frame centre already satisfies that, the shot keeps the centre.

Input : shots.json — [{id, start, end, dir, z_deep, src, src_time, map}] where `map` is
        optional [scale, pos_x, pos_y, anchor_x, anchor_y] for a scaled still.
Output: centers.json — one row per shot with the face box, the verdict and the Center XY.

usage: python zoom_center.py <shots.json> <frames_dir> <out.json>
"""
import json, os, subprocess, sys
import cv2

REPO = r'E:/Claude Projects/video-editor-client/video-editor'
MODEL = os.path.join(REPO, 'assets', 'models', 'face_detection_yunet_2023mar.onnx')
# The creator protects the FACE, not the hairline — a zoom may crop some hair, never the face.
TOP_MARGIN = 200      # the face top must stay this far below the frame edge after the zoom.
                      # Calibrated so the trigger rate (47 %) matches the creator own rate (45 %)
                      # across their 121 measured zooms.
HAIR = 0.45           # hair sits this fraction of a face height above the detected box (reported only)
ORIGIN_MIN = 200      # never pivot higher than this (their measured range bottoms out near 83)
FRAME_W, FRAME_H = 1080, 1920


def detect(path):
    img = cv2.imread(path)
    if img is None:
        return None, None
    h, w = img.shape[:2]
    det = cv2.FaceDetectorYN_create(MODEL, '', (w, h), score_threshold=0.6)
    det.setInputSize((w, h))
    ok, faces = det.detect(img)
    if faces is None or len(faces) == 0:
        return None, (w, h)
    f = sorted(faces, key=lambda f: -f[2] * f[3])[0]
    return [float(v) for v in f[:4]], (w, h)


def main(shots_path, frames_dir, out_path):
    shots = json.load(open(shots_path, encoding='utf-8'))
    os.makedirs(frames_dir, exist_ok=True)
    rows = []
    for s in shots:
        frame = os.path.join(frames_dir, 'shot%02d.png' % s['id'])
        if s['src'].lower().endswith('.png'):
            frame = s['src']
        elif not os.path.exists(frame):
            subprocess.run(['ffmpeg', '-hide_banner', '-loglevel', 'error', '-y',
                            '-ss', '%.4f' % s['src_time'], '-i', s['src'], '-frames:v', '1', frame],
                           check=True)
        face, size = detect(frame)
        row = {'id': s['id'], 'start': s['start'], 'end': s['end'], 'dir': s['dir'],
               'z_deep': s['z_deep']}
        if not face:
            row.update(face=None, center=[FRAME_W / 2, FRAME_H / 2], why='no face — keep centre')
            rows.append(row); continue

        x, y, fw, fh = face
        face_top, cy = y, y + fh / 2
        hair = y - fh * HAIR
        if s.get('map'):                                   # still scaled into the comp
            sc, px, py, ax, ay = s['map']
            face_top = py + (face_top - ay) * sc / 100.0
            cy = py + (cy - ay) * sc / 100.0
            hair = py + (hair - ay) * sc / 100.0

        k = 1.0 / s['z_deep']
        # where the top of the face lands if we zoom about the frame centre
        top_at_centre = face_top * k + (FRAME_H / 2) * (1 - k)
        row.update(face=[round(v, 1) for v in face], face_top=round(face_top),
                   face_cy=round(cy), hair_top=round(hair), top_if_centred=round(top_at_centre))
        if top_at_centre >= TOP_MARGIN:
            row.update(center=[FRAME_W / 2, FRAME_H / 2], why='face stays in frame — keep centre')
        else:
            oy = max(ORIGIN_MIN, min(cy, FRAME_H / 2))     # pivot on the face itself
            row.update(center=[FRAME_W / 2, round(oy)],
                       why='face top would reach y%d — pivot on the face' % round(top_at_centre))
        rows.append(row)

    json.dump(rows, open(out_path, 'w', encoding='utf-8'), indent=1)
    print('%-3s %-4s %-6s %-9s %-9s %-9s %-8s %s' % ('id','dir','zDeep','faceTop','faceCy','topIfCtr','centerY','why'))
    for r in rows:
        print('%-3d %-4s %-6.2f %-9s %-9s %-9s %-8s %s' % (
            r['id'], r['dir'], r['z_deep'], r.get('face_top', '-'), r.get('face_cy', '-'),
            r.get('top_if_centred', '-'), r['center'][1], r['why']))
    moved = sum(1 for r in rows if r['center'][1] != FRAME_H / 2)
    print('\n%d of %d shots need an off-centre origin -> %s' % (moved, len(rows), out_path))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
