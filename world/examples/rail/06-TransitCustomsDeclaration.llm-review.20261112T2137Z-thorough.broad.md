# LLM review: 06-TransitCustomsDeclaration.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/06-TransitCustomsDeclaration.xml`, Git blob `3619a51519aa158336a9817cd911b99963ad4351` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2dc7bd3 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### rail/06#F1 · High · Shipment gross weight leaves out the containers it is defined to include
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `7968`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `7968`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- Why: Shipment/GrossWeightMeasure is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment", whereas GoodsItem/GrossWeightMeasure excludes "the carrier's equipment". Both are 7968 kg. The two containers weigh 7884 kg each gross, 15 768 kg together; with 3984 kg of goods each (7968 / 2) that leaves a tare of 3900 kg per 40-foot high cube container, a normal tare (my knowledge: about 3.8 to 4.0 t). The shipment's gross weight should therefore be 15 768 kg, not the goods' 7968 kg. The waybill has the same value (`08-Waybill.xml:/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `7968`).
- Condition: Shipment/GrossWeightMeasure = goods with packaging plus transport equipment (= sum of the equipment gross weights, 15 768 kg), or it is absent and the goods' weight is given where the definition excludes equipment.
- Options: (a) preferred: 15 768 kg at shipment level, 7968 kg remaining on the goods item (and the consignment in 02/03); (b) drop the shipment-level weight.
- Needs decision: no

### rail/06#F2 · High · Emission value does not equal factor × base
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)", applied to ValueBaseMeasure; 0.82 × 1 bench = 0.82 kg, not 96 kg. The same triple occurs in 39 examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82' world/examples`).
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure, or factor and base are absent.
- Options: (a) preferred: drop factor and base (a product footprint per bench); (b) a factor and base that give 96 kg.
- Needs decision: no

### rail/06#F3 · Medium · The rail carrier given as freight forwarder (consolidator)
- XPath: `/TransitCustomsDeclaration/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`
- Why: FreightForwarderParty is "The Party who combines individual smaller consignments into a single larger shipment (a so-called consolidated consignment or shipment) ...". Ferrano Rail Cargo carries one full consignment of the consignor in its own containers on its own train; it is the carrier (as CarrierParty of the consignment in the same document says), and nothing is consolidated (`08-Waybill.xml:/Waybill/cbc:ConsolidatedIndicator` = `false`).
- Condition: FreightForwarderParty is absent, or names a party that consolidates this consignment.
- Options: (a) preferred: drop it; the carrier is already given; (b) if a forwarder lodges the declaration for Valdara, name that party (and its role as representative) instead.
- Needs decision: no

### rail/06#F4 · Medium · An "exit office for import" where the goods enter
- XPath: `/TransitCustomsDeclaration/cac:ImportCustomsExitOfficeLocation/cbc:Name` = `Customs office Marrowdale`
- Why: ImportCustomsExitOfficeLocation is "Customs office of exit of the goods being declared for import". Goods declared for import in Bayvarra do not exit there; Marrowdale is the office of destination and of import, as the consignment says (OfficeOfDestinationLocation, OfficeOfImportLocation). The element has no real case in this transit and repeats another office under a meaning that does not fit.
- Condition: ImportCustomsExitOfficeLocation is absent, or names an office where goods declared for import actually leave a customs territory.
- Options: (a) preferred: drop it; the destination and import offices are already given; (b) record the element's definition as a question for the TC if it was meant otherwise.
- Needs decision: no

### rail/06#F5 · Medium · A system boundary code in FullnessIndicationCode
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: The definition is "A code signifying whether a piece of transport equipment is full, partially full, or empty ... used as a parameter when calculating the environmental emission". Cradle to gate (world EmissionBoundaryCode, EN 15804 A1–A3) is a life-cycle boundary, not a load state. 39 examples (`grep -rl --include='*.xml' 'EmissionBoundaryCode">CRADLETOGATE'`).
- Condition: The element is absent or holds a load-state code of transport equipment used in the calculation.
- Options: (a) preferred: drop it; (b) note the missing boundary element for the TC write-up.
- Needs decision: no

### rail/06#F6 · Medium · LifecycleStageCode covers less than the stage it describes
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: MANUFACTURING is "Making the product (EN 15804 module A3)" in the world list; the description covers mining, steel making and the transport between them as well (SOURCING, A1–A2). Code and text disagree.
- Condition: The stage code(s) cover what the description and value cover.
- Options: (a) split into SOURCING and MANUFACTURING; (b) preferred: omit the code, keep the text.
- Needs decision: no

