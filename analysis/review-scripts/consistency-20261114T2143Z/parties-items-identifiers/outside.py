import glob,re
n=0
for f in sorted(glob.glob('*/*.llm-review.*.merged.md')):
    txt=open(f).read()
    m=re.search(r'^## Outside this review\n(.*?)(?=^## |\Z)',txt,re.S|re.M)
    if not m: continue
    items=re.split(r'\n(?=- )',m.group(1).strip())
    for it in items:
        it=it.strip()
        if not it.startswith('-'): continue
        n+=1
        print(f"[{n}] {f.split('.')[0]}: {it[2:]}\n")
