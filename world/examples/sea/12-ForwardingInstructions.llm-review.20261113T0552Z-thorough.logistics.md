# LLM review: 12-ForwardingInstructions.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/12-ForwardingInstructions.xml`, Git blob `1f7cbe1f873685d1f9299ab7815123702e495ea9` (committed)
- Last commit changing the example: 62a1919 2026-11-12 sea/12 no longer declares a carriage value; emergency card on the secondary hazard decided
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

### sea/12#F1 · High · Shipping order ID contradicts the bill of lading's shipping order
- XPath: `/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0132`
- XPath: `/ForwardingInstructions/cbc:ID` = `BF-FI-26-0137`
- Why: `ShippingOrderID` is a "Reference number to identify a Shipping Order or Forwarding Instruction". This document is the forwarder's shipping order to the carrier, and the bill of lading records it as such (`14-BillOfLading.xml:/BillOfLading/cbc:ShippingOrderID` = `BF-FI-26-0137`). Here the same element holds `LD-SH-26-0132`, the shipment's ID (`/ForwardingInstructions/cac:Shipment/cbc:ID` = `LD-SH-26-0132`): the two documents name different shipping orders for the same booking, and an identifier of one kind is used as another.
- Condition: the shipping order ID in this document and in the bill of lading are the same and identify a shipping order or forwarding instruction.
- Options: drop `ShippingOrderID` here (preferred: the document's own ID is the shipping order, which the bill of lading quotes); or set it to `BF-FI-26-0137`.
- Needs decision: no

### sea/12#F2 · Medium · Booking with the carrier without cargo, equipment, ports or sailing
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/ForwardingInstructions/cbc:Note` = `Please confirm the booking.`
- Why: Forwarding Instructions give "instructions regarding the action to be taken for the forwarding of goods described therein"; this one, from the forwarder to Tidewell Ocean Lines, is the booking ("Please confirm the booking"). It describes no goods (no goods item, description, packages, HS code), no equipment (the 40-foot box asked for in `09-ForwardingInstructions.xml`), no port of loading or discharge and no sailing, only a gross weight. A carrier cannot book a slot or plan stowage from it, yet the bill of lading later shows a confirmed booking `TWL-BK-26-55710` on vessel `Tidewell Harbour`, voyage `TH-26-19E`.
- Condition: the booking states the cargo (description, packages, gross weight), the equipment (one `42G1`), the ports (`XBLMP` to `XLSEL`) and the requested sailing or date.
- Options: add a goods item per product, the requested transport equipment and a main-carriage stage with ports and requested departure (preferred); or reference the transport service description `TOL-DOC-26-0130` for the service and add the cargo.
- Needs decision: no

### sea/12#F3 · Medium · Shipment gross weight excludes the transport equipment its definition includes
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". 4,106.4 kg is goods plus packaging; with the 40-foot box the shipment weighs 7,856.4 kg (`10-PackingList.xml:/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`).
- Condition: the shipment's gross weight includes the transport equipment, or the goods weight is carried by goods items.
- Options: carry the weight on goods items (preferred, see F2); or 7,856.4 kg.
- Needs decision: no

### sea/12#F4 · Low · Carrier's booking number in the request that asks for the booking to be confirmed
- XPath: `/ForwardingInstructions/cbc:CarrierAssignedID` = `TWL-BK-26-55710`
- XPath: `/ForwardingInstructions/cbc:Note` = `Please confirm the booking.`
- Why: the carrier assigns the booking number when it accepts the booking; the bill of lading carries it as the carrier's ID (`14-BillOfLading.xml:/BillOfLading/cbc:CarrierAssignedID` = `TWL-BK-26-55710`). A request that still asks the carrier to confirm the booking cannot already carry the number the confirmation produces, unless the slot was pre-booked, which nothing in the flow says.
- Condition: either the instructions follow a booking the carrier already confirmed (and do not ask for confirmation), or they carry no carrier-assigned ID.
- Options: drop the carrier-assigned ID here (preferred: the booking number first appears on the carrier's side); or change the note to refer to the confirmed booking.
- Needs decision: no

### sea/12#F5 · Low · Document reference to the buyer's order without saying it is the order
- XPath: `/ForwardingInstructions/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: a plain `DocumentReference` with only an ID, sent to the carrier, which has no relation to the buyer's purchase order (`05-Order.xml`); it cannot tell what the reference is.
- Condition: the reference states its document type, or is removed if the carrier does nothing with it.
- Options: add `DocumentTypeCode` `220` (preferred if the order number is wanted on the bill of lading); or drop the reference.
- Needs decision: no

## Checked and consistent
- Shipment `LD-SH-26-0132` and consignment `LD-CS-26-0133` are those of the shipper's instructions `09-ForwardingInstructions.xml`, issued the evening before (2026-05-09 16:45).
- The bill of lading references this document (`14-BillOfLading.xml:/BillOfLading/cac:DocumentReference/cbc:ID` = `BF-FI-26-0137`).

## Considered and refuted
- `/ForwardingInstructions/cbc:ID` = `BF-FI-26-0137`, dated 2026-05-10, while the forwarder's export declaration `BF-EX-26-0135` is dated 2026-05-12: suspected a number series running backwards in time — refuted because the flow's numbers form one running counter over all issuers and document types (0123 to 0154), not a per-issuer series whose order would have to follow the dates.

## Outside this review
- The booking is issued after the booking deadline of the transport service description (`08-TransportServiceDescription.xml`, nomination 2026-05-09 10:00); recorded as a finding in that example's review.
