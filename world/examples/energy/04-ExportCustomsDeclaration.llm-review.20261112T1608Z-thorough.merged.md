# LLM review: 04-ExportCustomsDeclaration.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/04-ExportCustomsDeclaration.xml`, Git blob `d23054c9c05d2dbe62a877d4d23f4891f2983d71` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows
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

### energy/04#F1 · High · Shipment KG-SH-26-0154 has another quantity and weight in the import declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `2940000`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:GrossWeightMeasure` = `2940000`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `2760000`
- XPath: `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`
- Why: `Shipment/cbc:ID` is "An identifier for this shipment"; the same identifier names the same shipment in both declarations, but the export gives 39200 MWh and 2 940 000 kg, the import 36800 MWh and 2 760 000 kg. The difference, 2400 MWh and 180 000 kg, is Kelpstone's sale to Ferrano Energy (07-Invoice.xml, F2). Both declarations have the same weight per energy (2 940 000 / 39200 = 2 760 000 / 36800 = 75 kg/MWh, recalculated), so the difference is a part of the shipment, not a measuring difference. One shipment cannot have two contents.
- Condition: a shipment identifier used in both declarations stands for the same quantity and weight in both, or the declarations use different shipment (or consignment) identifiers for different quantities.
- Options: (a) preferred, together with F2: split the export into the two buyers' parts (consignments or goods items), so that the import's shipment or consignment is exactly the part Montebrio Power imports; (b) give the import its own shipment identifier and relate it to the export shipment as part of it.
- Needs decision: yes (documents of the flow change)
- From: broad F1 (part), logistics F2, context F1 (part)

### energy/04#F2 · High · The whole export is consigned to Montebrio Power, but 2400 MWh of it are sold to Ferrano Energy
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1411200.00`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyIdentification/cbc:ID` = `XU-R-105918`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Montebrio Power`
- XPath: `06-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `36800`
- XPath: `07-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2400`
- XPath: `07-Invoice.xml:/Invoice/cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Ferrano Energy`
- XPath: `07-Invoice.xml:/Invoice/cac:BuyerCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Ferrano Energy`
- Why: `ConsigneeParty` is "The Party who receives the goods." The declaration has one goods item of 39200 MWh of March gas with one consignee, Montebrio Power. Kelpstone invoices that gas in two parts, both "measured at the border station" and zero-rated as exports: 36800 MWh to Montebrio Power (06) and 2400 MWh to Ferrano Energy (07); 36800 + 2400 = 39200, and the value 1 411 200 XBL × 100 = 141 120 000 XUF = 132 480 000 (06) + 8 640 000 (07). So for 2400 MWh this document names a receiver that the invoices contradict, and no import declaration in the flow names Ferrano Energy as importer. The money part noted that a consignee may differ from the buyer; that reading would need Montebrio to receive and pass on Ferrano Energy's gas, which nothing in the flow says.
- Condition: the parties who receive the exported gas, as declared, agree with the buyers in 06 and 07 and with the import declaration(s) for the shipment, or the story says why Montebrio Power receives Ferrano Energy's gas.
- Options: (a) preferred by broad, logistics and context: declare two consignments or goods items under the shipment, 36800 MWh to Montebrio Power and 2400 MWh to Ferrano Energy, each with its own weight and value, and add an import declaration by Ferrano Energy (keeps the single pipeline movement); (b) preferred by parties: limit this declaration to Montebrio's 36800 MWh and give Ferrano Energy's gas its own export and import declarations, so each declaration has one consignee; (c) keep one consignee and change 07 so that Ferrano Energy's gas is delivered through Montebrio Power.
- Needs decision: yes (who receives the gas, documents of the flow)
- From: broad F1 (part), parties F1, logistics F1, context F1 (part); money listed it as refuted (consignee may differ from buyer)

