# Research Session Decisions — UBL Sample Documents

**Session date:** 2026-02-19
**Branch:** `claude/research-ubl-samples-3IuwR`
**Purpose:** Record what was researched, what was agreed, how decisions were reached,
and which parties exchange which UBL documents — so this can serve as the authoritative
foundation for building coherent XML example sets.

---

## 1. What we set out to do

The session started with: *"lets do some research together into sample documents for UBL"*.

The goal was to build up enough understanding of the UBL 2.5 standard to create validated
sample XML documents that:
- Are realistic and logically related to each other (same fictional companies, same scenario)
- Cover as many of the UBL document types as possible
- Pass XML, XSD, and semantic validation

---

## 2. Key findings during research

### 2.1 UBL 2.5 has 101 document types, not 91

Initial research pointed to UBL 2.3 (91 document types). After locating the UBL 2.5 CSD02
zip at `/tmp/UBL-2.5.zip` and inspecting the `/xsdrt/maindoc/` directory, the actual count
was confirmed as **101 document types**.

The additional 10 types in UBL 2.5 compared to 2.3 include:
- `AnnotationType`-backed documents
- `WasteNotification`, `WasteMovement` (sustainability)
- `InvoiceStatusRequest`, `InvoiceStatusResponse`
- `PurchaseReceipt`
- `ProcurementStatus`, `ProcurementStatusRequest`
- `UnsubscribeFromProcedureRequest`, `UnsubscribeFromProcedureResponse`
- `WorkReport`

### 2.2 The XSD contains 310 Common Aggregate Component (ABIE) types

Parsing `UBL-CommonAggregateComponents-2.5.xsd` revealed **310 complexType definitions**.
These are the building blocks nested inside the 101 document types.

Additionally, `UBL-CommonBasicComponents-2.5.xsd` defines the scalar elements (dates,
amounts, codes, identifiers). These ~1,100 CBC elements live inside the 310 ABIE types.
Every type, and therefore every CBC element, is covered by the classification documents.

---

## 3. Classification approach — two complementary views

### 3.1 Bottom-up: domain grouping by semantic type names

**Decision:** Group the 310 ABIE types by their CCTS ObjectClass name, then assign the
101 document types to whichever group owns their root ABIE.

**Rationale:** UBL deliberately encodes domain membership in type names. `PaymentMeansType`
obviously belongs to financial; `ShipmentStageType` belongs to transport. This produces
groups that are stable and immediately intelligible to someone reading XSD.

**Output:** `analysis/ubl-domain-groups.md` — 15 domain groups, all 310 types, all 101 docs.

