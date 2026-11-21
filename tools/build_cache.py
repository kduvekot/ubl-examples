#!/usr/bin/env python3
"""The caches of the site build: a step that is slow and changes only when its inputs do keeps its last result with
the SHA-256 fingerprint of everything it reads, and is done again only when that fingerprint changes. The fingerprint
is made of the inputs themselves (file contents, tool versions, arguments), never of a commit's changes, so a skipped
build or a change in another commit cannot leave a result stale.

The caches live outside the published output: $BUILD_CACHE/<name>/, by default .cache/<name>/ in the repository (not
committed; GitHub Actions keeps .cache between runs). Used by tools/map_sheet.py and tools/map_still.py.
"""
import ast
import hashlib
import os
import shutil
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def cache_dir(name):
    return os.path.join(os.environ.get("BUILD_CACHE") or os.path.join(ROOT, ".cache"), name)


def repo_modules(path, seen, dirs=("tools",)):
    """The modules of the repository that the file at path imports, at any depth (also inside functions)."""
    for node in ast.walk(ast.parse(open(path, "rb").read(), path)):
        names = [a.name for a in node.names] if isinstance(node, ast.Import) else \
            [node.module] if isinstance(node, ast.ImportFrom) and node.module and not node.level else []
        for name in names:
            for d in dirs:
                f = os.path.join(d, *name.split(".")) + ".py"
                if os.path.exists(f) and f not in seen:
                    seen.add(f)
                    repo_modules(f, seen, dirs)
    return seen


class Fingerprint:
    """SHA-256 over labelled pieces: each piece is its label, its length and its bytes, so that pieces cannot run
    into each other."""
    def __init__(self):
        self.h = hashlib.sha256()

    def add(self, label, data):
        if isinstance(data, str):
            data = data.encode()
        self.h.update(label.encode() + b"\0" + str(len(data)).encode() + b"\0" + data)

    def add_files(self, paths):
        for f in paths:
            self.add(f, open(f, "rb").read())

    def hexdigest(self):
        return self.h.hexdigest()


def fetch(name, fp, out, filename):
    """Copy the cached result to out if it was made with fingerprint fp; True when it was."""
    d = cache_dir(name)
    kept, stamp = os.path.join(d, filename), os.path.join(d, "fingerprint")
    if os.path.exists(kept) and os.path.exists(stamp) and open(stamp).read().strip() == fp:
        shutil.copyfile(kept, out)
        return True
    return False


def store(name, fp, src, filename):
    """Keep src as the result made with fingerprint fp (written so that a stopped build leaves no half file)."""
    d = cache_dir(name)
    os.makedirs(d, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=d)
    os.close(fd)
    shutil.copyfile(src, tmp)
    os.replace(tmp, os.path.join(d, filename))
    stamp = os.path.join(d, "fingerprint")
    with open(stamp + ".tmp", "w") as f:
        f.write(fp + "\n")
    os.replace(stamp + ".tmp", stamp)
