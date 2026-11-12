# LLM review: 04-DespatchAdvice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/04-DespatchAdvice.xml`, Git blob `d5694687ad07a0bd4b1b8412513e13a712a00375` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 3a48551 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/04#F1 · High · Actual despatch reported 65 minutes after the advice is issued, and it is the departure, not the pickup
- XPath: `/DespatchAdvice/cbc:IssueDate` = `2026-03-23`
- XPath: `/DespatchAdvice/cbc:IssueTime` = `15:15:00`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ActualDespatchDate` = `2026-03-23`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ActualDespatchTime` = `16:20:00`
- Why: `ActualDespatchDate`/`Time` is "The actual despatch (pickup) date/time". The advice, issued 2026-03-23 15:15, reports an actual despatch at 16:20 the same day, 65 minutes in the future; an actual event cannot be reported before it happens (both are local times of Ferrano). The definition equates despatch with pickup, and the carrier's documents put the pickup at 15:05: `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:ActualPickupTransportEvent/cbc:OccurrenceTime` = `15:05:00`, repeated by the status issued the next day, `09-TransportationStatus.xml:/TransportationStatus/cac:UpdatedPickupTransportEvent/cbc:OccurrenceTime` = `15:05:00`; 16:20 is the truck's departure, `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `16:20:00` (logistics). Refutation attempts in the merge: (1) broad refuted the pickup/departure difference ("despatch is the moment the truck leaves the warehouse; loading began at 15:05"), but the definition says pickup, and the waybill records 15:05 as the pickup, not as start of loading; (2) the waybill cannot confirm 16:20 as already known at 15:15, since it is itself issued at 08:16 that morning (08's own problem, outside this review). The contradiction between issue time and reported actual time holds as written.
- Condition: no actual event in the advice is later than its issue time, and the actual despatch (pickup) time agrees with the pickup the transport documents record.
- Options: (a) ActualDespatchTime 15:05, the pickup (preferred: matches the definition, the waybill and the status, and then lies before the issue at 15:15, so both problems go with one change); (b) issue the advice after 16:20 and move the waybill's pickup to 16:20, if the hand-over is meant to be after the export release; (c) give 16:20 as estimated despatch.
- Needs decision: no
- From: broad (F1), logistics (F1, F3), context (F2)

### road/04#F2 · High · Emission factor × base does not give the emission value
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". 0.82 per 1 EA gives 0.82 kg CO2e per bench, not 96; 96 / 0.82 = 117.1 matches no count, material mass (56.5 kg consumed) or bench weight of the flow (recalculated in the merge). 39 examples, 9 in this flow (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'`).
- Condition: factor × (activity / base) equals the value, or factor and base are absent.
- Options: (a) drop factor and base (preferred, as in road/01 and the rail merge); (b) a factor and base whose product is 96 kg.
- Needs decision: no
- From: broad (F2), logistics (F2), context (F4)

### road/04#F3 · Medium · Urvanian province in Region instead of CountrySubentity
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is `CountrySubentity` ("The political or administrative division of a country ..."), which the Bayvarran address of the same document uses (`/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 files (`grep -rho`/`grep -rl --include='*.xml' '<cbc:Region>Province of'`).
- Condition: the province is in `CountrySubentity`; `Region` is absent or a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred); (b) define Urvanian provinces as non-administrative regions in the world's address rules.
- Needs decision: no
- From: broad (F3), parties (F1), context (F5)

### road/04#F4 · Medium · LocaleCode holds a language code
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (ISO 639) repeats `Language/ID` and names no locale. 362 occurrences in 213 files (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>en</cbc:LocaleCode>'`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) drop it (preferred; broad, parties, rail and air merges); (b) `en-XB` with a locale list (context).
- Needs decision: no
- From: broad (F4), parties (F2), context (F6)

### road/04#F5 · Medium · Gate number in AdditionalStreetName of Lumeway's address
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; `Gate 3` is an entrance of the business park, not part of the delivery customer's postal address. 79 occurrences in 76 files.
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance; where it matters for the delivery it is in a delivery location.
- Options: (a) drop the gate from the address (preferred); (b) carry it in the shipment's delivery location.
- Needs decision: no
- From: broad (F5), parties (F3)

