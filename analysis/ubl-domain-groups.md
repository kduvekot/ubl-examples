# UBL Domain Group Classification

This document defines the **15 domain groups** used to organise all 310 ABIE types and 101 document types in UBL 2.5 (CSD02).

It is the authoritative reference for how the [element reference files](./ubl-element-reference.md) and any future grouping of UBL sample documents are organised.

---

## Basis for classification

Each ABIE type is placed in exactly one group. The decision is made in priority order:

1. **CCTS ObjectClass** — the first word(s) in the type name identify the CCTS Object Class    (e.g., `Item`, `Party`, `Shipment`, `Payment`). This is the primary signal.
2. **Parent ABIE containment** — if a type appears *only* as a child of ABIEs in one group,    it belongs in that group even if its name is ambiguous    (e.g., `ConditionType` → child of `StatusType` → Documents).
3. **Document type association** — if a type appears only in a specific document family    (e.g., `Consumption*` types only in UtilityStatement), it follows that family.
4. **Version introduction** — UBL 2.4–2.5 maritime types are grouped together even when    their names might fit elsewhere, because they share a single regulatory context    (IMO FAL Convention / Maritime Single Window).

Where a type is genuinely cross-cutting (e.g., `PeriodType` appears everywhere), it is placed in the group where it is most commonly *semantically significant*, not just technically referenced.

---

## Contents

