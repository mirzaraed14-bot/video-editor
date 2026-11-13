# RUN: harry-potter-idea3 ("Hagrid Was Never Real 🤯"), Abundance Wisdom Short

## ▶ STATUS: resume here
- **12 Nov 2026, ~19:20: DROPPED AS BUILT.** Affan: "its horrendous not upload material at all its just 2 topics thats
  it nothing special either you find better moments to make a proper story or drop this idea".
  - **Verdict: DROPPED.** The built cut is dead, and no better Hagrid moments exist that make one story. Coltrane's 2022
    farewell (§ below) is a separate, unverified beat, not a rescue.
  - **12 Nov ~19:55, removed from ABW11 on his word ("Yes, remove it")**, with `premiere/remove_hagrid.js` under the
    Premiere lock:
    - the sequence was unchanged (V1 5, V2 6, A1 5, 4 markers);
    - it was his active sequence, so "Snape Prank - raw cut v3" was opened first;
    - "Hagrid - raw cut" was deleted, then the bin "Hagrid" (only our 6 source clips, used by no other sequence).
    - Read back (`premiere/list_seqs.js`): ABW11 now holds Snape Prank - raw cut v3 (52 clips), Sequence 01 (10),
      02 (26) and 03 (3). Active: Snape v3.
    - Not saved (his Ctrl+S). Source files in `src/` are untouched.
- **House style if this is ever revived and built (Affan, 12 Nov ~19:45, via the HP hub):**
  - The house style is the "Why Michael Jackson's Son Had To Step Outside" build (11-09) **exactly as shipped**. His
    words: "I like the Topaz, the head tracks, everything about it".
  - **That includes Affan's AE grade** (`grade_mode 'ae'`), not a Bolt grade. The Bolt grade is still an open trial (La
    Toya), and none of Bolt's measured numbers are ported by default. (Corrected 12 Nov by the HP hub; my first note
    here said "Bolt's grade", which was wrong.)
  - Template: `projects/mj-son-step-outside/` (BUILD.md + `build/`). The full parameters, with file:line references, are
    in `research/bolt-style-2026-11-12/findings.md` § "The template".
  - **Splits and reaction cutaways (Affan, 12 Nov, via the HP hub; rules in AW README § 13), decided at sequencing:**
    - **Splits:** on comparison beats, two shots stacked top and bottom. The seam sits at the base caption y, with a
      white line on it.
    - **Reaction cutaways:** 1-2 s picture-only covers of someone reacting to that exact moment, first-party, at most
      about one per 6-8 s.
    - **For a revival or the next HP Short,** look for a comparison beat (e.g. Coltrane vs the Hagrid double) and
      audience or co-star reactions that fit.
