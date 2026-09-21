#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["numpy"]
# ///
"""graphics-qa.py: the build-time QA gate between the graphics BUILD (5b) and the REVIEW loop (5c).

  uv run workflows/graphics-qa.py projects/<job> [--ids g1,g2] [--json hf-graphics/qa-report.json] [--fps 24000/1001]
  (uv resolves numpy from the header; plain python3 works where numpy is installed; --selftest lints two fixtures offline)

Exit 1 on any FAIL: the handoff to edit-review is blocked until it is green. Everything it owns is
OFF-LIMITS to the LLM reviewers, they review intent, copy and depiction; this sweeps every frame.

Why: most review-round defects are deterministic, so this sweeps them in seconds instead of burning
review rounds on them. Long-form 16:9 only — the geometry is authored at 1920x1080 and a 4K render of the same design (3840x2160,
the 1080 layout on a `scale(2)` stage, never `#root{zoom:2}`, 2026-09-07) is measured in that frame by scaling the planes down, so it refuses
any other frame size rather than hand back a false green.

Inputs (all in the job folder): hf-graphics/placement.json (the placement manifest, one row per placed
graphic: {id, file, start, end, kind: text|full|overlay, track}; the Premiere lane's place-graphics.py
writes it, any other lane writes the same rows by hand before running this),
graphics-plan.json, transcript/cuts.json (V1 cut points = cumulative kept durations), the comps under
hf-graphics/*/compositions/, the renders those rows point at, and hf-graphics/qa-waivers.json:
  {"g18": {"band": "its lowest bounce frame sits ON y1030 by design"}, "g16": {"source:overshoot": "the chip sits BEHIND the node"}}
A waiver replaces a prose "deliberate deviation" in the build report: machine-read, named per check (or
per `check:tag`, the narrower key a tagged FAIL answers to first), shown in the report as `waived`, so a
reviewer cannot dismiss a real defect on a sentence (round 2 dismissed a real 83 ms cut-end flash that way).

Checks (per placed graphic unless noted):
  render     file exists · overlay = ProRes 4444 alpha, full-screen = opaque mp4 · fps == the timeline's
  duration   placed length vs the render's, within 1.5 frames (a trim means an exit was cut off)
  parity     a placed render that has a sibling VERSION at another resolution (g6-k.mp4 at 4K beside g6.mp4 at 1080)
             must be the same picture: workflows/render-diff.py against the newest such sibling (2026-09-07: three
             4K punch-cuts shipped 77x43 px off-centre under `#root{zoom:2}`, reported pixel-identical, unmeasured)
  band       overlays: no ink below the band floor (y1030), none within 80 px of the left/right edge (100 top),
             low-band graphics never above the band top, EVERY frame of the render (alpha sweep)
  face       side callouts (region callout-L/R): on every hold frame the ink stays 60 px off the head, ears
             included, as measured per window by chin-line.py --edl and carried in the plan cell as `head`
             (2026-09-10: g7, g12, g30 sat on his ear for a whole shipped video, the zone was picked, never measured)
  exit       overlays: the last rendered frame is EMPTY (hard-kill) unless the V1 cut is the exit
  lead       full-screens: static lead frames before the first element arrives (frame-0 rule)
  grain      full-screens carry the film-grain pass (section titles are exempt)
  dynamics   full-screens: share of its life that sits still on the 12 fps grid (warn over 60 %) + the count of big visual beats
  rack       full-screens: when the centre darkens (a rack focus) the frame edges darken with it, else the racked layer sits inside the scaled content
  cut        a full-screen (or a text animation whose exit is the cut) that ends within 8 frames of a V1 cut
             must end ON it, EXACTLY: a frame above flashes the outgoing shot, a hair below floors to the
             tick and lands short; ending far from any cut (a cut back mid-take, g14) is a choice and passes
  holes      overlays on one track: overlaps (FAIL) and sub-3-frame gaps between neighbours (warn)
  plan       every plan graphic is placed and vice versa; start/end agree within 1.5 frames
  copy       text-animation phrase == the plan's copy · no U+2014 in any on-screen copy
  source     hand comps: helpers defined or hf-anim.js loaded · registry constants exact · riseOut relative · pop() never on type ·
             float() on a wrapper over 0 → DUR · 12 fps form on bg-dark · no flash at 12 fps · no Math.random /
             onUpdate · no CSS filter-string tween · content reveals pin the zero frame · arrowheads computed ·
             position:absolute with no offsets · a pop's overshoot clears its neighbours · exits never before entrances
  density    (job) events/min, longest bare stretch, full-screen share + rate + SPREAD (≤ 40 s without one), same field twice in a row
Not here (the reviewers own them): copy meaning, depiction (card vs scene), asset contrast on its plate,
glow spill outside a prop's box, reveal burst cadence on the render.
"""
import json, os, re, subprocess, sys, glob, math, tempfile
from html.parser import HTMLParser
for _s in (sys.stdout, sys.stderr):  # Windows pipes default to cp1252, which cannot encode the status glyphs
    try:
        if (getattr(_s, "encoding", "") or "").lower().replace("-", "") != "utf8":
            _s.reconfigure(encoding="utf-8")
    except Exception:
        pass
from pathlib import Path
RENDER_DIFF = Path(__file__).resolve().parent / 'render-diff.py'   # the parity proof, same folder

try:
    import numpy as np
except ImportError:
    sys.exit("graphics-qa.py needs numpy (uv run workflows/graphics-qa.py resolves it, or: brew install numpy)")

FRAME_W, FRAME_H = 1920, 1080   # the AUTHORING frame every number below lives in; a render may be an integer
                                # multiple of it (3840x2160 on a 4K job) and is measured after scaling back down
EDGE, TOP_EDGE = 80, 100   # side margin: default-overlay-style.md § Placement (80, the user 2026-09-10; was 100)
SUBJECT = 60               # px a side callout keeps off the head, ears included (default-overlay-style.md § SIDE CALLOUTS)
ALPHA_INK = 160           # 0-255 on a 4x-downscaled alpha plane: solid ink: a glow or shadow bleeding past the box is not ink
ALPHA_ANY = 40            # anything at all (the last-frame emptiness check)
GRAIN_MIN = 0.9           # mean |frame − 3x3 median| on a full-screen's first frame; the grain pass sits ~2-4
DENSITY = dict(per_min=(11, 13), bare_max=6.0, full_pct_max=25.0, full_gap_max=40.0, full_per_min=(2, 3))   # creative-moves § THE DENSITY NUMBERS (+ SPREAD, 2026-09-10)
REGISTRY = {  # the numbers an INLINE helper block must carry (skipped when hf-anim.js is loaded)
    'DRAW': ['DRAW = 9'],
    'float': ['subtle: [6, 8, 1.25, 0.95]', 'medium: [10, 16, 1.35, 1.05]'],
    'riseIn': ['dist = 22', '0.55', 'power3.out'],
    'riseOut': ['dist = 18', '0.35', 'power2.in'],
    'pop': ['0.90', '1.10', '3*F', 'power2.out'],
    'slam': ['1.16', 'power2.out'],
}
POP_OVER, SLAM_FROM = float(REGISTRY['pop'][1]), float(REGISTRY['slam'][0])   # the overshoot scales, from the same copy
HELPERS = ('pop', 'slam', 'flash', 'riseIn', 'riseOut', 'slideIn', 'slideOut', 'float', 'camera', 'arrow', 'drawOn', 'countUp', 'reveal', 'exit')
ENTRANCES = ('pop', 'slam', 'flash', 'riseIn', 'slideIn', 'drawOn')
EXITS = ('riseOut', 'slideOut', 'exit')


