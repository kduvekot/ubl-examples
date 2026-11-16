import csv,collections,re
rows=list(csv.DictReader(open('identifiers.csv')))
def pat(v): return re.sub(r'[A-Za-z]','A',re.sub(r'\d','9',v))
by=collections.defaultdict(list)
for r in rows:
    if r['scheme_id']: by[r['scheme_id']].append(r)
print("| schemeID | Identifies (element: uses) | Value format | Values | Uses | Files | Flows | Example |")
print("|---|---|---|---:|---:|---:|---|---|")
for s,rs in sorted(by.items(),key=lambda x:-len(x[1])):
    el=collections.Counter(r['parent']+'/'+r['element'] for r in rs)
    pats=collections.Counter(pat(r['value']) for r in rs)
    vals=sorted(set(r['value'] for r in rs))
    fl=sorted(set(r['flow'] for r in rs))
    els='; '.join(f'{k}: {v}' for k,v in el.most_common(4))+(' …' if len(el)>4 else '')
    ps=', '.join(f'`{k}`' for k,v in pats.most_common(3))
    flows='all 18' if len(fl)==18 else ','.join(fl)
    print(f"| `{s}` | {els} | {ps} | {len(vals)} | {len(rs)} | {len(set((r['flow'],r['file']) for r in rs))} | {flows} | `{vals[0]}` |")
