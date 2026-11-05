#!/usr/bin/env python3
"""Rebuild the history of the OASIS UBL sample documents as git commits.

Input
  history/manifest.json   written by crawl_oasis.py (what each stage published)
  --cache DIR             the files downloaded by crawl_oasis.py
  --oasis-repo DIR        optional clone of https://github.com/oasis-tcs/ubl,
                          used for intermediate edits between two stages

Output
  A branch (--branch, default "examples-history") in the repository given by
  --repo. Without --base the branch starts with a small root commit dated on
  the formation of the OASIS UBL TC (17 October 2001) that adds README.md.
  With --base it continues from that commit instead. The branch gets:

  * one commit per document change (add, modify or delete one file in xml/);
  * for changes made in the OASIS GitHub repository between two published
    stages, one commit per GitHub commit and file, with the original author,
    date and message;
  * for every other change, a commit dated on the stage's publication date,
    authored by "OASIS UBL TC";
  * per stage, one commit that adds the stage's release notes to README.md,
    also for stages without changes, with an annotated tag (e.g.
    "os-UBL-2.1"); its xml/ folder equals what that stage published.

The build is deterministic: commit and tag dates come from the sources and
the committer identity is fixed, so the same inputs give the same hashes.
--committer and --sign change the committer and add signatures (as used for
the published branch); authors, dates, messages and trees stay the same.

Usage
  python3 tools/build_history.py --cache DIR [--oasis-repo DIR] [--repo .]
"""
import argparse
import datetime
import hashlib
import json
import os
import subprocess
import sys

BASE_URL = "https://docs.oasis-open.org/ubl/"
GITHUB = "https://github.com/oasis-tcs/ubl/commit/"
TC_NAME = "OASIS UBL TC"
BUILDER = ["ubl-examples history builder", ""]  # committer; see --committer
SIGN = []  # ["-S"] with --sign
# Stage publication dates where the files' server timestamps are older than
# the stage itself (the files were republished unchanged).
DATE_OVERRIDES = {"os-UBL-2.0-update": "2008-05-29T12:00"}
STAGE_TIME = "12:00:00 +0000"
# Formation of the OASIS UBL TC, announced by OASIS on 17 October 2001:
# https://www.oasis-open.org/news/pr/oasis-members-form-technical-committee-to-develop-universal-business-language/
TC_START = "2001-10-17T12:00:00 +0000"
STAGE_NAMES = {"prd": "Public Review Draft", "csd": "Committee Specification Draft",
               "csprd": "Committee Specification Public Review Draft", "cs": "Committee Specification",
               "cos": "Candidate OASIS Standard", "os": "OASIS Standard"}
README_HEAD = """# ubl-examples

A set of validated sample documents for UBL (Universal Business Language,
OASIS Standard and ISO/IEC 19845).

`xml/` holds the sample documents published by the OASIS UBL Technical
Committee with each release of UBL 2.x, starting with UBL 2.0. Each release
below is tagged with the name of its directory on
<https://docs.oasis-open.org/ubl/>.
"""
ROOT_BODY = """The OASIS Universal Business Language Technical Committee was formed in
October 2001 (proposal submitted 28 August 2001, formation announced by
OASIS on 17 October 2001, first meeting the week of 29 October 2001). This
commit marks that start; the sample documents follow with the UBL 2.0
releases from 2006.

Source: https://www.oasis-open.org/news/pr/oasis-members-form-technical-committee-to-develop-universal-business-language/"""


def git(repo, *args, env=None, input=None):
    e = dict(os.environ)
    if env:
        e.update(env)
    r = subprocess.run(["git", "-C", repo, *args], env=e, input=input,
                       capture_output=True)
    if r.returncode:
        sys.exit(f"git {' '.join(args)} failed:\n{r.stderr.decode()}")
    return r.stdout


def utc(when):
    """Sortable UTC timestamp for an ISO date or a 'YYYY-MM-DDTHH:MM:SS +0000' date."""
    return datetime.datetime.fromisoformat(when.replace(" ", "")).astimezone(datetime.timezone.utc)


def stage_title(stage):
    """'csprd01-UBL-2.2' -> 'UBL 2.2 Committee Specification Public Review Draft 01'."""
    kind, _, rest = stage.partition("-UBL-")
    version, _, suffix = rest.partition("-")
    base = kind.rstrip("0123456789r")
    num = kind[len(base):]
    rev = ""
    if "r" in num:
        num, rev = num.split("r")
        rev = f", revision {rev}"
    title = f"UBL {version} {STAGE_NAMES[base]}" + (f" {num}" if num else "") + rev
    return title + (" Update" if suffix == "update" else "")


