# LLM review: 09-TransportationStatus.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/09-TransportationStatus.xml`, Git blob `e1a610d76310b4d013c2aaf846292a8900b63b3e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### road/09#F1 · High · Import declaration reported accepted before it was issued
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:SubStatus/cbc:Description` = `Import declaration accepted by Bayvarra's customs.`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:StatusReason` = `Customs released the goods at the border.`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceTime` = `08:55:00`
- XPath: `/TransportationStatus/cbc:IssueTime` = `09:10:00`
- Why: The report, issued on 2026-03-24 at 09:10, says that the border crossing was completed at 08:55 with the goods released and the import declaration accepted by Bayvarra's customs. The import declaration of this shipment is issued only at 09:54 that day (`10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cbc:IssueTime` = `09:54:00`, issue date 2026-03-24). A declaration cannot be accepted, and the goods released on it, before it is lodged.
- Condition: the import declaration's issue time precedes the release and acceptance reported here (and this report's issue time).
- Options: (a) preferred: issue the import declaration before the truck reaches the border (e.g. 2026-03-24 07:00 or the evening before; a pre-lodged declaration fits "the import by the distributor at the border"); (b) move the border crossing and this report after 09:54, which also moves the delivery chain.
- Needs decision: no

### road/09#F2 · Medium · Consignment ID given as the shipping order number
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0152`
- Why: ShippingOrderID is "a reference number for a shipping order". LD-CS-26-0152 is the consignment ID (`/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0152`). The order the carrier works under is the transport request `03-TransportExecutionPlanRequest.xml` (LD-TR-26-0151). The same misuse is in `08-Waybill.xml`.
- Condition: ShippingOrderID is the shipping order / transport request number (LD-TR-26-0151) or is absent.
- Options: (a) preferred: LD-TR-26-0151; (b) remove it.
- Needs decision: no

### road/09#F3 · Medium · Status location is the carrier's name
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Trasvia Haulage`
- Why: StatusLocation is one of the "locations associated with this Transportation Status report", i.e. where the status applies. The status is the border crossing and the truck being "in transit in Bayvarra"; "Trasvia Haulage" is the carrier, a party already given as ResponsibleParty and sender, and says nothing about a place.
- Condition: StatusLocation names or identifies a place the status refers to (the border crossing, or the truck's current position), or is absent.
- Options: (a) preferred: the border crossing (with an identifier, if the border post gets one in the customs documents) or the truck's position; (b) remove StatusLocation, since the event already has a location.
- Needs decision: no

### road/09#F4 · Low · Temperature range for goods that need no temperature control
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:Condition[2]/cbc:Description` = `No protection needed for steel benches.`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:Condition[2]/cbc:MinimumMeasure` = `4`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:Condition[2]/cbc:MaximumMeasure` = `18`
- Why: The condition gives a transport temperature with a range of 4–18 °C, as if the goods had to be kept within it, while its own description says the benches need no protection. Galvanised steel benches with hardwood slats in an unheated curtain-sider in March need no range; nothing else in the flow (request, waybill) states a temperature requirement.
- Condition: a temperature range is given only if the goods have one; otherwise the condition is absent (or gives only a measured value with a reason to report it).
- Options: (a) preferred: remove Condition[2]; (b) keep only the measured 14 °C if the tracking system reports it routinely, without a range.
- Needs decision: no

## Checked and consistent
- Consignment, carrier-assigned ID TH-26-04471, shipment CL-SH-26-0154 and the waybill reference TH-WB-26-0159 resolve to `08-Waybill.xml`.
- Updated pickup 2026-03-23 15:05 equals the waybill's actual pickup; updated delivery 2026-03-25 09:30 lies in the waybill's estimated delivery period 09:00–11:00 and before the required 10:00; the actual delivery is 09:40 (`11-ReceiptAdvice.xml`).
- Border event 07:30–08:55 on 2026-03-24 contains the waybill's seal check at 07:45; "all 25 pallets on board" equals the waybill's 25 handling units; the 70 % progress at the border is plausible.
- Status ONTIME against the reference 2026-03-25 10:00 equals the required delivery time.

## Considered and refuted
- `/TransportationStatus/cac:UpdatedPickupTransportEvent`: an "updated" pickup that already happened — refuted because reporting the pickup as it actually happened is an update of the planned 14:00 pickup, which it differs from.

## Outside this review
- Timeline: `/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cbc:Text` = `Driver resting in Marrowdale tonight under the driving-time rules.` The whole trip is 186 km (`14-Invoice.xml`), about three hours of driving; after crossing the border at 08:55 the truck could reach Marrowdale in the morning of 2026-03-24. The overnight wait is caused by the delivery slot on 2026-03-25, not by driving-time rules; and the departure at 16:20 the day before with the border reached only at 07:30 implies an overnight stop on the Urvanian side as well. For the cross-document timeline review.
