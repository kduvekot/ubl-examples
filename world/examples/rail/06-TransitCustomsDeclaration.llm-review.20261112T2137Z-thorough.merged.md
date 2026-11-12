# LLM review: 06-TransitCustomsDeclaration.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/06-TransitCustomsDeclaration.xml`, Git blob `3619a51519aa158336a9817cd911b99963ad4351` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit abfa39e 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
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

### rail/06#F1 · High · Shipment gross weight leaves out the containers its definition includes
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `7968`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `7968`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[2]/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7884`
- Why: Shipment/GrossWeightMeasure is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment", whereas GoodsItem/GrossWeightMeasure is "The weight of this goods item, including packing and packaging but excluding the carrier's equipment". Both are 7968 kg. Recalculated in the merge: the two loaded containers weigh 2 × 7884 = 15 768 kg; with the goods split evenly (7968 / 2 = 3984 kg per box) each container's tare is 7884 − 3984 = 3900 kg, a normal tare for a 40-foot high cube (own knowledge: about 3.7–3.9 t). Goods plus packaging plus equipment is therefore 15 768 kg, not 7968 kg. Refutation tried: a "gross mass" without equipment is the customs (WCO) convention, but UBL's definition of this element explicitly includes the equipment, and the equipment weights in the same document make the contradiction arithmetic. The waybill has the same value for the same shipment (`08-Waybill.xml:/Waybill/cac:Shipment/cbc:GrossWeightMeasure` = `7968`).
- Condition: Shipment/GrossWeightMeasure = goods with packaging plus transport equipment (here the sum of the containers' gross weights, 15 768 kg), or it is absent and the goods' 7968 kg stays on the goods item.
- Options: (a) preferred: 15 768 kg at shipment level, 7968 kg on the goods item; (b) drop the shipment-level weight.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### rail/06#F2 · High · Emission value is not factor × base
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)", ValueBaseMeasure "the base quantity to which the value factor applies". 0.82 × 1 EA = 0.82 kg CO2e, not 96 kg. Refutation tried in the merge: 96 / 0.82 = 117.1, which is neither the bench's gross weight (7968 / 192 = 41.5 kg) nor its material consumption (34 + 22.5 = 56.5 kg), so no reading of the base makes the triple consistent. The same triple is in 39 examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure, or factor and base are absent.
- Options: (a) preferred: drop factor and base (a product footprint per bench needs neither); (b) a factor and base that give 96 kg.
- Needs decision: no
- From: broad (F2), logistics (F2), context (F2)

### rail/06#F3 · Medium · The rail carrier as freight forwarder (consolidator)
- XPath: `/TransitCustomsDeclaration/cac:FreightForwarderParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`
- Why: FreightForwarderParty is "The Party who combines individual smaller consignments into a single larger shipment (a so-called consolidated consignment or shipment) which is sent to a counterpart who mirrors the consolidator's activity by dividing the consolidated consignment into its original components." Ferrano Rail Cargo carries one full-container consignment of one consignor to one consignee; it is the carrier, as CarrierParty in the same document says, and nothing is consolidated (`08-Waybill.xml:/Waybill/cbc:ConsolidatedIndicator` = `false`).
- Condition: FreightForwarderParty is absent, or names a party that consolidates this consignment with others into one shipment that a counterpart splits again.
- Options: (a) preferred: drop it; the carrier is already given; (b) if a forwarder lodges the declaration for Valdara or consolidates, name that party (and change the waybill accordingly).
- Needs decision: no (parties said yes; removing a duplicate of the carrier changes no story, only option (b) would)
- From: broad (F3), parties (F4), context (F4)

### rail/06#F4 · Medium · Customs administration described as a company in the commercial register
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyID` = `XU-R-105507`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: The Customs Administration of Urvania (`/TransitCustomsDeclaration/cac:CustomsParty/cbc:IndustryClassificationCode` = `8411`, general public administration) is a public authority. It is described as registered in the commercial register, with a company number and a liquidation status ("A code signifying the party's liquidation status"), which apply to companies (section 5: a public body is not a company in a commercial register and has no liquidation status). The values contradict the party's own classification. Parties counted the pattern (ISIC 8411 with a commercial-register scheme) 90 times in 75 example files.
- Condition: The authority's legal entity, if present, describes a public authority (established by law, a register of public bodies or none) and has no liquidation status.
- Options: (a) preferred: drop PartyLegalEntity for the authority, keeping name and identifier; (b) a register of public bodies with its own registration type, and no liquidation status.
- Needs decision: no
- From: parties (F5), broad (F12, legal-entity part)

