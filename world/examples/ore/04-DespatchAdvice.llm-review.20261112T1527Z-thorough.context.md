# LLM review: 04-DespatchAdvice.xml

Flow: ore (ORE-2026-01) · Review date: 2026-11-12 · Part: context

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

### ore/04#F1 · Medium · The shipment's gross weight is the ore alone, without the wagons
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `1788400`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `1788.4`
- Why: Shipment/GrossWeightMeasure is "the total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". The value equals the despatched ore (1788.4 t), so it is the net weight of loose goods with no packaging, but excludes the 30 wagons (`/DespatchAdvice/cac:DespatchLine/cbc:Note` = `One train: 30 wagons of about 60 tonnes.`). With a tare of roughly 20–25 t per four-axle ore wagon (own knowledge), the gross shipment weight would be about 2 390–2 540 t. The consignment's gross weight in 02/03 is defined "excluding the carrier's equipment", which is why 1 800 000 kg fits there; here the element's definition differs.
- Condition: Shipment/GrossWeightMeasure either includes the wagons' tare, or the ore weight is given in an element whose definition excludes transport equipment.
- Options: (a) preferred: give the ore weight as Consignment/GrossWeightMeasure or Shipment/NetWeightMeasure and leave Shipment/GrossWeightMeasure out (the wagons' tare is the carrier's data); (b) state the weight including wagons, if the despatcher weighed the loaded train.
- Needs decision: no

### ore/04#F2 · Medium · A province is given in `Region`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "the recognized geographic or economic region or group of countries"; a province is "the political or administrative division of a country" (`CountrySubentity`), as the world encodes Bayvarra's states. 104 XML examples carry "Province of Ferrano" (`grep -rl --include='*.xml'`).
- Condition: the province is in `CountrySubentity` in every address.
- Options: (a) preferred: move it to `CountrySubentity`; (b) rename it if it is an economic region.
- Needs decision: no

### ore/04#F3 · Low · The despatch advice does not say when the goods left
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `SM-SH-26-0309`
- Why: a Despatch Advice describes "the despatch or delivery of goods"; this one says what and how much, but not when the train was handed over at the siding (no Shipment/Delivery/Despatch/ActualDespatchDate or time) nor the expected arrival. The issue time (2026-03-10 15:37) is not the despatch time, and by the "nothing implied by absence" rule it may not stand in for it. The waybill was issued at the siding the same morning (`05-Waybill.xml:/Waybill/cbc:IssueTime` = `11:35:00`).
- Condition: the despatch advice states the actual despatch date (and, where known, time), consistent with the waybill.
- Options: (a) preferred: Shipment/Delivery/Despatch/ActualDespatchDate (and time) of the hand-over to Ferrano Rail Cargo; (b) add the estimated delivery period too, if the receiver plans unloading from it.
- Needs decision: no

### ore/04#F4 · Low · Despatch and delivery contacts are sales desks
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Sales office`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the despatch party's contact is the one who despatched the goods (loading/shipping at the siding); the delivery customer's contact receives them ("Please check the goods on arrival and report any damage", `/DespatchAdvice/cbc:Note[2]`). Both are customer-service desks in Sales, copied from master data; Valdara's is its own sales order desk.
- Condition: the despatch party's contact handles the loading/despatch, the delivery customer's contact receives goods.
- Options: (a) preferred: Serravona's siding/loading contact and Valdara's goods-receipt (raw-materials yard) contact; (b) omit the contacts.
- Needs decision: no

### ore/04#F5 · Low · Party master data the despatch advice does nothing with
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: the delivery recipient's stock-exchange listing and its warehousing-and-despatch provider play no part in a delivery of ore by train to Valdara's own siding; Castrano appears in no role in the flow. Same master data in 75 XML examples each.
- Condition: every aggregate of the parties has a use in this despatch advice.
- Options: (a) preferred: leave them out.
- Needs decision: no

## Checked and consistent
- OrderReference `VI-PO-26-0304` resolves to 01; OrderLineReference line 1 exists there; buyer, seller, delivery customer and despatch party agree with 01.
- Consignment `VI-CS-26-0306` is the one of 02/03; carrier Ferrano Rail Cargo as in 02/03/05.
- Quantity: 1788.4 t despatched against 1800 t ordered (−0.64 %), consistent with "30 wagons of about 60 tonnes" (30 × 60 = 1800) and with the invoiced 1788.4 t in 06 and 07.
- Item description, identifiers, HS 260111 and iron content 62 % identical to 01.
- Issue 2026-03-10 15:37, after the waybill of the same day (11:35) and within the service window of 03.

## Considered and refuted
- `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PhysicalLocation/cbc:Description` = `The mine and its rail siding`: physical location copied from master data — refuted because in a despatch advice it is the place of despatch, which the document has reason to state.
- `/DespatchAdvice/cbc:DespatchAdviceTypeCode` = `DELIVERY`: "Delivery" for an advice of despatch — refuted because the world list defines it as "Goods sent to the buyer against an order", which this is (the full call-off, not PARTIAL).
- `/DespatchAdvice/cbc:Note[2]` = `Please check the goods on arrival and report any damage on the consignment note.`: an instruction about the carrier's document in the seller's advice — refuted because under FCA the risk passes at the siding, and damage in transit is to be reserved on the consignment note against the carrier.
