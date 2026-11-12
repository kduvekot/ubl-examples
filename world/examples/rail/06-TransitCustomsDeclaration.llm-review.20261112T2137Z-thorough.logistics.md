# LLM review: 06-TransitCustomsDeclaration.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: logistics

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

### rail/06#F1 · High · Shipment gross weight leaves out the containers
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `7968`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `7968`
- Why: Shipment GrossWeightMeasure is "the total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". The goods with packaging weigh 7968 kg (goods item, and the consignment in rail/02 and rail/03). The two containers weigh 7884 kg each when loaded, together 15 768 kg; that is goods 3984 kg + tare 3900 kg per box (7968 / 2 = 3984; 7884 − 3984 = 3900 kg, a normal tare for a 40-foot high cube). The shipment total must therefore be 15 768 kg, not the goods weight. The waybill carries the same value for the same shipment VI-SH-26-0332 (`08-Waybill.xml:/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `7968`).
- Condition: Shipment GrossWeightMeasure equals the goods with packaging plus the transport equipment (here the sum of the containers' gross weights, 15 768 kg), or it is absent and the goods weight stays on the goods item.
- Options: (a) preferred: 15 768 kg, so that it agrees with the equipment weights; (b) remove the shipment gross weight and keep 7968 kg on the goods item (and on the consignment where it is given).
- Needs decision: no

### rail/06#F2 · High · Emission factor × base quantity does not give the stated emission
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: As in the order (rail/01#F1): with a factor "used to calculate the value measurement" of 0.82 and a base of 1 EA, the value would be 0.82 kg CO2e per bench, not 96 kg. The same triple is in 39 examples (`grep -rc --include='*.xml'`, see rail/01).
- Condition: ValueFactorNumeric × ValueBaseMeasure equals ValueMeasure, or the factor and base are absent.
- Options: as in rail/01 (preferred: remove factor and base).
- Needs decision: no

### rail/06#F3 · Medium · A transit declaration without the means of transport
- XPath: `/TransitCustomsDeclaration/cac:Shipment`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`
- Why: A transit declaration places goods under a transit procedure for a movement from the office of departure to the office of destination; customs at departure, at the border office of transit and at destination need the mode and means of transport at departure and at the border (own knowledge of transit procedures, e.g. the NCTS data set: identity and nationality of the means of transport, mode at the border). The declaration names the containers, seals and carrier but no shipment stage, mode of transport or means (the train FRC 4417 and wagon 31 46 4521 042-3 in rail/08). Without them the border post cannot match the declaration to the train it checks.
- Condition: The declaration states the mode of transport (rail, 2) and identifies the means of transport at departure and crossing the border.
- Options: (a) preferred: a `cac:MainCarriageShipmentStage` under the consignment with TransportModeCode 2 and `cac:TransportMeans` (TrainID, registration nationality XU), and the wagon via the containers' ApplicableTransportMeans; (b) at least the mode at the border on the shipment stage.
- Needs decision: no

### rail/06#F4 · Medium · Previous transit declaration used for an export declaration
- XPath: `/TransitCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `VI-CD-26-0330E`
- XPath: `/TransitCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:FunctionCode` = `EXPORT`
- Why: PreviousCustomsDeclaration in a Transit Customs Declaration is "a reference to a previously sent transit customs declaration" — an earlier version or a preceding transit declaration. The value refers to an export declaration (FunctionCode EXPORT), which is the preceding export procedure, not a previously sent transit declaration. The export declaration is not an example of the flow either (no example has ID VI-CD-26-0330E).
- Condition: PreviousCustomsDeclaration refers only to a previous transit declaration; the export declaration is referenced through an element meant for a related document.
- Options: (a) preferred: reference the export declaration in `cac:AdditionalDocumentReference` with a document type that says it is the export declaration; (b) keep the element only if the owner reads "previously sent … declaration" as any preceding declaration, and record it as a UBL definition question.
- Needs decision: no

### rail/06#F5 · Low · Customs offices only by name, and two office roles whose definitions do not fit
- XPath: `/TransitCustomsDeclaration/cac:ImportCustomsExitOfficeLocation/cbc:Name` = `Customs office Marrowdale`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfEntryLocation/cbc:Name` = `Customs post at the rail border station, Bayvarran side`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfDepartureLocation/cbc:Name` = `Customs office Ferrano Intermodal Hub`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfDestinationLocation/cbc:Name` = `Customs office Marrowdale`
- Why: (1) ImportCustomsExitOfficeLocation is "customs office of exit of the goods being declared for import"; Marrowdale is where the goods end transit and are imported, not where they leave a customs territory. (2) OfficeOfEntryLocation is defined as "the customs office or offices indicated in the authorisation as empowered to accept declarations entering goods for the arrangements" — an office named in an authorisation for a special procedure, not the border post at which the goods enter Bayvarra, which is already the office of transit. (3) All six offices are given only as text; transit offices are identified by office reference numbers (own knowledge: customs office lists such as the EU COL), and none of the offices carries an ID.
- Condition: Each office element holds an office that has the role its definition names, and each office carries an identifier of the customs office (in a national or Trade Accord office list), or the world states that offices are identified by name.
- Options: (a) preferred: remove ImportCustomsExitOfficeLocation and OfficeOfEntryLocation (the destination, import and transit offices already cover Marrowdale and the Bayvarran border post), and add `cbc:ID` with an office-list schemeID to the remaining offices; (b) keep OfficeOfEntryLocation only if the story has an authorisation (e.g. an authorised consignee) naming that office.
- Needs decision: yes

### rail/06#F6 · Low · Reference to the transport plan with only an ID
- XPath: `/TransitCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `FRC-TEP-26-0328`
- Why: The reference resolves to the transport execution plan rail/03, but AdditionalDocumentReference carries no DocumentTypeCode or DocumentType, so for customs it is an unexplained number. The checklist asks a reference with only an ID to say what it refers to where that is not obvious.
- Condition: The reference says what document it is (type code or text).
- Options: add `cbc:DocumentTypeCode`/`cbc:DocumentType` (preferred), or reference the consignment note (rail/08) that accompanies the goods, which customs is more likely to need.
- Needs decision: no

## Checked and consistent
- Containers FRXU1044175 and FRXU1044180: ISO 6346 check digits pass (check_ids.py); size type 45G1 (40 ft high cube general purpose) agrees with "40-foot containers" and the waybill's 12 192 mm length and "high cube"; seals XU-VI-30411 and XU-VI-30412 agree with rail/08 and with the note.
- Physics: 192 benches × 41.5 kg = 7968 kg goods gross; per container 3984 kg goods + 3900 kg tare = 7884 kg, well below the payload of a 40-foot box (about 26 t, own knowledge).
- Consignment VI-CS-26-0327, shipment VI-SH-26-0332, consignor, consignee and carrier agree with rail/08; quantity 192 EA and customs value 9 580 800 XUF agree with the order and the goods invoice (192 × 49 900).
- Commodity code 940179 (HS 2022) with the national 94017910 (benches with metal frames) fits the item; origin XU, consignee in XB: an external transit fits.
- Offices that do fit their definitions: departure at the Ferrano hub (where the train is loaded), exit and export exit on the Urvanian side of the border station, transit on the Bayvarran side, destination and import at Marrowdale.

## Considered and refuted
- `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:TransportEquipmentSeal/cbc:SealIssuerTypeCode` = `SHIPPER`: transit usually requires customs seals — refuted: shipper's seals are accepted for authorised consignors, and the note requires them to remain intact; nothing in the flow contradicts it.
- `/TransitCustomsDeclaration/cac:TransitCustomsExitOfficeLocation/cbc:Name` = `Customs post at the rail border station, Bayvarran side`: an "exit" office on the side of entry — refuted: for goods under transit, the Bayvarran border post is where the goods leave the transit leg through Urvania's customs territory into Bayvarra's control; the definition ("customs office of exit of the goods being declared for transit") admits that reading.
- `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure` = `34`: 34 kg steel + 22.5 kg hardwood = 56.5 kg consumed against a gross weight of 41.5 kg per bench — refuted: consumption includes casting and sawing losses; about 27 % loss is plausible.

## Outside this review
- Timeline across the flow: the transit declaration is issued on 2026-04-14 at 17:29, but the train left the office of departure at 06:52 that morning (rail/05, rail/08), and the waybill issued at 13:10 already lists this declaration. Transit has to be declared before departure. Which document's time is wrong is for the cross-document review.
