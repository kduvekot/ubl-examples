# LLM review: 20-DespatchAdvice.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### sea/20#F1 · Medium · Shipment gross weight leaves out the container
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `10-PackingList.xml:/PackingList/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`
- Why: Shipment/GrossWeightMeasure is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment." 4 106.4 kg is goods and pallets only (3 984 + 122.4, `10-PackingList.xml`); the shipment, a full 40-foot container, weighs 7 856.4 kg with the container (packing list and manifest).
- Condition: The shipment gross weight includes the container (7 856.4 kg), or the goods-only weight is given where the definition fits.
- Options: 7 856.4 kg (preferred); or omit the shipment weight in the despatch advice.
- Needs decision: no

### sea/20#F2 · Medium · Gate number in AdditionalStreetName of the despatch party's postal address
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address." "Gate 3" is a vehicle entrance, not a street name; it belongs to a pickup location, not to a postal address. The value occurs in 76 examples (`grep -l` over `world/examples/*/*.xml`).
- Condition: No gate in `AdditionalStreetName`; a gate, if needed, is in a despatch/pickup location.
- Options: remove it from the postal address (preferred); give it in `Shipment/Delivery/Despatch/DespatchLocation` if the story needs it.
- Needs decision: no

### sea/20#F3 · Low · Benches "from the distributor's stock" manufactured three days before despatch
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cbc:Description` = `The manufacturer's Serra bench, from the distributor's stock.`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:ItemInstance/cbc:ManufactureDate` = `2026-05-10`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-10`
- Why: The benches are said to come from Lumeway's stock in Bayvarra, but the lot and all 12 castings were made on 2026-05-10 (a Sunday) by Valdara Industries in Urvania, after the order of 2026-05-07 (`05-Order.xml`), and the goods were packed by 2026-05-12 (`10-PackingList.xml`) and despatched 2026-05-13. Goods made to order three days before despatch, in another country, are not distributor's stock.
- Condition: The manufacture dates are consistent with goods held in Lumeway's stock before the order, or the description no longer says "from the distributor's stock".
- Options: move the manufacture dates (and lot number) to before the order (preferred: keeps the stock story); or change the description.
- Needs decision: no

### sea/20#F4 · Low · Contacts whose name, title and department disagree
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Nalevi Warehousing's goods-inwards contact is a customer service officer in Sales, and Velumi's purchasing contact also sits in Sales. Name, job title and department contradict each other; a warehouse's receiving contact works in the warehouse, a buyer's in purchasing.
- Condition: For each contact, name, job title and department agree and fit the party's role (receiving goods, buying).
- Options: e.g. Goods inwards / Receiving clerk / Warehouse; Purchasing / Buyer / Purchasing.
- Needs decision: no

### sea/20#F5 · Low · No despatch or expected delivery date
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `LD-SH-26-0132`
- XPath: `/DespatchAdvice/cbc:IssueTime` = `08:52:00`
- Why: A despatch advice describes "the despatch or delivery of goods"; the receiving warehouse plans with the despatch date and the expected delivery. The shipment has no `Delivery` (no despatch, estimated delivery period or delivery location), although the order (`05-Order.xml`) names the delivery place (Lanoro warehouse, Selanu) and the container is accepted by the carrier at 10:15 the same day (`14-BillOfLading.xml`).
- Condition: The despatch advice states when the goods are despatched and when (or where) they are expected to be delivered.
- Options: add `Shipment/Delivery` with the despatch date and the estimated delivery period at Nalevi's warehouse (preferred); or a delivery period on the lines.
- Needs decision: no

### sea/20#F6 · Low · Product master data copied into the despatch advice
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cbc:WarrantyInformation` = `Five years on the frame against corrosion.`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:TransactionConditions/cbc:Description` = `Sold to trade customers only, per pallet of four benches.`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:CircularityProfile/cbc:MaintenanceFrequencyCode` = `YEARLY`
- Why: Warranty, search keywords, sales conditions, maintenance and repairability, emissions and the load test are catalogue data; the receiving warehouse does nothing with them when it checks a delivery. The identical item blocks appear in the order, packing list, customs declaration, receipt advice and invoice of the flow.
- Condition: The despatch line's item carries what is needed to identify and check the goods (identification, lot, serials, description), and other data only with a stated reason.
- Options: reduce the item to identification and traceability data (preferred).
- Needs decision: no

## Checked and consistent
- Order reference `VT-PO-26-0127` and order lines 1 and 2 resolve to `05-Order.xml`; packing list `LD-PL-26-0134` resolves to `10-PackingList.xml` with the same 96 + 12 units and the same shipment/consignment IDs.
- 24 pallets × 4 benches = 96 benches; 12 castings with 12 item instances, each with its own serial, trace and registration ID.
- Issue 2026-05-13 08:52 precedes the carrier's acceptance at 10:15 the same day (`14-BillOfLading.xml`).
- GTINs and GLN pass `check_ids.py`.
- Accounting cost `500` "Stock for municipal projects" agrees with the order and with `22-Invoice.xml`.

## Considered and refuted
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Nalevi Warehousing`: the B/L names Velumi Trading as final delivery party — refuted: Nalevi receives physically at its warehouse on behalf of Velumi, which the order's delivery party and the receipt advice confirm; the B/L's final party is the owner.
- `/DespatchAdvice/cbc:AccountingCostCode` = `500`: the buyer's cost centre on the seller's document — refuted: it is carried over from the order so the receiver can book the receipt; consistent across the flow.
- `/DespatchAdvice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`: originator and beneficiary on a despatch advice — refuted: the order was placed for the port's project; the despatch advice repeats the order's parties consistently.
