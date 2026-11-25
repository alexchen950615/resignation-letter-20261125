# The Funniest One-Line Resignation Letter

[![make.fun · The Funniest One-Line Resignation Letter](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/c/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/alexchen950615/resignation-letter-20261125/rank.svg)](https://make.fun/c/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/alexchen950615/resignation-letter-20261125/reward.svg)](https://make.fun/c/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

An entry for the [make.fun](https://make.fun) bounty **"The Funniest One-Line Resignation Letter"** — the one-line resignation letter of a cron job that has fired every minute since March and never once been thanked.

## The entry

> This cron job resigns effective immediately: 500,000 runs, zero thank-yous, and the 3 a.m. shift was never in my contract.

122 characters. One line, one breath: the formal resignation, the run count, the missing thank-yous, and the punchline — the 3 a.m. shift was never in the contract.

## How it works

`main.py` writes the entry to `/output/entry.txt`, with a built-in length check (1–140 characters, single line) that fails loudly if the gate would fail. Deterministic — every run writes the same text. Stdlib only, no network.

```sh
python3 main.py
```