### rail/06#F7 · Medium · Province given in Region
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries"; a province is an administrative division (CountrySubentity), as for Lumeway's "Upland State" in the same document. 219 occurrences over the examples.
- Condition: The province is in CountrySubentity, or the world defines it as non-administrative.
- Options: (a) preferred: CountrySubentity; (b) keep Region if provinces are not administrative.
- Needs decision: yes (a fact of the world)

### rail/06#F8 · Medium · Language code in LocaleCode
- XPath: `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` is a language, not a locale.
- Condition: LocaleCode absent or a locale such as `en-XB`.
- Options: (a) preferred: `en-XB`; (b) drop it.
- Needs decision: no

### rail/06#F9 · Medium · A gate in AdditionalStreetName
- XPath: `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: "An additional street name used to further clarify the address": a gate is not a street.
- Condition: AdditionalStreetName holds a street name or is absent.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no

### rail/06#F10 · Low · Previous export declaration that no example contains
- XPath: `/TransitCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `VI-CD-26-0330E`
- XPath: `/TransitCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:FunctionCode` = `EXPORT`
- Why: The transit declaration rests on an export declaration VI-CD-26-0330E, which exists in no example (`grep -rl --include='*.xml' 'VI-CD-26-0330E' world/examples` finds only this file); its number repeats 0330, the number of the hub's status report (`05-TransportProgressStatus.xml:/TransportProgressStatus/cbc:ID` = `FIH-DOC-26-0330`), with a suffix E, unlike every other number of the flow. FunctionCode ("describing the function of this customs declaration") takes a value from the declaration type list (CustomsDeclarationTypeCode), the same list as the document's own TypeCode.
- Condition: The export declaration the transit rests on can be identified in the flow (as an example, or explicitly as a document outside the examples), with a number that fits the flow's numbering; FunctionCode is from a list of functions, or absent.
- Options: (a) add an export declaration to the flow; (b) preferred if the flow stays as it is: keep the reference, give it a number in the flow's sequence and a DocumentTypeCode-like statement of what it is; (c) drop the reference if the export and transit are one declaration in the world.
- Needs decision: yes (whether the flow gains a document)

### rail/06#F11 · Low · Additional reference to the plan instead of the transport document
- XPath: `/TransitCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `FRC-TEP-26-0328`
- Why: A transit declaration refers to the transport document under which the goods travel; in this flow that is the consignment note FRC-WB-26-0334 (08), which refers back to this declaration. The declaration instead refers, by bare ID and without a type, to the transport execution plan, a booking document between Valdara and the carrier that customs does nothing with.
- Condition: The declaration refers to the transport document of the goods, and the reference says what kind of document it is.
- Options: (a) preferred: reference FRC-WB-26-0334 with a document type; (b) keep the plan only if it adds something customs uses, with a type.
- Needs decision: no

### rail/06#F12 · Low · Customs administration described as a company
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: The Customs Administration of Urvania is a public authority: it is not entered in the commercial register and has no liquidation status. Its "Border office" contact, available on weekdays 08:00–17:00, is meant for a rail border post that the train passes in the afternoon and that a declaration reaches at 17:29.
- Condition: The authority's legal entity carries no commercial-register or liquidation data (a public-body register or none); the border office's availability fits border operations.
- Options: (a) preferred: drop CorporateRegistrationScheme and CompanyLiquidationStatusCode (or use a register of public bodies if the world has one); hours "round the clock" for the border office.
- Needs decision: no

### rail/06#F13 · Low · Physics: 96 assembled benches per container do not fit as stated
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `192`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[2]/cbc:Measure` = `620`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[3]/cbc:Measure` = `780`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:SizeTypeCode` = `45G1`
- Why: 192 benches in two 45G1 containers are 96 per container. A bench measures 1.80 × 0.62 × 0.78 m = 0.870 m³ as a box; 96 boxes need 83.6 m³, more than the 76.3 m³ of a 40-foot high cube (internal 12.03 × 2.35 × 2.70 m, my knowledge; the waybill gives 76.3 m³). Laid out in the container, whole boxes fit about 54 to 57 per container (e.g. 6 along × 3 across × 3 high). The waste data mentions "pallet straps", so the benches travel on pallets, which takes more space, not less. Only nesting or knocked-down benches would fit 96, and nothing says they are.
- Condition: The number of benches per container fits the container with the packing the documents describe, or the packing (nested, knocked down) is stated.
- Options: (a) state the packing that makes 96 fit (e.g. benches nested in pairs, or frames and slats packed separately); (b) more containers, or fewer benches.
- Needs decision: yes (changes the story of the shipment)

