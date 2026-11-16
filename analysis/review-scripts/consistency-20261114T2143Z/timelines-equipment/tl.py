import csv,sys,collections,os
T='/home/user/ubl-examples/.review/tables/'
docs=list(csv.DictReader(open(T+'documents.csv')))
dates=collections.defaultdict(list)
for r in csv.DictReader(open(T+'dates.csv')):
    dates[(r['flow'],r['file'])].append(r)
refs=collections.defaultdict(list)
for r in csv.DictReader(open(T+'references.csv')):
    refs[(r['flow'],r['file'])].append(r)
out=sys.argv[1]
flows=sorted(set(d['flow'] for d in docs))
for fl in flows:
    with open(f'{out}/tl-{fl}.txt','w') as o:
        ds=[d for d in docs if d['flow']==fl]
        ds.sort(key=lambda d:d['file'])
        for d in ds:
            o.write(f"\n### {d['file']} {d['root']} id={d['id']} issue={d['issue_timestamp'] or d['issue_date']} issuer={d['issuer']}\n")
            for r in dates[(fl,d['file'])]:
                x=r['xpath'].split('/',2)[-1]
                if x in ('cbc:IssueDate','cbc:IssueTime'): continue
                if r['kind'].endswith('Time') and r['timestamp']: continue
                v=r['timestamp'] or r['value']
                o.write(f"   {v:22} {r['xpath']}\n")
            for r in refs[(fl,d['file'])]:
                o.write(f"   REF {r['element']} id={r['id']} date={r['issue_date']} {r['issue_time']} type={r['document_type'] or r['type_code']} -> {r['example_matches']}\n")