### energy/04#F3 · Medium · Language code in LocaleCode
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` is the language itself, already in `Language/ID`, and names no locale. A locale would be English as used in Bayvarra (`en-XB`, the variant the flow uses as `languageID`). `LocaleCode` = `en` occurs 362 times in 213 of the 250 `*.xml` examples (counts of the broad, parties and context parts).
- Condition: `LocaleCode` holds a locale (language plus region, from a stated locale list), or is absent.
- Options: (a) preferred: `en-XB` with a locale list ID (BCP 47 style); (b) omit LocaleCode, since `Language/ID` already says English.
- Needs decision: no
- From: broad F3, parties F3, context F3

### energy/04#F4 · Medium · Natural gas in a pipeline declared as dry bulk cargo
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification/cbc:CargoTypeCode` = `BULK`
- Why: `CargoTypeCode` is "A mutually agreed code signifying the type of cargo for purposes of commodity classification"; the world list defines BULK as "Dry bulk: loose dry goods such as ore or grain, poured into the hold". The goods are natural gas in gaseous state (HS 271121) carried by pipeline (`TransportModeCode` 7, `TransportMeansTypeCode` 71): nothing dry, loose or in a hold. The list has no code for gas, and LIQUID ("liquids in tanks") does not fit either. BULK with natural gas occurs only here and in 05-ImportCustomsDeclaration.xml (count of the logistics part over `*.xml`).
- Condition: the commodity classification carries no cargo type, or one whose meaning covers gas in a pipeline.
- Options: (a) preferred by broad and context: omit `CargoTypeCode`, since HS code and transport mode already describe pipeline gas; (b) preferred by logistics: add a code for gaseous bulk to the world's CargoTypeCode list and use it here and in 05, because cargo type is meaningful in a customs declaration.
- Needs decision: no
- From: broad F2, logistics F3, context F2

### energy/04#F5 · Medium · The declaration does not say for which period the gas was exported, nor where it left Bayvarra
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KG-P1-2603`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Description` = `Natural gas from the Kelpstone offshore field, treated to pipeline quality; per megawatt hour, measured at the border station.`
- Why: the declaration, issued 2026-04-02, declares 39200 MWh that already flowed through a pipeline; it only makes sense as the declaration of a period's flow (March 2026, the period of 06 and 07). Nothing states that period: no `ShipmentStage/TransitPeriod` ("The period during which this shipment stage actually took place"), no validity period, no note; only the identifier KG-P1-2603 hints at it. Nor does it say where the gas leaves Bayvarra: the item text names a border station, but there is no `CustomsDeclaration/CustomsExitOfficeLocation` (available in the model, checked in the merge) or other location, and the customs office at Marrowdale is not tied to the pipeline. Without period and exit point the declared quantity cannot be checked against the border metering.
- Condition: the declaration states the period of the declared flow in a structured element and the place (border station or exit office) where the gas leaves the country.
- Options: (a) preferred: `ShipmentStage/cac:TransitPeriod` 2026-03-01 → 2026-03-31 and `CustomsDeclaration/cac:CustomsExitOfficeLocation` (or the border station as a location of the stage); (b) at least the period, with the exit point in the stage's description; a Note is the weakest alternative.
- Needs decision: no
- From: broad F8 (period part, Low), logistics F4, context F4

### energy/04#F6 · Medium · Province held in Region
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political/administrative division, which belongs in `CountrySubentity`, as this very document does for the exporter (`/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:CountrySubentity` = `Northern Territory`). World convention via the XU address format; 219 occurrences in 104 of the 250 `*.xml` examples.
- Condition: no Urvanian address carries its province in `cbc:Region`, or the world states why it is an economic region.
- Options: (a) preferred: move the province to `CountrySubentity`; (b) keep `Region` only for a real region in UBL's sense.
- Needs decision: no
- From: broad F4, parties F4

### energy/04#F7 · Medium · Customs authority described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:ID` = `XB:FBR`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: the Customs and Border Service of Bayvarra is a public authority (ISIC 8411). `CorporateRegistrationTypeCode` `COMMERCIAL` places it in the federal business register as a commercial registration, and `CompanyLiquidationStatusCode` presumes a company that can be wound up; neither applies to a government agency. Counts: 18 `CustomsParty`/`AuthorityParty` elements in 18 files carry a liquidation status and 18 a `COMMERCIAL` registration type (parties part); 90 parties with ISIC 8411 in 75 files carry a liquidation status (broad part), both over `*.xml` with lxml.
- Condition: the authority's legal entity contains no commercial-register type and no liquidation status; if it is listed in a register at all, the registration type names a register of public bodies.
- Options: (a) preferred: reduce the authority's `PartyLegalEntity` to its registration name and the identifier under which public bodies are listed (or leave it out); (b) add a registration type for public bodies to the world's list and use it, without liquidation status.
- Needs decision: no
- From: broad F6 (Low), parties F2

### energy/04#F8 · Low · The plant description says the field lies four kilometres out; the coordinates are 6.1 km apart
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `52.80`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `18.00`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:OriginAddress/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `49.80`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:OriginAddress/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `16.20`
- Why: recalculated: plant 39°52.80′ S 15°18.00′ W, field (`OriginAddress`, grid cell 33/03) 39°49.80′ S 15°16.20′ W; Δlat 3.00′ = 5.56 km, Δlon 1.80′ × cos 39.85° = 2.56 km, distance 6.1 km, against "four kilometres out". The context part refuted this because the origin is a grid cell whose coordinate need not be the platform; that keeps it Low, but the gap is large for a value given to one figure. The same description is in 05, the same field coordinates in 06 and 07.
- Condition: the distance in the description agrees with the coordinates of plant and field (within its rounding), or the origin is explicitly the grid cell and not the platform.
- Options: (a) preferred: "about six kilometres out" (keeps the map coordinates); (b) move the field's coordinates to about 4 km from the plant, if the map allows.
- Needs decision: no
- From: broad F7, logistics F6; context listed it as refuted

