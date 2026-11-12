# LLM review: 16-ApplicationResponse.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/16-ApplicationResponse.xml`, Git blob `1e7f911b472f7aea92ee35fb380bd4e0c2647589` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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
- The response accepts the invoice that exists (`/ApplicationResponse/cac:DocumentResponse/cac:DocumentReference/cbc:ID` = `VI-INV-26-0166`), whose quantities and prices agree with the order (96 × 49 900 and 12 × 5 980, `15-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `4862160`), and the later remittance pays exactly that amount, so "accepted for payment" is what the flow then does.

## Considered and refuted
- `/ApplicationResponse/cac:DocumentResponse/cac:Response/cac:Status/cbc:Description` = `Three-way match passed.`: suspected that the match cannot pass while the corrected receipt shows 13 side frames against 12 ordered and invoiced (`13-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine[2]/cbc:ReceivedQuantity` = `13`) — refuted because a three-way match checks that the invoiced quantity is ordered and received; 12 invoiced against 12 ordered and 13 received passes. The unsettled extra unit is a finding of the receipt advice's review (road/13#F1 of this part).

## Outside this review
- The acceptance is effective 2026-03-25 at 06:12 (`/ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:EffectiveTime` = `06:12:00`), before the goods arrived (`14-Invoice.xml:/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:ActualDeliveryTransportEvent/cbc:OccurrenceTime` = `09:40:00` on the same day) and before either receipt advice (`11-ReceiptAdvice.xml:/ReceiptAdvice/cbc:IssueTime` = `15:40:00` the same day, and the corrected one on 2026-03-26); a three-way match needs the receipt. An order-of-documents question across the flow.
