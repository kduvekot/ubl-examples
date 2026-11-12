# LLM review: 10-ImportCustomsDeclaration.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/10-ImportCustomsDeclaration.xml`, Git blob `e4f412380312e36eb2dbbc9f243cbc69a0fee18e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 60500a8 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/10#F1 · High · Declaration issued after the transportation status reported it accepted
- XPath: `/ImportCustomsDeclaration/cbc:IssueDate` = `2026-03-24`
- XPath: `/ImportCustomsDeclaration/cbc:IssueTime` = `09:54:00`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cbc:IssueTime` = `09:10:00`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cbc:OccurrenceTime` = `08:55:00`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cac:CurrentStatus/cac:SubStatus/cbc:Description` = `Import declaration accepted by Bayvarra's customs.`
- Why: This import declaration is issued on 2026-03-24 at 09:54. The carrier's status, issued at 09:10 for the border crossing completed at 08:55, already reports this declaration as accepted and the goods as released. The release at the border cannot precede the declaration it is based on.
- Condition: The import declaration is issued before the time at which the flow reports the goods released on it.
- Options: (a, preferred) issue the declaration before the truck reaches the border (a pre-arrival declaration on 2026-03-24 early morning or the evening before); (b) move the release to a later status.
- Needs decision: no

### road/10#F2 · High · Emission value is not factor × base
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: UBL defines `ValueFactorNumeric` as "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` as "The base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". With a factor of 0.82 per 1 EA the calculated value is 0.82, not the stated 96 kg CO2e (`ValueMeasure`, "total emissions in kg CO2"). The factor does not fit any quantity in the item either (34 kg steel and 22.5 kg hardwood consumed per bench: 0.82 × 56.5 kg = 46.3 kg, 0.82 × 34 kg = 27.9 kg). The same block occurs in 39 examples across flows (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82' world/examples | wc -l`).
- Condition: `ValueFactorNumeric` × `ValueBaseMeasure` equals `ValueMeasure` (in consistent units), or the factor and base are absent.
- Options: (a, preferred) give the factor and base the 96 kg are actually calculated from (e.g. kg CO2e per kg of material with the bench's mass as base), so the arithmetic holds; (b) remove `ValueFactorNumeric` and `ValueBaseMeasure` and keep only the total, if no factor is known.
- Needs decision: no

### road/10#F3 · High · Certificate reference resolves to two documents
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `FCC-CO-26-0157`
- XPath: `06-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:ID` = `FCC-CO-26-0157`
- XPath: `07-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:ID` = `FCC-CO-26-0157`
- XPath: `06-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:VersionID` = `1`
- XPath: `07-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:VersionID` = `1`
- Why: The reference carries only the ID FCC-CO-26-0157, which is the ID of both the exporter's application (`06`, status SUBMITTED, issued 2026-03-20) and the chamber's approved certificate (`07`, issued 2026-03-22), both with version 1. Without a UUID, issue date, version or document type, the declaration cannot be linked to the approved certificate that preferential treatment requires.
- Condition: The reference identifies exactly one document, the approved certificate of origin (e.g. distinct IDs or versions, or the reference adds UUID/issue date and a document type).
- Options: (a, preferred) fix the duplicate ID in the certificate documents and add a document type (certificate of origin) here; (b) add the certificate's UUID and issue date to the reference.
- Needs decision: no

### road/10#F4 · Medium · Language code in LocaleCode
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is defined as "A code signifying the locale in which this language is used"; a locale is a combination of language and region (e.g. en-XB), not a language. The value repeats the ISO 639 language code of `Language/ID` (listID `ISO 639`), so the element carries a language, not a locale, and adds nothing to `Language/ID`. The same pattern occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: `LocaleCode` is either absent or holds a locale (language and region) from a locale list named in its listID, different in meaning from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`, since `Language/ID` already says English and nothing in the document needs the region; (b) give a real locale such as en-XB with a locale list as listID, if the region matters to the party.
- Needs decision: no

### road/10#F5 · Medium · Gate number in AdditionalStreetName of the postal address
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is not a street name but an entrance of the business park, information that matters only to vehicles delivering goods, and it is carried in Lumeway's postal/registered address in every document. The road flow itself mentions other entrances (`Gate B` as alternative delivery location and `dock 4` in the Order and Waybill), so the gate is a delivery instruction, not part of the address. Counted over `*.xml`: 76 examples (`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: `AdditionalStreetName` holds no gate, dock or entrance; such information, where needed, is in a delivery location or delivery instruction.
- Options: (a, preferred) remove `Gate 3` from the party address and, where the document is about delivery, put the gate in `Delivery/DeliveryLocation` or the delivery instructions; (b) keep it only in a delivery address with a dedicated element such as `Location/Description`.
- Needs decision: no

### road/10#F6 · Medium · Province in Region instead of CountrySubentity
- XPath: `/ImportCustomsDeclaration/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative subdivision of the country, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located", with `CountrySubentityCode`). The Bayvarran addresses of the same examples do use `CountrySubentity` (`Upland State`), so the two countries' addresses are structured differently for the same kind of information. Counted over `*.xml`: 104 examples carry `<cbc:Region>Province of …` (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: No address of this example holds a province in `Region`; the province is in `CountrySubentity` (and, where a list exists, `CountrySubentityCode`).
- Options: (a, preferred) move the value to `CountrySubentity`, with a code from the Urvanian subdivision list if one exists, like the Bayvarran addresses; (b) keep `Region` only if Urvania's provinces are defined as economic regions rather than administrative divisions, and say so in the world's address rules.
- Needs decision: no

### road/10#F7 · Medium · Public authority described as a company in the commercial register
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: `PartyLegalEntity` describes the party's legal registration. The Customs and Border Service of Bayvarra is a public authority: it is not entered in the commercial register (`CorporateRegistrationTypeCode` COMMERCIAL under the scheme "Commercial register"), and a liquidation status ("A code signifying the party's liquidation status") does not apply to a state administration, which cannot be liquidated like a company. The checklist of this review treats such a description as a meaning other than the element's definition.
- Condition: The authority's legal entity is not described as a commercially registered company with a liquidation status; if a legal entity is given, it names the public-law basis or register that applies to it.
- Options: (a, preferred) remove `CompanyLiquidationStatusCode` and the commercial `CorporateRegistrationScheme`, keeping the registration name; (b) use a registration scheme for public bodies, if the world has one.
- Needs decision: no

### road/10#F8 · Medium · Urvanian national tariff codes in Bayvarra's import declaration
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: The goods are declared for free circulation in Bayvarra (`JurisdictionRegionAddress` XB), but the national subdivisions are taken from Urvania's tariff (listID `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`). An import declaration classifies the goods in the importing country's tariff, on which duty and statistics depend (own knowledge of customs practice); the exporting country's tariff code has no role in it.
- Condition: The national commodity codes of the import declaration come from Bayvarra's tariff (or are absent, leaving the HS code), not from Urvania's.
- Options: (a, preferred) use Bayvarra's tariff codes with a Bayvarran listID; (b) keep only the HS 2022 code if Bayvarra's tariff has no list in the world.
- Needs decision: no

### road/10#F9 · Low · Duties said to be paid, but no duty data and a preferential certificate
- XPath: `/ImportCustomsDeclaration/cbc:Note` = `Duties paid by the importer's account at customs.`
- XPath: `/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `FCC-CO-26-0157`
- Why: The note says "Duties paid by the importer's account at customs", but the declaration carries no duty, tax or payment data, and it claims preferential origin with the certificate FCC-CO-26-0157, which under the trade accord would normally reduce the duty to zero. Whether duty is due, and whether import tax (Bayvarra's state tax) is collected at the border, is a judgment on the world's tax treatment that cannot be settled from the examples.
- Condition: The note, the preferential claim and the declaration's duty/tax data agree (either duty-free under preference, or duty and its amount stated).
- Options: (a, preferred) state the duty treatment (preferential 0 %, import tax if any) and adjust the note; (b) remove the note.
- Needs decision: yes

### road/10#F10 · Low · Export-side office and a validity period in an import declaration
- XPath: `/ImportCustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`
- XPath: `/ImportCustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure` = `30`
- Why: `CustomsExitOfficeLocation` is the "Customs exit office of the goods being declared"; for goods imported into Bayvarra, the Urvanian exit post belongs to the export declaration (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name`), while the Bayvarran office of entry is missing. A validity of 30 days has no role in a release for free circulation, which takes effect on release.
- Condition: The import declaration names the Bayvarran office where the goods enter (or none), and carries a validity only if the procedure has one.
- Options: (a, preferred) replace the exit office by the Bayvarran entry office and remove the validity period; (b) keep the validity only if the world's customs rules give import declarations one.
- Needs decision: no

