# LLM review: 05-Order.xml

Flow: medicines (QLM-TX-26-3960) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/medicines/05-Order.xml`, Git blob `51571bf6a7e8d6369f6172a6de2dadc60a275bab` (committed)
- Last commit changing the example: 2a048333 2026-11-20 Read-throughs of 2026-11-20: mechanical fixes in tender, contest, medicines, lpg, ore, rail, energy, utilities, reefer, waste, plastics, mast, air, packaging; owner decisions on the tender lead time, the plastics customs value, the air transit and O269
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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### medicines/05#F1 · Medium · A call-off order that names no agreement it calls off
- XPath: `/Order/cbc:OrderTypeCode` = `226`
- XPath: `/Order/cbc:Note` = `Week 25: one 20 GBq generator, reference Sunday 21 June 12:00 UTC, to arrive at Lumeport on Sunday 14 June.`
- Why: code 226 (UN/EDIFACT 1001) is a "call off order": an order under a blanket agreement for the call-off of goods. The note ("Week 25") implies a standing weekly supply, but the order has no `Contract` (or other reference) to the agreement whose terms, price and schedule it relies on. The type code's meaning depends on that agreement.
- Condition: the order references the framework agreement it calls off, or its type code is a plain order (220).
- Options: (a, preferred) a `cac:Contract` with the identifier of the weekly supply agreement with Haarvliet Isotopes; (b) type 220 if there is no agreement.
- Needs decision: no

### medicines/05#F2 · Low · "Six days after delivery" does not fit this delivery
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Description` = `A molybdenum-99/technetium-99m generator of 20 GBq nominal activity at its reference time, six days after delivery (European pre-calibration)…`
- XPath: `/Order/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:StartDate` = `2026-06-14`
- Why: the generator is to arrive at Lumeport on Sunday 14 June, and its reference is Sunday 21 June 12:00 UTC (the note, and `07-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Item/cac:ItemInstance/cac:AdditionalItemProperty[2]/cbc:Value`): seven days after delivery to Quillmoor. The six days are right only for the hospital's delivery on 15 June (`04-Order.xml`); the description describes the hospital's situation in the wholesaler's purchase.
- Condition: the description of the item in the purchase from Haarvliet agrees with the delivery date and reference time of this order.
- Options: (a, preferred) a description without the delivery-relative wording ("reference time stated on the order"), shared by all documents; (b) "seven days after delivery" in the documents between Haarvliet and Quillmoor.
- Needs decision: no

## Checked and consistent
- Dates: 14 and 21 June 2026 are Sundays; 15–21 June is ISO week 25 of 2026.
- Arithmetic: 1 × 1000 EUR = 1,000.00; VAT 0 with "Export outside the European Union" for a Dutch supplier shipping to Bayvarra.
- Delivery terms CPT Lumeport airport cargo terminal and quantity agree with `07-Invoice.xml` and `08-ImportCustomsDeclaration.xml`; the item identifiers match `04-Order.xml` (Quillmoor's `QLM-RAD-0020`, maker's `HVI-TCG-20`).
- The supplier's address in Alkmaar with offset +02:00 (summer time in the Netherlands) is consistent.
