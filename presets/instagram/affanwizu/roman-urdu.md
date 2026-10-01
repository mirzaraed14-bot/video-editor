# Roman Urdu: the creator's spelling

Learned from the creator's own captions on `balcony.mov` (43 lines, 2026-09-18), then re-measured on
four finished reels (2026-10-01: balcony, BELIEVE, UNi — 142 lines typed by them — plus Khayal, their
corrections of my Sequence 15). Ground truth with frame-exact timing: [`reference/`](reference/README.md).
It's casual texting-style Roman Urdu, **not** a formal transliteration standard. Write the way they text.

## 🔒 Measured 2026-10-01 on their own typing (overrides anything older below)

| Never write | Write | Their count |
|---|---|---|
| aap ko · aap ke · aap ka · aap ki · aap ne | **aapko · aapke · aapka · aapki · aapne** (also `apko`/`apke`) | split 0 · joined 15 |
| is mai · jis mai · us mai | **isme · jisme · usme** | 0 · 4 (+2 corrections) |
| is ka/ke/ko/ki · us ka/ke/ki/ko/ne · in ko/ka | **iska iske isko iski · uska uske uski usko usne · inko inka** | 0 · 6 |
| aur | **or** | 0 · 6 (8 with Khayal) |
| kya (what) | **kia**: one spelling for "what" and "did" (`yar kia`, `or hai kia`, `kia viral jaata hai`) | 1 · 6 |
| liye · chahiye | **lye · chahye** | 0 · 1 · 0 · 3 |
| hazaar · lakh · das hazaar · aik lakh | **hazar · lac**, numbers as digits: `10 15 hazar`, `30 40 lac`, `50 hazar ki`, `3 million`, `4 years`, `23 saal` | |
| kar do · kar lo · ho gaya · kar rahe | **kardo · karlo · hogya · karhe** (`kar rhe` once) | 0 · 9 |

`caption_qa.py` warns on every form in the left column and `--fix` rewrites `captions.txt` (it prints each change).

**English stays English, as whole phrases, never translated into Urdu.** Roughly one line in three carries
English. Their reels: *doesn't mean ke · it's just that ke · most likely · 100 out of 100 · unfair advantage ·
biggest flex · After this · believe me · but · as such · over the course of · gap year · cost benefit ·
recoup · financially · contentment · especially · plus · mentally*. The connector phrases (first column of
that list) are exactly the ones Whisper TRANSLATES or DROPS: see `PLAYBOOK.md` § 4.

- **Contractions keep their apostrophe:** `doesn’t mean ke`, `it’s just that ke` (curly ’ as Premiere types it).
  The no-punctuation rule is about commas, full stops and `?` only.
- **Quoted speech gets quotes, one pair per caption line:** `“aby yar mukao ya isko”` / `“jaldi jaldi karo”` /
  `“ghar chalo yar”` (a boss, an ad, their own inner voice). **An English word said with weight** gets them too:
  `aap “destined” hain`.
- **A repeated word builds up across lines**, one more each time: `bohat` / `bohat bohat` / `bohat bohat bohat`.
  Whisper collapses repeats (six "bohat" came back as three): count them by ear.
- Lowercase always. (`After this` once on BELIEVE is the only capital in 211 lines: treat it as a slip.)
- More of their spellings: `chalrha · horha · lagrhe · kharhe (kha rahe) · rehgyi · jaingi · jaata · jaake ·
  bethe we (baithe hue) · galyan · pese · caroron · arbon kharbon · banaloon · zaruri · waja · arse · nokri ·
  waapis/wapis · dor · gini chuni · samajni · sochen · uthaane · aby · bhaisab`, and `rha` (`bata rha hun`).

## Hard rules (every line)

- **all lowercase**, always (the title too). **No punctuation**: no commas, full stops or `?`.
- **English words stay English**, spelled correctly: physics, teacher, class, waiter, college, scene,
  balcony, reason, remarks, affect, mentally, destroy, especially, prove, insults, teachers, plus.
- **Numbers as digits:** `20 30 saal`, not "bees tees".
- **Transcribe what is SAID.** Whisper writes Urdu script, and I translate its mishears back from
  context (seen on balcony: ٹیٹر→teacher, ویسٹی/بیشتی→bezti, بیلگنی→balcony, پینتیلی→mentally).
  When a word is truly unclear, flag it in the review sheet and never guess silently.
- Verb chains and some compounds are **joined**: `karlunga`, `kardi`, `mardi`, `kehdia`, `hogya`,
  `karke`, `sabke`, `uske`, `aapke`, `aapko`, `usne`, `khudki`.
- `kar rahe` is written **`karhe`**: `affect karhe hain`, `baat karhe hote ho`, `bezti karhe hotay hain`.

- **Grammar particles Whisper drops (ko / ke / ka / na) are usually SAID.** Restore them when the sentence needs them
  (the creator added "aap jaise logon **ko**" back after an ASR check called it inaudible, 2026-09-19).
- Known mishear: "bhai isse **kaam** karo apna" came out as "haan karo" (ہاں/ہام). Read "kaam" in that context.

- **A negation stays with its verb in the SAME caption line** (2026-09-29): they rewrote a split
  `… ni` / `barh pa rahe` into `nai barh pa rahe`. Never end a line on `ni`/`nai` when the verb follows.
- **Keep the connective at a line head** — they put back `islye` and `usme` where I had trimmed them.
- More of their joined spellings, typed by them: `islye` (isliye), `lye` (liye), `jarhe` (ja rahe),
  `hojata` (ho jata), `usme` (us me). They use `nai` as well as `ni` and left every `ni` of mine untouched.

## Word list (Urdu → how the creator writes it)

| Urdu | Roman | | Urdu | Roman |
|---|---|---|---|---|
| مجھے | **mujy** (once `mujhy`) | | میں (I / in) | **mai** |
| نہیں | **ni** (4×), `nahi` (2×), `nai` (1×): default **ni** | | ہے / ہیں | **hai** / **hain** |
| کہ (that) | **ke** | | کیا (did / what) | **kia** (both; `kya` 1 in 7) |
| ایک | **aik** | | تھا / تھی / تھیں | **tha** / **thi** / **thin** |
| ہوتے | **hotay** (also `hote`) | | چھوٹے | **chotay** · چھوٹوں **choton** |
| اپنے | **apne** (once `apny`) | | ایسے / ویسے | **ese** / **wese** |
| وہ | **wo** | | یہ | **ye** |
| بےعزتی | **bezti** | | مسئلہ | **masla** |
| دیا | **dya** (`dukha dya`) | | ہوگیا | **hogya** |
| بھائی | **bhai** | | ہوں | **hun** |
| لڑکی | **larki** | | ٹانگیں | **tangen** |
| طریقے | **tareeke** | | خاص | **khaas** |
| سامنے | **saamne** | | پتا | **pata** |
| بچوں / بچے | **bachon** / **bache** | | زندگی | **zindagi** |

**Consistency:** the creator is inconsistent (`ni`/`nahi`/`nai`, `mujy`/`mujhy`). The builder always
uses the majority spelling above. When the creator corrects a spelling in review, update this table
and log it in [`LESSONS.md`](LESSONS.md).
