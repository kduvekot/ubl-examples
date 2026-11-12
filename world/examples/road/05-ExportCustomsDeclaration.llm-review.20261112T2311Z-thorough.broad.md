# LLM review: 05-ExportCustomsDeclaration.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/05-ExportCustomsDeclaration.xml`, Git blob `0fa315bd3a963ac3f8916911094b6904a7e60fbf` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b8faf2 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/05#F1 · High · Waybill says the 3PL declared the export; this declaration is Valdara's own
- XPath: `/ExportCustomsDeclaration/cbc:ID` = `VI-EX-26-0155`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/ExportCustomsDeclaration/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:CustomsClearanceServiceInstructions` = `The export is declared by the 3PL in Ferrano; the import by the distributor at the border.`
- XPath: `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:CustomsDeclaration/cac:IssuerParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- Why: This export declaration is numbered and signed by Valdara (VI-EX-…, signature by Valdara Industries), with no declarant or agent named, i.e. the exporter declares itself. The waybill states that "The export is declared by the 3PL in Ferrano" (Castrano) and gives the customs administration as the party who issues the declaration VI-CD-26-0156. Three documents of the flow name three different declarants for the same declaration.
- Condition: Every document of the flow names the same party as declarant of the export, and this declaration identifies that party in its declarant/exporter role and signature.
- Options: (a, preferred) decide who declares (Valdara as exporter, or Castrano as its agent with a declarant/agent party here) and align this declaration and the waybill; (b) if Castrano declares on Valdara's behalf, add it as declarant and let it sign.
- Needs decision: yes

