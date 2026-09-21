# /// script
# requires-python = ">=3.9"
# dependencies = []
# ///
"""
take-map.py — find the retakes in a multi-take shoot.

THE PROBLEM: a creator reading a script re-records lines they fluff, so the raw holds
the same sentence two, three, five times. The rough-cut rule is "keep the LAST take",
but finding every take by reading thousands of transcript words is slow and unreliable.

HOW IT WORKS: speech is chunked into utterances at pauses. Every utterance is compared
with the ones that follow it inside a time window, using CONTAINMENT — how much of the
SHORTER utterance is matched inside the longer one. Containment, not plain similarity,
is what catches a false start, where a clipped fragment ("He didn't break into any-")
is swallowed whole by the complete take that follows. Utterances that chain together
become a TAKE GROUP, and in each group every take but the last is a kill candidate.

Deliberately NOT script-aligned. An earlier version matched utterances against the
written script, which failed on exactly the sentences that matter: the script spells
numbers out ("Twenty-one and a half million", "eleven thirty-seven") while the
transcriber writes digits ("21.5 million", "1137"), so the number-heavy lines — the
ones a creator most often re-records — scored lowest. Comparing takes against EACH
OTHER sidesteps that entirely, because both sides come from the same transcriber.

This tool REPORTS. It never edits. The editor reads the groups, checks the flagged
ones and writes cuts.json.

USAGE
  uv run workflows/take-map.py <job_dir>
  uv run workflows/take-map.py <job_dir> --md transcript/take-map.md --json transcript/take-map.json
"""
import argparse, json, os, re, sys
from difflib import SequenceMatcher

WORD = re.compile(r"[a-z0-9']+")
# tokens too common to prove two utterances are the same line
STOP = set("a an the and or but so to of in on at it is was for that this with as i "
           "you he she they we my your his her их be been are were do did not no".split())


def norm(s):
    return WORD.findall(s.lower().replace("’", "'"))


def content(tokens):
    return [t for t in tokens if t not in STOP]


def load_words(job_dir):
    p = os.path.join(job_dir, "transcript", "words.json")
    d = json.load(open(p, encoding="utf-8"))
    out = []
    for c in d["clips"]:
        for w in c["words"]:
            if w.get("start") is None:
                continue
            out.append({"clip": c["clip"], "w": w["w"], "start": float(w["start"]),
                        "end": float(w["end"]), "prob": float(w.get("prob", 1.0))})
    out.sort(key=lambda x: x["start"])
    return out


def utterances(words, gap):
    utts, cur = [], []
    for w in words:
        if cur and w["start"] - cur[-1]["end"] >= gap:
            utts.append(cur); cur = []
        cur.append(w)
    if cur:
        utts.append(cur)
    return utts


def containment(a, b):
    """Fraction of the SHORTER token list matched inside the longer one."""
    if not a or not b:
        return 0.0
    short, long_ = (a, b) if len(a) <= len(b) else (b, a)
    m = SequenceMatcher(None, short, long_, autojunk=False)
    matched = sum(bl.size for bl in m.get_matching_blocks())
    return matched / len(short)


