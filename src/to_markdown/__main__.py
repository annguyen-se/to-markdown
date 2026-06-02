"""
Allow the package to be run as a module: python -m to_markdown
"""
from to_markdown.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
