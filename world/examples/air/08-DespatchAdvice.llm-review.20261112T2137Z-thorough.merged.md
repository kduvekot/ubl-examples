# LLM review: 08-DespatchAdvice.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/08-DespatchAdvice.xml`, Git blob `f521e89ceb8199134c10b0a779e9436a0465dcdb` (committed)
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

### air/08#F1 · High · The replacement despatch advice is issued seven hours before the cancellation that announces it
- XPath: `/DespatchAdvice/cbc:IssueDate` = `2026-05-14`
- XPath: `/DespatchAdvice/cbc:IssueTime` = `10:48:00`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:IssueTime` = `17:53:00`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:Note` = `A new despatch advice follows today.`
- Why: The fulfilment cancellation `07-FulfilmentCancellation.xml` (2026-05-14 17:53) cancels `LD-DA-26-0327` and says a new despatch advice follows. This advice, the replacement for the same goods, shipment and consignment, is issued the same day at 10:48, while the first one is still valid: for seven hours two despatch advices for the same eight castings exist, and the cancellation's statement is contradicted. Re-checked in the merge (same issuer, same time zone offset).
- Condition: the replacement despatch advice is issued after the cancellation of the first, or the cancellation says it was already sent.
- Options: (a) preferred: issue this advice after the cancellation, the timing settled together with the missed-flight story (07's review, F2); (b) issue the cancellation before 10:48, or reword its note as a reference to `LD-DA-26-0329`.
- Needs decision: no
- From: logistics (F4), context (F3); broad recorded it under 07 (Outside this review)

### air/08#F2 · High · The referenced order VT-PO-26-0319 does not exist
- XPath: `/DespatchAdvice/cac:OrderReference/cbc:ID` = `VT-PO-26-0319`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:OrderReference/cbc:ID` = `VT-OC-26-0320`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:OrderReference/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: OrderReference is "A reference to an Order with which this Despatch Advice is associated". No example has the ID VT-PO-26-0319 (`grep -rn --include='*.xml' VT-PO-26-0319 world/examples`: only the references in air/03, air/06 and air/08, re-run in the merge). The frames were ordered under `VT-PO-26-0127` (`sea/05-Order.xml`) as changed by `VT-OC-26-0320` (`01-OrderChange.xml`), the order `07-FulfilmentCancellation.xml` names for the despatch this one replaces. VT-PO-26-0319 is not the seller's order number either (`LD-SO-26-0123` in 07).
- Condition: the OrderReference resolves to the order (and order change) the goods were ordered under, and agrees with `07-FulfilmentCancellation.xml`.
- Options: (a) preferred: VT-PO-26-0127 with the order change VT-OC-26-0320 as its DocumentReference (or as in 07); (b) add an order VT-PO-26-0319 to the flow, which changes the story.
- Needs decision: no
- From: broad (F2), logistics (F1), context (F1, first part)

### air/08#F3 · High · The despatch line refers to the bench line of the order
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cbc:Name` = `Bench side frame casting`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `01-OrderChange.xml:/OrderChange/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- Why: OrderLineReference/LineID is "An identifier for the referenced order line, assigned by the buyer". Line 1 of `VT-PO-26-0127` is the 96 park benches, line 2 the 12 side frames by sea; the 8 air-freighted frames were added by the order change, which reuses ID 1 (a finding of the review of `01-OrderChange.xml`). The agreement with the order change's line ID does not refute it: in an order change a line ID names the order line it changes, so line 1 remains the bench line of the order that `07-FulfilmentCancellation.xml` gives.
- Condition: the OrderLineReference names the side-frame line of the air delivery, with the line ID of the (corrected) order change.
- Options: follow the order change's fix (preferred: a new line 3), as in `06-DespatchAdvice.xml`.
- Needs decision: no
- From: broad (F3), logistics (F2), context (F1, second part)

### air/08#F4 · High · The same serial numbers as in the cancelled despatch advice, but manufactured a day later
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-03190`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-11`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[8]/cbc:SerialID` = `VI-SF-03197`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[8]/cbc:ManufactureDate` = `2026-05-11`
- XPath: `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[8]/cbc:ManufactureDate` = `2026-05-10`
- Why: ItemInstance is "A trackable, unique instantiation of this item" and ManufactureDate "The date on which this item instance was manufactured". This replacement ships the same eight item instances as `06-DespatchAdvice.xml` (serials VI-SF-03190 … 03197, the same trace IDs, registration IDs, melt M-26-0412 and time 06:40), but each now has the manufacture date 11 May instead of 10 May (all of ItemInstance[1] to [8]; `diff` re-run in the merge). A cast part has one manufacture date. The merge tried to read the change as a correction: the only reason the flow gives for the replacement is the missed flight (`07-FulfilmentCancellation.xml`), and nothing marks a corrected date, so the two documents contradict each other.
- Condition: every item instance with the same serial number has the same manufacture date and time in both despatch advices.
- Options: (a) preferred: 10 May in both, which also places manufacture before the order change of 11 May 07:50; (b) 11 May in both, which needs a reason (cast at 06:40 on the morning the order change was issued at 07:50).
- Needs decision: no
- From: broad (F1), logistics (F3), context (F2)

### air/08#F5 · Medium · LocaleCode holds a language code
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value is the ISO 639 language code `en` (listID `ISO 639`), repeating the sibling `cbc:ID`. Section 6 names it a Medium case. 362 occurrences in 213 examples (`grep --include='*.xml'`, re-counted in the merge).
- Condition: every `cbc:LocaleCode` in this example holds a locale code from a locale list, or the element is absent.
- Options: (a) preferred: drop `LocaleCode`; (b) a real locale (e.g. `en-XB` from a locale list).
- Needs decision: no
- From: broad (F4), parties (F1), context (F4)

### air/08#F6 · Medium · A gate in AdditionalStreetName of the despatch party's postal address
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: UBL defines `Address/cbc:AdditionalStreetName` as "An additional street name used to further clarify the address". `Gate 3` is the entrance of Lumeway Distribution's site, not a street, and does not belong in its postal address. 79 occurrences in 76 examples (re-counted in the merge).
- Condition: Lumeway Distribution's `PostalAddress` has no `AdditionalStreetName` holding a gate; where the gate matters, it is carried by the despatch or pickup location.
- Options: (a) preferred: remove it; (b) give it as the despatch location of the shipment where the despatch point matters.
- Needs decision: no
- From: parties (F2), context (F5)

### air/08#F7 · Medium · The advice does not say when the goods leave or arrive, nor how they can be identified on arrival
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Kelaro Air Cargo`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Eight side frames, needed before the ship arrives.`
- Why: A Despatch Advice is "used to describe the despatch or delivery of goods"; the receiver (Nalevi Warehousing) uses it to prepare for the goods. As in `06-DespatchAdvice.xml`, this one has the carrier but no despatch date, no estimated delivery, no flight or transport stage, and no reference to the air waybill `KXL-WB-26-0325` or to the skid's SSCC `095206103190000015` (`03-ForwardingInstructions.xml`). In a document issued only because the flight changed, these are what it is for.
- Condition: the advice states the despatch date and the expected delivery (or the flight), and identifies the goods for collection (waybill reference and/or SSCC).
- Options: (a) preferred: Shipment/Delivery with despatch date and estimated delivery period, the TransportHandlingUnit with the SSCC and the waybill as a document reference; (b) at least the dates.
- Needs decision: no
- From: logistics (F5, Medium), broad (F7, Low)

### air/08#F8 · Low · The replacement does not say what it replaces, and nothing in it changed
- XPath: `/DespatchAdvice/cbc:ID` = `LD-DA-26-0329`
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `LD-SH-26-0323`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `8`
- Why: `07-FulfilmentCancellation.xml` cancels `LD-DA-26-0327` because the cargo goes on another flight "under a new despatch advice". This document has no reference to the cancelled advice or to the cancellation, and apart from ID, UUID, issue date and time and the contradictory manufacture dates (F4) it is identical to `06-DespatchAdvice.xml` (`diff`, re-run in the merge): same shipment, consignment, carrier, quantity, weight and notes, and no flight or date that the rebooking would change. A receiver cannot tell that it supersedes 06, nor what is new.
- Condition: the replacement identifies the despatch advice it replaces (e.g. an AdditionalDocumentReference to `LD-DA-26-0327`) and carries the information that changed with the rebooking; or, if nothing changed, the flow needs no cancellation and replacement (07's review, F7).
- Options: (a) preferred: the reference plus the new despatch or expected delivery (with F7); (b) drop the cancellation and replacement and report the delay by a transport status (changes the flow).
- Needs decision: yes (the documents of the flow)
- From: broad (F5, decision no), logistics (F6, decision yes), context (F9, decision yes)

### air/08#F9 · Low · "No status" document and line status
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`
- Why: DocumentStatusCode is "A code signifying the status of the Despatch Advice with respect to its original state. This code may be used if the document precedes the event and is subsequently found to be incorrect and in need of cancellation or revision." `NoStatus` says only what the absence of the element would say ("nothing implied by absence", IND5/IND6); the same holds for LineStatusCode. The context part cites the status only as evidence for F8 (nothing marks this advice as a replacement); as a finding of its own it is added by the merge for consistency with the merged reviews of the wood and plastics flows (Low).
- Condition: DocumentStatusCode and LineStatusCode are absent, or carry a status the definition's condition describes.
- Options: drop both (preferred).
- Needs decision: no
- From: merge (context F9 cites the value as evidence)

### air/08#F10 · Low · Damage to be reported "on the consignment note" in an air shipment
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- Why: The goods fly under the air waybill `KXL-WB-26-0325` (`04-Waybill.xml`, WaybillTypeCode `AWB`); "consignment note" without qualifier is the road or rail document. The logistics part refuted this because the Warsaw Convention calls the air waybill the "air consignment note" (own knowledge); the merge keeps it Low because the note does not say "air consignment note" and the flow calls its document the air waybill.
- Condition: the note names the transport document of this shipment, or is absent.
- Options: "… on the air waybill" (preferred) or "… on the delivery receipt".
- Needs decision: no
- From: broad (F6), context (F6); refuted by logistics (Considered and refuted)

### air/08#F11 · Low · English renderings of island addresses tagged en-XB here, en-XL elsewhere
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]/@languageID` = `en-XB`
- XPath: `01-OrderChange.xml:/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XL`
- XPath: `04-Waybill.xml:/Waybill/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`
- Why: The English renderings of the addresses of Nalevi Warehousing, Velumi Trading and Kelaro Air Cargo carry `en-XB` here, `en-XL` for the same text of the same parties elsewhere in the flow (35 examples tag `Port Wrenfield` `en-XB`, 27 `en-XL`; `grep -rl --include='*.xml'`, re-counted in the merge). The broad part refuted it because the tag follows the issuer's English consistently; that rule is possible but written down nowhere, and the island names argue for `en-XL`. The merge cannot settle it. The island parties' `CompanyLegalForm` is in English only, without `languageID`.
- Condition: the same rendering of the same address carries the same `languageID` in every example of the flow, chosen by a stated rule.
- Options: (a) preferred: `en-XL` for island addresses everywhere; (b) keep the writer's variety and record the rule.
- Needs decision: yes (which convention the world follows)
- From: parties (F3); refuted by broad (Considered and refuted), counter-argument above

### air/08#F12 · Low · The island parties' legal form in one untagged rendering
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Island limited company`
- Why: The legal form of Nalevi Warehousing, Velumi Trading and Kelaro Air Cargo appears here once, in English, without `languageID`, while the island-issued examples give it in Lisavan and English, each tagged (`09-TransportationStatus.xml`, `04-Waybill.xml`), and the addresses of the same parties are rendered in both languages in this very document. The parties part mentioned this as related to its language-tag finding (F11); the merge makes it a separate Low finding, aligned with the merges of air 01–05, wood and plastics ("render like the address"), because the same party's master data is described differently whichever tag rule is chosen.
- Condition: the legal form is rendered the same way as the party's address (both languages, tagged) in every example of the flow, or one documented rule explains the difference.
- Options: render it like the address, with `qal` and English tagged (preferred); or a documented rule.
- Needs decision: no
- From: parties (as a remark in F3)

