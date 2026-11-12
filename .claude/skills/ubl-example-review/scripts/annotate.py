"""List every element of a UBL instance with its XPath, value, UBL 2.5 definition (in its parent's
context, printed at the first occurrence) and the meaning of codes.

usage: python3 -I annotate.py <example.xml> [--full] [--hide-party-detail]

  default              indented element names (compact)
  --full               absolute XPaths on every line (to cite in a review)
  --hide-party-detail  collapse PostalAddress, PartyTaxScheme, PartyLegalEntity, Contact, Language,
                       ElectronicAddress subtrees to one line (for a first read; check them separately)

'!! NOT IN MODEL' marks an element the model does not define under that parent;
'?? NOT IN LIST' marks a code missing from the list its listID names.
"""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ubl_model import load_codelists, load_model  # noqa: E402

PARTY_DETAIL = {'PostalAddress', 'PartyTaxScheme', 'PartyLegalEntity', 'Contact', 'Language',
                'ElectronicAddress'}
ATTR_LISTS = (('unitCode', 'UnitOfMeasureCode'), ('currencyID', 'CurrencyCode'),
              ('mimeCode', 'BinaryObjectMimeCode'))


def ln(tag):
    return tag.split('}')[-1]


def prefix(tag):
    if 'CommonBasic' in tag:
        return 'cbc:'
    if 'CommonAggregate' in tag:
        return 'cac:'
    if 'CommonExtension' in tag:
        return 'ext:'
    return ''


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if len(args) != 1:
        sys.exit(__doc__)
    full = '--full' in sys.argv
    hide = '--hide-party-detail' in sys.argv
    children, documents = load_model()
    by_stem, by_id = load_codelists()

    def meaning(name, val, attrs):
        for a in ('listID', 'schemeID'):
            if a in attrs:
                lid = attrs[a]
                codes = by_id.get(lid) or by_stem.get(lid.split(':')[-1])
                if codes is not None:
                    return codes.get(val, f'?? NOT IN LIST {lid}')
        if name in by_stem:
            return by_stem[name].get(val, f'?? NOT IN LIST {name}')
        return None

    root = ET.parse(args[0]).getroot()
    doc = documents.get(ln(root.tag))
    print(f"/{ln(root.tag)}  :: {doc['Definition'] if doc else 'NOT A UBL 2.5 DOCUMENT'}")
    printed = set()

    def walk(el, path, oc, depth):
        counts = {}
        for c in el:
            counts[ln(c.tag)] = counts.get(ln(c.tag), 0) + 1
        seen = {}
        for c in el:
            n = ln(c.tag)
            seen[n] = seen.get(n, 0) + 1
            step = prefix(c.tag) + n + (f'[{seen[n]}]' if counts[n] > 1 else '')
            xp = f'{path}/{step}'
            label = xp if full else '  ' * depth + step
            if n == 'UBLExtensions':
                print(f'{label} (extensions)')
                continue
            r = children.get((oc, n)) if oc else None
            definition = ''
            if r is not None and (oc, n) not in printed:
                printed.add((oc, n))
                definition = f"  :: [{r['Cardinality']}] {r['Definition']}"
            text = (c.text or '').strip()
            if r is None:
                print(f'{label} = {text!r} {dict(c.attrib)}  !! NOT IN MODEL under {oc}')
                walk(c, xp, None, depth + 1)
            elif r['ComponentType'] == 'ASBIE':
                if hide and n in PARTY_DETAIL:
                    print(f"{label}  -> {r['AssociatedObjectClass']}  [detail hidden]")
                    continue
                print(f"{label}  -> {r['AssociatedObjectClass']}{definition}")
                walk(c, xp, r['AssociatedObjectClass'], depth + 1)
            else:
                attrs = dict(c.attrib)
                line = f"{label} = {text!r} " + ' '.join(f'@{k}="{v}"' for k, v in attrs.items())
                m = meaning(n, text, attrs)
                if m:
                    line += f'  {{code: {m}}}'
                for attr, stem in ATTR_LISTS:
                    if attr in attrs and stem in by_stem:
                        line += f" {{{attr}: {by_stem[stem].get(attrs[attr], '?? NOT IN LIST')}}}"
                print(line + definition)

    walk(root, '/' + ln(root.tag), doc['ObjectClass'] if doc else None, 1)


if __name__ == '__main__':
    main()
