# LLM review: 07-FulfilmentCancellation.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: broad

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
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### air/07#F1 · High · "A new despatch advice follows today", but it was issued seven hours earlier
- XPath: `/FulfilmentCancellation/cbc:Note` = `A new despatch advice follows today.`
- XPath: `/FulfilmentCancellation/cbc:IssueTime` = `17:53:00`
- XPath: `08-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueDate` = `2026-05-14`
- XPath: `08-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueTime` = `10:48:00`
- Why: The cancellation, issued on 14 May at 17:53, announces the replacement despatch advice as still to come. The replacement `LD-DA-26-0329` (`08-DespatchAdvice.xml`) was issued on 14 May at 10:48, before the cancellation of the document it replaces.
- Condition: the note's tense agrees with the replacement's issue time, and the replacement is not issued before the cancellation, or the cancellation refers to the replacement that already exists.
- Options: (a) issue the cancellation before the replacement (preferred: cancel, then reissue); (b) keep the times and change the note into a reference to `LD-DA-26-0329`.
- Needs decision: no

### air/07#F2 · High · "Goes on the next day's flight", but the cargo arrived the same day
- XPath: `/FulfilmentCancellation/cbc:CancellationNote` = `The cargo missed its flight; it goes on the next day's flight under a new despatch advice.`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cbc:Description` = `Cargo arrived and ready for customs clearance.`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- Why: On 14 May at 17:53 the cancellation says the cargo missed its flight and will fly on the next day's flight, i.e. 15 May. Five minutes later (17:58) Selanu Airport Cargo reports the same consignment arrived at Selanu on 14 May. The only flight in the flow is the 14 May 07:00 flight of the waybill. The documents contradict each other about whether the cargo flew on 14 May.
- Condition: the cancellation's account of the missed flight and the rebooking agrees with the waybill's flight and with the arrival in `09-TransportationStatus.xml`.
- Options: (a) the cargo missed a flight on 13 May and flew on 14 May; issue the cancellation (and the replacement) on 13 May and word the note accordingly (preferred: then 04, 08 and 09 stand); (b) the cargo flies on 15 May; move the arrival in 09 and the waybill's flight. This changes the flow's story.
- Needs decision: yes

### air/07#F3 · High · Its order reference contradicts the despatch advice it cancels
- XPath: `/FulfilmentCancellation/cac:OrderReference/cbc:ID` = `VT-OC-26-0320`
- XPath: `/FulfilmentCancellation/cac:OrderReference/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- XPath: `06-DespatchAdvice.xml:/DespatchAdvice/cac:OrderReference/cbc:ID` = `VT-PO-26-0319`
- Why: OrderReference here is "A reference to an Order document associated with the referenced Despatch or Receipt Advice(s)". The cancelled despatch advice `LD-DA-26-0327` names order `VT-PO-26-0319`, while this document names the order change `VT-OC-26-0320` of order `VT-PO-26-0127`. This document's reference is the one that resolves (`01-OrderChange.xml`, `sea/05-Order.xml`; UUID, date, time and SalesOrderID match 01). The two documents must still agree (see 06#F1).
- Condition: the order reference of this cancellation and that of `06-DespatchAdvice.xml` name the same order.
- Options: fix 06 (preferred); this document can stay as it is.
- Needs decision: no