### road/04#F6 · Medium · Lifecycle stage code says manufacturing only, its text says cradle to gate
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: in the world list `LifecycleStageCode`, `MANUFACTURING` is "Making the product (EN 15804 module A3)"; raw material supply and transport (A1, A2) is `SOURCING`. The text and description cover A1–A3 (cradle to gate), so the code names a narrower stage than the figure and its text.
- Condition: code and text name the same stage(s), and the figure covers exactly what they name.
- Options: (a) omit the code, keep the cradle-to-gate text (preferred); (b) keep `MANUFACTURING` and reduce figure and texts to A3.
- Needs decision: no
- From: context (F1)

### road/04#F7 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty ..."; the value is from the world list `EmissionBoundaryCode` (semantic conformance, UBL 2.5 §4.7). 39 examples do the same.
- Condition: the element is absent from this item emission or says how full transport equipment is; the boundary, if kept, is in text.
- Options: (a) drop it and state the boundary in text, recording the missing element for the UBL TC write-up (preferred).
- Needs decision: no
- From: context (F3)

### road/04#F8 · Low · NoStatus status codes carry nothing
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cbc:LineStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cbc:LineStatusCode` = `NoStatus`
- Why: `DocumentStatusCode` is "A code signifying the status of the Despatch Advice with respect to its original state. This code may be used if the document precedes the event and is subsequently found to be incorrect and in need of cancellation or revision"; `LineStatusCode` "the status of this despatch line with respect to its original state". This is an original advice with original lines; "no status" says what absence would say (IND6, no fillers). Context cited line 2's code as evidence in its F7 without making it a finding. Added by the merge, aligned with the rail and air merges (air 06/08 despatch advices). Unlike `02-OrderResponse.xml`, where `NoStatus` on line 1 distinguishes the unchanged line from the revised line 2, no line here is revised.
- Condition: the status codes are absent, or carry a status the advice or line actually has.
- Options: drop them (preferred).
- Needs decision: no
- From: merge

### road/04#F9 · Low · Contacts that do not fit their roles in the despatch
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the despatch supplier's contact is named `Warehouse office` but has a sales customer-service job title and department, so name, job title and department disagree; the delivery customer's contact receives the goods (goods-in), but Lumeway gives its customer service in Sales.
- Condition: the despatch party's contact agrees with itself and fits the warehouse; the delivery customer's contact is the receiving function.
- Options: (a) a warehouse job title and department for Castrano and a goods-in contact for Lumeway (preferred); (b) drop job title and department where none fits.
- Needs decision: no
- From: broad (F6), parties (F5), context (F8)

### road/04#F10 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Castrano and Trasvia share 1 January 1996, a public holiday; 271 occurrences in 181 files for at least 25 companies (`grep -rho`/`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`). A filler (IND5).
- Condition: each party's `RegistrationDate` is its own plausible date, or absent.
- Options: (a) own dates from the companies' histories (preferred); (b) leave them out.
- Needs decision: yes (company history; aligned with the rail and air merges)
- From: parties (F4)

### road/04#F11 · Low · Party master data the despatch advice does nothing with
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cac:ShareholderParty/cbc:ParticipationPercent` = `100`
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- Why: the seller's stock-exchange listing, the despatch supplier's shareholder and the carrier's operating permit play no part in announcing what was despatched (section 4.8, IND5). The permit is the weakest part: parties refuted it as borderline (the advice says who carries the goods across the border, and the licence qualifies that carrier); the merge keeps it with that argument because nothing in the advice refers to it.
- Condition: every party detail in the advice has a use in announcing or receiving the despatch.
- Options: drop them (preferred); keep the permit only if the advice makes it relevant.
- Needs decision: no
- From: parties (F6), context (F9)

### road/04#F12 · Low · Release identifier that no other example issues
- XPath: `/DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ReleaseID` = `XU-EX-REL-55120`
- Why: `ReleaseID` is "An identifier for the release of the despatch used as security control or cargo control (pick-up)"; its prefix makes it an Urvanian export release. The export declaration of the shipment (`05-ExportCustomsDeclaration.xml`, IDs VI-EX-26-0155 and VI-CD-26-0156) carries no release number, and the waybill only says the truck waits until customs has released the declaration; no XML of the flow contains the value (`grep -l 'XU-EX-REL' road/*.xml` finds only this file). Context refuted the value as having no use (it fits an export release shown at pickup) and left the link question outside its lens; the merge follows both: the element fits, the link is missing.
- Condition: the release identifier can be traced to the export clearance it confirms, or `ReleaseID` is absent.
- Options: (a) let the export declaration or the waybill's customs reference carry the same release number (preferred); (b) remove `ReleaseID`.
- Needs decision: no
- From: logistics (F5)

