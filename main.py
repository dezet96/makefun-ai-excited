"""Entry program for make.fun ai-excited-01.

Copies the bundled image (entry.png) to the output directory as
entry.png. Standard library only, no network access.
"""

import os
import shutil
import sys


def main() -> int:
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(repo_dir, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