### air/08#F13 · Low · The same registration date 1996-01-01 for many unrelated companies
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `PartyLegalEntity/cbc:RegistrationDate` as "The registration date of the CompanyID." 1996-01-01 is given for Nalevi Warehousing, Velumi Trading and Kelaro Air Cargo here, and for 25 companies in three registers over 181 examples (`grep -rl --include='*.xml'`, re-counted in the merge), while other companies of the same registers have individual dates. Without a story event it reads as a default value ("no fillers").
- Condition: each company's `RegistrationDate` is its own date, or it is absent; if a common date is meant, the story states why.
- Options: (a) a date per company; (b) drop it where no date is known; (c) record 1996-01-01 as a story event.
- Needs decision: yes (company histories)
- From: parties (F4)

### air/08#F14 · Low · Contact name, job title and department disagree, and do not fit the role
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Cargo sales`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Department` = `Operations`
- Why: `Contact/cbc:JobTitle` is "The job title or function of this contact" and `cbc:Department` "The department where this contact works". The delivery recipient's `Goods inwards` and the buyer's `Purchasing` contacts are customer service officers in Sales; the carrier's `Cargo sales` contact is an operations planner in Operations. Names, titles and departments disagree, and the receiving party's contact does not handle receipt. As in `06-DespatchAdvice.xml` and throughout the flow.
- Condition: in each contact, `Name`, `JobTitle` and `Department` describe the same function, and that function fits the party's role.
- Options: (a) preferred: matching titles and departments (buyer / Purchasing; warehouse supervisor / Warehouse; cargo sales agent / Sales, or a cargo operations desk); (b) drop `JobTitle` and `Department`.
- Needs decision: no
- From: broad (F8), parties (F5)

