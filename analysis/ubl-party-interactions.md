# UBL Party Interactions & Document Flows

This document describes how the 101 UBL 2.5 document types are exchanged between
business parties — what triggers each document, who sends it, who receives it, and
which documents logically belong together in an example set.

It is derived from the official UBL 2.5 process diagrams in the specification (`art/`
directory) and is the primary reference for building coherent, realistic XML example
sets for this repository.

---

## Party role vocabulary

The UBL specification uses consistent party role names across all its process diagrams.
The table below maps them so that example files can use the same party identifiers
when they belong to the same scenario.

| Role name used in diagrams | Meaning in examples |
|---|---|
| **Buyer / Originating Customer Party / Accounting Customer** | The organisation purchasing goods or services |
| **Seller / Supplier Party / Accounting Supplier** | The organisation selling goods or services |
| **Payee Party** | May differ from supplier — receives the actual payment |
| **Despatch Party / Consignor** | The party physically sending goods |
| **Delivery Party / Consignee** | The party physically receiving goods |
| **Forwarder** | Intermediate logistics agent consolidating or splitting shipments |
| **Transport User** | The party commissioning transport services (shipper) |
| **Transport Service Provider (TSP)** | The carrier executing the transport |
| **Transportation Network Manager** | Infrastructure authority reporting on transport progress |
| **Transport Regulator** | Regulatory body (port authority, maritime regulator) |
| **Contracting Authority** | Public body running a procurement procedure |
| **Economic Operator / Tenderer** | Supplier bidding in a procurement procedure |
| **Publication Body** | Journal/gazette publishing procurement notices |
| **Exporter / Importer Party** | Declarant submitting customs documents |
| **Customs Party** | Government customs authority |
| **Holder Party** | ATA carnet / goods passport holder |
| **Issuer Party** | Chamber of Commerce or authority issuing a passport/certificate |
| **Importing / Exporting Guarantor Party** | Body (usually Chamber of Commerce) guaranteeing goods re-export |
| **Export / Preparation / Certification Party** | Three-party chain for issuing a goods trade certificate |
| **Initiating / Responding Party** | Generic roles used in tender contract signing |
| **Participant Party 1 / 2** | Two endpoints negotiating digital interoperability |
| **Requester / Responder** | Generic enquiry roles |
| **Sender Party / Receiver Party** | Generic roles for one-way notifications |
| **Reporter Party / Authority Party** | Reporting party and receiving authority |
| **Publisher System / Registration Authority** | Roles in the business information notification process |

---

## How to read the flow notation

```
PartyA --> [DocumentName] --> PartyB
```
means PartyA sends the document and PartyB receives it.

```
PartyA <-- [DocumentName] <-- PartyB
```
is the same exchange described from the receiver's perspective (used for responses).

Documents in **bold** are the primary business document. Documents in plain text are
supporting/response documents.

---

## Group B: Order-to-Cash

**Parties:** Buyer (Originating Customer), Seller (Supplier), Payee Party

---

### B-1: Sourcing — Request for Quotation

```
Buyer   --> [RequestForQuotation] --> Seller
Buyer  <-- [Quotation]            <-- Seller
```

**Minimal example set:** `RequestForQuotation` + `Quotation`

---

### B-2: Ordering

```
Buyer --> [Order] --> Seller

# Seller can respond in two ways:
Buyer <-- [OrderResponseSimple]  <-- Seller   # immediate accept/reject
Buyer <-- [OrderResponse]        <-- Seller   # detailed response with line-level decisions

# Buyer can then:
Buyer --> [OrderChange]          --> Seller   # amend the order
Buyer --> [OrderCancellation]    --> Seller   # cancel
```

**Minimal example set:** `Order` + `OrderResponseSimple`

**Full scenario set:** `Order` → `OrderResponse` → `OrderChange` → `OrderResponse` → `OrderCancellation`

---

### B-3: Standard Billing — Invoice with Credit Note

