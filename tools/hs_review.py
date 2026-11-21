#!/usr/bin/env python3
"""The HS reasoning of the world's maker items, for the owner to verify in one sitting (stage 7 B5, O31, Q14).

An internal table, never published: per maker item with an HS code (world/items.json), the code, the heading and
subheading as the WCO's legal text gives them, the UN Comtrade short text (world/codelists/sources/hs2022/H6.json),
the General Interpretative Rules applied, the section and chapter notes relied on, the reasoning, and whether the
owner has verified it. The notes are in world/codelists/sources/hs2022-notes/ (WCO, HS 2022 edition; provenance in
world/codelists/sources/PROVENANCE-second-round.md).

Stamping records the verification in world/items.json: hs_verified {"by": "owner", "date", "hs", "hash"}, the hash
being the SHA-256 of the canonical JSON of hs_reason (tools/world_items.py, hs_reason_hash). From then on the build
stops if the item's code or its reasoning changes, until it is verified again.

Usage:
  python3 tools/hs_review.py                      the table on stdout (Markdown)
  python3 tools/hs_review.py -o FILE              the table into FILE (outside the site, e.g. .review/hs-review.md)
  python3 tools/hs_review.py --stamp ID [ID ...]  record the owner's verification of these items (today's date)
  python3 tools/hs_review.py --stamp --all        … of every unverified item
  python3 tools/hs_review.py --unstamp ID [...]   set hs_verified back to null
  --date YYYY-MM-DD                               the date of the stamp (default: today)
"""
import argparse
import datetime
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import world_data  # noqa: E402
import world_items  # noqa: E402

ITEMS = os.path.join(world_data.ROOT, "world", "items.json")


def cell(s):
    return str(s).replace("|", "\\|").replace("\n", " ")


def table(items):
    h6 = world_items.h6()
    out = ["# HS reasoning of the maker items (internal, for the owner's verification)", "",
           f"{len(items)} maker items with an HS code; "
           f"{sum(1 for i in items if i.get('hs_verified'))} verified. Sources: the WCO's HS 2022 legal texts in "
           "`world/codelists/sources/hs2022-notes/`. Stamp with `python3 tools/hs_review.py --stamp <item-id> ...`.",
           "", "| Item | Code | Heading (WCO) | Subheading (WCO); Comtrade text | GIR | Notes | Reasoning | Verified |",
           "|---|---|---|---|---|---|---|---|"]
    for it in items:
        r, v, hs = it.get("hs_reason") or {}, it.get("hs_verified"), it["hs"]
        if v:
            ok = world_items.hs_reason_hash(r) == v.get("hash") and v.get("hs") == hs
            ver = f"{v['by']}, {v['date']}" + ("" if ok else " (changed since: re-verify)")
        else:
            ver = "no"
        out.append("| " + " | ".join(cell(x) for x in (
            f"`{it['id']}` {it['name']}", f"{hs[:4]}.{hs[4:]}", r.get("heading", "(missing)"),
            f"{r.get('subheading', '(missing)')}; Comtrade: {h6.get(hs, '(not in H6.json)')}",
            r.get("gir", ""), "; ".join(r.get("notes", [])), r.get("text", "(missing)"), ver)) + " |")
    return "\n".join(out) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("-o", "--output", help="write the table to this file (not inside the published site)")
    ap.add_argument("--stamp", nargs="*", metavar="ID", help="record the owner's verification of these items")
    ap.add_argument("--all", action="store_true", help="with --stamp: every unverified item")
    ap.add_argument("--unstamp", nargs="+", metavar="ID", help="set hs_verified back to null")
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    a = ap.parse_args()
    text = open(ITEMS, encoding="utf-8").read()
    data = json.loads(text)
    items = world_items.hs_items(data)
    by_id = {i["id"]: i for i in items}
    if a.stamp is not None or a.unstamp:
        ids = list(a.unstamp or a.stamp or [])
        if a.stamp is not None and a.all:
            ids += [i["id"] for i in items if not i.get("hs_verified") and i["id"] not in ids]
        if not ids:
            sys.exit("hs_review: name the items to stamp, or --all")
        unknown = [x for x in ids if x not in by_id]
        if unknown:
            sys.exit(f"hs_review: not a maker item with an HS code: {', '.join(unknown)}")
        for x in ids:
            it = by_id[x]
            if a.unstamp:
                it["hs_verified"] = None
                continue
            if not isinstance(it.get("hs_reason"), dict):
                sys.exit(f"hs_review: {x} has no hs_reason to verify")
            it["hs_verified"] = {"by": "owner", "date": a.date, "hs": it["hs"],
                                 "hash": world_items.hs_reason_hash(it["hs_reason"])}
        open(ITEMS, "w", encoding="utf-8").write(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
        print(f"hs_review: {'unstamped' if a.unstamp else 'stamped'} {len(ids)} item(s): {', '.join(ids)}")
        return
    out = table(items)
    if a.output:
        site = os.path.join(world_data.ROOT, "_site")
        if os.path.abspath(a.output).startswith(os.path.abspath(site) + os.sep):
            sys.exit("hs_review: the table is internal; write it outside the published site")
        os.makedirs(os.path.dirname(os.path.abspath(a.output)), exist_ok=True)
        open(a.output, "w", encoding="utf-8").write(out)
        print(f"hs_review: {len(items)} items written to {a.output}")
    else:
        sys.stdout.write(out)


if __name__ == "__main__":
    main()
