"""Check that every value a review quotes is the value in the XML.

usage: python3 -I check_values.py <NN-DocumentType.llm-review.<run-id>[.<part>].md> [...]

Checks every `citation` = `value` pair (citation as in check_xpaths.py). It passes when one of the
elements the citation selects has exactly that text (leading and trailing white space ignored).
A quoted value ending in '…' is a shortened quote and passes when the element's text starts with it.
Values that wrap or are paraphrased are not in that form and are not checked: quote them exactly.
"""
import sys
from pathlib import Path

from lxml import etree

sys.path.insert(0, str(Path(__file__).resolve().parent))
from citations import resolve, text_of, value_citations  # noqa: E402


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    checked = failed = 0
    for md in sys.argv[1:]:
        for prefix, path, quoted in value_citations(md):
            checked += 1
            try:
                hits = resolve(md, prefix, path)
            except etree.XPathError as e:
                failed += 1
                print(f'{md}: INVALID {prefix}{path} ({e})')
                continue
            values = [text_of(n) for _, sel in hits for n in sel]
            q = quoted.strip()
            ok = q in values or (q.endswith('…') and any(v.startswith(q[:-1].rstrip()) for v in values))
            if not ok:
                failed += 1
                found = ', '.join(repr(v) for v in values[:3]) or 'nothing'
                print(f'{md}: VALUE {prefix}{path} quoted {quoted!r}, found {found}')
    print(f'{checked} quoted values checked: ' + ('all match' if not failed else f'{failed} do not match'))
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
