# UBL 2.5 Document-Level Semantic Analysis

Index of all 101 UBL 2.5 document types with party element analysis.
Each document has a dedicated markdown file mapping party-related schema
elements to the [26+C canonical parties](../session-decisions.md#53-final-agreed-party-set-26--consumer).

## Documents by Process Group

### Group B — Order-to-Cash

| Document | Party Elements | File |
|---|---|---|
| [CreditNote](CreditNote.md) | 12: DespatchDocumentReference, DeliveryNoteDocumentReference, OriginatorDocumentReference, BuyerReference, AccountingSupplierParty, AccountingCustomerParty, PayeeParty, BuyerCustomerParty, SellerSupplierParty, TaxRepresentativeParty, Delivery, DeliveryTerms | `CreditNote.md` |
| [DebitNote](DebitNote.md) | 12: DespatchDocumentReference, DeliveryNoteDocumentReference, OriginatorDocumentReference, BuyerReference, AccountingSupplierParty, AccountingCustomerParty, PayeeParty, BuyerCustomerParty, SellerSupplierParty, TaxRepresentativeParty, Delivery, DeliveryTerms | `DebitNote.md` |
| [FreightInvoice](FreightInvoice.md) | 6: DespatchDocumentReference, OriginatorDocumentReference, AccountingSupplierParty, AccountingCustomerParty, PayeeParty, TaxRepresentativeParty | `FreightInvoice.md` |
| [Invoice](Invoice.md) | 14: DespatchDocumentReference, DeliveryNoteDocumentReference, OriginatorDocumentReference, BuyerReference, AccountingSupplierParty, AccountingCustomerParty, PayeeParty, BuyerCustomerParty, SellerSupplierParty, OriginatorCustomerParty, BeneficiaryParty, TaxRepresentativeParty, Delivery, DeliveryTerms | `Invoice.md` |
| [InvoiceStatusRequest](InvoiceStatusRequest.md) | 2: SenderParty, ReceiverParty | `InvoiceStatusRequest.md` |
| [InvoiceStatusResponse](InvoiceStatusResponse.md) | 2: SenderParty, ReceiverParty | `InvoiceStatusResponse.md` |
| [Order](Order.md) | 9: OriginatorDocumentReference, BuyerCustomerParty, SellerSupplierParty, OriginatorCustomerParty, BeneficiaryParty, FreightForwarderParty, AccountingCustomerParty, Delivery, DeliveryTerms | `Order.md` |
| [OrderCancellation](OrderCancellation.md) | 5: OriginatorDocumentReference, BuyerCustomerParty, SellerSupplierParty, OriginatorCustomerParty, BeneficiaryParty | `OrderCancellation.md` |
| [OrderChange](OrderChange.md) | 10: OriginatorDocumentReference, BuyerCustomerParty, SellerSupplierParty, OriginatorCustomerParty, BeneficiaryParty, FreightForwarderParty, AccountingCustomerParty, AccountingSupplierParty, Delivery, DeliveryTerms | `OrderChange.md` |
| [OrderResponse](OrderResponse.md) | 10: OriginatorDocumentReference, SellerSupplierParty, BuyerCustomerParty, OriginatorCustomerParty, BeneficiaryParty, FreightForwarderParty, AccountingSupplierParty, AccountingCustomerParty, Delivery, DeliveryTerms | `OrderResponse.md` |
| [OrderResponseSimple](OrderResponseSimple.md) | 6: SellerSupplierParty, BuyerCustomerParty, OriginatorCustomerParty, BeneficiaryParty, AccountingSupplierParty, AccountingCustomerParty | `OrderResponseSimple.md` |
| [PurchaseReceipt](PurchaseReceipt.md) | 3: AccountingSupplierParty, AccountingCustomerParty, Delivery | `PurchaseReceipt.md` |
| [Quotation](Quotation.md) | 6: SellerSupplierParty, BuyerCustomerParty, OriginatorCustomerParty, BeneficiaryParty, Delivery, DeliveryTerms | `Quotation.md` |
| [Reminder](Reminder.md) | 4: AccountingSupplierParty, AccountingCustomerParty, PayeeParty, TaxRepresentativeParty | `Reminder.md` |
| [RemittanceAdvice](RemittanceAdvice.md) | 3: AccountingCustomerParty, AccountingSupplierParty, PayeeParty | `RemittanceAdvice.md` |
| [RequestForQuotation](RequestForQuotation.md) | 6: OriginatorCustomerParty, BeneficiaryParty, SellerSupplierParty, BuyerCustomerParty, Delivery, DeliveryTerms | `RequestForQuotation.md` |
| [SelfBilledCreditNote](SelfBilledCreditNote.md) | 12: DespatchDocumentReference, DeliveryNoteDocumentReference, OriginatorDocumentReference, BuyerReference, AccountingCustomerParty, AccountingSupplierParty, PayeeParty, BuyerCustomerParty, SellerSupplierParty, TaxRepresentativeParty, Delivery, DeliveryTerms | `SelfBilledCreditNote.md` |
| [SelfBilledInvoice](SelfBilledInvoice.md) | 14: DespatchDocumentReference, DeliveryNoteDocumentReference, OriginatorDocumentReference, BuyerReference, AccountingCustomerParty, AccountingSupplierParty, BuyerCustomerParty, SellerSupplierParty, OriginatorCustomerParty, BeneficiaryParty, PayeeParty, TaxRepresentativeParty, Delivery, DeliveryTerms | `SelfBilledInvoice.md` |
| [Statement](Statement.md) | 7: AccountingSupplierParty, AccountingCustomerParty, BuyerCustomerParty, SellerSupplierParty, OriginatorCustomerParty, BeneficiaryParty, PayeeParty | `Statement.md` |

### Group C — Fulfilment

| Document | Party Elements | File |
|---|---|---|
| [BillOfLading](BillOfLading.md) | 3: ConsignorParty, CarrierParty, FreightForwarderParty | `BillOfLading.md` |
| [CertificateOfOrigin](CertificateOfOrigin.md) | 4: ExporterParty, ImporterParty, EndorserParty, IssuerEndorsement | `CertificateOfOrigin.md` |
| [DeliveryNote](DeliveryNote.md) | 7: DespatchSupplierParty, DeliveryCustomerParty, BuyerCustomerParty, SellerSupplierParty, OriginatorCustomerParty, BeneficiaryParty, DespatchLine | `DeliveryNote.md` |
| [DespatchAdvice](DespatchAdvice.md) | 7: DespatchSupplierParty, DeliveryCustomerParty, BuyerCustomerParty, SellerSupplierParty, OriginatorCustomerParty, BeneficiaryParty, DespatchLine | `DespatchAdvice.md` |
| [ForwardingInstructions](ForwardingInstructions.md) | 3: ConsignorParty, CarrierParty, FreightForwarderParty | `ForwardingInstructions.md` |
| [FulfilmentCancellation](FulfilmentCancellation.md) | 7: DespatchDocumentReference, BuyerCustomerParty, SellerSupplierParty, DeliveryCustomerParty, DespatchSupplierParty, OriginatorCustomerParty, BeneficiaryParty | `FulfilmentCancellation.md` |
| [GoodsCertificate](GoodsCertificate.md) | 9: ExporterParty, ImporterParty, WarehouseParty, ConsignorParty, ConsigneeParty, FreightForwarderParty, IssuerParty, LegalAuthorityParty, ApplicantParty | `GoodsCertificate.md` |
| [InstructionForReturns](InstructionForReturns.md) | 3: SellerSupplierParty, RetailerCustomerParty, ManufacturerParty | `InstructionForReturns.md` |
| [Manifest](Manifest.md) | 4: SendingLogisticsOperatorParty, AuthorityParty, ConsignorParty, ConsigneeParty | `Manifest.md` |
| [PackingList](PackingList.md) | 3: ConsignorParty, CarrierParty, FreightForwarderParty | `PackingList.md` |
| [ReceiptAdvice](ReceiptAdvice.md) | 5: DespatchDocumentReference, DeliveryCustomerParty, DespatchSupplierParty, BuyerCustomerParty, SellerSupplierParty | `ReceiptAdvice.md` |
| [Waybill](Waybill.md) | 5: SenderParty, ReceiverParty, ConsignorParty, CarrierParty, FreightForwarderParty | `Waybill.md` |
| [WeightStatement](WeightStatement.md) | 5: SenderParty, ReceiverParty, WeighingParty, ShipperParty, ResponsibleParty | `WeightStatement.md` |

### Group D — Transport

| Document | Party Elements | File |
|---|---|---|
| [CommonTransportationReport](CommonTransportationReport.md) | 4: ReporterParty, AuthorityParty, SenderParty, ReceiverParty | `CommonTransportationReport.md` |
| [GoodsItemItinerary](GoodsItemItinerary.md) | 2: SenderParty, ReceiverParty | `GoodsItemItinerary.md` |
| [TransportExecutionPlan](TransportExecutionPlan.md) | 11: SenderParty, ReceiverParty, TransportUserParty, TransportServiceProviderParty, BillToParty, TransportServiceDescriptionDocumentReference, TransportServiceProviderResponseRequiredPeriod, MainTransportationService, AdditionalTransportationService, ServiceStartTimePeriod, ServiceEndTimePeriod | `TransportExecutionPlan.md` |
| [TransportExecutionPlanRequest](TransportExecutionPlanRequest.md) | 12: SenderParty, ReceiverParty, TransportUserParty, TransportServiceProviderParty, PayeeParty, BillToParty, TransportServiceDescriptionDocumentReference, TransportServiceProviderResponseDeadlinePeriod, MainTransportationService, AdditionalTransportationService, ServiceStartTimePeriod, ServiceEndTimePeriod | `TransportExecutionPlanRequest.md` |
| [TransportProgressStatus](TransportProgressStatus.md) | 3: SenderParty, ReceiverParty, SourceIssuerParty | `TransportProgressStatus.md` |
| [TransportProgressStatusRequest](TransportProgressStatusRequest.md) | 2: SenderParty, ReceiverParty | `TransportProgressStatusRequest.md` |
| [TransportServiceDescription](TransportServiceDescription.md) | 6: SenderParty, ReceiverParty, TransportServiceDescriptionRequestDocumentReference, TransportServiceProviderParty, ServiceChargePaymentTerms, TransportationService | `TransportServiceDescription.md` |
| [TransportServiceDescriptionRequest](TransportServiceDescriptionRequest.md) | 4: SenderParty, ReceiverParty, TransportServiceProviderParty, TransportationService | `TransportServiceDescriptionRequest.md` |
| [TransportationStatus](TransportationStatus.md) | 3: SenderParty, ReceiverParty, UpdatedDeliveryTransportEvent | `TransportationStatus.md` |
| [TransportationStatusRequest](TransportationStatusRequest.md) | 2: SenderParty, ReceiverParty | `TransportationStatusRequest.md` |

### Group E — Customs & Border

| Document | Party Elements | File |
|---|---|---|
| [ExportCustomsDeclaration](ExportCustomsDeclaration.md) | 1: ExporterParty | `ExportCustomsDeclaration.md` |
| [GoodsItemPassport](GoodsItemPassport.md) | 8: IssuerParty, HolderParty, RepresentativeParty, ExportingGuarantorParty, ImportingGuarantorParty, ExportingCustomsParty, ImportingCustomsParty, IssuerEndorsement | `GoodsItemPassport.md` |
| [ImportCustomsDeclaration](ImportCustomsDeclaration.md) | 6: ImporterParty, ConsignorParty, ConsigneeParty, FreightForwarderParty, CustomsParty, NotifierParty | `ImportCustomsDeclaration.md` |
| [ProofOfReexportation](ProofOfReexportation.md) | 3: ExportingCustomsParty, ImportingGuarantorParty, ExportingGuarantorParty | `ProofOfReexportation.md` |
| [ProofOfReexportationReminder](ProofOfReexportationReminder.md) | 4: ImportingGuarantorParty, ExportingGuarantorParty, ImportingCustomsParty, IssuerEndorsement | `ProofOfReexportationReminder.md` |
| [ProofOfReexportationRequest](ProofOfReexportationRequest.md) | 3: ImportingGuarantorParty, ExportingGuarantorParty, ImportingCustomsParty | `ProofOfReexportationRequest.md` |
| [TransitCustomsDeclaration](TransitCustomsDeclaration.md) | 6: TransitExporterParty, ConsignorParty, ConsigneeParty, FreightForwarderParty, CustomsParty, NotifierParty | `TransitCustomsDeclaration.md` |

### Group F — Catalogue

| Document | Party Elements | File |
|---|---|---|
| [Catalogue](Catalogue.md) | 4: ProviderParty, ReceiverParty, SellerSupplierParty, ContractorCustomerParty | `Catalogue.md` |
| [CatalogueDeletion](CatalogueDeletion.md) | 4: ReceiverParty, ProviderParty, SellerSupplierParty, ContractorCustomerParty | `CatalogueDeletion.md` |
| [CatalogueItemSpecificationUpdate](CatalogueItemSpecificationUpdate.md) | 4: ProviderParty, ReceiverParty, SellerSupplierParty, ContractorCustomerParty | `CatalogueItemSpecificationUpdate.md` |
| [CataloguePricingUpdate](CataloguePricingUpdate.md) | 4: ProviderParty, ReceiverParty, SellerSupplierParty, ContractorCustomerParty | `CataloguePricingUpdate.md` |
| [CatalogueRequest](CatalogueRequest.md) | 4: ReceiverParty, ProviderParty, SellerSupplierParty, ContractorCustomerParty | `CatalogueRequest.md` |
| [ItemInformationRequest](ItemInformationRequest.md) | 4: SenderParty, ReceiverParty, BuyerCustomerParty, SellerSupplierParty | `ItemInformationRequest.md` |

### Group G — Procurement

| Document | Party Elements | File |
|---|---|---|
| [AwardedNotification](AwardedNotification.md) | 2: SenderParty, ReceiverParty | `AwardedNotification.md` |
| [CallForTenders](CallForTenders.md) | 4: ContractingParty, OriginatorCustomerParty, BeneficiaryParty, ReceiverParty | `CallForTenders.md` |
| [ContractAwardNotice](ContractAwardNotice.md) | 4: ContractingParty, OriginatorCustomerParty, BeneficiaryParty, ReceiverParty | `ContractAwardNotice.md` |
| [ContractNotice](ContractNotice.md) | 4: ContractingParty, OriginatorCustomerParty, BeneficiaryParty, ReceiverParty | `ContractNotice.md` |
| [ExpressionOfInterestRequest](ExpressionOfInterestRequest.md) | 2: EconomicOperatorParty, ContractingParty | `ExpressionOfInterestRequest.md` |
| [ExpressionOfInterestResponse](ExpressionOfInterestResponse.md) | 2: EconomicOperatorParty, ContractingParty | `ExpressionOfInterestResponse.md` |
| [GuaranteeCertificate](GuaranteeCertificate.md) | 3: GuarantorParty, InterestedParty, BeneficiaryParty | `GuaranteeCertificate.md` |
| [PriorInformationNotice](PriorInformationNotice.md) | 4: ContractingParty, OriginatorCustomerParty, BeneficiaryParty, ReceiverParty | `PriorInformationNotice.md` |
| [ProcurementStatus](ProcurementStatus.md) | 4: ContractingParty, EconomicOperatorParty, DocumentProviderParty, TenderRecipientParty | `ProcurementStatus.md` |
| [ProcurementStatusRequest](ProcurementStatusRequest.md) | 2: ContractingParty, EconomicOperatorParty | `ProcurementStatusRequest.md` |
| [QualificationApplicationRequest](QualificationApplicationRequest.md) | 2: ContractingParty, EconomicOperatorParty | `QualificationApplicationRequest.md` |
| [QualificationApplicationResponse](QualificationApplicationResponse.md) | 2: ContractingParty, EconomicOperatorParty | `QualificationApplicationResponse.md` |
| [Tender](Tender.md) | 6: TendererParty, TendererQualificationDocumentReference, SubcontractorParty, ContractingParty, OriginatorCustomerParty, BeneficiaryParty | `Tender.md` |
| [TenderContract](TenderContract.md) | 3: ContractingParty, EconomicOperatorParty, ReceiverParty | `TenderContract.md` |
| [TenderReceipt](TenderReceipt.md) | 2: SenderParty, ReceiverParty | `TenderReceipt.md` |
| [TenderStatus](TenderStatus.md) | 4: ContractingParty, EconomicOperatorParty, DocumentProviderParty, TenderRecipientParty | `TenderStatus.md` |
| [TenderStatusRequest](TenderStatusRequest.md) | 2: ContractingParty, EconomicOperatorParty | `TenderStatusRequest.md` |
| [TenderWithdrawal](TenderWithdrawal.md) | 2: ContractingParty, TendererParty | `TenderWithdrawal.md` |
| [TendererQualification](TendererQualification.md) | 2: TendererPartyQualification, ContractingParty | `TendererQualification.md` |
| [TendererQualificationResponse](TendererQualificationResponse.md) | 2: SenderParty, ReceiverParty | `TendererQualificationResponse.md` |
| [UnawardedNotification](UnawardedNotification.md) | 2: SenderParty, ReceiverParty | `UnawardedNotification.md` |
| [UnsubscribeFromProcedureRequest](UnsubscribeFromProcedureRequest.md) | 2: EconomicOperatorParty, ContractingParty | `UnsubscribeFromProcedureRequest.md` |
| [UnsubscribeFromProcedureResponse](UnsubscribeFromProcedureResponse.md) | 2: EconomicOperatorParty, ContractingParty | `UnsubscribeFromProcedureResponse.md` |
| [WorkReport](WorkReport.md) | 3: SellerSupplierParty, BuyerCustomerParty, ApproverParty | `WorkReport.md` |

### Group H — CPFR / Retail

| Document | Party Elements | File |
|---|---|---|
| [ExceptionCriteria](ExceptionCriteria.md) | 4: SenderParty, ReceiverParty, BuyerCustomerParty, SellerSupplierParty | `ExceptionCriteria.md` |
| [ExceptionNotification](ExceptionNotification.md) | 4: SenderParty, ReceiverParty, BuyerCustomerParty, SellerSupplierParty | `ExceptionNotification.md` |
| [Forecast](Forecast.md) | 4: SenderParty, ReceiverParty, BuyerCustomerParty, SellerSupplierParty | `Forecast.md` |
| [ForecastRevision](ForecastRevision.md) | 4: SenderParty, ReceiverParty, BuyerCustomerParty, SellerSupplierParty | `ForecastRevision.md` |
| [InventoryReport](InventoryReport.md) | 3: RetailerCustomerParty, InventoryReportingParty, SellerSupplierParty | `InventoryReport.md` |
| [ProductActivity](ProductActivity.md) | 2: SenderParty, ReceiverParty | `ProductActivity.md` |
| [RetailEvent](RetailEvent.md) | 4: SenderParty, ReceiverParty, BuyerCustomerParty, SellerSupplierParty | `RetailEvent.md` |
| [StockAvailabilityReport](StockAvailabilityReport.md) | 3: SellerSupplierParty, RetailerCustomerParty, InventoryReportingParty | `StockAvailabilityReport.md` |
| [TradeItemLocationProfile](TradeItemLocationProfile.md) | 4: SenderParty, ReceiverParty, BuyerCustomerParty, SellerSupplierParty | `TradeItemLocationProfile.md` |

### Group I — Utility

| Document | Party Elements | File |
|---|---|---|
| [UtilityStatement](UtilityStatement.md) | 5: SenderParty, ReceiverParty, CustomerParty, SubscriberParty, SubscriberConsumption | `UtilityStatement.md` |

### Group J — Digital Infrastructure

| Document | Party Elements | File |
|---|---|---|
| [DigitalAgreement](DigitalAgreement.md) | 3: GovernorParty, ParticipantParty, RequiredCertificationDocumentReference | `DigitalAgreement.md` |
| [DigitalCapability](DigitalCapability.md) | 3: SenderParty, ReceiverParty, BusinessParty | `DigitalCapability.md` |

### Group K — Party & Business Info

| Document | Party Elements | File |
|---|---|---|
| [BusinessCard](BusinessCard.md) | 3: SenderParty, ReceiverParty, BusinessParty | `BusinessCard.md` |
| [BusinessInformation](BusinessInformation.md) | 4: SenderParty, ReceiverParty, BusinessParty, BusinessPartyGroup | `BusinessInformation.md` |

### Group L — Waste

| Document | Party Elements | File |
|---|---|---|
| [WasteMovement](WasteMovement.md) | 6: SenderParty, ReceiverParty, NotifierParty, DisposalFacilityParty, RecoveryFacilityParty, WasteProducerParty | `WasteMovement.md` |
| [WasteNotification](WasteNotification.md) | 7: SenderParty, ReceiverParty, NotifierParty, CustomsParty, DisposalFacilityParty, RecoveryFacilityParty, WasteProducerParty | `WasteNotification.md` |

### Group M — Admin / Cross-cutting

| Document | Party Elements | File |
|---|---|---|
| [ApplicationResponse](ApplicationResponse.md) | 2: SenderParty, ReceiverParty | `ApplicationResponse.md` |
| [AttachedDocument](AttachedDocument.md) | 2: SenderParty, ReceiverParty | `AttachedDocument.md` |
| [DocumentStatus](DocumentStatus.md) | 2: SenderParty, ReceiverParty | `DocumentStatus.md` |
| [DocumentStatusRequest](DocumentStatusRequest.md) | 2: SenderParty, ReceiverParty | `DocumentStatusRequest.md` |
| [Enquiry](Enquiry.md) | 2: RequestorParty, ResponderParty | `Enquiry.md` |
| [EnquiryResponse](EnquiryResponse.md) | 2: RequestorParty, ResponderParty | `EnquiryResponse.md` |

---

## Party Reference

The 26+C parties used in the mappings:

| # | Role | Short |
|---|---|---|
| 1 | Commercial Buyer | Buyer |
| 2 | Contracting Authority | ContrAuth |
| 3 | Customs Declarant / Broker | CustBroker |
| 4 | Raw Material Supplier | RawSupplier |
| 5 | Manufacturer | Manufacturer |
| 6 | Distributor | Distributor |
| 7 | Waste Processor | WasteProc |
| 8 | Seller's Warehouse (outbound 3PL) | SellerWH |
| 9 | Buyer's Warehouse (inbound 3PL) | BuyerWH |
| 10 | Freight Forwarder | FreightFwd |
| 11 | Ocean Carrier | OceanCarr |
| 12 | Air Carrier | AirCarr |
| 13 | Road Carrier | RoadCarr |
| 14 | Rail Carrier | RailCarr |
| 15 | Inland Waterway Carrier | InlandCarr |
| 16 | Seaport / Terminal Operator | Seaport |
| 17 | Airport / Air Terminal | Airport |
| 18 | Rail Hub / Intermodal Terminal | RailHub |
| 19 | Customs Authority | Customs |
| 20 | Chamber of Commerce | ChamComm |
| 21 | Government Information Service | GovInfo |
| 22 | Buyer's Bank | BuyerBank |
| 23 | Seller's Bank | SellerBank |
| 24 | Factor | Factor |
| 25 | Guarantor | Guarantor |
| 26 | Retailer | Retailer |
| C | Consumer | Consumer |