### air/08#F15 · Low · The Urvanian national tariff code in a Bayvarra–Lisavu despatch
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: The code is from Urvania's national tariff (listID `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`); the goods go from Bayvarra to Lisavu, Urvania is only the origin, and no party of this despatch uses it: copied from the item master (section 4.8). In 06 the broad part refuted the same value as the only national list with XU as origin; that explains where it comes from, not why this despatch carries it. 61 occurrences in 43 examples (re-counted in the merge).
- Condition: the item carries only classifications the parties of this despatch use, or the document gives a reason for the Urvanian one.
- Options: drop it, keeping HS 732599 (preferred).
- Needs decision: no
- From: context (F7)

### air/08#F16 · Low · A registration ID for castings that are registered nowhere
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:RegistrationID` = `VI-QR-03190`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[8]/cbc:RegistrationID` = `VI-QR-03197`
- Why: RegistrationID is "The registration identifier of this item instance", for items registered with an authority or registry. A bench side frame casting has no registration that the flow names; the value looks like a QR label code, already covered by ProductTraceID and SerialID. Applies to ItemInstance[1] to [8].
- Condition: RegistrationID is present only where the casting is registered somewhere the document can name; otherwise absent.
- Options: (a) preferred: drop it; (b) name the register if the world has one.
- Needs decision: no
- From: context (F8)

