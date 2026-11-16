"""cite(finding_id) -> list of '`flow/NN-Doc.xml:/path` = `value`' strings taken from the finding's XPath lines,
checked against the XML with the review skill's citations module."""
import csv, re, sys
from pathlib import Path
REPO = Path('/home/user/ubl-examples')
sys.path.insert(0, str(REPO / '.claude/skills/ubl-example-review/scripts'))
from citations import select, text_of  # noqa
ROWS = {r['finding']: r for r in csv.DictReader(open(REPO / '.review/worklist/findings.csv', encoding='utf-8'))}
CITE = re.compile(r'`((?:[\w.-]+/)?[\w.-]+\.xml:)?(/[A-Za-z][^`\s]*)`\s*=\s*`([^`]*)`')

def block(fid):
    r = ROWS[fid]
    text = (REPO / r['source']).read_text(encoding='utf-8')
    head = '### ' + fid + ' '
    i = text.index(head)
    j = text.find('\n### ', i + 1); k = text.find('\n## ', i + 1)
    ends = [x for x in (j, k) if x > 0]
    return text[i:min(ends) if ends else len(text)], r

def cite(fid, n=1):
    b, r = block(fid)
    out = []
    for line in re.findall(r'^- XPath: (.*)$', b, re.M):
        for m in CITE.finditer(line):
            pre, path, val = m.groups()
            if '…' in path or '…' in val:
                continue
            if pre:
                name = pre[:-1]
                xml = (REPO / 'world/examples' / name) if '/' in name else (REPO / 'world/examples' / r['flow'] / name)
                q = name if '/' in name else f"{r['flow']}/{name}"
            else:
                if r['flow'] == 'consistency':
                    continue
                xml = REPO / 'world/examples' / r['flow'] / (r['example'] + '.xml'); q = f"{r['flow']}/{r['example']}.xml"
            try:
                vals = [text_of(x) for x in select(path, xml)]
            except Exception:
                continue
            if val.strip() in vals:
                out.append(f'`{q}:{path}` = `{val}`')
            if len(out) >= n:
                return out
    return out

if __name__ == '__main__':
    for f in sys.argv[1:]:
        print(f, cite(f, 2))
