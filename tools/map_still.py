#!/usr/bin/env python3
"""The picture of the map on the home page: the 3D map as it opens, taken by a headless Chrome.

Usage: python3 tools/map_still.py <site-dir>/world.html <out.jpg>

Opens world.html?still (the map alone, without toolbar and panel: see site/world.html), waits for it to be
drawn, takes a screenshot at twice the size and makes it 1600 pixels wide. Chrome is found as $CHROME, on the
PATH (google-chrome, chromium, ...) or in Playwright's browser folder.
"""
import os
import shutil
import subprocess
import sys
import tempfile

from PIL import Image

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
print(f"map still: {out}")
