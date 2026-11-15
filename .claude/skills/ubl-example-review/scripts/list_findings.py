"""Every finding of the merged per-example reviews and of the cross-flow consistency review, as tables.

usage: python3 -I list_findings.py [<outdir>]      (default <repo>/.review/worklist/, git-ignored)

Reads every `world/examples/<flow>/*.llm-review.<run-id>.merged.md` and every
`analysis/consistency-review.<run-id>.<topic>.md` (not the index) and writes:

  findings.csv  one row per finding (### <flow>/<NN>#F<n> or ### <topic>#F<n> under "## Findings"):
                source, flow, example, run, finding id, severity, title, needs decision (yes/no),
                number of XPath lines, the distinct element names at the end of the cited XPaths,
                the first three cited values, the From:/Seen in reviews: line, the finding's length
  outside.csv   every entry (top-level bullet) of "## Outside this review"
  refuted.csv   every entry of "## Considered and refuted" (bullets) and "## Refuted in the merge"
                (### headings): source, kind, entry id, title or the first 150 characters

For consistency findings the flow column is `consistency` and the example column the topic.
Rows are sorted by flow, example and finding number, so the output is the same on every run.

The parser checks itself: per file, the number of findings it read must equal the number of
`### <flow>/<NN>#F<n>` (or `### <topic>#F<n>`) headings in the file; every finding must have a
severity and a "Needs decision" value; the finding IDs must name the file's flow and example and be
unique. A file that fails is reported (and the script exits 1) instead of being skipped.
"""
import csv
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ubl_model import EXAMPLES, REPO  # noqa: E402

ANALYSIS = REPO / 'analysis'
SECTION = re.compile(r'^## (.+?)\s*$', re.M)
HEADING = re.compile(r'^### (\S+?)#F(\d+) · (High|Medium|Low) · (.*)$')
ANY_FINDING_HEADING = re.compile(r'^### [\w-]+(?:/\d+)?#F\d+\b', re.M)
XPATH_LINE = re.compile(r'^- XPath: (.*)$', re.M)
CITE = re.compile(r'`((?:[\w.-]+/)?[\w.-]+\.xml:)?(/[A-Za-z][^`\s]*)`(?:\s*=\s*`([^`]*)`)?')
DECISION = re.compile(r'^- Needs decision: (yes|no)\b', re.M)
FROM = re.compile(r'^- (From|Seen in reviews): (.*)$', re.M)
SEV_ORDER = {'High': 0, 'Medium': 1, 'Low': 2}


def sections(text):
    """{title: body} of the ## sections (title without a trailing parenthesis)."""
    out = {}
    heads = list(SECTION.finditer(text))
    for i, m in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        title = re.sub(r'\s*\(.*\)$', '', m.group(1)).strip()
        out[title] = text[m.end():end]
    return out


def blocks(body):
    """The ### blocks of a section: (heading line, block text including the heading)."""
    parts = re.split(r'(?=^### )', body, flags=re.M)
    return [(p.splitlines()[0], p.rstrip('\n')) for p in parts if p.startswith('### ')]


def bullets(body):
    """The top-level bullets of a section, each with its continuation lines, joined to one line."""
    out = []
    for line in body.splitlines():
        if line.startswith('- '):
            out.append(line[2:].strip())
        elif out and line.startswith((' ', '\t')) and line.strip():
            out[-1] += ' ' + line.strip()
        elif out and not line.strip():
            out.append(None)  # a blank line ends the bullet
    return [b for b in out if b]


def last_element(path):
    step = path.rstrip('/').split('/')[-1]
    step = re.sub(r'\[.*?\]', '', step)
    return step.split(':')[-1]


def one_line(s, n=None):
    s = re.sub(r'\s+', ' ', s).strip()
    return s if n is None or len(s) <= n else s[:n].rstrip() + '…'


def source_meta(md):
    """(flow, example, run, kind) of a review file."""
    if md.parent == ANALYSIS:
        m = re.match(r'consistency-review\.(.+)\.([a-z]+)\.md$', md.name)
        return 'consistency', m.group(2), m.group(1), 'consistency'
    stem, _, rest = md.name.partition('.llm-review.')
    return md.parent.name, stem, rest[:-len('.merged.md')], 'merged'


