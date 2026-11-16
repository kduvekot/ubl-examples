# Review of document meaning in minimal/layer1, A to O

## Reviewed version

- Repository kduvekot/ubl-examples, branch `claude/elegant-franklin-kk2dky`, commit `01f8672db560e38bf39ff4e0388672c1298a2f4f` (2026-11-16 13:55 UTC, "minimal: findings on UBL 2.5 definitions, for the OASIS UBL TC").
- Scope: the 48 files directly in `minimal/layer1/` from `ApplicationResponse.xml` to `OrderResponse.xml`. `deprecated/` and P to Z are covered by another reviewer.
- Standard: UBL 2.5 OASIS Standard in `minimal/.ubl/os-UBL-2.5/`. Root definitions come from the `ccts:Definition` of each `xsd/maindoc/UBL-<Doc>-2.5.xsd`. Submitter and receiver roles come from section 3.2.x of `UBL-2.5.html`, and the process text from section 2.3.
- Method: I read each document as a whole and compared it with the root definition and the roles. I listed every child the schema allows, with its cardinality and definition. Each XPath below was run with lxml (`etree.xpath`, namespaces `cac`, `cbc` and the document namespace as `d`) against the file named. Scratch scripts are in `/tmp/claude-0/-home-user-ubl-examples/cf0e0c4e-4ca5-5fb4-92ba-ea1bf0fe6f57/scratchpad/review4a/`.

### The test used

A document is a finding only when **the thing its definition says it does is absent**, so that the purpose is carried only by the document type name or by the absence of data. Two rules make that a violation:

- IND6: "The absence of a construct or data in a UBL instance document SHALL NOT carry meaning."
- Section 2.2.2 "Manifest Values": "The receiver cannot presume to know that the sender has omitted an absent value as an assumption ... The onus is on the sender to include all infor[mation]".

The things that count are:
- what a response says;
- what a request asks for or about;
- what a cancellation cancels;
- what an update changes;
- what a report or list contains;
- who the counterparty is, where the definition itself names that party.

Details that make a document richer but are not needed to understand it (prices in a Catalogue, delivery dates, contacts, totals) are **not** findings.

### Common cause

`FILL` (gen_minimal.py l. 222-288) adds optional children *inside* aggregates where chapter 4 needs them. It has no entry for optional **root-level** children that carry a document's purpose. Most findings below share this cause. There is precedent for fixing it: `ResponseType: {cbc:ResponseCode}` and `BillingReferenceType: {cac:InvoiceDocumentReference}` were added for InvoiceStatusRequest/Response for this very reason ("nothing else says ..."). The same reasoning has not been applied to the other document types.

## Findings

### ApplicationResponse

#### DM#F1 · High · An application response with no response and no referenced transaction

- **Where:** `ApplicationResponse.xml`, `count(/d:ApplicationResponse/cac:DocumentResponse)` = 0. The document has 4 children: ID, IssueDate, SenderParty, ReceiverParty.
- **Why:** The root definition is "A document to indicate the application's response to a transaction." `DocumentResponse` [0..unbounded] is "A response to a document". Without it, the document does not say what it responds to or what the response is (accepted, rejected, acknowledged). That is left to absence (IND6). In the catalogue and waste processes the Application Response is the means of "providing consent or rejection" (spec 2.3.5.x), so the answer is the whole content.
- **Condition:** At least one `DocumentResponse` with `Response/ResponseCode` (the answer) and `DocumentReference/ID` (the transaction answered).
- **Options:**
  1. `FILL["ApplicationResponseType"] = {"cac:DocumentResponse"}`. DocumentResponseType already requires Response and DocumentReference, and `FILL["ResponseType"]` already adds ResponseCode. Use a descriptive value as `CODE_VALUES["ResponseCode"] = "ACCEPTED"` does. No UBL default list exists for ResponseCode (checked in `cva/UBL-DefaultDTQ-2.5.cva`).
  2. Leave it out, and record in the generator why an empty application response is acceptable.
- **Needs decision:** no. Option 1 follows the decision already taken for InvoiceStatusResponse.

### BillOfLading

#### DM#F2 · High · A bill of lading that consists only of its own ID

- **Where:** `BillOfLading.xml`, `count(/d:BillOfLading/*)` = 1, `cbc:ID` = `BillOfLading-1`.
- **Why:** The root definition is "A document issued by the party who acts as an agent for a transportation carrier ... to the party who gives instructions for the transportation services (shipper, consignor, etc.) stating the details of the transportation ... The document evidences a contract of carriage ... and the acceptance of responsibility for the goods by the carrier". The roles are Freight Forwarder or Carrier as submitter, Consignor or Freight Forwarder as receiver. The document names no carrier or issuer, no consignor, no goods (`cac:Shipment` [0..1] is absent) and no issue date. It cannot evidence a contract of carriage for anything. The type name alone carries the purpose.
- **Condition:** The issuer (carrier or forwarder), the party it is issued to (consignor) and the goods carried (at least a shipment reference) are stated.
- **Options:** `FILL["BillOfLadingType"] = {"cac:CarrierParty", "cac:ConsignorParty", "cac:Shipment"}`, with schemes for the new roles in `PARTY_SCHEMES`/`ROLE_NAMES`. Shipment then gets its ID through the existing `FILL["ShipmentType"]`.
- **Needs decision:** yes (which roles; schemes for CarrierParty and ConsignorParty).

