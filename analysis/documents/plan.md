# Plan: Document-Level Semantic Analysis for 101 UBL 2.5 Documents

## Context

We have a validated set of 26+C canonical parties (in `analysis/session-decisions.md`) and deep knowledge of UBL 2.5's 101 document types, their party elements, document reference chains, and process group flows (in `analysis/ubl-party-interactions.md` and `analysis/ubl-process-groups.md`). The goal is to create a per-document analysis that maps every party-bearing element to one of the 26+C parties, considering the full document structure (nested elements, line items, delivery/payment/shipment sub-structures) and cross-document information flow (how party details echo between chained documents).

## What Gets Created

```
analysis/documents/
├── README.md                           (index — already created)
├── plan.md                             (this file)
├── Order.md                            (one file per document type)
├── OrderResponse.md
├── Invoice.md
├── ...                                 (101 files total)
```

## Markdown Format Per Document

Each file follows this structure:

```markdown
# {DocumentName}

**Process Group**: {X} — {GroupName}
**Schema**: `maindoc/UBL-{DocumentName}-2.5.xsd`

## Description
2-3 sentences: what this document is, who sends it to whom, and what business
action it represents.

## Document Chain Position
- **Predecessors**: Which documents feed party info INTO this one
  (e.g., "Order provides BuyerCustomerParty + SellerSupplierParty")
- **Successors**: Which documents consume party info FROM this one
- **Key References**: OrderReference, DespatchDocumentReference, etc.
- **Line References**: How line numbers chain back to predecessors

## Party Element Mapping

### Primary Scenario: {scenario description}

#### Document Level

| Element | Card. | Party # | Party Name | Rationale |
|---|---|---|---|---|
| BuyerCustomerParty | 1..1 | 1 | Commercial Buyer | Initiates the order... |
| SellerSupplierParty | 1..1 | 5 | Manufacturer | Fulfils the order... |

#### Delivery / Shipment Level
(elements within Delivery, Consignment, Shipment sub-structures)

| Element Path | Card. | Party # | Party Name | Rationale |
|---|---|---|---|---|
| Delivery > DeliveryParty | 0..1 | 9 | Buyer's Warehouse | Physical receive location... |
| Delivery > CarrierParty | 0..1 | 13 | Road Carrier | Last-mile delivery... |

#### Payment / Financial Level
(elements within PaymentMeans, financial account structures)

| Element Path | Card. | Party # | Party Name | Rationale |
|---|---|---|---|---|
| PaymentMeans > PayerFinancialAccount | 0..1 | 22 | Buyer's Bank | Payer's account... |

#### Line Level
(party elements within line items, Item sub-structures)
Only if the document has line-level party elements.

### Variant: {alternative scenario}
(different party assignments — e.g., Distributor instead of Manufacturer,
Retailer as buyer, factoring scenario, self-billing, freight, etc.)

## Information Flow
- Which party elements does the SENDER populate from their own data?
- Which party elements does the SENDER echo from a predecessor document?
- Example: In OrderResponse, the Seller authors SellerSupplierParty but
  echoes back BuyerCustomerParty from the received Order.

## Notes
- Conditional elements, mutual exclusivity, cardinality constraints
- Cross-document consistency requirements
```

## Processing Approach

### Smarter Party Element Extraction (not 124K paths)

The deep recursive extraction produced millions of paths due to recursive types. Instead, I'll extract party elements at **meaningful structural levels only**:

1. **Document root** — top-level cac: elements that are party-bearing
2. **Delivery/Despatch** — party elements within DeliveryType, DespatchType
3. **Consignment/Shipment** — party elements within ConsignmentType, ShipmentType
4. **PaymentMeans** — financial account structures (party-like)
5. **Line items** — party elements within InvoiceLine > Item, OrderLine > LineItem
6. **Transport** — TransportHandlingUnit, TransportEvent party elements

I'll write a focused extraction script that caps depth at these meaningful levels and produces a clean JSON per document (not 124K entries, more like 15-30 meaningful party paths per document).

### Sequential Subagent Processing

Process documents **in chain order within each group**, so each subagent can reference the predecessor document's analysis:

**Group B — Order-to-Cash** (19 docs, chain order):
1. RequestForQuotation → 2. Quotation → 3. Order → 4. OrderChange →
5. OrderCancellation → 6. OrderResponse → 7. OrderResponseSimple →
8. Invoice → 9. CreditNote → 10. DebitNote → 11. SelfBilledInvoice →
12. SelfBilledCreditNote → 13. FreightInvoice → 14. RemittanceAdvice →
15. Reminder → 16. Statement → 17. InvoiceStatusRequest →
18. InvoiceStatusResponse → 19. PurchaseReceipt

**Group C — Fulfilment** (13 docs):
1. DespatchAdvice → 2. DeliveryNote → 3. ReceiptAdvice →
4. FulfilmentCancellation → 5. ForwardingInstructions → 6. BillOfLading →
7. Waybill → 8. PackingList → 9. WeightStatement → 10. Manifest →
11. GoodsCertificate → 12. CertificateOfOrigin → 13. InstructionForReturns

