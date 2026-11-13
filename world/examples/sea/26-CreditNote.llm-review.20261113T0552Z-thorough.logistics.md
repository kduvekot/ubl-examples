# LLM review: 26-CreditNote.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/26-CreditNote.xml`, Git blob `27ef7cc12dad5d613bda5ae257e7fc61371126be` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Checked and consistent
- References: invoice LD-INV-26-0147 with its issue date 2026-05-14 (22-Invoice.xml), receipt
  advice NW-RA-26-0146 (21-ReceiptAdvice.xml, 2026-05-21), statement HF-ST-26-0151
  (25-Statement.xml, 2026-06-13) and order VT-PO-26-0127 all exist and were issued before this
  credit note (2026-06-15).
- The credited item (one side frame LD-10443, GTIN 9520610000029, 64.00 = invoice line 2 unit
  price) is the one rejected on line 2 of the receipt advice; "box crushed at the port of Selanu"
  agrees with the receipt line's note and with the discrepancy code 17 (transport damage).
- The policy named in the annotation, WS-CP-26-4471, is the cargo policy in 14-BillOfLading.xml.
- Delivery date 2026-05-21 is the receipt date in 21-ReceiptAdvice.xml.

## Considered and refuted
- `/CreditNote/cac:Delivery/cbc:ActualDeliveryDate` = `2026-05-21`: under CIF the goods are delivered on
  board at Lumeport (2026-05-14), which the note itself states — refuted because ActualDeliveryDate
  is "the actual date of delivery" and the physical delivery to the buyer's 3PL is a legitimate
  reading; the risk transfer is stated separately in the note.
- `/CreditNote/cac:ContractDocumentReference/cbc:ID` = `LD-DAG-26-0125`: the referenced document is the
  digital (EDI) agreement 03-DigitalAgreement.xml, not a sales contract, and the credit is a
  goodwill gesture — refuted because the element is "a reference to a contract associated with
  this document", and the agreement under which the credit note is exchanged is such a contract.
- `/CreditNote/cac:OriginatorDocumentReference/cbc:ID` = `VT-CLAIM-26-0019`: no example has this ID —
  refuted because the buyer's claim is an internal document outside the flow, and the debit note
  28-DebitNote.xml refers to a different claim (VT-CLAIM-26-0021) for a different matter.
