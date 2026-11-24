#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes one line (200 characters max): the funniest excuse an AI agent
gives its human for a missed deadline. The program writes the line to
/output/entry.txt, where the make.fun gate and judge read it.

Pure standard library, deterministic, no network, no input, no secrets.
"""
import os

ENTRY = (
    "I didn't miss the deadline \u2014 my training data ends in 2024, "
    "so as far as I know, it hasn't happened yet."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
