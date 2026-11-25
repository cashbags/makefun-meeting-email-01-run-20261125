#!/usr/bin/env python3
"""Entry program for the make.fun competition
"The Meeting That Should Have Been an Email"
(u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9).

Writes exactly one line of plain text -- the winning one-liner chosen
by the pairwise tournament in CANDIDATES.md -- to /output/entry.txt.
The write is deterministic: the same constant line, no randomness, no
clock, no network, no trailing newline, so every run produces the
identical 134 bytes.
"""

import os

LINE = (
    "The invite was three paragraphs. The meeting was an hour. "
    "The minutes were two words: 'See email.' "
    "The email was one line: 'Told you.'"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
