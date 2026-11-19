#!/usr/bin/env python3
"""Check the coverage register (analysis/coverage-register.md) against the examples.

The register lists every endorsed UBL 2.5 element that no example covers (owner, 2026-11-19, O145):
- every element the coverage tool reports as missing must have a row under "Missing" or "Left out on purpose";
- every row there must still be missing (an element that comes back moves to "Won back");
- every row under "Won back" must be covered.
Prints the problems and exits 1 when there are any. Run by tools/check_world.py.

Usage: python3 tools/coverage_register.py
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTER = os.path.join(ROOT, "analysis", "coverage-register.md")
MODEL = os.path.join(ROOT, ".ubl", "mod", "UBL-Entities-2.5.gc")
MODEL_URL = "https://docs.oasis-open.org/ubl/os-UBL-2.5/mod/UBL-Entities-2.5.gc"


def missing_elements():
    """The elements the coverage tool reports as missing, as "Parent/Element"."""
    if not os.path.exists(MODEL) or os.path.getsize(MODEL) == 0:
        os.makedirs(os.path.dirname(MODEL), exist_ok=True)
        urllib.request.urlretrieve(MODEL_URL, MODEL)
    tmp = tempfile.mkdtemp()
    try:
        xml = os.path.join(tmp, "xml")
        os.mkdir(xml)
        examples = os.path.join(ROOT, "world", "examples")
        for flow in sorted(os.listdir(examples)):
            folder = os.path.join(examples, flow)
            if os.path.isdir(folder):
                for name in sorted(os.listdir(folder)):
                    if name.endswith(".xml"):
                        shutil.copy(os.path.join(folder, name), os.path.join(xml, f"{flow}-{name}"))
        report = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "coverage.py"), "--model", MODEL,
                                 "--examples", xml, "--endorsed", os.path.join(ROOT, "world", "ubl-model.json")],
                                capture_output=True, text=True, check=True).stdout
    finally:
        shutil.rmtree(tmp)
    found, in_section, doc = set(), False, None
    for line in report.split("\n"):
        if line.startswith("## "):
            in_section = line.startswith("## Missing elements per placement")
        if not in_section:
            continue
        if re.search(r"<summary><b>[^<]*</b>", line):
            doc = True
        if doc and line.startswith("| ") and not line.startswith("| Parent") and not line.startswith("|---"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2:
                found.add(f"{cells[0]}/{cells[1]}")
    return found


def register_rows():
    """The register's rows per part: {"missing": {...}, "won back": {...}}; a part's rows by element."""
    parts, part = {"missing": {}, "won back": {}}, None
    for number, line in enumerate(open(REGISTER, encoding="utf-8"), 1):
        if line.startswith("## "):
            title = line[3:].strip().lower()
            part = ("missing" if title in ("missing", "left out on purpose")
                    else "won back" if title == "won back" else None)
            continue
        m = re.match(r"\| `([A-Za-z]+/[A-Za-z]+)` \|", line)
        if m and part:
            if m.group(1) in parts[part]:
                parts[part][m.group(1)].append(number)
            else:
                parts[part][m.group(1)] = [number]
    return parts


def main():
    missing = missing_elements()
    rows = register_rows()
    problems = []
    for element in sorted(missing - set(rows["missing"])):
        problems.append(f"{element}: missing from every example, but not in the register (add its row, with the cause)")
    for element in sorted(set(rows["missing"]) - missing):
        problems.append(f"{element}: in the register as missing (line {rows['missing'][element][0]}), "
                        "but an example covers it (move it to Won back)")
    for element in sorted(set(rows["won back"]) & missing):
        problems.append(f"{element}: under Won back (line {rows['won back'][element][0]}), but missing again")
    for part in rows.values():
        for element, lines in sorted(part.items()):
            if len(lines) > 1:
                problems.append(f"{element}: listed more than once (lines {', '.join(map(str, lines))})")
    if problems:
        print("coverage register: " + str(len(problems)) + " problem(s)")
        for p in problems:
            print("  " + p)
        sys.exit(1)
    print(f"coverage register: {len(missing)} missing elements, each with its row")


if __name__ == "__main__":
    main()
