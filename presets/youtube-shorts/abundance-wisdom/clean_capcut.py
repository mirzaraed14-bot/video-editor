#!/usr/bin/env python
"""Repair the CapCut caption export before it goes back into After Effects ("black static" frames).

ROOT CAUSE (found 2026-09-26, LESSONS): CapCut's 4K HEVC export (~4 Mbit/s) lifts the black background
to levels 1-7 in a dithered field on ONE frame every ~2 s: frames 5, 119, 239, 359, 479, 600, 719 ...
(the same frames in every export). In AE the black is keyed out and the caption stack (Deep Glow
Unmult, Bevel Alpha, 2 x Drop Shadow at full opacity, Sharpen, Turbulent Displace) turns that faint
field into a visible dark mesh over the whole picture for one frame.

FIX: on each such frame only, every pixel that is pure black in BOTH neighbouring frames and faint in
this one is set back to black (Y 16, chroma neutral). The caption text and its motion blur are never
touched (they are not black in the neighbours), and clean frames pass through unchanged. Output is a
high-quality re-encode with the same size, rate, range and frame count.

usage: python clean_capcut.py "<CapCut export.mp4>" [out.mp4]      (default: <name>_clean.mp4 beside it)
"""
import json, os, subprocess, sys
import numpy as np

BLACK_NB, FAINT, MIN_FRAC = 16, 16 + 24, 0.005   # neighbours at Y 16 = black (limited range); a lift <= 24 levels is noise


def probe(path):
    s = json.loads(subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
                                   'stream=width,height,r_frame_rate,nb_frames', '-of', 'json', path],
                                  capture_output=True, text=True).stdout)['streams'][0]
    return int(s['width']), int(s['height']), s['r_frame_rate'], int(s.get('nb_frames', 0) or 0)


def main(src, out=None):
    out = out or os.path.splitext(src)[0] + '_clean.mp4'
    W, H, rate, nb = probe(src)
    ys, cs = W * H, (W // 2) * (H // 2)
    size = ys + 2 * cs
    dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', src, '-map', '0:v:0', '-fps_mode', 'passthrough',
                            '-pix_fmt', 'yuv420p', '-f', 'rawvideo', '-'], stdout=subprocess.PIPE)
    # The raw pipe carries no colour info: tag the INPUT exactly like the output, or ffmpeg CONVERTS
    # (it treated the pipe as BT.601 and shifted every coloured caption ~13 levels; white text was fine).
    tags = ['-color_range', 'tv', '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709']
    enc = subprocess.Popen(['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'yuv420p', '-s', '%dx%d' % (W, H),
                            '-r', rate] + tags + ['-i', '-', '-i', src, '-map', '0:v', '-map', '1:a?', '-c:a', 'copy',
                            '-c:v', 'libx264', '-preset', 'slow', '-crf', '2',
                            '-x264-params', 'psy-rd=0.0,0.0:aq-mode=0:deblock=-2,-2', '-pix_fmt', 'yuv420p'] + tags +
                           ['-movflags', '+faststart', out], stdin=subprocess.PIPE)

    def read():
        b = dec.stdout.read(size)
        return np.frombuffer(b, np.uint8).copy() if len(b) == size else None

    prev, cur, nxt, idx, fixed = None, read(), read(), 0, []
    while cur is not None:
        y = cur[:ys].reshape(H, W)
        if prev is not None and nxt is not None:
            yp, yn = prev[:ys].reshape(H, W), nxt[:ys].reshape(H, W)
            u = cur[ys:ys + cs].reshape(H // 2, W // 2)
            v = cur[ys + cs:].reshape(H // 2, W // 2)
            # the lift is mostly CHROMA (U/V 126-131 around 128) plus Y 16 -> 17 on ~35 % of pixels
            nbm = (yp <= BLACK_NB) & (yn <= BLACK_NB)         # black in both neighbours
            faint = nbm & (y <= FAINT)
            nbc = faint.reshape(H // 2, 2, W // 2, 2).all(axis=(1, 3))
            frac = max(float((faint & (y != 16)).mean()), float((nbc & ((u != 128) | (v != 128))).mean()))
            if frac > MIN_FRAC:                       # a lifted-black frame, not a caption moving
                y[faint] = 16
                u[nbc] = 128
                v[nbc] = 128
                fixed.append((idx, round(frac * 100, 1)))
        enc.stdin.write(cur.tobytes())
        prev, cur, nxt, idx = cur, nxt, read(), idx + 1
    enc.stdin.close(); enc.wait(); dec.wait()
    print('%s: %d frames (source says %d), cleaned %d: %s' % (os.path.basename(src), idx, nb, len(fixed),
          ', '.join('%d (%.1f%% of px)' % f for f in fixed)))
    print('wrote', out)
    return fixed


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)
