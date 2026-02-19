# UBL Process Group Classification

This document defines **13 process groups** that organise all 310 ABIE types and 101 document types in UBL 2.5 (CSD02) **top-down from the documents**.


The companion document [ubl-domain-groups.md](./ubl-domain-groups.md) provides the same 310 types organised **bottom-up by semantic meaning** (15 groups derived from CCTS ObjectClass names and containment hierarchy).


---

## Approach: top-down from documents

Rather than asking *what is this type?* (bottom-up), this grouping asks *which business process uses this type?*


**Methodology:**

1. The 101 UBL document types are assigned to 13 process groups based on which business lifecycle step they belong to.

2. The 114 ABIE types that appear directly in one or more document XSDs ("root types") are assigned to the group of the document(s) that uses them most — or to the Common Infrastructure group if they appear in 15+ documents.

3. The remaining 196 ABIE types ("interior types") never appear at document-header level. They are only reachable by traversing the type containment graph. Each is assigned to the group of the root type(s) that most commonly reference it, transitively.

4. Six types are manually overridden where the algorithm's result conflicts with clear semantic intent (see Group L and Group G notes).


---

## Relationship to CBC elements

UBL 2.5 defines **1,202 CBC (Common Basic Component) elements** — the leaf-level fields that carry actual values (`Amount`, `Name`, `Code`, `Indicator`, etc.).


- **1,100 CBCs** are referenced inside one or more of the 310 ABIE types. Grouping the ABIE types implicitly groups these CBCs within their usage context.

- **102 CBCs** are used only at document-header level (e.g., `UBLVersionID`, `DocumentCurrencyCode`, `LineCountNumeric`). These are assigned to the same group as the document type that uses them.


---

## Contents

