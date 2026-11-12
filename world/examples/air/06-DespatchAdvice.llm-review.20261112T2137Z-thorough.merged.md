# LLM review: 06-DespatchAdvice.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/06-DespatchAdvice.xml`, Git blob `b0da93c08c27cd4207d5ea850651a870b97f6b62` (committed)
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

### air/06#F1 · High · The referenced order VT-PO-26-0319 does not exist
- XPath: `/DespatchAdvice/cac:OrderReference/cbc:ID` = `VT-PO-26-0319`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:OrderReference/cbc:ID` = `VT-OC-26-0320`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:OrderReference/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: OrderReference is "A reference to an Order with which this Despatch Advice is associated". No example has the ID VT-PO-26-0319 (`grep -rn --include='*.xml' VT-PO-26-0319 world/examples`: only the references in air/03, air/06 and air/08, re-run in the merge). The eight side frames were ordered by the order change VT-OC-26-0320 (`01-OrderChange.xml`) to order VT-PO-26-0127 (`sea/05-Order.xml`), and the fulfilment cancellation of this very despatch advice (`07-FulfilmentCancellation.xml`) names exactly these two as its order, so the flow contradicts itself about which order this despatch belongs to. The merge tried to read VT-PO-26-0319 as another identifier of the same order (e.g. the seller's): it is not, because the seller's order number is `LD-SO-26-0123` (`07-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:OrderReference/cbc:SalesOrderID` = `LD-SO-26-0123`).
- Condition: the OrderReference resolves to the order (and order change) the goods were ordered under, and agrees with `07-FulfilmentCancellation.xml`.
- Options: (a) preferred: OrderReference ID VT-PO-26-0127 with the order change VT-OC-26-0320 as its DocumentReference (or the other way round, exactly as 07 has it), because 07 already carries the resolving reference; (b) add an order VT-PO-26-0319 to the flow, which changes the story.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1, first part)

### air/06#F2 · High · The despatch line refers to the bench line of the order
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cbc:Name` = `Bench side frame casting`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[2]/cac:LineItem/cac:Item/cbc:Name` = `Bench side frame casting`
- XPath: `01-OrderChange.xml:/OrderChange/cac:OrderLine/cac:LineItem/cbc:ID` = `1`
- Why: OrderLineReference/LineID is "An identifier for the referenced order line, assigned by the buyer". In order VT-PO-26-0127 line 1 is the 96 park benches and line 2 the 12 side frames sent by sea; the 8 frames for air were added by the order change, which gives its new line the ID 1, the ID of the bench line (a finding of the review of `01-OrderChange.xml`). The merge tried to refute this: the line ID agrees with the order change as written. It does not save the reference: in an order change a line ID names the order's line it changes, so line 1 is still the bench line of VT-PO-26-0127, the order that `07-FulfilmentCancellation.xml` gives for this despatch. The despatch line thus ships side frames against the bench line.
- Condition: the OrderLineReference names the order line of the eight air-freighted side frames, with the same line ID the (corrected) order change gives that line.
- Options: follow the fix of the order change (preferred there and here: a new line 3), carried through `02-OrderResponse.xml`, this example and `08-DespatchAdvice.xml`.
- Needs decision: no
- From: broad (F2), logistics (F2), context (F1, second part)

### air/06#F3 · High · The same eight castings have another manufacture date in the replacement despatch advice
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-03190`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[8]/cbc:SerialID` = `VI-SF-03197`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[8]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `08-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-03190`
- XPath: `08-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-11`
- Why: ItemInstance is "A trackable, unique instantiation of this item" and ManufactureDate "The date on which this item instance was manufactured". Both despatch advices list the same eight castings (SerialID VI-SF-03190 to VI-SF-03197, the same ProductTraceID, RegistrationID, melt M-26-0412 and time 06:40), but this one says they were made on 2026-05-10 and `08-DespatchAdvice.xml` on 2026-05-11. A `diff` of the two files (re-run in the merge) shows that apart from ID, UUID, issue date and time, the eight ManufactureDate values are the only difference, in all of ItemInstance[1] to [8]. The merge tried to read 08 as a correction of a wrong date in 06; the cancellation gives a missed flight as the only reason for the replacement (`07-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:CancellationNote` = `The cargo missed its flight; it goes on the next day's flight under a new despatch advice.`), not an error in 06, so the contradiction stands.
- Condition: every item instance has the same manufacture date and time in `06-DespatchAdvice.xml` and `08-DespatchAdvice.xml`.
- Options: (a) preferred: 2026-05-10 in both, so that the frames exist before the order change of 2026-05-11 07:50 and come from stock; (b) 2026-05-11 in both, which needs a reason why castings poured at 06:40 that morning were promised 70 minutes later.
- Needs decision: no
- From: logistics (F3), context (F2)