### road/04#F13 · Low · Item number reads as a real GTIN-12
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- Why: 12 digits with a valid GS1 mod-10 check digit (recomputed: 7), readable as a GTIN-12 in the GS1 US range; `771` is a GS1 prefix range (GS1 Colombia; own knowledge). Fictional values must not be mistakable for real register entries.
- Condition: the item numbers cannot be read as validly check-digited GTINs of a real GS1 prefix.
- Options: (a) a non-GS1 structure, or GS1 prefix 952 if the scheme is meant to mimic GTIN (preferred); (b) drop `IssuerScopeID`/`BarcodeSymbologyID`.
- Needs decision: yes (the world's item scheme; aligned with road/01, rail, plastics)
- From: broad (F7)

### road/04#F14 · Low · Catalogue and product-passport data the despatch advice does nothing with
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission`
- Why: a despatch advice tells the receiver what was sent so that it can check it on arrival; keywords, warranty, circularity profile and LCA emission are catalogue or passport data that neither the despatch nor the receipt that follows uses (section 4.8, IND5).
- Condition: the despatch line's item carries what identifies and describes the despatched goods, and no catalogue data without a use.
- Options: (a) drop keyword, warranty, circularity profile and emission from the line (preferred); (b) keep them only if the story gives the advice a role in passing on product data.
- Needs decision: no
- From: context (F10)

### road/04#F15 · Low · Side frames despatched without saying they are the substituted 2026 casting
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `VI-C180`
- XPath: `02-OrderResponse.xml:/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `2026`
- Why: the order response replaced the ordered side frame by the 2026 casting, identified with `ExtendedID` ("An extended identifier for the item that identifies the item with specific properties") 2026. The despatch advice, which says what was actually sent, identifies the item only as `VI-C180` with the ordered description; only the manufacture date 2026-03-20 hints at the new casting. No example after the order response carries ExtendedID 2026 (`grep -l '<cbc:ExtendedID>2026<' road/*.xml` finds only 02), while `16-ApplicationResponse.xml:/ApplicationResponse/cac:DocumentResponse/cac:LineResponse/cac:Response/cbc:Description` = `Matched to the substituted 2026 casting.`
- Condition: the despatch line identifies the casting actually shipped as the order response does (`ExtendedID` 2026 or equivalent).
- Options: (a) carry `ExtendedID` 2026 (and, if useful, the data sheet `VI-DS-C180-2026`) on line 2 (preferred); (b) a line note naming the 2026 casting.
- Needs decision: no
- From: broad (F8), logistics (F4), context (F7)

### road/04#F16 · Low · RegistrationID on castings that have no registration
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:RegistrationID` = `VI-QR-01490`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-01490`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:ProductTraceID` = `VI-TR-01490`
- Why: `RegistrationID` is "The registration identifier of this item instance"; a spare side frame is registered nowhere in the flow, and `VI-QR-…` reads as the number of a QR label, a third rendering of the serial's running number (context). The same applies to all 12 instances (`ItemInstance[1]` to `ItemInstance[12]`). Broad refuted the three identifiers as filler: trace, registration and serial are distinct concepts, and replacement castings are tracked individually for warranty. The merge cannot settle whether a warranty registration exists in the world: kept as Low with both arguments.
- Condition: `RegistrationID` is absent on the castings, or names a registration the castings have in the world (e.g. a warranty register), stated somewhere in the flow.
- Options: (a) drop `RegistrationID`, keep serial and trace IDs (preferred: nothing in the flow registers castings); (b) state the register if the world has one.
- Needs decision: yes
- From: context (F11)

## Checked and consistent
- `OrderReference` LD-PO-26-0149 resolves to `01-Order.xml`; delivered quantities 96 and 12 equal the order and the order response; order line references 1 and 2 match; `LineCountNumeric` 2 (broad, logistics, context).
- Shipment CL-SH-26-0154, consignment LD-CS-26-0152 (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cbc:ID` = `LD-CS-26-0152`) and gross 4106.4 kg agree with 03, 05, 06, 08 and 10 (broad, logistics, context).
- "24 pallets of 4 benches" plus one pallet of 12 boxed side frames = 25 handling units and 108 packages, as in the waybill (broad, logistics, context).
- 12 item instances (serials VI-SF-01490 to VI-SF-01501, consecutive and unique) for 12 side frames, one melt M-26-0412 cast 2026-03-20 06:40; manufacture dates before despatch (broad, logistics, context).
- Export declaration `05-ExportCustomsDeclaration.xml` issued 13:25, before the pickup at 15:05 (broad).
- Packaging waste 0.4 kg × 96 = 38.4 kg lies within the 344.4 kg between the waybill's gross (4106.4) and net (3762) weight (logistics).
- `DespatchAdviceTypeCode` DELIVERY ("Goods sent to the buyer against an order") fits a single complete despatch (context).
- Party identity and roles agree with 01 and 08; Castrano's shareholder Valdara (100 %) agrees with Valdara's service provider; GLN and ISIN check digits pass (parties, broad).

