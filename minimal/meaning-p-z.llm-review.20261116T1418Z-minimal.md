# Review of document meaning in minimal/layer1, P to Z and deprecated/

## Reviewed version

- Run: `20261116T1418Z-minimal`
- Source: branch `claude/elegant-franklin-kk2dky`, commit `01f8672db560e38bf39ff4e0388672c1298a2f4f`. Files: `minimal/gen_minimal.py` (869 lines), the 49 files `minimal/layer1/[P-Z]*.xml` (PackingList ... WorkReport) and the 8 files `minimal/layer1/deprecated/*.xml`.
- Model: UBL 2.5 OASIS Standard, unpacked at `minimal/.ubl/os-UBL-2.5/`. The document definitions are the `ccts:Definition` of each root type in `xsd/maindoc/UBL-<Doc>-2.5.xsd`. Child definitions come from `xsd/common/UBL-CommonAggregateComponents-2.5.xsd`. The business-process text comes from `UBL-2.5.html` (section 2.3.5.6.6.5 for re-exportation).
- Method: I read each document in scope as a whole and compared it with its root definition and with every optional root child. All XPaths below were run with lxml (`/tmp/.../scratchpad/review4b/xp.py`, `dup.py`, `loc.py`). In the XPaths, `d:` is the document's own namespace. `count(...) = 0` means the element is absent.
- Out of scope, not repeated: `ubl-findings.md` F1–F10, the decisions listed in the assignment, and the findings of the earlier reviews (L1#, PH#) that have been processed.

## Common cause (context for most findings)

The generator adds optional children only per *type* (FILL, LAYER1). At document level, the "the purpose needs it" argument is used in just two places: `QualificationApplicationResponseType: {cac:TenderingCriterion}` (l. 283–287) and `TenderedProjectType: {cac:LegalMonetaryTotal}`. It is not used for the other document types. So many documents contain only the schema minimum: an ID, sometimes one party, sometimes an empty Shipment or line. Nothing in them says what is described, paid, requested or reported. The root element's name is the only carrier of the purpose, so the purpose is implied (IND6 at document level).

Most findings below are therefore instances of one missing decision: a per-document "purpose content" table, applied the same way as the QualificationApplicationResponse rule. Each finding names the smallest content that would make its document make sense.

## Findings

### Across the set

#### DM#F101 · Medium · Reference identifiers repeat across unrelated documents ("values are unique across the set" not applied)

- **Where:** `id_for` (l. 119–131) numbers labels with `IDS`, and `IDS = {}` is reset per document (l. 695). So every first reference of a kind is `<Label>-1` in every document. Verified duplicates (`dup.py`):
  - `Shipment-1` in 11 files, including `PackingList.xml:/d:PackingList/cac:Shipment/cbc:ID`, `Waybill.xml:/d:Waybill/cac:Shipment/cbc:ID`, `WeightStatement.xml:/d:WeightStatement/cac:Shipment/cbc:ID`, `WasteMovement.xml:/d:WasteMovement/cac:Shipment/cbc:ID`, `WasteNotification.xml:/d:WasteNotification/cac:Shipment/cbc:ID` and `deprecated/FreightInvoice.xml:/d:FreightInvoice/cac:Shipment/cbc:ID`.
  - `ContractFolderID-1` in 13 files, including `QualificationApplicationRequest.xml`, `QualificationApplicationResponse.xml`, `Tender.xml`, `TenderContract.xml`, `TenderReceipt.xml`, `TendererQualification.xml`, `TendererQualificationResponse.xml` and `UnawardedNotification.xml`, all at `/d:*/cbc:ContractFolderID`.
  - `GoodsItemPassportCounterfoil-1` at `ProofOfReexportation.xml:/d:ProofOfReexportation/cac:GoodsItemPassportCounterfoil/cbc:ID`, at `ProofOfReexportationReminder.xml:/d:ProofOfReexportationReminder/cac:GoodsItemPassportCounterfoil/cbc:ID` and at `GoodsItemPassport.xml:/d:GoodsItemPassport/cac:GoodsItemPassportCounterfoil/cbc:ID` (a JP document).
  - `LicensePlateID-1` at `TransportProgressStatus.xml:/d:TransportProgressStatus/cac:TransportMeans/cac:RoadTransport/cbc:LicensePlateID` (JP, +09:00) and at `TransportProgressStatusRequest.xml:/d:TransportProgressStatusRequest/cac:TransportMeans/cac:RoadTransport/cbc:LicensePlateID` (IN, +05:30).
  - `Consignment-1` at `TransportExecutionPlan.xml` and `TransportExecutionPlanRequest.xml` (`/d:*/cac:Consignment/cbc:ID`).
  - `OrderReference-1` in `deprecated/OrderResponseSimple.xml` and in three Order* files.
  - `ParentDocumentReference-1` in `UtilityStatement.xml` and `deprecated/EnquiryResponse.xml`.
  - `DocumentReference-1` in `ProofOfReexportation.xml` and `InvoiceStatusResponse.xml`.
- **Why:** The docstring (l. 15–16) says "The documents are unrelated to each other: values are unique across the set, and references point outside it". Only the document IDs (`<Doc>-1`) and the party identifiers (`k` = position × 10 + n, l. 417) follow this. Read as a set, the duplicates say the opposite:
  - the ProofOfReexportation and its Reminder prove or chase the counterfoil of the set's own GoodsItemPassport;
  - a progress-status request in India and a status in Japan concern the same vehicle;
  - 13 procurement documents in five locales belong to one process file ("An identifier ... for the process file (i.e., record) to which this document belongs").
  
  The comment at l. 116–118 claims only that "no reference equals any document's ID", which is true, but that is a weaker property than the stated decision. PH#F9 was fixed only partly. Its "Considered and refuted" accepted the shared ContractFolderID only "if they are one procedure", and that is now excluded by the decision.
- **Condition:** Every identifier value outside the line and sequence IDs occurs in at most one document of the set.
- **Options:** (1) Keep one `IDS` counter across the set instead of one per document, giving `Shipment-1` … `Shipment-11`. (2) Number by document position, as for parties, e.g. `Shipment-61`. (3) Add a set-wide uniqueness check to `check()`.
- **Needs decision:** no (applies a decision already taken).

### Procurement

#### DM#F102 · Medium · PriorInformationNotice: an intention to buy, with nothing to buy

- **Where:** `PriorInformationNotice.xml`: `count(/d:PriorInformationNotice/cac:ProcurementProject)` = 0 and `count(/d:PriorInformationNotice/cbc:ContractFolderID)` = 0. The document contains only `cbc:IssueDate` and `cac:ContractingParty` (`Example Contracting Authority 541`).
- **Why:** The definition is "A document used by a contracting party to declare the intention to buy goods, services, or works during a specified period". This one declares neither what is to be bought nor the period. The generator already has a reason and a value for this case: `ProcurementProjectType: {cbc:Name}` (l. 244–247, "a particular undertaking gets a name") with `ProcurementProject/Name` = "Office supplies 2026". It is just never reached, because ProcurementProject is optional at root.
- **Condition:** A PIN names the object of the intended purchase.
- **Options:** (1) Add `cac:ProcurementProject` at root, which gets its Name from FILL. "2026" in the name then covers the period loosely. (2) Also add `cbc:PlannedDate` ("planned ... for publication of the contract notice"), which a later layer could do instead.
- **Needs decision:** yes.

#### DM#F103 · Medium · ProcurementStatus, ProcurementStatusRequest, TenderStatus, TenderStatusRequest: status of an unidentified procedure

- **Where:** `count(/d:X/cbc:ContractFolderID | /d:X/cac:ProcurementProject | /d:X/cbc:ID)` = 0 in `ProcurementStatus.xml`, `ProcurementStatusRequest.xml`, `deprecated/TenderStatus.xml` and `deprecated/TenderStatusRequest.xml`. Each has only IssueDate, ContractingParty and EconomicOperatorParty.
- **Why:**
  - ProcurementStatus is "A document sent by a Contracting Party to an Economic Operator describing the status of a procurement procedure, Project, or Lot".
  - The Request is "asking about the details and status of a procurement procedure, Project, or Lot".
  - TenderStatus and TenderStatusRequest have the same wording for "a tendering procedure".
  
  None of the four says which procedure. The parties are right (sender and receiver as defined), but the subject is implied. The 13 sibling procurement documents identify their procedure by ContractFolderID (required there). Here it is optional, so it was dropped.
- **Condition:** A status (request) identifies the procedure, project or lot it is about.
- **Options:** (1) Add `cbc:ContractFolderID` at root for these four document types. (2) Add `cac:ProcurementProject`, whose Name comes from FILL. Either way, the status itself (periods, ProcedureCode) can stay for a later layer. Identification is the essential part.
- **Needs decision:** yes.

#### DM#F104 · Medium · TenderWithdrawal: nothing says which tender is withdrawn

- **Where:** `TenderWithdrawal.xml`: `count(/d:TenderWithdrawal/cbc:ContractFolderID | /d:TenderWithdrawal/cac:TenderDocumentReference | /d:TenderWithdrawal/cbc:ID)` = 0.
- **Why:** The definition is "A document sent by an Economic Operator to a Contracting Party with the intention of withdrawing a previously sent Tender document". The parties fit: the TendererParty is "the economic operator ... who withdraws the Tender". But neither the procedure nor the tender is identified, so the withdrawal applies to no tender.
- **Condition:** The withdrawn tender, or at least its procedure, is identified.
- **Options:** (1) `cac:TenderDocumentReference` ("A reference to a received Tender"), whose ID points outside the set. (2) `cbc:ContractFolderID`.
- **Needs decision:** yes.

#### DM#F105 · Medium · UnsubscribeFromProcedureRequest / Response: unsubscribe from which procedure?

- **Where:** `count(/d:UnsubscribeFromProcedureRequest/cbc:ContractFolderID | .../cac:ProcurementProject)` = 0. `count(/d:UnsubscribeFromProcedureResponse/cbc:ContractFolderID | .../cac:ProcurementProject | .../cac:UnsubscribeToProcedureDocumentReference)` = 0.
- **Why:** The Request is "A request to unsubscribe from a tendering procedure ... allows the Economic Operator to be removed from the list of interested parties". The Response is "confirming that the latter has been unsubscribed from a tendering procedure". The procedure is the object of both documents, and it is absent from both.
- **Condition:** The procedure is identified.
- **Options:** `cbc:ContractFolderID` in both. For the Response, alternatively `cac:UnsubscribeToProcedureDocumentReference` pointing outside the set.
- **Needs decision:** yes.

#### DM#F106 · High · QualificationApplicationRequest defines no criterion, while the Response repeats one "as described in the Request"

- **Where:** `QualificationApplicationRequest.xml`: `count(/d:QualificationApplicationRequest/cac:TenderingCriterion)` = 0. The document has only ContractFolderID, IssueDate and ContractingParty.
- **Why:** The definition is "A document issued by a buyer defining how the Exclusion Grounds and the Selection Criteria should be addressed in a Single Procurement Document". The criteria are the whole content, and there are none. The generator added a criterion to the *Response* for exactly this reason (l. 283–287: the response "repeats the question it answers ('the criterion as described in the Qualification Application Request')"). The question is defined in the Request in the first place, so the rule is applied to the answer but not to the question.
- **Condition:** The Request contains at least the criterion that a Response would repeat.
- **Options:** Add `"QualificationApplicationRequestType": {"cac:TenderingCriterion"}` to FILL. The existing `TenderingCriterionType` / `TenderingCriterionPropertyType` fills and the `TenderingCriterionProperty/Description` text then apply unchanged (in ja-Latn here).
- **Needs decision:** no (the same rule as the Response).

#### DM#F107 · Low · QualificationApplicationResponse: the generator comment contradicts the document

- **Where:** `gen_minimal.py` l. 277–282: "The answer is a neutral text placeholder, not an Indicator: "true" would state a real answer; a later layer fills it". But `"ResponseValueType": {"cbc:ResponseIndicator"}` and `INDICATOR_VALUES["ResponseIndicator"] = "true"` (l. 64–65) give `QualificationApplicationResponse.xml:/d:QualificationApplicationResponse/cac:TenderingCriterionResponse/cac:ResponseValue/cbc:ResponseIndicator` = `true`.
- **Why:** The document itself is coherent: the question "Is the economic operator enrolled in a trade register?" is answered yes, which fits the definition "A self-declaration of an economic operator, stating that it ... meets the Selection Criteria". But the stated reason for the value is stale, and "every decision and its reason is a comment" is the generator's contract.
- **Condition:** The comment matches the value.
- **Options:** Rewrite l. 279–280 ("the answer is an Indicator, true: yes to the one property in the same document, needing no evidence").
- **Needs decision:** no.

#### DM#F108 · Low · TendererQualification: a qualifying party with no qualification

- **Where:** `TendererQualification.xml`: `count(/d:TendererQualification/cac:TendererPartyQualification/cac:MainQualifyingParty/*)` = 1 (only `cac:Party`), and `count(/d:TendererQualification/cac:Evidence)` = 0.
- **Why:** The definition is "A document declaring the qualifications of a tenderer". FILL l. 228–230 adds `QualifyingParty/Party` because "nothing else says who the tenderer is". That answers *who*, but the document declares no qualification. QualifyingPartyType has only optional qualification content (e.g. `cac:Declaration`, `cac:CompletedTask`, `cbc:OperatingYearsQuantity`), and none is present.
- **Condition:** At least one declared qualification, or an explicit decision that the party alone counts as the declaration.
- **Options:** (1) Add one qualification in QualifyingParty, e.g. a `cac:Declaration` (needs its own reasoning). (2) Accept the gap and record why in the generator.
- **Needs decision:** yes.

### Commerce and finance

#### DM#F109 · High · RemittanceAdvice: details of a payment, without any amount or payee reference

- **Where:** `RemittanceAdvice.xml`: `count(//cbc:*[@currencyID])` = 0, `count(//cac:BillingReference)` = 0, and `count(/d:RemittanceAdvice/cac:RemittanceAdviceLine/*)` = 1 (only `cbc:ID`).
- **Why:** The definition is "A document that specifies details of an actual payment". The payer (AccountingCustomerParty) and payee (AccountingSupplierParty) are present and in the right roles, but no amount is paid and no invoice is settled. The line is "A line specifying a balance", and it has no balance. The other monetary documents in scope all carry the set's amount of 100 (VALUES l. 37–43). This one has none, so the payment is entirely implied.
- **Condition:** The paid amount is stated, and preferably also what it pays.
- **Options:**
  1. Root `cbc:TotalPaymentAmount` ("must be positive") = 100 EUR.
  2. On the line, `cbc:CreditLineAmount` or `cbc:BalanceAmount` = 100, plus `cac:BillingReference` pointing outside the set.
  
  With (1) alone, the remittance is credible but says nothing of which invoice it pays.
- **Needs decision:** yes.

#### DM#F110 · Medium · Reminder: no line says what is past due

- **Where:** `Reminder.xml`: `count(/d:Reminder/cac:ReminderLine/*)` = 1 (only `cbc:ID`), and `count(//cbc:DueDate | //cac:BillingReference)` = 0. The only amount is `/d:Reminder/cac:LegalMonetaryTotal/cbc:PayableAmount` = `100` USD.
- **Why:** The definition is "A document used to remind a customer of payments past due". ReminderLine is "A line describing a payment past due", and its only content is an ID. The 100 USD total is payable now, but nothing says it was due earlier or which invoice it belongs to. "Past due" is carried only by the document type.
- **Condition:** The reminder line identifies the overdue item: the invoice and/or its amount.
- **Options:** `ReminderLine/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` (outside the set), plus `ReminderLine/cbc:DebitLineAmount` = 100, which equals the total.
- **Needs decision:** yes.

#### DM#F111 · Medium · Statement: a statement of account without a balance

- **Where:** `Statement.xml`: `count(//cbc:*[@currencyID])` = 0, `/d:Statement/cbc:DocumentCurrencyCode` = `USD`, and `count(/d:Statement/cac:StatementLine/*)` = 1 (only `cbc:ID`).
- **Why:** The definition is "A document used to report the status of orders, billing, and payment. This document is a statement of account". It reports no status. There is no total, no line balance and no referenced bill. PH's "Considered and refuted" accepted the lone currency code as not a *filler*, because it is required. That still holds. The point here is different: the document as a whole states no account position, so the currency qualifies nothing.
- **Condition:** At least one balance.
- **Options:** Root `cbc:TotalBalanceAmount` = 100 USD, and/or `StatementLine/cbc:BalanceAmount` = 100 with a BillingReference.
- **Needs decision:** yes.

#### DM#F112 · Medium · SelfBilledCreditNote: 100 BRL credited for nothing

- **Where:** `SelfBilledCreditNote.xml`: `count(/d:SelfBilledCreditNote/cac:CreditNoteLine/*)` = 1 (only `cbc:ID`), `count(//cac:BillingReference | //cac:DiscrepancyResponse)` = 0, and `/d:SelfBilledCreditNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `100`.
- **Why:** The definition is "A credit note created by the debtor in a self billing arrangement with a creditor". The roles fit: the customer issues and the supplier is credited. But the line credits no item, no quantity and no amount, and no invoice or reason is referenced. Compare `SelfBilledInvoice.xml`, whose InvoiceLine has an Item ("Ballpoint pen, blue") because the schema requires one. CreditNoteLine/Item is optional, so the credit note lost the only thing that says what is credited.
- **Condition:** The credit says what it credits: an item or a referenced invoice.
- **Options:** (1) `"CreditNoteLineType": {"cac:Item"}` in FILL. The existing `Item/Description` text then applies, and the same change would cover CreditNote (A-O scope). (2) `cac:BillingReference` to the credited self-billed invoice, outside the set.
- **Needs decision:** yes.

#### DM#F113 · Medium · ReceiptAdvice: a receipt of nothing

- **Where:** `ReceiptAdvice.xml`: `count(/d:ReceiptAdvice/cac:ReceiptLine | /d:ReceiptAdvice/cac:Shipment | /d:ReceiptAdvice/cac:DespatchDocumentReference | /d:ReceiptAdvice/cac:OrderReference)` = 0.
- **Why:** The definition is "A document used to describe the receipt of goods and services or as a reply to a despatch advice". The parties are right: DeliveryCustomerParty (consignee, GLN) and DespatchSupplierParty (shipper, GLN). But no goods are described and no despatch advice is answered, so both readings of the definition are empty.
- **Condition:** Either a ReceiptLine (item and received quantity) or a reference to the despatch advice being answered.
- **Options:** (1) `cac:ReceiptLine` with `cbc:ReceivedQuantity unitCode="H87"` = 10 and `cac:Item` (needs a QUANTITY_UNITS entry). (2) `cac:DespatchDocumentReference` outside the set.
- **Needs decision:** yes.

#### DM#F114 · High · FreightInvoice (deprecated): invoices the goods, not the freight

- **Where:** `deprecated/FreightInvoice.xml:/d:FreightInvoice/cac:InvoiceLine/cac:Item/cbc:Description` = `Caneta esferográfica, azul`, next to `/d:FreightInvoice/cac:Shipment/cbc:ID` = `Shipment-1`.
- **Why:** The definition is "(Deprecated) A document stating the charges incurred for a logistics service", and `cac:Shipment` is "Details about one or more shipments covered by this Freight Invoice". The shipment is what was carried, and the invoice line should be the logistics service. Instead, the line's item is the ballpoint pen, i.e. the goods. That turns it into a sales invoice for pens with a shipment attached, which contradicts the purpose. The cause is that `TEXTS["Item/Description"]` (l. 501) is one text for every Item in the set.
- **Condition:** The FreightInvoice line's item is a logistics service.
- **Options:** A document-qualified text key, e.g. `"FreightInvoice:Item/Description"` = ("Road freight", "Straßentransport", "Frete rodoviário", "Rikujō yusō"), with `text_for` looking up `DOC + ":" + key` first (as `date_for` already does). The wording needs a check.
- **Needs decision:** no (the wording yes).

#### DM#F115 · Medium · WorkReport: 10 hours of unspecified work

- **Where:** `WorkReport.xml:/d:WorkReport/cac:WorkReportLine/cbc:Quantity` = `10` (`unitCode="HUR"`), with `count(/d:WorkReport/cac:WorkReportLine/*)` = 2 (ID and Quantity only).
- **Why:** The definition is "A document used to report work performed". WorkReportLine is "specifying the work performed". The quantity of work is there, but the work itself is not: there is no `cbc:WorkItemDescription` ("A description of the specific work item to which this line relates") and no WorkItemID. Every other line type in the set gets an `Item/Description` for exactly this reason. WorkReportLine has no Item, so it got nothing.
- **Condition:** The line says what work was done.
- **Options:** `"WorkReportLineType": {"cbc:WorkItemDescription"}` with a text in pt, e.g. "Manutenção de equipamentos de escritório" (to be checked).
- **Needs decision:** yes.

#### DM#F116 · Medium · UtilityStatement: a consumption supplement without consumption

- **Where:** `UtilityStatement.xml`: `count(/d:UtilityStatement/cac:SubscriberConsumption | /d:UtilityStatement/cac:MainOnAccountPayment)` = 0, while `/d:UtilityStatement/cbc:UtilityStatementTypeCode` = `ELECTRICITY`.
- **Why:** The definition is "A supplement to an Invoice or Credit Note, containing information on the consumption of services provided by utility suppliers". The parent invoice is referenced and the service type is named, but no consumption is given. The generator's own comment (l. 190–191) anticipates it: "a later layer with consumption must match (KWH)". Consumption, though, is what the document is for, not a refinement.
- **Condition:** At least one consumption point with a consumed quantity.
- **Options:** `cac:SubscriberConsumption` with its required children and a quantity in KWH. This is a larger addition, so it could also be the first item of a later layer, recorded as such.
- **Needs decision:** yes.

### Retail and inventory

#### DM#F117 · Medium · RetailEvent: a planned event of unknown kind, with no issue date

- **Where:** `RetailEvent.xml`: `/d:RetailEvent/cbc:RetailEventStatusCode` = `PLANNED` and `/d:RetailEvent/cac:Period/cbc:StartDate` = `2026-08-26`. `count(/d:RetailEvent/cbc:IssueDate | /d:RetailEvent/cbc:Description | /d:RetailEvent/cbc:RetailEventName | /d:RetailEvent/cac:PromotionalEvent | /d:RetailEvent/cac:MiscellaneousEvent)` = 0.
- **Why:** The definition is "basic information about retail events (such as promotions, product introductions, and community or environmental events) that affect supply or demand". The document gives a period and a state, but no event: neither a Description ("Definition of the discrete activity affecting supply or demand") nor a name nor a type. The generator chose `PLANNED` because the event is "announced two weeks ahead" (l. 187–188, DATE_OFFSETS l. 105–106). But IssueDate is absent, so "two weeks ahead" cannot be read from the document. PLANNED relative to what is implied.
- **Condition:** The event says what it is, and the document is dated, so that the period and the status can be read against the issue date.
- **Options:** (1) `cbc:Description`, e.g. "Back-to-school promotion" (en). (2) `cbc:IssueDate` = D.
- **Needs decision:** yes.

#### DM#F118 · Medium · StockAvailabilityReport (deprecated): the receiving branch is named "Inventory Reporter"

- **Where:** `deprecated/StockAvailabilityReport.xml:/d:StockAvailabilityReport/cac:InventoryReportingParty/cac:PartyName/cbc:Name` = `Beispielbestandsmelder 732`. The cause is `ROLE_NAMES["InventoryReportingParty"]` (l. 467).
- **Why:** In this document, InventoryReportingParty is "The party that will receive and use the Stock Availability Report (normally the branch for which the stock is reported)". The report itself is "sent by a Seller (for example a producer) to a Buyer (for example a retailer)". So the party is the recipient. In InventoryReport the same element is "The Party that is reporting the inventory details", and there the name fits. One name per role gives this party the opposite role here (semantic conformance, §4.7/§7.2). The sender, SellerSupplierParty, is correct.
- **Condition:** The party name follows the element's definition in this document.
- **Options:** A document-qualified role name, e.g. `"StockAvailabilityReport/InventoryReportingParty": ("Branch", "Filiale", "Filial", "Shiten")`, looked up as PARTY_SCHEMES already does with `Document/Role` keys.
- **Needs decision:** no (the wording yes).

### Transport and logistics

#### DM#F119 · High · TransportServiceDescription, TransportationStatus, TransportationStatusRequest: documents that are only an ID

- **Where:** `count(/d:TransportServiceDescription/*)` = 1, `count(/d:TransportationStatus/*)` = 1 and `count(/d:TransportationStatusRequest/*)` = 1. Each contains only `cbc:ID`.
- **Why:**
  - TransportServiceDescription: "A document sent by a transport service provider to announce the availability of a transport service". It announces no service and names no provider.
  - TransportationStatus: "A document to circulate reports of transportation status or changes in status (events) among a group of participants". It reports no status, about nothing.
  - TransportationStatusRequest: "A document requesting a Transportation Status report". It does not say what about.
  
  The root name is the only content of each. Compare TransportServiceDescriptionRequest, where the required TransportationService with `DOOR_TO_DOOR` gives the request a subject.
- **Condition:** Each document has the one element its purpose is about.
- **Options:**
  - TransportServiceDescription: `cac:TransportationService` with `cbc:TransportServiceCode` (a code already decided for the request), or `cac:TransportServiceProviderParty` (LEI, as in TEP).
  - TransportationStatus: `cbc:TransportExecutionStatusCode` ("the overall status of transport service execution", a descriptive value without listID per the decisions) plus `cac:Consignment`.
  - TransportationStatusRequest: `cac:Consignment` ("A consignment regarding which status is requested") or `cbc:ShippingOrderID`.
- **Needs decision:** yes.

#### DM#F120 · Medium · PackingList and Waybill: an ID and an empty shipment

- **Where:** `count(/d:PackingList/*)` = 2 and `count(/d:PackingList/cac:Shipment/*)` = 1. `count(/d:Waybill/*)` = 2 and `count(/d:Waybill/cac:Shipment/*)` = 1. Each has only `Shipment/cbc:ID` = `Shipment-1`.
- **Why:**
  - PackingList is "A document describing how goods are packed". No goods and no packages are described.
  - Waybill is "A transport document describing a shipment. It is issued by the party who undertakes to provide transportation services ... to the party who gives instructions". It describes no shipment and names neither the carrier nor the consignor.
  
  FILL gives ShipmentType its ID as "a transaction reference" (l. 240–243). That identifies the shipment but describes nothing.
- **Condition:** The packing list has at least one package (or goods item) of the shipment. The waybill has at least the carrier, i.e. its issuer by definition.
- **Options:**
  - PackingList: `Shipment/cac:TransportHandlingUnit` or `cac:GoodsItem` with the Item description.
  - Waybill: `cac:CarrierParty` (LEI or GLN by the existing logistics rules) and optionally `cac:ConsignorParty`.
- **Needs decision:** yes.

#### DM#F121 · Medium · TransitCustomsDeclaration: declares nothing

- **Where:** `count(/d:TransitCustomsDeclaration/*)` = 2: `cbc:ID` and `/d:TransitCustomsDeclaration/cac:CustomsParty/cac:PartyName/cbc:Name` = `Example Customs 831`.
- **Why:** The document has a customs authority ("The Authority who is legally responsible for processing the Declaration"), but no declarant (`cac:TransitExporterParty`, "The Party who makes the Transit Customs Declaration") and no goods (`cac:Shipment`). A declaration with neither a declarant nor declared goods is not a credible instance. (The root definition reads "describes an import customs declaration", which looks like a copy from ImportCustomsDeclaration. See Not verified.)
- **Condition:** A declarant and what is declared.
- **Options:** `cac:TransitExporterParty` (TAX, like ExporterParty) and `cac:Shipment` (ID from FILL).
- **Needs decision:** yes.

#### DM#F122 · Medium · TransportProgressStatus: a status with no status

- **Where:** `TransportProgressStatus.xml`: `count(/d:TransportProgressStatus/cac:TransportSchedule | .../cbc:StatusAvailableIndicator | .../cac:SenderParty | .../cac:ReceiverParty)` = 0. Only `cac:TransportMeans/cac:RoadTransport/cbc:LicensePlateID` = `LicensePlateID-1` is present.
- **Why:** The definition is "A document sent from a Transportation Network Manager to a Transport Service Provider giving the status of the whereabouts and schedule of the transport means". The vehicle is named, but no whereabouts or schedule is given. The request counterpart (TransportProgressStatusRequest: vehicle plus date) is credible as it is. The answer is not.
- **Condition:** The document gives a status, or says that none is available.
- **Options:** (1) `cac:TransportSchedule`: its required SequenceNumeric 1 and StatusLocation, whose Name comes from FILL. (2) `cbc:StatusAvailableIndicator` = false, a real minimal answer ("no progress information available"). That needs its reason recorded.
- **Needs decision:** yes.

#### DM#F123 · High · WeightStatement: no weight

- **Where:** `WeightStatement.xml`: `count(//cbc:*[@unitCode])` = 0 and `count(/d:WeightStatement/cac:Shipment/*)` = 1 (only `cbc:ID`).
- **Why:** The definition is "A document used to report weight or verified mass measurements in the transport chain". The Shipment is "The relevant shipment information with details on the transport equipment weight or mass measurements, including verified gross mass (VGM)". The document reports no measurement, so its sole purpose is implied.
- **Condition:** At least one weight measure with a unit.
- **Options:** `Shipment/cbc:GrossWeightMeasure unitCode="KGM"` with a value per MEASURE_VALUES/UNITS. For VGM, a TransportEquipment-level measure, which needs more structure.
- **Needs decision:** yes.

#### DM#F124 · Medium · WasteMovement and WasteNotification: no waste

- **Where:** `count(/d:WasteMovement/cac:Shipment/*)` = 1 and `count(/d:WasteNotification/cac:Shipment/*)` = 1 (only `cbc:ID` = `Shipment-1`).
- **Why:** WasteMovement is "A document used to report the transport of waste", and WasteNotification is "used to notify the competent authorities of planned movements of waste". In both, the Shipment is defined as "The relevant shipment information describing the planned transport and the waste material". All the parties are there (sender, receiver, notifier, producer, and the customs authority in the notification), but no waste is described. The waste stays implied by the document type.
- **Condition:** The shipment names the waste material.
- **Options:** `Shipment/cac:GoodsItem` with a description of the waste. A document-qualified text is needed, because the set's Item text is a ballpoint pen.
- **Needs decision:** yes.

#### DM#F125 · Low · TransportExecutionPlan / Request: a transport with no route and no service

- **Where:** `count(/d:TransportExecutionPlan/cac:FromLocation | .../cac:ToLocation | .../cac:MainTransportationService | .../cac:TransportUserParty)` = 0, and the same for `TransportExecutionPlanRequest`. `Consignment/*` holds only `cbc:ID` (`Consignment-1` in both, see DM#F101).
- **Why:** TransportExecutionPlanRequest is "sent by a transport user to request a transport service". TransportExecutionPlan is "used in the negotiation of a transport service between a transport user and a transport service provider". The provider and the consignment are there, so who carries and what is identified. Where to and what service are not, and the user (the requester) is absent from both. This is weaker than the other transport findings: a negotiation can start from a consignment reference alone. Hence Low.
- **Condition:** (if accepted) the documents state either the service or the route.
- **Options:** `cac:MainTransportationService` with the already decided TransportServiceCode, or From/To locations with Names from FILL.
- **Needs decision:** yes.

### Deprecated: enquiries

#### DM#F126 · Medium · Enquiry and EnquiryResponse: no question and no answer

- **Where:** `count(/d:Enquiry/cbc:Description | /d:Enquiry/cac:Attachment)` = 0 and `count(/d:EnquiryResponse/cbc:Description | /d:EnquiryResponse/cac:Attachment)` = 0.
- **Why:** Enquiry is "A document sent by a requestor to a responder requesting information about a particular business process". EnquiryResponse is "answering a particular enquiry". The parties and the reference to the enquiry are right, but neither the question nor the answer is present. Their only carriers in these document types are Description (free text) and Attachment.
- **Condition:** The enquiry asks something and the response answers it.
- **Options:** `cbc:Description` in both: a question in en (Enquiry) and an answer in de (EnquiryResponse).
- **Needs decision:** yes.

## Checked and consistent

- **ProductActivity (en, GLN):** a store's sales of 10 pens (`SALES`) over the four weeks before the issue date, at a named store, from sender to receiver. It fits "the movement of goods at specified retail locations".
- **ProofOfReexportation:** a counterfoil plus a reference to evidence matches "a proof that goods have been re-exported". The parties are optional and the counterfoil identifies the case (apart from DM#F101).
- **ProofOfReexportationReminder (en):** the importing guarantor ("on behalf of their Customs Authority issues this Document") reminds the exporting guarantor about a referenced request under `TEMPORARY_ADMISSION`, the ATA procedure. This matches UBL 2.5 §2.3.5.6.6.5 (apart from DM#F101).
- **ProofOfReexportationRequest (en):** the guarantor pair and the GoodsItemPassportID match the process description ("the importing guarantor party ... sending a Request For Proof Of Re-exportation to the exporting guarantor party").
- **PurchaseReceipt (DE):** the seller (VAT), 100 EUR and one line with an item. A credible cash receipt. (UBL F1 on the line Item definition is out of scope.)
- **Quotation (BR) and RequestForQuotation (JP):** the seller is the issuer or addressee as defined, with one item line. The Quotation has a total. The buyer is optional and is the other end of the exchange.
- **SelfBilledInvoice (ZA):** the customer issues and the supplier is billed, both with VAT numbers. One item line and 100 ZAR.
- **Tender (JP):** the tenderer offers 100 JPY for the tendered project in the identified process file. It matches "makes a formal offer ... to a contracting authority".
- **TenderContract (en):** the authority announces an award (AwardDate D−3) to an economic operator, within its file. (UBL F6 is out of scope.)
- **TenderReceipt (BR):** the authority (sender) acknowledges, with registered date and time, to the tenderer (receiver) within the file. The tender is identified enough by the file plus the receiver.
- **TendererQualificationResponse (en):** the authority notifies admission (`AdmissionCode` true, UBL F7 out of scope), resolved D−3.
- **UnawardedNotification (JP):** the authority tells a tenderer of an award made D−3 within the file.
- **TradeItemLocationProfile (BR):** a one-year replenishment profile (Period = EffectivePeriod) for one item, from sender to receiver.
- **TransportProgressStatusRequest (IN):** a provider asks for the status of a named vehicle, on a dated and timed request. A credible minimal request (apart from DM#F101).
- **TransportServiceDescriptionRequest (DE):** a request for information on a `DOOR_TO_DOOR` service. The definition's subject is present.
- **QualificationApplicationResponse (en):** the question and the yes-answer are in the same document, between the right parties (only the comment, DM#F107).
- **AttachedDocument (deprecated, de):** a real PDF, the parent document ID, sender and receiver. It matches "a wrapper that allows a document of any kind to be packaged".
- **OrderResponseSimple (deprecated, pt):** the seller accepts (`true`) a referenced order from the buyer. It is complete for "simple acceptance ... of an entire Order".
- **Locale per document:** for all 57 files in scope, the languageID, currencyID, country codes, UTC offsets and schemeIDs belong to one locale (`loc.py`).

## Considered and refuted

- **One-line documents with a total but no quantity or line amount** (PurchaseReceipt, Quotation, SelfBilledInvoice, FreightInvoice): a reader can see what was bought and the total. The quantity refines the document but is not needed for it to make sense. The deferral is also recorded (VALUES comment l. 37–42). Not a finding at document level.
- **Quotation and RFQ without a BuyerCustomerParty:** both are defined around the seller ("request a Quotation ... from a Seller"). The buyer is the other end of the exchange and is not needed for the meaning.
- **ProofOfReexportation without parties or date:** the counterfoil and the evidence reference are what the proof consists of. The issuer is the other end of the request.
- **TenderReceipt without TenderDocumentReference:** within a process file, the receiver (the tenderer) and the registered date and time identify the receipt.
- **Japanese Corporate Number for JP economic operators and authorities, and LEI for the BR/DE/US/IN contracting authorities:** decisions already taken, applied consistently in scope.
- **Dates:** every date in scope is in order: award and resolution dates before issue, activity periods before issue, validity periods from issue, RetailEvent in the future. Only the missing RetailEvent IssueDate is raised (DM#F117).
- **Earlier findings regressed?** No. L1#F16 (UtilityStatement receiver now D-U-N-S), PH#F1/F2 (amounts and quantities now 100/10), PH#F3, PH#F6 and PH#F18 are fixed in the files in scope. PH#F9 is fixed only for equality with document IDs; the rest is DM#F101.

## Not verified

- **TransitCustomsDeclaration root definition** ("A document that describes an import customs declaration"): this looks like a UBL definition error and is not in `ubl-findings.md`. It is outside the scope of this review, so it is only noted here for the owner.
- **Suggested texts** ("Road freight", "Back-to-school promotion", the pt/de/ja-Latn wordings, "Filiale"/"Shiten") are not checked by native speakers or against any terminology source.
- **Business-process descriptions:** only the re-exportation process (UBL 2.5 §2.3.5.6.6.5) and the root and child definitions were read in full. The intermodal, waste and procurement process chapters were not checked for further role constraints.
- **Regeneration:** no option was generated, schema-validated or run through `check()`. The required children of the suggested aggregates (e.g. SubscriberConsumption, TransportSchedule) were checked only for TransportSchedule (SequenceNumeric, StatusLocation).
- **A-O documents** that share a cause (CreditNote line, DespatchAdvice, InventoryReport, the Order* references in DM#F101) are cited only for comparison. They are covered by the A-O review.
