#!/usr/bin/env python3
"""The identifier schemes of the UBL example world, and their checks (decisions ID-Q1 to ID-Q4).

An identifier that comes from a scheme names it in schemeID. The schemes are kept in world/countries.json:

  identifier_schemes        the schemes of the Trade Accord and the real external schemes the world uses, by
                            their schemeID: the Accord's in the world's lowercase URN style
                            (urn:ubl-examples:world:endpoint), the external ones in UBL's text style (ISO 11649);
  countries.<CC>.identifiers  each country's own schemes, by kind; a kind with "scheme": true is named
                            urn:ubl-examples:world:<CC>:<kind> (urn:ubl-examples:world:XB:vehicle-register),
                            the others (call signs, MMSIs, driving licences, national ID numbers) have a format
                            the world checks, but no schemeID: the element already says what they are.

Every scheme has a pattern; some have a check digit, named in "check" and computed here. A code held in an
identifier (TaxCategory/ID, Language/ID ...) is not a scheme of this registry: its schemeID is the listID of its
code list (world/codelists/lists.json), and the world's code list validation checks it.
"""
import re

import world_data


# ---------------------------------------------------------------- check digits
def _alnum_digits(s):
    return "".join(str(int(ch, 36)) for ch in s)


def mod97(s):
    """ISO 7064 mod 97-10 over a string whose letters count as 10..35 (ISO 13616, ISO 11649): the remainder is 1."""
    return int(_alnum_digits(s)) % 97 == 1


def iso13616(v):
    return mod97(v[4:] + v[:4])


def iso11649(v):
    return v.startswith("RF") and mod97(v[4:] + v[:4])


def luhn(digits):
    total = 0
    for i, ch in enumerate(reversed(digits)):
        n = int(ch) * (2 if i % 2 else 1)
        total += n - 9 if n > 9 else n
    return total % 10 == 0


def luhn_digit(digits):
    """The Luhn check digit to append to a string of digits."""
    return next(str(d) for d in range(10) if luhn(digits + str(d)))


def iso6166(v):
    return luhn(_alnum_digits(v))


ISO6346_VALUES = {c: v for c, v in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", [10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 24, 25,
                                                                   26, 27, 28, 29, 30, 31, 32, 34, 35, 36, 37, 38])}


def iso6346_digit(code):
    total = sum((ISO6346_VALUES[c] if c.isalpha() else int(c)) * 2 ** i for i, c in enumerate(code))
    return str(total % 11 % 10)


def iso6346(v):
    return iso6346_digit(v[:10]) == v[10]


def gs1_digit(digits):
    """The GS1 check digit (mod 10, weights 3 and 1 from the right) to append to the digits of a GTIN, GLN or SSCC."""
    s = sum(int(d) * (3 if i % 2 == 0 else 1) for i, d in enumerate(reversed(digits)))
    return str(-s % 10)


def gs1(v):
    digits = re.sub(r"\D", "", v)
    return gs1_digit(digits[:-1]) == digits[-1]


def uic_digit(digits):
    """The check digit of a UIC wagon number: the eleven digits weighted 2, 1, 2 ... from the left, the digits of the
    products summed; the check digit makes the sum a multiple of 10."""
    s = sum(sum(divmod(int(d) * (2 if i % 2 == 0 else 1), 10)) for i, d in enumerate(digits))
    return str(-s % 10)


def uic(v):
    digits = re.sub(r"\D", "", v)
    return len(digits) == 12 and uic_digit(digits[:11]) == digits[11]


def mod11_xu(v):
    """The XU tax number: weights 9..2 over the 8 digits after XU, modulus 11 (remainder 10 is never issued)."""
    digits = v[2:]
    s = sum(int(d) * w for d, w in zip(digits, range(9, 1, -1))) % 11
    return s != 10 and str(s) == digits[8]


def mod10_iso15459(v):
    """The check character of a Codana licence plate (ISO 15459 style): GS1-style mod 10 over its digits."""
    return gs1(v)


def gs1_grai(v):
    """A GRAI: the filler digit 0, company prefix and asset type (12 digits), the check digit over them, and the
    asset's serial number."""
    return gs1_digit(v[:13]) == v[13]


CHECKS = {"gs1-grai": gs1_grai, "iso13616": iso13616, "iso11649": iso11649, "iso6166": iso6166, "iso6346": iso6346, "gs1": gs1,
          "uic": uic, "mod11-xu": mod11_xu, "luhn": lambda v: luhn(re.sub(r"\D", "", v)), "iso15459": mod10_iso15459}


# ---------------------------------------------------------------- the registry
def national_scheme(country, kind):
    return f"urn:ubl-examples:world:{country}:{kind}"


def registry(world=None):
    """Every scheme the world knows, by schemeID: {schemeID: spec}; spec has name, pattern, check (optional),
    country (for a national scheme) and kind."""
    world = world or world_data.load()
    out = {}
    for sid, spec in world.get("identifier_schemes", {}).items():
        out[sid] = {**spec, "kind": spec.get("kind", sid)}
    for cc, c in world["countries"].items():
        for kind, spec in c.get("identifiers", {}).items():
            if spec.get("scheme", True):
                out[national_scheme(cc, kind)] = {**spec, "country": cc, "kind": kind}
    return out


def formats(world, kind):
    """The national formats of one kind of identifier: [(country, spec)]."""
    return [(cc, c["identifiers"][kind]) for cc, c in world["countries"].items() if kind in c.get("identifiers", {})]


def problem(spec, value):
    """Why a value does not fit its scheme, or None."""
    if not re.fullmatch(spec["pattern"], value):
        return f"'{value}' does not have the format of {spec['name']} ({spec.get('format', spec['pattern'])})"
    if spec.get("check") and not CHECKS[spec["check"]](value):
        return f"'{value}' has a wrong check digit ({spec['name']}: {spec['check']})"
    return None


def country_of(world, kind, value):
    """The country whose scheme of a kind the value fits, or None."""
    hits = [cc for cc, spec in formats(world, kind) if re.fullmatch(spec["pattern"], value)]
    return hits[0] if len(hits) == 1 else None


# ---------------------------------------------------------------- making identifiers (decision ID-Q7)
def gs1_number(prefix, ref, length):
    """A GS1 key of `length` digits: the company prefix, the reference padded to fill, and the check digit."""
    body = prefix + str(ref).zfill(length - 1 - len(prefix))
    return body + gs1_digit(body)


def sscc(prefix, serial):
    return gs1_number("0" + prefix, serial, 18)


def licence_plate(cin, serial):
    """An ISO/IEC 15459 licence plate of the Codana Identification Agency (IAC KXU): KXU, the company number, a
    nine-digit serial and a mod-10 check digit over the digits."""
    body = f"{cin}{str(serial).zfill(9)}"
    return f"KXU{body}{gs1_digit(body)}"