**Group D — Transport** (10 docs):
1. TransportServiceDescriptionRequest → 2. TransportServiceDescription →
3. TransportExecutionPlanRequest → 4. TransportExecutionPlan →
5. GoodsItemItinerary → 6. TransportProgressStatusRequest →
7. TransportProgressStatus → 8. TransportationStatusRequest →
9. TransportationStatus → 10. CommonTransportationReport

**Group E — Customs** (7 docs):
1. ExportCustomsDeclaration → 2. ImportCustomsDeclaration →
3. TransitCustomsDeclaration → 4. GoodsItemPassport →
5. ProofOfReexportationRequest → 6. ProofOfReexportation →
7. ProofOfReexportationReminder

**Group F — Catalogue** (6 docs):
1. CatalogueRequest → 2. Catalogue → 3. CataloguePricingUpdate →
4. CatalogueItemSpecificationUpdate → 5. CatalogueDeletion →
6. ItemInformationRequest

**Group G — Procurement** (24 docs):
1. PriorInformationNotice → 2. ContractNotice → 3. ContractAwardNotice →
4. CallForTenders → 5. ExpressionOfInterestRequest →
6. ExpressionOfInterestResponse → 7. QualificationApplicationRequest →
8. QualificationApplicationResponse → 9. Tender → 10. TenderReceipt →
11. TenderWithdrawal → 12. TendererQualification →
13. TendererQualificationResponse → 14. AwardedNotification →
15. UnawardedNotification → 16. TenderContract →
17. TenderStatus → 18. TenderStatusRequest →
19. ProcurementStatus → 20. ProcurementStatusRequest →
21. UnsubscribeFromProcedureRequest → 22. UnsubscribeFromProcedureResponse →
23. GuaranteeCertificate → 24. WorkReport

**Group H — CPFR** (9 docs):
1. ExceptionCriteria → 2. ExceptionNotification → 3. Forecast →
4. ForecastRevision → 5. RetailEvent → 6. ProductActivity →
7. TradeItemLocationProfile → 8. InventoryReport → 9. StockAvailabilityReport

**Groups I-M** (13 docs):
I: UtilityStatement
J: DigitalCapability → DigitalAgreement
K: BusinessCard → BusinessInformation
L: WasteNotification → WasteMovement
M: ApplicationResponse → AttachedDocument → DocumentStatus →
   DocumentStatusRequest → Enquiry → EnquiryResponse

### Subagent Prompt Construction

Each subagent gets a **focused, dedicated prompt** containing:

1. **Document-specific data**: party elements at all structural levels (from enhanced extraction), exact cardinalities, element documentation from XSD
2. **Chain context**: which predecessor documents feed into this one, which successors consume from it, what party info is "echoed"
3. **Group context**: typical flow for this process group (from ubl-party-interactions.md)
4. **The 26+C party table** (compact form from /tmp/party_reference.md)
5. **Scenario guidance**: primary scenario + which variants make sense for this specific document
6. **File path to write**: /home/user/ubl-examples/analysis/documents/{DocName}.md

The subagent reads the actual XSD to verify element structure, then writes the markdown file.

### Multiple Scenarios Per Document

Documents that appear in multiple contexts get multiple scenario mappings:

| Document | Primary Scenario | Variants |
|---|---|---|
| Order | Buyer(1) → Manufacturer(5) | Retailer(26) → Distributor(6); ContrAuth(2) via procurement |
| Invoice | Manufacturer(5) → Buyer(1) | With factoring (Factor=24 as PayeeParty); Self-billing flip |
| DespatchAdvice | SellerWH(8) → BuyerWH(9) | Direct from Manufacturer(5); Returns (reverse) |
| BillOfLading | OceanCarrier(11) issues | AirCarrier(12) issues Waybill variant |
| GoodsItemPassport | ChamComm(20) issues | 4-stage lifecycle (export→import→return) |
| Waybill | RoadCarrier(13) issues | Per transport mode |

## Verification

After all 101 files are generated:
1. Check every file exists: `ls analysis/documents/*.md | wc -l` should be 102 (101 + README)
2. Grep for unmapped elements: ensure no party element is left without a party # assignment
3. Cross-check consistency: same party should have same # across all documents (e.g., BuyerCustomerParty = #1 everywhere it means Commercial Buyer)
4. Verify document chains: OrderResponse references Order's party assignments; ReceiptAdvice references DespatchAdvice's assignments

## Steps

1. Write enhanced extraction script (meaningful levels only, not recursive explosion)
2. Generate per-document JSON data files
3. Process Group B (19 docs) sequentially via subagents
4. Process Group C (13 docs)
5. Process Group D (10 docs)
6. Process Group E (7 docs)
7. Process Group F (6 docs)
8. Process Group G (24 docs)
9. Process Group H (9 docs)
10. Process Groups I-M (13 docs)
11. Update README.md index with final links
12. Verify completeness and consistency
13. Commit and push
