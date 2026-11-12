"""Check that every absolute XPath cited in a review resolves in the reviewed XML.

usage: python3 -I check_xpaths.py <NN-DocumentType.llm-review.md> [...]

Only backticked paths that start with the review's own root element are checked; paths into other
documents (e.g. `/Waybill/...` cited from a TransportationStatus review) are listed as skipped.
Paths containing '…' are shorthand and are not checked.
"""
import re
import sys

from lxml import etree

NS = {'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
      'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2',
      'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2'}


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    failed = 0
    for md in sys.argv[1:]:
        xml = md.replace('.llm-review.md', '.xml')
        doc = etree.parse(xml)
        root = doc.getroot()
        ns = dict(NS, d=root.nsmap[None])
        name = etree.QName(root).localname
        for p in sorted(set(re.findall(r'`(/[A-Za-z][^`\s]*)`', open(md, encoding='utf-8').read()))):
            if '…' in p:
                continue
            if not p.startswith(f'/{name}/') and p != f'/{name}':
                print(f'{md}: skipped (other document) {p}')
                continue
            q = re.sub(r'(^|/)([A-Z][A-Za-z]*)(?=/|\[|$)', lambda m: m.group(1) + 'd:' + m.group(2), p)
            try:
                ok = bool(doc.xpath(q, namespaces=ns))
            except etree.XPathError as e:
                ok, p = False, f'{p} ({e})'
            if not ok:
                failed += 1
                print(f'{md}: NO MATCH {p}')
    print('all cited XPaths resolve' if not failed else f'{failed} XPath(s) do not resolve')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
