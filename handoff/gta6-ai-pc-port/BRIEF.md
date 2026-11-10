# gta6-ai-pc-port · Affan Afterhours YouTube Short ("AI Ports", his 9 Nov script)

▶ STATUS: resume here (2026-11-10 03:07): **DELIVERED v1** on the defaults (RUN.md lists them); his review pending. Full state: RUN.md.

## The ask (2026-11-09, verbatim)
"Start a new session for this and also if you can there's a little speck of dandruff on my hair if there's any editing trick that you can do to like remove it please do so and justice improve the overall editing by one percent That's what our rule is"
Session brief on top: fresh job, own folder; name after the content; ask about C1454 in one line and don't use it until he answers; remove the speck at the SOURCE with proof (outside-mask numbers, mask on every frame, real-speed check) and his OK before it enters the edit; a Short = sequencing as text first + music and sensitive-word questions, code-built MP4 at native 59.94 into `X:\Claude Projects\Exports\`, his own branding, never Scott's; work in silence; nothing on C:, no phone encode; no Fable agents, builders Sonnet, ask before new agents; ask before Higgsfield credits; other sessions are live, stay in this folder.

## Source
- Raw: `X:\Recordings\Afterhours\C1453.MP4` (copied byte-identical to `raw/C1453.MP4`, original untouched): 1920x1080 h264 59.94p, PCM stereo 48 kHz (camera carries the voice, like C1448), 94.59 s, TC 11:11:19:16, recorded 2026-11-09.
- **`C1454.MP4` (119.6 s, TC 11:12:53:50) starts within a frame of where C1453 stops.** Not mentioned by him; not opened, not transcribed, not used until he says what it is.
- Script: `X:\Claude Projects\GTA 6\sweeps\shorts-sweep-2026-11-09.md` ("AI Ports", his draft tightened, prediction logged 9 Nov).
- Room: same Skool-neon room as C1448 (red mic, sunglasses); he reads off a screen to his side BETWEEN lines and says every line on the lens.

## Channel + format (my read, stated for a one-word override)
- **Channel: Affan Afterhours (GTA).** The words are his 9 Nov "AI Ports" Short script; the recording folder agrees.
- **Format: YouTube Short, 9:16 1080x1920 in the Scott YT Short look (own branding),** like C1448: horizontal raw, but the script is a ~35 s Short and the kept lines total ~27 s.
- Bar to beat: `projects/gta6-head-start` (C1448), approved 2026-11-06 with no notes.

## What he actually said vs the script (burst clock, last take of each line)
- Hook: "Here's why Rockstar **will** bring GTA 6 to PC way, way sooner than you think." Script's fix 1 asked for "might have to" (the "will" overclaims Vermeij). Audio stays as said; frame 1's hook block is an UNSENT prompt "port GTA 6 to PC" (a question on screen, not a claim; no second text card, his "too much text at the beginning" note). His call.
- "A former Rockstar tech director says, because AI could port the PS5 version first." (restart inside the burst: "port the PC-" then a clean retake from 29.69 s; WhisperX hid it, the slice pass found it.)
- **Not recorded in C1453:** the script's reason line "That would hurt sales. So he wouldn't be surprised if Rockstar pulled the PC release closer." and the payoff as "the PC guy" on a new angle. C1454 may be either.
- "Now they just type it." (script fix 3 asked for "they'll"; the on-screen prompt bar makes it read as the joke anyway.)
- "Make Lucy a Shrek" (both ASR passes; almost certainly "Lucia" run into "a": caption LUCIA, checked at build). "Jason riding through a shark on my city" (both slice passes "my city", WhisperX in context "Vice City"; caption VICE CITY, checked at build).
- Payoff: "So we are not going to wait a year this time, ladies and gentlemen." (script: "We ain't gonna have to wait a year, gentlemen.")
- Retakes dropped (last-take rule): hook "here's why rockstar will bring g-" · "His words, I don't really see how you could..." (first, incomplete) · "Because in GTA 5" x3 (last at 43.25) · the port line's first half.