def fmt(t):
    return f"{int(t//60):02d}:{t%60:06.3f}"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("job_dir")
    ap.add_argument("--gap", type=float, default=0.5, help="pause that ends an utterance")
    ap.add_argument("--window", type=float, default=240.0,
                    help="seconds ahead to look for a retake of the same line")
    ap.add_argument("--thresh", type=float, default=0.70, help="containment to call it a retake")
    ap.add_argument("--min-tokens", type=int, default=3,
                    help="utterances shorter than this only group on a near-exact match")
    ap.add_argument("--md", metavar="FILE"); ap.add_argument("--json", metavar="FILE")
    a = ap.parse_args()

    words = load_words(a.job_dir)
    if not words:
        sys.exit("no words in transcript")
    utts = utterances(words, a.gap)

    rows = []
    for i, u in enumerate(utts):
        toks = [t for w in u for t in norm(w["w"])]
        rows.append({
            "i": i, "start": round(u[0]["start"], 3), "end": round(u[-1]["end"], 3),
            "dur": round(u[-1]["end"] - u[0]["start"], 3),
            "text": " ".join(w["w"] for w in u),
            "toks": toks, "content": content(toks),
            "mean_prob": round(sum(w["prob"] for w in u) / len(u), 3),
            "min_prob": round(min(w["prob"] for w in u), 3),
        })

    # --- link each utterance to a later retake of itself ----------------------
    nxt = {}
    for i, r in enumerate(rows):
        ci = r["content"]
        if not ci:
            continue
        for j in range(i + 1, len(rows)):
            rj = rows[j]
            if rj["start"] - r["end"] > a.window:
                break
            cj = rj["content"]
            if not cj:
                continue
            need = a.thresh if min(len(ci), len(cj)) >= a.min_tokens else 0.95
            c = containment(ci, cj)
            if c >= need:
                nxt[i] = {"j": j, "containment": round(c, 3)}
                break

    # --- chain links into take groups ----------------------------------------
    # Links are chained so a 3+ take run holds together, but a chain is NOT trusted on
    # its own: A->B->C can link A and C even when they share nothing. Two utterances
    # 70 seconds apart got merged because both contained the word "game". So every
    # tentative group is re-verified member-by-member against its keeper below, and
    # anything that does not match the keeper DIRECTLY is released.
    parent = list(range(len(rows)))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]; x = parent[x]
        return x

    for i, link in nxt.items():
        ri, rj = find(i), find(link["j"])
        if ri != rj:
            parent[max(ri, rj)] = min(ri, rj)

    tentative = {}
    for i in range(len(rows)):
        tentative.setdefault(find(i), []).append(i)

    def pick_keeper(members):
        """The LAST take, but never a fragment over a complete one.

        A creator who fluffs a line says it partly, stops, and says it again, so the
        last take is normally the good one. But the transcriber also splits a take at
        any half-second breath, which leaves a stub like "Within six weeks," sitting
        AFTER the complete sentence. Blindly keeping the last one would ship the stub
        and bin the take. So only takes carrying at least 80% of the group's best
        content count are eligible, and the last of THOSE wins."""
        best = max(len(rows[i]["content"]) for i in members)
        eligible = [i for i in members if len(rows[i]["content"]) >= 0.8 * best]
        return eligible[-1]

    take_groups, released = [], []
    for members in tentative.values():
        if len(members) < 2:
            continue
        members = sorted(members)
        keeper = pick_keeper(members)
        kc = rows[keeper]["content"]
        coherent = [i for i in members
                    if i == keeper or containment(rows[i]["content"], kc) >= a.thresh]
        released += [i for i in members if i not in coherent]
        if len(coherent) >= 2:
            take_groups.append(sorted(coherent))
    take_groups.sort(key=lambda g: g[0])

    superseded = set()
    keepers = {}
    for g in take_groups:
        k = pick_keeper(g)
        keepers[g[0]] = k
        for i in g:
            if i != k:
                superseded.add(i)

    for r in rows:
        r["superseded"] = r["i"] in superseded
        r["retake_link"] = nxt.get(r["i"])

    span = words[-1]["end"] - words[0]["start"]
    speech = sum(r["dur"] for r in rows)
    dup = sum(rows[i]["dur"] for i in superseded)
    keep = speech - dup

    print(f"utterances        : {len(rows)}")
    print(f"speech span       : {fmt(words[0]['start'])} -> {fmt(words[-1]['end'])}  ({span/60:.1f} min)")
    print(f"speaking          : {speech/60:.1f} min     silence {(span-speech)/60:.1f} min")
    print(f"take groups       : {len(take_groups)}  covering {sum(len(g) for g in take_groups)} utterances")
    print(f"superseded takes  : {len(superseded)}  = {dup/60:.1f} min")
    print(f"speech after keeping the LAST take of each: {keep/60:.1f} min")
    big = sorted(take_groups, key=len, reverse=True)[:8]
    if big:
        print("\nbiggest take groups:")
        for g in big:
            print(f"  {len(g)} takes @ {fmt(rows[g[0]]['start'])}  \"{rows[g[-1]]['text'][:70]}\"")

    out = {
        "utterances": [{k: v for k, v in r.items() if k not in ("toks", "content")}
                       for r in rows],
        "take_groups": take_groups,
        "superseded": sorted(superseded),
        "stats": {"span_s": round(span, 2), "speech_s": round(speech, 2),
                  "superseded_s": round(dup, 2), "keep_s": round(keep, 2),
                  "groups": len(take_groups)},
    }
    if a.json:
        json.dump(out, open(a.json, "w", encoding="utf-8"), indent=1)
        print(f"\nwrote {a.json}")
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write(f"# take map — {os.path.basename(a.job_dir)}\n\n")
            f.write(f"{len(rows)} utterances · {len(take_groups)} take groups · "
                    f"{len(superseded)} superseded takes ({dup/60:.1f} min)\n\n")
            f.write("`KILL` = an earlier take of a line that is said again later. "
                    "The LAST take of each group is kept.\n\n")
            f.write("| # | start | end | dur | | p | text |\n|---|---|---|---|---|---|---|\n")
            for r in rows:
                mark = "**KILL**" if r["superseded"] else ""
                f.write(f"| {r['i']} | {fmt(r['start'])} | {fmt(r['end'])} | {r['dur']:.2f} "
                        f"| {mark} | {r['min_prob']:.2f} "
                        f"| {r['text'][:200].replace('|','/')} |\n")
            f.write("\n\n## Take groups\n\n")
            for g in take_groups:
                k = pick_keeper(g)
                f.write(f"\n### {len(g)} takes — keep #{k}\n\n")
                for i in g:
                    tag = "KEEP " if i == k else "kill "
                    f.write(f"- `{tag}` **#{i}** {fmt(rows[i]['start'])}–{fmt(rows[i]['end'])} "
                            f"({rows[i]['dur']:.2f}s) — {rows[i]['text'][:200]}\n")
            if released:
                f.write(f"\n\n## Released by the coherence check ({len(released)})\n\n")
                f.write("Chained into a group but not actually similar to its keeper. "
                        "These are NOT retakes and are kept.\n\n")
                for i in sorted(released):
                    f.write(f"- #{i} {fmt(rows[i]['start'])} — {rows[i]['text'][:140]}\n")
        print(f"wrote {a.md}")


if __name__ == "__main__":
    main()
