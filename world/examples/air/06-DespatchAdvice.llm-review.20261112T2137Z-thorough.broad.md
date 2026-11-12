# LLM review: 06-DespatchAdvice.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/06-DespatchAdvice.xml`, Git blob `b0da93c08c27cd4207d5ea850651a870b97f6b62` (committed)
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

### air/06#F1 · High · The referenced order does not exist
- XPath: `/DespatchAdvice/cac:OrderReference/cbc:ID` = `VT-PO-26-0319`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:OrderReference/cbc:ID` = `VT-OC-26-0320`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:OrderReference/cac:DocumentReference/cbc:ID` = `VT-PO-26-0127`
- Why: No example has the ID `VT-PO-26-0319`. The goods (8 side frames LD-10443) were ordered by `VT-PO-26-0127` (`sea/05-Order.xml`) as changed by `VT-OC-26-0320` (`01-OrderChange.xml`). The fulfilment cancellation of this very despatch advice names exactly those two as its order, which contradicts this reference.
- Condition: OrderReference resolves to the order (and change) the goods were ordered under, and agrees with `07-FulfilmentCancellation.xml`.
- Options: (a) `VT-PO-26-0127`, with the change identified as in 07 (preferred); (b) add an order `VT-PO-26-0319` to the flow (changes the story).
- Needs decision: no

### air/06#F2 · High · The despatch line refers to the bench line of the order
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cbc:Name` = `Bench side frame casting`
- XPath: `sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`
- Why: Order line 1 of `VT-PO-26-0127` is 96 park benches. The side frames are line 2, or a new line added by `01-OrderChange.xml`, whose own line 1 has the same collision (01#F1). This despatch line ships side frames against the bench line.
- Condition: the OrderLineReference names the order line of the side frames, using the same line identification the order change uses.
- Options: follow the fix of 01#F1 (a new line 3 is preferred there).
- Needs decision: no

### air/06#F3 · Medium · LocaleCode holds a language code
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used". `en` with listID ISO 639 is a language code (213 example files).
- Condition: LocaleCode holds a locale or is absent.
- Options: (a) a locale such as `en-XB`; (b) remove it.
- Needs decision: no

### air/06#F4 · Low · Damage to be reported "on the consignment note" in an air shipment
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- Why: A consignment note is the road (CMR) or rail document. These goods fly under the air waybill `KXL-WB-26-0325` (`04-Waybill.xml`), so the receiver has no consignment note to write on.
- Condition: the note names the transport document of this shipment (the air waybill or the delivery receipt at Selanu), or is absent.
- Options: "… on the air waybill / delivery receipt".
- Needs decision: no

### air/06#F5 · Low · No despatch date or expected delivery
- XPath: `/DespatchAdvice/cac:Shipment/cbc:ID` = `LD-SH-26-0323`
- XPath: `/DespatchAdvice/cac:DespatchLine/cbc:Note` = `Eight side frames, needed before the ship arrives.`
- Why: A despatch advice describes "the despatch or delivery of goods". This one carries neither a despatch date and time nor an estimated delivery (Shipment/Delivery, Despatch/ActualDespatchDate, EstimatedDeliveryPeriod), and no flight. The issue date is the only time reference. The cancellation in `07-FulfilmentCancellation.xml` gives a missed flight as the reason this document became wrong, but the document never mentions a flight.
- Condition: the despatch advice states when the goods were despatched and when (or by which flight) they are expected, so that a change of flight changes the document.
- Options: add Shipment/Delivery with the actual despatch and the estimated delivery (preferred), or the flight as a shipment stage.
- Needs decision: no

### air/06#F6 · Low · Contacts do not fit their roles
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Goods inwards`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/DespatchAdvice/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Cargo sales`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- Why: The recipient's "Goods inwards" and the buyer's "Purchasing" contacts are customer service officers in Sales. The carrier's "Cargo sales" contact is an operations planner. Names and titles disagree, and the delivery recipient's contact does not handle receipt. These combinations recur in 10, 52 and 8 example files.
- Condition: each contact's name, title and department agree with each other and with the role.
- Options: align names or titles.
- Needs decision: no

## Checked and consistent
- Shipment `LD-SH-26-0323`, consignment `LD-CS-26-0324` and gross weight 81.6 kg agree with `03-ForwardingInstructions.xml` and `04-Waybill.xml`. Kelaro is the carrier there too.
- Quantity 8 and the item (LD-10443, VI-C180, GTIN 9520610000029 with valid check digit, HS 732599, origin XU, Valdara Industries) agree with `01-OrderChange.xml` and `sea/05-Order.xml` line 2.
- 8 item instances, serials VI-SF-03190 … 03197, all from melt M-26-0412 on 10 May 06:40: consistent with each other (one pour). The manufacture date is before the order change (11 May), which fits frames taken from stock.
- The delivery recipient Nalevi Warehousing agrees with `01-OrderChange.xml` DeliveryParty.

## Considered and refuted
- `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Lagoon Road`: `en-XB` tag on a Lisavu address. Refuted because the tag follows the issuer's English consistently across the examples.
- `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`: an Urvanian national tariff code. Refuted because it is the only national tariff list in the examples (61 occurrences, all XU), and XU is the item's country of origin.

## Outside this review
- Timeline: issued 13 May 10:07, two minutes after `05-TransportationStatus.xml` reports the cargo accepted at the airport terminal, and before the waybill (10:43). For the timeline review.