### CataloguePricingUpdate

#### DM#F3 · High · A pricing update that carries no price

- **Where:** `CataloguePricingUpdate.xml`. `count(//cac:CataloguePricingUpdateLine/*)` = 1 (only `cbc:ID` = `1`), and `count(//cac:Price)` = 0.
- **Why:** The root definition is "A document used to update information about prices in an existing Catalogue." The line is "each line updating a specific catalogue item", but it updates nothing: line 1 of the catalogue `RelatedCatalogueReference-1` gets no new value. The purpose is only implied.
- **Condition:** Each line carries the updated price (`RequiredItemLocationQuantity/Price/PriceAmount`, "Updated properties of the item ... dependent on location and quantity").
- **Options:**
  1. `FILL["CataloguePricingUpdateLineType"] = {"cac:RequiredItemLocationQuantity"}` and `FILL["ItemLocationQuantityType"] = {"cac:Price"}`. PriceAmount then follows from the schema, with currency BRL from the locale and the AmountType value 100.
  2. Also add the item (`Item/Description`) so the reader sees which product the price is for. That would be nice, not essential, because the line ID refers to the catalogue line.
- **Needs decision:** yes (small: which price structure).

### CertificateOfOrigin

#### DM#F4 · High · The issuer's endorsement is given by a party other than the issuer

- **Where:** `CertificateOfOrigin.xml`:
  - `//cac:CertificateOfOriginApplication/cac:IssuerParty/cac:PartyName/cbc:Name` = `Example Issuer 123`;
  - `/d:CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cbc:RoleCode` = `ISSUER`;
  - `/d:CertificateOfOrigin/cac:IssuerEndorsement/cac:EndorserParty/cac:Party/cac:PartyName/cbc:Name` = `Example Endorser 124`.
- **Why:** IssuerParty is "The authorised Organisation who issues the Certificate of Origin", and IssuerEndorsement holds "Issuer Endorsement details". Spec 2.3.5.5 says the exporter submits the application "for authentication to a recognized authority ... This party becomes the Endorser and will issue the Certificate of Origin document." The generator names parties by position (`k = document position x 10 + n`), so the two names state two distinct parties. The document therefore says that party 124 gave the issuer's endorsement for a certificate issued by party 123, which contradicts the process. The generator's own comment on ENDORSERS ("the issuer endorses first") assumes they are the same party.
- **Condition:** The party in the ISSUER endorsement is the IssuerParty: same name, and in later layers the same identifier.
- **Options:**
  1. In `generate()`, give the ISSUER EndorserParty/Party the name and number of the application's IssuerParty. That is a party-identity map instead of numbering by position.
  2. Give the endorsement a different role code, which would contradict the element name IssuerEndorsement. Not recommended.
- **Needs decision:** yes (small: party identity must override numbering by position, which also matters for later layers).

#### DM#F5 · Medium · A certificate of origin that does not state the origin

- **Where:** `CertificateOfOrigin.xml`. `count(//cac:Shipment/*)` = 1 (only `cbc:ID` = `Shipment-1`), and `count(//cac:OriginAddress|//cac:ExportCountry|//cac:GoodsItem)` = 0. The only country in the document is `IssuingCountry/IdentificationCode` = `US`.
- **Why:** Spec 2.3.5.5: "A Certificate Of Origin is a document required by regulatory bodies declaring that goods in a particular international shipment are of a certain origin." IssuingCountry is "The country where the requested CoO will be issued", not the origin of the goods. The certificate's one essential claim, the origin, is missing. A reader who takes `US` as the origin is relying on an implication (IND6).
- **Condition:** The origin of the goods is stated explicitly, for example in `Shipment/GoodsItem/OriginAddress/Country` or `Shipment/OriginAddress/Country` ("The region in which the goods have been produced or manufactured ...").
- **Options:**
  1. A role-specific fill such as `FILL["ShipmentType@Shipment"]` for this document only, adding `cac:OriginAddress`, then `AddressType@OriginAddress: {cac:Country}` with the locale country.
  2. Leave the origin to the referenced shipment, and record in the generator why. That is weak, because the certificate itself is the attestation.
- **Needs decision:** yes.

### CommonTransportationReport

#### DM#F6 · Medium · A report to authorities that reports nothing and names no authority

- **Where:** `CommonTransportationReport.xml`. The XPath `count(/d:CommonTransportationReport/cbc:ReportTypeCode|.../cbc:ReportType|.../cbc:Description|.../cac:AuthorityParty|.../cac:Shipment)` = 0. Present: ID, IssueDate, ReporterParty, SenderParty, ReceiverParty.
- **Why:** The root definition is "A common document used for reporting transport related issues to authorities or regulators". The receiver role is "Authority party", and `AuthorityParty` [0..1] is "The Party who receives the Common Transportation Report. This Party is normally an Authority or regulator." The document neither says what kind of report it is nor whom (which authority) it is for. Only message parties remain. ReceiverParty here is a GLN-identified message receiver, `Beispielempfänger 133`, which is consistent with the GLN rule for this document because the authority is a separate element.
- **Condition:** The document states at least the type of report (`ReportType` text, or `ReportTypeCode` as a descriptive value) and the authority it is for.
- **Options:** `FILL["CommonTransportationReportType"] = {"cbc:ReportType", "cac:AuthorityParty"}`, with ReportType text in `TEXTS` and AuthorityParty identified by name only, as the generator's rule for authorities says (l. 302-304).
- **Needs decision:** yes (which report type).

