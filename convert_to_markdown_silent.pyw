from __future__ import annotations

import sys
from pathlib import Path

from to_markdown.cli import main


def output_path_for(input_path: Path) -> Path:
    return input_path.with_suffix(".md")


def run() -> int:
    if len(sys.argv) < 2:
        return 1

    input_path = Path(sys.argv[1])
    output_path = output_path_for(input_path)
    return main([str(input_path), "-o", str(output_path)])


if __name__ == "__main__":
    raise SystemExit(run())