## Considered and refuted
- `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:ItemInstance`: one instance for 96 benches — refuted because it carries only lot and manufacture date, UBL's way of lot-level traceability (from broad).
- `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:RegistrationID` = `VI-QR-01490`: three identifiers per casting as filler — refuted by broad (distinct concepts, warranty tracking); not followed in full by the merge, see F16.
- Pickup 15:05 in the waybill vs actual despatch 16:20 here — refuted by broad (despatch = truck leaving); not followed by the merge, see F1.
- `/DespatchAdvice/cac:Shipment/cbc:GrossWeightMeasure`: shipment gross weight without transport equipment — refuted because the goods travel loose on the haulier's trailer, which belongs to the means of transport (from logistics).
- `/DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ReleaseID` = `XU-EX-REL-55120`: a value without a use — refuted because it fits an export release shown at pickup (from context); the missing link to the declaration is F12.
- `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty`: master data — refuted because it states why Castrano despatches for Valdara (from context).
- `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization`: carrier licence copied — refuted by parties as borderline; kept by the merge as the weakest part of F11, with the argument.
- `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]`: Italian-looking name tagged `en-XU` — refuted: proper names, subtag follows the sender (from parties).
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:AdditionalPartyIdentification[1]/cbc:ID`: real GLN — refuted: prefix 952, check digit correct (from parties).
- `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Telephone`: real numbers — refuted: +999 reserved (from parties).
- `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: contract number — refuted: the definition does not say who assigns it (from parties).

## Changed in the merge
- broad/F1, logistics/F1, logistics/F3, context/F2 → F1: combined into one finding because one change (ActualDespatchTime 15:05) resolves both; logistics/F3's Medium absorbed into the High; preferred option changed from "issue after 16:20" (broad, logistics/F1, context) to 15:05 (logistics/F3), because the definition says pickup and 09 confirms 15:05.
- broad/F2, logistics/F2, context/F4 → F2: combined; context's Medium raised to High (arithmetic); preferred option drop factor and base.
- broad/F3, parties/F1, context/F5 → F3; broad/F4, parties/F2, context/F6 → F4 (parties' "Needs decision: yes" set to no); broad/F5, parties/F3 → F5: combined.
- context/F1 → F6: High lowered to Medium, aligned with road/01 and the rail merge.
- context/F3 → F7: unchanged apart from wording.
- F8: added by the merge (`NoStatus`), aligned with the rail and air merges.
- broad/F6, parties/F5, context/F8 → F9: combined.
- parties/F4 → F10: "Needs decision" set to yes (aligned with the rail and air merges).
- parties/F6, context/F9 → F11: combined; parties' refutation of the carrier permit carried.
- broad/F8, logistics/F4, context/F7 → F15: combined; context's `LineStatusCode` XPath moved to F8.
- context/F11 → F16: "Needs decision" set to yes and broad's refutation carried, since the merge cannot settle whether castings are registered.

## Outside this review
- `08-Waybill.xml` is issued 2026-03-23 08:16 but reports the actual pickup at 15:05 and the departure at 16:20 of the same day; a problem of 08 (documents reporting events after their issue time).
- The timeline between pickup (15:05) and departure (16:20), and the export release in between, is a cross-document question (noted by parties).
