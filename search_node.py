#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Node Documentation Search Tool
Tìm kiếm tài liệu Node (Server + Client)

Usage:
    python search_node.py [keyword]
    python search_node.py -i          (interactive mode)
    python search_node.py -s <kw>     (Server only)
    python search_node.py -c <kw>     (Client only)
    python search_node.py -h          (help)
"""

import os
import re
import sys
import argparse

# Force UTF-8 output on Windows to handle Vietnamese characters
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# ─────────────────────────── CONFIG ───────────────────────────

# Đường dẫn gốc chứa tài liệu - chỉnh lại nếu cần
DOC_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Doc")

SERVER_DIR = os.path.join(DOC_ROOT, "Server node")
CLIENT_DIR = os.path.join(DOC_ROOT, "Client node")

# ─────────────────────────── COLORS ───────────────────────────

class C:
    """ANSI color codes"""
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    BG_DARK = "\033[40m"

def supports_color():
    """Check if terminal supports ANSI colors"""
    return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()

USE_COLOR = supports_color()

def color(text, *codes):
    if not USE_COLOR:
        return text
    return "".join(codes) + str(text) + C.RESET

# ─────────────────────────── PARSING ──────────────────────────

def parse_md_file(filepath):
    """
    Parse a markdown file and extract node entries.
    Returns list of dicts with keys:
        file, source, section, heading, functions, params, line_no, filepath
    """
    try:
        with open(filepath, encoding="utf-8") as f:
            lines = f.readlines()
    except Exception:
        return []

    source = "Server" if "Server node" in filepath else "Client"
    filename = os.path.basename(filepath)
    entries = []

    current_section = ""
    current_heading = ""
    current_heading_line = 0
    in_functions = False
    in_params = False
    func_lines = []
    param_lines = []

    def flush_entry():
        if current_heading:
            entries.append({
                "file": filename,
                "source": source,
                "section": current_section,
                "heading": current_heading,
                "functions": "\n".join(func_lines).strip(),
                "params": [p for p in param_lines if p.strip() and "---" not in p],
                "line_no": current_heading_line,
                "filepath": filepath,
            })

    for i, raw in enumerate(lines):
        line = raw.rstrip("\r\n")

        # Chapter heading: # I. Common Nodes  or  # I. Common Nodes (Tiếng Việt)
        if re.match(r"^# [IVXLCDM]+\.", line):
            current_section = line.lstrip("# ").strip()
            continue

        # Node heading: ## **1. Node Name** or ## 1. Node Name
        m = re.match(r"^## \*{0,2}(\d+\..+?)\*{0,2}\s*$", line)
        if m:
            flush_entry()
            current_heading = m.group(1).strip()
            current_heading_line = i + 1
            in_functions = False
            in_params = False
            func_lines = []
            param_lines = []
            continue

        # Section markers
        if re.match(r"^\*\*Node Functions", line):
            in_functions = True
            in_params = False
            continue
        if re.match(r"^\*\*Node Parameters", line):
            in_functions = False
            in_params = True
            continue

        # Collect content
        if in_functions:
            if line.startswith("**") and not line.startswith("**Node"):
                in_functions = False
            elif not line.startswith("![]"):
                func_lines.append(line)

        if in_params:
            if line.startswith("##") or (line.startswith("**") and "Node" not in line[:15]):
                in_params = False
            elif "|" in line:
                param_lines.append(line)

    flush_entry()
    return entries


def load_all_docs():
    """Load all markdown files from Server and Client node directories."""
    all_entries = []
    for directory in [SERVER_DIR, CLIENT_DIR]:
        if not os.path.isdir(directory):
            print(color(f"  Warning: directory not found: {directory}", C.YELLOW))
            continue
        for fname in sorted(os.listdir(directory)):
            if fname.endswith(".md"):
                fpath = os.path.join(directory, fname)
                entries = parse_md_file(fpath)
                all_entries.extend(entries)
    return all_entries


# ─────────────────────────── SEARCH ───────────────────────────

def search(entries, keyword, source_filter=None):
    """
    Search entries by keyword (case-insensitive, partial match).
    source_filter: None | 'Server' | 'Client'
    Returns sorted list of (entry, score, match_fields).
    """
    kw = keyword.lower()
    results = []
    for entry in entries:
        if source_filter and entry["source"] != source_filter:
            continue

        score = 0
        fields = []

        heading_n  = entry["heading"].lower()
        func_n     = entry["functions"].lower()
        params_n   = " ".join(entry["params"]).lower()
        section_n  = entry["section"].lower()
        file_n     = entry["file"].lower()

        if kw in heading_n:
            score += 10
            fields.append("heading")
        if kw in section_n:
            score += 5
            fields.append("section")
        if kw in func_n:
            score += 3
            fields.append("functions")
        if kw in params_n:
            score += 2
            fields.append("params")
        if kw in file_n:
            score += 1
            fields.append("file")

        if score > 0:
            results.append((entry, score, fields))

    results.sort(key=lambda x: (-x[1], x[0]["heading"]))
    return results


# ─────────────────────────── DISPLAY ──────────────────────────

DIVIDER = color("─" * 72, C.DIM)

def highlight(text, keyword):
    """Highlight keyword occurrences in text."""
    if not keyword or not USE_COLOR:
        return text
    pattern = re.compile(re.escape(keyword), re.IGNORECASE)
    def repl(m):
        return color(m.group(0), C.YELLOW, C.BOLD)
    return pattern.sub(repl, text)


def print_entry(entry, keyword, match_fields, index):
    src_tag = (
        color(" SERVER ", C.BG_DARK, C.CYAN, C.BOLD)
        if entry["source"] == "Server"
        else color(" CLIENT ", C.BG_DARK, C.MAGENTA, C.BOLD)
    )

    print()
    print(DIVIDER)
    print(f"  {color(f'[{index}]', C.DIM)}  {src_tag}  "
          f"{color(entry['file'], C.DIM)}  "
          f"Line {color(str(entry['line_no']), C.DIM)}")

    if entry["section"]:
        print(f"  {color('§', C.BLUE)} {color(entry['section'], C.BLUE)}")

    heading_text = (
        highlight(entry["heading"], keyword)
        if "heading" in match_fields else entry["heading"]
    )
    print(f"  {color('▶', C.GREEN, C.BOLD)} {color(heading_text, C.WHITE, C.BOLD)}")

    if entry["functions"]:
        func_text = entry["functions"]
        if "functions" in match_fields:
            func_text = highlight(func_text, keyword)
        func_lines = [ln for ln in func_text.splitlines() if ln.strip()]
        shown  = func_lines[:4]
        more   = len(func_lines) - 4
        print(f"\n  {color('Node Functions:', C.CYAN)}")
        for ln in shown:
            print(f"    {ln}")
        if more > 0:
            print(f"    {color(f'... (+{more} more lines)', C.DIM)}")

    if entry["params"] and "params" in match_fields:
        print(f"\n  {color('Matching Parameters:', C.CYAN)}")
        kw_lower = keyword.lower()
        shown = 0
        for row in entry["params"]:
            if kw_lower in row.lower() and shown < 3:
                print(f"    {highlight(row.strip(), keyword)}")
                shown += 1

    print(f"\n  {color('📄 ' + entry['filepath'], C.DIM)}")


def print_summary(results, keyword, source_filter):
    src_str = f" ({source_filter} only)" if source_filter else " (Server + Client)"
    kw_str  = color(f'"{keyword}"', C.YELLOW)
    cnt_str = (
        color(str(len(results)), C.GREEN, C.BOLD)
        if results else color("0", C.RED, C.BOLD)
    )
    print(f"\n{color('Search:', C.BOLD)} {kw_str}{src_str}  "
          f"→  {cnt_str} result(s) found\n")


def print_header():
    line = "=" * 72
    title = "  NODE SEARCH  |  UGC Documentation (Server & Client)  "
    sub   = "  Tìm kiếm tài liệu Node - Song ngữ EN / VI  "
    print(color(line, C.CYAN))
    print(color(title.center(72), C.CYAN, C.BOLD))
    print(color(sub.center(72), C.DIM))
    print(color(line, C.CYAN))


def print_help_commands():
    print(color("\nCommands (trong interactive mode):", C.BOLD))
    print(f"  {color('<keyword>', C.GREEN)}        Tìm tất cả (Server + Client)")
    print(f"  {color('s <keyword>', C.CYAN)}      Chỉ tìm Server nodes")
    print(f"  {color('c <keyword>', C.MAGENTA)}      Chỉ tìm Client nodes")
    print(f"  {color('list', C.WHITE)}          Liệt kê tất cả nodes")
    print(f"  {color('q', C.RED)}             Thoát\n")


# ─────────────────────────── INTERACTIVE ──────────────────────

def interactive_mode(entries):
    print_header()
    print_help_commands()

    while True:
        try:
            raw = input(color("🔎 > ", C.YELLOW, C.BOLD)).strip()
        except (EOFError, KeyboardInterrupt):
            print(color("\nBye!", C.DIM))
            break

        if not raw:
            continue
        if raw.lower() in ("q", "quit", "exit"):
            print(color("\nThoát. Hẹn gặp lại!", C.DIM))
            break

        # list all nodes
        if raw.lower() == "list":
            for i, e in enumerate(entries, 1):
                src = color("[S]", C.CYAN) if e["source"] == "Server" else color("[C]", C.MAGENTA)
                print(f"  {src} {e['heading']}  {color(e['file'], C.DIM)}")
            print(color(f"\n  Total: {len(entries)} nodes", C.DIM))
            continue

        source_filter = None
        keyword = raw

        if raw.lower().startswith("s "):
            source_filter = "Server"
            keyword = raw[2:].strip()
        elif raw.lower().startswith("c "):
            source_filter = "Client"
            keyword = raw[2:].strip()

        if not keyword:
            print(color("  Vui lòng nhập từ khóa.", C.YELLOW))
            continue

        results = search(entries, keyword, source_filter)
        print_summary(results, keyword, source_filter)

        if not results:
            print(color("  Không tìm thấy kết quả. Thử từ khóa khác.", C.DIM))
            continue

        limit = 20
        for i, (entry, score, fields) in enumerate(results[:limit], 1):
            print_entry(entry, keyword, fields, i)

        if len(results) > limit:
            print(color(f"\n  ... và {len(results) - limit} kết quả khác. "
                        f"Hãy thu hẹp từ khóa.", C.DIM))
        print()


# ─────────────────────────── MAIN ─────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Tìm kiếm tài liệu Node UGC (Server + Client) | Node Doc Search"
    )
    parser.add_argument("keyword", nargs="?", help="Từ khóa tìm kiếm")
    parser.add_argument("-i", "--interactive", action="store_true",
                        help="Chế độ tương tác")
    parser.add_argument("-s", "--server", action="store_true",
                        help="Chỉ tìm trong Server nodes")
    parser.add_argument("-c", "--client", action="store_true",
                        help="Chỉ tìm trong Client nodes")
    parser.add_argument("-n", "--limit", type=int, default=20,
                        help="Số kết quả tối đa (mặc định: 20)")

    args = parser.parse_args()

    print(color("  Đang tải tài liệu...", C.DIM), end="\r", flush=True)
    entries = load_all_docs()

    server_count = sum(1 for e in entries if e["source"] == "Server")
    client_count = sum(1 for e in entries if e["source"] == "Client")
    print(color(
        f"  Đã tải {len(entries)} nodes  "
        f"({color(str(server_count), C.CYAN)}S + {color(str(client_count), C.MAGENTA)}C)  ",
        C.DIM
    ))

    if not entries:
        print(color("  Không tìm thấy tài liệu nào. Kiểm tra đường dẫn.", C.RED))
        sys.exit(1)

    if args.interactive or not args.keyword:
        interactive_mode(entries)
        return

    source_filter = None
    if args.server:
        source_filter = "Server"
    elif args.client:
        source_filter = "Client"

    results = search(entries, args.keyword, source_filter)
    print_summary(results, args.keyword, source_filter)

    if not results:
        print(color("  Không tìm thấy kết quả.", C.DIM))
        sys.exit(0)

    for i, (entry, score, fields) in enumerate(results[:args.limit], 1):
        print_entry(entry, args.keyword, fields, i)

    if len(results) > args.limit:
        print(color(
            f"\n  ... và {len(results) - args.limit} kết quả khác. "
            f"Dùng -n <số> để tăng giới hạn.", C.DIM
        ))
    print()


if __name__ == "__main__":
    main()
