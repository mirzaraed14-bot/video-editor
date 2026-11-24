# make_v4.py: applies the v4 changes (hub's checks + Fable #3) to SEQUENCE.md. Run once from the session folder.
p = 'SEQUENCE.md'
s = open(p, encoding='utf-8').read()


def rep(a, b):
    global s
    assert a in s, a[:90]
    s = s.replace(a, b)


rep('(sequence in text, v3, 19 Nov ~20:40 PKT; nothing built)',
    '(sequence in text, v4, 19 Nov ~21:05 PKT; supersedes v3; nothing built)\n\n'
    '**v4 = the hub\'s three checks + Fable #3 on Gate A.** The family\'s own receipt is back in the cut (Speed: "Did it like contact you?" /\n'
    'his dad: "No, no."), so the Short says out loud that it\'s probably a coincidence and still lands "We finally made it". The on-screen\n'
    '"never confirmed" line goes. ~38.7 s. v3 is kept as `SEQUENCE.v3.md`.')

rep('''- **The viewer gets:** it doesn't matter whether Rockstar meant it. To the loudest streamer alive, a shop sign in a video game was the
  auto parts store his dad says the family opened after the Korean War and lost when cars changed, and the first thing he did was call
  his dad. The judgment it turns around: "he's just yelling about a common name."''',
    '''- **The viewer gets (the belief turned around):** "it's a coincidence, so it means nothing." His own dad says nobody from Rockstar
  called them, and it still meant everything: "We finally made it", for the auto parts store his dad says the family opened after the
  Korean War and lost when cars changed. A thing doesn't have to be made for you to mean something to you. And the first thing the
  loudest streamer alive did was call his dad.''')

rep('''  - Turn: he calls his dad. His dad: "We finally made it… That's the old company"; back from the Korean War, he "invested his money
    into auto shop"; "we still run a name, but we don't have the company"; "we couldn't keep up with the parts". Then "Dad, I love
    you." "Love you too, man."''',
    '''  - Turn: he calls his dad. His dad: "We finally made it… That's the old company"; back from the Korean War, he "invested his money
    into auto shop". Speed: "Did it like contact you?" Dad: "No, no." Then "we still run a name, but we don't have the company… we
    couldn't keep up with the parts". Then "Dad, I love you." "Love you too, man."''')

rep('## 2. The sequence (O1, chronological; ~35.6 s)', '## 2. The sequence (O1, chronological; ~38.7 s)')

start = s.index('| 7 | 0:20.5-0:26.6')
end = s.index('**Every speaker is named on screen:**')
new_rows = '''| 7 THE RECEIPT | 0:20.5-0:23.4 | the FaceTime, Speed's inset | Speed: "Did it like contact you?" (1694.82-1696.30) · Dad: "No, no." (1697.72-1698.76) [the 1.4 s gap tightened to 0.3 s; Speed's "Did you know about it or no?" just before it is cut] | Speed on his own mic (-16 dBFS, loud) / the dad 155 Hz at -18 dBFS | OURS: the family's own answer to "is it really about you?" |
| 8 | 0:23.6-0:29.7 | the dad | [trimmed: "See what it was is that they wanted to keep it like… They like the name is still in, we"] "We still run a name, but we don't have the company." (1706.47-1708.77) → "When they started changing cars, we couldn't keep up with the parts." (1720.08-1723.72) | dad: 146-192 Hz, quiet | OURS: the loss |
| 9 | 0:29.9-0:31.8 | Speed smiling at the phone / the dad | Speed: "All right, Dad, I love you." (1754.14-1754.88) · Dad: "All right, love you too, man." (1756.14-1757.09) | Speed 211 Hz / dad 181 Hz at -23 dBFS | OURS |
| 10 | 0:32.0-0:37.0 | card `18 MONTHS LATER` (0.6 s). Then top: GTA 6 gameplay, his character at the real WATKINS AUTO PARTS storefront (daylight, the sign above the door); bottom: Speed's face cam (red sweater, headset). He's smiling at "my name"; at "about to cry" he is overwhelmed: he leaves his chair, comes back and holds his head over his headset. The picture stays on the frames that match each line. Label `ISHOWSPEED · 18 NOV 2026` | "Bro, my name really in the game, chat." (clip 0.25-2.83) → "I'm about to cry, bro." (clip 10.57-12.19) | his face cam, on camera | Words proven: the stream audio inside fan clip `g_sN6aWzrOE` (WhisperX), the same words Sportskeeda quotes. The original: VOD `qSyo5d-dVzA` (1080p60), offset to find (§ 9) |
| 11 ENDING | 0:37.2-0:38.7 | same | "They put my dad in the game, bro." (clip 24.18-25.64). Hard cut on "bro". | same | as beat 10 |

'''
s = s[:start] + new_rows + s[end:]

rep('- **O1 (sent):** chronological, 2025 → 2026, ~35.6 s.',
    '- **O1 (sent):** chronological, 2025 → 2026, ~38.7 s.\n'
    '- v3 (sent earlier to the hub): the same without beat 7, with a `ROCKSTAR NEVER CONFIRMED A LINK` line on the ending (~35.6 s).')
