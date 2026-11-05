# UBL 2.5 element coverage: initial analysis

How many UBL 2.5 elements appear in at least one sample document in `xml/`,
which are missing, and where each missing element fits best: in one of the
current examples, or in a new example document.

Generated tables with every missing element:
[`element-coverage-details.md`](element-coverage-details.md). Produced by
`tools/coverage.py` (see [Reproduce](#reproduce)).

## Method

- **Element = child in its context.** Each BBIE and ASBIE of the UBL 2.5 model
  (`mod/UBL-Entities-2.5.gc` of `os-UBL-2.5`) counts as one element:
  `Address/StreetName` and `Party/PostalAddress` are separate elements, and so
  are `Invoice/Note` and `Order/Note`. That gives **5,443 elements**: 2,570 at
  document level (101 document types) and 2,873 in the 310 library aggregates.
- **Counted:** the `cac`/`cbc` elements in the 75 sample documents.
  `UBL-Invoice-2.0-Detached-Signature.xml` is an XML signature, not a UBL
  document. Not counted: attributes (`schemeID`, `currencyID`, …), code-list
  values, and extension content (signatures).
- **Placement** (automatic, then reviewed below). Each aggregate has *home*
  documents: the document types that reach it in the fewest steps.
  - **extend:** a home-document example already contains the parent, so add the
    element there.
  - **add structure:** a home-document example exists, so add the parent (and
    the path to it) there.
  - **new example:** no home document has an example.

  If several examples qualify, the script picks the one that needs the fewest
  new elements, already uses the parent most fully, and is the newest version.
- **Validity baseline:** all 75 examples are valid against the UBL 2.5 OS
  schemas (`xsdrt/maindoc`, checked with `xmllint`). Every element they use
  exists in the 2.5 model.

## Results

| | Elements | Used | Missing | Coverage |
|---|---:|---:|---:|---:|
| Document level | 2,570 | 730 | 1,840 | 28% |
| Library (in context) | 2,873 | 730 | 2,143 | 25% |
| **All** | **5,443** | **1,460** | **3,983** | **27%** |

- **Aggregates (cac types) used at least once:** 136 of 310.
- **Document types with an example:** 55 of 101.
- **Elements new in UBL 2.5:** 386 of 387 are not used anywhere (2.4: 103 of
  146 missing).

Where the 3,983 missing elements fit:

| Placement | Elements | Meaning |
|---|---:|---|
| extend | 1,755 | Add to an existing example; the parent is already there |
| add structure | 701 | Add to an existing example, with the parent structure |
| new example | 1,521 | Needs an example of a document type that has none |
| not reachable | 6 | `PerformanceDataLine`: left over in the library since PerformanceHistory was dropped (2.1 PRD3); no document uses it |

So **about 60% of the gap can be closed in documents we already have**. The
remaining 40% needs new example documents.

## New example documents needed

46 document types have no example. Grouped by process, with the number of
missing elements that only fit there:

| Priority | Process | Document types (elements) |
|---|---|---|
| 1 | Catalogue | Catalogue (65), CatalogueRequest (52), CatalogueItemSpecificationUpdate (30), CataloguePricingUpdate (30), CatalogueDeletion (22) |
| 1 | Billing | SelfBilledInvoice (62), FreightInvoice (48), InvoiceStatusRequest (13, new in 2.5), InvoiceStatusResponse (15, new in 2.5) |
| 1 | Fulfilment and trade | DeliveryNote (25, new in 2.5), BillOfLading (26), PackingList (20), CertificateOfOrigin (35) |
| 1 | Generic | ApplicationResponse (23), AttachedDocument (19), DocumentStatus (15), DocumentStatusRequest (15) |
| 2 | eTendering | QualificationApplicationRequest (80), Tender (68), QualificationApplicationResponse (53), AwardedNotification (38), GuaranteeCertificate (33), ContractAwardNotice (31), CallForTenders (28), ContractNotice (28), TenderStatus (28), TenderContract (25), TendererQualificationResponse (24), TendererQualification (21), ExpressionOfInterestResponse (19), UnawardedNotification (19), TenderReceipt (18), TenderWithdrawal (18), TenderStatusRequest (17), Enquiry (17), EnquiryResponse (16), UnsubscribeFromProcedureRequest (16), UnsubscribeFromProcedureResponse (17), ProcurementStatus (27, new in 2.5), ProcurementStatusRequest (17, new in 2.5) |
| 3 | Other domains | UtilityStatement (204, the largest single gap), WorkReport (43, new in 2.5), BusinessInformation (34, new in 2.4), ItemInformationRequest (24), WasteMovement (23, new in 2.5), WasteNotification (20, new in 2.5) |

Priority 1 covers the documents most implementers meet first. Several of them
(ApplicationResponse, Catalogue, DeliveryNote) are central to the document
chains of part 2 (Catalogue → Order → … → Invoice → ApplicationResponse).

## Existing examples to extend

The biggest gaps in documents that already have an example (document-level
coverage):

| Document type | Coverage | Note |
|---|---:|---|
| PriorInformationNotice | 10% | The two examples are minimal |
| Reminder | 18% | |
| DebitNote | 21% | The only 2.5 example, yet 12 new 2.5 elements are missing |
| OrderResponse | 23% | |
| OrderChange | 26% | |
| SelfBilledCreditNote | 28% | |
| GoodsCertificate | 30% | |
| CreditNote | 37% | |
| Invoice | 44% | 9 examples, mostly variants of the same content (signatures, namespaces) |

The detailed list targets 61 example files. The largest are
TransportExecutionPlan-2.1 (119 elements, mostly `Consignment`),
Waybill-2.0 (116, mostly `ShipmentStage`), CreditNote-2.1 (113) and
GoodsItemItinerary-2.1 (90).

## Review of the automatic placement

The script only uses the structure, so some placements are technically
possible but not where the element belongs in meaning. My corrections:

| Elements | Automatic placement | Better fit | Why |
|---|---|---|---|
| Circularity, new in 2.5 (`CircularityProfile`, `EndOfLifeTreatment`, `ResourceConsumption`, `WasteGenerated`, repairability `Score`) | Invoice line item | **Catalogue** (new) | Product master data that the supplier publishes, not billing data |
| Maritime port reporting (`MaritimeHealthDeclaration`, `BallastWaterSummary`, `ISPSRequirements`, `MaritimeWaste`, `DestinationPortCall`, `Storage`) | Waybill-2.0 | **CommonTransportationReport-2.3** | That is the ship-to-port reporting document these were added for (2.3); a waybill is a transport contract |
| Tendering terms and process (`TenderingProcess`, `AwardingTerms`, `AwardingCriterion`, `TendererQualificationRequest`, …) | PriorInformationNotice | **ContractNotice / CallForTenders** (new) | A PIN announces a procurement; the full terms belong in the contract notice and call for tenders |
| `ElectronicAddress`, `SecurityListing` (party, new in 2.5) | Waybill consignor; Invoice payee | **BusinessCard** | Party profile data; BusinessCard is the document that exchanges it |
| `FuelConsumption`, `FuelMetering`, `FuelProperty` (2.4) | Invoice-2.1 delivery | **New Invoice variant** (fuel delivery) | Fits the Invoice, but as its own scenario rather than in the generic example |
| `InsurancePolicy` (shipment, new in 2.5) | Waybill-2.0 | Waybill or **BillOfLading** (new) | Either works; BillOfLading if we add one |
| `PenaltyInterestRate` (new in 2.5) | Invoice payment terms | Invoice, and also **Reminder** | Late-payment interest is what a reminder charges |

General observations:

1. **Don't put everything in one example.** Some aggregates have 50–90
   missing elements. Adding them all to one existing file makes it unreadable.
   Scenario-specific variants (e.g. `Invoice-2.5-Example-Fuel`) are clearer
   and fit the "coherent world" of part 2.
2. **Many targets are old OASIS examples** (Waybill-2.0, Statement-2.0,
   DespatchAdvice-2.0, ReceiptAdvice-2.0, RemittanceAdvice-2.0). They are
   valid against 2.5 but reflect the 2.0 data. Changing them changes files
   that were published by OASIS.
3. **Coverage of 2.5 is the weakest point:** 386 of the 387 elements new in 2.5
   are not in any example yet. That is also where examples help adopters most.

## Open decision

Should coverage be added by **changing the OASIS example files** (the history
of `xml/` then continues after `os-UBL-2.5`), or by **adding new example
files** next to them and leaving the OASIS originals as published? The second
option keeps the reconstructed history clean, and the new files can follow the
part 2 party set from the start.

## Reproduce

The model file is in the release zip
(<https://docs.oasis-open.org/ubl/os-UBL-2.5/UBL-2.5.zip>, `mod/UBL-Entities-2.5.gc`).

```bash
python3 tools/coverage.py --model /path/to/UBL-Entities-2.5.gc --examples xml > analysis/element-coverage-details.md
```