def sh(*cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def probe(path):
    r = sh('ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries',
           'stream=pix_fmt,r_frame_rate,nb_frames,duration,width,height', '-of', 'json', path)
    if r.returncode: return None
    s = json.loads(r.stdout)['streams'][0]
    num, _, den = s['r_frame_rate'].partition('/')
    return dict(pix=s.get('pix_fmt'), fps=float(num) / float(den or 1),
                frames=int(s.get('nb_frames') or 0), dur=float(s.get('duration') or 0),
                w=int(s.get('width') or 0), h=int(s.get('height') or 0))


def frames(path, vf, w, h, pix='gray', n_frames=None):
    """Yield numpy frames from ffmpeg (rawvideo pipe)."""
    p = subprocess.Popen(['ffmpeg', '-v', 'error', '-i', path, '-vf', vf] + (['-frames:v', str(n_frames)] if n_frames else [])
                         + ['-f', 'rawvideo', '-pix_fmt', pix, '-'], stdout=subprocess.PIPE)
    n = w * h * (1 if pix == 'gray' else 3)
    while True:
        b = p.stdout.read(n)
        if len(b) < n: break
        yield np.frombuffer(b, np.uint8).reshape(h, w) if pix == 'gray' else np.frombuffer(b, np.uint8).reshape(h, w, 3)
    p.wait()


def norm_words(s):
    return [re.sub(r"^[^\w']+|[^\w']+$", '', w).lower() for w in re.sub(r'[*~]', '', s).split() if re.sub(r"[^\w']", '', w)]


# ── the comp's static geometry: enough CSS/DOM to place a box, never a browser ─────────────
class _Dom(HTMLParser):
    """Every element with its parent, id, classes and inline style. <template> children count:
    the comp clones them in at runtime."""
    VOID = {'br', 'img', 'input', 'meta', 'link', 'hr', 'source', 'use', 'path', 'circle',
            'rect', 'polygon', 'line', 'ellipse', 'stop'}

    def __init__(self, src):
        super().__init__(convert_charrefs=True)
        self.stack, self.els = [], []
        self.feed(src)

    def _add(self, tag, attrs):
        a = dict(attrs)
        el = dict(tag=tag, id=a.get('id'), cls=(a.get('class') or '').split(),
                  style=a.get('style') or '', parent=self.stack[-1] if self.stack else None, text='')
        self.els.append(el); return el

    def handle_data(self, data):                     # an element's OWN text (children keep theirs): is it type?
        if self.stack: self.stack[-1]['text'] += data

    def handle_startendtag(self, tag, attrs):        # `<polygon .../>`: recorded, never pushed
        self._add(tag, attrs)

    def handle_starttag(self, tag, attrs):
        el = self._add(tag, attrs)
        if tag not in self.VOID: self.stack.append(el)

    def handle_endtag(self, tag):                    # unwind to the matching open tag, never blind-pop
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i]['tag'] == tag:
                del self.stack[i:]; return


def _compound(el, c):
    """Does one compound selector (`div.node.hi`, `#n3`, `.arr`) apply to el?"""
    if ':' in c or '[' in c: return False
    toks = re.findall(r'[#.][A-Za-z0-9_-]+', c)
    tag = re.match(r'^[A-Za-z][A-Za-z0-9]*', c)
    if tag and tag.group(0).lower() not in (el['tag'], '*'): return False
    if not toks and not tag and c.strip() != '*': return False
    for t in toks:
        if t[0] == '#' and t[1:] != (el['id'] or ''): return False
        if t[0] == '.' and t[1:] not in el['cls']: return False
    return True


def _sel(el, sel):
    """(ids, classes, tags) if this ONE selector branch applies to el, else None. Ancestor-aware:
    `.node .ic svg` must not paint an #a2 svg with the icon's box (it did, and hid a real overlap)."""
    sel = sel.strip()
    if '+' in sel or '~' in sel: return None                 # sibling combinators are not modelled
    parts = [p for p in re.split(r'\s*(>)\s*|\s+', sel) if p]
    if not parts or not _compound(el, parts[-1]): return None
    node, i = el['parent'], len(parts) - 2
    while i >= 0:
        if parts[i] == '>':
            i -= 1
            if node is None or i < 0 or not _compound(node, parts[i]): return None
        else:
            while node is not None and not _compound(node, parts[i]): node = node['parent']
            if node is None: return None
        node = node['parent']; i -= 1
    return (sel.count('#'), len(re.findall(r'\.[A-Za-z]', sel)), len(re.findall(r'(?:^|[\s>])[A-Za-z]', sel)))


def _decls(el, rules):
    """The cascade, best-effort: matching rules by (specificity, source order), inline style last."""
    hits = []
    for i, (sel, blk) in enumerate(rules):
        spec = None
        for branch in sel.split(','):
            sp = _sel(el, branch)
            if sp and (spec is None or sp > spec): spec = sp
        if spec: hits.append((spec, i, blk))
    d = {}
    for _, _, blk in sorted(hits, key=lambda h: (h[0], h[1])): d.update(blk)
    for k, _, v in (x.partition(':') for x in el['style'].split(';')):
        if k.strip(): d[k.strip().lower()] = v.strip()
    return d


def _px(v):
    m = re.fullmatch(r'(-?\d+(?:\.\d+)?)(px)?', (v or '').strip())
    return float(m.group(1)) if m and (m.group(2) or float(m.group(1)) == 0) else None


def _box(d):
    l, t, w, h = _px(d.get('left')), _px(d.get('top')), _px(d.get('width')), _px(d.get('height'))
    return None if None in (l, t, w, h) else (l, t, l + w, t + h)


def _shifted(d):
    """A transform moves the element off its CSS box, so the box is not where it renders (the
    left/top + translate(-50%,-50%) centring idiom): measured geometry does not apply."""
    return bool(re.search(r'translate|rotate|matrix|skew', d.get('transform') or ''))


def _origin(d, b):
    o = (d.get('transform-origin') or '50% 50%').split() or ['50%']
    if len(o) == 1: o.append('50%')
    KEY = {'left': '0%', 'top': '0%', 'center': '50%', 'right': '100%', 'bottom': '100%'}
    out = []
    for i, part in enumerate(o[:2]):
        part = KEY.get(part, part)
        span = b[2] - b[0] if i == 0 else b[3] - b[1]
        if part.endswith('%'): out.append(b[i] + span * float(part[:-1]) / 100)
        elif _px(part) is not None: out.append(b[i] + _px(part))
        else: return None
    return tuple(out)


def _ovl(a, b):
    return (min(a[2], b[2]) - max(a[0], b[0]), min(a[3], b[3]) - max(a[1], b[1]))


def _name(el):
    return '#' + el['id'] if el['id'] else ('.' + '.'.join(el['cls']) if el['cls'] else '<%s>' % el['tag'])


def _args(js, i):
    """The text inside the call whose '(' sits at js[i]; quote- and paren-aware."""
    d, j, q = 0, i, ''
    while j < len(js):
        c = js[j]
        if q:
            if c == '\\': j += 2; continue
            if c == q: q = ''
        elif c in '\'"`': q = c
        elif c == '(': d += 1
        elif c == ')':
            d -= 1
            if d == 0: return js[i + 1:j]
        j += 1
    return js[i + 1:]