- [Group 01: Party & Organization](#party) — 21 types, 1 document types, 15 with examples
- [Group 02: Address, Location & Communication](#address) — 11 types, 0 document types, 8 with examples
- [Group 03: Items, Products & Classification](#items) — 25 types, 5 document types, 11 with examples
- [Group 04: Shipment, Goods & Delivery](#shipment) — 26 types, 13 document types, 15 with examples
- [Group 05: Transport Means & Operations](#transport) — 14 types, 11 document types, 13 with examples
- [Group 06: Maritime & Port Operations](#maritime) — 21 types, 1 document types, 0 with examples
- [Group 07: Procurement & Tendering](#procurement) — 57 types, 24 document types, 6 with examples
- [Group 08: Contract & Legal](#contract) — 16 types, 8 document types, 5 with examples
- [Group 09: Financial, Payment & Tax](#financial) — 24 types, 0 document types, 16 with examples
- [Group 10: Orders, Invoices & Trade Lines](#orders) — 24 types, 18 document types, 16 with examples
- [Group 11: Documents, References & Responses](#documents) — 12 types, 6 document types, 7 with examples
- [Group 12: Retail, Supply Chain & Planning](#retail) — 20 types, 9 document types, 17 with examples
- [Group 13: Digital Services & Security](#digital) — 9 types, 2 document types, 9 with examples
- [Group 14: Utility Services](#utility) — 23 types, 1 document types, 0 with examples
- [Group 15: Sustainability & Circular Economy](#sustainability) — 5 types, 2 document types, 1 with examples

---

## Group 01: Party & Organization {#party}

**21 ABIE types** · **1 document types** · **15 types observed in examples** · **6 XSD-only types**

Types representing trading partners, roles, and organisational units. All derive from the CCTS ObjectClass 'Party'. Role wrappers (CustomerPartyType, SupplierPartyType, etc.) add context-specific references around the core PartyType. PersonType and ContactType are included because they describe the human agents within or acting on behalf of a party.

**Document types in this group:**

| Document type | Description |
|---|---|
| `BusinessCard` | Business Card |

**ABIE types:**

| Type | In examples | Rationale |
|---|:---:|---|
| `PartyType` | ✓ | Core ABIE for any trading partner; parent of all role-specific party wrappers |
| `BranchType` | ✓ | A branch office or sub-unit of an organisation or financial institution |
| `CapabilityType` | ✓ | A declared capability of a party — financial, technical, or equipment |
| `ContactType` | ✓ | Contact details (name, phone, email) for a person or department within a party |
| `ContractingPartyType` | ✓ | A party acting as contracting authority in procurement |
| `CorporateRegistrationSchemeType` |  | Scheme under which a party is registered as a legal entity |
| `CustomerPartyType` | ✓ | Buyer/customer role wrapper around PartyType |
| `EconomicOperatorPartyType` | ✓ | Supplier/contractor in procurement; wraps PartyType with ESPD reference |
| `EndorserPartyType` | ✓ | A party that signs or endorses a goods document or certificate |
| `ParticipantPartyType` | ✓ | A party participating in a digital collaboration or process |
| `PartyGroupType` |  | A named grouping of parties — consortia, syndicates, joint ventures |
| `PartyIdentificationType` | ✓ | An identifier for a party under a specific scheme (GLN, DUNS, VAT, EORI) |
| `PartyLegalEntityType` | ✓ | Legal registration details of a party — company ID and registered address |
| `PartyNameType` | ✓ | A trading name or alias for a party |
| `PartyTaxSchemeType` | ✓ | A party's registration under a specific tax scheme — VAT ID, tax category |
| `PersonType` | ✓ | A natural person — contacts, crew members, authorised representatives |
| `PowerOfAttorneyType` |  | Power of attorney granting an agent the right to act for a principal |
| `ServiceProviderPartyType` |  | A party providing a transport or logistics service |
| `ShareholderPartyType` |  | A party holding shares in a company (beneficial ownership disclosure) |
| `SupplierPartyType` | ✓ | Seller/supplier role wrapper around PartyType |
| `WinningPartyType` |  | A party that won a tender result |

---

## Group 02: Address, Location & Communication {#address}

**11 ABIE types** · **0 document types** · **8 types observed in examples** · **3 XSD-only types**

Types describing where parties, goods, or deliveries are located and how to reach them. AddressType and LocationType are the primary spatial types; CommunicationType, ElectronicAddressType, SocialMediaProfileType and WebSiteType capture the channels through which parties communicate. LanguageType belongs here because it qualifies multilingual content associated with addresses and communications.

**Document types in this group:**

*No top-level document type — types used within other groups' documents.*

**ABIE types:**

| Type | In examples | Rationale |
|---|:---:|---|
| `AddressType` | ✓ | A full postal address — street, city, postal code, country |
| `AddressLineType` | ✓ | A single free-text line within a structured postal address |
| `CommunicationType` |  | A communication channel — phone, fax, email, or URI — for a contact |
| `CountryType` | ✓ | A country identified by ISO 3166-1 alpha-2 code and/or name |
| `ElectronicAddressType` |  | An electronic endpoint address (Peppol participant ID, EAS scheme) |
| `LanguageType` | ✓ | A language identified by ISO 639 code — used to qualify multilingual content |
| `LocationCoordinateType` | ✓ | Geographic coordinates in WGS-84 — latitude, longitude, altitude |
| `LocationType` | ✓ | A named location with optional address, coordinates, and location code |
| `SocialMediaProfileType` | ✓ | A social media presence — platform name and URL or handle |
| `WebSiteType` | ✓ | A website URI with optional description |
| `WebSiteAccessType` |  | Access credentials or URI structure for a specific area of a website |

---

## Group 03: Items, Products & Classification {#items}

**25 ABIE types** · **5 document types** · **11 types observed in examples** · **14 XSD-only types**

Types describing physical or virtual goods and services — their identity, properties, classification, and catalogue presentation. ItemType is the core ABIE; ItemIdentificationType and CommodityClassificationType handle coding under external schemes (GTIN, UNSPSC, HS, CPV). Catalogue*Type subtypes are included because they are structurally line-level wrappers around ItemType in catalogue documents. AttestationType is here because attestations relate to product conformity.

**Document types in this group:**

| Document type | Description |
|---|---|
| `Catalogue` | Catalogue |
| `CatalogueDeletion` | Catalogue Deletion |
| `CatalogueItemSpecificationUpdate` | Catalogue Item Specification Update |
| `CataloguePricingUpdate` | Catalogue Pricing Update |
| `CatalogueRequest` | Catalogue Request |

**ABIE types:**

| Type | In examples | Rationale |
|---|:---:|---|
| `ItemType` | ✓ | An item (product or service) with identification, description, and properties |
| `ActivityPropertyType` |  | A named property describing characteristics of an item or activity |
| `AttestationLineType` | ✓ | A line in an attestation document, certifying a product attribute or lot |
| `AttestationType` | ✓ | An attestation (conformity claim) associated with an item or batch |
| `CatalogueItemSpecificationUpdateLineType` |  | A line updating item specification data in a catalogue |
| `CatalogueLineType` |  | A catalogue entry for one product or service offering |
| `CataloguePricingUpdateLineType` |  | A line updating pricing in an existing catalogue |
| `CatalogueReferenceType` |  | A reference to a specific catalogue document and line |
| `CatalogueRequestLineType` |  | A line in a request for catalogue data, specifying item criteria |
| `ClassificationCategoryType` |  | A category node within a classification scheme (UNSPSC, CPV, GPC) |
| `ClassificationSchemeType` |  | A classification scheme definition — UNSPSC, CPV, HS, GPC, etc. |
| `CommodityClassificationType` | ✓ | Classification of a commodity by code scheme — HS, UNSPSC, CPV, etc. |
| `DimensionType` | ✓ | A physical dimension of an item — length, width, height, weight, volume |
| `ItemComparisonType` |  | A comparative property enabling catalogue item comparison |
| `ItemIdentificationType` | ✓ | An identification of an item under a scheme — GTIN, seller ID, buyer ID |
| `ItemInstanceType` | ✓ | A specific individual instance — serial number, batch, or lot |
| `ItemLocationQuantityType` | ✓ | A quantity of an item available or required at a specific location or under specific terms |
| `ItemPropertyGroupType` |  | A group of related item properties within a catalogue line |
| `ItemPropertyRangeType` |  | A permissible range (min/max) for an item property value |
| `ItemPropertyType` | ✓ | A named characteristic or property of an item |
| `LotIdentificationType` | ✓ | A production or manufacturing batch/lot identifier for an item |
| `PhysicalAttributeType` |  | A physical attribute of an item — colour, shape, size designation |
| `PropertyIdentificationType` |  | An identifier for an item property definition |
| `RelatedItemType` |  | An item related to another — accessory, replacement, variant, component |
| `SalesItemType` | ✓ | An item with quantity sold and activity context in a supply-chain report |

---

## Group 04: Shipment, Goods & Delivery {#shipment}

**26 ABIE types** · **13 document types** · **15 types observed in examples** · **11 XSD-only types**

Types governing the movement of physical goods from origin to consignee. ShipmentType and ConsignmentType model the overarching shipment; GoodsItemType and PackageType describe individual cargo units. DeliveryType and DespatchType record the handover events. Hazardous and radioactive material types are here because they are properties of the goods-in-transit, not of the transport mode. TemperatureType belongs here as it describes a controlled-atmosphere requirement for cargo, not for the vehicle.

**Document types in this group:**

| Document type | Description |
|---|---|
| `BillOfLading` | Bill Of Lading |
| `DeliveryNote` | Delivery Note |
| `DespatchAdvice` | Despatch Advice |
| `ForwardingInstructions` | Forwarding Instructions |
| `FulfilmentCancellation` | Fulfilment Cancellation |
| `GoodsCertificate` | Goods Certificate |
| `GoodsItemItinerary` | Goods Item Itinerary |
| `GoodsItemPassport` | Goods Item Passport |
| `InstructionForReturns` | Instruction For Returns |
| `Manifest` | Manifest |
| `PackingList` | Packing List |
| `ReceiptAdvice` | Receipt Advice |
| `WeightStatement` | Weight Statement |

**ABIE types:**

| Type | In examples | Rationale |
|---|:---:|---|
| `ShipmentType` | ✓ | A shipment — goods moving from an origin to a named destination |
| `ConsignmentType` | ✓ | A consignment — goods under a single contract of carriage |
| `GoodsItemType` | ✓ | A goods item being transported, stored, or customs-declared |
| `GoodsItemContainerType` |  | A container used to carry a specific goods item |
| `GoodsItemPassportCounterfoilType` | ✓ | The counterfoil of a goods item passport (ATA carnet / CPD) |
| `GoodsProcessingType` |  | A processing step applied to goods in transit — cutting, canning, inspection |
| `HazardousGoodsTransitType` |  | Hazardous goods transit requirements per IMDG, ADR, or RID |
| `HazardousItemType` |  | An item classified as hazardous for transport — UN number, packing group |
| `PackageType` | ✓ | A physical package containing one or more goods items |
| `TransportHandlingUnitType` | ✓ | A handling unit — pallet, container, crate — used in transport |
| `DeliveryType` | ✓ | A delivery event — when, where, and to whom goods are delivered |
| `DeliveryChannelType` | ✓ | A channel or modality through which a delivery is made |
| `DeliveryTermsType` | ✓ | Delivery terms and conditions — Incoterms, lead time, delivery location |
| `DeliveryUnitType` |  | A unit in which goods are delivered — pallet, carton, drum |
| `DespatchType` | ✓ | A despatch event — the act of sending goods to the consignee |
| `DespatchLineType` | ✓ | A line in a despatch advice referencing an ordered line item |
| `InstructionForReturnsLineType` | ✓ | A line in an instruction for returning goods |
| `OrderedShipmentType` |  | A shipment as ordered — links an order to a specific planned shipment |
| `PickupType` | ✓ | A pickup event — when and where goods are collected from the sender |
| `RadioactiveIsotopeType` |  | Isotope data for radioactive material in a consignment |
| `RadioactiveMaterialType` |  | Radioactive material classification, activity, and transport index |
| `SecondaryHazardType` |  | A secondary hazard class for a dangerous-goods item |
| `StorageType` |  | Storage conditions or facility for goods — temperature, humidity, warehouse |
| `StowageType` |  | Stowage position or instructions for cargo aboard a vessel or vehicle |
| `TemperatureType` | ✓ | A temperature measurement or controlled-atmosphere requirement for cargo |
| `VerifiedGrossMassType` | ✓ | Verified Gross Mass of a packed container per SOLAS regulation |

---

## Group 05: Transport Means & Operations {#transport}

**14 ABIE types** · **11 document types** · **13 types observed in examples** · **1 XSD-only types**

Types describing how goods move — the vehicle, vessel, aircraft, or train; the stages of a multi-modal journey; and the events, schedules, and equipment used during transportation. TransportMeansType is the generic wrapper; the four modal subtypes (Air, Maritime, Rail, Road) carry mode-specific identification. ShipmentStageType models one leg within a multi-modal route. MaritimeTransportType sits here (not in Maritime & Port Operations) because it describes the vessel as a means of transport, not port-call administration.

**Document types in this group:**

| Document type | Description |
|---|---|
| `CommonTransportationReport` | Common Transportation Report |
| `FreightInvoice` | Freight Invoice |
| `TransportExecutionPlan` | Transport Execution Plan |
| `TransportExecutionPlanRequest` | Transport Execution Plan Request |
| `TransportProgressStatus` | Transport Progress Status |
| `TransportProgressStatusRequest` | Transport Progress Status Request |
| `TransportServiceDescription` | Transport Service Description |
| `TransportServiceDescriptionRequest` | Transport Service Description Request |
| `TransportationStatus` | Transportation Status |
| `TransportationStatusRequest` | Transportation Status Request |
| `Waybill` | Waybill |

**ABIE types:**

| Type | In examples | Rationale |
|---|:---:|---|
| `TransportMeansType` | ✓ | The means of transport — vessel, truck, aircraft, locomotive |
| `AirTransportType` | ✓ | Air transport mode — aircraft registration, IATA/ICAO flight number |
| `MaritimeTransportType` | ✓ | Maritime transport — vessel name, flag state, IMO number, call sign |
| `RailTransportType` | ✓ | Rail transport — train ID, rail car IDs |
| `RoadTransportType` | ✓ | Road transport — vehicle registration, haulier identification |
| `ShipmentStageType` | ✓ | One leg or stage in a multi-modal transport route |
| `ServiceFrequencyType` |  | The frequency of a transport service — daily, weekly, on-demand |
| `TransportEquipmentType` | ✓ | Transport equipment — ISO container, trailer, tank, swap body |
| `TransportEquipmentSealType` | ✓ | A seal applied to transport equipment (ISO container seal number) |
| `TransportEventType` | ✓ | A transport event — departure, arrival, waypoint, loading, discharge |
| `TransportExecutionTermsType` | ✓ | Terms for executing a transport service — service level, packing rules |
| `TransportScheduleType` | ✓ | A scheduled time/location entry in a transport execution plan |
| `TransportationSegmentType` | ✓ | A segment of a transportation service, possibly with its own carrier |
| `TransportationServiceType` | ✓ | A transportation service offered or contracted |

---

## Group 06: Maritime & Port Operations {#maritime}

**21 ABIE types** · **1 document types** · **0 types observed in examples** · **21 XSD-only types**

Types specific to the maritime domain and the IMO FAL Convention port-clearance process. These are absent from earlier UBL versions and were added in UBL 2.4–2.5 to support the IMO Maritime Single Window and related port community systems. MaritimeTransportType is kept in group 05 because it identifies the vessel as a transport means; the types here concern port-call administration, safety, environmental compliance, and vessel operations.

**Document types in this group:**

| Document type | Description |
|---|---|
| `BusinessInformation` | Business Information |

**ABIE types:**

| Type | In examples | Rationale |
|---|:---:|---|
| `PortCallType` |  | A port call — a vessel arriving at and departing from a port |
| `PortCallRecordType` |  | A record of information exchanged during an IMO FAL port call |
| `PortCallPurposeType` |  | Purpose of a port call — cargo ops, bunkering, crew change, repair |
| `ShipRequirementType` |  | A requirement about the vessel itself — draught, LOA, GT — for a port |
| `VesselDynamicsType` |  | Dynamic vessel data — AIS position, speed, heading, draught |
| `ShipToShipActivityRecordType` |  | A ship-to-ship transfer (STS) activity record |
| `BallastWaterSummaryType` |  | Summary of ballast water management operations during a voyage |
| `BallastWaterTransactionType` |  | A single ballast water uptake or discharge transaction |
| `FuelConsumptionType` |  | Fuel consumption data for a vessel voyage segment (IMO DCS/CII) |
| `FuelMeteringType` |  | A fuel metering record for bunkering or consumption monitoring |
| `FuelPropertyType` |  | Properties of a fuel — density, sulphur content, viscosity |
| `MaritimeHealthDeclarationType` |  | Maritime Declaration of Health for a vessel arriving in port |
| `MaritimeWasteType` |  | Waste category, quantity, and planned delivery port for MARPOL notification |
| `ISPSRequirementsType` |  | ISPS Code security requirements for a vessel's port call |
| `SecurityMeasureType` |  | A security measure applied to or required of a vessel or its operations |
| `SanitaryMeasureType` |  | A sanitary or phytosanitary measure applied to a vessel or its cargo |
| `PersonnelHealthIncidentType` |  | A health incident involving a person on board |
| `CrewPersonEffectType` |  | Personal effects declared by a crew member on arrival or departure |
| `ShipStoreArticleType` |  | An article in the ship's stores — provisions, spare parts, equipment |
| `WHOAffectedAreaVisitType` |  | A visit to a WHO-designated affected or endemic area by the vessel |
| `OperationTypeType` |  | An operation type code for a vessel or port operation (BusinessInformation context) |

---

## Group 07: Procurement & Tendering {#procurement}

**57 ABIE types** · **24 document types** · **6 types observed in examples** · **51 XSD-only types**

The largest domain group, reflecting UBL's extensive eTendering and eSourcing vocabulary introduced in UBL 2.1–2.3 and significantly extended in 2.4–2.5 to cover the EU ESPD (European Single Procurement Document) and eForms regulation. Types are grouped here when their primary purpose is to support the procurement lifecycle: from project definition through notice publication, qualification, tendering, evaluation, and award. ItemManagementProfileType is included because it governs replenishment agreement terms negotiated between buyer and supplier.

**Document types in this group:**

| Document type | Description |
|---|---|
| `AwardedNotification` | Awarded Notification |
| `CallForTenders` | Call For Tenders |
| `ContractAwardNotice` | Contract Award Notice |
| `ContractNotice` | Contract Notice |
| `ExpressionOfInterestRequest` | Expression Of Interest Request |
| `ExpressionOfInterestResponse` | Expression Of Interest Response |
| `ItemInformationRequest` | Item Information Request |
| `PriorInformationNotice` | Prior Information Notice |
| `ProcurementStatus` | Procurement Status |
| `ProcurementStatusRequest` | Procurement Status Request |
| `QualificationApplicationRequest` | Qualification Application Request |
| `QualificationApplicationResponse` | Qualification Application Response |
| `Tender` | Tender |
| `TenderContract` | Tender Contract |
| `TenderReceipt` | Tender Receipt |
| `TenderStatus` | Tender Status |
| `TenderStatusRequest` | Tender Status Request |
| `TenderWithdrawal` | Tender Withdrawal |
| `TendererQualification` | Tenderer Qualification |
| `TendererQualificationResponse` | Tenderer Qualification Response |
| `UnawardedNotification` | Unawarded Notification |
| `UnsubscribeFromProcedureRequest` | Unsubscribe From Procedure Request |
| `UnsubscribeFromProcedureResponse` | Unsubscribe From Procedure Response |
| `WorkReport` | Work Report |

**ABIE types:**

| Type | In examples | Rationale |
|---|:---:|---|
| `ProcurementProjectType` | ✓ | A procurement project — subject, nature, estimated value, CPV codes |
| `ProcurementProjectLotType` |  | A lot — a subdivision of a procurement project for separate award |
| `ProcurementProjectLotReferenceType` | ✓ | A reference to a specific lot within a procurement project |
| `TenderingProcessType` |  | Tendering process parameters — procedure type, deadlines, submission rules |
| `TenderingTermsType` | ✓ | General terms and conditions for a tendering procedure |
| `TenderPreparationType` | ✓ | Requirements for preparing a tender — languages, copies, format |
| `TenderRequirementType` |  | A document required to be submitted as part of a tender response |
| `TenderLineType` |  | A line in a tender offer, pricing specific items or services |
| `TenderedProjectType` |  | A project proposed by a tenderer in their offer response |
| `TenderResultType` |  | The result of evaluating a tender — awarded, rejected, etc. |
| `TenderingCriterionType` |  | A structured criterion for qualification, selection, or award (ESPD) |
| `TenderingCriterionPropertyGroupType` |  | A group of related properties within a tendering criterion |
| `TenderingCriterionPropertyType` |  | A single property/question within a structured tendering criterion |
| `TenderingCriterionResponseType` |  | A tenderer's answer to a tendering criterion question |
| `AwardingTermsType` |  | The overall terms and criteria framework for awarding a contract |
| `AwardingCriterionType` |  | A criterion for evaluating and comparing tenders — quality, price, etc. |
| `AwardingCriterionResponseType` |  | A tenderer's scored response to an awarding criterion |
| `EvidenceType` | ✓ | A document or dataset submitted as evidence for a qualification criterion |
| `EvidenceSuppliedType` |  | Evidence actually submitted in response to a criterion |
| `EvaluationCriterionType` |  | A qualitative evaluation criterion for pre-qualification |
| `QualifyingPartyType` |  | A party undergoing or having completed a qualification assessment |
| `QualificationResolutionType` |  | Resolution on a tenderer's qualification — admitted, rejected, etc. |
| `TendererPartyQualificationType` |  | Qualification data provided by a tenderer (financials, experience) |
| `TendererQualificationRequestType` |  | A request for specific qualification data from a tenderer |
| `TendererRequirementType` |  | A capability or compliance requirement that tenderers must satisfy |
| `RequestForTenderLineType` |  | A line in a call for tenders describing required items or services |
| `RequestedTenderTotalType` |  | Estimated or requested total values and conditions for a procurement |
| `SubcontractTermsType` |  | Terms and limits on subcontracting under the awarded contract |
| `FrameworkAgreementType` |  | A framework agreement — number of operators, max value, duration |
| `AuctionTermsType` |  | Terms for an electronic auction embedded in a procurement process |
| `AppealTermsType` |  | Terms and procedures for appealing a procurement decision |
| `LotDistributionType` |  | Rules for distributing lots across winning tenderers |
| `LotsGroupType` |  | A grouping of lots to which combined tendering or award rules apply |
| `PostAwardProcessType` |  | Post-award electronic process requirements — e-invoicing, e-ordering, ESPD |
| `ContractExecutionRequirementType` |  | A condition for executing the contract — social, environmental, or security clauses |
| `ContractExtensionType` |  | Extension options — number of renewals and maximum duration for the contract |
| `ContractingActivityType` |  | Type of contracting activity — works, supplies, or services |
| `ContractingPartyTypeType` |  | Type of contracting authority — central body, utility, etc. |
| `ContractingRepresentationTypeType` |  | Representation type of the contracting party — joint, central PB |
| `ContractingSystemType` |  | Procurement system used — open, restricted, negotiated, competitive |
| `EconomicOperatorRoleType` |  | The role of an economic operator in a joint or consortium tender |
| `EconomicOperatorShortListType` |  | A shortlist of pre-qualified economic operators |
| `NoticeSubTypeType` |  | Sub-type of a procurement notice — contract notice, PIN, contract award |
| `ProcurementAdditionalTypeType` |  | An additional classification label for the procurement type |
| `ProcessJustificationType` |  | Justification for deviating from standard procurement procedure |
| `BudgetAccountType` |  | A budget account for procurement funding |
| `BudgetAccountLineType` |  | A budget account line funding part of a procurement project |
| `InsurancePolicyType` |  | An insurance policy required of or provided by a tenderer |
| `SecurityClearanceTermType` |  | Security clearance requirements applicable to contract performance |
| `CompletedTaskType` |  | A completed project cited as past experience for selection criteria |
| `CriterionItemType` |  | An item or lot referenced by a selection or exclusion criterion |
| `ScoreType` |  | A numeric or weighted score given to a criterion response |
| `PrizeType` |  | A prize awarded in a design contest or competition |
| `ProjectReferenceType` |  | A reference to a project in a works or concession procurement context |
| `WorkPhaseReferenceType` |  | A reference to a phase within a works contract schedule |
| `WorkQuantityTotalType` |  | Total quantities for a bill-of-quantities work item |
| `WorkReportLineType` |  | A line reporting progress or completion on a works project item |
| `ItemInformationRequestLineType` |  | A line in a request for item performance or inventory information |
| `ItemManagementProfileType` | ✓ | A supply-chain management profile (replenishment parameters) for an item at a location — governs buyer/supplier planning terms |

---

## Group 08: Contract & Legal {#contract}

**16 ABIE types** · **8 document types** · **5 types observed in examples** · **11 XSD-only types**

Types representing contractual obligations, regulatory compliance, legal instruments, and formal declarations. ContractType is the root reference. LegislationType and RegulationType reference external law. DeclarationType covers the formal statements parties make (e.g., ESPD exclusion grounds). CustomsDeclarationType is here rather than Shipment because it is a legal filing, not a logistics operation.

**Document types in this group:**

| Document type | Description |
|---|---|
| `CertificateOfOrigin` | Certificate Of Origin |
| `ExportCustomsDeclaration` | Export Customs Declaration |
| `GuaranteeCertificate` | Guarantee Certificate |
| `ImportCustomsDeclaration` | Import Customs Declaration |
| `ProofOfReexportation` | Proof Of Reexportation |
| `ProofOfReexportationReminder` | Proof Of Reexportation Reminder |
| `ProofOfReexportationRequest` | Proof Of Reexportation Request |
| `TransitCustomsDeclaration` | Transit Customs Declaration |

**ABIE types:**

| Type | In examples | Rationale |
|---|:---:|---|
| `ContractType` | ✓ | A contract reference with type, description, and validity period |
| `AnnotationType` |  | A text annotation or note appended to a legal or regulatory document |
| `AuthorizationType` |  | An authorisation granted to a party for a regulated activity |
| `ClauseType` |  | A specific clause or provision in a contract, SLA, or terms document |
| `CustomsDeclarationType` | ✓ | A customs declaration associated with a goods movement |
| `DeclarationType` |  | A formal declaration by a party — economic, exclusion, or ethical |
| `DutyType` |  | A customs or regulatory duty applicable to imported or exported goods |
| `EndorsementType` | ✓ | An endorsement or official approval on a goods document or certificate |
| `FinancialGuaranteeType` |  | A financial guarantee — bank bond, surety bond — required by a contract |
| `ImmobilizedSecurityType` |  | An immobilised security used as financial collateral |
| `LegislationType` |  | A reference to a specific law, directive, or regulation |
| `NotificationRequirementType` | ✓ | A requirement to notify a party upon a defined trigger event |
| `RegulationType` |  | A regulatory or statutory requirement applicable to a transaction or party |
| `ResultOfVerificationType` |  | The outcome of verifying a party's declarations or credentials |
| `SecurityListingType` |  | A listing of securities held or traded by a party |
| `SignatureType` | ✓ | A digital or electronic signature on a document |

---

## Group 09: Financial, Payment & Tax {#financial}

**24 ABIE types** · **0 document types** · **16 types observed in examples** · **8 XSD-only types**

Types governing the monetary aspects of transactions. PriceType and AllowanceChargeType apply at document or line level; TaxTotalType, TaxSubtotalType, and TaxCategoryType form a hierarchy modelling VAT and other taxes. PaymentMeansType, PaymentTermsType, and PaymentType represent how and when money moves. PeriodType is included because its primary usage is in financial contexts — billing periods, settlement windows. TradingTermsType (Incoterms, retention-of-title) belongs here as it defines commercial financial obligations.

**Document types in this group:**

*No top-level document type — types used within other groups' documents.*

**ABIE types:**

| Type | In examples | Rationale |
|---|:---:|---|
| `MonetaryTotalType` | ✓ | Monetary totals for a document — line extension, tax, and payable amounts |
| `AllowanceChargeType` | ✓ | An allowance (discount) or surcharge applied at document or line level |
| `PriceType` | ✓ | A unit price with amount, currency, and optional base quantity |
| `TaxTotalType` | ✓ | The aggregate tax total for a document or line item |
| `TaxSubtotalType` | ✓ | A tax subtotal for one category within the document's total tax |
| `TaxCategoryType` | ✓ | A tax category — VAT standard rate, zero rate, exempt, reverse charge |
| `TaxSchemeType` | ✓ | A tax scheme — VAT, GST, customs duty, excise, etc. |
| `PaymentMeansType` | ✓ | The means of payment — credit transfer, card, direct debit, cheque |
| `PaymentTermsType` | ✓ | Payment terms — due dates, settlement discount, late-payment penalties |
| `PaymentType` | ✓ | An actual payment made, with amount, date, and reference |
| `PaymentMandateType` |  | A direct-debit mandate authorising recurring automatic payment |
| `FinancialAccountType` | ✓ | A bank or financial account — IBAN, account number |
| `FinancialInstitutionType` | ✓ | A financial institution (bank) identified by BIC, name, or address |
| `CardAccountType` |  | A payment card account — card type, holder, masked number |
| `CreditAccountType` |  | A credit account against which charges are billed |
| `CashRegisterType` | ✓ | A cash register or POS device used in a retail transaction |
| `ExchangeRateType` | ✓ | A currency exchange rate between source and target currencies |
| `InterestRateType` |  | An interest rate applicable to a payment obligation or financing |
| `TradeFinancingType` |  | A trade financing arrangement — letter of credit, factoring, open account |
| `TradingTermsType` |  | Commercial trading terms — Incoterms, retention of title |
| `TransactionConditionsType` | ✓ | Conditions applying to the commercial transaction — discount, retention |
| `DependentPriceReferenceType` |  | A reference defining a formula-based or index-linked price |
| `UnstructuredPriceType` |  | A price expressed as free text rather than structured amount + currency |
| `PeriodType` | ✓ | A time period defined by start and/or end date/time — billing, settlement, SLA |

---

## Group 10: Orders, Invoices & Trade Lines {#orders}

**24 ABIE types** · **18 document types** · **16 types observed in examples** · **8 XSD-only types**

Types modelling the lifecycle of a commercial transaction — from quotation and order through invoice and statement. *LineType subtypes model individual line items within each document type. The *ReferenceType subtypes link documents across the lifecycle (order → despatch → invoice). PricingReferenceType and PriceExtensionType are here rather than Financial because they describe line-level pricing logic in trade documents.

**Document types in this group:**

| Document type | Description |
|---|---|
| `CreditNote` | Credit Note |
| `DebitNote` | Debit Note |
| `Invoice` | Invoice |
| `InvoiceStatusRequest` | Invoice Status Request |
| `InvoiceStatusResponse` | Invoice Status Response |
| `Order` | Order |
| `OrderCancellation` | Order Cancellation |
| `OrderChange` | Order Change |
| `OrderResponse` | Order Response |
| `OrderResponseSimple` | Order Response Simple |
| `PurchaseReceipt` | Purchase Receipt |
| `Quotation` | Quotation |
| `Reminder` | Reminder |
| `RemittanceAdvice` | Remittance Advice |
| `RequestForQuotation` | Request For Quotation |
| `SelfBilledCreditNote` | Self Billed Credit Note |
| `SelfBilledInvoice` | Self Billed Invoice |
| `Statement` | Statement |

**ABIE types:**

| Type | In examples | Rationale |
|---|:---:|---|
| `InvoiceLineType` | ✓ | An invoice line charging for one item, service, or charge |
| `CreditNoteLineType` | ✓ | A credit-note line crediting a previously invoiced amount |
| `DebitNoteLineType` | ✓ | A debit-note line debiting an additional amount owed |
| `OrderLineType` | ✓ | A line in a purchase order |
| `LineItemType` | ✓ | An order line item with item, quantity, price, and delivery details |
| `QuotationLineType` | ✓ | A quoted line offering an item or service at a stated price |
| `RequestForQuotationLineType` | ✓ | A line in a request for quotation specifying a needed item |
| `ReceiptLineType` | ✓ | A line in a receipt advice confirming received items |
| `PurchaseReceiptLineType` | ✓ | A line confirming receipt of goods or services against a purchase order |
| `ReminderLineType` | ✓ | A line in a payment reminder referencing an outstanding invoice |
| `RemittanceAdviceLineType` | ✓ | A line matching a payment to a specific invoice or credit note |
| `StatementLineType` | ✓ | A line in an account statement showing a transaction |
| `OrderReferenceType` | ✓ | A reference to an order document |
| `OrderLineReferenceType` | ✓ | A reference to a specific line in an order document |
| `BillingReferenceType` | ✓ | A reference to a previous billing document — invoice or credit note |
| `BillingReferenceLineType` |  | A reference to a specific line in a previous billing document |
| `BuyerReferenceType` |  | A buyer-assigned reference number on an order or invoice |
| `PurchaseReferenceType` | ✓ | A reference to a purchase order or purchase agreement |
| `LineReferenceType` |  | A reference to a specific line in another document |
| `LineResponseType` |  | A response to a specific document line — accepted, rejected, or conditional |
| `RenewalType` |  | A renewal option — number of renewals and duration for an order or contract |
| `PriceExtensionType` |  | The line extension amount (unit price × quantity) with any allowances |
| `PriceListType` |  | A price list from which line prices are drawn |
| `PricingReferenceType` |  | A reference to an original or alternative price basis for comparison |

---

## Group 11: Documents, References & Responses {#documents}

**12 ABIE types** · **6 document types** · **7 types observed in examples** · **5 XSD-only types**

Types providing the documentary scaffolding common to all UBL transactions — attachments, references to other documents, and responses acknowledging receipt or acceptance. These types are cross-cutting: they appear in almost every UBL document type regardless of domain. CertificateType is included because certificates are documentary artefacts attached to many document types.

**Document types in this group:**

| Document type | Description |
|---|---|
| `ApplicationResponse` | Application Response |
| `AttachedDocument` | Attached Document |
| `DocumentStatus` | Document Status |
| `DocumentStatusRequest` | Document Status Request |
| `Enquiry` | Enquiry |
| `EnquiryResponse` | Enquiry Response |

**ABIE types:**

| Type | In examples | Rationale |
|---|:---:|---|
| `DocumentReferenceType` | ✓ | A reference to another UBL or external document by ID and type |
| `AttachmentType` | ✓ | An attachment — embedded binary or URI reference to a file |
| `ExternalReferenceType` | ✓ | A reference to an external resource — URI, file name, hash, MIME type |
| `DocumentMetadataType` | ✓ | Metadata about a document — format, encoding, version, size |
| `DocumentDistributionType` | ✓ | A distribution instruction specifying who receives copies |
| `DocumentResponseType` |  | A structured response to a received document — accept, reject, or condition |
| `ResponseType` | ✓ | A general response code and description — accept, reject, warning |
| `ResponseValueType` |  | A value (answer) provided in response to a criterion or question |
| `StatusType` | ✓ | A status code with description and optional conditions |
| `ConditionType` |  | A condition associated with a status or response (the 'why' behind a status) |
| `CertificateOfOriginApplicationType` |  | An application for issuing a certificate of origin |
| `CertificateType` |  | A certificate — quality, conformity, phytosanitary, health — for goods |

---

## Group 12: Retail, Supply Chain & Planning {#retail}

**20 ABIE types** · **9 document types** · **17 types observed in examples** · **3 XSD-only types**

Types supporting collaborative planning, forecasting, and replenishment (CPFR) between retailers and their suppliers, introduced in UBL 2.1. The domain covers forecast submission and exception handling, inventory and stock reporting, promotional event management, and supply-chain performance measurement. All types are associated with the retail and FMCG supply-chain document types (Forecast, ForecastRevision, ExceptionCriteria, RetailEvent, StockAvailabilityReport, etc.).

**Document types in this group:**

| Document type | Description |
|---|---|
| `ExceptionCriteria` | Exception Criteria |
| `ExceptionNotification` | Exception Notification |
| `Forecast` | Forecast |
| `ForecastRevision` | Forecast Revision |
| `InventoryReport` | Inventory Report |
| `ProductActivity` | Product Activity |
| `RetailEvent` | Retail Event |
| `StockAvailabilityReport` | Stock Availability Report |
| `TradeItemLocationProfile` | Trade Item Location Profile |

**ABIE types:**

| Type | In examples | Rationale |
|---|:---:|---|
| `ActivityDataLineType` | ✓ | A supply-chain activity data line — sales, shipments, or inventory at a location |
| `EventType` |  | A retail or supply-chain event — promotion, season, or holiday |
| `EventLineItemType` | ✓ | A line item within a promotional or supply-chain event |
| `EventTacticType` | ✓ | A promotional tactic — feature, display, price reduction, coupon |
| `EventTacticEnumerationType` | ✓ | An enumerated list of tactics used in a promotional event |
| `EventCommentType` |  | A comment or annotation associated with a retail or supply-chain event |
| `MiscellaneousEventType` |  | A miscellaneous supply-chain event not covered by standard categories |
| `ForecastLineType` | ✓ | A forecast quantity for an item at a location over a period |
| `ForecastRevisionLineType` | ✓ | A revised forecast line updating a previous forecast submission |
| `ForecastExceptionType` | ✓ | An exception where actual quantity deviates from forecast beyond threshold |
| `ForecastExceptionCriterionLineType` | ✓ | A criterion defining when a deviation from forecast triggers an exception |
| `ExceptionCriteriaLineType` | ✓ | A line defining a metric and threshold that triggers a supply-chain exception |
| `ExceptionNotificationLineType` | ✓ | A line in a supply-chain exception notification |
| `InventoryReportLineType` | ✓ | A line in an inventory report showing on-hand stock levels |
| `StockAvailabilityReportLineType` | ✓ | A line in a stock availability report for a SKU |
| `PerformanceDataLineType` | ✓ | A line of KPI performance data — actual versus target |
| `PromotionalEventType` | ✓ | A promotional event — sales promotion, trade event, or seasonal campaign |
| `PromotionalEventLineItemType` | ✓ | A line item in a promotional event specification |
| `PromotionalSpecificationType` | ✓ | The specification of a promotional activity |
| `RetailPlannedImpactType` | ✓ | The planned impact of a promotion on sales volume or inventory |

---

## Group 13: Digital Services & Security {#digital}

**9 ABIE types** · **2 document types** · **9 types observed in examples** · **0 XSD-only types**

Types introduced in UBL 2.2–2.3 to support eProcurement network interoperability, specifically the DigitalAgreement and DigitalCapability document types used in 4-corner network architectures (Peppol, OpenPEPPOL). Encryption types support payload security in transport-level integrations. ServiceLevelAgreementType quantifies performance commitments for a digital service.

**Document types in this group:**

| Document type | Description |
|---|---|
| `DigitalAgreement` | Digital Agreement |
| `DigitalCapability` | Digital Capability |

**ABIE types:**

| Type | In examples | Rationale |
|---|:---:|---|
| `DigitalServiceType` | ✓ | A digital service capability — document type, transport protocol, profile |
| `DigitalAgreementTermsType` | ✓ | Terms of a digital trading agreement — process scope, SLA, certificates |
| `DigitalProcessType` | ✓ | A digital business process — e.g., order-to-invoice flow or invoice process |
| `DigitalCollaborationType` | ✓ | A collaboration type defined within a digital agreement |
| `ServiceLevelAgreementType` | ✓ | An SLA specifying performance metrics for a digital or transport service |
| `MessageDeliveryType` | ✓ | Electronic message delivery endpoint and transport protocol |
| `EncryptionDataType` | ✓ | Encryption data — algorithm ID, public key, IV — for secure payload |
| `EncryptionCertificatePathChainType` | ✓ | A certificate path chain for asymmetric payload encryption |
| `EncryptionSymmetricAlgorithmType` | ✓ | Symmetric algorithm specification (AES-256-CBC, etc.) |

---

## Group 14: Utility Services {#utility}

**23 ABIE types** · **1 document types** · **0 types observed in examples** · **23 XSD-only types**

Types specific to the UtilityStatement document type introduced in UBL 2.1 for metered-utility billing (electricity, gas, water, telecommunications). All Consumption* types describe measured usage; Meter* types describe the measuring device; Telecommunications* types handle telco-specific line items. OnAccountPaymentType covers estimated-consumption advance payments common in utility billing.

**Document types in this group:**

| Document type | Description |
|---|---|
| `UtilityStatement` | Utility Statement |

**ABIE types:**

| Type | In examples | Rationale |
|---|:---:|---|
| `ConsumptionType` |  | A utility consumption quantity with type and measurement period |
| `ConsumptionLineType` |  | A line in a utility consumption report for one tariff or period |
| `ConsumptionPointType` |  | A consumption point — a meter connection point for a utility service |
| `ConsumptionReportType` |  | A consumption report summarising utility usage data |
| `ConsumptionReportReferenceType` |  | A reference to a previous consumption report |
| `ConsumptionHistoryType` |  | Historical consumption data included for comparison in a utility statement |
| `ConsumptionAverageType` |  | An average consumption figure used for comparison in a utility bill |
| `ConsumptionCorrectionType` |  | A correction applied to a previously reported consumption reading |
| `MeterType` |  | A utility meter — gas, electricity, or water — with identification and readings |
| `MeterReadingType` |  | A reading taken from a utility meter at a point in time |
| `MeterPropertyType` |  | A property of a utility meter — multiplier, dial format, accuracy class |
| `EnergyWaterSupplyType` |  | Supply details for an energy or water utility service |
| `EnergyConsumptionAllocationType` |  | An allocation of energy consumption to a specific use or cost centre |
| `EnergyTaxReportType` |  | A report on taxes (excise duty, levy) applicable to energy consumption |
| `ResourceConsumptionType` |  | Consumption of a resource — electricity, gas, water — in a billing period |
| `SubscriberConsumptionType` |  | A subscriber's consumption data in a utility statement |
| `SupplierConsumptionType` |  | A utility supplier's view of consumption for a subscriber account |
| `OnAccountPaymentType` |  | A payment on account based on estimated consumption |
| `TelecommunicationsSupplyType` |  | A telecommunications supply — a bundle of services on a bill |
| `TelecommunicationsSupplyLineType` |  | A supply line for a telecommunications service |
| `TelecommunicationsServiceType` |  | A telecommunications service line — calls, data, SMS |
| `UtilityItemType` |  | A utility tariff component — standing charge, unit rate — in a consumption line |
| `FeeType` |  | A fee charged in addition to the base utility tariff (e.g., connection fee, surcharge) |

---

## Group 15: Sustainability & Circular Economy {#sustainability}

**5 ABIE types** · **2 document types** · **1 types observed in examples** · **4 XSD-only types**

New types introduced in UBL 2.5 to support the EU Green Deal, ESPR (Ecodesign for Sustainable Products Regulation), and IMO environmental regulations. EnvironmentalEmissionType (previously the only sustainability type, used in transport and shipment examples) moves here from the Items group to consolidate all environmental data under one heading. These types have no official examples yet as of UBL 2.5 CSD02.

**Document types in this group:**

| Document type | Description |
|---|---|
| `WasteMovement` | Waste Movement |
| `WasteNotification` | Waste Notification |

**ABIE types:**

| Type | In examples | Rationale |
|---|:---:|---|
| `EnvironmentalEmissionType` | ✓ | An environmental emission — CO₂, NOₓ, SOₓ, PM — for a product, shipment, or activity |
| `CircularityProfileType` |  | Circular economy profile of a product — recycled content, repairability, durability |
| `EmissionCalculationMethodType` |  | The calculation method used to derive an environmental emission value |
| `EndOfLifeTreatmentType` |  | End-of-life treatment pathway for a product — reuse, recycle, landfill |
| `WasteGeneratedType` |  | Waste generated during production, use, or disposal of a product |

---


## Summary

| | Count |
|---|---|
| UBL 2.5 document types | **101** |
| ABIE types (total) | **310** |
| ABIE types with examples | **139** |
| ABIE types XSD-only | **171** |
| Domain groups | **15** |

---

*Classification based on UBL 2.5 CSD02 XSD and CCTS v2.01 ObjectClass naming conventions.*  
*Last updated: 2026-02-19*