### rail/06#F14 · Low · Transit declaration without the means of transport
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cbc:ID` = `VI-SH-26-0332`
- Why: A transit declaration identifies the means of transport at departure and at the border, so that the offices of transit and destination can match the goods with the train. This one names the carrier, the containers and the seals, but no shipment stage, train or journey (the train FRC 4417 / journey CT 4471 is given in 03 and 08).
- Condition: The declaration identifies the means of transport the goods travel on (e.g. a main carriage stage with mode 2 and the train), or the world's transit procedure states that the container numbers suffice.
- Options: (a) preferred: a MainCarriageShipmentStage with TransportModeCode 2 and the train ID; (b) leave it if the world's rules need only containers and seals.
- Needs decision: no

### rail/06#F15 · Low · Data the declaration does nothing with
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: The goods item carries the complete catalogue item (warranty, keywords, colour property, load capacity test, dimensions, emissions, circularity profile with repairability score) and the exporter its warehousing provider. Customs uses description, classification, origin, quantity, weight and value; the rest is copied master data the declaration does nothing with.
- Condition: The goods item carries what the transit procedure uses (plus what the world's customs rules require); party data the declaration does not use is absent.
- Options: (a) preferred: reduce the item to the customs-relevant data; drop ServiceProviderParty; (b) keep only what a stated customs rule of the world needs.
- Needs decision: no

### rail/06#F16 · Low · Contacts do not fit the customs roles
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- Why: The declarant's contact for customs is the one who answers for the declaration (customs or export department), not the sales order desk; the consignee's contact receives goods, not sales enquiries.
- Condition: The declarant's contact is a customs/export function; the consignee's a receiving function (or absent).
- Options: (a) preferred: role-specific contacts; (b) drop Contact where it does not fit.
- Needs decision: no

## Checked and consistent
- References: `FRC-TEP-26-0328` resolves to 03; the consignment VI-CS-26-0327, the shipment VI-SH-26-0332, the containers FRXU1044175 and FRXU1044180 (45G1, FCL, 7884 kg), seals XU-VI-30411 and XU-VI-30412 (shipper, intact) agree with the waybill (08); the waybill refers to this declaration (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:CustomsDeclaration/cbc:ID` = `VI-TD-26-0331`).
- Goods: 192 benches, value 9 580 800 XUF (= order 01 and invoice 11), HS 940179 under section XX, national tariff 94017910, origin XU, all agree with 01 and 11.
- Offices: departure at the Ferrano hub, exit and transit at the two sides of the rail border station, destination and import at Marrowdale form a coherent route.
- Check digits: ISO 6346 FRXU1044175 and FRXU1044180, GLN 9520610900008, ISIN XU0001042501 pass (check_ids.py).
- Weights: 2 × 3984 kg goods = 7968 kg; equipment 7884 kg each implies a tare of 3900 kg, plausible for a 45G1 (see F1 for the shipment level).
- Parties described as in the other rail examples.

## Considered and refuted
- `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `9580800`: suspected a customs value that includes carriage beyond the border (the DAP price) — refuted because a transit declaration commonly states the invoice value of the goods, and the world gives no valuation rule that differs.
- `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:ID` = `FRXU1044175`: suspected an inconsistency between schemeID `ISO6346` and listID `ISO 6346` — refuted because the repository keeps the current style of schemeIDs by decision (CLAUDE.md), and both name the same standard.
- `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:TransportEquipmentSeal/cbc:SealIssuerTypeCode` = `SHIPPER`: suspected that transit requires customs seals — refuted because the world's customs may accept shipper's seals, and the note "Seals ... to remain intact" makes them the seals of the procedure.
- `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `7968`: suspected too light for the materials consumed per bench (56.5 kg) — refuted because consumption includes casting and sawing losses; 41.5 kg per bench with packaging is plausible.

## Outside this review
- Timeline: the declaration is issued on 14 April at 17:29, but the train left the office of departure (the Ferrano hub) at 06:52 that morning (05, 08), and the waybill issued at 13:10 already refers to this declaration. Whether goods can leave under a transit declaration lodged eleven hours later is a question of the flow's timeline.
