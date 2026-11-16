# Findings on UBL 2.5 definitions

## Context

These findings come from building a set of minimal, semantically meaningful example documents for all 101 UBL 2.5 document types. Each value was chosen from the element's UBL definition, as required for semantic conformance (UBL 2.5 §4.7, §7.2). In a few places the definitions themselves turned out to be wrong, inconsistent or unclear. They are listed here for the OASIS UBL TC.

- **Source:** UBL 2.5 OASIS Standard, package `UBL-2.5.zip` from <https://docs.oasis-open.org/ubl/os-UBL-2.5/> (pubdate 12 August 2026).
- **Locations:** given as `file:line` in the package's `xsd/` directory. The same text appears in the model spreadsheets and the HTML documentation.
- **Quotations:** every quoted definition is copied verbatim from the schema.

## Summary

| # | Element | Kind |
|---|---|---|
| F1 | PurchaseReceiptLine. Item | definition copied from another class |
| F2 | Digital Process. Identifier | definition names the wrong class |
| F3 | Endorser Party. Signatory Contact | definition fits only one of its contexts |
| F4 | Evidence (class) | class definition is limited to tendering but reused in customs |
| F5 | Tendering Criterion Response. Validated Criterion Property Identifier | definition does not say what is identified |
| F6 | TenderContract. Economic Operator Party | definition copied from another document |
| F7 | Qualification Resolution. Admission Code | Code whose definition is an Indicator |
| F8 | Contact. Name | general guidance conflicts with a contextual use |
| F9 | (16 definitions) | spelling: "reponsible" |
| F10 | TenderStatusRequest. Contracting Party | spelling: "eceiving" |

## Findings

### F1 · PurchaseReceiptLine. Item: definition copied from InvoiceLine

- **Location:** `common/UBL-CommonAggregateComponents-2.5.xsd:36425` (PurchaseReceiptLineType, `cac:Item`)
- **Current definition:** "The item associated with this invoice line."
- **Issue:** the element belongs to a purchase receipt line, not an invoice line. The text appears to be copied from InvoiceLine.
- **Suggested definition:** "The item associated with this purchase receipt line."

### F2 · Digital Process. Identifier: definition names the wrong class

- **Location:** `common/UBL-CommonAggregateComponents-2.5.xsd:15341` (DigitalProcessType, `cbc:ID`)
- **Current definition:** "An identifier for the digital collaboration."
- **Issue:** the element identifies the digital process. Digital Collaboration is a separate class, and DigitalProcess contains it (`cac:DigitalCollaboration`). As written, a user cannot tell whether the ID identifies the process or a collaboration within it.
- **Suggested definition:** "An identifier for this digital process."

### F3 · Endorser Party. Signatory Contact: definition fits only one of its contexts

- **Location:** `common/UBL-CommonAggregateComponents-2.5.xsd:17301` (EndorserPartyType, `cac:SignatoryContact`)
- **Current definition:** "The individual representing the exporter who signs the Certificate of Origin application before submitting it to the issuer party."
- **Issue:** EndorserParty is used both in CertificateOfOriginApplication and in IssuerEndorsement (EndorsementType, `cac:EndorserParty`, line 17202: "The type of party providing this endorsement."). In an IssuerEndorsement the endorser is the issuing side, for example a chamber of commerce or an embassy, not the exporter, and it signs an endorsement, not the application. The class-level definition therefore contradicts one of its own uses.
- **Suggested definition:** "The individual who signs this endorsement on behalf of the endorsing party."

### F4 · Evidence (class): definition limited to tendering, but reused in customs

- **Location:** `common/UBL-CommonAggregateComponents-2.5.xsd:18415` (EvidenceType)
- **Current definition:** "A class to describe an item of evidentiary support for representations of capabilities or the ability to meet tendering requirements, which an economic operator must provide for acceptance into a tendering process."
- **Use outside tendering:** `maindoc/UBL-ProofOfReexportation-2.5.xsd:290` (`cac:ReexportationEvidence`): "One or more references to evidence supporting that goods have been re-exported".
- **Issue:** read literally, the class cannot describe evidence of re-exportation in a customs (ATA Carnet) document, yet ProofOfReexportation uses it for exactly that.
- **Suggested action:** generalise the class definition, e.g. "A class to describe an item of evidentiary support, such as for capabilities in a tendering process or for a customs procedure." Alternatively, introduce a separate class for customs evidence.