### energy/04#F9 · Low · The plant's InformationURI is the company's home page
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PhysicalLocation/cbc:InformationURI` = `https://www.kelpstone.example`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cbc:WebsiteURI` = `https://www.kelpstone.example`
- Why: `Location/InformationURI` is "The Uniform Resource Identifier (URI) of a document providing information about this location." The value is the party's own web site, already in `WebsiteURI`, not a document about the gas treatment plant.
- Condition: `InformationURI` points to information about the location itself, or is absent.
- Options: (a) preferred: leave it out; (b) point it to a page about the plant if the story has one.
- Needs decision: no
- From: parties F7

### energy/04#F10 · Low · Exporter's contact is its gas sales manager
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Gas sales manager`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Commercial`
- Why: the exporter's contact in an export declaration is the one customs turns to about the declaration (export/customs compliance, or gas dispatching). The gas sales manager of the commercial department is the party's general master-data contact and appears unchanged in every Kelpstone document of the flow (05–09).
- Condition: the exporter's contact deals with the export formalities or the gas movement.
- Options: (a) preferred: an export/customs or dispatching contact in Kelpstone's customs documents; (b) leave the contact out.
- Needs decision: no
- From: parties F6

### energy/04#F11 · Low · The customs value is not linked to the invoices it is the sum of
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1411200.00`
- Why: the declared value is exactly the two March invoices 06 (KG-INV-26-0157) and 07 (KG-INV-26-0158) converted to lume, a transaction value, but the declaration does not name them, although `CustomsDeclaration/AdditionalDocumentReference` exists for this (checked in the model in the merge). The import side has the same gap (energy/05#F6).
- Condition: the commercial invoices behind the customs value can be identified from the declaration.
- Options: (a) preferred: `CustomsDeclaration/cac:AdditionalDocumentReference` to KG-INV-26-0157 and KG-INV-26-0158 with a commercial-invoice type code (per consignment, if F2 splits the export); (b) a note; (c) leave it if the world's customs profile does not reference invoices, and say so in the profile.
- Needs decision: no
- From: broad F8 (invoice part)

### energy/04#F12 · Low · JourneyID carries a month's flow, not a service schedule
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KG-P1-2603`
- Why: `TransportMeans/JourneyID` is "An identifier for the regular service schedule of this means of transport." The value reads as pipeline 1, March 2026 (the suffix 2603 follows the flow's period identifiers, e.g. `01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cbc:ConsumptionID` = `FG-CP-4120-G1-2603`), i.e. one month's flow, not a schedule of the pipeline. It is also the only place the period appears (F5). The same value is in 05.
- Condition: `JourneyID` identifies a regular schedule of the pipeline (e.g. a nomination or flow schedule), or is absent; the period is stated where F5 asks.
- Options: (a) preferred: leave `JourneyID` out and identify the pipeline itself (`TransportMeans` with a name or identifier), with the period per F5; (b) keep it if the story gives the pipeline a monthly flow schedule with this number.
- Needs decision: no
- From: logistics F5

### energy/04#F13 · Low · The consignee's Urvanian address is tagged as Bayvarran English, its legal form untagged
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Via della Centrale`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]` = `Serravona`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Serravona`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Società urvaniana per azioni (public limited company)`
- Why: the English renderings of Montebrio Power's street and town carry `languageID="en-XB"` (English as used in Bayvarra), while the same texts are tagged `en-XU` in `05-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:StreetName[2]` = `Via della Centrale` and in 03 and 09. The legal form, given in `qau` and `en-XU` there, is a single untagged text here. The tag follows the issuer's country rather than the language of the text, so the same address is described differently in the flow. Over `*.xml`: 107 Urvanian addresses in 39 files carry an `en-XB` rendering, and 34 SUA legal entities in 34 files have an untagged `CompanyLegalForm` (parties part, lxml).
- Condition: the renderings of an Urvanian party's address and legal form carry the same `languageID` values in every example, whoever issues the document.
- Options: (a) preferred: tag the English rendering of an Urvanian name `en-XU` and keep the `qau` rendering of the legal form; (b) if the world intends tags by the issuer's locale, record that rule and apply it to the legal form too.
- Needs decision: no
- From: broad F5, parties F5

## Checked and consistent
- Value, recalculated: 39200 MWh × 36 XBL = 1 411 200 XBL; 3600 XUF/MWh at 100 XUF per XBL (rate of 06, 2026-01-02, the same as in other flows, e.g. `tender/32-Invoice.xml:/Invoice/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01` in the opposite direction) = 36 XBL; (132 480 000 + 8 640 000) / 100 = 1 411 200; 1 411 200 / 39200 = 36 = `06-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `3600` / 100.
- Weight against energy: 2 940 000 kg / 39200 MWh = 75 kg/MWh = 13.33 kWh/kg = 48.0 MJ/kg; typical pipeline gas about 50.8 MJ/kg, pure methane 55.5 MJ/kg (own knowledge): plausible with some inerts. Shipment and goods item weight agree; gross = net for pipeline gas.
- Capacity: 39200 MWh / 744 h = 52.7 MW average, about 3.7 million m³ a month at 10.5 kWh/m³: a small export pipeline; no capacity stated.
- Codes: HS 271121, section V, CPC 12020, transport mode 7 and means type 71 (pipeline), MWH and KGM agree with each other and with the goods.
- Parties: Kelpstone Gas (`20412877`) described identically (59 leaf values) here and in 05–09; exporter with right of disposal (ISIC 0620) fits; customs trader ID `XB-TR-412877` as in 05; carrier Kelpstone running its own export pipeline is plausible; the customs party is the Bayvarran authority (ISIC 8411).
- Dates: issued 2026-04-02 16:41, before the import declaration (16:55).
- The customs value in lume is right for a declaration to Bayvarra's customs (money part).

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cbc:ID` = `KG-CD-26-0153`: a second document number — refuted: "An identifier associated with customs related procedures" allows a separate procedure number (from broad, context)
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Kelpstone Gas`: the exporter cannot be the carrier — refuted: a producer operating its export pipeline is the carrier, and no other party is said to run it (from broad, logistics, context)
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:StandardItemIdentification/cbc:ID`: a GTIN with a real GS1 prefix — refuted: its scheme is the world's own item scheme (`urn:ubl-examples:world:item`) (from broad)
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `1411200.00`: declared in lume while the invoices are in ferra — refuted: the exporting country's currency is right, and the figure agrees exactly (from money)
- Same element: value declared before the invoices exist (2026-04-03) — refuted: price fixed by contract and quantity by border metering (from logistics)
- The export also covers the 2400 MWh of 07 while the only consignee is Montebrio — the money part refuted it as a money finding (a consignee may differ from the buyer); the merge keeps it as High F2 with that reading in Why
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyTaxScheme/cac:TaxScheme/cbc:ID` = `STT` with TaxLevelCode `STATE`: an exporter registered only for state sales tax — refuted: the world gives Bayvarra a state sales tax, and the territory agrees with the address (from parties)
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:JobTitle` = `Public service officer` and `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Department` = `Public services`: a generic contact for the office handling a pipeline export — refuted: the contact name `Border office` says which office it is, and title and department agree (from parties; the broad part had included the department in its F6, see "Changed in the merge")
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Energy trading`: a trader as consignee contact — refuted: for pipeline gas the receiver's trading desk nominates and takes over the quantities (from parties)
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:PhysicalLocation/cbc:Description`: data the declaration does not use — refuted: the plant is where the goods leave the producer (from context); the distance in it is F8

## Changed in the merge
- broad F1 → F1 and F2: split. The shipment-ID clash contradicts 05 and the consignee clash contradicts 07; they have different conditions, so each is its own High finding (logistics had them apart, broad and context combined them).
- parties F1, logistics F1, context F1 (consignee part) → F2: options of all parts kept, each with the part that preferred it; money's refutation quoted in Why.
- broad F2, logistics F3, context F2 → F4: both preferred options kept (omit vs. new list code), attributed.
- broad F8 → F5 and F11: split into the missing period (merged with logistics F4 and context F4 at Medium, because the document's purpose depends on it; broad had Low) and the missing invoice link (kept Low).
- broad F4, parties F4 → F6: Needs decision set to no (broad had yes); same decision across the flow.
- broad F6, parties F2 → F7: Medium (broad had Low), because `COMMERCIAL` and the liquidation status state something about the party that does not apply to a public body; the contact department from broad F6 moved to "Considered and refuted" with the parties part's refutation.
- broad F7, logistics F6 → F8: combined; context's refutation quoted; Low kept.
- broad F5, parties F5 → F13: combined; legal form line added from parties.

## Outside this review
- Whether Ferrano Energy's 2400 MWh were imported into Urvania at all (no import declaration in the flow) is a finding here (F2) and in the review of 07-Invoice.xml; the timeline of the pipeline flow against the declaration date is not examined.
