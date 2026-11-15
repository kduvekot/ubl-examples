"""Mechanical cross-flow hits from the tables of extract_tables.py: exact, no judgement.

usage: python3 -I check_consistency.py [<tablesdir>]      (default: <repo>/.review/tables/)

Prints, per check, the number of hits and every hit with the places it comes from
(`flow/file:xpath`), plus summary lines per kind where a check has several kinds. A hit is not a
finding: it only shows where values differ that a reviewer should look at. Comparisons are exact
string comparisons of the table cells; empty cells are ignored, and so are cells that hold nothing but
'-' placeholders and ' | ' separators: an empty identifier or name is not "the same identifier" and is
never used as the key of a group. Exit code is always 0.

Checks:
  1 same-id-different-thing   the same identifier value + scheme on things with different names
                              (parties, items, transport means, equipment, financial accounts)
  2 party-name-variants       the same party name with different values in a column of parties.csv
  3 item-variants             the same item main identifier with different descriptive values
  4 document-id-repeats       two examples with the same document ID and issuer; repeated UUIDs
  5 numbering-vs-date         per issuer, document type and ID pattern, numbers out of date order
  6 reference-mismatch        references to an example's ID with another issue date, UUID or type
                              (a DocumentTypeCode passes if it equals one of the example's *TypeCode
                              values or its root element name)
  7 exchange-rate-variants    the same currency pair and date with different rates
  8 person-variants           the same contact/person name under different parties or with
                              different job title, department, telephone or mail
  9 period-end-before-start   periods whose end is before their start
 10 mention-before-issue      a row of references.csv or document_id_mentions.csv whose matched example
                              was issued after the citing document (date only unless both carry a time;
                              skipped if either side has no issue date; for several matches, the earliest)
"""
import csv
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
DEFAULT = REPO / '.review' / 'tables'


