# LLM review: 05-ImportCustomsDeclaration.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/05-ImportCustomsDeclaration.xml`, Git blob `7a7660d1d073ae04f45f02effa30b140182e1c33` (committed)
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

### energy/05#F1 · High · Same shipment as the export declaration, different quantity and weight
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `2760000`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `36800`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `2940000`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:Quantity` = `39200`
- XPath: `07-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `2400`
- Why: `Shipment/cbc:ID` is "An identifier for this shipment". This declaration gives shipment KG-SH-26-0154 36800 MWh and 2 760 000 kg; the export declaration gives the same shipment 39200 MWh and 2 940 000 kg, with Montebrio Power as sole consignee. The difference, 2400 MWh and 180 000 kg (75 kg/MWh in both, recalculated), is the gas Kelpstone sells to Ferrano Energy (07-Invoice.xml), for which the flow has no import declaration. The importer's quantity agrees with its own invoice (`06-Invoice.xml:/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `36800`), but the shared shipment identifier makes the two declarations contradict each other: either this declaration under-declares the shipment, or the export consigns to Montebrio gas it does not receive (energy/04#F2).
- Condition: the shipment identifier in this declaration stands for exactly the quantity and weight imported here, in every example that uses it, and every quantity exported in the flow is imported under a declaration naming its actual importer.
- Options: (a) preferred: keep 36800 MWh here as Montebrio's part of a shipment that the export declaration splits into two consignments (36800 MWh Montebrio, 2400 MWh Ferrano Energy), with a separate import declaration by Ferrano Energy; (b) give each buyer's gas its own shipment identifier in both directions, or give this import its own identifier and relate it to the export shipment as part of it; (c) Montebrio imports all 39200 MWh and resells 2400 MWh, which changes 07 (less plausible per broad: Ferrano Energy owns its gas).
- Needs decision: yes (documents of the flow and who imports the gas)
- From: broad F1, logistics F1, context F1

### energy/05#F2 · Medium · Province held in Region
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political/administrative division, which belongs in `CountrySubentity`, as this document does for the consignor (`/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:CountrySubentity` = `Northern Territory`). World convention via the XU address format; 219 occurrences in 104 of the 250 `*.xml` examples.
- Condition: no Urvanian address carries its province in `cbc:Region`, or the world states why it is an economic region.
- Options: (a) preferred: move the province to `CountrySubentity`; (b) keep `Region` only for a real region in UBL's sense.
- Needs decision: no
- From: broad F4, parties F2

### energy/05#F3 · Medium · Language code in LocaleCode
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` is the language itself, repeating `Language/ID`, not a locale such as `en-XB`. 362 occurrences in 213 of the 250 `*.xml` examples.
- Condition: `LocaleCode` holds a locale from a stated locale list, or is absent.
- Options: (a) preferred: `en-XB` with a locale list ID, matching the languageID of English renderings in the world; (b) leave it out.
- Needs decision: no
- From: broad F3, parties F3, context F3

### energy/05#F4 · Medium · Customs authority described as a company in the commercial register
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:ID` = `XU:CR`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: the Customs Administration of Urvania is a public authority (ISIC 8411). Its legal entity places it in the commercial register of Urvania and gives it a liquidation status, which presumes a company that can be wound up; neither applies to a government agency. Counts over `*.xml` (lxml): 18 `CustomsParty`/`AuthorityParty` elements in 18 files carry a liquidation status and 18 a `COMMERCIAL` registration type (parties part); 90 parties with ISIC 8411 in 75 files carry a liquidation status (broad part).
- Condition: the authority's legal entity contains no commercial-register scheme and no liquidation status; if it is listed at all, the registration type names a register of public bodies.
- Options: (a) preferred: reduce the authority's `PartyLegalEntity` to its registration name and the identifier under which public bodies are listed (or leave it out); (b) add a register of public bodies to the world and use it.
- Needs decision: no
- From: broad F5 (Low), parties F1

