"""Check that every XPath a review cites resolves.

usage: python3 -I check_xpaths.py <NN-DocumentType.llm-review.<run-id>[.<part>].md> [...]

Citations (see citations.py): `/Root/…` in the reviewed example or, if it does not resolve there,
in the other examples of the same flow with that root; `<flow>/NN-Doc.xml:/Root/…` or
`NN-Doc.xml:/Root/…` in the named example. Paths containing '…' are shorthand and are skipped.
"""
import sys
from pathlib import Path

from lxml import etree

sys.path.insert(0, str(Path(__file__).resolve().parent))
from citations import citations, resolve, review_xml  # noqa: E402


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    failed = 0
    for md in sys.argv[1:]:
        own = review_xml(md).resolve()
        for prefix, path in citations(md):
            try:
                hits = resolve(md, prefix, path)
            except etree.XPathError as e:
                failed += 1
                print(f'{md}: INVALID {prefix}{path} ({e})')
                continue
            if not hits:
                failed += 1
                print(f'{md}: NO MATCH {prefix}{path}')
            elif hits[0][0].resolve() != own:
                where = ', '.join(f'{f.parent.name}/{f.name}' for f, _ in hits)
                print(f'{md}: other document, resolves in {where}: {prefix}{path}')
    print('all cited XPaths resolve' if not failed else f'{failed} XPath(s) do not resolve')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
