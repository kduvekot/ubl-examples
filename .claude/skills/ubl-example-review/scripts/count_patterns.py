"""Count the registered recurring patterns over the XML examples, reproducibly.

usage: python3 -I count_patterns.py [R<n> ...] [--list]

Without arguments: one line per pattern with occurrences and number of examples.
With pattern IDs: only those. --list also prints every occurrence as `<flow>/<file>: <XPath>`.

Each pattern is a function that yields (element, note) for the occurrences in one document.
When a new pattern is added to world/examples/recurring.llm-review.md, add its rule here with the
same ID, and state the rule in the register's "How counted" line.
"""
import re
import sys
from pathlib import Path

from lxml import etree

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ubl_model import EXAMPLES  # noqa: E402

CBC = 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2'
CAC = 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2'
ITALIAN = re.compile(r'\b(Via|Viale|Piazza|Piazzale|Corso|Largo|Vicolo|Strada|Lungomare|Valico|'
                     r'Società|del|della|delle|dei|degli|di)\b')
CUSTOMER_ROLES = {'BuyerCustomerParty', 'AccountingCustomerParty', 'DeliveryCustomerParty',
                  'ConsigneeParty', 'ContractorCustomerParty', 'OriginatorCustomerParty'}
SUPPLIER_ROLES = {'SellerSupplierParty', 'AccountingSupplierParty', 'DespatchSupplierParty',
                  'ConsignorParty'}


def ln(e):
    return etree.QName(e).localname


def cbc(e, name):
    return e.find(f'{{{CBC}}}{name}')


def text(e):
    return (e.text or '').strip() if e is not None else ''


def r1(doc):  # LocaleCode holds a bare language code
    for e in doc.iter(f'{{{CBC}}}LocaleCode'):
        if ln(e.getparent()) == 'Language' and re.fullmatch(r'[a-z]{2,3}', text(e)):
            yield e


def r2(doc):  # Italian text tagged as English
    for e in doc.iter():
        if isinstance(e.tag, str) and (e.get('languageID') or '').startswith('en') and ITALIAN.search(text(e)):
            yield e


def r3(doc):  # Region holds a subdivision of one country
    for e in doc.iter(f'{{{CBC}}}Region'):
        if re.match(r'(Province|State|County|District|Region) of ', text(e)):
            yield e


def r4(doc):  # a gate in AdditionalStreetName
    for e in doc.iter(f'{{{CBC}}}AdditionalStreetName'):
        if re.match(r'Gate\b', text(e)):
            yield e


def r5(doc):  # placeholder registration date
    for e in doc.iter(f'{{{CBC}}}RegistrationDate'):
        if text(e) == '1996-01-01':
            yield e


def r6(doc):  # ShippingOrderID holds a consignment identifier of the same document
    consignments = {text(c) for c in doc.iter(f'{{{CAC}}}Consignment') for c in [cbc(c, 'ID')] if c is not None}
    for e in doc.iter(f'{{{CBC}}}ShippingOrderID'):
        if text(e) in consignments:
            yield e


def r7(doc):  # public authority described as registered in a commercial register
    for party in doc.iter():
        if not isinstance(party.tag, str):
            continue
        isic = cbc(party, 'IndustryClassificationCode')  # any element that is a party
        if isic is None or not text(isic).startswith('84'):
            continue
        for t in party.iterfind(f'{{{CAC}}}PartyLegalEntity/{{{CAC}}}CorporateRegistrationScheme/'
                                f'{{{CBC}}}CorporateRegistrationTypeCode'):
            if text(t) == 'COMMERCIAL':
                yield t


def r8(doc):  # contact contradicts the party's role, or contradicts itself
    ns = {'cac': CAC, 'cbc': CBC}
    seen = set()
    for party in doc.iter():
        if not isinstance(party.tag, str):
            continue
        role = ln(party)
        wrong = 'Sales' if role in CUSTOMER_ROLES else 'Procurement' if role in SUPPLIER_ROLES else None
        # the role's own contact: directly in the role, or in its cac:Party (not nested parties)
        for contact in party.xpath('cac:Contact | cac:Party/cac:Contact', namespaces=ns):
            d = text(cbc(contact, 'Department'))
            name = text(cbc(contact, 'Name'))
            buying = re.search(r'\b(Buying|Purchasing)\b', name)
            if (wrong and d == wrong) or (buying and d == 'Sales'):
                if id(contact) not in seen:
                    seen.add(id(contact))
                    yield cbc(contact, 'Department')


def r9(doc):  # FullnessIndicationCode used for the emission system boundary
    for e in doc.iter(f'{{{CBC}}}FullnessIndicationCode'):
        if ln(e.getparent()) == 'EmissionCalculationMethod':
            yield e


def r10(doc):  # emission value does not equal factor x base
    for em in doc.iter(f'{{{CAC}}}EnvironmentalEmission'):
        v, f, b = (cbc(em, n) for n in ('ValueMeasure', 'ValueFactorNumeric', 'ValueBaseMeasure'))
        if v is not None and f is not None and b is not None:
            if abs(float(text(v)) - float(text(f)) * float(text(b))) > 0.005:
                yield v


def r11(doc):  # a party's own tax exemption worded as a transaction
    for e in doc.iter(f'{{{CBC}}}ExemptionReasonCode'):
        if ln(e.getparent()) == 'PartyTaxScheme' and text(e) == 'PUBLIC':
            yield e


PATTERNS = {'R1': r1, 'R2': r2, 'R3': r3, 'R4': r4, 'R5': r5, 'R6': r6, 'R7': r7, 'R8': r8, 'R9': r9,
            'R10': r10, 'R11': r11}


def xpath_of(e):
    parts = []
    while e is not None and isinstance(e.tag, str):
        p = e.getparent()
        prefix = 'cbc:' if CBC in e.tag else 'cac:' if CAC in e.tag else ''
        step = prefix + ln(e)
        if p is not None:
            same = [s for s in p if s.tag == e.tag]
            if len(same) > 1:
                step += f'[{same.index(e) + 1}]'
        parts.append(step)
        e = p
    return '/' + '/'.join(reversed(parts))


def main():
    wanted = [a for a in sys.argv[1:] if not a.startswith('--')] or list(PATTERNS)
    show = '--list' in sys.argv
    docs = [(f, etree.parse(str(f)).getroot()) for f in sorted(EXAMPLES.glob('*/*.xml'))]
    for pid in wanted:
        hits = [(f, e) for f, root in docs for e in PATTERNS[pid](root)]
        files = {f for f, _ in hits}
        print(f'{pid}: {len(hits)} occurrences in {len(files)} examples')
        if show:
            for f, e in hits:
                print(f'   {f.parent.name}/{f.name}: {xpath_of(e)}')


if __name__ == '__main__':
    main()
