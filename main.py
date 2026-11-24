#!/usr/bin/env python3
"""Write one two-sentence horror story to entry.txt.

The story lives here as a single string. Running this program writes it
unchanged to ``$MAKEFUN_OUTPUT_DIR/entry.txt`` (falling back to
``/output/entry.txt`` when the variable is not set), creating the output
directory if needed. Standard library only; no input is read.
"""

import os

STORY = (
    "It snowed overnight, and this morning there was a single set of "
    "footprints leading from my back door to the woods. "
    "They were mine \u2014 same boots, same stride \u2014 and I have not "
    "left the house in three days."
)


def main() -> None:
    if len(STORY) > 400:
        raise SystemExit("story is over the 400-character limit")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(STORY)


if __name__ == "__main__":
    main()
