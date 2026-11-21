#!/usr/bin/env python3
"""The picture of the map on the home page: the 3D map as it opens, taken by a headless Chrome.

Usage: python3 tools/map_still.py <site-dir>/world.html <out.jpg>

Opens world.html?still (the map alone, without toolbar and panel: see site/world.html), waits for it to be
drawn, and takes a screenshot of 1600 x 1000 pixels (the home page shows it at most about 1100 pixels wide). Chrome is found as $CHROME, on the
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
    """$CHROME, else Playwright's Chromium where it is installed (in the cloud sessions), else a Chrome or Chromium on
    the PATH (GitHub Actions has google-chrome)."""
    for c in [os.environ.get("CHROME"), "/opt/pw-browsers/chromium", "chromium", "chromium-browser", "google-chrome",
              "google-chrome-stable"]:
        if c and (shutil.which(c) or (os.path.isfile(c) and os.access(c, os.X_OK))):
            return shutil.which(c) or c
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
def by_playwright(shot):
    """The picture through Python's Playwright, where it is installed: no outside requests, and taken when the page
    says it is drawn (data-ready). False when Playwright is not there."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return False
    try:
        return _playwright(sync_playwright, shot)
    except Exception as e:                     # no browser for this Playwright, or it failed: the command line
        print(f"map still: Playwright failed ({type(e).__name__}), using Chrome's command line", file=sys.stderr)
        return False


def _playwright(sync_playwright, shot):
    with sync_playwright() as pw:
        b = pw.chromium.launch(**({"executable_path": exe} if os.environ.get("CHROME") else {}))
        try:
            pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
            pg.route(lambda url: url.startswith(("http:", "https:")), lambda route: route.abort())
            pg.goto(f"file://{page}?still")
            pg.wait_for_function("document.documentElement.dataset.ready === '1'", timeout=45000)
            pg.screenshot(path=shot)
        finally:
            b.close()
    return True


def by_command_line(shot, tmp):
    """The picture through Chrome's command line (GitHub Actions): the still page stops animating once it is drawn,
    so that the virtual time budget ends."""
    subprocess.run([exe, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars", "--mute-audio",
                    f"--user-data-dir={tmp}/profile", f"--window-size={W},{H}", "--force-device-scale-factor=1",
                    # no outside requests (the web fonts): headless Chrome's virtual time waits for every request;
                    # the labels fall back to a system font, and the picture is the same everywhere
                    "--host-resolver-rules=MAP * ~NOTFOUND",
                    # the still page is drawn in its first frame (the whole world at the opening zoom comes from the
                    # overview, with no chunks to wait for) and then stops: a short budget is enough, and where
                    # virtual time runs slowly (as it did in GitHub Actions) a long one is waited for in full
                    "--virtual-time-budget=5000", f"--screenshot={shot}", f"file://{page}?still"],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=45)


import time  # noqa: E402
t0 = time.time()
with tempfile.TemporaryDirectory() as tmp:
    shot = os.path.join(tmp, "still.png")
    how = "Playwright" if by_playwright(shot) else "Chrome's command line"
    if how != "Playwright":
        by_command_line(shot, tmp)
    im = Image.open(shot).convert("RGB")
if im.width < W or len(im.resize((32, 20)).getcolors(1024) or []) < 8:      # a blank or broken page has a handful of colours
    sys.exit(f"map_still.py: the screenshot looks empty ({im.size})")
im.resize((W, round(im.height * W / im.width)), Image.LANCZOS).save(out, quality=84, optimize=True, progressive=True)
build_cache.store("map-still", fp, out, "world-preview.jpg")
print(f"map still: taken ({fp[:12]}) with {how} in {time.time() - t0:.1f} s")
