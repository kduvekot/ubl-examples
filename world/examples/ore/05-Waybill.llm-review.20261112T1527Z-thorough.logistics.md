# LLM review: 05-Waybill.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/05-Waybill.xml`, Git blob `e7a36055c2d576e9c4683563c6c0c9a29856e375` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 560fd44 2026-11-12 Reviews of carnet and mast, run 20261112T1443Z-thorough: all merged reviews
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### ore/05#F1 · Medium · Shipping order ID holds the consignment ID
- XPath: `/Waybill/cbc:ShippingOrderID` = `VI-CS-26-0306`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cbc:ID` = `VI-CS-26-0306`
- Why: `ShippingOrderID` is "an identifier (in the form of a reference number) of the Shipping Order
  or Forwarding Instruction associated with this shipment". `VI-CS-26-0306` is the consignment's
  identifier (02, 03, 04 and this waybill's own consignment). The instruction the user gave the
  carrier is the transport execution plan request `VI-TR-26-0305`
  (02-TransportExecutionPlanRequest.xml). The consignment ID is used as a document number. The same
  pattern (ShippingOrderID equal to a consignment ID in the same document) is in 14 of the 19
  examples that carry a ShippingOrderID (lxml over `*/*.xml`).
- Condition: `ShippingOrderID` holds the identifier of a shipping order or forwarding instruction,
  or is left out.
- Options: (a, preferred) `VI-TR-26-0305`, the request that instructed the carrier (or remove it,
  since the plan is already referenced); (b) remove it.
- Needs decision: no

### ore/05#F2 · Medium · Consignment note without goods, places and wagons
- XPath: `/Waybill/cac:Shipment/cbc:ID` = `SM-SH-26-0309`
- XPath: `/Waybill/cbc:Description` = `The ore train from the mine siding to the factory.`
- Why: a waybill "states the instructions" for the shipment and describes it; a CIM consignment note
  (`/Waybill/cbc:Name` = `Rail consignment note under the CIM uniform rules`) needs at least the
  description of the goods, the place of taking over and of delivery, and the wagon numbers (CIM
  Art. 7, own knowledge). The shipment holds only its ID, a gross weight and the consignee: no goods
  item or description, no commodity code, no place of taking over or delivery, no transport mode or
  stage, no wagons. These appear only in the free-text description. The consignee is asked to check
  the goods and report damage on this note (04-DespatchAdvice.xml), which it cannot do against
  anything structured.
- Condition: the waybill's shipment describes the goods (description, HS code), the places of taking
  over and delivery, and the wagons (number and identifiers) in structured form.
- Options: (a, preferred) `GoodsItem` with the ore description and `260111`, `ShipmentStage` (rail)
  or `Delivery`/`Despatch` with the two sidings, `TransportHandlingUnit`/`TransportEquipment` for the
  30 wagons with their numbers and loaded weights; (b) at minimum the goods item and the two places,
  with a reference to the wagon list.
- Needs decision: no

### ore/05#F3 · Medium · Shipment gross weight leaves out the wagons
- XPath: `/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `1788400`
- Why: `Shipment/GrossWeightMeasure` is "the weight of the goods plus packaging plus transport
  equipment". 1 788 400 kg is the despatched ore alone
  (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `1788.4` t);
  with 30 wagons of about 22–25 t tare (own knowledge) the weight including equipment is about
  2448–2538 t.
- Condition: the shipment gross weight includes the wagons, or the ore weight is given as consignment
  gross weight (which excludes the carrier's equipment) or net weight.
- Options: (a, preferred) `Consignment/cbc:GrossWeightMeasure` = 1788400 kg, as in 02/03;
  (b) add the wagons' tare to the shipment weight.
- Needs decision: no

### ore/05#F4 · Low · Three originals announced, one listed
- XPath: `/Waybill/cbc:Note[2]` = `Three originals: consignor, consignee, carrier.`
- XPath: `/Waybill/cac:DocumentDistribution[1]/cbc:DistributionTypeCode` = `ORIGINALWITHGOODS`
- XPath: `/Waybill/cac:DocumentDistribution[2]/cbc:DistributionTypeCode` = `ELECTRONICCOPY`
- Why: the note names three originals (consignor, consignee, carrier), but the distribution list has
  one original (to the consignee) and an electronic copy, again to the consignee
  (`/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyName/cbc:Name` = `Valdara Industries`). The
  consignor's original (the CIM duplicate) is not listed.
- Condition: the distribution list and the note agree on who receives which original or copy.
- Options: (a, preferred) list the consignor's original (Serravona Mining) and drop or justify the
  consignee's extra electronic copy; (b) change the note to what the list says.
- Needs decision: no

### ore/05#F5 · Low · Issue location names the consignor, reference with only an ID
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Serravona Mining`
- XPath: `/Waybill/cac:DocumentReference/cbc:ID` = `FRC-TEP-26-0307`
- Why: the place of issue is the mine siding (the consignor's physical location `XUSRV`, "The mine and
  its rail siding"), but the location carries the company name and no identifier (46 places in 25
  examples have a party name as location name, lxml over `*/*.xml`). The generic document reference
  does not say it is the transport execution plan; it resolves to 03-TransportExecutionPlan.xml only
  by its number.
- Condition: the issue location names (or identifies) the place; the document reference states its
  type.
- Options: (a, preferred) "Serravona mine siding" with `cbc:ID` `XUSRV`; `DocumentTypeCode` on the
  reference; (b) leave the reference and fix only the location.
- Needs decision: no

## Checked and consistent
- Waybill type `CIM` (rail consignment note) fits a rail carriage; carrier, consignor and consignee agree
  with 02, 03 and 04; shipment ID `SM-SH-26-0309` and consignment ID `VI-CS-26-0306` agree with
  04-DespatchAdvice.xml.
- Reference `FRC-TEP-26-0307` resolves to 03-TransportExecutionPlan.xml, which is valid
  2026-03-04 to 2026-03-13; the waybill is issued 2026-03-10 11:35, the first day of the service window.
- Physics: 1788.4 t over 30 wagons = 59.61 t per wagon (04-DespatchAdvice.xml), matching the planned
  1800 t (02/03) within 0.64 %.
- The weight is known at 11:35, before the despatch advice (15:37), consistent with weighing at the
  siding before departure.

## Considered and refuted
- `/Waybill/cbc:AdValoremIndicator` = `false`: suspected filler — refuted because no value is declared
  for the carriage, so "false" states that no ad valorem charge applies.

## Outside this review
- When the train arrived at the factory, and so whether the bonus or the penalty of
  03-TransportExecutionPlan.xml applies, is not recorded in any document of the flow (timeline across
  documents).