### rail/06#F5 · Medium · Previous customs declaration holds an export declaration that no example contains
- XPath: `/TransitCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `VI-CD-26-0330E`
- XPath: `/TransitCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:FunctionCode` = `EXPORT`
- Why: In a Transit Customs Declaration, PreviousCustomsDeclaration is "A reference to a previously sent transit customs declaration" (checked in the gc): an earlier transit declaration or version. The value is an export declaration (FunctionCode EXPORT), i.e. the preceding export procedure, not a previously sent transit declaration. FunctionCode ("A code describing the function of this customs declaration") takes its value from the declaration type list (CustomsDeclarationTypeCode), the same list as the document's own TypeCode. The export declaration exists in no example (`grep -rl --include='*.xml' 'VI-CD-26-0330E' world/examples` finds only this file), and its number reuses 0330, the number of the hub's status report (`05-TransportProgressStatus.xml:/TransportProgressStatus/cbc:ID` = `FIH-DOC-26-0330`), with a suffix E unlike every other number of the flow.
- Condition: PreviousCustomsDeclaration refers only to a previous transit declaration; the export declaration, if the transit rests on one, is referenced through an element meant for a related document, says what it is, and can be identified (as an example, or explicitly as a document outside the examples) with a number in the flow's numbering.
- Options: (a) preferred: reference the export declaration in AdditionalDocumentReference with a document type saying it is the export declaration, under a number in the flow's sequence; (b) add an export declaration to the flow; (c) drop the reference if export and transit are one declaration in the world.
- Needs decision: yes (whether the flow gains a document)
- From: logistics (F4), broad (F10)

### rail/06#F6 · Medium · An "exit office for import" at the inland office where the goods are imported
- XPath: `/TransitCustomsDeclaration/cac:ImportCustomsExitOfficeLocation/cbc:Name` = `Customs office Marrowdale`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfDestinationLocation/cbc:Name` = `Customs office Marrowdale`
- Why: ImportCustomsExitOfficeLocation is "Customs office of exit of the goods being declared for import". Marrowdale is the inland office where the transit ends and the goods are imported, as the consignment says (office of destination and of import); nothing exits a customs territory there. The element repeats another office under a meaning that does not fit.
- Condition: ImportCustomsExitOfficeLocation is absent, or names an office where goods declared for import leave a customs territory.
- Options: (a) preferred: drop it; destination and import offices already name Marrowdale; (b) record the element's definition as a question for the TC if it was meant otherwise.
- Needs decision: no (context said yes; dropping a repeated office changes no story)
- From: broad (F4), context (F3, first place), logistics (F5, point 1)

### rail/06#F7 · Medium · A system boundary code in FullnessIndicationCode
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: FullnessIndicationCode is "A code signifying whether a piece of transport equipment is full, partially full, or empty ... used as a parameter when calculating the environmental emission". Cradle to gate (world list EmissionBoundaryCode, EN 15804 A1–A3) is a life-cycle boundary, not a load state. 39 examples carry it (`grep -rl --include='*.xml' 'EmissionBoundaryCode">CRADLETOGATE' world/examples | wc -l`).
- Condition: The element is absent or holds a load state of transport equipment used in the calculation.
- Options: (a) preferred: drop it and record the missing boundary element for the TC write-up; (b) keep it only as a recorded gap.
- Needs decision: no (context said yes; the fix is encoding, aligned with rail 01 and earlier flows)
- From: broad (F5), context (F5)

