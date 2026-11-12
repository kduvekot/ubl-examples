# LLM review: 05-ExportCustomsDeclaration.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/05-ExportCustomsDeclaration.xml`, Git blob `0fa315bd3a963ac3f8916911094b6904a7e60fbf` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 3a48551 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/05#F1 · High · Declared by the exporter itself, while the waybill says the 3PL declares and names customs as issuer
- XPath: `/ExportCustomsDeclaration/cbc:ID` = `VI-EX-26-0155`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `/ExportCustomsDeclaration/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`
- XPath: `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:CustomsClearanceServiceInstructions` = `The export is declared by the 3PL in Ferrano; the import by the distributor at the border.`
- XPath: `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:CustomsDeclaration/cac:IssuerParty/cac:PartyName/cbc:Name` = `Customs Administration of Urvania`
- Why: this declaration is numbered in Valdara's series (VI-), signed by Valdara and names no declarant, agent or representative other than the exporter; Castrano Logistics appears only as Valdara's service provider for "Warehousing and despatch". The carrier's waybill for the same consignment says the export is declared by the 3PL, and gives the customs administration as issuer of the declaration VI-CD-26-0156. Three statements of the flow name three different parties for the same declaration. Refutation attempt in the merge: "declared by the 3PL in Ferrano" cannot be read as "declared at the 3PL's place", since it is contrasted with "the import by the distributor", a party; and Castrano's role as service provider for warehousing does not make it a customs representative. The issuer statement of 08 also contradicts this document's own signatory (the IssuerParty error itself lies in 08).
- Condition: every document of the flow names the same party as declarant of the export, and this declaration identifies that party in its exporter/declarant role and signature.
- Options: (a) the exporter declares: correct the waybill's text and issuer party (preferred: the declaration is complete as it stands; logistics' preference); (b) Castrano declares as Valdara's agent: show it in this declaration (a representative or declarant party, its signature) and keep the waybill's text.
- Needs decision: yes (who declares is part of the story)
- From: broad (F1), logistics (F1)

