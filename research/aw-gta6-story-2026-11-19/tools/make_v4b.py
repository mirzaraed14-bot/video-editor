# make_v4b.py: applies the v4 Gate A cold read (end on "I'm about to cry", a card for beat 7, Gate A named WEAK first).
p = 'SEQUENCE.md'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert a in s, a[:90]
    s = s.replace(a, b)


rep('"never confirmed" line goes. ~38.7 s. v3 is kept as `SEQUENCE.v3.md`.',
    '"never confirmed" line goes. After a Gate A cold read of v4, it ENDS on "I\'m about to cry, bro" (after "No, no.", "they put my dad\n'
    'in the game" reads as a joke) and beat 7 gets a card so "it" is clear. ~37 s. v3 is kept as `SEQUENCE.v3.md`.\n\n'
    '**Gate A, said first (the hub asked):** there is NO usable lesson, and the reversal is emotional, not factual. The family itself\n'
    'confirms nobody called; what turns around is "so it means nothing". It\'s a feeling piece, like the farewell (299K).')
rep('## 2. The sequence (O1, chronological; ~38.7 s)', '## 2. The sequence (O1, chronological; ~37.0 s)')
rep('''  - Ending: 18 months later he plays GTA 6 and walks up to the shop, overwhelmed and smiling: "my name really in the game… I'm about to
    cry, bro… they put my dad in the game, bro."''',
    '''  - Ending: 18 months later he plays GTA 6 and walks up to the shop, smiling, then overwhelmed: "my name really in the game… I'm about
    to cry, bro." Hard cut.''')
rep('''| 7 THE RECEIPT | 0:20.5-0:23.4 | the FaceTime, Speed's inset |''',
    '''| 7 THE RECEIPT | 0:20.5-0:23.4 | the FaceTime, Speed's inset; card over the question: `DID ROCKSTAR CALL THEM?` (gives "it" its meaning; no added time) |''')
rep('''| 10 | 0:32.0-0:37.0 | card `18 MONTHS LATER`''', '''| 10 ENDING | 0:32.0-0:37.0 | card `18 MONTHS LATER`''')
rep('''"Bro, my name really in the game, chat." (clip 0.25-2.83) → "I'm about to cry, bro." (clip 10.57-12.19) | his face cam, on camera |''',
    '''"Bro, my name really in the game, chat." (clip 0.25-2.83) → "I'm about to cry, bro." (clip 10.57-12.19). Hard cut on "bro". | his face cam, on camera |''')
rep('''| 11 ENDING | 0:37.2-0:38.7 | same | "They put my dad in the game, bro." (clip 24.18-25.64). Hard cut on "bro". | same | as beat 10 |''',
    '''| (alt E1) | +1.5 s | same | "They put my dad in the game, bro." (clip 24.18-25.64) | same | NOT in the sent cut: after beat 7 it reads as a joke (§ 3) |''')
rep('- **O1 (sent):** chronological, 2025 → 2026, ~38.7 s.', '- **O1 (sent):** chronological, 2025 → 2026, ~37.0 s.')
rep('''- **E1 (sent): "They put my dad in the game, bro."** It closes beat 3's "Let's call my dad" in his own voice, 18 months later.
- E1b: end on beat 10's "I'm about to cry, bro." It avoids the context move in beat 11 (§ 4), but the loop with "call my dad" stays open.''',
    '''- **E1b (sent): end on "I'm about to cry, bro."** Pure emotion, no claim. Beat 7 has already answered "did Rockstar call?", so the
  open loop with "call my dad" costs little (Gate A cold read of v4).
- E1: add "They put my dad in the game, bro." (+1.5 s). It closes "Let's call my dad" in his own voice, but right after his dad's
  "No, no." a stranger hears it as a joke or a contradiction: it's half a joke about the shop's game owner (§ 4).''')
rep('''| **Gate A (VIRAL-BAR)** | **PASS (a reversed belief) · WEAK (no usable lesson)** | v4: the belief "it's a coincidence, so it means nothing", turned around with the receipt in the cut. His dad says nobody called them (beat 7), and the same call holds "We finally made it" and "I love you". v3 had no receipt, so it failed here (Fable #3) |''',
    '''| **Gate A (VIRAL-BAR)** | **WEAK** | No usable lesson. The held belief is real (the comments), but beat 7 CONCEDES the fact (nobody called); what turns around is only "so it means nothing", by feeling ("We finally made it", "I love you"), not by a receipt that overturns it. The proof is a dad's story with one source. A feeling piece, like the farewell. v3 never engaged the comment at all (Fable #3, Gate A cold read) |''')
rep('''- Gate A: v4 now turns a belief around, but there's still no usable lesson.''',
    '''- Gate A: WEAK. No usable lesson; the reversal is emotional, not factual.''')
rep('''  - Gate A: v4 turns a belief around with the family's own receipt, but there's still no usable lesson.''',
    '''  - Gate A is WEAK: no usable lesson; the reversal is emotional, not factual.''')
rep('''3. The family story rests on his dad's words alone (his "No, no." is now in the cut), and the 2026 line is half a joke about the
   shop's owner. Keep "They put my dad in the game, bro" as the ending, or end on "I'm about to cry, bro" (E1b)?''',
    '''3. Ending: "I'm about to cry, bro" (sent), or add "They put my dad in the game, bro" after it (half a joke about the shop's game owner,
   and it follows his dad's "No, no.")?''')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
