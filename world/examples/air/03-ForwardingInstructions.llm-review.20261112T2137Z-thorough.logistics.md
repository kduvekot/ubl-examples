# LLM review: 03-ForwardingInstructions.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/03-ForwardingInstructions.xml`, Git blob `0b8c1e57de771a3aa28a4f5ad2687ce72817a1ac` (committed)
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

### air/03#F1 · High · Reference to an order VT-PO-26-0319 that does not exist
- XPath: `/ForwardingInstructions/cac:DocumentReference/cbc:ID` = `VT-PO-26-0319`
- XPath: `01-OrderChange.xml:/OrderChange/cac:OrderReference/cbc:ID` = `VT-PO-26-0127`
- XPath: `01-OrderChange.xml:/OrderChange/cbc:ID` = `VT-OC-26-0320`
- Why: No example has the document ID VT-PO-26-0319 (searched `grep -rn --include='*.xml'
  VT-PO-26-0319 world/examples`: it occurs only as a reference, here and in air/06 and air/08). The
  goods are the 8 side frames that the buyer's order VT-PO-26-0127 (sea/05-Order.xml) was changed to
  include by order change VT-OC-26-0320 (air/01). The number looks like a separate air purchase order
  that the flow never issues.
- Condition: the reference resolves to a document of the flow or of sea/05-Order.xml, the order
  that the goods belong to (VT-PO-26-0127, and/or the order change VT-OC-26-0320).
- Options: (a) preferred: refer to VT-PO-26-0127 and VT-OC-26-0320, the documents the flow has;
  (b) add an air purchase order VT-PO-26-0319 to the flow, which changes the story.
- Needs decision: no

### air/03#F2 · High · The box cannot hold the goods: 0.072 m³ of box for 0.42 m³ of frames
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:MeasurementDimension[1]/cbc:Measure` = `800`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:MeasurementDimension[2]/cbc:Measure` = `300`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:MeasurementDimension[3]/cbc:Measure` = `300`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cbc:Quantity` = `8`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cbc:NetVolumeMeasure` = `0.42`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:GrossVolumeMeasure` = `0.576`
- Why: MeasurementDimension is "A measurable dimension … of this package". The box LD-AIR-BOX is
  800 × 300 × 300 mm = 0.8 × 0.3 × 0.3 = 0.072 m³ and is said to contain all 8 frames, whose net
  volume ("excluding packaging") the consignment gives as 0.42 m³, almost six times the box. The
  waybill gives 0.576 m³ gross for the consignment (which with 96 kg chargeable weight is the IATA
  6000 cm³/kg rule, own knowledge: 576 000 / 6000 = 96), so the handling unit is far larger than the
  box. In addition, a Serra 180 bench is 620 mm deep and 780 mm high (sea/05-Order.xml, item
  dimensions); an end frame spanning these (own reading of what a bench side frame is) cannot lie in
  a 300 × 300 mm cross-section.
- Condition: the package dimensions give a volume at least the goods' net volume, and are consistent
  with the waybill's gross volume and the frame size (or the net volume is corrected to what fits).
- Options: (a) preferred: dimension the packing as it must be for 8 frames of about 0.0525 m³ each
  (e.g. a box or crate of about 1200 × 800 × 600 mm = 0.576 m³ on the skid, matching the waybill);
  (b) lower the net volume, if the frames really nest into 0.072 m³, and then the waybill's gross
  volume and chargeable weight change too.
- Needs decision: no