def parse(md, problems):
    text = md.read_text(encoding='utf-8')
    flow, example, run, kind = source_meta(md)
    rel = md.relative_to(REPO).as_posix()
    secs = sections(text)
    want_prefix = example if kind == 'consistency' else f'{flow}/{example[:2]}'
    findings, outside, refuted = [], [], []
    if 'Findings' not in secs:
        problems.append(f'{rel}: no "## Findings" section')
    for head, block in blocks(secs.get('Findings', '')):
        m = HEADING.match(head)
        if not m:
            problems.append(f'{rel}: finding heading not understood: {head[:100]}')
            continue
        prefix, num, sev, title = m.groups()
        if prefix != want_prefix:
            problems.append(f'{rel}: finding {prefix}#F{num} does not name this file ({want_prefix})')
        dec = DECISION.search(block)
        if not dec:
            problems.append(f'{rel}: {prefix}#F{num} has no "Needs decision: yes|no"')
        xlines = XPATH_LINE.findall(block)
        elems, values = [], []
        for line in xlines:
            for c in CITE.finditer(line):
                e = last_element(c.group(2))
                if e and e not in elems:
                    elems.append(e)
                if c.group(3) is not None and len(values) < 3:
                    values.append(c.group(3))
        frm = FROM.search(block)
        findings.append({
            'source': rel, 'flow': flow, 'example': example, 'run': run,
            'finding': f'{prefix}#F{num}', 'severity': sev, 'title': title.strip(),
            'needs_decision': dec.group(1) if dec else '',
            'xpath_lines': len(xlines), 'elements': ' '.join(elems),
            'values': ' | '.join(values), 'from': one_line(frm.group(2)) if frm else '',
            'length': len(block), '_n': int(num)})
    expected = len(ANY_FINDING_HEADING.findall(text))
    if expected != len(findings):
        problems.append(f'{rel}: {expected} finding headings in the file, {len(findings)} parsed')
    for i, b in enumerate(bullets(secs.get('Outside this review', '')), 1):
        outside.append({'source': rel, 'flow': flow, 'example': example, 'run': run,
                        'entry': f'{want_prefix}#O{i}', 'text': one_line(b)})
    for i, b in enumerate(bullets(secs.get('Considered and refuted', '')), 1):
        refuted.append({'source': rel, 'flow': flow, 'example': example, 'kind': 'considered',
                        'entry': f'{want_prefix}#R{i}', 'title': one_line(b, 150)})
    for head, block in blocks(secs.get('Refuted in the merge', '')):
        m = re.match(r'^### (\S+) · (?:(High|Medium|Low) · )?(.*)$', head)
        refuted.append({'source': rel, 'flow': flow, 'example': example, 'kind': 'merge',
                        'entry': f'{want_prefix}:{m.group(1)}' if m else want_prefix,
                        'title': one_line(m.group(3) if m else head[4:], 150)})
    return findings, outside, refuted


def write(path, rows, fields):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore', lineterminator='\n')
        w.writeheader()
        w.writerows(rows)


def main():
    if len(sys.argv) > 2:
        sys.exit(__doc__)
    out = Path(sys.argv[1]) if len(sys.argv) == 2 else REPO / '.review' / 'worklist'
    out.mkdir(parents=True, exist_ok=True)
    files = sorted(EXAMPLES.glob('*/*.llm-review.*.merged.md'))
    files += sorted(p for p in ANALYSIS.glob('consistency-review.*.*.md'))
    problems, findings, outside, refuted = [], [], [], []
    for md in files:
        f, o, r = parse(md, problems)
        findings += f
        outside += o
        refuted += r
    findings.sort(key=lambda r: (r['flow'] == 'consistency', r['flow'], r['example'], r['_n']))
    dup = [k for k, n in Counter(r['finding'] for r in findings).items() if n > 1]
    for k in dup:
        problems.append(f'finding ID {k} occurs more than once')
    for r in findings:
        if not r['severity'] or r['needs_decision'] not in ('yes', 'no'):
            problems.append(f"{r['finding']}: severity or decision missing")
    write(out / 'findings.csv', findings,
          ['source', 'flow', 'example', 'run', 'finding', 'severity', 'title', 'needs_decision',
           'xpath_lines', 'elements', 'values', 'from', 'length'])
    write(out / 'outside.csv', outside, ['source', 'flow', 'example', 'run', 'entry', 'text'])
    write(out / 'refuted.csv', refuted, ['source', 'flow', 'example', 'kind', 'entry', 'title'])

    flows = sorted({r['flow'] for r in findings}, key=lambda f: (f == 'consistency', f))
    print(f"{'flow':14} {'files':>5} {'High':>5} {'Medium':>6} {'Low':>5} {'total':>6} {'decision':>8}")
    tot = Counter()
    for fl in flows:
        rows = [r for r in findings if r['flow'] == fl]
        c = Counter(r['severity'] for r in rows)
        d = sum(r['needs_decision'] == 'yes' for r in rows)
        nfiles = len({r['source'] for r in rows})
        print(f"{fl:14} {nfiles:5} {c['High']:5} {c['Medium']:6} {c['Low']:5} {len(rows):6} {d:8}")
        tot.update(c)
        tot['decision'] += d
    print(f"{'total':14} {len(files):5} {tot['High']:5} {tot['Medium']:6} {tot['Low']:5} {len(findings):6} "
          f"{tot['decision']:8}")
    print(f'{len(outside)} outside-this-review entries, {len(refuted)} refuted entries '
          f"({sum(r['kind'] == 'merge' for r in refuted)} refuted in the merge); written to {out}")
    if problems:
        print(f'PARSER PROBLEMS ({len(problems)}):')
        for p in problems:
            print('  ' + p)
        sys.exit(1)
    print(f'parser check passed for all {len(files)} files: findings per file = finding headings, '
          'every finding has a severity and a decision value, IDs unique')


if __name__ == '__main__':
    main()
