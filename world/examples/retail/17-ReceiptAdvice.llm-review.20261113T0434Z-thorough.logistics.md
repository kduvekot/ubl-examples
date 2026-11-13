# LLM review: 17-ReceiptAdvice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/17-ReceiptAdvice.xml`, Git blob `47b28c9a1fccb7811613ffb860e40b9269d5dddc` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 49b7b4a 2026-11-13 Reviews of the cotton and retail flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### retail/17#F1 · High · Receipt line `1` exists twice, with different quantities
- XPath: `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cac:ReceivedHandlingUnitReceiptLine/cbc:ID` = `1`
- XPath: `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cac:ReceivedHandlingUnitReceiptLine/cbc:ReceivedQuantity` = `3`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:ID` = `1`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedQuantity` = `23`
- Why: ReceivedHandlingUnitReceiptLine is "A receipt line associated with this transport handling unit"; its ID identifies the receipt line. Inside pallet 3 the receipt line `1` has 3 received and 1 rejected; the document's receipt line `1` has 23 received and 1 rejected. The invoice 18 and credit note 19 reference "receipt line 1 of BS-RA-26-0235" (`19-CreditNote.xml:/CreditNote/cac:CreditNoteLine/cac:ReceiptLineReference/cbc:LineID` = `1`), which can be either. The same pattern as despatch line `1` in 12 (12/F1).
- Condition: each receipt line ID identifies one line with one set of quantities; the pallet-level line either is the document's line (with a distinct ID or clearly the same line) or has an ID of its own.
- Options: (a, preferred) give the pallet-level line its own ID (e.g. `1-3`, pallet 3 of line 1) referring to despatch line 1; (b) drop the pallet-level receipt line and keep the damage on the handling unit (DamageRemarks, Status, attachment), which already say what happened.
- Needs decision: no

### retail/17#F2 · High · Emission value is not factor × base
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: 0.82 × 1 EA = 0.82, not 96 kg (ValueFactorNumeric: "A numeric factor used to calculate the value measurement"). Same as 02/F1; 39 examples carry these values (`grep -rl --include='*.xml' '<cbc:ValueFactorNumeric>0.82<' world/examples | wc -l`).
- Condition: ValueMeasure = ValueFactorNumeric × ValueBaseMeasure, or factor and base are absent.
- Options: (a, preferred) drop factor and base; (b) factor 96 per 1 EA.
- Needs decision: no

### retail/17#F3 · Medium · Received on 30 April, while the forwarder expected arrival on 29 April at 14:00
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedDate` = `2026-04-30`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedTime` = `10:40:00`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cac:UpdatedDeliveryTransportEvent/cbc:OccurrenceDate` = `2026-04-29`
- XPath: `15-TransportationStatus.xml:/TransportationStatus/cac:UpdatedDeliveryTransportEvent/cbc:OccurrenceTime` = `14:00:00`
- Why: The truck was "on its way" on 2026-04-29 at 11:49 for a 38 km trip (16) and expected at 14:00 that day; this receipt records arrival the next morning. No document explains the overnight delay, and the timing complaint speaks only of 40 minutes into a slot. See 15/F2 and 12/F5.
- Condition: receipt time, the forwarder's status and the despatch advice describe one consistent delivery.
- Options: (a, preferred) keep 2026-04-30 10:40 and move the "on its way" status in 15 to that morning; (b) receipt on 2026-04-29 afternoon.
- Needs decision: yes (which day the benches were delivered)

### retail/17#F4 · Medium · Damaged "carton", while the despatch advice describes no cartons
- XPath: `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cbc:DamageRemarks` = `One carton torn, the bench's armrest bent.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:Note` = `One bench arrived in a damaged carton and was refused.`
- XPath: `12-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[3]/cac:ActualPackage/cbc:PackagingTypeCode` = `PX`
- XPath: `12-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[3]/cbc:TotalPackageQuantity` = `4`
- Why: For the same pallet (SSCC `095206102170000038`), the despatch advice lists one package, a pallet (`PX`), and no carton; this receipt reports a torn carton. The four packages counted in 12 are presumably the cartons, but 12 never says so; the two documents describe the packaging of the same handling unit differently. See 12/F2.
- Condition: the packaging the receipt advice reports as damaged is the packaging the despatch advice declares for that pallet.
- Options: (a, preferred) declare the four cartons in 12 (see 12/F2) and keep the carton here; (b) if the benches travel unpacked, report the damage without a carton here and in 19.
- Needs decision: no