### road/10#F11 · Low · Contacts that do not fit the role
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ImportCustomsDeclaration/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Name` = `Border office`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/ImportCustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Department` = `Public services`
- Why: The importer's contact for a customs declaration should handle import formalities; Lumeway gives its `Customer service` desk in `Sales`. The customs contact has the generic job title `Public service officer` in `Public services`.
- Condition: The importer's contact handles customs formalities; the customs contact's title and department fit a customs office.
- Options: (a, preferred) give fitting contacts; (b) omit JobTitle/Department.
- Needs decision: no

### road/10#F12 · Low · Item master data copied into a document that does not use it
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:AdditionalItemProperty[5]`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile`
- Why: A import customs declaration needs the goods description, classification, origin, quantity, value and weight. The bench is carried with its warranty, load test, colour property group, dimensions, cradle-to-gate emissions, resource consumption, waste and repairability score. None of this is used by the document's purpose (section 4.8: data copied from master data into a document that does not use it).
- Condition: The item in this document carries what its purpose needs; environmental, circularity, warranty and test data are absent unless the document uses them.
- Options: (a, preferred) reduce the item to description, name, identifiers, origin and commodity classification; (b) keep single properties that the authority actually checks and say why.
- Needs decision: no

### road/10#F13 · Low · Item number looks like a real GTIN-12 with issuer scope 771
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`
- XPath: `/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- Why: The standard item numbers 771020000027 and 771020000034 (scheme `urn:ubl-examples:world:item`) are 12 digits with a valid GS1 mod-10 check digit (computed: 7 and 4), so any scanner or GS1 check reads them as GTIN-12s; a GTIN-12 starting with 7 lies in the UPC range administered by GS1 US, and the issuer scope `771` is also a GS1 prefix (GS1 Colombia, 770–771). This rests on my knowledge of the GS1 prefix allocation. The rule that fictional values must not be mistakable for real register entries applies. In addition, only the bench carries `BarcodeSymbologyID` and `IssuerScopeID`; the side frame's number from the same scheme carries neither.
- Condition: The item numbers cannot be read as validly check-digited GTINs of a real GS1 prefix, and both items of the same scheme are described the same way.
- Options: (a, preferred) confirm against the world's identifier rules whether the world item scheme is meant to mimic GTIN; if so, use a GS1 prefix reserved for demonstration or a non-GS1 structure; (b) drop `IssuerScopeID`/`BarcodeSymbologyID` where they have no role in the document.
- Needs decision: yes

