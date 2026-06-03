# to-markdown

Chuyển đổi file sang Markdown bằng [MarkItDown](https://github.com/microsoft/markitdown).

## Định dạng hỗ trợ

PDF, Word (`.docx`), Excel (`.xlsx`, `.xls`), PowerPoint (`.pptx`), ảnh (`.jpg`, `.png`, …), HTML, CSV, JSON, XML, và nhiều hơn.

## Cài đặt

### 1. Tạo môi trường ảo và cài gói

Mở PowerShell tại thư mục dự án:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[docx,pdf,xlsx,pptx,xls,images]"
```

### 2. Thêm vào menu chuột phải Windows

Double-click `install_context_menu.reg` → bấm **Yes**.

> **Lưu ý:** Nếu di chuyển thư mục dự án sang vị trí khác, phải chạy lại bước này để cập nhật đường dẫn.

### Gỡ cài đặt menu chuột phải

Double-click `uninstall_context_menu.reg` → bấm **Yes**.

---

## Cách dùng

### Chuột phải (khuyến nghị)

Chuột phải vào bất kỳ file nào → **Convert to Markdown**.  
File `.md` tạo ra cùng thư mục với file gốc. Chạy ngầm, không hiện cửa sổ.

### CLI

In kết quả ra terminal:

```powershell
to-markdown path\to\file.pdf
```

Lưu ra file:

```powershell
to-markdown path\to\file.docx -o output.md
```

Chạy không cần cài:

```powershell
python -m to_markdown path\to\file.xlsx -o output.md
```