### retail/17#F5 · Low · Two different references for the damage photos, with numbers that suggest other dates
- XPath: `/ReceiptAdvice/cac:AdditionalDocumentReference/cbc:ID` = `BM-GI-PHOTO-26-0510`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:DocumentReference/cbc:ID` = `BS-PHOTO-26-0118`
- XPath: `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cac:DamageDocumentationAttachment/cac:ExternalReference/cbc:URI` = `https://www.brightmarket.example/goods-in/26-0510/pallet-3.jpg`
- Why: The damage of one bench is documented by an attachment on the pallet, a document `BM-GI-PHOTO-26-0510` at document level and a document `BS-PHOTO-26-0118` at line level, with two different prefixes (BM-, BS-) of the same party and numbers that read like 10 May and 18 January, although the goods were received on 2026-04-30. Neither reference says what it is, and neither exists elsewhere (searched over `*.xml`). It is unclear whether there are one, two or three photo sets.
- Condition: the damage documentation is referenced consistently (one identifier per photo set, of the party's own numbering, that fits the receipt), and each reference says what it is.
- Options: (a, preferred) one photo-set ID (e.g. `BS-PHOTO-26-0430-03`) used at document and line level with DocumentType "Damage photos", and the attachment's URI built from it; (b) drop the line-level reference.
- Needs decision: no

### retail/17#F6 · Low · Late against a delivery slot that no document agreed
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:TimingComplaintCode` = `LATE`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:TimingComplaint` = `Arrived 40 minutes into the slot; unloading delayed the next truck.`
- Why: Neither the order 08, nor the transport request 11, nor the despatch advice 12 states a delivery slot or time; 11 only gives a service period to 2026-05-02. The complaint refers to an agreement the flow does not show, and "40 minutes into the slot" is late only if the slot was shorter than the unloading time.
- Condition: the delivery slot the complaint refers to is stated in a document the delivery was based on (order, transport request or despatch advice), or the complaint does not rely on it.
- Options: (a, preferred) a requested delivery time window in 08 (see 08/F2) or in 11, e.g. 2026-04-30 10:00–10:30; (b) reword the complaint.
- Needs decision: no

## Checked and consistent
- Quantities: document line 23 received + 1 rejected = 24 = despatched (12) = ordered (08); pallet 3: 3 + 1 = 4 = its despatch line in 12. The rejected 1 is what the credit note 19 credits.
- SSCC `095206102170000038` is pallet 3 of 6 in 12 ("003 of 006"), the photo is named pallet-3.
- Shipment `LD-SH-26-0230`, OrderReference `BS-PO-26-0224`, DespatchDocumentReference `LD-DA-26-0229` resolve; issue time 15:21 is after the receipt at 10:40.
- Codes: DeliveryAcceptanceCode `PARTIAL`, RejectReasonCode `DAMAGED`, RejectActionCode `CREDIT` and QuantityDiscrepancyCode `DAMAGED` agree with the notes and with 19's DiscrepancyResponse "Transport damage".
- Buyer's item ID `BM-551210` is the item ID the store uses in the purchase receipt 21.

## Considered and refuted
- `/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedQuantity` = `23`: suspected that ReceivedQuantity should include the rejected bench (24) — refuted because UBL defines ReceivedQuantity only as "The quantity received" and RejectedQuantity separately; reading 23 accepted + 1 rejected is consistent with the pallet line (3 + 1) and with the credit note.
