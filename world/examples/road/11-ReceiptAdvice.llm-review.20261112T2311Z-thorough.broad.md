# LLM review: 11-ReceiptAdvice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/11-ReceiptAdvice.xml`, Git blob `6223208a8a0ee6befbffd7cfc33c817e4bdf5f7e` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5c0d61b 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/11#F1 · High · Emission value is not factor × base
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: UBL defines `ValueFactorNumeric` as "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` as "The base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". With a factor of 0.82 per 1 EA the calculated value is 0.82, not the stated 96 kg CO2e (`ValueMeasure`, "total emissions in kg CO2"). The factor does not fit any quantity in the item either (34 kg steel and 22.5 kg hardwood consumed per bench: 0.82 × 56.5 kg = 46.3 kg, 0.82 × 34 kg = 27.9 kg). The same block occurs in 39 examples across flows (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82' world/examples | wc -l`).
- Condition: `ValueFactorNumeric` × `ValueBaseMeasure` equals `ValueMeasure` (in consistent units), or the factor and base are absent.
- Options: (a, preferred) give the factor and base the 96 kg are actually calculated from (e.g. kg CO2e per kg of material with the bench's mass as base), so the arithmetic holds; (b) remove `ValueFactorNumeric` and `ValueBaseMeasure` and keep only the total, if no factor is known.
- Needs decision: no

### road/11#F2 · Medium · Language code in LocaleCode
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is defined as "A code signifying the locale in which this language is used"; a locale is a combination of language and region (e.g. en-XB), not a language. The value repeats the ISO 639 language code of `Language/ID` (listID `ISO 639`), so the element carries a language, not a locale, and adds nothing to `Language/ID`. The same pattern occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: `LocaleCode` is either absent or holds a locale (language and region) from a locale list named in its listID, different in meaning from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`, since `Language/ID` already says English and nothing in the document needs the region; (b) give a real locale such as en-XB with a locale list as listID, if the region matters to the party.
- Needs decision: no

### road/11#F3 · Medium · Gate number in AdditionalStreetName of the postal address
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is not a street name but an entrance of the business park, information that matters only to vehicles delivering goods, and it is carried in Lumeway's postal/registered address in every document. The road flow itself mentions other entrances (`Gate B` as alternative delivery location and `dock 4` in the Order and Waybill), so the gate is a delivery instruction, not part of the address. Counted over `*.xml`: 76 examples (`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: `AdditionalStreetName` holds no gate, dock or entrance; such information, where needed, is in a delivery location or delivery instruction.
- Options: (a, preferred) remove `Gate 3` from the party address and, where the document is about delivery, put the gate in `Delivery/DeliveryLocation` or the delivery instructions; (b) keep it only in a delivery address with a dedicated element such as `Location/Description`.
- Needs decision: no

### road/11#F4 · Medium · Province in Region instead of CountrySubentity
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/ReceiptAdvice/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative subdivision of the country, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located", with `CountrySubentityCode`). The Bayvarran addresses of the same examples do use `CountrySubentity` (`Upland State`), so the two countries' addresses are structured differently for the same kind of information. Counted over `*.xml`: 104 examples carry `<cbc:Region>Province of …` (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: No address of this example holds a province in `Region`; the province is in `CountrySubentity` (and, where a list exists, `CountrySubentityCode`).
- Options: (a, preferred) move the value to `CountrySubentity`, with a code from the Urvanian subdivision list if one exists, like the Bayvarran addresses; (b) keep `Region` only if Urvania's provinces are defined as economic regions rather than administrative divisions, and say so in the world's address rules.
- Needs decision: no

### road/11#F5 · Low · Contacts that do not fit the role
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ReceiptAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/ReceiptAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: A receipt advice comes from goods-in: the delivery customer's contact should be the receiving warehouse, but Lumeway's contact is its `Customer service` desk in `Sales`. Castrano's contact is named `Warehouse office` but titled `Customer service officer` in `Sales`, which contradicts its name.
- Condition: Contact name, job title and department agree with each other and with the role (goods-in for the receiver, warehouse for the despatcher).
- Options: (a, preferred) give Lumeway a goods-in contact and Castrano a warehouse title and department; (b) omit JobTitle/Department.
- Needs decision: no

### road/11#F6 · Low · Item number looks like a real GTIN-12 with issuer scope 771
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`
- XPath: `/ReceiptAdvice/cac:ReceiptLine[1]/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- Why: The standard item numbers 771020000027 and 771020000034 (scheme `urn:ubl-examples:world:item`) are 12 digits with a valid GS1 mod-10 check digit (computed: 7 and 4), so any scanner or GS1 check reads them as GTIN-12s; a GTIN-12 starting with 7 lies in the UPC range administered by GS1 US, and the issuer scope `771` is also a GS1 prefix (GS1 Colombia, 770–771). This rests on my knowledge of the GS1 prefix allocation. The rule that fictional values must not be mistakable for real register entries applies. In addition, only the bench carries `BarcodeSymbologyID` and `IssuerScopeID`; the side frame's number from the same scheme carries neither.
- Condition: The item numbers cannot be read as validly check-digited GTINs of a real GS1 prefix, and both items of the same scheme are described the same way.
- Options: (a, preferred) confirm against the world's identifier rules whether the world item scheme is meant to mimic GTIN; if so, use a GS1 prefix reserved for demonstration or a non-GS1 structure; (b) drop `IssuerScopeID`/`BarcodeSymbologyID` where they have no role in the document.
- Needs decision: yes

## Checked and consistent
- References: order LD-PO-26-0149 (`01`), despatch advice CL-DA-26-0153 (`04`) with lines 1 and 2, waybill TH-WB-26-0159 as delivery note (`08`), shipment CL-SH-26-0154.
- Quantities: line 1 received 95 + short 1 = 96 despatched; line 2 received 13 − oversupply 1 = 12 despatched; the note (one bench short, one box over) and the line notes (a pallet held three benches and a box) agree with them and with each other.
- Actual delivery 2026-03-25 09:40 is after the carrier's updated delivery time 09:30 (`09-TransportationStatus.xml`) and before the issue at 15:40; within the latest delivery time of the waybill.

## Considered and refuted
- `/ReceiptAdvice/cbc:DeliveryAcceptanceCode` = `ACCEPTED` with a shortage and a replacement request on line 1 — refuted: the delivery is accepted as a whole while the shortage is handled by the line's `ShortageActionCode`; the two are compatible.
- The receipt contradicts the despatch advice and waybill (24 pallets of 4 benches) — refuted: revealing a mis-pick against the despatch documents is the purpose of this receipt advice.
