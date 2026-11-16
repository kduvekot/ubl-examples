"""Build analysis/worklist.md, analysis/worklist-decisions.md and analysis/worklist-assignments.csv from the
assignment table a.csv (assign.py), meta.py and decisions.py."""
import csv
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import meta  # noqa: E402
import decisions as dec  # noqa: E402
from cite import cite  # noqa: E402

REPO = Path('/home/user/ubl-examples')
OUT = REPO / 'analysis'
rows = list(csv.DictReader(open(HERE / 'a.csv', encoding='utf-8')))
for r in rows:
    r['key'] = meta.MERGE.get(r['cause'], r['cause'])
keys = {r['key'] for r in rows}
missing = keys - set(meta.C)
extra = set(meta.C) - keys
assert not missing, missing
assert not extra, extra

by = defaultdict(list)
for r in rows:
    by[r['key']].append(r)


def fnum(fid):
    m = re.match(r'(.+?)(?:/(\d+))?#F(\d+)$', fid)
    return (m.group(1), int(m.group(2) or 0), int(m.group(3)))


def order_key(k):
    m = meta.C[k]
    fo = meta.FLOW_ORDER.index(m['flow']) if m['stage'] == 6 else 0
    return (m['stage'], fo, -len(by[k]), k)


ordered = sorted(meta.C, key=order_key)
CID = {k: f'C{i:02d}' for i, k in enumerate(ordered, 1)}

# decisions: symbolic key -> causes
owner = defaultdict(list)
for k in ordered:
    dsym = meta.C[k]['decision']
    if dsym.startswith('D'):
        owner[dsym].append(k)
assert set(owner) <= set(dec.D), set(owner) - set(dec.D)
bulk_rows = [r for r in rows if not meta.C[r['key']]['decision'].startswith('D') and r['needs_decision'] == 'yes']
dcount = {s: sum(len(by[k]) for k in ks) for s, ks in owner.items()}
dcount['D47'] = len(bulk_rows)
groups = defaultdict(list)
for s, v in dec.D.items():
    groups[v['group']].append(s)
gorder = sorted([g for g in groups if g not in ('bulk', 'flows')], key=lambda g: -sum(dcount.get(s, 0) for s in groups[g])) + ['flows', 'bulk']
DNUM, n = {}, 0
for g in gorder:
    for s in sorted(groups[g], key=lambda s: -dcount.get(s, 0)):
        n += 1
        DNUM[s] = f'D{n}'
unused = [s for s in dec.D if s != 'D47' and s not in owner]
assert not unused, unused


def dlabel(k):
    d = meta.C[k]['decision']
    if d.startswith('D'):
        return f'owner: {DNUM[d]}'
    return d


def drefs(text):
    """Replace symbolic decision keys inside free text (e.g. 'D5x', 'D47') by their numbers."""
    return re.sub(r'\bD\d+x?\b', lambda m: DNUM.get(m.group(0), m.group(0)), text)


def cref(text):
    """Replace mnemonic cause keys written in capitals by their C-ids."""
    stop = {'GTIN', 'ISIC'}
    return re.sub(r'\b[A-Z]{4,}\b', lambda m: CID[m.group(0)] if m.group(0) in CID and m.group(0) not in stop
                  else m.group(0), text)


def finding_decision(r):
    d = meta.C[r['key']]['decision']
    if d.startswith('D'):
        return DNUM[d]
    if r['needs_decision'] == 'yes':
        return DNUM['D47']
    return ''


