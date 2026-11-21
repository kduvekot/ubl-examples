#!/usr/bin/env python3
"""The published site states the world as fact (the rule "two layers: the workshop and the world",
analysis/codelist-decisions.md): no internal references in what a reader sees. Scans the text of the built HTML pages
(not code, not the method note, which describes the project) and fails on

  * decision, open-point and cause numbers: D12, O226, MO004, OW001, ID-Q7, "worklist C23", "(C72)";
  * review finding IDs: tender/09#F4;
  * repository paths: world/items.json, tools/build_examples.py;
  * names of real specifications the world does not follow: EN 16931, Peppol, XRechnung;
  * the project's own notes: code-list decisions (P-SB), any mention of "the (UBL|OASIS) TC";
  * finding IDs in any form: "(timelines#F6)", "#F12" with any prefix, a bare "(F7)", "UBL rule IND6", "(IND5)";
  * reasons from the UBL examples or principles, which mean nothing in the world (owner, Q3): "Manifest Values",
    "UBL 2.5, 2.2.2", "OASIS example"; and the Trade Accord, a proper name, in lower case ("trade accord");
  * European standards and law the world does not follow (owner, O265: what is globally accepted as the norm stays,
    such as ISO, GS1, the GHG Protocol, SOLAS, Basel, Montreal, CMNI, CIM/COTIF, IAEA, IPPC/ISPM, UNECE FFV, WTO
    and PCI DSS): "EN nnnn" standard numbers except EN_ALLOWED, RecyClass, the European List of Waste, VATEX,
    "EU" and "European Union"; these may stand on the pages of the one party abroad in the EU (EU_PARTY) and of
    the documents it issues or receives, which follow or quote its own country's rules;

  * "dispatch" where a UBL concept is meant (UBL's own spelling is "despatch"; owner, 2026-11-21): "dispatch
    advice", "dispatch date", "dispatch note", "dispatched to", "date of dispatch" and the like;

and warns on words that tell the project's history ("no longer", "was moved", "proposed addition").

It also reads the names and descriptions of the world's own code lists (the Trade Accord's and the national lists in
world/codelists/lists.json, published as genericode files) with the same rules and one more, for the EU's law: "EU",
"European Union", "Directive" (owner, O256 a). Copies of established international lists (UN/EDIFACT, ISO, the WCO's
HS, UN CPC, UNECE recommendations …) keep their codes and texts as published and are not read.

Usage: python3 tools/check_published.py <site-dir>
"""
import json
import os
import re
import sys
from html.parser import HTMLParser

FAIL = re.compile(r"(?<![\w`/=-])(?:D\d{1,2}(?: point \d+)?|O\d{1,3}|MO\d{3}|OW\d{3}|ID-Q\d+)\b(?![\w-])"
                  r"|\bworklist C\d+|\(C\d{2,3}\)|\b[a-z]+/\d{2}#F\d+"
                  r"|\b(?:world|tools|analysis)/[\w/-]+\.(?:json|py|md)\b|\bEN 16931\b|\bPeppol\b|\bXRechnung\b"
                  r"|\bdecision P-[A-Z0-9]+\b|\bP-SB\b|\bthe (?:OASIS )?(?:UBL )?TC\b"
                  r"|#F\d+\b|\(F\d{1,3}\)|\bIND\d+\b"
                  r"|\bManifest Values\b|\bOASIS example\b|\bUBL 2\.5, 2\.2\.2\b")   # the UBL examples have no
#                                                            meaning in the world (owner, 2026-11-21, Q3)
# the Trade Accord is a proper name (Q3); "one trade accord", "a trade accord" are the common noun
PROPER_NAMES = re.compile(r"(?<!\bone )(?<!\ba )(?<!\ban )\b(?:[Tt]rade accord|trade Accord)\b")
EN_STANDARD = re.compile(r"\bEN \d{3,5}(?:-\d+)*\b")
EN_ALLOWED = {"EN 15804"}                            # environmental product declarations: kept (owner, O265)
EUROPEAN = re.compile(r"\bRecyClass\b|\bEuropean List of Waste\b|\bVATEX\b|\bEU\b|\bEuropean Union\b")
EU_PARTY = "51-nl"                                   # Haarvliet Isotopes, in the Netherlands
EU_LAW = re.compile(r"\bEU\b|\bEuropean Union\b|\bDirective\b")
OWN_LISTS = ("regional", "XU", "XB", "XL")          # the scopes of the world's own lists in world/codelists/lists.json
WARN = re.compile(r"\b(?:no longer|was moved|proposed addition)\b"
                  r"|\bthe build checks\b|\boutside the examples\b|\boutside the world\b|\bis fictional\b"
                  r"|\bare invented\b|\buser-assigned\b", re.I)   # project voice (second site review, SR2-02):
                                                            # warnings until the generators' texts are rewritten
