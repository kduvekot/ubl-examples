# LLM review: 09-RemittanceAdvice.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/09-RemittanceAdvice.xml`, Git blob `64ddc3389c441e3d1a8906ba4cb8cd22d97d45ce` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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
- References: line 1 KG-INV-26-0157 is `06-Invoice.xml` (debit 132 480 000 XUF = its payable amount); line 2 KG-DOC-26-0159 is `08-Reminder.xml` (Reminder of Kelpstone Gas to Montebrio Power), which carries the surcharge; `PaymentID` RF41KGINV260157 = `06-Invoice.xml:/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF41KGINV260157`.
- Dates: issued 2026-06-06 16:36, after the reminder (2026-06-03) and before its new due date 2026-06-10.
- `LineCountNumeric` 2 = number of lines; the note ("The March gas invoice, with the surcharge of the reminder") agrees with the two references.
- `check_ids.py`: RF41KGINV260157 and both account check digits OK.

## Considered and refuted
- `/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `KG-INV-26-0157`: suspected that the reference needs the invoice's issue date to be unambiguous — refuted because the identifier is unique in the flow and the payment reference RF41KGINV260157 repeats it.
