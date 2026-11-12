# LLM review: 05-ExportCustomsDeclaration.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/05-ExportCustomsDeclaration.xml`, Git blob `0fa315bd3a963ac3f8916911094b6904a7e60fbf` (committed)
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

### road/05#F1 · High · Lifecycle stage code says manufacturing only, its text says cradle to gate
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies" and `LifecycleStageDescription` "The lifecycle stage to which this emission applies, expressed as a text", so both must name the same stage. In the world list `LifecycleStageCode`, `MANUFACTURING` is "Making the product (EN 15804 module A3)"; raw material supply and its transport (A1, A2) is `SOURCING`. The text and the emission's description include mining, steel making and the transport between the steps, i.e. A1 to A3 (cradle to gate, as the boundary code next to it also says). Code and text contradict each other. The same item data occurs in 9 examples of the flow (`grep -l MANUFACTURING world/examples/road/*.xml`).
- Condition: the lifecycle stage code and text name the same stage(s), and the emission figure covers exactly what they name.
- Options: (a) keep the cradle-to-gate figure and state the stage in text only, or with a code covering A1 to A3 if the world list gets one (preferred: the figure is a cradle-to-gate figure); (b) keep `MANUFACTURING` and reduce figure, text and description to module A3.
- Needs decision: no

### road/05#F2 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: UBL 2.5 defines `EmissionCalculationMethod/FullnessIndicationCode` as "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the emission". The value comes from the world list `EmissionBoundaryCode` (how much of a product's life the figure covers), which has nothing to do with the load of transport equipment (semantic conformance, UBL 2.5 §4.7). 39 examples do the same (`grep -rl 'FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode"'` over `*.xml`); the other uses of the element take `LoadTypeCode`, which fits the definition.
- Condition: `FullnessIndicationCode` is absent from this item emission, or says how full transport equipment is; the system boundary, if kept, is stated where UBL allows it (e.g. in text).
- Options: (a) drop it and state the boundary in `LifecycleStageDescription` or `Description` (preferred: an item's cradle-to-gate figure involves no transport equipment); (b) record the missing boundary element as a finding for the UBL TC.
- Needs decision: no

### road/05#F3 · Medium · Emission factor and base do not give the stated emission
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 EA the factor says 0.82 kg CO2e per bench, but the value for one bench is 96 kg (96 / 0.82 = 117.1 benches, matching nothing in the flow). The factor cannot have produced the value, so it does nothing here or is the wrong figure.
- Condition: `ValueFactorNumeric` × the activity quantity in the unit of `ValueBaseMeasure` gives `ValueMeasure`, or factor and base are absent.
- Options: (a) drop factor and base, since the value is a per-item figure from the LCA (preferred); (b) state a factor and base whose product is 96 kg per bench.
- Needs decision: no

### road/05#F4 · Medium · Province given as Region
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country ... such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the flow use for their state (`Upland State`). 104 examples carry a province in `Region` (`grep -rl '<cbc:Region>Province'` over `*.xml`).
- Condition: the Urvanian province is in `CountrySubentity`; `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no

### road/05#F5 · Medium · LocaleCode holds a language code
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region (e.g. `en-XB`, the form the examples use in `languageID`). `en` with `listID` ISO 639 repeats `Language/ID` and names no locale. All 362 `LocaleCode` elements in the examples are `en` with ISO 639 (`grep -rho '<cbc:LocaleCode[^<]*<'` over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) `en-XB` with a locale list (BCP 47 / CLDR style) as listID (preferred: matches the `languageID` already used); (b) drop it.
- Needs decision: no

### road/05#F6 · Medium · The customs administration is described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: `CorporateRegistrationScheme` is "The corporate registration scheme used to register the party" and `CompanyLiquidationStatusCode` "A code signifying the party's liquidation status". The Customs Administration of Urvania is a state authority (ISIC 8411, general public administration); it is not entered in the commercial register and cannot go into liquidation. The legal-entity data describe a company, which this party is not.
- Condition: the customs party carries no commercial-register scheme and no liquidation status; if it has a legal-entity description at all, it is that of a public body.
- Options: (a) drop `PartyLegalEntity` from the customs party, keeping name, identifier and address (preferred: the declaration needs only to address the authority); (b) describe it with a register of public bodies, if the world has one, and without liquidation status.
- Needs decision: no

### road/05#F7 · Low · Contacts that do not fit an export declaration
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: customs asks the exporter's contact about the declaration, which is the export or customs function, not the order desk in Sales. The consignee's contact in Lumeway's Sales customer service is the contact for Lumeway's own customers.
- Condition: the exporter's contact handles exports or customs; the consignee's contact, if any, receives or imports goods.
- Options: (a) an export/customs contact for Valdara and drop or replace the consignee's contact (preferred); (b) drop the job title and department where none fits.
- Needs decision: no

### road/05#F8 · Low · Party master data the export declaration does nothing with
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: an export declaration identifies exporter, consignee and carrier; the exporter's stock-exchange listing, the carrier's road haulage permit and the consignee's share capital play no part in it and look copied from master data (section 4.8, IND5).
- Condition: every party detail in the declaration has a use in declaring the export.
- Options: drop them (preferred).
- Needs decision: no

### road/05#F9 · Low · Product passport data in a customs declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:AdditionalItemProperty[5]/cbc:ValueQuantity` = `450`
- Why: customs needs the goods description, commodity code, origin, quantity, weight and value. Search keywords, warranty, the circularity profile, the product's LCA emission and its tested load capacity are catalogue or product-passport data with no role in an export declaration; nothing in the declaration refers to them.
- Condition: the goods items carry what customs needs to identify, classify and value the goods, and no catalogue data without a use in the declaration.
- Options: (a) drop keyword, warranty, item properties, dimensions, circularity profile and environmental emission from the goods items (preferred); (b) keep any of them only where the world's customs rules ask for it.
- Needs decision: no

### road/05#F10 · Low · Additional document reference by ID only
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `LD-PO-26-0149`
- Why: the reference names the buyer's purchase order (`01-Order.xml`) but carries no type code or description, so customs cannot tell what kind of document it is; for a customs declaration the commercial document supporting the declared value would normally be the commercial invoice (`15-Invoice.xml` is issued later, on 2026-03-24).
- Condition: the reference says what the referenced document is (type code or description).
- Options: (a) add a document type (purchase order) (preferred); (b) refer to the commercial document customs actually needs, if the story has one at the time of declaration.
- Needs decision: no

### road/05#F11 · Low · Signature with an ID built from the example's flow name and nothing else
- XPath: `/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `VI-SIG-EX-road`
- Why: `Signature/ID` is "An identifier for this signature". The value ends in `road`, the name of the example flow in this repository, which has no meaning for Valdara or customs; the signature also carries no method, time or attachment, so it states only that someone signed. Counted over `*.xml` with `grep -rhoE '<cbc:ID>[A-Z]+-SIG-[^<]*-[a-z]+<'`, 14 signature IDs end in a flow name.
- Condition: the signature ID follows the signer's own numbering without repository names, and the signature says what it is (e.g. method or time) or is absent.
- Options: (a) a signature ID in Valdara's numbering (e.g. after the declaration ID) with `SignatureMethod` or `ValidationDate` (preferred); (b) drop the signature if the story has no signed declaration.
- Needs decision: no

## Checked and consistent
- Goods items: bench 96 EA, value 4 790 400 XUF (= order line 96 × 49 900), side frames 12 EA, 71 760 XUF (= 12 × 5 980); gross 3 984 + 122.4 = 4 106.4 kg, the shipment's and consignment's gross weight in `04-DespatchAdvice.xml`.
- Shipment `CL-SH-26-0154` and consignment `LD-CS-26-0152` are the ones of the despatch advice; the carrier is Trasvia as in `03-TransportExecutionPlanRequest.xml`.
- `ExportTypeCode` `PERMANENT` and `ExportReasonCode` `SALE` fit a sale of benches to Bayvarra; `FunctionCode` 9 (original) fits a first declaration; validity 90 days from the declaration date matches common export practice (own knowledge: goods must leave within a set period after release).
- Issued 2026-03-23 13:25, before the requested pickup at 14:00 and the despatch, as the order's despatch instruction asks.
- Customs exit office on the Urvanian side of the land border fits a road export to Bayvarra.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`: suspected wrong because the Shipment definition includes "transport equipment" — refuted because the shipment has no transport equipment (benches on pallets on a curtain-side truck, no container or detachable equipment in any document of the flow), so goods plus packaging is the whole figure.
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:ServiceProviderParty`: suspected master data — refuted because it explains that the goods leave from Castrano's warehouse.
