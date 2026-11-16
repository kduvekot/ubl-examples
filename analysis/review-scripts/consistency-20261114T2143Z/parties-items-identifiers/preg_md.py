import csv,collections,re
P=list(csv.DictReader(open('parties.csv')))
C=list(csv.DictReader(open('contacts.csv')))
A=list(csv.DictReader(open('financial_accounts.csv')))
by=collections.defaultdict(list)
for r in P: by[r['name']].append(r)
def en(v):
    parts=v.split(' | '); e=[p for p in parts if p.startswith('[en')]
    return re.sub(r'^\[[^\]]*\] ','',(e or parts)[0]) if v else ''
def top(rs,c):
    cnt=collections.Counter(r[c] for r in rs if r[c]); return cnt.most_common(1)[0][0] if cnt else ''
cont=collections.defaultdict(collections.Counter)
for r in C:
    if r['party_name'] and r['name']: cont[r['party_name']][f"{r['name']} ({r['job_title'] or '-'}, {r['telephone'] or '-'})"]+=1
acc=collections.defaultdict(set)
for r in A:
    acc[r['name'].rsplit(' ',1)[0] if r['name'].split()[-1] in('Ltd','SUA','SRU','Corp') else r['name']].add(r['id'])
print("| Party | Ctry | Register ID | Other party IDs | Tax ID | Postal address (English rendering) | Legal form · registered · size · capital | ISIC | Files (flows) | Main roles | Contacts (name, job title, phone) | Account | Varies |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for n,rs in sorted(by.items(),key=lambda x:-len(x[1])):
    g=lambda c: top(rs,c)
    reg=g('party_id')
    oth='; '.join(sorted(set(f"{a} ({b.replace('urn:ubl-examples:world:','')})" for r in rs if r['additional_party_id'] for a,b in zip(r['additional_party_id'].split(' | '),r['additional_party_id_scheme'].split(' | ')))))
    addr=', '.join(x for x in [en(g('street'))+(' '+g('building_number') if g('building_number') else ''),en(g('additional_street')),g('postal_zone'),en(g('city')),en(g('subentity')),en(g('region'))] if x)
    aid=g('address_id')
    if aid: addr+=f" [ID {aid}]"
    le=' · '.join(x or '–' for x in [g('legal_form_code'),g('registration_date'),g('size_code'),g('stock_amount')])
    if le=='– · – · – · –': le='—'
    files=len(set((r['flow'],r['file']) for r in rs)); flows=','.join(sorted(set(r['flow'] for r in rs)))
    roles=', '.join(f"{k} {v}" for k,v in collections.Counter(r['role'] for r in rs).most_common(4))
    cs='; '.join(f"{k}" for k,v in cont[n].most_common(3))
    ac='; '.join(sorted(acc.get(n,[])))
    var=[]
    for c in ['street','city','legal_form','legal_registration_city']:
        vals=set(r[c] for r in rs if r[c])
        if len(vals)>1:
            tags=sorted(set(t for v in vals for t in re.findall(r'\[(en-X.)\]',v)))
            var.append(c+(' ('+'/'.join(tags)+')' if tags else ' (tagged/untagged)'))
    tax=g('tax_company_id')
    row=f"| {n} | {g('country') or '–'} | {reg or '–'} | {oth or '–'} | {tax or '–'} | {addr or '–'} | {le} | {g('industry_code') or '–'} | {files} ({flows}) | {roles} | {cs or '–'} | {ac or '–'} | {', '.join(var) or 'none'} |"
    print(row)