### road/05#F2 · High · Emission factor × base does not give the emission value
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 per 1 EA gives 0.82 kg CO2e per bench, not 96; 96 / 0.82 = 117.1 matches nothing in the flow (recalculated in the merge). 39 examples, 9 in this flow (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'`).
- Condition: factor × (activity / base) equals the value, or factor and base are absent.
- Options: (a) drop factor and base (preferred, as road/01); (b) a factor and base whose product is 96 kg.
- Needs decision: no
- From: broad (F2), logistics (F2), context (F3)

### road/05#F3 · Medium · Urvanian province in Region instead of CountrySubentity
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is `CountrySubentity`, which the Bayvarran address of the same document uses (`/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 files.
- Condition: the province is in `CountrySubentity`; `Region` is absent or a real region.
- Options: (a) move it to `CountrySubentity` (preferred); (b) define Urvanian provinces as non-administrative regions.
- Needs decision: no
- From: broad (F3), parties (F1), context (F4)

### road/05#F4 · Medium · Lifecycle stage code says manufacturing only, its text says cradle to gate
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: `MANUFACTURING` is "Making the product (EN 15804 module A3)" in the world list, while the text and description cover A1–A3 (mining, steel making, transport between the steps).
- Condition: code and text name the same stage(s).
- Options: (a) omit the code and keep the text (preferred); (b) reduce figure and texts to A3.
- Needs decision: no
- From: context (F1)

### road/05#F5 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: the element is "A code signifying whether a piece of transport equipment is full, partially full, or empty ..."; `CRADLETOGATE` is from the world list `EmissionBoundaryCode` (semantic conformance, §4.7). 39 examples do the same.
- Condition: absent from this item emission, or saying how full transport equipment is.
- Options: (a) drop it, state the boundary in text and record the missing element for the UBL TC write-up (preferred).
- Needs decision: no
- From: context (F2)

### road/05#F6 · Medium · LocaleCode holds a language code
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (ISO 639) repeats `Language/ID`. 362 occurrences in 213 files.
- Condition: `LocaleCode` is absent or a locale from a list of locales.
- Options: (a) drop it (preferred; broad, parties, rail and air merges); (b) `en-XB` with a locale list (context).
- Needs decision: no
- From: broad (F4), parties (F2), context (F5)

### road/05#F7 · Medium · Gate number in AdditionalStreetName of the consignee's address
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; `Gate 3` is an entrance, not a street. 79 occurrences in 76 files.
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance.
- Options: (a) drop it from the address (preferred).
- Needs decision: no
- From: broad (F5), parties (F3)

### road/05#F8 · Medium · The customs administration is described as a company in the commercial register
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Commercial register of Urvania`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: `CorporateRegistrationScheme` is "The corporate registration scheme used to register the party" and `CompanyLiquidationStatusCode` "A code signifying the party's liquidation status". The Customs Administration of Urvania is a state authority (ISIC 8411, general public administration): it is not entered in the commercial register and cannot be liquidated like a company; the checklist names exactly this case.
- Condition: the customs party carries no commercial-register scheme and no liquidation status; if it has a legal-entity description, it is that of a public body.
- Options: (a) keep only `RegistrationName`, or drop `PartyLegalEntity` for the authority (preferred: the declaration only addresses the authority); (b) a register of public bodies, if the world has one.
- Needs decision: no
- From: broad (F6), parties (F4), context (F6)

### road/05#F9 · Low · Contacts that do not fit an export declaration
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Department` = `Public services`
- Why: customs asks the exporter's export or customs function about the declaration, not the order desk in Sales; the consignee's contact in Lumeway's Sales customer service serves Lumeway's own customers; the customs office's `Border office` has a generic job title and department that say nothing about customs work.
- Condition: the exporter's contact handles exports or customs; the consignee's contact, if any, receives or imports goods; the customs contact's job title and department fit a customs office.
- Options: (a) an export/customs contact for Valdara, an import or goods-in contact (or none) for Lumeway, a customs job title for the office (preferred); (b) drop job title and department where none fits.
- Needs decision: no
- From: broad (F7), parties (F6), context (F7)

### road/05#F10 · Low · Party master data the export declaration does nothing with
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: the exporter's stock-exchange listing, the carrier's haulage permit and the consignee's share capital play no part in declaring the export (section 4.8, IND5); the exporter is identified by its customs trader ID.
- Condition: every party detail has a use in declaring the export.
- Options: drop them (preferred).
- Needs decision: no
- From: parties (F5), context (F8)

### road/05#F11 · Low · Registration date 1996-01-01 looks like a default
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Trasvia carries 1 January 1996, a public holiday, the date found 271 times in 181 files for at least 25 companies (`grep -rho`/`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`). A filler (IND5).
- Condition: the carrier's `RegistrationDate` is its own plausible date, or absent.
- Options: (a) its own date (preferred); (b) leave it out.
- Needs decision: yes (company history; aligned with the rail and air merges)
- From: parties (F7)

### road/05#F12 · Low · Item number reads as a real GTIN-12
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- Why: valid GS1 mod-10 check digit (recomputed: 7), readable as a GTIN-12 of the GS1 US range; `771` is a GS1 prefix range (own knowledge). Fictional values must not be mistakable for real register entries.
- Condition: the item numbers cannot be read as validly check-digited GTINs of a real prefix.
- Options: (a) a non-GS1 structure or prefix 952 (preferred); (b) drop `IssuerScopeID`/`BarcodeSymbologyID`.
- Needs decision: yes (the world's item scheme; aligned with road/01, rail, plastics)
- From: broad (F9)

### road/05#F13 · Low · Product-passport data in a customs declaration
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:AdditionalItemProperty[5]/cbc:ValueQuantity` = `450`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: customs needs description, commodity code, origin, quantity, weight and value; keywords, warranty, the tested load, the circularity profile and the LCA emission are catalogue or product-passport data that nothing in the declaration refers to (section 4.8, IND5).
- Condition: the goods items carry what customs needs to identify, classify and value the goods, and no catalogue data without a use.
- Options: (a) drop keyword, warranty, item properties without customs relevance, circularity profile and emission (preferred); (b) keep a property only where the world's customs rules ask for it.
- Needs decision: no
- From: broad (F8), context (F9)

### road/05#F14 · Low · Exit office and border vehicle only described, not identified
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsExitOfficeLocation/cbc:Name` = `Customs post at the land border, Urvanian side`
- Why: an export is cleared against the office of exit; here the office is a free-text name without an identifier, and the declaration names the carrier but not the vehicle (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cac:RoadTransport/cbc:LicensePlateID` = `UR 4160 KT`). The same border post is only described again in `10-ImportCustomsDeclaration.xml` and `09-TransportationStatus.xml`, so the documents cannot be linked to one place.
- Condition: the exit office is identified (an office or location identifier used consistently in the flow); the border means of transport is stated if the world's customs procedure needs it.
- Options: (a) an ID for the exit office, the same in 09 and 10 (preferred); (b) add the means of transport to the declared shipment.
- Needs decision: no
- From: logistics (F3)

### road/05#F15 · Low · Border customs contact hours exclude the time the goods were at the border
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Name` = `Border office`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cac:Period/cbc:StartTime` = `07:30:00`
- XPath: `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExaminationTransportEvent/cbc:OccurrenceTime` = `07:45:00`
- Why: `Contact/Note` describes the circumstances under which the contact can be used; the border office is limited to weekdays 08:00–17:00, while the truck was at the land border from 07:30 on Tuesday 2026-03-24 and examined at 07:45, before those hours. A road border post is normally staffed around the clock (own knowledge). Contact hours are not necessarily office hours, which keeps this Low.
- Condition: the customs contact's stated hours cover the time the consignment was at the border, or the contact is one reachable then.
- Options: (a) hours that fit a road border post (e.g. 24 hours) (preferred); (b) move the border passage into the stated hours.
- Needs decision: no
- From: parties (F8)

### road/05#F16 · Low · Additional document reference by ID only
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `LD-PO-26-0149`
- Why: the reference names the buyer's purchase order (`01-Order.xml`) but carries no type code, type text or issue date, so customs cannot tell what it is; in a customs declaration an untyped supporting document would rather be read as an invoice or licence. The commercial invoice (`15-Invoice.xml`) is issued only the next day, 2026-03-24, so it could not be referenced here.
- Condition: the reference says what the referenced document is (type code or text), and refers to a document that exists when the declaration is issued.
- Options: (a) add `DocumentTypeCode` (purchase order) from the world's list (preferred: smallest change); (b) if customs needs the invoice, issue it before the declaration and refer to it.
- Needs decision: no
- From: broad (F10), logistics (F4), context (F10)

### road/05#F17 · Low · Signature ID built from the flow name
- XPath: `/ExportCustomsDeclaration/cac:Signature/cbc:ID` = `VI-SIG-EX-road`
- Why: `Signature/ID` is "An identifier for this signature"; `road` is the name of this repository's flow, meaningless to Valdara or customs, while other signatures of the flow follow the signer's numbering (e.g. `07-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:IssuerEndorsement/cac:Signature/cbc:ID` = `FCC-SIG-26-0309`). Counted with `grep -rhoE --include='*.xml' '<cbc:ID>[A-Z]+-SIG-[^<]*-[a-z]+<'`: 14 signature IDs end in a flow name. The signature also carries only an ID and a signatory, no method, time or attachment (context); the air merge treated such signatures as a convention (Low, needs decision); this finding is about the ID only.
- Condition: the signature ID follows the signer's own numbering, without repository or flow names.
- Options: (a) number it in Valdara's series, e.g. after the declaration ID (preferred); (b) drop the signature if the story has no signed declaration (the air merge's preference for unsigned signatures).
- Needs decision: no
- From: broad (F11), context (F11)

