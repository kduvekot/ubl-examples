# LLM review: 17-Invoice.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/17-Invoice.xml`, Git blob `66ce2e15ac8d6433692b369df50c1ad798bd1603` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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
- References: `/Invoice/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0581` resolves to `15-Order.xml`; `/Invoice/cac:WorkReportDocumentReference/cbc:ID` = `BF-DOC-26-0582` resolves to `16-WorkReport.xml`, and its line 1 exists (14 h).
- Quantities and arithmetic: 6 desks × 880 = 5280.00, 14 h × 48 = 672.00, sum 5952.00, plus the charge 24.00 = 5976.00; quantities, prices and the charge agree with `15-Order.xml` and `16-WorkReport.xml`; the line note "Two installers, seven hours" agrees with the work report's sub-lines.
- The invoice period of line 2 (2026-04-08 to 2026-04-09) equals the reported period of the work report.
- Item dimensions (1600 × 800 × 740 mm) and identifiers agree with the order; GTIN and GLN check digits pass, the RF reference RF52BFINV260583 passes.

## Considered and refuted
- `/Invoice/cbc:IssueTime` = `10:10:00`: suspected an invoice issued before the invoiced work ended (the work runs to 2026-04-09 and is invoiced at 10:10 that day) — refuted because the 14 hours span two days, so the second day may have ended early in the morning (e.g. most of the seven hours per installer on 2026-04-08), and the work report carries no issue time that the invoice would precede.
- `/Invoice/cac:InvoiceLine[1]`: suspected an invoice for desks without a delivery date — refuted because the desks were delivered and placed during the referenced work (`16-WorkReport.xml`, 2026-04-08 to 2026-04-09), which the invoice references at document level.