rep('''- E1b: end on beat 9's "I'm about to cry, bro." It avoids the context move in beat 10 (§ 4), but the loop with "call my dad" stays open.''',
    '''- E1b: end on beat 10's "I'm about to cry, bro." It avoids the context move in beat 11 (§ 4), but the loop with "call my dad" stays open.''')
rep('''- E2: end on beat 8, "Love you too, man",''', '''- E2: end on beat 9, "Love you too, man",''')
rep('''- "Did it like contact you?" "No, no.": kept OUT of the cut but IN the facts (§ 4).''',
    '''- v3 kept "Did it like contact you?" "No, no." out. v4 puts it back (Fable #3): without it, the Short never answers the comment it
  turns around.''')
rep('''Darren Watkins Sr. ("DaddySpeed", 590K subs, `api/daddyspeed_stats.json`).''',
    '''Darren Watkins Sr. ("DaddySpeed", 590K subs, `api/daddyspeed_stats.json`; born 1983 as REPORTED by low-tier bio sites).''')
rep('''  - The Short never says Rockstar did it on purpose; it carries only their own words.
  - The hook says "family name" (his surname), not "family".
  - Beat 10 carries `ROCKSTAR NEVER CONFIRMED A LINK` (small, in the bottom band, no added time; your call to remove it).''',
    '''  - The Short never says Rockstar did it on purpose. It carries only their own words, and beat 7 says it out loud ("No, no.").
  - The hook says "family name" (his surname), not "family".
  - There's no "never confirmed" line on screen any more, because the receipt is in the cut. (Your call to put it back.)''')
rep('''  - Checked outside the stream (19 Nov ~20:55, 2 web searches): no record, directory listing or article of a Watkins auto parts store
    tied to the family. Nothing contradicts it either. Unverified.''',
    '''  - Checked outside the stream (19 Nov ~20:55-21:00, 3 web searches: Cincinnati, Detroit/Michigan, and the family + the Korean War):
    no record, directory listing or article of a Watkins auto parts store tied to the family. Nothing contradicts it either.
    Unverified. On the call Speed sums it up as "different owners basically", so the name may still trade somewhere.''')
rep('''  - **Named as a context move:** placed after the 2025 call, it lands as his real dad. The on-screen line `ROCKSTAR NEVER CONFIRMED A
    LINK` keeps the cut honest. E1b (end on "I'm about to cry") avoids the move entirely.''',
    '''  - **Named as a context move:** placed after the 2025 call, it lands as his real dad. Beat 7 has already told the viewer that nobody
    called the family, so it reads as his joy, not as a claim. E1b (end on "I'm about to cry") avoids the move entirely.''')
rep('''| **Gate A (VIRAL-BAR)** | **WEAK** | The payoff turns around a judgment ("he's yelling about a common name") and lands a feeling, not a usable lesson. The plain one inside it: he called his dad |''',
    '''| **Gate A (VIRAL-BAR)** | **PASS (a reversed belief) · WEAK (no usable lesson)** | v4: the belief "it's a coincidence, so it means nothing", turned around with the receipt in the cut. His dad says nobody called them (beat 7), and the same call holds "We finally made it" and "I love you". v3 had no receipt, so it failed here (Fable #3) |''')
rep('''**Weakest, named first:**
- Gate A: a feeling, not a lesson.''', '''**Weakest, named first:**
- Gate A: v4 now turns a belief around, but there's still no usable lesson.''')
rep('''  - Gate A is WEAK: a feeling, not a lesson.''',
    '''  - Gate A: v4 turns a belief around with the family's own receipt, but there's still no usable lesson.''')
rep('''- **Biggest risk:** Speed fans swipe''',
    '''- **Dated note, 19 Nov ~21:00 (Fable #3; the lock stands, the read changes):** the three "dad Shorts" above are all Michael Jackson
  Shorts. In the same 30 uploads, the 12 non-MJ Shorts have a median of 32.4K (MJ: 132.6K), and the only GTA/Speed lane points are the
  farewell 299K and the Speed Short 70K. **Honest read: AT the 150K bar, not above it.** The 200K lock was already sent, so it stays.
- **Biggest risk:** Speed fans swipe''')
rep('''3. The family story rests on his dad's words alone, and the 2026 line is half a joke about the shop's owner. Keep the ending with the
   small `ROCKSTAR NEVER CONFIRMED A LINK` line (sent), or end on "I'm about to cry, bro" (E1b)?''',
    '''3. The family story rests on his dad's words alone (his "No, no." is now in the cut), and the 2026 line is half a joke about the
   shop's owner. Keep "They put my dad in the game, bro" as the ending, or end on "I'm about to cry, bro" (E1b)?''')
rep('''4. Restore "1950" in beat 6, or keep it trimmed?''',
    '''4. Restore "1950" in beat 6, or keep it trimmed?
5. The Darren Short (aw-speed-beats, waiting for your OK) is about the same name. Either (a) two separate Shorts, this one FIRST
   because launch week won't wait (my pick); or (b) this Watkins payoff as the Darren Short's ending. (b) joins a loneliness arc to a
   joy payoff, which makes two topics.''')
open(p, 'w', encoding='utf-8').write(s)
print('ok')
