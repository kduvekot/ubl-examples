# LLM review: 10-Invoice.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/10-Invoice.xml`, Git blob `4f8e76fdb62682517ade76167e8a942e4bcac42e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### air/10#F1 · High · Freight "per kilogram chargeable weight" is invoiced on the gross weight
- XPath: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `81.6`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Airport-to-airport air freight per kilogram chargeable weight, road feeder included.`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:ChargeableWeightMeasure` = `96`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `81.6`
- Why: The item is priced per kilogram of chargeable weight (6.8 XBL per 1 KGM). The waybill this
  invoice refers to gives a chargeable weight of 96 kg (volume weight of 0.576 m³ at 6000 cm³/kg);
  81.6 kg is the gross weight. Invoiced as described, the quantity is 96 kg and the line
  96 × 6.8 = 652.80 XBL, not 81.6 × 6.8 = 554.88 XBL.
- Condition: the invoiced quantity equals the chargeable weight of the waybill (96 kg), or the
  description says the freight is charged on gross weight.
- Options: (a) preferred: InvoicedQuantity 96 KGM with the amounts recalculated, because the
  chargeable weight is how air freight is charged (own knowledge) and the waybill states it;
  (b) change the description to gross weight, which contradicts air freight practice.
- Needs decision: no

### air/10#F2 · Low · "Road feeder included" for a carriage that has no road leg
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Airport-to-airport air freight per kilogram chargeable weight, road feeder included.`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:TransportModeCode` = `4`
- Why: The waybill has a single air stage, Lumeport airport to Selanu airport; no document of the
  flow has a road feeder service (a truck on an air waybill) or a pre-carriage to the airport. The
  service is described as airport to airport, which leaves no room for a feeder either.
- Condition: the description names only services that the transport documents show, or the waybill
  shows the road feeder leg.
- Options: drop "road feeder included" (preferred); or add the leg in air/04, which changes the story.
- Needs decision: no

### air/10#F3 · Low · Reference to a May statement that cannot exist on 15 May
- XPath: `/Invoice/cac:StatementDocumentReference/cbc:ID` = `BF-SOA-26-05`
- XPath: `/Invoice/cbc:IssueDate` = `2026-05-15`
- Why: StatementDocumentReference is "A reference to a Statement associated with this document".
  The ID reads as the forwarder's statement of account for May 2026, which would be issued at the end of
  the month, after this invoice; no statement is in the flow (`grep -rn --include='*.xml' BF-SOA-26-05
  world/examples`: only this reference). An invoice cannot point to a statement not yet drawn up,
  unless it refers to an earlier statement.
- Condition: the reference points to a statement that exists at the invoice's issue date (or is not there).
- Options: drop the reference (preferred: the invoice does not need it); or refer to an earlier
  statement, or add the statement later in the flow and let it refer to the invoice instead.
- Needs decision: yes

### air/10#F4 · Low · The delivery of the service has no date and no shipment ID
- XPath: `/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- Why: The invoice bills a transport. Its Delivery identifies the consignment and the carrier but not
  when the service was completed (Delivery/ActualDeliveryDate, the arrival on 2026-05-14 in air/09)
  nor the shipment LD-SH-26-0323 that the forwarder was instructed with (air/03), which the customer
  would use to match the invoice with its own shipment.
- Condition: the invoice states the date the service was performed (delivery date or invoice period)
  and identifies the shipment the customer knows.
- Options: add ActualDeliveryDate 2026-05-14 (or the date that air/07#F1 settles) and Shipment/ID
  LD-SH-26-0323 (preferred).
- Needs decision: no

## Checked and consistent
- `AdditionalDocumentReference/ID` KXL-WB-26-0325 resolves to air/04-Waybill.xml (issued 2026-05-13,
  before this invoice); consignment LD-CS-26-0324 and the carrier Kelaro Air Cargo agree with it.
- Seller Bayforth Forwarding is the freight forwarder of air/03 and air/04; buyer Lumeway Distribution
  is the consignor who instructed it (air/03) and, under CPT (air/01), bears the freight.
- Arithmetic of the line as it stands: 81.6 × 6.8 = 554.88 XBL = LineExtensionAmount.

## Considered and refuted
- `/Invoice/cac:AdditionalDocumentReference/cbc:ID` = `KXL-WB-26-0325`: the forwarder invoices against
  the carrier's waybill rather than its own house waybill (air/04 has a child consignment
  BF-HAWB-26-0918) — refuted as a finding of this example: for a direct air waybill, which every other
  document of the flow assumes, the carrier's waybill is the right transport document; the
  contradiction lies in air/04 (air/04#F2).
