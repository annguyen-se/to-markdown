# to-markdown

A small Python CLI that converts files to Markdown using [MarkItDown](https://github.com/microsoft/markitdown).

## Supported formats

PDF, Word (`.docx`), Excel (`.xlsx`, `.xls`), PowerPoint (`.pptx`), images (`.jpg`, `.png`, …), HTML, CSV, JSON, XML, and more.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

## CLI Usage

Print converted Markdown to the terminal:

```powershell
to-markdown path\to\file.pdf
```

Save converted Markdown to a file:

```powershell
to-markdown path\to\file.docx -o output.md
```

Run the module directly without installing:

```powershell
python -m to_markdown path\to\file.xlsx -o output.md
```

## Windows Right-Click Context Menu

Adds a **"Convert to Markdown"** option when you right-click any file in Windows Explorer.

### Install

1. Make sure the virtual environment is set up at `.venv\` (see [Setup](#setup) above).
2. Double-click `install_context_menu.reg` → click **Yes**.

### How it works

- Right-click any file → **Convert to Markdown**.
- A `.md` file with the same name is created in the same folder.
- The conversion runs completely in the background — no terminal window, no log files.

### Uninstall

Double-click `uninstall_context_menu.reg` → click **Yes**.

### Moving the project

The `.reg` files contain absolute paths to this project folder (`D:\SE\project\to-markdown`).  
If you move the project, update the paths inside `install_context_menu.reg` and re-run it.