```
Seller --> [Invoice] --> Buyer

# If overcharged:
Seller --> [CreditNote] --> Buyer

# If under-charged:
Seller --> [DebitNote]  --> Buyer

# Invoice status reconciliation (optional):
Buyer  --> [InvoiceStatusRequest]  --> Seller
Buyer <-- [InvoiceStatusResponse] <-- Seller
```

**Minimal example set:** `Invoice`

**Full scenario set (credit):** `Invoice` + `CreditNote` + `InvoiceStatusResponse`

**Full scenario set (debit):** `Invoice` + `DebitNote` + `InvoiceStatusResponse`

> The `InvoiceStatusRequest` / `InvoiceStatusResponse` pair can also appear independently
> of a correction — the buyer queries status and the seller confirms no action is needed.

---

### B-4: Self-Billing

The **buyer** raises the invoice on behalf of the seller.

```
Buyer --> [SelfBilledInvoice] --> Seller

# If buyer over-charged (compared to actual delivery):
Buyer --> [SelfBilledCreditNote] --> Seller

# If seller disputes (discrepancy in charges):
Seller --> [ApplicationResponse] --> Buyer
```

**Minimal example set:** `SelfBilledInvoice`

**Full scenario set:** `SelfBilledInvoice` + `SelfBilledCreditNote`

---

### B-5: Payment Settlement

```
# Reminder (seller to buyer for unpaid invoice):
Seller --> [Reminder] --> Buyer

# Remittance advice (buyer notifies seller and payee of payment):
Buyer --> [RemittanceAdvice] --> Seller
Buyer --> [RemittanceAdvice] --> Payee Party   # if payee differs from seller

# Statement of account (periodic):
Seller --> [Statement] --> Buyer
```

**Typical pairing:** `Invoice` → `Reminder` → `RemittanceAdvice`

**Statement scenario:** `Statement` (standalone — summarises multiple open invoices)

---

### B-6: Purchase Receipt

```
Buyer --> [PurchaseReceipt] --> Seller   # confirmation of goods/services received
```

Links back to the originating `Order` via `OrderReference`.

---

### B-7: Freight Invoice

```
Transport Service Provider --> [FreightInvoice] --> Transport User
```

Follows a completed transport execution (see Group D). Shares billing structure with
`Invoice` but references transport-specific data (`ConsignmentID`, `ShipmentID`).

**Minimal example set:** `FreightInvoice` (standalone or paired with `TransportExecutionPlan`)

---

## Group C: Fulfilment & Goods

**Parties:** Despatch Party (Seller/Consignor), Delivery Party (Buyer/Consignee),
Forwarder, Logistics Operator, Authority Party

---

### C-1: Simple Fulfilment — one shipment, one consignment

```
Despatch Party --> [DespatchAdvice]  --> Delivery Party
Despatch Party <-- [ReceiptAdvice]   <-- Delivery Party

# If fulfilment is cancelled:
Despatch Party --> [FulfilmentCancellation] --> Delivery Party
```

**Minimal example set:** `DespatchAdvice` + `ReceiptAdvice`

**Cancellation set:** `DespatchAdvice` + `FulfilmentCancellation`

> The `DespatchAdvice` references the original `Order` via `OrderReference`.
> The `ReceiptAdvice` references the `DespatchAdvice`.

---

### C-2: Split Fulfilment — one shipment, multiple consignments

Same document types as C-1, but multiple `DespatchAdvice` documents all reference the
same `OrderReference`, with each covering a subset of the ordered lines.

**Example set:** `Order` + 2× `DespatchAdvice` (different `ConsignmentID`) + `ReceiptAdvice`

---

### C-3: Intermediary Fulfilment (via forwarder)

```
Supplier --> [DespatchAdvice] --> Forwarder     # consignment in
Forwarder --> [DespatchAdvice] --> Buyer        # consignment(s) out
Buyer     --> [ReceiptAdvice]  --> Forwarder
Forwarder --> [ReceiptAdvice]  --> Supplier
```

---

### C-4: Goods documents (travel with the cargo)

