"""planlib.py: helpers for a reaction job's build_plan.py (Seq 37/38 onward): word anchors on the TIGHTENED timeline,
the caption word list (transcript/seqwords.json, each word tagged with its A1 clip), and per-beat face x for face-only.

  W = Words(job)            ; W.at("phrase", after=t) -> start of the phrase's first word ; W.end("phrase", after=t) -> end of its last
  check(plan_path)          ; the plan checker (= overlays.py <plan> --check): (errors, warnings), after --captions
"""
import json, os, re, subprocess

norm = lambda s: re.sub(r"[^a-z0-9']", "", s.lower())


class Words:
    def __init__(self, job):
        self.job = job
        self.w = json.load(open(os.path.join(job, "transcript", "words.tight.json"), encoding="utf-8"))["clips"][0]["words"]

    def _find(self, phrase, after):
        toks = [norm(t) for t in phrase.split() if norm(t)]
        for i in range(len(self.w) - len(toks) + 1):
            if self.w[i]["start"] < after - 1e-6: continue
            if all(norm(self.w[i + k]["w"]) == toks[k] for k in range(len(toks))): return i, i + len(toks) - 1
        raise SystemExit(f"anchor not found after {after}: {phrase!r}")

    def at(self, phrase, after=0.0):
        i, _ = self._find(phrase, after); return round(self.w[i]["start"], 3)

    def end(self, phrase, after=0.0):
        _, j = self._find(phrase, after); return round(self.w[j]["end"], 3)

    def span(self, first, last, after=0.0, pad=0.1):
        """a reviewed-video range: from just after the word BEFORE `first` to just before the word AFTER `last` (WhisperX starts a
        word late after a pause, so the sample's own first-word start runs late; the neighbouring words of Affan are the edges)"""
        i, _ = self._find(first, after); _, j = self._find(last, self.w[i]["start"])
        a = self.w[i - 1]["end"] + pad if i > 0 else self.w[i]["start"]
        b = self.w[j + 1]["start"] - pad if j + 1 < len(self.w) else self.w[j]["end"] + 0.3
        return [round(a, 3), round(b, 3)]


def seqwords(job, dump_path, seq_name):
    """transcript/seqwords.json for overlays.py captions: [{w, start, end, clip}] on the tightened timeline"""
    seq = next(s for s in json.load(open(dump_path, encoding="utf-8")) if s["name"] == seq_name)
    a1 = seq["a"][0]["clips"]
    out = []
    for x in json.load(open(os.path.join(job, "transcript", "words.tight.json"), encoding="utf-8"))["clips"][0]["words"]:
        m = (x["start"] + x["end"]) / 2
        k = next((i for i, c in enumerate(a1) if c["s"] - 1e-3 <= m < c["e"] + 1e-3), None)
        if k is None: continue
        out.append(dict(w=x["w"], start=x["start"], end=x["end"], clip=k))
    json.dump(out, open(os.path.join(job, "transcript", "seqwords.json"), "w", encoding="utf-8"), indent=0, ensure_ascii=False)
    return len(out)


def check(plan_path, out=print):
    """the plan checker (overlays.py --check): run it after `overlays.py <plan> --captions`; returns (errors, warnings).
    A build_plan.py can end with `e, w = check(os.path.join(HERE, "plan.json")); if e: raise SystemExit(...)`."""
    import overlays as O
    plan, seq = O.load(plan_path)
    return O.check(plan, seq, out=out)
