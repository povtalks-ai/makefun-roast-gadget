#!/usr/bin/env python3
"""One-line roast entry for make.fun bounty
u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.

Writes a single original line (at most 200 characters) roasting
a gadget used every day to /output/entry.txt. Standard library
only, no network, no input files: everything the program writes
is in this file.
"""

import os
import sys

# The roast: wireless earbuds, where the left one always dies
# first. A specific gripe with a concrete detail (the left one,
# every single time), a fresh angle (the two earbuds as a pair
# that agreed on the division of labour), and a sting of
# recognition for anyone who has owned a pair.
ROAST = (
    "My wireless earbuds always die in the left one first, every "
    "single time, like the pair agreed the left one does all the "
    "work and the right one just takes the credit."
)

MAX_CHARS = 200


def validate(text):
    """The gate accepts UTF-8 text of 1 to 200 characters."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("roast must not be only whitespace")
    if len(stripped) > MAX_CHARS:
        raise ValueError(
            "roast is %d characters, over the %d limit"
            % (len(stripped), MAX_CHARS)
        )
    # One line: a newline inside would make it two lines.
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("roast must be a single line")
    return stripped


def output_path():
    """The grader sets MAKEFUN_OUTPUT_DIR; default is /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, "entry.txt")


def main():
    text = validate(ROAST)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %d characters to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
