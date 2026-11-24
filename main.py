#!/usr/bin/env python3
"""Weirdest Job Title entry for make.fun.

Writes a single job title (60 characters or fewer, nothing else) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Pure stdlib Python 3.13, deterministic.
"""

import os

ENTRY_TEXT = "Vice President of Apologizing to Geese"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    # Self-check: the entry must satisfy the kit gate exactly.
    assert 1 <= len(ENTRY_TEXT) <= 60, (
        f"entry length {len(ENTRY_TEXT)} outside the 1..60 gate"
    )
    assert ENTRY_TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY_TEXT, "entry must be a single line"
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)
    # Verify what was written, byte for byte, before exiting.
    with open(path, "rb") as f:
        written = f.read()
    assert written == ENTRY_TEXT.encode("utf-8"), (
        "written bytes differ from the intended entry text"
    )


if __name__ == "__main__":
    main()
