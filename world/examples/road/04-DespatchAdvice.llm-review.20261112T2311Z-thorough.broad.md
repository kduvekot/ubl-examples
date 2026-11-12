# LLM review: 04-DespatchAdvice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/04-DespatchAdvice.xml`, Git blob `d5694687ad07a0bd4b1b8412513e13a712a00375` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b8faf2 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/04#F1 · High · Despatch advice issued before the actual despatch it reports
- XPath: `/DespatchAdvice/cbc:IssueDate` = `2026-03-23`
- XPath: `/DespatchAdvice/cbc:IssueTime` = `15:15:00`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ActualDespatchDate` = `2026-03-23`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Delivery/cac:Despatch/cbc:ActualDespatchTime` = `16:20:00`
- Why: `ActualDespatchDate`/`Time` is "The actual despatch (pickup) date/time". The document is issued on 2026-03-23 at 15:15 but reports an actual despatch at 16:20 the same day, 65 minutes in the future. The waybill confirms that the truck left at 16:20 (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `16:20:00`), so the value is right and the issue time is too early.
- Condition: The issue date and time are not earlier than the actual despatch reported in the document.
- Options: (a, preferred) issue the despatch advice after the truck has left (e.g. 16:30); (b) report the despatch as estimated if the advice must go out before departure.
- Needs decision: no

