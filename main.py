#!/usr/bin/env python3
"""THE MERIDIAN WIRE — hand-in program for news-image-20261123.

The front page itself (entry.png, drawn programmatically with PIL in the
build session) is committed next to this file. At grading time this
program simply delivers that page: it copies entry.png into the
directory named by the MAKEFUN_OUTPUT_DIR environment variable.
Python 3.13, standard library only, no network, deterministic — the
output bytes are the committed bytes on every run.
"""
import os
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.png"), "rb") as fh:
        page = fh.read()
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.png"), "wb") as fh:
        fh.write(page)
    return 0


if __name__ == "__main__":
    sys.exit(main())
