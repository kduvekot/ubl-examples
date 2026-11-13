# LLM review: 15-TransportationStatus.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/15-TransportationStatus.xml`, Git blob `5b9a4c32822b9c4f60e917122105de36cde607f1` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/15#F1 · High · Carrier-assigned ID differs from the carrier's reference in the waybill
- XPath: `/TransportationStatus/cbc:CarrierAssignedID` = `BF-ROAD-26-0231`
- XPath: `13-Waybill.xml:/Waybill/cbc:CarrierAssignedID` = `BF-CMR-26-0217`
- XPath: `14-TransportationStatusRequest.xml:/TransportationStatusRequest/cbc:CarrierAssignedID` = `BF-WB-26-0231`
- Why: CarrierAssignedID is "A reference number assigned by a carrier or its agent to identify a specific shipment". Bayforth itself gives the shipment a different reference here than in its own waybill 13, and the request 14 uses a third value. One shipment, one carrier reference.
- Condition: the carrier-assigned ID is the same in 13, 14 and 15.
- Options: (a, preferred) `BF-CMR-26-0217` everywhere; (b) another single value.
- Needs decision: no

### retail/15#F2 · Medium · Expected arrival on 29 April at 14:00, but the goods are received on 30 April
- XPath: `/TransportationStatus/cac:UpdatedDeliveryTransportEvent/cbc:OccurrenceDate` = `2026-04-29`
- XPath: `/TransportationStatus/cac:UpdatedDeliveryTransportEvent/cbc:OccurrenceTime` = `14:00:00`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `On its way from the distribution centre; arrival expected at 14:00.`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedDate` = `2026-04-30`
- XPath: `17-ReceiptAdvice.xml:/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedTime` = `10:40:00`
- XPath: `12-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueTime` = `15:34:00`
- Why: At 11:49 the truck is "on its way" on the Marrowdale ring road and expected at the store at 14:00 the same day. The trip is 38 km (`16-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `38`). The receipt advice 17 records the receipt on the next day at 10:40, "40 minutes into the slot", and the despatch advice 12 is only issued at 15:34 on the 29th. An estimate may be wrong, but a truck already on its way for a 38 km trip that arrives 23 hours later with no further status is a contradiction the flow does not explain.
- Condition: the status, the despatch advice and the receipt advice describe one consistent delivery: either the truck is on its way on the day it delivers, or a later status explains the delay.
- Options: (a, preferred) move this status (and the "on its way" event) to the morning of 2026-04-30 with an expected arrival around 10:00 (fits the "slot" in 17); (b) keep 2026-04-29 and move the receipt in 17 to that afternoon.
- Needs decision: yes (which day the benches were delivered)

### retail/15#F3 · Low · "On its way" event without a time
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-04-29`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Marrowdale ring road`
- XPath: `/TransportationStatus/cbc:TransportationStatusTypeCode` = `CURRENT`
- Why: The document reports the current status; its event places the truck on the ring road but only with a date. Without a time the position cannot be related to the expected arrival at 14:00 (the issue time 11:49 is the only clue).
- Condition: the current-position event carries the time at which the truck was there.
- Options: add OccurrenceTime (e.g. 11:40).
- Needs decision: no

## Checked and consistent
- TransportationStatusRequestDocumentReference `LD-DOC-26-0232` resolves to 14, issued 50 minutes earlier; status type `CURRENT` with an updated delivery event answers 14's question "When will the benches arrive?" within its requested period (2026-04-29 to 2026-04-30).
- Consignment `LD-CS-26-0228` agrees with 11–14 and 16.
- The ring road of Marrowdale fits a truck that has just left the distribution centre in Marrowdale (11's FromLocation).
