# LLM review: 38-ReceiptAdvice.xml

Flow: tender (PWD/2026/0566) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/tender/38-ReceiptAdvice.xml`, Git blob `ad063b4236912ea8a2efb00dfa751126f70f19a0` (committed)
- Last commit changing the example: d34fe695 2026-11-21 O277 (3): UBL's spelling "despatch" for UBL concepts, and a published-text rule for it
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

### tender/38#F1 · High · Despatch supplier differs from the despatch advice it answers
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `29-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: The receipt advice refers to despatch advice CAS-DA-26-1459 (`29-DespatchAdvice.xml`, header and line 1), in which the despatch supplier is Castrano Logistics, Valdara's warehouse, and Valdara Industries is the seller (`SellerSupplierParty`). Here Valdara is named as the despatch supplier, with a "Despatch office / Despatch coordinator / Warehouse" contact that is Castrano's role in 29. The two documents name different parties for the same despatch. The receipt advice clearly has to reach Valdara, which installs the benches and is credited and paid (`33-CreditNote.xml`, `39-Invoice.xml`), but the role for that is the seller.
- Condition: `DespatchSupplierParty` names the same party as in `29-DespatchAdvice.xml`, and Valdara Industries, if named, is in `SellerSupplierParty` (with `BuyerCustomerParty` for the department, if needed); or 29 is changed so that Valdara is the despatch supplier there too.
- Options: (a) preferred: Castrano Logistics as despatch supplier and Valdara Industries as seller, as in 29 and in `rail/15-DespatchAdvice.xml` for the same warehouse; the receipt advice is still sent to the seller; (b) make Valdara the despatch supplier in both 29 and 38, if the story is that Valdara despatches and Castrano only stores.
- Needs decision: no

## Checked and consistent
- Quantities: 40 benches received on 31 March (as delivered in `29-DespatchAdvice.xml` and invoiced in `32-Invoice.xml`, delivery date 2026-03-31), 1 rejected as damaged with action CREDIT, credited by `33-CreditNote.xml` (1 bench); 39 installations received, as invoiced in `39-Invoice.xml` (39 × installation, 702.00 XBL).
- Timing: ordered completion by Tuesday 7 April (`26-Order.xml` note); completed Friday 10 April = 3 working days late, one waived = 2 days; `36-RemittanceAdvice.xml` deducts 2 × 0.5 % × 702.00 = 7.02 XBL, which agrees with the timing complaint.
- "The 30 days of payment run from today" (13 April) agrees with `39-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-05-13` and with the terms "30 days after the release is accepted".
- Order PWD/2026/0567 → `26-Order.xml` (lines 1 and 2, 40 each), despatch advice → 29; ProfileExecutionID PWD/2026/0566 as in 26, 29, 32, 33, 39; item in moss green GRN as changed by `27-OrderChange.xml`; the Urvanian item texts repeat those of the order.

## Considered and refuted
- `/ReceiptAdvice/cac:ReceiptLine[1]/cbc:RejectReason` = `Side frame cracked while the bench was anchored on 2 April.`: a bench damaged by the supplier's own installer after receipt is rejected as received goods — refuted because the release is accepted as a whole (goods and installation) on 13 April, and the rejection at acceptance with a credit is what the contract's acceptance step is for.
- `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cbc:Description[1]`: Urvanian text in a document between two English-speaking parties — refuted: it is the seller's item text as carried in the order and despatch advice.