# UBL's spelling for UBL concepts (owner, 2026-11-21, O277 (3)): "despatch" as in DespatchAdvice, ActualDespatchDate,
# DespatchLine, DespatchContact, DespatchParty; the railway's "dispatches every train" is another word and stays
UNFILLED = re.compile(r"\{fact:[^}]*\}")    # a world fact the builders did not fill in (tools/world_facts.py)
SPELLING = re.compile(r"\bdispatch(?:ed|ing)?[ -](?:advice|advices|date|time|line|lines|note|notes|to|from|office|"
                      r"coordinator|area|party|contact|address|location|quantity|period)\b|\bdispatch@"
                      r"|\b(?:date|time|place|country|day|point) of dispatch\b", re.I)
SKIP_DIRS = {"note", "codelists", "examples"}
SKIP_PAGES = {"releases.html", "history.html"}      # the OASIS samples' history: about the project, not the world


class Text(HTMLParser):
    """The visible text of a page, without code, preformatted text, scripts and styles."""
    def __init__(self):
        super().__init__()
        self.depth, self.parts, self.title, self.in_h1 = 0, [], "", False

    def handle_starttag(self, tag, attrs):
        if tag in ("code", "pre", "script", "style"):
            self.depth += 1
        if tag == "h1" and not self.title:
            self.in_h1 = True

    def handle_endtag(self, tag):
        if tag in ("code", "pre", "script", "style") and self.depth:
            self.depth -= 1
        if tag == "h1":
            self.in_h1 = False

    def handle_data(self, data):
        if not self.depth:
            self.parts.append(data)
            if self.in_h1:
                self.title += data


def european(text, exempt):
    """The hits of the European standards and law in a text; the EU party's own pages may name its law."""
    hits = [m for m in EN_STANDARD.finditer(text) if m.group(0) not in EN_ALLOWED]
    return hits + ([] if exempt else list(EUROPEAN.finditer(text)))


def main(site):
    fails, warns = [], []
    root = os.path.join(os.path.dirname(__file__), "..", "world")
    parties = json.load(open(os.path.join(root, "parties.json"), encoding="utf-8"))
    eu = next(p for p in parties["parties"] + parties.get("abroad", []) if p["id"] == EU_PARTY)
    name = re.escape(eu['identity']['name'])
    eu_issues = re.compile(rf"^\s*\w[\w ]*: (?:{name} to |.* to {name}\b)")   # a page of a document from or to it
    for dirpath, dirs, files in os.walk(site):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for f in sorted(files):
            if not f.endswith(".html") or f in SKIP_PAGES:
                continue
            p = Text()
            p.feed(open(os.path.join(dirpath, f), encoding="utf-8").read())
            text = " ".join(p.parts)
            exempt = f == f"world-{EU_PARTY}.html" or bool(eu_issues.match(" ".join(p.title.split())))
            for m in list(FAIL.finditer(text)) + list(PROPER_NAMES.finditer(text)) + european(text, exempt) + list(SPELLING.finditer(text)) + list(UNFILLED.finditer(text)):
                fails.append(f"{f}: …{text[max(0, m.start() - 50):m.end() + 10].strip()}…")
            for m in WARN.finditer(text):
                warns.append(f"{f}: …{text[max(0, m.start() - 50):m.end() + 10].strip()}…")
    lists = json.load(open(os.path.join(os.path.dirname(__file__), "..", "world", "codelists", "lists.json"),
                           encoding="utf-8"))["lists"]
    for key, cl in lists.items():
        if cl.get("scope") not in OWN_LISTS:
            continue
        texts = [("name", cl.get("name", "")), ("description", cl.get("description", ""))]
        for code, v in (cl.get("codes") or {}).items():
            texts += [(f"code {code}", t) for t in (v if isinstance(v, list) else [v]) if isinstance(t, str)]
        for what, t in texts:
            for rule in (FAIL, EU_LAW, EUROPEAN, EN_STANDARD, PROPER_NAMES, SPELLING):
                for m in rule.finditer(t):
                    if rule is EN_STANDARD and m.group(0) in EN_ALLOWED:
                        continue
                    if rule is FAIL and "Basel" in t[max(0, m.start() - 60):m.end()]:
                        continue                      # the Basel Convention's own operation codes D1 to D15
                    fails.append(f"code list {key}, {what}: …{t[max(0, m.start() - 50):m.end() + 10].strip()}…")
    for w in warns[:5]:
        print("warning:", w)
    if warns:
        print(f"published text: {len(warns)} words that may tell the project's history (warnings)")
    if fails:
        print("\n".join(fails[:60]))
        sys.exit(f"published text: {len(fails)} internal references or names of real specifications")
    print("published text: no internal references")


if __name__ == "__main__":
    main(sys.argv[1])
