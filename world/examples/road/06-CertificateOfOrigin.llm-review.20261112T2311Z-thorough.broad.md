# LLM review: 06-CertificateOfOrigin.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/06-CertificateOfOrigin.xml`, Git blob `faaaba8b3816ead4cce39fdf9204e831ab65f4f7` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 60500a8 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/06#F1 · High · Two different certificate documents with the same ID and version
- XPath: `/CertificateOfOrigin/cbc:ID` = `FCC-CO-26-0157`
- XPath: `/CertificateOfOrigin/cbc:VersionID` = `1`
- XPath: `/CertificateOfOrigin/cbc:UUID` = `a46337e2-176c-5866-9871-158007b21756`
- XPath: `/CertificateOfOrigin/cbc:IssueDate` = `2026-03-20`
- XPath: `07-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:UUID` = `3152b116-509a-5a0d-8b57-97a8e2b066d0`
- XPath: `07-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:IssueDate` = `2026-03-22`
- Why: `ID` is "An identifier for this document, assigned by the sender" and `VersionID` "Identifies the version of this Certificate of Origin". `06-CertificateOfOrigin.xml` (the exporter's application, status SUBMITTED, endorsement Pending, issued 2026-03-20 and signed by Valdara) and `07-CertificateOfOrigin.xml` (the chamber's approved and legalised certificate, issued 2026-03-22) are two different documents with different UUIDs and senders, yet both carry ID FCC-CO-26-0157 and version 1. The application carries the chamber's certificate number before the chamber has approved anything, although the application has its own reference (`ReferenceID` VI-AP-26-0158). The import declaration's reference to FCC-CO-26-0157 (`10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID`) therefore resolves to both documents (`flow_index.py` lists both).
- Condition: Each of the two documents has its own document ID, or they share the ID with different version numbers that make clear which is the issued certificate; the reference in the import declaration resolves to exactly one of them.
- Options: (a, preferred) give the application the exporter's own number (e.g. derived from VI-AP-26-0158) and keep FCC-CO-26-0157 for the chamber's certificate; (b) keep the shared ID and number the versions (1 = application, 2 = approved certificate).
- Needs decision: no

### road/06#F2 · High · Emission value is not factor × base
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: UBL defines `ValueFactorNumeric` as "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` as "The base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". With a factor of 0.82 per 1 EA the calculated value is 0.82, not the stated 96 kg CO2e (`ValueMeasure`, "total emissions in kg CO2"). The factor does not fit any quantity in the item either (34 kg steel and 22.5 kg hardwood consumed per bench: 0.82 × 56.5 kg = 46.3 kg, 0.82 × 34 kg = 27.9 kg). The same block occurs in 39 examples across flows (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82' world/examples | wc -l`).
- Condition: `ValueFactorNumeric` × `ValueBaseMeasure` equals `ValueMeasure` (in consistent units), or the factor and base are absent.
- Options: (a, preferred) give the factor and base the 96 kg are actually calculated from (e.g. kg CO2e per kg of material with the bench's mass as base), so the arithmetic holds; (b) remove `ValueFactorNumeric` and `ValueBaseMeasure` and keep only the total, if no factor is known.
- Needs decision: no

### road/06#F3 · Medium · Province in Region instead of CountrySubentity
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative subdivision of the country, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located", with `CountrySubentityCode`). The Bayvarran addresses of the same examples do use `CountrySubentity` (`Upland State`), so the two countries' addresses are structured differently for the same kind of information. Counted over `*.xml`: 104 examples carry `<cbc:Region>Province of …` (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: No address of this example holds a province in `Region`; the province is in `CountrySubentity` (and, where a list exists, `CountrySubentityCode`).
- Options: (a, preferred) move the value to `CountrySubentity`, with a code from the Urvanian subdivision list if one exists, like the Bayvarran addresses; (b) keep `Region` only if Urvania's provinces are defined as economic regions rather than administrative divisions, and say so in the world's address rules.
- Needs decision: no

### road/06#F4 · Medium · Language code in LocaleCode
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is defined as "A code signifying the locale in which this language is used"; a locale is a combination of language and region (e.g. en-XB), not a language. The value repeats the ISO 639 language code of `Language/ID` (listID `ISO 639`), so the element carries a language, not a locale, and adds nothing to `Language/ID`. The same pattern occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: `LocaleCode` is either absent or holds a locale (language and region) from a locale list named in its listID, different in meaning from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`, since `Language/ID` already says English and nothing in the document needs the region; (b) give a real locale such as en-XB with a locale list as listID, if the region matters to the party.
- Needs decision: no

### road/06#F5 · Medium · Gate number in AdditionalStreetName of the postal address
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is not a street name but an entrance of the business park, information that matters only to vehicles delivering goods, and it is carried in Lumeway's postal/registered address in every document. The road flow itself mentions other entrances (`Gate B` as alternative delivery location and `dock 4` in the Order and Waybill), so the gate is a delivery instruction, not part of the address. Counted over `*.xml`: 76 examples (`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: `AdditionalStreetName` holds no gate, dock or entrance; such information, where needed, is in a delivery location or delivery instruction.
- Options: (a, preferred) remove `Gate 3` from the party address and, where the document is about delivery, put the gate in `Delivery/DeliveryLocation` or the delivery instructions; (b) keep it only in a delivery address with a dedicated element such as `Location/Description`.
- Needs decision: no

### road/06#F6 · Medium · Buyer's purchase order number used as the job number of the application
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:OriginalJobID` = `LD-PO-26-0149`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:SupportingDocumentReference/cbc:ID` = `LD-PO-26-0149`
- Why: `OriginalJobID` is "The latest job number given to the CoO application. This is used by the system to keep track of amendments to or cancellation of any earlier applications." It is a number of the application procedure, assigned in the issuing system. The value is Lumeway's purchase order number (`01-Order.xml:/Order/cbc:ID` = `LD-PO-26-0149`), an identifier of another kind and issuer, which the application also cites correctly as a supporting document.
- Condition: `OriginalJobID` holds a job number of the certificate application procedure (exporter's or chamber's numbering), not the purchase order number.
- Options: (a, preferred) use the application's own job number (e.g. the chamber's job number or VI-AP-26-0158); (b) leave the order only in `SupportingDocumentReference`.
- Needs decision: no

