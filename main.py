#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

make.fun bounty: u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3

Writes one review line (max 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
The grader runs this as `python3 -P -s /bot/main.py` in a sandbox with no
network; the output is a fixed string, so the run is fully deterministic.

Usage: set MAKEFUN_OUTPUT_DIR to the directory that should receive
entry.txt (defaults to /output), then run `python3 -P -s main.py`.
After writing, the entry re-reads entry.txt and asserts it contains exactly
the review line plus a trailing newline, so a partial or failed write can
never pass silently.
"""

import os

REVIEW = (
    "Has held the same door open for six years and never once been "
    "thanked, promoted, or even noticed."
)

assert 1 <= len(REVIEW) <= 200, f"review is {len(REVIEW)} characters"
assert REVIEW.strip(), "review must not be only whitespace"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(REVIEW + "\n")
    # Read back and verify: the file must contain exactly the review + newline.
    with open(entry_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == REVIEW + "\n", (
        f"entry.txt mismatch: expected {len(REVIEW) + 1} chars, "
        f"got {len(written)} chars"
    )


if __name__ == "__main__":
    main()
