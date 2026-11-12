# LLM review: 13-ReceiptAdvice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/13-ReceiptAdvice.xml`, Git blob `604fd2f166bf65e6e949e78ef14e8423b7c4b8ad` (committed)
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

### road/13#F1 · High · Lifecycle stage code says manufacturing only, its text says cradle to gate
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies" and `LifecycleStageDescription` "The lifecycle stage to which this emission applies, expressed as a text", so both must name the same stage. In the world list `LifecycleStageCode`, `MANUFACTURING` is "Making the product (EN 15804 module A3)"; raw material supply and its transport (A1, A2) is `SOURCING`. The text and the emission's description include mining, steel making and the transport between the steps, i.e. A1 to A3 (cradle to gate, as the boundary code next to it also says). Code and text contradict each other. The same item data occurs in 9 examples of the flow (`grep -l MANUFACTURING world/examples/road/*.xml`).
- Condition: the lifecycle stage code and text name the same stage(s), and the emission figure covers exactly what they name.
- Options: (a) keep the cradle-to-gate figure and state the stage in text only, or with a code covering A1 to A3 if the world list gets one (preferred: the figure is a cradle-to-gate figure); (b) keep `MANUFACTURING` and reduce figure, text and description to module A3.
- Needs decision: no

### road/13#F2 · Medium · "Revised" receipt advice that does not say what it revises
- XPath: `/ReceiptAdvice/cbc:DocumentStatusCode` = `Revised`
- XPath: `/ReceiptAdvice/cbc:ID` = `LD-RA-26-0164`
- XPath: `/ReceiptAdvice/cbc:Note` = `Recounted: all benches received; one box of side frames over.`
- Why: `DocumentStatusCode` `Revised` means "Document has been revised"; this receipt advice replaces the cancelled one (`11-ReceiptAdvice.xml:/ReceiptAdvice/cbc:ID` = `LD-RA-26-0162`, cancelled by `12-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:ReceiptDocumentReference/cbc:ID` = `LD-RA-26-0162`), but it has a new ID and refers neither to the receipt advice it corrects nor to the cancellation. The despatch party cannot link the revision to the document it revises.
- Condition: the corrected receipt advice refers to the receipt advice it replaces (or to the cancellation), or its status says it is a new original.
- Options: (a) add a document reference to `LD-RA-26-0162` (and, if wanted, `LD-DOC-26-0163`) with a type or description (preferred: the status then has an object); (b) keep the new ID with status `NoStatus` and let the cancellation's note carry the link.
- Needs decision: no

### road/13#F3 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: UBL 2.5 defines `EmissionCalculationMethod/FullnessIndicationCode` as "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the emission". The value comes from the world list `EmissionBoundaryCode` (how much of a product's life the figure covers), which has nothing to do with the load of transport equipment (semantic conformance, UBL 2.5 §4.7). 39 examples do the same (`grep -rl 'FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode"'` over `*.xml`); the other uses of the element take `LoadTypeCode`, which fits the definition.
- Condition: `FullnessIndicationCode` is absent from this item emission, or says how full transport equipment is; the system boundary, if kept, is stated where UBL allows it (e.g. in text).
- Options: (a) drop it and state the boundary in `LifecycleStageDescription` or `Description` (preferred: an item's cradle-to-gate figure involves no transport equipment); (b) record the missing boundary element as a finding for the UBL TC.
- Needs decision: no

### road/13#F4 · Medium · Emission factor and base do not give the stated emission
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 EA the factor says 0.82 kg CO2e per bench, but the value for one bench is 96 kg (96 / 0.82 = 117.1 benches, matching nothing in the flow). The factor cannot have produced the value, so it does nothing here or is the wrong figure.
- Condition: `ValueFactorNumeric` × the activity quantity in the unit of `ValueBaseMeasure` gives `ValueMeasure`, or factor and base are absent.
- Options: (a) drop factor and base, since the value is a per-item figure from the LCA (preferred); (b) state a factor and base whose product is 96 kg per bench.
- Needs decision: no

### road/13#F5 · Medium · Province given as Region
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ReceiptAdvice/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country ... such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the flow use for their state (`Upland State`). 104 examples carry a province in `Region` (`grep -rl '<cbc:Region>Province'` over `*.xml`).
- Condition: the Urvanian province is in `CountrySubentity`; `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no

### road/13#F6 · Medium · LocaleCode holds a language code
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region (e.g. `en-XB`, the form the examples use in `languageID`). `en` with `listID` ISO 639 repeats `Language/ID` and names no locale. All 362 `LocaleCode` elements in the examples are `en` with ISO 639 (`grep -rho '<cbc:LocaleCode[^<]*<'` over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) `en-XB` with a locale list (BCP 47 / CLDR style) as listID (preferred: matches the `languageID` already used); (b) drop it.
- Needs decision: no

### road/13#F7 · Low · Contacts that do not fit a receipt advice
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the receipt advice is issued by the party that counted the goods at goods-in, so the delivery customer's contact is the receiving function, not Lumeway's customer service in Sales. The despatch supplier's contact is named "Warehouse office" but has a sales customer-service job title and department, so name, job title and department disagree.
- Condition: the delivery customer's contact is goods-in; the despatch supplier's contact has a name, job title and department that agree and fit the warehouse.
- Options: (a) goods-in for Lumeway, a warehouse job title and department for Castrano (preferred); (b) drop job titles and departments that do not fit.
- Needs decision: no

### road/13#F8 · Low · Master and product data the receipt advice does nothing with
- XPath: `/ReceiptAdvice/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PartyLegalEntity/cac:ShareholderParty/cbc:ParticipationPercent` = `100`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: a receipt advice reports what was received against what was despatched. The seller's stock-exchange listing, the despatch supplier's shareholder, search keywords, warranty, the circularity profile and the product's emission figure play no part in that (section 4.8, IND5); the item identification and description are what the receipt needs.
- Condition: party and item data in the receipt advice have a use in reporting the receipt.
- Options: drop them (preferred).
- Needs decision: no

## Checked and consistent
- Order, despatch advice (lines 1 and 2), waybill and shipment resolve as in `11-ReceiptAdvice.xml`.
- Line 1: 96 received = 96 despatched; line 2: 13 received = 12 despatched + 1 oversupply; the note ("all benches received; one box of side frames over") and the line notes agree; this matches the cancellation's reason (`12-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:CancellationNote` = `The recount found the bench reported short; the shortage did not exist.`).
- Issued 2026-03-26 10:48, two minutes after the cancellation (10:46) that announces it ("A corrected receipt advice follows").
- The carrier's invoice refers to this receipt advice (`14-Invoice.xml`), i.e. to the corrected one.

## Considered and refuted
- `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:Note` = `One box more than despatched: picked twice at the 3PL.`, which gives another reason than the cancelled receipt advice ("The mis-picked box, in place of the missing bench"): suspected a contradiction between examples — refuted because the first explanation depended on the shortage that the recount disproved; the corrected document is free to correct the reason too.
