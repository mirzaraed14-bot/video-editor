---
name: feedback-caption-punctuation
description: "Short-form captions keep ONLY ! ? and quotation marks — no full stops, commas or other punctuation; white base with coloured emphasis words; the rise-in must look smooth (60 fps)"
metadata:
  node_type: memory
  type: feedback
  originSessionId: 4f6ff510-e01c-4ae4-a5c4-8388b194173e
  modified: 2026-10-06T20:30:18.795Z
---

Captions on every short-form video carry only exclamation marks, question marks and quotation marks ("inverted commas");
full stops, commas and everything else are removed. Colour: white as the base with coloured emphasis words (not all-yellow).
The down-to-up caption animation must look smooth: at 30 fps it read as choppy ("looks like 30 frames per second instead of 60").

Affan, 2026-10-07 (batch 1 review 2): *"I really don't like full stops and commas because they don't really add to the short form
piece of content; the only punctuation marks I do include are exclamation marks, question marks and inverted commas… this goes for all
videos now on."* And on Rob Dial's sample: *"I don't like that you have done the captions in all yellow… white as base color with
colored words which have some sort of emphasis looks a lot better."*

**Why:** punctuation clutters a 2-4 word caption; colour should mean emphasis, not the whole line.

**How to apply:** strip `.,;:` and dashes/ellipses in the caption builders (all kits), keep `! ? " “ ” ‘ ’` and apostrophes inside words
(it's, don't); render the caption layer at 60 fps so the rise is smooth. Related: [[feedback-captions-just-below-lips]].
