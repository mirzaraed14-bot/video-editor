"""prproj-seq.py: read one sequence's edit straight out of a Premiere .prproj (gzip XML), no Premiere needed.

  python workflows/prproj-seq.py <file.prproj | --latest NAME> "<Sequence name>" [--edl OUT.json --offset S --clip FILE]

--latest NAME   newest autosave whose file name starts with NAME (e.g. ABW10) under E:/Premiere Pro Exports (any depth)
Prints every video and audio track item: timeline start-end, source in-out (seconds, 254016000000 ticks/s), clip name.
Affan's convention (client Shorts, 2026-10-15): V1 = the cut, V2 = a full-screen overlay slot, V3 = a split slot.
--edl writes the CUT as segments from audio track 1 (contiguous source pieces merged), shifted by --offset (file t = source t
- offset) onto --clip, the cuts.json shape splice.sh reads. Used on fubu-50-shirts: reproduces work/cut/affan-seq02.txt.
"""
import argparse, glob, gzip, json, os, sys
import xml.etree.ElementTree as ET

TPS = 254016000000


def latest(name):
    hits = glob.glob("E:/Premiere Pro Exports/**/" + name + "*.prproj", recursive=True) + glob.glob("E:/Premiere Pro Exports/**/" + name, recursive=True)
    if not hits:
        sys.exit(f"prproj-seq: no {name}*.prproj under E:/Premiere Pro Exports")
    return max(hits, key=os.path.getmtime)


def read(path, seq):
    raw = open(path, "rb").read()
    root = ET.fromstring(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)
    byid = {e.get("ObjectID"): e for e in root if e.get("ObjectID")}
    byuid = {e.get("ObjectUID"): e for e in root if e.get("ObjectUID")}
    ref = lambda el: None if el is None else byid.get(el.get("ObjectRef")) if el.get("ObjectRef") else byuid.get(el.get("ObjectURef"))
    T = lambda x: int(x) / TPS if x not in (None, "") else None
    sq = next((e for e in root if e.tag == "Sequence" and e.findtext("Name") == seq), None)
    if sq is None:
        sys.exit(f"prproj-seq: no sequence named {seq!r} (have: {sorted({e.findtext('Name') for e in root if e.tag == 'Sequence'})})")
    tracks = {"video": [], "audio": []}
    for tg in sq.iter("TrackGroup"):
        g = ref(tg.find("Second"))
        if g is None:
            continue
        kind = "video" if g.tag.startswith("Video") else "audio"
        for tr in g.iter("Track"):
            t = ref(tr)
            if t is None:
                continue
            items = []
            for ti in t.iter("TrackItem"):
                it = ref(ti)
                if it is None:
                    continue
                sc = ref(it.find(".//SubClip"))
                c = ref(sc.find("Clip")) if sc is not None else None
                items.append(dict(start=T(it.findtext(".//TrackItem/Start")) or 0.0, end=T(it.findtext(".//TrackItem/End")),
                                  src_in=T(c.findtext(".//Clip/InPoint")) if c is not None else None,
                                  src_out=T(c.findtext(".//Clip/OutPoint")) if c is not None else None,
                                  speed=c.findtext(".//Clip/PlaybackSpeed") if c is not None else None,
                                  name=sc.findtext("Name") if sc is not None else None))
            if items:
                tracks[kind].append(sorted(items, key=lambda x: x["start"]))
    return tracks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project"); ap.add_argument("sequence")
    ap.add_argument("--edl"); ap.add_argument("--offset", type=float, default=0.0); ap.add_argument("--clip")
    a = ap.parse_args()
    path = latest(a.project[len("--latest "):]) if a.project.startswith("--latest ") else a.project
    tr = read(path, a.sequence)
    print("project", path)
    for kind in ("video", "audio"):
        for i, items in enumerate(tr[kind]):
            print(f"{kind[0].upper()}{i + 1}: {len(items)} items")
            for x in items:
                sp = f" speed {x['speed']}" if x["speed"] not in (None, "1", "1.") else ""
                print(f"  {x['start']:8.3f}-{x['end']:8.3f} ({x['end'] - x['start']:6.3f})  src {x['src_in']:.3f}-{x['src_out']:.3f}{sp}  {(x['name'] or '')[:48]}")
    if a.edl:
        segs = []
        for x in tr["audio"][0]:
            if segs and abs(segs[-1][1] - x["src_in"]) < 1e-3:
                segs[-1][1] = x["src_out"]
            else:
                segs.append([x["src_in"], x["src_out"]])
        clip = a.clip or os.path.basename(tr["audio"][0][0]["name"] or "")
        json.dump({"segments": [dict(clip=clip, start=round(s - a.offset, 3), end=round(e - a.offset, 3)) for s, e in segs]},
                  open(a.edl, "w"), indent=1)
        print(f"edl: {len(segs)} segments, {sum(e - s for s, e in segs):.3f} s -> {a.edl}")


if __name__ == "__main__":
    main()
