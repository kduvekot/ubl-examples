# LLM review: 01-OrderChange.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/01-OrderChange.xml`, Git blob `16f89e4161a30f6558c8105aa5b37873619d1f2c` (committed)
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

### air/01#F1 · High · The added line reuses the ID of the existing bench line of the order
- XPath: `/OrderChange/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- XPath: `/OrderChange/cbc:Note[2]` = `Add eight side frames by air; the rest of the order is unchanged.`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cbc:ID` = `1`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[2]/cac:LineItem/cbc:ID` = `2`
- Why: OrderLine in an Order Change is "An association to one or more (changed) Order Lines", and
  LineItem/ID is "An identifier for this line item, assigned by the buyer". The order being changed
  (`OrderReference/ID` VT-PO-26-0127, sea/05-Order.xml) already has line 1 (96 Serra 180 benches)
  and line 2 (12 side frames). This change carries one line, ID 1, with 8 side frames. Read by its
  ID it replaces the bench line with 8 side frames, which contradicts the note ("add …; the rest of
  the order is unchanged") and the anticipated total, which still includes the 96 benches. The same
  line ID 1 is carried on in air/02-OrderResponse.xml and in the order line references of both
  despatch advices (air/06, air/08), so the whole air flow points at the bench line.
- Condition: the added side frames have a line ID that is not used by an existing line of
  VT-PO-26-0127 (e.g. 3), and every later document of the flow that refers to this line uses that ID.
- Options: (a) preferred: give the new line ID 3 and carry it into air/02, air/06 and air/08, because
  the note says the line is added; (b) if the intent is to raise line 2 from 12 to 20 frames, use
  ID 2 with the new total quantity and change the note; this changes the story.
- Needs decision: no

### air/01#F2 · Medium · Document-level delivery terms CPT contradict "the rest of the order stays CIF"
- XPath: `/OrderChange/cac:DeliveryTerms/cbc:ID` = `CPT`
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryTerms/cbc:SpecialTerms` = `The rest of the order stays CIF by sea.`
- XPath: `sea/05-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `CIF`
- Why: The document-level DeliveryTerms is "A set of delivery terms associated with this document",
  i.e. the order as changed. Set to CPT (Selanu airport) it changes the terms of the whole order,
  while the special terms say the rest of the order stays CIF (Port of Selanu, as in
  sea/05-Order.xml). The CPT terms belong only to the air delivery, which `cac:Delivery/cac:DeliveryTerms`
  already states. The same CPT also appears at line level in air/02-OrderResponse.xml, which is the
  right place there.
- Condition: the CPT terms are attached only to the air delivery or the added line; nothing at
  document level says the whole order is CPT, or the document-level terms are CIF as in the order.
- Options: (a) preferred: drop the document-level DeliveryTerms and keep CPT in Delivery/DeliveryTerms
  (or on the line, as air/02 does), with the airport as its DeliveryLocation; (b) keep the
  document-level CIF of the original order and CPT on the air delivery.
- Needs decision: no

### air/01#F3 · Low · The airport is named only by a description, without its UN/LOCODE
- XPath: `/OrderChange/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Selanu airport, cargo terminal`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:ID` = `XLSLA`
- Why: The named place of a CPT term is the place the risk passes; the same airport is identified as
  UN/LOCODE XLSLA in air/04-Waybill.xml. The checklist asks for the identifier where the same
  place is identified elsewhere.
- Condition: the delivery location carries `cbc:ID` XLSLA (schemeID UN/LOCODE) or an equivalent
  identifier, and its name as `cbc:Name`.
- Options: add ID and Name (preferred); keep the description as additional text.
- Needs decision: no

### air/01#F4 · Low · The change gives no requested delivery date, although urgency is the reason for it
- XPath: `/OrderChange/cac:Delivery/cac:DeliveryTerms/cbc:ID` = `CPT`
- XPath: `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Eight side frames, needed before the ship arrives.`
- Why: The change asks for frames by air because they are needed before the sea shipment arrives
  (as the despatch advice says). The Delivery carries a carrier, a delivery party and terms, but no
  RequestedDeliveryPeriod (or a latest delivery date on the line), so the seller cannot tell from the
  change by when the frames are needed. The forwarding instructions (air/03) later request delivery
  on 2026-05-14, a date that appears in no ordering document.
- Condition: the change states by when the added frames are to be delivered (Delivery/RequestedDeliveryPeriod
  or the line's delivery).
- Options: add a RequestedDeliveryPeriod ending on or before 2026-05-14 (preferred, it matches air/03);
  or state the date in the line.
- Needs decision: no

### air/01#F5 · Low · The buyer names the air carrier in a CPT order change
- XPath: `/OrderChange/cac:Delivery/cac:CarrierParty/cac:PartyName/cbc:Name` = `Kelaro Air Cargo`
- Why: Under CPT the seller contracts the carriage (here through Bayforth Forwarding, air/02 and
  air/03; the carrier is chosen in the waybill air/04). A carrier named by the buyer on 2026-05-11,
  before the seller had a quotation or booking (air/02 cites the forwarder's quote, air/03 asks for
  the booking on 2026-05-12), is either a buyer's routing instruction or data that the order change
  has no reason to carry. Own knowledge of Incoterms 2020 (CPT A4: seller contracts carriage).
- Condition: either the carrier is not named in the order change, or the change states it as the
  buyer's routing wish (e.g. in SpecialTerms).
- Options: drop CarrierParty (preferred); or keep it and say in the special terms that the buyer
  asks for this carrier.
- Needs decision: yes

## Checked and consistent
- `OrderReference/ID` VT-PO-26-0127 resolves to sea/05-Order.xml (Order, same buyer and seller,
  issued 2026-05-07, before this change of 2026-05-11).
- `Contract/ID` LD-DAG-26-0125 resolves to sea/03-DigitalAgreement.xml.
- The item (LD-10443, GTIN 9520610000029, VI-C180) is the same as line 2 of sea/05-Order.xml; check
  digits of the GTIN and the GLN pass (check_ids.py).
- DestinationCountry XL agrees with the delivery party's address (Port Wrenfield/Selanu, Lisavu)
  and with the unloading airport XLSLA in air/04.
- Quantity 8 EA agrees with air/02 (8), air/03 (package quantity 8) and air/06 and air/08
  (DeliveredQuantity 8).

## Considered and refuted
- `/OrderChange/cac:Delivery/cac:NotifyParty/cac:PartyName/cbc:Name`: notify party equal to the
  delivery party, possibly redundant — refuted because under CPT to the airport the warehouse has to
  be told when to collect the frames at the cargo terminal, which is a real reason to notify it.
- `/OrderChange/cbc:SalesOrderID` = `LD-SO-26-0123`: the definition here is "An identifier for the
  Order Change, assigned by the seller", and the value is the seller's sales order number of the
  original order (sea/06-OrderResponse.xml) — refuted as a logistics finding: a seller commonly keeps
  one sales order for the order and its changes, and air/07 cites the same pair; the reading is left
  to the context review.
