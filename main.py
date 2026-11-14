#!/usr/bin/env python3
"""ai-happy-01 entry (Python 3.13, standard library only).

The image is the entry.png beside this file: a flour-dusted little robot
proudly presenting a tray of star-shaped cookies to a laughing little girl
in a sunlit kitchen. The program copies it to /output/entry.png.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

ENTRY = Path(__file__).resolve().parent / "entry.png"

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
dest = output_dir / "entry.png"
shutil.copyfile(ENTRY, dest)
# The grader runs this twice and both runs must write the same bytes:
# copyfile is deterministic, and this guard fails loudly if anything
# ever made the copy differ from the image shipped in the repository.
if dest.read_bytes() != ENTRY.read_bytes():
    raise SystemExit("entry.png copy differs from the repository image")