```
# Shipper instructs freight forwarder:
Shipper --> [ForwardingInstructions] --> Forwarder

# Carrier issues to shipper (proof of receipt):
Carrier --> [BillOfLading]          --> Shipper

# Road/air/rail transport document:
Carrier --> [Waybill]               --> Shipper

# Packing detail (accompanies shipment):
Supplier --> [PackingList]          --> Buyer

# Weight certification (port / weigh station):
Weighing Party --> [WeightStatement] --> Shipper / Authority

# Delivery confirmation note:
Supplier --> [DeliveryNote]         --> Buyer
```

**Typical set for a sea shipment:**
`ForwardingInstructions` → `BillOfLading` + `PackingList` + `WeightStatement`

**Road/Air set:** `ForwardingInstructions` + `Waybill` + `PackingList`

---

### C-5: Manifest

```
Sending Logistics Operator --> [Manifest] --> Authority Party
```

Submitted at port or border. References multiple consignments.

---

### C-6: Returns

```
Buyer  --> [InstructionForReturns] --> Seller   # buyer instructs return
```

Followed by a reverse-direction `DespatchAdvice` (Buyer as despatch party).

---

### C-7: Goods Certificate for export

Three-party certification chain:

```
Export Party  --> [GoodsCertificate] (draft)  --> Preparation Party
Preparation Party --> [GoodsCertificate] (bundle) --> Certification Party
Certification Party --> [GoodsCertificate] (stamped) --> Preparation Party
Preparation Party --> [GoodsCertificate] (authorised) --> Export Party

# If rejected:
Certification Party --> [ApplicationResponse] (reject) --> Preparation Party
```

---

## Group D: Transport Operations

**Parties:** Transport User, Transport Service Provider (TSP),
Transportation Network Manager, Transport Regulator

---

### D-1: Service Discovery

```
Transport User --> [TransportServiceDescriptionRequest] --> TSP
Transport User <-- [TransportServiceDescription]        <-- TSP
```

---

### D-2: Booking & Execution Plan (negotiation loop)

```
Transport User --> [TransportExecutionPlanRequest] (NotConfirmed) --> TSP

# TSP accepts:
Transport User <-- [TransportExecutionPlan] (Confirmed) <-- TSP
Transport User --> [TransportExecutionPlan] (Confirmed) --> TSP   # buyer confirms

# TSP rejects:
Transport User <-- [TransportExecutionPlan] (Rejected)  <-- TSP

# Buyer rejects TSP's plan and updates request:
Transport User --> [TransportExecutionPlanRequest] (updated) --> TSP   # loop
```

---

### D-3: Goods Item Itinerary

```
TSP --> [GoodsItemItinerary] --> Transport User   # planned multi-leg route
```

Referenced by the `TransportExecutionPlan`.

---

### D-4: Shipment Status Monitoring

```
# Shipper queries carrier:
Sender Party --> [TransportationStatusRequest] --> Receiver Party
Sender Party <-- [TransportationStatus]         <-- Receiver Party

# OR carrier pushes status unprompted:
TSP --> [TransportationStatus] --> Transport User
```

---

### D-5: Transport Progress (infrastructure/regulator)

```
TSP                    --> [TransportProgressStatusRequest] --> Network Manager
TSP                   <-- [TransportProgressStatus]         <-- Network Manager
```

---

### D-6: Common Transportation Report (authority reporting)

```
Reporter Party --> [CommonTransportationReport] --> Authority Party
```

---

### D-7: Full intermodal flow

A complete intermodal scenario combines documents from D-1 through D-6:

```
Transport User --> [TransportServiceDescriptionRequest] --> TSP
Transport User <-- [TransportServiceDescription]        <-- TSP
Transport User --> [TransportExecutionPlanRequest]      --> TSP
Transport User <-- [TransportExecutionPlan] (Confirmed) <-- TSP
TSP            --> [GoodsItemItinerary]                 --> Transport User
TSP            --> [TransportationStatus]               --> Transport User
TSP            --> [TransportProgressStatusRequest]     --> Network Manager
TSP           <-- [TransportProgressStatus]             <-- Network Manager
TSP            --> [FreightInvoice]                     --> Transport User
```