### ContractAwardNotice

#### DM#F7 · Low · An award notice without the winner

- **Where:** `ContractAwardNotice.xml`, `count(//cac:WinningParty)` = 0. TenderResult holds only `AwardDate` = `2026-08-09`.
- **Why:** The root definition is "A document published by a Contracting Party to announce the awarding of a procurement project." `TenderResult/WinningParty` [0..unbounded] is "A party that is identified as the awarded by a tender result." The notice does state that procedure `ContractFolderID-1` was awarded and when, so it is a credible minimal notice. But the award has no awardee. Compare AwardedNotification, where the winner is the ReceiverParty.
- **Condition:** If an award notice is taken to require the awardee, `WinningParty` is present. Otherwise the generator records that the awardee is deliberately left out.
- **Options:**
  1. `FILL["TenderResultType@TenderResult"]` for this document, adding `cac:WinningParty`, plus a scheme: DUNS (JPCN in JP), as for tenderers.
  2. Keep as is, and add a comment.
- **Needs decision:** yes.

### CreditNote

#### DM#F8 · Medium · A credit note without the debtor, and a line that says nothing

- **Where:** `CreditNote.xml`:
  - `count(/d:CreditNote/cac:AccountingCustomerParty)` = 0;
  - `count(/d:CreditNote/cac:CreditNoteLine/*)` = 1 (only `cbc:ID` = `1`).
- **Why:** The root definition is "A document used to specify credits due to the Debtor from the Creditor", and the receiver role is "Customer Accounting Party". The creditor is present (supplier with CNPJ, `PayableAmount` = `100` BRL). The debtor named in the definition is not, so it is unclear to whom the 100 BRL credit is due. The line has neither item nor amount, so what is credited is also implied. The generator already has the decisions this needs: `PARTY_SCHEMES["AccountingCustomerParty"] = TAX` and `ROLE_NAMES` entries. Reminder.xml and Statement.xml (P-Z) do carry AccountingCustomerParty, because the schema requires it there. So the decision is applied only where the schema forces it.
- **Condition:** The party the credit is due to is stated.
- **Options:**
  1. `FILL["CreditNoteType"] = {"cac:AccountingCustomerParty"}`. Its `cac:Party` follows from the existing `CustomerPartyType` fill, and the CNPJ from the BR rule.
  2. Optionally add `CreditNoteLine/LineExtensionAmount` = 100 so the line agrees with the total. That would be nice; the total already states the credit.
- **Needs decision:** no (option 1 reuses existing decisions).

### DebitNote

#### DM#F9 · Medium · A debit note without the debtor

- **Where:** `DebitNote.xml`, `count(/d:DebitNote/cac:AccountingCustomerParty)` = 0. The creditor (ZA VAT `4000001712`) and `DebitNoteLine/LineExtensionAmount` = `100` ZAR are present.
- **Why:** The root definition is "A document used to specify debits due to the Creditor from the Debtor". The receiver role is "Customer Accounting Party". The debtor is absent. Same cause as DM#F8.
- **Condition:** As DM#F8.
- **Options:** `FILL["DebitNoteType"] = {"cac:AccountingCustomerParty"}`.
- **Needs decision:** no.

### DeliveryNote

#### DM#F10 · Medium · A delivery note without the delivered quantity, referencing line 1 of no order

- **Where:** `DeliveryNote.xml`:
  - `count(//cac:DespatchLine/cbc:DeliveredQuantity)` = 0;
  - `count(//cac:OrderReference)` = 0;
  - `//cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1`.
- **Why:**
  - The root definition is "A document confirming the actual delivery of goods or services, detailing delivered items, quantities, and shipment information." The definition names the quantity, but the line says only that blue ballpoint pens were delivered. The quantity is left open, or read as "1" or "as ordered" by absence (IND6).
  - The schema requires OrderLineReference ([1..unbounded]). Its LineID is "An identifier for the referenced order line, assigned by the buyer", and a line number identifies a line only within its order. With no order reference, the order is implied.
