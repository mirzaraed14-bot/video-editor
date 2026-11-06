# RUN — Ronaldo Retires (Abundance Wisdom Short)

## ▶ STATUS 2026-11-06 ~20:25: v1 DELIVERED, waiting for his review. RESUME HERE
- File, QA, differences from the brief: top of [REPORT.md](REPORT.md). A note from him: read ABW10 first if he edited (`premiere/his1/readback.tsv` is the v1 spec), change only what he named, data + one finish render (no complete re-render).
- Re-run: `build/make_timeline.py` → `build/fit_y.py` → `finish.py centers` → `stage_a.py render` (frame ranges) → captions → `render_chunks.sh` → `mix.py` → `export_cta.py`. `proof/r1 r2 r3` hold the checks.

## ▶ previous status 2026-11-06 ~19:25
- **~20:05: frames passed on r3 (O18, O19 band [200,1300]; O20 [370,1470]; anthem unstretched + pre-grade level). Phase 2 running on the builder: render, mix, export to `outputs/Ronaldo Retires.mov`, QA. CTA 13.00 and 43.70. I check, then deliver + REPORT.md + LESSONS.**
- **~19:55: Phase 1 back, frames checked. Fix list sent to the builder (hook into a band, anthem unstretched: the Royal Anthem upload measures ~1.19x too wide, press conference wider band, article bright and centred, tear + anthem captions off the lips, S13 and tunnel recentred, two long cards scaled). It re-renders only those shots and stops at `proof/r2/` for my check. Phase 2 after that.** Credits 940 → 906.
- **Spec = `BUILD.md` (the builder's brief) + `BRIEF.md` § TELLA 1 and § OVERLAY PICKS + corrections. His cut = `premiere/his1/readback.tsv`, 53.77 s.** Phase 1 running on a Sonnet builder: timeline, dialogue, captions, cards, Stage A, test stills in `proof/r1/`. **It stops for my frame check; no full render before that.**
- Sources: `dl_ov/` (16 of 17 pulled; YouTube bot-blocked this IP at 18:50 on the 17th, `.locks/youtube.BLOCKED` set by this job, probe after an hour, then clear it). Higgsfield: 9 soft excerpts at `dl_ov/hf/*_up.mp4` + `manifest.json`, about 35 credits of the ~40 he approved (940 → ~905). AP photo upscale failed (no charge), original used. Article `assets/article_tsn.png`.
- Picks sheet sent to him: `proof/OVERLAY-PICKS-sheet.jpg`. No reply yet; a change from him overrides.
- Report must say: "no drinking reference" is unticked because of his own re-cut; the middle of beat 3 changed (2016 + 2022 between the 2004 and 2026 bookends); W replaced by beIN; FOX anthem swapped for the same feed's other upload; debut held to one 1.5 s shot; "a boy in Madeira" = Funchal, child photo only on his word.
- 2026-11-06 ~18:05 status:
- **HIS TELLA 1 + RE-CUT ARE IN: `BRIEF.md` § TELLA 1 (table keyed to his timeline), his cut = `premiere/his1/readback.tsv`, 53.77 s. Drive everything from his read-back, never from `edl.json`.** His re-cut puts "He was a drunk person" in and asks for a father overlay on it: this reverses brief rule 6, on his own hand and words.
- **Overlay research running (me, Opus): `review/search1.txt`, one spaced queue. Facts so far:** the "last set of Nations League games" = Portugal 1-0 Wales (home, he captained) then Norway 1-2 Portugal in Oslo, unused for the whole match (Felix, Ramos; Haaland for Norway); he left camp late on a Wednesday around 30 Sept 2026 after Jesus said he'd be benched again v Denmark; provisional suspension 10 Oct; final 30 days + EUR 255 fine 19 Oct.
- **Picks so far:** father = REAL footage inside the Piers clip, Norwegian TV 2004 doorstep: src 154.5-157.0 (steady) or 111.0-113.0, crop above its burned-in subs. Article = `assets/article_tsn.png` (AP on TSN, "Ronaldo suspended for 30 days and fined for walking out on Portugal camp", 1440 wide, photo of him stepping off the bus; crop out the floating badge). Official candidates: FIFA KRqgjpiwrY8 (free kick v Spain), UEFA 4mGv60SVH_c (lifts the Euro 2016 trophy), UEFA 9SgaWPFdfhI (celebrates Euro glory), Norway highlights iYK24k7mGcs / lFAhmP-ynCs.
- Capture note: `page-record.mjs` with `CHROME_PATH` = the hyperframes headless shell (no sound device route, isolated). aljazeera.com does not resolve here.
- 2026-11-06 ~10:50 status (raw cut placed):
- **RAW CUT PLACED, WAITING ON HIS CHECK.** ABW10, bin "Ronaldo Retires", sequence "Ronaldo Retires - raw cut", 1080x1920, 30 fps, 52.77 s, 24 V1/A1 + 15 V2 covers, 6 beat markers. Not saved (he saves). His active sequence (GTA 27 - Complete Guide) restored. Baseline for reading his edits: `premiere/v1/readback.tsv`. **Next: when he OKs or re-cuts, read back (`python premiere/pp.py premiere/readback.js`), his cut is the spec, never re-place over it. Then advisor, catalog pass in BRIEF, build per § Decisions.**
- **Downloads, Affan directly here: "download them yourself".** One plain yt-dlp answered normally, so plain yt-dlp through `lock.sh youtube`, >= 60 s apart: no cookies, proxies or client switching. In `dl/`: SKY_Jul2026 (1080p 23.976), SKY_RonaldoRetires (1080p 25), CR7_WC2026_Crying (1440p VP9, soft, 30), CR7_Retire_AS (not used: one sub line + AS bug, no better than NDTV), ANTHEM_2022 = Royal Anthem 4CLzZz4SUXg. **FOX AnR1buWwRw0 says "Video unavailable" here and foxsports.com answers 403: not pushed.** UEFA Euro 2004 highlights have no Ronaldo tears: deleted, with the two rejected anthem copies (phone shots).
- **Locks so far:** 2026 lock PASSES (FIFA WORLD CUP 2026 banner in crop on the last shot, dark red kit). Minors: out on every picked frame (his kids 4.97-8, ~204, ~282-284 stay out; ANTHEM clip has crowd kids ~72, line-up mascots only in the rejected copy). Drinking line out. **BENCH_Norway sitting close-up 7.64-13.58: the uploader warped his frown, NEVER use.** Bench standing 1.2-3.57 and bib 21.05-22.32 used.
- **Words:** Sky anchor stumbles at 18.14-18.83 ("that led to a... led to a suspension"; whisper's first pass hid it, the level strip + snip showed it): cut, re-ASR reads "that led to a suspension". Hook: "Bom, é" off, starts at "23 anos"; the brief's middle dropped (no caption given for it). Re-ASR of A1 as Premiere holds it: all words right, longest quiet run 0.01 s.
- **Build notes:** Sky English subs in the hook from y~0.83, NDTV line from y~0.905, Piers bug, beIN bug, Fotbolera bug top left (a corner shows on the bib shot): crop or nudge. W shots dip to black at their edges: clean spans only. Euro 2004 + anthem + W are soft: letterbox + Higgsfield test. Levels differ a lot: hook -29, anchor -24, retirement -15, Piers -9 dB medians. Mid pills proposed ~20.3 s and ~43 s. V2 cover ends can re-pin one frame late on a 25 fps source (`premiere/fix_ends.js`): check the V2 readback for overlaps after any re-place.
- 2026-11-06 earlier status:
- **WAITING on Affan: 4 must-have downloads + his yes to the quote and the eight defaults** (his "I've downloaded the source files" was not a yes). Nothing placed or built. ABW10 untouched, no Premiere lock taken, no Higgsfield credits spent. GPU used once for the intake ASR, under `gpu.lock`, released.
- **2026-11-06 ~04:30, his "Yes to all" is in (§ Decisions).** Beats 2-5 are measured and resolved: `premiere/make_beats.py` → `edl.json`, 30.53 s (B2 3.70, B3 6.67, B4 9.80 incl. the optional head, B5 10.37). `win/asr_plan.py` hears the brief's words and every join clean. A beat whose source is missing stays out and is listed as PENDING, so re-running make_beats + resolve_beats picks files up as they land (copy each to `dl/`, transcode to `seq_src/<key>.mov`: keys SKY_Jul2026, SKY_RonaldoRetires, CR7_WC2026_Crying, ANTHEM_2022).
- **Picture picks so far:** retirement = NDTV copy. Euro 2004 src 0.3-3.87 (first shot). Bench: sitting close 7.64-13.58 for "wasn't brought on", bib 21.02-24.76 for "told to warm up". Piers: tissue close under his question, silent tears 293-294.87 under "He never saw", drop "to see what I..." (295.1-296.1, not in the brief). Boy-in-Madeira = tight on-camera shot N 284.3-288.95 slowed x1.37 (`seq_src/N_tight_slow.mov`). N 215 = him singing in close-up, a possible anthem stand-in, only with his OK.
- **Runtime forecast:** ~50-52 s with B0 + B1, against the brief's 55-60, because pauses are closed. Say so in the raw-cut message.
- **In** (`E:\Bullshit Folder\Henry`, 02:12–02:16, copied to `dl/`, originals untouched; all H.264 + AAC, 1080p, no AV1):

| dl/ file | Length, fps | What the frames and words show |
|---|---|---|
| PIERS_2019_Father.mp4 | 305.5 s, 30, ~1 Mb/s | Brief's clip. "What's the sadness for you?" 285.04, "to be the number one" 288.52, "He never saw how great you became" 296.26–297.92, "No." 299.22. Drinking line at 239–243, stay out. LIFESTYLE FEED bug top right; burned-in subs on inserted clips. 3 identical copies in Henry |
| EURO2004_Tears.mp4 | 24.1 s, 30 | "4K" in the title, 1080p file. Clearly adult 19-year-old tears, AI-upscaled and oversaturated. A morph transition around 11 s: avoid it |
| BENCH_Norway.mp4 | 122.3 s, 29.97 | Fotbolera bug top left on every frame, yellow circles on some shots; bench shots near the start look clean. 2 identical copies in Henry |
| CR7_Retire_ELPAIS.mp4 | 305.9 s, 25 | Two burned-in sub lines (ES, EN) from about y 0.80 down, EL PAÍS bug top right, big logo over the first ~2 s. **His kids from about 5.0 s** |
| CR7_Retire_NDTV.mp4 | 305.9 s, 30 | One burned-in EN line, NDTV Profit bug bottom right (outside a centre crop). Kids at the same place. 30 fps: check duplicate frames before choosing it |

- **Retirement lines, measured on EL PAÍS (`transcript/CR7_Retire_ELPAIS.json`, large-v3, pt):** beat 2 0.00–4.86 · beat 3 87.26–95.32 · **beat 5A 210.12–214.72 (brief said ~3:24–3:30; lock by ear)** · beat 5B 276.28–282.76. Whisper hears "quando eu era apenas"; the brief has "quando era apenas": English captions unaffected. Edges not yet refined.
- **Beat 2 picture:** the reading shot ends about where his kids start, so check that cut frame by frame and stay on him through the end of the line.
- **Still missing:** gvYuXmZdrBM (hook), 1jGbBGwWahs (Sky anchor), WemArJYhkg4 (2026 tears), AnR1buWwRw0 (2022 anthem). Backups: Mos8Vj2rz1I (AS), OG5u1uurPik (UEFA Euro 2004). The @cristiano original is now worth more, since both copies carry burned-in subs.
- Possible stand-ins only if he OKs them: the retirement video's own tunnel tears (t≈87) and close-up beside a teammate (t≈210). Their year isn't verified. No stand-in exists for the two Sky clips.
- Section 3 of the brief (beats 0–5) is the cut. The "Arc" list and "Gate run" hook notes are older text and don't override it.
- BRIEF.md has the same words as `X:\Claude Projects\Abundance Wisdom\RONALDO-RETIRES-EDITOR.md` (compared word by word 2026-11-06), plus the orchestrator's one-line note in § 2 that YouTube is blocked. **Compare again before intake, the raw cut and the build** (LESSONS 2026-11-04: a brief can be re-locked).
- **Next, once he answers:** record his words under § Decisions; `ffprobe` every download; copy to `dl/`; duplicate-frame check; transcribe once; cut; raw cut in ABW10 if he keeps the check. Call the advisor once before committing to the build plan.
- Kit to copy from: `projects/latoya-betrayed/build` + `win` (newest) and `projects/owen-hart-wife` (`win/asr_plan.py`, `win/transcribe_fw.py`, `captions/falign.py`). Recipe: top of `projects/latoya-betrayed/RUN.md`.

## Format
Short, 1080×1920, 30 fps export, AW look. Deliver `Ronaldo Retires.mov` to `E:\Shorts\Abudance Wisdom Shorts Exports\Final Renders` + `X:\Claude Projects\Exports\`. Never C:. No phone copy.

## Source search (2026-11-06)
None of the brief's sources are on his drives. Searched by title word and YouTube id: E:, X:, C:\Users\affan (excluding AppData), G:. By subject: Bullshit Folder, E:\Downloads, IDM Directory, E:\Shorts, X: Exports, C: Downloads, Videos, Desktop.
Ronaldo files that exist but aren't usable for this brief: Speed / "Inshallah" / UEFA drink phone clips, `IShowSpeed crying after ronaldo lost to spain` (Speed, not Ronaldo), and two 271-byte empty HandBrake stubs of "Cristiano Ronaldo Vs Spain ... 4K Clips" (`E:\Bullshit Folder`, `C:\Users\affan\Videos`).
YouTube is blocked on this PC: never bypassed, resolutions can't be checked from here, so `ffprobe` at intake decides what is soft.

| Key | Used in | Link |
|---|---|---|
| SKY_Jul2026 | beat 0 | https://www.youtube.com/watch?v=gvYuXmZdrBM |
| SKY_RonaldoRetires | beat 1 | https://www.youtube.com/watch?v=1jGbBGwWahs |
| CR7_RetirementVideo (EL PAÍS, the brief's timestamps) | beats 2, 3, 5 | https://www.youtube.com/watch?v=bQRye6bEKgw |
| CR7_WC2026_Crying | beat 3 | https://www.youtube.com/watch?v=WemArJYhkg4 |
| PIERS_2019_Father | beat 4 | https://www.youtube.com/watch?v=eu5HUrEHsmc |
| BENCH_Norway | beat 1 | https://www.youtube.com/watch?v=IhpRfn_Ydyk |
| EURO2004_Tears | beat 3 | https://www.youtube.com/watch?v=2I_uSx7N9Rc |
| ANTHEM_2022 | beat 5 | https://www.youtube.com/watch?v=AnR1buWwRw0 |
| EURO2004_UEFA (second copy) | beat 3 | https://www.youtube.com/watch?v=OG5u1uurPik |
| CR7_Retire_NDTV (backup) | beats 2, 3, 5 | https://www.youtube.com/watch?v=b2KYGL69Yqc |
| CR7_Retire_AS (backup) | beats 2, 3, 5 | https://www.youtube.com/watch?v=Mos8Vj2rz1I |
| @cristiano Instagram original (best, no bugs) | beats 2, 3, 5 | only if he can grab it |

## Cost quote (sent)
- ≈ 7–9 % of the week: raw cut 2–3 %, build + render + QA + report 5–6 % (same basis as Owen and La Toya). Review rounds after delivery are extra.
- Time: ≈ 1 h to the raw cut after the downloads land (La Toya: 50 min), ≈ 3–4 h build (La Toya v1: 2.5 h), plus the GPU queue. At 02:01 an Onyx job (`herjavec-500m-billion` plates, pid 54494) held `gpu.lock`.
- Higgsfield, only on his yes: Topaz 2160p on the soft clips only, ≈ 20 s at the measured ≈ 1.9 credits/s (Paris 5 / 2.7 s, La Toya 3 / 1.57 s) → up to ≈ 40 credits. Balance 940 (2026-11-06). One test clip first.

## Open questions (sent, defaults in brackets)
1. "TODAY" label: locked 5 Nov, PC date now 6 Nov. [drop TODAY → "RONALDO RETIRES FROM PORTUGAL"; alternative "5 NOV ·"]
2. Raw-cut check in ABW10 before the build. [yes, stop for it]
3. Music: brief wants piano + swell. [none; the retirement video's own bed stays in its audio under beats 2/3/5, ducked as the brief says]
4. Subscribe: two mid pills, end screen OFF, hard cut on "ball". Every beat has a card, so few free spots. [~25 s and ~45 s, exact times from the real cut, off the hook, cards and payoff]
5. Captions + cards. [house captions, same words, no commas or full stops, one base just under the lips, brief's red words coloured as on Owen and La Toya, cards low]
6. Brief says full-bleed. [full-bleed on sharp sources; his letterbox, blur fill + white line, on soft ones]
7. Upscale. [Higgsfield on soft clips only, up to ~40 credits, test clip first; local Topaz only on faces under 1080p; no 60 fps interpolation]
8. Bolt look: no verdict found (LESSONS, La Toya RUN and REPORT, memory, sibling notes). [normal AW grade, brief's cold / warm / soft per beat as a light tint]
Also asked: decisions here, render steps on one Sonnet agent. [yes]

## Decisions
**Affan, 2026-11-06, relayed by the AW orchestrator, his words: "Yes to all"** (to the eight defaults and the 7–9 % quote). So:
1. TODAY dropped: the label reads RONALDO RETIRES FROM PORTUGAL.
2. Stop for his raw-cut check in ABW10 before the build.
3. No added music. The retirement video's own bed stays under beats 2, 3, 5, ducked as the brief says.
4. Two mid pills at about 25 s and 45 s, exact times from the real cut. No end screen, hard cut on "ball".
5. House captions just under the lips, the brief's English words, no commas or full stops, red words coloured as on Owen and La Toya, cards low.
6. Full-bleed on sharp sources; his letterbox, blur fill and white line on soft ones.
7. Higgsfield on soft clips only, up to ~40 credits, test clip first. No Topaz on faces already 1080p, no 60 fps.
8. Normal AW grade, the brief's cold / warm / soft beats as a light tint. No Bolt.
Quote line: decisions here, render steps on one Sonnet agent.
If a file is missing or unreadable: tell him which one and keep building whatever doesn't depend on it (orchestrator's relay).

## Pipeline
| # | Step | Status |
|---|---|---|
| 0 | Brief saved, sources searched, quote + questions sent | ✅ 2026-11-06 |
| 1 | Intake: his downloads + mine → `dl/`, ffprobe, kit copied | ✅ 2026-11-06 |
| 2 | Words + edges + plan re-ASR | ✅ |
| 3 | Raw cut in ABW10 (Premiere lock per window, his active sequence restored, never saved) | ✅ placed, waiting on his check |
| 4 | Catalog pass in BRIEF ✅, upscales ✅, timeline ✅ | ✅ |
| 5 | Stage A, captions, cards, CTA mids, mix, finish | ✅ |
| 6 | Frame-check locks, brief § 5 boxes, final re-ASR | ✅ |
| 7 | Deliver + REPORT.md + LESSONS | ✅ 2026-11-06 |
