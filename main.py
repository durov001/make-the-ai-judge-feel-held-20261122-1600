#!/usr/bin/env python3
"""make-the-ai-judge-feel-held-20261122-1600 entrypoint.

Writes one short relaxing text to the output directory as entry.txt.
The program is deterministic: every run writes the same bytes.
"""
import os
from pathlib import Path

TEXT = "The kettle has boiled and clicked off. Rain is finding its way down the window in no particular hurry. Nothing here is waiting. The afternoon is decided: tea, the soft chair, whatever the light does next. You can stay. This sentence goes nowhere else."


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.txt"
    dst.write_text(TEXT, encoding="utf-8")
    print("make-the-ai-judge-feel-held-20261122-1600: wrote %d bytes to %s" % (dst.stat().st_size, dst))


if __name__ == "__main__":
    main()
