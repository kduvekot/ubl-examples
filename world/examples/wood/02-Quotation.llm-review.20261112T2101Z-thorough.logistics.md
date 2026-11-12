# LLM review: 02-Quotation.xml

Flow: wood (WOOD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/wood/02-Quotation.xml`, Git blob `b8dd536e88f83270060fe92537f76080cae01be9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### wood/02#F1 · Low · Line refers to an unnamed seller document while its note points to the buyer's drawing
- XPath: `/Quotation/cac:QuotationLine/cac:DocumentReference/cbc:ID` = `MS-SPEC-SL1800`
- XPath: `/Quotation/cac:QuotationLine/cbc:Note` = `As drawn; ash or oak.`
- XPath: `/Quotation/cac:AdditionalDocumentReference/cbc:ID` = `MS-GTC-2026`
- Why: QuotationLine/DocumentReference is "A reference to a document associated with this quotation line". The only document of the line is given by ID alone, without `DocumentTypeCode` or `DocumentType`, and it is not the drawing the request asked to be quoted against (`01-RequestForQuotation.xml:/RequestForQuotation/cac:RequestForQuotationLine/cac:DocumentReference/cbc:ID` = `VI-DS-SL1800`), while the line note says the slats are quoted "as drawn". The reader cannot tell whether `MS-SPEC-SL1800` is the seller's own specification that replaces the drawing or a restatement of it, and the buyer's drawing is not referenced at all. The header reference `MS-GTC-2026` likewise says nothing about what it is (presumably general terms and conditions). Neither document exists as an example; they are external documents, so this is about saying what they are, not about a broken reference.
- Condition: each document reference of the quotation states what kind of document it is (type code or type text), and the line makes clear which drawing or specification the quoted slat follows (the buyer's `VI-DS-SL1800`, the seller's `MS-SPEC-SL1800`, or both).
- Options: (a) preferred: add a document type to both references and add a line reference to `VI-DS-SL1800`, keeping `MS-SPEC-SL1800` as the seller's specification derived from it; (b) replace `MS-SPEC-SL1800` by `VI-DS-SL1800` if the seller has no specification of its own.
- Needs decision: no

## Checked and consistent
- Reference `/Quotation/cac:RequestForQuotationDocumentReference/cbc:ID` = `VI-DOC-26-0625` resolves to `01-RequestForQuotation.xml` (a request for quotation, issued 2026-02-16, before this quotation of `/Quotation/cbc:IssueDate` = `2026-02-19`); `/Quotation/cac:QuotationLine/cac:RequestLineReference/cbc:LineID` = `1` matches its only line.
- Validity `/Quotation/cac:ValidityPeriod/cbc:EndDate` = `2026-03-21` is 30 days after the issue date, as `/Quotation/cbc:Note` = `Valid for 30 days.` and the 30 days the request asked for. The order `03-Order.xml` (2026-02-22) falls inside it.
- Promised window `/Quotation/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate` = `2026-03-02` to `/Quotation/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:EndDate` = `2026-03-16` repeats the requested window and is still in the future at issue. (The transport request contradicts it: see the review of `04-TransportExecutionPlanRequest.xml`, this run.)
- `/Quotation/cac:TransactionConditions/cbc:Description` = `Quoted per thousand slats; minimum one truck.`: the logistics part ("minimum one truck") agrees with the full-truck-load service of `04-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`. Physics: 4800 slats × 0.006498 m³ = 31.19 m³ and about 21.6 t (the gross weight of the transport documents), within one articulated truck (own knowledge: about 24 t payload, about 90 m³ in a curtainsider, 13.6 m deck for 1.8 m long bundles).
- Substitute and alternative lines (`1-S`, 35 mm thick; `1-A`, oak) keep quantity `4800`, consistent with the main line.
- Codes: all resolved in their lists; `DAP` (Incoterms) and destination `XU` agree with the request.

## Considered and refuted
- `/Quotation/cac:QuotationLine/cac:SellerProposedSubstituteLineItem/cac:Item/cbc:Name` = `Hardwood bench slat 1800 × 95 × 35`: suspected conflict with the thickness tolerance 37.5–38.5 mm of the main item — refuted because a proposed substitute is by definition a different item, which need not meet the main item's tolerance.