### air/06#F4 · Medium · LocaleCode holds a language code
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/cbc:LocaleCode` as "A code signifying the locale in which this language is used." A locale is a language as used in a region, not the language itself. The value is the ISO 639 language code `en` (listID `ISO 639`), the same value the sibling `cbc:ID` already carries. The skill's severity guide names "a language code in `LocaleCode`" as a Medium case. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^<]*<' world/examples` and `grep -rl`, re-counted in the merge).
- Condition: every `cbc:LocaleCode` in this example holds a locale code from a locale list (with a matching listID), or the element is absent.
- Options: (a) preferred: drop `LocaleCode` where the party has no locale beyond its language; (b) a real locale (e.g. a BCP 47 tag such as `en-XB`, with a listID naming that list), if the world has a reason to state the locale.
- Needs decision: no
- From: broad (F3), parties (F1), context (F3)

### air/06#F5 · Medium · A gate in AdditionalStreetName of the despatch party's postal address
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: UBL defines `Address/cbc:AdditionalStreetName` as "An additional street name used to further clarify the address". `Gate 3` is not a street name but the entrance of Lumeway Distribution's site, information about access, not part of its postal address (whose street, building number, block and plot are given). The skill's checklist: "a gate or dock is not a street name; a postal address holds nothing that only matters for vehicles." The same value occurs 79 times in 76 examples (`grep -rh`/`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, re-counted in the merge).
- Condition: Lumeway Distribution's `PostalAddress` has no `AdditionalStreetName` holding a gate; where the gate matters (a pickup or despatch place), it is carried by an element meant for it (e.g. the name or description of the despatch `Location`).
- Options: (a) preferred: remove it from the postal address; (b) move it to the despatch or pickup location of the documents that need it.
- Needs decision: no
- From: parties (F2), context (F4)

### air/06#F6 · Medium · The advice does not say when the goods leave or arrive, nor how they can be identified on arrival
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `LD-SH-26-0323`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyName/cbc:Name` = `Kelaro Air Cargo`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Eight side frames, needed before the ship arrives.`
- Why: A Despatch Advice is "used to describe the despatch or delivery of goods"; the receiver (Nalevi Warehousing) uses it to prepare for the goods. This one has the carrier but no despatch date (Shipment/Delivery/Despatch/ActualDespatchDate), no estimated delivery (Delivery/EstimatedDeliveryPeriod), no transport stage or flight, and no reference to the air waybill (`KXL-WB-26-0325`, `04-Waybill.xml`) or to the skid's SSCC `095206103190000015` (`03-ForwardingInstructions.xml:/ForwardingInstructions/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit/cbc:ID` = `095206103190000015`), by which the warehouse would collect and identify the goods at Selanu airport. The issue date is its only time reference, while its own line note says time is the point of the delivery. The cancellation in `07-FulfilmentCancellation.xml` gives a missed flight as the reason this document became wrong, but the document never mentions a flight (see 07's and 08's reviews). Checked in the merge: the XML has no Delivery, Despatch, ShipmentStage, TransportHandlingUnit or DocumentReference element at all.
- Condition: the despatch advice states when the goods were despatched and when (or by which flight) they are expected, and identifies them for collection (waybill reference and/or the handling unit's SSCC), so that a change of flight changes the document.
- Options: (a) preferred: Shipment/Delivery with the actual despatch and the estimated delivery period, the TransportHandlingUnit with the SSCC and the waybill as a document reference; (b) at least the dates, or the flight as a shipment stage.
- Needs decision: no
- From: logistics (F4, Medium), broad (F5, Low)

### air/06#F7 · Low · "No status" document and line status
- XPath: `/DespatchAdvice/cbc:DocumentStatusCode` = `NoStatus`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:LineStatusCode` = `NoStatus`
- Why: DocumentStatusCode is "A code signifying the status of the Despatch Advice with respect to its original state. This code may be used if the document precedes the event and is subsequently found to be incorrect and in need of cancellation or revision." At issue the document is in its original state, and `NoStatus` states only what its absence would say, which the rule "nothing implied by absence" (IND5/IND6) excludes. The same holds for LineStatusCode ("with respect to its original state"). Not raised as a finding by any part of this run; added by the merge for consistency with the merged reviews of the wood and plastics flows, which record `NoStatus` as Low.
- Condition: DocumentStatusCode and LineStatusCode are absent, or carry a status the definition's condition describes.
- Options: drop both (preferred).
- Needs decision: no
- From: merge (no part)

### air/06#F8 · Low · Damage to be reported "on the consignment note" in an air shipment
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- Why: The goods fly under the air waybill `KXL-WB-26-0325` (`04-Waybill.xml`, WaybillTypeCode `AWB`); "consignment note" without qualifier is the road (CMR) or rail document. The logistics part refuted this because the Warsaw Convention calls the air waybill the "air consignment note" (own knowledge). The merge keeps it as Low: the term in the note is "consignment note", not "air consignment note", and the flow calls its document the air waybill, so the receiver has to guess which document is meant.
- Condition: the note names the transport document of this shipment (the air waybill, or the delivery receipt at Selanu), or is absent.
- Options: "… on the air waybill" (preferred) or "… on the delivery receipt".
- Needs decision: no
- From: broad (F4), context (F5); refuted by logistics (Considered and refuted)

### air/06#F9 · Low · English renderings of island addresses tagged en-XB here, en-XL elsewhere
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
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XL`
- Why: The English renderings of the addresses of the island parties Nalevi Warehousing (`Lagoon Road`, `Port Wrenfield`), Velumi Trading (`Reef Street`, `Port Wrenfield`) and Kelaro Air Cargo (`Airfield Road`, `Port Wrenfield`) carry `en-XB` (English as used in Bayvarra) here, but `en-XL` for the same text of the same parties in other examples of the flow. Across all examples, `languageID="en-XB">Port Wrenfield` occurs in 35 examples and `languageID="en-XL">Port Wrenfield` in 27 (`grep -rl --include='*.xml'`, re-counted in the merge). The broad part refuted this because the tag follows the issuer's English consistently; that is a possible rule (the variety of the writer), but it is written down nowhere, and the island's own English names argue for `en-XL`. The merge cannot settle which rule the world follows. Related: the island parties' `CompanyLegalForm` appears here in English only, without `languageID`, where island-issued examples give it in `qal` and `en-XL`.
- Condition: the same rendering of the same address carries the same `languageID` in every example of the flow, chosen by a stated rule (the language variety of the place, or of the writer).
- Options: (a) preferred: tag the English renderings of island addresses `en-XL` everywhere, since they are island names; (b) keep the writer's variety, and record that rule where the world's language conventions are written down.
- Needs decision: yes (which convention the world follows)
- From: parties (F3); refuted by broad (Considered and refuted), counter-argument kept above

### air/06#F10 · Low · The island parties' legal form in one untagged rendering
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- XPath: `09-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Island limited company`
- Why: The legal form of Nalevi Warehousing, Velumi Trading and Kelaro Air Cargo appears here once, in English, without `languageID`, while the island-issued examples give it in Lisavan and English, each tagged (`09-TransportationStatus.xml`, `04-Waybill.xml`), and the addresses of the same parties are rendered in both languages in this very document. The parties part mentioned this as related to its language-tag finding (F9); the merge makes it a separate Low finding, aligned with the merges of air 01–05, wood and plastics ("render like the address"), because the same party's master data is described differently whichever tag rule is chosen.
- Condition: the legal form is rendered the same way as the party's address (both languages, tagged) in every example of the flow, or one documented rule explains the difference.
- Options: render it like the address, with `qal` and English tagged (preferred); or a documented rule.
- Needs decision: no
- From: parties (as a remark in F3)

### air/06#F11 · Low · The same registration date 1996-01-01 for many unrelated companies
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `PartyLegalEntity/cbc:RegistrationDate` as "The registration date of the CompanyID." The date 1996-01-01 (a New Year's Day) is given here for Nalevi Warehousing, Velumi Trading and Kelaro Air Cargo, and for 25 different companies in three countries and three registers over all examples (181 examples, `grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`, re-counted in the merge), while other companies of the same registers have individual dates (Lumeway Distribution 1988-10-03 in this example). Unless the world has an event that registered all these companies on that day, it reads as a default value, which the rule "no fillers" excludes.
- Condition: each company's `RegistrationDate` is its own date, consistent with its history, or it is absent; if a common date is meant, the world's story states why.
- Options: (a) give each company a date that fits its history (company histories are open work for the encyclopaedia); (b) drop `RegistrationDate` where no date is known; (c) if 1996-01-01 is an event in the story (a new register), keep it and say so there.
- Needs decision: yes (company histories)
- From: parties (F4)

### air/06#F12 · Low · Contact name, job title and department disagree, and do not fit the role
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Cargo sales`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Department` = `Operations`
- Why: `Contact/cbc:JobTitle` is "The job title or function of this contact" and `cbc:Department` "The department where this contact works". Nalevi Warehousing's `Goods inwards` contact (the party receiving the goods) and Velumi Trading's `Purchasing` contact (the buyer) are both customer service officers in Sales; Kelaro Air Cargo's `Cargo sales` contact is an operations planner in Operations. Name, title and department of one contact disagree, and the delivery recipient's contact does not handle receipt. The same combinations recur for these parties throughout the flow (`Purchasing` with `Customer service officer`/`Sales` in 52 places over all `*.xml`, `grep -rh -A2 '<cbc:Name>Purchasing</cbc:Name>'`, count from the parties part).
- Condition: in each contact, `Name`, `JobTitle` and `Department` describe the same function, and that function fits the party's role in the document (a buyer's contact buys, a delivery party's contact receives goods, a carrier's contact handles the transport).
- Options: (a) preferred: job titles and departments that match the functional names (Purchasing: buyer / Purchasing; Goods inwards: warehouse supervisor / Warehouse; Cargo sales: cargo sales agent / Sales, or rename the Kelaro contact to a cargo operations desk); (b) drop `JobTitle` and `Department` where they add nothing to the functional name.
- Needs decision: no
- From: broad (F6), parties (F5)

### air/06#F13 · Low · The Urvanian national tariff code in a Bayvarra–Lisavu despatch
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: The code is from the national tariff of Urvania (listID `urn:ubl-examples:world:XU:codelist:CustomsTariffCode`); the goods are despatched from Bayvarra to Lisavu, Urvania is only the country of origin, and no customs procedure in Urvania is part of this despatch. Neither the despatch party nor the receiver uses it; it looks copied from the item master (section 4.8). The broad part refuted this because it is the only national tariff list in the examples (61 occurrences in 43 examples, re-counted in the merge with `grep -rh`/`grep -rl --include='*.xml' 'XU:codelist:CustomsTariffCode'`) and XU is the origin; the merge disagrees: that explains where the code comes from, not why this despatch carries it.
- Condition: the item carries only classifications the parties of this despatch use, or the document gives a reason for the Urvanian one.
- Options: drop it, keeping HS 732599 (preferred).
- Needs decision: no
- From: context (F6); refuted by broad (Considered and refuted), counter-argument above

### air/06#F14 · Low · A registration ID for castings that are registered nowhere
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:RegistrationID` = `VI-QR-03190`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[8]/cbc:RegistrationID` = `VI-QR-03197`
- Why: RegistrationID is "The registration identifier of this item instance", used for items registered with an authority or registry (vehicles, devices). A bench side frame casting has no registration that the flow names; the value looks like the code of a QR label, already covered by ProductTraceID and SerialID. Applies to ItemInstance[1] to [8].
- Condition: RegistrationID is present only where the casting is registered somewhere the document can name; otherwise absent.
- Options: (a) preferred: drop RegistrationID; (b) name the register if the world has one for castings (e.g. a public-works asset register of the Port of Selanu).
- Needs decision: no
- From: context (F7)

## Checked and consistent
- Shipment `LD-SH-26-0323`, consignment `LD-CS-26-0324`, gross weight 81.6 kg and the carrier Kelaro Air Cargo (`IC41311`) agree with `03-ForwardingInstructions.xml` and `04-Waybill.xml` (all parts; re-checked in the merge).
- DeliveredQuantity 8 EA = 8 item instances = package quantity 8 in `03-ForwardingInstructions.xml`; LineCountNumeric 1 = one despatch line (logistics).
- The item (LD-10443, VI-C180, GTIN 9520610000029 with valid check digit, HS 732599, origin XU, manufacturer Valdara Industries `XU-R-104274`) agrees with `01-OrderChange.xml` and `sea/05-Order.xml` line 2 (broad, logistics, parties, context).
- The eight castings share melt M-26-0412 and 06:40; consistent with each other (one pour) (broad, logistics).
- Lumeway Distribution is described identically wherever it appears in full: register `20410274`, GLN `9520610900008` (check digit correct; GS1 prefix 952 is GS1's range for demonstrations), customs trader `XB-TR-410274`, state tax number with jurisdiction Upland State matching `XB-UL`; Ltd, MEDIUM, registered 1988-10-03 (parties).
- Despatch supplier and seller Lumeway Distribution, buyer Velumi Trading, delivery customer Nalevi Warehousing as in the order change (`01-OrderChange.xml:/OrderChange/cac:Delivery/cac:DeliveryParty/cac:PartyIdentification/cbc:ID` = `IC41722`); DespatchAdviceTypeCode `DELIVERY` fits an ordinary despatch (parties, context).
- 06 and 08 describe every party identically (parties; confirmed by `diff` in the merge).
- Telephone numbers `+999 …` use the ITU-reserved, unassigned country code 999; web and mail domains use `.example` (parties, own knowledge).

## Considered and refuted
- `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureTime` = `06:40:00`: eight castings with the same minute — refuted because castings of one melt (M-26-0412, the same for all eight) are poured together (from logistics; broad came to the same conclusion).
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Nalevi Warehousing`: delivery customer differs from the consignee Velumi Trading of air/03 and air/04 — refuted because the buyer's warehouse receives the goods for the buyer, as the order change says (DeliveryParty) (from logistics).
- `/DespatchAdvice/cac:SellerSupplierParty`: repeats the despatch supplier — refuted: identifier only, no condition in the definition (from parties).
- `/DespatchAdvice/cac:BuyerCustomerParty` described in full in a despatch advice — refuted: the buyer is the party to whom the goods are advised as sold; it is not a different party from the order (from parties).
- `/DespatchAdvice/cbc:Note`: "consignment note" in air freight — refuted by logistics (Warsaw "air consignment note"); the merge disagrees in part and keeps it as F8.
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`: `en-XB` tag on a Lisavu address — refuted by broad (tag follows the issuer); the merge cannot settle it and keeps it as F9.
- `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`: national tariff code — refuted by broad (only national list, XU is origin); the merge disagrees and keeps it as F13.

## Changed in the merge
- context/F1 → F1 and F2: split into the non-existent order and the wrong order line, because they are different elements with different fixes (the order line depends on the order change's fix).
- broad/F5 (Low) and logistics/F4 (Medium) → F6, Medium: a despatch advice's purpose depends on despatch and delivery dates; same severity as the merged reviews of DespatchAdvice in wood and plastics. Evidence from both parts combined.
- broad/F6 and parties/F5 → F12: combined; the Department values added to every contact.
- broad/F3 options: the preferred option is now "drop LocaleCode" (as parties and context, and the other flows), not "a locale such as en-XB".
- F7 is new in the merge (no part raised NoStatus), for consistency with wood and plastics.
- parties/F3 (Low, yes) → F9: broad's refutation added as counter-argument; severity and decision unchanged.
- context/F6 → F13: broad's refutation added as counter-argument; kept Low.
- context/F7 → F14: the last instance's XPath added.

## Outside this review
- Timeline: issued 13 May 10:07, two minutes after `05-TransportationStatus.xml` reports the cargo accepted at the airport terminal, and before the waybill (10:43) (from broad).
- The castings are manufactured in Urvania on 10 May (or 11 May according to air/08) at 06:40, the day before (or the morning of) the order change of 11 May 07:50, and are ready for despatch in Marrowdale, Bayvarra, on 12–13 May (`03-ForwardingInstructions.xml`); whether that is possible is a cross-flow timeline question (from logistics, context).
