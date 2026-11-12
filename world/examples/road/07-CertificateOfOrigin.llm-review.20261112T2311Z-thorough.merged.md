# LLM review: 07-CertificateOfOrigin.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/07-CertificateOfOrigin.xml`, Git blob `9dd12c4b7afb7cb32c342c0e094823576afb0a28` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 3a48551 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/07#F1 · High · Application and issued certificate are two documents with the same ID and version
- XPath: `/CertificateOfOrigin/cbc:ID` = `FCC-CO-26-0157`
- XPath: `/CertificateOfOrigin/cbc:VersionID` = `1`
- XPath: `/CertificateOfOrigin/cbc:UUID` = `3152b116-509a-5a0d-8b57-97a8e2b066d0`
- XPath: `/CertificateOfOrigin/cbc:IssueDate` = `2026-03-22`
- XPath: `06-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:ID` = `FCC-CO-26-0157`
- XPath: `06-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:VersionID` = `1`
- XPath: `06-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:UUID` = `a46337e2-176c-5866-9871-158007b21756`
- XPath: `06-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:IssueDate` = `2026-03-20`
- XPath: `10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `FCC-CO-26-0157`
- Why: `ID` is "An identifier for this document, assigned by the sender" and `VersionID` "Identifies the version of this Certificate of Origin". `06-CertificateOfOrigin.xml` (the exporter's application, `ApplicationStatusCode` SUBMITTED, issuer endorsement `Pending`, signed by Valdara, 2026-03-20) and this example (approved, endorsed and legalised by the chamber and the accord council, 2026-03-22) have different content, UUIDs, issue dates and signers, yet the same ID and the same version 1. The application already carries the chamber's certificate number although its own sender is Valdara and it has its own reference (`/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:ReferenceID` = `VI-AP-26-0158`). The import declaration's reference to `FCC-CO-26-0157` therefore resolves to both documents (`flow_index.py` lists both). Merge check: the refutation "the same certificate goes back and forth through the workflow" fails, because the same ID with the same version cannot then hold two contents.
- Condition: the two documents can be told apart by ID or by version, and the reference in the import declaration resolves to the issued certificate only.
- Options: (a, preferred, aligned with merger A for 06) keep the shared ID, which the chamber may well pre-assign to the application form, and give this approved certificate version 2, with the import declaration citing the version or issue date; (b) give the application its own ID (e.g. from VI-AP-26-0158) and keep `FCC-CO-26-0157` version 1 for the certificate (broad's and context's preference).
- Needs decision: no
- From: broad (F1, High), context (F3, Medium), logistics (F4, Low)

### road/07#F2 · High · Emission value is not factor × base
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". 0.82 per 1 EA gives 0.82 kg CO2e per bench, not 96. Recalculated in the merge: 96 / 0.82 = 117.1, which matches no quantity of the flow; 0.82 × 56.5 kg of material (34 kg steel + 22.5 kg hardwood, `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile/cac:ResourceConsumption[1]/cbc:ConsumptionMeasure` = `34`) = 46.3 kg, 0.82 × 34 = 27.9 kg. The same triple occurs in 39 examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: `ValueFactorNumeric` × the activity quantity in the unit of `ValueBaseMeasure` equals `ValueMeasure`, or factor and base are absent.
- Options: (a, preferred, as in rail and air) drop factor and base, the value being a per-item LCA figure; (b) state the factor and base the 96 kg are actually calculated from (e.g. per kg of steel, base in KGM).
- Needs decision: no
- From: broad (F2, High), logistics (F1, High), context (F5, Medium)

### road/07#F3 · Medium · Province in Region instead of CountrySubentity
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; `CountrySubentity` is "The political or administrative division of a country in which this address is located, such as the name of its county, province, or state". The Bayvarran address of the same document uses `CountrySubentity` (`/CertificateOfOrigin/cac:ImporterParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 104 examples carry `<cbc:Region>Province of` (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: no Urvanian address of this example holds the province in `Region`; it is in `CountrySubentity` (with `CountrySubentityCode` where a list exists).
- Options: (a, preferred) move it to `CountrySubentity`, as for Bayvarra; (b) if Urvanian provinces are meant as economic regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no
- From: broad (F3), context (F6), parties (F1)

### road/07#F4 · Medium · Language code in LocaleCode
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region. `en` with listID `ISO 639` repeats `Language/ID` and names no locale. Counted: 362 `LocaleCode` elements with `en` (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>en</cbc:LocaleCode>' world/examples | wc -l`) in 213 files.
- Condition: `LocaleCode` is absent or holds a locale from a list of locales named in its listID.
- Options: (a, preferred) drop it: `Language/ID` already says English; (b) a locale such as `en-XB` with a locale list as listID (context's preference).
- Needs decision: no
- From: broad (F4), context (F7), parties (F2, Needs decision yes)

### road/07#F5 · Medium · Gate number in AdditionalStreetName of the importer's postal address
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". `Gate 3` is an entrance of the business park, relevant only to vehicles; in Lumeway's postal address of a certificate of origin it is no street name and has no use. The flow names other entrances for deliveries (`Gate B`, dock 4), so the gate is a delivery instruction, not part of the address.
- Condition: no `AdditionalStreetName` holds a gate, dock or entrance; where a delivery needs it, it is in a delivery location or instruction.
- Options: (a, preferred) drop it from the party address; (b) keep it only in delivery locations (`Location/Description`).
- Needs decision: no
- From: broad (F5), parties (F3)

### road/07#F6 · Medium · The buyer's order number used as the job number of the application
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:OriginalJobID` = `LD-PO-26-0149`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:SupportingDocumentReference/cbc:ID` = `LD-PO-26-0149`
- Why: `OriginalJobID` is "The latest job number given to the CoO application. This is used by the system to keep track of amendments to or cancellation of any earlier applications." The value is Lumeway's purchase order (`01-Order.xml:/Order/cbc:ID` = `LD-PO-26-0149`), an identifier of another kind and issuer, which the application also cites as its supporting document. The application's own number is `ReferenceID` VI-AP-26-0158.
- Condition: `OriginalJobID` holds a job number of the CoO application (applicant's or chamber's numbering), the same in 06 and 07; the order stays only in `SupportingDocumentReference`.
- Options: (a, preferred) the application's job number (e.g. VI-AP-26-0158 or one derived from it); (b) a chamber job number, if the chamber assigns one.
- Needs decision: no
- From: broad (F6), context (F8), logistics (F2)

### road/07#F7 · Medium · Lifecycle stage code MANUFACTURING for a cradle-to-gate figure
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies"; in the world list `MANUFACTURING` is module A3 (making the product), while raw-material supply and its transport (A1, A2) is `SOURCING`. The description and text cover A1 to A3. Code and text name different stages.
- Condition: the lifecycle stage code and text name the same stage(s), and the figure covers exactly what they name.
- Options: (a, preferred) keep the cradle-to-gate figure and omit the code (or give two entries, if the figure can be split); (b) keep `MANUFACTURING` and reduce figure and texts to module A3.
- Needs decision: no
- From: context (F2, High)

### road/07#F8 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: `FullnessIndicationCode` is "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the emission". The value is from the world list `EmissionBoundaryCode`, about the part of a product's life a figure covers, unrelated to the load of transport equipment (semantic conformance). 39 examples do the same (`grep -rl --include='*.xml' 'FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode"' world/examples | wc -l`).
- Condition: `FullnessIndicationCode` is absent from this item emission, or says how full transport equipment is.
- Options: (a, preferred) drop it, state the boundary in text, and record the missing boundary element for the UBL TC write-up.
- Needs decision: no
- From: context (F4)

### road/07#F9 · Medium · Two endorsements with the same sequence number
- XPath: `/CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cbc:SequenceNumeric` = `1`
- XPath: `/CertificateOfOrigin/cac:EmbassyEndorsement/cac:EndorserParty/cbc:SequenceNumeric` = `2`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cac:EndorserParty/cbc:SequenceNumeric` = `2`
- XPath: `06-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:InsuranceEndorsement/cac:EndorserParty/cbc:SequenceNumeric` = `2`
- Why: `SequenceNumeric` is "A number indicating the order of the endorsement provided by this party in the sequence in which endorsements are to be applied". The legalisation and the insurer's endorsement both have 2, so the order is not stated; the legalisation ("Signature of the Ferrano chamber confirmed") must follow the chamber, and in the application (06) the insurer had already endorsed with number 2 while the chamber's endorsement 1 was pending. Merge: not High: equal numbers can be read as parallel steps, so there is no hard contradiction; but the element then does not do what its definition says (order), so Medium.
- Condition: each endorsement has its own sequence number, in the order in which they are applied, unless parallel endorsement is meant and stated.
- Options: (a, preferred) chamber 1, insurer 2, legalisation 3 if both stay (context), or insurer 1, chamber 2, legalisation 3 if the order of 06 counts (parties); (b) drop the insurance and/or embassy endorsement (F10, F23) and renumber.
- Needs decision: no
- From: broad (F7, Medium), context (F1, High), parties (F9, Low)

### road/07#F10 · Medium · Embassy endorsement given by the Trade Accord Council on a preferential certificate
- XPath: `/CertificateOfOrigin/cac:EmbassyEndorsement/cbc:ApprovalStatus` = `Legalised`
- XPath: `/CertificateOfOrigin/cac:EmbassyEndorsement/cac:EndorserParty/cbc:RoleCode` = `LEGALISATION`
- XPath: `/CertificateOfOrigin/cac:EmbassyEndorsement/cac:EndorserParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Trade Accord Council`
- XPath: `/CertificateOfOrigin/cac:EmbassyEndorsement/cac:EndorserParty/cac:Party/cac:PartyIdentification/cbc:ID` = `20411096`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:CertificateType` = `Preferential`
- Why: `EmbassyEndorsement` holds "Embassy Endorsement details", the legalisation by the importing country's embassy or consulate. The endorser is a treaty body, not an embassy, identified in Bayvarra's business register (scheme `urn:ubl-examples:world:XB:register`), which is unusual for an intergovernmental body; and a preferential certificate within a trade accord is normally accepted without legalisation (own knowledge of preferential origin practice). The import declaration does not use the legalisation. Merge: Medium as parties (the element carries a body that is not what its name and definition describe); broad and context had Low. Needs decision because the world's treaty rules could give the council this role.
- Condition: the certificate has no embassy endorsement, or it is given by Bayvarra's consular authority, or the world's rules give the council a legalisation role and the confirmation is carried in an endorsement that does not call it an embassy.
- Options: (a, preferred) drop the embassy endorsement; (b) Bayvarra's embassy or consulate legalises; (c) a general endorser with a council role, recorded in the world's treaty rules.
- Needs decision: yes
- From: parties (F4, Medium), broad (F16, Low), context (F15, Low)

### road/07#F11 · Low · Certificate issued on a Sunday by an office open on weekdays
- XPath: `/CertificateOfOrigin/cbc:IssueDate` = `2026-03-22`
- XPath: `/CertificateOfOrigin/cbc:IssueTime` = `08:41:00`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: 2026-03-22 is a Sunday (checked in the merge); the chamber approves and signs and the accord council legalises at 08:41, while the chamber's certificates office works "Weekdays 08:00–17:00". The application was submitted on Friday 2026-03-20, the goods leave on Monday 2026-03-23.
- Condition: the certificate is issued when the issuing office works, or the note allows weekend issue.
- Options: (a, preferred) Monday 2026-03-23 morning, before the export declaration at 13:25; (b) Friday 2026-03-20 afternoon.
- Needs decision: no
- From: broad (F8), context (F17)

### road/07#F12 · Low · Signature IDs built from the example number and aggregate name
- XPath: `/CertificateOfOrigin/cac:Signature/cbc:ID` = `FCC-SIG-CO-07`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Signature/cbc:ID` = `VI-SIG-COA`
- Why: `Signature/ID` is "An identifier for this signature". `07` is the number of this example file (the application has `06-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:Signature/cbc:ID` = `VI-SIG-CO-06`) and `COA` the aggregate's name; the endorsement signatures of the same document follow a real numbering (`/CertificateOfOrigin/cac:IssuerEndorsement/cac:Signature/cbc:ID` = `FCC-SIG-26-0309`, `LTAC-SIG-26-0311`).
- Condition: signature IDs follow the signer's own numbering, without example numbers or aggregate names.
- Options: (a, preferred) number them like the endorsement signatures (prefix, year, running number).
- Needs decision: no
- From: broad (F9), context (F16)

### road/07#F13 · Low · Contacts that do not fit a certificate of origin
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:Contact/cbc:Name` = `Certificates office`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:Contact/cbc:JobTitle` = `Public service officer`
- Why: the exporter's contact for an origin certificate is its order desk in Sales, the importer's its customer service in Sales; neither handles export, import or origin formalities. The chamber's certificates office has the generic title `Public service officer` (department `Public services`).
- Condition: the contacts handle the certificate's subject (export/import formalities, certification), with fitting titles and departments, or are absent.
- Options: (a, preferred) role-specific contacts (export desk, import/customs desk, certificates officer); (b) drop job title and department where none fits.
- Needs decision: no
- From: broad (F10), context (F11), parties (F6)

### road/07#F14 · Low · Party master data the certificate does nothing with
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: `SecurityListing` ("One or more securities issued by this Party Legal Entity that are listed on regulated markets") plays no part in certifying origin (section 4.8, IND5). The ISIN's check digit is correct (`check_ids.py`).
- Condition: every optional party aggregate present has a reason in this document's purpose.
- Options: (a, preferred) leave the listing out of this document.
- Needs decision: no
- From: parties (F5), context (F12, party part)

### road/07#F15 · Low · Chamber of commerce described as a commercially registered company
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: the chamber issues certificates of origin, a public function; in many countries chambers are public-law bodies (own knowledge), which are not in a commercial register and have no liquidation status. Its legal nature in Urvania is a question of the world's story.
- Condition: the chamber's legal entity matches its legal nature in the world.
- Options: (a, preferred) decide it; if public-law, drop the commercial registration and liquidation status; (b) if private, keep it with a legal form.
- Needs decision: yes
- From: broad (F11), parties (F7)

### road/07#F16 · Low · Endorser's SignatoryContact used against its definition
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- XPath: `/CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- Why: UBL 2.5 defines `EndorserParty/SignatoryContact` as "The individual representing the exporter who signs the Certificate of Origin application before submitting it to the issuer party"; the examples use it for the endorser's own signer. Context: under semantic conformance the use differs from the definition; the definition looks copied from the application's signer, a defect of the model. Broad refuted it as a finding of this example, because the element is mandatory in `EndorserParty` and the defect lies in UBL. Neither argument settles it; kept as Low with a decision.
- Condition: either the use follows the definition, or the difference is recorded as a finding for the UBL TC and the examples keep the endorser's signer deliberately.
- Options: (a, preferred) record it in the findings for the TC and keep the endorser's signer; (b) nothing else is possible while the element is mandatory.
- Needs decision: yes
- From: context (F10); broad considered and refuted it

### road/07#F17 · Low · Endorsement signatories are desks, not individuals
- XPath: `/CertificateOfOrigin/cac:EmbassyEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Legalisation desk`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Cargo claims desk`
- XPath: `/CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- Why: a signatory is an individual who signs ("The individual …"); the values are functional desk names. The insurer signs through its claims desk, which handles claims, not endorsements (broad, within its insurance finding).
- Condition: each `SignatoryContact` names the signing individual or at least the signing function (e.g. job title), fitting the endorsement.
- Options: (a, preferred) a signing function in `JobTitle` (certificates officer, underwriter), functional names kept if personal names are avoided; (b) named fictional persons.
- Needs decision: no
- From: parties (F8), broad (F17, the claims desk)

### road/07#F18 · Low · Previous job ID for a first application
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:PreviousJobID` = `VI-CO-25-0412`
- Why: `PreviousJobID` is "An identifier for the previous job used in case the application requires query or change". This is a first application for the shipment; VI-CO-25-0412 occurs only in the two certificates of origin (`grep -rl --include='*.xml' VI-CO-25-0412 world/examples`), so nothing explains it (IND5).
- Condition: `PreviousJobID` is present only if the application changes or queries an earlier, identifiable job.
- Options: (a, preferred) drop it; (b) make the application an amendment of a named earlier one, or cite an earlier certificate as a typed supporting document.
- Needs decision: no
- From: broad (F12), context (F9), logistics (F3)

### road/07#F19 · Low · Customs values on a certificate whose origin rule is a processing rule
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `4790400`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[2]/cbc:DeclaredCustomsValueAmount` = `71760`
- Why: `DeclaredCustomsValueAmount` is "The total declared value for customs purposes of the goods item." The remarks give a processing rule (`/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:Remarks` = `Benches made of Urvanian steel and Bayvarran timber; the processing in Urvania gives origin.`), so neither the chamber nor customs needs the value from this document; the import declaration carries its own (`10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `47904.00`, XBL). Preferential certificates in real use carry no value unless a value criterion applies (own knowledge); a value-based chamber fee would be a reason, which the example does not state. The values themselves are right: 96 × 49 900 = 4 790 400 and 12 × 5 980 = 71 760 XUF.
- Condition: the goods items carry no customs value, or the example gives the reason the chamber needs it.
- Options: (a, preferred) drop the amounts; (b) keep them with a stated reason (value criterion of the accord, fee basis).
- Needs decision: yes
- From: money (F1)

### road/07#F20 · Low · Product passport and catalogue data copied into the certificate
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:AdditionalItemProperty[5]`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: a certificate of origin needs description, classification, origin, quantity and the facts that confer origin. Keywords, warranty, load test and colour properties, cradle-to-gate emission, waste and repairability play no part (section 4.8). The resource consumption with its origins could support the origin claim, but nothing in the certificate refers to it.
- Condition: the item carries what the certificate's purpose needs; environmental, circularity, warranty and test data are absent unless the document uses them.
- Options: (a, preferred) reduce the item to description, name, identifiers, origin and classification; (b) keep the resource consumption only if the remarks or the endorsement refer to it.
- Needs decision: no
- From: broad (F13), context (F12, item part)

### road/07#F21 · Low · Item number reads as a real GTIN-12
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000034`
- Why: both numbers (scheme `urn:ubl-examples:world:item`) are 12 digits with a valid GS1 mod-10 check digit (recomputed in the merge: 7 and 4), so they read as GTIN-12s in the range of a real GS1 prefix (own knowledge: 770–771 GS1 Colombia; a GTIN-12 starting 7 is in the UPC range). Fictional values must not be mistakable for real register entries. Only the bench carries `BarcodeSymbologyID` and `IssuerScopeID`.
- Condition: the item numbers cannot be read as check-digit-valid GTINs of a real GS1 prefix, and both items of the scheme are described alike.
- Options: (a, preferred) a non-GS1 structure or a GS1 prefix reserved for examples (952, as the GLNs use); (b) drop `IssuerScopeID`/`BarcodeSymbologyID` where they have no role.
- Needs decision: yes
- From: broad (F14)

### road/07#F22 · Low · Supporting document referred to by ID only
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:SupportingDocumentReference/cbc:ID` = `LD-PO-26-0149`
- Why: the reference has no type, date or description, so the chamber cannot tell that it is the buyer's order; origin is normally supported by the invoice and production records (the issuer endorsement says it verified against "the exporter's production records"), not by the buyer's order.
- Condition: the reference says what the referenced document is, and refers to a document that supports origin.
- Options: (a, preferred) add `DocumentTypeCode` (purchase order) or a description; (b) refer to the production records or the invoice instead.
- Needs decision: no
- From: broad (F15), context (F13)

### road/07#F23 · Low · Insurance endorsement without a role in the flow, numbered after a sea-flow policy
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cbc:DocumentID` = `WS-CP-26-4471-E1`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cbc:Remarks` = `The goods described in this certificate are insured door to door.`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cac:EndorserParty/cac:Party/cac:PartyName/cbc:Name` = `Wavesure Cargo Insurance`
- XPath: `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:ID` = `WS-CP-26-4471`
- XPath: `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cbc:InsuredValueAmount` = `59155.80`
- Why: a certificate of origin certifies origin; no other road document mentions insurance or Wavesure, and under FCA (`01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FCA`) the buyer's risk begins at the Ferrano warehouse, so "door to door" says more than the buyer's cover needs. The ID is built on the sea flow's policy, which insures another consignment two months later with beneficiary `sea/14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:InsurancePolicy/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Velumi Trading`. Whether an open cover of Lumeway is meant cannot be settled.
- Condition: the certificate carries an insurance endorsement only if the road shipment is insured under a policy the flow names, with remarks that fit the delivery terms.
- Options: (a, preferred) drop the insurance endorsement; (b) make WS-CP-26-4471 an open cover of Lumeway, named in the waybill.
- Needs decision: yes
- From: broad (F17), context (F14)

### road/07#F24 · Low · Italian street names tagged as English
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Piazza del Mercato`
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: the second rendering of the Urvanian names is Italian text with `languageID` `en-XU` (the same holds for the Italian legal form). Parties refuted it: English keeps foreign street names unchanged and the region subtag follows the sender. Against that, the tag states English for words that are not, next to an Urvanian (`qau`) rendering, so the Italian form is a third language without a tag of its own. The merge cannot settle which reading the world intends; aligned with rail and the other road merges (Low, decision). Rail counted 217 such renderings in 102 files (over `*.xml`).
- Condition: one rule for Italian-form names in English renderings, recorded in the world's language rules, and the tags follow it.
- Options: (a, preferred) record that English renderings keep the Italian exonym (then no change); (b) an Italian language tag for the Italian form.
- Needs decision: yes
- From: merge (parties considered and refuted it)

### road/07#F25 · Low · Side frames not identified as the substituted 2026 casting
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `VI-C180`
- XPath: `02-OrderResponse.xml:/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `2026`
- Why: the order response substituted the 2026 casting for the ordered side frame (and proposed the 2025 casting from stock); this document identifies the side frames only as VI-C180, so it does not say which casting it covers. Added by the merge (no part raised it here), aligned with the other road merges and with logistics' finding on `11-ReceiptAdvice.xml`.
- Condition: the side frame is identified as the order response identifies the substitute.
- Options: (a, preferred) `ExtendedID` 2026; (b) drop the version distinction everywhere if it has no role.
- Needs decision: no
- From: merge

## Checked and consistent
- Goods items (96 benches, 12 side frames), customs values, gross weights (3984 and 122.4 kg) and shipment ID CL-SH-26-0154 agree with `05-ExportCustomsDeclaration.xml`, `06-CertificateOfOrigin.xml` and `10-ImportCustomsDeclaration.xml` (broad, context, logistics).
- `CertificateType` Preferential, the note and the origin remarks agree; both items have origin XU (broad, context, logistics).
- Roles: preparation party and exporter Valdara, importer Lumeway, issuer and first endorser the chamber; the certificate's and the issuer endorsement's signatures are the chamber's, the application's Valdara's (broad, parties).
- Approval: `ApplicationStatusCode` APPROVED and issuer endorsement `Approved` follow the submitted application of 2026-03-20 and precede the import declaration of 2026-03-24 (broad, context).
- Party identity of Lumeway, Valdara, Castrano and Trasvia is the same across the flow apart from the region subtag of English renderings (parties).
- Check digits: GLN 9520610900008 and ISIN XU0001042501 correct (`check_ids.py`, re-run in the merge); GTIN-like check digits recomputed (F21).
- Day of the week of 2026-03-22 (Sunday) and 2026-03-20 (Friday) recomputed in the merge.

## Considered and refuted
- `/CertificateOfOrigin/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Ferrano Chamber of Commerce` while the application inside is signed by Valdara — refuted because the certificate is the chamber's document and the application keeps the exporter's signature (from broad).
- `/CertificateOfOrigin/cac:ExporterParty/cac:ServiceProviderParty`: suspected copied master data — refuted because it explains that the goods leave from Castrano's warehouse (from context).
- Endorser party at document level and again in the application: suspected redundant — refuted because UBL has both and both describe the same chamber consistently (from context).
- `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cbc:ID`: the 3PL's shipment ID appears before the despatch advice that reports it (`04-DespatchAdvice.xml`, 2026-03-23) — refuted because a shipment number is commonly reserved when the shipment is planned (from logistics).
- `/CertificateOfOrigin/cac:ExporterParty/cac:PostalAddress/cbc:StreetName[2]`: Italian-language street name tagged `en-XU` — refuted by parties because English text keeps foreign street names unchanged and the subtag follows the sender; the merge does not follow the refutation and made it F24, aligned with rail and merger C.
- `/CertificateOfOrigin/cac:ImporterParty/cac:AdditionalPartyIdentification[1]/cbc:ID`: GLN that could be real — refuted because prefix 952 is GS1's prefix for demonstrations and the check digit is correct (from parties).
- `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:Telephone`: numbers could be real — refuted because +999 is reserved in ITU-T E.164 (from parties).
- `/CertificateOfOrigin/cac:ExporterParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: looks like a contract number — refuted because the definition does not say who assigns the ID; Valdara's own number for its provider is a legitimate reading (from parties).
- `/CertificateOfOrigin/cac:EmbassyEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Legalisation desk` against the definition of `SignatoryContact` — broad refuted it as a model defect; the merge does not follow the refutation and keeps the question as F16 (context's finding).

## Changed in the merge
- New F24 (Italian tags, from parties' refuted candidate) and F25 (2026 casting, added by the merge), aligned with rail and mergers A and C.
- broad/F1, context/F3, logistics/F4 → F1: combined; High kept (logistics had Low, context Medium) because the reference in 10 resolves to two documents with different content (section 6, broken reference). Preferred option changed to version 2 (logistics' preference), aligned with merger A, which reviews 06.
- broad/F2, logistics/F1, context/F5 → F2: combined; High (context had Medium) because the arithmetic does not hold; option (a) preferred as in rail and air (logistics preferred a real factor).
- parties/F2 → F4: Needs decision changed from yes to no, aligned with broad, context and the earlier flows.
- context/F2 → F7: High lowered to Medium, aligned with rail and air (the code names another stage than the figure; the fix is encoding, not a contradiction between two figures).
- broad/F7, context/F1, parties/F9 → F9: Medium (context High, parties Low); options of context and parties combined.
- parties/F4, broad/F16, context/F15 → F10: Medium as parties (broad and context had Low); the register identification added from parties.
- context/F12 split into F14 (party master data, with parties/F5) and F20 (item data, with broad/F13), as in rail.
- broad/F17's claims-desk remark moved to F17 (with parties/F8); F23 keeps the insurance question.
- broad's refutation of the `SignatoryContact` definition not followed: kept as F16 (context/F10, Low, yes).

## Outside this review
- Whether the application `06-CertificateOfOrigin.xml` should carry the chamber's number at all belongs to the review of 06 (the fix of F1 may be made there).
