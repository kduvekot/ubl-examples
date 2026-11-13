# LLM review: 13-CreditNote.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/13-CreditNote.xml`, Git blob `62fa2031ce86b8f92b5eb82929f1d00df2904665` (committed)
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
- References: `/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `BF-INV-26-0575` resolves to `09-Invoice.xml`, and its issue date `/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:IssueDate` = `2026-03-22` equals that invoice's; BS-PO-26-0574 resolves to `08-Order.xml`; BF-DOC-26-0578 resolves to `12-InstructionForReturns.xml`.
- Quantity: `/CreditNote/cac:CreditNoteLine/cbc:CreditedQuantity` = `6` sets, the quantity of the return instruction, out of the 20 invoiced.
- Arithmetic: 6 × 610 = 3660.00 = item price extension; 5 % of 3660.00 = 183.00; 3660.00 − 183.00 = 3477.00 = line extension = payable.
- Dates: the credit note (2026-05-03) follows the actual return delivery of 2026-05-02 recorded in `14-DebitNote.xml`.

## Considered and refuted
- `/CreditNote`: suspected a credit for returned goods with no record that they arrived — refuted because the flow records the arrival (`14-DebitNote.xml:/DebitNote/cac:Delivery/cbc:ActualDeliveryDate` = `2026-05-02`), and a credit note need not carry the receipt itself.
