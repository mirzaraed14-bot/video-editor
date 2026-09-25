# BRIEF — gta6-pc-release (the creator's overlay walkthrough, resolved)

## ▶ STATUS: resume here (2026-09-22)
**All six open placements are closed.** The creator's answer was "go off the label of the blocks", and the labels
are now read exactly — not guessed from the picture. Build the 27 overlay blocks below.

**Two corrections to anything written earlier:**
1. **The timeline is 5:16.65, not 5:51.** The creator cut ~34 s after the replay. **Every position in the first
   version of this brief was stale.** The table below is rebuilt from their actual clips.
2. **V1 is 152 clips, not 141.** Their splits are the cut-zoom nests. **Never re-replay the EDL.**

Sources: guide `brief/raw/editing-guide.mp4` (12:22) · narration `brief/transcript/words.json` ·
labels `brief/v1-labels.json` · merged blocks `brief/blocks.json` · reader `brief/readlabels.py`.

---

## How the labels were read (Premiere 25.0 has no API for this)

Every documented route returns nothing: `getColorLabel` is not a function on the DOM TrackItem, the QE clip has
no such property, `export_as_fcp_xml` times out without writing a file, and `select_clips_by_color` reports zero
at all sixteen indices. The `.prproj` does carry it, but **not** in the obvious place — the 829
`BE.Prefs.LabelColors` entries under `ProjectItem` are *bin* labels and a red herring. The per-clip label is:

```
VideoClipTrackItem → ClipTrackItem → SubClip[ObjectRef] → SubClip → Clip[ObjectRef]
  → VideoClip → Clip → Properties → asl.clip.label.name   ("BE.Prefs.LabelColors.<n>")
```

with that clip's `InPoint`/`OutPoint` alongside it, which is what joins each block to the words spoken under it.
Note the two different reference attributes: `ObjectRef` → `ObjectID`, `ObjectURef` → `ObjectUID`.

## The legend

| Label | Count | Means |
|---|---|---|
| **Tan** | 4 clips / 3 blocks | meme overlay, found and downloaded |
| **Violet** | 9 clips / 5 blocks | Higgsfield still, GTA 6 themed, professional |
| **Blue** | 12 clips / 4 blocks | Google image, enhanced in Higgsfield if blurry |
| **Rose** | 19 clips / 8 blocks | YouTube overlay, real footage |
| **Mango** | 11 clips / 7 blocks | motion graphic, GTA 6 theme colours |
| **Iris** | 97 clips / 25 blocks | default: face motion only, no overlay |

## 🔒 GLOBAL RULES

1. **No overlay fills the frame.** Each sits zoomed out so the animated colour matte reads around it.
2. **Drop shadow on every overlay.**
3. **1080p floor** on anything downloaded.
4. **The slow motions are already done — add no speed changes.**
5. **Default Iris blocks:** cut zooms inside the nest, then a slow zoom on the nest. **100 → 110** when the nest
   is long, **100 → 105** when short.

---

## The cue sheet — 27 overlay blocks

Positions are the creator's live timeline. The quoted line is what is actually spoken under that block.

