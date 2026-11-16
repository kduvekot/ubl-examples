import glob,re,sys
out=[]
for f in sorted(glob.glob('world/examples/*/*.llm-review.*.merged.md')):
    t=open(f).read()
    m=re.search(r'^## Outside this review\s*\n(.*?)(?=^## |\Z)',t,re.S|re.M)
    if not m: continue
    items=re.split(r'\n(?=- )',m.group(1).strip())
    for it in items:
        it=it.strip()
        if it: out.append((f.split('world/examples/')[1].split('.llm')[0],it))
for f,it in out: print('###',f,'\n',it,'\n')
print(len(out),file=sys.stderr)
