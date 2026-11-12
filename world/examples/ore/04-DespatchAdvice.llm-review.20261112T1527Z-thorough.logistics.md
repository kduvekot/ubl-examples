# LLM review: 04-DespatchAdvice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/04-DespatchAdvice.xml`, Git blob `91b2319d44d11307c315fd3ed9bfda3c8f447141` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### ore/04#F1 · Medium · Shipment gross weight leaves out the wagons
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `1788400`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `1788.4`
- Why: `Shipment/GrossWeightMeasure` is "the total gross weight of a shipment; the weight of the goods
  plus packaging plus transport equipment". The value equals the despatched quantity of ore
  (1788.4 t = 1 788 400 kg), so it is the net weight of the loose goods. With 30 wagons
  (`/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One train: 30 wagons of about 60 tonnes.`) and a
  tare of about 22–25 t per four-axle ore wagon (own knowledge), the weight including the transport
  equipment is about 1788.4 + 30 × 22…25 = 2448–2538 t. The same value is in
  `05-Waybill.xml:/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `1788400`.
- Condition: the shipment gross weight includes the wagons, or the 1788.4 t is given in an element
  whose definition excludes the equipment (e.g. `Consignment/GrossWeightMeasure`, "excluding the
  carrier's equipment", or a net weight).
- Options: (a, preferred) state the ore weight as `Consignment/cbc:GrossWeightMeasure` (and/or
  `NetWeightMeasure`), as 02/03 already do, and drop the shipment gross weight or give it with the
  wagons' tare; (b) keep the shipment weight and add the tare of the 30 wagons.
- Needs decision: no

### ore/04#F2 · Low · The despatch itself is not described
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `SM-SH-26-0309`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One train: 30 wagons of about 60 tonnes.`
- Why: a despatch advice is "used to describe the despatch or delivery of goods". The shipment
  carries no despatch date or time, no place of despatch, and the 30 wagons appear only in a line
  note, not as transport equipment or handling units with their identifiers and loaded weights. The
  consignee, asked to "check the goods on arrival and report any damage on the consignment note"
  (`/DespatchAdvice/cbc:Note[2]`), has no wagon list to check against. That the despatch took place on
  the issue date would be implied by absence.
- Condition: the despatch advice states when (and from where) the goods were despatched, and the
  wagons are identifiable in structured form, or a reference to the wagon list is given.
- Options: (a, preferred) `Shipment/Delivery/Despatch/ActualDespatchDate` (and time) at the mine
  siding, and the wagons as `TransportHandlingUnit`/`TransportEquipment` with their numbers and
  loaded weights; (b) at least the despatch date and a reference to the carrier's wagon list
  `FRC-WAGON-LIST-11` (03-TransportExecutionPlan.xml).
- Needs decision: no

### ore/04#F3 · Low · Item number in the world's item scheme is a valid GTIN-12 in the real UPC range
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771010000013`
- Why: as in 01-Order.xml: a twelve-digit number with a correct GTIN-12 check digit (3), read as
  GTIN-13 `0771010000013` with GS1 US prefix 077; could be mistaken for a real GTIN without the
  schemeID (own knowledge of GS1 prefix ranges, no register lookup). 64 examples use the world item
  scheme.
- Condition: the item number cannot be read as a valid GTIN in a real prefix range, or a decision
  records why it is safe.
- Options: (a, preferred) change the world scheme's number form; (b) record the decision.
- Needs decision: yes

## Checked and consistent
- Physics: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `1788.4` t over 30 wagons is
  59.61 t per wagon, matching "about 60 tonnes"; 30 × 60 t = 1800 t ordered, so 11.6 t (0.64 %)
  short, a normal loading tolerance for bulk. 60 t of lump ore at 2.3–2.8 t/m³ is 21–26 m³ per wagon,
  well within an open ore wagon; 82–85 t gross per four-axle wagon, 20.5–21.3 t per axle.
- References: `VI-PO-26-0304` resolves to 01-Order.xml, order line `1` exists, and item, HS and CPC codes
  agree with it. Shipment `SM-SH-26-0309` and consignment `VI-CS-26-0306` agree with 05-Waybill.xml
  and 02/03.
- Times: issued 2026-03-10 15:37, after the waybill (2026-03-10 11:35) and inside the transport window.
- Carrier `Ferrano Rail Cargo` agrees with 01, 03 and 05.

## Considered and refuted
- `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `1788.4` against the ordered 1800 t
  without an outstanding quantity: suspected missing backorder information — refuted because a
  0.64 % difference on a bulk train is within loading tolerance and is invoiced as despatched in
  07-Invoice.xml.
