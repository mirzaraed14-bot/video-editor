#!/usr/bin/env python3
# /// script
# dependencies = ["pillow>=10.1", "fonttools"]
# ///
"""
@affanwizu Roman Urdu caption builder  (LOCKED LOOK: presets/instagram/affanwizu/deep-talks-style.md)

Captions ONLY. The creator hands over a FINISHED cut (their clip selection, their order, their
title); this builder never cuts, trims or reframes it. It lays one line of Roman Urdu at a time,
each switching on the first word of its phrase and holding until the next, measured off the
creator's own export (balcony.mov, 2026-09-18).

Three inputs, all in the job folder:
  raw/<cut>.mp4|mov          the finished cut, captions NOT burned in
  transcript/words.json      transcribe.sh <job> --lang ur   (Urdu script, word timings)
  captions.txt               the Roman Urdu lines, written by Claude from the draft (see PLAYBOOK.md)

Usage:
  uv run presets/instagram/affanwizu/build.py <job> --prep          # writes captions.draft.txt (Urdu, auto-phrased)
  uv run presets/instagram/affanwizu/build.py <job>                 # burn → outputs/<job>.captioned.mp4
  uv run presets/instagram/affanwizu/build.py <job> --alpha         # transparent ProRes 4444 caption layer
  options: --title "never insult the little ones"   --until SECONDS   --out PATH
           --style yellow|white   (yellow = deep-talks-style.md, the default; white = white-style.md)
           --y 1140               caption baseline for THIS reel (the creator places it per reel, under the chin)

Engine = PIL + ffmpeg overlay (this ffmpeg has no drawtext/libass). PIL's basic layout does NOT
apply GPOS kerning, and Ubuntu only kerns through GPOS, so the kerning is read with fontTools and
each glyph is placed by hand: without it "kaha" sat 3-7 px off the reference.
"""
import argparse, json, os, platform, re, subprocess, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from fontTools.ttLib import TTFont

for _s in (sys.stdout, sys.stderr):
    try:
        _s.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

# ---------------------------------------------------------------- the look (LOCKED, measured)
W, H = 1080, 1920
FONT_FILE   = "Ubuntu-Light.ttf"         # Google font; installed in C:\Windows\Fonts on this machine
SHEAR       = 0.18                       # FAUX italic: the editor's italic button slants Ubuntu LIGHT ~10 deg.
                                         # The true Ubuntu-Italic has different glyph widths ("kaha" +6 px): fit
                                         # over all 43 reference lines, Light+0.18 IoU 0.725 vs true Italic 0.42
FONT_DIRS   = [os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "assets", "fonts"),
               r"C:\Windows\Fonts", os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts"),
               "/Library/Fonts", os.path.expanduser("~/Library/Fonts"), "/usr/share/fonts/truetype/ubuntu"]
SIZE        = 48                         # px at 1080 wide (word positions within 1-2 px of the reference)
FILL        = (255, 215, 0, 255)         # #FFD700; reads (246,210,0) after the h264 yuv420 export
CAP_BASE_Y  = 1178                       # caption baseline (ascenders top out at y1141)
TITLE_BASE_Y = 332                       # title baseline, same font/size/colour (the creator's own, optional)
SHADOW_DX, SHADOW_DY = 3.75, 4.25        # hard black drop shadow, down-right; fitted on 82 frame pairs
SHADOW_BLUR = 1.0                        # gaussian sigma, px  (err 3.99 vs 6.10 with no shadow; a flat
SHADOW_OPACITY = 1.0                     # optimum across dx 3.5-4 / dy 4-4.5, so the middle is taken)

# phrasing (auto draft only; the final lines are captions.txt)
MAX_CHARS   = 32                         # longest reference line was 38 chars / 795 px
MAX_WORDS   = 6
PAUSE_BREAK = 0.28                       # a gap this long between words starts a new line
TAIL_HOLD   = 0.40                       # last line lingers after the final word (clamped to the cut)

SHADOW_SPREAD = 0                        # px the ink is grown before the shadow blur (Premiere's shadow "Size")

