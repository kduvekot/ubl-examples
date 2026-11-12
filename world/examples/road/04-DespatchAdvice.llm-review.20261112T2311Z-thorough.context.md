# LLM review: 04-DespatchAdvice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/04-DespatchAdvice.xml`, Git blob `d5694687ad07a0bd4b1b8412513e13a712a00375` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### road/04#F1 · High · Lifecycle stage code says manufacturing only, its text says cradle to gate
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies" and `LifecycleStageDescription` "The lifecycle stage to which this emission applies, expressed as a text", so both must name the same stage. In the world list `LifecycleStageCode`, `MANUFACTURING` is "Making the product (EN 15804 module A3)"; raw material supply and its transport (A1, A2) is `SOURCING`. The text and the emission's description include mining, steel making and the transport between the steps, i.e. A1 to A3 (cradle to gate, as the boundary code next to it also says). Code and text contradict each other. The same item data occurs in 9 examples of the flow (`grep -l MANUFACTURING world/examples/road/*.xml`).
- Condition: the lifecycle stage code and text name the same stage(s), and the emission figure covers exactly what they name.
- Options: (a) keep the cradle-to-gate figure and state the stage in text only, or with a code covering A1 to A3 if the world list gets one (preferred: the figure is a cradle-to-gate figure); (b) keep `MANUFACTURING` and reduce figure, text and description to module A3.
- Needs decision: no

### road/04#F2 · High · Actual despatch reported for a time after the advice was issued
- XPath: `/DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ActualDespatchTime` = `16:20:00`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ActualDespatchDate` = `2026-03-23`
- XPath: `/DespatchAdvice/cbc:IssueTime` = `15:15:00`
- Why: `ActualDespatchDate`/`Time` is "The actual despatch (pickup) date/time"; an actual event can only be reported once it has happened, but the advice issued on 2026-03-23 at 15:15 states a despatch at 16:20 the same day. The waybill also has the departure at 16:20 (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `16:20:00`), so the despatch time is right and the issue time is too early (or the value is an estimate).
- Condition: the actual despatch time is not later than the issue time, or the value is given as an estimate.
- Options: (a) issue the advice after the truck has left (e.g. 16:30) (preferred: a despatch advice normally follows the despatch); (b) state the time as `EstimatedDespatchDate`/`Time`.
- Needs decision: no

### road/04#F3 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: UBL 2.5 defines `EmissionCalculationMethod/FullnessIndicationCode` as "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the emission". The value comes from the world list `EmissionBoundaryCode` (how much of a product's life the figure covers), which has nothing to do with the load of transport equipment (semantic conformance, UBL 2.5 §4.7). 39 examples do the same (`grep -rl 'FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode"'` over `*.xml`); the other uses of the element take `LoadTypeCode`, which fits the definition.
- Condition: `FullnessIndicationCode` is absent from this item emission, or says how full transport equipment is; the system boundary, if kept, is stated where UBL allows it (e.g. in text).
- Options: (a) drop it and state the boundary in `LifecycleStageDescription` or `Description` (preferred: an item's cradle-to-gate figure involves no transport equipment); (b) record the missing boundary element as a finding for the UBL TC.
- Needs decision: no

### road/04#F4 · Medium · Emission factor and base do not give the stated emission
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 EA the factor says 0.82 kg CO2e per bench, but the value for one bench is 96 kg (96 / 0.82 = 117.1 benches, matching nothing in the flow). The factor cannot have produced the value, so it does nothing here or is the wrong figure.
- Condition: `ValueFactorNumeric` × the activity quantity in the unit of `ValueBaseMeasure` gives `ValueMeasure`, or factor and base are absent.
- Options: (a) drop factor and base, since the value is a per-item figure from the LCA (preferred); (b) state a factor and base whose product is 96 kg per bench.
- Needs decision: no

### road/04#F5 · Medium · Province given as Region
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country ... such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the flow use for their state (`Upland State`). 104 examples carry a province in `Region` (`grep -rl '<cbc:Region>Province'` over `*.xml`).
- Condition: the Urvanian province is in `CountrySubentity`; `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no

### road/04#F6 · Medium · LocaleCode holds a language code
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region (e.g. `en-XB`, the form the examples use in `languageID`). `en` with `listID` ISO 639 repeats `Language/ID` and names no locale. All 362 `LocaleCode` elements in the examples are `en` with ISO 639 (`grep -rho '<cbc:LocaleCode[^<]*<'` over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) `en-XB` with a locale list (BCP 47 / CLDR style) as listID (preferred: matches the `languageID` already used); (b) drop it.
- Needs decision: no

