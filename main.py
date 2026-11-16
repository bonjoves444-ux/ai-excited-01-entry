"""Entry for make.fun ai-excited-01: copy the bundled artwork to the output.

The artwork is a single still image shipped in this repository. This
program does no drawing and no network access; it only places a copy of
that image where the grader reads it, so both runs produce identical bytes.
"""

import os
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
BUNDLED_IMAGE = REPO_ROOT / "image.jpg"


def main() -> None:
    # The grader reads only /output (or MAKEFUN_OUTPUT_DIR when set);
    # never write beside this program and never remove the output dir.
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(BUNDLED_IMAGE, output_dir / "entry.png")


if __name__ == "__main__":
    main()
