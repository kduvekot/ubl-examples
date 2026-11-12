"""Check that every absolute XPath cited in a review resolves in the reviewed XML.

usage: python3 -I check_xpaths.py <NN-DocumentType.llm-review.md> [...]

Backticked absolute paths are checked against the reviewed XML. A path with another root element
(e.g. `/Waybill/...` cited from a TransportationStatus review) is checked against the examples of
the same flow with that root; it passes if it resolves in at least one of them, and the matching
files are named. Paths containing '…' are shorthand and are not checked.
"""
import re
import sys
from pathlib import Path

from lxml import etree

NS = {'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
      'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2',
      'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2'}


def resolves(path, xml_file):
    doc = etree.parse(str(xml_file))
    ns = dict(NS, d=doc.getroot().nsmap[None])
    q = re.sub(r'(^|/)([A-Z][A-Za-z]*)(?=/|\[|$)', lambda m: m.group(1) + 'd:' + m.group(2), path)
    return bool(doc.xpath(q, namespaces=ns))


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    failed = 0
    for md in sys.argv[1:]:
        xml = md.replace('.llm-review.md', '.xml')
        name = etree.QName(etree.parse(xml).getroot()).localname
        flow = Path(xml).parent
        for p in sorted(set(re.findall(r'`(/[A-Za-z][^`\s]*)`', open(md, encoding='utf-8').read()))):
            if '…' in p:
                continue
            root = p.split('/')[1].split('[')[0]
            try:
                if root == name:
                    ok, where = resolves(p, xml), ''
                else:
                    hits = [f.name for f in sorted(flow.glob('*.xml'))
                            if etree.QName(etree.parse(str(f)).getroot()).localname == root and resolves(p, f)]
                    ok, where = bool(hits), ', '.join(hits)
            except etree.XPathError as e:
                ok, where = False, str(e)
            if not ok:
                failed += 1
                print(f'{md}: NO MATCH {p} {where}')
            elif where:
                print(f'{md}: other document, resolves in {where}: {p}')
    print('all cited XPaths resolve' if not failed else f'{failed} XPath(s) do not resolve')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