### energy/05#F5 · Medium · Natural gas in a pipeline declared as dry bulk cargo
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cac:CommodityClassification/cbc:CargoTypeCode` = `BULK`
- Why: `CargoTypeCode` is "A mutually agreed code signifying the type of cargo for purposes of commodity classification"; the world list defines BULK as "Dry bulk: loose dry goods such as ore or grain, poured into the hold". The goods are natural gas in gaseous state (HS 271121) carried by pipeline (mode 7, means type 71). The list has no code for gas, and LIQUID does not fit either. Same code in 04-ExportCustomsDeclaration.xml (energy/04#F4).
- Condition: no cargo type, or one whose meaning covers gas in a pipeline.
- Options: (a) preferred by broad and context: leave `CargoTypeCode` out; (b) preferred by logistics: add a gaseous-bulk code to the world list and use it in both declarations.
- Needs decision: no
- From: broad F2, logistics F2, context F2

### energy/05#F6 · Medium · The declaration does not say for which period the gas was imported, nor where it entered Urvania
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KG-P1-2603`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cac:Item/cbc:Description` = `Natural gas from the Kelpstone offshore field, treated to pipeline quality; per megawatt hour, measured at the border station.`
- Why: issued 2026-04-02, the declaration covers 36800 MWh that already flowed through the pipeline, i.e. the flow of March 2026, the period of 06-Invoice.xml on which the customs value rests. No element states the period (no `ShipmentStage/TransitPeriod`, "The period during which this shipment stage actually took place", no note), and nothing states where the gas entered Urvania, although the item text names the border station as the measuring point; only the identifier KG-P1-2603 hints at the month. Without period and entry point the declared quantity cannot be checked against the border metering.
- Condition: the declaration states the period of the imported flow in a structured element and the place of entry (border station).
- Options: (a) preferred: `ShipmentStage/cac:TransitPeriod` 2026-03-01 → 2026-03-31 and the border station as a location of the stage or as `Shipment/cac:FirstArrivalPortLocation`; (b) at least the period; a Note is the weakest alternative.
- Needs decision: no
- From: broad F6 (period part, Low), logistics F3, context F4

### energy/05#F7 · Low · Importer's and consignor's contacts are their trading and sales desks
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Energy trader`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:Contact/cbc:JobTitle` = `Gas sales manager`
- Why: the importer is the party who makes the import declaration; its contact is the one customs turns to about the declaration and the duties (customs or tax compliance), not the trader who bought the gas. The consignor's gas sales manager is likewise its general master-data contact, unchanged in every Kelpstone document of the flow.
- Condition: the importer's and consignor's contacts deal with the customs formalities or the gas movement.
- Options: (a) preferred: customs/compliance or dispatching contacts; (b) leave the contacts out.
- Needs decision: no
- From: parties F4 (contact part)

### energy/05#F8 · Low · The plant description says four kilometres to the field; the field's coordinates are 6.1 km away
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PhysicalLocation/cbc:Description` = `Gas treatment plant on the north coast; the platform of the offshore field lies four kilometres out.`
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `52.80`
- XPath: `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:OriginAddress/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `49.80`
- Why: recalculated: plant 39°52.80′ S 15°18.00′ W (this example), field 39°49.80′ S 15°16.20′ W (04, 06, 07): Δlat 5.56 km, Δlon 1.80′ × cos 39.85° = 2.56 km, distance 6.1 km, against "four kilometres". The field coordinate is a grid cell (04), so the platform need not sit there; hence Low.
- Condition: the distance in the description agrees with the coordinates of plant and field.
- Options: (a) preferred: "about six kilometres out"; (b) move the field's coordinates.
- Needs decision: no
- From: logistics F5

### energy/05#F9 · Low · The plant's InformationURI is the company's home page
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PhysicalLocation/cbc:InformationURI` = `https://www.kelpstone.example`
- Why: `Location/InformationURI` is "The Uniform Resource Identifier (URI) of a document providing information about this location"; the value repeats the party's `WebsiteURI` and is not about the gas treatment plant.
- Condition: `InformationURI` points to information about the location, or is absent.
- Options: (a) preferred: leave it out; (b) point it to a page about the plant.
- Needs decision: no
- From: parties F5

### energy/05#F10 · Low · The customs authority carries a VAT registration the declaration does not use
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyTaxScheme/cbc:CompanyID` = `XU007385602`
- Why: the authority's VAT registration plays no part in an import declaration it processes; it looks copied from master data (section 4.8). The Bayvarran authority in 04-ExportCustomsDeclaration.xml carries none.
- Condition: the authority carries no tax registration the declaration does not use.
- Options: (a) preferred: no `PartyTaxScheme` on the customs party; (b) keep it only with a reason in the story.
- Needs decision: no
- From: parties F4 (tax-scheme part)

### energy/05#F11 · Low · Customs value without a reference to the invoice it comes from
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `132480000`
- XPath: `06-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `132480000`
- Why: the declared customs value is exactly Kelpstone's invoice KG-INV-26-0157 (06), a transaction value, but the declaration does not name the invoice. `ImportCustomsDeclaration/AdditionalDocumentReference` ("A reference to additional documents related to or relevant for this customs declaration") exists for this, and customs authorities ask for the commercial invoice behind a transaction value.
- Condition: the commercial invoice behind the customs value can be identified from the declaration.
- Options: (a) preferred: `cac:AdditionalDocumentReference` with ID KG-INV-26-0157 and a commercial-invoice type code; (b) a note; (c) leave it if the world's customs profile does not reference invoices, and say so in the profile.
- Needs decision: no
- From: broad F6 (invoice part), context F5

