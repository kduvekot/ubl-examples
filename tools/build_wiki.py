#!/usr/bin/env python3
"""The Encyclopedia of the UBL World (CLAUDE.md, open work 2): articles generated from the world data.

Every article's prose sits next to the data it is about, in a "wiki" key on its record:

  * a country: world/countries.json  countries.<code>.wiki
  * the Trade Accord: world/countries.json  trade_accord.wiki
  * a town: world/map.json  towns[].wiki
  * a party: world/parties.json  parties[].wiki

  "wiki": {"short": "a short description under the title",
           "lead": "the opening paragraph",
           "sections": [{"title": "History", "text": "..."}, ...]}

Texts are Markdown. "{population}" and the like are filled in from the data (an unknown name stops the build);
"[[Name]]" or "[[Name|text]]" links another article by its title (a name the world does not know stops the build; a
name without an article yet is written as plain text). The infobox, the districts, the companies of a town, the
and the categories are made from the data. An encyclopedia does not list the business documents a company exchanges
(owner): those stay on the main site.

Usage: python3 tools/build_wiki.py <md-dir>     writes <md-dir>/<slug>.md, one per article, and index.md
"""
import json
import math
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(__file__))
import world_data  # noqa: E402

ROOT = os.path.join(os.path.dirname(__file__), "..")
out = sys.argv[1]
import world_facts  # noqa: E402
world = world_facts.fill_world(world_data.load())   # {fact:…} in the published texts (stage 7 B2)
world_data.number_documents(world)
countries = world["countries"]
PARTY = {p["id"]: p for p in world["parties"]}
MAP = world_facts.fill_world(json.load(open(os.path.join(ROOT, "world", "map.json"), encoding="utf-8")))
CJSON = world_facts.fill_world(json.load(open(os.path.join(ROOT, "world", "countries.json"), encoding="utf-8")))
SITE = "../"                                   # the main site, seen from /wiki/ (one setting, for a later subdomain)
problems = []


def slug(name):
    s = unicodedata.normalize("NFKD", name).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def n0(v):
    return f"{v:,}"


# ---------------------------------------------------------------- the subjects: every thing an article may be about
articles = {}       # title -> {"kind", "key", "data", "wiki"}
known = set()       # every name the world knows, with or without an article
for code, c in countries.items():
    known.add(c["name"])
    if c.get("wiki"):
        articles[c["name"]] = {"kind": "country", "key": code, "data": c, "wiki": c["wiki"]}
acc = CJSON.get("trade_accord")
if acc:
    known.add(acc["name"])
    if acc.get("wiki"):
        articles[acc["name"]] = {"kind": "accord", "key": "accord", "data": acc, "wiki": acc["wiki"]}
for t in MAP["towns"]:
    known.add(t["name"])
    if t.get("wiki"):
        articles[t["name"]] = {"kind": "town", "key": t["name"], "data": t, "wiki": t["wiki"]}
for v in MAP.get("villages", []):
    if v.get("name"):
        known.add(v["name"])
        articles[v["name"]] = {"kind": "village", "key": v["name"], "data": v, "wiki": v.get("wiki") or {}}
for v in MAP.get("localities", []):
    known.add(v["name"])
    articles[v["name"]] = {"kind": "locality", "key": v["name"], "data": v, "wiki": v.get("wiki") or {}}
for r in MAP["routes"]:
    if r.get("wiki"):
        known.add(r["wiki"]["title"])
        articles[r["wiki"]["title"]] = {"kind": "route", "key": r["id"], "data": r, "wiki": r["wiki"]}
for code, lang in CJSON.get("languages", {}).items():
    known.add(lang["name"])
    if lang.get("wiki"):
        articles[lang["name"]] = {"kind": "language", "key": code, "data": lang, "wiki": lang["wiki"]}
for code, c in countries.items():
    cur = c["currency"]
    known.add(cur["name"])
    if cur.get("wiki"):
        articles[cur["name"]] = {"kind": "currency", "key": cur["code"], "data": dict(cur, country=code), "wiki": cur["wiki"]}
for p in world["parties"]:
    known.add(p["identity"]["name"])
    if p["identity"].get("person"):         # no articles about persons, and no names of persons (owner)
        continue
    if p.get("wiki"):
        articles[p["identity"]["name"]] = {"kind": "party", "key": p["id"], "data": p, "wiki": p["wiki"]}
for it in world["items"]:
    known.add(it["name"])
    if it.get("wiki"):
        articles[it["name"]] = {"kind": "item", "key": it["id"], "data": it, "wiki": it["wiki"]}
# the rivers the terrain finds (world/terrain.json, rivers) under the names world/map.json gives them, matched by mouth
TERR = json.load(open(os.path.join(ROOT, "world", "terrain.json"), encoding="utf-8"))
RIVERS = {}         # (land, id) -> the river's article data
for land, found in TERR.get("rivers", {}).items():
    for r in found:
        rec = min(MAP.get("rivers", []), key=lambda n: math.hypot(n["mouth"][0] - r["mouth"][0], n["mouth"][1] - r["mouth"][1])
                  if n["land"] == land else 1e9, default=None)
        if not rec or math.hypot(rec["mouth"][0] - r["mouth"][0], rec["mouth"][1] - r["mouth"][1]) > 0.5:
            problems.append(f"the river of {land} with its mouth at {r['mouth']} has no name in world/map.json (rivers)")
            continue
        RIVERS[(land, r["id"])] = dict(r, land=land, rec=rec)
for (land, rid), r in RIVERS.items():
    r["into"] = RIVERS.get((land, r["parent"])) if r["parent"] else None
    r["tributaries"] = sorted((q for q in RIVERS.values() if q["land"] == land and q["parent"] == rid),
                              key=lambda q: -q["basin_km2"])
    known.add(r["rec"]["title"])
    articles[r["rec"]["title"]] = {"kind": "river", "key": f"{land}-{rid}", "data": r, "wiki": r["rec"].get("wiki") or {}}
