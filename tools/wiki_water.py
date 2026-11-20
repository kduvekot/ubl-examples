"""The encyclopedia's water maps: the rivers it names, their basins and the watersheds between them, drawn from the
terrain (world/terrain.json and the rasters in world/terrain/), with numpy and PIL only (tools/build_wiki.py).

  water_map(land, rivers, path)        the whole mainland or Lisavu: every stream of the printed map, each named
                                       river's basin tinted by the river it reaches the sea by, the border, the
                                       towns and the rivers' names
  locator(land, rivers, rid, path)     a small map for one river's article: its basin and course on its land
"""
import json
import math
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.path.join(os.path.dirname(__file__), "..")
TERRAIN = json.load(open(os.path.join(ROOT, "world", "terrain.json"), encoding="utf-8"))
MAP = json.load(open(os.path.join(ROOT, "world", "map.json"), encoding="utf-8"))
FONTS = "/usr/share/fonts/truetype/dejavu/"
SEA = (190, 214, 230)
LAND = (236, 233, 222)
RIVER = (38, 96, 160)
BORDER = (150, 45, 45)
# a hue per river that reaches the sea; its tributaries' basins take the same hue, lighter and darker by turns
HUES = [(120, 170, 90), (215, 160, 80), (150, 120, 190), (90, 160, 175), (205, 110, 110), (175, 170, 80),
        (100, 140, 205), (190, 130, 90), (110, 175, 130), (185, 120, 165), (140, 140, 140), (210, 180, 90),
        (130, 150, 110)]


def font(size, bold=False, serif=False):
    name = ("DejaVuSerif" if serif else "DejaVuSans") + ("-Bold" if bold else "") + ".ttf"
    try:
        return ImageFont.truetype(os.path.join(FONTS, name), size)
    except OSError:
        return ImageFont.load_default()


def rasters(land):
    r = TERRAIN["rasters"][land]
    load = lambda k: np.array(Image.open(os.path.join(ROOT, r[k])))
    z = load("height").astype(float) - r["offset_m"]
    return z, load("cover") == 0, load("basins").astype(int), r


def roots(rivers):
    """river id -> the id of the river by which its water reaches the sea, and its depth below it."""
    by = {r["id"]: r for r in rivers}
    out = {}
    for r in rivers:
        q, depth = r, 0
        while q["parent"]:
            q, depth = by[q["parent"]], depth + 1
        out[r["id"]] = (q["id"], depth)
    return out


def tint(rivers, lab, sea, strength=0.45):
    rt = roots(rivers)
    sea_ids = sorted({v[0] for v in rt.values()}, key=lambda i: -next(r["basin_km2"] for r in rivers if r["id"] == i))
    hue = {i: HUES[k % len(HUES)] for k, i in enumerate(sea_ids)}
    img = np.zeros(lab.shape + (3,), float)
    img[:] = LAND
    for r in rivers:
        root, depth = rt[r["id"]]
        h = np.array(hue[root], float)
        s = strength * (1.0 if depth % 2 == 0 else 0.7)
        img[lab == r["id"]] = np.array(LAND) * (1 - s) + h * s
    img[sea] = SEA
    return img


def shade(img, z, sea, k=0.0022):
    gy, gx = np.gradient(z)
    sh = np.clip(1 - (gx - gy) * k, 0.82, 1.1)
    out = img * sh[..., None]
    out[sea] = SEA
    return np.clip(out, 0, 255).astype(np.uint8)


class Canvas:
    def __init__(self, land, scale):
        self.z, self.sea, self.lab, self.r = rasters(land)
        self.land, self.scale = land, scale
        self.S, self.X0, self.Y0 = self.r["cells_per_square"], self.r["x0"], self.r["y0"]

    def px(self, x, y):
        """squares to pixels"""
        return ((x - self.X0) * self.S * self.scale, (y - self.Y0) * self.S * self.scale)

    def image(self, arr):
        h, w = self.z.shape
        im = Image.fromarray(arr).resize((w * self.scale, h * self.scale), Image.BILINEAR)
        return im

    def estuary(self, dr):
        if self.land != "mainland":
            return
        for x, y in TERRAIN.get("estuary", []):
            (a, b), (c, d) = self.px(x, y), self.px(x + 1, y + 1)
            dr.rectangle([a, b, c, d], fill=SEA)

    def streams(self, dr, div, minimum=1, colour=RIVER):
        for line in TERRAIN["streams"][self.land]:
            for (x0, y0, a0), (x1, y1, a1) in zip(line, line[1:]):
                if a0 < minimum:
                    continue
                w = max(1, int(round(math.sqrt(a0) / div * self.scale / 2)))
                dr.line([self.px(x0, y0), self.px(x1, y1)], fill=colour, width=w)

    def border(self, dr, width):
        cc = TERRAIN["country"]
        for y in range(len(cc)):
            for x in range(len(cc[y])):
                if x + 1 < len(cc[y]) and {cc[y][x], cc[y][x + 1]} == {"U", "B"}:
                    dr.line([self.px(x + 1, y), self.px(x + 1, y + 1)], fill=BORDER, width=width)
                if y + 1 < len(cc) and {cc[y][x], cc[y + 1][x]} == {"U", "B"}:
                    dr.line([self.px(x, y + 1), self.px(x + 1, y + 1)], fill=BORDER, width=width)


