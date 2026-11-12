# LLM review: 07-FulfilmentCancellation.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: context

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
- XPath: `08-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueTime` = `10:48:00`
- Why: The cancellation is issued on 14 May at 17:53 and says the new despatch advice follows. The replacement, 08-DespatchAdvice.xml (LD-DA-26-0329, same goods, consignment and shipment), was issued on 14 May at 10:48. The statement contradicts the flow, and between 10:48 and 17:53 two valid despatch advices existed for the same goods.
- Condition: the note and the order of the documents agree: the cancellation precedes the replacement, or the note says the replacement has been sent (and names it).
- Options: (preferred) the cancellation before the replacement (its time, or the replacement's, moved), with a reference to the replacement once it exists; or reword the note to "replaced by LD-DA-26-0329".
- Needs decision: no

### air/07#F2 · High · "Next day's flight", but the cargo is reported arrived the same day
- XPath: `/FulfilmentCancellation/cbc:CancellationNote` = `The cargo missed its flight; it goes on the next day's flight under a new despatch advice.`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cbc:Description` = `Cargo arrived and ready for customs clearance.`
- Why: CancellationNote is "The reason for cancellation of the referenced document". The flight booked was on 14 May 07:00 (04-Waybill.xml); "the next day's flight" is 15 May. Five minutes after this cancellation, on 14 May at 17:58, the destination handler reports the cargo arrived at Selanu on 14 May. The reason given contradicts the arrival report.
- Condition: the reason for cancellation and the arrival report agree on when the cargo flies and arrives.
- Options: (preferred) settle the story once (missed the morning flight, flown on a later flight the same day, arrived 14 May) and word the note accordingly; or move the arrival report to 15 May.
- Needs decision: yes (when the cargo flew)

### air/07#F3 · Medium · Cancelling a despatch advice that nothing in the missed flight changes
- XPath: `/FulfilmentCancellation/cac:DespatchDocumentReference/cbc:ID` = `LD-DA-26-0327`
- XPath: `/FulfilmentCancellation/cac:AdditionalDocumentReference/cbc:ID` = `KXL-OFFLOAD-26-0513`
- Why: A Fulfilment Cancellation is "A document used to cancel an entire fulfilment document". The reason here is that the cargo was offloaded from its flight. The despatch advice LD-DA-26-0327 (06-DespatchAdvice.xml) says nothing about the flight: no despatch or delivery date, no transport stage; it states only what was despatched, by which carrier, for which consignment and shipment, and all of that stays true. Its replacement 08-DespatchAdvice.xml is identical apart from issue time and manufacture dates. The goods were despatched once; a missed flight is a transport event (reported by the carrier or the terminal), not a reason to cancel the despatch. The document is used for a situation it does not fit.
- Condition: either the cancelled advice contains information the missed flight makes wrong (and the replacement corrects it), or the flow reports the missed flight without cancelling the despatch advice.
- Options: (preferred) replace the cancellation and second despatch advice by a transportation status from Kelaro or Lumeport (offloaded, rebooked), as the delay is a carriage matter; or give 06 and 08 the flight-dependent data (planned delivery) that justifies cancelling and replacing.
- Needs decision: yes (changes the documents of the flow)

### air/07#F4 · Medium · CustomerReference of the order reference holds a project name, not a purchasing-card tag
- XPath: `/FulfilmentCancellation/cac:OrderReference/cbc:CustomerReference` = `Harbour parks Selanu`
- Why: In OrderReference, CustomerReference is defined as "Text used for tagging purchasing card transactions". No purchasing card is used in the flow (the only payment, in 10-Invoice.xml, is by credit transfer and concerns freight); the value is the buyer's project. The value is valid as a reference at document level of an order (where the definition is broader) but not in this element.
- Condition: OrderReference/CustomerReference is present only with a purchasing-card tag; otherwise absent.
- Options: (preferred) drop it from the order reference (the project is already the buyer's CustomerReference in 01-OrderChange.xml); or, if the project matters to the cancellation, put it in a note.
- Needs decision: no

### air/07#F5 · Medium · LocaleCode holds a language code
- XPath: `/FulfilmentCancellation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) is a language and repeats Language/ID. 362 such elements over `world/examples/*/*.xml` (grep).
- Condition: LocaleCode holds a locale, or is absent.
- Options: (preferred) drop it; or a real locale code with a locale list.
- Needs decision: no

### air/07#F6 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/FulfilmentCancellation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address"; a gate is not a street and does not belong in a postal address.
- Condition: no gate in a street-name element of the postal address.
- Options: (preferred) drop it.
- Needs decision: no

### air/07#F7 · Low · The offload reference says nothing about what it is
- XPath: `/FulfilmentCancellation/cac:AdditionalDocumentReference/cbc:ID` = `KXL-OFFLOAD-26-0513`
- Why: The reference has only an ID; no DocumentTypeCode or DocumentDescription says that it is the carrier's offload notice, and no example has this ID. A receiver of the cancellation cannot use the reference without knowing what it points to.
- Condition: the reference states what document it is (type or description) and who issued it.
- Options: (preferred) add a DocumentDescription (Kelaro's offload notice) and the issue date; or drop it if the cancellation note suffices.
- Needs decision: no

### air/07#F8 · Low · Originator and beneficiary in a cancellation of a despatch advice
- XPath: `/FulfilmentCancellation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/FulfilmentCancellation/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: The document cancels Lumeway's despatch advice to Velumi's warehouse. The Port of Selanu, originator and beneficiary of the order, receives nothing and does nothing under this cancellation, and the cancelled despatch advice itself does not name it. The parties look copied from the order.
- Condition: the cancellation names only parties it concerns, or states why the port needs to know.
- Options: (preferred) drop both; or keep them if the port is to be told that its frames are delayed (then also as a note).
- Needs decision: no

### air/07#F9 · Low · Signature aggregate without a signature
- XPath: `/FulfilmentCancellation/cac:Signature/cbc:ID` = `LD-SIG-26-FC`
- Why: Signature is "A signature applied to this document"; the aggregate holds only an ID and the signatory, with no method, attachment or extension. 131 of 133 Signature aggregates over `world/examples/*/*.xml` are like this (lxml count).
- Condition: either a verifiable signature or no Signature aggregate.
- Options: (preferred) drop it.
- Needs decision: yes (a convention across many examples)

## Checked and consistent
- DespatchDocumentReference LD-DA-26-0327 resolves to 06-DespatchAdvice.xml, of the right kind; the parties (buyer, seller, delivery and despatch party) agree with it.
- OrderReference VT-OC-26-0320 resolves to 01-OrderChange.xml: SalesOrderID, UUID, issue date and time agree, and OrderTypeCode `230` ("Purchase order change request") fits; its DocumentReference VT-PO-26-0127 resolves to sea/05-Order.xml. (That 06-DespatchAdvice.xml names another order is a finding of that review.)
- Contract LD-DAG-26-0125 resolves to sea/03-DigitalAgreement.xml.