---

## Group E: Customs & Trade Compliance

**Parties:** Exporter/Importer/Transit Exporter Party, Customs Party,
Holder Party, Issuer Party, Importing/Exporting Guarantor Party,
Export/Preparation/Certification Party

---

### E-1: Export Customs Declaration

```
Exporter --> [ExportCustomsDeclaration]     --> Customs Party
Exporter <-- [ExportCustomsDeclaration] (stamped) <-- Customs Party   # approved
Exporter <-- [ApplicationResponse] (reject) <-- Customs Party          # rejected
```

---

### E-2: Import Customs Declaration

```
Importer --> [ImportCustomsDeclaration] --> Customs Party
Importer <-- [ApplicationResponse] (approved / rejected) <-- Customs Party
```

---

### E-3: Transit Customs Declaration

```
Transit Exporter --> [TransitCustomsDeclaration] --> Customs Party
Transit Exporter <-- [ApplicationResponse] (approved / rejected) <-- Customs Party
```

---

### E-4: Goods Item Passport — Approval

```
Holder Party --> [GoodsItemPassport] (drafted)    --> Issuer Party
Holder Party <-- [ApplicationResponse] (declined) <-- Issuer Party   # rejected
Holder Party <-- [GoodsItemPassport] (authorised) <-- Issuer Party   # approved
```

---

### E-5: Goods Item Passport — Presentation at border (export + import)

```
# At exporting border:
Holder --> [GoodsItemPassport] (approved)  --> Exporting Customs
Holder <-- [ApplicationResponse] (reject)  <-- Exporting Customs    # if invalid
Holder <-- [GoodsItemPassport] (exported)  <-- Exporting Customs    # if valid

# At importing border:
Holder --> [GoodsItemPassport] (exported)  --> Importing Customs
Holder <-- [ApplicationResponse] (reject)  <-- Importing Customs
Holder <-- [GoodsItemPassport] (imported)  <-- Importing Customs
```

---

### E-6: Goods Item Passport — Return

```
# At importing border (goods returning):
Holder --> [GoodsItemPassport] (imported)    --> Importing Customs
Holder <-- [GoodsItemPassport] (reexported)  <-- Importing Customs

# At exporting (original) border:
Holder --> [GoodsItemPassport] (reexported)  --> Exporting Customs
Holder <-- [GoodsItemPassport] (reimported)  <-- Exporting Customs
```

---

### E-7: Proof of Re-exportation

```
Importing Customs --> [ProofOfReexportationRequest] --> Importing Guarantor
Importing Guarantor --> [ProofOfReexportationRequest] --> Exporting Guarantor
Exporting Guarantor --> [ProofOfReexportation]        --> Importing Guarantor
Importing Guarantor --> [ProofOfReexportation]        --> Importing Customs

# If goods have not left / rejected:
Exporting Guarantor --> [ApplicationResponse] (declined) --> Importing Guarantor
Importing Guarantor --> [ApplicationResponse]            --> Importing Customs

# Overdue:
Importing Customs --> [ProofOfReexportationReminder] --> Importing Guarantor
```

---

### E-8: Full ATA Carnet example set

Coherent set covering an item taken abroad for a trade fair and returned:
`GoodsItemPassport` (authorised) → `GoodsItemPassport` (exported) →
`GoodsItemPassport` (imported) → `GoodsItemPassport` (reexported) →
`GoodsItemPassport` (reimported) → `ProofOfReexportation`

---

## Group F: Catalogue Management

**Parties:** Receiver Party (Buyer/Procurer), Provider Party (Supplier)

All catalogue transactions follow the same request–accept/reject–document–acknowledge
pattern. Either party can initiate.

---

### F-1: Publish Catalogue

```
Receiver --> [CatalogueRequest]         --> Provider   # buyer-initiated
                                                       # OR provider-initiated (no request)
Receiver <-- [ApplicationResponse] (accept/reject) <-- Provider

Provider --> [Catalogue]                --> Receiver
Receiver --> [ApplicationResponse] (accept/query/reject) --> Provider
```