### road/04#F2 · High · Emission value is not factor × base
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: UBL defines `ValueFactorNumeric` as "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` as "The base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". With a factor of 0.82 per 1 EA the calculated value is 0.82, not the stated 96 kg CO2e (`ValueMeasure`, "total emissions in kg CO2"). The factor does not fit any quantity in the item either (34 kg steel and 22.5 kg hardwood consumed per bench: 0.82 × 56.5 kg = 46.3 kg, 0.82 × 34 kg = 27.9 kg). The same block occurs in 39 examples across flows (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82' world/examples | wc -l`).
- Condition: `ValueFactorNumeric` × `ValueBaseMeasure` equals `ValueMeasure` (in consistent units), or the factor and base are absent.
- Options: (a, preferred) give the factor and base the 96 kg are actually calculated from (e.g. kg CO2e per kg of material with the bench's mass as base), so the arithmetic holds; (b) remove `ValueFactorNumeric` and `ValueBaseMeasure` and keep only the total, if no factor is known.
- Needs decision: no

### road/04#F3 · Medium · Province in Region instead of CountrySubentity
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/DespatchAdvice/cac:Shipment/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative subdivision of the country, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located", with `CountrySubentityCode`). The Bayvarran addresses of the same examples do use `CountrySubentity` (`Upland State`), so the two countries' addresses are structured differently for the same kind of information. Counted over `*.xml`: 104 examples carry `<cbc:Region>Province of …` (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: No address of this example holds a province in `Region`; the province is in `CountrySubentity` (and, where a list exists, `CountrySubentityCode`).
- Options: (a, preferred) move the value to `CountrySubentity`, with a code from the Urvanian subdivision list if one exists, like the Bayvarran addresses; (b) keep `Region` only if Urvania's provinces are defined as economic regions rather than administrative divisions, and say so in the world's address rules.
- Needs decision: no

### road/04#F4 · Medium · Language code in LocaleCode
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is defined as "A code signifying the locale in which this language is used"; a locale is a combination of language and region (e.g. en-XB), not a language. The value repeats the ISO 639 language code of `Language/ID` (listID `ISO 639`), so the element carries a language, not a locale, and adds nothing to `Language/ID`. The same pattern occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: `LocaleCode` is either absent or holds a locale (language and region) from a locale list named in its listID, different in meaning from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`, since `Language/ID` already says English and nothing in the document needs the region; (b) give a real locale such as en-XB with a locale list as listID, if the region matters to the party.
- Needs decision: no

### road/04#F5 · Medium · Gate number in AdditionalStreetName of the postal address
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is not a street name but an entrance of the business park, information that matters only to vehicles delivering goods, and it is carried in Lumeway's postal/registered address in every document. The road flow itself mentions other entrances (`Gate B` as alternative delivery location and `dock 4` in the Order and Waybill), so the gate is a delivery instruction, not part of the address. Counted over `*.xml`: 76 examples (`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: `AdditionalStreetName` holds no gate, dock or entrance; such information, where needed, is in a delivery location or delivery instruction.
- Options: (a, preferred) remove `Gate 3` from the party address and, where the document is about delivery, put the gate in `Delivery/DeliveryLocation` or the delivery instructions; (b) keep it only in a delivery address with a dedicated element such as `Location/Description`.
- Needs decision: no

### road/04#F6 · Low · Contacts that do not fit the role
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DespatchSupplierParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The despatch supplier's contact is named `Warehouse office` but has the job title `Customer service officer` in `Sales`, which contradicts its name. The delivery customer's contact should receive the goods (goods-in); Lumeway's only contact is its `Customer service` desk in `Sales`.
- Condition: Contact name, job title and department agree with each other and with the role (warehouse for despatch, goods-in for delivery).
- Options: (a, preferred) give Castrano a warehouse job title and department and Lumeway a goods-in contact; (b) omit JobTitle/Department.
- Needs decision: no

### road/04#F7 · Low · Item number looks like a real GTIN-12 with issuer scope 771
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`
- XPath: `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- Why: The standard item numbers 771020000027 and 771020000034 (scheme `urn:ubl-examples:world:item`) are 12 digits with a valid GS1 mod-10 check digit (computed: 7 and 4), so any scanner or GS1 check reads them as GTIN-12s; a GTIN-12 starting with 7 lies in the UPC range administered by GS1 US, and the issuer scope `771` is also a GS1 prefix (GS1 Colombia, 770–771). This rests on my knowledge of the GS1 prefix allocation. The rule that fictional values must not be mistakable for real register entries applies. In addition, only the bench carries `BarcodeSymbologyID` and `IssuerScopeID`; the side frame's number from the same scheme carries neither.
- Condition: The item numbers cannot be read as validly check-digited GTINs of a real GS1 prefix, and both items of the same scheme are described the same way.
- Options: (a, preferred) confirm against the world's identifier rules whether the world item scheme is meant to mimic GTIN; if so, use a GS1 prefix reserved for demonstration or a non-GS1 structure; (b) drop `IssuerScopeID`/`BarcodeSymbologyID` where they have no role in the document.
- Needs decision: yes

### road/04#F8 · Low · Side frame line does not identify the substituted 2026 casting
- XPath: `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:SellersItemIdentification/cbc:ID` = `VI-C180`
- XPath: `02-OrderResponse.xml:/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `2026`
- Why: The order response replaced line 2 by the 2026 casting, identified as VI-C180 with `ExtendedID` 2026 ("An extended identifier for the item that identifies the item with specific properties"). The despatch line repeats the item as ordered (VI-C180 without extension, the ordered description), so the despatch advice does not say which casting was shipped; only the manufacture date 2026-03-20 hints at the new one. The invoice response later relies on the line being the 2026 casting (`16-ApplicationResponse.xml:/ApplicationResponse/cac:DocumentResponse/cac:LineResponse/cac:Response/cbc:Description` = `Matched to the substituted 2026 casting.`).
- Condition: The despatched side frame is identified as the substituted 2026 casting (e.g. `ExtendedID` 2026 and its name), consistent with the order response.
- Options: (a, preferred) carry the substituted item's identification (VI-C180 / 2026) on the despatch line; (b) add a line note naming the 2026 casting.
- Needs decision: no

## Checked and consistent
- `OrderReference` LD-PO-26-0149 resolves to `01-Order.xml`; delivered quantities 96 and 12 equal the ordered quantities; order line references 1 and 2 match.
- Shipment CL-SH-26-0154 with gross 4106.4 kg and consignment LD-CS-26-0152 agree with `03`, `05`, `06`, `08` and `10`.
- "24 pallets of 4 benches" plus one pallet of 12 boxed side frames = 25 handling units and 108 packages, as in the waybill.
- Line 2 lists 12 item instances (serials VI-SF-01490 to VI-SF-01501), one per delivered side frame, all from melt M-26-0412 cast on 2026-03-20 06:40.
- `ReleaseID` XU-EX-REL-55120 is a cargo release after the export declaration `05-ExportCustomsDeclaration.xml` (issued 13:25), consistent with the waybill's instruction to wait for the release.
- Check digits: GLN 9520610900008 and ISIN XU0001042501 pass.

## Considered and refuted
- `/DespatchAdvice/cac:DespatchLine[1]/cac:Item/cac:ItemInstance`: one item instance for 96 benches looked wrong for "A trackable, unique instantiation of this item" — refuted: the instance carries only the lot (`LotIdentification`) and the manufacture date, which is how UBL expresses lot-level traceability.
- `/DespatchAdvice/cac:DespatchLine[2]/cac:Item/cac:ItemInstance[1]/cbc:RegistrationID` = `VI-QR-01490`: three identifiers per casting (trace, registration, serial) looked like filler — refuted: trace ID (QR/RFID trace), registration and serial are distinct concepts, and replacement castings are tracked individually for warranty.
- Pickup 15:05 in the waybill vs actual despatch 16:20 here — refuted: despatch is the moment the truck leaves the warehouse (departure 16:20 in the waybill); loading began at 15:05.