### road/05#F18 · Low · Italian street names and legal forms tagged as English
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Via dei Trasporti`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:StreetName[2]` = `Valico di Confine`
- Why: these renderings carry an English `languageID` but are Italian. Parties (and broad in 01) refuted this: English text keeps foreign street names as proper names, and the subtag follows the sender. Counter-argument: where a `qau` rendering already gives the local name, a second rendering tagged English has a reason only if it is English, and a legal-form text such as "Società urvaniana per azioni" is not a proper name. The merge cannot settle which rule the world follows; added from the parts' refutation, aligned with the rail merge and the merger of road 13–17 (217 renderings in 102 files tagged `en-XU`/`en-XB` start with Via/Viale/Piazza/Valico/Corso/Largo/Strada/Banchina, the rail merge's count).
- Condition: every rendering tagged as English is English, or the world's rule that place names and legal forms keep their source form under an English tag (and which region subtag an Urvanian address gets in a Bayvarran document) is documented.
- Options: (a) document the rule for street names and render legal forms in English (preferred: street names as proper names are common practice, legal forms are not); (b) tag the Italian renderings with a tag of their own language, if the world has one.
- Needs decision: yes
- From: merge (from the refutation of parties)

## Checked and consistent
- Goods items: 96 benches valued 4 790 400 XUF (= 96 × 49 900) and 12 side frames 71 760 XUF (= 12 × 5 980), equal to `15-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:LineExtensionAmount` = `4790400`; the exporter is the invoice's seller (`15-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-104274`), which supports the export exemption; the import side converts at 0.01 XBL per XUF (`10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `47904.00`) (broad, money, logistics, context).
- Weights: 3984 + 122.4 = 4106.4 kg = shipment gross weight in 04, 06, 07, 08 and 10; 41.5 kg gross per bench, 10.2 kg per boxed casting; with the waybill's net 3762 kg the tare is 344.4 kg for 25 pallets, 96 films (38.4 kg) and 12 boxes, about 12 kg per pallet (broad, logistics, context).
- Issued 2026-03-23 13:25, before the requested pickup (14:00), the pickup (15:05) and the departure, as the note "Declared electronically before the goods leave" and the order's despatch instruction say (broad, logistics, context).
- `FunctionCode` 9 (original), `VersionID` 1, validity 90 days from 2026-03-23; `ExportTypeCode` PERMANENT and `ExportReasonCode` SALE fit a sale (broad, context).
- Shipment CL-SH-26-0154, consignment LD-CS-26-0152 and carrier Trasvia agree with 03, 04 and 08; VI-CD-26-0156 is the number 08 and 10 quote (broad, logistics, context).
- HS 940179 and 732599 fit bench and cast side frame (broad).
- Customs trader IDs XU-TR-104274 and XB-TR-410274 used consistently in 05, 06, 07 and 10; GLN and ISIN check digits pass (parties).