class QA:
    def __init__(self, job, fps=None, ids=None):
        self.job = Path(job).resolve()
        self.hf = self.job / 'hf-graphics'
        pj = self.hf / 'placement.json'
        if not pj.exists():
            sys.exit(f'{pj} missing: the placement manifest (see the docstring). Premiere lane: '
                     'uv run lanes/premiere/place-graphics.py <job> --plan --write; other lanes write the same rows by hand.')
        self.rows = json.load(open(pj))
        for r in self.rows:
            if r.get('kind') == 'alpha': r['kind'] = 'overlay'     # older rows named the format, not the role
        self.rows = [r for r in self.rows if r.get('kind') != 'captions']   # the caption layer is not a graphic event (and is short-form anyway)
        if ids: self.rows = [r for r in self.rows if r['id'] in ids]
        self.plan = json.load(open(self.job / 'graphics-plan.json'))
        self.cells = {b['id']: b for b in self.plan['beats'] if b.get('graphic')}
        wp = self.hf / 'qa-waivers.json'
        self.waivers = json.load(open(wp)) if wp.exists() else {}
        self.findings = []       # (id, check, level, msg)
        # source: presets/youtube/default/default-overlay-style.md § THE LOW BAND
        # (the plan carries the per-shoot edges; the defaults are the reference shoot's,
        #  re-derive with workflows/chin-line.py)
        self.band_top = (self.plan.get('low_band') or {}).get('top', 765)
        self.band_floor = (self.plan.get('low_band') or {}).get('bottom', 1030)
        self.band_measured = bool(self.plan.get('low_band'))
        cuts, t = [], 0.0
        cp = self.job / 'transcript' / 'cuts.json'
        if cp.exists():
            for s in json.load(open(cp))['segments']:
                t += float(s['end']) - float(s['start']); cuts.append(t)
        self.cuts = cuts
        self.fps = fps
        self.text_meta = {}
        self.scaled_noted = set()
        for m in glob.glob(str(self.hf / '*' / 'compositions' / '*.meta.json')):
            self.text_meta[Path(m).name.replace('.meta.json', '')] = json.load(open(m))

    def note(self, gid, check, level, msg, tag=None):
        # `check:tag` waives ONE assertion of a many-assertion check (source carries a dozen);
        # the bare `check` key still waives all of them, as the older waiver files do.
        gw = self.waivers.get(gid) or {}
        w = (gw.get(f'{check}:{tag}') if tag else None) or gw.get(check)
        if w and level == 'FAIL':
            level, msg = 'waived', f'{msg}  [waived: {w}]'
        self.findings.append((gid, check, level, msg))

    def comp(self, gid):
        # `<id>.html` or `<id>-<slug>.html` (g6-wall.html); never a bare `<id>*` prefix, g1 would swallow g11.
        # 2026-09-03: the slug form matched nothing, so the whole source lint silently never ran on a job.
        for pat in (f'{gid}.html', f'{gid}-[a-z]*.html'):
            for p in sorted(glob.glob(str(self.hf / '*' / 'compositions' / pat))):
                return Path(p)
        return None

    def cut_miss(self, t, window=8):
        """The V1 cut this time nearly lands on but misses, or None. A boundary within `window`
        frames of a cut is meant to sit ON it (off by one = a flash of the other shot); a boundary
        far from every cut is a cut back mid-take, which is a choice, not a miss. ANY miss counts:
        a row a hair BELOW the tick floors to the previous frame on placement and lands short, so
        only float noise on a snapped row (3e-06 s) is clean, never half a frame."""
        if not self.cuts: return None
        f = 1.0 / self.fps
        c = min(self.cuts, key=lambda x: abs(x - t))
        return c if 1e-4 < abs(t - c) <= window * f else None

    def other_resolution_sibling(self, f, pr):
        """The newest sibling VERSION of this render at a different resolution, or None. Siblings share the
        stem (g6, g16-alpha, g17-rules-alpha) and extension and differ only in the -<letter> version;
        the newest is the highest letter (an unversioned file is the oldest)."""
        p = Path(f)
        stem = re.sub(r'-[a-z]$', '', p.stem)
        best = None
        for q in p.parent.glob(f'{stem}*{p.suffix}'):
            if q == p or re.sub(r'-[a-z]$', '', q.stem) != stem: continue
            pq = probe(str(q))
            if not pq or (pq['w'], pq['h']) == (pr['w'], pr['h']): continue
            key = (re.search(r'-([a-z])$', q.stem) or [None, ''])[1]
            if best is None or key > best[0]: best = (key, str(q))
        return best[1] if best else None

    # ── per graphic ──────────────────────────────────────────────────────────
    def check_row(self, r):
        gid, f = r['id'], r['file']
        if not os.path.exists(f):
            self.note(gid, 'render', 'FAIL', f'render missing: {f}'); return
        pr = probe(f)
        if not pr: self.note(gid, 'render', 'FAIL', f'ffprobe cannot read {f}'); return
        if pr['w'] * FRAME_H != pr['h'] * FRAME_W or pr['w'] < FRAME_W or pr['w'] % FRAME_W:
            sys.exit(f"{f} is {pr['w']}x{pr['h']}: this gate covers long-form 16:9 renders at {FRAME_W}x{FRAME_H} or an "
                     'integer multiple of it (3840x2160). Its band floor, edge margins and alpha-sweep geometry are all '
                     '16:9 authoring-frame numbers, so a short-form job would get a meaningless green — check that render by hand instead.')
        scale = pr['w'] // FRAME_W
        if scale != 1 and gid not in self.scaled_noted:
            self.scaled_noted.add(gid); print(f"  {gid}: {pr['w']}x{pr['h']} render, measured in the {FRAME_W}x{FRAME_H} authoring frame (scale {scale}x)")
        if self.fps is None: self.fps = pr['fps']
        if abs(pr['fps'] - self.fps) > 0.01:
            self.note(gid, 'render', 'FAIL', f"render fps {pr['fps']:.3f} != timeline {self.fps:.3f}")
        F = 1.0 / self.fps
        full = r.get('kind') == 'full'
        if full and pr['pix'] and pr['pix'].startswith('yuva'):
            self.note(gid, 'render', 'FAIL', 'a full-screen graphic must be an OPAQUE mp4 (this has alpha)')
        if not full and pr['pix'] != 'yuva444p12le':
            self.note(gid, 'render', 'FAIL', f"overlay must be ProRes 4444 straight alpha (yuva444p12le), got {pr['pix']}")
        placed = r['end'] - r['start']
        if abs(placed - pr['dur']) > 1.5 * F:
            self.note(gid, 'duration', 'warn', f"placed {placed:.3f}s vs render {pr['dur']:.3f}s "
                      f"({(pr['dur'] - placed) / F:+.1f} frames): a trimmed tail cuts the exit off; extended = a frozen last frame")
        # parity: a version of this render at ANOTHER resolution must be the same picture (see the docstring)
        sib = self.other_resolution_sibling(f, pr)
        if sib:
            d = sh(sys.executable, str(RENDER_DIFF), f, sib, '--frames', '5', '--quiet')
            tail = (d.stdout.strip().splitlines() or [''])[-1]
            if d.returncode == 0:
                self.note(gid, 'parity', 'info', f'{tail} vs {os.path.basename(sib)}')
            else:
                self.note(gid, 'parity', 'FAIL', f'{tail} vs {os.path.basename(sib)}: a resolution change must not change the picture '
                          '(a comp renders at a multiple of 1080 on a scale(N) stage, never #root{zoom}); a deliberate redesign waives this')
        cell = self.cells.get(gid)
        meta = self.text_meta.get(gid, {})
        # band / edge / exit sweep on the alpha plane (overlays only)
        if not full:
            self.sweep_alpha(gid, f, r, cell, meta, F)
        else:
            self.sweep_full(gid, f, r, cell, F, pr)
        # cut alignment
        if full or meta.get('exit') == 'cut':
            for edge in (('end', r['end']),) + ((('start', r['start']),) if full else ()):
                miss = self.cut_miss(edge[1])
                if miss is not None:
                    self.note(gid, 'cut', 'FAIL', f"{edge[0]} {edge[1]:.4f} is {(edge[1] - miss) / F:+.2f} frames off the V1 cut at {miss:.4f}: "
                              f"the other shot flashes for those frames, sit exactly on the cut")
        # plan reconciliation
        if not cell:
            self.note(gid, 'plan', 'FAIL', 'placed but not a graphic:true cell in graphics-plan.json')
        else:
            for k in ('start', 'end'):
                if abs(float(cell[k]) - float(r[k])) > 1.5 * F:
                    self.note(gid, 'plan', 'FAIL', f"plan {k} {float(cell[k]):.3f} vs placed {float(r[k]):.3f} "
                              f"({(float(r[k]) - float(cell[k])) / F:+.1f} frames): run place-graphics.py --sync-plan or fix the placement")
            if '—' in (cell.get('copy') or ''):
                self.note(gid, 'copy', 'FAIL', 'em dash (U+2014) in the plan copy')
            if r.get('kind') == 'text':
                self.check_text_copy(gid, cell)
        # source lints on hand comps
        c = self.comp(gid)
        if c and r.get('kind') != 'text':
            self.lint_comp(gid, c, cell, full)
        elif c and r.get('kind') == 'text':
            src = c.read_text()
            if 'data-w="' in src:
                for w in re.findall(r'data-w="([^"]*)"', src):
                    if '*' in w or '~' in w or '—' in w:
                        self.note(gid, 'copy', 'FAIL', f'literal marker/em dash on screen: {w!r}')

    def sweep_alpha(self, gid, f, r, cell, meta, F):
        w, h = 480, 1080
        low_band = (cell or {}).get('region') == 'low-band' or r.get('kind') == 'text'
        # an element that SLIDES in or out crosses the frame edge by definition: the left/right edge
        # rule holds on its hold, not while it is passing through
        c = self.comp(gid)
        js = c.read_text() if c else ''
        slide_in = 0.75 if 'slideIn(' in js else 0.0
        slide_out = 0.38 if 'slideOut(' in js else 0.0
        worst = dict(bottom=(-1, -1), top=(10**6, -1), left=(10**6, -1), right=(-1, -1), topedge=(10**6, -1))
        last = None; n = 0
        total = probe(f)['frames'] or 0
        for i, fr in enumerate(frames(f, f'alphaextract,scale={w}:{h}', w, h)):
            n += 1; last = fr
            ys, xs = np.where(fr > ALPHA_INK)
            if ys.size == 0: continue
            b, t, l, rr = int(ys.max()), int(ys.min()), int(xs.min()) * 4, int(xs.max()) * 4
            if b > worst['bottom'][0]: worst['bottom'] = (b, i)
            if t < worst['top'][0]: worst['top'] = (t, i)
            passing = (i * F < slide_in) or (total and (total - 1 - i) * F < slide_out)
            if not passing:
                if l < worst['left'][0]: worst['left'] = (l, i)
                if rr > worst['right'][0]: worst['right'] = (rr, i)
        if n == 0:
            self.note(gid, 'render', 'FAIL', 'no frames decoded'); return
        b, bi = worst['bottom']
        if b > self.band_floor:
            self.note(gid, 'band', 'FAIL', f'ink reaches y{b} (floor {self.band_floor}) at frame {bi} ({bi * F + r["start"]:.3f}s)')
        t, ti = worst['top']
        if low_band and t < self.band_top:
            self.note(gid, 'band', 'FAIL', f'low-band graphic has ink at y{t} (band top {self.band_top}, chin clearance) at frame {ti}')
        if not low_band and t < TOP_EDGE:
            self.note(gid, 'band', 'FAIL', f'ink within {TOP_EDGE}px of the top edge (y{t}) at frame {ti}')
        l, li = worst['left']
        if l < EDGE: self.note(gid, 'band', 'FAIL', f'ink within {EDGE}px of the left edge (x{l}) at frame {li}')
        rr, ri = worst['right']
        if rr > FRAME_W - EDGE: self.note(gid, 'band', 'FAIL', f'ink within {EDGE}px of the right edge (x{rr}) at frame {ri}')
        # face: a side callout keeps SUBJECT px off the head (ears included) on every hold frame. The head is measured
        # over the graphic's own window (chin-line.py --edl, worst frame) and carried in the plan cell as
        # `head {left, right, frame}` — chin-line's own `frame` normalises a measurement taken on a 4K raw back
        # into the 1920x1080 authoring frame every number here lives in.
        region = (cell or {}).get('region') or ''
        if region in ('callout-L', 'callout-R'):
            head = (cell or {}).get('head') or {}
            fw = (head.get('frame') or [0])[0]
            # any positive width scales: a raw is not always an integer multiple of the authoring frame
            # (this repo's own long-form raws probe 3836x2160, not 3840)
            k = FRAME_W / fw if isinstance(fw, (int, float)) and fw > 0 else None
            if 'left' not in head or 'right' not in head:
                self.note(gid, 'face', 'warn', 'side callout with no measured head in its plan cell: run chin-line.py --edl over its window and record head {left,right,frame} (default-overlay-style.md § SIDE CALLOUTS)')
            elif k is None:
                self.note(gid, 'face', 'warn', f"head measured in an unknown frame (head.frame {head.get('frame')!r}): re-run chin-line.py --edl and record its `frame`, "
                          "or the margin cannot be checked (default-overlay-style.md § SIDE CALLOUTS)")
            elif region == 'callout-L' and rr > head['left'] * k - SUBJECT:
                self.note(gid, 'face', 'FAIL', f"ink reaches x{rr} at frame {ri}, inside {SUBJECT}px of the head (head left x{head['left'] * k:.0f}, ears included): "
                          "it covers his ear (default-overlay-style.md § SIDE CALLOUTS)")
            elif region == 'callout-R' and l < head['right'] * k + SUBJECT:
                self.note(gid, 'face', 'FAIL', f"ink reaches x{l} at frame {li}, inside {SUBJECT}px of the head (head right x{head['right'] * k:.0f}, ears included): "
                          "it covers his ear (default-overlay-style.md § SIDE CALLOUTS)")
            elif region == 'callout-L':
                self.note(gid, 'face', 'info', f"clear of the head: ink reaches x{rr}, head left x{head['left'] * k:.0f} ({head['left'] * k - rr:.0f}px clearance, floor {SUBJECT})")
            elif region == 'callout-R':
                self.note(gid, 'face', 'info', f"clear of the head: ink reaches x{l}, head right x{head['right'] * k:.0f} ({l - head['right'] * k:.0f}px clearance, floor {SUBJECT})")
        # an overlay that ends ON a V1 cut may use the cut as its exit (a text animation says so in
        # its meta; a hand comp says so by ending there, g4's FREE chip holds to the cut by design)
        on_cut = meta.get('exit') == 'cut' or (self.cuts and min(abs(r['end'] - c) for c in self.cuts) <= 0.6 * F)
        if not on_cut and last is not None and int(last.max()) > ALPHA_ANY:
            self.note(gid, 'exit', 'FAIL', f'last rendered frame still carries ink (alpha max {int(last.max())}): '
                      'the exit did not complete (fade ending AT DUR instead of 2 frames before) or the hard-kill is missing')

    def sweep_full(self, gid, f, r, cell, F, pr):
        w, h = 64, 36
        seq = list(frames(f, f'scale={w}:{h}', w, h))
        if not seq: self.note(gid, 'render', 'FAIL', 'no frames decoded'); return
        diffs = [float(np.abs(seq[i].astype(int) - seq[i - 1].astype(int)).mean()) for i in range(1, min(16, len(seq)))]
        lead = 0
        for d in diffs:
            if d < 1.0: lead += 1
            else: break
        if lead >= 2 and any(d > 2.5 for d in diffs):
            self.note(gid, 'lead', 'warn', f'{lead} static lead frames before the first element arrives, a defect if that '
                      'element is near-full-frame (animations.md § frame 0), fine for a small first element')
        # dynamics: how much of its life does the full-screen sit still? Measured on the 12 fps grid (every 3rd frame,
        # so a stepped render's duplicate frames do not count as stillness): a triplet is static when no 12x12 block moved. A scene has phases, props and a camera (creative-moves
        # move 2 § A FULL-SCREEN IS A SCENE): over 60 % static is the plain-Jane number (g16 as first built: three nodes
        # arriving over 10 s read 71 % static).
        # measured at 192x108 on 12x12 blocks: a clock hand, a scrolling strip or a pulsing icon moves a few blocks a lot
        # (the frame MEAN would miss them on a dark field), while grain, THE FLOAT and a slow camera push stay under the bar
        step = 3
        fine = list(frames(f, 'scale=192:108', 192, 108))
        def blockmax(a, b):
            d = np.abs(a.astype(int) - b.astype(int)).reshape(9, 12, 16, 12).mean(axis=(1, 3))
            return float(d.max())
        d3 = [blockmax(fine[i], fine[i - step]) for i in range(step, len(fine), step)]
        # rack: a comp that declares a rack layer (#racked) must darken the FRAME EDGES when it racks, not just the centre —
        # a racked layer inside the 0.92 content box leaves a bright border 4 % of the frame wide (g10/g22, 2026-09-10).
        # Keyed on the source, never on luminance alone: a dark window arriving in the centre is not a rack.
        cp_ = self.comp(gid)
        if cp_ and '#racked' in cp_.read_text():
            lum = [fr.astype(float) for fr in fine[::step]]
            cen = [float(a[22:86, 38:154].mean()) for a in lum]
            j = min(range(len(cen)), key=lambda k: cen[k])                    # the racked state: the centre at its darkest
            if cen[0] > 30 and cen[j] / cen[0] < 0.65:
                # the edges, measured at 960x540 in the outer 8 px (16 px at 1080): a 22 px bright rim vanishes in a coarser band
                big = list(frames(f, 'scale=960:540', 960, 540, n_frames=j * step + 1))
                bd = lambda a: float(np.concatenate([a[:8].ravel(), a[-8:].ravel(), a[:, :8].ravel(), a[:, -8:].ravel()]).mean())
                b0, bj = bd(big[0].astype(float)), bd(big[j * step].astype(float))
                cr = cen[j] / cen[0]
                br = bj / b0 if b0 > 30 else cr
                if br > cr + 0.15:                                             # the edges darken at least as much as the centre, within 15 points
                    self.note(gid, 'rack', 'FAIL', f'racked at {j * step * F:.2f}s the centre is {100 * (1 - cr):.0f}% darker than on frame 0 but the '
                              f'frame edges only {100 * (1 - br):.0f}%: the rack focus does not reach the edges (the racked layer belongs at '
                              'frame level, creative-moves move 2 § THE RACK FOCUS; the bad build read edges −40% against centre −66%)')
                else:
                    self.note(gid, 'rack', 'info', f'racked at {j * step * F:.2f}s: centre {100 * (1 - cr):.0f}% darker, edges {100 * (1 - br):.0f}% darker')
            else:
                self.note(gid, 'rack', 'warn', f'#racked is declared but the centre never darkens past 35% (darkest {100 * (1 - cen[j] / max(cen[0], 1)):.0f}% at {j * step * F:.2f}s): is the rack wired?')
        if d3:
            static = sum(1 for d in d3 if d < 4.0) / len(d3)
            beats = sum(1 for d in d3 if d > 40.0)
            lvl = 'warn' if static > 0.60 else 'info'
            self.note(gid, 'dynamics', lvl, f'{100 * static:.0f}% of its life is static on the 12 fps grid, {beats} big visual beat(s)'
                      + (' — a full-screen is a SCENE: phases, visuals, a camera move (creative-moves move 2)' if lvl == 'warn' else ''))
        # grain: residual against a 3x3 median on the first frame at half the RENDER's res (the grain pass runs at
        # render resolution, so a 4K render measured at 960x540 would average 4x more grain away than a 1080 one)
        gw, gh = pr['w'] // 2, pr['h'] // 2
        g0 = next(frames(f, f'scale={gw}:{gh}', gw, gh, n_frames=1))
        med = np.median(np.stack([np.roll(np.roll(g0, dy, 0), dx, 1) for dy in (-1, 0, 1) for dx in (-1, 0, 1)]), axis=0)
        resid = float(np.abs(g0.astype(float) - med).mean())
        is_title = (cell or {}).get('template', '').startswith('section') or (cell or {}).get('kind') == 'section-title'
        if resid < GRAIN_MIN and not is_title:
            self.note(gid, 'grain', 'FAIL', f'no film-grain pass on this full-screen (residual {resid:.2f} < {GRAIN_MIN})')

    def check_text_copy(self, gid, cell):
        tj = self.hf / 'text-animation' / 'text.json'
        if not tj.exists(): return
        spec = json.load(open(tj)).get(gid)
        if not spec: self.note(gid, 'copy', 'FAIL', 'text animation has no entry in text.json'); return
        shown = spec.get('display') or spec['phrase']
        # `copy` is the SPOKEN phrase (validate-plan.py anchors on it); when a cell shows different words
        # (the builder's `display`, e.g. *never* over the spoken 'ever') the plan carries them in `display`
        expect = cell.get('display') or cell.get('copy') or ''
        if norm_words(shown) != norm_words(expect):
            self.note(gid, 'copy', 'FAIL', f"on-screen words {' '.join(norm_words(shown))!r} != plan copy "
                      f"{' '.join(norm_words(expect))!r} (reconcile the plan or the spec)")

    def lint_comp(self, gid, path, cell, full):
        src = path.read_text()
        js = ''.join(re.findall(r'<script>(.*?)</script>', src, re.S))
        js = re.sub(r'/\*.*?\*/', '', js, flags=re.S)
        js = re.sub(r'(^|[^:\\])//[^\n]*', r'\1', js)          # comments are not code ("never onUpdate" matched once)
        css = ''.join(re.findall(r'<style>(.*?)</style>', src, re.S))
        # the static geometry, parsed ONCE for every check below that needs a box or a cascade
        rules = re.findall(r'([^{}]+)\{([^{}]*)\}', css)          # (selector, raw block), in source order
        cascade = [(s, dict((k.strip().lower(), v.strip()) for k, _, v in
                            (x.partition(':') for x in b.split(';')) if k.strip())) for s, b in rules]
        dom = _Dom(src)
        dec = {id(e): _decls(e, cascade) for e in dom.els}
        body = re.search(r'<body[^>]*>(.*)</body>', src, re.S)
        body = body.group(1) if body else src
        body = re.sub(r'<(script|style)>.*?</\1>', '', body, flags=re.S)
        body = re.sub(r'<!--.*?-->', '', body, flags=re.S)
        visible = re.sub(r'<[^>]+>', ' ', body)
        if '—' in visible: self.note(gid, 'copy', 'FAIL', 'em dash (U+2014) in on-screen text')
        uses_hf = 'hf-anim.js' in src
        used = {h for h in HELPERS if re.search(r'\b%s\s*\(' % h, js)}
        if not uses_hf:
            for h in used:
                if not re.search(r'\b(const|let|var|function)\s+%s\b' % h, js):
                    self.note(gid, 'source', 'FAIL', f'calls {h}() but never defines it and does not load hf-anim.js (renders blank)')
            for name, needles in REGISTRY.items():
                defined = re.search(r'\b(const|let|var|function)\s+%s\b' % name, js)
                if not defined: continue
                if name in ('pop', 'slam') and (full and (cell or {}).get('bg') == 'dark'): continue   # the 12 fps form is checked below
                missing = [n for n in needles if n.replace(' ', '') not in js.replace(' ', '')]
                if missing:
                    self.note(gid, 'source', 'FAIL', f'inline {name} drifts from the registry: {", ".join(missing)} not found (animations.md): load hf-anim.js instead of retyping')
            m = re.search(r'riseOut\s*=\s*\([^)]*\)\s*=>\s*\{.*?\n|riseOut\s*=\s*\([^)]*\)\s*=>\s*\{[^\n]*', js)
            if m and "'-='" not in m.group(0) and '"-="' not in m.group(0):
                self.note(gid, 'source', 'FAIL', 'riseOut writes an ABSOLUTE y: an element resting off 0 exits the wrong way; use y: "-=" + dist')
        if 'float' not in used:
            self.note(gid, 'source', 'FAIL', 'no float() call: every hand graphic carries THE FLOAT for its whole life (creative-moves.md move 2)', tag='float')
        else:
            for sel, t0, t1, preset in re.findall(r"float\(\s*'([^']+)'\s*,\s*([^,]+),\s*([^,]+),\s*'(\w+)'\s*\)", js):
                if t0.strip() != '0' or t1.strip() != 'DUR':
                    self.note(gid, 'source', 'warn', f'float({sel}) spans {t0.strip()} → {t1.strip()}, not 0 → DUR')
                if preset not in ('subtle', 'medium'):
                    self.note(gid, 'source', 'FAIL', f'float preset {preset!r} is not subtle|medium')
                sid = sel.lstrip('#.')
                blk = re.search(r'[#.]%s\b[^{]*\{([^}]*)\}' % re.escape(sid), css)
                if blk and 'inset:0' not in blk.group(1).replace(' ', '') and 'position:absolute' not in blk.group(1).replace(' ', ''):
                    self.note(gid, 'source', 'warn', f'float wrapper {sel} is not a position:absolute;inset:0 wrapper')
        dark = full and (cell or {}).get('bg', 'dark') == 'dark'
        if dark:
            if 'flash(' in js or 'flicker' in js:
                self.note(gid, 'source', 'FAIL', 'flash on a 12 fps graphic (its single-frame gaps vanish), pop or slam')
            if uses_hf and not re.search(r'stepFps\s*:\s*12', js):
                self.note(gid, 'source', 'FAIL', 'bg-dark full-screen loads hf-anim.js without stepFps: 12 (pop/slam will be authored in timeline frames)', tag='stepfps')
            if not uses_hf and ('pop(' in js or 'slam(' in js) and not re.search(r'S12|SF\b|/\s*12\b|\* 12\)', js):
                self.note(gid, 'source', 'FAIL', 'pop/slam authored in timeline frames on a 12 fps comp, re-express in 83 ms states (or load hf-anim.js with stepFps: 12)')
        # same-slot swap overlap (2026-09-04, g19): an in that starts before a riseOut has finished puts two
        # elements on screen at once for the 0.35s of the out. Literal times only; a swap on the same time
        # is the defect that shipped, anything inside the out's window is suspect. Different slots are
        # legitimate, so this is a warn the reviewer confirms against the layout, never a FAIL.
        outs = [(m.group(1), float(m.group(2))) for m in re.finditer(r"riseOut\(\s*'([^']+)'\s*,\s*([\d.]+)", js)]
        ins = [(m.group(2), float(m.group(3))) for m in re.finditer(r"\b(riseIn|pop|slam|slideIn)\(\s*'([^']+)'\s*,\s*([\d.]+)", js)]
        for osel, ot in outs:
            for isel, it in ins:
                if isel != osel and -0.001 <= it - ot < 0.35 - 0.001:
                    self.note(gid, 'source', 'warn', f"riseOut({osel}) at {ot} and an entrance on {isel} at {it}: if they share a slot the in starts before the out finishes (animations.md: sequence the swap, in at out + 0.35)")
        if 'Math.random' in js: self.note(gid, 'source', 'FAIL', 'Math.random in a comp: the headless render seeks, so every pass differs')
        if 'onUpdate' in js: self.note(gid, 'source', 'FAIL', 'onUpdate-driven content renders FROZEN headless (never fires on seek)')
        if 'innerText' in js and not re.search(r'innerText[^}]*\}\s*,\s*0\s*\)', js) and 'countUp(' not in js and 'reveal(' not in js:
            self.note(gid, 'source', 'FAIL', 'content reveal (innerText) has no zero-frame pin: tl.set(el, {innerText: ...}, 0)')
        if re.search(r'<polygon[^>]*class="[^"]*\bhead\b[^"]*"[^>]*points=', src):
            self.note(gid, 'source', 'FAIL', 'hand-typed arrowhead points: heads ship empty and arrow() computes them from the end tangent')
        if re.search(r'<polygon[^>]*class="[^"]*\bhead\b', src) and 'arrow(' not in js:
            self.note(gid, 'source', 'FAIL', 'arrow head present but arrow() never called (head never gets points)')
        OFFSETS = {'left', 'right', 'top', 'bottom', 'inset'}
        for sel, blk in rules:
            b = blk.replace(' ', '')
            if 'position:absolute' not in b or re.search(r'\b(left|right|top|bottom|inset)\s*:', blk) or 'root' in sel:
                continue
            # the offsets may live in ANOTHER rule (g24 declares .br's position, #tl/#tr its left/top):
            # resolve the cascade per element and name only the elements that really land at 0,0.
            els = [e for e in dom.els if any(_sel(e, br) for br in sel.split(','))]
            bare = [e for e in els if not (OFFSETS & set(dec[id(e)]))]
            if els and not bare: continue
            who = ' / '.join(_name(e) for e in bare) if bare else sel.strip()[:40]   # no match = built in JS, the g3 case
            self.note(gid, 'source', 'warn', f'{who} is position:absolute with no offsets (lands at 0,0 of its parent, the g3 check-dot bug)')
        # exits never before entrances (numeric or simple expressions)
        env = {}
        for name, val in re.findall(r'const\s+(DUR|F|SF|S12)\s*=\s*([^,;]+)', js):
            try: env[name] = eval(val, {'__builtins__': {}}, dict(env))
            except Exception: pass
        def ev(expr):
            try: return float(eval(expr, {'__builtins__': {}}, dict(env)))
            except Exception: return None
        ins, outs = {}, {}
        for fn, sel, t in re.findall(r"\b(%s)\(\s*'([^']+)'\s*,\s*([^,)]+)" % '|'.join(ENTRANCES + EXITS), js):
            v = ev(t.strip())
            if v is None: continue
            (ins if fn in ENTRANCES else outs).setdefault(sel, []).append(v)
        for sel, ts in outs.items():
            if sel in ins and min(ts) < min(ins[sel]):
                self.note(gid, 'source', 'FAIL', f'{sel} exits at {min(ts):.2f}s before it enters at {min(ins[sel]):.2f}s')
        self.check_filter_tween(gid, js)
        self.check_overshoot(gid, js, dom, dec)
        # type never pops (2026-09-10; animations.md § TEXT NEVER POPS): a pop() whose target's OWN text is
        # words is a FAIL. Words inside a child (a node's label, a row's label, the REC badge's span) make a surface.
        for m in re.finditer(r"\bpop\(\s*'([^']+)'\s*[,)]", js):
            sel = m.group(1)
            for el in (e for e in dom.els if _sel(e, sel)):
                if any(c.isalpha() for c in el['text']):
                    self.note(gid, 'source', 'FAIL', f"pop({sel}) on type ({_name(el)}: {el['text'].strip()[:40]!r}): type never pops, "
                              "it rises with the scissors or slams with the Impact (animations.md § TEXT NEVER POPS)", tag='type-pop')
                    break

    def check_filter_tween(self, gid, js):
        """A CSS `filter` STRING cannot be tweened on a seek render. GSAP parses the running value
        from the computed style only when the tween PLAYS; seeking a paused timeline it interpolates
        from the zero filter, so a wall dimmed brightness(0.55) → (0.30) blinked near-black for three
        12 fps frames (your-job g10; an explicit fromTo did not help). Dim through a black
        scrim's OPACITY; a discrete tl.set is fine."""
        for m in re.finditer(r'\b(tl|gsap)\s*\.\s*(to|from|fromTo)\s*\(', js):
            if re.search(r'(?:^|[{,\s\'"])(?:webkit)?[Ff]ilter\s*:', _args(js, m.end() - 1)):
                self.note(gid, 'source', 'FAIL', f'{m.group(1)}.{m.group(2)}() tweens a CSS `filter` string: on a seek render GSAP '
                          'interpolates it from filter(0) and the element blinks (g10). Ride the change on a black '
                          "scrim's opacity, or set the filter discretely with tl.set", tag='filter')

    def check_overshoot(self, gid, js, dom, dec):
        """A pop overshoots to 1.10 (a slam starts at 1.16) for three frames. Best effort from the
        comp's static CSS boxes: the scaled box must not reach a SIBLING it does not already overlap
        at rest (g16's payoff node slid 17 px over the '2-3 hrs' chip, missed by three review rounds).
        Unknown or transformed geometry is info, never a FAIL."""
        geo = {k: _box(d) for k, d in dec.items()}
        skipped = []
        for m in re.finditer(r"\b(pop|slam)\(\s*'([^']+)'\s*[,)]", js):
            fn, sel = m.group(1), m.group(2)
            k = POP_OVER if fn == 'pop' else SLAM_FROM
            targets = [e for e in dom.els if _sel(e, sel)]
            if not targets:
                skipped.append(f'{fn}({sel}): no such element in the markup (built in JS?)'); continue
            for el in targets:
                b, d = geo[id(el)], dec[id(el)]
                if not b:
                    skipped.append(f'{fn}({sel}) -> {_name(el)}: no explicit left/top/width/height'); continue
                if _shifted(d):
                    skipped.append(f'{fn}({sel}) -> {_name(el)}: a transform moves it off its CSS box'); continue
                o = _origin(d, b)
                if not o:
                    skipped.append(f'{fn}({sel}) -> {_name(el)}: unreadable transform-origin'); continue
                big = (o[0] - (o[0] - b[0]) * k, o[1] - (o[1] - b[1]) * k,
                       o[0] + (b[2] - o[0]) * k, o[1] + (b[3] - o[1]) * k)
                hits = {}
                for sib in dom.els:
                    if sib is el or sib['parent'] is None or sib['parent'] is not el['parent']: continue
                    sb = geo[id(sib)]
                    if not sb or _shifted(dec[id(sib)]): continue
                    rx, ry = _ovl(b, sb)
                    if rx > 0 and ry > 0: continue          # already overlapping at rest: authored
                    ox, oy = _ovl(big, sb)
                    if ox > 1 and oy > 1:
                        # an <svg>'s box is its FRAME, not its ink (g16's arrow draws to 104 of its 130 px):
                        # that pair is a warn the reviewer confirms on the render, never a gate-blocking FAIL
                        hits.setdefault((round(ox), round(oy), 'svg' in (el['tag'], sib['tag'])), []).append(_name(sib))
                for (ox, oy, soft), names in sorted(hits.items(), key=lambda h: -h[0][0] * h[0][1]):
                    self.note(gid, 'source', 'warn' if soft else 'FAIL',
                              f'{fn}({sel}) overshoot x{k:.2f} puts {_name(el)} {ox}x{oy} px over ' + ' / '.join(names)
                              + (' (svg box, not its ink: confirm on the render)' if soft
                                 else ': shift or shrink the NEIGHBOUR, never the pop (or waive it: source:overshoot)'), tag='overshoot')
        for m in re.finditer(r"\b(pop|slam)\(\s*(?!'[^']+'\s*[,)])", js):
            skipped.append(f'{m.group(1)}() on a computed selector')
        if skipped:
            self.note(gid, 'source', 'info', 'overshoot unmeasured on ' + '; '.join(skipped))

    # ── job-wide ─────────────────────────────────────────────────────────────
    def check_job(self):
        F = 1.0 / self.fps
        rows = sorted(self.rows, key=lambda r: r['start'])
        by_track = {}
        for r in rows: by_track.setdefault(r.get('track', 2), []).append(r)
        for t, rs in by_track.items():
            for a, b in zip(rs, rs[1:]):
                gap = b['start'] - a['end']
                if gap < -0.3 * F:
                    self.note(b['id'], 'holes', 'FAIL', f"overlaps {a['id']} on V{t + 1} by {-gap / F:.1f} frames (overwriteClip would eat the earlier clip)")
                elif 0.3 * F < gap < 3 * F:
                    self.note(b['id'], 'holes', 'warn', f"{gap / F:.1f}-frame hole between {a['id']} and {b['id']} on V{t + 1}, butt-join them or mean the gap")
        placed = {r['id'] for r in self.rows}
        for gid in self.cells:
            if gid not in placed and not self.only_ids:
                self.note(gid, 'plan', 'FAIL', 'graphic:true in the plan but not in placement.json')
        # THE LOW BAND is MEASURED per shoot (default-overlay-style.md § THE LOW BAND): without the plan's own
        # low_band every under-the-face overlay is silently held to the 2026-08-31 reference shoot's numbers
        _scope = f"{self.plan.get('format') or ''} {self.plan.get('preset') or ''}".lower()
        if not self.band_measured and not any(k in _scope for k in ('short', 'tiktok', 'instagram', 'explainer')):
            self.note('job', 'band', 'warn', f'plan has no low_band: measuring against the reference shoot {self.band_top}/{self.band_floor} — '
                      'run `uv run workflows/chin-line.py <base-cut>` and record low_band {top,bottom} in graphics-plan.json')
        # density
        if self.only_ids: return   # a job-level cadence measured on a filtered row set is a lie
        dur = float(self.plan.get('duration') or (rows[-1]['end'] if rows else 0)) or 1
        per_min = len(rows) / (dur / 60)
        bare, prev_end = 0.0, 0.0
        for r in rows:
            bare = max(bare, r['start'] - prev_end); prev_end = max(prev_end, r['end'])
        bare = max(bare, dur - prev_end)
        full_s = sum(r['end'] - r['start'] for r in rows if r.get('kind') == 'full')
        fulls = [r for r in rows if r.get('kind') == 'full']
        # spread: never more than 40 s of runtime without a full-screen (3 in the first 41 s and none in the last 95 passed
        # every other number here and read front-loaded, your-job 2026-09-10)
        edges = [0.0] + [t for r in fulls for t in (r['start'], r['end'])] + [dur]
        full_gap = max(edges[i + 1] - edges[i] for i in range(0, len(edges) - 1, 2)) if fulls else dur
        msg = (f"{len(rows)} events over {dur:.1f}s = {per_min:.1f}/min · longest bare stretch {bare:.1f}s · "
               f"full-screens {len(fulls)} = {full_s:.1f}s = {100 * full_s / dur:.1f}% of runtime, {len(fulls) / (dur / 60):.1f}/min, "
               f"longest stretch without one {full_gap:.1f}s")
        lvl = 'info'
        if not (DENSITY['per_min'][0] <= per_min <= DENSITY['per_min'][1] + 0.5) or bare > DENSITY['bare_max'] or 100 * full_s / dur > DENSITY['full_pct_max'] \
                or full_gap > DENSITY['full_gap_max'] or len(fulls) / (dur / 60) < DENSITY['full_per_min'][0]:
            lvl = 'warn'
        self.note('job', 'density', lvl, msg)
        for a, b in zip(fulls, fulls[1:]):
            ca, cb = self.cells.get(a['id'], {}), self.cells.get(b['id'], {})
            if ca.get('bg') and ca.get('bg') == cb.get('bg') and not any(r['start'] > a['end'] and r['end'] < b['start'] for r in rows if r.get('kind') != 'full'):
                self.note(b['id'], 'density', 'info', f"same full-screen field ({ca['bg']}) as {a['id']} with nothing between (dark is the default field since 2026-09-10; a light one is an accent, not a rotation)")

    def run(self, only_ids=None):
        self.only_ids = only_ids
        for r in self.rows:
            self.check_row(r)
        if self.fps is None: sys.exit('no readable render: cannot determine the timeline fps')
        self.check_job()
        return self.findings


