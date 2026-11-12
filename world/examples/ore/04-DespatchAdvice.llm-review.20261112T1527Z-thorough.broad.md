# LLM review: 04-DespatchAdvice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: broad

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### ore/04#F1 · Medium · Shipment gross weight is the net weight of the ore, without the wagons
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `1788400`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `1788.4`
- Why: Shipment/GrossWeightMeasure is "The total gross weight of a shipment; the weight of the goods
  plus packaging plus transport equipment". The value equals the despatched quantity of ore
  (1 788.4 t) exactly, so it holds the goods alone. The shipment travels in 30 wagons
  (`/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One train: 30 wagons of about 60 tonnes.`); with a
  tare of roughly 20–25 t per open ore wagon (own knowledge) the gross weight as defined would be
  about 2 390–2 540 t. The consignment's gross weight elsewhere is defined without the carrier's
  equipment (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cbc:GrossWeightMeasure`
  = `1800000`), which is why the figures there are right; here the element is a different one.
- Condition: the shipment's gross weight includes the transport equipment, or the weight of the ore
  is carried in an element whose definition is the goods' weight.
- Options: (a, preferred) `cbc:NetWeightMeasure` (or the consignment's gross weight) for 1 788 400 kg,
  and a shipment gross weight only if the wagons' tare is known; (b) compute the gross weight with
  the wagons' tare from the wagon list.
- Needs decision: no

### ore/04#F2 · Medium · Province carried in Region instead of CountrySubentity
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province
  belongs in `CountrySubentity`. 104 `*.xml` files do the same
  (`grep -rl --include='*.xml' '<cbc:Region>Province of'`).
- Condition: no address of the example holds a province in `cbc:Region`.
- Options: (a, preferred) move to `CountrySubentity`; (b) drop.
- Needs decision: no

### ore/04#F3 · Low · Despatch advice without the date of despatch and with the wagons only in a note
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `SM-SH-26-0309`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One train: 30 wagons of about 60 tonnes.`
- Why: a despatch advice is "used to describe the despatch or delivery of goods"; the receiver uses
  it to expect the goods. The document gives no despatch date or time (e.g.
  `cac:Shipment/cac:Delivery/cac:Despatch/cbc:ActualDespatchDate`) and no expected arrival, only its
  issue date; the number of wagons is in free text only, although the carrier has a wagon list
  (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:AdditionalDocumentReference/cbc:ID` =
  `FRC-WAGON-LIST-11`).
- Condition: the despatch advice says when the train was despatched (and, if known, when it is
  expected), and the wagon count is not only in a note.
- Options: (a, preferred) despatch date/time in the shipment's delivery/despatch and the 30 wagons as
  transport handling units or equipment; (b) at least the despatch date.
- Needs decision: no

### ore/04#F4 · Low · Contacts do not fit the roles
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the despatch party's contact answers questions about the despatch (siding, loading), not
  sales; the delivery customer's contact receives the goods (goods-in at the factory siding), not
  a sales customer-service officer. The same contacts are used for every role in the flow.
- Condition: the despatch party's contact handles despatch; the delivery customer's contact handles
  receipt of goods.
- Options: (a, preferred) role-specific contacts; (b) drop job title and department.
- Needs decision: no

### ore/04#F5 · Low · Buyer's logistics service provider copied into the despatch advice
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- Why: Castrano Logistics plays no part in the receipt of the ore, which the consignee unloads
  itself (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms`
  = `Delivery within the agreed slot; the consignee unloads.`). Master data without use; 75 `*.xml`
  files carry it.
- Condition: no service provider without a role in the despatch.
- Options: (a, preferred) leave it out; (b) give it a role.
- Needs decision: no

### ore/04#F6 · Low · World item number has the form of a valid GTIN-12 in the GS1 US range
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771010000013`
- Why: 12 digits with a correct GS1 mod-10 check digit; as GTIN-13 `0771010000013`, prefix 077 in the
  GS1 US range (own knowledge). The world scheme `urn:ubl-examples:world:item` (64 `*.xml` files)
  can therefore be mistaken for real GTINs. Whether this GTIN is assigned I could not check.
- Condition: the item number cannot be mistaken for a real GTIN, or its non-assignment is recorded.
- Options: (a, preferred) a format that cannot be a GTIN; (b) record a GS1 check in the sources.
- Needs decision: yes (the scheme is world-wide)

## Checked and consistent
- Order reference `VI-PO-26-0304` and line 1 resolve to `01-Order.xml`; item description, seller's
  ID, HS and CPC codes and the iron content equal the order's.
- Consignment `VI-CS-26-0306` and shipment `SM-SH-26-0309` are the same as in `05-Waybill.xml`; the
  carrier is the one of the transport plan.
- Physics: 1 788.4 t / 30 wagons = 59.6 t per wagon, "about 60 tonnes" as the note says. At a bulk
  density of lump iron ore of about 2.2–2.6 t/m³ (own knowledge), 60 t is 23–27 m³, which fits an
  open ore wagon (typically 30–75 m³) within the payload of a 4-axle wagon (about 60–70 t at 22.5 t
  axle load).
- The despatched quantity 1 788.4 t is the quantity invoiced in `07-Invoice.xml` and the quantity the
  carrier bills in `06-Invoice.xml`.
- Party descriptions identical to the other examples of the flow.

## Considered and refuted
- `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `1788.4`: suspected short delivery
  against 1 800 t ordered without backorder or reason — refuted because 0.6 % under is within normal
  loading tolerance for bulk ore and the order calls off "one train", not an exact tonnage.
- `/DespatchAdvice/cbc:Note[2]` = `Please check the goods on arrival and report any damage on the consignment note.`:
  suspected unfit for bulk ore — refuted because shortages and contamination of bulk goods are also
  noted on the consignment note.
- `/DespatchAdvice/cbc:DespatchAdviceTypeCode` = `DELIVERY`: suspected wrong type — refuted because
  the code means "Delivery" and the document announces a delivery to the buyer.