### F5 · Tendering Criterion Response. Validated Criterion Property Identifier: unclear definition

- **Location:** `common/UBL-CommonAggregateComponents-2.5.xsd:48678` (TenderingCriterionResponseType, `cbc:ValidatedCriterionPropertyID`)
- **Current definition:** "An identifier for this item of criterion support."
- **Issue:** in practice (ESPD), the element refers to the criterion property, i.e. the question in the QualificationApplicationRequest or in the repeated TenderingCriterion, that this response answers. The definition does not say so. "This item of criterion support" reads as if it identified the response itself, which already has its own `cbc:ID`.
- **Suggested definition:** "An identifier of the tendering criterion property to which this response applies."

### F6 · TenderContract. Economic Operator Party: definition copied from another document

- **Location:** `maindoc/UBL-TenderContract-2.5.xsd:355` (`cac:EconomicOperatorParty`)
- **Current definition:** "The Economic Operator issuing the inquiry on the status of a tendering process."
- **Issue:** a TenderContract is not an inquiry about the status of a tendering process. The text matches the procurement status request documents and appears to be copied from there.
- **Suggested definition:** "The economic operator that is party to this contract."

### F7 · Qualification Resolution. Admission Code: a Code defined as an Indicator

- **Location:** `common/UBL-CommonAggregateComponents-2.5.xsd:36527` (QualificationResolutionType, `cbc:AdmissionCode`)
- **Current definition:** "An indicator that the economic operator has been accepted into the tendering process (true) or rejected from the tendering process (false)."
- **Issue:** the element is a Code (data type Code), but the definition describes a boolean Indicator with the values true/false. Implementers cannot tell whether to send a code from a list or `true`/`false`, and no code list is associated.
- **Suggested action:** either change the element to an Indicator (e.g. `AdmissionIndicator`), or keep the Code and redefine it as "A code signifying whether the economic operator has been admitted to the tendering process", with an associated code list.

### F8 · Contact. Name: general guidance conflicts with the signatory role

- **Location:** `common/UBL-CommonAggregateComponents-2.5.xsd:10770` (ContactType, `cbc:Name`)
- **Current definition:** "The name of this contact. It is recommended that this be used for a functional name and not a personal name."
- **Issue:** the recommendation suits contact points ("Customer Service"), but ContactType is also used for signatories (F3: "The individual … who signs"). A signature must name the person who signs, so the recommendation cannot be followed there.
- **Suggested action:** limit the recommendation, e.g. "… It is recommended that this be used for a functional name and not a personal name, except where the contact is an individual such as a signatory."

### F9 · Spelling: "reponsible" (16 definitions, 9 files)

- **Issue:** "reponsible" should be "responsible".
- **Occurrences:**
  - "The Party who is reponsible for sending the goods." (10 occurrences, `cac:ConsignorParty`): `common/UBL-CommonAggregateComponents-2.5.xsd:8554` and the documents BillOfLading (364), ForwardingInstructions (357), GoodsCertificate (339), ImportCustomsDeclaration (338), Manifest (336), PackingList (272), TransitCustomsDeclaration (377), Waybill (441).
  - "The Party who is reponsible for the Contract." (`cac:Party` in ContractingParty)
  - "The Party reponsible for this Transport Event." (`cac:ResponsibleParty`)
  - "The Party who is reponsible of the Verified Gross Mass (VGM) according to the SOLAS Convention. …" (`cac:ShipperParty`). This one also has "of", which should be "for".
  - "The Transport Service Provider who is reponsible for the Transportation Service in this Transportation Segment." (`cac:TransportServiceProviderParty`)
  - "The Transport Service Provider who is reponsible for this Transportation Service." (`cac:ResponsibleTransportServiceProviderParty`)
  - "The security officer reponsible for these ISPC requirements." (`cac:SecurityOfficerPerson`)
- **Found with:** `grep -rn reponsible xsd/`

### F10 · Spelling: "eceiving"

- **Location:** `maindoc/UBL-TenderStatusRequest-2.5.xsd:275` (`cac:ContractingParty`)
- **Current definition:** "The Contracting Party eceiving the tender status inquiry."
- **Issue:** "eceiving" should be "receiving". TenderStatusRequest is deprecated in UBL 2.5, but the text is still published.