def release_notes(stage, date, url, prev, added, updated, removed, total):
    lines = [f"### {stage_title(stage)} ({date[:10]})", "", f"Tag `{stage}` · <{url}> · {total} files", ""]
    if not (added or updated or removed):
        lines.append(f"No changes to the sample documents since `{prev}`." if prev else "No sample documents.")
    for label, names in (("Added", added), ("Updated", updated), ("Removed", removed)):
        if names:
            lines.append(f"{label} ({len(names)}):")
            lines.append("")
            lines += [f"- `{n}`" for n in names]
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def stage_order(manifest):
    out = []
    for name, st in manifest["stages"].items():
        if not st["files"]:
            continue
        date = DATE_OVERRIDES.get(name) or max(f["mtime"] for f in st["files"])
        out.append((date, name))
    out.sort()
    return out


def github_versions(oasis_repo, path, after, until):
    """Commits in oasis-tcs/ubl touching raw/xml/<path> in (after, until]."""
    if not oasis_repo:
        return []
    log = git(oasis_repo, "log", "--all", "--reverse", "--format=%H%x00%an%x00%ae%x00%aI%x00%B%x01",
              "--", f"raw/xml/{path}").decode()
    res = []
    for rec in log.split("\x01"):
        rec = rec.strip("\n")
        if not rec:
            continue
        h, an, ae, ad, msg = rec.split("\x00", 4)
        if not (after < ad[:16] <= until):
            continue
        r = subprocess.run(["git", "-C", oasis_repo, "show", f"{h}:raw/xml/{path}"], capture_output=True)
        data = r.stdout if r.returncode == 0 else None  # None = deleted
        res.append({"hash": h, "name": an, "email": ae, "date": ad, "msg": msg.strip(), "data": data})
    return res


