#!/usr/bin/env python3
"""The published site states the world as fact (the rule "two layers: the workshop and the world",
analysis/codelist-decisions.md): no internal references in what a reader sees. Scans the text of the built HTML pages
(not code, not the method note, which describes the project) and fails on

  * decision, open-point and cause numbers: D12, O226, MO004, OW001, ID-Q7, "worklist C23", "(C72)";
  * review finding IDs: tender/09#F4;
  * repository paths: world/items.json, tools/build_examples.py;
  * names of real specifications the world does not follow: EN 16931, Peppol, XRechnung;

and warns on words that tell the project's history ("no longer", "was moved", "proposed addition").

Usage: python3 tools/check_published.py <site-dir>
"""
import os
import re
import sys
from html.parser import HTMLParser

FAIL = re.compile(r"(?<![\w`/=-])(?:D\d{1,2}(?: point \d+)?|O\d{1,3}|MO\d{3}|OW\d{3}|ID-Q\d+)\b(?![\w-])"
                  r"|\bworklist C\d+|\(C\d{2,3}\)|\b[a-z]+/\d{2}#F\d+"
                  r"|\b(?:world|tools|analysis)/[\w/-]+\.(?:json|py|md)\b|\bEN 16931\b|\bPeppol\b|\bXRechnung\b")
WARN = re.compile(r"\b(?:no longer|was moved|proposed addition)\b", re.I)
SKIP_DIRS = {"note", "codelists", "examples"}
SKIP_PAGES = {"releases.html", "history.html"}      # the OASIS samples' history: about the project, not the world


class Text(HTMLParser):
    """The visible text of a page, without code, preformatted text, scripts and styles."""
    def __init__(self):
        super().__init__()
        self.depth, self.parts = 0, []

    def handle_starttag(self, tag, attrs):
        if tag in ("code", "pre", "script", "style"):
            self.depth += 1

    def handle_endtag(self, tag):
        if tag in ("code", "pre", "script", "style") and self.depth:
            self.depth -= 1

    def handle_data(self, data):
        if not self.depth:
            self.parts.append(data)


def main(site):
    fails, warns = [], []
    for dirpath, dirs, files in os.walk(site):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for f in sorted(files):
            if not f.endswith(".html") or f in SKIP_PAGES:
                continue
            p = Text()
            p.feed(open(os.path.join(dirpath, f), encoding="utf-8").read())
            text = " ".join(p.parts)
            for m in FAIL.finditer(text):
                fails.append(f"{f}: …{text[max(0, m.start() - 50):m.end() + 10].strip()}…")
            for m in WARN.finditer(text):
                warns.append(f"{f}: …{text[max(0, m.start() - 50):m.end() + 10].strip()}…")
    for w in warns[:5]:
        print("warning:", w)
    if warns:
        print(f"published text: {len(warns)} words that may tell the project's history (warnings)")
    if fails:
        print("\n".join(fails[:60]))
        sys.exit(f"published text: {len(fails)} internal references or names of real specifications")
    print("published text: no internal references")


if __name__ == "__main__":
    main(sys.argv[1])