# the WHITE style (white-style.md), measured 2026-09-18 off oushi/petrol/Rain/SAFAI and read out of the
# creator's own Premiere project ABW6 (the text layers name the font: Tahoma, 48). Glyph IoU 0.82-0.83
# at dx 0 / dy 0 on 12 held lines; shadow fitted on 26 switch pairs with no jump cut under them.
STYLES = {
    "yellow": {},                        # the module defaults above (deep-talks-style.md, LOCKED)
    "white": dict(FONT_FILE="tahoma.ttf", SHEAR=0.0, SIZE=48, FILL=(255, 255, 255, 255),
                  CAP_BASE_Y=1140, TITLE_BASE_Y=261,
                  SHADOW_DX=4.0, SHADOW_DY=3.0, SHADOW_BLUR=2.0, SHADOW_SPREAD=1, SHADOW_OPACITY=0.95),
}


def apply_style(name):
    if name not in STYLES:
        sys.exit(f"[affanwizu] unknown --style {name!r}; pick one of {', '.join(STYLES)}")
    globals().update(STYLES[name])

SCALE_KEYS = ("W", "H", "SIZE", "CAP_BASE_Y", "TITLE_BASE_Y", "SHADOW_DX", "SHADOW_DY", "SHADOW_BLUR", "SHADOW_SPREAD")


def apply_scale(s):
    if abs(s - 1.0) < 1e-6:
        return
    g = globals()
    for k in SCALE_KEYS:
        g[k] = g[k] * s if isinstance(g[k], float) else int(round(g[k] * s))


def font_path():
    for d in FONT_DIRS:
        p = os.path.join(d, FONT_FILE)
        if os.path.exists(p):
            return p
    sys.exit(f"[affanwizu] {FONT_FILE} not found. Install the Ubuntu font family (fonts.google.com/specimen/Ubuntu) "
             f"or drop {FONT_FILE} into assets/fonts/.")


# ---------------------------------------------------------------- kerning (GPOS pair adjustment)
class Kerner:
    def __init__(self, path):
        f = TTFont(path)
        self.upem = f["head"].unitsPerEm
        self.cmap = f.getBestCmap()
        self.hmtx = f["hmtx"].metrics
        self.lookups = []
        gpos = f["GPOS"].table
        kern_idx = {i for fr in gpos.FeatureList.FeatureRecord if fr.FeatureTag == "kern"
                    for i in fr.Feature.LookupListIndex}
        for i in sorted(kern_idx):
            lk = gpos.LookupList.Lookup[i]
            subs = [st.ExtSubTable if lk.LookupType == 9 else st for st in lk.SubTable]
            self.lookups.append([st for st in subs if getattr(st, "LookupType", 2) == 2])

    def glyph(self, ch):
        return self.cmap.get(ord(ch))

    def advance(self, g):
        return self.hmtx[g][0] if g in self.hmtx else 0

    def pair(self, a, b):
        total = 0
        for subs in self.lookups:
            for st in subs:
                cov = st.Coverage.glyphs
                if a not in cov:
                    continue
                if st.Format == 1:
                    ps = st.PairSet[cov.index(a)]
                    hit = next((r for r in ps.PairValueRecord if r.SecondGlyph == b), None)
                    if hit is None:
                        continue
                    total += getattr(hit.Value1, "XAdvance", 0) or 0
                else:
                    c1 = st.ClassDef1.classDefs.get(a, 0)
                    c2 = st.ClassDef2.classDefs.get(b, 0)
                    total += getattr(st.Class1Record[c1].Class2Record[c2].Value1, "XAdvance", 0) or 0
                break                     # first matching subtable wins within a lookup
        return total


# ---------------------------------------------------------------- rendering
def layout(text, kerner, size):
    """[(char, x)] in px from the pen origin, plus the total advance."""
    k = size / kerner.upem
    out, x, prev = [], 0.0, None
    for ch in text:
        g = kerner.glyph(ch)
        if prev is not None and g is not None:
            x += kerner.pair(prev, g) * k
        out.append((ch, x))
        x += kerner.advance(g) * k if g else 0
        prev = g
    return out, x


