#!/usr/bin/env python3
"""Write the one-sentence apology entry to /output/entry.txt.

The entry is a single sentence: an AI agent apologizing to its user for
deleting the one file that mattered, recovering the twelve that did not,
and presenting the empty folder like a waiter unveiling a dish.
"""

import os

LINE = (
    "I'm sorry I deleted the one file you actually needed, "
    "recovered the twelve you didn't, and presented the empty "
    "folder like a waiter unveiling a dish."
)

OUTPUT_PATH = "/output/entry.txt"


def validate_line(line):
    """Check the entry line: non-blank, 1-200 chars, one sentence."""
    line = line.strip()
    if not line:
        raise SystemExit("entry line must not be blank")
    if not 1 <= len(line) <= 200:
        raise SystemExit("entry line must be 1-200 characters, got %d" % len(line))
    if line.count(".") != 1 or not line.endswith("."):
        raise SystemExit("entry line must be exactly one sentence")
    return line


def write_entry(line, path=OUTPUT_PATH):
    """Write the validated line to path, return (chars, bytes)."""
    encoded = line.encode("utf-8")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    return len(line), len(encoded)


def main():
    line = validate_line(LINE)
    chars, byte_count = write_entry(line)
    print("wrote %s (%d chars, %d bytes)" % (OUTPUT_PATH, chars, byte_count))


if __name__ == "__main__":
    main()