for lm in MAP.get("landmarks", []):                  # mountains, capes, coasts, meeting grounds
    known.add(lm["name"])
    if lm.get("wiki"):
        articles[lm["name"]] = {"kind": "landmark", "key": lm["name"], "data": lm, "wiki": lm["wiki"]}
WATERS = MAP.get("waters")
if WATERS and RIVERS:
    known.add(WATERS["title"])
    articles[WATERS["title"]] = {"kind": "waters", "key": "waters", "data": WATERS, "wiki": WATERS["wiki"]}
page = {title: slug(title) + ".html" for title in articles}


def links(text, where):
    def one(m):
        target, label = (m.group(1).split("|", 1) + [None])[:2]
        label = label or target
        if target in page:
            return f"[{label}]({page[target]})"
        if target not in known:
            problems.append(f"{where}: [[{target}]] names nothing the world knows")
        return label
    return re.sub(r"\[\[([^\]]+)\]\]", one, text)


def fill(text, values, where):
    def one(m):
        if m.group(1) not in values:
            problems.append(f"{where}: {{{m.group(1)}}} is not a value of this subject")
            return m.group(0)
        return str(values[m.group(1)])
    try:                                          # the world's registered facts first (tools/world_facts.py, B2)
        text = world_facts.fill(text)
    except KeyError as e:
        problems.append(f"{where}: {e.args[0]}")
    return re.sub(r"\{([a-z_][a-z0-9_]*)\}", one, text)


# ---------------------------------------------------------------- articles the data writes by itself: villages, localities
LANGNAME = {code: lang["name"] for code, lang in CJSON.get("languages", {}).items()}
BAND = {"hamlet": "hamlet", "village": "village", "large village": "village", "small town": "small town",
        "country town": "country town"}


def lies(text):
    """'Where a stream …' or 'On the plateau …' as a sentence: 'It lies where a stream …'."""
    t = text.strip()
    return "It lies " + t[0].lower() + t[1:] if t and t.split()[0] in ("Where", "On", "In", "At", "By", "Near", "Between", "Beside", "Above", "Below", "Just", "High", "Low", "Along", "Behind", "Under") else t


def lives(text):
    """'Cotton, fishing.' as 'It lives from cotton and fishing.'; a sentence of its own ('A sheep station's village: …') stays."""
    t = text.strip()
    if t.split()[0] in ("A", "An", "The", "Its"):
        return t
    t = t[0].lower() + t[1:]
    if ";" not in t and " and " not in t and t.count(", ") >= 1:
        head, _, last = t.rpartition(", ")
        t = f"{head} and {last}"
    return "It lives from " + t


PEOPLE = {"Urvanian": "Urvanians", "Lisavan": "Lisavans", "British": "the British", "Italian": "Italians",
          "Sardinian": "Sardinians", "Tuscan": "Tuscans"}


MORE = {"the station 19th century": "its station dates from the 19th century",
        "the village after it": "the village grew up after it",
        "the Urvanian hamlet older": "the Urvanian hamlet is older",
        "named under Italian rule": "it was named under Italian rule",
        "the harbour light Italian, 1890s": "the harbour light was built under Italian rule in the 1890s"}


def variant(seed, n):
    """A stable choice among n wordings, so that generated texts do not all read alike."""
    import hashlib
    return int(hashlib.sha256(seed.encode()).hexdigest(), 16) % n


def founded(text, seed=""):
    """'Urvanian, before 1600; named under Italian rule' as a sentence: 'It was founded by Urvanians before 1600; …'."""
    who, _, rest = text.partition(", ")
    when, sep, more = rest.partition("; ")
    when, paren, note = when.partition(" (")
    if when == "old":
        when = "long before the settlers came"
    elif m := re.match(r"(\w+) to (\w+ century)(.*)", when):
        when = f"in the {m[1]} or {m[2]}{m[3]}"
    elif m := re.match(r"(\d\w+) to (\d\w+)$", when):
        when = f"between the {m[1]} and the {m[2]}"
    elif re.match(r"\d{4}\b", when):
        when = "in " + when
    elif re.match(r"\d|late |early ", when):
        when = "in the " + when
    by = PEOPLE.get(who, who)
    out = [f"It was founded by {by} {when}", f"{by[0].upper()}{by[1:]} founded it {when}",
           f"Its first settlers were {by}, {when}"][variant(seed + text, 2 if "settlers" in by or by.startswith("the ") else 3)]
    if paren:
        out += " (" + note
    if sep:
        out += "; " + MORE.get(more, more)
    return out + "."


for title, a in articles.items():
    if a["kind"] in ("village", "locality") and not a["wiki"].get("lead"):
        d = a["data"]
        cname = countries[d["country"]]["name"]
        if a["kind"] == "village":
            a["wiki"] = {"short": f"{BAND.get(d.get('band'), 'village').capitalize()} in {cname}",
                         "lead": f"**{title}** is a {BAND.get(d.get('band'), 'village')} in [[{cname}]], with about {n0(d['people'])} people.",
                         "sections": [x for x in (
                             {"title": "Geography", "text": lies(d["why"])} if d.get("why") else None,
                             {"title": "History", "text": founded(d["founded"], title)} if d.get("founded") else None,
                             {"title": "Economy", "text": lives(d["lives_on"])}
                             if d.get("lives_on") else None) if x]}
        else:
            lo, hi = d["population"]
            a["wiki"] = {"short": f"Locality in {cname}",
                         "lead": f"**{title}** is a locality in [[{cname}]], with {n0(lo)} to {n0(hi)} people. {d.get('note', '')}".strip(),
                         "sections": []}