### road/04#F7 · Low · The despatched side frames do not say they are the substituted 2026 casting
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `VI-C180`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cbc:LineStatusCode` = `NoStatus`
- Why: the order response replaced the ordered side frame by the 2026 casting (`02-OrderResponse.xml:/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `2026`). A despatch advice says what was actually sent; line 2 identifies only the base item `VI-C180`, without the extended ID or a reference to the 2026 data sheet, so the buyer cannot tell from it that the substituted casting arrived (only the manufacture date 2026-03-20 hints at it).
- Condition: line 2 identifies the despatched casting as the 2026 variant the order response substituted (e.g. `ExtendedID` `2026`).
- Options: (a) add the extended ID `2026` (and, if useful, the data sheet `VI-DS-C180-2026`) to the item (preferred: same identification as in the order response); (b) a line note saying the 2026 casting was sent.
- Needs decision: no

### road/04#F8 · Low · Contacts that do not fit their roles in the despatch
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the despatch supplier's contact is named "Warehouse office" but has a sales customer-service job title and department, so name, job title and department disagree. The delivery customer's contact receives the goods (goods-in), but the document names Lumeway's customer service in Sales.
- Condition: the despatch party's contact has a name, job title and department that agree and fit the warehouse; the delivery customer's contact is the receiving function.
- Options: (a) a warehouse job title and department for Castrano and a goods-in contact for Lumeway (preferred); (b) drop the job title and department where none fits.
- Needs decision: no

### road/04#F9 · Low · Party master data the despatch advice does nothing with
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cac:ShareholderParty/cbc:ParticipationPercent` = `100`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- Why: the seller's stock-exchange listing, the despatch supplier's shareholder and the carrier's operating permit play no part in announcing what was despatched; they look copied from master data (section 4.8, IND5).
- Condition: every party detail in the despatch advice has a use in announcing or receiving the despatch.
- Options: drop them (preferred).
- Needs decision: no

### road/04#F10 · Low · Item master data the despatch advice does nothing with
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: a despatch advice tells the receiver what was sent so that it can check it on arrival. Search keywords, warranty text, the circularity profile (maintenance, materials, waste, repairability) and the product's LCA emission are catalogue or product-passport data; nothing in the despatch or the receipt that follows uses them. The identification, description, lot and dimensions are what the receiver checks.
- Condition: the item in the despatch line carries what identifies and describes the despatched goods, and no catalogue data without a use in this despatch.
- Options: (a) drop keyword, warranty, circularity profile and environmental emission from the despatch line (preferred); (b) keep them only if the story gives the despatch advice a role in passing on product data (it does not now).
- Needs decision: no

### road/04#F11 · Low · RegistrationID on castings that have no registration
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:RegistrationID` = `VI-QR-01490`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-01490`
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:ProductTraceID` = `VI-TR-01490`
- Why: `ItemInstance/RegistrationID` is "An identifier used for registration of this item instance" (e.g. a registered vehicle or device). A spare side frame is not registered anywhere; the value `VI-QR-…` reads as the number of a QR label, i.e. a third rendering of the same running number as the serial and trace IDs. The same applies to all 12 instances (`ItemInstance[1]` to `ItemInstance[12]`).
- Condition: `RegistrationID` is absent on the castings, or names a registration the castings really have.
- Options: (a) drop `RegistrationID` and keep serial and trace IDs (preferred); (b) state the register if the world has one for castings.
- Needs decision: no

## Checked and consistent
- `OrderReference` `LD-PO-26-0149` resolves to `01-Order.xml`; despatched quantities 96 and 12 EA match the order and the order response; line 1's note (24 pallets of 4) and the transport request's 25 pallets (24 for the benches plus one for the side frames) agree.
- Consignment `LD-CS-26-0152` is the one of the transport request (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cbc:ID` = `LD-CS-26-0152`) with the same gross weight 4106.4 kg; the carrier is the buyer's haulier.
- `DespatchAdviceTypeCode` `DELIVERY` ("Goods sent to the buyer against an order") fits a single complete despatch.
- Manufacture date of lot and castings (2026-03-20) is before despatch.

## Considered and refuted
- `/DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ReleaseID` = `XU-EX-REL-55120`: suspected a value without a use — refuted because "An identifier for the release of the despatch used as security control or cargo control (pick-up)" fits an export release that the haulier shows at pickup, which the order's instruction to have the export declaration ready implies (that the release appears in no other example, so it cannot be linked to `05-ExportCustomsDeclaration.xml`, is a reference question outside the context lens).
- `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty`: suspected master data — refuted because it states why Castrano despatches for Valdara.
