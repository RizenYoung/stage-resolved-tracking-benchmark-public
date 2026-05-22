"""List files included in the curated public release."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    for path in sorted(p for p in ROOT.rglob("*") if p.is_file()):
        rel = path.relative_to(ROOT).as_posix()
        print(f"{rel}\t{path.stat().st_size}")


if __name__ == "__main__":
    main()

