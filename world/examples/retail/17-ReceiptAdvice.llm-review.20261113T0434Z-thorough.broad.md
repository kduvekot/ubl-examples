# LLM review: 17-ReceiptAdvice.xml

Flow: retail (RETAIL-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0434Z-thorough`
- Example: `world/examples/retail/17-ReceiptAdvice.xml`, Git blob `47b28c9a1fccb7811613ffb860e40b9269d5dddc` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 44b84c0 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### retail/17#F1 · High · Emission factor and base do not give the stated emission
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies". With a base of 1 each the factor says 0.82 kg CO2e per bench, while the value says 96 kg per bench; both cannot hold. 96 / 0.82 ≈ 117 suggests a per-kWh factor, whose base would not be "each". The same triple occurs in 39 examples (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82'`).
- Condition: factor × base quantity equals the stated value in the base's unit, or factor and base are absent.
- Options: (a, preferred) drop factor and base, the value per bench is what the documents use; (b) state the activity and its unit so that factor × activity = 96 kg.
- Needs decision: no

### retail/17#F2 · Medium · Language codes in LocaleCode
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with `listID` `ISO 639` repeats the language code that `Language/cbc:ID` already holds and names no locale. The pattern occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^>]*>[^<]*'` over `world/examples`).
- Condition: every `LocaleCode` holds a locale (language and region) from a list that defines locales, or is absent.
- Options: (a, preferred) drop it; (b) a locale such as `en-XB` from a list that defines it, if a regional variant matters.
- Needs decision: no

### retail/17#F3 · Medium · A vehicle gate as additional street name in Lumeway's postal address
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address". A gate of a business park is a vehicle access detail, not a street name, and has no place in a postal address. The value occurs in 76 examples (`grep -rc --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`, files with a non-zero count).
- Condition: no address of Lumeway holds a gate in `AdditionalStreetName`.
- Options: (a, preferred) drop it from the postal address and give the gate where a vehicle needs it (loading location, delivery instructions); (b) if Bayvarra's address format really makes the gate part of the postal address, record that in the format definition; the finding is then dismissed.
- Needs decision: no

### retail/17#F4 · Low · A damaged carton, but the benches travel unboxed on pallets
- XPath: `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cbc:DamageRemarks` = `One carton torn, the bench's armrest bent.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:Note` = `One bench arrived in a damaged carton and was refused.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:CircularityProfile/cac:WasteGenerated/cbc:WasteTypeDescription` = `Stretch film and pallet straps, per bench`
- Why: the item's own data gives its packaging waste as stretch film and pallet straps, and 12-DespatchAdvice describes pallets of four benches with no cartons (the only package type in the flow is the pallet, `PX`). The receipt advice speaks of a torn carton. The damage description and the packaging the flow describes do not agree.
- Condition: the damage remark refers to packaging the goods actually have, as described in the despatch advice and the item data.
- Options: (a, preferred) describe the damage in terms of the wrapping (e.g. "stretch film torn, one armrest bent"); (b) add cartons to the packaging in 02 and 12.
- Needs decision: no