### energy/05#F12 · Low · No reference to the export declaration of the same gas
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cbc:ID` = `KG-SH-26-0154`
- Why: the gas comes under the export declaration KG-EX-26-0152 (04-ExportCustomsDeclaration.xml), but this declaration does not cite it; the broad part asked for the link. The logistics part refuted that: an import declaration need not cite the other country's export declaration, and the shared shipment identifier already links the two (with the contradiction of F1). The model offers `ImportCustomsDeclaration/PreviousCustomsDeclaration` (checked in the merge), which could hold it, but whether the world's customs profile wants the link the merge could not settle.
- Condition: either the import declaration identifies the export declaration it follows, or the world's customs profile states that the shipment identifier is the link.
- Options: (a) `cac:PreviousCustomsDeclaration` or `cac:AdditionalDocumentReference` with KG-EX-26-0152; (b) leave it and rely on the shipment identifier once F1 is resolved (logistics' view).
- Needs decision: yes (could not settle whether it is a problem)
- From: broad F6 (export-declaration part); logistics listed it as refuted

### energy/05#F13 · Low · JourneyID carries a month's flow, not a service schedule
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KG-P1-2603`
- Why: `TransportMeans/JourneyID` is "An identifier for the regular service schedule of this means of transport." The value reads as pipeline 1, March 2026 (suffix 2603 as in the flow's other monthly identifiers), one month's flow rather than a schedule. The same value is in 04 (energy/04#F12).
- Condition: `JourneyID` identifies a regular schedule of the pipeline, or is absent; the period is stated where F6 asks.
- Options: (a) preferred: leave `JourneyID` out and identify the pipeline itself; (b) keep it if the story gives the pipeline a monthly flow schedule with this number.
- Needs decision: no
- From: logistics F4

## Checked and consistent
- Value, recalculated: 36800 MWh × 3600 XUF = 132 480 000 XUF = the declared customs value = 06-Invoice.xml line, total and payable amount; the gas is priced "measured at the border station", so the invoice price is a border value.
- Against the export declaration: 36800 of the 39200 MWh; the value and the weight are the same share (2 940 000 × 36800 / 39200 = 2 760 000 kg).
- Weight against energy: 2 760 000 kg / 36800 MWh = 75 kg/MWh = 48.0 MJ/kg, plausible for pipeline gas (own knowledge); goods item and shipment weights agree.
- Codes: transport mode 7, means type 71 (pipeline), HS 271121, section V, CPC 12020 as in 04; item KG-NG, origin XB, as in 06.
- Parties: importer = consignee = Montebrio Power, the buyer of 06, described identically (52 leaf values) as in 03 and 09 with `en-XU` tags; customs trader ID `XU-TR-105918` as in 04; consignor Kelpstone as in 04 and 06–09; the customs party (`XU-R-105507`) identical (44 leaf values) in ten examples of other flows.
- Physics downstream: 36800 MWh of gas against 18400 MWh of electricity in 03-Invoice.xml = 50 % efficiency, plausible for a combined-cycle plant.
- Dates: issued 2026-04-02 16:55, after the export declaration (16:41).

## Considered and refuted
- `/ImportCustomsDeclaration/cbc:IssueDate` and `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem/cbc:DeclaredCustomsValueAmount` = `132480000`: value taken from an invoice issued only the next day (06, 2026-04-03 11:25) — refuted: price and quantity are fixed by contract and border metering before the invoice is written (from broad, logistics)
- `/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Postbox` = `PB 18` with street and building number under `AddressTypeCode` `POSTAL` — refuted: a postal address may give both; the type code says it is the address for mail (from broad, parties)
- `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:JobTitle` = `Public service officer` and `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Department` = `Public services`: generic contact — refuted: the name `Border office` identifies the office, and title and department agree (from parties; the broad part had included the department in its F5, see "Changed in the merge")
- Import VAT and duty not stated — refuted: UBL 2.5 ImportCustomsDeclaration has no tax total or duty element; the declaration carries the value on which they are assessed (from money)
- The remaining 2400 MWh of the export declaration are not in this import — refuted for this example as a money finding: the declaration is Montebrio's own and matches its purchase; the missing import is part of F1 and of energy/04#F2 (from money)
- `/ImportCustomsDeclaration/cac:Shipment`: missing reference to the export declaration — refuted by logistics; the merge could not settle it and keeps it as Low F12 with Needs decision yes
- `/ImportCustomsDeclaration/cac:ConsigneeParty/cac:PartyName/cbc:Name` = `Montebrio Power`: repetition of ImporterParty — refuted: the definitions differ (declarant vs "The Party who receives the goods"); the short form avoids repeating the detail (from context)
- `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PhysicalLocation/cbc:Description`: copied master data — refuted: the consignor's dispatch site is relevant to an import declaration (from context); the distance in it is F8

## Changed in the merge
- broad F4, parties F2 → F2: Needs decision set to no (broad had yes); same decision across the flow.
- broad F5, parties F1 → F4: Medium (broad had Low), as in energy/04#F7; the contact department from broad F5 moved to "Considered and refuted" with the parties part's refutation.
- broad F6 → F6, F11 and F12: split into the missing period (merged with logistics F3 and context F4 at Medium, because the document's purpose depends on it), the missing invoice reference (with context F5, Low) and the missing export-declaration reference (Low, Needs decision yes, since logistics refuted it and the merge could not settle it).
- parties F4 → F7 and F10: split into the contacts and the authority's tax registration, which are different problems with different conditions.

## Outside this review
- Ferrano Energy's 2400 MWh (07-Invoice.xml) have no import declaration in the flow; that is part of F1 here and a finding of 04 and 07 (from parties).
