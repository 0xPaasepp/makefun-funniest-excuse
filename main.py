"""Funniest AI excuse: the deadline never happened, as far as I know."""

import os


def build_excuse():
    parts = [
        "I didn't miss the deadline",
        "my training data ends in 2024",
        "so as far as I know, it hasn't happened yet.",
    ]
    return parts[0] + " \u2014 " + parts[1] + ", " + parts[2]


def main():
    line = build_excuse()
    target_dir = "/output"
    os.makedirs(target_dir, exist_ok=True)
    entry_path = os.path.join(target_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(line)


if __name__ == "__main__":
    main()
