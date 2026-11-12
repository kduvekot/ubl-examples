"""Verify check digits of identifiers in a UBL instance.

usage: python3 -I check_ids.py <example.xml>

Checks, by schemeID (or by shape where no schemeID is given):
  GS1 GLN, GTIN, SSCC, GRAI (GS1 mod-10) · ISIN (ISO 6166) · IBAN-like accounts (ISO 13616 mod 97)
  · creditor references RF (ISO 11649) · container numbers (ISO 6346)
Prints every identifier checked, with OK or WRONG.
"""
import re
import sys

from lxml import etree


def gs1(s):
    body, check = s[:-1], int(s[-1])
    total = sum(int(c) * (3 if i % 2 == 0 else 1) for i, c in enumerate(reversed(body)))
    return (10 - total % 10) % 10 == check


def isin(s):
    digits = ''.join(str(int(c, 36)) for c in s[:-1])
    total = 0
    for i, ch in enumerate(reversed(digits)):
        n = int(ch) * (2 if i % 2 == 0 else 1)
        total += n // 10 + n % 10
    return (10 - total % 10) % 10 == int(s[-1])


def mod97(s):
    r = s[4:] + s[:4]
    return int(''.join(str(int(c, 36)) for c in r)) % 97 == 1


def iso6346(s):
    values, v = {}, 10
    for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if v % 11 == 0:
            v += 1
        values[c] = v
        v += 1
    total = sum((values[c] if c.isalpha() else int(c)) * 2 ** i for i, c in enumerate(s[:10]))
    return total % 11 % 10 == int(s[10])


def classify(scheme, val):
    s = (scheme or '').upper()
    if 'GLN' in s or 'GTIN' in s or 'SSCC' in s or ('GRAI' in s and val.isdigit()):
        return 'GS1', gs1(val[:14] if 'GRAI' in s else val)
    if '6166' in s or 'ISIN' in s:
        return 'ISIN', isin(val)
    if '11649' in s or re.fullmatch(r'RF\d\d[0-9A-Z]{1,21}', val):
        return 'RF', mod97(val)
    if '6346' in s or re.fullmatch(r'[A-Z]{4}\d{7}', val):
        return 'ISO 6346', iso6346(val)
    if re.fullmatch(r'[A-Z]{2}\d\d[A-Z0-9]{10,30}', val):
        return 'IBAN-like', mod97(val)
    return None, None


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    for e in etree.parse(sys.argv[1]).getroot().iter():
        if not isinstance(e.tag, str) or len(e):
            continue
        val = (e.text or '').strip()
        if not val or ' ' in val:
            continue
        kind, ok = classify(e.get('schemeID'), val)
        if kind:
            print(f"{'OK   ' if ok else 'WRONG'} {kind:10} {etree.QName(e).localname} = {val}")


if __name__ == '__main__':
    main()
