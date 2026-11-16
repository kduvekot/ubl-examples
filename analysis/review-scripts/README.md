# Scripts kept from the reviews of November 2026

Helper scripts that the reviewers and the worklist run wrote in the session's temporary folder, kept
so that they are not lost. They are a record of how results were made. They are not part of the
build, were not reviewed, and may not run as they stand: they read tables from `.review/tables/`
and files from temporary folders that no longer exist.

| Folder | From | What the scripts did |
|---|---|---|
| `consistency-20261114T2143Z/conditions/` | The consistency review, topic conditions | Pivots of exchange rates, taxes, payment terms and prices; the check of the review's citations |
| `consistency-20261114T2143Z/timelines-equipment/` | Topics timelines and equipment | The timeline per flow, references between documents, events after the issue time |
| `consistency-20261114T2143Z/parties-items-identifiers/` | Topics parties, items and identifiers | The party, item and scheme registers and the variants per party |
| `worklist/` | The worklist by root cause | `rules.py`, `pre.py` and `assign.py` assigned the 3,348 findings to causes (result: `analysis/worklist-assignments.csv`); `meta.py`, `decisions.py`, `make_docs.py` and `cite.py` wrote the first versions of `analysis/worklist.md` and `analysis/worklist-decisions.md` |

**Do not run `worklist/make_docs.py`.** It writes `analysis/worklist.md` and
`analysis/worklist-decisions.md` anew. `analysis/worklist-decisions.md` has been edited by hand since
(the owner's decisions, the story lines, the open points), and a new run would overwrite them.

What was not kept: the per-example reviewers' scratch files (the review skill treats them as
temporary), copies of the generated tables, and downloads whose address is recorded where they are
cited (the UBL 2.5 specification, the E.D.C. guide to ISO/IEC 15459).