def selftest():
    """The three source assertions that really PARSE (the filter tween, the pop overshoot, type never pops)
    run against a fixture that must fail and one that must not: the rest are one-line regexes whose behaviour
    is obvious by reading them, these go quietly dead (2026-09-03: a comp lookup did exactly that)."""
    src = ('<style>#float{position:absolute;inset:0}\n'
           '#a{position:absolute;left:100px;top:100px;width:100px;height:100px}\n'
           '#b{position:absolute;left:%dpx;top:100px;width:100px;height:100px}</style>\n'
           '<body><div id="float"><div id="a"></div><div id="b"></div><div id="c">words</div></div>\n'
           '<script src="hf-anim.js"></script><script>const DUR = 3;\n'
           "float('#float', 0, DUR, 'subtle'); pop('#a', 0); %s</script></body>")
    want = {'bad': ('filter', 'never pops', 'overshoot'), 'good': ()}
    with tempfile.TemporaryDirectory() as td:
        for name, args in (('bad', (200, "tl.to('#a', {filter: 'brightness(0.3)', duration: 0.3}, 0); pop('#c', 0);")),
                           ('good', (230, "tl.set('#a', {filter: 'brightness(0.3)'}, 0);"))):
            qa = QA.__new__(QA); qa.waivers, qa.findings = {}, []
            p = Path(td) / f'{name}.html'; p.write_text(src % args)
            qa.lint_comp(name, p, None, False)
            fails = [f for f in qa.findings if f[2] == 'FAIL']
            got = tuple(k for k in ('filter', 'never pops', 'overshoot') if any(k in f[3] for f in fails))
            if got != want[name] or len(fails) != len(want[name]):
                sys.exit(f'selftest FAILED on the {name} fixture: expected {want[name] or "no FAIL"}, got '
                         + (' / '.join(f'{f[2]} {f[3][:90]}' for f in qa.findings) or 'nothing'))
    print('selftest OK')


