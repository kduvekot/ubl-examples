#!/usr/bin/env python3
"""Crawl the UBL sample documents published on docs.oasis-open.org.

For every UBL 2.x stage directory (prd2-UBL-2.0 ... os-UBL-2.5) this script
walks the stage's ``xml/`` folder recursively, downloads every file into a
local cache and writes a manifest describing exactly what was published:

    path in the stage's xml/ folder, size, server timestamp, SHA-256

The manifest (``history/manifest.json``) is the input for
``build_history.py``. Re-running the crawl and comparing manifests shows
whether OASIS changed anything since.

Usage:
    python3 tools/crawl_oasis.py --cache <dir> [--out history/manifest.json]

Standard library only. Honours HTTPS_PROXY and SSL_CERT_FILE.
"""
import argparse
import hashlib
import json
import os
import re
import ssl
import sys
import time
import urllib.parse
import urllib.request

BASE = "https://docs.oasis-open.org/ubl/"
# Stage directories of UBL 2.x itself (not NDR, JSON, ASN.1, UML, ...).
STAGE_RE = re.compile(r"^(prd\d*(r\d+)?|cs\d*|cos\d*|csd\d+|csprd\d+|os|errata)-UBL-2\.\d(-update)?/$")
# Apache "fancy index" line:  <a href="x">x</a>   12-Dec-2006 12:00   6K
ROW_RE = re.compile(r'<a href="([^"?]+)">[^<]*</a>\s+(\d{2}-\w{3}-\d{4} \d{2}:\d{2})\s+(\S+)')

def ssl_ctx():
    cafile = os.environ.get("SSL_CERT_FILE") or (
        "/root/.ccr/ca-bundle.crt" if os.path.exists("/root/.ccr/ca-bundle.crt") else None)
    return ssl.create_default_context(cafile=cafile)

CTX = ssl_ctx()

def get(url, retries=4):
    for attempt in range(retries + 1):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ubl-examples-crawler/1.0"})
            with urllib.request.urlopen(req, context=CTX, timeout=60) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return 404, b""
            err = e
        except Exception as e:  # network hiccup
            err = e
        time.sleep(2 ** (attempt + 1))
    raise RuntimeError(f"failed to fetch {url}: {err}")

def listing(url):
    """Return (subdirs, files) of an Apache index page; files are (name, mtime)."""
    status, body = get(url)
    if status == 404:
        return None
    html = body.decode("utf-8", "replace")
    dirs, files = [], []
    for href, mtime, _size in ROW_RE.findall(html):
        if href.startswith(("/", "..", "http")):
            continue
        name = urllib.parse.unquote(href)
        t = time.strftime("%Y-%m-%dT%H:%M", time.strptime(mtime, "%d-%b-%Y %H:%M"))
        (dirs if href.endswith("/") else files).append((name.rstrip("/"), t))
    return dirs, files

def walk(url, prefix=""):
    res = listing(url)
    if res is None:
        return
    dirs, files = res
    for name, t in files:
        yield prefix + name, url + urllib.parse.quote(name), t
    for name, _t in dirs:
        yield from walk(url + urllib.parse.quote(name) + "/", prefix + name + "/")

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cache", required=True, help="directory to store downloaded files")
    ap.add_argument("--out", default="history/manifest.json")
    args = ap.parse_args()

    _, root = get(BASE)
    stages = sorted({m for m in re.findall(r'href="([^"/]+/)"', root.decode()) if STAGE_RE.match(m)})
    manifest = {"source": BASE, "crawled": time.strftime("%Y-%m-%d"), "stages": {}}
    for stage in stages:
        stage = stage.rstrip("/")
        entries = []
        for path, url, mtime in walk(f"{BASE}{stage}/xml/"):
            dest = os.path.join(args.cache, stage, "xml", path)
            if not os.path.exists(dest):
                status, data = get(url)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                with open(dest, "wb") as f:
                    f.write(data)
            with open(dest, "rb") as f:
                data = f.read()
            entries.append({"path": path, "size": len(data), "mtime": mtime,
                            "sha256": hashlib.sha256(data).hexdigest()})
        manifest["stages"][stage] = {"has_xml": bool(entries), "files": entries}
        print(f"{stage:24} {len(entries):4} files", file=sys.stderr)
    os.makedirs(os.path.dirname(args.out) or ".", exist_ok=True)
    with open(args.out, "w") as f:
        json.dump(manifest, f, indent=1, sort_keys=False)
        f.write("\n")

if __name__ == "__main__":
    main()
