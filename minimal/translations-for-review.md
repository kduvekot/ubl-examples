# Translations for review: minimal UBL 2.5 examples

These words and sentences appear in the minimal UBL example documents (`minimal/layer0`, `minimal/layer1`). Each document has one locale, and its texts are written in that locale's language. Please translate each English term into German, Brazilian Portuguese and Japanese, using the context given.

## Conventions

- **Languages:** German (`de`), Brazilian Portuguese (`pt`), Japanese (`ja-Latn`). English is the source and is used as-is for the US, India and South Africa.
- **Latin script only.** Japanese must be romanized in **Hepburn**, with macrons for long vowels (ō, ū), e.g. *Tōkyō*. No kana or kanji.
- **Party names** are built as *[word for "Example"] + [role] + [number]*, e.g. `Example Buyer 492` in English. They must be visibly fictitious, so no legal forms (GmbH, Ltda., K.K.).
- **Role words** should be the term a business or public-procurement professional in that country would use for that role, not a literal translation. The UBL definition is given as context.
- **Texts** are short business texts. Keep them as short as the English.

## 1. The word "Example" (prefix of all party names)

| English | German | Portuguese (Brazil) | Japanese (Hepburn) |
|---|---|---|---|
| Example | | | |

## 2. Party roles

Each role names a party in a business document. "Context" is the UBL 2.5 definition of the role, and "Documents" lists where it occurs.

