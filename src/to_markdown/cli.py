from __future__ import annotations

import argparse
import sys
from pathlib import Path

from markitdown import MarkItDown


def convert_file(input_path: Path) -> str:
    """Convert a file to Markdown."""
    if not input_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_path}")

    markdown = MarkItDown()
    result = markdown.convert(str(input_path))
    return result.text_content


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="to-markdown",
        description="Convert a file to Markdown using MarkItDown.",
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Path to the file to convert.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        help="Optional path where the Markdown output should be saved.",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="Encoding to use when writing output files. Defaults to utf-8.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        markdown_text = convert_file(args.input)

        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(markdown_text, encoding=args.encoding)
        else:
            sys.stdout.write(markdown_text)
            if markdown_text and not markdown_text.endswith("\n"):
                sys.stdout.write("\n")
    except Exception as error:
        parser.exit(status=1, message=f"error: {error}\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
