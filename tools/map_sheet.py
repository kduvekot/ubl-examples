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
import glob
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_cache  # noqa: E402

ROOT = build_cache.ROOT
SCRIPT = "analysis/world-position/refine_map.py"
ARGS = ["5", "0", "sheet"]                     # LEVELS, PX, the sheet
MAP = "world/map.json"
FONTS = ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
         "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"]
MODULE_DIRS = ("tools",)                       # refine_map.py puts tools/ on its path; -I keeps its own folder off it


def fingerprint(model):
    import numpy
    import PIL
    fp = build_cache.Fingerprint()
    fp.add("args", " ".join([MAP] + ARGS))
    fp.add("versions", f"{sys.version} numpy {numpy.__version__} Pillow {PIL.__version__}")
    fp.add("model", open(model, "rb").read())
    fp.add_files([SCRIPT, MAP, "world/terrain.json", "world/parties.json"] + sorted(glob.glob("world/terrain/*.png"))
                 + sorted(build_cache.repo_modules(SCRIPT, set(), MODULE_DIRS)) + FONTS)
    return fp.hexdigest()


def main():
    model, out = (os.path.abspath(a) for a in sys.argv[1:3])
    os.chdir(ROOT)                             # refine_map.py reads world/ and tools/ from the working directory
    fp = fingerprint(model)
    cache = os.path.relpath(build_cache.cache_dir("map-sheet"), ROOT)
    if build_cache.fetch("map-sheet", fp, out, "map-sheet.png"):
        print(f"map sheet: unchanged inputs ({fp[:12]}), taken from {cache}", file=sys.stderr)
        return
    print(f"map sheet: drawing ({fp[:12]})", file=sys.stderr)
    subprocess.run([sys.executable, "-I", SCRIPT, model, MAP, out] + ARGS, check=True, stdout=subprocess.DEVNULL)
    build_cache.store("map-sheet", fp, out, "map-sheet.png")


if __name__ == "__main__":
    main()