# ------------------------------------------------------------------ assignments CSV
asg = sorted(rows, key=lambda r: (CID[r['key']], fnum(r['finding'])))
with open(OUT / 'worklist-assignments.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['finding', 'source', 'severity', 'needs_decision', 'cause', 'decision'])
    for r in asg:
        w.writerow([r['finding'], r['source'], r['severity'], r['needs_decision'], CID[r['key']], finding_decision(r)])


# ------------------------------------------------------------------ helpers
def sev(ms):
    c = Counter(r['severity'] for r in ms)
    return c['High'], c['Medium'], c['Low']


def flist(ms):
    per = defaultdict(list)
    for r in sorted(ms, key=lambda r: fnum(r['finding'])):
        fl = r['flow']
        per[fl].append(r['finding'].split('/', 1)[1] if fl != 'consistency' else r['finding'])
    flows = sorted(per, key=lambda f: (f == 'consistency', f))
    if len(ms) > 60:
        parts = [f"{fl} ({len(per[fl])}): {', '.join(per[fl][:5])}{' …' if len(per[fl]) > 5 else ''}" for fl in flows]
        return '; '.join(parts) + '. Full list in `analysis/worklist-assignments.csv`.'
    return '; '.join(f"{fl}: {', '.join(per[fl])}" for fl in flows)


def examples(ms, n=2):
    """Typical findings: the most frequent title first, then other titles, High before Medium before Low."""
    tc = Counter(r['title'] for r in ms)
    picks = sorted(ms, key=lambda r: (-tc[r['title']], {'High': 0, 'Medium': 1, 'Low': 2}[r['severity']],
                                      r['flow'] == 'consistency', fnum(r['finding'])))
    seen_flows = set()
    out = []
    for r in picks:
        if r['flow'] in seen_flows:
            continue
        cs = cite(r['finding'], 1)
        if cs:
            seen_flows.add(r['flow'])
            out.append(f"{cs[0]} ({r['finding']})")
        if len(out) >= n:
            break
    return out


commit = subprocess.run(['git', '-C', str(REPO), 'rev-parse', '--short', 'HEAD'], capture_output=True, text=True).stdout.strip()
branch = subprocess.run(['git', '-C', str(REPO), 'branch', '--show-current'], capture_output=True, text=True).stdout.strip()
runs = sorted({r['run'] for r in rows})
total = len(rows)
H, M, L = sev(rows)
yes = sum(r['needs_decision'] == 'yes' for r in rows)
waiting = sum(1 for r in rows if finding_decision(r))
nflows = len({r['flow'] for r in rows if r['flow'] != 'consistency'})
nfiles = len({r['source'] for r in rows})

# ------------------------------------------------------------------ worklist.md
L_ = []
a = L_.append
a('# Worklist: the review findings by root cause')
a('')
a(f'Made on 2026-11-15 at commit {commit} (branch `{branch}`). Read: the 250 merged per-example reviews '
  f'(`world/examples/<flow>/*.llm-review.<run>.merged.md`, {len(runs) - 1} thorough runs from '
  f'`{runs[0]}` to `{runs[-2]}`) and the six topic files of the consistency review `20261114T2143Z-consistency` '
  f'(index `analysis/consistency-review.20261114T2143Z-consistency.md`), with `analysis/review-merge-decisions.md`, '
  '`analysis/codelist-decisions.md`, `note/src/03-world.md` and the generators for the source places.')
a('')
a(f'**{total} findings** in {nfiles} review files ({nflows} flows plus the consistency review): '
  f'**{H} High, {M} Medium, {L} Low**; {yes} are marked "Needs decision: yes". They are assigned to '
  f'**{len(ordered)} causes**; {waiting} findings wait on one of **{len(DNUM)} owner decisions** '
  '(`analysis/worklist-decisions.md`).')
a('')
a('How the assignment was made: `list_findings.py` turns every finding into one row of a table (title, severity, '
  'decision, the element names and values of its XPath lines). An ordered list of rules (patterns over title, '
  'elements and flow; first match wins) assigns a cause; about 150 findings that the rules put in the wrong place '
  'were corrected by hand after reading their titles, and the 32 consistency findings were assigned by reading. '
  'Each cause was then checked against the titles of all its findings, the options of every High finding and the '
  'full text of samples; the source place was found with grep in `tools/` and `world/`. Every finding has exactly '
  'one cause (`analysis/worklist-assignments.csv`).')
a('')
a('Reproduce the findings table:')
a('')
a('    python3 -I .claude/skills/ubl-example-review/scripts/list_findings.py    # writes .review/worklist/{findings,outside,refuted}.csv')
a('')
a('## How to read this')
a('')
a('- A **cause** is the place in the source (a builder, a default, a world-data value, a scenario) that produces '
  'findings. Fixing it resolves all its findings at once; a fixing session takes one cause (or one stage) at a time.')
a('- **Kind**: encoding (a shared builder writes the wrong element or value), master data (world/*.json), world rule '
  '(a rule the owner must set), cross-flow story, generator mechanism (times, numbers, references derived by method), '
  'flow story (one flow\'s scenario). No cause is only a missing build check; the checks are listed in stage 7.')
a('- **Decision**: "none" (the reviews and the merge decisions agree on the fix), "taken: …" (an earlier decision '
  'settles it), or "owner: D<n>" (see `analysis/worklist-decisions.md`). Findings marked "yes" inside a cause without '
  f'an owner decision are confirmed in bulk under {DNUM["D47"]}.')
a('- **Files** counts review files, one per example (plus the consistency topic files). Severity counts are per finding.')
a('- "Possibly not a problem" and "Conflict" notes mark findings that contradict the world story or an earlier '
  'decision. They stay assigned; the owner decides.')
a('- Example citations name the example file and the absolute XPath in one pair of backticks, followed by the quoted value; '
  'all of them are checked with `check_xpaths.py` and `check_values.py`.')
a('')
a('## Summary')
a('')
a('| Kind of cause | Causes | Findings | High | Waiting on an owner decision |')
a('|---|---:|---:|---:|---:|')
for kind in meta.KINDS:
    ks = [k for k in ordered if meta.C[k]['kind'] == kind]
    ms = [r for k in ks for r in by[k]]
    a(f'| {kind} | {len(ks)} | {len(ms)} | {sev(ms)[0]} | {sum(1 for r in ms if finding_decision(r))} |')
a(f'| **Total** | **{len(ordered)}** | **{total}** | **{H}** | **{waiting}** |')
a('')
a('| Cause | Title | Kind | Findings | Files | Flows | H/M/L | Decision | Source (short) |')
a('|---|---|---|---:|---:|---:|---|---|---|')


def short_src(s):
    m = re.findall(r'`([^`]+)`', s)
    files = []
    for x in m:
        if re.search(r'\.(py|json)$', x) or x.endswith('()'):
            files.append(x)
    return ', '.join(dict.fromkeys(files[:2])) or s[:40]


for k in ordered:
    ms = by[k]
    h, mm, l = sev(ms)
    flows = len({r['flow'] for r in ms if r['flow'] != 'consistency'})
    a(f"| {CID[k]} | {meta.C[k]['title']} | {meta.C[k]['kind']} | {len(ms)} | {len({r['source'] for r in ms})} | "
      f"{flows} | {h}/{mm}/{l} | {dlabel(k)} | {short_src(meta.C[k]['source'])} |")
a('')
a('## Order of work')
a('')
for st in range(1, 8):
    title, why = meta.STAGES[st]
    ks = [k for k in ordered if meta.C[k]['stage'] == st]
    ms = [r for k in ks for r in by[k]]
    a(f'### Stage {st}: {title}')
    a('')
    a(why)
    a('')
    if ks:
        a(f"Causes ({len(ks)}, {len(ms)} findings): {', '.join(CID[k] for k in ks)}.")
        a('')
    if st == 1:
        safe = [k for k in ks if not meta.C[k]['decision'].startswith('D') and 'Conflict' not in meta.C[k]['note']
                and meta.C[k]['deps'] == 'none' and 'depends on' not in meta.C[k]['note']]
        later = [k for k in ks if k not in safe]
        a(f"Safe to fix immediately (no decision, no dependency, no conflict): {', '.join(CID[k] for k in safe)}.")
        a('')
        if later:
            a(f"Fix after the named decision or cause: " + '; '.join(
                f"{CID[k]} ({drefs(meta.C[k]['note'] or meta.C[k]['deps'])[:90].rstrip()}…)" for k in later) + '.')
            a('')
        share = sum(len(by[k]) for k in ks)
        a(f'Stage 1 covers {share} of {total} findings ({100 * share / total:.0f} %).')
        a('')
    if st == 2:
        a('Decide first, then implement in this order: the language rules (they touch most files), the payment, '
          'customs and tax rules, the calendar, and the geography (which the sea voyage depends on). Item and '
          'catalogue data whose decision conflicts with an earlier one (FullnessIndicationCode, item data in documents) '
          'are here because the conflict must be settled before stage 1\'s item fixes are finished.')
        a('')
    if st == 4:
        a('The goods chain comes before the generator mechanisms because it changes lots, dates and possibly '
          'documents; the melt and serial fix follows the chosen lots.')
        a('')
    if st == 5:
        a('Issue times first (they decide document order), then numbering, prefixes and the execution ID (which '
          'depend on the final order), then references (which use the final numbers).')
        a('')
    if st == 6:
        for fl in meta.FLOW_ORDER:
            fk = [k for k in ks if meta.C[k]['flow'] == fl]
            if fk:
                a(f"- {fl}: {', '.join(CID[k] for k in fk)} ({sum(len(by[k]) for k in fk)} findings)")
        a('')
    if st == 7:
        checks = [
            ('Issue time after every actual event and every referenced document of the same flow', ['ISSUETIME', 'REFID']),
            ('Due date − issue date = the period of the cited terms ID', ['DUEDATE', 'CONTRACTTERMS']),
            ('Tax arithmetic per subtotal, including document-level allowances and charges', ['TAXTOTALS', 'UTILAMOUNTS']),
            ('Emission value = factor × base where both are given', ['EMISSION']),
            ('No `NoStatus`, no identity exchange rate, no pricing currency other than the price\'s', ['NOSTATUS', 'FXRATE']),
            ('Every document reference typed; every reference to an example resolves (flow_index "-> ?")', ['REFTYPE', 'REFID']),
            ('`ShippingOrderID` resolves to forwarding instructions of the flow', ['SHIPORDER']),
            ('Shipment gross weight ≥ goods + equipment tare', ['GROSSWT']),
            ('Waybill note and distribution list agree on the originals', ['ORIGINALS']),
            ('Customs offices of a declaration belong to the declaring country; national tariff only in its country', ['CUSTOMSDECL', 'TARIFF']),
            ('No customs-trader ID outside customs and cross-border documents; no share capital outside the issuer\'s own invoice', ['MASTERCOPY']),
            ('Issue weekday per issuer kind (after the calendar decision)', ['WEEKEND']),
            ('Document numbers rise per issuer with the issue timestamp; one prefix per party', ['NUMBERING', 'PREFIX']),
            ('Coordinates against stated distances and durations (after the map decision)', ['MAPSCALE', 'SEAVOYAGE']),
        ]
        for t, ck in checks:
            a(f"- {t}: guards {', '.join(CID[k] for k in ck)}.")
        a('')
a('Dependencies across stages: ' + '; '.join(
    f"{CID[k]} — {cref(drefs(meta.C[k]['deps']))}" for k in ordered if meta.C[k]['deps'] != 'none') + '.')
a('')
a('## Causes')
a('')
for k in ordered:
    m = meta.C[k]
    ms = by[k]
    h, mm, l = sev(ms)
    flows = {r['flow'] for r in ms if r['flow'] != 'consistency'}
    nyes = sum(r['needs_decision'] == 'yes' for r in ms)
    dl = dlabel(k)
    if not m['decision'].startswith('D') and nyes:
        dl += f' ({nyes} finding{"s" if nyes != 1 else ""} marked "yes" go{"" if nyes != 1 else "es"} to {DNUM["D47"]})'
    a(f"### {CID[k]} · {m['title']}")
    a(f"- Kind: {m['kind']} · Findings: {len(ms)} (High {h}, Medium {mm}, Low {l}) in "
      f"{len({r['source'] for r in ms})} file{'s' if len({r['source'] for r in ms}) != 1 else ''}, {len(flows)} flow{'s' if len(flows) != 1 else ''} · Needs decision: {dl}")
    ex = examples(ms)
    a(f"- What is wrong: {cref(m['wrong'])}" + (f" Example: {'; '.join(ex)}." if ex else ''))
    a(f"- Where it comes from: {m['source']}")
    a(f"- What must be true afterwards: {m['after']}")
    a(f"- Fix direction: {cref(drefs(m['fix']))}")
    a(f"- Depends on / blocks: {cref(drefs(m['deps']))}")
    if m['note']:
        a(f"- Note: {cref(drefs(m['note']))}")
    a(f"- Findings: {flist(ms)}")
    a('')
(OUT / 'worklist.md').write_text('\n'.join(L_) + '\n', encoding='utf-8')

# ------------------------------------------------------------------ worklist-decisions.md
D_ = []
a = D_.append
a('# Decisions for the owner')
a('')
a(f'These are the questions only the owner can answer before the causes of `analysis/worklist.md` can be fixed. '
  f'There are **{len(DNUM)} decisions**; {waiting} of the {total} findings wait on one of them, in '
  f'{len(owner)} causes (plus the bulk confirmation {DNUM["D47"]}). The 21 "needs decision" consistency findings, '
  'the "Cannot be told from the documents" questions of the six topic files and the per-example "yes" findings are '
  'folded in by cause: a cause with many "yes" findings is one decision, and the flow stories are one decision per '
  'flow. Where the world story (`note/src/03-world.md`) or an earlier decision (`analysis/codelist-decisions.md`) '
  'already says something, it is quoted; several findings contradict them, and those conflicts are the first thing '
  'to settle.')
a('')
a('The decisions are grouped; a group is meant to be taken together. The world-level groups come first, ordered by '
  'the number of findings they unblock, and within a group the decisions are ordered the same way. The flow decisions '
  'come after them although some are large (the tender alone holds 210 findings), because they build on the world '
  'rules (payment terms, tax, customs, the goods chain); the bulk confirmation is last.')
a('')
for g in gorder:
    syms = sorted(groups[g], key=lambda s: -dcount.get(s, 0))
    gsum = sum(dcount.get(s, 0) for s in syms)
    a(f'## {dec.GROUPS[g]} ({gsum} findings)')
    a('')
    for s in syms:
        v = dec.D[s]
        cs = owner.get(s, [])
        a(f"### {DNUM[s]} · {drefs(v['question'])}")
        if s == 'D47':
            bc = Counter(CID[r['key']] for r in bulk_rows)
            why = (f"{len(bulk_rows)} findings marked \"yes\" in causes without an owner decision: "
                   + ', '.join(f'{c} ({n})' for c, n in sorted(bc.items())) + '.')
        else:
            why = (f"Cause{'s' if len(cs) > 1 else ''} {', '.join(CID[k] + ' ' + meta.C[k]['title'] for k in cs)}; {dcount[s]} finding{'s' if dcount[s] != 1 else ''} "
                   f"({sum(r['needs_decision'] == 'yes' for k in cs for r in by[k])} marked \"yes\").")
        a(f'- Why it matters: {why}')
        a(f"- What the documents say now: {cref(drefs(v['now']))}")
        a('- Options:')
        for o in v['options']:
            a(f'  - {drefs(o)}')
        a(f"- Recommendation: {cref(drefs(v['rec']))}")
        a(f"- Related: {drefs(v['related'])}")
        a('')
(OUT / 'worklist-decisions.md').write_text('\n'.join(D_) + '\n', encoding='utf-8')
print('causes', len(ordered), 'decisions', len(DNUM), 'waiting', waiting, 'total', total)
for s in sorted(DNUM, key=lambda s: int(DNUM[s][1:])):
    print(DNUM[s], s, dcount.get(s))
