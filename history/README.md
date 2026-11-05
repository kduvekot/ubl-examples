# History of the OASIS UBL sample documents

The `xml/` folder of this repository holds the sample documents that OASIS
published with UBL 2.0 up to UBL 2.5. Its git history is **rebuilt** from the
published sources: you can see when each example was added, changed or removed,
as if the examples had been maintained here from the start. UBL 1.0 is out of
scope.

## Sources

1. **docs.oasis-open.org.** Every UBL 2.x stage directory with an `xml/` folder:
   <https://docs.oasis-open.org/ubl/>. `tools/crawl_oasis.py` downloads every file
   and records it in [`manifest.json`](manifest.json) (path, size, server
   timestamp, SHA-256).
2. **github.com/oasis-tcs/ubl.** The TC's working repository. It starts in May
   2021 (a copy of 2.3 CSD05). Only 12 of its commits touch the examples
   (`raw/xml/`). They give finer detail for two stages: intermediate versions of
   Invoice-2.1, PurchaseReceipt-2.4 and DebitNote-2.5, plus who removed
   DebitNote-2.1 and FreightInvoice-2.1, and when.

## How the history is built

- **Starting commit.** The history starts on 17 October 2001, when OASIS
  announced the formation of the UBL Technical Committee
  ([press release](https://www.oasis-open.org/news/pr/oasis-members-form-technical-committee-to-develop-universal-business-language/)).
  The proposal was submitted on 28 August 2001; the first meeting was held the
  week of 29 October 2001, hosted by Sun Microsystems
  ([Cover Pages](http://xml.coverpages.org/UBL-Subcommittees20011112.html)).
  This commit only adds `README.md`.
- **One document per commit.** Each commit adds, updates or removes exactly one
  file in `xml/`.
- **Published changes** are dated on the stage's publication date (12:00 UTC)
  and authored by "OASIS UBL TC". The commit message names the stage, the source
  URL and the SHA-256 of the published file.
- **Changes from the OASIS GitHub repository** keep the original author, date and
  message, with a link to the source commit. Versions that never appeared on
  docs.oasis-open.org are marked *intermediate*.
- **Every stage ends with a release commit**, also when it changed nothing. That
  commit adds the stage's release notes (added, updated and removed files) to
  `README.md`. It gets an annotated tag with the stage's directory name (e.g.
  `os-UBL-2.1`), and its `xml/` folder equals what the stage published, byte for
  byte; the build stops if it doesn't.
- **Stage order and date** come from the server timestamps of the published
  files. Exception: `os-UBL-2.0-update` republished the 2006 files unchanged and is
  dated on its publication date, 2008-05-29.
- **Deterministic.** The same manifest, cache and GitHub clone always give the
  same commit hashes. The published branch was built with
  `--committer "Claude <noreply@anthropic.com>" --sign`, so its commits are
  signed and their hashes depend on the signing key. Authors, dates, messages and
  file contents are the same as in an unsigned build, so you can compare with
  `git diff` or by tree hash (`git log --format=%T`).

## Reproduce

```bash
python3 tools/crawl_oasis.py --cache /path/to/cache --out history/manifest.json
```

```bash
git clone --filter=blob:none --no-checkout https://github.com/oasis-tcs/ubl.git /path/to/oasis-ubl
```

```bash
python3 tools/build_history.py --cache /path/to/cache --oasis-repo /path/to/oasis-ubl --repo . --branch examples-history
```

Re-running the crawl and comparing `manifest.json` (`git diff`) shows whether
anything was published or changed on docs.oasis-open.org since the last crawl.

## Stages

Crawled 2026-11-05. 36 stages have an `xml/` folder; `prd-UBL-2.0` and
`errata-UBL-2.0` have none. 15 stages changed the examples, 21 republished them
unchanged.

| Stage (tag) | Date | Files | Changed |
|---|---|---:|---:|
| prd2-UBL-2.0 | 2006-07-20 | 10 | 10 |
| prd3-UBL-2.0 | 2006-09-21 | 10 | 10 |
| prd3r1-UBL-2.0 | 2006-10-05 | 13 | 13 |
| cs-UBL-2.0 | 2006-10-12 | 13 | – |
| os-UBL-2.0 | 2006-12-12 | 13 | – |
| os-UBL-2.0-update | 2008-05-29 | 13 | – |
| prd1-UBL-2.1 | 2010-09-25 | 45 | 45 |
| prd2-UBL-2.1 | 2011-05-30 | 53 | 18 |
| prd3-UBL-2.1 | 2013-02-23 | 57 | 37 |
| csd4-UBL-2.1 | 2013-05-14 | 57 | – |
| prd4-UBL-2.1 | 2013-05-14 | 57 | – |
| cs1-UBL-2.1 | 2013-06-29 | 57 | – |
| cos1-UBL-2.1 | 2013-07-15 | 57 | – |
| os-UBL-2.1 | 2013-11-04 | 57 | – |
| csprd01-UBL-2.2 | 2016-12-21 | 65 | 8 |
| csprd02-UBL-2.2 | 2017-11-01 | 65 | 3 |
| csprd03-UBL-2.2 | 2018-02-21 | 65 | – |
| cs01-UBL-2.2 | 2018-03-22 | 65 | – |
| cos01-UBL-2.2 | 2018-04-22 | 65 | – |
| os-UBL-2.2 | 2018-07-09 | 65 | – |
| csprd01-UBL-2.3 | 2019-08-07 | 65 | 1 |
| csprd02-UBL-2.3 | 2020-01-29 | 70 | 5 |
| csd03-UBL-2.3 | 2020-07-29 | 73 | 12 |
| csd04-UBL-2.3 | 2020-11-25 | 76 | 3 |
| cs01-UBL-2.3 | 2021-01-19 | 76 | – |
| cs02-UBL-2.3 | 2021-05-25 | 76 | – |
| os-UBL-2.3 | 2021-06-15 | 76 | – |
| csd01-UBL-2.4 | 2023-02-08 | 77 | 21 |
| csd02-UBL-2.4 | 2023-07-26 | 77 | – |
| cs01-UBL-2.4 | 2023-10-17 | 77 | – |
| os-UBL-2.4 | 2024-06-20 | 77 | – |
| csd01-UBL-2.5 | 2025-08-28 | 76 | 3 |
| csd02-UBL-2.5 | 2025-12-03 | 76 | – |
| csd03-UBL-2.5 | 2026-02-09 | 76 | – |
| cs01-UBL-2.5 | 2026-04-22 | 76 | – |
| os-UBL-2.5 | 2026-08-12 | 76 | – |

In total there are 189 published document changes (82 added, 101 updated,
6 removed) and 6 intermediate versions from GitHub: 195 document commits.
With the starting commit and the 36 release commits, the rebuilt history has
232 commits. The commits adding this tooling come on top.

## Relation to earlier attempts

The branches `claude/ubl-samples-hist-3IuwR` and `sample-research` (`official/`)
held partial copies: only changed files, and no CS/COS/OS stages. Every file
version on those branches is part of this history.