### road/10#F14 · Low · Signature ID made from the example number or flow name
- XPath: `/ImportCustomsDeclaration/cac:Signature/cbc:ID` = `LD-SIG-IM-road`
- Why: `Signature/ID` is "An identifier for this signature". The value `LD-SIG-IM-road` is built from the example's place in the collection (the example number or the flow name), not from a numbering the signing party would use; the other signature IDs of the flow follow the party's own document numbering (e.g. `FCC-SIG-26-0309`, `LTAC-SIG-26-0311`, `XB-CUS-SIG-0884`). An identifier that reveals the example structure is out of the world's story.
- Condition: The signature ID follows the signing party's own numbering and contains no example number or flow name.
- Options: (a, preferred) number the signature like the party's other signatures (prefix, year, running number); (b) derive it from the document ID.
- Needs decision: no

## Checked and consistent
- Customs values converted at 0.01 XBL per XUF: 4 790 400 → 47 904.00 and 71 760 → 717.60, the rate of `15-Invoice.xml:/Invoice/cac:PaymentExchangeRate/cbc:CalculationRate` = `0.01`.
- Quantities 96 and 12, gross weights 3984 and 122.4 kg (total 4106.4), shipment CL-SH-26-0154 agree with `04`, `05` and `08`; despatch line references 1 and 2 of CL-DA-26-0153 resolve to `04-DespatchAdvice.xml`.
- Roles: importer, consignee and notifier Lumeway, consignor Valdara, customs the Bayvarran service; consistent with the waybill's instruction that the distributor declares the import.
- `PreviousCustomsDeclaration` VI-CD-26-0156 is the export declaration in `05-ExportCustomsDeclaration.xml`.

## Considered and refuted
- `/ImportCustomsDeclaration/cac:PreviousCustomsDeclaration/cbc:ID` = `VI-CD-26-0156`: a previous declaration of another customs territory looked out of place — refuted: the definition is "A reference to a previously sent customs declaration", and linking import to the partner country's export declaration is plausible under the trade accord.
- Customs value equal to the FCA price without freight to the border — refuted as a finding: the world's valuation rules (FCA, FOB or CIF basis) are not stated in the examples, so the value cannot be shown to be wrong.
