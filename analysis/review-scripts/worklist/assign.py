"""Assign every finding of findings.csv to a cause: ordered rules (first match wins), then a manual table.

usage: python3 -I assign.py <findings.csv> <out.csv>   (prints counts and the unassigned findings)
"""
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from rules import RULES, MANUAL  # noqa: E402


def match(rule, r):
    cid, cond = rule
    for field, pat in cond.items():
        if field == 'flow':
            if r['flow'] not in pat:
                return False
            continue
        if field == 'not_title':
            if re.search(pat, r['title'], re.I):
                return False
            continue
        if field == 'any':  # title, elements or values
            hay = ' '.join((r['title'], r['elements'], r['values']))
            if not re.search(pat, hay, re.I):
                return False
            continue
        if field == 'docs':
            if r['example'][:2] not in pat:
                return False
            continue
        if field == 'ids':
            if r['finding'] not in pat:
                return False
            continue
        if not re.search(pat, r[field], re.I):
            return False
    return True


def main():
    rows = list(csv.DictReader(open(sys.argv[1], encoding='utf-8')))
    out = []
    unassigned = []
    for r in rows:
        cid = MANUAL.get(r['finding'])
        if not cid:
            for rule in RULES:
                if match(rule, r):
                    cid = rule[0]
                    break
        if not cid:
            unassigned.append(r)
            cid = ''
        out.append(dict(r, cause=cid))
    with open(sys.argv[2], 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()), lineterminator='\n')
        w.writeheader()
        w.writerows(out)
    c = Counter(r['cause'] for r in out if r['cause'])
    for k, n in sorted(c.items()):
        print(f'{k:6} {n}')
    print('assigned', sum(c.values()), 'unassigned', len(unassigned))
    per = Counter(r['flow'] for r in unassigned)
    print(dict(per))
    if len(sys.argv) > 3:
        flows = sys.argv[3].split(',')
        for r in unassigned:
            if r['flow'] in flows or flows == ['all']:
                print(f"{r['finding']:18} {r['severity'][0]} {r['needs_decision'][0]} {r['title'][:125]} | {r['elements'][:70]}")


if __name__ == '__main__':
    main()
