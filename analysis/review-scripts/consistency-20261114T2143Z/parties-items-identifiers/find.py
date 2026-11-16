import csv,sys
# usage: find.py table value [flowfile-prefix]
t=sys.argv[1]; v=sys.argv[2]; pre=sys.argv[3] if len(sys.argv)>3 else ''
col='value'
for r in csv.DictReader(open('/home/user/ubl-examples/.review/tables/'+t)):
    if r.get(col)==v and (r['flow']+'/'+r['file']).startswith(pre):
        print(f"`{r['flow']}/{r['file']}:{r['xpath']}` = `{r['value']}`")