**Minimal example set:** `CatalogueRequest` + `Catalogue` + `ApplicationResponse`

---

### F-2: Update Catalogue Pricing

```
Receiver --> [CatalogueRequest]          --> Provider   # optional request
Provider --> [CataloguePricingUpdate]    --> Receiver
Receiver --> [ApplicationResponse]       --> Provider
```

---

### F-3: Update Item Specification

```
Provider --> [CatalogueItemSpecificationUpdate] --> Receiver
Receiver --> [ApplicationResponse]              --> Provider
```

---

### F-4: Delete Catalogue

```
Provider --> [CatalogueDeletion]   --> Receiver
Receiver --> [ApplicationResponse] --> Provider
```

---

### F-5: Full catalogue lifecycle set

`CatalogueRequest` → `Catalogue` → `CataloguePricingUpdate` →
`CatalogueItemSpecificationUpdate` → `CatalogueDeletion`

Each step with its `ApplicationResponse`.

---

## Group G: Procure-to-Award

**Parties:** Contracting Authority (CA), Economic Operator (EO) / Tenderer,
Publication Body, Financial Institution (for guarantees)

The full pre-award process has six phases. Documents shown below are as
published in the UBL 2.3 pre-award process diagram.

---

### G-1: Market Engagement (optional pre-notification)

```
CA   --> [PriorInformationNotice]       --> Publication Body
CA   --> [PriorInformationNotice]       --> EO (broadcast)
```

---

### G-2: Launch Procedure

```
CA   --> [ContractNotice]               --> Publication Body
CA   --> [CallForTenders]               --> EO
```

---

### G-3: Expression of Interest

```
EO   --> [ExpressionOfInterestRequest]  --> CA
EO  <-- [ExpressionOfInterestResponse] <-- CA
```

---

### G-4: Qualification (for restricted/negotiated procedures)

```
CA   --> [QualificationApplicationRequest]  --> EO
CA  <-- [QualificationApplicationResponse] <-- EO

# CA evaluates and may send:
EO  <-- [TendererQualificationResponse]    <-- CA
```

Also, separately, a tenderer may submit unsolicited qualification data:
```
EO   --> [TendererQualification]            --> CA
```

---

### G-5: Tender Status Enquiry (EO-initiated at any point)

```
EO   --> [TenderStatusRequest] --> CA
EO  <-- [TenderStatus]         <-- CA
```

---

### G-6: Tender Submission

```
EO   --> [Tender]          --> CA
EO  <-- [TenderReceipt]   <-- CA

# EO may withdraw:
EO   --> [TenderWithdrawal] --> CA
```

---

### G-7: Guarantee Deposit

```
EO gets [GuaranteeCertificate] from Financial Institution
EO   --> [GuaranteeCertificate] --> CA
```

---

### G-8: Unsubscribe

```
EO   --> [UnsubscribeFromProcedureRequest]  --> CA
EO  <-- [UnsubscribeFromProcedureResponse] <-- CA
```

---

### G-9: Award

```
CA   --> [AwardedNotification]   --> winning EO
CA   --> [UnawardedNotification] --> losing EOs
CA   --> [ContractAwardNotice]   --> Publication Body
```

---

### G-10: Contract Signing (Pre-initiated by CA)

```
CA   --> [TenderContract]           --> EO        # CA signs first
EO      adds W3C digital signature
EO  --> [TenderContract]            --> CA        # EO returns signed
CA      adds second signature
CA  --> [TenderContract]            --> EO        # final fully-signed copy
```

---

### G-11: Works Reporting (Post-award)

```
EO   --> [WorkReport]  --> CA   # periodic report on works performed
```

---

### G-12: Procurement Status (CA or EO can query)

```
Requester --> [ProcurementStatusRequest] --> CA
Requester <-- [ProcurementStatus]        <-- CA
```

---

### G-13: Minimal example sets by sub-process

