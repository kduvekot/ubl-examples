# LLM review: 04-DespatchAdvice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1527Z-thorough`
- Example: `world/examples/ore/04-DespatchAdvice.xml`, Git blob `91b2319d44d11307c315fd3ed9bfda3c8f447141` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit dbcb14a 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: all five parts
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
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

### ore/04#F1 · Medium · Shipment gross weight is the ore alone, without the wagons
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `1788400`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `1788.4`
- Why: Shipment/GrossWeightMeasure is "The total gross weight of a shipment; the weight of the goods
  plus packaging plus transport equipment". The value equals the despatched quantity of ore
  (1 788.4 t = 1 788 400 kg), so it holds the goods alone, without the 30 wagons
  (`/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One train: 30 wagons of about 60 tonnes.`). With a
  tare of about 20–25 t per four-axle open ore wagon (own knowledge), the weight as defined would be
  about 1 788.4 + 30 × 20…25 = 2 388–2 538 t. The consignment's gross weight in 02/03 is defined
  "excluding the carrier's equipment", which is why 1 800 000 kg fits there; here the element is a
  different one. The same value is in
  `05-Waybill.xml:/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `1788400`.
- Condition: the shipment's gross weight includes the wagons' tare, or the weight of the ore is
  carried in an element whose definition excludes the transport equipment.
- Options: (a, preferred) give the ore weight as `Consignment/cbc:GrossWeightMeasure` or
  `cbc:NetWeightMeasure`, as 02/03 do, and leave the shipment gross weight out (the wagons' tare is
  the carrier's data); (b) state the weight including the wagons from the wagon list, if the loaded
  train was weighed.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### ore/04#F2 · Medium · Province carried in Region instead of CountrySubentity
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this
  address is located"; a province belongs in `CountrySubentity`, as the world does for Bayvarra's
  states. 219 occurrences in 104 `*.xml` files (`grep -rl --include='*.xml' '<cbc:Region>Province of'`).
- Condition: no address of the example holds a province in `cbc:Region`, or the world states why an
  Urvanian province is a region.
- Options: (a, preferred) move to `CountrySubentity` in all Urvanian addresses; (b) record a decision
  if deliberate; (c) drop.
- Needs decision: no
- From: broad (F2), parties (F1), context (F2)

### ore/04#F3 · Low · The despatch itself is not described: no despatch date, wagons only in a note
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `SM-SH-26-0309`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One train: 30 wagons of about 60 tonnes.`
- Why: a despatch advice is "used to describe the despatch or delivery of goods". The shipment
  carries no despatch date or time (e.g. `Shipment/Delivery/Despatch/ActualDespatchDate`), no place of
  despatch and no expected arrival; the issue time (2026-03-10 15:37) is not the despatch time and by
  the "nothing implied by absence" rule may not stand in for it (the waybill was issued at
  `05-Waybill.xml:/Waybill/cbc:IssueTime` = `11:35:00`). The 30 wagons appear only in a line note,
  not as equipment or handling units, and there is no reference to the carrier's wagon list
  (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:AdditionalDocumentReference/cbc:ID` =
  `FRC-WAGON-LIST-11`), although the consignee is asked to
  (`/DespatchAdvice/cbc:Note[2]` = `Please check the goods on arrival and report any damage on the consignment note.`).
- Condition: the despatch advice states when (and from where) the goods were despatched, consistent
  with the waybill, and the wagons are identifiable in structured form or through a reference to the
  wagon list.
- Options: (a, preferred) `Shipment/Delivery/Despatch/ActualDespatchDate` (and time) at the mine
  siding, and the wagons as `TransportHandlingUnit`/`TransportEquipment` with their numbers and loaded
  weights; (b) at least the despatch date and a reference to `FRC-WAGON-LIST-11`; optionally the
  estimated delivery period.
- Needs decision: no
- From: broad (F3), logistics (F2), context (F3)

### ore/04#F4 · Low · Despatch and delivery contacts are sales desks
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Contact is "The primary contact for this party". The despatch party's contact answers
  questions about the despatch (loading, weights at the siding); the delivery customer's contact
  receives the goods, which the note asks to check on arrival. Both are customer-service desks in
  Sales, copied from master data; Valdara's is its own sales order desk (75 `*.xml` files with
  `order@valdara.example`).
- Condition: the despatch party's contact handles loading/despatch and the delivery customer's
  contact handles goods receipt (or each is left out).
- Options: (a, preferred) Serravona's siding/loading contact and Valdara's goods-receipt
  (raw-materials yard) contact; (b) omit contacts or job title and department.
- Needs decision: no
- From: broad (F4), parties (F2), context (F4)

### ore/04#F5 · Low · Party master data the despatch advice does nothing with
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Conditions` = `Unpaved access road; heavy vehicles only.`
- Why: section 4.8 and IND5. Castrano Logistics has no part in receiving ore the consignee unloads
  itself (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms`
  = `Delivery within the agreed slot; the consignee unloads.`) and occurs in no role in the flow;
  Valdara's share listing has no use in a despatch advice; the road-access condition does not concern
  a despatch by train from the mine's own siding. Service provider and ISIN each in 75 `*.xml` files.
- Condition: every aggregate of the parties has a use in this despatch advice.
- Options: (a, preferred) leave them out (the PhysicalLocation itself, the place of despatch, stays);
  (b) give Castrano a role in the story.
- Needs decision: no
- From: broad (F5: service provider), parties (F3), context (F5: service provider and security
  listing)

### ore/04#F6 · Low · World item number is a valid GTIN-12 in the GS1 US prefix range
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771010000013`
- Why: as in ore/01#F6: twelve digits with a correct GS1 check digit (3, recomputed in the merge);
  as GTIN-13 `0771010000013`, prefix 077 in the GS1 US range (own knowledge, no register lookup).
  The world scheme `urn:ubl-examples:world:item` (64 `*.xml` files) can be mistaken for real GTINs.
- Condition: the item number cannot be read as a valid GTIN in a real prefix range, or a recorded
  decision (with a GS1 check) states why the form is safe.
- Options: (a, preferred) change the world scheme's number form; (b) record the decision and the
  check in the sources.
- Needs decision: yes (the scheme is world-wide)
- From: broad (F6), logistics (F3)

## Checked and consistent
- Order reference `VI-PO-26-0304` and order line `1` resolve to 01; item description, seller's ID, HS
  260111, CPC 14100 and iron content 62 % equal the order's; buyer, seller, delivery customer and
  despatch party agree with 01.
- Consignment `VI-CS-26-0306` (02/03/05) and shipment `SM-SH-26-0309` (05) agree; carrier Ferrano Rail
  Cargo as in 01, 02, 03 and 05.
- Physics: 1 788.4 t / 30 wagons = 59.61 t per wagon, "about 60 tonnes"; 60 t of lump ore at about
  2.2–2.8 t/m³ (own knowledge) is 21–27 m³, inside an open ore wagon; 82–85 t gross per four-axle
  wagon, 20.5–21.3 t per axle, under 22.5 t.
- Quantity: 1 788.4 t against 1 800 t ordered (−0.64 %), the quantity invoiced in 06 and 07.
- Times: issued 2026-03-10 15:37, after the waybill of the same day (11:35) and inside the service
  window of 03.
- Party descriptions identical in all eight ore examples; ISIN check digit correct.

## Considered and refuted
- `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `1788.4`: suspected a short delivery
  against 1 800 t without backorder or reason — refuted because 0.64 % under is within normal
  loading tolerance for bulk ore, the order calls off "one train", and 07 invoices the despatched
  quantity. (from broad, logistics)
- `/DespatchAdvice/cbc:Note[2]` = `Please check the goods on arrival and report any damage on the consignment note.`:
  suspected unfit for bulk ore, or an instruction about the carrier's document in the seller's
  advice — refuted because shortages and contamination of bulk goods are also noted on the
  consignment note, and under FCA damage in transit is reserved against the carrier. (from broad,
  context)
- `/DespatchAdvice/cbc:DespatchAdviceTypeCode` = `DELIVERY`: suspected wrong type — refuted because
  the world list defines it as goods sent to the buyer against an order, which this is (the full
  call-off, not PARTIAL). (from broad, context)
- `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The mine and its rail siding`:
  physical location copied from master data — refuted because in a despatch advice it is the place
  of despatch. (from context; its road-access condition is part of F5)
- English renderings in Italian form, `+999` telephone numbers, ISO 6523 ICD `0990`, Ferrano Rail
  Cargo `SMALL`: refuted as in 01. (from parties)

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined; tare range widened to 20–25 t to cover both
  parts' figures.
- broad/F2, parties/F1, context/F2 → F2: combined; Needs decision no (parties: yes), as in ore/01#F1.
- broad/F3, logistics/F2, context/F3 → F3: combined.
- broad/F4, parties/F2, context/F4 → F4: combined.
- broad/F5, parties/F3, context/F5 → F5: combined; the road-access condition (parties) kept,
  consistent with ore/02#F8 and ore/03#F13.
- broad/F6, logistics/F3 → F6: combined.