### road/06#F7 · Low · Signature ID made from the example number or flow name
- XPath: `/CertificateOfOrigin/cac:Signature/cbc:ID` = `VI-SIG-CO-06`
- Why: `Signature/ID` is "An identifier for this signature". The value `VI-SIG-CO-06` is built from the example's place in the collection (the example number or the flow name), not from a numbering the signing party would use; the other signature IDs of the flow follow the party's own document numbering (e.g. `FCC-SIG-26-0309`, `LTAC-SIG-26-0311`, `XB-CUS-SIG-0884`). An identifier that reveals the example structure is out of the world's story.
- Condition: The signature ID follows the signing party's own numbering and contains no example number or flow name.
- Options: (a, preferred) number the signature like the party's other signatures (prefix, year, running number); (b) derive it from the document ID.
- Needs decision: no

### road/06#F8 · Low · Contacts that do not fit the role
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:Contact/cbc:Name` = `Certificates office`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:Contact/cbc:Department` = `Public services`
- Why: The exporter's contact for an origin certificate is Valdara's `Order desk` in `Sales`, the importer's is Lumeway's `Customer service` desk in `Sales`; neither handles origin or customs matters. The chamber's `Certificates office` has the generic job title `Public service officer` in `Public services`.
- Condition: The contacts handle the certificate's subject (export/import formalities, certification) and their job titles and departments fit.
- Options: (a, preferred) give the parties export, import and certification contacts; (b) omit JobTitle/Department.
- Needs decision: no

### road/06#F9 · Low · Chamber of commerce described as a commercially registered company
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: The Ferrano Chamber of Commerce issues certificates of origin, a public function; in many countries chambers are public-law bodies (own knowledge). It is described as entered in the commercial register (COMMERCIAL) with a liquidation status, like a company. Whether chambers in Urvania are public-law bodies is a question of the world's story.
- Condition: The chamber's legal entity matches its legal nature in the world (public-law body or registered association/company), and a liquidation status appears only if it applies.
- Options: (a, preferred) decide the chamber's legal form in the world and describe it accordingly; (b) remove the commercial registration and liquidation status.
- Needs decision: yes

