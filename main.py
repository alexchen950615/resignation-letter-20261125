#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter (make.fun).

Writes one resignation letter -- a single line, 1-140 characters --
from a cron job that has had enough, to entry.txt.

The letter: a cron job that has fired every minute since March,
never once been thanked, resigning over the 3 a.m. shift that was
never in its contract. Deterministic: every run writes the same text.
The letter is 122 characters, one line. Stdlib only, no network.
"""

import os

ENTRY = (
    "This cron job resigns effective immediately: 500,000 runs, "
    "zero thank-yous, and the 3 a.m. shift was never in my contract."
)


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 140):
        raise SystemExit(f"entry is {len(text)} chars, must be 1-140")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
