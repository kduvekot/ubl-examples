# LLM review: 10-ImportCustomsDeclaration.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/10-ImportCustomsDeclaration.xml`, Git blob `e4f412380312e36eb2dbbc9f243cbc69a0fee18e` (committed)
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

### road/10#F1 · High · Import declared after the status report says it was accepted and the goods released
- XPath: `/ImportCustomsDeclaration/cbc:IssueDate` = `2026-03-24`
- XPath: `/ImportCustomsDeclaration/cbc:IssueTime` = `09:54:00`
- Why: the carrier's status report says the border was passed at 08:55 with the import declaration "accepted by Bayvarra's customs" and the goods released (`09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:SubStatus/cbc:Description` = `Import declaration accepted by Bayvarra's customs.`, issued at `09-TransportationStatus.xml:/TransportationStatus/cbc:IssueTime` = `09:10:00`). This declaration, the only import declaration of the consignment, is issued an hour after the release it was needed for.
- Condition: the import declaration is issued before the time at which the flow reports it accepted and the goods released.
- Options: (a) issue it before the border crossing (pre-lodged, e.g. on 2026-03-23 after despatch or early on 2026-03-24) (preferred: release at the border needs a lodged declaration); (b) move the release to a later status report.
- Needs decision: no

### road/10#F2 · High · Lifecycle stage code says manufacturing only, its text says cradle to gate
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies" and `LifecycleStageDescription` "The lifecycle stage to which this emission applies, expressed as a text", so both must name the same stage. In the world list `LifecycleStageCode`, `MANUFACTURING` is "Making the product (EN 15804 module A3)"; raw material supply and its transport (A1, A2) is `SOURCING`. The text and the emission's description include mining, steel making and the transport between the steps, i.e. A1 to A3 (cradle to gate, as the boundary code next to it also says). Code and text contradict each other. The same item data occurs in 9 examples of the flow (`grep -l MANUFACTURING world/examples/road/*.xml`).
- Condition: the lifecycle stage code and text name the same stage(s), and the emission figure covers exactly what they name.
- Options: (a) keep the cradle-to-gate figure and state the stage in text only, or with a code covering A1 to A3 if the world list gets one (preferred: the figure is a cradle-to-gate figure); (b) keep `MANUFACTURING` and reduce figure, text and description to module A3.
- Needs decision: no

### road/10#F3 · Medium · Reference to the certificate of origin resolves to two different documents
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `FCC-CO-26-0157`
- Why: the reference carries only the ID, and two examples have it: the submitted application (`06-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:ID` = `FCC-CO-26-0157`, status submitted, issuer endorsement pending) and the issued certificate (`07-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:ID` = `FCC-CO-26-0157`, approved), with the same version. Customs needs the issued certificate; neither a type, a version, a UUID nor an issue date says which one is meant.
- Condition: the reference identifies exactly one document, the issued certificate of origin, and says what it is.
- Options: (a) give the reference the document type (certificate of origin) and the UUID or issue date of `07-CertificateOfOrigin.xml` (preferred: works even if the IDs stay the same); (b) resolve the duplicate ID in the certificates (see their reviews).
- Needs decision: no

### road/10#F4 · Medium · The customs service is described as a company in the business register
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: `CorporateRegistrationScheme` is "The corporate registration scheme used to register the party" and `CompanyLiquidationStatusCode` "A code signifying the party's liquidation status". The Customs and Border Service of Bayvarra is a state authority (ISIC 8411); it is not entered in the business register and cannot go into liquidation.
- Condition: the customs party carries no business-register scheme and no liquidation status.
- Options: (a) drop `PartyLegalEntity` from the customs party (preferred); (b) describe it with a register of public bodies, if the world has one, without liquidation status.
- Needs decision: no