**Correction made during session:** `BusinessInformation` was initially placed in
*Maritime & Port Operations* because the search for `OperationTypeType` was run while
studying maritime types, and the CCTS `OperationType` was misread as referring to a
*vessel operation*. The correct reading (CCTS definition: *"a code to specify the type
of operation (e.g. deletion)"*) makes clear it is a generic CRUD classifier. Both the
document and `OperationTypeType` were moved to **Party & Organization**, where
`BusinessCard` (its sibling document) already sat.

**Lesson recorded:** Type name proximity is not sufficient for classification; the CCTS
ObjectClass definition and the sibling elements of the parent document must be checked.

### 3.2 Top-down: process grouping starting from documents

**Decision:** Build a usage matrix — which ABIE types does each document directly reference —
then assign types to the process group of the documents that most use them.

**Rationale:** The bottom-up view assigns `AllowanceChargeType` to Financial, but it is
used in 13/14 Order-to-Cash documents and almost nowhere else. Starting from documents
prevents this. It also surfaces an explicit **Common Infrastructure** tier: types used in
15 or more documents (`SignatureType` in all 101, `PartyType` in ~90, `DocumentReferenceType`
in 82) belong to no single process and must be treated as backbone.

**Output:** `analysis/ubl-process-groups.md` — 13 process groups (A–M), all 310 types.

**Key structural insight from the top-down view:**
- **3 bottom-up groups dissolve:** Financial/Payment/Tax (absorbed into Order-to-Cash),
  Address/Location/Communication (becomes infrastructure), Documents/References/Responses
  (becomes infrastructure — `DocumentReferenceType` is in 82/101 docs)
- **1 new group surfaces:** Common Infrastructure (11 types with ≥15 doc usage)

Both classification documents are kept as they serve different purposes:
- `ubl-domain-groups.md` → answer "what is this type for?"
- `ubl-process-groups.md` → answer "which process does this document belong to?"

---

## 4. Party interactions document

**Output:** `analysis/ubl-party-interactions.md`

This document was derived from the official UBL 2.5 process diagrams (PNG files in the
`art/` directory of the specification) and records:
- A canonical **party role vocabulary** mapping UBL role names to plain descriptions
- ~40 sub-process flows (who sends what to whom, what triggers it, what responds)
- Minimal and full example sets for each flow
- 7 cross-process scenarios (end-to-end trade, international shipment + customs, etc.)

---

## 5. The canonical party set for examples

### 5.1 Starting point: minimum number of parties

**Question posed:** *"In a hypothetical world where everyone uses UBL and there is the
minimum number of companies — each really good at one thing — how many distinct parties
would there be?"*

**First answer: 9 parties — later expanded to 26 + Consumer**

The logic: which roles genuinely require a different *type* of organisation, such that
merging them would either break the process or create a conflict of interest?

| # | Party | Core specialisation | Why it cannot be merged |
|---|---|---|---|
| 1 | Buyer | Needs things | Can't be own counterparty |
| 2 | Seller | Supplies things | Can't be own counterparty |
| 3 | Freight Forwarder | Moves things on paper (consolidation, docs) | IMFM diagrams show distinct swim lane from Carrier |
| 4 | Carrier | Moves things physically | Distinct from Forwarder; issues transport docs |
| 5 | Port / Network Authority | Manages infrastructure, reports positions | Knows network state; neither buys nor sells |
| 6 | Customs Authority | Stamps declarations | Only body with legal authority to clear goods |
| 7 | Chamber of Commerce | Issues trust documents (GoodsItemPassport, GoodsCertificate) | Semi-private trust anchor; different from public gazette |
| 8 | Government Information Service | Publishes procurement notices + business registry | Never buys/sells; purely public record |
| 9 | Financial Institution | Holds accounts, routes payments, issues guarantees | Payee/guarantor role must be independent of commercial party |

### 5.2 Consolidation considered but reversed

During the session a consolidation from the original 26+C list down to 13 parties was
explored. The rationale included merging carrier modal types, supply chain tiers, and
financial institution roles. After review, the decision was reversed: the full 26+C
set is more faithful to UBL's actual process diagrams and avoids forcing unrelated roles
onto a single fictional entity.

Key consolidations that were tried and then undone:

| Consolidation tried | Why reversed |
|---|---|
| 5 carrier types → 1 carrier | Ocean/Air/Road/Rail/Inland each have distinct document types (`BillOfLading` vs `Waybill` vs `AirWaybill`) and interact with different infrastructure parties |
| 3 supply tiers → 1 seller | S1/S2/S3 have different positions in the chain — raw material supplier, manufacturer, and distributor each appear as `AccountingSupplierParty` in different flows |
| 3 infrastructure parties → 1 port authority | Seaport, airport, and intermodal hub each interact with their respective carrier type |
| 4 financial roles → 1 bank | Buyer's bank, seller's bank, factor, and guarantor have legally distinct roles; a single bank playing all four creates conflicts of interest |
| Customs declarant merged with exporter | The declarant/broker is a licensed agent distinct from the goods owner |

### 5.3 Final agreed party set (26 + Consumer)

The numbering below matches the original provisional matrix from the session start.
Parties 16–18 (infrastructure) and 20–21 (trust/publication) were implied in that
matrix and are filled in here. Fictional company names are **not yet assigned** —
that will be done in a separate session.

#### Demand Side

| # | Alias | Role | UBL roles covered |
|---|---|---|---|
| **1** | — | Commercial Buyer | AccountingCustomerParty, Transport User, Importer, Digital Participant A |
| **2** | — | Contracting Authority | ContractingParty, Waste Sender |
| **3** | — | Customs Declarant / Broker | ExporterParty / ImporterParty (declarant role on behalf of goods owner) |

#### Supply Side

| # | Alias | Role | UBL roles covered |
|---|---|---|---|
| **4** | S3 | Raw Material Supplier | AccountingSupplierParty (upstream), Consignor |
| **5** | S1 | Manufacturer | AccountingSupplierParty, Economic Operator/Tenderer, Exporter, Utility Provider, Digital Participant B |
| **6** | S2 | Distributor | AccountingSupplierParty (distribution tier), Catalogue publisher |
| **7** | S4 | Waste Processor | SellerParty (scrap/waste services), Waste receiver |

#### Warehousing

| # | Alias | Role | UBL roles covered |
|---|---|---|---|
| **8** | W1 | Seller's Warehouse (outbound 3PL) | DespatchParty, ConsignorParty on transport docs, sends InventoryReport to Seller |
| **9** | W2 | Buyer's Warehouse (inbound 3PL) | DeliveryParty, issues ReceiptAdvice on behalf of Buyer, sends InventoryReport to Buyer |

#### Logistics — Carriers

| # | Alias | Role | UBL roles covered |
|---|---|---|---|
| **10** | — | Freight Forwarder | Forwarder, Intermediary Consignee/Consignor, Preparation Party |
| **11** | L1 | Ocean Carrier | TSP (sea), issues BillOfLading, Reporter Party |
| **12** | L2 | Air Carrier | TSP (air), issues AirWaybill |
| **13** | L3 | Road Carrier | TSP (road), issues Waybill |
| **14** | L4 | Rail Carrier | TSP (rail), issues rail consignment note |
| **15** | L5 | Inland Waterway Carrier | TSP (inland), issues inland waterway bill |

#### Logistics — Infrastructure

| # | Alias | Role | UBL roles covered |
|---|---|---|---|
| **16** | — | Seaport / Terminal Operator | TransportationNetworkManager (sea), TransportRegulator, AuthorityParty |
| **17** | — | Airport / Air Terminal | TransportationNetworkManager (air), AuthorityParty |
| **18** | — | Rail Hub / Intermodal Terminal | TransportationNetworkManager (rail/intermodal), AuthorityParty |

#### Compliance & Publication

| # | Alias | Role | UBL roles covered |
|---|---|---|---|
| **19** | — | Customs Authority | CustomsParty, Exporting/Importing Customs Party |
| **20** | — | Chamber of Commerce | IssuerParty, ImportingGuarantor, ExportingGuarantor, CertificationParty |
| **21** | — | Government Information Service | PublicationBody, RegistrationAuthority, PublisherSystem |

#### Financial

| # | Alias | Role | UBL roles covered |
|---|---|---|---|
| **22** | — | Buyer's Bank | PayerFinancialAccount holder, routes buyer's payments |
| **23** | — | Seller's Bank | PayeeParty, receives payments on behalf of sellers |
| **24** | — | Factor | Invoice discounting / factoring counterparty |
| **25** | — | Guarantor | GuaranteeCertificate issuer for tender deposits and trade guarantees |

#### Retail & End Consumer

| # | Alias | Role | UBL roles covered |
|---|---|---|---|
| **26** | — | Retailer | RetailerParty, CPFR Buyer Party |
| **(C)** | — | Consumer (private individual) | Receives `PurchaseReceipt` from Retailer (26); otherwise outside UBL's core B2B scope |

> Note: Parties 8/W1 and 9/W2 are 3PL operators — they appear as party roles in
> logistics documents but do not initiate commercial processes independently.
> Party (C) is outside UBL's B2B scope entirely.
> Fictional company names to be assigned in a separate session.

---

## 6. Document exchanges per party pair

This section records which UBL documents flow between each party pair. It is derived from
`analysis/ubl-party-interactions.md` — consult that file for the full sub-process flows and
sequence details.

> **Note:** The party identifiers below (P01–P11, W1, W2) reflect the old 13-party
> consolidation. They need to be re-mapped to the agreed 26+C numbering in section 5.3:
> P01→1, P02→5, P03→2, P04→26, P05→10, P06→11, P07→16, P08→19, P09→20, P10→21,
> P11→23/25, W1→8, W2→9. New parties (3,4,6,7,12–15,17,18,22,24) need their own flow
> sections added.

### 6.1 P01 (Buyer) ↔ P02 (Seller)

**Process group B — Order-to-Cash** (core commercial flow)

| Document | Sender → Receiver | Trigger / Purpose |
|---|---|---|
| `RequestForQuotation` | P01 → P02 | Buyer requests a price quote |
| `Quotation` | P02 → P01 | Seller responds with price and terms |
| `Order` | P01 → P02 | Buyer places a purchase order |
| `OrderResponseSimple` | P02 → P01 | Seller accepts/rejects immediately |
| `OrderResponse` | P02 → P01 | Seller responds with line-level detail |
| `OrderChange` | P01 → P02 | Buyer amends the order |
| `OrderCancellation` | P01 → P02 | Buyer cancels the order |
| `Invoice` | P02 → P01 | Seller bills for delivered goods |
| `CreditNote` | P02 → P01 | Seller corrects/reduces a prior invoice |
| `DebitNote` | P02 → P01 | Seller increases a prior invoice |
| `SelfBilledInvoice` | P01 → P02 | Buyer self-bills (reverse billing) |
| `SelfBilledCreditNote` | P01 → P02 | Buyer corrects a self-billed invoice |
| `Reminder` | P02 → P01 | Seller reminds of overdue payment |
| `Statement` | P02 → P01 | Seller provides account balance summary |
| `ApplicationResponse` | P01 → P02 | Acknowledgement of any received document |

**Process group F — Catalogue Management**

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `CatalogueRequest` | P01 → P02 | Buyer requests a catalogue |
| `Catalogue` | P02 → P01 | Seller publishes product catalogue |
| `CataloguePricingUpdate` | P02 → P01 | Seller updates prices only |
| `CatalogueItemSpecificationUpdate` | P02 → P01 | Seller updates item specs |
| `CatalogueDeletion` | P02 → P01 | Seller withdraws catalogue |
| `ApplicationResponse` | P01 → P02 | Buyer confirms catalogue receipt |

### 6.2 P01 (Buyer) ↔ P11 (Financial Institution)

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `RemittanceAdvice` | P01 → P11 | Buyer instructs payment allocation |
| `Invoice` *(copy)* | P11 → P01 | Bank forwards factored invoice |

### 6.3 P02 (Seller) ↔ W1 (Seller's Warehouse)

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `DespatchAdvice` *(pick trigger)* | P02 → W1 | Seller triggers pick-pack-ship |
| `InventoryReport` | W1 → P02 | Warehouse reports stock-on-hand |
| `StockAvailabilityReport` | W1 → P02 | Warehouse confirms availability |

### 6.4 W1 (Seller's Warehouse) ↔ P05 (Freight Forwarder)

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `ForwardingInstructions` | P02/W1 → P05 | Seller instructs forwarder to collect |
| `DespatchAdvice` | W1 → P05 | Handover notification at collection |

### 6.5 P05 (Forwarder) ↔ P06 (Carrier)

**Process group D — Transport Operations**

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `TransportServiceDescriptionRequest` | P05 → P06 | Forwarder asks for service capabilities |
| `TransportServiceDescription` | P06 → P05 | Carrier describes available services |
| `TransportExecutionPlanRequest` | P05 → P06 | Forwarder requests a transport plan |
| `TransportExecutionPlan` | P06 → P05 | Carrier proposes plan |
| `TransportExecutionPlanRequest` *(counter)* | P06 → P05 | Carrier counter-proposes |
| `TransportExecutionPlan` *(confirmed)* | P05 → P06 | Forwarder confirms plan |
| `GoodsItemItinerary` | P06 → P05 | Carrier provides routing detail |
| `TransportationStatusRequest` | P05 → P06 | Forwarder requests status update |
| `TransportationStatus` | P06 → P05 | Carrier reports current status |
| `FreightInvoice` | P06 → P05 | Carrier invoices for transport services |

### 6.6 P06 (Carrier) ↔ W1/W2 (Warehouses)

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `Waybill` | P06 → W1, W2 | Carrier issues road transport document |
| `BillOfLading` | P06 → P05 | Carrier issues sea transport document |
| `PackingList` | W1 → P06 | Warehouse provides packing detail for shipment |
| `DeliveryNote` | P06 → W2 | Carrier confirms delivery |

### 6.7 P06 (Carrier) ↔ P07 (Port Authority)

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `TransportProgressStatusRequest` | P05 → P07 | Forwarder asks network manager for progress |
| `TransportProgressStatus` | P07 → P05 | Network manager reports position |
| `CommonTransportationReport` | P06 → P07 | Carrier reports to transport authority |

### 6.8 W1/W2 (Warehouses) ↔ P01/P02 (Buyer/Seller)

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `ReceiptAdvice` | W2 → P01 | Buyer's warehouse confirms receipt (triggers invoice matching) |
| `InventoryReport` | W2 → P01 | Buyer's warehouse reports stock levels |
| `InstructionForReturns` | P01 → W2/P02 | Buyer initiates a return |

### 6.9 P02 (Seller/Exporter) ↔ P08 (Customs)

**Process group E — Customs & Trade Compliance**

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `ExportCustomsDeclaration` | P02 → P08 | Declarant notifies export |
| `ImportCustomsDeclaration` | P02/P01 → P08 | Declarant notifies import |
| `TransitCustomsDeclaration` | P05 → P08 | Forwarder notifies transit |
| `GoodsItemPassport` *(approval req.)* | P09 → P08 | Chamber requests Customs approval of carnet |
| `GoodsItemPassport` *(approved)* | P08 → P09 | Customs approves passport |
| `ProofOfReexportationRequest` | P08 → P09 | Customs requests proof from Chamber |
| `ProofOfReexportation` | P09 → P08 | Chamber provides proof |
| `ProofOfReexportationReminder` | P08 → P09 | Customs reminds Chamber |

### 6.10 P02 (Seller) ↔ P09 (Chamber of Commerce)

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `CertificateOfOrigin` | P09 → P02 | Chamber certifies goods origin |
| `GoodsCertificate` | P09 → P02 | Chamber certifies goods quality/compliance |
| `GoodsItemPassport` *(holder copy)* | P09 → P02 | Chamber issues ATA carnet to holder |

### 6.11 P03 (Contracting Authority) ↔ P02 (Seller/Economic Operator)

**Process group G — Procure-to-Award** (public procurement)

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `PriorInformationNotice` | P03 → P10 | CA announces upcoming procurement |
| `ContractNotice` | P03 → P10 | CA publishes tender invitation |
| `CallForTenders` | P03 → P02 | CA sends tender documents |
| `QualificationApplicationRequest` | P03 → P02 | CA requests qualification evidence |
| `QualificationApplicationResponse` | P02 → P03 | EO submits qualification |
| `ExpressionOfInterestRequest` | P03 → P02 | CA requests expressions of interest |
| `ExpressionOfInterestResponse` | P02 → P03 | EO expresses interest |
| `TenderStatusRequest` | P02 → P03 | EO requests status of own tender |
| `TenderStatus` | P03 → P02 | CA reports tender status |
| `Tender` | P02 → P03 | EO submits tender |
| `TenderReceipt` | P03 → P02 | CA acknowledges tender receipt |
| `AwardedNotification` | P03 → P02 | CA notifies winning EO |
| `UnawardedNotification` | P03 → P02 | CA notifies unsuccessful EOs |
| `TenderWithdrawal` | P02 → P03 | EO withdraws tender |
| `ContractAwardNotice` | P03 → P10 | CA publishes award decision |
| `TenderContract` | P03 ↔ P02 | Contract signed between CA and winner |
| `WorkReport` | P02 → P03 | Contractor reports works progress |
| `GuaranteeCertificate` | P11 → P03 | Bank provides tender deposit guarantee |
| `ProcurementStatusRequest` | P03 → P02 | CA requests status from EO |
| `ProcurementStatus` | P02 → P03 | EO reports status |
| `UnsubscribeFromProcedureRequest` | P02 → P03 | EO withdraws from procedure |
| `UnsubscribeFromProcedureResponse` | P03 → P02 | CA confirms withdrawal |

### 6.12 P04 (Retailer) ↔ P02 (Seller) — CPFR

**Process group H — Retail & Supply Chain Planning**

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `ExceptionCriteria` | P04 → P02 | Retailer defines deviation thresholds |
| `ExceptionNotification` | P02 → P04 | Seller alerts to threshold breach |
| `Forecast` | P04 → P02 | Retailer shares demand forecast |
| `ForecastRevision` | P04 → P02 | Retailer updates forecast |
| `RetailEvent` | P04 → P02 | Retailer notifies of promo/event |
| `ProductActivity` | P04 → P02 | Retailer shares POS sales data |
| `ItemInformationRequest` | P04 → P02 | Retailer requests item master data |
| `TradeItemLocationProfile` | P02 → P04 | Seller provides item/location attributes |
| `StockAvailabilityReport` | P02 → P04 | Seller confirms stock availability |

### 6.13 P01 (Buyer/Utility Customer) ↔ P02 (Utility Provider)

**Process group I — Utility Billing**

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `UtilityStatement` | P02 → P01 | Utility provider issues consumption statement |
| `Invoice` | P02 → P01 | Utility invoice referencing statement |
| `InvoiceStatusRequest` | P01 → P02 | Buyer queries invoice status |
| `InvoiceStatusResponse` | P02 → P01 | Seller responds to status query |
| `PurchaseReceipt` | P01 → P02 | Buyer acknowledges purchase |

### 6.14 P01 ↔ P02 — Digital Interoperability

**Process group J — Digital Interoperability**

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `DigitalCapability` | P01 ↔ P02 | Each party publishes supported doc types |
| `DigitalAgreement` | P01 ↔ P02 | Parties agree on digital exchange terms |

### 6.15 P02 / P03 → P10 (Government Information Service)

**Process group K — Party & Business Profile**

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `BusinessCard` | P02 → P10 | Company publishes basic profile |
| `BusinessInformation` | P02 → P10 | Company registers structured profile |

### 6.16 P03 (Contracting Authority) → Waste parties

**Process group L — Sustainability**

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `WasteNotification` | P03 → authorities | Waste sender notifies of waste movement |
| `WasteMovement` | P03 → P08 | Waste movement manifest |

### 6.17 Administrative / cross-party

**Process group M — Administrative**

| Document | Sender → Receiver | Purpose |
|---|---|---|
| `Enquiry` | any → any | One party enquires about a topic |
| `EnquiryResponse` | any → any | Response to enquiry |
| `DocumentStatus` | any → any | Party reports status of a referenced document |
| `DocumentStatusRequest` | any → any | Party requests status of a document |
| `AttachedDocument` | any → any | Wraps any document as an attachment |
| `ApplicationResponse` | any → any | Generic acknowledgement / acceptance / rejection |

---

## 7. Documents not yet mapped to a flow

The following document types exist in UBL 2.5 but were not explicitly traced to one of the
above party pairs in this session. They may be variants, sub-flows, or context-specific:

| Document | Notes |
|---|---|
| `Manifest` | Carrier-level cargo manifest; related to `PackingList` |
| `WeightStatement` | Port/carrier weighing certification |
| `InstructionForReturns` | Buyer → Seller; triggers return logistics via W2 |
| `ReceiptAdvice` | Already covered — issued by W2 on behalf of P01 |
| `FulfilmentCancellation` | Buyer cancels a despatch in progress |
| `Waybill` | Already covered under D-group |
| `CommonTransportationReport` | Already covered under D-group |

---

## 8. Files created in this session

| File | Purpose |
|---|---|
| `analysis/ubl-domain-groups.md` | Bottom-up: 15 domain groups, all 310 ABIE types, all 101 docs |
| `analysis/ubl-process-groups.md` | Top-down: 13 process groups (A–M), all 310 ABIE types, all 101 docs |
| `analysis/ubl-party-interactions.md` | ~40 sub-process flows, party vocabulary, cross-process scenarios |
| `analysis/ubl-element-reference.md` | CBC element index + links to domain files |
| `analysis/cac-01-party-organization.md` through `cac-12-digital-services.md` | Per-domain deep dives into ABIE types with CBC details |
| `analysis/session-decisions.md` | This file — session record, decisions, rationale, party-document matrix |

---

## 9. Open questions / next steps

1. **Assign fictional identifiers** to all 26+C parties (GLN, VAT numbers, addresses,
   bank accounts) so all example files reference the same master data.
2. **Re-map section 6** — update all party IDs from the old P01–P11/W1–W2 scheme to
   the agreed 1–26+C numbering, and add exchange flow sections for new parties
   (3, 4, 6, 7, 12–15, 17, 18, 22, 24).
3. **Pick a priority scenario** to implement first — the core Order-to-Cash loop
   (Party 1 → Party 5, groups B + C + D) covers the highest-value document types.
4. **Validate samples** against the UBL 2.5 XSDs in `schemas/ubl-2.5/csd02/xsdrt/`.
