"""Copy the shipped roast line to the grader output directory.

Reads entry.txt shipped beside this script and writes those exact bytes
to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset),
with a single direct write and mode 0644 so the grader can read it.
"""
import os
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    data = (here / "entry.txt").read_bytes()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        out_path = out_dir / "entry.txt"
        out_path.write_bytes(data)
        os.chmod(out_path, 0o644)
    except OSError as exc:
        raise SystemExit(f"failed to write output entry: {exc}") from exc


if __name__ == "__main__":
    main()
