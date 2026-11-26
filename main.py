"""Entry for make.fun bounty u-motasimfuad-name-the-robot-band-1ffc6a74.

Writes one funny robot band name plus a few words on its hit song
to <output>/entry.txt. Standard library only; deterministic.
"""

import os

LINE = (
    "The Buffering Boys: their hit single 'Loading...' has been stuck "
    "at 99% for six months, and it is still their most-streamed song."
)


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry must be 1-200 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
