# LLM review: 07-FulfilmentCancellation.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/07-FulfilmentCancellation.xml`, Git blob `d10c8ccd74a876708b4debda27481eed12f840a9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b6aed1 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
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

### air/07#F1 · High · "A new despatch advice follows today", but it was issued seven hours earlier
- XPath: `/FulfilmentCancellation/cbc:Note` = `A new despatch advice follows today.`
- XPath: `/FulfilmentCancellation/cbc:IssueDate` = `2026-05-14`
- XPath: `/FulfilmentCancellation/cbc:IssueTime` = `17:53:00`
- XPath: `08-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueDate` = `2026-05-14`
- XPath: `08-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueTime` = `10:48:00`
- Why: The cancellation, issued on 14 May at 17:53, announces the replacement despatch advice as still to come. The replacement `LD-DA-26-0329` (`08-DespatchAdvice.xml`, same goods, shipment and consignment) was issued on 14 May at 10:48, before the cancellation of the document it replaces, so between 10:48 and 17:53 two valid despatch advices existed for the same eight castings. The merge tried to refute it: both documents are issued by Lumeway in the same time zone (no time zone offset differs), and "follows" cannot be read as "has followed".
- Condition: the note agrees with the order of issue: the replacement is issued after the cancellation, or the note refers to the replacement as already sent (by its ID).
- Options: (a) preferred: cancel first, then reissue (move the replacement after the cancellation, or the cancellation before 10:48), with the timing settled together with F2; (b) keep the times and change the note into a reference to `LD-DA-26-0329`.
- Needs decision: no
- From: broad (F1), logistics (F2), context (F1)

### air/07#F2 · High · "Goes on the next day's flight", but the cargo is reported arrived the same day
- XPath: `/FulfilmentCancellation/cbc:CancellationNote` = `The cargo missed its flight; it goes on the next day's flight under a new despatch advice.`
- XPath: `/FulfilmentCancellation/cbc:IssueDate` = `2026-05-14`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportMeans/cbc:JourneyID` = `KXL207`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cbc:Description` = `Cargo arrived and ready for customs clearance.`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cbc:IssueTime` = `17:58:00`
- Why: CancellationNote is "The reason for cancellation of the referenced document". The only flight in the flow is KXL207, departing 2026-05-14 07:00 (`04-Waybill.xml`). If the cargo missed it, "the next day's flight" is on 15 May; yet `09-TransportationStatus.xml`, issued five minutes after this cancellation, reports the same consignment `LD-CS-26-0324` arrived at Selanu on 14 May. The merge checked the other reading (logistics): if an earlier flight on 13 May was missed (`03-ForwardingInstructions.xml` has an untyped event at 13 May 19:00, and the reference `KXL-OFFLOAD-26-0513` suggests 13 May), then "the next day's flight" is KXL207 of the 14th, which had already flown and landed when this was issued at 17:53 ("it goes" is future), and the waybill issued on 13 May at 10:43 already booked it. No reading makes the cancellation, the waybill and the arrival report agree.
- Condition: the missed flight, the replacement flight, the waybill's flight and the arrival date in `09-TransportationStatus.xml` tell one consistent story, and the cancellation is issued no later than it can be useful.
- Options: (a) preferred: an evening flight on 13 May was missed, the waybill books KXL207 on the 14th, and this cancellation and the replacement advice are issued on the 13th or early on the 14th (then 04, 08 and 09 stand, and F1 is resolved at the same time); (b) KXL207 on the 14th was missed: the arrival in 09 moves to the 15th and the waybill shows the new flight. Either changes the flow's story.
- Needs decision: yes (when the cargo flew)
- From: broad (F2), logistics (F1), context (F2)

### air/07#F3 · High · Its order reference contradicts the despatch advice it cancels
- XPath: `/FulfilmentCancellation/cac:OrderReference/cbc:ID` = `VT-OC-26-0320`
- XPath: `/FulfilmentCancellation/cac:OrderReference/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- XPath: `06-DespatchAdvice.xml:/DespatchAdvice/cac:OrderReference/cbc:ID` = `VT-PO-26-0319`
- Why: OrderReference here is "A reference to an Order document associated with the referenced Despatch or Receipt Advice(s)". The cancelled despatch advice `LD-DA-26-0327` names order `VT-PO-26-0319`, which no example has (re-checked in the merge), while this document names the order change `VT-OC-26-0320` of order `VT-PO-26-0127`. The values here are the ones that resolve (`01-OrderChange.xml`: UUID, issue date and time and SalesOrderID agree; `sea/05-Order.xml`), so the fix lies in `06-DespatchAdvice.xml` (and `08-DespatchAdvice.xml`); until then the two documents contradict each other.
- Condition: the order reference of this cancellation and that of `06-DespatchAdvice.xml` name the same order.
- Options: correct 06 and 08 (preferred); this document can stay as it is.
- Needs decision: no
- From: broad (F3), logistics (F3)

