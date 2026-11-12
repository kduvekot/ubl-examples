"""Run ID and the version header of a review: which XML, which commit, which skill, which register.

usage:
  python3 -I review_meta.py run-id <kind>          print a new run ID, e.g. 20261112T1430Z-thorough
  python3 -I review_meta.py header <run-id> <example.xml>
                                                   print the "Reviewed version" block for a review

The run ID is the UTC start time of the run plus its kind (quick, thorough, manual, …). Use one run
ID for every example reviewed in the same run.
"""
import datetime
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ubl_model import EXAMPLES, MODEL_SHA256, REPO  # noqa: E402

SKILL = Path(__file__).resolve().parent.parent
REGISTER = EXAMPLES / 'recurring.llm-review.md'


def git(*args):
    r = subprocess.run(['git', '-C', str(REPO), *args], capture_output=True, text=True)
    return r.stdout.strip()


def commit_line(fmt_rev, path=None):
    args = ['log', '-1', '--format=%h %cs %s', fmt_rev] + (['--', str(path)] if path else [])
    return git(*args) or '(not committed)'


def state(path):
    """'committed' / 'modified, not committed' / 'not tracked' for a path."""
    if not git('ls-files', '--', str(path)):
        return 'not tracked'
    return 'modified, not committed' if git('status', '--porcelain', '--', str(path)) else 'committed'


def header(run_id, xml):
    xml = Path(xml).resolve()
    rel = xml.relative_to(REPO)
    lines = [
        '## Reviewed version',
        f'- Run: `{run_id}`',
        f"- Example: `{rel}`, Git blob `{git('hash-object', str(xml))}` ({state(xml)})",
        f"- Last commit changing the example: {commit_line('HEAD', xml)}",
        f"- Checkout: branch `{git('rev-parse', '--abbrev-ref', 'HEAD')}`, commit {commit_line('HEAD')}",
        f"- Skill: `.claude/skills/ubl-example-review`, last commit {commit_line('HEAD', SKILL)}"
        f" ({state(SKILL / 'SKILL.md')})",
    ]
    if REGISTER.exists():
        lines.append(f"- Register: `{REGISTER.relative_to(REPO)}`, Git blob "
                     f"`{git('hash-object', str(REGISTER))}` ({state(REGISTER)})")
    else:
        lines.append('- Register: none')
    lines.append(f'- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 {MODEL_SHA256[:8]}…{MODEL_SHA256[-7:]})')
    return '\n'.join(lines)


def main():
    if len(sys.argv) == 3 and sys.argv[1] == 'run-id':
        now = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%MZ')
        print(f'{now}-{sys.argv[2]}')
    elif len(sys.argv) == 4 and sys.argv[1] == 'header':
        print(header(sys.argv[2], sys.argv[3]))
    else:
        sys.exit(__doc__)


if __name__ == '__main__':
    main()
