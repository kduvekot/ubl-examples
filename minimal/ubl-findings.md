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
| F11 | TransitCustomsDeclaration (document) | definition copied from another document |
| F12 | CatalogueRequest. Provider Party | definition contradicts the specification's roles |
| E1–E80 | (80 elements in about 45 document types) | optional, but essential to the document's defined purpose |

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

### F11 · TransitCustomsDeclaration: the document is defined as an import declaration

- **Location:** `endorsed/xsd/maindoc/UBL-TransitCustomsDeclaration-2.5.xsd:41` (TransitCustomsDeclarationType)
- **Current definition:** "A document that describes an import customs declaration."
- **Issue:** a transit declaration is not an import declaration; ImportCustomsDeclaration is a separate document type. The text appears to be copied from it.
- **Suggested definition:** "A document that describes a transit customs declaration."

### F12 · CatalogueRequest. Provider Party: definition contradicts the roles in the specification

- **Location:** `endorsed/xsd/maindoc/UBL-CatalogueRequest-2.5.xsd:341` (`cac:ProviderParty`, 1..1)
- **Current definition:** "The Party who sends the Catalogue Request."
- **Issue:** the specification (§3.2, Catalogue Request) gives the submitter role as *Contracting Party* and the receiver role as *Seller*. The party that sends a catalogue request is the one asking for the catalogue, not its provider. The element's name (ProviderParty, the catalogue provider) and the specification point to the receiver, while the definition says sender. ReceiverParty is defined as "The Party who receives the Catalogue Request.", so both definitions together leave the provider's role unclear.
- **Suggested definition:** "The Party who provides the requested Catalogue." Alternatively, add a separate requesting party.

## Elements essential to a document's purpose but optional in UBL 2.5

### Why this matters

UBL defines each document type by its purpose ("A document used to request payment", "A document used to update information about prices in an existing Catalogue" …). In many document types, however, the element that carries that purpose is optional. A schema-valid instance may then contain only an identifier and an issue date, and its purpose is implied by the document type alone. That is meaning by absence, which UBL 2.5 §4.4 (IND6) rules out for instances, and it undermines semantic conformance (§4.7, §7.2).

While building minimal but meaningful example documents, these 80 optional elements turned out to be necessary for a document to fulfil its own UBL definition. For each, the TC may want to consider:

- making the element required (minOccurs 1) in the document's schema or in its endorsed cardinality, or
- stating in the document type's definition what a conforming instance must at least contain.

### How the list was made

- **Source:** two independent reviews read every document type as a whole against its UBL definition and the specification's process description, asking whether anything essential to the purpose was missing. They separated "essential for the document to make sense" from "would be nice"; only the first is listed.
- **Choice of element:** where several elements could carry the purpose, the one chosen in the examples is listed. Other choices may be equally valid.
- **Cardinality, definition and location:** taken from the endorsed schemas of the UBL 2.5 package.

### The elements

