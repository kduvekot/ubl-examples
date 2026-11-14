# LLM review: 29-DespatchAdvice.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: logistics

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/29-DespatchAdvice.xml`, Git blob `79edc7989dc6f0f5e4d8a3b040fb4fdfaa8e1ecc` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
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

### tender/29#F1 · High · The line says moss green, the item is identified and described as Ferro grey
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Forty benches in moss green, RAL 6005, as the order change asked.`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `GRY`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:DescriptionCode` = `GRY`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:SellersItemIdentification/cac:PhysicalAttribute/cbc:Description` = `Frame in Ferro grey`
- Why: ExtendedID "identifies the item with specific properties" (the model's own example is the colour of a chair). The despatched goods are the moss-green variant agreed by `27-OrderChange.xml` and `28-OrderResponse.xml`, as the line note says; the structured identification, the colour code (GRY = grey; the list has GRN, "Green, such as moss green (RAL 6005)") and the property "Frame colour: Ferro grey" in the same item describe the grey variant of the original order. A receiver checking the goods against the structured data would reject them.
- Condition: Item variant, colour attribute and colour property describe what was despatched (moss green, RAL 6005), in agreement with the note.
- Options: (a) preferred: extended ID and colour code of the green variant (GRN), description "Frame in moss green (RAL 6005)", property value accordingly; (b) none: the note cannot be the only place where the colour is right.
- Needs decision: no

### tender/29#F2 · High · Emission factor × base does not give the emission value
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: "A numeric factor used to calculate the value measurement" applied to "the base quantity to which the value factor applies": 0.82 × 1 EA = 0.82, not 96 kg CO2e (96 / 0.82 = 117.07 of an unstated unit). Same values as in 25, 26, 30–33 and, in all, 39 examples across flows (files containing `ValueFactorNumeric>0.82<`, grep over `world/examples/**/*.xml`).
- Condition: factor × base = value with the base in the factor's unit, or factor and base are absent.
- Options: as in the review of `25-Catalogue.xml` (F4).
- Needs decision: no

### tender/29#F3 · Medium · "Outstanding quantity" is the rest of the framework, not of the order
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:OutstandingQuantity` = `200`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:OutstandingReason` = `Later releases under the framework contract.`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `40`
- Why: OutstandingQuantity is "the quantity outstanding (which will follow in a later despatch)" for the despatch line, which refers to line 1 of order `LPWD-PO-26-0212`. That line orders `26-Order.xml:/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `40`, and 40 are delivered: nothing of the order is outstanding. 200 (= 240 − 40) is the estimated remainder of the framework, which has not been ordered (the framework's minimum is 120, its maximum 288) and which the despatching party cannot promise to send.
- Condition: The outstanding quantity is the ordered quantity not yet despatched (0 for the benches), or absent.
- Options: (a) preferred: remove quantity and reason (the invoice already carries "First release: 40 benches; 200 remain" as an annotation); (b) set it to 0.
- Needs decision: no

### tender/29#F4 · Medium · The advice does not say when the goods left, when they arrive or where they go
- XPath: `/DespatchAdvice/cac:Shipment`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName` = `Civic Square`
- Why: A despatch advice "describe[s] the despatch or delivery of goods". This one has no `cac:Delivery` on shipment or line: no actual despatch date and time, no estimated delivery, no despatch address and no delivery address. The only address of the receiving side is the department's office at Civic Square, whereas the order names another place of delivery (`26-Order.xml:/Order/cac:DeliveryTerms/cac:DeliveryLocation/cbc:Description` = `Public works depot, Lumeport`). The note asks the receiver to check the goods "on arrival", but the receiver is not told when or where that is; the debit note for lateness (34) later depends on dates no document of the release states.
- Condition: The despatch advice states the despatch date (and time), the expected arrival and the delivery location, the latter agreeing with the order's delivery location.
- Options: (a) preferred: `cac:Shipment/cac:Delivery` with ActualDespatchDate/Time, an EstimatedDeliveryPeriod, DeliveryAddress (the depot) and a Despatch/DespatchAddress (Castrano's warehouse); (b) at least the dates.
- Needs decision: no

### tender/29#F5 · Low · No packages, handling units or vehicle for a palletised road shipment
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment`
- Why: The benches are sold on pallets of four (`15-Tender.xml`: orderable unit "Pallet of 4"; the catalogue speaks of stretch film and pallet straps), so the shipment is ten pallets on a lorry of the carrier. The shipment gives only a gross weight and the carrier: no number or kind of packages, no handling units with their identifiers, no vehicle. The receiver cannot count what arrives against the advice, and the request to "report any damage on the consignment note" has no unit to refer to. Missing details the document could carry.
- Condition: The shipment states at least the number and kind of packages or handling units (10 pallets with 4 benches each), consistent with quantity and weight.
- Options: (a) preferred: `cac:TransportHandlingUnit` ×10 (or `TotalTransportHandlingUnitQuantity` 10) and the lorry's registration in a shipment stage; (b) the package count only.
- Needs decision: no

### tender/29#F6 · Low · Gross weight is light against the materials the item is said to contain
- XPath: `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure` = `1660`
- Why: Calculated: 1660 kg / 40 benches = 41.5 kg gross per bench, including pallets, film, 36 anchor sets and 170 bolts. Deducting ten pallets (about 20 kg each, my estimate: 200 kg), the anchor sets (four anchors per set at about 1 kg, my estimate: 144 kg) and the bolts (about 0.1 kg each: 17 kg) leaves about 1300 kg, i.e. about 32 kg per bench. The item's own data (same document, `cac:CircularityProfile`) give 34 kg of steel and 22.5 kg of hardwood consumed per bench, 56.5 kg; a finished weight of 32 kg would mean that over 40 % of the material is lost in production, which is not credible for cast frames and sawn slats. A cast-steel bench of 1.8 m with five hardwood slats weighs 50 kg or more (my knowledge). At 56.5 kg the benches alone would weigh 2260 kg.
- Condition: Gross weight ≥ 40 × the bench's weight + packaging and accessories, with a bench weight that agrees with the materials stated for it.
- Options: (a) preferred: a gross weight of about 2600 kg (40 × ~56 kg + pallets and accessories); (b) lower the resource consumption figures of the item so that they fit a 32 kg bench. The same 1660 kg is declared to customs in 30 and 31.
- Needs decision: no

### tender/29#F7 · Low · No serial numbers although the contract requires them on the benches
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cac:LotIdentification/cbc:LotNumberID` = `VI-LOT-260327`
- Why: The procedure's additional condition, carried into the contract, is `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cbc:AdditionalConditions` = `Benches must carry the maker's serial number.` The despatch advice identifies the 40 benches by one lot only; `cac:ItemInstance/cbc:SerialID` is not used. The later damage case concerns one particular bench (credit note 33, "PARK-HB-B17"), which no document can tie to a serial number.
- Condition: The despatched benches are identified by their serial numbers (or the document says where the list is).
- Options: (a) 40 item instances with SerialID, or a serial range in one; (b) leave the lot and cite a packing list; preference (a) for the first.
- Needs decision: no

### tender/29#F8 · Low · Line document reference with only an ID
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:DocumentReference/cbc:ID` = `PWD-2026-PARKS`
- Why: "A reference to a document associated with this despatch line", with only an ID. The value is the number of the framework contract (and of the procurement file); the reference does not say so.
- Condition: The reference states what it refers to (`cbc:DocumentType` "Framework contract"), or is absent.
- Options: add the document type (preferred).
- Needs decision: no

### tender/29#F9 · Low · Status codes that say "no status"
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`
- Why: Both codes signify the status "with respect to its original state" and are meant for cancelled or revised documents and lines. "NoStatus" states that there is nothing to state; under the repository's rule against fillers (a value needs a business reason; nothing is implied by absence) the elements have no reason to be present in an original despatch advice.
- Condition: The status codes are present only when the document or line has a status to report.
- Options: remove both (preferred).
- Needs decision: no

### tender/29#F10 · Low · Programme code differs from the procurement documents
- XPath: `/DespatchAdvice/cac:ProjectReference/cbc:ID` = `PWD-PARKS-26`
- XPath: `/DespatchAdvice/cbc:AccountingCostCode` = `PWD-PARKS-26`
- Why: As in `26-Order.xml` (F7): the programme is coded PARKS-26 in 01, 02, 03 and 24 (`03-CallForTenders.xml:/CallForTenders/cac:TenderingTerms/cbc:FundingProgramCode` = `PARKS-26`), and the same string serves here as project identifier and as the buyer's accounting code (header and line).
- Condition: One code for the programme throughout the flow.
- Options: as in 26.
- Needs decision: no

## Checked and consistent
- `check_ids.py`: no failures.
- `cac:OrderReference/cbc:ID` LPWD-PO-26-0212 and `cac:OrderLineReference/cbc:LineID` 1 resolve to the order and its only line; delivered quantity 40 EA = ordered quantity; `cbc:LineCountNumeric` 1 = one despatch line.
- Issue time 30 March 17:37 follows the order response (25 March), the manufacture date of the lot (27 March; lot number VI-LOT-260327 encodes the same date) and the export declaration (30 March 13:40, "declared before the goods leave"), and precedes the import declaration (31 March 11:14).
- Shipment CL-SH-26-0216 (header and line), consignment CL-CS-26-0217, carrier Trasvia Haulage with permit XU-HAUL-2020-0877 (valid to 2030-06-30) and gross weight 1660 kg are the same in `30-ExportCustomsDeclaration.xml`; shipment and weight also in 31.
- Sub-lines: 36 + 4 anchor sets = 40, one per bench; 170 bolts − 10 oversupplied = 160 = 40 × 4, matching "four ground anchors and the bolts to fix them".
- Volume: a bench of 1.8 × 0.62 × 0.78 m takes 0.87 m³, 40 benches 35 m³ before stacking: one articulated lorry (about 90 m³) suffices.
- Castrano Logistics as despatch party agrees with its role as Valdara's warehousing and despatch provider in every example.
- DespatchAdviceTypeCode DELIVERY, CertificateTypeCode PERMIT, ISIC 4923 (freight transport by road) for the carrier: in their lists and fitting.

## Considered and refuted
- `/DespatchAdvice/cac:DespatchLine/cac:SubDespatchLine[2]/cbc:OversupplyQuantity`: "over and above that ordered", although bolts are not an order line — refuted: the sub-lines detail what belongs to the ordered bench (four anchors and bolts each), so the ordered quantity is implied (160).
- `/DespatchAdvice/cac:DespatchLine/cac:SubDespatchLine[1]/cbc:BackorderQuantity`: 4 sets late while the invoice bills complete benches — refuted for this document: stated with reason and a time ("within a week"); no later despatch document exists (see below).
- `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance/cbc:ManufactureDate`: 27 March, two days after the colour change was accepted (25 March 16:15) — refuted: coating 40 stocked frames in two days is feasible.
- `/DespatchAdvice/cbc:ID`: the numbers 0215 (advice), 0216 (shipment), 0217 (consignment) continue a running number shared with other parties' documents (…0214 order response, …0218 export declaration) — refuted as a finding of this example: each identifier is of the kind its element names; the shared counter is a property of the whole flow.

## Outside this review
- No later despatch of the four anchor sets on back order appears in the flow.
- Whether a lorry of Trasvia Haulage can run from Ferrano to Lumeport on the map's routes, and how long it takes, is a question of the cross-flow consistency review.