def halo_text(dr, xy, text, f, fill, anchor="mm"):
    x, y = xy
    for dx in (-2, -1, 0, 1, 2):
        for dy in (-2, -1, 0, 1, 2):
            if dx or dy:
                dr.text((x + dx, y + dy), text, font=f, fill=(255, 255, 255), anchor=anchor)
    dr.text((x, y), text, font=f, fill=fill, anchor=anchor)


def water_map(land, rivers, names, path, scale=2):
    """rivers: the terrain's rivers of the land; names: river id -> its name on the map."""
    c = Canvas(land, scale)
    im = c.image(shade(tint(rivers, c.lab, c.sea), c.z, c.sea))
    dr = ImageDraw.Draw(im)
    c.estuary(dr)
    c.streams(dr, 26 if land == "mainland" else 9)
    if land == "mainland":
        c.border(dr, 3)
    taken = []

    def free(bb):
        return all(bb[2] < t[0] or bb[0] > t[2] or bb[3] < t[1] or bb[1] > t[3] for t in taken)

    ft = font(19, bold=True)
    for t in MAP["towns"]:
        if (land == "lisavu") != (t["country"] == "XL"):
            continue
        x, y = c.px(t["c"][0] + .5, t["c"][1] + .5)
        dr.rectangle([x - 6, y - 6, x + 6, y + 6], fill=(30, 30, 30), outline=(255, 255, 255))
        bb = dr.textbbox((x + 10, y), t["name"], font=ft, anchor="lm")
        halo_text(dr, (x + 10, y), t["name"], ft, (25, 25, 25), anchor="lm")
        taken.append((x - 8, y - 8, bb[2] + 4, bb[3] + 4))
    for r in sorted(rivers, key=lambda r: -r["basin_km2"]):
        size = 22 if r["basin_km2"] >= 5000 else 18 if r["basin_km2"] >= 1500 else 15
        f = font(size, bold=r["basin_km2"] >= 5000, serif=True)
        n = len(r["course"])
        for frac in (0.55, 0.45, 0.65, 0.35, 0.75, 0.3, 0.8, 0.5, 0.6, 0.4, 0.7):
            x, y = c.px(*r["course"][min(n - 1, int(n * frac))])
            bb = dr.textbbox((x, y - size * 0.9), names[r["id"]], font=f, anchor="mm")
            bb = (bb[0] - 3, bb[1] - 2, bb[2] + 3, bb[3] + 2)
            if free(bb):
                halo_text(dr, (x, y - size * 0.9), names[r["id"]], f, (20, 70, 135))
                taken.append(bb)
                break
    im = im.convert("P", palette=Image.ADAPTIVE, colors=128)
    im.save(path, optimize=True)


def locator(land, rivers, rid, path, scale=1):
    """One river's basin (its own and its tributaries') and course, on its land, small."""
    c = Canvas(land, scale)
    by = {r["id"]: r for r in rivers}
    inside = {rid}
    grew = True
    while grew:
        more = {r["id"] for r in rivers if r["parent"] in inside} - inside
        grew, inside = bool(more), inside | more
    arr = np.zeros(c.lab.shape + (3,), float)
    arr[:] = LAND
    mask = np.isin(c.lab, list(inside))
    arr[mask] = np.array(LAND) * 0.45 + np.array((120, 165, 205)) * 0.55
    arr[c.sea] = SEA
    im = c.image(shade(arr, c.z, c.sea))
    dr = ImageDraw.Draw(im)
    c.estuary(dr)
    c.streams(dr, 60 if land == "mainland" else 20, colour=(110, 150, 190))
    if land == "mainland":
        c.border(dr, 1)
    pts = [c.px(x, y) for x, y in by[rid]["course"]]
    dr.line(pts, fill=(15, 60, 130), width=4 if land == "mainland" else 3)
    for t in MAP["towns"]:
        if (land == "lisavu") != (t["country"] == "XL"):
            continue
        x, y = c.px(t["c"][0] + .5, t["c"][1] + .5)
        dr.rectangle([x - 3, y - 3, x + 3, y + 3], fill=(30, 30, 30))
    im = im.filter(ImageFilter.SMOOTH) if scale > 1 else im
    im = im.convert("P", palette=Image.ADAPTIVE, colors=64)
    im.save(path, optimize=True)