- [Group A: Common Infrastructure](#common-infrastructure) — 34 types, 101 document types

- [Group B: Order-to-Cash](#order-to-cash) — 50 types, 19 document types

- [Group C: Fulfilment & Goods](#fulfilment-goods) — 20 types, 14 document types

- [Group D: Transport Operations](#transport-operations) — 41 types, 9 document types

- [Group E: Customs & Trade Compliance](#customs-trade-compliance) — 7 types, 8 document types

- [Group F: Catalogue Management](#catalogue-management) — 12 types, 5 document types

- [Group G: Procure-to-Award](#procure-to-award) — 55 types, 23 document types

- [Group H: Retail & Supply Chain Planning](#retail-supply-chain-planning) — 45 types, 10 document types

- [Group I: Utility Billing](#utility-billing) — 23 types, 1 document types

- [Group J: Digital Interoperability](#digital-interoperability) — 9 types, 2 document types

- [Group K: Party & Business Profile](#party-business-profile) — 4 types, 2 document types

- [Group L: Sustainability & Environment](#sustainability-environment) — 5 types, 2 document types

- [Group M: Administrative & General](#administrative-general) — 5 types, 6 document types

---

## Group A: Common Infrastructure

**34 ABIE types** · **101 document types**


Types used directly in 15 or more of the 101 document types. They are process-neutral backbone — every UBL document uses `SignatureType`, nearly every one uses `PartyType` and `DocumentReferenceType`. In the bottom-up grouping these were split across Party, Financial, and Documents groups based on their semantic names, but measured by actual usage they belong to no single process.


**Document types:** all 101 document types


**ABIE types:**


| Type | Kind | Description |

|---|:---:|---|

| `ContractingPartyType` | root | Contracting authority in a public procurement procedure |

| `CustomerPartyType` | root | Buyer role wrapper — embeds PartyType with buyer-specific context |

| `DocumentReferenceType` | root | Reference to another document by ID, type, and date |

| `OrderReferenceType` | root | Reference to a purchase order by ID and date |

| `PartyType` | root | Core representation of any trading partner |

| `PeriodType` | root | A date/time interval with start, end, and duration |

| `ProcurementProjectType` | root | The subject of a public procurement procedure |

| `ShipmentType` | root | A shipment of goods — the central logistics container type |

| `SignatureType` | root | XML digital signature attached to the document |

| `SupplierPartyType` | root | Seller role wrapper — embeds PartyType with supplier-specific context |

| `TaxTotalType` | root | Total tax amount, broken down by tax subtotals |

| `AuthorizationType` | interior |  |

| `ContractExtensionType` | interior |  |

| `ContractingActivityType` | interior |  |

| `ContractingPartyTypeType` | interior |  |

| `ContractingRepresentationTypeType` | interior |  |

| `CorporateRegistrationSchemeType` | interior |  |

| `ElectronicAddressType` | interior |  |

| `PartyIdentificationType` | interior |  |

| `PartyLegalEntityType` | interior |  |

| `PartyNameType` | interior |  |

| `PartyTaxSchemeType` | interior |  |

| `PowerOfAttorneyType` | interior |  |

| `ProcurementAdditionalTypeType` | interior |  |

| `RenewalType` | interior |  |

| `RequestForTenderLineType` | interior |  |

| `RequestedTenderTotalType` | interior |  |

| `ResultOfVerificationType` | interior |  |

| `SecurityListingType` | interior |  |

| `ServiceProviderPartyType` | interior |  |

| `ShareholderPartyType` | interior |  |

| `SocialMediaProfileType` | interior |  |

| `TaxSubtotalType` | interior |  |

| `WebSiteType` | interior |  |


---

## Group B: Order-to-Cash {order-to-cash}

**50 ABIE types** · **19 document types**


The commercial transaction lifecycle: quoting, ordering, invoicing, and payment settlement. Covers both buyer-initiated flow (RFQ → Quotation → Order → Invoice) and seller-initiated variants (SelfBilledInvoice, SelfBilledCreditNote). FreightInvoice is included here rather than in Transport Operations because it is a billing document — it shares 27 CAC types with Invoice and only 4 with TransportExecutionPlan.


**Document types in this group:**


| Document type | Description |

|---|---|

| `CreditNote` | Reduction of a previously issued invoice |

| `DebitNote` | Additional charge against a buyer |

| `FreightInvoice` | Invoice for transport/freight services |

| `Invoice` | Commercial invoice |

| `InvoiceStatusRequest` | Request for the status of a submitted invoice |

| `InvoiceStatusResponse` | Response to an invoice status request |

| `Order` | Purchase order from buyer to seller |

| `OrderCancellation` | Cancellation of a previously submitted order |

| `OrderChange` | Amendment to a previously submitted order |

| `OrderResponse` | Seller's response to a purchase order |

| `OrderResponseSimple` | Simplified accept/reject response to an order |

| `PurchaseReceipt` | Confirmation of goods/services received against a purchase |

| `Quotation` | Seller's price quotation in response to an RFQ |

| `Reminder` | Payment reminder for an outstanding invoice |

| `RemittanceAdvice` | Notification of a payment being made |

| `RequestForQuotation` | Request to a supplier for a price quotation |

| `SelfBilledCreditNote` | Credit note issued by the buyer (self-billing) |

| `SelfBilledInvoice` | Invoice issued by the buyer on behalf of the seller |

| `Statement` | Statement of outstanding invoices / account balance |


**ABIE types:**


| Type | Kind | Description |

|---|:---:|---|

| `AllowanceChargeType` | root | A discount or surcharge applied at header or line level |

| `AnnotationType` | root |  |

| `BillingReferenceType` | root |  |

| `BuyerReferenceType` | root |  |

| `CashRegisterType` | root |  |

| `ContactType` | root |  |

| `ContractType` | root | Reference to the contract governing a transaction |

| `CountryType` | root |  |

| `CreditNoteLineType` | root |  |

| `DebitNoteLineType` | root |  |

| `DeliveryTermsType` | root |  |

| `DeliveryType` | root | Delivery details — location, requested/actual dates |

| `ExchangeRateType` | root | Currency exchange rate between two currencies |

| `InvoiceLineType` | root | One line item on an invoice |

| `MonetaryTotalType` | root | Summary monetary amounts for a document (payable, tax exclusive, etc.) |

| `OrderLineType` | root | One line item on a purchase order |

| `PaymentMeansType` | root | Method of payment (bank transfer, card, cheque, etc.) |

| `PaymentTermsType` | root | Terms governing when and how payment is due |

| `PaymentType` | root |  |

| `ProjectReferenceType` | root |  |

| `PurchaseReceiptLineType` | root |  |

| `PurchaseReferenceType` | root |  |

| `QuotationLineType` | root |  |

| `ReminderLineType` | root |  |

| `RemittanceAdviceLineType` | root |  |

| `RequestForQuotationLineType` | root |  |

| `ResponseType` | root |  |

| `StatementLineType` | root |  |

| `TransactionConditionsType` | root |  |

| `BillingReferenceLineType` | interior |  |

| `BranchType` | interior |  |

| `CardAccountType` | interior |  |

| `ClauseType` | interior |  |

| `CreditAccountType` | interior |  |

| `DeliveryUnitType` | interior |  |

| `DependentPriceReferenceType` | interior |  |

| `FinancialAccountType` | interior |  |

| `FinancialInstitutionType` | interior |  |

| `InterestRateType` | interior |  |

| `ItemLocationQuantityType` | interior |  |

| `LineItemType` | interior |  |

| `OrderLineReferenceType` | interior |  |

| `OrderedShipmentType` | interior |  |

| `PaymentMandateType` | interior |  |

| `PriceExtensionType` | interior |  |

| `PriceListType` | interior |  |

| `PriceType` | interior | A price — unit price, base quantity, and price type code |

| `PricingReferenceType` | interior |  |

| `TradeFinancingType` | interior |  |

| `WorkPhaseReferenceType` | interior |  |


---

## Group C: Fulfilment & Goods {fulfilment--goods}

**20 ABIE types** · **14 document types**


The physical movement of goods once an order is confirmed: despatch, receipt, returns, packing, and the goods documents that travel with cargo. ForwardingInstructions, BillOfLading, and Waybill are included here (rather than Transport Operations) because they are shipper-facing goods documents that describe cargo — not carrier-facing operational plans.


**Document types in this group:**


| Document type | Description |

|---|---|

| `BillOfLading` | Goods receipt and title document issued by a carrier |

| `DeliveryNote` | Accompanies goods at the point of delivery |

| `DespatchAdvice` | Notification that goods have been despatched |

| `ForwardingInstructions` | Shipper instructions to a freight forwarder |

| `FulfilmentCancellation` | Cancellation of a fulfilment (despatch or receipt) |

| `GoodsCertificate` | Government-issued certificate accompanying goods |

| `GoodsItemItinerary` | Planned route for a goods item |

| `GoodsItemPassport` | ATA Carnet-type temporary export document for goods |

| `InstructionForReturns` | Instruction to return goods to a supplier |

| `Manifest` | List of cargo items in a shipment or vessel |

| `PackingList` | Detailed list of packages and their contents |

| `ReceiptAdvice` | Confirmation that goods have been received |

| `Waybill` | Transport document for road/air/rail shipments |

| `WeightStatement` | Official statement of the weight of a shipment |


**ABIE types:**


| Type | Kind | Description |

|---|:---:|---|

| `AttestationType` | root |  |

| `DespatchLineType` | root |  |

| `DocumentDistributionType` | root |  |

| `GoodsItemType` | root |  |

| `GoodsProcessingType` | root |  |

| `InstructionForReturnsLineType` | root |  |

| `PackageType` | root |  |

| `PersonType` | root |  |

| `ReceiptLineType` | root |  |

| `TransportEquipmentType` | root |  |

| `TransportationSegmentType` | root |  |

| `AttestationLineType` | interior |  |

| `CommunicationType` | interior |  |

| `CriterionItemType` | interior |  |

| `DespatchType` | interior |  |

| `EnergyConsumptionAllocationType` | interior |  |

| `GoodsItemContainerType` | interior |  |

| `PickupType` | interior |  |

| `TransportEquipmentSealType` | interior |  |

| `VerifiedGrossMassType` | interior |  |


---

## Group D: Transport Operations {transport-operations}

**41 ABIE types** · **9 document types**


Carrier-facing documents that plan, execute, monitor, and report on transport services. These share a dense sub-vocabulary of `ShipmentStageType`, `MaritimeTransportType`, `AirTransportType`, `RailTransportType`, and `RoadTransportType`. Maritime types (BallastWater, PortCall, VesselDynamics) appear here because they are nested inside transport-level ABIE types — the dedicated IMO FAL maritime document types are expected in a future UBL release.


**Document types in this group:**


| Document type | Description |

|---|---|

| `CommonTransportationReport` | Status report on a transport operation |

| `TransportExecutionPlan` | Carrier's confirmed plan for executing a transport service |

| `TransportExecutionPlanRequest` | Shipper's request for a transport execution plan |

| `TransportProgressStatus` | Status update on transport progress |

| `TransportProgressStatusRequest` | Request for transport progress status |

| `TransportServiceDescription` | Carrier's description of an available transport service |

| `TransportServiceDescriptionRequest` | Request for a transport service description |

| `TransportationStatus` | Status of a shipment or consignment in transit |

| `TransportationStatusRequest` | Request for the status of a shipment or consignment |


**ABIE types:**


| Type | Kind | Description |

|---|:---:|---|

| `ConsignmentType` | root | A consignment of goods being transported together |

| `LocationType` | root | A physical location — port, warehouse, delivery point |

| `TransportEventType` | root |  |

| `TransportExecutionTermsType` | root |  |

| `TransportMeansType` | root | The vehicle, vessel, or aircraft used for transport |

| `TransportScheduleType` | root |  |

| `TransportationServiceType` | root | Description of a transport service offered by a carrier |

| `AirTransportType` | interior |  |

| `BallastWaterSummaryType` | interior | Summary of ballast water management operations (IMO BWM Convention) |

| `BallastWaterTransactionType` | interior |  |

| `ConditionType` | interior |  |

| `CrewPersonEffectType` | interior |  |

| `EventType` | interior |  |

| `FuelConsumptionType` | interior |  |

| `FuelMeteringType` | interior |  |

| `FuelPropertyType` | interior |  |

| `ISPSRequirementsType` | interior |  |

| `InsurancePolicyType` | interior |  |

| `LocationCoordinateType` | interior |  |

| `MaritimeHealthDeclarationType` | interior |  |

| `MaritimeTransportType` | interior | Maritime transport leg details including vessel and voyage |

| `MaritimeWasteType` | interior | Waste generated or delivered during a port call |

| `NotificationRequirementType` | interior |  |

| `PersonnelHealthIncidentType` | interior |  |

| `PortCallPurposeType` | interior |  |

| `PortCallRecordType` | interior |  |

| `PortCallType` | interior | A vessel's call at a port (IMO FAL form data) |

| `RailTransportType` | interior |  |

| `RoadTransportType` | interior |  |

| `SanitaryMeasureType` | interior |  |

| `SecurityMeasureType` | interior |  |

| `ServiceFrequencyType` | interior |  |

| `ShipRequirementType` | interior |  |

| `ShipStoreArticleType` | interior |  |

| `ShipToShipActivityRecordType` | interior |  |

| `ShipmentStageType` | interior | One leg of a multi-stage shipment |

| `StatusType` | interior |  |

| `StorageType` | interior |  |

| `TransportHandlingUnitType` | interior |  |

| `VesselDynamicsType` | interior | Vessel movement and fuel consumption data |

| `WHOAffectedAreaVisitType` | interior |  |


---

## Group E: Customs & Trade Compliance {customs--trade-compliance}

**7 ABIE types** · **8 document types**


Documents filed with or issued by customs authorities. They share `CustomsDeclarationType`, `EndorsementType`, and `GoodsItemPassportCounterfoilType`. CertificateOfOrigin and GuaranteeCertificate are included because they are regulatory compliance documents, not logistics handover documents.


**Document types in this group:**


| Document type | Description |

|---|---|

| `CertificateOfOrigin` | Certificate declaring the country of origin of goods |

| `ExportCustomsDeclaration` | Declaration for goods being exported |

| `GuaranteeCertificate` | Financial or performance guarantee |

| `ImportCustomsDeclaration` | Declaration for goods being imported |

| `ProofOfReexportation` | Evidence that previously imported goods have been re-exported |

| `ProofOfReexportationReminder` | Reminder to provide proof of re-exportation |

| `ProofOfReexportationRequest` | Request for proof of re-exportation |

| `TransitCustomsDeclaration` | Customs declaration for goods in transit |


**ABIE types:**


| Type | Kind | Description |

|---|:---:|---|

| `CertificateOfOriginApplicationType` | root |  |

| `CustomsDeclarationType` | root |  |

| `EndorsementType` | root |  |

| `EndorserPartyType` | root |  |

| `GoodsItemPassportCounterfoilType` | root |  |

| `ImmobilizedSecurityType` | root |  |

| `RegulationType` | root |  |


---

## Group F: Catalogue Management {catalogue-management}

**12 ABIE types** · **5 document types**


Catalogue documents are structurally distinct: they use `CatalogueLineType`, `ItemLocationQuantityType`, and `ClassificationSchemeType` heavily, with minimal use of the financial types (no `TaxTotalType` or `MonetaryTotalType` at the top level). They form an isolated cluster with high intra-group Jaccard similarity.


**Document types in this group:**


| Document type | Description |

|---|---|

| `Catalogue` | Full product/service catalogue |

| `CatalogueDeletion` | Request to delete a previously published catalogue |

| `CatalogueItemSpecificationUpdate` | Update to item specifications in a catalogue |

| `CataloguePricingUpdate` | Update to prices in a catalogue |

| `CatalogueRequest` | Request for a catalogue from a supplier |


**ABIE types:**


| Type | Kind | Description |

|---|:---:|---|

| `AddressType` | root |  |

| `CatalogueItemSpecificationUpdateLineType` | root |  |

| `CatalogueLineType` | root | One product line in a catalogue |

| `CataloguePricingUpdateLineType` | root |  |

| `CatalogueReferenceType` | root |  |

| `CatalogueRequestLineType` | root |  |

| `ClassificationSchemeType` | root |  |

| `LanguageType` | root |  |

| `TradingTermsType` | root |  |

| `AddressLineType` | interior |  |

| `ClassificationCategoryType` | interior |  |

| `ItemComparisonType` | interior |  |


---

## Group G: Procure-to-Award {procure-to-award}

**55 ABIE types** · **23 document types**


UBL's largest process group by document count: the full public procurement lifecycle from market engagement through contract award. Documents share `TenderingProcessType`, `ProcurementProjectType`, and `TenderingCriterionType`. WorkReport is included because it reports on works contract performance, a post-award procurement obligation. `PerformanceDataLineType` is assigned here as the only type with no traceable document home — contract performance measurement is its closest semantic domain.


**Document types in this group:**


| Document type | Description |

|---|---|

| `AwardedNotification` | Notification to the winning tenderer |

| `CallForTenders` | Invitation to submit a tender |

| `ContractAwardNotice` | Formal notice of contract award (EU procurement) |

| `ContractNotice` | Tender notice published to the market |

| `ExpressionOfInterestRequest` | Market engagement before a formal tender |

| `ExpressionOfInterestResponse` | Response to an expression of interest request |

| `PriorInformationNotice` | Advance notice of a forthcoming tender (EU procurement) |

| `ProcurementStatus` | Status of a procurement procedure |

| `ProcurementStatusRequest` | Request for the status of a procurement procedure |

| `QualificationApplicationRequest` | Request to qualify as a supplier in a procurement system |

| `QualificationApplicationResponse` | Response to a supplier qualification request |

| `Tender` | Tenderer's offer in response to a call for tenders |

| `TenderContract` | Signed contract arising from a tender award |

| `TenderReceipt` | Acknowledgement of receipt of a tender submission |

| `TenderStatus` | Status update on a tender |

| `TenderStatusRequest` | Request for the status of a tender |

| `TenderWithdrawal` | Withdrawal of a previously submitted tender |

| `TendererQualification` | Qualification information submitted by a tenderer |

| `TendererQualificationResponse` | Response to a tenderer qualification submission |

| `UnawardedNotification` | Notification to unsuccessful tenderers |

| `UnsubscribeFromProcedureRequest` | Request to unsubscribe from a procurement procedure |

| `UnsubscribeFromProcedureResponse` | Response to an unsubscribe request |

| `WorkReport` | Report on work performed under a works contract |


**ABIE types:**


| Type | Kind | Description |

|---|:---:|---|

| `AppealTermsType` | root |  |

| `EconomicOperatorPartyType` | root | A tenderer or supplier in a procurement procedure |

| `EvidenceType` | root |  |

| `FinancialGuaranteeType` | root |  |

| `ProcurementProjectLotReferenceType` | root |  |

| `ProcurementProjectLotType` | root | One lot within a multi-lot procurement project |

| `QualificationResolutionType` | root |  |

| `TenderResultType` | root |  |

| `TenderedProjectType` | root |  |

| `TendererPartyQualificationType` | root |  |

| `TenderingCriterionResponseType` | root |  |

| `TenderingCriterionType` | root |  |

| `TenderingProcessType` | root | The procedural rules governing a procurement procedure |

| `TenderingTermsType` | root | Commercial and legal terms for a tendering procedure |

| `WorkQuantityTotalType` | root |  |

| `WorkReportLineType` | root |  |

| `AuctionTermsType` | interior |  |

| `AwardingCriterionResponseType` | interior |  |

| `AwardingCriterionType` | interior |  |

| `AwardingTermsType` | interior |  |

| `BudgetAccountLineType` | interior |  |

| `BudgetAccountType` | interior |  |

| `CompletedTaskType` | interior |  |

| `ContractExecutionRequirementType` | interior |  |

| `ContractingSystemType` | interior |  |

| `DeclarationType` | interior |  |

| `EconomicOperatorRoleType` | interior |  |

| `EconomicOperatorShortListType` | interior |  |

| `EncryptionCertificatePathChainType` | interior |  |

| `EncryptionDataType` | interior |  |

| `EncryptionSymmetricAlgorithmType` | interior |  |

| `EvaluationCriterionType` | interior |  |

| `EvidenceSuppliedType` | interior |  |

| `FeeType` | interior |  |

| `FrameworkAgreementType` | interior |  |

| `LegislationType` | interior |  |

| `LotDistributionType` | interior |  |

| `LotsGroupType` | interior |  |

| `PerformanceDataLineType` | interior | Performance measurement data for a contract activity |

| `PostAwardProcessType` | interior |  |

| `PrizeType` | interior |  |

| `ProcessJustificationType` | interior |  |

| `QualifyingPartyType` | interior |  |

| `RelatedItemType` | interior |  |

| `ResponseValueType` | interior |  |

| `SecurityClearanceTermType` | interior |  |

| `SubcontractTermsType` | interior |  |

| `TenderLineType` | interior |  |

| `TenderPreparationType` | interior |  |

| `TenderRequirementType` | interior |  |

| `TendererQualificationRequestType` | interior |  |

| `TendererRequirementType` | interior |  |

| `TenderingCriterionPropertyGroupType` | interior |  |

| `TenderingCriterionPropertyType` | interior |  |

| `WinningPartyType` | interior |  |


---

## Group H: Retail & Supply Chain Planning {retail--supply-chain-planning}

**45 ABIE types** · **10 document types**


Collaborative Planning, Forecasting and Replenishment (CPFR) documents introduced in UBL 2.1. They share `ActivityDataLineType`, `ForecastLineType`, and `EventType` — vocabulary that appears nowhere else. ItemInformationRequest is a CPFR document, not a catalogue or procurement document. Item-level types (`ItemType`, `ItemIdentificationType`, `HazardousItemType`, etc.) are included here because they are most densely referenced through the CPFR line types.


**Document types in this group:**


| Document type | Description |

|---|---|

| `ExceptionCriteria` | CPFR criteria defining what constitutes an exception |

| `ExceptionNotification` | CPFR notification of a forecast exception |

| `Forecast` | CPFR demand or supply forecast |

| `ForecastRevision` | Revision to a previously submitted CPFR forecast |

| `InventoryReport` | CPFR report on current inventory levels |

| `ItemInformationRequest` | CPFR request for item sales/activity data |

| `ProductActivity` | CPFR report on product sales or movement activity |

| `RetailEvent` | CPFR notification of a planned retail event (promotion, etc.) |

| `StockAvailabilityReport` | CPFR report on stock availability |

| `TradeItemLocationProfile` | CPFR profile for a trade item at a specific location |


**ABIE types:**


| Type | Kind | Description |

|---|:---:|---|

| `ActivityDataLineType` | root | One line of retail activity data (sales, stock movement) |

| `EventCommentType` | root |  |

| `ExceptionCriteriaLineType` | root |  |

| `ExceptionNotificationLineType` | root |  |

| `ForecastLineType` | root | One demand or supply forecast line for a product |

| `ForecastRevisionLineType` | root |  |

| `InventoryReportLineType` | root |  |

| `ItemInformationRequestLineType` | root |  |

| `ItemManagementProfileType` | root |  |

| `MiscellaneousEventType` | root |  |

| `PromotionalEventType` | root |  |

| `StockAvailabilityReportLineType` | root |  |

| `ActivityPropertyType` | interior |  |

| `CertificateType` | interior |  |

| `CommodityClassificationType` | interior |  |

| `DimensionType` | interior |  |

| `EventLineItemType` | interior |  |

| `EventTacticEnumerationType` | interior |  |

| `EventTacticType` | interior |  |

| `ForecastExceptionCriterionLineType` | interior |  |

| `ForecastExceptionType` | interior |  |

| `HazardousGoodsTransitType` | interior |  |

| `HazardousItemType` | interior |  |

| `ItemIdentificationType` | interior |  |

| `ItemInstanceType` | interior |  |

| `ItemPropertyGroupType` | interior |  |

| `ItemPropertyRangeType` | interior |  |

| `ItemPropertyType` | interior |  |

| `ItemType` | interior | A product or service item — the core catalogue/line item entity |

| `LotIdentificationType` | interior |  |

| `PhysicalAttributeType` | interior |  |

| `PromotionalEventLineItemType` | interior |  |

| `PromotionalSpecificationType` | interior |  |

| `PropertyIdentificationType` | interior |  |

| `RadioactiveIsotopeType` | interior |  |

| `RadioactiveMaterialType` | interior |  |

| `ResourceConsumptionType` | interior |  |

| `RetailPlannedImpactType` | interior |  |

| `SalesItemType` | interior |  |

| `ScoreType` | interior |  |

| `SecondaryHazardType` | interior |  |

| `StowageType` | interior |  |

| `TaxCategoryType` | interior | A VAT or tax category with rate and exemption reason |

| `TaxSchemeType` | interior | Identification of a tax scheme (VAT, GST, etc.) |

| `TemperatureType` | interior |  |


---

## Group I: Utility Billing {utility-billing}

**23 ABIE types** · **1 document types**


A single document type with a highly specialised vocabulary: `SubscriberConsumptionType`, `MeterReadingType`, `EnergyWaterSupplyType`, and `ConsumptionReportType`. None of these types appear in any other document group. The Utility group in the bottom-up classification has 23 types; all 22 that have a traceable parent path are assigned here.


**Document types in this group:**


| Document type | Description |

|---|---|

| `UtilityStatement` | Utility bill (electricity, gas, water, telecom) |


**ABIE types:**


| Type | Kind | Description |

|---|:---:|---|

| `OnAccountPaymentType` | root |  |

| `SubscriberConsumptionType` | root | A utility subscriber's consumption record |

| `ConsumptionAverageType` | interior |  |

| `ConsumptionCorrectionType` | interior |  |

| `ConsumptionHistoryType` | interior |  |

| `ConsumptionLineType` | interior |  |

| `ConsumptionPointType` | interior |  |

| `ConsumptionReportReferenceType` | interior |  |

| `ConsumptionReportType` | interior |  |

| `ConsumptionType` | interior | Metered consumption of a utility resource |

| `DutyType` | interior |  |

| `EnergyTaxReportType` | interior |  |

| `EnergyWaterSupplyType` | interior |  |

| `MeterPropertyType` | interior |  |

| `MeterReadingType` | interior | A reading from a utility meter |

| `MeterType` | interior |  |

| `SupplierConsumptionType` | interior |  |

| `TelecommunicationsServiceType` | interior |  |

| `TelecommunicationsSupplyLineType` | interior |  |

| `TelecommunicationsSupplyType` | interior |  |

| `UnstructuredPriceType` | interior |  |

| `UtilityItemType` | interior |  |

| `WebSiteAccessType` | interior |  |


---

## Group J: Digital Interoperability {digital-interoperability}

**9 ABIE types** · **2 document types**


Network-layer documents for 4-corner e-delivery architectures (Peppol, EESSI). Share `DigitalServiceType`, `DigitalProcessType`, and `DigitalCollaborationType` — types used nowhere else.


**Document types in this group:**


| Document type | Description |

|---|---|

| `DigitalAgreement` | Agreement on digital messaging capabilities between parties |

| `DigitalCapability` | Declaration of a party's digital messaging capabilities |


**ABIE types:**


| Type | Kind | Description |

|---|:---:|---|

| `DigitalAgreementTermsType` | root |  |

| `DigitalProcessType` | root | A business process supported by a digital agreement |

| `ParticipantPartyType` | root |  |

| `DeliveryChannelType` | interior |  |

| `DigitalCollaborationType` | interior |  |

| `DigitalServiceType` | interior | An e-delivery endpoint and its capabilities |

| `DocumentMetadataType` | interior |  |

| `MessageDeliveryType` | interior |  |

| `ServiceLevelAgreementType` | interior |  |


---

## Group K: Party & Business Profile {party--business-profile}

**4 ABIE types** · **2 document types**


Documents describing a trading partner itself rather than a transaction. BusinessCard and BusinessInformation share `CapabilityType` and `PartyGroupType` and use almost no financial or logistics types.


**Document types in this group:**


| Document type | Description |

|---|---|

| `BusinessCard` | Business contact card for a party |

| `BusinessInformation` | Comprehensive party profile and capabilities |


**ABIE types:**


| Type | Kind | Description |

|---|:---:|---|

| `CapabilityType` | root |  |

| `NoticeSubTypeType` | root |  |

| `OperationTypeType` | root |  |

| `PartyGroupType` | root |  |


---

## Group L: Sustainability & Environment {sustainability--environment}

**5 ABIE types** · **2 document types**


New in UBL 2.5: documents for environmental compliance and waste tracking. Five ABIE types are manually assigned here from their algorithmic Group H placement: `WasteGeneratedType`, `EnvironmentalEmissionType`, `EmissionCalculationMethodType`, `CircularityProfileType`, and `EndOfLifeTreatmentType`. These are semantically sustainability types used in WasteMovement and WasteNotification; the algorithm placed them in H because the Item-type containment chain is shared with CPFR documents.


**Document types in this group:**


| Document type | Description |

|---|---|

| `WasteMovement` | Record of a waste consignment movement |

| `WasteNotification` | Notification of a planned waste movement |


**ABIE types:**


| Type | Kind | Description |

|---|:---:|---|

| `CircularityProfileType` | interior | Circular economy profile of a product |

| `EmissionCalculationMethodType` | interior | Method used to calculate an environmental emission |

| `EndOfLifeTreatmentType` | interior | Prescribed treatment for a product at end of life |

| `EnvironmentalEmissionType` | interior | An emission to the environment (CO2, NOx, etc.) |

| `WasteGeneratedType` | interior | Waste generated during a process or operation |


---

## Group M: Administrative & General {administrative--general}

**5 ABIE types** · **6 document types**


Cross-process utility documents: confirmations, enquiries, and generic document status tracking. These are deliberately process-agnostic and share few types with any specific group.


**Document types in this group:**


| Document type | Description |

|---|---|

| `ApplicationResponse` | Generic application-level response |

| `AttachedDocument` | Document wrapper with embedded attachment |

| `DocumentStatus` | Status response for a previously submitted document |

| `DocumentStatusRequest` | Request for the status of a previously submitted document |

| `Enquiry` | Request for information |

| `EnquiryResponse` | Response to an enquiry |


**ABIE types:**


| Type | Kind | Description |

|---|:---:|---|

| `AttachmentType` | root |  |

| `DocumentResponseType` | root |  |

| `LineReferenceType` | root |  |

| `ExternalReferenceType` | interior |  |

| `LineResponseType` | interior |  |


---

## Notes on kind column

| Kind | Meaning |

|---|---|

| `root` | This type is referenced directly in one or more document XSD files via a `cac:` element ref |

| `interior` | This type is only reachable by traversing the CAC containment graph — it appears as a child of another ABIE type, never directly in a document header |


---

## Comparison to bottom-up grouping

| Dimension | Bottom-up (ubl-domain-groups.md) | Top-down (this document) |

|---|---|---|

| Number of groups | 15 | 13 |

| Classification basis | CCTS ObjectClass semantics | Business process lifecycle |

| "Financial" group | Standalone (24 types) | Absorbed into Order-to-Cash |

| "Address/Location" group | Standalone (11 types) | Absorbed into Infrastructure |

| "Documents/References" group | Standalone (12 types) | Absorbed into Infrastructure |

| Maritime types | Own group — 20 types, 0 documents | Part of Transport Operations — pending future IMO FAL document types |

| Infrastructure types | Distributed across semantic groups | Explicit group A — 38 types, all 101 docs |

| Interior types visible | Only via containment narrative | Explicit assignment via graph traversal |


*Last updated: 2026-02-19*
