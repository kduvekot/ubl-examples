# LLM review: 20-DespatchAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/20-DespatchAdvice.xml`, Git blob `48649a02a6dba4b51ed92b3c8c00d3a15724cd7a` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit d34e9aa 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
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

### sea/20#F1 · Medium · The despatch advice does not say when or in what the goods are despatched
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `LD-SH-26-0132`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cbc:Note` = `One 40-foot container: 24 pallets of 4 benches.`
- Why: a despatch advice is "a document used to describe the despatch or delivery of goods". This
  one gives the items and quantities but no despatch date or expected delivery period (no
  Shipment/Delivery or Delivery/Despatch with dates), no container and no handling units: the
  container TWLU4120872 and the 25 pallets with their SSCCs (14-BillOfLading.xml) appear only as
  the free text above. The receiving 3PL, Nalevi Warehousing (DeliveryCustomerParty), is the
  party that needs exactly these data to plan and check the receipt (its receipt advice
  21-ReceiptAdvice.xml refers to this document). DespatchLine/Note is meant for information "not
  contained explicitly in other structures"; container and pallets have such structures.
- Condition: the despatch advice states the despatch date and the expected delivery (date or
  period) and identifies the container and the pallets (SSCCs) the lines are packed in.
- Options: (a, preferred) Shipment/Delivery with the despatch date (2026-05-13) and the estimated
  delivery period, Shipment/TransportHandlingUnit with the container and the 25 SSCC-labelled
  pallets, and the lines linked to them (DespatchLine/Shipment or the handling units' goods items);
  (b) at least the dates and the container ID, keeping the pallet detail in the referenced packing
  list.
- Needs decision: no

### sea/20#F2 · Medium · Shipment gross weight without the container
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- Why: Shipment/GrossWeightMeasure is "the total gross weight of a shipment; the weight of the
  goods plus packaging plus transport equipment". 4106.4 kg is the goods with packaging (benches
  3984 kg + side frames 122.4 kg, 10-PackingList.xml); with the 3750 kg container tare the shipment
  weighs 7856.4 kg
  (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`).
  The same value is in Shipment/GrossWeightMeasure of 8 examples of the flow (XPath query over
  `sea/*.xml`).
- Condition: Shipment/GrossWeightMeasure includes the container, or the goods' weight is stated in
  an element whose definition excludes it.
- Options: (a, preferred) 7856.4 kg with the container stated (see F1); (b) remove the shipment
  weight.
- Needs decision: no

### sea/20#F3 · Low · Damage to be reported "on the consignment note" of a sea shipment
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- Why: the goods travel by sea under bill of lading TOL-BL-26-0139 (14-BillOfLading.xml), with
  on-carriage by Nalevi's own transport; no consignment note exists in the flow. The receiver
  records damage in its receipt advice (21-ReceiptAdvice.xml) or on the carrier's delivery
  receipt.
- Condition: the note names a document the receiver actually has.
- Options: (a, preferred) "… report any damage in the receipt advice"; (b) name the bill of
  lading or the delivery receipt.
- Needs decision: no

## Checked and consistent
- References: order VT-PO-26-0127 (05-Order.xml) and packing list LD-PL-26-0134
  (10-PackingList.xml, issued 2026-05-12 15:59, before this advice) exist; order line IDs 1 and 2.
- Quantities: 96 benches (24 pallets × 4) and 12 side frames, equal to the packing list, the bill
  of lading (24 pallets of 4 packages + 1 pallet of 12 boxes = 25 pallets) and the import
  declaration; twelve item instances for the twelve frames, serials VI-SF-01230 to VI-SF-01241
  without gaps.
- Timing: issued 2026-05-13 08:52, after the VGM weighing of the packed container (2026-05-12
  15:30) and before the drop-off at the Lumeport terminal (2026-05-13 10:15) in
  14-BillOfLading.xml. Consignment LD-CS-26-0133 and carrier Tidewell Ocean Lines agree with it;
  DeliveryCustomerParty Nalevi Warehousing is the bill of lading's notify party and logistics
  operator.
- GTINs 9520610000012, 9520610000029 and GLN 9520610900008 pass their check digits.

## Outside this review
- The benches are described as "from the distributor's stock" in Bayvarra, but their item instance
  gives `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:ItemInstance/cbc:ManufactureDate` = `2026-05-10` at
  the manufacturer in Urvania (also for the frames), three days after the order of 2026-05-07 and
  two days before the container was weighed in Bayvarra: whether production and the Urvania–Bayvarra
  movement fit that is a timeline question across flows.