### retail/17#F5 · Low · Late against a slot that no document agreed
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:TimingComplaintCode` = `LATE`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:TimingComplaint` = `Arrived 40 minutes into the slot; unloading delayed the next truck.`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedTime` = `10:40:00`
- Why: the complaint refers to a delivery slot, but no document of the flow sets one: the order has no requested delivery time (`08-Order.xml:/Order/cac:Delivery/cac:DeliveryLocation/cbc:ID` = `9522610900019` is all its delivery says), and the carrier's last expectation was 2026-04-29 at 14:00 (15-TransportationStatus), a day before the receipt. A delivery that arrives "40 minutes into the slot" is also within the slot, which reads oddly as "late". The reader cannot verify the complaint.
- Condition: the slot the complaint refers to is stated in the flow (order, transport request or status), and the text says how the arrival relates to it.
- Options: (a, preferred) a delivery slot in 08-Order or 11-TransportExecutionPlanRequest (e.g. 10:00–10:30 on 2026-04-30), and "arrived 10 minutes after the end of the slot"; (b) drop the timing complaint.
- Needs decision: no

### retail/17#F6 · Low · Two different photo references for the same damage, neither described
- XPath: `/ReceiptAdvice/cac:AdditionalDocumentReference/cbc:ID` = `BM-GI-PHOTO-26-0510`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:DocumentReference/cbc:ID` = `BS-PHOTO-26-0118`
- XPath: `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cac:DamageDocumentationAttachment/cac:ExternalReference/cbc:URI` = `https://www.brightmarket.example/goods-in/26-0510/pallet-3.jpg`
- Why: the damage on pallet 3 is documented by an attached photo (the URI's folder `26-0510` matches the header reference `BM-GI-PHOTO-26-0510`). The receipt line refers to another document, `BS-PHOTO-26-0118`, in Brightmarket's document numbering. Neither reference says what it is, and it is not clear whether there are two photo records or one.
- Condition: the damage photo is referenced once (or each reference says what it is), consistently with the attachment.
- Options: (a, preferred) keep the attachment and one reference with a document type; drop the other; (b) describe both if they are different records.
- Needs decision: no

### retail/17#F7 · Low · Delivery customer's contact is the buying office, not goods-in
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Buying office`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the receipt advice reports what goods-in counted and checked ("Counted and checked at goods-in."); the delivery customer's contact is Brightmarket's buying office, with a job title and department (customer service officer, sales) that contradict its name. The order names the goods-in contact (`08-Order.xml:/Order/cac:BuyerCustomerParty/cac:DeliveryContact/cbc:Name` = `Goods-in, garden department`). Lumeway's contact as despatch supplier is its customer service in sales, while the order names a dispatch office.
- Condition: the contacts fit receiving and despatching, with name, job title and department that agree.
- Options: (a, preferred) Brightmarket's goods-in and Lumeway's dispatch office.
- Needs decision: no

### retail/17#F8 · Low · Handling unit receipt line reuses the receipt line's ID with another quantity
- XPath: `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cac:ReceivedHandlingUnitReceiptLine/cbc:ID` = `1`
- XPath: `/ReceiptAdvice/cac:Shipment/cac:TransportHandlingUnit/cac:ReceivedHandlingUnitReceiptLine/cbc:ReceivedQuantity` = `3`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:ID` = `1`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedQuantity` = `23`
- Why: both are receipt lines; receipt line 1 covers 23 benches received, the handling unit's receipt line 1 the 3 of pallet 3. The same line ID denotes two lines with different quantities, so a credit note referring to receipt line 1 is ambiguous.
- Condition: receipt line IDs are unique within the document, or the handling unit line is clearly a breakdown of line 1.
- Options: (a, preferred) an ID such as `1.3` for the pallet's line.
- Needs decision: no

### retail/17#F9 · Low · Whole item master data copied into the receipt line
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:EnvironmentalEmission`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:CircularityProfile`
- XPath: `/ReceiptAdvice/cac:ReceiptLine/cac:Item/cac:CommodityClassification[2]/cbc:CommodityCode` = `94017910`
- Why: a receipt advice identifies what was received; the item's catalogue data (emissions, circularity, load test, dimensions, Urvania's tariff code in a domestic Bayvarran delivery, and the distributor's wording "from the distributor's stock" in a document written by the buyer) is not used by it.
- Condition: the received item carries its identifiers and what the receipt depends on.
- Options: (a, preferred) drop the catalogue data from the item.
- Needs decision: no

## Checked and consistent
- 23 received + 1 rejected = 24 despatched (`12-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `24`); on pallet 3, 3 + 1 = 4 benches, as despatched on that pallet.
- The damaged handling unit `095206102170000038` is pallet 3 of 12-DespatchAdvice (`12-DespatchAdvice.xml:/DespatchAdvice/cac:Shipment/cac:TransportHandlingUnit[3]/cbc:ShippingMarks` = `BRIGHTMARKET LUMEPORT / 003 of 006`), matching the photo `pallet-3.jpg`; shipment `LD-SH-26-0230` is that of 12 and 13.
- References: order `BS-PO-26-0224` and order line 1, despatch advice `LD-DA-26-0229` and despatch line 1 resolve; despatch line 1 is the line with 24 benches.
- Reject reason, action (credit requested) and acceptance code (partly refused) agree with each other and with the credit note 19-CreditNote, which credits one bench.
- Received on 2026-04-30 at 10:40, advice issued the same day at 15:21; buyer's item ID `BM-551210` equals 08-Order's.

## Considered and refuted
- `/ReceiptAdvice/cac:ReceiptLine/cbc:ReceivedQuantity` = `23`: suspected that UBL's "quantity received" should include the rejected bench (24) — refuted: received and rejected quantities add up to the delivered quantity and the status text ("Three benches accepted, one refused") makes the reading clear; UBL's definitions ("The quantity received", "The quantity rejected") allow it.

## Outside this review
- Timeline: received on 2026-04-30 at 10:40, while 15-TransportationStatus expected arrival on 2026-04-29 at 14:00, for a haul billed as 38 km (16-Invoice).