## Checked and consistent
- Everything except ID, UUID, issue date and time and the manufacture dates is identical to `06-DespatchAdvice.xml` (`diff`, broad; re-run in the merge): parties, shipment `LD-SH-26-0323`, consignment `LD-CS-26-0324`, gross 81.6 kg, carrier, item and quantity 8; these agree with `03-ForwardingInstructions.xml` and `04-Waybill.xml` (all parts).
- DeliveredQuantity 8 EA = 8 item instances = package quantity 8 in air/03; LineCountNumeric 1 (logistics).
- GTIN 9520610000029 and GLN 9520610900008: check digits OK; item, manufacturer Valdara Industries `XU-R-104274` and HS 732599 agree with `01-OrderChange.xml` (broad, logistics, parties, context).
- Despatch supplier and seller Lumeway Distribution, buyer Velumi Trading, delivery customer Nalevi Warehousing as in the order change; carrier Kelaro Air Cargo as in the waybill; DespatchAdviceTypeCode `DELIVERY` fits (parties, context).
- Telephone numbers use the unassigned code +999 and domains `.example` (parties).

## Considered and refuted
- `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureTime` = `06:40:00`: eight castings with the same minute — refuted because castings of one melt (M-26-0412) are poured together (from logistics).
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Nalevi Warehousing`: delivery customer differs from the consignee Velumi Trading of air/03 and air/04 — refuted because the buyer's warehouse receives the goods for the buyer, as the order change says (from logistics).
- `/DespatchAdvice/cac:SellerSupplierParty`: repeats the despatch supplier — refuted: identifier only, no condition in the definition (from parties).
- `/DespatchAdvice/cac:BuyerCustomerParty` described in full — refuted: the buyer is the party to whom the goods are advised as sold (from parties).
- `/DespatchAdvice/cbc:Note`: "consignment note" in air freight — refuted by logistics (Warsaw term); the merge disagrees in part and keeps it as F10.
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`: `en-XB` tag on a Lisavu address — refuted by broad (tag follows the issuer); the merge cannot settle it and keeps it as F11.

## Changed in the merge
- context/F1 → F2 and F3: split into the non-existent order and the wrong order line (different elements, different fixes).
- broad/F1 → F4: the per-instance XPath lines shortened to the first and last instance with the condition covering all eight; logistics and context combined.
- broad/F7 (Low) and logistics/F5 (Medium) → F7, Medium: a despatch advice's purpose depends on the dates; aligned with 06 and the DespatchAdvice reviews of wood and plastics.
- broad/F5, logistics/F6, context/F9 → F8: combined; Needs decision yes (two of three parts, and the fix may remove documents from the flow).
- F9 is new as a finding (context/F9 cites NoStatus only as evidence), for consistency with wood and plastics.
- broad/F4 options: "drop LocaleCode" now preferred, as parties, context and the other flows.
- broad/F8 and parties/F5 → F14: combined.
- parties/F3 (remark on the untagged legal form) → F12: a finding of its own, aligned with the merges of air 01–05, wood and plastics.

## Outside this review
- Timeline: issued 14 May 10:48, after the 07:00 departure of KXL207 in `04-Waybill.xml` and before the arrival report of `09-TransportationStatus.xml`; which flight the cargo took is recorded in 07's review (F2) (from broad).
- The castings are manufactured in Urvania (11 May according to this advice, 10 May according to 06) and were accepted at Lumeport on 13 May (`05-TransportationStatus.xml`) after leaving Marrowdale; whether that is possible is a cross-flow timeline question (from logistics, context).