## Eye line (raw clock, Otsu +0.379, separation 3.45 SD = reliable, 65 % on the lens)
camera: 3.75-5.75, 11.25-19.5, 21-23.75, 26-32.25, 34-38.5, 39.5-44.5, 46.25-51.25, 54.5-57.5, 59.25-61.5, 63.25-67, 68.75-72, 76.75-80.25, 82.25-88.25, 89.5-90.75 · reading: only the gaps between lines. **Every kept line is on the lens**, so the face is usable anywhere; overlays are chosen by the story, not to hide reading.

## The dandruff speck (removed at the source, his OK pending)
- **Where:** one ~3 px cream speck on the front of his hair above the right brow (about x1253 y202 at 0:20). **Stays put on the hair for the whole take, rides with the head, never falls off:** on screen in every frame he is in the chair, 238 to 5431 (3.97-90.6 s; it enters with him from the top of frame and leaves the same way). Motion-blurred into a short streak while he sits down / gets up and on fast head turns (frames 3544, 3797).
- **How:** `work/speck/track_speck.py` (LK flow on the hair + white top-hat refine, every frame) + `extend_track.py` (the blurred entry/exit frames), verified on 1 s sheets across the whole take and frame by frame at the entry, the exit and the fastest move (`work/speck/sheet_*.png`). `patch_speck.py`: per frame, the speck's own blob (a motion streak is measured, not assumed round) grown 1 px, feathered over 3 px, filled with OpenCV Telea inpaint in YUV (Y full res, U/V half res), so every pixel outside the mask is the raw's own decoded value before encoding. Output `raw/gta6-ai-pc-port.clean.mov`: ProRes 422 HQ, 59.94, same pts, TC 11:11:19:16, bt709 tags, PCM audio stream-copied.
- **Proof:** numbers in RUN.md § Speck proof; crops + real-speed clip in `review/`.

## Catalog pass (CLAUDE.md § learning loop; all of CATALOG.md read, all 137 stills in `shots/` viewed on 12 labelled sheets `work/catalog/sheet_*.jpg`, 2026-11-09)
**The last video of this kind** (`gta6-head-start`) leaned on: the numbered 1·2·3·4 strip, FX-11 PS5/Xbox split, the 3 % running bar, FX-55 hand underline on a support page, FX-41 giant 29, drawn console menus. **Rest here:** all of those (this is not a list, there is no console-war beat, no support page).

