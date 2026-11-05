#!/usr/bin/env python3
"""Element coverage of the UBL sample documents.

Compares every element of the UBL model (each BBIE and ASBIE, i.e. each
child element in the context of its parent) with the elements used in the
sample documents in xml/, and suggests where each missing element fits.

Input
  --model    UBL-Entities-<version>.gc from the release (mod/ folder)
  --examples folder with the sample documents (default: xml)

Placement rules for an element that no example uses (parent P, child C):
  * Each aggregate P has "home" documents: the document types from which P
    can be reached in the fewest steps. Document-level elements have exactly
    one home: their own document type.
  * If an example of a home document (or one step further) already contains
    P, add C there                                       -> "extend"
  * Else, if an example of a home document exists, add P with C to it
                                                          -> "add structure"
  * Else, if an example of any document already contains P, add C there
                                                          -> "extend (other)"
  * Else a new example of the closest home document is needed -> "new example"
  * Aggregates that no document type can reach are listed  -> "not reachable"

Usage
  python3 tools/coverage.py --model UBL-Entities-2.5.gc [--examples xml] > report.md
"""
import argparse
import collections
import glob
import os
import xml.etree.ElementTree as ET

CAC = "urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2"
CBC = "urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2"


def load_model(path):
    rows = []
    for el in ET.parse(path).getroot().iter():
        if el.tag.rsplit("}", 1)[-1] == "Row":
            rows.append({v.get("ColumnRef"): (v.findtext("{*}SimpleValue") or v.findtext("SimpleValue") or "")
                         for v in el})
    abie_by_den, abies, docs = {}, {}, set()
    current = None
    for r in rows:
        if r["ComponentType"] == "ABIE":
            current = r["ComponentName"]
            abies[current] = {"row": r, "props": []}
            abie_by_den[r["DictionaryEntryName"].rsplit(". Details", 1)[0]] = current
            if not r["ModelName"].startswith("UBL-CommonLibrary"):
                docs.add(current)
        else:
            abies[current]["props"].append(r)
    for a in abies.values():
        for p in a["props"]:
            if p["ComponentType"] == "ASBIE":
                q, o = p.get("AssociatedObjectClassQualifier", ""), p["AssociatedObjectClass"]
                p["target"] = abie_by_den[f"{q}_ {o}" if q else o]
    return abies, docs


def depths(abies, docs):
    """depth[doc][abie] = fewest ASBIE steps from the document to the aggregate."""
    out = {}
    for d in docs:
        dist, todo = {d: 0}, collections.deque([d])
        while todo:
            a = todo.popleft()
            for p in abies[a]["props"]:
                t = p.get("target")
                if t and t not in dist:
                    dist[t] = dist[a] + 1
                    todo.append(t)
        out[d] = dist
    return out


def path_to(abies, doc, target, present=frozenset()):
    """Shortest path doc -> target; steps the example already has cost nothing."""
    cost, prev, todo = {doc: (0, 0)}, {doc: None}, collections.deque([doc])
    while todo:
        a = todo.popleft()
        for p in abies[a]["props"]:
            t = p.get("target")
            if not t:
                continue
            free = (a, p["ComponentName"]) in present
            c = (cost[a][0] + (0 if free else 1), cost[a][1] + 1)
            if t not in cost or c < cost[t]:
                cost[t], prev[t] = c, (a, p["ComponentName"])
                (todo.appendleft if free else todo.append)(t)
    if target not in cost:
        return None, 99
    steps, a = [], target
    while prev.get(a):
        a, name = prev[a]
        steps.append(name)
    return "/".join([doc] + steps[::-1]), cost[target][0]


def scan_examples(folder, abies, docs):
    elem_type = {}  # cac element name -> aggregate
    for a in abies.values():
        for p in a["props"]:
            if p.get("target"):
                elem_type[p["ComponentName"]] = p["target"]
    used = collections.defaultdict(set)       # (parent, child) -> examples
    instances = collections.defaultdict(set)  # aggregate -> examples
    ex_doc, skipped = {}, []
    for f in sorted(glob.glob(os.path.join(folder, "*.xml"))):
        name = os.path.basename(f)
        root = ET.parse(f).getroot()
        doc = root.tag.rsplit("}", 1)[-1]
        if doc not in docs:
            skipped.append((name, doc))
            continue
        ex_doc[name] = doc

        def walk(el, agg):
            instances[agg].add(name)
            for c in el:
                ns, _, local = c.tag[1:].partition("}")
                if ns == CBC:
                    used[(agg, local)].add(name)
                elif ns == CAC:
                    used[(agg, local)].add(name)
                    walk(c, elem_type[local])
        walk(root, doc)
    return used, instances, ex_doc, skipped


