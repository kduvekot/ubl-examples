# LLM review: 29-DespatchAdvice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: broad

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/29-DespatchAdvice.xml`, Git blob `79edc7989dc6f0f5e4d8a3b040fb4fdfaa8e1ecc` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 1ae0e51 2026-11-14 Reviews of the tender flow, run 20261114T1433Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/29#F1 · High · The line says moss green, the item on the same line says Ferro grey
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Forty benches in moss green, RAL 6005, as the order change asked.`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:AdditionalItemProperty[4]/cbc:ListValue` = `Ferro grey`
- Why: the order change (27) asked for moss green RAL 6005 and the seller accepted it (28). The despatch line's note confirms that green benches are despatched, while the item on that line is identified as the grey variant (ExtendedID GRY: "an extended identifier for the item that identifies the item with specific properties"), with a physical attribute and a property both saying Ferro grey. The structured data and the note describe different goods.
- Condition: the item's variant identifier, colour attribute and colour property state the colour that the note and the order change state.
- Options: (a) green variant in ExtendedID, PhysicalAttribute and "Frame colour" (preferred); (b) none other seen.
- Needs decision: no

### tender/29#F2 · High · Gross weight of the shipment is less than the materials of the benches
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `1660`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `40`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure` = `34`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[2]/cbc:ConsumptionMeasure` = `22.5`
- Why: the same line states that one bench contains 34 kg of steel and 22.5 kg of hardwood, 56.5 kg together. Forty benches weigh 40 × 56.5 = 2260 kg net, before 36 anchor sets, 170 M12 bolts, the packaging (0.4 kg per bench) and ten pallets (pallets of 4; a wooden pallet weighs about 20–25 kg, my knowledge). The shipment's gross weight of 1660 kg is 41.5 kg per bench, 600 kg less than the benches alone. Gross weight cannot be below net weight. (Even if the consumption figures included production scrap, the document gives no lower product weight.)
- Condition: the gross weight is at least the number of benches times the weight of a bench plus accessories, packaging and pallets, and the per-bench material figures agree with it.
- Options: (a) gross weight of about 2600 kg (2260 + anchors and bolts + about 250 kg of pallets and packaging), also in 30 and 31 (preferred); (b) lower material figures in the item (25, 26, 30–33) so that a bench weighs under 40 kg, which a cast-steel bench of 1800 mm hardly does.
- Needs decision: no

### tender/29#F3 · Medium · "Outstanding" 200 benches that were never ordered
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:OutstandingQuantity` = `200`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:OutstandingReason` = `Later releases under the framework contract.`
- Why: OutstandingQuantity is "The quantity outstanding (which will follow in a later despatch)" of what the line's order asked for. The line refers to order line 1 of LPWD-PO-26-0212, which orders `26-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `40`; 40 are delivered, so nothing is outstanding. The 200 are the rest of the framework's estimated 240, which the department may or may not release (minimum 120, 21); they are not owed under this order and no despatch for them is pending.
- Condition: outstanding quantity = ordered quantity of the referenced order line minus delivered quantity (here 0, or absent).
- Options: (a) remove OutstandingQuantity and OutstandingReason (preferred); (b) none other seen.
- Needs decision: no

### tender/29#F4 · Medium · The advice does not say when the goods left or where they are going
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:InhouseMail` = `Room 2.14`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:Department` = `Procurement office`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Procurement office`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cbc:ID` = `CL-CS-26-0217`
- Why: a despatch advice describes "the despatch or delivery of goods". This one has no Delivery: no despatch date or time, no expected arrival, no delivery address. The only address of the delivery recipient is the procurement office in room 2.14 of Civic Square 6, while the order asks for delivery to the "Public works depot, Lumeport" (`26-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description`); 40 benches on pallets cannot be received in an office, and the recipient's contact is the buying office, not the depot that takes in goods. The shipment has a gross weight and a carrier but no number of pallets or packages (the tender speaks of pallets of 4), no vehicle and no route, although the goods cross a border the same day (30).
- Condition: the advice states the actual despatch date, the delivery location (the depot, with address) and a receiving contact, and the handling units the receiver has to count.
- Options: (a) add Shipment/Delivery with ActualDespatchDate, EstimatedDeliveryPeriod and DeliveryLocation/Address of the depot, a depot contact, and the number of pallets (preferred).
- Needs decision: no

### tender/29#F5 · Medium · Emission factor that does not lead to the emission value
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- Why: ValueFactorNumeric is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)". 0.82 × the base of 1 bench is not 96 kg; 96 / 0.82 = 117.07 of an activity the document does not state. Same block as in the catalogue (25).
- Condition: factor × the stated base or activity gives the value, or the factor is absent.
- Options: (a) drop ValueFactorNumeric (preferred); (b) state the activity.
- Needs decision: no

