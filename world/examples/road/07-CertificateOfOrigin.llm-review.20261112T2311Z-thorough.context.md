# LLM review: 07-CertificateOfOrigin.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/07-CertificateOfOrigin.xml`, Git blob `9dd12c4b7afb7cb32c342c0e094823576afb0a28` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### road/07#F1 · High · Two endorsements with the same sequence number
- XPath: `/CertificateOfOrigin/cac:EmbassyEndorsement/cac:EndorserParty/cbc:SequenceNumeric` = `2`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cac:EndorserParty/cbc:SequenceNumeric` = `2`
- Why: `SequenceNumeric` is "A number indicating the order of the endorsement provided by this party in the sequence in which endorsements are to be applied". The legalisation by the Trade Accord Council and the insurer's endorsement both claim place 2 after the chamber (1), so the order in which they are applied is not stated. The legalisation ("Signature of the Ferrano chamber confirmed") was added after the application (`06-CertificateOfOrigin.xml` has no embassy endorsement but the same insurer endorsement as 2), which suggests legalisation is 3 or the insurer's number changed.
- Condition: each endorsement has its own sequence number, in the order in which they are applied.
- Options: (a) chamber 1, insurer 2, legalisation 3, if the insurer's endorsement stays (preferred: matches the order in which they appear across 06 and 07); (b) drop the insurer's endorsement (see F14) and keep legalisation 2.
- Needs decision: no

### road/07#F2 · High · Lifecycle stage code says manufacturing only, its text says cradle to gate
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies" and `LifecycleStageDescription` "The lifecycle stage to which this emission applies, expressed as a text", so both must name the same stage. In the world list `LifecycleStageCode`, `MANUFACTURING` is "Making the product (EN 15804 module A3)"; raw material supply and its transport (A1, A2) is `SOURCING`. The text and the emission's description include mining, steel making and the transport between the steps, i.e. A1 to A3 (cradle to gate, as the boundary code next to it also says). Code and text contradict each other. The same item data occurs in 9 examples of the flow (`grep -l MANUFACTURING world/examples/road/*.xml`).
- Condition: the lifecycle stage code and text name the same stage(s), and the emission figure covers exactly what they name.
- Options: (a) keep the cradle-to-gate figure and state the stage in text only, or with a code covering A1 to A3 if the world list gets one (preferred: the figure is a cradle-to-gate figure); (b) keep `MANUFACTURING` and reduce figure, text and description to module A3.
- Needs decision: no

### road/07#F3 · Medium · Issued certificate has the same ID and version as the submitted application
- XPath: `/CertificateOfOrigin/cbc:ID` = `FCC-CO-26-0157`
- XPath: `/CertificateOfOrigin/cbc:VersionID` = `1`
- Why: `VersionID` "Identifies the version of this Certificate of Origin". This instance differs from `06-CertificateOfOrigin.xml` (approved instead of submitted, issuer and legalisation signatures added, different UUID and issue date), yet carries the same ID and the same version (`06-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:VersionID` = `1`). Two different contents under one ID and version cannot be told apart by anyone who refers to the certificate by ID (as `10-ImportCustomsDeclaration.xml` does).
- Condition: two instances with different content do not share ID and version: either the application has its own ID (see the review of 06) or the issued certificate has a higher version.
- Options: (a) the application gets an ID of its own and the issued certificate keeps `FCC-CO-26-0157` version 1 (preferred: the import declaration refers to the issued certificate); (b) keep the ID and give this instance version 2.
- Needs decision: no

### road/07#F4 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: UBL 2.5 defines `EmissionCalculationMethod/FullnessIndicationCode` as "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the emission". The value comes from the world list `EmissionBoundaryCode` (how much of a product's life the figure covers), which has nothing to do with the load of transport equipment (semantic conformance, UBL 2.5 §4.7). 39 examples do the same (`grep -rl 'FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode"'` over `*.xml`); the other uses of the element take `LoadTypeCode`, which fits the definition.
- Condition: `FullnessIndicationCode` is absent from this item emission, or says how full transport equipment is; the system boundary, if kept, is stated where UBL allows it (e.g. in text).
- Options: (a) drop it and state the boundary in `LifecycleStageDescription` or `Description` (preferred: an item's cradle-to-gate figure involves no transport equipment); (b) record the missing boundary element as a finding for the UBL TC.
- Needs decision: no

### road/07#F5 · Medium · Emission factor and base do not give the stated emission
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 EA the factor says 0.82 kg CO2e per bench, but the value for one bench is 96 kg (96 / 0.82 = 117.1 benches, matching nothing in the flow). The factor cannot have produced the value, so it does nothing here or is the wrong figure.
- Condition: `ValueFactorNumeric` × the activity quantity in the unit of `ValueBaseMeasure` gives `ValueMeasure`, or factor and base are absent.
- Options: (a) drop factor and base, since the value is a per-item figure from the LCA (preferred); (b) state a factor and base whose product is 96 kg per bench.
- Needs decision: no

### road/07#F6 · Medium · Province given as Region
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country ... such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the flow use for their state (`Upland State`). 104 examples carry a province in `Region` (`grep -rl '<cbc:Region>Province'` over `*.xml`).
- Condition: the Urvanian province is in `CountrySubentity`; `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no

### road/07#F7 · Medium · LocaleCode holds a language code
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region (e.g. `en-XB`, the form the examples use in `languageID`). `en` with `listID` ISO 639 repeats `Language/ID` and names no locale. All 362 `LocaleCode` elements in the examples are `en` with ISO 639 (`grep -rho '<cbc:LocaleCode[^<]*<'` over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) `en-XB` with a locale list (BCP 47 / CLDR style) as listID (preferred: matches the `languageID` already used); (b) drop it.
- Needs decision: no

### road/07#F8 · Medium · The buyer's order number given as the CoO application's job number
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:OriginalJobID` = `LD-PO-26-0149`
- Why: `OriginalJobID` is "The latest job number given to the CoO application. This is used by the system to keep track of amendments to or cancellation of any earlier applications." The value is Lumeway's purchase order number (`01-Order.xml:/Order/cbc:ID` = `LD-PO-26-0149`), an identifier of another kind assigned by another party; it does not number the application (whose own reference is `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:ReferenceID` = `VI-AP-26-0158`) and cannot track its amendments.
- Condition: `OriginalJobID` holds the job number of this CoO application in the numbering of the applicant or the issuer, not an order number; the order, if needed, stays in `SupportingDocumentReference`.
- Options: (a) the application's job number (e.g. the same as or derived from `ReferenceID`) (preferred); (b) the chamber's job number, if the chamber assigns one.
- Needs decision: no

### road/07#F9 · Low · Previous job ID with no previous application in the story
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:PreviousJobID` = `VI-CO-25-0412`
- Why: `PreviousJobID` is "An identifier for the previous job used in case the application requires query or change". This is a first application for this shipment, with no query or change; a 2025 job number appears in no other example (`grep -r VI-CO-25-0412` over `*.xml` finds only the two certificates of origin), so nothing explains what it refers to (IND5).
- Condition: `PreviousJobID` is absent, or refers to an earlier application this one changes or queries, as the story states.
- Options: (a) drop it (preferred); (b) give the story a previous application this one amends.
- Needs decision: no

### road/07#F10 · Low · Endorser's signatory contact is the chamber, the definition asks for the exporter's signer
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- XPath: `/CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- Why: UBL 2.5 defines `EndorserParty/SignatoryContact` as "The individual representing the exporter who signs the Certificate of Origin application before submitting it to the issuer party". The examples use it for the endorser's own signing office (the chamber's certificates office, and in the other endorsements the insurer's and legaliser's desks). The literal definition does not fit an endorser party at all, which looks like a defect of the UBL definition; under the semantic-conformance rule the use still differs from it.
- Condition: either the use follows the definition, or the difference is recorded as a finding for the UBL TC and the examples keep the endorser's signer deliberately.
- Options: (a) record it as a UBL finding (definition of `EndorserParty/SignatoryContact` copied from the application's signer) and keep the endorser's office (preferred: an endorser's signatory is what the aggregate needs); (b) drop `SignatoryContact` from the endorser parties.
- Needs decision: yes

### road/07#F11 · Low · Contacts that do not fit a certificate of origin
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- Why: the chamber asks the exporter's export or customs function about origin, not the order desk in Sales; the importer's contact for a certificate it uses at import is its import or purchasing function, not its own customer service.
- Condition: the exporter's and importer's contacts handle export/import formalities, or are absent.
- Options: (a) export and import contacts (preferred); (b) drop job title and department where none fits.
- Needs decision: no

### road/07#F12 · Low · Master and product data the certificate does nothing with
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: a certificate of origin needs the goods' description, classification, quantity and origin, and the facts that confer origin (stated in the remarks: Urvanian steel, Bayvarran timber, processing in Urvania). The exporter's stock-exchange listing, search keywords, warranty, the circularity profile and the product's emission figure play no part in it (section 4.8, IND5). The resource consumption with its origins could support the origin claim, but nothing in the certificate refers to it.
- Condition: party and item data in the certificate have a use for establishing or stating origin.
- Options: (a) drop the listing, keyword, warranty, emission and the rest of the circularity profile (preferred); (b) keep the resource consumption only if the remarks or the endorsement refer to it.
- Needs decision: no

### road/07#F13 · Low · Supporting document referred to by ID only
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:SupportingDocumentReference/cbc:ID` = `LD-PO-26-0149`
- Why: the reference carries neither a type nor a description, so the chamber cannot tell what kind of document supports the application; origin is normally supported by the commercial invoice and production records (the endorsement remarks say "verified against the exporter's production records" in the issued certificate), not by the buyer's order.
- Condition: the supporting document reference says what the referenced document is, and refers to a document that supports origin.
- Options: (a) add a document type (purchase order) or description (preferred: smallest change); (b) refer to the production records or the invoice instead.
- Needs decision: no

### road/07#F14 · Low · Insurance endorsement without a role in the flow
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cbc:DocumentID` = `WS-CP-26-4471-E1`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cbc:Remarks` = `The goods described in this certificate are insured door to door.`
- Why: no other document of the flow mentions cargo insurance or the policy `WS-CP-26-4471` (`grep -r 'WS-CP-26-4471\|Wavesure'` over `*.xml` finds only the two certificates of origin), and under FCA (`01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FCA`) the buyer's risk begins only at the Ferrano warehouse, so "door to door" says more than the buyer's cover needs. Nothing in the certificate's purpose depends on the endorsement (IND5).
- Condition: the insurance endorsement is absent, or the story has a cargo insurance that the certificate's use depends on, with remarks that fit the delivery terms.
- Options: (a) drop it (preferred); (b) add the insurance to the story and say why it is endorsed on the certificate.
- Needs decision: yes

### road/07#F15 · Low · Legalisation by the Trade Accord Council in the embassy endorsement of a preferential certificate
- XPath: `/CertificateOfOrigin/cac:EmbassyEndorsement/cac:EndorserParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Trade Accord Council`
- XPath: `/CertificateOfOrigin/cac:EmbassyEndorsement/cbc:ApprovalStatus` = `Legalised`
- Why: `EmbassyEndorsement` holds "Embassy Endorsement details", i.e. the legalisation by the importing country's embassy or consulate. The endorser is the Trade Accord Council, a treaty body, not an embassy; and a preferential certificate under the accord (`/CertificateOfOrigin/cbc:Note[2]` = `Preferential origin under the trade accord.`) is normally accepted between accord members without legalisation (own knowledge of preferential origin practice). The story gives no reason why Bayvarra would require legalisation here.
- Condition: either the legalisation has a reason in the world's rules (and the endorser is the body those rules name), or the embassy endorsement is absent.
- Options: (a) drop the embassy endorsement (preferred: no legalisation within the accord); (b) state in the world's rules that the accord council legalises certificates and why, and keep it.
- Needs decision: yes

### road/07#F16 · Low · Signature IDs built from the example number and aggregate name
- XPath: `/CertificateOfOrigin/cac:Signature/cbc:ID` = `FCC-SIG-CO-07`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Signature/cbc:ID` = `VI-SIG-COA`
- Why: `Signature/ID` is "An identifier for this signature". `07` is the number of this example file (the application has `06-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:Signature/cbc:ID` = `VI-SIG-CO-06`) and `COA` the aggregate's name; the chamber's endorsement signature in the same document follows a real numbering (`/CertificateOfOrigin/cac:IssuerEndorsement/cac:Signature/cbc:ID` = `FCC-SIG-26-0309`).
- Condition: signature IDs follow the signer's own numbering, without repository file numbers or aggregate names.
- Options: number them like the endorsement signatures (preferred).
- Needs decision: no

### road/07#F17 · Low · Certificate issued on a Sunday by an office open on weekdays
- XPath: `/CertificateOfOrigin/cbc:IssueDate` = `2026-03-22`
- XPath: `/CertificateOfOrigin/cbc:IssueTime` = `08:41:00`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: 2026-03-22 is a Sunday; the chamber's certificates office that approves and signs the certificate is available on weekdays 08:00–17:00 according to its own contact note in this document.
- Condition: the certificate is issued at a time when the issuing office works, or the contact note allows weekend issue.
- Options: (a) issue it on Monday 2026-03-23 morning, still before the declaration at 13:25 and the despatch (preferred); (b) issue it on Friday 2026-03-20 afternoon.
- Needs decision: no

## Checked and consistent
- Shipment `CL-SH-26-0154`, goods items, values and weights match `05-ExportCustomsDeclaration.xml` and `06-CertificateOfOrigin.xml`.
- The application status `APPROVED`, the issuer endorsement `Approved` with its remark and the chamber's signatures fit an issued certificate, and follow the submitted application of 2026-03-20.
- `CertificateType` `Preferential`, the note and the origin remarks agree; both items have origin XU.
- The import declaration refers to this certificate (`10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:CustomsDeclaration/cac:AdditionalDocumentReference/cbc:ID` = `FCC-CO-26-0157`).

## Considered and refuted
- `/CertificateOfOrigin/cac:ExporterParty/cac:ServiceProviderParty`: suspected master data — refuted because it explains that the goods leave from Castrano's warehouse.
- Duplicate endorser party at document level and in the application: suspected redundant — refuted because UBL has both and both describe the same chamber consistently.
