# LLM review: 07-BillOfLading.xml

Flow: reefer (BYF-TX-26-2160) · Review date: 2026-11-21 · Part: single

## Reviewed version
- Run: `20261121T1048Z-quick`
- Example: `world/examples/reefer/07-BillOfLading.xml`, Git blob `42c79ff38a6feddc3a67cda4234ffd6e404af843` (committed)
- Last commit changing the example: d34fe695 2026-11-21 O277 (3): UBL's spelling "despatch" for UBL concepts, and a published-text rule for it
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

### reefer/07#F1 · Low · A bill of lading of which no original is issued
- XPath: `/BillOfLading/cbc:OtherInstruction` = `Express release: no original issued; the reefer is released at Selanu to the consignee named.`
- XPath: `/BillOfLading/cbc:ToOrderIndicator` = `false`
- Why: UBL defines the Bill of Lading as the document by which "the carrier undertakes to deliver the goods against surrender of the document". A carrier's transport document that is not negotiable, of which no original is issued and against which the goods are released to the named consignee without surrender, is a sea waybill (UBL's Waybill), not a bill of lading (own knowledge: an "express" or "telex" release normally means originals were issued and surrendered at origin, which the instruction excludes). The document type and the instruction tell two different stories.
- Condition: the document type and the release instruction agree: either a bill of lading whose originals are issued (and, for an express release, surrendered at origin), or a waybill for release to the named consignee without originals.
- Options: (a) keep the bill of lading and say the originals were issued and surrendered at Lumeport before the express release (preferred if the flow is meant to show a bill of lading); (b) issue the carrier's document as a Waybill, which fits a straight consignment to a known buyer in two days' sailing.
- Needs decision: yes

### reefer/07#F2 · Low · A daily rate given as the amount of a charge
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:ServiceAllowanceCharge/cbc:AllowanceChargeReason` = `Reefer power and monitoring at Selanu after discharge, a day`
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:ServiceAllowanceCharge/cbc:Amount` = `45.00`
- Why: AllowanceCharge/Amount is "the monetary amount of this allowance or charge to be applied", not a rate. The reason text makes 45.00 a price per day, but the number of days is unknown when the bill is issued (the charge is collect from the consignee, `/BillOfLading/cac:Shipment/cac:Consignment/cac:CollectPaymentTerms/cbc:Note` = `Reefer power and monitoring at Selanu after discharge collect from the consignee.`), so the amount stated is not the amount that will be charged. The reefer is on the port's power from 26 April 08:25 until it leaves on 27 April (`10-TransportationStatus.xml`).
- Condition: the allowance charge's Amount is the amount charged, with any rate expressed as a rate (e.g. a base amount and multiplier, or a note on the tariff), or the per-day tariff is stated outside the amount.
- Options: (a) state the rate in the reason text or the tariff and leave the amount to the carrier's invoice to the consignee (preferred: the bill is issued before the days are known); (b) state the expected charge for the planned stay (one day) as the amount.
- Needs decision: no

### reefer/07#F3 · Low · Arrival at the buyer's cold store recorded as a receipt event
- XPath: `/BillOfLading/cac:Shipment/cac:Consignment/cac:OnCarriageShipmentStage/cac:ReceiptTransportEvent/cac:Location/cbc:Name` = `Hafefo Fresh Produce, cold store, Selanu`
- Why: ShipmentStage has ReceiptTransportEvent ("the receipt of goods in this shipment stage", the carrier taking over the goods at the start of the stage) and DeliveryTransportEvent ("the delivery of goods in this shipment stage"). The on-carriage by road from the port to the cold store starts at the port of Selanu and ends at the cold store; what happens at the cold store on 27 April is the delivery of that stage, not its receipt. The pre-carriage stage of the same document uses DropoffTransportEvent at its end.
- Condition: the event at the end of the on-carriage, at the cold store, is the stage's delivery (or drop-off) event; a receipt event, if kept, is at the port where the on-carrier takes the reefer over.
- Options: (a) use DeliveryTransportEvent for the cold store (preferred); (b) keep a receipt event at Selanu port and add the delivery.
- Needs decision: no

## Checked and consistent
- VGM: 21,728 kg cargo + 4,800 kg tare = 26,528 kg = `/BillOfLading/cac:Shipment/cbc:GrossWeightMeasure` = `26528` = equipment gross = verified gross mass; method SM2 (calculated from weighed packages plus tare) fits a pallet scale; a 4.8 t tare is typical for a 40-foot high-cube reefer (own knowledge).
- Shipment counts: one goods item, one consignment, 20 handling units of 56 cartons, as in `06-DespatchAdvice.xml`; SSCC and container check digits pass.
- Freight: 4,400.00 + 400.00 bunker prepaid, consistent with the export value of `05-ExportCustomsDeclaration.xml` (see its review).
- Times: acceptance and drop-off at Lumeport 22 April 17:40; bill issued 23 April 14:30, before the estimated departure 18:00 in `05-ExportCustomsDeclaration.xml`; "shipped on board" fits.
- Vessel data agree with `05-ExportCustomsDeclaration.xml`; seal, container and temperatures agree with `03-ForwardingInstructions.xml` and `06-DespatchAdvice.xml`.

## Considered and refuted
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:DeliveryTerms/cbc:LossRisk` = `Risk passes when the reefer is handed to the carrier at Lumeport.`: under CIP the risk passes at the first carrier, which would be the pre-carriage truck at Harrowmead — refuted: Incoterms 2020 lets the parties agree a specific point of delivery, and the truck is merchant haulage the seller arranges (`03-ForwardingInstructions.xml`, MERCHHAUL), so handing over to the ocean carrier at Lumeport is a legitimate agreed point.
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:ExtraAllowanceCharge/cbc:AllowanceChargeReasonCode` = `FC`: a bunker surcharge coded as "freight service" — refuted: UN/EDIFACT 7161 has no bunker code, and the surcharge is part of the freight.
- `/BillOfLading/cac:Shipment/cac:Consignment/cac:OnCarriageShipmentStage/cac:CarrierParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`: a port-to-port carrier's bill naming the consignee's road haulier — refuted: the stages are given as information for the merchant haulage at both ends, and the on-carrier is the consignee's.