### air/03#F3 · Medium · The instructions do not say how, from where or to where the goods are to be forwarded
- XPath: `/ForwardingInstructions/cac:Shipment/cbc:ID` = `LD-SH-26-0323`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:Delivery/cac:RequestedDeliveryPeriod/cbc:EndDate` = `2026-05-14`
- XPath: `/ForwardingInstructions/cbc:Description` = `Instructions for the shipment to the island.`
- Why: Forwarding Instructions give "instructions regarding the action to be taken for the forwarding
  of goods". This one has no transport mode, no shipment stage, no origin or destination location,
  no delivery address and no delivery terms: the forwarder learns from the structured data that 8
  frames are ready at a dispatch area and must be delivered on 2026-05-14, but not that they go by
  air (the reason for the whole flow), from which airport, to which airport or to whom at delivery
  (Nalevi Warehousing in the despatch advices, Velumi Trading as consignee here). "To the island" is
  the only hint.
- Condition: the instructions state at least the transport mode (air), the place of departure
  (origin or loading airport) and the destination (Selanu airport, XLSLA, and/or the delivery party),
  in the structured elements for them (e.g. Shipment/ShipmentStage with TransportModeCode and
  locations, Consignment/Delivery, DeliveryTerms CPT Selanu airport).
- Options: add a main-carriage ShipmentStage (mode 4, loading XBLMA, unloading XLSLA) and the
  delivery terms (preferred, they match air/04); or a Delivery with location and party.
- Needs decision: no

### air/03#F4 · Medium · A transport event with date and time but no type or location
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-13`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportEvent/cbc:OccurrenceTime` = `19:00:00`
- XPath: `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportEvent/cbc:CompletionIndicator` = `false`
- Why: Consignment/TransportEvent is "any additional significant occurrences … not specified
  elsewhere". Without TransportEventTypeCode, Description or Location the event says nothing: it
  could be a cut-off for acceptance, a requested pickup or a departure. It also matches no other
  time of the flow: the requested despatch is 2026-05-13 (no time), the waybill's flight departs
  2026-05-14 07:00 (air/04), and the order response speaks of a "morning flight".
- Condition: the event has a type (and a location where it happens) that tells what happens at
  2026-05-13 19:00, or it is not in the document.
- Options: type it (e.g. latest acceptance at the origin cargo terminal, with its location; preferred,
  it fits a 07:00 flight next morning); or drop it.
- Needs decision: no

### air/03#F5 · Medium · Instruction to send a bill of lading for an air consignment
- XPath: `/ForwardingInstructions/cbc:OtherInstruction` = `Send the bill of lading to the forwarder.`
- XPath: `04-Waybill.xml:/Waybill/cbc:WaybillTypeCode` = `AWB`
- Why: The goods go by air; the transport document is the air waybill air/04 ("Air waybill under the
  Montreal Convention"), which is not a bill of lading and not a document of title (own knowledge:
  air waybills are non-negotiable). The instruction asks for a document that does not exist for this
  consignment. The same text occurs in cotton/09-ForwardingInstructions.xml (counted with
  `grep -rn --include='*.xml' "Send the bill of lading" world/examples`: 2 files), where it may be right.
- Condition: the instruction names the transport document that this consignment gets (the air
  waybill), or is not there.
- Options: "Send the air waybill to the forwarder" (preferred); or drop the instruction.
- Needs decision: no

## Checked and consistent
- SSCC 095206103190000015: check digit correct (check_ids.py); company prefix 9520610 is that of
  the consignor's GLN 9520610900008.
- Weights: Shipment gross 81.6 kg = waybill air/04 (81.6 kg) = despatch advices air/06 and air/08
  (81.6 kg); net 76 kg = 8 × 9.5 kg, as in air/02 (see there for the derivation from
  sea/10-PackingList.xml). Gross per frame 81.6 / 8 = 10.2 kg, the same as in sea/10-PackingList.xml
  (122.4 kg for 12 frames).
- Package quantity 8, BatchQuantity 8 and the 8 items of air/06 agree; TotalGoodsItemQuantity 1 and
  ConsignmentQuantity 1 match the one goods item and the one consignment.
- Shipment LD-SH-26-0323 and consignment LD-CS-26-0324 are used with the same meaning in air/04,
  air/05, air/06, air/08, air/09 and air/10.
- Dates: earliest pickup 2026-05-12 (goods ready at the dispatch area), requested despatch
  2026-05-13, requested delivery 2026-05-14; the waybill's flight (2026-05-14 07:00–10:00) fits.

## Considered and refuted
- `/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`: the shipping order number equals
  the shipment ID — refuted because a consignor may number its shipping order with its own shipment
  number; it is a reference the forwarder can quote. (The waybill and the status reports quote a
  different number, see air/04 and air/05.)
- Gross minus net: 81.6 − 76 = 5.6 kg for a skid, a box and bags — refuted as a finding: a small
  wooden skid of about 3–4 kg and a corrugated box of about 1–1.5 kg (own estimates) and light bags
  fit 5.6 kg; for the larger box that air/03#F2 calls for, the tare would have to be rechecked.
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:ContainedPackage/cbc:Quantity` = `8`: one bag with 8 frames inside a box of 8 frames
  looked odd — refuted because Package/Quantity is "the quantity of items contained in this package"
  and both values count the same 8 frames; one bag per frame would be clearer but nothing contradicts.
- `/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cac:Package/cac:Pickup/cbc:ID` = `BF-PU-26-0611`: a forwarder's pickup number before the booking is confirmed —
  refuted because it shares the number 0611 with the forwarder's quotation BF-QUOTE-AIR-26-0611 cited
  in air/02, so the forwarder had already assigned it when quoting.

## Outside this review
- The frames are made in Urvania (ManufactureDate 2026-05-10 in air/06) and are ready at the
  distributor's dispatch area in Marrowdale, Bayvarra, on 2026-05-12; whether that transfer is
  possible in two days is a cross-flow timeline question.
