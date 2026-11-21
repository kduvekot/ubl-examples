# LLM review: 13-DebitNote.xml

Flow: rail (LMW-TX-26-0734) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/rail/13-DebitNote.xml`, Git blob `74b0e80fd3a6c4ef8437e7222944bccd110393f2` (committed)
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

### rail/13#F1 · Low · Reference to the carrier's debit note, which the buyer has not received, without attachment or description
- XPath: `/DebitNote/cac:AdditionalDocumentReference[2]/cbc:ID` = `2026/2888`
- XPath: `/DebitNote/cac:AdditionalDocumentReference[2]/cbc:DocumentTypeCode` = `DebitNote`
- Why: The reference resolves to `12-DebitNote.xml`, which Ferrano Rail Cargo sent to Valdara Industries, not to Lumeway Distribution. For the customer of this debit note the ID alone is a number from a document it never saw: it cannot check the charge against it. As supporting evidence for a passed-on charge, the reference would need the document attached, or at least an issuer and a description saying what it is (the carrier's demurrage charge to the seller).
- Condition: The reference either carries the carrier's debit note (Attachment) or says whose document it is and what it shows (e.g. `IssuerParty` and `DocumentDescription`), or is left out.
- Options: (a) preferred: add `DocumentDescription` ("Ferrano Rail Cargo's demurrage debit note to the seller") and, if the buyer is to verify it, an attachment; (b) drop the reference, since the note already gives the dates and the waybill reference.
- Needs decision: no

## Checked and consistent
- Arithmetic: 2 days × 7 500 = 15 000 XUF; settlement discount 2 % of 15 000 = 300; settlement period 24 April to 4 May = 10 days; due date 2026-05-25: 30 days after 24 April fall on Sunday 24 May, moved to the following Monday.
- The charge passes on `12-DebitNote.xml` exactly (same container FRXU1044180, same period 21–22 April, same 2 days at 7 500); FRXU1044180 is the second container in `08-Waybill.xml` (after FRXU1044175), which agrees with the note "the second container".
- `DiscrepancyResponse` cites the delivered-at-place terms: `01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `DAP`, with delivery at Lumeway's siding; under DAP the buyer unloads, so a delay in unloading is the buyer's.
- Order LMW-PO-26-0734 → `01-Order.xml`; invoice 2026/1770 → `11-Invoice.xml` (same parties, tax category G/EXP, payment terms XU-STD wording, channel RTNS and rail TRADE-ACCORD-PAY); ProfileExecutionID LMW-TX-26-0734 as in 01 and 11.
- GLN, RF reference and IBAN-like account pass `check_ids.py`.

## Considered and refuted
- `/DebitNote/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `G`: demurrage is a service, not an export of goods — refuted because the debit note raises the consideration of the export sale billed in `11-Invoice.xml` (DAP), and an increase in the price of a supply follows that supply's treatment.
- `/DebitNote/cac:PaymentTerms/cbc:SettlementDiscountPercent` = `2`: a cash discount on a passed-on cost — refuted because these are the seller's standard terms (`XU-STD`), applied as on the invoice.
