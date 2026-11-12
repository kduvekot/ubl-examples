# LLM review: 06-CertificateOfOrigin.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/06-CertificateOfOrigin.xml`, Git blob `faaaba8b3816ead4cce39fdf9204e831ab65f4f7` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 3a48551 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/06#F1 · High · The application and the issued certificate share ID and version
- XPath: `/CertificateOfOrigin/cbc:ID` = `FCC-CO-26-0157`
- XPath: `/CertificateOfOrigin/cbc:VersionID` = `1`
- XPath: `/CertificateOfOrigin/cbc:UUID` = `a46337e2-176c-5866-9871-158007b21756`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:ApplicationStatusCode` = `SUBMITTED`
- XPath: `07-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:UUID` = `3152b116-509a-5a0d-8b57-97a8e2b066d0`
- XPath: `07-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:VersionID` = `1`
- XPath: `10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `FCC-CO-26-0157`
- Why: `ID` is "An identifier for this document, assigned by the sender" and `VersionID` "Identifies the version of this Certificate of Origin". This document is Valdara's submitted application (status SUBMITTED, issuer endorsement Pending, signed by Valdara, issued 2026-03-20); `07-CertificateOfOrigin.xml` is the chamber's approved and legalised certificate (issued 2026-03-22). Both carry ID FCC-CO-26-0157 and version 1 with different UUIDs and contents, so the import declaration's reference resolves to both (`flow_index.py` lists both). In addition the application's ID is in the chamber's numbering (FCC-CO-…), although its sender is Valdara and it has its own reference `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:ReferenceID` = `VI-AP-26-0158` (context). Refutation attempt in the merge: chambers do issue pre-numbered certificate forms that the exporter fills in (own knowledge), so the chamber's number on the application can be legitimate; but even then the two states of the document need different versions, and the reference in 10 stays ambiguous. Logistics had Low; the ambiguous reference is a broken reference (section 6), so High.
- Condition: the two documents can be told apart by their identifiers, and the reference in `10-ImportCustomsDeclaration.xml` resolves to exactly one of them (the issued certificate).
- Options: (a) give the application Valdara's own ID (e.g. derived from VI-AP-26-0158) and keep FCC-CO-26-0157 for the chamber's certificate (preferred by broad and context, and by the merger of 07–12; it also makes the ID the sender's); (b) keep the pre-assigned number and give 07 `VersionID` 2 (logistics), stating that the chamber pre-numbers its forms.
- Needs decision: no
- From: broad (F1), logistics (F4), context (F3)

### road/06#F2 · High · Emission factor × base does not give the emission value
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 per 1 EA gives 0.82 kg CO2e per bench, not 96; 96 / 0.82 = 117.1 matches nothing in the flow (recalculated in the merge). 39 examples, 9 in this flow.
- Condition: factor × (activity / base) equals the value, or factor and base are absent.
- Options: (a) drop factor and base (preferred, as road/01); (b) a factor and base whose product is 96 kg.
- Needs decision: no
- From: broad (F2), logistics (F1), context (F5)

### road/06#F3 · High · Second endorsement given while the first is still pending
- XPath: `/CertificateOfOrigin/cac:IssuerEndorsement/cbc:ApprovalStatus` = `Pending`
- XPath: `/CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cbc:SequenceNumeric` = `1`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cbc:ApprovalStatus` = `Endorsed`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cac:EndorserParty/cbc:SequenceNumeric` = `2`
- Why: `EndorserParty/SequenceNumeric` is "A number indicating the order of the endorsement provided by this party in the sequence in which endorsements are to be applied". The insurer's endorsement is number 2 and already given and signed ("The goods described in this certificate are insured door to door"), while number 1, the chamber's, is still pending: either the order is not the stated one, or the insurer endorsed a certificate that did not yet exist. Refutation attempt in the merge: an insurance endorsement does not depend on the chamber's approval in substance, but the document itself states the order in which the endorsements are to be applied, and the statuses contradict it. Parties had Low; a contradiction between values of the same document is High (section 6).
- Condition: no endorsement with a higher sequence number is given while one with a lower number is pending; or the numbers reflect the order in which the endorsements are actually given.
- Options: (a) drop the insurance endorsement from the application (preferred by context; goes together with F22, where the endorsement has no role in the flow); (b) number the insurer 1 and the chamber 2 if the insurer endorses before submission (parties' preference, consistent with 07 only if 07 is renumbered too).
- Needs decision: no
- From: parties (F8), context (F1)

### road/06#F4 · Medium · Urvanian province in Region instead of CountrySubentity
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is `CountrySubentity`, which the Bayvarran address of the same document uses (`/CertificateOfOrigin/cac:ImporterParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 files.
- Condition: the province is in `CountrySubentity`; `Region` is absent or a real region.
- Options: (a) move it to `CountrySubentity` (preferred); (b) define Urvanian provinces as non-administrative regions.
- Needs decision: no
- From: broad (F3), parties (F1), context (F6)

### road/06#F5 · Medium · LocaleCode holds a language code
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (ISO 639) repeats `Language/ID`. 362 occurrences in 213 files.
- Condition: absent, or a locale from a list of locales.
- Options: (a) drop it (preferred; broad, parties, rail and air merges); (b) `en-XB` with a locale list (context).
- Needs decision: no
- From: broad (F4), parties (F2), context (F7)

### road/06#F6 · Medium · Gate number in AdditionalStreetName of the importer's address
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; `Gate 3` is an entrance, not a street. 79 occurrences in 76 files.
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance.
- Options: (a) drop it from the address (preferred).
- Needs decision: no
- From: broad (F5), parties (F3)

### road/06#F7 · Medium · The buyer's order number given as the application's job number
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:OriginalJobID` = `LD-PO-26-0149`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:SupportingDocumentReference/cbc:ID` = `LD-PO-26-0149`
- Why: `OriginalJobID` is "The latest job number given to the CoO application. This is used by the system to keep track of amendments to or cancellation of any earlier applications." The value is Lumeway's purchase order number (`01-Order.xml:/Order/cbc:ID` = `LD-PO-26-0149`), an identifier of another kind and issuer, which the application also cites as supporting document; it cannot track the application's amendments. Verified in the merge: the same value stands in 07.
- Condition: `OriginalJobID` holds a job number of this application in the applicant's or the chamber's numbering, the same in 06 and 07; the order stays in `SupportingDocumentReference`.
- Options: (a) the application's own job number, e.g. derived from `ReferenceID` VI-AP-26-0158 (preferred); (b) the chamber's job number, if it assigns one.
- Needs decision: no
- From: broad (F6), logistics (F2), context (F8)

### road/06#F8 · Medium · Lifecycle stage code says manufacturing only, its text says cradle to gate
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- Why: `MANUFACTURING` is "Making the product (EN 15804 module A3)" in the world list, while text and description cover A1–A3.
- Condition: code and text name the same stage(s).
- Options: (a) omit the code and keep the text (preferred); (b) reduce figure and texts to A3.
- Needs decision: no
- From: context (F2)

### road/06#F9 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: the element is "A code signifying whether a piece of transport equipment is full, partially full, or empty ..."; `CRADLETOGATE` is from the world list `EmissionBoundaryCode` (semantic conformance, §4.7). 39 examples do the same.
- Condition: absent from this item emission, or saying how full transport equipment is.
- Options: (a) drop it, state the boundary in text, record the missing element for the UBL TC write-up (preferred).
- Needs decision: no
- From: context (F4)

### road/06#F10 · Low · Signature IDs built from the example number and the aggregate name
- XPath: `/CertificateOfOrigin/cac:Signature/cbc:ID` = `VI-SIG-CO-06`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Signature/cbc:ID` = `VI-SIG-COA`
- Why: `Signature/ID` is "An identifier for this signature". `06` is this example's file number (the issued certificate has `07-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:Signature/cbc:ID` = `FCC-SIG-CO-07`) and `COA` the name of the aggregate; neither is a number Valdara would assign, while other signatures follow the signer's series (`07-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:IssuerEndorsement/cac:Signature/cbc:ID` = `FCC-SIG-26-0309`). 17 signature IDs end in a two-digit number and 14 in a flow name (`grep -rhoE --include='*.xml' '<cbc:ID>[A-Z]+-SIG-[^<]*-[0-9]{2}<'`, and `-[a-z]+<`; the first pattern also matches running numbers, so 17 is an upper bound). The signatures carry no method, time or value (context; the air merge's "signature without signature" convention).
- Condition: signature IDs follow the signer's own numbering, without file numbers, flow or aggregate names.
- Options: (a) number them in Valdara's series, e.g. after VI-AP-26-0158 (preferred); (b) drop the document-level signature, since the application already carries the applicant's.
- Needs decision: no
- From: broad (F7), context (F15)

### road/06#F11 · Low · Contacts that do not fit a certificate of origin
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:Contact/cbc:JobTitle` = `Public service officer`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:Contact/cbc:Department` = `Public services`
- Why: the chamber asks the exporter's export or customs function about origin, not the order desk in Sales; the importer's contact for a certificate it uses at import is its import function, not its own customer service; the chamber's `Certificates office` carries a generic job title and department.
- Condition: exporter's and importer's contacts handle export/import formalities; the chamber's contact's job title and department fit certification.
- Options: (a) export, import and certification contacts (preferred); (b) drop job title and department where none fits.
- Needs decision: no
- From: broad (F8), parties (F5), context (F11)

### road/06#F12 · Low · Exporter's stock-exchange listing in a certificate of origin
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: the listing of Valdara's shares plays no part in stating or establishing origin (section 4.8, IND5).
- Condition: every party detail in the certificate has a use for origin.
- Options: drop it (preferred).
- Needs decision: no
- From: parties (F4), context (F12 in part)

### road/06#F13 · Low · Italian street names and legal form tagged as English
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- Why: these renderings carry `languageID` `en-XU` next to an Urvanian (`qau`) rendering, but are Italian. Parties refuted this: English text keeps foreign street names as proper names, and the subtag follows the sender. Counter-argument: the `qau` rendering already gives the local name, so a second rendering tagged English has a reason only if it is English; a legal-form text "Società urvaniana per azioni" is not a proper name. The merge cannot settle which rule the world follows; added from the parts' refutation, aligned with the rail merge and the merger of road 13–17 (217 renderings in 102 files tagged `en-XU`/`en-XB` start with Via/Viale/Piazza/Valico/Corso/Largo/Strada/Banchina, rail merge's count).
- Condition: every rendering tagged as English is English, or the world's rule that place names and legal forms stay in their source form under an English tag is documented.
- Options: (a) document the rule and render legal forms in English only (preferred: street names as proper names are common practice, legal forms are not); (b) tag the Italian renderings with an Italian-like tag, if the world has one.
- Needs decision: yes
- From: merge (from parties' refutation)

### road/06#F14 · Low · Chamber of commerce described as a company in the commercial register
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the Ferrano Chamber of Commerce (ISIC 9411, membership organisation) issues certificates of origin, a public function, yet is described as entered in the commercial register with a liquidation status. In many countries chambers are public-law bodies (own knowledge); whether Urvanian chambers are, the examples do not say. Unlike the customs administration (road/05 F8, Medium), the chamber's legal nature is open.
- Condition: the chamber's legal entity matches what it is in the world (public-law body without commercial registration and liquidation status, or a private entity registered as such, with a legal form).
- Options: (a) decide the chamber's legal nature; if public-law, drop commercial registration and liquidation status (preferred); (b) if private, keep it and give it a legal form.
- Needs decision: yes
- From: broad (F9), parties (F6)

### road/06#F15 · Low · Endorser's signatory contact against a definition for the exporter's signer
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- XPath: `/CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Cargo claims desk`
- Why: UBL 2.5 defines `EndorserParty/SignatoryContact` as "The individual representing the exporter who signs the Certificate of Origin application before submitting it to the issuer party". The examples use it for the endorser's own signing office. Broad refuted this as a defect of the UBL definition (the element is mandatory in `EndorserParty`, the definition copied from the application's context), not of the example; under the semantic-conformance rule the use still differs from the definition, so it is recorded here and for the TC write-up (context).
- Condition: either the use follows the definition, or the difference is recorded as a UBL finding and the examples keep the endorser's signer deliberately.
- Options: (a) record it for the UBL TC write-up and keep the endorser's signer (preferred: an endorser's signatory is what the aggregate needs, and the element is mandatory); (b) none that drops it, since the element is mandatory.
- Needs decision: yes
- From: context (F10)

### road/06#F16 · Low · Endorsement signatories are desks, not individuals
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Cargo claims desk`
- Why: whatever the definition (F15), a signatory is the individual or signing function who signs; `Certificates office` and `Cargo claims desk` are desks, and a claims desk handles claims, not endorsements (broad, F22).
- Condition: each `SignatoryContact` identifies the individual or at least the signing function (e.g. by `JobTitle`).
- Options: (a) give the signatory contacts a signing function (certificates officer, underwriter) while keeping names functional if the world avoids personal names (preferred); (b) named fictional persons.
- Needs decision: no
- From: parties (F7)

### road/06#F17 · Low · Previous job ID for a first application
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:PreviousJobID` = `VI-CO-25-0412`
- Why: `PreviousJobID` is "An identifier for the previous job used in case the application requires query or change". This is a first application, with no query or change, and the 2025 number appears only in the two certificates of origin (`grep -rl --include='*.xml' VI-CO-25-0412`: 06 and 07); nothing explains it (IND5).
- Condition: `PreviousJobID` is present only if the application changes or queries an earlier, identifiable job.
- Options: (a) remove it (preferred); (b) if an earlier certificate for the same benches supports this one, refer to it as a typed supporting document.
- Needs decision: no
- From: broad (F10), logistics (F3), context (F9)

### road/06#F18 · Low · Customs values on a certificate that grants origin by processing
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `4790400`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `71760`
- Why: `DeclaredCustomsValueAmount` is "The total declared value for customs purposes of the goods item". The origin rule stated is a processing rule (`/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:Remarks` = `Benches made of Urvanian steel and Bayvarran timber; the processing in Urvania gives origin.`), not a value rule, so neither the chamber nor import customs needs the value from this document; the import declaration carries its own (`10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `47904.00`). Preferential certificates (EUR.1, Form A) carry no value unless a value criterion applies; some chambers charge fees by value, which would be a reason the example does not state (own knowledge). Broad checked the values as consistent with 05 (they are).
- Condition: the goods items carry no customs value, or the example gives the reason the chamber needs it.
- Options: (a) remove the two amounts (preferred); (b) keep them and state the reason (e.g. a value-content criterion of the Trade Accord).
- Needs decision: yes (whether a value criterion exists in the world)
- From: money (F1)

### road/06#F19 · Low · Item number reads as a real GTIN-12
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- Why: valid GS1 mod-10 check digit (recomputed: 7), readable as a GTIN-12 of the GS1 US range; `771` is a GS1 prefix range (own knowledge).
- Condition: the item numbers cannot be read as validly check-digited GTINs of a real prefix.
- Options: (a) a non-GS1 structure or prefix 952 (preferred); (b) drop `IssuerScopeID`/`BarcodeSymbologyID`.
- Needs decision: yes (the world's item scheme; aligned with road/01, rail, plastics)
- From: broad (F12)

### road/06#F20 · Low · Product-passport data in a certificate of origin
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:AdditionalItemProperty[5]`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: a certificate of origin needs description, classification, quantity and origin and the facts that confer origin (the remarks). Keywords, warranty, the load test, the LCA emission and the circularity profile play no part in it (section 4.8, IND5). The resource consumption with its origins could support the origin claim, but nothing in the certificate refers to it (context).
- Condition: item data in the certificate have a use for establishing or stating origin.
- Options: (a) drop keyword, warranty, properties, emission and the circularity profile apart from what the remarks rely on (preferred); (b) keep the resource consumption only if the remarks or the endorsement refer to it.
- Needs decision: no
- From: broad (F11), context (F12 in part)

### road/06#F21 · Low · Supporting document referred to by ID only
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:SupportingDocumentReference/cbc:ID` = `LD-PO-26-0149`
- Why: the reference carries no type, description or date, so the chamber cannot tell it is the buyer's order rather than an invoice or production record; origin is normally supported by the invoice and production records (the issued certificate says "Origin verified against the exporter's production records").
- Condition: the reference says what the referenced document is, and refers to a document that supports origin.
- Options: (a) add a document type (purchase order) (preferred: smallest change); (b) refer to production records or the invoice instead.
- Needs decision: no
- From: broad (F13), context (F13)

### road/06#F22 · Low · Insurance endorsement without a role in the flow, numbered after a sea-flow policy
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cbc:DocumentID` = `WS-CP-26-4471-E1`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cbc:Remarks` = `The goods described in this certificate are insured door to door.`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cac:EndorserParty/cac:Party/cac:PartyName/cbc:Name` = `Wavesure Cargo Insurance`
- Why: nothing in the road flow uses insurance: no policy in the waybill, no insured value, and under FCA (`01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FCA`) the buyer's risk begins at the Ferrano warehouse, so "door to door" says more than the buyer's cover needs. The endorsement's ID is built on the policy of the sea flow, `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:ID` = `WS-CP-26-4471`, which insures a different consignment (beneficiary `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Velumi Trading`). In this flow only 06 and 07 mention the policy (`grep -rl --include='*.xml' WS-CP-26-4471`: road/06, road/07 and sea/14, 19, 26). Whether an open cover of Lumeway is meant cannot be settled.
- Condition: the certificate carries an insurance endorsement only if the road shipment is insured under a policy the flow names, with remarks that fit the delivery terms.
- Options: (a) remove the insurance endorsement (preferred; also resolves F3); (b) make WS-CP-26-4471 an open cover of Lumeway that also covers this shipment and name it in the waybill.
- Needs decision: yes
- From: broad (F14), context (F14)

## Checked and consistent
- Goods items (96 benches, 12 side frames), values 4 790 400 and 71 760 XUF (= the invoice line amounts, `15-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:LineExtensionAmount` = `4790400`), gross 3984 and 122.4 kg and shipment CL-SH-26-0154 agree with `05-ExportCustomsDeclaration.xml` and `10-ImportCustomsDeclaration.xml` (broad, money, logistics, context).
- `CertificateType` Preferential, the note on preferential origin under the trade accord and the remarks agree with origin XU on both items and with the item origins in 01 and 04 (broad, logistics, context).
- Roles: preparation party and exporter Valdara, importer Lumeway, issuer and first endorser the chamber; electronic copy to the importer, who uses it in 10 (broad, parties, context).
- Application status SUBMITTED with the chamber's endorsement Pending is consistent for an application before approval; the exporter signs at this stage (broad, parties).
- Issued Friday 2026-03-20, before the despatch on 2026-03-23 (context).
- GLN and ISIN check digits pass; party identity agrees across the flow apart from the region subtag (parties).

## Considered and refuted
- `/CertificateOfOrigin/cac:IssuerEndorsement/cbc:DocumentID` = `FCC-CO-26-0157`: the endorsement's ID equal to the certificate number — refuted: the chamber's endorsement is identified by the certificate number it stamps (from broad).
- `/CertificateOfOrigin/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office` against a definition for the exporter's signer — refuted by broad as a UBL model defect; not followed by the merge, see F15.
- `/CertificateOfOrigin/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Valdara Industries`: certificate signed by the exporter — refuted because this is the application stage (from parties).
- `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cbc:ID`: the 3PL's shipment ID before the despatch advice that first reports it — refuted: a shipment number is reserved when the shipment is planned (from logistics).
- `/CertificateOfOrigin/cac:ExporterParty/cac:ServiceProviderParty`: master data — refuted because it explains that the goods leave from Castrano's warehouse, which the chamber may inspect (from context).
- Endorser party at document level and in the application (`/CertificateOfOrigin/cac:EndorserParty`, `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:EndorserParty`) — refuted: UBL has both and both describe the chamber consistently (from context).
- `/CertificateOfOrigin/cac:ExporterParty/cac:PostalAddress/cbc:StreetName[2]`: Italian name tagged `en-XU` — refuted by parties (proper names, subtag follows the sender); not followed in full by the merge, see F13.
- `/CertificateOfOrigin/cac:ImporterParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: real GLN — refuted: prefix 952, check digit correct (from parties).
- `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:Telephone`: real numbers — refuted: +999 reserved (from parties).
- `/CertificateOfOrigin/cac:ExporterParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: contract number — refuted: the definition does not say who assigns it (from parties).
- Side frame without the substituted casting's `ExtendedID` 2026 (a finding in road/04): considered by the merge — refuted for this document, because origin, HS code and value are the same for both castings (from merge).

## Changed in the merge
- broad/F1, logistics/F4, context/F3 → F1: combined; logistics' Low raised to High (reference resolving to two documents); context's "Needs decision: yes" set to no (both options are encoding); preferred option (a) separate IDs, aligned with the merger of road 07–12; the pre-numbered-forms argument added as refutation attempt.
- broad/F2, logistics/F1, context/F5 → F2: combined; context's Medium raised to High; preferred option drop factor and base.
- parties/F8, context/F1 → F3: combined; parties' Low raised to High (contradiction within the document); preferred option tied to F22.
- broad/F3, parties/F1, context/F6 → F4; broad/F4, parties/F2, context/F7 → F5 (parties' "yes" set to no); broad/F5, parties/F3 → F6: combined.
- broad/F6, logistics/F2, context/F8 → F7: combined.
- context/F2 → F8: High lowered to Medium, aligned with road/01 and the rail merge.
- broad/F7, context/F15 → F10: combined.
- broad/F8, parties/F5, context/F11 → F11: combined, including the chamber's contact (broad).
- parties/F4 and the listing in context/F12 → F12; the item part of context/F12 with broad/F11 → F20: split into party master data and item data, as the rail merge does.
- F13: added by the merge from parties' refutation, aligned with the rail merge and the merger of road 13–17.
- broad/F9, parties/F6 → F14: combined.
- context/F10 → F15 (broad's refutation carried as argument); parties/F7 → F16: kept separate (different conditions).
- broad/F10, logistics/F3, context/F9 → F17; broad/F13, context/F13 → F21; broad/F14, context/F14 → F22: combined.

## Outside this review
- `07-CertificateOfOrigin.xml` gives both the embassy's legalisation and the insurer's endorsement `SequenceNumeric` 2; a problem of 07.
- `07-CertificateOfOrigin.xml` repeats `OriginalJobID` LD-PO-26-0149 and `PreviousJobID` VI-CO-25-0412; their review covers them.