def load(d, name):
    with open(d / f'{name}.csv', encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def blank(s):
    """True for an empty cell or one with nothing but '-' placeholders, ' | ' separators and spaces."""
    return not s.strip('-| \t')


def keyed(ident, key):
    """The group `key`, or '' (= no group) if the identifier or name `ident` in it is blank."""
    return '' if blank(ident) else key


def where(r, xpath=None):
    return f'{r["flow"]}/{r["file"]}:{xpath or r["xpath"]}'


class Report:
    def __init__(self):
        self.checks = []

    def start(self, name, title):
        self.cur = {'name': name, 'title': title, 'hits': [], 'kinds': defaultdict(int)}
        self.checks.append(self.cur)

    def hit(self, kind, text, places):
        self.cur['hits'].append((kind, text, places))
        self.cur['kinds'][kind] += 1

    def print(self):
        print('# check_consistency: mechanical hits (not findings)\n')
        for ch in self.checks:
            print(f'{ch["name"]}: {len(ch["hits"])} hit(s)  {ch["title"]}')
        for ch in self.checks:
            print(f'\n== {ch["name"]}: {len(ch["hits"])} hit(s)  {ch["title"]}')
            if len(ch['kinds']) > 1 or len(ch['hits']) > 20:
                for k, n in sorted(ch['kinds'].items(), key=lambda x: (-x[1], x[0])):
                    print(f'   summary {k}: {n}')
            for kind, text, places in ch['hits']:
                print(f'-- [{kind}] {text}')
                for variant, ps in places:
                    print(f'     {variant}')
                    for p in ps:
                        print(f'        {p}')


def variants(rows, key, value, rep, kind, label, min_variants=2, value_label=None):
    """Group rows by key(r); where value(r) takes >= 2 distinct non-empty values, report a hit."""
    groups = defaultdict(lambda: defaultdict(list))
    for r in rows:
        k = key(r)
        v = value(r)
        if k and v and not blank(v):
            groups[k][v].append(where(r))
    for k in sorted(groups):
        vs = groups[k]
        if len(vs) >= min_variants:
            rep.hit(kind, f'{label} {k!r}: {len(vs)} variants', [(f'{v!r}', ps) for v, ps in sorted(vs.items())])


def check_same_id(d, rep):
    rep.start('1 same-id-different-thing', 'same identifier value + scheme, different names')
    pids = load(d, 'party_ids')
    variants(pids, lambda r: keyed(r['value'], (r['value'], r['scheme_id'])), lambda r: r['party_name'], rep, 'party',
             'party identifier (value, scheme)')
    iids = load(d, 'item_ids')
    variants(iids, lambda r: keyed(r['value'], (r['kind'], r['value'], r['scheme_id'])), lambda r: r['item_name'], rep, 'item',
             'item identifier (kind, value, scheme)')
    tm = load(d, 'transport_means')
    for col, scheme, desc in (('vessel_id', 'vessel_id_scheme', ('vessel_name', 'type_code', 'registration_nationality_id')),
                              ('mmsi', None, ('vessel_name',)), ('call_sign', None, ('vessel_name',)),
                              ('license_plate', 'license_plate_scheme', ('type_code', 'registration_nationality_id')),
                              ('trailer_plate', None, ('type_code',)), ('train_id', None, ('type_code',)),
                              ('rail_car_id', 'rail_car_id_scheme', ('type_code',)),
                              ('aircraft_id', 'aircraft_id_scheme', ('type_code', 'registration_nationality_id'))):
        variants(tm, lambda r: keyed(r[col], (r[col], r[scheme]) if scheme else r[col]),
                 lambda r: ' / '.join(f'{x}={r[x]}' for x in desc if r[x]), rep, f'transport_means.{col}',
                 f'{col}')
    eq = load(d, 'transport_equipment')
    variants(eq, lambda r: keyed(r['id'], (r['id'], r['id_scheme'])),
             lambda r: ' / '.join(f'{x}={r[x]}' for x in ('type_code', 'size_type', 'tare_weight') if r[x]),
             rep, 'equipment', 'equipment (id, scheme)')
    fa = load(d, 'financial_accounts')
    variants(fa, lambda r: keyed(r['id'], (r['id'], r['id_scheme'])),
             lambda r: ' / '.join(f'{x}={r[x]}' for x in ('name', 'currency', 'institution_id', 'branch_id') if r[x]),
             rep, 'account', 'financial account (id, scheme)')


PARTY_SKIP = {'flow', 'file', 'xpath', 'element', 'parent', 'role_path', 'role', 'name', 'contacts', 'role_extras',
              'other', 'party_role', 'party_name', 'line_id', 'entity', 'entity_xpath'}


def check_party_names(d, rep):
    rep.start('2 party-name-variants', 'same party name (exact PartyName cell), different values per column')
    rows = load(d, 'parties')
    cols = [c for c in rows[0] if c not in PARTY_SKIP]
    for col in cols:
        variants(rows, lambda r: r['name'], lambda r: r[col], rep, col, f'party {col} for name')


ITEM_COLS = ['name', 'description', 'brand', 'model', 'commodity_code', 'commodity_code_list', 'item_classification',
             'item_classification_list', 'nature_code', 'cargo_type', 'origin_country', 'dimensions', 'hazardous',
             'standard_id', 'manufacturers_id']


def check_items(d, rep):
    rep.start('3 item-variants', 'same item main identifier (Kind=value), different values per column')
    rows = load(d, 'items')
    for col in ITEM_COLS:
        variants(rows, lambda r: r['main_id'], lambda r: r[col], rep, col, f'item {col} for')


def check_documents(d, rep):
    rep.start('4 document-id-repeats', 'same document ID from the same issuer; repeated UUIDs')
    docs = load(d, 'documents')
    g = defaultdict(list)
    for r in docs:
        if r['id'] and not blank(r['issuer']):
            g[(r['issuer'], r['id'])].append(r)
    for k in sorted(g):
        if len(g[k]) > 1:
            rep.hit('same issuer and ID', f'issuer {k[0]!r}, ID {k[1]!r}: {len(g[k])} examples',
                    [(f'{r["root"]} issued {r["issue_timestamp"]}'
                      + (f' VersionID {r["version_id"]}' if r['version_id'] else ''), [where(r)]) for r in g[k]])
    u = defaultdict(list)
    for r in docs:
        if r['uuid']:
            u[r['uuid']].append(r)
    for k in sorted(u):
        if len(u[k]) > 1:
            rep.hit('repeated UUID', f'UUID {k}: {len(u[k])} examples',
                    [(f'{r["root"]} {r["id"]}', [where(r)]) for r in u[k]])


def numkey(s):
    return tuple(int(x) for x in re.findall(r'\d+', s))


def comparable(a, b):
    """The two timestamps cut to a common precision (date only unless both carry a time)."""
    if 'T' in a and 'T' in b:
        return a, b
    return a[:10], b[:10]


def check_numbering(d, rep):
    rep.start('5 numbering-vs-date', 'per issuer + root + ID pattern (digits as #): number order vs issue order')
    docs = load(d, 'documents')
    g = defaultdict(list)
    for r in docs:
        if r['id'] and r['issue_timestamp'] and re.search(r'\d', r['id']) and not blank(r['issuer']):
            g[(r['issuer'], r['root'], re.sub(r'\d', '#', r['id']))].append(r)
    for k in sorted(g):
        rs = sorted(g[k], key=lambda r: (numkey(r['id']), r['id']))
        for a, b in zip(rs, rs[1:]):
            x, y = comparable(a['issue_timestamp'], b['issue_timestamp'])
            if numkey(a['id']) < numkey(b['id']) and y < x:
                rep.hit('number order contradicts issue order',
                        f'issuer {k[0]!r} {k[1]} {k[2]}: {a["id"]} issued {a["issue_timestamp"]}, '
                        f'later number {b["id"]} issued {b["issue_timestamp"]}',
                        [(a['id'], [where(a)]), (b['id'], [where(b)])])


def check_references(d, rep):
    rep.start('6 reference-mismatch', 'reference to an example\'s document ID with another issue date, UUID or type code')
    docs = load(d, 'documents')
    by_id = defaultdict(list)
    for r in docs:
        by_id[r['id']].append(r)
    for r in load(d, 'references'):
        targets = [t for t in by_id.get(r['id'], []) if f'{t["flow"]}/{t["file"]}' != f'{r["flow"]}/{r["file"]}']
        if not r['id'] or not targets:
            continue
        for field, get in (('issue_date', lambda t: t['issue_date']), ('uuid', lambda t: t['uuid'])):
            if r[field] and all(get(t) != r[field] for t in targets):
                rep.hit(f'{field} differs', f'{r["element"]} {r["id"]!r} states {field} {r[field]!r}',
                        [('reference', [where(r)])] +
                        [(f'example states {get(t)!r}', [where(t)]) for t in targets])
        if r['type_code']:
            def codes(t):
                return {x.split('=', 1)[1] for x in t['type_codes'].split(' | ') if '=' in x}
            if all(r['type_code'] not in codes(t) | {t['root']} for t in targets):
                rep.hit('type code differs', f'{r["element"]} {r["id"]!r} states DocumentTypeCode {r["type_code"]!r}',
                        [('reference', [where(r)])] +
                        [(f'example {t["root"]} states {t["type_codes"] or "no type code"!r}', [where(t)])
                         for t in targets])


def check_rates(d, rep):
    rep.start('7 exchange-rate-variants', 'same source/target currency and date, different rate or operator')
    rows = load(d, 'exchange_rates')
    variants(rows, lambda r: (r['source_currency'], r['target_currency'], r['date'])
             if r['date'] and not blank(r['source_currency']) and not blank(r['target_currency']) else '',
             lambda r: f'rate {r["rate"]} operator {r["operator"] or "-"} base {r["source_base_rate"] or "-"}/'
                       f'{r["target_base_rate"] or "-"}', rep, 'same pair and date', '(source, target, date)')
    undated = [r for r in rows if not r['date']]
    variants(undated, lambda r: keyed(r['source_currency'] + r['target_currency'], (r['source_currency'], r['target_currency'])),
             lambda r: f'rate {r["rate"]} operator {r["operator"] or "-"}', rep, 'same pair, no date',
             '(source, target) without date')


def check_persons(d, rep):
    rep.start('8 person-variants', 'same contact/person name under different parties or with different details')
    rows = load(d, 'contacts')
    for r in rows:
        r['_name'] = r['name'] or ' '.join(x for x in (r['first_name'], r['middle_name'], r['family_name']) if x)
    variants(rows, lambda r: r['_name'], lambda r: r['party_name'], rep, 'party', 'name under parties')
    for col in ('job_title', 'department', 'telephone', 'mail'):
        variants(rows, lambda r: r['_name'], lambda r: r[col], rep, col, f'{col} for name')


def check_periods(d, rep):
    rep.start('9 period-end-before-start', 'end before start (date only unless both carry a time; '
                                           'time of day only where a side has no date)')
    for r in load(d, 'periods'):
        if r['start_date'] and r['end_date']:
            a, b = comparable(r['start'], r['end'])
        elif r['start_time'] and r['end_time']:
            a, b = r['start_time'], r['end_time']
        else:
            continue
        if b < a:
            rep.hit('end before start', f'{r["element"]} {r["start"]} -> {r["end"]}', [('period', [where(r)])])


def check_mentions(d, rep):
    rep.start('10 mention-before-issue', 'cited example issued after the citing document (references.csv and '
                                         'document_id_mentions.csv; date only unless both carry a time)')
    issue = {f'{r["flow"]}/{r["file"]}': r['issue_timestamp'] for r in load(d, 'documents')}
    for table in ('references', 'document_id_mentions'):
        for r in load(d, table):
            own = issue.get(f'{r["flow"]}/{r["file"]}', '')
            matches = [m for m in r['example_matches'].split(' | ') if m and issue.get(m)]
            if not own or not matches:
                continue
            first_m = min(matches, key=lambda m: issue[m])  # the earliest version
            a, b = comparable(own, issue[first_m])
            if b > a:
                rep.hit(table, f'{r["element"]} {r.get("value") or r["id"]!r} cites an example issued later',
                        [(f'citing document issued {own}', [where(r)]),
                         (f'cited example issued {issue[first_m]}', [first_m])])


def main():
    d = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    if not (d / 'documents.csv').exists():
        print(f'no tables in {d}: run extract_tables.py first')
        sys.exit(0)
    rep = Report()
    for f in (check_same_id, check_party_names, check_items, check_documents, check_numbering, check_references,
              check_rates, check_persons, check_periods, check_mentions):
        f(d, rep)
    try:
        rep.print()
    except BrokenPipeError:  # output piped into head etc.
        sys.stderr.close()
    sys.exit(0)


if __name__ == '__main__':
    main()
