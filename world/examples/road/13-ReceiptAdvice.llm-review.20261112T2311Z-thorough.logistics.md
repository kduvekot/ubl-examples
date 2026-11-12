# LLM review: 13-ReceiptAdvice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/13-ReceiptAdvice.xml`, Git blob `604fd2f166bf65e6e949e78ef14e8423b7c4b8ad` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### road/13#F1 · High · Emission factor × base does not give the emission value
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: ValueFactorNumeric is "a numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and ValueBaseMeasure "the base quantity to which the value factor applies". A factor of 0.82 per 1 EA (one bench) gives 0.82 kg CO2e per bench, not the 96 kg stated. No other reading fits: 96 / 0.82 = 117.1, which is neither a count in the flow, nor the bench's materials (34 kg steel + 22.5 kg hardwood = 56.5 kg in the CircularityProfile), nor the bench weight implied by the transport documents (about 38 kg net). The same three values are in 39 examples (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<'`, all with ValueMeasure 96 KGM), 9 of them in this flow.
- Condition: ValueFactorNumeric × (activity quantity / ValueBaseMeasure) equals ValueMeasure, with the activity and the factor's unit evident from the values; or factor and base are absent.
- Options: (a) preferred: relate the factor to the activity it really measures (e.g. per kg of steel, base in KGM), so the value can be recalculated; (b) drop ValueFactorNumeric and ValueBaseMeasure and keep the total.
- Needs decision: no

### road/13#F2 · Medium · The carrier's consignment note referenced as a delivery note
- XPath: `/ReceiptAdvice/cac:Shipment/cac:Delivery/cac:DeliveryNoteDocumentReference/cbc:ID` = `TH-WB-26-0159`
- Why: DeliveryNoteDocumentReference is "a reference to a Delivery Note associated with this Delivery". TH-WB-26-0159 is the carrier's CMR waybill (`08-Waybill.xml:/Waybill/cbc:ID` = `TH-WB-26-0159`, WaybillTypeCode CMR), a transport contract document, not the supplier's delivery note. The supplier's document that accompanies the goods is the despatch advice, already referenced as `/ReceiptAdvice/cac:DespatchDocumentReference/cbc:ID` = `CL-DA-26-0153`. A reference element of one document kind is used for another.
- Condition: DeliveryNoteDocumentReference, if present, refers to a delivery note; the waybill, if it is to be referenced, is referenced through an element (or document type) that says it is a transport document.
- Options: (a) preferred: move the waybill reference to an additional document reference with the document type Waybill (the signed CMR is the consignee's proof of receipt for the carrier); (b) remove it.
- Needs decision: no

### road/13#F3 · Low · Revised receipt advice does not refer to the advice it revises
- XPath: `/ReceiptAdvice/cbc:DocumentStatusCode` = `Revised`
- XPath: `/ReceiptAdvice/cbc:ID` = `LD-RA-26-0164`
- Why: The document says it is a revision, but it has a new ID and no reference to the receipt advice it corrects (`11-ReceiptAdvice.xml`, LD-RA-26-0162) or to the cancellation that announced it (`12-FulfilmentCancellation.xml`, LD-DOC-26-0163, note "A corrected receipt advice follows."). The despatch party cannot tell from this document which earlier figures it replaces.
- Condition: the revised receipt advice carries a reference to LD-RA-26-0162 (and may refer to the cancellation).
- Options: (a) preferred: an additional document reference to LD-RA-26-0162 with its document type; (b) keep the ID LD-RA-26-0162 with a higher version, if the world treats a revision as a new version of the same document (the cancellation would then be unnecessary, which changes the flow).
- Needs decision: no

### road/13#F4 · Low · Received side frames not identified as the substituted 2026 casting
- XPath: `/ReceiptAdvice/cac:ReceiptLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `VI-C180`
- Why: The order response replaced the ordered side frame by the 2026 casting (`02-OrderResponse.xml:/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `2026`) and also proposed the 2025 casting from stock. The receipt line records only VI-C180, so the receipt does not show which casting arrived, and the application response's "matched to the substituted 2026 casting" (`16-ApplicationResponse.xml`) has nothing in the goods documents to match against. The same gap is in the despatch advice (`04-DespatchAdvice.xml`).
- Condition: the receipt line identifies the casting version received in the same way the order response identifies the substitute.
- Options: (a) preferred: ExtendedID 2026 on the item (as in the order response); (b) drop the version distinction everywhere if it has no role.
- Needs decision: no

## Checked and consistent
- Received 96 benches and 13 side frames: OversupplyQuantity 1 = 13 − 12 ordered; no shortage, in line with the cancellation of the earlier advice (`12-FulfilmentCancellation.xml`: "the shortage did not exist").
- Actual delivery 2026-03-25 09:40 equals `11-ReceiptAdvice.xml` and `14-Invoice.xml`; issue time 2026-03-26 10:48 follows the cancellation at 10:46.
- References to the order, despatch advice and despatch lines resolve.

## Considered and refuted
- `/ReceiptAdvice/cac:ReceiptLine[2]/cbc:ReceivedQuantity`: 96 benches and 13 boxes are 109 packages, one more than the 108 the carrier took over without reservation (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:TotalPackagesQuantity` = `108`) — refuted because the story is a box picked twice at the 3PL; the despatch advice and waybill record what was believed to be loaded, and reporting the difference found on receipt is the purpose of this document.
