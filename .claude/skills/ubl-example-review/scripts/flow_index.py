"""Compact index of one flow: per document its type, ID, issue date/time, its top-level parties by role, and the
identifiers it references, each resolved to the example file whose document ID it is.

usage: python3 -I flow_index.py <flow>        (e.g. rail; a folder under world/examples)

A reference shown as '-> ?' does not match the document ID of any example in any flow: either it
points to a document outside the examples (fine if the referenced thing is not an example), or it
is broken. Check those.
"""
import sys
from pathlib import Path

from lxml import etree

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ubl_model import EXAMPLES  # noqa: E402


def ln(e):
    return etree.QName(e).localname


def top(root, name):
    return root.xpath(f'string(*[local-name()="{name}"])')


def parties(root):
    """Every top-level party role of the document with the party's name."""
    out = []
    for p in root:
        if isinstance(p.tag, str) and ln(p).endswith('Party'):
            n = p.xpath('string(.//*[local-name()="PartyName"]/*[local-name()="Name"]'
                        ' | .//*[local-name()="RegistrationName"])')
            out.append(f'{ln(p)}={n or "?"}')
    return ', '.join(dict.fromkeys(out)) or '-'


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    flow = EXAMPLES / sys.argv[1]
    ids = {}
    for f in sorted(EXAMPLES.glob('*/*.xml')):
        did = top(etree.parse(str(f)).getroot(), 'ID')
        if did:
            ids.setdefault(did, []).append(f'{f.parent.name}/{f.name}')
    for f in sorted(flow.glob('*.xml')):
        root = etree.parse(str(f)).getroot()
        print(f"== {f.name}  {ln(root)}  ID={top(root, 'ID')}  issued {top(root, 'IssueDate')} "
              f"{top(root, 'IssueTime')[:5]}")
        print(f'   parties: {parties(root)}')
        refs = []
        for e in root.iter():
            if isinstance(e.tag, str) and (ln(e).endswith('Reference') or ln(e) == 'Contract') and len(e):
                rid = e.xpath('string(*[local-name()="ID"])')
                if rid:
                    target = ', '.join(x for x in ids.get(rid, []) if x != f'{flow.name}/{f.name}') or '?'
                    refs.append(f'{ln(e)} {rid} -> {target}')
        for r in dict.fromkeys(refs):
            print(f'   ref {r}')


if __name__ == '__main__':
    main()