| # | Timeline | Label | Line underneath | Build |
|---|---|---|---|---|
| 1 | 0:00.0 – 0:01.9 | Tan | "internet has officially decided." | meme fitting the line |
| 2 | 0:01.9 – 0:04.7 | Violet | "GTA 6 is coming out on PC in 2028." | Higgsfield: an official-looking GTA 6 announcement, coming 2028 |
| 3 | 0:06.6 – 0:11.0 | Tan | "all five stages of grief … sitting at acceptance" | meme on the five stages of grief |
| 4 | 0:20.9 – 0:24.5 | Violet | "Rockstar's own history kind of proves it." | Higgsfield: **collage of Rockstar history** — RDR2, GTA 5, GTA 4, GTA 3, San Andreas, Vice City merged |
| 5 | 0:28.4 – 0:38.0 | Rose | "nobody at Rockstar has said this … a pattern in Rockstar's last three games" | a real **Rockstar official interview**, framed so it reads as if they are saying this |
| 6 | 0:42.1 – 0:47.4 | Mango | "The CEO of Take-Two said something four days ago…" | motion graphic |
| 7 | 0:54.3 – 0:58.4 | Violet | "at the very end I'm giving you the exact month" | Higgsfield: the release date, **deliberately blurred** |
| 8 | 1:04.3 – 1:08.2 | Rose | "Because if everybody is saying 2028. Someone had to say it first." | a **popular YouTuber** on a clean frame looking into camera. Creator's suggestion: IShowSpeed |
| 9 | 1:10.4 – 1:15.6 | Rose | "Bro, I heard this and that. Who told you? … everyone is going viral" | a **movie scene** two-hander from YouTube, cut to the back-and-forth |
| 10 | 1:23.2 – 1:25.9 | Violet | "The 2028 thing mostly comes from people" | Higgsfield: the same announcement but **rumoured** — must not read as official Rockstar |
| 11 | 1:43.0 – 1:53.9 | Blue | "GTA 4 … April 2008 … PC in December … GTA 5 … September 2013, PC April 2015" | Google images in order: GTA 4, an official Rockstar statement of GTA 4's PC date, then GTA 5 |
| 12 | 1:58.0 – 2:01.7 | Rose | "now Red Dead 2, their most latest game, came out October 2018" | RDR2 trailer / gameplay |
| 13 | 2:13.5 – 2:16.7 | Tan | "the console that sounded like it's going to take off in your living room" | meme: **a house blowing up / on fire** |
| 14 | 2:25.5 – 2:28.6 | Rose | "GTA came out at the end of a generation." | ordinary GTA 5 trailer footage |
| 15 | 2:32.4 – 2:36.2 | Rose | "So GTA 6 is built for modern hardware from day one." | **GTA 6 Extended Look** footage |
| 16 | 2:40.2 – 2:44.2 | Blue | "now what the CEO said. Four days ago, September 17th." | Google image for the shareholder meeting |
| 17 | 2:46.2 – 2:48.9 | Mango | "Strauss Zelnick is the CEO of Take-Two." | motion graphic built on a **PNG cut-out of the CEO** |
| 18 | 2:56.7 – 3:04.8 | Mango | "more and more important … a meaningful audience" | one **continuous** motion graphic across both quotes, styled as the CEO saying them |
| 19 | 3:16.9 – 3:21.2 | Rose | "hackers … going to ruin the game for everyone, modding" | **GTA 5 hackers and modders** footage, 1080p minimum |
| 20 | 3:22.4 – 3:25.5 | Blue | "an ex-Rockstar developer, Mike York, he actually worked there" | image of **Mike York** |
| 21 | 3:25.5 – 3:28.7 | Mango | "number one, PlayStation sells the most" | motion graphic |
| 22 | 3:35.2 – 3:38.0 | Mango | "every single person has a different PC" | motion graphic |
| 23 | 4:02.5 – 4:06.0 | Mango | "York says they test on 10 or 20 different setups" | motion graphic |
| 24 | 4:15.0 – 4:18.1 | Rose | "Red Dead had the exact same problem and they solved it within a year" | RDR2 trailer / gameplay |
| 25 | 4:23.5 – 4:24.5 | Mango | "number one is money" | motion graphic |
| 26 | 4:37.8 – 4:45.1 | Violet | "GTA 5 has sold over 230 million copies across every console" | Higgsfield: **230 million sales** across every console |
| 27 | 4:57.8 – 5:00.1 | Blue | "the PS6 comes out … with that" | **PS6 concept image** from Google, enhanced in Higgsfield |

The other 25 blocks are Iris and take face motion only.

## Higgsfield spend

Five Violet stills (cues 2, 4, 7, 10, 26) plus one plate for the mango work. `gpt_image_2_5` preflights at
**1 credit** per 16:9 image, `nano_banana_pro` at 2. So **6 credits of generation**, plus a retry budget, plus
whatever the Blue enhancements and the CEO cut-out cost — neither `upscale_image` nor `remove_background` will
quote a price without a real uploaded file, so both get preflighted at the moment of use.

**Keep text out of the generated plates.** Cues 2, 7, 10 and 26 all carry wording, and the channel's own Hot
Coffee test found generated type morphs and invents itself. Generate the plate clean, set the type as our own
graphic on top. Cues 2 and 10 are the same announcement twice, once official and once rumoured, so one plate can
serve both.

## Still blocked

**GTA 6: An Extended Look is not downloaded** — YouTube age-gates it and refuses without a signed-in session.
**Cue 15 needs it.** Either read the creator's browser session, or they download it themselves.