## Considered and refuted
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ValidityPeriod/cbc:DurationMeasure` = `90`: validity on an export declaration — refuted: export declarations commonly set an exit period, and the definition is "A period, assigned by the issuer, during which the information in the declaration is valid" (from broad).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `4790400`: export value should be a frontier value — refuted: the declared value is the transaction value (FCA); a frontier value would be the statistical value, absent here (from money).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4` without transport equipment — refuted: the shipment has no transport equipment; the trailer belongs to the means of transport (from logistics, context).
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:ServiceProviderParty`: master data — refuted because it explains that the goods leave from Castrano's warehouse (from context); it does not make Castrano the declarant (F1).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PartyTaxScheme`: customs authority with a VAT registration — refuted because public bodies are commonly VAT-registered for their taxable activities (from parties).
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:Postbox` = `PB 18` with a street and type POSTAL — refuted: a postal address may carry both (from parties).
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:StreetName[2]`: Italian-looking name tagged `en-XU` — refuted: proper names, subtag follows the sender (from parties). Not followed in full by the merge, see F18.
- `/ExportCustomsDeclaration/cac:CustomsDeclaration/cac:ConsigneeParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: real GLN — refuted: prefix 952, check digit correct (from parties).
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:Contact/cbc:Telephone`: real numbers — refuted: +999 reserved (from parties).
- `/ExportCustomsDeclaration/cac:ExporterParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: contract number — refuted: the definition does not say who assigns it (from parties).
- Side frame `VI-C180` without the substituted casting's `ExtendedID` 2026 (a finding in road/04): considered by the merge — refuted for this document, because the HS code, origin and value of the casting are the same for both versions, so the declaration's purpose does not depend on the version (from merge).

## Changed in the merge
- broad/F1, logistics/F1 → F1: combined; the waybill's IssuerParty (broad) kept as a second contradiction; preferred option (a) from logistics (broad left it open).
- broad/F2, logistics/F2, context/F3 → F2: combined; context's Medium raised to High (arithmetic); preferred option drop factor and base.
- broad/F3, parties/F1, context/F4 → F3; broad/F4, parties/F2, context/F5 → F6 (parties' "Needs decision: yes" set to no); broad/F5, parties/F3 → F7: combined.
- context/F1 → F4: High lowered to Medium, aligned with road/01 and the rail merge.
- broad/F6, parties/F4, context/F6 → F8: combined.
- broad/F7, parties/F6, context/F7 → F9: combined (exporter, consignee and customs contacts).
- parties/F5, context/F8 → F10: combined.
- parties/F7 → F11: "Needs decision" set to yes (aligned with the rail and air merges).
- broad/F8, context/F9 → F13: combined.
- broad/F10, logistics/F4, context/F10 → F16: combined.
- broad/F11, context/F11 → F17: combined; context's "signature says what it is" kept as option (b) only, the condition is about the ID.
- F18: added by the merge from parties' refutation, aligned with the rail merge and the merger of road 13–17.

## Outside this review
- `08-Waybill.xml` names the customs administration as `IssuerParty` of the declaration; that element's error lies in 08 (its contradiction with this document is F1).
- `09-TransportationStatus.xml` and `10-ImportCustomsDeclaration.xml` describe the border post without an identifier; the link to this declaration's exit office is F14, the rest is theirs.