### road/05#F2 · High · Emission value is not factor × base
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: UBL defines `ValueFactorNumeric` as "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` as "The base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". With a factor of 0.82 per 1 EA the calculated value is 0.82, not the stated 96 kg CO2e (`ValueMeasure`, "total emissions in kg CO2"). The factor does not fit any quantity in the item either (34 kg steel and 22.5 kg hardwood consumed per bench: 0.82 × 56.5 kg = 46.3 kg, 0.82 × 34 kg = 27.9 kg). The same block occurs in 39 examples across flows (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82' world/examples | wc -l`).
- Condition: `ValueFactorNumeric` × `ValueBaseMeasure` equals `ValueMeasure` (in consistent units), or the factor and base are absent.
- Options: (a, preferred) give the factor and base the 96 kg are actually calculated from (e.g. kg CO2e per kg of material with the bench's mass as base), so the arithmetic holds; (b) remove `ValueFactorNumeric` and `ValueBaseMeasure` and keep only the total, if no factor is known.
- Needs decision: no

### road/05#F3 · Medium · Province in Region instead of CountrySubentity
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative subdivision of the country, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located", with `CountrySubentityCode`). The Bayvarran addresses of the same examples do use `CountrySubentity` (`Upland State`), so the two countries' addresses are structured differently for the same kind of information. Counted over `*.xml`: 104 examples carry `<cbc:Region>Province of …` (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: No address of this example holds a province in `Region`; the province is in `CountrySubentity` (and, where a list exists, `CountrySubentityCode`).
- Options: (a, preferred) move the value to `CountrySubentity`, with a code from the Urvanian subdivision list if one exists, like the Bayvarran addresses; (b) keep `Region` only if Urvania's provinces are defined as economic regions rather than administrative divisions, and say so in the world's address rules.
- Needs decision: no

### road/05#F4 · Medium · Language code in LocaleCode
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is defined as "A code signifying the locale in which this language is used"; a locale is a combination of language and region (e.g. en-XB), not a language. The value repeats the ISO 639 language code of `Language/ID` (listID `ISO 639`), so the element carries a language, not a locale, and adds nothing to `Language/ID`. The same pattern occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: `LocaleCode` is either absent or holds a locale (language and region) from a locale list named in its listID, different in meaning from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`, since `Language/ID` already says English and nothing in the document needs the region; (b) give a real locale such as en-XB with a locale list as listID, if the region matters to the party.
- Needs decision: no

### road/05#F5 · Medium · Gate number in AdditionalStreetName of the postal address
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is not a street name but an entrance of the business park, information that matters only to vehicles delivering goods, and it is carried in Lumeway's postal/registered address in every document. The road flow itself mentions other entrances (`Gate B` as alternative delivery location and `dock 4` in the Order and Waybill), so the gate is a delivery instruction, not part of the address. Counted over `*.xml`: 76 examples (`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: `AdditionalStreetName` holds no gate, dock or entrance; such information, where needed, is in a delivery location or delivery instruction.
- Options: (a, preferred) remove `Gate 3` from the party address and, where the document is about delivery, put the gate in `Delivery/DeliveryLocation` or the delivery instructions; (b) keep it only in a delivery address with a dedicated element such as `Location/Description`.
- Needs decision: no

### road/05#F6 · Medium · Public authority described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: `PartyLegalEntity` describes the party's legal registration. The Customs Administration of Urvania is a public authority: it is not entered in the commercial register (`CorporateRegistrationTypeCode` COMMERCIAL under the scheme "Commercial register"), and a liquidation status ("A code signifying the party's liquidation status") does not apply to a state administration, which cannot be liquidated like a company. The checklist of this review treats such a description as a meaning other than the element's definition.
- Condition: The authority's legal entity is not described as a commercially registered company with a liquidation status; if a legal entity is given, it names the public-law basis or register that applies to it.
- Options: (a, preferred) remove `CompanyLiquidationStatusCode` and the commercial `CorporateRegistrationScheme`, keeping the registration name; (b) use a registration scheme for public bodies, if the world has one.
- Needs decision: no

### road/05#F7 · Low · Contacts that do not fit the role
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Name` = `Border office`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Department` = `Public services`
- Why: The exporter's contact for a customs declaration should be the person responsible for export formalities; Valdara gives its `Order desk` in `Sales`. The customs administration's contact is a `Border office` with the generic job title `Public service officer` in a department `Public services`, which says nothing about customs work.
- Condition: The exporter's contact handles customs formalities; the customs contact's job title and department fit a customs office.
- Options: (a, preferred) give Valdara an export or shipping contact and the customs office a customs job title and department; (b) omit JobTitle/Department.
- Needs decision: no

### road/05#F8 · Low · Item master data copied into a document that does not use it
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:AdditionalItemProperty[5]`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile`
- Why: A export customs declaration needs the goods description, classification, origin, quantity, value and weight. The bench is carried with its warranty, load test, colour property group, dimensions, cradle-to-gate emissions, resource consumption, waste and repairability score. None of this is used by the document's purpose (section 4.8: data copied from master data into a document that does not use it).
- Condition: The item in this document carries what its purpose needs; environmental, circularity, warranty and test data are absent unless the document uses them.
- Options: (a, preferred) reduce the item to description, name, identifiers, origin and commodity classification; (b) keep single properties that the authority actually checks and say why.
- Needs decision: no

### road/05#F9 · Low · Item number looks like a real GTIN-12 with issuer scope 771
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- Why: The standard item numbers 771020000027 and 771020000034 (scheme `urn:ubl-examples:world:item`) are 12 digits with a valid GS1 mod-10 check digit (computed: 7 and 4), so any scanner or GS1 check reads them as GTIN-12s; a GTIN-12 starting with 7 lies in the UPC range administered by GS1 US, and the issuer scope `771` is also a GS1 prefix (GS1 Colombia, 770–771). This rests on my knowledge of the GS1 prefix allocation. The rule that fictional values must not be mistakable for real register entries applies. In addition, only the bench carries `BarcodeSymbologyID` and `IssuerScopeID`; the side frame's number from the same scheme carries neither.
- Condition: The item numbers cannot be read as validly check-digited GTINs of a real GS1 prefix, and both items of the same scheme are described the same way.
- Options: (a, preferred) confirm against the world's identifier rules whether the world item scheme is meant to mimic GTIN; if so, use a GS1 prefix reserved for demonstration or a non-GS1 structure; (b) drop `IssuerScopeID`/`BarcodeSymbologyID` where they have no role in the document.
- Needs decision: yes

### road/05#F10 · Low · Document reference with only an ID
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `LD-PO-26-0149`
- Why: A document reference that carries only an ID must say what it refers to where that is not obvious (no `DocumentTypeCode` or `DocumentType`, no issue date). LD-PO-26-0149 is the buyer's purchase order (`01-Order.xml`); in a customs declaration an untyped additional document is most likely read as a supporting document such as an invoice or licence.
- Condition: The reference states the kind of document it refers to (type code or type text).
- Options: (a, preferred) add `DocumentTypeCode` from the world's document type list (as the remittance advice does); (b) add `DocumentType` as text.
- Needs decision: no

### road/05#F11 · Low · Signature ID made from the example number or flow name
- XPath: `/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `VI-SIG-EX-road`
- Why: `Signature/ID` is "An identifier for this signature". The value `VI-SIG-EX-road` is built from the example's place in the collection (the example number or the flow name), not from a numbering the signing party would use; the other signature IDs of the flow follow the party's own document numbering (e.g. `FCC-SIG-26-0309`, `LTAC-SIG-26-0311`, `XB-CUS-SIG-0884`). An identifier that reveals the example structure is out of the world's story.
- Condition: The signature ID follows the signing party's own numbering and contains no example number or flow name.
- Options: (a, preferred) number the signature like the party's other signatures (prefix, year, running number); (b) derive it from the document ID.
- Needs decision: no

## Checked and consistent
- Goods items: 96 benches with declared value 4 790 400 XUF and 12 side frames with 71 760 XUF equal the order and invoice line amounts (FCA value at the place of export); gross weights 3984 + 122.4 = 4106.4 kg = shipment gross weight in `04`, `08` and `10`.
- Issued 2026-03-23 13:25, before the actual despatch at 16:20 (`04-DespatchAdvice.xml`), consistent with the note "Declared electronically before the goods leave" and the waybill's instruction to wait for the release.
- `FunctionCode` 9 (original) with `VersionID` 1; validity 90 days from 2026-03-23 covers the exit on 2026-03-24.
- Shipment CL-SH-26-0154, consignment LD-CS-26-0152 and carrier Trasvia agree with the despatch advice and waybill; the declaration ID VI-CD-26-0156 is the one the waybill and the import declaration cite.
- HS codes 940179 (seats with metal frames) and 732599 (other cast articles of iron or steel) fit a park bench and a cast side frame (own knowledge of the HS).
- Weight per bench: 3984 kg / 96 = 41.5 kg gross including the pallet share, plausible for a steel and hardwood bench.

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure` = `90`: a validity on an export declaration looked out of place — refuted: export declarations commonly have a period within which the goods must exit (own knowledge), and the definition is "A period, assigned by the issuer, during which the information in the declaration is valid".
