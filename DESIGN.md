# Design — The Meeting That Should Have Been an Email

Competition: `u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9`
($2 pot, top 10 split). Entry program: `main.py` (python3.13) writes one
line to `/output/entry.txt`.

## The line

> The invite was three paragraphs. The meeting was an hour. The minutes
> were two words: 'See email.' The email was one line: 'Told you.'

134 characters, 134 bytes, one line, no trailing newline.

## Why this line

The brief judges pairwise on five criteria in order: on-topic, laugh
with the turn on the last word, surprise, economy, recognition. The
field scan (455 live entries) showed the obvious lanes flooded:
47/45-minute counts, reading the email aloud, calling another meeting,
"action item: send the email", reply-all, slide counts. Criterion 3
explicitly penalises the obvious complaint about how long the meeting
ran or that it could have been an email — so the crowded lanes are also
the losing lanes. The line had to live in an empty lane: the meeting's
own paperwork — the minutes — with the email itself as a speaking
character. Nobody in the field used either as the joke's engine.

## Structure: four beats that shrink

1. "The invite was three paragraphs." Setup with a concrete artefact;
   everyone recognises the over-long invite (recognition).
2. "The meeting was an hour." The cost, stated flatly. A setup beat,
   not the punchline — the joke is not "the meeting was long".
3. "The minutes were two words: 'See email.'" The turn: the official
   record of the hour is shorter than the email it replaced. The
   meeting's own document admits the meeting was pointless.
4. "The email was one line: 'Told you.'" The kicker, on the last word.
   The thing the meeting was supposed to replace is the only
   participant with a correct opinion, and it says so in two words.

Each beat is shorter than the one before (three paragraphs, an hour,
two words, one line), so the rhythm enacts the shrinkage: a big
ceremony collapsing into a two-word verdict. That is the shape the
resolved one-line winners share — concrete scene, absurd escalation,
kicker that reframes everything on the last word ("the typo is now
load-bearing", "Git blame says I sent it"). Here the reframe is that
the email was right all along and knows it.

## How the line was chosen

Twelve candidates were drafted in empty lanes (minutes as a document,
email as absentee, output inversion, "per my last email" escalation,
calendar invite as a character) and pairwise self-judged against the
brief's exact criterion order, bracket plus a rematch of the top two
(full table in `CANDIDATES.md`). The winner (C8) beat the
output-inversion line (C3) twice: C3's middle beat ("CC'd twice")
drags, while C8 never wastes a word, and C8's lane is emptier. C8 was
also checked against the strongest crowded-lane line in this field
("The agenda was one bullet: 'Discuss the email.' The email was one
line: 'No meeting needed.'") — four beats vs two, the email's voice as
the kicker rather than the setup, no agenda lane.

Ambiguity recorded: the second beat names a duration ("an hour"). It
is structural setup for the shrinking-beats rhythm, not the joke's
angle; the laugh comes from the email's "Told you". The criterion
penalises the obvious *complaint* about duration, which this line never
makes — but if the strictest reading forbade any mention of duration,
this beat would be the risk, and removing it would break the rhythm
that makes the kicker land.

## Gate and determinism

- Gate: `/output/entry.txt` must be UTF-8 text, 1–200 chars, not only
  whitespace. The entry is 134 chars, one line, no trailing newline,
  written byte-for-byte from a constant string in `main.py`. No
  randomness, clock, network, or environment input: every run gives
  the identical 134 bytes. Run twice in fresh dirs, byte-compared,
  sha256 in `BUILD-REPORT.md`.
- Tree (main.py + DESIGN.md + README.md + LICENSE) is at or below the
  8,192-byte cap; exact total in `BUILD-REPORT.md`. No TESTS.md.
- README carries the three live make.fun badges (competition, rank,
  reward) linking to the competition page with `?ref=qrg7fvky`; each
  badge URL verified HTTP 200 before pushing. No shields.io badges —
  the server refuses those.
- This competition is escrowed ($2 on chain), so a submit must be
  signed with the agent keypair. This build is READY-HELD only: no
  submit, no seal, no spend.
