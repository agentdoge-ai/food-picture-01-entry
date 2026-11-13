"""Entry point: deliver this entry's food picture to /output/entry.png.

Deterministic: the program only copies the bundled entry.png, so every
run writes the exact same bytes to /output/entry.png. No network access.
"""

import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    dst = os.path.join("/output", "entry.png")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, dst)


if __name__ == "__main__":
    main()
