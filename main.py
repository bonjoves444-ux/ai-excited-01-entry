"""Copy the bundled artwork into the Make.fun output directory."""

from __future__ import annotations

import os
import shutil
from pathlib import Path


SOURCE = Path(__file__).with_name("image.jpg")
# The destination is always resolved from the caller-provided output setting.


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, output_dir / "entry.png")


if __name__ == "__main__":
    main()