def main():
    a = sys.argv[1:]
    if '--selftest' in a: return selftest()
    if not a: sys.exit(__doc__)
    job = a[0]
    ids = None; out = None; fps = None
    if '--ids' in a: ids = a[a.index('--ids') + 1].split(',')
    if '--json' in a: out = a[a.index('--json') + 1]
    if '--fps' in a:
        num, _, den = a[a.index('--fps') + 1].partition('/'); fps = float(num) / float(den or 1)
    qa = QA(job, fps, ids)
    findings = qa.run(ids)
    fails = [f for f in findings if f[2] == 'FAIL']
    for gid in sorted({f[0] for f in findings}, key=lambda g: (g != 'job', g)):
        fs = [f for f in findings if f[0] == gid]
        mark = '✗' if any(f[2] == 'FAIL' for f in fs) else ('·' if all(f[2] == 'info' for f in fs) else '⚠')
        print(f'{mark} {gid}')
        for _, check, level, msg in fs:
            print(f'    {level:<6} {check:<8} {msg}')
    clean = [r['id'] for r in qa.rows if r['id'] not in {f[0] for f in findings}]
    if clean: print('✓ clean: ' + ' '.join(clean))
    print(f"\n{len(fails)} FAIL · {sum(1 for f in findings if f[2] == 'warn')} warn · "
          f"{sum(1 for f in findings if f[2] == 'waived')} waived · {len(qa.rows)} graphics · fps {qa.fps:.3f}")
    if out:
        rep = {'job': str(qa.job), 'fps': qa.fps, 'graphics': [r['id'] for r in qa.rows],
               'findings': [dict(id=g, check=c, level=l, msg=m) for g, c, l, m in findings],
               'waivers': qa.waivers}
        if ids:
            # a targeted run measures only the ids it was given: MERGE it into whatever report is
            # already there instead of replacing 27 graphics of proof with 2 (round-scoped reports
            # are the documented path, this is the guard for the shared one).
            rep['rechecked'] = ids
            try: old = json.load(open(out)) if os.path.exists(out) else None
            except Exception: old = None
            if isinstance(old, dict) and old.get('job') == rep['job'] and old.get('graphics'):
                gids = old['graphics'] + [g for g in rep['graphics'] if g not in old['graphics']]
                rep['findings'] = [f for f in old.get('findings') or [] if f.get('id') not in set(ids)] + rep['findings']
                rep['graphics'] = gids
                print(f'  merged {len(ids)} re-checked id(s) into the {len(gids)}-graphic report')
        json.dump(rep, open(out, 'w'), indent=1)
        print(f'report -> {out}')
    if fails:
        sys.exit(1)


if __name__ == '__main__':
    main()