### road/06#F10 · Low · Previous job ID for a first application
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:PreviousJobID` = `VI-CO-25-0412`
- Why: `PreviousJobID` is "An identifier for the previous job used in case the application requires query or change". This is a first application for a new shipment, not a query or change; VI-CO-25-0412 (a 2025 job of Valdara) has no relation to it in any document of the flow (IND5: no filler).
- Condition: `PreviousJobID` is present only if the application changes or queries an earlier job, and that job is related to this shipment.
- Options: (a, preferred) remove `PreviousJobID`; (b) make the application an amendment of a named earlier application, if the story wants it.
- Needs decision: no

### road/06#F11 · Low · Item master data copied into a document that does not use it
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:AdditionalItemProperty[5]`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile`
- Why: A certificate of origin needs the goods description, classification, origin, quantity, value and weight. The bench is carried with its warranty, load test, colour property group, dimensions, cradle-to-gate emissions, resource consumption, waste and repairability score. None of this is used by the document's purpose (section 4.8: data copied from master data into a document that does not use it).
- Condition: The item in this document carries what its purpose needs; environmental, circularity, warranty and test data are absent unless the document uses them.
- Options: (a, preferred) reduce the item to description, name, identifiers, origin and commodity classification; (b) keep single properties that the authority actually checks and say why.
- Needs decision: no

### road/06#F12 · Low · Item number looks like a real GTIN-12 with issuer scope 771
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- Why: The standard item numbers 771020000027 and 771020000034 (scheme `urn:ubl-examples:world:item`) are 12 digits with a valid GS1 mod-10 check digit (computed: 7 and 4), so any scanner or GS1 check reads them as GTIN-12s; a GTIN-12 starting with 7 lies in the UPC range administered by GS1 US, and the issuer scope `771` is also a GS1 prefix (GS1 Colombia, 770–771). This rests on my knowledge of the GS1 prefix allocation. The rule that fictional values must not be mistakable for real register entries applies. In addition, only the bench carries `BarcodeSymbologyID` and `IssuerScopeID`; the side frame's number from the same scheme carries neither.
- Condition: The item numbers cannot be read as validly check-digited GTINs of a real GS1 prefix, and both items of the same scheme are described the same way.
- Options: (a, preferred) confirm against the world's identifier rules whether the world item scheme is meant to mimic GTIN; if so, use a GS1 prefix reserved for demonstration or a non-GS1 structure; (b) drop `IssuerScopeID`/`BarcodeSymbologyID` where they have no role in the document.
- Needs decision: yes

### road/06#F13 · Low · Document reference with only an ID
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:SupportingDocumentReference/cbc:ID` = `LD-PO-26-0149`
- Why: A document reference that carries only an ID must say what it refers to where that is not obvious (no `DocumentTypeCode` or `DocumentType`, no issue date). LD-PO-26-0149 is the buyer's purchase order; a chamber reading the application cannot tell from the reference that it is an order rather than an invoice or production record.
- Condition: The reference states the kind of document it refers to (type code or type text).
- Options: (a, preferred) add `DocumentTypeCode` from the world's document type list (as the remittance advice does); (b) add `DocumentType` as text.
- Needs decision: no

### road/06#F14 · Low · Insurance endorsement on a certificate of origin, numbered after a sea-flow policy
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cbc:DocumentID` = `WS-CP-26-4471-E1`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cbc:Remarks` = `The goods described in this certificate are insured door to door.`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cac:EndorserParty/cac:Party/cac:PartyName/cbc:Name` = `Wavesure Cargo Insurance`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Cargo claims desk`
- Why: A certificate of origin certifies origin; nothing in the road flow uses insurance (no insurance policy in the waybill, the Incoterm FCA leaves insurance to the buyer, and no insured value appears). The endorsement's ID WS-CP-26-4471-E1 is built on the policy of the sea flow, `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:ID` = `WS-CP-26-4471`, which insures a different consignment for Lumeway with the beneficiary `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Velumi Trading` and an insured value of `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80` XBL, two months later. The insurer signs through its `Cargo claims desk`, which handles claims, not endorsements. Whether an open cover of Lumeway's is meant cannot be settled from the examples.
- Condition: The certificate carries an insurance endorsement only if the road shipment is insured under a policy that the flow names, and the endorsement's ID refers to that policy.
- Options: (a, preferred) remove the insurance endorsement; (b) make WS-CP-26-4471 an open cover of Lumeway that also covers this shipment, and state the policy in the waybill.
- Needs decision: yes

## Checked and consistent
- Goods items (96 benches, 12 side frames), customs values, gross weights and shipment ID CL-SH-26-0154 agree with `05-ExportCustomsDeclaration.xml`.
- `CertificateType` Preferential and the note on preferential origin under the trade accord agree with the remark that Urvanian processing of Urvanian steel and Bayvarran timber gives origin; the item's resource origins say the same.
- Roles: preparation party and exporter Valdara, importer Lumeway, issuer and first endorser the Ferrano Chamber of Commerce; distribution of an electronic copy to the importer.
- Status of the application: `ApplicationStatusCode` SUBMITTED and issuer endorsement `Pending`, consistent with an application before approval; endorsement sequence chamber 1, insurer 2.

## Considered and refuted
- `/CertificateOfOrigin/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`: the UBL definition of `SignatoryContact` is "The individual representing the exporter who signs the Certificate of Origin application before submitting it to the issuer party", which does not fit an endorser — refuted as a finding of this example: the element is mandatory in `EndorserParty` and the definition is copied from the application's context; this is a defect of the UBL model's definition (a candidate for the findings write-up), not of the example.
- `/CertificateOfOrigin/cac:IssuerEndorsement/cbc:DocumentID` = `FCC-CO-26-0157`: the endorsement's ID equal to the certificate number looked like a reuse — refuted: the chamber's endorsement is identified by the certificate number it stamps.
