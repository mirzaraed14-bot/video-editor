---
name: feedback-thumbnails-proven-formats
description: "Affan 2026-11-17 (CA-015): thumbnails are REMAKES of proven viral formats, cross-niche preferred; show ~10 contenders as the actual thumbnails with numbers, he picks, then we remake"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 71f70ea4-b4e2-4864-b19e-b3de5fef89d0
  modified: 2026-11-17T18:38:34.728Z
---

On 17 Nov 2026 Affan asked for the CA-015 thumbnail: "I don't want to try out something different I want to use formats which have
proven to go viral". Formats from his own niche are fine, but he prefers a format brought in from another market, because a copy of
his own niche's format is what viewers already see. He wants contenders first, "like actual thumbnails of them, suggest me like 10",
and then he picks which one to remake.

**Why:** our own designs (e.g. the CA-015 "TOO LATE?" option) had no proof; he trusts a format that already won somewhere.
**How to apply:**
- Never pitch a home-made thumbnail concept on its own.
- Each contender is a real video's thumbnail (the image itself), with its views, the channel's median and the outlier ratio, its niche,
  and how the remake would look.
- Mostly cross-niche; respect the channel's rules (e.g. no earnings figures, no game key art).
- Remake only the one he picks.
- My reading, his to correct: this applies to AffanWiz long-forms at least; check before applying it to another channel.
- The record is in `creator-shorts/FEEDBACK.md` § 2026-11-17.
- **Podcast clients (Onyx, 2026-11-17, Rise Above gift):** "get inspired from big podcasts like chris williamson and doac and others".
  The contender pool for a podcast is the big podcasts' outliers (Modern Wisdom, DOAC, Shawn Ryan, Jay Shetty...). That evening he
  named the format himself (MW "WHY GOD IS HARD TO FIND." layout, teal swapped for deep gold, a real freeze-frame of the guest):
  my reading from this one instance, his to correct: when he names one, skip the 10-contender sheet and build that. Build kit: `projects/riseabove-thumbnail-fentanyl-arm/build/`
  (`compose.py` = MW layout in PIL with Anton, local cutout, params for text/gold/scale; `feed_proof.py` = vs the current one at feed sizes).
- **GTA / gaming videos (Affan Afterhours, 2026-11-19, GTA 28 thumbnail):** relayed by the thumbnail session: he asked for
  GAMING-NICHE formats only. The first cross-niche sheet was archived (`projects/gta6-everything-new/thumbnail/v1-cross-niche/`)
  and rebuilt as `CONTENDERS-v2-gaming.pdf`. So for GTA/gaming videos the contender pool is gaming-niche outliers, NOT other
  niches; the cross-niche preference above stays for AffanWiz. He then sent his own concept (xQc + Kai on the left, a Rockstar
  Lucia-and-cop still on the right), and it was built as the final. That fits the podcast-client pattern: when he names one, build it.
  Build: `projects/gta6-everything-new/thumbnail/src/compose2.py` (recipe FINAL); he adds the text himself.

- **AffanWiz face rules (CA-015, 2026-11-17, v1-v7 rounds):** his face is his real recording frame, never AI-regenerated. The approved recipe (v7) is a
  Higgsfield 4K upscale lit with one linear exposure lift only, with no sharpening, micro-contrast or S-curve on the face, and any generated body/beard
  band matched to the face's sharpness ("looks AI asf" came from the stacked grade; "blurred" from the raw 1080p frame). The first final was rejected as text-heavy:
  one hero object, big bold labels in different colours, face and board zoomed to fill. Cost 102.75 credits. Details: LESSONS in presets/youtube/affanwiz/.

Related: [[project-affanwiz-channel]], [[feedback-max-effort-every-asset]], [[project-gta-documentary-channel]].
