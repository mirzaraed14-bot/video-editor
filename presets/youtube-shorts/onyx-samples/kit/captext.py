"""captext.py: the caption punctuation rule, shared by both Onyx looks (ig_overlay.py, yt_overlay.py).

Affan, 2026-10-07 (all videos from now on): captions keep ONLY exclamation marks, question marks and quotation marks; full stops,
commas and everything else go, thousands commas included ("$15,000" -> "$15K", "1,500" -> "1500"); decimals and clock times survive
("2.5", "9:30"), so do apostrophes and hyphens inside words
("don't", "ex-CEO", "F*CKED").

  >>> clean("Well, this is why.")             -> "Well this is why"
  >>> clean("right around $23,000.")          -> "right around $23K"
  >>> clean('"This is not by me."')           -> '"This is not by me"'
  >>> clean("Wait... what?!")                 -> "Wait what?!"
"""
import re

_DIGIT_SEP = re.compile(r"(?<=\d)[.,:](?=\d)")          # 23,000  2.5  9:30
_DROP = re.compile(r"[.,;:…·•]")                         # full stops, commas, (semi)colons, ellipses, bullets
_DASH = re.compile(r"\s[-–—]+\s|[–—]+|^[-–—]+|[-–—]+$")  # spaced / em / en dashes and dangling hyphens (in-word hyphens stay)


_K = re.compile(r"(?<![\d,])(\d{1,3}),000(?![,\d])")     # 15,000 -> 15K (Affan: no commas, and $15K is how short-form writes it)
_GROUP = re.compile(r"(?<=\d),(?=\d{3}(?!\d))")               # any other thousands comma goes: 1,500 -> 1500


def clean(text):
    text = _GROUP.sub("", _K.sub(lambda m: m.group(1) + "K", text))
    keep = {}
    def hold(m):
        k = f"\x00{len(keep)}\x00"; keep[k] = m.group(0); return k
    t = _DIGIT_SEP.sub(hold, text)
    t = _DROP.sub("", t)
    t = _DASH.sub(" ", t)
    for k, v in keep.items():
        t = t.replace(k, v)
    return re.sub(r"\s{2,}", " ", t).strip()


if __name__ == "__main__":
    for s in ("Well, this is why.", "right around $23,000.", '"This is not by me."', "Wait... what?!", "BlockFi's ex-CEO — FTX",
              "IT'S A DOLLAR SIGN RED PILL.", "Mr. Clark,”", "9:30, then 2.5 hours", "I F*CKED UP.", "So — no"):
        print(f"{s!r:40} -> {clean(s)!r}")