| Scenario | Documents |
|---|---|
| Open procedure (simplified) | `ContractNotice` → `CallForTenders` → `Tender` → `TenderReceipt` → `AwardedNotification` + `UnawardedNotification` → `ContractAwardNotice` → `TenderContract` |
| Restricted procedure | adds `QualificationApplicationRequest` + `QualificationApplicationResponse` before `CallForTenders` |
| EoI pre-step | prepends `PriorInformationNotice` + `ExpressionOfInterestRequest` + `ExpressionOfInterestResponse` |
| Tender withdrawal | `Tender` → `TenderReceipt` → `TenderWithdrawal` |
| Status query | `TenderStatusRequest` + `TenderStatus` |
| Guarantee | `GuaranteeCertificate` (standalone, references tender) |
| Works contract | `TenderContract` → `WorkReport` |

---

## Group H: Retail & Supply Chain Planning (CPFR)

**Parties:** Retailer (Buyer side), Supplier/Producer (Seller side)

CPFR (Collaborative Planning, Forecasting and Replenishment) is a nine-step
process defined by the GS1 CPFR standard. UBL documents cover steps 1–2
(setup) and steps 6–9 (execution).

---

### H-1: Establish Collaboration (Step 1)

```
# Exception criteria negotiation:
Retailer --> [ExceptionCriteria]          --> Supplier
Retailer <-- [ExceptionCriteria revision] <-- Supplier  # loop until accepted
```

---

### H-2: Create Joint Business Plan (Step 2)

```
# Retail event coordination:
Retailer --> [RetailEvent]               --> Supplier
Supplier --> [RetailEvent revision]      --> Retailer   # loop until accepted

# Trade item location profiling:
Retailer --> [TradeItemLocationProfile]  --> Supplier   # or supplier-initiated
Supplier --> [TradeItemLocationProfile revision] --> Retailer
```

---

### H-3: Sales Forecasting (Step 3–5, partially manual)

```
Retailer --> [Forecast]         --> Supplier
Supplier --> [ForecastRevision] --> Retailer  # loop until accepted
```

---

### H-4: Execution — Activity Data & Ordering (Steps 6–9)

```
Retailer --> [ItemInformationRequest] --> Supplier   # request POS/sales data
Supplier --> [ProductActivity]        --> Retailer   # actual POS data
Supplier --> [StockAvailabilityReport]--> Retailer   # current stock
Retailer --> [InventoryReport]        --> Supplier   # retailer inventory

# Exception handling:
Supplier --> [ExceptionNotification]  --> Retailer   # exception signal
```

---

### H-5: Minimal example sets

| Scenario | Documents |
|---|---|
| Collaboration setup | `ExceptionCriteria` + `RetailEvent` + `TradeItemLocationProfile` |
| Forecasting | `Forecast` + `ForecastRevision` |
| Execution | `ItemInformationRequest` + `ProductActivity` + `InventoryReport` + `ExceptionNotification` |
| Full CPFR cycle | All of the above in sequence |

---

## Group I: Utility Billing

**Parties:** Accounting Supplier (Utility), Accounting Customer (Consumer)

---

### I-1: Utility Billing Process

```
Supplier --> [Invoice]          --> Customer   # from billing process
Supplier --> [UtilityStatement] --> Customer   # detailed usage report

# Customer reconciles:
Customer --> [InvoiceStatusRequest]  --> Supplier   # if querying
Customer <-- [InvoiceStatusResponse] <-- Supplier
```

**Minimal example set:** `UtilityStatement` (standalone — summarises meter readings
and consumption)

**Full set:** `Invoice` + `UtilityStatement` + `InvoiceStatusResponse`

> The `UtilityStatement` references the same billing period as the `Invoice` and
> includes `MeterReading`, `ConsumptionReport`, and `SubscriberConsumption` data.

---

## Group J: Digital Interoperability

**Parties:** Participant Party 1, Participant Party 2

---

### J-1: Capability Discovery and Agreement

