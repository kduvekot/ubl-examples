import csv,collections,re
I=list(csv.DictReader(open('items.csv')))
L=list(csv.DictReader(open('lines.csv')))
D={(r['flow'],r['file']):r for r in csv.DictReader(open('documents.csv'))}
def en(v):
    parts=v.split(' | '); e=[p for p in parts if p.startswith('[en')] or [p for p in parts if not p.startswith('[q')] or parts
    return re.sub(r'^\[[^\]]*\] ','',e[0]) if v else ''
# group items by physical item: manufacturer id, else sellers id
def key(r):
    m=r['manufacturers_id'] or ''
    s=r['sellers_id']
    ids=set(filter(None,[m,s]))
    return ids
groups=[]
for r in I:
    ids=set(x for x in [r['manufacturers_id'],r['sellers_id'],r['standard_id'],r['additional_id']] if x)
    if not ids: ids={'(no ID) '+en(r['name'])}
    for g in groups:
        if g['ids']&ids: g['ids']|=ids; g['rows'].append(r); break
    else: groups.append({'ids':ids,'rows':[r]})
# merge transitively
changed=True
while changed:
    changed=False
    for i in range(len(groups)):
        for j in range(i+1,len(groups)):
            if groups[i]['ids']&groups[j]['ids']:
                groups[i]['ids']|=groups[j]['ids']; groups[i]['rows']+=groups[j]['rows']; del groups[j]; changed=True; break
        if changed: break
price=collections.defaultdict(list)
for r in L:
    if r['price'] and r['item_main_id']:
        d=D[(r['flow'],r['file'])]
        price[r['item_main_id'].split('=',1)[1]].append((d['issuer'],r['price'].split(' | ')[0]))
print("| Item (English name) | Seller's IDs | Manufacturer's ID | Standard ID (scheme) | Additional ID | Buyer's IDs | HS / CPC | Origin | Flows (items) | Prices (seller: price) |")
print("|---|---|---|---|---|---|---|---|---|---|")
for g in sorted(groups,key=lambda g:-len(g['rows'])):
    rs=g['rows']
    S=lambda c: '; '.join(sorted(set(r[c] for r in rs if r[c])))
    name=collections.Counter(en(r['name']) for r in rs).most_common(1)[0][0]
    std='; '.join(sorted(set(f"{r['standard_id']} ({r['standard_id_scheme'].replace('urn:ubl-examples:world:','')})" for r in rs if r['standard_id'])))
    hs='; '.join(sorted(set((r['commodity_code'].split(' | ')[0] if r['commodity_code'] else '')+'/'+r['item_classification'] for r in rs if r['commodity_code'] or r['item_classification'])))
    fl=collections.Counter(r['flow'] for r in rs)
    pr=[]
    for sid in sorted(set(r['sellers_id'] for r in rs if r['sellers_id'])):
        for iss,p in sorted(set(price.get(sid,[]))): pr.append(f"{iss}: {p}")
    cells=[name,S('sellers_id'),S('manufacturers_id'),std,S('additional_id'),S('buyers_id'),hs,S('origin_country'),', '.join(f'{k} {v}' for k,v in sorted(fl.items())),'; '.join(pr) or '–']
    cells=[(c or '–').replace('|','/') for c in cells]
    print('| '+' | '.join(cells)+' |')