- Earlier status, kept for the record:
- **12 Nov 2026, about 16:00: RAW CUT PLACED in ABW11** as "Hagrid - raw cut" (new bin "Hagrid"): 1080x1920, 30 fps,
  0-21.70 s.
  - V1/A1: 5 clips each (Columbus, in three spans, split at the podcast's camera cuts).
  - V2: 6 picture-only covers (their audio removed).
  - 4 markers.
- **Read back** (`premiere/readback.tsv`): spans, scales and positions as planned. Framing proof: `proof/framing_raw.jpg`.
- His active sequence ("Snape Prank - raw cut v3") was restored. **ABW11 NOT saved** (his Ctrl+S).
- The Premiere lock was free; it was taken and released for each window.
- Placed three times; v3 is the one. The two earlier versions were our own sequence, deleted by a guarded script that
  checked it was untouched:
  - v1: one edge ran into Osman's "Yes", and Premiere's in-point rounding put another into the tail of "think".
  - v2: two framings were off (the head crop and the 2001 Hagrid shot).
- **Next:** he reviews it (Tella or notes), then BRIEF.md and the build.
- **Build to-dos already known:**
  - the label for "Aug 2025" on line B;
  - a blurred fill behind the two letterboxed shots;
  - by-ear checks of the first edge;
  - credit for the agency photos;
  - whether to keep Osman's "Martin Bayfield".

## The cut (`premiere/plan.json`; words = WhisperX word-aligned `_rk/transcript/words.json`, offset 1500 s)
| Seq | Columbus says (TRE AZGH_imo_3g, 28 Aug 2025) | Source | Picture (V2 cover, else Columbus) |
|---|---|---|---|
| 0.00-10.90 | "A rugby player who played…" [Osman: "Martin Bayfield."] "Yes, who played Hagrid with a giant, sort of fake rubber Hagrid head that we sometimes replaced with CGI." | 1539.067-1549.967 | 0-2.43 the tall man next to Coltrane in costume tests (Collider re-cut of WB EPK 368.13, letterboxed); 2.43-3.90 the body suit (Collider 331.97); 3.90-7.83 the real animatronic head (studio tour 1080p60, scale 140); 7.83-10.90 Columbus |
| 10.90-16.37 | "I looked online and there were photographs of Nick Frost as Hagrid," | 1526.533-1532.000 | 10.90-13.20 Columbus; 13.20-16.37 the 2025 photo of Frost as Hagrid (Click News and Media) |
| 16.37-21.70 | "and he's wearing the exact same costume that we designed for Hagrid. Part of me was like, what's the point?" | 1558.133-1563.467 | 16.37-18.53 a 2025 costume photo; 18.53-19.83 2001 Hagrid's back in the coat (Warner "Yer a wizard, Harry" 247.77, letterboxed source scaled to fill); 19.83-21.70 Columbus, hard cut on "point?" |

- **Edges, loudness at the actual placed points:**
  - A in: -11 dB. "Name. A" runs together, so check by ear.
  - A out: -41 dB.
  - B in: about -28 dB.
  - B out: -19 dB (the dip after "Hagrid", before Osman's "Yes").
  - C in: -35 dB.
  - C out: -44 dB.
- **Premiere's in-point rule (measured here):** it floors to the source's 25 fps frame grid, then to the sequence's 30
  fps grid. Plan in-points on the 25 fps grid.
- Camera cuts in the podcast: 1526.84 and 1549.92 (V1 razors), and 1561.60 (cover c6 re-pinned to end there, so no stray
  frame of the earlier shot).
- **Dropped on purpose:**
  - his "still Martin… I could be wrong" guess (reports name another double);
  - "Now, that's not Nick Frost": the only clear photos of the double show the new child Harry.
  - The "he" in line C then reads as the 2025 Hagrid; the costume claim is true either way.
- **Length 21.7 s.** That's short for AW (the prank was about 48 s). The only longer first-party material is Bayfield's
  2010 "Team Hagrid" lines (270p, possibly music under them), dropped at his OK.

## Files
- **Sources:** `src/` (see `SOURCES.md`): tre, making, headtour, yerawizard, and the set2025 photos rendered as 6 s
  1080x1920 clips.
- **Premiere:**
  - `premiere/build_place.py` → `place_hagrid.jsx`;
  - `run_window_v3.py` (state → delete our old one → create → place → readback → restore);
  - `delete_ours.js` (refuses unless the sequence is exactly as we placed it).
- **Proofs:** `proof/framing_raw.jpg`, `proof/anchor_fair.jpg` (Columbus finish), `proof/bts_finish_compare.jpg`.

## Checked and rejected as a rescue (12 Nov ~19:20): Columbus's reveal + Coltrane's farewell
**It fails the new §4 rule.** The joining line ("the giant was a trick, the goodness was the man…") is mine; no speaker
says it. Nothing in Coltrane's words answers Columbus's, so it reads as "reveal + farewell": two topics again.
Kept here only as a record. Coltrane's farewell is a separate beat, not this idea.

| # | Voice | Words | Picture |
|---|---|---|---|
| 1 (hook) | Columbus, Aug 2025 (on disk, 1080p, finish-tested) | "a rugby player who played Hagrid with a giant, sort of fake rubber Hagrid head that we sometimes replaced with CGI" | 2001 two-men costume test, then the 1080p60 animatronic head |
| 2 | Coltrane, *Return to Hogwarts* (HBO, 1 Jan 2022) | "Everybody in the world would like a really big, huge, strong, good man on their side … Hagrid was always obviously the good guy" | Coltrane, then the film's Hagrid (Warner 1080p) |
| 3 (end) | Coltrane, same special | "you could be watching in 50 years' time, easy. I'll not be here, sadly, but Hagrid will." | His face; optional low label "Robbie Coltrane, 1950-2022" |

**Wording source:** press transcripts only, not heard. Newsweek's 14 Oct 2022 piece quotes both lines; the "good man"
line is via CNN. Outlets differ: a fan tweet has "I won't be around in 50 years".

**Proof found:** after his death (14 Oct 2022) the clip went viral; one tweet carrying it had about 40K likes and 19.4K
retweets within 2 hours (Newsweek). Instagram numbers are unread.

**Open rows (even as a separate beat, nothing here is verified):**
- **Source:** the Coltrane footage isn't on disk. The original is HBO's special (Max). YouTube copies are likely fan
  re-uploads, and none is verified, because YouTube is blocked (15:28) and I made no request.
- **Instagram proof:** unread. One keyword search page, then my post-meta loop timed out on my side but kept running in
  the page, and I started a second loop on top of it: up to about 17 `/p/` fetches about 3 s apart, then HTTP 429.
  That broke the no-loops rule. All Instagram work stopped and the tab is closed.
- **Freshness:** Shorts of the Coltrane line, and of our join (the reveal into his farewell), are unknown.
- **Death lane:** the ending leans on his death. His call.
- **The two-men shot is still Collider's re-cut** (❌ "not a competitor's re-cut"). The 1080p60 head alone could carry
  beat 1.
- **G5:** hear both lines by ear on the downloaded special. Check Coltrane's health on set (the press says he was
  ailing) before any label.

**Also in the episode, not pitched** (single voice, no Instagram proof):
- **Columbus "cast the parents" after Home Alone,** 21:43-22:58. Clean audio (flatness 0.182, -11.4 LUFS). Its pictures
  need Culkin child footage, the minors line logged 10 Nov.
- **"I've been Harry Potter, I've been Hermione… that's why there are so many cuts in the first film,"** 49:59-50:40.
