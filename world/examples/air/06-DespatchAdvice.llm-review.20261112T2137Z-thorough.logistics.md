# LLM review: 06-DespatchAdvice.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/06-DespatchAdvice.xml`, Git blob `b0da93c08c27cd4207d5ea850651a870b97f6b62` (committed)
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

### air/06#F1 · High · Reference to an order VT-PO-26-0319 that does not exist
- XPath: `/DespatchAdvice/cac:OrderReference/cbc:ID` = `VT-PO-26-0319`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:OrderReference/cbc:ID` = `VT-OC-26-0320`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:OrderReference/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: OrderReference is "A reference to an Order with which this Despatch Advice is associated".
  No example has the ID VT-PO-26-0319 (`grep -rn --include='*.xml' VT-PO-26-0319 world/examples`:
  only references, in air/03, air/06 and air/08). The frames were ordered by the order change
  VT-OC-26-0320 (air/01) to order VT-PO-26-0127 (sea/05-Order.xml), and the fulfilment cancellation
  air/07 gives exactly these two as the order of the despatch it cancels, so the flow contradicts
  itself about which order this despatch belongs to.
- Condition: the order reference resolves to VT-PO-26-0127 (with the order change VT-OC-26-0320
  where the element allows it), the same as in air/07.
- Options: OrderReference ID VT-PO-26-0127 and DocumentReference VT-OC-26-0320 inside it, as air/07
  has (preferred); or add an order VT-PO-26-0319 to the flow, which changes the story.
- Needs decision: no

### air/06#F2 · High · The order line reference points to the bench line of the order
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cbc:Name` = `Bench side frame casting`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- Why: OrderLineReference/LineID is "An identifier for the referenced order line, assigned by the
  buyer". In order VT-PO-26-0127 line 1 is the 96 benches; the frames are line 2 (12 by sea) and the
  8 added by the order change, which reuses ID 1 (air/01#F1).
- Condition: the line reference carries the line ID of the added side-frame line as fixed in air/01.
- Options: follow air/01#F1 (preferred: line 3).
- Needs decision: no

### air/06#F3 · High · The same eight serial numbers have a different manufacture date in air/08
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-03190`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[8]/cbc:SerialID` = `VI-SF-03197`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[8]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `08-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-11`
- Why: ItemInstance is "A trackable, unique instantiation of this item" and ManufactureDate "The date
  on which this item instance was manufactured". Both despatch advices list the same eight castings
  (SerialID VI-SF-03190 to VI-SF-03197, the same trace and registration IDs and melt M-26-0412), all
  at 06:40, but this one says they were made on 2026-05-10 and air/08 on 2026-05-11. The castings did
  not change between the two advices (air/07: the same cargo goes on a later flight). The difference
  holds for all eight instances.
- Condition: every item instance has the same manufacture date and time in air/06 and air/08.
- Options: one date in both (preferred: 2026-05-10, so that the frames exist before the order change of
  2026-05-11 07:50 and come from stock); or 2026-05-11 in both.
- Needs decision: no

### air/06#F4 · Medium · The advice does not say when the goods leave or arrive, nor by which transport document
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Kelaro Air Cargo`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Eight side frames, needed before the ship arrives.`
- Why: A Despatch Advice is "used to describe the despatch or delivery of goods"; the receiver
  (Nalevi Warehousing) uses it to prepare for the goods. This one has the carrier but no despatch
  date (Shipment/Delivery/Despatch/ActualDespatchDate), no estimated delivery (Delivery/EstimatedDeliveryPeriod),
  no transport mode and no reference to the air waybill (KXL-WB-26-0325, AWB KXL-AWB-26-0319) or
  to the skid's SSCC 095206103190000015 from air/03, by which the warehouse would collect and
  identify the goods at Selanu airport. The line note says time is the point of the delivery.
- Condition: the advice states the despatch date and the expected delivery date and identifies the
  goods for collection (waybill reference and/or the handling unit's SSCC).
- Options: add Shipment/Delivery with despatch date and estimated delivery period, the
  TransportHandlingUnit with the SSCC, and the waybill as a document reference (preferred); at least
  the dates.
- Needs decision: no

## Checked and consistent
- Shipment LD-SH-26-0323, consignment LD-CS-26-0324, gross weight 81.6 kg and the carrier Kelaro Air
  Cargo agree with air/03 and air/04.
- DeliveredQuantity 8 EA = 8 item instances = package quantity 8 in air/03.
- The item (LD-10443, GTIN 9520610000029 with correct check digit, HS 732599) agrees with air/01.
- LineCountNumeric 1 = one despatch line.

## Considered and refuted
- `/DespatchAdvice/cbc:Note`: "report any damage on the consignment note" for an air consignment —
  refuted because the air waybill is the air consignment note (the term of the Warsaw Convention,
  still common; own knowledge), so the wording is not wrong for air.
- `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureTime` = `06:40:00`: eight castings with the same minute — refuted because
  castings of one melt (M-26-0412, the same for all eight) are poured together.
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Nalevi Warehousing`:
  delivery customer differs from the consignee Velumi Trading of air/03 and air/04 — refuted because
  the buyer's warehouse receives the goods for the buyer, as the order change air/01 says (DeliveryParty).

## Outside this review
- The castings are made in Urvania on 2026-05-10 or -11 and are ready in Marrowdale, Bayvarra, on
  2026-05-12 (air/03); whether that is possible is a cross-flow timeline question.