**Moves that fit this video:**
| Move | Where | Why it fits |
|---|---|---|
| **The prompt bar** (a running prop; nearest refs FX-18 Karaoke type + the head-start's running bar) | frame 1 ("port GTA 6 to PC" typing), then each joke types itself on his words with a DONE stamp on his "Done." | his script asks for "a text prompt box on screen for each"; one prop carries the escalation from news to joke |
| **FX-27 Red Word Quote** with a rack-out | "His words: I don't really see how you could protect against that." | a verbatim line that should be read twice; PROTECT in pink, attribution small under it |
| **FX-16 Portal Zoom** | "Make it run on a fridge" then "and it will run better than the PS5 version": push through the fridge's screen into full-frame official GTA 6 footage | the fridge IS the frame within a frame; last time FX-16 was rejected for having no scene to travel into |
| **FX-42 Kin Tag** + a row of the covers he worked on | "A former Rockstar tech director" | a name stack (OBBE VERMEIJ / TECHNICAL DIRECTOR, ROCKSTAR NORTH) beside the GTA III · VC · SA · IV covers already on disk; no fake portrait |
| **FX-39 Source Handle Tag** | the GTA V Franklin/Chop mod clip | borrowed footage carries its @handle, bottom-left |

**Not used on this channel's Shorts yet:** the prompt bar, FX-27, FX-16, FX-42, FX-39.
**The new moves committed for this Short (>= 2, rule 5 + UPGRADES.md):** (1) the prompt bar as the running prop, (2) FX-27 Red Word Quote, (3) FX-16 Portal Zoom through the fridge. Extras, dropped if their check clip fails: FX-42, FX-39. Each is a drawn MG with its own kill switch.

**Looked at and rejected:** FX-13 Depth type with "PC" (two letters clears the killed note's <= 4-letter bar, but frame 1 already carries captions + the prompt bar; another layer is clutter); a separate hook text card (the captions already print the claim; the prompt bar is the hook block); FX-11 Rival split PC vs PS5 (used last time, and "runs better than PS5" is a joke, not a spec sheet: no numbers on screen); FX-46/56 CRT Witness (no footage of Vermeij); FX-41 year ghost on "a year" (giant number used last time); map, archive and paper families (no fit).

**What this one does better than the last (rule 5):** the source picture itself is cleaned (a first on any of his Shorts); the jokes get their own visual engine instead of a checklist strip; ~27 s instead of 52 s (the three 281-859K winners ran 29-37 s); every line on the lens; the first joke lands at ~0:15, ahead of the 0:20 his pre-mortem names as the 5K risk.

## Pick test + Bombas (Scott ENGINE; scored honestly; his pick stands; nothing written to Scott's files)
- Pick test **1 / 3**: (a) held belief ½ ("PC players wait a year") · (b) famous face speaks it 0 (his own channel) · (c) a cost or reversal ½ (the wait collapses).
- Bombas **7 / 11 = worse** (no B1, no B4, structural for his solo channel): B2 ½ ("way, way sooner", no money) · B3 ½ · B5 ✓ GTA 6 on PC, untold AI angle · B6 ½ (drawn prompt at frame 1, no real event) · B7 ✓ Rockstar / GTA / PS5 / Lucia / Jason / Shrek / Franklin / Chop · B8 ✓ the escalating prompts on his delivery · B9 ✓ the fridge · B10 ✓ one subject, ~27 s · B11 ½ (cover IT RUNS ON A FRIDGE).

## Prediction (his script, 9 Nov, mirrored verbatim, do not edit)
- **YouTube Shorts 5K–200K. IG 10K–300K.**
- **Biggest risk:** the second-variation hypothesis. This is your third PC-themed Short, and returns may be shrinking.
- **Pre-mortem, 5K:** an ex-dev quote reads as news; the jokes land too late (after 0:20).
- **Pre-mortem, 500K:** PC-vs-console war bait plus absurd prompts plus a PC-guy payoff. It's the menace formula, with AI as the new weapon.

## Timing
His sweep: Take-Two's earnings call is tonight, 4:30 pm ET (2:30 am PKT on the 10th); post this Short BEFORE the call in case PC comes up.

## Facts (from his sweep's table; nothing new claimed on screen)
| Line | Label | Use on screen |
|---|---|---|
| Vermeij, former Rockstar North technical director (GTA III; VC, SA, GTA IV; left 2009) | CONFIRMED | Kin Tag |
| "I don't really see how you could protect against that" | CONFIRMED (Rock Paper Shotgun, via DualShockers) | FX-27 quote, attributed |
| A GTA V mod swaps Franklin and Chop | CONFIRMED (the mod exists) | its footage, with the uploader's handle |
| "Rockstar will bring it to PC sooner" | his read, NOT Vermeij's words ("I wouldn't be surprised...") | an unsent prompt, never a printed claim |
| "because AI could port the PS5 version first" | Vermeij's WORRY, not a thing that works today | the prompt types and waits unsent: no progress bar, no DONE |
| Lucia Shrek, the shark, the fridge, "runs better than PS5" | JOKES | prompt bar, no numbers, no fake specs |
| PC date | not said, not shown | none |

## Assets
- On disk: official GTA 6 footage (`projects/gta6-pc-release/broll/`, Extended Look `E:\Bullshit Folder\Simone\...`, Launch Trailer `E:\Bullshit Folder\Henry\...`), official GTA V gameplay `E:\Bullshit Folder\Canelo\Grand Theft Auto V Official Gameplay Video.mp4`, covers `projects/gta6-all-fit-inside/yt/assets/covers/` (gta3, vc, sa, gta4, gta5, gta6), smoothed clips `projects/gta6-all-fit-inside/yt/assets/broll/`. COPY out, never edit those folders.
- To fetch (named before pulling, his rule): the GTA V Franklin/Chop role-swap mod clip from YouTube, H.264, a few seconds, with its @handle.
- Drawn, never faked as captures: prompt bar, DONE stamps, fridge.
