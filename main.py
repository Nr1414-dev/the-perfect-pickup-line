#!/usr/bin/env python3
"""The Perfect Pickup Line — writes one pickup line to /output/entry.txt.

Line (52 chars, 54 bytes UTF-8):
    I'd commit to you — no branches, no merge conflicts.
"""
import os
import unicodedata

LINE = "I'd commit to you — no branches, no merge conflicts."


def main():
    text = LINE
    # Gate counts characters (Unicode code points), not bytes or UTF-16 units.
    if not (1 <= len(text) <= 200):
        raise SystemExit("entry must be 1-200 characters")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if any(unicodedata.category(ch).startswith("C") for ch in text):
        raise SystemExit("entry must not contain control characters")
    if text != text.strip():
        raise SystemExit("entry must not have leading or trailing whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)
    # Read back and confirm the file on disk is byte-identical to the line.
    with open("/output/entry.txt", "rb") as f:
        if f.read() != text.encode("utf-8"):
            raise SystemExit("written entry does not match the line")


if __name__ == "__main__":
    main()
