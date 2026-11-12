# LLM review: 06-DespatchAdvice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/06-DespatchAdvice.xml`, Git blob `87ee027fe7a7634e3733f7816740466502baaf2c` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit ebb6439 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: all merged reviews
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

### packaging/06#F1 · Medium · The despatch advice does not say when the goods were despatched or will arrive
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `LTM-SH-26-0527`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cbc:ID` = `LTM-CS-26-0528`
- Why: A despatch advice is "A document used to describe the despatch or delivery of goods and services". This one describes what is sent (600 shirts, 168 kg), by whom and to whom, but not when: there is no `Shipment/cac:Delivery` with an estimated or requested delivery period, no `Despatch` with an actual despatch date and time, and no transport event. The receiving store, which is asked to "check the goods on arrival", cannot plan goods-in from it, and nothing else in the flow gives the date (the order `05-Order.xml` has none either). Information the document's purpose depends on is missing. Of the world's 11 despatch advices, 10 carry no despatch or delivery date at all (`*/*-DespatchAdvice.xml`; only `road/04-DespatchAdvice.xml` has `cbc:ActualDespatchDate`; counted by listing every `cbc:*Date`/`cbc:*Time` element other than issue, registration, validity and manufacture dates).
- Condition: the despatch advice states when the goods were (or will be) despatched and when they are expected at the store, after or at its issue time 2026-05-12 11:35 for anything actual.
- Options: (a, preferred) add `Shipment/cac:Delivery` with `cac:Despatch/cbc:ActualDespatchDate`/`ActualDespatchTime` and `cac:EstimatedDeliveryPeriod`, since both the sending and the expected arrival matter to the receiver; (b) at least the estimated delivery period.
- Needs decision: no

### packaging/06#F2 · Low · The note refers to a consignment note the document does not identify
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- Why: The note tells the store to record damage on "the consignment note", but the despatch advice carries no reference to one (no `AdditionalDocumentReference`, no `Consignment` carrier reference), and no consignment note, waybill or CMR exists in the flow. The free text thus relies on a document that cannot be linked. Low, because a road consignment note travelling with the goods is normal practice.
- Condition: either the consignment note is identified (its number in a document reference or as the carrier's consignment reference), or the note does not rely on it.
- Options: (a, preferred) add a document reference to Bayforth Forwarding's consignment note, because the store needs its number to record damage against; (b) reword the note (e.g. "report any damage to the driver").
- Needs decision: no

### packaging/06#F3 · Low · Nothing says how many packages to check on arrival
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `168`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `600`
- Why: The store is asked to check the goods on arrival, which in goods-in means counting packages against the advice; the despatch advice gives the shirt count and the gross weight but no number of cartons or handling units (`Shipment/cbc:TotalTransportHandlingUnitQuantity`, `Consignment/cbc:TotalPackagesQuantity`, or `TransportHandlingUnit`/`Package`). Without it a missing carton cannot be noticed at the door. Completeness remark.
- Condition: the number of packages (and, if palletised, handling units) of the shipment is stated.
- Options: (a, preferred) add `Consignment/cbc:TotalPackagesQuantity` (e.g. 20 cartons of 30 shirts, which fits the weight below); (b) a `TransportHandlingUnit` with its packages, if the cartons travel on a pallet.
- Needs decision: no

### packaging/06#F4 · Low · The carrier's contact is its export desk, for a delivery inside Lumeport
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Export desk`
- Why: The carrier's contact should be the one who handles this transport. The shipment goes from the mill to the store, both in Lumeport, Bayvarra; Bayforth Forwarding's export desk is not the desk for a local delivery. The contact name `Export desk` occurs in 25 of the world's examples (`grep -rl --include='*.xml' '<cbc:Name>Export desk</cbc:Name>'`), so it looks like the party's standard contact copied into this role.
- Condition: the carrier's contact fits a domestic delivery (e.g. a local delivery or operations desk), or the contact is left out.
- Options: (a, preferred) use a domestic operations or delivery contact for Bayforth in this role; (b) drop the contact.
- Needs decision: no

### packaging/06#F5 · Low · The world's item number is a valid GTIN-12 in a real GS1 range
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:StandardItemIdentification/cbc:ID` = `772030000090`
- Why: The element is "Identifying information for this item, assigned according to a standard system", and the scheme is the world's own (`urn:ubl-examples:world:item`). The value is twelve digits with a valid GS1 mod-10 check digit, i.e. it is a well-formed GTIN-12 (UPC-A); read as GTIN-13 (`0` + the twelve digits) its prefix 077 lies in the range GS1 US allocates (060–139, own knowledge). A reader or a GS1 scanner will take it for a real UPC, and whether that UPC is assigned cannot be excluded. The agreed rule is that fictional values must not be mistaken for real ones. The same scheme carries 8 distinct twelve-digit values, all with valid GTIN-12 check digits, in 64 examples (`grep -rl --include='*.xml' 'schemeID="urn:ubl-examples:world:item"'`; check digits computed for all 8 values).
- Condition: no identifier in the world's item scheme is a well-formed GTIN in a range GS1 allocates to real companies, or the choice is recorded as checked against the real register.
- Options: (a, preferred) give the world's item numbers a form that cannot be read as a GTIN (letters, another length, or a failing mod-10 digit), because that removes the confusion at the source; (b) move them into GS1's demonstration prefix 952, like the world's GTINs, if the world wants them to be GTINs; (c) keep them and record why they are not mistaken for real UPCs.
- Needs decision: yes

## Checked and consistent
- `/DespatchAdvice/cac:OrderReference/cbc:ID` = `BS-PO-26-0525` resolves to `05-Order.xml`; buyer, seller, delivery customer (`20410411`) and despatch supplier (`20412603`) agree with the order; the despatch line refers to order line `1`, and the delivered quantity 600 EA equals the ordered `05-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `600`, so type code `DELIVERY` ("Goods sent to the buyer against an order", not partial) fits. The advice (2026-05-12) is issued after the order (2026-05-07).
- Carrier under DDP: the seller arranges carriage, and the carrier (Bayforth Forwarding, Lumeport) is engaged by the seller, consistent with `05-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `DDP`.
- Physics, gross weight against goods: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `168` kg for 600 shirts is 0.28 kg per shirt gross. A men's woven cotton shirt weighs about 0.20–0.25 kg (own knowledge; 0.22 kg taken), the garment bag of `03-Order.xml` about 17 g (60 cm × 1 m × 2 layers × 15 µm × 920 kg/m³, dimensions partly assumed), and 20 cartons of 30 shirts about 1 kg each: 600 × 0.22 + 600 × 0.017 + 20 × 1 ≈ 132 + 10 + 20 = 162 kg, within 4 % of 168 kg. No transport equipment is stated, so "goods plus packaging plus transport equipment" reduces to goods plus packaging; consistent.
- The shirts are packed "in a garment bag", which links them to the garment bags the mill bought from Rivermouth Packaging (`03-Order.xml`, 20 000 bags; 600 are used here).
- Identifiers: the shipment ID `LTM-SH-26-0527` and consignment ID `LTM-CS-26-0528` are the seller's own and do not occur in any other example (`grep -rn --include='*.xml'`), so they are not mistaken for document numbers.
- `check_ids.py`: the store's GLN `9522610900002` passes (GS1 prefix 952 is reserved for demonstrations, own knowledge).

## Considered and refuted
- `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cbc:IndustryClassificationCode` = `5229`: suspected that a forwarder (ISIC 5229, transport support activities) is not the party "who provides the transport of goods between named points" — refuted because Bayforth Forwarding also carries goods itself in the world (`retail/16-Invoice.xml:/Invoice/cac:Delivery/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`; `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:PreCarriageShipmentStage/cac:CarrierParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`), and a forwarder can contract as carrier.
- `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`: suspected a filler — refuted for this lens: the code exists in UBL's own list and says the advice is neither a revision nor a cancellation; whether it is needed is a question for the context review.
