import csv,collections
T='/home/user/ubl-examples/.review/tables/'
docs={(d['flow'],d['file']):d for d in csv.DictReader(open(T+'documents.csv'))}
def ts(d): return d['issue_timestamp'] or d['issue_date']
for r in csv.DictReader(open(T+'references.csv')):
    src=docs[(r['flow'],r['file'])]
    for m in filter(None,[x.strip() for x in r['example_matches'].split('|')]):
        fl,fi=(m.split('/',1) if '/' in m else (r['flow'],m))
        t=docs.get((fl,fi))
        if not t: print('?',m); continue
        if ts(t)>ts(src):
            print(f"{r['flow']}/{r['file']} [{ts(src)}] refs {fl}/{fi} [{ts(t)}] via {r['xpath']}")
