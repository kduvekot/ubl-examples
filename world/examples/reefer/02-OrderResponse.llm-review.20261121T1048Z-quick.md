# LLM review: 02-OrderResponse.xml

Flow: reefer (26-0214) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/reefer/02-OrderResponse.xml`, Git blob `ab086b03ce983c09b24061da3543b6ffa6980a7b` (committed)
- Last commit changing the example: 99d799b3 2026-11-20 O97 and O78: the call states the withholding, tenders carry the tax subtotal, every time carries its place's UTC offset
- Checkout: branch `claude/gifted-sagan-eb1o6c`, commit 2acb7b1b 2026-11-21 Merge remote-tracking branch 'origin/main' into claude/gifted-sagan-eb1o6c
- Skill: `.claude/skills/ubl-example-review`, last commit eb70c59e 2026-11-19 O157: the farm register's keeper is the island's Department of Agriculture (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### reefer/02#F1 · Low · The conditional acceptance is never answered by the buyer
- XPath: `/OrderResponse/cbc:OrderResponseCode` = `CA`
- XPath: `/OrderResponse/cac:ValidityPeriod/cbc:EndDate` = `2026-04-17`
- Why: code CA of UN/EDIFACT 4343 means "conditionally accepted": the seller changes lines 2 and 3 (280 Granny Smith instead of 224, 168 pears instead of 224) and says the offer stands until Friday 17 April at noon. No document of the flow shows the buyer accepting the change (no OrderChange, no second Order, no response from the buyer), yet every later document carries the changed quantities (`06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[2]/cbc:DeliveredQuantity` = `280`, `08-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:InvoicedQuantity` = `168`), and `11-ReceiptAdvice.xml` and `12-RemittanceAdvice.xml` speak of "the mix of your order response". The seller books the reefer with `03-ForwardingInstructions.xml` at 10:40 on 17 April, before the deadline, without anything saying that the buyer agreed. A reader of the flow cannot see when or how the counter-offer became the contract.
- Condition: the flow shows the buyer's acceptance of the changed quantities before the goods are despatched (a document, or a statement in a document of the flow), or the response is not conditional.
- Options: (a) state the buyer's acceptance in a later document the buyer sends, e.g. a note in a later buyer document or an OrderChange carrying 280/168 (preferred if a document is added: it makes the counter-offer binding); (b) keep the flow and say in the despatch advice's note that the buyer accepted on a given date; (c) make the change an accepted-with-amendment response if the world's practice treats silence as acceptance.
- Needs decision: yes

## Checked and consistent
- 672 × 26 = 17,472.00; 280 × 24.5 = 6,860.00; 168 × 27 = 4,536.00; sum 28,868.00 = `/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `28868.00`.
- The counter-offer keeps 20 pallets of 56 cartons: 12 Gala + 5 Granny Smith + 3 pears, as the note says ("three pallets of pears instead of four and a fifth pallet of Granny Smith").
- The dates in the note: 17 April 2026 is a Friday, the ship on Thursday is 23 April (the sailing named in `01-Order.xml`).
- Order reference `26-0215` resolves to `01-Order.xml`; party data agree with that order.

## Considered and refuted
- `/OrderResponse/cac:OrderLine[1]/cac:OrderLineReference/cbc:LineID` = `1`: OrderLineReference is defined for another line "such as in a replacement order" — refuted: in an order response it is the usual way to point at the order line being answered.