```
# Phase 1 — Capability exchange:
Party 1 --> [DigitalCapability]   --> Party 2
Party 2 --> [ApplicationResponse] --> Party 1   # acknowledges / accepts

# Phase 2 — Agreement negotiation:
Party 2 --> [DigitalAgreement]    --> Party 1
Party 1 --> [ApplicationResponse] --> Party 2   # Party 1 accepts or counters

# If Party 1 needs to counter:
Party 1 --> [DigitalAgreement]    --> Party 2   # revised agreement
Party 2 --> [ApplicationResponse] --> Party 1
```

**Minimal example set:** `DigitalCapability` + `DigitalAgreement` + `ApplicationResponse`

> `DigitalCapability` is typically published to an SMP (Service Metadata Publisher)
> in a Peppol-style 4-corner network, not sent directly. `DigitalAgreement` is then
> exchanged between the two corners.

---

## Group K: Party & Business Profile

**Parties:** Business Party (publisher), Business Parties 0..n (recipients),
Economic Operator, Registration Authority, Publisher System

---

### K-1: Business Card

```
Business Party 1 --> [BusinessCard] --> Business Parties 0..n
                                        (published / broadcast, no response)
```

**Minimal example set:** `BusinessCard` (standalone)

---

### K-2: Business Information (Registration Notification)

Three-party notification process:

```
# Publisher publishes conformant registration information:
Publisher System --> BusinessInformation Notice --> EO (data entry agent)

# EO submits registration request:
EO --> Business Registration Request --> Registration Authority
Registration Authority processes and confirms
Registration Authority --> BusinessInformation --> Publisher System
Publisher System publishes notice --> EO
```

UBL document: `BusinessInformation`

**Minimal example set:** `BusinessInformation` (standalone — the published record)

---

## Group L: Sustainability & Environment

**Parties:** Sender Party, Receiver Party

Both waste documents follow the same simple notification pattern.

---

### L-1: Waste Notification (advance notice)

```
Sender --> [WasteNotification] --> Receiver
Sender <-- [ApplicationResponse] <-- Receiver
```

---

### L-2: Waste Movement (actual transport record)

```
Sender --> [WasteMovement] --> Receiver
                              (no response document — one-way)
```

**Typical paired set:** `WasteNotification` + `ApplicationResponse` + `WasteMovement`

> `WasteNotification` is sent **before** the waste is collected (advance notification
> required by the Basel Convention for transboundary waste movements).
> `WasteMovement` accompanies the physical movement.

---

## Group M: Administrative & General

These documents are **process-agnostic** and appear alongside documents from any other
group. They do not form a standalone business scenario but are used to request
information, acknowledge receipt, or wrap attachments.

---

### M-1: Enquiry

```
Requester --> [Enquiry]         --> Responder
Requester <-- [EnquiryResponse] <-- Responder
```

Can reference any business document (order, tender, shipment, etc.) via
`AdditionalDocumentReference`.

---

### M-2: Document Status

```
Requester --> [DocumentStatusRequest] --> Responder
Requester <-- [DocumentStatus]        <-- Responder
```

Used to ask "what is the current processing status of document X?".

---

### M-3: Application Response

```
Responder --> [ApplicationResponse] --> Requester
```

Generic accept/reject/acknowledge for any business document. Used across
Groups B, C, E, F, H, J, K, and L as the confirmation mechanism.

---

### M-4: Attached Document

```
Sender --> [AttachedDocument] --> Receiver
```

Wraps any binary or XML document for transport. No response expected.

---

## Cross-process example scenarios

These are multi-group scenarios that illustrate how documents from different process
groups combine into a complete business transaction.

---

### Scenario 1: End-to-end trade — from catalogue to payment

| Step | Group | Document |
|---|:---:|---|
| Supplier publishes catalogue | F | `Catalogue` |
| Buyer requests quotation | B | `RequestForQuotation` |
| Supplier quotes | B | `Quotation` |
| Buyer places order | B | `Order` |
| Seller accepts | B | `OrderResponseSimple` |
| Seller despatches | C | `DespatchAdvice` |
| Goods travel by sea | C | `BillOfLading` + `PackingList` |
| Buyer receives and confirms | C | `ReceiptAdvice` |
| Seller invoices | B | `Invoice` |
| Buyer pays | B | `RemittanceAdvice` |

