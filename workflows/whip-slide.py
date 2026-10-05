#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""whip-slide.py: the YouTube-look whip-slide (horizontal slide + mirrored edges + motion blur) at every cut of a PICTURE track.

  uv run workflows/whip-slide.py IN.mp4 CUTS.json OUT.mp4          # render
  uv run workflows/whip-slide.py IN.mp4 CUTS.json OUT.mp4 --dry    # print the plan, render nothing
  (plain `python` works where numpy is installed)

Run it on the rendered picture track BEFORE the captions, watermark and hook title go on: those sit above the whip
and stay sharp and still. The spec, measured frame by frame on the reference Short:
presets/youtube-shorts/onyx-samples-youtube/README.md § 4 (look: projects/_ref-yt-shorts-shawn-ryan-farm/analysis/board/2-whip.jpg).
Not HyperFrames' `whip-pan` shader: that crossfades two edge-clamped blurred frames, which looks nothing like this.

CUTS.json   {"cuts": [{"t": 3.337, "dir": "left"}, {"frame": 120, "dir": "right"}]}
  t | frame   the cut k = the FIRST frame of the incoming shot. Seconds snap to the first frame whose start time is
              >= t - half a frame; `frame` is a 0-based index.
  dir         the way the CONTENT travels. "left": the outgoing shot exits leftward and the incoming shot enters from
              the right (it starts right of rest). "right" is the mirror image.
  optional    "offsets": [460, 260, ...]  incoming offset off rest on k, k+1, ... (px at 1080 wide); at rest after the last
              "out": [12, 55]             outgoing shift on k-2, k-1 (any length: the last entry is k-1)
              "blur": [...], "out_blur": [...]   smear lengths, replacing the defaults derived from those offsets

Per frame (px at 1080 wide, scaled to the track's width; one step per frame at the track's own rate):
  k-2, k-1   the outgoing shot shifted 12, then 55 px in the travel direction; smear 6, then 62 px
  k          the incoming shot 460 px (43 %) off rest, on the side it comes from; smear 350 px (unreadable streaks).
             A hard cut inside the motion: no flash, no zoom, no crossfade.
  k+1..k+7   260, 118, 52, 24, 12, 5, 2 px (about halving per frame); smear 2.0 x offset^0.84 = 213, 110, 55, 29,
             16, 8, 4 px, so the shot reads from k+2 and is sharp by k+5..k+7
  k+8        at rest, untouched
Those defaults are this model fitted to the reference's own frames (camera motion removed); the 3-pass profile fits
them better than a single hard-edged box.
The strip a shift uncovers is a mirror copy (a reflection across the edge, so the seam is continuous), never black.
The smear is horizontal only: 3 box passes (running sums, a Gaussian-like profile) whose combined spread equals one
box of the smear length, run over the mirror-tiled picture so the frame edges blur into the reflection too.

