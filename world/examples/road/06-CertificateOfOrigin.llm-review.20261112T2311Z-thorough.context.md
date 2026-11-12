# LLM review: 06-CertificateOfOrigin.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/06-CertificateOfOrigin.xml`, Git blob `faaaba8b3816ead4cce39fdf9204e831ab65f4f7` (committed)
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

### road/06#F1 · High · Second endorsement given while the first is still pending
- XPath: `/CertificateOfOrigin/cac:IssuerEndorsement/cbc:ApprovalStatus` = `Pending`
- XPath: `/CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cbc:SequenceNumeric` = `1`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cbc:ApprovalStatus` = `Endorsed`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cac:EndorserParty/cbc:SequenceNumeric` = `2`
- Why: `EndorserParty/SequenceNumeric` is "A number indicating the order of the endorsement provided by this party in the sequence in which endorsements are to be applied". The insurer's endorsement is number 2, to follow the chamber's (number 1), but in the submitted application the chamber's endorsement is pending while the insurer's is already given ("The goods described in this certificate are insured door to door"), i.e. the insurer endorsed a certificate that did not yet exist.
- Condition: no endorsement with a higher sequence number is given while one with a lower number is pending; or the sequence numbers reflect the order in which the endorsements are actually given.
- Options: (a) drop the insurance endorsement from the application and add it, if at all, after issue (preferred: the application stage has only the applicant's signature); (b) number the insurer 1 and the chamber 2 if the insurer endorses first in the world's procedure.
- Needs decision: no

### road/06#F2 · High · Lifecycle stage code says manufacturing only, its text says cradle to gate
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies" and `LifecycleStageDescription` "The lifecycle stage to which this emission applies, expressed as a text", so both must name the same stage. In the world list `LifecycleStageCode`, `MANUFACTURING` is "Making the product (EN 15804 module A3)"; raw material supply and its transport (A1, A2) is `SOURCING`. The text and the emission's description include mining, steel making and the transport between the steps, i.e. A1 to A3 (cradle to gate, as the boundary code next to it also says). Code and text contradict each other. The same item data occurs in 9 examples of the flow (`grep -l MANUFACTURING world/examples/road/*.xml`).
- Condition: the lifecycle stage code and text name the same stage(s), and the emission figure covers exactly what they name.
- Options: (a) keep the cradle-to-gate figure and state the stage in text only, or with a code covering A1 to A3 if the world list gets one (preferred: the figure is a cradle-to-gate figure); (b) keep `MANUFACTURING` and reduce figure, text and description to module A3.
- Needs decision: no

### road/06#F3 · Medium · The exporter's application carries the chamber's certificate number as its ID
- XPath: `/CertificateOfOrigin/cbc:ID` = `FCC-CO-26-0157`
- XPath: `/CertificateOfOrigin/cac:Signature/cbc:ID` = `VI-SIG-CO-06`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:ApplicationStatusCode` = `SUBMITTED`
- Why: `ID` is "An identifier for this document, assigned by the sender". This instance is the exporter's submitted application (signed by Valdara, issuer endorsement pending), so its sender is Valdara, yet its ID is in the Ferrano Chamber of Commerce's certificate numbering (`FCC-CO-…`), the number of the certificate the chamber issues two days later (`07-CertificateOfOrigin.xml:/CertificateOfOrigin/cbc:ID` = `FCC-CO-26-0157`). Either the chamber assigned the number before receiving the application, or the sender's ID is not the sender's.
- Condition: the ID of the submitted application is assigned by its sender (Valdara), and the chamber's certificate number appears where the chamber has assigned it (the issued certificate and its endorsement).
- Options: (a) give the application a Valdara document ID and keep `FCC-CO-26-0157` for the issued certificate (preferred); (b) state in the story that the chamber pre-assigns certificate numbers to applicants, and say so in a note.
- Needs decision: yes

### road/06#F4 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: UBL 2.5 defines `EmissionCalculationMethod/FullnessIndicationCode` as "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the emission". The value comes from the world list `EmissionBoundaryCode` (how much of a product's life the figure covers), which has nothing to do with the load of transport equipment (semantic conformance, UBL 2.5 §4.7). 39 examples do the same (`grep -rl 'FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode"'` over `*.xml`); the other uses of the element take `LoadTypeCode`, which fits the definition.
- Condition: `FullnessIndicationCode` is absent from this item emission, or says how full transport equipment is; the system boundary, if kept, is stated where UBL allows it (e.g. in text).
- Options: (a) drop it and state the boundary in `LifecycleStageDescription` or `Description` (preferred: an item's cradle-to-gate figure involves no transport equipment); (b) record the missing boundary element as a finding for the UBL TC.
- Needs decision: no

### road/06#F5 · Medium · Emission factor and base do not give the stated emission
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 EA the factor says 0.82 kg CO2e per bench, but the value for one bench is 96 kg (96 / 0.82 = 117.1 benches, matching nothing in the flow). The factor cannot have produced the value, so it does nothing here or is the wrong figure.
- Condition: `ValueFactorNumeric` × the activity quantity in the unit of `ValueBaseMeasure` gives `ValueMeasure`, or factor and base are absent.
- Options: (a) drop factor and base, since the value is a per-item figure from the LCA (preferred); (b) state a factor and base whose product is 96 kg per bench.
- Needs decision: no

### road/06#F6 · Medium · Province given as Region
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country ... such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran addresses of the flow use for their state (`Upland State`). 104 examples carry a province in `Region` (`grep -rl '<cbc:Region>Province'` over `*.xml`).
- Condition: the Urvanian province is in `CountrySubentity`; `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no

### road/06#F7 · Medium · LocaleCode holds a language code
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region (e.g. `en-XB`, the form the examples use in `languageID`). `en` with `listID` ISO 639 repeats `Language/ID` and names no locale. All 362 `LocaleCode` elements in the examples are `en` with ISO 639 (`grep -rho '<cbc:LocaleCode[^<]*<'` over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) `en-XB` with a locale list (BCP 47 / CLDR style) as listID (preferred: matches the `languageID` already used); (b) drop it.
- Needs decision: no

### road/06#F8 · Medium · The buyer's order number given as the CoO application's job number
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:OriginalJobID` = `LD-PO-26-0149`
- Why: `OriginalJobID` is "The latest job number given to the CoO application. This is used by the system to keep track of amendments to or cancellation of any earlier applications." The value is Lumeway's purchase order number (`01-Order.xml:/Order/cbc:ID` = `LD-PO-26-0149`), an identifier of another kind assigned by another party; it does not number the application (whose own reference is `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:ReferenceID` = `VI-AP-26-0158`) and cannot track its amendments.
- Condition: `OriginalJobID` holds the job number of this CoO application in the numbering of the applicant or the issuer, not an order number; the order, if needed, stays in `SupportingDocumentReference`.
- Options: (a) the application's job number (e.g. the same as or derived from `ReferenceID`) (preferred); (b) the chamber's job number, if the chamber assigns one.
- Needs decision: no

### road/06#F9 · Low · Previous job ID with no previous application in the story
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:PreviousJobID` = `VI-CO-25-0412`
- Why: `PreviousJobID` is "An identifier for the previous job used in case the application requires query or change". This is a first application for this shipment, with no query or change; a 2025 job number appears in no other example (`grep -r VI-CO-25-0412` over `*.xml` finds only the two certificates of origin), so nothing explains what it refers to (IND5).
- Condition: `PreviousJobID` is absent, or refers to an earlier application this one changes or queries, as the story states.
- Options: (a) drop it (preferred); (b) give the story a previous application this one amends.
- Needs decision: no

### road/06#F10 · Low · Endorser's signatory contact is the chamber, the definition asks for the exporter's signer
- XPath: `/CertificateOfOrigin/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- XPath: `/CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cac:SignatoryContact/cbc:Name` = `Certificates office`
- Why: UBL 2.5 defines `EndorserParty/SignatoryContact` as "The individual representing the exporter who signs the Certificate of Origin application before submitting it to the issuer party". The examples use it for the endorser's own signing office (the chamber's certificates office, and in the other endorsements the insurer's and legaliser's desks). The literal definition does not fit an endorser party at all, which looks like a defect of the UBL definition; under the semantic-conformance rule the use still differs from it.
- Condition: either the use follows the definition, or the difference is recorded as a finding for the UBL TC and the examples keep the endorser's signer deliberately.
- Options: (a) record it as a UBL finding (definition of `EndorserParty/SignatoryContact` copied from the application's signer) and keep the endorser's office (preferred: an endorser's signatory is what the aggregate needs); (b) drop `SignatoryContact` from the endorser parties.
- Needs decision: yes

### road/06#F11 · Low · Contacts that do not fit a certificate of origin
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/CertificateOfOrigin/cac:ImporterParty/cac:Contact/cbc:Department` = `Sales`
- Why: the chamber asks the exporter's export or customs function about origin, not the order desk in Sales; the importer's contact for a certificate it uses at import is its import or purchasing function, not its own customer service.
- Condition: the exporter's and importer's contacts handle export/import formalities, or are absent.
- Options: (a) export and import contacts (preferred); (b) drop job title and department where none fits.
- Needs decision: no

### road/06#F12 · Low · Master and product data the certificate does nothing with
- XPath: `/CertificateOfOrigin/cac:ExporterParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:Keyword` = `park bench, street furniture`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cbc:WarrantyInformation[2]` = `Five years on the frame against corrosion.`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Shipment/cac:GoodsItem[1]/cac:Item/cac:CircularityProfile/cac:RepairabilityScore/cbc:ScoreNumeric` = `8`
- Why: a certificate of origin needs the goods' description, classification, quantity and origin, and the facts that confer origin (stated in the remarks: Urvanian steel, Bayvarran timber, processing in Urvania). The exporter's stock-exchange listing, search keywords, warranty, the circularity profile and the product's emission figure play no part in it (section 4.8, IND5). The resource consumption with its origins could support the origin claim, but nothing in the certificate refers to it.
- Condition: party and item data in the certificate have a use for establishing or stating origin.
- Options: (a) drop the listing, keyword, warranty, emission and the rest of the circularity profile (preferred); (b) keep the resource consumption only if the remarks or the endorsement refer to it.
- Needs decision: no

### road/06#F13 · Low · Supporting document referred to by ID only
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:SupportingDocumentReference/cbc:ID` = `LD-PO-26-0149`
- Why: the reference carries neither a type nor a description, so the chamber cannot tell what kind of document supports the application; origin is normally supported by the commercial invoice and production records (the endorsement remarks say "verified against the exporter's production records" in the issued certificate), not by the buyer's order.
- Condition: the supporting document reference says what the referenced document is, and refers to a document that supports origin.
- Options: (a) add a document type (purchase order) or description (preferred: smallest change); (b) refer to the production records or the invoice instead.
- Needs decision: no

### road/06#F14 · Low · Insurance endorsement without a role in the flow
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cbc:DocumentID` = `WS-CP-26-4471-E1`
- XPath: `/CertificateOfOrigin/cac:InsuranceEndorsement/cbc:Remarks` = `The goods described in this certificate are insured door to door.`
- Why: an insurer's endorsement on a certificate of origin needs a reason in the story (e.g. an insurance certificate that the importer or a bank needs together with the origin certificate). No other document of the flow mentions cargo insurance or the policy `WS-CP-26-4471` (`grep -r 'WS-CP-26-4471\|Wavesure'` over `*.xml` finds only the two certificates of origin), and under FCA (`01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FCA`) the buyer's risk only begins at the Ferrano warehouse, so "door to door" says more than the buyer's cover needs. It looks like an aggregate filled because the document type has it (IND5).
- Condition: the insurance endorsement is absent, or the story has a cargo insurance that the certificate's use depends on, and its remarks fit the delivery terms.
- Options: (a) drop it (preferred); (b) add the insurance to the story (policy, insured party, cover from the FCA place) and say why it is endorsed on the certificate.
- Needs decision: yes

### road/06#F15 · Low · Signature IDs built from the example number
- XPath: `/CertificateOfOrigin/cac:Signature/cbc:ID` = `VI-SIG-CO-06`
- XPath: `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:Signature/cbc:ID` = `VI-SIG-COA`
- Why: `Signature/ID` is "An identifier for this signature". `06` is the number of this example file in the repository (the issued certificate has `07-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:Signature/cbc:ID` = `FCC-SIG-CO-07`), and `COA` is the name of the aggregate; neither is a number Valdara would assign. The signatures carry no method, time or value, so they only state that Valdara signed.
- Condition: signature IDs follow the signer's own numbering, without repository file numbers or flow names.
- Options: (a) number them after the application (e.g. after `VI-AP-26-0158`) (preferred); (b) drop the document-level signature, since the application already carries the applicant's signature.
- Needs decision: no

## Checked and consistent
- Shipment `CL-SH-26-0154` and the goods items (96 benches, 12 side frames, values 4 790 400 and 71 760 XUF, gross 3 984 and 122.4 kg) match the export declaration `05-ExportCustomsDeclaration.xml`.
- `CertificateType` `Preferential`, the note "Preferential origin under the trade accord" and the remarks on Urvanian steel, Bayvarran timber and processing in Urvania agree with each other and with origin XU on both items.
- Preparation party = exporter = Valdara; issuer = chamber; importer = Lumeway; distribution of an electronic copy to Lumeway fits the importer's later use (`10-ImportCustomsDeclaration.xml` refers to `FCC-CO-26-0157`).
- Issued Friday 2026-03-20, before the despatch on 2026-03-23.

## Considered and refuted
- `/CertificateOfOrigin/cac:ExporterParty/cac:ServiceProviderParty`: suspected master data — refuted because it explains that the goods leave from Castrano's warehouse, which the chamber may inspect.
- Duplicate endorser party at document level and in the application (`/CertificateOfOrigin/cac:EndorserParty` and `/CertificateOfOrigin/cac:CertificateOfOriginApplication/cac:EndorserParty`): suspected redundant — refuted because UBL has both (endorser of the certificate and endorser requested by the application) and both describe the same chamber consistently.
