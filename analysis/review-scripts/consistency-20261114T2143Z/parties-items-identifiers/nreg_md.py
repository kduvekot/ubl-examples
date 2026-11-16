import csv,collections,re
D=list(csv.DictReader(open('documents.csv')))
# real issuer = by prefix
pre=collections.defaultdict(list)
for d in D:
    m=re.match(r'([A-Z]+)-([A-Z]+)-(\d\d)-(\d{4})$',d['id'])
    if m: pre[m.group(1)].append((m.group(2),int(m.group(4)),d['flow'],d['issuer'],d['root']))
    else: pre['(other)'].append((d['id'],0,d['flow'],d['issuer'],d['root']))
print("| Prefix | Issuers (mechanical issuer column) | Type infixes | Numbers | Flows |")
print("|---|---|---|---|---|")
for p,v in sorted(pre.items()):
    iss=collections.Counter(x[3] for x in v)
    inf=sorted(set(x[0] for x in v))
    nums=sorted(x[1] for x in v)
    fl=sorted(set(x[2] for x in v))
    print(f"| `{p}` | {', '.join(f'{k} {c}' for k,c in iss.most_common())} | {', '.join(inf)} | {nums[0]:04d}–{nums[-1]:04d} ({len(v)} docs) | {','.join(fl)} |")
fr=collections.defaultdict(list)
for d in D:
    m=re.search(r'-(\d{4})$',d['id'])
    if m: fr[d['flow']].append(int(m.group(1)))
print()
print("| Flow | Number range of root IDs | Documents |")
print("|---|---|---:|")
for f,v in sorted(fr.items(),key=lambda x:min(x[1])): print(f"| {f} | {min(v):04d}–{max(v):04d} | {len(v)} |")