| # | English | Context (UBL definition) | Documents | German | Portuguese (Brazil) | Japanese (Hepburn) |
|---|---|---|---|---|---|---|
| R1 | Supplier | The Accounting Supplier Party related to the remittance information reported on this Remittance Advice Line. / The Accounting Supplier Party related to the statement information reported on this Statement Line. | CreditNote, DebitNote, FreightInvoice, Invoice, PurchaseReceipt, Reminder, RemittanceAdvice, SelfBilledCreditNote, SelfBilledInvoice, Statement | | | |
| R2 | Customer | The Accounting Customer Party related to the remittance information reported on this Remittance Advice Line. / The Accounting Customer Party related to the statement information reported on this Statement Line. | FreightInvoice, Reminder, RemittanceAdvice, SelfBilledCreditNote, SelfBilledInvoice, Statement | | | |
| R3 | Seller | The Seller requesting the Item Information. / The party providing the work. | InstructionForReturns, Order, OrderCancellation, OrderChange, OrderResponse, OrderResponseSimple, Quotation, RequestForQuotation, StockAvailabilityReport, WorkReport | | | |
| R4 | Buyer | Association to the Buyer. / The Buyer from whom the Item Information is requested. | Order, OrderCancellation, OrderChange, OrderResponse, OrderResponseSimple, WorkReport | | | |
| R5 | Shipper | The Party that executed the delivery. / The despatch party. | DeliveryNote, DespatchAdvice, ReceiptAdvice | | | |
| R6 | Consignee | The Party to whom the goods or services were delivered. / The customer party. | DeliveryNote, DespatchAdvice, ReceiptAdvice | | | |
| R7 | Retailer | The retailer, who sends this message. / The retailer. | InstructionForReturns, InventoryReport | | | |
| R8 | Inventory Reporter | The Party that is reporting the inventory details. / The party that will receive and use the Stock Availability Report (normally the branch for which the stock is reported). | InventoryReport, StockAvailabilityReport | | | |
| R9 | Provider | The Party who provides this Catalogue. / The Party who provides this piece of Transport Equipment. | Catalogue, CatalogueDeletion, CatalogueItemSpecificationUpdate, CataloguePricingUpdate, CatalogueRequest | | | |
| R10 | Sender | The Party sending this Item Information Request. / The Party sending this document. | ApplicationResponse, AttachedDocument, AwardedNotification, CommonTransportationReport, ExceptionCriteria, ExceptionNotification, Forecast, ForecastRevision, InvoiceStatusRequest, ItemInformationRequest, ProductActivity, RetailEvent, TenderReceipt, TendererQualificationResponse, TradeItemLocationProfile, UnawardedNotification, UtilityStatement, WasteMovement, WasteNotification, WeightStatement | | | |
| R11 | Receiver | The Party receiving this Document. / The Party receiving this Item Information Request. | ApplicationResponse, AttachedDocument, AwardedNotification, Catalogue, CatalogueDeletion, CatalogueItemSpecificationUpdate, CataloguePricingUpdate, CatalogueRequest, CommonTransportationReport, ExceptionCriteria, ExceptionNotification, Forecast, ForecastRevision, InvoiceStatusRequest, ItemInformationRequest, ProductActivity, RetailEvent, TenderReceipt, TendererQualificationResponse, TradeItemLocationProfile, UnawardedNotification, UtilityStatement, WasteMovement, WasteNotification, WeightStatement | | | |
| R12 | Requester | The Party who issued the Enquiry. / The Party who issues this Enquiry. | Enquiry, EnquiryResponse | | | |
| R13 | Responder | The Party who responds to the Enquiry. / The Party who responds to this Enquiry. | Enquiry, EnquiryResponse | | | |
| R14 | Participant | The business parties agreeing on a set of digital processes, terms and conditions to ensure interoperability. | DigitalAgreement | | | |
| R15 | Carrier | The Party who offers the transport service based upon a request from a transport user. / The Party who provides the transport services referenced in the Transport Execution Plan Request. | GoodsItemItinerary, TransportExecutionPlan, TransportExecutionPlanRequest | | | |
| R16 | Logistics Operator | The Party who issues this Manifest.This Party is normally the Logistics Operator. | Manifest | | | |
| R17 | Reporter | The Party who provides this Common Transportation Report. | CommonTransportationReport | | | |
| R18 | Contracting Authority | The Contracting Party eceiving the tender status inquiry. / The Contracting Party issuing the information about the tender status. | CallForTenders, ContractAwardNotice, ContractNotice, ExpressionOfInterestRequest, ExpressionOfInterestResponse, PriorInformationNotice, ProcurementStatus, ProcurementStatusRequest, QualificationApplicationRequest, QualificationApplicationResponse, TenderContract, TenderStatus, TenderStatusRequest, TenderWithdrawal, UnsubscribeFromProcedureRequest, UnsubscribeFromProcedureResponse | | | |
| R19 | Economic Operator | The Economic Operator issuing the Qualification Application Response. / The Economic Operator issuing the expression of interest. | ExpressionOfInterestRequest, ExpressionOfInterestResponse, ProcurementStatus, ProcurementStatusRequest, QualificationApplicationResponse, TenderContract, TenderStatus, TenderStatusRequest, UnsubscribeFromProcedureRequest, UnsubscribeFromProcedureResponse | | | |
| R20 | Tenderer | The Party who submits this Tender. / The economic operator or the main Tenderer in case of a consortium who withdraws the Tender. | Tender, TenderWithdrawal | | | |
| R21 | Main Tenderer | The qualifications of the main tenderer party. | TendererQualification | | | |
| R22 | Depositor | The Party who deposits the bid bond guarantee. | GuaranteeCertificate | | | |
| R23 | Guarantor | The guarantee creditor organisation who has the authority to charge bid bond guarantee credit. | GuaranteeCertificate | | | |
| R24 | Business | The Party who owns these Digital Capabilities. / The Party who owns this Business Card. | BusinessCard, BusinessInformation, DigitalCapability | | | |
| R25 | Exporter | The Party who exports the goods or has similar right of disposal over them at the time of export. / The Party who makes the export declaration, or on whose behalf the export declaration is made, and who is the owner of the goods or has similar right of disposal over them at the time when the declaration is accepted. | ExportCustomsDeclaration | | | |
| R26 | Holder | The Party who holds the Goods Item Passport. This Party is normally the temporary exporter of the Goods. | GoodsItemPassport | | | |
| R27 | Notifier | The Party responsible for providing the Waste Notification information and acting in the role of notifier in the waste movement process. / The Party that acts as the notifier in relation to the Waste Movements covered by this document. | WasteMovement, WasteNotification | | | |
| R28 | Waste Producer | The Party producing the waste material. | WasteMovement, WasteNotification | | | |
| R29 | Customs | The Authority who is legally responsible for processing the Declaration. / The Authority who processes this Customs Declaration. | TransitCustomsDeclaration, WasteNotification | | | |
| R30 | Importing Guarantor | The Party who on behalf of their Customs Authority issues the Proof of Reexportation. This Party is normally a chamber of commerce. / The Party who on behalf of their Customs Authority issues this Document. This Party is normally a chamber of commerce. | ProofOfReexportationReminder, ProofOfReexportationRequest | | | |
| R31 | Exporting Guarantor | The Party who is fiscally responsible for the Goods Item Passport counterfoils which the Customs Party is requesting. This Party is normally a chamber of commerce. / The Party who provides a guarantee for the Goods while being temporarily exported. This Party is normally a chamber of commerce. | ProofOfReexportationReminder, ProofOfReexportationRequest | | | |
| R32 | Issuer | The Party who issues the Immobilized Security Certificate. / The Party who issues the Referenced Document. | CertificateOfOrigin, GoodsCertificate | | | |
| R33 | Endorser | A party providing an endorsement to the CoO. / The Party providing the endorsement. | CertificateOfOrigin | | | |
| R34 | Preparer | The Party who prepares this Certificate of Origin Application. This Party is normally an individual, a group or a body. | CertificateOfOrigin | | | |

## 3. Texts and names

| # | English | Context | German | Portuguese (Brazil) | Japanese (Hepburn) |
|---|---|---|---|---|---|
| T1 | Ballpoint pen, blue | Description of the traded item (an item line in orders, invoices, despatch advices etc.). | | | |
| T2 | Ordered in error | The (general) reason for cancelling an order or a fulfilment. | | | |
| T3 | Ordinary | The type of Certificate of Origin applied for (examples in UBL: Ordinary, Re-export, Commonwealth Preferential). | | | |
| T4 | Approved | The status of an endorsement on a Certificate of Origin. | | | |
| T5 | Is the economic operator enrolled in a trade register? | A question in a public-procurement qualification (ESPD), answered yes/no by the economic operator. | | | |
| T6 | Ordering | A kind of digital trade process that parties agree on or support. | | | |
| T7 | Alex Example | A fictitious personal name: the person who signs a Certificate of Origin application. | | | |
| T8 | Example Store 1 | A fictitious store name: the location where sales were observed. | | | |
| T9 | Office supplies 2026 | The title of a public procurement project. | | | |
