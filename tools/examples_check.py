#!/usr/bin/env python3
"""The site build's checks of the example documents, done only when their inputs changed.

  1. tools/build_examples.py --check: the committed examples are what the generators make of the world now;
  2. tools/validate_examples.py: every example is valid (UBL 2.5 schemas, code lists).

Each check is run when the fingerprint of everything it reads differs from that of its last passing run, and is
skipped otherwise (tools/build_cache.py; the fingerprints are of the files themselves, never of a commit's changes).
Their inputs, found by recording what the checks open during a run, taken wide: every Python file in tools/, every
file under world/ but the reviews (*.llm-review.*: not generated, not read), and the versions of Python and lxml;
for the validation also the UBL 2.5 files in .ubl/ (the schemas, the code list stylesheets and Saxon) and the Java
version. A failing check is not remembered, so it runs again next time.

Usage (from the repository root): python3 tools/examples_check.py   ($WORLD_MODEL is passed on to the generators)
"""
import glob
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_cache  # noqa: E402

os.chdir(build_cache.ROOT)


def common():
    import lxml.etree
    fp = build_cache.Fingerprint()
    fp.add("versions", f"{sys.version} lxml {lxml.etree.LXML_VERSION} libxml2 {lxml.etree.LIBXML_VERSION}")
    fp.add_files(sorted(glob.glob("tools/*.py")) + build_cache.tree_files("world", lambda p: ".llm-review." in p))
    return fp


def run(name, fp, cmd, what):
    if build_cache.passed(name, fp):
        print(f"{what}: unchanged inputs ({fp[:12]}), passed before")
        return
    print(f"{what}: checking ({fp[:12]})", flush=True)
    r = subprocess.run(cmd)
    if r.returncode:
        sys.exit(r.returncode)
    build_cache.mark_passed(name, fp)


examples = sorted(glob.glob("world/examples/*/*.xml"))
fp = common()
run("examples-check", fp.hexdigest(), [sys.executable, "tools/build_examples.py", "--check"], "examples up to date")
fp = common()
java = subprocess.run(["java", "-version"], capture_output=True, text=True).stderr.strip()
fp.add("java", java)
fp.add_files(build_cache.tree_files(".ubl"))
run("examples-valid", fp.hexdigest(), [sys.executable, "tools/validate_examples.py"] + examples, "examples valid")
