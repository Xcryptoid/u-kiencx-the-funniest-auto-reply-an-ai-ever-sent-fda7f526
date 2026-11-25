"""Copy the pre-written auto-reply into the grader's output directory.

The entry text lives in entry.txt next to this file; this program only
moves it into place, unchanged, so the run is deterministic.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    # The auto-reply itself is already written and kept in entry.txt;
    # this step only carries that finished line into the output folder
    # exactly as it stands, without touching a word of it.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.txt"),
        os.path.join(out_dir, "entry.txt"),
    )


if __name__ == "__main__":
    main()
