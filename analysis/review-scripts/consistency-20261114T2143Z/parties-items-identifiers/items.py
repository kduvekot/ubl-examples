import csv,collections
rows=list(csv.DictReader(open('items.csv')))
by=collections.defaultdict(list)
for r in rows: by[r['main_id']].append(r)
skip={'flow','file','xpath','element','parent','role_path','line_xpath','party_role','party_name','line_id','entity','entity_xpath','main_id'}
cols=[c for c in rows[0] if c not in skip]
for k,rs in sorted(by.items(),key=lambda x:-len(x[1])):
    print(f"#### {k} ({len(rs)} items, flows {','.join(sorted(set(r['flow'] for r in rs)))})")
    for c in cols:
        cnt=collections.Counter(r[c] for r in rs if r[c])
        if not cnt: continue
        e=sum(1 for r in rs if not r[c])
        if len(cnt)==1: print(f"  {c} = {list(cnt)[0][:300]}  [{e} empty]")
        else:
            print(f"  {c} VARIES ({e} empty):")
            for v,n in cnt.most_common():
                ex=sorted(set(r['flow']+'/'+r['file'][:2] for r in rs if r[c]==v))
                print(f"     {n:3d} {v[:250]!r} in {', '.join(ex[:12])}")