### tender/29#F6 · Medium · Language code in LocaleCode; provinces in Region
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; the value repeats the ISO 639 language code (213 of 250 examples, `grep -l 'LocaleCode listID="ISO 639"' world/examples/*/*.xml`). Region is "The recognized geographic or economic region or group of countries"; a province belongs in CountrySubentity (104 examples, `grep -l '<cbc:Region>Province of' world/examples/*/*.xml`).
- Condition: LocaleCode identifies a locale or is absent; provinces are in CountrySubentity.
- Options: (a) a locale code, and move the provinces (preferred).
- Needs decision: no

### tender/29#F7 · Low · "No status" codes that state nothing
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`
- Why: both codes signify the status of the document or line "with respect to its original state" (revised, cancelled …). This is the original advice; "NoStatus" says that there is nothing to say. Under the examples' rule against fillers a value needs a business reason, and absence would say the same.
- Condition: a status code is present only when the document or line has a status (revised, cancelled, …).
- Options: (a) remove both (preferred).
- Needs decision: no

### tender/29#F8 · Low · The warehouse office's contact is a sales customer service officer
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: name, job title and department of one contact should agree. The despatching party is a warehouse operator (ISIC 5210) and the contact is called "Warehouse office", but its title and department are those of a sales desk (the same pair as Valdara's order desk and Brackenmere's trade sales).
- Condition: job title and department of the despatch contact fit a warehouse office.
- Options: (a) e.g. "Despatch clerk" / "Warehouse" (preferred).
- Needs decision: no

### tender/29#F9 · Low · The full catalogue record of the item in a logistics provider's despatch advice; reference with only an ID; department as a company
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:DocumentReference/cbc:ID` = `PWD-2026-PARKS`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the despatch line repeats the catalogue's whole item record (search keywords, warranty, test method, emissions, circularity profile, repairability), which a warehouse despatching pallets neither states nor uses; what a despatch needs (identification, lot, quantity) is there too. The line's document reference has no type and carries the identifier that is at once procurement file and contract (see 24). The department carries a company liquidation status.
- Condition: the despatch line identifies the goods and their lot; catalogue content is absent; a bare reference says what it refers to; no liquidation status on the department.
- Options: (a) reduce the item to identification, name, lot and physical data; add DocumentTypeCode or drop the reference (preferred).
- Needs decision: no

## Checked and consistent
- `/DespatchAdvice/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212` is the order (26); delivered 40 EA = ordered 40 EA on line 1.
- Sub-lines: anchor sets 36 delivered + 4 on back order = 40, one per bench; bolts 170 delivered with 10 over-supplied = 160 required = 4 per bench × 40, matching "four ground anchors and the bolts to fix them".
- Shipment CL-SH-26-0216 and consignment CL-CS-26-0217 are the ones the export and import declarations (30, 31) carry, with the same gross weight 1660 kg (so F2 applies to all three).
- Lot VI-LOT-260327 and manufacture date 2026-03-27 agree with each other and lie between the acceptance of the colour change (2026-03-25) and the despatch (2026-03-30).
- Despatch party Castrano Logistics is the seller's logistics service provider (ServiceProviderParty of Valdara); carrier Trasvia Haulage (ISIC 4923) holds an international haulage permit valid to 2030-06-30, which a cross-border road movement needs.
- The note asks to report damage on the consignment note; the credit note (33) later concerns a damaged bench.
- Issue 2026-03-30 17:37 follows the export declaration of the same day (13:40) and precedes the import declaration (2026-03-31).
- check_ids.py: ISIN XU0001042501 correct.

## Considered and refuted
- `/DespatchAdvice/cbc:AccountingCostCode`: the buyer's cost code in a document of the seller's warehouse — refuted, it is passed on from the order so the buyer can book the receipt.
- `/DespatchAdvice/cac:DespatchLine/cac:SubDespatchLine[2]/cbc:OversupplyQuantity`: bolts were not ordered as such — refuted, they belong to the bench ("supplied with … the bolts"), 4 per bench, so 10 over that is an oversupply.
- `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cbc:ManufactureDate`: forty benches made two days after the colour was agreed — refuted as a timeline matter; coating in another colour of stocked frames is feasible.
- `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType`: master data — refuted, it explains why Castrano despatches.
- `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:AdditionalPartyIdentification/cbc:ID`: ICD 0990 — not an assigned ISO 6523 ICD (my knowledge).

## Outside this review
- Whether 40 benches of 1800 × 620 × 780 mm on ten pallets fit one road vehicle, and the route and border crossing, are capacity and location questions.