# ---------------------------------------------------------------- rivers: facts the terrain gives
CCODE = {"U": "XU", "B": "XB", "L": "XL"}


def rlink(r):
    t, n = r["rec"]["title"], r["rec"]["name"]
    return f"[[{t}]]" if t == n else f"[[{t}|{n}]]"


def river_countries(r):
    tot = sum(r["countries"].values()) or 1
    return [CCODE[c] for c, k in sorted(r["countries"].items(), key=lambda kv: -kv[1]) if k / tot >= 0.15]


def river_places(r):
    """the towns and villages on the river, downstream, within a square of its course"""
    out = []
    for t in MAP["towns"] + MAP.get("villages", []):
        if not t.get("name"):
            continue
        x, y = t["c"][0] + .5, t["c"][1] + .5
        dist = [math.hypot(px - x, py - y) for px, py in r["course"]]
        k = min(range(len(dist)), key=dist.__getitem__)
        if dist[k] <= 1.0:
            out.append((k, t["name"]))
    return [n for _, n in sorted(out)]


_BASINS = {}


def basin_towns(r):
    """the towns whose water reaches the sea by this river: in its own basin or a tributary's"""
    import numpy as np
    from PIL import Image
    land, ras = r["land"], TERR["rasters"][r["land"]]
    if land not in _BASINS:
        _BASINS[land] = np.array(Image.open(os.path.join(ROOT, ras["basins"])))
    lab = _BASINS[land]
    inside, grew = {r["id"]}, True
    while grew:
        more = {q["id"] for q in RIVERS.values() if q["land"] == land and q["parent"] in inside} - inside
        grew, inside = bool(more), inside | more
    S = ras["cells_per_square"]
    out = []
    for t in sorted(MAP["towns"], key=lambda t: -t["population"]):
        cy, cx = int((t["c"][1] + .5 - ras["y0"]) * S), int((t["c"][0] + .5 - ras["x0"]) * S)
        if 0 <= cy < lab.shape[0] and 0 <= cx < lab.shape[1] and int(lab[cy, cx]) in inside:
            out.append(t["name"])
    return out


def border_km(r):
    if r["land"] != "mainland":
        return 0
    bw = TERR.get("border_water", [])
    near = [min(math.hypot(px - bx, py - by) for bx, by in bw) <= 0.75 for px, py in r["course"]] if bw else []
    km = sum(math.hypot(r["course"][k][0] - r["course"][k - 1][0], r["course"][k][1] - r["course"][k - 1][1]) * 3.5
             for k in range(1, len(near)) if near[k] and near[k - 1])
    return int(round(km, -1))


