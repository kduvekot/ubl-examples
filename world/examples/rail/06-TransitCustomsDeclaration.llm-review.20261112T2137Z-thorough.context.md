# LLM review: 06-TransitCustomsDeclaration.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/06-TransitCustomsDeclaration.xml`, Git blob `3619a51519aa158336a9817cd911b99963ad4351` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/06#F1 · High · Shipment gross weight excludes the containers that its definition includes
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `7968`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- Why: Shipment/GrossWeightMeasure is "the total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". The goods item weighs 7968 kg with packing (`/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `7968`), and the two containers weigh 7884 kg each with their load: 2 × 7884 = 15768 kg, which implies a tare of (15768 − 7968) / 2 = 3900 kg per 40-foot high cube container, a realistic figure. The shipment total should be 15768 kg; 7968 kg is the goods weight without the containers.
- Condition: Shipment/GrossWeightMeasure = goods with packaging + the containers' tare (= sum of the containers' gross weights, 15768 kg), or the element is absent.
- Options: (a) preferred: 15768 kg; (b) drop the shipment weight and keep goods-item and container weights.
- Needs decision: no

### rail/06#F2 · High · Emission factor × base does not give the emission value
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: The factor is "used to calculate the value measurement (e.g., emissions per unit of activity)", the base is "the base quantity to which the value factor applies". 0.82 × 1 bench = 0.82, not 96 kg CO2e. Same values in 39 examples over `*.xml`.
- Condition: factor × base = value, or factor and base absent.
- Options: (a) preferred: drop factor and base; (b) the real factor and base.
- Needs decision: no

### rail/06#F3 · Medium · Customs offices in elements that mean other offices
- XPath: `/TransitCustomsDeclaration/cac:ImportCustomsExitOfficeLocation/cbc:Name` = `Customs office Marrowdale`
- XPath: `/TransitCustomsDeclaration/cac:TransitCustomsExitOfficeLocation/cbc:Name` = `Customs post at the rail border station, Bayvarran side`
- Why: ImportCustomsExitOfficeLocation is the "customs office of exit of the goods being declared for import" and TransitCustomsExitOfficeLocation the "customs office of exit of the goods being declared for transit". Marrowdale is the inland office where the goods arrive and are imported (the declaration itself gives it as `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfDestinationLocation/cbc:Name` = `Customs office Marrowdale` and as office of import); nothing exits there. The transit does not exit at the Bayvarran border post either: it ends at the office of destination in Marrowdale; the Bayvarran post is the office of entry and of transit, as the consignment states.
- Condition: each office element names an office that performs the function the element names in this transit (or is absent).
- Options: (a) preferred: drop ImportCustomsExitOfficeLocation and TransitCustomsExitOfficeLocation, keeping export exit, departure, transit, entry, destination and import offices; (b) keep them only with offices that fit (e.g. the Urvanian border post as exit of the transit from Urvania, if the world treats the transit as two national legs).
- Needs decision: yes

### rail/06#F4 · Medium · The rail carrier as freight forwarder
- XPath: `/TransitCustomsDeclaration/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`
- Why: FreightForwarderParty is "the Party who combines individual smaller consignments into a single larger shipment (a so-called consolidated consignment or shipment) which is sent to a counterpart". Ferrano Rail Cargo carries one full-container consignment of one consignor (FCL, ConsolidatedIndicator false in the waybill); it is the carrier and already appears as `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`. It consolidates nothing.
- Condition: FreightForwarderParty is absent, or a party that consolidates consignments in this shipment.
- Options: (a) preferred: drop it (the carrier is given); (b) a forwarder, if the story has one.
- Needs decision: no

### rail/06#F5 · Medium · FullnessIndicationCode carries the emission boundary
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The element is "a code signifying whether a piece of transport equipment is full, partially full, or empty", a parameter of a transport emission. A product's cradle-to-gate boundary is no such value. 39 occurrences over `*.xml`.
- Condition: FullnessIndicationCode, where present, says how full transport equipment is.
- Options: (a) preferred: drop it here and carry the boundary in the stage code/description; (b) keep it as a recorded gap for the UBL TC.
- Needs decision: yes

### rail/06#F6 · Medium · Lifecycle stage code covers less than its description
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: MANUFACTURING is EN 15804 module A3 in the world's list; the description covers A1–A3 (SOURCING and MANUFACTURING).
- Condition: code(s) and description name the same stages.
- Options: (a) preferred: two entries; (b) narrow the description.
- Needs decision: no

### rail/06#F7 · Medium · LocaleCode holds a bare language code
- XPath: `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; `en` (ISO 639) names no locale. 362 occurrences over `*.xml`.
- Condition: a locale (e.g. `en-XB`) or absent.
- Options: (a) preferred: `en-XB`; (b) drop it.
- Needs decision: no

### rail/06#F8 · Medium · Province in Region
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: A province is an administrative division (CountrySubentity), not a Region.
- Condition: Urvanian provinces are in CountrySubentity, unless the world defines them otherwise.
- Options: (a) preferred: CountrySubentity; (b) Region with a stated world rule.
- Needs decision: yes

### rail/06#F9 · Low · Product passport data in a customs declaration
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- Why: A transit declaration needs the goods' description, classification, origin, quantity, weight and value. Warranty, keywords, load-capacity test, repairability, maintenance, resource consumption and the product footprint are not used by customs in transit; they are the seller's catalogue data.
- Condition: the goods item carries what the transit procedure uses.
- Options: (a) preferred: reduce the item to description, identification, classification and origin; (b) keep a property only where the story gives customs a use for it.
- Needs decision: no

### rail/06#F10 · Low · Jurisdiction limited to Urvania for a transit ending in Bayvarra
- XPath: `/TransitCustomsDeclaration/cac:JurisdictionRegionAddress/cac:Country/cbc:IdentificationCode` = `XU`
- Why: JurisdictionRegionAddress is "a geographic area in which this declaration is relevant". The transit runs from the office of departure in Ferrano to the office of destination in Marrowdale, Bayvarra, and the declaration names Bayvarran offices of entry, transit, destination and import; it is relevant in both countries (under the Trade Accord).
- Condition: the jurisdiction covers every country whose offices act on the declaration, or the element is absent.
- Options: (a) preferred: a Trade Accord region or both countries, if the world's transit is a common procedure; (b) drop it.
- Needs decision: yes

### rail/06#F11 · Low · Share listing and warehouse provider of the declarant
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:PartyLegalEntity/cac:SecurityListing`
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:ServiceProviderParty`
- Why: Neither the stock-exchange listing nor the warehousing provider of Valdara has a use in the transit declaration.
- Condition: the declarant carries no party data without a reason in the declaration.
- Options: (a) preferred: drop both here.
- Needs decision: no

## Checked and consistent
- TypeCode TRANSIT with SubTypeCode EXTTRANSIT for goods leaving Urvania under transit to Bayvarra; previous export declaration referenced (function EXPORT).
- The seals in the note (XU-VI-30411, XU-VI-30412) are the seals of the two containers, applied by the shipper, intact.
- Container weights: 2 × 7884 kg against 7968 kg goods gives 3900 kg tare each, plausible for 45G1 (see F1).
- Consignment ID VI-CS-26-0327 and shipment ID VI-SH-26-0332 are the same as in the waybill rail/08.
- ISO 6346 check digits of FRXU1044175 and FRXU1044180 pass `check_ids.py`.

## Considered and refuted
- `/TransitCustomsDeclaration/cac:NotifierParty/cac:PartyName/cbc:Name` = `Valdara Industries`: suspected a party without a role here — refuted because the "party responsible for contact on master level" may well be the declarant itself.
- `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:FullnessIndicationCode` = `FCL`: checked — the correct use of FullnessIndicationCode (fullness of a container), unlike F5.

## Outside this review
- Timeline: the declaration placing the goods under transit is issued on 14 April 17:29, but the train left the office of departure (the hub) at 06:52 that morning (rail/05, rail/08), and the waybill issued at 13:10 already cites this declaration's ID (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:CustomsDeclaration/cbc:ID` = `VI-TD-26-0331`).
