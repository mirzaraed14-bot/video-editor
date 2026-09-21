#!/usr/bin/env python3
"""validate-plan.py: the hard gate at graphics-plan Step 5: a plan that fails here is not PRESENTED.

  uv run .claude/skills/graphics-plan/scripts/validate-plan.py projects/<job> [--fps 24000/1001]

Exit 1 on any FAIL. Checks (2026-09-02, from the your-job retro, every one is a defect
the build or the review loop later paid for):
  anchor    a text-animation cell STARTS on the first word of its own copy (word.start − 0.08 lead,
            within 0.15s): not on the sentence, not on a guess (g18b, g6)
  cut       a full-screen / punch-cut edge within 8 frames of a cuts.json boundary sits ON it to the
            frame, exactly: a rounded end flashes the outgoing shot (g2 83 ms, g11 42 ms, g7 25 ms),
            and Premiere floors seconds to ticks, so an end written 16.783 for the cut at 16.78343
            lands the pin a frame early; an edge far from any cut is a cut back mid-take and passes
  readable  a cell flagged "readable": true (prompt, command, code, config, quote) holds ≥ 3.0s
            (a 2s hold of the complete content plus its reveal) and, unless it is a captured file,
            names the source_artifact it is copied from; quote/comment kinds without the
            flag are asked about
  copy      exact written source when source_artifact is set; otherwise no em dash, text animations lowercase-casual (a leading capital that is not a
            proper noun is asked about), copy present on every graphic:true cell
  shape     ids unique, start < end, kind/template/region/content present, no card overlapping a card
  capture   a screen-rec / screenshot cell carries "asset" (a file already in the job folder) or
            "capture" {source, target, action, seconds | still}: the build records it, never guesses
            (graphics-plan § THE CAPTURE GATE, 2026-09-11)
  density   the per-minute block printed against creative-moves.md § THE DENSITY NUMBERS
"""
import json, re, sys, subprocess, glob
for _s in (sys.stdout, sys.stderr):  # Windows pipes default to cp1252, which cannot encode the status glyphs
    try:
        if (getattr(_s, "encoding", "") or "").lower().replace("-", "") != "utf8":
            _s.reconfigure(encoding="utf-8")
    except Exception:
        pass
from pathlib import Path

LEAD = 0.08
FULL_KINDS = {'punch-cut', 'full-screen', 'scene', 'kinetic-title'}
TEXT_KINDS = {'text-animation'}
FILLERS = {"um", "uh", "like", "you", "know", "so", "right", "okay", "ok", "actually", "basically", "just",
           "literally", "kinda", "kind", "of", "sort", "i", "mean", "yeah", "well", "and", "then"}
PROPER = {'claude', 'premiere', 'cfo', 'youtube', 'instagram', 'tiktok', 'p&l', 'ai'}   # plus any word the transcript itself capitalizes


def _num(v):
    try: return float(v or 0)
    except (TypeError, ValueError): return 0.0


def norm(w):
    return re.sub(r"^[^\w']+|[^\w']+$", '', w).lower()