- **Condition:** The despatch line states the quantity delivered, and the referenced order is identified.
- **Options:**
  1. `FILL["DespatchLineType"] = {"cbc:DeliveredQuantity"}` with `QUANTITY_UNITS["DespatchLine/DeliveredQuantity"] = "H87"`.
  2. `FILL["OrderLineReferenceType"] = {"cac:OrderReference"}`. Its required ID follows, as `OrderReference-n` (but see DM#F31).
- **Needs decision:** no for the quantity; yes (small) for where the order reference goes (line or root).

### DespatchAdvice

#### DM#F11 · Medium · A despatch advice without the despatched quantity, referencing line 1 of no order

- **Where:** `DespatchAdvice.xml`. `count(//cac:DespatchLine/cbc:DeliveredQuantity)` = 0, `count(//cac:OrderReference)` = 0, and LineID = `1`.
- **Why:** The root definition is "A document used to describe the despatch or delivery of goods and services". DeliveredQuantity is "The quantity despatched (picked up)". Spec 2.3.5.1.3 has the Receipt Advice "state any shortages from the claimed despatch quantity": the despatch quantity is the figure the process turns on. The order reference has the same problem as in DM#F10.
- **Condition and options:** As DM#F10 (the same `DespatchLineType` fill fixes both).
- **Needs decision:** as DM#F10.

### DigitalAgreement

#### DM#F12 · High · An agreement with one participant

- **Where:** `DigitalAgreement.xml`, `count(/d:DigitalAgreement/cac:ParticipantParty)` = 1 (`Sanpuru Sankasha 201`).
- **Why:** The root definition is "A document used to support business parties agreeing on a set of digital processes ...". ParticipantParty [1..unbounded] is "The business parties agreeing ...". The submitter and receiver roles are both "Agreement Participant". Spec 2.3.8.4 says "Bi-lateral and multi-lateral trading partner agreements". An agreement of one party is not an agreement, so the document contradicts its purpose. Taking only minOccurs instances of a repeatable element is right in general, but not where the meaning needs two.
- **Condition:** At least two ParticipantParty elements, with distinct names and identifiers.
- **Options:**
  1. A small repetition table in the generator, for example `REPEAT = {"DigitalAgreementType/cac:ParticipantParty": 2}`, applied in `content()`. The party numbering (k) already gives distinct values.
  2. No other option keeps the document credible.
- **Needs decision:** yes (new generator mechanism).

### DocumentStatus

#### DM#F13 · High · A status document with no status and no document

- **Where:** `DocumentStatus.xml`, `count(/d:DocumentStatus/*)` = 2 (ID, IssueDate).
- **Why:** The root definition is "A document used to provide information about the status of a collaboration/process associated with a document." `DocumentResponse` [0..1] ("A response to the document") is absent, so the document names neither the document nor its status. Since UBL 2.5 deprecated EnquiryResponse ("Use Document Status instead"), this type carries that role as well. The purpose is entirely implied.
- **Condition:** A `DocumentResponse` with `Response/ResponseCode` and `DocumentReference/ID`.
- **Options:** `FILL["DocumentStatusType"] = {"cac:DocumentResponse"}`, reusing the ResponseType fill and a descriptive ResponseCode, as in InvoiceStatusResponse.
- **Needs decision:** no.

### DocumentStatusRequest

#### DM#F14 · High · A status request that does not say what it asks about

- **Where:** `DocumentStatusRequest.xml`. `count(/d:DocumentStatusRequest/cac:RequestedDocumentReference)` = 0, and `count(/d:DocumentStatusRequest/*)` = 2.
- **Why:** The root definition is "A document used to request the status of a collaboration/process associated with a document." `RequestedDocumentReference` [0..1] is "The document about which status is requested". The request asks about nothing. UBL 2.5 deprecated Enquiry in favour of this type ("Use Document Status Request instead"), so it is the general request.
- **Condition:** `RequestedDocumentReference/ID` is present.
- **Options:** `FILL["DocumentStatusRequestType"] = {"cac:RequestedDocumentReference"}`.
- **Needs decision:** no.

### ExceptionCriteria

#### DM#F15 · Medium · A threshold of "10 pieces" of an unstated measure

- **Where:** `ExceptionCriteria.xml`:
  - `//cbc:ThresholdQuantity` = `10` (unitCode H87);
  - `ThresholdValueComparisonCode` = `FALLS_BELOW_EXCEPTION_VALUE`;
  - `count(//cac:ExceptionCriteriaLine/cbc:SupplyChainActivityTypeCode|.../cbc:PerformanceMetricTypeCode|//cac:ForecastExceptionCriterionLine)` = 0.
- **Why:** The root definition is "thresholds for forecast variance, product activity, and performance history". `SupplyChainActivityTypeCode` is defined as: "There can be three types of exception criteria: Operational, Metric and Forecast Exceptions. This will be set if this Exception is about an Operational Exception ... CANCELED_ORDERS ... ON_HAND ORDERS RECEIPTS SALES SHIPMENTS". None of the three is set. The criterion therefore reads "trigger when 10 pens falls below", without saying 10 of what: sales, stock on hand, orders or forecast. The kind of exception is implied.
- **Condition:** Each criteria line states which of the three kinds it is (and, for an operational exception, which activity).
- **Options:** `CODE_VALUES["ExceptionCriteria:SupplyChainActivityTypeCode"]` with a FILL for the line. Use `SALES`, the value already chosen for ProductActivity, from the values UBL lists in the definition, or `ON_HAND` for a stock-out threshold.
- **Needs decision:** yes (small: which activity).

### ExceptionNotification

#### DM#F16 · Medium · An exception of 8 against 10 pieces of an unstated measure

- **Where:** `ExceptionNotification.xml`:
  - `ComparedValueMeasure` = `8` H87 and `SourceValueMeasure` = `10` H87;
  - `count(//cac:ExceptionNotificationLine/cbc:SupplyChainActivityTypeCode|.../cbc:PerformanceMetricTypeCode|//cac:ForecastException)` = 0.
- **Why:** The root definition is "A document used to notify an exception in forecast variance, product activity, or performance history." The line's `SupplyChainActivityTypeCode` is defined as "Establishes the criterion for one of the three types of exceptions: Operational, performance metric and forecast." As in DM#F15, the reader cannot tell what 8 and 10 count. The PH#F3 fix (8 differs from 10) has not regressed.
- **Condition and options:** As DM#F15, with the same activity code so that the two documents read alike.
- **Needs decision:** yes (small).

### ExpressionOfInterestRequest

#### DM#F17 · High · Interest in no particular tendering process

- **Where:** `ExpressionOfInterestRequest.xml`. The XPath `count(/d:ExpressionOfInterestRequest/cbc:ContractFolderID|.../cac:ProcurementProject|.../cac:ProcurementProjectLotReference|.../cbc:ContractName)` = 0.
- **Why:** The root definition is "An expression of interest to a tendering process. ... Upon reception, the Contracting Party registers the interest of the Economic Operator". With no process file, project, lot or contract name, the contracting authority cannot register the interest for anything, so the purpose fails. The other procurement documents in the set all carry ContractFolderID, because it is required there. Here it is optional (`ContractFolderID` [0..1]), so it was left out.
- **Condition:** The process the interest is for is identified.
- **Options:** `FILL["ExpressionOfInterestRequestType"] = {"cbc:ContractFolderID"}`, or `cac:ProcurementProject`, which already has a Name fill ("Office supplies 2026").
- **Needs decision:** no.

### ExpressionOfInterestResponse

#### DM#F18 · High · A confirmation of registration for no particular process

- **Where:** `ExpressionOfInterestResponse.xml`. The XPath `count(/d:ExpressionOfInterestResponse/cbc:ContractFolderID|.../cac:ProcurementProject|.../cac:ExpressionOfInterestDocumentReference|.../cbc:ContractName)` = 0.
- **Why:** The root definition is "The purpose of this document is to inform the Economic Operator he has been registered as an interested party." It says neither for which process the operator is registered nor which expression of interest it answers.
- **Condition:** The process (ContractFolderID or ProcurementProject) is identified. The answered expression of interest would be nice to have.
- **Options:** `FILL["ExpressionOfInterestResponseType"] = {"cbc:ContractFolderID"}`.
- **Needs decision:** no.

### Forecast

#### DM#F19 · High · A forecast that forecasts no item and no quantity

- **Where:** `Forecast.xml`. `count(//cac:ForecastLine/cac:SalesItem)` = 0. The line has 2 children: ID and `ForecastTypeCode` = `TOTAL`.
- **Why:** The root definition is "A document used to forecast sales or orders." `ForecastLine/SalesItem` [0..1] is "Sales information for the item to which this line applies", and SalesItem requires Quantity and Item. Without it the forecast has period, purpose (`SALES_FORECAST`) and type, but nothing is forecast.
- **Condition:** Each forecast line states the item and the forecast quantity.
- **Options:** `FILL["ForecastLineType"] = {"cac:SalesItem"}`. `QUANTITY_UNITS["SalesItem/Quantity"] = "H87"` and the Item Description fill already exist, so nothing else is needed.
- **Needs decision:** no.

### ForecastRevision

#### DM#F20 · High · A revision line that revises nothing

- **Where:** `ForecastRevision.xml`. `count(//cac:ForecastRevisionLine/cac:SalesItem)` = 0. The line holds ID, `RevisedForecastLineID` = `RevisedForecastLineID-1` and the source forecast's issue date and time.
- **Why:** The root definition is "A document used to revise a Forecast." ForecastRevisionLine is "A line that revises a line in the Forecast". The line identifies what is revised but gives no new value, so the revision itself is implied.
- **Condition:** Each revision line carries the revised value (SalesItem with Quantity and Item).
- **Options:** `FILL["ForecastRevisionLineType"] = {"cac:SalesItem"}`. Optionally add `OriginalDocumentReference` ("The Forecast document being revised"); that would be nice, because the source forecast is already identified by issue date and time.
- **Needs decision:** no.

### ForwardingInstructions

#### DM#F21 · Medium · Instructions with no instructing party, no forwarder and no instruction

- **Where:** `ForwardingInstructions.xml`, `count(/d:ForwardingInstructions/*)` = 2 (ID, `Shipment/ID` = `Shipment-1`).
- **Why:** The root definition is "A document issued to a forwarder, giving instructions regarding the action to be taken for the forwarding of goods described therein. ... The parties who issue this document are commonly referred to as the shipper or consignor, while the parties who receive this document are forwarders, carriers". `ConsignorParty`, `FreightForwarderParty` and `CarrierParty` are all [0..1] and absent. Apart from the shipment reference, nothing says what is to be done. The type name carries "forward this shipment".
- **Condition:** At least the instructing party and the party instructed are present. "Forward Shipment-1", with the parties stated, would then be a minimal but explicit instruction.
- **Options:** `FILL["ForwardingInstructionsType"] = {"cac:ConsignorParty", "cac:FreightForwarderParty"}`, with schemes for the new roles. Destination and other details can wait for a later layer.
- **Needs decision:** yes (schemes for these roles).

### FulfilmentCancellation

#### DM#F22 · High · A cancellation that does not say what it cancels

- **Where:** `FulfilmentCancellation.xml`. `count(/d:FulfilmentCancellation/cac:DespatchDocumentReference|.../cac:ReceiptDocumentReference)` = 0. `CancellationNote` = `Ordered in error`, and there are no parties.
- **Why:** The root definition is "A document used to cancel an entire fulfilment document (Despatch Advice or Receipt Advice)". `CancellationNote` is "The reason for cancellation of **the referenced document**", but no document is referenced. A reason with nothing it applies to, from nobody, cannot be acted on.
- **Condition:** The cancelled Despatch Advice or Receipt Advice is referenced.
- **Options:**
  1. `FILL["FulfilmentCancellationType"] = {"cac:DespatchDocumentReference"}` (a despatch cancelled by the supplier "when ... the order is cancelled", spec 2.3.5.1.4).
  2. A ReceiptDocumentReference instead.
  3. Adding the despatch and delivery parties would be nice, not essential.
- **Needs decision:** yes (small: despatch or receipt).

### GoodsCertificate

#### DM#F23 · Low · A certificate that does not say what it certifies

- **Where:** `GoodsCertificate.xml`, `count(/d:GoodsCertificate/cbc:TypeCode|.../cbc:Description|.../cac:Attestation)` = 0. Present: ID, IssuerParty, `Shipment/ID` = `Shipment-1`.
- **Why:** The root definition is "A document that describes a certificate of goods for importation and exportation". The receiver role is "Legal Authority Party". The type covers many certificates (`TypeCode` "the type of goods certificate", `Attestation` "Any attestations made for the goods"). The document says which shipment it is for and who issues it, but not what is certified. It is Low because the UBL definition itself is generic, so a reader may accept "a goods certificate for Shipment-1".
- **Condition:** The certificate's kind or attestation is stated (for example a `Description` text in the locale language).
- **Options:** `FILL["GoodsCertificateType"] = {"cbc:Description"}` with a TEXTS entry, or keep as is with a comment.
- **Needs decision:** yes.

### ImportCustomsDeclaration

#### DM#F24 · Low · An import declaration made by no one

- **Where:** `ImportCustomsDeclaration.xml`, `count(/d:ImportCustomsDeclaration/*)` = 2 (ID, `Shipment/ID` = `Shipment-1`).
- **Why:** The root definition is "A customs declaration document for importing goods". The submitter role is "Importer Party", and `ImporterParty` [0..1] is "The Party who makes the import declaration, or on whose behalf the import declaration is made". The counterpart ExportCustomsDeclaration has its ExporterParty (required there). Here the declarant is implied. It is Low because the goods are referenced and a customs declaration is understandable without the declarant in the minimal reading.
- **Condition:** The declarant (ImporterParty) is stated, as in the export declaration.
- **Options:** `FILL["ImportCustomsDeclarationType"] = {"cac:ImporterParty"}` with `PARTY_SCHEMES["ImporterParty"] = TAX`, as for ExporterParty.
- **Needs decision:** no (it mirrors the export decision).

### Invoice

#### DM#F25 · Medium · A request for payment addressed to no one

- **Where:** `Invoice.xml`, `count(/d:Invoice/cac:AccountingCustomerParty)` = 0. `PayableAmount` = `100` EUR, and the supplier has a DE VAT number.
- **Why:** The root definition is "A document used to request payment." The receiver role is "Customer Accounting Party". It is unclear whom the payment is requested from. Same cause as DM#F8. Reminder.xml (a payment reminder, P-Z) names its AccountingCustomerParty, but the invoice does not.
- **Condition and options:** As DM#F8, with `FILL["InvoiceType"] = {"cac:AccountingCustomerParty"}`.
- **Needs decision:** no.

### ItemInformationRequest

#### DM#F26 · Medium · A request that does not say which information it requests

- **Where:** `ItemInformationRequest.xml`. The XPath `count(//cac:ItemInformationRequestLine/cbc:SupplyChainActivityTypeCode|.../cbc:ForecastTypeCode|.../cbc:PerformanceMetricTypeCode)` = 0.
- **Why:** The root definition is "A document used to request product activity, forecast, or performance data." The line's `ForecastTypeCode` is defined as "The information request can be either about supply chain activity or about forecasts or about performance metrics, so it will be optional". The three alternatives are distinguished only by these codes, and none is set. The past period (2026-07-15 to 2026-08-11) suggests activity data, but only by implication.
- **Condition:** Each line states which kind of information it requests.
- **Options:** `SupplyChainActivityTypeCode` = `SALES` for the line, the value ProductActivity uses and one the definition lists ("Examples: CANCELED_ORDERS EMERGENCY_ORDERS ON_HAN[D] ...").
- **Needs decision:** yes (small).

### Manifest

#### DM#F27 · High · A manifest that lists nothing

- **Where:** `Manifest.xml`, `count(/d:Manifest/*)` = 2 (ID, SendingLogisticsOperatorParty).
- **Why:** The root definition is "A document listing the contents, cargo, passengers and crew of an airplane, a ship, a truck or a wagon." There is no Shipment, CrewPerson or PassengerPerson, and no means of transport. The document lists nothing and names no vehicle. It has no IssueDate either ([0..1]). The purpose is carried only by the type name.
- **Condition:** At least one listed entry (the cargo as a Shipment reference, or crew or passengers).
- **Options:** `FILL["ManifestType"] = {"cac:Shipment"}`. Shipment's ID fill gives a cargo reference. The vehicle (Shipment/Consignment/.../TransportMeans) can be a later layer.
- **Needs decision:** yes (what the minimal manifest lists).

### Order

#### DM#F28 · Medium · An order line without a quantity

- **Where:** `Order.xml`, `count(//cac:LineItem/cbc:Quantity)` = 0. The item is "Ballpoint pen, blue".
- **Why:** The root definition is "A document used to order goods and services". OrderLine is "specifying a kind of item being ordered", and `LineItem/Quantity` [0..1] is "The quantity of items associated with this line item". Without it, the seller cannot fulfil the order without assuming a quantity (IND6; spec 2.2.2: "the sender cannot rely on the receiver deriving absent values").
- **Condition:** Each ordered line item states its quantity with a unitCode.
- **Options:** `FILL["LineItemType"] = {"cbc:Quantity"}` and `QUANTITY_UNITS["LineItem/Quantity"] = "H87"`. This also affects OrderChange (DM#F29) and the P-Z documents that use LineItem.
- **Needs decision:** no.

### OrderChange

#### DM#F29 · Medium · A changed order line that does not say what changed

- **Where:** `OrderChange.xml`. `count(//cac:LineItem/*)` = 2 (ID `1`, `Item/Description` = `Bōrupen, ao`), and `count(/d:OrderChange/cbc:ID)` = 0.
- **Why:** The root definition is "A document used to specify changes to an existing Order." OrderLine is "An association to one or more (changed) Order Lines." The line repeats the item and changes nothing visible: no quantity, no LineStatusCode, no delivery. The change is implied. (The document has no own ID; it is [0..1] in 2.5, and SequenceNumberID with OrderReference identifies it. That is not a finding.)
- **Condition:** The changed line carries the changed value. With DM#F28 fixed, the quantity is the natural one: a new quantity different from the original order's, which the document cannot show but would state.
- **Options:**
  1. Fix DM#F28 and accept "new quantity 10" as the change.
  2. Additionally add `LineStatusCode` (UBL default list LineStatusCode: `Revised`, per `cva/UBL-DefaultDTQ-2.5.cva`) to state explicitly that the line is changed.
- **Needs decision:** yes.

### OrderResponse

#### DM#F30 · High · An order response that neither accepts, rejects nor counter-offers

- **Where:** `OrderResponse.xml`, `count(/d:OrderResponse/cbc:OrderResponseCode|/d:OrderResponse/cac:OrderLine)` = 0. Present: ID, IssueDate, `OrderReference/ID` = `OrderReference-1`, seller, buyer.
- **Why:** The root definition is "A document used to indicate detailed acceptance or rejection of an Order or to make a counter-offer." `OrderResponseCode` [0..1] is "A code signifying the type of response for this Order". The document does not say which of the three it is. A reader would assume "accepted unchanged" from the absence of lines, which IND6 forbids.
- **Condition:** The type of response is stated.
- **Options:** `CODE_VALUES["OrderResponseCode"] = "ACCEPTED"` with `FILL["OrderResponseType"] = {"cbc:OrderResponseCode"}`. That is a descriptive value without listID, as the decision for codes without a UBL default list prescribes (OrderResponseCode has none in the CVA), and the same answer as InvoiceStatusResponse.
- **Needs decision:** no.

### Cross-document (applies to several of the documents above)

#### DM#F31 · Medium · Reference identifiers repeat across documents, which ties unrelated documents together

- **Where:** `id_for()` numbers labels per document, and `generate()` resets `IDS = {}` for each document, so every document's first reference of a kind is `<Label>-1`. Verified with `string(/*/cbc:ContractFolderID)`, `string(//cac:Shipment/cbc:ID)`, `string(//cac:OrderReference/cbc:ID)` and so on.
  - In scope:
    - `ContractFolderID-1` in AwardedNotification (JP), CallForTenders (US), ContractAwardNotice (JP), ContractNotice (IN) and GuaranteeCertificate (IN);
    - `Shipment-1` in CertificateOfOrigin, ForwardingInstructions, GoodsCertificate, GoodsItemPassport and ImportCustomsDeclaration;
    - `OrderReference-1` in OrderCancellation (DE), OrderChange (JP) and OrderResponse (US);
    - `RelatedCatalogueReference-1` in CatalogueItemSpecificationUpdate and CataloguePricingUpdate;
    - `DocumentReference-1` in InvoiceStatusResponse;
    - `GoodsItemPassportCounterfoil-1` in GoodsItemPassport.
  - Set-wide: ContractFolderID-1 is in 13 files, Shipment-1 in 11, OrderReference-1 in 4 (incl. deprecated/OrderResponseSimple), and GoodsItemPassportCounterfoil-1 in 3 (also in ProofOfReexportation and ProofOfReexportationReminder).
- **Why:** The generator's docstring sets the decision: "The documents are unrelated to each other: values are unique across the set, and references point outside it". Party values follow it (k per document position), but reference values do not. Read together, the set says that:
  - one order `OrderReference-1` is cancelled by a German buyer, changed by a Japanese buyer and answered by a US seller;
  - one procurement file `ContractFolderID-1` is run by contracting authorities in the US, JP and IN. That also contradicts "never cross-country".

  ContractFolderID is "An identifier, assigned by the sender, for the process file", so values could legitimately repeat between different senders. But the set's own rule is uniqueness, and the repetition creates false links.
- **Condition:** Every non-line identifier value occurs in only one document of the set (within the document it may repeat where it denotes the same thing).
- **Options:**
  1. Keep `IDS` across documents, or prefix the number with the document position k as party values do (e.g. `OrderReference-501`).
  2. Use the document type in the value (`OrderChange-OrderReference-1`). That is longer and adds nothing.
- **Needs decision:** no (it applies an existing decision). This is not a regression: earlier these values were all `X` (PH#F9). The fix made them unique within a document only.

## Checked and consistent

Each of these documents states what its definition requires, with parties in roles that match the submitter and receiver roles of spec section 3.2.x.

- **AwardedNotification:** the contracting authority (Sender, JP Corporate Number) informs the winner (Receiver). The procedure is ContractFolderID, and AwardDate = issue date - 3. The receiver is the winner by the document's definition, so no WinningParty is needed. (Its shared ContractFolderID is DM#F31.)
- **BusinessCard:** the BusinessParty is the information. The capabilities are optional detail.
- **BusinessInformation:** the same, for the business registration information.
- **CallForTenders:** the contracting authority defines a named project ("Office supplies 2026"). The year in the name is the period, and dates would be nice to have.
- **Catalogue:** provider to receiver, with one item described. The definition mentions prices, but a catalogue of items without prices is a credible minimal catalogue (GS1 item catalogue), and is not contradicted.
- **CatalogueDeletion:** the deleted catalogue is referenced, from provider to receiver.
- **CatalogueItemSpecificationUpdate:** the line gives the updated description ("technical descriptions") for catalogue line 1 of the referenced catalogue.
- **CatalogueRequest:** a request for a catalogue needs no further content. The parties mirror the element names.
- **ContractNotice:** the authority announces a named project. IssueDate is [0..1] in 2.5, and its absence carries no action.
- **ExportCustomsDeclaration:** the exporter (CNPJ in PartyLegalEntity, BR jurisdiction stated) and the referenced customs declaration of the goods.
- **DigitalCapability:** the business party and one supported process ("Ordering").
- **GoodsItemItinerary:** the TEP reference identifies the transport, and the one segment has a service extent (PORT_TO_PORT) and a provider (LEI). Its time has the DE offset +02:00.
- **GoodsItemPassport:** the holder (JP Corporate Number, the L1#F7 fix is kept), the shipment and the counterfoil. The receiver role (IssuerParty) is not a required content.
- **GuaranteeCertificate:** the guarantor (a bank, LEI), the depositor (DUNS), the liability 100 INR and the procedure, which matches "notify the deposit of a Guarantee".
- **InstructionForReturns:** the seller (producer) instructs the retailer to return 10 pens, matching the roles Seller to Buyer.
- **InventoryReport:** the retailer sends, and a reporting party reports 10 pens in stock. The seller receiver is [0..1]; it is not needed to read the report.
- **InvoiceStatusRequest:** both parties have JP qualified-invoice numbers (an invoice context), and the invoice is referenced by a typed reference.
- **InvoiceStatusResponse:** the referenced document plus ResponseCode `ACCEPTED`. The parties are [0..1], and the answer is explicit. (Its shared DocumentReference-1 is DM#F31.)
- **OrderCancellation:** the order reference, the reason "Irrtümlich bestellt", buyer and seller, matching the roles Buyer to Seller.

Also checked across the scope:
- One locale per document: currency, country, language, UTC offset and tax scheme agree in every file.
- No `X` placeholder is left (no `>X<` in A-O).
- Earlier fixes PH#F1, F2, F3, F5, F6, F8, F14 and F15 and L1#F1, F6, F7, F9 and F10 have not regressed.

## Considered and refuted

- **CommonTransportationReport ReceiverParty identified by GLN although "authorities are identified by name only":** refuted. The authority is the separate `AuthorityParty` ("normally an Authority or regulator"), so ReceiverParty is a message receiver. The missing authority is part of DM#F6.
- **CertificateOfOrigin, the same signatory "Alex Example" for the embassy and the issuer endorsement:** refuted. UBL defines every EndorserParty/SignatoryContact as "The individual representing the exporter who signs the Certificate of Origin application" (already in ubl-findings.md F3), so one exporter representative in both places is consistent with that definition.
- **FulfilmentCancellation reason "Ordered in error" fits an order, not a despatch:** refuted. Spec 2.3.5.1.4 lists "the order is cancelled" as a reason to cancel a Despatch Advice.
- **CatalogueRequest, where ProviderParty is "The Party who sends the Catalogue Request" but the spec's submitter role is the Contracting Party:** this is a UBL inconsistency (out of scope; not in ubl-findings.md, which may want it). The document only mirrors the element names, so it introduces no contradiction of its own.
- **GuaranteeCertificate, a bid bond of 100 INR is implausibly small:** the AmountType value 100 is a recorded decision, and nothing in the document contradicts it.
- **Invoice lines without quantity or amount:** the total states the amount requested. Line amounts are a later layer's job, as the VALUES comment says. This is not essential to the request for payment (the missing payer is DM#F25).
- **OrderChange without its own ID:** `cbc:ID` is [0..1] in 2.5, and SequenceNumberID with OrderReference identifies the change.
- **ContractNotice without IssueDate:** it is optional in 2.5, and the notice is understandable without it.

## Not verified

- Whether `SALES` and `ON_HAND` (DM#F15, F16, F26) are used this way in GS1 CPFR practice. The values come from UBL's own definitions, not from GS1 sources.
- Whether a minimal Contract Award Notice without an awardee is acceptable under any regulatory domain (DM#F7). EU and other notice rules were not consulted.
- The real-world minimum content of a Bill of Lading, Manifest or Forwarding Instructions (DM#F2, F27, F21) under transport law. The findings rest only on the UBL definitions and roles.
- How the P-Z documents are affected by the suggested fills `LineItemType` and `OrderLineReferenceType` (DM#F10, F28): not checked, because they are out of scope.
