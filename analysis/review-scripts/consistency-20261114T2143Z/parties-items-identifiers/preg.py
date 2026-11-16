import csv,collections,re
rows=list(csv.DictReader(open('parties.csv')))
by=collections.defaultdict(list)
for r in rows: by[r['name']].append(r)
def strip(v): 
    # keep english rendering only
    parts=v.split(' | ')
    en=[p for p in parts if p.startswith('[en')]
    p=(en or parts)[0]
    return re.sub(r'^\[[^\]]*\] ','',p)
def top(rs,c):
    cnt=collections.Counter(r[c] for r in rs if r[c])
    return cnt.most_common(1)[0][0] if cnt else ''
for n,rs in sorted(by.items(),key=lambda x:-len(x[1])):
    g=lambda c: top(rs,c)
    pid=' ; '.join(sorted(set(f"{r['party_id']}({r['party_id_scheme']})" for r in rs if r['party_id'])))
    apid=' ; '.join(sorted(set(f"{r['additional_party_id']}({r['additional_party_id_scheme']})" for r in rs if r['additional_party_id'])))
    ep=' ; '.join(sorted(set(f"{r['endpoint']}({r['endpoint_scheme']})" for r in rs if r['endpoint'])))
    addr=', '.join(x for x in [strip(g('street')),g('building_number'),strip(g('additional_street')),g('postal_zone'),strip(g('city')),strip(g('subentity')),g('subentity_code'),strip(g('region')),g('country')] if x)
    roles=collections.Counter(r['role'] for r in rs)
    print(f"| {n} | {g('country')} | {pid} | {apid} | {ep} | {g('legal_company_id')}({g('legal_company_id_scheme')}) | {g('tax_company_id')}({g('tax_company_id_scheme')}) {strip(g('tax_scheme'))} | {g('legal_form_code')} | {g('registration_date')} | {g('size_code')} | {g('stock_amount')} | {g('industry_code')}({g('industry_code_list')}) | {addr} | {g('website')} | {len(set(r['file'] for r in rs))} files: {','.join(sorted(set(r['flow'] for r in rs)))} | {', '.join(f'{k} {v}' for k,v in roles.most_common())} |")
