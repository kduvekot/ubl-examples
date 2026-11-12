# LLM review: 07-FulfilmentCancellation.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/07-FulfilmentCancellation.xml`, Git blob `d10c8ccd74a876708b4debda27481eed12f840a9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### air/07#F1 · High · The cancellation reason contradicts the waybill and the arrival report
- XPath: `/FulfilmentCancellation/cbc:CancellationNote` = `The cargo missed its flight; it goes on the next day's flight under a new despatch advice.`
- XPath: `/FulfilmentCancellation/cbc:IssueDate` = `2026-05-14`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cbc:Description` = `Cargo arrived and ready for customs clearance.`
- Why: CancellationNote is "The reason for cancellation of the referenced document". The only flight
  in the flow is KXL207 on 2026-05-14 at 07:00 (air/04). If the cargo missed it, the next day's
  flight is on 2026-05-15; yet air/09, issued five minutes after this cancellation, reports the cargo
  arrived at Selanu on 2026-05-14. If instead an earlier flight was missed (air/03 has an untyped
  event at 2026-05-13 19:00, and the reference KXL-OFFLOAD-26-0513 suggests an offload on 13 May),
  then the "next day's flight" is the one of the 14th, which had already flown when this was issued at
  17:53, and the waybill issued on the 13th at 10:43 already named it. No reading makes the three
  documents agree.
- Condition: the missed flight, the replacement flight, the waybill's flight and the arrival date in
  air/09 tell one consistent story, and the cancellation is issued no later than it can be useful.
- Options: (a) preferred: an evening flight on 2026-05-13 was missed, the waybill books KXL207 on the
  14th, and this cancellation and the replacement advice are issued on the 13th or early on the 14th;
  (b) KXL207 on the 14th was missed: arrival in air/09 on the 15th and the waybill shows the new flight.
- Needs decision: yes

### air/07#F2 · High · "A new despatch advice follows today", but it was issued seven hours earlier
- XPath: `/FulfilmentCancellation/cbc:Note` = `A new despatch advice follows today.`
- XPath: `/FulfilmentCancellation/cbc:IssueTime` = `17:53:00`
- XPath: `08-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueDate` = `2026-05-14`
- XPath: `08-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueTime` = `10:48:00`
- Why: The replacement despatch advice LD-DA-26-0329 (air/08) is issued on 2026-05-14 at 10:48; this
  cancellation is issued the same day at 17:53 and says the new one follows.
- Condition: the note agrees with the order of issue: the replacement is issued after the
  cancellation, or the note refers to it as already sent (by its ID).
- Options: move the replacement after 17:53 (preferred, see air/08#F4); or say "replaced by
  despatch advice LD-DA-26-0329" and keep the times.
- Needs decision: no

### air/07#F3 · High · The order given for the cancelled despatch advice differs from that advice's own order reference
- XPath: `/FulfilmentCancellation/cac:OrderReference/cbc:ID` = `VT-OC-26-0320`
- XPath: `/FulfilmentCancellation/cac:OrderReference/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- XPath: `06-DespatchAdvice.xml:/DespatchAdvice/cac:OrderReference/cbc:ID` = `VT-PO-26-0319`
- Why: OrderReference here is "A reference to an Order document associated with the referenced
  Despatch or Receipt Advice(s)". The cancelled advice LD-DA-26-0327 (air/06) refers to order
  VT-PO-26-0319, which does not exist (air/06#F1); this cancellation gives the order change
  VT-OC-26-0320 and the order VT-PO-26-0127. The values here are the ones that resolve (air/01, with
  matching UUID, issue date and time), so the fix lies in air/06; the two documents contradict each
  other until then.
- Condition: the order reference of the cancelled despatch advice and the one stated here are the same.
- Options: correct air/06 (and air/08) to VT-PO-26-0127/VT-OC-26-0320 (preferred).
- Needs decision: no

### air/07#F4 · Low · A reference with only an ID, to a document of unknown kind
- XPath: `/FulfilmentCancellation/cac:AdditionalDocumentReference/cbc:ID` = `KXL-OFFLOAD-26-0513`
- Why: The reference is presumably the carrier's offload notice, the evidence for the reason, but it
  has no DocumentTypeCode or DocumentDescription and the document is not in the flow. Its number
  (0513) also points to 13 May, which bears on air/07#F1.
- Condition: the reference says what the document is (type or description) and its date agrees with
  the missed flight.
- Options: add DocumentDescription "Offload notice, flight …" with its issue date (preferred).
- Needs decision: no

### air/07#F5 · Low · The cancelled advice contained nothing that the missed flight made wrong
- XPath: `/FulfilmentCancellation/cac:DespatchDocumentReference/cbc:ID` = `LD-DA-26-0327`
- XPath: `06-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- Why: A Fulfilment Cancellation is "used to cancel an entire fulfilment document". The cancelled
  advice air/06 states no flight, no despatch date and no delivery date; the replacement air/08 has the
  same shipment, consignment, carrier, quantity and weight (only the manufacture dates differ, which is
  itself an error, air/08#F3). A missed flight changes nothing the advice says, so the cancellation
  has no visible reason in the data.
- Condition: either the despatch advices carry the data the missed flight changes (despatch/delivery
  dates, flight), so the replacement differs from the original in it, or the flow does not cancel and
  replace the advice.
- Options: add the delivery dates to both advices (preferred, see air/06#F4); or drop the cancellation
  and the replacement, which changes the story.
- Needs decision: yes

## Checked and consistent
- `DespatchDocumentReference/ID` LD-DA-26-0327 resolves to air/06-DespatchAdvice.xml (issued
  2026-05-13 10:07, before this cancellation).
- The order reference's UUID 8d871217-f7db-5dad-9bd8-24d8c75c812d, IssueDate 2026-05-11 and IssueTime
  07:50 are those of air/01-OrderChange.xml; OrderTypeCode 230 (purchase order change request) fits an
  order change; SalesOrderID LD-SO-26-0123 is the seller's order number of sea/06-OrderResponse.xml.
- `Contract/ID` LD-DAG-26-0125 resolves to sea/03-DigitalAgreement.xml.
- Delivery customer, despatch supplier, buyer and seller agree with air/06.
