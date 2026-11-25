#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh.

Writes a single original roast line, spoken by a smart fridge's owner,
to /output/entry.txt. The line is fixed in this file so every run
produces byte-identical output.
"""

import os

# The roast: the fridge's firmware update turned a basic fact about
# the milk into a paid feature. Specific to smart fridges (firmware,
# subscription, milk-expiry nagging), tight, and it dodges the obvious
# "it orders groceries / it watches you" cracks.
LINE = (
    "My smart fridge updated its firmware overnight and now charges "
    "a monthly fee to tell me the milk expired yesterday."
)

MAX_CHARS = 200


def main():
    line = LINE.strip()
    if not line:
        raise SystemExit("entry line is empty")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    line.encode("utf-8")  # gate requires UTF-8 text

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    os.chmod(path, 0o644)
    # Read it back: the gate reads the file, so confirm what landed
    # on disk is exactly the line we validated above.
    with open(path, encoding="utf-8") as f:
        if f.read().rstrip("\n") != line:
            raise SystemExit("entry.txt on disk does not match the validated line")
    print(line)


if __name__ == "__main__":
    main()
