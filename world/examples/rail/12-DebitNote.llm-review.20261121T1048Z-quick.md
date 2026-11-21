# LLM review: 12-DebitNote.xml

Flow: rail (9900043586) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/rail/12-DebitNote.xml`, Git blob `8dbeb5efd0889f1c5a1c6f699aac24f4f9412841` (committed)
- Last commit changing the example: 2a048333 2026-11-20 Read-throughs of 2026-11-20: mechanical fixes in tender, contest, medicines, lpg, ore, rail, energy, utilities, reefer, waste, plastics, mast, air, packaging; owner decisions on the tender lead time, the plastics customs value, the air transit and O269
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
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

## Findings

### rail/12#F1 · Low · Payment terms of the freight copied to the demurrage debit note
- XPath: `/DebitNote/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- XPath: `/DebitNote/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-05-14`
- XPath: `10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net from the consignment note.`
- Why: The debit note charges demurrage for 21 and 22 April, which accrued a week after the consignment note `08-Waybill.xml` (issued 2026-04-14). Its terms repeat the freight invoice's "30 days net from the consignment note" and give the same due date as the invoice, 21 days after this debit note was issued. The term in `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cac:PaymentTerms/cbc:Note` was agreed for the freight. Counting the payment period for a charge from a document that was issued before the charge existed is an odd term, and it looks copied from the invoice.
- Condition: The debit note's payment terms state a basis that fits a charge raised after delivery (e.g. counted from the debit note's issue date), and the due date agrees with that basis; or the framework contract is shown to count every charge of the consignment from the consignment note.
- Options: (a) preferred: terms counted from the debit note (e.g. "30 days net from the date of the debit note", due 2026-05-23), as is usual for an additional charge; (b) keep it, if the contract really does align every charge of the consignment to one due date (then the note could say so).
- Needs decision: no

## Checked and consistent
- Demurrage arithmetic: placed 15 April, free time five days counted from the day after placement (16–20 April, the DemurrageInstructions of 03 and 08), released 22 April: 21 and 22 April = 2 days; 2 × 7 500 = 15 000 XUF; the rate 7,500 ferra per container day agrees with `03-TransportExecutionPlan.xml` and `08-Waybill.xml`.
- Line and header InvoicePeriod (21–22 April) agree with the note; totals 15 000 throughout; tax 0 with category E.
- `BillingReference` 2026/2732 resolves to `10-Invoice.xml` (same supplier, customer, contract FRC-CON-2026-005, same exemption EXPTRANSPORT); waybill 7200092547 resolves to `08-Waybill.xml`; container FRXU1044180 occurs in 06, 07, 08, 09.
- RF reference RF7020262888 and the IBAN-like account pass `check_ids.py`; payee account, channel and rail agree with `10-Invoice.xml`.
- Type code 383 (debit note) fits; ProfileExecutionID 9900043586 is the one of the freight collaboration (02, 03, 07–10).

## Considered and refuted
- `/DebitNote/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXPTRANSPORT`: demurrage is a charge at the consignee's siding in Bayvarra, not transport — refuted because it is an ancillary charge of the export transport under the same contract, and the freight invoice uses the same exemption; the treatment is consistent within the flow.
- Only one of the two containers is charged — refuted: the other may have been released within the free time; nothing in the flow says otherwise.
