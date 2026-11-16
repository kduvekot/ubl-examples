import csv,sys,re
T='/home/user/ubl-examples/.review/tables/'
fl,fi,pat=sys.argv[1],sys.argv[2],sys.argv[3]
for t in ['dates','identifiers','texts','measures','codes','amounts']:
    for r in csv.DictReader(open(T+t+'.csv')):
        if r['flow']==fl and r['file'].startswith(fi) and re.search(pat,r['xpath']):
            print(f"- XPath: `{fl}/{r['file']}:{r['xpath']}` = `{r['value']}`")
