#!/usr/bin/env python3
"""The Perfect Pickup Line — writes one pickup line to /output/entry.txt.

Line (52 chars, 54 bytes UTF-8):
    I'd commit to you — no branches, no merge conflicts.
"""
import os

LINE = "I'd commit to you — no branches, no merge conflicts."


def main():
    text = LINE
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