### air/07#F4 · Medium · CustomerReference of the order reference holds a project name, not a purchasing-card tag
- XPath: `/FulfilmentCancellation/cac:OrderReference/cbc:CustomerReference` = `Harbour parks Selanu`
- Why: In OrderReference, CustomerReference is defined as "Text used for tagging purchasing card transactions" (definition checked in the merge with `annotate.py`). No purchasing card is used in the flow (the only payment, in `10-Invoice.xml`, is a credit transfer for freight); the value is the buyer's project. It would fit a document-level customer reference of an order, where the definition is broader, but not this element.
- Condition: OrderReference/CustomerReference is present only with a purchasing-card tag; otherwise absent.
- Options: (a) preferred: drop it from the order reference (the project is already the buyer's reference in `01-OrderChange.xml`); (b) if the project matters to the cancellation, put it in a note.
- Needs decision: no
- From: context (F4)

### air/07#F5 · Medium · LocaleCode holds a language code
- XPath: `/FulfilmentCancellation/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value is the ISO 639 language code `en` (listID `ISO 639`), the same value the sibling `cbc:ID` already carries. The skill's severity guide names "a language code in `LocaleCode`" as a Medium case. 362 occurrences in 213 examples (`grep -rho`/`grep -rl --include='*.xml' '<cbc:LocaleCode'`, re-counted in the merge).
- Condition: every `cbc:LocaleCode` in this example holds a locale code from a locale list (with a matching listID), or the element is absent.
- Options: (a) preferred: drop `LocaleCode`; (b) a real locale (e.g. `en-XB` from a locale list), if the world has a reason to state it.
- Needs decision: no
- From: broad (F4), parties (F1), context (F5)

### air/07#F6 · Medium · A gate in AdditionalStreetName of the seller's postal address
- XPath: `/FulfilmentCancellation/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: UBL defines `Address/cbc:AdditionalStreetName` as "An additional street name used to further clarify the address". `Gate 3` is the entrance of Lumeway Distribution's site, not a street, and has no place in its postal address. 79 occurrences in 76 examples (`grep --include='*.xml'`, re-counted in the merge).
- Condition: Lumeway Distribution's `PostalAddress` has no `AdditionalStreetName` holding a gate.
- Options: (a) preferred: remove it from the postal address; (b) carry it only in a pickup or despatch location of documents that need it.
- Needs decision: no
- From: parties (F2), context (F6)

### air/07#F7 · Low · The cancelled despatch advice contains nothing that the missed flight made wrong
- XPath: `/FulfilmentCancellation/cac:DespatchDocumentReference/cbc:ID` = `LD-DA-26-0327`
- XPath: `06-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cbc:ID` = `LD-SH-26-0323`
- XPath: `06-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- Why: A Fulfilment Cancellation is "A document used to cancel an entire fulfilment document". The reason given is a missed flight. `06-DespatchAdvice.xml` names no flight, no despatch date and no delivery date (its review, F6); it states what was despatched, by which carrier, for which consignment and shipment, and all of that stays true. The replacement `08-DespatchAdvice.xml` is identical apart from ID, UUID, issue time and the manufacture dates (`diff`, re-run in the merge), and that difference is itself a contradiction (its review). So the cancellation has no visible reason in the data. The context part rated this Medium (the document is used for a transport event it does not fit); the merge keeps it Low with the broad and logistics parts: cancelling and reissuing a despatch advice when the expected delivery changes is a legitimate use of the document, and what is missing is the data that the delay changes, a plausibility and completeness question (section 6, Low), not a use of the document against its definition.
- Condition: either the cancelled despatch advice carries the data the missed flight changes (its flight, despatch or expected delivery), and the replacement corrects it, or the flow reports the delay without cancelling the despatch advice.
- Options: (a) preferred: despatch advices that state the flight or the expected delivery (see 06's and 08's reviews), so the reissue has a purpose; (b) report the missed flight by a transportation status from Kelaro or the terminal, keep 06 and remove 07 and 08 (changes the flow).
- Needs decision: yes (the documents of the flow)
- From: broad (F5, Low), logistics (F5, Low), context (F3, Medium)

### air/07#F8 · Low · The offload reference has only an ID, and "offloaded" is not "missed its flight"
- XPath: `/FulfilmentCancellation/cac:AdditionalDocumentReference/cbc:ID` = `KXL-OFFLOAD-26-0513`
- XPath: `05-TransportationStatus.xml:/TransportationStatus/cbc:Description` = `Cargo accepted and built up for the flight.`
- Why: The reference is presumably Kelaro's offload notice, the evidence for the reason, but it has no DocumentTypeCode or DocumentDescription, no example has this ID (`grep -rn --include='*.xml' KXL-OFFLOAD`, re-run in the merge: this reference only), and a receiver cannot use it without knowing what it points to. An offload by the airline is not the same as cargo that "missed its flight", while `05-TransportationStatus.xml` reports the cargo accepted and built up for the flight in time. Its number (0513) also points to 13 May, which bears on F2.
- Condition: the reference says what the document is (type or description), who issued it and when, and the cancellation note and that document tell the same story (offloaded by the carrier, or late at the terminal).
- Options: (a) preferred: add DocumentDescription "Offload notice, flight …" (or a type code) with its issue date, and word the note as an offload; (b) drop the reference if the note suffices.
- Needs decision: no
- From: broad (F6), logistics (F4), context (F7)

### air/07#F9 · Low · Signature aggregate without a signature
- XPath: `/FulfilmentCancellation/cac:Signature/cbc:ID` = `LD-SIG-26-FC`
- Why: Signature is "A signature applied to this document"; the aggregate holds only an ID and the signatory, with no method, attachment or extension, so nothing is signed. Of 147 Signature aggregates over `world/examples/*/*.xml`, 137 hold only ID and SignatoryParty (lxml count in the merge; the context part's count 131 of 133 corrected).
- Condition: either a verifiable signature (method, attachment or validation data) or no Signature aggregate.
- Options: (a) preferred: drop it; (b) give it the elements of a real signature.
- Needs decision: yes (a convention across many examples)
- From: context (F9)

### air/07#F10 · Low · English renderings of island addresses tagged en-XB here, en-XL elsewhere
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/FulfilmentCancellation/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/FulfilmentCancellation/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/FulfilmentCancellation/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `01-OrderChange.xml:/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XL`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XL`
- Why: The English renderings of the addresses of Velumi Trading (`Reef Street`, `Port Wrenfield`) and Nalevi Warehousing (`Lagoon Road`, `Port Wrenfield`) carry `en-XB` here, `en-XL` for the same text of the same parties in other examples of the flow. 35 examples tag `Port Wrenfield` `en-XB`, 27 `en-XL` (`grep -rl --include='*.xml'`, re-counted in the merge). The tag seems to follow the issuer's country; that rule is written down nowhere, and the island's own English names argue for `en-XL`. In the merged review of `06-DespatchAdvice.xml` the broad part's opposite view (the tag follows the issuer, so it is consistent) is recorded; the merge cannot settle which rule the world follows. Related: the island parties' `CompanyLegalForm` appears here in English only, without `languageID`.
- Condition: the same rendering of the same address carries the same `languageID` in every example of the flow, chosen by a stated rule.
- Options: (a) preferred: `en-XL` for the English renderings of island addresses everywhere; (b) keep the writer's variety, and record that rule where the world's language conventions are written down.
- Needs decision: yes (which convention the world follows)
- From: parties (F3)

### air/07#F11 · Low · The island parties' legal form in one untagged rendering
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/FulfilmentCancellation/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: The legal form of Velumi Trading and Nalevi Warehousing appears here once, in English, without `languageID`, while the island-issued examples give it in Lisavan and English, each tagged (`09-TransportationStatus.xml`, `01-OrderChange.xml`), and the addresses of the same parties are rendered in both languages in this document. The parties part mentioned this as related to its language-tag finding (F10); the merge makes it a separate Low finding, aligned with the merges of air 01–05, wood and plastics, because the same party's master data is described differently whichever tag rule is chosen.
- Condition: the legal form is rendered the same way as the party's address (both languages, tagged) in every example of the flow, or one documented rule explains the difference.
- Options: render it like the address, with `qal` and English tagged (preferred); or a documented rule.
- Needs decision: no
- From: parties (as a remark in F3)

### air/07#F12 · Low · The same registration date 1996-01-01 for many unrelated companies
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/FulfilmentCancellation/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `PartyLegalEntity/cbc:RegistrationDate` as "The registration date of the CompanyID." The date 1996-01-01 is given for Velumi Trading and Nalevi Warehousing here, and for 25 different companies in three registers over all examples (181 examples, `grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`, re-counted in the merge), while other companies of the same registers have individual dates. Unless the world has an event that registered them all that day, it reads as a default value ("no fillers").
- Condition: each company's `RegistrationDate` is its own date, consistent with its history, or it is absent; if a common date is meant, the world's story states why.
- Options: (a) a date per company that fits its history; (b) drop `RegistrationDate` where no date is known; (c) record 1996-01-01 as an event in the story.
- Needs decision: yes (company histories)
- From: parties (F4)

### air/07#F13 · Low · Contact name, job title and department disagree, and do not fit the role
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/FulfilmentCancellation/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/FulfilmentCancellation/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/FulfilmentCancellation/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/FulfilmentCancellation/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: `Contact/cbc:JobTitle` is "The job title or function of this contact" and `cbc:Department` "The department where this contact works". Velumi Trading's `Purchasing` contact and Nalevi Warehousing's `Goods inwards` contact are both customer service officers in Sales: name, title and department of one contact disagree, and they do not show which function fits the party's role. The same combinations recur throughout the flow (52 `Purchasing` contacts with these values over all `*.xml`, count from the parties part).
- Condition: in each contact, `Name`, `JobTitle` and `Department` describe the same function, and that function fits the party's role.
- Options: (a) preferred: matching job titles and departments (Purchasing: buyer / Purchasing; Goods inwards: warehouse supervisor / Warehouse); (b) drop `JobTitle` and `Department` where they add nothing.
- Needs decision: no
- From: broad (F8), parties (F5)

### air/07#F14 · Low · Originator and beneficiary of the order copied into the cancellation of a despatch advice
- XPath: `/FulfilmentCancellation/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/FulfilmentCancellation/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `01-OrderChange.xml:/OrderChange/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Port of Selanu`
- Why: The cancellation concerns the despatch between Lumeway Distribution and Nalevi Warehousing / Velumi Trading. The Port of Selanu, originator and beneficiary of the order, receives nothing and does nothing under this cancellation, and neither the cancelled despatch advice nor its replacement names it (checked in the merge: no OriginatorCustomerParty or BeneficiaryParty in 06 or 08). The parties look copied from the order.
- Condition: the cancellation carries only parties it concerns, or states why the port needs to know (e.g. a note that its frames are delayed).
- Options: (a) preferred: drop both, matching the cancelled despatch advice; (b) keep them if the story wants the port told of the delay, and say so in a note.
- Needs decision: no
- From: broad (F7), parties (F6), context (F8)

## Checked and consistent
- `LD-DA-26-0327` resolves to `06-DespatchAdvice.xml` (issued 2026-05-13 10:07, before this cancellation), of the right kind, with the same despatch supplier, delivery customer, buyer and seller (all parts).
- The order reference carries the UUID `8d871217-f7db-5dad-9bd8-24d8c75c812d`, issue date 2026-05-11 07:50 and SalesOrderID `LD-SO-26-0123` of `01-OrderChange.xml`; OrderTypeCode 230 ("Purchase order change request") fits an order change; its DocumentReference `VT-PO-26-0127` is the original order (`sea/05-Order.xml`) (broad, logistics, context).
- `LD-DAG-26-0125` resolves to `sea/03-DigitalAgreement.xml`, the agreement between Lumeway and Velumi under which these documents are exchanged (broad, logistics, context).
- Lumeway Distribution is described identically wherever it appears in full; Port of Selanu `IC41037` is the same party as in the order change; telephone numbers use the unassigned code +999 and domains `.example` (parties).

## Considered and refuted
- `/FulfilmentCancellation/cac:Contract/cbc:ID` = `LD-DAG-26-0125`: a digital (EDI) agreement given as the contract — refuted because the definition includes "framework agreements with which the referenced fulfilment document is associated", and the exchange agreement governs these documents (from broad).
- `/FulfilmentCancellation/cac:OrderReference/cbc:ID` = `VT-OC-26-0320`: an order change in OrderReference — refuted because the OrderTypeCode 230 says what it is and the DocumentReference names the order itself (from broad).
- `/FulfilmentCancellation/cac:Signature/cac:SignatoryParty`: signed by the seller rather than the buyer — refuted: the despatch supplier cancels its own despatch advice (from parties).
- `/FulfilmentCancellation/cac:DespatchSupplierParty` with identifier and name only while the seller is given in full — refuted: same party, the full description is in `SellerSupplierParty` (from parties).

## Changed in the merge
- context/F3 (Medium) → F7, Low: kept at the severity of broad/F5 and logistics/F5; reason in the finding (a legitimate use of the document; what is missing is data, a plausibility question).
- broad/F6, logistics/F4, context/F7 → F8: combined (ID only, offload versus missed flight, date in the number).
- context/F9 → F9: count corrected to 137 of 147 Signature aggregates (lxml count in the merge).
- broad/F4 options: "drop LocaleCode" is now preferred, as in parties, context and the other flows.
- broad/F8 and parties/F5 → F13: combined, Department values added.
- parties/F3 (remark on the untagged legal form) → F11: a finding of its own, aligned with the merges of air 01–05, wood and plastics.
- broad/F1, logistics/F2, context/F1 → F1: combined; option (a) tied to F2's timing.
- broad/F2, logistics/F1, context/F2 → F2: combined; logistics' second reading kept, needs decision yes as in all three parts.
