import csv,collections,sys
rows=list(csv.DictReader(open('parties.csv')))
skip={'flow','file','xpath','element','parent','role_path','role','role_extras','other','party_role','party_name','line_id','entity','entity_xpath','name','contacts'}
cols=[c for c in rows[0].keys() if c not in skip]
by=collections.defaultdict(list)
for r in rows: by[r['name']].append(r)
for n,rs in sorted(by.items(),key=lambda x:-len(x[1])):
    print(f"#### {n}  ({len(rs)} rows, {len(set(r['file'] for r in rs))} files, flows {','.join(sorted(set(r['flow'] for r in rs)))})")
    roles=collections.Counter(r['role'] for r in rs)
    print("  roles:",dict(roles))
    for c in cols:
        cnt=collections.Counter(r[c] for r in rs)
        if len(cnt)==1:
            v=list(cnt)[0]
            if v: print(f"  {c} = {v[:200]}")
        else:
            print(f"  {c} VARIES:")
            for v,k in cnt.most_common():
                ex=[r['flow']+'/'+r['file'].split('-')[0] for r in rs if r[c]==v]
                exs=sorted(set(ex))
                print(f"     {k:4d} {v[:180]!r}  e.g. {', '.join(exs[:8])}{' ...' if len(exs)>8 else ''}")
