# LLM review: 17-Invoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/17-Invoice.xml`, Git blob `7bc3532e1225094de3f9e7a64900c767d56742c2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

## Findings

### cotton/17#F1 · Low · Sea freight invoiced although the bill of lading says "freight collect"
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Port-to-port sea freight for one 40-foot container, booked with the ocean carrier.`
- XPath: `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `TOL-BL-26-0206`
- XPath: `13-BillOfLading.xml:/BillOfLading/cbc:Note` = `Freight collect.`
- Why: The invoice charges the mill for the port-to-port sea freight and refers to the bill of lading 13, which is marked "Freight collect", i.e. the carrier collects the freight from the consignee (the mill) at destination. Unless the forwarder collects the freight as the carrier's agent or has paid it and recharges it, which the invoice does not say, the mill would pay the same freight to the carrier and to the forwarder.
- Condition: the invoice and the bill of lading describe one way in which the sea freight is paid.
- Options: (preferred) say in the invoice line (description or note) that the forwarder collects the freight on the carrier's behalf, or that it is the forwarder's own charge for a freight it prepaid (then mark 13 prepaid); see the review of 13.
- Needs decision: yes (who pays the carrier is part of the story)

### cotton/17#F2 · Low · The container invoiced is not identified
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cbc:ID` = `LTM-CS-26-0201`
- XPath: `12-WeightStatement.xml:/WeightStatement/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:ID` = `TWLU4123110`
- Why: The invoice is priced per container ("one 40-foot container", quantity 1 service unit) and describes the shipment through the consignment and the carrier, but does not identify the container (`TWLU4123110`, 12) or its size type, nor the shipment `SCG-SH-26-0200`. A freight invoice priced per container usually names it; the bill of lading it refers to does not carry the container either (review of 13), so the container cannot be traced from the invoice. Completeness remark.
- Condition: the container the freight is charged for can be identified from the invoice or from the document it refers to.
- Options: (preferred) add a transport handling unit with the container (ID and size type 40-foot) to the delivery's shipment; or rely on the bill of lading once it carries the container.
- Needs decision: no

## Checked and consistent
- `AdditionalDocumentReference` `TOL-BL-26-0206` resolves to 13; consignment `LTM-CS-26-0201` and carrier Tidewell Ocean Lines agree with 09 and 13.
- The forwarder invoicing the mill fits FOB (08): the buyer pays the main carriage.
- "30 days net" from 2026-03-04 gives 2026-04-03, the due date stated three times; the penalty period starts the day after (2026-04-04).
- 40-foot container agrees with the tare 3750 kg in 12.