def newest_first(ex):
    """Sort key: examples of a newer UBL version first (UBL-X-2.4-... before UBL-X-2.0-...)."""
    import re
    m = re.search(r"-2\.(\d)-", ex)
    return (-(int(m.group(1)) if m else 0), ex)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", required=True)
    ap.add_argument("--examples", default="xml")
    args = ap.parse_args()

    abies, docs = load_model(args.model)
    dep = depths(abies, docs)
    used, instances, ex_doc, skipped = scan_examples(args.examples, abies, docs)
    docs_with_ex = collections.defaultdict(list)
    for ex, d in ex_doc.items():
        docs_with_ex[d].append(ex)

    props = [(a, p) for a in abies for p in abies[a]["props"]]
    per_ex = collections.defaultdict(set)  # example -> (parent, child) pairs it uses
    for k, exs in used.items():
        for ex in exs:
            per_ex[ex].add(k)

    def richness(ex, agg):
        """How many of agg's elements the example already uses."""
        return sum(1 for k in per_ex[ex] if k[0] == agg)
    missing = [(a, p) for a, p in props if (a, p["ComponentName"]) not in used]

    def homes(agg):
        reach = {d: dep[d][agg] for d in docs if agg in dep[d]}
        best = min(reach.values())
        return reach, best

    plan = []  # (category, target, parent, prop)
    for a, p in missing:
        if a in docs:
            reach, best = {a: 0}, 0
        elif not any(a in dep[d] for d in docs):
            plan.append(("not reachable", "no document type uses " + a, a, p))
            continue
        else:
            reach, best = homes(a)
        near = sorted((d for d, n in reach.items() if n <= best + 1), key=lambda d: (reach[d], d))
        inst_near = sorted({ex for ex in instances.get(a, ()) if ex_doc[ex] in near},
                           key=lambda ex: (reach[ex_doc[ex]], -richness(ex, a), newest_first(ex)))
        ex_near = [d for d in near if d in docs_with_ex]
        if inst_near:
            plan.append(("extend", inst_near[0], a, p))
        elif ex_near:
            # Example needing the fewest new elements on the way to the aggregate;
            # then the closest document type, the richest example, the newest version.
            opts = []
            for d in ex_near:
                for ex in docs_with_ex[d]:
                    path, new_steps = path_to(abies, d, a, per_ex[ex])
                    opts.append(((new_steps, reach[d], -len(per_ex[ex]), newest_first(ex)), ex, path))
            _, ex, path = min(opts)
            plan.append(("add structure", ex + " — " + path, a, p))
        elif instances.get(a):
            ex = sorted(instances[a], key=lambda e: (reach.get(ex_doc[e], 99), -richness(e, a), newest_first(e)))[0]
            plan.append(("extend (other)", ex, a, p))
        else:
            plan.append(("new example", near[0], a, p))

    w = print
    n_props, n_used = len(props), len(props) - len(missing)
    lib = [x for x in props if x[0] not in docs]
    w("# UBL 2.5 element coverage of the sample documents\n")
    w(f"Model: `{os.path.basename(args.model)}` · examples: `{args.examples}/` "
      f"({len(ex_doc)} UBL documents, {len(skipped)} other files)\n")
    w("## Summary\n")
    w("| | Elements | Used in an example | Missing | Coverage |\n|---|---:|---:|---:|---:|")
    for label, sel in (("Document level", [x for x in props if x[0] in docs]), ("Library (cac/cbc in context)", lib),
                       ("All", props)):
        u = sum(1 for a, p in sel if (a, p["ComponentName"]) in used)
        w(f"| {label} | {len(sel)} | {u} | {len(sel) - u} | {100 * u / len(sel):.0f}% |")
    aggs_used = sum(1 for a in abies if a not in docs and instances.get(a))
    w(f"\nAggregates (cac types) instantiated at least once: {aggs_used} of {len(abies) - len(docs)}.")
    w(f"Document types with at least one example: {len(docs_with_ex)} of {len(docs)}.\n")
    cats = collections.Counter(c for c, *_ in plan)
    w("Where the missing elements fit:\n")
    w("| Placement | Elements |\n|---|---:|")
    for c in ("extend", "add structure", "extend (other)", "new example", "not reachable"):
        w(f"| {c} | {cats[c]} |")
    w("")

    w("## Missing elements by the UBL version that introduced them\n")
    ver = collections.Counter(p.get("CurrentVersion", "?") for a, p in props)
    vmiss = collections.Counter(p.get("CurrentVersion", "?") for a, p in missing)
    w("| Version | Elements | Missing |\n|---|---:|---:|")
    for v in sorted(ver):
        w(f"| {v} | {ver[v]} | {vmiss[v]} |")
    w("")

    w("## Coverage per document type (document-level elements)\n")
    w("| Document type | Examples | Elements | Used | Coverage |\n|---|---:|---:|---:|---:|")
    rows = []
    for d in docs:
        tot = len(abies[d]["props"])
        u = sum(1 for p in abies[d]["props"] if (d, p["ComponentName"]) in used)
        rows.append((len(docs_with_ex.get(d, [])) == 0, -u / tot, d, len(docs_with_ex.get(d, [])), tot, u))
    for _, _, d, n, tot, u in sorted(rows):
        w(f"| {d} | {n} | {tot} | {u} | {100 * u / tot:.0f}% |")
    w("")

    w("## Document types without an example\n")
    newdoc = collections.Counter(t for c, t, *_ in plan if c == "new example")
    w("| Document type | Missing elements that only fit here |\n|---|---:|")
    for d in sorted(docs - set(docs_with_ex), key=lambda d: (-newdoc[d], d)):
        w(f"| {d} | {newdoc[d]} |")
    w("")

    w("## Missing elements per placement\n")
    by = collections.defaultdict(list)
    for c, t, a, p in plan:
        by[(c, t)].append((a, p))
    for c in ("extend", "add structure", "extend (other)", "new example", "not reachable"):
        keys = sorted((k for k in by if k[0] == c), key=lambda k: (-len(by[k]), k[1]))
        if not keys:
            continue
        w(f"### {c} ({cats[c]})\n")
        for k in keys:
            w(f"<details><summary><b>{k[1]}</b> — {len(by[k])} elements</summary>\n")
            w("| Parent | Element | Card. | Definition |\n|---|---|---|---|")
            for a, p in sorted(by[k], key=lambda x: (x[0], x[1]["ComponentName"])):
                d = p.get("Definition", "").replace("|", "/").replace("\n", " ")
                w(f"| {a} | {p['ComponentName']} | {p.get('Cardinality', '')} | {d} |")
            w("\n</details>\n")
    if skipped:
        w("## Files not counted\n")
        for n, r in skipped:
            w(f"- `{n}` (root element `{r}`)")


if __name__ == "__main__":
    main()