### rail/06#F8 · Medium · LifecycleStageCode covers less than the stage it describes
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: MANUFACTURING is "Making the product (EN 15804 module A3)" in the world list; the description (and the emission Description "Mining, steel making, casting, galvanising, sawing and the transport between them.") covers raw material supply and its transport as well (SOURCING, A1–A2). Code and text disagree.
- Condition: The stage code(s) cover what the description and the value cover.
- Options: (a) preferred: omit the code and keep the text (broad), or (b) two entries SOURCING and MANUFACTURING (context's preference); (c) narrow the description.
- Needs decision: no
- From: broad (F6), context (F6)

### rail/06#F9 · Medium · Province given in Region
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division, which UBL puts in CountrySubentity ("…such as the name of its county, province, or state"), as the consignee's address in the same document does (`/TransitCustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 example files (`grep -ro --include='*.xml' '<cbc:Region>Province of'`).
- Condition: No Urvanian address in this example carries the province in Region; where given, it is in CountrySubentity.
- Options: (a) preferred: CountrySubentity; (b) drop it.
- Needs decision: no (broad and context said yes; the name itself says "Province", so moving it is encoding; aligned with rail 01–05, wood, plastics)
- From: broad (F7), parties (F1), context (F8)

### rail/06#F10 · Medium · Language code in LocaleCode
- XPath: `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) is a language and repeats `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:ID` = `en`. 364 occurrences in 213 example files (`grep -ro --include='*.xml' 'LocaleCode listID="ISO 639">en<'`; the parts counted 362).
- Condition: LocaleCode is absent or names a locale from a list of locales.
- Options: (a) preferred: drop it (parties); (b) a locale such as `en-XB` with a locale list (broad, context).
- Needs decision: no
- From: broad (F8), parties (F2), context (F7)

### rail/06#F11 · Medium · A gate in AdditionalStreetName of the consignee's postal address
- XPath: `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address"; a gate is an entrance of the site, not a street, and has no meaning for the consignee's address in a customs declaration.
- Condition: Lumeway's postal address has no gate in AdditionalStreetName.
- Options: (a) preferred: drop it from the postal address; (b) where a transport document needs a gate, state it at a delivery location.
- Needs decision: no
- From: broad (F9), parties (F3)

### rail/06#F12 · Low · Transit exit office and office of entry fit their definitions only under a loose reading
- XPath: `/TransitCustomsDeclaration/cac:TransitCustomsExitOfficeLocation/cbc:Name` = `Customs post at the rail border station, Bayvarran side`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfEntryLocation/cbc:Name` = `Customs post at the rail border station, Bayvarran side`
- Why: TransitCustomsExitOfficeLocation is "Customs office of exit of the goods being declared for transit". Context: the transit does not end or exit at the Bayvarran border post, it ends at the office of destination in Marrowdale; the Bayvarran post is the office of transit. Logistics refuted this: for goods under transit, the Bayvarran post is where the goods leave the transit leg through Urvania's territory into Bayvarra's control, which the definition admits. OfficeOfEntryLocation is "The customs office or offices indicated in the authorisation as empowered to accept declarations entering goods for the arrangements" (checked in the gc): an office named in an authorisation for a special procedure, not the border post where the goods enter Bayvarra; the story has no such authorisation (logistics). The merge cannot settle either reading with certainty (the element names suggest the border-post readings, the definitions do not), so both stay as Low with both arguments.
- Condition: Each office element holds an office that has the role its definition names in this transit, or it is absent; or the owner records how these definitions are read.
- Options: (a) preferred: drop both (export exit, departure, transit, destination and import offices already cover the route); (b) keep OfficeOfEntryLocation only if the story has an authorisation (e.g. an authorised consignee) naming that office; (c) keep TransitCustomsExitOfficeLocation with the Urvanian border post if the world treats the transit as two national legs.
- Needs decision: yes (cannot be settled from the definitions alone)
- From: context (F3, second place), logistics (F5, point 2; it refuted the transit exit office)

### rail/06#F13 · Low · Customs offices identified by description only
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfDepartureLocation/cbc:Name` = `Customs office Ferrano Intermodal Hub`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfDestinationLocation/cbc:Name` = `Customs office Marrowdale`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfTransitLocation/cbc:Name` = `Customs post at the rail border station, Bayvarran side`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfExitLocation/cbc:Name` = `Customs post at the rail border station, Urvanian side`
- Why: Locations carry identifiers where they are places of a register (section 5). Transit offices are identified by customs office reference numbers (own knowledge: e.g. the EU customs office list used in NCTS); all offices here are given only as text, partly phrased as descriptions ("Customs post at the rail border station, …") rather than office names, with nothing that ties them to an office register of the world.
- Condition: Each customs office location carries an identifier from the world's (national or Trade Accord) office list and the same name wherever it recurs, or the world states that offices are identified by name.
- Options: (a) preferred: office identifiers from a world or Trade Accord list, if the world defines one; (b) at least office names used identically.
- Needs decision: no
- From: parties (F12), logistics (F5, point 3)

### rail/06#F14 · Low · Transit declaration without the means of transport
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cbc:ID` = `VI-SH-26-0332`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Ferrano Rail Cargo`
- Why: A transit declaration usually identifies the mode and means of transport at departure and at the border, so that the offices of transit and destination can match the goods with the train (own knowledge of transit data sets such as NCTS). This one names the carrier, the containers and the seals but no shipment stage, mode or train (train FRC 4417, wagon 31 46 4521 042-3 in 08). Whether the world's transit procedure needs them, or containers and seals suffice, cannot be read from the XML, so the merge keeps broad's Low rather than logistics' Medium (aligned with plastics 05, "no transport mode / means at the border": Low).
- Condition: The declaration identifies the mode (rail, 2) and the means of transport, or the world's transit procedure states that containers and seals suffice.
- Options: (a) preferred: a MainCarriageShipmentStage under the consignment with TransportModeCode 2 and TransportMeans (TrainID, registration nationality XU); (b) leave it if the world's rules need only containers and seals.
- Needs decision: no
- From: broad (F14), logistics (F3)

### rail/06#F15 · Low · 96 assembled benches per container do not fit by volume
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `192`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[1]/cbc:Measure` = `1800`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[2]/cbc:Measure` = `620`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:Dimension[3]/cbc:Measure` = `780`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:SizeTypeCode` = `45G1`
- Why: Physics redone in the merge. 192 benches in two 45G1 containers are 96 per container. Bounding box per bench 1.80 × 0.62 × 0.78 m = 0.870 m³; 96 × 0.870 = 83.6 m³, more than the internal volume of a 40-foot high cube (about 12.03 × 2.35 × 2.70 m = 76.3 m³, own knowledge; the waybill states 76.3 m³). Whole boxes: 6 along × 3 across × 3 high = 54 upright; the best orientation (bench on its back, 0.62 m high: 6 × 3 × 4) gives 72; none reaches 96. Weight is no limit: 96 × 41.5 = 3984 kg per box against a payload of about 26.5 t (30 480 kg maximum gross minus 3900 kg tare, own knowledge). So 96 per box is possible only if the benches travel knocked down or nested, which no document says (the item's packaging waste "Stretch film and pallet straps, per bench" points to wrapped benches). Low, not higher, because the contradiction rests on an unstated assumption (assembled benches), and cast-frame benches are commonly shipped knocked down.
- Condition: The number of benches per container fits the container with the packing the documents describe, or the packing (knocked down, nested) is stated.
- Options: (a) preferred: state that the benches are shipped knocked down (frames and slats packed separately, about 0.25 m³ each), e.g. in the goods description or as packages; (b) more containers (about four) or fewer benches, which changes the order and the invoices.
- Needs decision: yes (changes the story of the shipment)
- From: broad (F13)

### rail/06#F16 · Low · Additional reference to the transport plan, with only an ID
- XPath: `/TransitCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `FRC-TEP-26-0328`
- Why: The reference resolves to the transport execution plan (03), but carries no DocumentTypeCode or DocumentType, so for customs it is an unexplained number. A transit declaration refers to the transport document under which the goods travel; in this flow that is the consignment note FRC-WB-26-0334 (08), which refers back to this declaration, while the plan is a booking between Valdara and the carrier that customs does nothing with.
- Condition: The declaration refers to the transport document of the goods (or to a document customs uses), and the reference says what kind of document it is.
- Options: (a) preferred: reference FRC-WB-26-0334 with a document type; (b) keep the plan, with a type, only if it adds something customs uses.
- Needs decision: no
- From: broad (F11), logistics (F6)

### rail/06#F17 · Low · Declared customs value includes carriage inside Bayvarra
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `9580800`
- XPath: `11-Invoice.xml:/Invoice/cbc:Note[2]` = `Delivered at place: the price includes the carriage to the siding.`
- XPath: `10-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `109200`
- Why: DeclaredCustomsValueAmount is "the total declared value for customs purposes of the goods item". The value is the DAP sale price (192 × 49 900), which by the sales invoice includes the carriage to Lumeway's siding in Marrowdale, beyond the border. Under the usual valuation rules (own knowledge: WTO Valuation Agreement, value at the border) carriage after the border is deducted when known separately; here the whole rail freight is known (109 200 XUF, 10). Broad refuted this: a transit declaration commonly states the invoice value (for the guarantee), and the world gives no valuation rule that differs. Neither argument can be settled from the XML; the difference is at most 1.1 % of the value.
- Condition: The declared customs value is the value on the basis the world's customs rules require, or the example states why the DAP price is right.
- Options: (a) keep the DAP price if the world's transit rules use the invoice price; (b) deduct the share of carriage beyond the border. No preference: it depends on the world's rule.
- Needs decision: yes (customs valuation rule)
- From: money (F1); broad listed it under "Considered and refuted"

### rail/06#F18 · Low · Jurisdiction limited to Urvania for a transit ending in Bayvarra
- XPath: `/TransitCustomsDeclaration/cac:JurisdictionRegionAddress/cac:Country/cbc:IdentificationCode` = `XU`
- Why: JurisdictionRegionAddress is "A geographic area in which this declaration is relevant". The transit runs from Ferrano to the office of destination in Marrowdale, and the declaration names Bayvarran offices of transit, destination and import; it is relevant in both countries (under the Trade Accord).
- Condition: The jurisdiction covers every country whose offices act on the declaration, or the element is absent.
- Options: (a) preferred: a Trade Accord region or both countries, if the world's transit is a common procedure; (b) drop it.
- Needs decision: yes (whether the world's transit is a common procedure)
- From: context (F10)

### rail/06#F19 · Low · "English" renderings of Urvanian addresses and legal forms are Italian
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:StreetName[2]` = `Valico di Confine`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- Why: Each repeated rendering must be in the language its languageID names (section 5). These are tagged `en-XU` but are Italian (own knowledge; "Valico di Confine" means "border crossing"); the Urvanian renderings are different names. Whether English usage in the world keeps Italianate street names is a world convention the XML cannot settle; the legal forms are not proper names, which makes them the stronger case. 217 such renderings in 102 example files (`grep -roE --include='*.xml' 'languageID="en-X[UB]">(Via|Viale|Piazza|Valico|Corso|Largo|Strada|Banchina) '`, the count of rail 01–05's merge; the parts counted 63 files with `en-XU` only).
- Condition: Every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms.
- Options: (a) record the convention in the world's story (preferred if intended); (b) translate into English; (c) tag with the language the text is in.
- Needs decision: yes
- From: parties (F6); the carrier's legal form added by the merge (same problem, same document)

### rail/06#F20 · Low · Declarant's and consignee's contacts do not fit the customs roles
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: Valdara makes and signs the declaration (TransitExporterParty: "The Party who makes the Transit Customs Declaration, or on whose behalf…"); customs' questions go to its customs/export function, not the sales order desk. A consignee's contact receives goods and, under transit, presents them at the office of destination; Lumeway's sales customer service serves Lumeway's own customers.
- Condition: The declarant's contact is a customs/export/shipping function; the consignee's a goods-receiving or customs function (or absent).
- Options: (a) preferred: role-specific contacts; (b) drop Contact where it does not fit.
- Needs decision: no
- From: broad (F16), parties (F7, F8)

### rail/06#F21 · Low · Customs contact is the border office, not the office that processes the declaration
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Name` = `Border office`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:OfficeOfDepartureLocation/cbc:Name` = `Customs office Ferrano Intermodal Hub`
- Why: CustomsParty is "The Authority who is legally responsible for processing the Declaration"; a transit declaration is accepted at the office of departure ("A Customs Office where the customs declaration placing goods under transit is accepted"), here the office at the hub. The contact is the border office, which only sees the goods when they cross.
- Condition: The customs party's contact is the office that accepts and processes the declaration, or the contact says why the border office is the contact.
- Options: (a) preferred: the office of departure at the hub as contact; (b) keep the border office and say in the note what it is for.
- Needs decision: no
- From: parties (F11)

### rail/06#F22 · Low · VAT registration of the customs administration
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `VAT`
- Why: The authority processing a transit declaration acts as a public authority; a VAT registration (possible for taxable side activities) has nothing to do with the declaration (section 4.8). Kept separate from F4 and Low, as in plastics 05: a public body may have a VAT registration, so it does not contradict the party's nature; it is copied master data.
- Condition: The customs party carries no tax scheme, or one with a reason in this document.
- Options: (a) preferred: drop PartyTaxScheme for the authority; (b) keep it only if the world gives the authority taxable activities and the document uses it.
- Needs decision: no
- From: parties (F10)

### rail/06#F23 · Low · Party master data the declaration does nothing with
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/TransitCustomsDeclaration/cac:TransitExporterParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/TransitCustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: A transit declaration does nothing with the declarant's stock-exchange listing, its warehousing provider (Castrano Logistics plays no role in the declaration) or the share capital of declarant and consignee (section 4.8).
- Condition: Every legal-entity and service-provider element present has a purpose in the declaration.
- Options: (a) preferred: drop them here; (b) a reduced party description for customs documents.
- Needs decision: no
- From: parties (F9), context (F11), broad (F15, party part)

### rail/06#F24 · Low · Catalogue and product-passport data on the goods item
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- Why: Customs in transit uses description, classification, origin, quantity, weight and value. Warranty, keywords, colour, load-capacity test, repairability, maintenance, resource consumption and the product footprint are the seller's catalogue data, which the declaration does nothing with (section 4.8). Kept separate from the party master data (F23), as in the earlier flows.
- Condition: The goods item carries what the transit procedure uses (plus what a stated customs rule of the world requires).
- Options: (a) preferred: reduce the item to description, identification, classification and origin; (b) keep a property only where the story gives customs a use for it.
- Needs decision: no
- From: broad (F15, item part), context (F9)

### rail/06#F25 · Low · Carrier's registration date 1996-01-01
- XPath: `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Not raised by any part of this run; added by the merge for consistency with rail 01–05, wood, plastics and air, where it is a finding. 1 January 1996 recurs as the registration date of many unrelated companies (271 occurrences in 181 example files, `grep -ro --include='*.xml' '<cbc:RegistrationDate>1996-01-01'`), which reads as a default rather than each company's own date, unless a 1996 (re-)registration is part of the world's story.
- Condition: Each company's registration date is its own (from its history), or the world records a general 1996 registration.
- Options: (a) preferred: own date per company; (b) record a 1996 re-registration in the story.
- Needs decision: yes
- From: merge

## Checked and consistent
- References: `FRC-TEP-26-0328` resolves to 03; consignment VI-CS-26-0327, shipment VI-SH-26-0332, containers FRXU1044175 and FRXU1044180 (45G1, FCL, 7884 kg), seals XU-VI-30411 and XU-VI-30412 (shipper, intact) agree with the waybill (08), which refers to this declaration (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:CustomsDeclaration/cbc:ID` = `VI-TD-26-0331`).
- Goods: 192 benches, value 9 580 800 XUF = 192 × 49 900 (= order 01 and invoice 11), HS 940179 under section XX, national tariff 94017910, origin XU; NatureOfTransactionCode PURCHASE fits the sale of 01 and 11; currency XUF is that of the sale and of the declaring country.
- Weights (merge recalculation): 192 × 41.5 = 7968 kg goods; per container 3984 + 3900 tare = 7884 kg, far below the payload of a 40-foot box.
- Offices that fit their definitions: departure at the Ferrano hub, exit and export exit on the Urvanian side of the border station, transit on the Bayvarran side, destination and import at Marrowdale.
- TypeCode TRANSIT with SubTypeCode EXTTRANSIT fits goods leaving Urvania under transit to Bayvarra.
- Check digits (check_ids.py, from the parts): ISO 6346 FRXU1044175 and FRXU1044180, GLN 9520610900008, ISIN XU0001042501 pass.
- Parties (Valdara, Lumeway, Ferrano Rail Cargo), tax registrations (XU007299291, UL-1230822, XU007328060) and Codana Identification Agency (`XU-R-105644`) as issuer of the property identifier agree with the other rail examples.

## Considered and refuted
- `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:ID` = `FRXU1044175`: inconsistency between schemeID `ISO6346` and listID `ISO 6346` — refuted because schemeIDs keep their current style by decision (CLAUDE.md), and both name the same standard. (from broad)
- `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:TransportEquipmentSeal/cbc:SealIssuerTypeCode` = `SHIPPER`: transit requires customs seals — refuted because the world's customs may accept shipper's seals (authorised consignor), and the note "Seals ... to remain intact" makes them the seals of the procedure. (from broad, logistics)
- `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure` = `34`: 34 kg steel + 22.5 kg hardwood = 56.5 kg consumed against 41.5 kg gross per bench — refuted because consumption includes casting and sawing losses (about 27 %). (from broad, logistics)
- `/TransitCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `9580800`: value includes carriage beyond the border — broad's refutation (invoice value is common, no world rule) is carried into F17, where the money part's finding stands as Low with both arguments. (from broad)
- `/TransitCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:JobTitle` = `Public service officer`: generic job title for a customs contact — refuted: vague, but not contrary to the role. (from parties)
- `/TransitCustomsDeclaration/cac:NotifierParty/cac:PartyName/cbc:Name` = `Valdara Industries`: notifier equal to the declarant, or a party without a role — refuted: NotifierParty is "The Party who is responsible for contact on master level", which the declarant can be. (from parties, context)
- `/TransitCustomsDeclaration/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cbc:FullnessIndicationCode` = `FCL`: checked — the correct use of FullnessIndicationCode, unlike F7. (from context)

## Refuted in the merge
### broad/F12 (part) · Low · Border office reachable only on weekdays 08:00–17:00
- XPath: `/TransitCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Broad: the "Border office" contact, available on weekdays 08:00–17:00, is meant for a rail border post that the train passes in the afternoon and that a declaration reaches at 17:29; condition: the border office's availability fits border operations ("round the clock").
- Refuted because: the train passes the border on a Tuesday at about 13:00–13:20 (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualWaypointTransportEvent/cbc:OccurrenceTime` = `13:20:00`), within those hours (as parties found). That the declaration is issued at 17:29, after them, is part of the declaration's timeline problem (see "Outside this review"), not of the contact. The rest of broad/F12 (company attributes) is in F4.

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined; physics recalculated (2 × 7884 = 15 768; tare 3900), refutation (WCO gross mass) added.
- broad/F2, logistics/F2, context/F2 → F2: combined; 96 / 0.82 = 117.1 checked against bench mass and consumption.
- broad/F3, parties/F4, context/F4 → F3: combined; needs decision no (parties yes) because only option (b) changes the story.
- parties/F5 + broad/F12 → F4: combined at Medium (broad Low) because the values contradict the party's ISIC 8411; aligned with wood, plastics. Broad's hours part moved to "Refuted in the merge".
- logistics/F4 (Medium, no) + broad/F10 (Low, yes) → F5: combined at Medium (the gc definition "previously sent transit customs declaration" is not met); needs decision yes from broad (the flow may gain a document).
- broad/F4, context/F3 (first place), logistics/F5 (point 1) → F6: ImportCustomsExitOfficeLocation as its own Medium; needs decision no (context yes).
- context/F3 (second place) + logistics/F5 (point 2) → F12: TransitCustomsExitOfficeLocation (logistics refuted it) and OfficeOfEntryLocation lowered to Low, needs decision yes, because the merge could not settle the readings.
- parties/F12 + logistics/F5 (point 3) → F13: office identifiers as their own Low.
- broad/F5, context/F5 → F7; broad/F6, context/F6 → F8: combined; F7 needs decision no (context yes), aligned with rail 01.
- broad/F7, parties/F1, context/F8 → F9: needs decision no (broad, context yes), aligned with rail 01–05, wood, plastics.
- broad/F8, parties/F2, context/F7 → F10: combined; count corrected to 364.
- broad/F9, parties/F3 → F11: combined.
- broad/F14 (Low) + logistics/F3 (Medium) → F14: kept Low, because whether the world's transit needs the means cannot be read from the XML (aligned with plastics 05).
- broad/F13 → F15: physics redone (best layout 72, volume 83.6 > 76.3 m³, weight 3984 kg against about 26.5 t payload); severity and decision unchanged.
- broad/F11 + logistics/F6 → F16: combined.
- parties/F6 → F19: carrier's legal form added (same problem); count replaced by 217 renderings in 102 files.
- broad/F16 + parties/F7, F8 → F20: combined.
- parties/F9, context/F11, broad/F15 (party part) → F23; broad/F15 (item part), context/F9 → F24: broad/F15 split into party and item data, as in the earlier flows.
- F25 added by the merge (registration date 1996-01-01), for consistency with rail 01–05 and earlier flows.

## Outside this review
- Timeline: the declaration placing the goods under transit is issued on 14 April at 17:29, but the train left the office of departure (the hub) at 06:52 that morning (05, 08), and the waybill issued at 13:10 already cites its number (raised as a reference finding in the merged review of 08). Transit has to be declared before departure; which time is wrong is for the cross-document review. (from broad, logistics, context)