---

### Scenario 2: International shipment with customs

| Step | Group | Document |
|---|:---:|---|
| Seller arranges freight | D | `TransportExecutionPlanRequest` + `TransportExecutionPlan` |
| Seller instructs forwarder | C | `ForwardingInstructions` |
| Carrier issues bill of lading | C | `BillOfLading` |
| Seller files export declaration | E | `ExportCustomsDeclaration` |
| Customs stamps declaration | E | `ExportCustomsDeclaration` (approved) |
| Seller despatches | C | `DespatchAdvice` + `PackingList` |
| Buyer files import declaration | E | `ImportCustomsDeclaration` |
| Customs responds | M | `ApplicationResponse` |
| Buyer receives | C | `ReceiptAdvice` |
| Carrier invoices transport | B | `FreightInvoice` |
| Seller invoices goods | B | `Invoice` |

---

### Scenario 3: Public procurement → contract → works

| Step | Group | Document |
|---|:---:|---|
| CA publishes notice | G | `PriorInformationNotice` + `ContractNotice` |
| CA invites | G | `CallForTenders` |
| EO expresses interest | G | `ExpressionOfInterestRequest` + `ExpressionOfInterestResponse` |
| EO submits qualification | G | `TendererQualification` |
| CA requests qualification info | G | `QualificationApplicationRequest` + `QualificationApplicationResponse` |
| EO submits tender | G | `Tender` + `TenderReceipt` |
| EO provides guarantee | G | `GuaranteeCertificate` |
| CA awards | G | `ContractAwardNotice` + `AwardedNotification` + `UnawardedNotification` |
| Contract signed | G | `TenderContract` (3 exchanges) |
| Works performed | G | `WorkReport` |
| Works invoiced | B | `Invoice` |

---

### Scenario 4: Goods Item Passport (ATA Carnet) full lifecycle

| Step | Group | Document |
|---|:---:|---|
| Holder requests passport | E | `GoodsItemPassport` (drafted) |
| Issuer approves | E | `GoodsItemPassport` (authorised) |
| Export border crossing | E | `GoodsItemPassport` (exported) |
| Import border crossing | E | `GoodsItemPassport` (imported) |
| Return export | E | `GoodsItemPassport` (reexported) |
| Return import | E | `GoodsItemPassport` (reimported) |
| Guarantor confirms return | E | `ProofOfReexportation` |

---

### Scenario 5: CPFR → replenishment order → delivery

| Step | Group | Document |
|---|:---:|---|
| Establish exception criteria | H | `ExceptionCriteria` |
| Create retail event plan | H | `RetailEvent` + `TradeItemLocationProfile` |
| Share forecast | H | `Forecast` |
| Share POS data | H | `ProductActivity` + `InventoryReport` |
| Exception raised | H | `ExceptionNotification` |
| Replenishment order | B | `Order` |
| Seller despatches | C | `DespatchAdvice` |
| Buyer confirms | C | `ReceiptAdvice` |

---

### Scenario 6: Utility billing cycle

| Step | Group | Document |
|---|:---:|---|
| Meter reading period ends | I | `UtilityStatement` |
| Invoice issued | B | `Invoice` |
| Customer queries | B | `InvoiceStatusRequest` |
| Supplier confirms | B | `InvoiceStatusResponse` |
| Customer pays | B | `RemittanceAdvice` |

---

### Scenario 7: Digital onboarding → first transaction

| Step | Group | Document |
|---|:---:|---|
| Party 1 publishes capabilities | J | `DigitalCapability` |
| Parties agree protocol | J | `DigitalAgreement` + `ApplicationResponse` |
| Supplier publishes catalogue | F | `Catalogue` |
| Buyer places first order | B | `Order` |

---

*Last updated: 2026-02-19. Source: UBL 2.5 CSD02 process diagrams (`art/` directory).*