def coast(r):
    cc = TERR["country"]
    want = "L" if r["land"] == "lisavu" else "UB"
    sq = [(x, y) for y in range(len(cc)) for x in range(len(cc[y])) if cc[y][x] in want]
    cx, cy = sum(x for x, _ in sq) / len(sq), sum(y for _, y in sq) / len(sq)
    ang = math.degrees(math.atan2(-(r["mouth"][1] - cy), r["mouth"][0] - cx)) % 360
    return ["east", "north-east", "north", "north-west", "west", "south-west", "south", "south-east"][int(((ang + 22.5) % 360) // 45)]


for title, a in articles.items():
    if a["kind"] != "river":
        continue
    r, w = a["data"], a["wiki"]
    rec = r["rec"]
    cs = river_countries(r)
    where = " and ".join(f"[[{countries[c]['name']}]]" for c in cs)
    places = river_places(r)
    if r["into"]:
        end = f"joins the {rlink(r['into'])}"
    else:
        end = f"reaches the sea on the {rec.get('coast') or coast(r)} coast" + (f" at [[{places[-1]}]]" if places and places[-1] in articles else "")
    lead = [f"The **{rec['name']}** is a river of {where}, {{km}} km long, with a basin of {{basin}} km². "
            f"It rises at about {{source_m}} m and {end}.",
            f"The **{rec['name']}**, a river of {where} {{km}} km long, drains a basin of {{basin}} km². "
            f"From its source at about {{source_m}} m it {end}.",
            f"The **{rec['name']}** rises at about {{source_m}} m in {where} and {end} after {{km}} km; "
            f"its basin covers {{basin}} km²."][variant(title, 3)]
    bk = border_km(r)
    if bk >= 10:
        lead += f" For about {bk} km it forms the border between [[Urvania]] and [[Bayvarra]]."
    nf = rec.get("name_from", {})
    if r["land"] == "mainland" and "qau" in nf and rec["names"].get("it"):
        lead += f" Its Urvanian name, *{rec['names']['qau']}*, means {nf['qau']}."
    elif "qal" in nf:
        lead += f" Its Lisavan name means {nf['qal']}."
    a["wiki"] = dict({"short": f"River of {' and '.join(countries[c]['name'] for c in cs)}", "lead": lead}, **w)


PLACES = sorted((t for t, a in articles.items() if a["kind"] in ("town", "village", "locality", "country")), key=len, reverse=True)


def autolink(text, own):
    """The first mention of each town, village or country in a generated text becomes a link."""
    for t in PLACES:
        if t != own and "[[" + t not in text:
            text = re.sub(rf"(?<![\w\[]){re.escape(t)}(?![\w\]])", f"[[{t}]]", text, count=1)
    return text


for title, a in articles.items():
    if a["kind"] in ("village", "locality") and not a["data"].get("wiki"):
        for sec in a["wiki"].get("sections", []):
            sec["text"] = autolink(sec["text"], title)


# ---------------------------------------------------------------- facts from the data, per kind
def town_of(p):
    return p["identity"]["address"].get("CityName", "")


def flight_values():
    """The air route's timetable as the texts write it, from world/map.json (route "air", "flight") and the map's
    distance between the airports (tools/world_map.py flight): one block time everywhere (stage 7 A3)."""
    import world_map
    f = world_map.flight(world)
    m = round(f["still_air"] * 4) / 4                 # still air to the quarter hour, in words as a timetable is not
    words = f"{int(m)}{dict([(0.0, ''), (0.25, '¼'), (0.5, '½'), (0.75, '¾')])[m - int(m)]} hours"
    return {"flight_km": n0(int(round(f["km"], -1))), "flight_east": world_map.duration(f["east"]),
            "flight_west": world_map.duration(f["west"]), "flight_still_air": words}


def values(a):
    d = a["data"]
    if a["kind"] == "route" and d["mode"] == "air":
        return flight_values()
    if a["kind"] == "country":
        pop = d.get("population", {})
        tot = pop.get("total", 0)
        about = f"{tot / 1e6:.1f} million" if tot >= 1e6 else n0(round(tot, -4))    # prose rounds; the infobox is exact
        return {"population": about, "currency": d["currency"]["name"],
                "currency_code": d["currency"]["code"], "code": a["key"]}
    if a["kind"] == "town":
        return {"population": n0(d["population"]), "built_km": d["built_km"], "country": countries[d["country"]]["name"]}
    if a["kind"] == "village":
        return {"people": n0(d["people"])}
    if a["kind"] == "river":
        return {"km": n0(d["km"]), "basin": n0(d["basin_km2"]), "source_m": n0(d["source_m"])}
    if a["kind"] == "waters":
        main = RIVERS.get(("mainland", 1))
        area = TERR["measures"]["mainland"]["area_km2"]
        return {"mainland_rivers": sum(1 for k in RIVERS if k[0] == "mainland"),
                "lisavu_rivers": sum(1 for k in RIVERS if k[0] == "lisavu"),
                "main_km": n0(main["km"]), "main_basin": n0(main["basin_km2"]),
                "main_share": round(100 * main["basin_km2"] / area), "main_source_m": n0(main["source_m"])}
    if a["kind"] == "party":
        lg = d["identity"].get("legal", {})
        return {"founded_year": lg.get("founded", "")[:4], "employees": n0(lg.get("headcount", 0)),
                "town": town_of(d), **(flight_values() if any(f.get("kind") == "air"
                                                                for f in d.get("fleet") or []) else {})}
    return {}


def infobox(a):
    d, rows = a["data"], []
    if a["kind"] == "country":
        capital = next((t["name"] for t in MAP["towns"] if t["country"] == a["key"] and t["population"] ==
                        max(x["population"] for x in MAP["towns"] if x["country"] == a["key"])), "")
        langs = ", ".join(world["languages"][code]["name"] if code in world.get("languages", {}) else code
                          for code in d.get("languages", []))
        rows = [("Capital", f"[[{capital}]]"), ("Languages", langs),
                ("Population", n0(d.get("population", {}).get("total", 0))),
                ("Currency", f"{d['currency']['name']} ({d['currency']['code']})"),
                ("Time", d.get("legal_time", "")), ("Country code", a["key"]),
                ("Taxes", "; ".join(x["name"] for x in d["tax"]["schemes"]))]
    elif a["kind"] == "accord":
        rows = [("Signed", d.get("signed", "")), ("In force", d.get("in_force", "")),
                ("Members", ", ".join(f"[[{countries[c]['name']}]]" for c in d.get("members", []))),
                ("Seat", f"[[{d['seat']}]]" if d.get("seat") else "")]
    elif a["kind"] == "town":
        rows = [("Country", f"[[{countries[d['country']]['name']}]]"), ("Population", n0(d["population"])),
                ("Built-up area", f"about {d['built_km']} km across"),
                ("Districts", str(len(d.get("districts", []))))]
    elif a["kind"] == "party":
        idn, lg = d["identity"], d["identity"].get("legal", {})
        form = countries[d["c"]].get("legal_forms", {}).get(lg.get("form"), {}).get("name", lg.get("form", ""))
        rows = [("Type", form), ("Founded", longdate(lg.get("founded", ""))), ("Seat", f"[[{town_of(d)}]], [[{countries[d['c']]['name']}]]"),
                ("Employees", n0(lg["headcount"]) if lg.get("headcount") else ""),
                ("Website", idn.get("website", ""))]
    elif a["kind"] == "village":
        rows = [("Country", f"[[{countries[d['country']]['name']}]]"), ("Population", n0(d["people"])),
                ("Founded", d.get("founded", "")),
                ("Names", " · ".join(f"{v} ({LANGNAME.get(k, k)})" for k, v in d.get("names", {}).items())
                 if len(set(d.get("names", {}).values())) > 1 else "")]
    elif a["kind"] == "locality":
        rows = [("Country", f"[[{countries[d['country']]['name']}]]"),
                ("Population", f"{n0(d['population'][0])} to {n0(d['population'][1])}"),
                ("Names", " · ".join(f"{v} ({LANGNAME.get(k, {'en': 'English', 'it': 'Italian'}.get(k, k))})" for k, v in d.get("names", {}).items())
                 if len(set(d.get("names", {}).values())) > 1 else "")]
    elif a["kind"] == "route":
        rows = [("Kind", {"rail": "Railway", "pipeline": "Pipeline", "river": "River", "sea": "Shipping route",
                          "air": "Air route"}[d["mode"]])]
    elif a["kind"] == "language":
        rows = [("Own name", d.get("own_name", "")), ("Spoken in", f"[[{countries[d['country']]['name']}]]" if d.get("country") in countries else "")]
    elif a["kind"] == "currency":
        rows = [("Code", d["code"]), ("Country", f"[[{countries[d['country']]['name']}]]"),
                ("Minor unit", {0: "none", 2: "1/100", 3: "1/1000"}.get(d.get("minor_units"), ""))]
    elif a["kind"] == "river":
        rec = d["rec"]
        names = rec.get("names", {})
        rows = [("", f'<img src="river-{a["key"]}.png" alt="The basin and course of the river {rec["name"]}">'),
                ("Country", ", ".join(f"[[{countries[c]['name']}]]" for c in river_countries(d))
                 + ("; the border with [[Bayvarra]] for about " + f"{border_km(d)} km" if border_km(d) >= 10 else "")),
                ("Length", f"{n0(d['km'])} km"), ("Basin", f"{n0(d['basin_km2'])} km²"),
                ("Source", f"about {n0(d['source_m'])} m"),
                ("Mouth", rlink(d["into"]) if d["into"] else "the sea"),
                ("Tributaries", ", ".join(rlink(q) for q in d["tributaries"])),
                ("Names", " · ".join(f"{v} ({LANGNAME.get(k, {'it': 'Italian', 'en': 'English'}.get(k, k))})"
                                      for k, v in names.items()) if len(names) > 1 else "")]
    elif a["kind"] == "landmark":
        land = d.get("country") or {"lisavu": "XL"}.get(d["land"], "")
        names = d.get("names", {})
        rows = [("Kind", d["kind"].capitalize()), ("Country", f"[[{countries[land]['name']}]]" if land else ""),
                ("Height", f"about {n0(d['height_m'])} m" if d.get("height_m") else ""),
                ("Names", " · ".join(f"{v} ({LANGNAME.get(k, {'en': 'English'}.get(k, k))})" for k, v in names.items())
                 if len(names) > 1 else "")]
    elif a["kind"] == "item":
        rows = [("Maker", f"[[{PARTY[d['seller']]['identity']['name']}]]"),
                ("Dimensions", " × ".join(str(x) for x in d["dimensions_mm"]) + " mm" if d.get("dimensions_mm") else ""),
                ("Weight", f"{d['net_kg']:g} kg" if d.get("net_kg") else "")]
    rows += [(k, fill(v, values(a), a.get("key", ""))) for k, v in (a["wiki"].get("facts") or {}).items()]
    cells = "".join((f"<tr><th>{k}</th><td>{v}</td></tr>" if k else f'<tr><td colspan="2" class="map">{v}</td></tr>')
                    for k, v in rows if v)
    return cells


def md_inline(text, where):
    """Markdown links inside the infobox's HTML: [[...]] to <a>."""
    def one(m):
        target, label = (m.group(1).split("|", 1) + [None])[:2]
        label = label or target
        if target in page:
            return f'<a href="{page[target]}">{label}</a>'
        if target not in known:
            problems.append(f"{where}: [[{target}]] names nothing the world knows")
        return label
    return re.sub(r"\[\[([^\]]+)\]\]", one, text)


CLIMATE = json.load(open(os.path.join(ROOT, "world", "climate.json"), encoding="utf-8")) \
    if os.path.exists(os.path.join(ROOT, "world", "climate.json")) else {}
LAPSE_C_PER_M = 0.0065


def town_climate(t, point):
    """A capital's climate table: the base values at sea level (world/climate.json), the temperature corrected for
    the town's height (6.5 °C per 1,000 m), the rain scaled to the town's yearly rain in the terrain."""
    import base64
    import numpy as np
    from PIL import Image
    base = CLIMATE["points"][point]
    cm = TERR["corners_m"]
    z = np.frombuffer(base64.b64decode(cm["int16_le_base64"]), dtype="<i2").reshape(cm["rows"], cm["cols"])
    x, y = t["c"]
    height = float(z[max(y - 1, 0):y + 3, max(x - 1, 0):x + 3].min())   # the town's lowest ground nearby: a port on the shore stands at the sea
    land = "lisavu" if t["country"] == "XL" else "mainland"
    ras = TERR["rasters"][land]
    rain = np.array(Image.open(os.path.join(ROOT, ras["rain"]))).astype(float)
    S = ras["cells_per_square"]
    cy, cx = int((y + .5 - ras["y0"]) * S), int((x + .5 - ras["x0"]) * S)
    year_rain = float(rain[max(cy - 2, 0):cy + 3, max(cx - 2, 0):cx + 3].mean())
    k = year_rain / sum(base["rain_mm"])
    dt = LAPSE_C_PER_M * max(height, 0)
    r1 = lambda v: f"{v:.1f}"
    rows = [("Mean daily high (°C)", [r1(v - dt) for v in base["high_c"]], r1(sum(base["high_c"]) / 12 - dt)),
            ("Daily mean (°C)", [r1(v - dt) for v in base["mean_c"]], r1(sum(base["mean_c"]) / 12 - dt)),
            ("Mean daily low (°C)", [r1(v - dt) for v in base["low_c"]], r1(sum(base["low_c"]) / 12 - dt)),
            ("Rain (mm)", [f"{round(v * k)}" for v in base["rain_mm"]], f"{round(year_rain):,}"),
            ("Solar radiation (kWh/m² a day)", [r1(v) for v in base["sun_kwh_m2_day"]], r1(sum(base["sun_kwh_m2_day"]) / 12))]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    where_ = "at sea level" if height < 15 else f"about {round(height, -1):.0f} m above the sea"
    out = ["## Climate", "", f"Climate data for {t['name']} ({where_}), averages of 2001 to 2025:", "",
           "| | " + " | ".join(months) + " | Year |", "|---|" + "---:|" * 13]
    out += [f"| {name} | " + " | ".join(vals) + f" | {year} |" for name, vals, year in rows] + [""]
    return out


PROPER = tuple(n for c in countries.values() for n in (c["name"], c["name"][:-1])) + ("Urvanian", "Bayvarran", "Lisavan")


def described(p):
    """A party's short description in a list, lower-case at the start unless it begins with a proper name."""
    t = ((p.get("wiki") or {}).get("short") or p.get("what", "")).rstrip(".")
    return t if t.startswith(PROPER) or t[:1].isdigit() else t[:1].lower() + t[1:]


def generated_sections(a):
    d, out_ = a["data"], []
    has = lambda title: any(x["title"] == title for x in a["wiki"].get("sections", []))
    if a["kind"] == "town":
        if a["wiki"].get("climate_from") and CLIMATE:
            out_ += town_climate(d, a["wiki"]["climate_from"])
        if d.get("districts"):
            out_ += ["## Districts", "", "| District | Grew | Character |", "|---|---|---|"]
            out_ += [f"| {x['name']} | {x.get('years', '')} | {x.get('note', '')} |" for x in d["districts"]] + [""]
        here = [p for p in world["parties"] if town_of(p) == d["name"] and p["c"] == d["country"]
                and not p["identity"].get("person")]
        if here:
            out_ += ["## Companies and institutions", ""]
            out_ += [f"- [[{p['identity']['name']}]], " + described(p) for p in sorted(here, key=lambda p: p["identity"]["name"])] + [""]
    if a["kind"] == "party":
        sold = [it for it in world["items"] if it["seller"] == a["key"] and not it.get("resale_of")]
        if sold and not has("Products"):
            out_ += ["## Products", ""] + [f"- [[{it['name']}]]" for it in sold] + [""]
        fleet = d.get("fleet") or []
        if fleet and not has("Fleet"):
            out_ += ["## Fleet", ""] + [f"- {f['name']}" for f in fleet] + [""]
    if a["kind"] == "river":
        if d["tributaries"]:
            out_ += ["## Tributaries", "", "| River | Length | Basin |", "|---|---:|---:|"]
            out_ += [f"| {rlink(q)} | {n0(q['km'])} km | {n0(q['basin_km2'])} km² |" for q in d["tributaries"]] + [""]
        places = river_places(d)
        if places:
            out_ += ["## On the river", "", "From the source down to the mouth: " +
                     ", ".join(f"[[{n}]]" for n in places) + ".", ""]
        towns = [t for t in basin_towns(d) if t not in places]
        if towns:
            out_ += ["## Towns in its basin", "", ", ".join(f"[[{n}]]" for n in towns) + ".", ""]
    if a["kind"] == "waters":
        out_ += ["## Map", "", "![The rivers of the mainland, their basins and the border](water-mainland.png)", "",
                 "![The rivers of Lisavu and their basins](water-lisavu.png)", ""]
        out_ += ["## The rivers", "", "| River | Length | Basin | Flows into | Country |", "|---|---:|---:|---|---|"]
        for land in ("mainland", "lisavu"):
            for r in sorted((r for r in RIVERS.values() if r["land"] == land), key=lambda r: -r["basin_km2"]):
                out_ += [f"| {rlink(r)} | {n0(r['km'])} km | {n0(r['basin_km2'])} km² | "
                         f"{rlink(r['into']) if r['into'] else 'the sea'} | "
                         f"{', '.join(countries[c]['name'] for c in river_countries(r))} |"]
        out_ += [""]
    if a["kind"] == "country":
        towns = sorted((t for t in MAP["towns"] if t["country"] == a["key"]), key=lambda t: -t["population"])
        if towns:
            out_ += ["## Towns", "", "| Town | Population |", "|---|---:|"]
            out_ += [f"| [[{t['name']}]] | {n0(t['population'])} |" for t in towns] + [""]
        hol = d.get("holidays", {}).get("2026", {})
        if hol:
            out_ += ["## Public holidays", "", "| Date (2026) | Holiday |", "|---|---|"]
            out_ += [f"| {longdate(day, weekday=True)} | {name} |" for day, name in sorted(hol.items())] + [""]
    return out_


MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
          "November", "December"]


def longdate(iso, weekday=False):
    """2026-01-01 as '1 January 2026' (or 'Thursday 1 January' with weekday=True, for a year's calendar)."""
    import datetime
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", iso or ""):
        return iso or ""
    d = datetime.date.fromisoformat(iso)
    return f"{d.strftime('%A')} {d.day} {MONTHS[d.month - 1]}" if weekday else f"{d.day} {MONTHS[d.month - 1]} {d.year}"


def timeline(a, where):
    """The article's dated key events (wiki "timeline": [date, text]) as a list; checks order, the founding year
    and the calendar; a company's founding year must be among its dates (earlier rows tell its forerunners)."""
    items = a["wiki"].get("timeline") or []
    if not items:
        return []
    out, prev = [], ""
    for date, text in items:
        if not re.fullmatch(r"\d{4}(-\d{2}-\d{2})?", date):
            problems.append(f"{where}: timeline date {date!r} is not a year or an ISO date")
            continue
        if date < prev:
            problems.append(f"{where}: timeline not in order at {date}")
        if date[:4] > "2026":
            problems.append(f"{where}: timeline date {date} is after the world's calendar")
        prev = date
        shown = date if len(date) == 4 else f"{int(date[8:])} {MONTHS[int(date[5:7]) - 1]} {date[:4]}"
        out.append(f"- **{shown}**: {text}")
    if a["kind"] == "party":
        founded = a["data"]["identity"].get("legal", {}).get("founded", "")[:4]
        if founded and founded not in [d[:4] for d, _ in items]:
            problems.append(f"{where}: the timeline has no entry for the founding year {founded}")
    return out


# References, as a reference work gives them: the world's own sources for an article, by its kind. The sources are
# not online yet: every reference leads to one page that says so (owner, 2026-11-21: the pages look complete, the
# sources come later).
SOURCE_PAGE = "sources.html"
REGISTER = {"XU": "Chamber of Commerce of Ferrano, register of companies", "XB": "Bayvarra Information Service, "
            "federal business register", "XL": "Government Secretariat of Lisavu, island register of companies"}
CONSTITUTION = {"XU": "Constitution of Urvania (1962)", "XB": "Federal Constitution of Bayvarra (1899)",
                "XL": "Constitution of Lisavu (1962)"}


def references(a, title):
    d, k = a["data"], a["kind"]
    cn = lambda code: countries[code]["name"] if code in countries else ""
    if k == "party":
        c = d["c"]
        out = []
        if d["identity"].get("legal", {}).get("form"):
            out.append(f"{REGISTER.get(c, 'Register of companies')}: entry for {title}")
        else:
            out.append(f"Government of {cn(c)}, list of public bodies: {title}")
        if d["identity"].get("website"):
            out.append(f"{title}, website: about us")
        if a["wiki"].get("timeline"):
            out.append(f"{title}, history of the company" if d["identity"].get("legal", {}).get("form") else f"{title}, annual report")
        return out
    if k == "country":
        return [CONSTITUTION.get(a["key"], ""), f"National statistics of {d['name']}: population census of 2025",
                f"Government of {d['name']}: calendar of public holidays, 2026", "Lumeport Trade Accord (1994)"]
    if k == "accord":
        return ["Lumeport Trade Accord, text of 1994", "Protocol on public procurement (1999)",
                "Protocol on the payment link and card schemes (2003)", "Energy protocol (2007)",
                "Protocol on electronic business documents (2014)"]
    if k in ("town", "village", "locality"):
        c = d.get("country", "")
        out = [f"National map survey of {cn(c)}", f"National statistics of {cn(c)}: population census of 2025"]
        if a["wiki"].get("climate_from"):
            out.append(f"Meteorological service of {cn(c)}: climate averages 2001–2025")
        return out
    if k in ("river", "waters", "landmark"):
        return ["National map surveys of Urvania, Bayvarra and Lisavu", "Lumeport Trade Accord, hydrographic survey"]
    if k == "route":
        return ["National map surveys of Urvania and Bayvarra", f"{title}: operator's timetable and route description"]
    if k == "language":
        return [f"{d['name']}: dictionary and grammar", f"Government of {cn(d.get('country', ''))}: law on official languages"
                if d.get("country") in countries else ""]
    if k == "currency":
        return ["Lumeport Trade Accord: rules of the fixed parity", f"{cn(d.get('country', ''))}: central bank, the {d['name'].lower()}"]
    if k == "item":
        return [f"{PARTY[d['seller']]['identity']['name']}: catalogue"]
    return []


CATEGORY = {"country": "Countries", "accord": "Treaties", "town": "Towns", "party": "Companies and institutions",
            "village": "Villages and localities", "locality": "Villages and localities", "route": "Transport", "language": "Languages",
            "currency": "Currencies", "item": "Products", "river": "Rivers", "waters": "Rivers", "landmark": "Landmarks"}


def categories(a):
    d, cats = a["data"], [CATEGORY[a["kind"]]]
    if a["kind"] == "village" and d.get("band") in ("small town", "country town"):
        cats = ["Towns"]
    c = d.get("country") if isinstance(d.get("country"), str) else None
    c = c or d.get("c") or (a["key"] if a["kind"] == "country" else None)
    if c and c in countries and a["kind"] != "country":
        cats.append(f"{countries[c]['name']}")
    if a["kind"] == "river":
        cats += [countries[c]["name"] for c in river_countries(d)]
    if a["kind"] == "landmark":
        land = d.get("country") or {"lisavu": "XL"}.get(d["land"], "")
        if land in countries:
            cats.append(countries[land]["name"])
    return cats


# ---------------------------------------------------------------- write the articles
os.makedirs(out, exist_ok=True)
by_cat = {}
for title, a in sorted(articles.items()):
    w, where = a["wiki"], f"{a['kind']} {title}"
    vals = values(a)
    for k in ("short", "lead"):
        if not w.get(k):
            problems.append(f"{where}: the wiki has no {k}")
    body = [f"# {title}", "", f'<p class="short">{fill(w.get("short", ""), vals, where)}</p>', "",
            (f'<table class="infobox"><caption>{title}</caption>{md_inline(infobox(a), where)}</table>' if infobox(a) else ""), "",
            links(fill(w.get("lead", ""), vals, where), where), ""]
    rest = []
    gen = [links(l, where) for l in generated_sections(a)]
    if a["kind"] == "waters":              # the map comes first, the table of rivers last
        k = gen.index("## The rivers")
        rest, gen = gen[:k], gen[k:]
    secs = list(w.get("sections", []))
    tl = timeline(a, where)
    if tl and not any(x["title"] == "History" for x in secs):
        secs.insert(0, {"title": "History", "text": ""})
    for i, s in enumerate(secs):
        rest += [("### " if s.get("sub") else "## ") + s["title"], ""]
        if s["text"]:
            rest += [links(fill(s["text"], vals, where), where), ""]
        last_of_history = s["title"] == "History" or (s.get("sub") and any(x["title"] == "History" for x in secs[:i]))
        if tl and last_of_history and not (i + 1 < len(secs) and secs[i + 1].get("sub")):
            rest += ["### Timeline", ""] + [links(l, where) for l in tl] + [""]
            tl = None
    rest += gen
    see = []
    if a["kind"] == "party":
        see.append(f"[{title} on the map]({SITE}world.html#{a['key']})")
    if a["kind"] == "river":
        see.append(f"[[{WATERS['title']}]]" if WATERS else "")
    if a["kind"] in ("town", "country", "village", "locality"):
        see.append(f"[The map of the world]({SITE}world.html) · [the printed map sheet]({SITE}map-sheet.html)")
    same = lambda kind: sorted(t for t, x in articles.items() if x["kind"] == kind and t != title)
    if a["kind"] in ("currency", "language", "route", "landmark"):
        see.append(" · ".join(f"[[{t}]]" for t in same(a["kind"])))
    if a["kind"] in ("currency", "accord"):
        acc_ = CJSON.get("trade_accord", {}).get("name")
        see.append(" · ".join(f"[[{t}]]" for t in (same("currency") if a["kind"] == "accord" else [])
                              + ([acc_] if a["kind"] == "currency" and acc_ in page else [])
                              + (["Lumeport Trade Accord Council"] if a["kind"] == "accord" and "Lumeport Trade Accord Council" in page else [])))
    see = [links(x, where) for x in see if x]
    if see:
        rest += ["## See also", ""] + [x for line in see for x in (line, "")]
    refs = references(a, title)
    if refs:
        rest += ["## References", "", '<ol class="refs">'] + \
                [f'<li id="ref-{k + 1}"><a href="{SOURCE_PAGE}">{r}</a></li>' for k, r in enumerate(refs)] + ["</ol>", ""]
        lead_i = body.index(links(fill(w.get("lead", ""), vals, where), where))
        body[lead_i] += "".join(f'<sup class="ref"><a href="#ref-{k + 1}">[{k + 1}]</a></sup>' for k in range(min(2, len(refs))))
    heads = [l[3:] for l in rest if l.startswith("## ")]
    if len(heads) >= 3:                       # the contents, after the lead, as an encyclopedia has it
        body += ['<details class="wtoc" open><summary>Contents</summary><ol>'
                 + "".join(f'<li><a href="#{re.sub(r"[^a-z0-9 -]", "", h.lower()).replace(" ", "-")}">{h}</a></li>' for h in heads)
                 + "</ol></details>", ""]
    body += rest
    cats = categories(a)
    for c in cats:
        by_cat.setdefault(c, []).append(title)
    body += ['<p class="categories">Categories: ' + " · ".join(f'<a href="category-{slug(c)}.html">{c}</a>' for c in cats) + "</p>", ""]
    open(os.path.join(out, slug(title) + ".md"), "w", encoding="utf-8").write("\n".join(body))

# the water maps (tools/wiki_water.py): the whole map for the article on the rivers, a small one per river
if RIVERS:
    import wiki_water  # noqa: E402
    imgdir = os.path.join(os.path.dirname(os.path.abspath(out)), "wiki")
    os.makedirs(imgdir, exist_ok=True)
    for land in ("mainland", "lisavu"):
        found = TERR["rivers"][land]
        names = {r["id"]: RIVERS[(land, r["id"])]["rec"]["name"] for r in found if (land, r["id"]) in RIVERS}
        wiki_water.water_map(land, found, names, os.path.join(imgdir, f"water-{land}.png"))
        for r in found:
            wiki_water.locator(land, found, r["id"], os.path.join(imgdir, f"river-{land}-{r['id']}.png"))

for c, titles in by_cat.items():
    body = [f"# Category: {c}", "", f"Articles in the category {c}:", ""] + [f"- [{t}]({page[t]})" for t in sorted(titles)] + [""]
    open(os.path.join(out, f"category-{slug(c)}.md"), "w", encoding="utf-8").write("\n".join(body))

open(os.path.join(out, "sources.md"), "w", encoding="utf-8").write(
    "# Sources\n\n<p class=\"short\">The sources the Encyclopedia cites</p>\n\n"
    "The registers, laws, surveys, statistics and company documents the articles cite are not yet in the "
    "Encyclopedia's online library. They will be added here.\n\n[Back to the main page](index.html)\n")
index = ["# The UBL World", "", '<p class="short">The reference work of Urvania, Bayvarra and Lisavu.</p>', "",
         "The countries of the Lumeport Trade Accord: their history and geography, their towns, villages, rivers and "
         "landmarks, and their companies and institutions.", ""]
for c in ("Countries", "Treaties", "Towns", "Villages and localities", "Rivers", "Landmarks", "Companies and institutions", "Transport",
          "Languages", "Currencies", "Products"):
    if c in by_cat:
        index += [f"## {c}", ""] + [f"- [{t}]({page[t]})" for t in sorted(by_cat[c])] + [""]
open(os.path.join(out, "index.md"), "w", encoding="utf-8").write("\n".join(index))

# no names of persons in the encyclopedia (owner): the people the world's data names (consumers, staff, drivers,
# ship masters, designers) are looked for in every article
PERSONS = set()


def _people(x):
    if isinstance(x, dict):
        for k, v in x.items():
            if k in ("person_name", "driver", "master", "employee") and isinstance(v, dict):
                full = " ".join(v.get(f, "") for f in ("first", "family")).strip()
                if full:
                    PERSONS.add(full)
            _people(v)
    elif isinstance(x, list):
        for v in x:
            _people(v)


_people(world["parties"])
PERSONS |= {p["identity"]["name"] for p in world["parties"] if p["identity"].get("person")}
for f in os.listdir(out):
    text = open(os.path.join(out, f), encoding="utf-8").read()
    for who in PERSONS:
        if re.search(rf"\b{re.escape(who)}\b", text):
            problems.append(f"{f}: names a person, {who}")

if problems:
    sys.exit("encyclopedia problems:\n  " + "\n  ".join(problems))
print(f"encyclopedia: {len(articles)} articles, {len(by_cat)} categories")