| # | Document(s) | Element (in class) | UBL cardinality | UBL definition | Why the document needs it | Location |
|---|---|---|---|---|---|---|
| E1 | ApplicationResponse | `cac:DocumentResponse` (ApplicationResponse) | 0..n | A response to a document. | the response is the document's whole content | `endorsed/xsd/maindoc/UBL-ApplicationResponse-2.5.xsd:298` |
| E2 | DocumentStatus | `cac:DocumentResponse` (DocumentStatus) | 0..1 | A response to the document. | the status of a document is its whole content | `endorsed/xsd/maindoc/UBL-DocumentStatus-2.5.xsd:250` |
| E3 | DocumentStatusRequest | `cac:RequestedDocumentReference` (DocumentStatusRequest) | 0..1 | The document about which status is requested. | a status request must say which document it asks about | `endorsed/xsd/maindoc/UBL-DocumentStatusRequest-2.5.xsd:216` |
| E4 | OrderResponse | `cbc:OrderResponseCode` (OrderResponse) | 0..1 | A code signifying the type of response for this Order. | an order response must accept, reject or counter-offer | `endorsed/xsd/maindoc/UBL-OrderResponse-2.5.xsd:203` |
| E5 | BillOfLading | `cac:CarrierParty` (BillOfLading) | 0..1 | The Party who provides the transport of goods between named points. | evidences a contract of carriage: who carries | `endorsed/xsd/maindoc/UBL-BillOfLading-2.5.xsd:376` |
| E6 | BillOfLading | `cac:ConsignorParty` (BillOfLading) | 0..1 | The Party who is reponsible for sending the goods. | ... for whom | `endorsed/xsd/maindoc/UBL-BillOfLading-2.5.xsd:358` |
| E7 | BillOfLading | `cac:Shipment` (BillOfLading) | 0..1 | An identifiable collection of one or more goods items to be transported between the seller party and the buyer party. | ... what is carried | `endorsed/xsd/maindoc/UBL-BillOfLading-2.5.xsd:412` |
| E8 | Waybill | `cac:CarrierParty` (Waybill) | 0..1 | The Party who provides the transport of goods between named points. | issued by the carrier (its issuer by definition) | `endorsed/xsd/maindoc/UBL-Waybill-2.5.xsd:453` |
| E9 | Waybill | `cac:ConsignorParty` (Waybill) | 0..1 | The Party who is reponsible for sending the goods. | issued to the consignor | `endorsed/xsd/maindoc/UBL-Waybill-2.5.xsd:435` |
| E10 | Manifest | `cac:Shipment` (Manifest) | 0..1 | A shipment associated with this manifest. | a manifest that lists nothing is no manifest | `endorsed/xsd/maindoc/UBL-Manifest-2.5.xsd:398` |
| E11 | ForwardingInstructions | `cac:ConsignorParty` (ForwardingInstructions) | 0..1 | The Party who is reponsible for sending the goods. | instructions need someone who instructs | `endorsed/xsd/maindoc/UBL-ForwardingInstructions-2.5.xsd:351` |
| E12 | ForwardingInstructions | `cac:FreightForwarderParty` (ForwardingInstructions) | 0..1 | The Party who combines individual smaller consignments into a single larger shipment (a so-called consolidated consignment or shipment) which is sent to a counterpart who mirrors the consolidator's activity by dividing the consolidated consignment into its original components. | ... and a forwarder who is instructed | `endorsed/xsd/maindoc/UBL-ForwardingInstructions-2.5.xsd:387` |
| E13 | TransportServiceDescription | `cac:TransportationService` (TransportServiceDescription) | 0..n | A transportation service announced in this Transport Service Description. | announces a transport service: which service | `endorsed/xsd/maindoc/UBL-TransportServiceDescription-2.5.xsd:349` |
| E14 | TransportServiceDescription | `cac:TransportServiceProviderParty` (TransportServiceDescription) | 0..1 | The Transport Service Provider. | ... by which provider | `endorsed/xsd/maindoc/UBL-TransportServiceDescription-2.5.xsd:298` |
| E15 | TransportationStatus | `cbc:TransportExecutionStatusCode` (TransportationStatus) | 0..1 | A code signifying the overall status of transport service execution. | a status report must state a status | `endorsed/xsd/maindoc/UBL-TransportationStatus-2.5.xsd:298` |
| E16 | TransportationStatus | `cac:Consignment` (TransportationStatus) | 0..n | A consignment associated with this Transportation Status report. | ... about something | `endorsed/xsd/maindoc/UBL-TransportationStatus-2.5.xsd:314` |
| E17 | TransportationStatusRequest | `cac:Consignment` (TransportationStatusRequest) | 0..n | A consignment regarding which status is requested. | a status request must say what it asks about | `endorsed/xsd/maindoc/UBL-TransportationStatusRequest-2.5.xsd:352` |
| E18 | TransportProgressStatus | `cac:TransportSchedule` (TransportProgressStatus) | 0..n | Describes the status and schedule of the transport means operating the transport service as well as the current location of the transport means. | a progress status must state progress | `endorsed/xsd/maindoc/UBL-TransportProgressStatus-2.5.xsd:315` |
| E19 | TransportExecutionPlan | `cac:MainTransportationService` (TransportExecutionPlan) | 0..1 | Description of the main transportation service referenced in the Transport Execution Plan. | a transport plan must state the transport service | `endorsed/xsd/maindoc/UBL-TransportExecutionPlan-2.5.xsd:551` |
| E20 | TransportExecutionPlanRequest | `cac:MainTransportationService` (TransportExecutionPlanRequest) | 0..1 | A description of the main transportation service referenced in the Transport Execution Plan Request. | as above | `endorsed/xsd/maindoc/UBL-TransportExecutionPlanRequest-2.5.xsd:478` |
| E21 | CommonTransportationReport | `cbc:ReportType` (CommonTransportationReport) | 0..n | A text that identifies the type of report to business users. | a report to authorities must say what it reports | `endorsed/xsd/maindoc/UBL-CommonTransportationReport-2.5.xsd:214` |
| E22 | CommonTransportationReport | `cac:AuthorityParty` (CommonTransportationReport) | 0..1 | The Party who receives the Common Transportation Report. This Party is normally an Authority or regulator. | ... and to which authority | `endorsed/xsd/maindoc/UBL-CommonTransportationReport-2.5.xsd:295` |
| E23 | WeightStatement | `cbc:GrossWeightMeasure` (Shipment) | 0..1 | The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment. | a weight statement must state a weight | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:40833` |
| E24 | PackingList; WasteMovement; WasteNotification; TransitCustomsDeclaration; Waybill | `cac:GoodsItem` (Shipment) | 0..n | A goods item included in this shipment. | describes how goods are packed / which waste is moved: the goods must be stated | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:41130` |
| E25 | CertificateOfOrigin | `cac:OriginAddress` (Shipment) | 0..1 | The region in which the goods have been produced or manufactured, according to criteria laid down for the purposes of application of the customs tariff, or of quantitative restrictions, or of any other measure related to trade. | the origin is the certificate's one essential claim | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:41211` |
| E26 | GoodsCertificate | `cbc:Description` (GoodsCertificate) | 0..n | Textual description of this goods certificate | a certificate must say what it certifies | `endorsed/xsd/maindoc/UBL-GoodsCertificate-2.5.xsd:198` |
| E27 | ImportCustomsDeclaration | `cac:ImporterParty` (ImportCustomsDeclaration) | 0..1 | The Party who makes the import declaration, or on whose behalf the import declaration is made, and who is the owner of the goods or has similar right of disposal over them at the time when the declaration is accepted. | a declaration needs a declarant | `endorsed/xsd/maindoc/UBL-ImportCustomsDeclaration-2.5.xsd:314` |
| E28 | TransitCustomsDeclaration | `cac:TransitExporterParty` (TransitCustomsDeclaration) | 0..1 | The Party who makes the Transit Customs Declaration, or on whose behalf the Transit Customs Declaration is made. This Party is the owner of the Goods or has similar right of disposal over them at the time when the Declaration is accepted. | a declaration needs a declarant | `endorsed/xsd/maindoc/UBL-TransitCustomsDeclaration-2.5.xsd:354` |
| E29 | TransitCustomsDeclaration | `cac:Shipment` (TransitCustomsDeclaration) | 0..n | The shipment related to this trade certificate. | ... and something declared | `endorsed/xsd/maindoc/UBL-TransitCustomsDeclaration-2.5.xsd:456` |
| E30 | Invoice | `cac:AccountingCustomerParty` (Invoice) | 0..1 | The accounting customer party. | a request for payment must say whom it is addressed to | `endorsed/xsd/maindoc/UBL-Invoice-2.5.xsd:707` |
| E31 | CreditNote | `cac:AccountingCustomerParty` (CreditNote) | 0..1 | The accounting customer party. | a credit must say to whom it is due | `endorsed/xsd/maindoc/UBL-CreditNote-2.5.xsd:722` |
| E32 | DebitNote | `cac:AccountingCustomerParty` (DebitNote) | 0..1 | The accounting customer party. | a debit must say who owes it | `endorsed/xsd/maindoc/UBL-DebitNote-2.5.xsd:722` |
| E33 | CreditNote; SelfBilledCreditNote | `cac:Item` (CreditNoteLine) | 0..1 | The item associated with this credit note line. | a credit line must say what is credited | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:12325` |
| E34 | Reminder | `cac:BillingReference` (ReminderLine) | 0..n | A reference to a billing document associated with this reminder line. | a reminder must say what is past due | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:37682` |
| E35 | Reminder | `cbc:DebitLineAmount` (ReminderLine) | 0..1 | The amount debited on this reminder line. | ... and how much | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:37550` |
| E36 | RemittanceAdvice | `cbc:TotalPaymentAmount` (RemittanceAdvice) | 0..1 | The total payable amount for the Remittance Advice (must be positive). | advice of a payment must state the amount paid | `endorsed/xsd/maindoc/UBL-RemittanceAdvice-2.5.xsd:252` |
| E37 | RemittanceAdvice | `cac:BillingReference` (RemittanceAdviceLine) | 0..n | A reference to a billing document associated with this remittance advice line. | a remittance line must say what it pays | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:38000` |
| E38 | RemittanceAdvice | `cbc:DebitLineAmount` (RemittanceAdviceLine) | 0..1 | The amount debited on this remittance advice line. | ... and how much | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:37781` |
| E39 | Statement | `cbc:TotalBalanceAmount` (Statement) | 0..1 | The total amount for the Statement. | a statement of account must state a balance | `endorsed/xsd/maindoc/UBL-Statement-2.5.xsd:252` |
| E40 | Statement | `cac:BillingReference` (StatementLine) | 0..n | A reference to a billing document associated with this statement line. | a statement line must say which item it concerns | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:43190` |
| E41 | Statement | `cbc:BalanceAmount` (StatementLine) | 0..1 | The balance amount on this statement line. | ... and its balance | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:42990` |
| E42 | CataloguePricingUpdate | `cac:RequiredItemLocationQuantity` (CataloguePricingUpdateLine) | 0..n | Updated properties of the item in this catalogue line that are dependent on location and quantity. | a pricing update must carry the updated price | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:5517` |
| E43 | Order; OrderChange; Quotation; RequestForQuotation | `cbc:Quantity` (LineItem) | 0..1 | The quantity of items associated with this line item. | an ordered or quoted line must state the quantity | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:26364` |
| E44 | OrderChange | `cbc:LineStatusCode` (LineItem) | 0..1 | A code signifying the status of this line item with respect to its original state. | a changed line must say that it is changed | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:26347` |
| E45 | DespatchAdvice; DeliveryNote | `cbc:DeliveredQuantity` (DespatchLine) | 0..1 | The quantity despatched (picked up). | a despatch line must state the quantity despatched | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:14881` |
| E46 | ReceiptAdvice | `cac:ReceiptLine` (ReceiptAdvice) | 0..n | A line detailing a kind of item received. | a receipt must say what was received | `endorsed/xsd/maindoc/UBL-ReceiptAdvice-2.5.xsd:472` |
| E47 | ReceiptAdvice | `cbc:ReceivedQuantity` (ReceiptLine) | 0..1 | The quantity received. | ... and how much | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:37029` |
| E48 | WorkReport | `cbc:WorkItemDescription` (WorkReportLine) | 0..n | A description of the specific work item to which this line relates. | a work report must say what work was done | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:54640` |
| E49 | FulfilmentCancellation | `cac:DespatchDocumentReference` (FulfilmentCancellation) | 0..n | A reference to a Despatch Advice associated with this document. | a cancellation must say what it cancels | `endorsed/xsd/maindoc/UBL-FulfilmentCancellation-2.5.xsd:218` |
| E50 | Forecast | `cac:SalesItem` (ForecastLine) | 0..1 | Sales information for the item to which this line applies. | a forecast line must forecast an item and a quantity | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:20013` |
| E51 | ForecastRevision | `cac:SalesItem` (ForecastRevisionLine) | 0..1 | Sales information for the item to which this line applies. | a revision line must carry the revised value | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:20180` |
| E52 | ExceptionCriteria | `cbc:SupplyChainActivityTypeCode` (ExceptionCriteriaLine) | 0..1 | Establishes the criterion for one of the three types of exceptions. There can be three types of exception criteria: Operational, Metric and Forecast Exceptions. This will be set if this Exception is about an Operational Exception. Description could be: A code used to identify an operational exception. Possible values are: CANCELED_ORDERS EMERGENCY_ORDERS ON_HAND ORDERS RECEIPTS SALES SHIPMENTS | a threshold must say what is counted | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:18530` |
| E53 | ExceptionNotification | `cbc:SupplyChainActivityTypeCode` (ExceptionNotificationLine) | 0..1 | Establishes the criterion for one of the three types of exceptions: Operational, performance metric and forecast. This reports an exception notification about an operational exception. Description could be: A code used to identify an operational exception. Possible values are: CANCELED_ORDERS EMERGENCY_ORDERS ON_HAND ORDERS RECEIPTS SALES SHIPMENTS | an exception must say what is counted | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:18778` |
| E54 | ItemInformationRequest | `cbc:SupplyChainActivityTypeCode` (ItemInformationRequestLine) | 0..1 | A code used to identify the type of supply chain activity about which information request is issued. Examples: CANCELED_ORDERS EMERGENCY_ORDERS ON_HAND ORDERS | a request must say which information it requests | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:24996` |
| E55 | RetailEvent | `cbc:Description` (RetailEvent) | 0..n | Definition of the discrete activity affecting supply or demand in the supply chain | an event announcement must say what the event is | `endorsed/xsd/maindoc/UBL-RetailEvent-2.5.xsd:267` |
| E56 | RetailEvent | `cbc:IssueDate` (RetailEvent) | 0..1 | The date, assigned by the sender, on which this document was issued. | ... and be dated, so its period and status can be read | `endorsed/xsd/maindoc/UBL-RetailEvent-2.5.xsd:154` |
| E57 | DigitalAgreement | `cac:ParticipantParty` (DigitalAgreement) | 1..n | The business parties agreeing on a set of digital processes, terms and conditions to ensure interoperability. | minOccurs 1, but an agreement needs at least two parties | `endorsed/xsd/maindoc/UBL-DigitalAgreement-2.5.xsd:289` |
| E58 | ExpressionOfInterestRequest | `cbc:ContractFolderID` (ExpressionOfInterestRequest) | 0..1 | An identifier, assigned by the sender, for the process file (i.e., record) to which this document belongs. | interest must be in a particular procedure | `endorsed/xsd/maindoc/UBL-ExpressionOfInterestRequest-2.5.xsd:149` |
| E59 | ExpressionOfInterestResponse | `cbc:ContractFolderID` (ExpressionOfInterestResponse) | 0..1 | An identifier, assigned by the sender, for the process file (i.e., record) to which this document belongs. | a confirmation must name the procedure | `endorsed/xsd/maindoc/UBL-ExpressionOfInterestResponse-2.5.xsd:149` |
| E60 | ProcurementStatus | `cbc:ContractFolderID` (ProcurementStatus) | 0..1 | An identifier, assigned by the sender, for the process file (i.e., record) to which this document belongs. | a status must identify its procedure | `endorsed/xsd/maindoc/UBL-ProcurementStatus-2.5.xsd:152` |
| E61 | ProcurementStatusRequest | `cbc:ContractFolderID` (ProcurementStatusRequest) | 0..1 | An identifier, assigned by the sender, for the process file (i.e., record) to which this document belongs. | a status request must identify its procedure | `endorsed/xsd/maindoc/UBL-ProcurementStatusRequest-2.5.xsd:152` |
| E62 | TenderWithdrawal | `cbc:ContractFolderID` (TenderWithdrawal) | 0..1 | An identifier, assigned by the sender, for the process file (i.e., record) to which this document belongs. | a withdrawal must identify the tender (procedure + tenderer) | `endorsed/xsd/maindoc/UBL-TenderWithdrawal-2.5.xsd:152` |
| E63 | UnsubscribeFromProcedureRequest | `cbc:ContractFolderID` (UnsubscribeFromProcedureRequest) | 0..1 | An identifier, assigned by the sender, for the process file (i.e., record) to which this document belongs. | unsubscribing needs a procedure | `endorsed/xsd/maindoc/UBL-UnsubscribeFromProcedureRequest-2.5.xsd:149` |
| E64 | UnsubscribeFromProcedureResponse | `cbc:ContractFolderID` (UnsubscribeFromProcedureResponse) | 0..1 | An identifier, assigned by the sender, for the process file (i.e., record) to which this document belongs. | as above | `endorsed/xsd/maindoc/UBL-UnsubscribeFromProcedureResponse-2.5.xsd:149` |
| E65 | PriorInformationNotice | `cac:ProcurementProject` (PriorInformationNotice) | 0..1 | An overall definition of this procurement project. | an intention to buy must name what is to be bought | `endorsed/xsd/maindoc/UBL-PriorInformationNotice-2.5.xsd:480` |
| E66 | QualificationApplicationRequest | `cac:TenderingCriterion` (QualificationApplicationRequest) | 0..n | A criterion supporting Tenderer qualifications. | a qualification request must state the criteria to be answered | `endorsed/xsd/maindoc/UBL-QualificationApplicationRequest-2.5.xsd:403` |
| E67 | QualificationApplicationResponse | `cac:TenderingCriterion` (QualificationApplicationResponse) | 0..n | The criterion as described in the Qualification Application Request. | the answers refer to criteria | `endorsed/xsd/maindoc/UBL-QualificationApplicationResponse-2.5.xsd:419` |
| E68 | TendererQualification | `cbc:OperatingYearsQuantity` (QualifyingParty) | 0..1 | The number of years that this qualifying party has been in operation. | a qualification must state at least one qualifying characteristic (here one of UBL's examples) | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:36335` |
| E69 | ContractAwardNotice | `cac:WinningParty` (TenderResult) | 0..n | A party that is identified as the awarded by a tender result. | an award notice must name the winner | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:46790` |
| E70 | UtilityStatement | `cac:SubscriberConsumption` (UtilityStatement) | 0..n | A utility statement for a particular consumption point. | a statement "containing information on the consumption" must state a consumption | `endorsed/xsd/maindoc/UBL-UtilityStatement-2.5.xsd:409` |
| E71 | DebitNote | `cac:Item` (DebitNoteLine) | 0..1 | The item associated with this debit note line. | a debit line must say what is debited | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:13406` |
| E72 | DebitNote | `cbc:DebitedQuantity` (DebitNoteLine) | 0..1 | The quantity of Items debited in this debit note line. | ... and how much, so the amount reads as quantity x price | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:12990` |
| E73 | Invoice; SelfBilledInvoice | `cbc:InvoicedQuantity` (InvoiceLine) | 0..1 | The quantity (of items) on this invoice line. | an invoice line must state the quantity invoiced, so the amount reads as quantity x price | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:23623` |
| E74 | CreditNote; SelfBilledCreditNote | `cbc:CreditedQuantity` (CreditNoteLine) | 0..1 | The quantity of items credited in this credit note line. | a credit line must state the quantity credited | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:11893` |
| E75 | PurchaseReceipt | `cbc:Quantity` (PurchaseReceiptLine) | 0..1 | The quantity (of items) on this purchase receipt line. | a receipt line must state the quantity purchased | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:35970` |
| E76 | CommonTransportationReport | `cac:Shipment` (CommonTransportationReport) | 0..1 | A shipment to which this common transportation report applies. | a pre-arrival notification must say what arrives | `endorsed/xsd/maindoc/UBL-CommonTransportationReport-2.5.xsd:364` |
| E77 | CataloguePricingUpdate | `cbc:BaseQuantity` (Price) | 0..1 | The quantity at which this price applies. | a price must say for which quantity it applies | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:34371` |
| E78 | TransportProgressStatus | `cac:ActualArrivalTransportEvent` (TransportSchedule) | 0..1 | The actual arrival at a location. | a progress status must state the event, not imply it | `endorsed/xsd/common/UBL-CommonAggregateComponents-2.5.xsd:52725` |
| E79 | TransportationStatus | `cbc:IssueDate` (TransportationStatus) | 0..1 | The date, assigned by the sender, on which this document was issued. | a status must say as of when | `endorsed/xsd/maindoc/UBL-TransportationStatus-2.5.xsd:169` |
| E80 | ProcurementStatus | `cac:TenderSubmissionDeadlinePeriod` (ProcurementStatus) | 0..1 | The period during which tenders must be delivered. | a procedure status must state a status; UBL has no status code, so the open tender period carries it | `endorsed/xsd/maindoc/UBL-ProcurementStatus-2.5.xsd:251` |