In/out: an ffmpeg rawvideo rgb24 pipe in, libx264 -crf 14 -preset medium -pix_fmt yuv420p out at the input's exact
frame rate (24000/1001 stays 24000/1001), the same colour matrix both ways. Frames away from the cuts pass through
untouched. Audio, if any, is copied. The whip itself is silent.
"""
import argparse, json, math, subprocess, sys, time
from fractions import Fraction
for _s in (sys.stdout, sys.stderr):  # Windows pipes default to cp1252, which cannot encode the status glyphs
    try:
        if (getattr(_s, "encoding", "") or "").lower().replace("-", "") != "utf8":
            _s.reconfigure(encoding="utf-8")
    except Exception:
        pass

try:
    import numpy as np
except ImportError:
    sys.exit("whip-slide.py needs numpy (uv run workflows/whip-slide.py resolves it from the header)")

REF_W = 1080                                  # every px number below is at this width
# Defaults = this model fitted to the reference frames (shift + mirror + 3-pass smear, camera motion removed):
# incoming on the cuts at f120 and f314, outgoing on f78-79, f271-272 and f358-359. They agree to a few px.
OUT_PX = (12, 55)                             # outgoing shift on k-2, k-1 (~1 %, then ~5 % of the width)
OUT_BLUR = (6, 62)                            # outgoing smear on k-2, k-1
IN_PX = (460, 260, 118, 52, 24, 12, 5, 2)     # incoming offset on k .. k+7 (about halving per frame); k+8 at rest
IN_BLUR = (2.0, 0.84)                         # incoming smear = 2.0 x offset^0.84 (offset in px at 1080 wide):
                                              # 350 on the cut, 213, 110, 55, 29, 16, 8, 4. That is ~0.75 x the offset
                                              # at the cut and ~1.3 x at 12 px; a constant ratio fits the reference worse
PASSES = 3                                    # box passes per smear (3 = Gaussian-like; 1, a hard box, fits the reference worse)
MIN_BLUR = 1.5                                # a smear shorter than this is skipped
CUT_CHECK = 1.5                               # warn when a frame next to the cut changes this much more than the cut itself
MATRIX = {'bt709': 'bt709', 'smpte170m': 'smpte170m', 'bt470bg': 'bt470', 'bt2020nc': 'bt2020', 'bt2020c': 'bt2020',
          'fcc': 'fcc', 'smpte240m': 'smpte240m'}   # ffprobe color_space -> swscale matrix name


# ── probe ───────────────────────────────────────────────────────────────────────────────────────
def probe(path):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries',
                        'stream=codec_type,width,height,r_frame_rate,avg_frame_rate,nb_frames,'
                        'color_space,color_range,color_transfer,color_primaries:format=duration',
                        '-of', 'json', path], capture_output=True, text=True)
    if r.returncode:
        sys.exit(f"✗ ffprobe cannot read {path}: {r.stderr.strip()}")
    j = json.loads(r.stdout)
    v = next((s for s in j.get('streams', []) if s.get('codec_type') == 'video'), None)
    if v is None:
        sys.exit(f"✗ {path} has no video stream")
    rates = [Fraction(s) for s in (v.get('r_frame_rate'), v.get('avg_frame_rate')) if s and s != '0/0']
    rate = next((x for x in rates if 0 < x <= 240), None)
    if rate is None:
        sys.exit(f"✗ cannot read a frame rate from {path}")
    if len(rates) == 2 and rates[0] != rates[1]:
        print(f"⚠ r_frame_rate {rates[0]} ≠ avg_frame_rate {rates[1]}: a variable-rate input; encoding at {rate}")
    dur = float(j.get('format', {}).get('duration') or 0)
    nb = int(v.get('nb_frames') or 0) or int(round(dur * rate))
    return dict(w=int(v['width']), h=int(v['height']), rate=rate, frames=nb, dur=dur,
                audio=any(s.get('codec_type') == 'audio' for s in j['streams']),
                space=v.get('color_space'), range=v.get('color_range'),
                trc=v.get('color_transfer'), prim=v.get('color_primaries'))


# ── the cut list ────────────────────────────────────────────────────────────────────────────────
def frame_of(t, rate):
    """The first frame whose start time is >= t - half a frame (exact rational arithmetic)."""
    return max(0, math.ceil(Fraction(str(t)) * rate - Fraction(1, 2)))


def default_in_blur(offset):
    return IN_BLUR[0] * abs(offset) ** IN_BLUR[1]


def default_out_blur(out):
    return [OUT_BLUR[-1] / OUT_PX[-1] * o if j == len(out) - 1 else OUT_BLUR[0] / OUT_PX[0] * o
            for j, o in enumerate(out)]


def load_cuts(path, rate):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    rows = data.get('cuts') if isinstance(data, dict) else data
    if not isinstance(rows, list) or not rows:
        sys.exit(f"✗ {path}: expected {{\"cuts\": [{{\"t\": 3.337, \"dir\": \"left\"}}, ...]}}")
    cuts = []
    for n, c in enumerate(rows, 1):
        if 'frame' in c:
            k = int(c['frame'])
        elif 't' in c:
            k = frame_of(c['t'], rate)
        else:
            sys.exit(f"✗ cut {n}: needs \"t\" (seconds) or \"frame\"")
        d = str(c.get('dir', '')).strip().lower()
        d = {'l': 'left', 'r': 'right'}.get(d, d)
        if d not in ('left', 'right'):
            sys.exit(f"✗ cut {n} (frame {k}): \"dir\" must be \"left\" or \"right\" (the way the content travels)")
        offs = [float(x) for x in c.get('offsets', IN_PX)]
        out = [float(x) for x in c.get('out', OUT_PX)]
        blur = [float(x) for x in c.get('blur', [default_in_blur(o) for o in offs])]
        oblur = [float(x) for x in c.get('out_blur', default_out_blur(out))]
        if len(blur) != len(offs) or len(oblur) != len(out):
            sys.exit(f"✗ cut {n} (frame {k}): \"blur\" needs one value per offset, \"out_blur\" one per \"out\"")
        cuts.append(dict(n=n, k=k, dir=d, t=c.get('t'), offs=offs, out=out, blur=blur, oblur=oblur))
    cuts.sort(key=lambda c: c['k'])
    for a, b in zip(cuts, cuts[1:]):
        if a['k'] == b['k']:
            sys.exit(f"✗ two cuts on frame {a['k']}")
    return cuts


def build_plan(cuts, nframes, scale):
    """frame -> [signed offset px, smear px, labels]. + offset = content displaced right of rest."""
    plan = {}
    for i, c in enumerate(cuts):
        s = -1 if c['dir'] == 'left' else 1
        lo = cuts[i - 1]['k'] if i else 0                          # an outgoing frame belongs to this cut's outgoing shot
        hi = cuts[i + 1]['k'] if i + 1 < len(cuts) else nframes   # an incoming frame stops where the next shot starts
        rows = [(c['k'] - len(c['out']) + j, s * o, b, 'out') for j, (o, b) in enumerate(zip(c['out'], c['oblur']))]
        rows += [(c['k'] + j, -s * o, b, 'in') for j, (o, b) in enumerate(zip(c['offs'], c['blur']))]
        c['frames'] = []
        for f, o, b, ph in rows:
            if not (lo <= f < hi) or f >= nframes:
                continue
            e = plan.setdefault(f, [0.0, 0.0, []])
            e[0] += o * scale
            e[1] = math.hypot(e[1], b * scale)                    # two whips on one frame: spreads add in quadrature
            e[2].append(f"{c['n']}{ph}")
            c['frames'].append(f)
    return plan


# ── the frame pass ──────────────────────────────────────────────────────────────────────────────
def box_widths(length, passes=PASSES):
    """Odd box widths whose `passes`-fold combination spreads like one box `length` px long (variance length²/12)."""
    if length < MIN_BLUR:
        return []
    var = length * length / 12.0
    wl = int(math.sqrt(12.0 * var / passes + 1))
    wl = max(1, wl - (wl % 2 == 0))
    m = round((12 * var - passes * wl * wl - 4 * passes * wl - 3 * passes) / (-4 * wl - 4))
    m = min(max(m, 0), passes)
    return [w for w in [wl] * m + [wl + 2] * (passes - m) if w > 1]


def mirror_cols(cols, n):
    """Column indices folded back into 0..n-1 by reflection across the edges (edge pixel repeated, np.pad 'symmetric')."""
    m = np.mod(cols, 2 * n)
    return np.where(m >= n, 2 * n - 1 - m, m)


def box_pass(a, w):
    """One horizontal box filter of odd width w over float32 (H, N, 3), 'valid' mode: returns N - w + 1 columns."""
    c = np.cumsum(a, axis=1, dtype=np.float32)
    out = np.empty((a.shape[0], a.shape[1] - w + 1, a.shape[2]), np.float32)
    out[:, 0] = c[:, w - 1]
    np.subtract(c[:, w:], c[:, :-w], out=out[:, 1:])
    out *= 1.0 / w
    return out


def whip_frame(img, offset, blur, passes=PASSES):
    """img (H, W, 3) uint8 -> shifted `offset` px (+ = content moves right; the uncovered strip is a mirror copy)
    and smeared horizontally over `blur` px."""
    h, w, _ = img.shape
    d = int(round(offset))
    widths = box_widths(blur, passes)
    pad = sum((b - 1) // 2 for b in widths)                     # the kernel reaches this far past each edge
    tile = np.take(img, mirror_cols(np.arange(-pad - d, w + pad - d), w), axis=1)
    if not widths:
        return np.ascontiguousarray(tile)
    a = tile.astype(np.float32)
    a -= 127.5                                                 # centred values keep the float32 running sums exact enough
    for b in widths:
        a = box_pass(a, b)
    a += 128.0                                                 # +127.5 back, +0.5 to round
    return np.clip(a, 0, 255).astype(np.uint8)


# ── main ────────────────────────────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(description='Whip-slide with mirrored edges at every cut of a picture track.')
    ap.add_argument('src', help='the rendered picture track (no captions)')
    ap.add_argument('cuts', help='CUTS.json')
    ap.add_argument('out', help='output .mp4')
    ap.add_argument('--dry', action='store_true', help='print the plan and stop')
    ap.add_argument('--passes', type=int, default=PASSES, choices=(1, 2, 3, 4), help='box passes per smear (default 3)')
    ap.add_argument('--blur-scale', type=float, default=1.0, help='multiply every smear length (default 1.0)')
    a = ap.parse_args()

    p = probe(a.src)
    W, H, rate = p['w'], p['h'], p['rate']
    scale = W / REF_W
    cuts = load_cuts(a.cuts, rate)
    print(f"whip-slide: {a.src}  {W}x{H} @ {rate.numerator}/{rate.denominator} fps, {p['frames']} frames"
          + (" (+ audio, copied)" if p['audio'] else ""))
    if W * 16 != H * 9:
        print(f"⚠ not 9:16; offsets scaled to the width ({W} px)")
    for c in [c for c in cuts if not 0 < c['k'] < p['frames']]:
        print(f"⚠ cut {c['n']}: frame {c['k']} is outside the track (1..{p['frames'] - 1}); skipped")
    cuts = [c for c in cuts if 0 < c['k'] < p['frames']]
    if not cuts:
        sys.exit("✗ no cut falls inside the track: nothing to do")
    for c in cuts:
        c['blur'] = [b * a.blur_scale for b in c['blur']]
        c['oblur'] = [b * a.blur_scale for b in c['oblur']]
    plan = build_plan(cuts, p['frames'], scale)
    for c in cuts:
        k = c['k']
        sgn = '−' if c['dir'] == 'left' else '+'
        ins = ' '.join(f"{'+' if c['dir'] == 'left' else '−'}{round(o * scale)}" for o in c['offs'])
        outs = ' '.join(f"{sgn}{round(o * scale)}" for o in c['out'])
        when = f"{float(Fraction(k) / rate):.3f} s" + (f", asked {c['t']}" if c['t'] is not None else "")
        print(f"  cut {c['n']}: frame {k} ({when}), content travels {c['dir']:<5}  out {outs}  | in {ins} → 0 px"
              f"   smear {' '.join(str(round(b * scale)) for b in c['oblur'])} | {' '.join(str(round(b * scale)) for b in c['blur'])} px")
        short = [f for f in range(k - len(c['out']), k + len(c['offs'])) if f not in c['frames']]
        if short:
            print(f"    ⚠ frames {short[0]}..{short[-1]} not whipped: the track ends or a neighbouring cut is too close")
        shared = sorted(f for f in c['frames'] if len(plan[f][2]) > 1)
        if shared:
            print(f"    ⚠ frames {shared} carry two whips at once (offsets added): cuts closer than ~10 frames")
    if a.dry:
        print(f"(dry run: {len(plan)} frames would be processed, nothing written)")
        return

    # one matrix both ways, so an untouched frame goes back to the same YUV it came from; the input's tags are set
    # on the frames (setparams), because ffmpeg takes them from the frames over the -color_* encoder flags
    mat = MATRIX.get(p['space'] or '', 'bt709')
    rng = 'pc' if p['range'] in ('pc', 'jpeg') else 'tv'
    tags = [f'{k}={v}' for k, v in (('colorspace', p['space']), ('color_primaries', p['prim']),
                                    ('color_trc', p['trc']), ('range', p['range'])) if v and v != 'unknown']
    flags = 'accurate_rnd+full_chroma_int'
    dec = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', a.src, '-map', '0:v:0', '-fps_mode', 'passthrough',
                            '-vf', f'scale=in_color_matrix={mat}:in_range={rng}:flags={flags},format=rgb24',
                            '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], stdout=subprocess.PIPE, bufsize=0)
    rate_s = f"{rate.numerator}/{rate.denominator}"
    enc_cmd = ['ffmpeg', '-v', 'error', '-y', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}',
               '-framerate', rate_s, '-i', '-']
    if p['audio']:
        enc_cmd += ['-i', a.src, '-map', '0:v:0', '-map', '1:a?', '-c:a', 'copy']
    enc_cmd += ['-vf', f'scale=out_color_matrix={mat}:out_range={rng}:flags={flags},format=yuv420p'
                + (',setparams=' + ':'.join(tags) if tags else ''),
                '-c:v', 'libx264', '-crf', '14', '-preset', 'medium', '-pix_fmt', 'yuv420p', '-r', rate_s,
                '-movflags', '+faststart', a.out]
    enc = subprocess.Popen(enc_cmd, stdin=subprocess.PIPE)

    near = {f for c in cuts for f in range(c['k'] - 3, c['k'] + 3)}   # small thumbnails to check each cut lands on a shot change
    thumbs, t0, n, done, size = {}, time.time(), 0, 0, W * H * 3
    buf = bytearray(size)            # one reused frame buffer, filled with readinto: a big pipe buffer is ~10x slower on Windows
    view = memoryview(buf)
    try:
        while True:
            got = 0
            while got < size:
                r = dec.stdout.readinto(view[got:])
                if not r:
                    break
                got += r
            if got < size:
                break
            frame = view
            if n in near or n in plan:
                img = np.frombuffer(buf, np.uint8).reshape(H, W, 3)
                if n in near:
                    thumbs[n] = img[::8, ::8].astype(np.float32).mean(axis=2)
                if n in plan:
                    off, blur, _ = plan[n]
                    frame = whip_frame(img, off, blur, a.passes).tobytes()
                    done += 1
            enc.stdin.write(frame)
            n += 1
    except OSError:                  # the encoder died (on Windows a dead pipe raises EINVAL, not always BrokenPipeError):
        pass                         # its return code below says so
    finally:
        dec.stdout.close()
        dec.wait()
        try:
            enc.stdin.close()
        except OSError:
            pass
        enc.wait()
    if dec.returncode or enc.returncode:
        sys.exit(f"✗ ffmpeg failed (decode {dec.returncode}, encode {enc.returncode})")

    for c in cuts:                                                  # a cut time off by a frame shows up here
        k = c['k']
        diffs = {i: float(np.abs(thumbs[i] - thumbs[i - 1]).mean())
                 for i in range(k - 2, k + 3) if i in thumbs and i - 1 in thumbs}
        if k in diffs and diffs:
            j = max(diffs, key=diffs.get)
            if j != k and diffs[j] > CUT_CHECK * diffs[k]:
                print(f"⚠ cut {c['n']}: the picture changes most at frame {j}, not {k} "
                      f"(difference {diffs[j]:.1f} vs {diffs[k]:.1f}): is the cut time right?")
    if n != p['frames']:
        print(f"⚠ decoded {n} frames, the header said {p['frames']}")
    dt = time.time() - t0
    print(f"✓ {a.out}: {n} frames, {done} whipped across {len(cuts)} cuts, {dt:.1f} s ({n / max(dt, 1e-6):.0f} fps)")


if __name__ == '__main__':
    main()