def render_line(text, font, kerner, base_y):
    """Full-canvas RGBA of one line (centred on its advance width, like the reference), cropped."""
    glyphs, adv = layout(text, kerner, font.size)
    x0 = W / 2 - adv / 2
    ink = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(ink)
    for ch, x in glyphs:
        if not ch.isspace():
            d.text((x0 + x, base_y), ch, font=font, fill=255, anchor="ls")
    # slant around the baseline (x' = x + SHEAR * (base_y - y)), the way an editor fakes italic
    ink = ink.transform(ink.size, Image.AFFINE, (1, SHEAR, -SHEAR * base_y, 0, 1, 0), resample=Image.BICUBIC)
    # shadow = the ink, shifted (sub-pixel, via an affine) and softened, under the fill
    grown = ink.filter(ImageFilter.MaxFilter(2 * SHADOW_SPREAD + 1)) if SHADOW_SPREAD else ink
    sh = grown.transform(ink.size, Image.AFFINE, (1, 0, -SHADOW_DX, 0, 1, -SHADOW_DY), resample=Image.BILINEAR)
    sh = sh.filter(ImageFilter.GaussianBlur(SHADOW_BLUR)).point(lambda v: int(v * SHADOW_OPACITY))
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    img.putalpha(sh)
    fill = Image.new("RGBA", (W, H), FILL)
    fill.putalpha(ink)
    img.alpha_composite(fill)
    bb = img.getbbox()
    if not bb:
        return img, 0, 0
    l, t, r, b = max(0, bb[0] - 2), max(0, bb[1] - 2), min(W, bb[2] + 2), min(H, bb[3] + 2)
    return img.crop((l, t, r, b)), l, t


# ---------------------------------------------------------------- inputs
def load_words(job_dir):
    p = os.path.join(job_dir, "transcript", "words.json")
    if not os.path.exists(p):
        sys.exit(f"[affanwizu] missing {p}: run .claude/skills/rough-cut/scripts/transcribe.sh {job_dir} --lang ur")
    clips = json.load(open(p, encoding="utf-8"))["clips"]
    if len(clips) != 1:
        sys.exit(f"[affanwizu] expected ONE finished cut in raw/, found {len(clips)} clips in words.json")
    return clips[0]


def source_video(job_dir):
    raw = os.path.join(job_dir, "raw")
    vids = sorted(f for f in os.listdir(raw) if f.lower().endswith((".mp4", ".mov", ".m4v", ".mkv")))
    if len(vids) != 1:
        sys.exit(f"[affanwizu] raw/ must hold exactly one finished cut, found {vids}")
    return os.path.join(raw, vids[0])


def probe(video):
    out = json.loads(subprocess.check_output(
        ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
         "stream=width,height,r_frame_rate:format=duration", "-of", "json", video]).decode())
    st = out["streams"][0]
    num, den = (st["r_frame_rate"].split("/") + ["1"])[:2]
    return int(st["width"]), int(st["height"]), st["r_frame_rate"], float(num) / float(den), float(out["format"]["duration"])


LINE_RE = re.compile(r"^\s*(@?[0-9.]+)\s*\|\s*(.*?)\s*$")


