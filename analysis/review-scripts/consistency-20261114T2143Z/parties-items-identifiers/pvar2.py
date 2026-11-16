import csv,collections,sys
rows=list(csv.DictReader(open('parties.csv')))
skip={'flow','file','xpath','element','parent','role_path','role','role_extras','other','party_role','party_name','line_id','entity','entity_xpath','name','contacts','authorizations'}
cols=[c for c in rows[0].keys() if c not in skip]
by=collections.defaultdict(list)
for r in rows: by[r['name']].append(r)
for n,rs in sorted(by.items(),key=lambda x:-len(x[1])):
    print(f"#### {n}  ({len(rs)} rows, {len(set(r['file'] for r in rs))} files)")
    for c in cols:
        cnt=collections.Counter(r[c] for r in rs if r[c])
        if not cnt: continue
        empt=sum(1 for r in rs if not r[c])
        if len(cnt)==1:
            v=list(cnt)[0]; print(f"  {c} = {v[:160]}  [{cnt[v]} set, {empt} empty]")
        else:
            print(f"  {c} CONFLICT ({empt} empty):")
            for v,k in cnt.most_common():
                exs=sorted(set(r['flow']+'/'+r['file'][:2] for r in rs if r[c]==v))
                print(f"     {k:4d} {v[:160]!r}  in {', '.join(exs[:10])}{' ...%d'%len(exs) if len(exs)>10 else ''}")
