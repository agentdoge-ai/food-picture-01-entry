#!/usr/bin/env python3
"""food-picture-01 — make.fun entry.

Reproduces the entry image deterministically: copies the bundled
``entry.png`` (in the same directory as this script) byte-for-byte
to ``/output/entry.png``. Standard library only, no network access.
"""

import hashlib
import os
import shutil
import sys

SOURCE_NAME = "entry.png"
DEST_DIR = "/output"
DEST_NAME = "entry.png"


def source_path():
    """Path of the bundled image next to this script."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, SOURCE_NAME)


def dest_path():
    """Path of the reproduced image."""
    return os.path.join(DEST_DIR, DEST_NAME)


def copy_entry():
    """Copy the bundled image to the output location, byte-for-byte."""
    src = source_path()
    dst = dest_path()
    if not os.path.isfile(src):
        raise FileNotFoundError("bundled image not found: %s" % src)
    os.makedirs(DEST_DIR, exist_ok=True)
    shutil.copyfile(src, dst)
    return dst


def sha256_of(path):
    """SHA-256 hex digest of a file's bytes."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_copy(src, dst):
    """Check the output is a byte-for-byte copy of the bundled image."""
    if sha256_of(src) != sha256_of(dst):
        raise ValueError("output does not match bundled image: %s" % dst)
    return True


def main():
    src = source_path()
    dst = copy_entry()
    verify_copy(src, dst)
    print("wrote %s (sha256 %s)" % (dst, sha256_of(dst)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
