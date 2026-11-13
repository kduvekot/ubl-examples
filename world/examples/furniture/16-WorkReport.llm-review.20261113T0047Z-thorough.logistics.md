# LLM review: 16-WorkReport.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/16-WorkReport.xml`, Git blob `ff4f75f1f6e61357a2aa095fc65cac1d3e911e09` (committed)
- Last commit changing the example: d9001cd 2026-11-11 Correction pass: Rec 28, airline designator, source texts, DG and CPC checks, distribution, text partners, fillers
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Checked and consistent
- References: `/WorkReport/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0581` resolves to `15-Order.xml`, as does the work order reference of the work phase; the invoice `17-Invoice.xml` refers back to this report and its line 1.
- Quantities: sub-lines 7 h + 7 h = 14 h = line quantity = `WorkQuantityTotal` = ordered hours in `15-Order.xml`; 14 × 48 = 672.00; with the packaging-disposal charge 24.00 the payable amount is 696.00. "Six desks assembled and placed" matches the six desks ordered.
- Dates: the reported period, the line period and the work phase all run 2026-04-08 to 2026-04-09; the report is dated 2026-04-09, the last day of the work; completion and progress 100 % fit a finished phase.
- Codes: INSTALL, FURNISH, HUR and AEO (collection and recycling, for packaging disposal) resolve and fit.

## Considered and refuted
- `/WorkReport/cac:WorkReportLine/cac:ActivityOriginLocation/cbc:Name` = `Lumeport Public Works Department, Civic Square`: suspected a company name instead of a place — refuted because the name designates the department's building on Civic Square, the place where the work was done, and agrees with the delivery place of `15-Order.xml`.
- `/WorkReport/cac:AdditionalDocumentReference/cbc:ID` = `BF-PHOTO-26-0408` and `/WorkReport/cac:WorkReportLine/cac:DocumentReference/cbc:ID` = `BF-CHECK-26-0408`: suspected references to documents that do not exist — refuted because a photo record and a checklist are not UBL documents and need not exist as examples; their IDs follow the maker's numbering with the date of the work.
- `/WorkReport/cac:BillingReference/cac:AdditionalDocumentReference/cbc:ID` = `PWD-COMMIT-26-0381` and `/WorkReport/cac:ProjectReference/cbc:ID` = `PWD-PLAN-OFFICE-26`: suspected unresolvable references — refuted because a budget commitment and a project plan of the department are internal records, not documents of the exchange.
- `/WorkReport/cbc:IssueDate`: suspected that a report issued on the last day of the work cannot cover the whole day — refuted because `IssueTime` is optional and absent, so the report may have been issued after the work ended; whether `17-Invoice.xml` (2026-04-09 10:10) could follow it is noted there.
