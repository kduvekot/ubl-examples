"""Every review of an example, or of every example of a flow: run, part, findings and the version
reviewed. For whoever works through the reviews, so that no review is overlooked.

usage: python3 -I list_reviews.py <flow>/<NN-DocumentType> | <flow>

Per example: one line per review file, oldest run first, with the run ID, the part, the number of
findings by severity, the number of entries under "Considered and refuted", "Refuted in the merge"
and "Outside this review", and whether the example has changed since that review (its Git blob now
against the blob the review records).
"""
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ubl_model import EXAMPLES, REPO  # noqa: E402

FINDING = re.compile(r'^### \S+#F\d+ · (High|Medium|Low) ·', re.M)
OLD_FINDING = re.compile(r'^### \d+\. .*\((High|Medium|Low)\b', re.M)  # manual reviews of 2026-11-12
SECTION = re.compile(r'^## (.+?)\s*(?:\(.*\))?$', re.M)


def blob(path):
    return subprocess.run(['git', '-C', str(REPO), 'hash-object', str(path)],
                          capture_output=True, text=True).stdout.strip()


def entries(text, title):
    """Number of entries (### headings or - bullets) in a ## section."""
    m = re.search(rf'^## {re.escape(title)}\b.*?$(.*?)(?=^## |\Z)', text, re.M | re.S)
    if not m:
        return 0
    body = m.group(1)
    heads = len(re.findall(r'^### ', body, re.M))
    return heads or len(re.findall(r'^- ', body, re.M))


def describe(review, now_blob):
    text = review.read_text(encoding='utf-8')
    name = review.name.split('.llm-review.', 1)[1][:-3]
    run, _, part = name.partition('.')
    sev = {s: 0 for s in ('High', 'Medium', 'Low')}
    for s in FINDING.findall(text) or OLD_FINDING.findall(text):
        sev[s] += 1
    m = re.search(r'Git blob `([0-9a-f]{40})`', text)
    state = 'version unknown' if not m else ('same version' if m.group(1) == now_blob
                                             else 'example changed since')
    extra = []
    for title, label in (('Considered and refuted', 'refuted'), ('Refuted in the merge', 'refuted in merge'),
                         ('Outside this review', 'outside'), ('Recurring patterns', 'pattern lines')):
        n = entries(text, title)
        if n:
            extra.append(f'{n} {label}')
    return (f"  {run:28} {part or 'single':10} H{sev['High']} M{sev['Medium']} L{sev['Low']}"
            f"{'  · ' + ', '.join(extra) if extra else ''}  · {state}")


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    target = sys.argv[1].removesuffix('.xml')
    if '/' in target:
        xmls = [EXAMPLES / f'{target}.xml']
    else:
        xmls = sorted((EXAMPLES / target).glob('*.xml'))
    if not xmls or not xmls[0].exists():
        sys.exit(f'no example {target}')
    for xml in xmls:
        reviews = sorted(xml.parent.glob(f'{xml.stem}.llm-review.*.md'))
        print(f'{xml.parent.name}/{xml.name}: {len(reviews)} review(s)')
        now = blob(xml)
        for r in reviews:
            print(describe(r, now))


if __name__ == '__main__':
    main()
