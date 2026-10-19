# Scott D. Clary (Success Story Podcast) · client Shorts: ENGINE

Channel folder per the shorts-engine method (Affan, 2026-10-19). Every number about THIS channel lives here, never in another channel's
files. Read this first on any Scott job, then FINDINGS.md, then the job's row in RESULTS.md.

## The line for one Short
1. **Pick** (Claude): read the episode transcript in full (the show's RSS `podcast:transcript` VTT, never YouTube), score candidates on
   the viral bar (`projects/_onyx-batch3-2026-10/VIRAL-BAR.md`, gates A-E), give them to Affan as text (hook, beats with times, button).
2. **Freshness** (Claude + Affan): web search for the story AT THIS ANGLE (no YouTube requests from this machine); Affan scrolls
   Scott's own Shorts tab for the episode before posting. A prior Short on the same story + angle disqualifies it.
3. **Lock the prediction** in RESULTS.md BEFORE upload: view range at 7 days + the single biggest failure reason, Claude AND Affan,
   plus the pre-mortem (3 reasons it got 5K, 3 reasons it got 5M). Never edited afterwards.
4. **Affan sequences** it in Premiere and records a Tella walkthrough; **Claude builds** it with
   `presets/youtube-shorts/onyx-samples-youtube/CLIENT-SHORT-RECIPE.md`.
5. **Title + thumbnail** ship with the Short (format below).
6. **After 7 days** (never sooner): views, stayed-to-watch, average view %, subs gained, feed share into RESULTS.md, then the
   post-mortem: name the assumption that failed or held, and move it into FINDINGS.md (validated, or FALSIFIED with the date).

## Channel overrides (decided by Affan)
- The look: the YouTube "Sean Ryan" kit (onyx-samples-youtube), watermark "SUCCESS STORY WITH SCOTT D. CLARY", no CTA, no Onyx.
- **No music bed** in our export: Affan adds it. SFX on every graphic.
- **Never the Abundance Wisdom grade / letterbox look** (faceless videos only, 2026-10-19). AW head lock is welcome.
- His sequencing is followed exactly; popular faces beat brand faces ("50 Cent, not LL Cool J").

## Title + thumbnail format (locked 2026-10-19; never changed per video)
- **Title** carries the FULL reversal and the name (search value): "Ryan Serhant saw a bank CEO's calendar. It was almost empty."
- **Thumbnail**: a real photo of the person or the event (never a talking-head frame of the podcast), full-bleed 9:16; 2-4 words in Anton
  caps, white with a black outline, centred at ~66 % of the height; **exactly one word in teal #19D3C5**; a sentence fragment, not a
  summary; no logos. Built by `python presets/youtube-shorts/scott-clary/thumbnail.py PHOTO OUT.jpg "LINE ONE" "LINE TWO" --teal WORD`.