def main():
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    job = Path(a[0]).resolve()
    fps = None
    if '--fps' in a:
        n, _, d = a[a.index('--fps') + 1].partition('/'); fps = float(n) / float(d or 1)
    if fps is None:
        raws = sorted(glob.glob(str(job / 'raw' / '*')))
        if raws:
            r = subprocess.run(['ffprobe', '-v', 'error', '-select_streams', 'v:0', '-show_entries', 'stream=r_frame_rate',
                                '-of', 'csv=p=0', raws[0]], capture_output=True, text=True).stdout.strip().split('\n')[0]
            n, _, d = r.strip(',').partition('/'); fps = float(n) / float(d or 1)
    fps = fps or 30000 / 1001
    F = 1.0 / fps
    plan = json.load(open(job / 'graphics-plan.json'))
    # the SCENE and SPREAD rules are youtube/default rules (creative-moves.md): a short-form plan is not
    # held to them. Default to long-form when the plan states neither, so a long-form plan never loses them.
    _scope = f"{plan.get('format') or ''} {plan.get('preset') or ''}".lower()
    LONG = not any(k in _scope for k in ('short', 'tiktok', 'instagram', 'explainer'))
    beats = plan['beats']
    cells = [b for b in beats if b.get('graphic')]
    words = []
    tp = job / 'outputs' / f'{job.name}.transcript.json'
    if tp.exists():
        d = json.load(open(tp)); words = [w for w in (d['words'] if isinstance(d, dict) else d) if w.get('type', 'word') == 'word']
    cuts, t = [], 0.0
    cp = job / 'transcript' / 'cuts.json'
    if cp.exists():
        for s in json.load(open(cp))['segments']:
            t += float(s['end']) - float(s['start']); cuts.append(t)
    fails, warns = [], []
    F_ = fails.append; W_ = warns.append
    # names the transcript corrections already capitalize (brands, people) are proper nouns here too
    proper = PROPER | {norm(w['text']) for w in words if w['text'][:1].isupper()}

    ids = [b['id'] for b in beats]
    for i in set(ids):
        if ids.count(i) > 1: F_(f'{i}: duplicate id')
    # a graphic split into part clips for BUILD reasons (graphics-build § split part clips) is ONE graphic:
    # each continuation carries "part_of": "<stem id>", and the cut / scene / readable / density maths below
    # measure the GROUP, so a split graphic is held to exactly the numbers an unsplit one is
    by_id = {c['id']: c for c in cells}
    parts = set()
    for c in cells:
        p = c.get('part_of')
        if p is None: continue
        stem = by_id.get(p)
        if stem is None or p == c['id']:
            F_(f"{c['id']}: part_of {p!r} names no other graphic cell in this plan")
        elif stem.get('kind') != c.get('kind'):
            F_(f"{c['id']}: part_of {p!r} is a {stem.get('kind')} cell: the parts of one graphic share its kind")
        elif stem.get('part_of'):
            F_(f"{c['id']}: part_of {p!r} is itself a part: every part names the STEM cell")
        else:
            parts.add(c['id'])
    groups = {}
    for c in cells:
        groups.setdefault(c['part_of'] if c['id'] in parts else c['id'], []).append(c)
    for g in groups.values():
        g.sort(key=lambda x: float(x.get('start') or 0))
    inner = set()   # a split graphic's INTERNAL seams: not outer boundaries, so the cut gate skips them
    for g in groups.values():
        for i, c in enumerate(g):
            if i: inner.add((c['id'], 'start'))
            if i < len(g) - 1: inner.add((c['id'], 'end'))
        for a1, b1 in zip(g, g[1:]):
            d = float(b1.get('start') or 0) - float(a1.get('end') or 0)
            if abs(d) > 0.5 * F:
                F_(f"{b1['id']}: part starts {d / F:+.2f} frames from the end of {a1['id']} ({float(a1.get('end') or 0):.5f}): "
                   f"the parts of one graphic butt-join (the shot underneath flashes for those frames)")
    for c in cells:
        gid = c['id']
        for k in ('kind', 'region', 'content', 'start', 'end'):
            if k not in c: F_(f'{gid}: missing {k}')
        if LONG and c.get('kind') in FULL_KINDS and c.get('bg') not in ('dark', 'light'):
            F_(f'{gid}: full-screen without "bg": dark is the default CHOICE, write it — the locked render flags follow the field (bg-dark = STEP_FPS=12 + the glow pass; creative-moves.md move 2)')
        if 'start' in c and 'end' in c and float(c['end']) <= float(c['start']): F_(f'{gid}: end <= start')
        if c.get('region') in ('callout-L', 'callout-R'):
            hd = c.get('head')
            if not (isinstance(hd, dict) and 'left' in hd and 'right' in hd and 'frame' in hd):
                F_(f"{gid}: side callout without a measured head: run chin-line.py --edl over its window and record head {{left, right, frame}} (preset § SIDE CALLOUTS)")
        copy = c.get('copy') or ''
        if not copy and c.get('kind') not in ('screen-rec', 'screenshot', 'b-roll', 'enacting-overlay', 'annotation', 'captions'):
            W_(f'{gid}: no copy on a {c.get("kind")} cell (fine only if the graphic has no words)')
        artifact = c.get('source_artifact')
        if artifact:
            source = (job / str(artifact)).resolve()
            if job not in source.parents:
                F_(f'{gid}: source_artifact {artifact!r} is outside the job folder (job-relative paths only)')
            elif not source.is_file():
                F_(f'{gid}: source_artifact file missing: {artifact}')
            elif copy.strip() != source.read_text(encoding='utf-8').strip():
                F_(f'{gid}: copy differs from the complete source_artifact (preserve punctuation and case)')
        else:
            if c.get('readable') and copy and not c.get('asset') and not c.get('capture'):
                F_(f'{gid}: readable copy with no source_artifact: a readable cell IS the written thing — name the '
                   f'job-relative file it is copied from and make copy that file in full')
            if '—' in copy:
                F_(f'{gid}: em dash in authored copy {copy!r}; verbatim artifacts need source_artifact')
        if c.get('kind') in TEXT_KINDS and c.get('entrance') in ('pop', 'punch'):
            F_(f"{gid}: entrance {c['entrance']!r} on a text animation: type never pops (animations.md § TEXT NEVER POPS); rise (default) or slam")
        kind = c.get('kind')
        # anchor: the first word of the copy is spoken at start + LEAD
        if kind in TEXT_KINDS and words and copy:
            cw = [norm(w) for w in re.sub(r'[*~]', '', copy).split() if norm(w)]
            if cw:
                near = [w for w in words if abs(w['start'] - LEAD - float(c['start'])) <= 0.15 and norm(w['text']) == cw[0]]
                if not near:
                    cands = [w for w in words if norm(w['text']) == cw[0] and abs(w['start'] - float(c['start'])) < 3.0]
                    hint = f" ('{cw[0]}' is spoken at {', '.join(f'{w['start']:.2f}' for w in cands)}; start = word − {LEAD})" if cands else \
                           f" ('{cw[0]}' is not spoken within 3s of {float(c['start']):.2f})"
                    F_(f"{gid}: start {float(c['start']):.2f} does not anchor to the first word of its copy{hint}")
            # duration: a text animation is a few words in the low band; one over 8 s is an anchor that
            # matched the WRONG occurrence of its first word (g11 anchored to an 'ever' 36 s early, 2026-09-04)
            if float(c['end']) - float(c['start']) > 8.0:
                F_(f"{gid}: text animation spans {float(c['end']) - float(c['start']):.1f}s, over 8s; the start probably anchored to an earlier occurrence of {cw[0]!r}")
            # lowercase-casual register
            first = re.sub(r'[*~"\'(]', '', copy.split()[0]) if copy.split() else ''
            if first[:1].isupper() and first.lower() not in proper and not first.isupper():
                W_(f"{gid}: text animation starts with a capital ({first!r}), captions keep the lowercase-casual register unless it is a name")
        # cut: a full-screen edge within 8 frames of a V1 cut sits ON it (off by one flashes the
        # other shot); an edge far from every cut is a cut back mid-take, which is a choice
        if (kind in FULL_KINDS or c.get('bg')) and cuts:
            for edge in ('start', 'end'):
                if (gid, edge) in inner: continue   # an internal seam of a split graphic, not an outer boundary
                t_ = float(c[edge])
                nearest = min(cuts, key=lambda x: abs(x - t_))
                if 1e-4 < abs(nearest - t_) <= 8 * F:
                    F_(f"{gid}: full-screen {edge} {t_:.4f} is {(t_ - nearest) / F:+.2f} frames off the V1 cut at {nearest:.5f}, "
                       f"set {edge} = {nearest:.5f} exactly (off by a frame flashes the other shot)")
        # a full-screen's cut-IN leads a spoken word by a hair (~1-3 frames): one that leads nothing is
        # anchored to the wrong word (the your-job hook was first computed off "shot," instead of "one")
        if (kind in FULL_KINDS or c.get('bg')) and words:
            st = float(c['start'])
            lead = [w for w in words if 0 <= w['start'] - st <= 0.12]
            on_cut = cuts and min(abs(st - x) for x in cuts) <= 1.5 * F
            if not lead and not on_cut:
                W_(f"{gid}: full-screen cut-in at {st:.3f} leads no spoken word within 120 ms and sits on no V1 cut; check which word it was meant to anchor")
        # a full-screen is a SCENE: phases (≥ 2 visual beats) + visuals (≥ 1 that is not type) stated in the cell
        # (creative-moves.md move 2 § A FULL-SCREEN IS A SCENE, you 2026-09-10: "more moving parts, more visuals")
        if LONG and (kind in FULL_KINDS or c.get('bg')) and gid not in parts:   # once per graphic, on the stem cell
            ph = c.get('phases'); vs = c.get('visuals')
            if not (isinstance(ph, list) and len(ph) >= 2 and all(isinstance(x, dict) and 'at' in x and 'what' in x for x in ph)):
                F_(f'{gid}: a full-screen needs "phases": [{{at, what}}, …] with at least 2 visual beats (a scene arriving/leaving, a rack focus, a reveal): it is a SCENE, not a card (creative-moves.md move 2 § A FULL-SCREEN IS A SCENE)')
            if not (isinstance(vs, list) and len(vs) >= 1):
                F_(f'{gid}: a full-screen needs "visuals": [...] naming at least one element that is not type (a picture, artifact, prop, diagram, UI) (creative-moves.md move 2 § A FULL-SCREEN IS A SCENE)')
        # readable hold — the whole graphic's span, so a split graphic is measured across its parts
        if c.get('readable') and gid not in parts:
            g_ = groups[gid]
            hold = float(g_[-1]['end']) - float(g_[0]['start'])
            if hold < 3.0:
                F_(f"{gid}: readable graphic holds {hold:.2f}s, needs ≥ 3.0s (2s complete-content hold + reveal), or less text")
        elif kind in ('quote', 'comment', 'screenshot') and 'readable' not in c:
            W_(f"{gid}: a {kind} cell with no \"readable\" flag, if the viewer is meant to read it, flag it and size the slot")
        # capture: a screen-rec / screenshot cell names its file or says what the build records
        if kind in ('screen-rec', 'screenshot'):
            cap, asset = c.get('capture'), c.get('asset')
            if not asset and not cap:
                F_(f'{gid}: a {kind} cell needs "asset" (a file already in the job folder) or "capture" {{source, target, action, seconds | still}}: the build records it, it never guesses (graphics-plan § THE CAPTURE GATE)')
            if asset:
                ap = (job / str(asset)).resolve()
                if job not in ap.parents: F_(f'{gid}: asset {asset!r} is outside the job folder (job-relative paths only)')
                elif not ap.exists(): F_(f'{gid}: asset {asset!r} not found under the job folder')
            if cap is not None:
                if not isinstance(cap, dict): cap = {}
                if not cap.get('target'):
                    F_(f'{gid}: "capture" needs a target (an app name or a URL)')
                src = cap.get('source')
                if src not in ('url', 'app'):
                    F_(f'{gid}: "capture" needs "source": "url" (page-record.mjs, headless) or "app" (screen-record.sh / window-grab.sh): the build routes on it')
                elif src == 'url' and not re.match(r'https?://', str(cap.get('target') or '')):
                    F_(f'{gid}: a "url" capture needs an http(s) target, got {cap.get("target")!r}')
                if kind == 'screen-rec' and cap.get('still'):
                    F_(f'{gid}: "still" on a screen-rec cell: a still is a screenshot cell (kind "screenshot"), a recording needs "seconds"')
                if kind == 'screen-rec' and not _num(cap.get('seconds')) > 0:
                    F_(f'{gid}: a screen-rec capture needs "seconds" (a number > 0), how long the take runs')
                if not cap.get('action'):
                    W_(f'{gid}: capture has no "action": say what is on screen / what happens during the take, or the build guesses the state')
    # the caption layer (short-form, kind "captions") spans the whole cut on its own track: it is not an
    # event, so it stays out of the overlap, anti-stale and density maths below
    cells = [c for c in cells if c.get('kind') != 'captions']
    # overlaps between non-text cells (V4 exists, but a collision is a choice to state)
    ov = [c for c in cells if c.get('kind') not in TEXT_KINDS]
    for i, a1 in enumerate(ov):
        for b1 in ov[i + 1:]:
            if float(a1['start']) < float(b1['end']) and float(b1['start']) < float(a1['end']):
                W_(f"{a1['id']} and {b1['id']} overlap on the timeline ({max(float(a1['start']), float(b1['start'])):.2f} → "
                   f"{min(float(a1['end']), float(b1['end'])):.2f}): the second goes to V4; say so in content")
    # anti-stale: same template twice in a row (text animations exempt)
    seq = [c for c in sorted(cells, key=lambda c: float(c['start'])) if c.get('kind') not in TEXT_KINDS]
    for a1, b1 in zip(seq, seq[1:]):
        # a punch-cut on the OTHER field is a different look (dark ≠ light: the other field reads as a different look), so the pair is (template, bg)
        if a1.get('template') and (a1.get('template'), a1.get('bg')) == (b1.get('template'), b1.get('bg')):
            W_(f"{b1['id']}: same template as the previous graphic {a1['id']} ({a1['template']}{' on ' + a1['bg'] if a1.get('bg') else ''}), the anti-stale law")
    # density block — a split graphic counts ONCE, over its whole span: its parts are a build mechanic
    ev = []
    for c in cells:
        if c['id'] in parts: continue
        g_ = [x for x in groups[c['id']] if x.get('kind') != 'captions']
        ev.append(dict(c, start=float(g_[0]['start']), end=float(g_[-1]['end'])) if len(g_) > 1 else c)
    dur = float(plan.get('duration') or max(float(c['end']) for c in ev))
    n = len(ev); per_min = n / (dur / 60)
    texts = sum(1 for c in ev if c.get('kind') in TEXT_KINDS)
    fulls = [c for c in ev if c.get('kind') in FULL_KINDS or c.get('bg')]
    full_s = sum(float(c['end']) - float(c['start']) for c in fulls)
    push = sum(1 for c in ev if c.get('push_in'))
    bare, prev = 0.0, 0.0
    for c in sorted(ev, key=lambda c: float(c['start'])):
        bare = max(bare, float(c['start']) - prev); prev = max(prev, float(c['end']))
    bare = max(bare, dur - prev)
    print(f"density: {n} events / {dur:.1f}s = {per_min:.1f}/min (11-13) · text animations {texts} ({texts / (dur / 60):.1f}/min, 6-7) · "
          f"full-screens {len(fulls)} = {full_s:.1f}s = {100 * full_s / dur:.1f}% (25% decorative guideline; demonstrations may exceed) · push-ins {push} ({push / (dur / 60):.1f}/min, 2-3) · "
          f"longest bare {bare:.1f}s (≤6)")
    if per_min < 10.5: W_(f'density {per_min:.1f}/min is under the look (11-13)')
    if bare > 6.0: W_(f'longest bare stretch {bare:.1f}s > 6s')
    if 100 * full_s / dur > 25: W_(f'full-screens are {100 * full_s / dur:.1f}% of runtime (> 25% decorative guideline): review coverage; retain required prompt/capture demonstrations for their whole explanation and record the reason in content')
    # spread: never more than 40 s of runtime without a full-screen (creative-moves § THE DENSITY NUMBERS, SPREAD;
    # your-job shipped 3 in its first 41 s and none in the last 95, 2026-09-10)
    fs = sorted(fulls, key=lambda c: float(c['start'])) if LONG else []
    if fs:
        gaps = [(float(fs[0]['start']), f"0 → {fs[0]['id']}")] + \
               [(float(b['start']) - float(a['end']), f"{a['id']} → {b['id']}") for a, b in zip(fs, fs[1:])] + \
               [(dur - float(fs[-1]['end']), f"{fs[-1]['id']} → end")]
        g, where = max(gaps)
        if g > 40: W_(f'full-screens are not spread: {g:.0f}s of runtime without one ({where}); ≤ 40 s (creative-moves.md § THE DENSITY NUMBERS, SPREAD)')
        if len(fs) / (dur / 60) < 2: W_(f'full-screens {len(fs) / (dur / 60):.1f}/min under the look (2-3)')
    elif LONG:
        W_('no full-screen graphic at all (2-3/min, spread ≤ 40 s apart)')
    for w in warns: print(f'  warn {w}')
    for f in fails: print(f'  FAIL {f}')
    print(f"{len(fails)} FAIL · {len(warns)} warn · {n} graphics · fps {fps:.3f}")
    if fails: sys.exit(1)


if __name__ == '__main__':
    main()
