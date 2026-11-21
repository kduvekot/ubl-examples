#!/usr/bin/env python3
"""Draw the printed map sheet (analysis/world-position/refine_map.py ... 5 0 sheet), or take it from the cache.

Drawing the A3 sheet at 300 dpi takes about a minute; it changes only when one of its inputs does. The cache keeps
the last sheet with the SHA-256 fingerprint of everything the drawing reads: the world model's content (the JSON
tools/world_model.py writes), world/map.json, world/terrain.json and the terrain rasters (world/terrain/*.png),
world/parties.json, the drawing script and every module of the repository it imports (found by reading their
imports), the fonts it draws its labels with, the versions of Python, numpy and Pillow, and the arguments. When the
fingerprint matches, the cached sheet is copied; otherwise the sheet is drawn and stored. The cache lives outside
the published output: $BUILD_CACHE/map-sheet/, by default .cache/map-sheet/ in the repository (not committed).

Usage (from the repository root): python3 tools/map_sheet.py model.json out.png
"""
import ast
import glob
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = "analysis/world-position/refine_map.py"
ARGS = ["5", "0", "sheet"]                     # LEVELS, PX, the sheet
MAP = "world/map.json"
FONTS = ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"]
MODULE_DIRS = ["tools"]                        # refine_map.py puts tools/ on its path; -I keeps its own folder off it


def repo_modules(path, seen):
    """The modules of the repository that the file at path imports, at any depth (also inside functions)."""
    for node in ast.walk(ast.parse(open(path, "rb").read(), path)):
        names = [a.name for a in node.names] if isinstance(node, ast.Import) else \
            [node.module] if isinstance(node, ast.ImportFrom) and node.module and not node.level else []
        for name in names:
            for d in MODULE_DIRS:
                f = os.path.join(d, *name.split(".")) + ".py"
                if os.path.exists(f) and f not in seen:
                    seen.add(f)
                    repo_modules(f, seen)
    return seen


def fingerprint(model):
    import numpy
    import PIL
    h = hashlib.sha256()

    def add(label, data):
        h.update(label.encode() + b"\0" + str(len(data)).encode() + b"\0" + data)

    add("args", " ".join([MAP] + ARGS).encode())
    add("versions", f"{sys.version} numpy {numpy.__version__} Pillow {PIL.__version__}".encode())
    add("model", open(model, "rb").read())
    files = [SCRIPT, MAP, "world/terrain.json", "world/parties.json"] + sorted(glob.glob("world/terrain/*.png")) \
        + sorted(repo_modules(SCRIPT, set())) + FONTS
    for f in files:
        add(f, open(f, "rb").read())
    return h.hexdigest()


def main():
    model, out = (os.path.abspath(a) for a in sys.argv[1:3])
    os.chdir(ROOT)                             # refine_map.py reads world/ and tools/ from the working directory
    cache = os.path.join(os.environ.get("BUILD_CACHE") or os.path.join(ROOT, ".cache"), "map-sheet")
    fp = fingerprint(model)
    sheet, stamp = os.path.join(cache, "map-sheet.png"), os.path.join(cache, "fingerprint")
    if os.path.exists(sheet) and os.path.exists(stamp) and open(stamp).read().strip() == fp:
        shutil.copyfile(sheet, out)
        print(f"map sheet: unchanged inputs ({fp[:12]}), taken from {os.path.relpath(cache, ROOT)}", file=sys.stderr)
        return
    print(f"map sheet: drawing ({fp[:12]})", file=sys.stderr)
    subprocess.run([sys.executable, "-I", SCRIPT, model, MAP, out] + ARGS, check=True, stdout=subprocess.DEVNULL)
    os.makedirs(cache, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=cache)
    os.close(fd)
    shutil.copyfile(out, tmp)
    os.replace(tmp, sheet)
    with open(stamp + ".tmp", "w") as f:
        f.write(fp + "\n")
    os.replace(stamp + ".tmp", stamp)


if __name__ == "__main__":
    main()