### road/10#F5 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: UBL 2.5 defines `EmissionCalculationMethod/FullnessIndicationCode` as "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the emission". The value comes from the world list `EmissionBoundaryCode` (how much of a product's life the figure covers), which has nothing to do with the load of transport equipment (semantic conformance, UBL 2.5 §4.7). 39 examples do the same (`grep -rl 'FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode"'` over `*.xml`); the other uses of the element take `LoadTypeCode`, which fits the definition.
- Condition: `FullnessIndicationCode` is absent from this item emission, or says how full transport equipment is; the system boundary, if kept, is stated where UBL allows it (e.g. in text).
- Options: (a) drop it and state the boundary in `LifecycleStageDescription` or `Description` (preferred: an item's cradle-to-gate figure involves no transport equipment); (b) record the missing boundary element as a finding for the UBL TC.
- Needs decision: no

### road/10#F6 · Medium · Emission factor and base do not give the stated emission
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 EA the factor says 0.82 kg CO2e per bench, but the value for one bench is 96 kg (96 / 0.82 = 117.1 benches, matching nothing in the flow). The factor cannot have produced the value, so it does nothing here or is the wrong figure.
- Condition: `ValueFactorNumeric` × the activity quantity in the unit of `ValueBaseMeasure` gives `ValueMeasure`, or factor and base are absent.
- Options: (a) drop factor and base, since the value is a per-item figure from the LCA (preferred); (b) state a factor and base whose product is 96 kg per bench.
- Needs decision: no

### road/10#F7 · Medium · Province given as Region
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country ... such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the flow use for their state (`Upland State`). 104 examples carry a province in `Region` (`grep -rl '<cbc:Region>Province'` over `*.xml`).
- Condition: the Urvanian province is in `CountrySubentity`; `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no

### road/10#F8 · Medium · LocaleCode holds a language code
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region (e.g. `en-XB`, the form the examples use in `languageID`). `en` with `listID` ISO 639 repeats `Language/ID` and names no locale. All 362 `LocaleCode` elements in the examples are `en` with ISO 639 (`grep -rho '<cbc:LocaleCode[^<]*<'` over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) `en-XB` with a locale list (BCP 47 / CLDR style) as listID (preferred: matches the `languageID` already used); (b) drop it.
- Needs decision: no

### road/10#F9 · Low · Urvanian national tariff code in Bayvarra's import declaration
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: the goods are declared for free circulation in Bayvarra, so the national subheading that matters is Bayvarra's tariff; both goods items carry the Urvanian tariff (`listID` `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`), copied from the export side. The world has no Bayvarran tariff list (only `XU-CustomsTariffCode` in `world/codelists/gc`), so either the accord uses one common tariff, which the list's name does not say, or the declaration carries a code Bayvarra's customs does not use.
- Condition: the national commodity code in the import declaration is from the tariff the importing country applies, or is absent (leaving the HS code).
- Options: (a) drop the national code from the import declaration and keep the HS code (preferred: no Bayvarran tariff exists in the world); (b) add a Bayvarran (or Trade Accord) tariff list and use it.
- Needs decision: yes

### road/10#F10 · Low · Contacts that do not fit an import declaration
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: customs contacts the importer's import or customs function about its declaration, not its customer service in Sales; the consignor's order desk plays no part in Bayvarra's import.
- Condition: the importer's contact handles imports or customs; the consignor carries no contact, or one that fits.
- Options: (a) an import/customs contact for Lumeway and no consignor contact (preferred); (b) drop the job titles and departments that do not fit.
- Needs decision: no

### road/10#F11 · Low · Master and product data the import declaration does nothing with
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: an import declaration needs the goods' description, classification, origin, quantity, weight and customs value. The consignor's stock-exchange listing, search keywords, warranty, the circularity profile and the product's emission figure play no part in it (section 4.8, IND5).
- Condition: party and item data in the declaration have a use for declaring the import.
- Options: drop them (preferred).
- Needs decision: no

### road/10#F12 · Low · Signature ID built from the example's flow name
- XPath: `/ImportCustomsDeclaration/cac:Signature/cbc:ID` = `LD-SIG-IM-road`
- Why: `road` is the name of this example flow in the repository and has no meaning for Lumeway or customs; the signature carries nothing but the ID and the signer. 14 signature IDs end in a flow name (`grep -rhoE '<cbc:ID>[A-Z]+-SIG-[^<]*-[a-z]+<'` over `*.xml`).
- Condition: the signature ID follows the signer's own numbering, without repository names.
- Options: (a) a Lumeway signature number after the declaration ID (preferred); (b) drop the signature.
- Needs decision: no

## Checked and consistent
- Shipment `CL-SH-26-0154`, gross weight 4 106.4 kg, quantities 96 and 12 EA and the despatch line references (`CL-DA-26-0153` lines 1 and 2) match `04-DespatchAdvice.xml`.
- `PreviousCustomsDeclaration` `VI-CD-26-0156` is the export declaration of `05-ExportCustomsDeclaration.xml`, a fitting previous declaration for a cross-border movement.
- `TypeCode` `IMPORT`, `SubTypeCode` `FREECIRC` and `NatureOfTransactionCode` `PURCHASE` fit a distributor buying benches for resale; the note on duties paid from the importer's account fits.
- Importer = consignee = notifier (Lumeway): `NotifierParty` is "The Party who is responsible for contact on master level", which for an importer declaring itself is the importer.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`: suspected the wrong office for an import declaration — refuted because UBL 2.5's Import Customs Declaration has only `CustomsExitOfficeLocation` ("Customs exit office of the goods being declared"), and the Urvanian exit post is that office; the entry office has no element.
- `/ImportCustomsDeclaration/cac:ValidityPeriod`: suspected meaningless for an import declaration — refuted because UBL defines it as "A period, assigned by the issuer, during which the information in the declaration is valid", which a declarant may set.
