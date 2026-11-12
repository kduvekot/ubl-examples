# LLM review: 08-DespatchAdvice.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/08-DespatchAdvice.xml`, Git blob `f521e89ceb8199134c10b0a779e9436a0465dcdb` (committed)
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

### air/08#F1 · High · Same serial numbers as in the cancelled despatch advice, but manufactured a day later
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-03190`; `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-11`; `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[2]/cbc:SerialID` = `VI-SF-03191`; `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[2]/cbc:ManufactureDate` = `2026-05-11`; `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[2]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[3]/cbc:SerialID` = `VI-SF-03192`; `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[3]/cbc:ManufactureDate` = `2026-05-11`; `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[3]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[4]/cbc:SerialID` = `VI-SF-03193`; `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[4]/cbc:ManufactureDate` = `2026-05-11`; `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[4]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[5]/cbc:SerialID` = `VI-SF-03194`; `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[5]/cbc:ManufactureDate` = `2026-05-11`; `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[5]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[6]/cbc:SerialID` = `VI-SF-03195`; `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[6]/cbc:ManufactureDate` = `2026-05-11`; `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[6]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[7]/cbc:SerialID` = `VI-SF-03196`; `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[7]/cbc:ManufactureDate` = `2026-05-11`; `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[7]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[8]/cbc:SerialID` = `VI-SF-03197`; `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[8]/cbc:ManufactureDate` = `2026-05-11`; `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[8]/cbc:ManufactureDate` = `2026-05-10`
- Why: This replacement despatch advice ships the same eight item instances as `06-DespatchAdvice.xml`: the same serials VI-SF-03190 … 03197, trace IDs, registration IDs, melt number M-26-0412 and manufacture time 06:40. Each one now has the manufacture date 11 May instead of 10 May. A cast part has one manufacture date, so the two documents contradict each other about the same physical items.
- Condition: every item instance with the same serial number has the same manufacture date and time in both despatch advices.
- Options: (a) 10 May in both, as in 06, which also places manufacture before the order change of 11 May 07:50 (preferred); (b) 11 May in both, but then the frames were cast at 06:40 on the morning the order change was issued (07:50), which needs a reason.
- Needs decision: no

### air/08#F2 · High · The referenced order does not exist
- XPath: `/DespatchAdvice/cac:OrderReference/cbc:ID` = `VT-PO-26-0319`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:OrderReference/cbc:ID` = `VT-OC-26-0320`
- Why: No example has the ID `VT-PO-26-0319`. The frames were ordered under `VT-PO-26-0127` (`sea/05-Order.xml`) as changed by `VT-OC-26-0320` (`01-OrderChange.xml`), the order `07-FulfilmentCancellation.xml` names for this despatch.
- Condition: OrderReference resolves to the order (and change) the goods were ordered under.
- Options: as 06#F1.
- Needs decision: no

### air/08#F3 · High · The despatch line refers to the bench line of the order
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- Why: Order line 1 of `VT-PO-26-0127` is 96 park benches. The side frames despatched here are line 2 or a line added by the order change (01#F1).
- Condition: the OrderLineReference names the side frame line, with the line identification of the order change.
- Options: as 06#F2.
- Needs decision: no

### air/08#F4 · Medium · LocaleCode holds a language code
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". `en` with listID ISO 639 is a language code (213 example files).
- Condition: LocaleCode holds a locale or is absent.
- Options: (a) a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### air/08#F5 · Low · The replacement does not say what it replaces or what changed
- XPath: `/DespatchAdvice/cbc:ID` = `LD-DA-26-0329`
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `LD-SH-26-0323`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `8`
- Why: `07-FulfilmentCancellation.xml` cancels `LD-DA-26-0327` because the cargo goes on another flight "under a new despatch advice". This document has no reference to the cancelled advice or to the cancellation. Apart from ID, UUID, issue time and the contradictory manufacture dates (F1), it is identical to 06: same shipment, consignment, quantity and note. It carries no flight or date that the rebooking would change. A receiver cannot tell that it replaces 06, or why.
- Condition: the replacement identifies the despatch advice it replaces (e.g. an AdditionalDocumentReference to `LD-DA-26-0327`) and contains the information that changed with the rebooking.
- Options: add the reference and the new despatch or expected delivery (see 06#F5 and 07#F5).
- Needs decision: no

### air/08#F6 · Low · Damage to be reported "on the consignment note" in an air shipment
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- Why: A consignment note is the road or rail document. These goods fly under the air waybill `KXL-WB-26-0325`.
- Condition: the note names the transport document of this shipment, or is absent.
- Options: "… on the air waybill / delivery receipt".
- Needs decision: no

### air/08#F7 · Low · No despatch date or expected delivery
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Eight side frames, needed before the ship arrives.`
- Why: As in 06: no despatch date or time, no estimated delivery, no flight. In a document issued only because the flight changed, these are what it is for.
- Condition: the despatch advice states when the goods were despatched and when (or by which flight) they are expected.
- Options: Shipment/Delivery with the despatch and the estimated delivery.
- Needs decision: no

### air/08#F8 · Low · Contacts do not fit their roles
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Cargo sales`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- Why: Names and titles disagree, as in 06 (these combinations recur in 10, 52 and 8 example files).
- Condition: each contact's name, title and department agree with each other and with the role.
- Options: align names or titles.
- Needs decision: no

## Checked and consistent
- Everything except ID, UUID, issue date and time and the manufacture dates is identical to `06-DespatchAdvice.xml` (compared with `diff`): parties, shipment `LD-SH-26-0323`, consignment `LD-CS-26-0324`, gross 81.6 kg, item and quantity 8. These agree with `03-ForwardingInstructions.xml` and `04-Waybill.xml`.
- GTIN 9520610000029 and GLN 9520610900008: check digits OK.

## Considered and refuted
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`: `en-XB` tag on a Lisavu address. Refuted because the tag follows the issuer's English consistently across the examples.

## Outside this review
- Timeline: issued 14 May 10:48. That is after the 07:00 flight of `04-Waybill.xml`, before the cancellation of its predecessor (17:53, recorded as 07#F1), and before the arrival report of `09-TransportationStatus.xml`. Which flight the cargo took is recorded as 07#F2.
