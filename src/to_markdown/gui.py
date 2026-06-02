import argparse
import base64
import os
import sys
import tempfile
from pathlib import Path

import eel
from markitdown import MarkItDown


# Initialize markitdown globally for Eel access
_markitdown = MarkItDown()

@eel.expose
def convert_file_data(filename: str, data_url: str) -> str:
    """
    Convert base64 data URL to markdown.
    Used when the browser reads the file directly.
    """
    try:
        # Extract base64 data from data URL (e.g., "data:application/pdf;base64,JVBERi...")
        if "," in data_url:
            base64_data = data_url.split(",")[1]
        else:
            base64_data = data_url

        # Decode base64 to bytes
        file_bytes = base64.b64decode(base64_data)

        # Write to a temporary file
        suffix = Path(filename).suffix
        with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as temp_file:
            temp_file.write(file_bytes)
            temp_path = temp_file.name

        try:
            # Convert using MarkItDown
            result = _markitdown.convert(temp_path)
            return result.text_content
        finally:
            # Clean up temp file
            if os.path.exists(temp_path):
                os.remove(temp_path)

    except Exception as e:
        raise Exception(f"Failed to convert file: {str(e)}")

@eel.expose
def save_markdown(content: str, suggested_name: str) -> str | None:
    """
    Ask the user where to save the markdown content.
    Returns the saved path or None if cancelled.
    """
    try:
        import tkinter as tk
        from tkinter import filedialog

        # We need a root window to use filedialog, but we want it hidden
        root = tk.Tk()
        root.withdraw()

        # Ensure it appears on top of the Eel browser window
        root.attributes('-topmost', True)

        file_path = filedialog.asksaveasfilename(
            initialfile=suggested_name,
            defaultextension=".md",
            filetypes=[("Markdown files", "*.md"), ("All files", "*.*")],
            title="Save Markdown As"
        )

        root.destroy()

        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            return file_path

        return None
    except Exception as e:
        print(f"Error saving file: {e}")
        raise Exception(f"Failed to save file: {str(e)}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="to-markdown-ui",
        description="Launch the to-markdown GUI.",
    )
    parser.add_argument(
        "--dev",
        action="store_true",
        help="Run in development mode (connects to local Vite server on port 5173).",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to run the Python backend on.",
    )
    parser.add_argument(
        "--host",
        type=str,
        default="localhost",
        help="Host to bind the server to (use 0.0.0.0 for Docker).",
    )
    parser.add_argument(
        "--mode",
        type=str,
        default="chrome",
        help="Browser mode: 'chrome' to open native window, 'none' for server-only (Docker/headless).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    # Determine the mode for Eel
    # 'chrome' opens a native browser window, 'none' runs server-only
    mode = False if args.mode.lower() == "none" else args.mode

    try:
        if args.dev:
            # In dev mode, we connect to the Vite dev server
            # Vite must be running on localhost:5173
            print(f"Starting Eel in development mode on port {args.port}...")
            print("Ensure Vite is running via 'npm run dev' in the ui/ folder.")

            # Start Eel, pointing it at the Vite dev server URL
            # We don't need a local directory since Vite serves the files
            eel.init("ui/dist")  # Required by Eel even if unused in dev mode

            # Start Eel app
            eel.start(
                {"port": 5173}, # The page to load (Vite dev server)
                host=args.host,
                port=args.port,
                mode=mode,
                size=(900, 700),
                position=(300, 200)
            )
        else:
            # In production mode, we serve the built static files
            ui_dir = Path(__file__).parent.parent.parent / "ui" / "dist"

            if not ui_dir.exists():
                print(f"Error: UI directory not found at {ui_dir}")
                print("Please build the UI first: cd ui && npm install && npm run build")
                return 1

            print(f"Starting Eel in production mode from {ui_dir}...")
            print(f"Access the UI at: http://{args.host}:{args.port}")
            eel.init(str(ui_dir))

            eel.start(
                "index.html",
                host=args.host,
                port=args.port,
                mode=mode,
                size=(900, 700),
                position=(300, 200)
            )

    except Exception as error:
        print(f"Error starting GUI: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