class Builder:
    def __init__(self, repo, branch, base):
        self.repo, self.branch = repo, branch
        self.head = git(repo, "rev-parse", base).decode().strip() if base else None
        self.tree = {}  # path in xml/ -> bytes
        self.readme = None  # README.md bytes
        self.count = 0

    def commit(self, path, data, subject, body, author, date):
        """Commit one document change (data None = delete); path None = README only."""
        if path is None:
            pass
        elif data is None:
            self.tree.pop(path, None)
        else:
            self.tree[path] = data
        idx = os.path.join(git(self.repo, "rev-parse", "--absolute-git-dir").decode().strip(), "history-index")
        env = {"GIT_INDEX_FILE": idx}
        if self.head:
            git(self.repo, "read-tree", self.head, env=env)
            git(self.repo, "rm", "-q", "-f", "--cached", "-r", "--ignore-unmatch", "xml", "README.md", env=env)
        else:
            git(self.repo, "read-tree", "--empty", env=env)
        for p, d in sorted(self.tree.items()):
            blob = git(self.repo, "hash-object", "-w", "--stdin", input=d).decode().strip()
            git(self.repo, "update-index", "--add", "--cacheinfo", f"100644,{blob},xml/{p}", env=env)
        if self.readme is not None:
            blob = git(self.repo, "hash-object", "-w", "--stdin", input=self.readme).decode().strip()
            git(self.repo, "update-index", "--add", "--cacheinfo", f"100644,{blob},README.md", env=env)
        tree = git(self.repo, "write-tree", env=env).decode().strip()
        os.remove(idx)
        cenv = {"GIT_AUTHOR_NAME": author[0], "GIT_AUTHOR_EMAIL": author[1], "GIT_AUTHOR_DATE": date,
                "GIT_COMMITTER_NAME": BUILDER[0], "GIT_COMMITTER_EMAIL": BUILDER[1], "GIT_COMMITTER_DATE": date}
        parent = ["-p", self.head] if self.head else []
        self.head = git(self.repo, "commit-tree", *SIGN, tree, *parent, "-F", "-", env=cenv,
                        input=f"{subject}\n\n{body}\n".encode()).decode().strip()
        self.count += 1

    def tag(self, name, msg, date):
        env = {"GIT_COMMITTER_NAME": BUILDER[0], "GIT_COMMITTER_EMAIL": BUILDER[1], "GIT_COMMITTER_DATE": date}
        git(self.repo, "tag", "-f", "-a", name, self.head, "-m", msg, env=env)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--manifest", default="history/manifest.json")
    ap.add_argument("--cache", required=True)
    ap.add_argument("--oasis-repo")
    ap.add_argument("--repo", default=".")
    ap.add_argument("--branch", default="examples-history")
    ap.add_argument("--base", default=None, help="commit to continue from (default: none, a new root)")
    ap.add_argument("--committer", help='committer identity "Name <email>" (default: a fixed builder identity)')
    ap.add_argument("--sign", action="store_true", help="sign the commits (git commit-tree -S); signatures make hashes key-dependent")
    args = ap.parse_args()
    if args.committer:
        name, _, email = args.committer.partition("<")
        BUILDER[:] = [name.strip(), email.rstrip(">").strip()]
    if args.sign:
        SIGN.append("-S")

    manifest = json.load(open(args.manifest))
    b = Builder(args.repo, args.branch, args.base)
    notes = []  # release notes, newest first
    def write_readme():
        b.readme = (README_HEAD + "\n## Releases\n\n" + "\n".join(notes) if notes else README_HEAD).encode()
    if not args.base:
        write_readme()
        b.commit(None, None, "Start of the OASIS UBL Technical Committee", ROOT_BODY, (TC_NAME, ""), TC_START)
    published = {}  # path -> bytes, as last published
    prev_date = "0000"
    prev_stage = None
    stages = stage_order(manifest)
    for date, stage in stages:
        files = {f["path"]: f for f in manifest["stages"][stage]["files"]}
        new = {}
        for p, f in files.items():
            data = open(os.path.join(args.cache, stage, "xml", p), "rb").read()
            if sha(data) != f["sha256"]:
                sys.exit(f"cache mismatch for {stage}/{p}")
            new[p] = data
        stage_date = f"{date[:10]}T{STAGE_TIME.split()[0]} {STAGE_TIME.split()[1]}"
        url = f"{BASE_URL}{stage}/xml/"
        changed = sorted(p for p in set(new) | set(published) if new.get(p) != published.get(p))
        # Collect the changes per document, then commit them in date order.
        events = []
        for p in changed:
            before, after = published.get(p), new.get(p)
            verb = "Add" if before is None else "Remove" if after is None else "Update"
            state = before
            # Intermediate edits from the OASIS GitHub repository.
            for v in github_versions(args.oasis_repo, p, prev_date, date):
                if v["data"] == state:
                    continue  # no content change (e.g. mode or re-import)
                gverb = "Remove" if v["data"] is None else "Add" if state is None else "Update"
                final = v["data"] == after
                note = (f"Published in {stage} ({url})." if final else
                        f"Intermediate version; not published on docs.oasis-open.org.")
                events.append((utc(v["date"]), p, v["data"], f"{gverb} {p}",
                               f"{v['msg']}\n\nSource: {GITHUB}{v['hash']}\n{note}",
                               (v["name"], v["email"]), v["date"]))
                state = v["data"]
            if state != after:
                body = f"Stage: {stage} (published {date[:10]})\nSource: {url}{p}"
                if after is not None:
                    body += f"\nSHA-256: {sha(after)}"
                events.append((utc(stage_date), p, after, f"{verb} {p}", body, (TC_NAME, ""), stage_date))
        for _, p, data, subject, body, author, when in sorted(events, key=lambda e: (e[0], e[1])):
            b.commit(p, data, subject, body, author, when)
        n = len(changed)
        added = [p for p in changed if p not in published]
        removed = [p for p in changed if p not in new]
        updated = [p for p in changed if p in published and p in new]
        notes.insert(0, release_notes(stage, date, url, prev_stage, added, updated, removed, len(new)))
        write_readme()
        summary = (f"{len(added)} added, {len(updated)} updated, {len(removed)} removed." if n else
                   "No changes to the sample documents.")
        b.commit(None, None, f"Release {stage}", f"{stage_title(stage)}, published {date[:10]}.\n"
                 f"{summary}\n\nSource: {url}", (TC_NAME, ""), stage_date)
        tagmsg = (f"{stage}: UBL sample documents as published on {date[:10]}\n\n{url}\n"
                  f"{len(new)} files; " + (f"{n} changed since the previous stage." if n else
                                          "no changes since the previous stage."))
        b.tag(stage, tagmsg, stage_date)
        if dict(b.tree) != new:
            sys.exit(f"tree mismatch after {stage}")
        print(f"{stage:22} {date[:10]}  {len(new):3} files  {n:3} changed", file=sys.stderr)
        published, prev_date, prev_stage = new, date, stage
    git(args.repo, "update-ref", f"refs/heads/{args.branch}", b.head)
    print(f"{b.count} commits on {args.branch}, {len(stages)} tags", file=sys.stderr)


if __name__ == "__main__":
    main()