### air/07#F4 · Medium · LocaleCode holds a language code
- XPath: `/FulfilmentCancellation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". `en` with listID ISO 639 is a language code (213 example files).
- Condition: LocaleCode holds a locale or is absent.
- Options: (a) a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### air/07#F5 · Low · The cancellation reason does not touch anything the cancelled despatch advice says
- XPath: `/FulfilmentCancellation/cac:DespatchDocumentReference/cbc:ID` = `LD-DA-26-0327`
- XPath: `06-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cbc:ID` = `LD-SH-26-0323`
- Why: A fulfilment cancellation cancels "an entire fulfilment document". The reason given is a missed flight. `06-DespatchAdvice.xml` names no flight and no date beyond its issue date, and the replacement `08-DespatchAdvice.xml` repeats it with the same shipment, consignment, line and quantity. Only the manufacture dates change, and that change is itself a contradiction (08#F1). Nothing in the cancelled document became wrong through the missed flight, so the cancellation has no reason inside the documents.
- Condition: the cancelled despatch advice contains the information the reason makes wrong (e.g. its flight or estimated delivery), and the replacement corrects it, or the story uses another way to report the delay (e.g. a transport status) instead of cancelling the despatch advice.
- Options: (a) despatch advices that state the flight or the expected delivery (see 06#F5), so the reissue has a purpose (preferred); (b) report the missed flight by a transportation status and keep 06, removing 07 and 08 (changes the flow).
- Needs decision: yes

### air/07#F6 · Low · "Offload" reference by ID only, and offloaded versus "missed its flight"
- XPath: `/FulfilmentCancellation/cac:AdditionalDocumentReference/cbc:ID` = `KXL-OFFLOAD-26-0513`
- XPath: `05-TransportationStatus.xml:/TransportationStatus/cbc:Description` = `Cargo accepted and built up for the flight.`
- Why: The reference has no DocumentTypeCode or description, and no example has this ID. Its name suggests Kelaro's offload notice. An offload by the airline is not the same as cargo that "missed its flight", and `05-TransportationStatus.xml` reports the cargo accepted and built up for the flight in time.
- Condition: the reference says what it is, and the cancellation note and the referenced notice tell the same story (offloaded by the carrier or late at the terminal).
- Options: add DocumentTypeCode/DocumentDescription ("Carrier's offload notice") and word the note as an offload.
- Needs decision: no

### air/07#F7 · Low · Originator and beneficiary in a cancellation of a despatch advice
- XPath: `/FulfilmentCancellation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/FulfilmentCancellation/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: The cancellation concerns the despatch between Lumeway and Nalevi/Velumi. The Port of Selanu is the end customer of the order, but neither the cancelled despatch advice nor the replacement names it. This document does nothing with it, so it looks copied from the order.
- Condition: the parties are absent, or the document has a reason to inform the port (e.g. it is distributed to it).
- Options: remove them (preferred).
- Needs decision: no

### air/07#F8 · Low · Contacts do not fit their roles
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/FulfilmentCancellation/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/FulfilmentCancellation/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- Why: "Purchasing" and "Goods inwards" contacts are both customer service officers in Sales. Name, title and department disagree (52 and 10 example files).
- Condition: name, title and department agree with each other and with the role.
- Options: align names or titles.
- Needs decision: no

## Checked and consistent
- `LD-DA-26-0327` resolves to `06-DespatchAdvice.xml`, with the same despatch supplier, delivery customer, buyer and seller.
- The order reference carries the UUID `8d871217-f7db-5dad-9bd8-24d8c75c812d`, issue date 2026-05-11 07:50, SalesOrderID `LD-SO-26-0123` and CustomerReference of `01-OrderChange.xml`. OrderTypeCode 230 ("Purchase order change request") fits an order change. Its DocumentReference `VT-PO-26-0127` is the original order (`sea/05-Order.xml`).
- `LD-DAG-26-0125` resolves to `sea/03-DigitalAgreement.xml`, the agreement between Lumeway and Velumi under which these documents are exchanged.

## Considered and refuted
- `/FulfilmentCancellation/cac:Contract/cbc:ID` = `LD-DAG-26-0125`: a digital (EDI) agreement given as the contract. Refuted because the definition includes "framework agreements with which the referenced fulfilment document is associated", and the exchange agreement governs these documents.
- `/FulfilmentCancellation/cac:OrderReference/cbc:ID` = `VT-OC-26-0320`: an order change in OrderReference. Refuted because the OrderTypeCode 230 says what it is and the DocumentReference names the order itself.