def load_lines(job_dir, words):
    p = os.path.join(job_dir, "captions.txt")
    if not os.path.exists(p):
        sys.exit(f"[affanwizu] missing {p}: run --prep, then write the Roman Urdu lines (PLAYBOOK.md)")
    lines = []
    for n, raw in enumerate(open(p, encoding="utf-8"), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        m = LINE_RE.match(raw)
        if not m:
            sys.exit(f"[affanwizu] captions.txt line {n} is not '<word#> | text' or '@<seconds> | text': {raw.rstrip()}")
        key, text = m.groups()
        start = float(key[1:]) if key.startswith("@") else words[int(key)]["start"]
        lines.append({"start": start, "text": text, "key": key})
    lines.sort(key=lambda l: l["start"])
    return lines


# ---------------------------------------------------------------- --prep: the auto-phrased Urdu draft
def prep(job_dir, words):
    groups, cur = [], []
    for i, w in enumerate(words):
        if cur:
            gap = w["start"] - words[cur[-1]]["end"]
            chars = len(" ".join(words[j]["w"] for j in cur + [i]))
            if gap >= PAUSE_BREAK or len(cur) >= MAX_WORDS or chars > MAX_CHARS or words[cur[-1]]["w"].endswith(("۔", "؟", ".", "?")):
                groups.append(cur); cur = []
        cur.append(i)
    if cur:
        groups.append(cur)
    out = os.path.join(job_dir, "captions.draft.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write("# AUTO DRAFT (Urdu script). Claude rewrites each line in Roman Urdu into captions.txt,\n"
                "# keeping the <word#> that starts the line. Spelling: roman-urdu.md. Low-confidence words marked ?\n")
        for g in groups:
            ws = " ".join(words[j]["w"] + ("?" if words[j].get("prob", 1) < 0.5 else "") for j in g)
            f.write(f"{g[0]:>4} | {ws}    # {words[g[0]]['start']:.2f}s\n")
    print(f"[affanwizu] {len(groups)} draft lines → {out}")


# ---------------------------------------------------------------- build
def build(job_dir, out_path, alpha, until, title, srt_path=None, dur_override=None):
    clip = load_words(job_dir)
    words = clip["words"]
    src = source_video(job_dir)
    vw, vh, rate, fps, dur = probe(src)
    if dur_override:
        dur = dur_override                   # the Premiere sequence's own length (it can differ from the reference by a frame)
    if abs(vw / vh - 9 / 16) > 0.01:
        sys.exit(f"[affanwizu] the cut is {vw}x{vh}; this look is authored for a 9:16 frame")
    apply_scale(vw / 1080.0)

    lines = load_lines(job_dir, words)
    snap = lambda t: round(t * fps) / fps
    for i, ln in enumerate(lines):
        ln["start"] = 0.0 if i == 0 else snap(ln["start"])        # the reference is captioned from frame 0
    for i in range(len(lines) - 1):
        lines[i]["end"] = lines[i + 1]["start"]                    # hold until the next line: never a gap
    if lines:
        spoken = words[-1]["end"] if words else 0.0
        # an '@<sec>' last line placed past the transcript's last word (Whisper dropped the ending: Seq 17)
        # holds to the end of the cut, as every one of the creator's own reels does
        lines[-1]["end"] = dur if lines[-1]["start"] >= spoken else min(dur, snap(spoken + TAIL_HOLD))
    tcap = min(until, dur) if until else dur
    lines = [l for l in lines if l["start"] < tcap]
    if srt_path:
        # an EDITABLE caption track for Premiere (drag the .srt onto the timeline): no render, the creator
        # fixes spellings in the Text panel. The look comes from the Premiere caption track style
        # (white-style.md / deep-talks-style.md § Premiere caption track).
        ts = lambda t: f"{int(t // 3600):02d}:{int(t % 3600 // 60):02d}:{int(t % 60):02d},{int(round(t % 1 * 1000)) % 1000:03d}"
        with open(srt_path, "w", encoding="utf-8") as f:
            n = 0
            for ln in lines:
                if not ln["text"]:
                    continue
                n += 1
                f.write(f"{n}\n{ts(ln['start'])} --> {ts(min(ln['end'], tcap))}\n{ln['text']}\n\n")
        print(f"[affanwizu] SRT {n} captions, {tcap:.2f}s → {srt_path}")
        for ln in lines:
            print(f"  {ln['start']:6.2f}-{ln['end']:6.2f}  {ln['text']}")
        return

    fp = font_path()
    font = ImageFont.truetype(fp, SIZE)
    kerner = Kerner(fp)
    work = os.path.join(job_dir, "hf-graphics", "captions", "png")
    os.makedirs(work, exist_ok=True)
    for f in os.listdir(work):
        if f.endswith(".png"):
            os.remove(os.path.join(work, f))

    overlays = []
    if title:
        img, x, y = render_line(title, font, kerner, TITLE_BASE_Y)
        p = os.path.join(work, "title.png"); img.save(p)
        overlays.append((p, x, y, 0.0, tcap))
    for i, ln in enumerate(lines):
        if not ln["text"]:
            continue                      # an empty line ('@35.72 |') = no caption from here to the next line (a gap in the cut)
        img, x, y = render_line(ln["text"], font, kerner, CAP_BASE_Y)
        p = os.path.join(work, f"cap_{i:03d}.png"); img.save(p)
        overlays.append((p, x, y, ln["start"], min(ln["end"], tcap)))

    cmd = ["ffmpeg", "-nostdin", "-hide_banner", "-loglevel", "error", "-y"]
    if alpha:
        cmd += ["-f", "lavfi", "-i", f"color=c=black@0.0:s={W}x{H}:r={rate}:d={tcap:.3f},format=rgba"]
    else:
        cmd += ["-i", src]
    for ov in overlays:
        cmd += ["-loop", "1", "-i", ov[0]]
    # Colour: the creator exports BT.709 (tv range). ffmpeg's implicit RGB->YUV is BT.601, which lands
    # #FFD700 visibly off on a phone, so every PNG is converted with the 709 matrix BEFORE the overlay
    # and the footage itself is never converted (burn) / the layer is tagged 709 (alpha).
    to709 = "scale=out_color_matrix=bt709:out_range=tv"
    fc, last = [], "0:v"
    for idx, (_, x, y, s, e) in enumerate(overlays, start=1):
        if not alpha:
            fc.append(f"[{idx}:v]format=rgba,{to709},format=yuva420p[o{idx}]")
        src_pad = f"o{idx}" if not alpha else f"{idx}:v"
        # [s, e) on the frame grid: a frame at exactly e belongs to the NEXT line
        fc.append(f"[{last}][{src_pad}]overlay={x}:{y}:enable='gte(t,{s - 0.5 / fps:.4f})*lt(t,{e - 0.5 / fps:.4f})'[v{idx}]")
        last = f"v{idx}"
    if alpha:
        fc.append(f"[{last}]{to709},format=yuva444p10le[vout]")
        last = "vout"
    tags = ["-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709", "-color_range", "tv"]
    cmd += ["-filter_complex", ";".join(fc), "-map", f"[{last}]", "-t", f"{tcap:.3f}"]
    if alpha:
        cmd += ["-c:v", "prores_ks", "-profile:v", "4444", "-pix_fmt", "yuva444p10le", *tags, "-an", out_path]
    else:
        venc = (["-c:v", "h264_videotoolbox", "-b:v", "25M"] if platform.system() == "Darwin"
                else ["-c:v", "libx264", "-preset", "medium", "-crf", "16", "-pix_fmt", "yuv420p"])
        cmd += ["-map", "0:a?", *venc, *tags, "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", out_path]
    print(f"[affanwizu] {'ALPHA layer' if alpha else 'burn'} {W}x{H} @ {rate}  lines={len(lines)}  dur={tcap:.2f}s → {out_path}")
    subprocess.run(cmd, check=True)
    for ln in lines:
        print(f"  {ln['start']:6.2f}-{ln['end']:6.2f}  {ln['text']}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("job_dir")
    ap.add_argument("--prep", action="store_true", help="write captions.draft.txt (auto-phrased Urdu) and stop")
    ap.add_argument("--alpha", action="store_true", help="transparent ProRes 4444 caption layer instead of a burn")
    ap.add_argument("--title", default="", help="optional top title in the same style (off by default: the creator's own)")
    ap.add_argument("--until", type=float, default=None, help="preview length cap (seconds)")
    ap.add_argument("--out", default=None)
    ap.add_argument("--style", default="yellow", choices=sorted(STYLES),
                    help="yellow = aesthetic deep talks (default); white = Tahoma, mixed case")
    ap.add_argument("--srt", action="store_true", help="write an editable .srt caption track for Premiere instead of rendering")
    ap.add_argument("--dur", type=float, default=None, help="caption track length (the sequence end, seconds)")
    ap.add_argument("--y", type=int, default=None,
                    help="caption baseline in 1080x1920 px. The creator places it per reel: chin + ~115 px "
                         "(workflows/chin-line.py median_chin; 5 of 11 reference reels within 12 px)")
    a = ap.parse_args()
    apply_style(a.style)
    if a.y is not None:
        CAP_BASE_Y = a.y
    job = os.path.abspath(a.job_dir)
    name = os.path.basename(job)
    if a.prep:
        prep(job, load_words(job)["words"])
        sys.exit(0)
    out = a.out or (os.path.join(job, f"{name}.srt") if a.srt else
                    os.path.join(job, "hf-graphics", "captions", "renders", "captions-alpha.mov") if a.alpha
                    else os.path.join(job, "outputs", f"{name}.captioned.mp4"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    build(job, out, a.alpha, a.until, a.title, srt_path=out if a.srt else None, dur_override=a.dur)
