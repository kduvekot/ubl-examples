#!/usr/bin/env python3
"""The picture of the map on the home page: the 3D map as it opens, taken by a headless Chrome.

Usage: python3 tools/map_still.py <site-dir>/world.html <out.jpg>

Opens world.html?still (the map alone, without toolbar and panel: see site/world.html), waits for it to be
drawn, takes a screenshot at twice the size and makes it 1600 pixels wide. Chrome is found as $CHROME, on the
PATH (google-chrome, chromium, ...) or in Playwright's browser folder. The picture is kept in the build cache
(tools/build_cache.py, "map-still") with the fingerprint of the page (which carries all the map's data), this script
and Chrome's version, and taken again only when one of them changes.
"""
import os
import shutil
import subprocess
import sys
import tempfile

from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_cache  # noqa: E402

page, out = os.path.abspath(sys.argv[1]), sys.argv[2]
W, H = 1600, 1000                          # the browser window (CSS pixels); the picture is 1600 x 1000


def chrome():
    for c in [os.environ.get("CHROME"), "google-chrome", "google-chrome-stable", "chromium", "chromium-browser"]:
        if c and shutil.which(c):
            return shutil.which(c)
    for c in ["/opt/pw-browsers/chromium/chrome-linux/chrome", "/opt/pw-browsers/chromium/chrome-linux64/chrome"]:
        if os.path.exists(c):
            return c
    return None


exe = chrome()
if not exe:
    sys.exit("map_still.py: no Chrome or Chromium found (set CHROME to its path)")
fp = build_cache.Fingerprint()
fp.add("page", open(page, "rb").read())
fp.add("script", open(os.path.abspath(__file__), "rb").read())
fp.add("chrome", subprocess.run([exe, "--version"], capture_output=True, text=True, timeout=60).stdout.strip())
fp = fp.hexdigest()
if build_cache.fetch("map-still", fp, out, "world-preview.jpg"):
    print(f"map still: unchanged inputs ({fp[:12]}), taken from the cache")
    sys.exit(0)
with tempfile.TemporaryDirectory() as tmp:
    shot = os.path.join(tmp, "still.png")
    subprocess.run([exe, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--mute-audio",
                    f"--user-data-dir={tmp}/profile", f"--window-size={W},{H}", "--force-device-scale-factor=2",
                    "--virtual-time-budget=15000", f"--screenshot={shot}", f"file://{page}?still"],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=180)
    im = Image.open(shot).convert("RGB")
if im.width < W or len(im.resize((32, 20)).getcolors(1024) or []) < 8:      # a blank or broken page has a handful of colours
    sys.exit(f"map_still.py: the screenshot looks empty ({im.size})")
im.resize((W, round(im.height * W / im.width)), Image.LANCZOS).save(out, quality=84, optimize=True, progressive=True)
build_cache.store("map-still", fp, out, "world-preview.jpg")
print(f"map still: taken ({fp[:12]})")
