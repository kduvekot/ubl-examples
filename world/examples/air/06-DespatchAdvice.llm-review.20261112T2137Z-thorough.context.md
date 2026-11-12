# LLM review: 06-DespatchAdvice.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: context

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

### air/06#F1 · High · Reference to an order that does not exist, and to the order's bench line
- XPath: `/DespatchAdvice/cac:OrderReference/cbc:ID` = `VT-PO-26-0319`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:OrderLineReference/cbc:LineID` = `1`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cac:OrderReference/cbc:ID` = `VT-OC-26-0320`
- Why: OrderReference is "A reference to an Order with which this Despatch Advice is associated". No example has the ID VT-PO-26-0319 (searched over `world/examples/*/*.xml`); the order is VT-PO-26-0127 (sea/05-Order.xml), changed by VT-OC-26-0320. The fulfilment cancellation of this very despatch advice names VT-OC-26-0320 as its order, so the two documents disagree. The order line reference `1` points, in VT-PO-26-0127, to the 96 benches (`sea/05-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cbc:Name` = `Park bench Serra 180`), not to the side frames.
- Condition: OrderReference resolves to the order (or order change) the goods were ordered under, agrees with 07-FulfilmentCancellation.xml, and the line reference points to the side-frame line.
- Options: (preferred) VT-PO-26-0127 with the line ID the order change gives the added air line (see the review of 01-OrderChange.xml), and the order change as an additional reference; or VT-OC-26-0320, as 07 does.
- Needs decision: no

### air/06#F2 · High · The same castings have another manufacture date in the replacement despatch advice
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-10`
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-03190`
- XPath: `08-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:ManufactureDate` = `2026-05-11`
- XPath: `08-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:SerialID` = `VI-SF-03190`
- Why: ManufactureDate is "The date on which this item instance was manufactured". The eight item instances VI-SF-03190 to VI-SF-03197 (same serials, trace IDs, registration IDs and melt M-26-0412) are manufactured on 10 May here and on 11 May in 08-DespatchAdvice.xml, the despatch advice that replaces this one for the same goods. The same casting cannot have two manufacture dates. Applies to ItemInstance[1] to [8] alike.
- Condition: each item instance has the same manufacture date and time in both despatch advices.
- Options: (preferred) the same date in both (10 May, the earlier, as these are the castings already despatched on 13 May); the replacement only changes what the missed flight changes.
- Needs decision: no

### air/06#F3 · Medium · LocaleCode holds a language code
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) is a language and repeats Language/ID. 362 such elements over `world/examples/*/*.xml` (grep).
- Condition: LocaleCode holds a locale, or is absent.
- Options: (preferred) drop it; or a real locale code with a locale list.
- Needs decision: no

### air/06#F4 · Medium · A gate in AdditionalStreetName of the postal address
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: AdditionalStreetName is "An additional street name used to further clarify the address"; a gate is not a street and does not belong in the despatch party's postal address.
- Condition: no gate in a street-name element of the postal address.
- Options: (preferred) drop it; or, where the despatch point matters, give it as the despatch location of the shipment.
- Needs decision: no

### air/06#F5 · Low · The note asks for remarks on a consignment note in air freight
- XPath: `/DespatchAdvice/cbc:Note` = `Please check the goods on arrival and report any damage on the consignment note.`
- Why: The goods travel by air under an air waybill (04-Waybill.xml, WaybillTypeCode `AWB`); "consignment note" is the road (CMR) or rail document. The consignee would note damage on the air waybill or delivery receipt.
- Condition: the note names the transport document of this shipment.
- Options: (preferred) "… on the air waybill" or "… on the delivery receipt".
- Needs decision: no

### air/06#F6 · Low · The Urvanian national tariff code in a Bayvarra–Lisavu despatch
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `73259990`
- Why: The code is from the national tariff of Urvania (`urn:ubl-examples:world:XU:codelist:CustomsTariffCode`); the goods are despatched from Bayvarra to Lisavu, and Urvania is only the country of origin. Neither the despatch party nor the receiver uses it; it looks copied from the item master. 43 examples carry this list (grep over `*.xml`).
- Condition: the item carries only classifications the parties of this despatch use, or the document gives a reason for the Urvanian one.
- Options: (preferred) drop it, keeping HS 732599.
- Needs decision: no

### air/06#F7 · Low · A registration ID for castings that are registered nowhere
- XPath: `/DespatchAdvice/cac:DespatchLine/cac:Item/cac:ItemInstance[1]/cbc:RegistrationID` = `VI-QR-03190`
- Why: RegistrationID is "The registration identifier of this item instance", used for items registered with an authority or registry (vehicles, devices). A bench side frame casting has no registration; the value looks like the code of a QR label, which is already covered by ProductTraceID ("an identifier used for tracing this item instance") and SerialID. Applies to ItemInstance[1] to [8].
- Condition: RegistrationID is present only where the casting is registered somewhere the document can name; otherwise absent.
- Options: (preferred) drop RegistrationID; or name the register if the world has one for castings (e.g. a public-works asset register of the Port of Selanu).
- Needs decision: no

## Checked and consistent
- Shipment LD-SH-26-0323, consignment LD-CS-26-0324, gross weight 81.6 kg and the carrier agree with 03-ForwardingInstructions.xml and 04-Waybill.xml.
- 8 item instances for a delivered quantity of 8; item, GTIN (check digit OK) and manufacturer agree with 01-OrderChange.xml.
- Delivery to Nalevi Warehousing and buyer Velumi Trading agree with 01-OrderChange.xml; DespatchAdviceTypeCode `DELIVERY` ("Delivery") fits an ordinary despatch.

## Outside this review
- The castings are manufactured in Urvania on 10 May 06:40, the day before the order change (11 May 07:50), and despatched from Marrowdale (Bayvarra) on 13 May: whether they could be there in time is a timeline question across documents.
