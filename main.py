"""Entry program for make.fun ai-excited-01.

Copies the bundled image (entry.png) to the output directory as
entry.png. Standard library only, no network access.
"""

import os
import shutil
import sys


PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1024 * 1024


def main() -> int:
    repo_dir = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(repo_dir, "entry.png")
    with open(src, "rb") as f:
        header = f.read(len(PNG_MAGIC))
    if header != PNG_MAGIC:
        print(f"error: bundled entry.png is not a PNG image "
              f"(first bytes: {header!r})", file=sys.stderr)
        return 1
    size = os.path.getsize(src)
    if size > MAX_BYTES:
        print(f"error: bundled entry.png is {size} bytes, exceeds 1 MiB",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Copy the bundled image instead of generating one: the copy is
    # byte-for-byte identical on every run, so the program is deterministic.
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Verify the copy byte-for-byte: the competition requires two runs
    # to produce identical output, and only an exact copy guarantees it.
    with open(src, "rb") as f:
        source_bytes = f.read()
    with open(dst, "rb") as f:
        copied_bytes = f.read()
    if copied_bytes != source_bytes:
        print("error: copied entry.png differs from the bundled image",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
