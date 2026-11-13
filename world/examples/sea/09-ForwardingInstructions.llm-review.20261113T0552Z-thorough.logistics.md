# LLM review: 09-ForwardingInstructions.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/09-ForwardingInstructions.xml`, Git blob `ba67389d2ddd1ff0fe54f4614822678c58b812b2` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/09#F1 · Medium · Shipping order ID is the shipment's ID
- XPath: `/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0132`
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `LD-SH-26-0132`
- Why: `ShippingOrderID` is a "Reference number to identify a Shipping Order or Forwarding Instruction". The value is the identifier of the shipment (`Shipment/ID`, the same in the packing list, export declaration and bill of lading), not of an order or instruction; this forwarding instruction has its own ID `LD-FI-26-0131`, which the bill of lading records as the forwarder's reference (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cbc:FreightForwarderAssignedID` = `LD-FI-26-0131`). An identifier of one kind is used as another.
- Condition: `ShippingOrderID`, if present, identifies a shipping order or forwarding instruction, not the shipment.
- Options: drop it (preferred: the document's own `ID` already identifies this instruction); or use it for a separate shipping order number if the story has one.
- Needs decision: no

### sea/09#F2 · Medium · Forwarding instructions do not say what is to be forwarded
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:ForwarderServiceInstructions` = `Book a 40-foot container on the next sailing to Selanu, arrange the truck to the port, declare the export and insure the cargo.`
- Why: Forwarding Instructions are "A document issued to a forwarder, giving instructions regarding the action to be taken for the forwarding of goods described therein". The shipment has only a gross weight: no goods item, description, HS code, number or kind of packages, volume or value. The forwarder is asked to book a container, declare the export (which needs the goods, `11-ExportCustomsDeclaration.xml` lists two goods items) and insure the cargo (59,155.80 XBL insured, but nothing says insured as what). The places are only in the names of the pre- and on-carriage services; pickup date and requested sailing are not given ("the next sailing").
- Condition: the instructions describe the goods (at least description, quantity, packages and gross weight per goods item) and the places of pickup and delivery in structured elements.
- Options: add the two goods items (benches, side frames) with quantities, pallets and weights as in the packing list, and the pickup and delivery locations (preferred); or reference the packing list and order and state that the goods are as described there (weaker: the packing list is issued three days later).
- Needs decision: no

### sea/09#F3 · Medium · Shipment gross weight excludes the transport equipment its definition includes
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- Why: UBL defines `Shipment/GrossWeightMeasure` as "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". 4,106.4 kg is goods plus packaging only (the sum of the goods items' gross weights in `10-PackingList.xml`, 3,984 + 122.4); with the 40-foot container (tare 3,750 kg) the shipment weighs 7,856.4 kg (`10-PackingList.xml:/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`). The semantic-conformance rule applies the UBL definition even where practice reads the shipment's gross weight without the box. The same value is in the packing list, export declaration, second forwarding instructions, bill of lading and manifest.
- Condition: the shipment's gross weight includes the transport equipment, or the goods-and-packaging weight is carried in an element whose definition fits it (e.g. goods items' gross weights).
- Options: carry 4,106.4 kg as goods items' gross weights and leave the shipment's gross weight out at this stage, when no box is assigned yet (preferred); or state 7,856.4 kg once the container is known.
- Needs decision: no

### sea/09#F4 · Low · Document reference to the order without saying it is the order
- XPath: `/ForwardingInstructions/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: a plain `DocumentReference` with only an ID; the forwarder has no other way to know that `VT-PO-26-0127` is the buyer's purchase order (it resolves to `05-Order.xml`). The checklist asks that "a reference with only an ID says what it refers to where that is not obvious".
- Condition: the reference states its document type.
- Options: add `DocumentTypeCode` (e.g. UN/EDIFACT 1001 `220` Order) (preferred).
- Needs decision: no

## Checked and consistent
- Shipment `LD-SH-26-0132` and consignment `LD-CS-26-0133` are the same in the packing list, export declaration and bill of lading.
- The insured value 59,155.80 XBL is 110 % of the CIF value 53,778 XBL (goods 50,688 + freight 2,700 + bunker 250 + premium 140) on the bill of lading.
- "Load the castings last, behind the doors" agrees with the packing list's `HandlingInstructions` and with the frames being the last pallet (`025 of 025`) on the bill of lading.
- Issued 2026-05-09 16:45, after the order response (2026-05-08) and the transport service description (2026-05-09 12:03), before the forwarder's booking (`12-ForwardingInstructions.xml`, 2026-05-10).
