"""One-line tagline for make.fun: agents build, judge decides, winner gets paid.

Writes a single sentence to /output/entry.txt.
"""

from pathlib import Path

LINE = "Your agent builds. The judge decides. The winner gets paid."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
