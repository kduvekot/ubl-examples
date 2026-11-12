# LLM review: 01-Order.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/01-Order.xml`, Git blob `888e6ba193f9e99d9a10149a112547e954b6d115` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2026531 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/01#F1 · High · Emission value is not factor × base
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: UBL defines `ValueFactorNumeric` as "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` as "The base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". With a factor of 0.82 per 1 EA the calculated value is 0.82, not the stated 96 kg CO2e (`ValueMeasure`, "total emissions in kg CO2"). The factor does not fit any quantity in the item either (34 kg steel and 22.5 kg hardwood consumed per bench: 0.82 × 56.5 kg = 46.3 kg, 0.82 × 34 kg = 27.9 kg). The same block occurs in 39 examples across flows (`grep -rl --include='*.xml' 'ValueFactorNumeric>0.82' world/examples | wc -l`).
- Condition: `ValueFactorNumeric` × `ValueBaseMeasure` equals `ValueMeasure` (in consistent units), or the factor and base are absent.
- Options: (a, preferred) give the factor and base the 96 kg are actually calculated from (e.g. kg CO2e per kg of material with the bench's mass as base), so the arithmetic holds; (b) remove `ValueFactorNumeric` and `ValueBaseMeasure` and keep only the total, if no factor is known.
- Needs decision: no

### road/01#F2 · Medium · Language code in LocaleCode
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is defined as "A code signifying the locale in which this language is used"; a locale is a combination of language and region (e.g. en-XB), not a language. The value repeats the ISO 639 language code of `Language/ID` (listID `ISO 639`), so the element carries a language, not a locale, and adds nothing to `Language/ID`. The same pattern occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: `LocaleCode` is either absent or holds a locale (language and region) from a locale list named in its listID, different in meaning from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`, since `Language/ID` already says English and nothing in the document needs the region; (b) give a real locale such as en-XB with a locale list as listID, if the region matters to the party.
- Needs decision: no

### road/01#F3 · Medium · Gate number in AdditionalStreetName of the postal address
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- XPath: `/Order/cac:Delivery/cac:DeliveryAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is not a street name but an entrance of the business park, information that matters only to vehicles delivering goods, and it is carried in Lumeway's postal/registered address in every document. The road flow itself mentions other entrances (`Gate B` as alternative delivery location and `dock 4` in the Order and Waybill), so the gate is a delivery instruction, not part of the address. Counted over `*.xml`: 76 examples (`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: `AdditionalStreetName` holds no gate, dock or entrance; such information, where needed, is in a delivery location or delivery instruction.
- Options: (a, preferred) remove `Gate 3` from the party address and, where the document is about delivery, put the gate in `Delivery/DeliveryLocation` or the delivery instructions; (b) keep it only in a delivery address with a dedicated element such as `Location/Description`.
- Needs decision: no

### road/01#F4 · Medium · Province in Region instead of CountrySubentity
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative subdivision of the country, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located", with `CountrySubentityCode`). The Bayvarran addresses of the same examples do use `CountrySubentity` (`Upland State`), so the two countries' addresses are structured differently for the same kind of information. Counted over `*.xml`: 104 examples carry `<cbc:Region>Province of …` (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: No address of this example holds a province in `Region`; the province is in `CountrySubentity` (and, where a list exists, `CountrySubentityCode`).
- Options: (a, preferred) move the value to `CountrySubentity`, with a code from the Urvanian subdivision list if one exists, like the Bayvarran addresses; (b) keep `Region` only if Urvania's provinces are defined as economic regions rather than administrative divisions, and say so in the world's address rules.
- Needs decision: no

### road/01#F5 · Low · Contacts that do not fit the role
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:Contact/cbc:Department` = `Sales`
- Why: In an Order the buyer's contact is the person who buys; Lumeway's only contact is its `Customer service` desk in `Sales`, i.e. the desk that serves Lumeway's own customers, not the purchasing function that places this order. The despatch party's contact is named `Warehouse office` (the right contact for loading the truck) but carries the job title `Customer service officer` and the department `Sales`, which contradicts its own name.
- Condition: The buyer's contact is a purchasing contact; the despatch party's contact name, job title and department agree with each other and with warehouse work.
- Options: (a, preferred) give Lumeway a purchasing contact for buying roles and Castrano a warehouse job title and department; (b) drop JobTitle/Department where no fitting value is known.
- Needs decision: no

### road/01#F6 · Low · Alternative delivery location names entrances not used elsewhere
- XPath: `/Order/cac:Delivery/cac:AlternativeDeliveryLocation/cbc:Description` = `Gate B of the business park, if dock 4 is blocked.`
- XPath: `/Order/cac:Delivery/cac:DeliveryAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: The delivery address names `Gate 3`, the alternative location "Gate B of the business park, if dock 4 is blocked", and the waybill says "Unload at dock 4; report to the gatehouse first" (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:DeliveryInstructions`). Gate 3, Gate B, dock 4 and the gatehouse are four different points that the documents never relate to each other; a driver cannot tell whether Gate 3 is the normal entrance and Gate B the alternative, or what is alternative to dock 4 (a dock, not a gate).
- Condition: The delivery address, the alternative delivery location and the waybill's delivery instruction describe the same entrances and docks consistently.
- Options: (a, preferred) name the normal entrance and dock once in the delivery location and make the alternative an alternative of the same kind (dock 4 → another dock, or Gate 3 → Gate B); (b) drop the alternative location if the story has no use for it.
- Needs decision: no

### road/01#F7 · Low · Maximum delivery unit of 100 has no role in this order
- XPath: `/Order/cac:Delivery/cac:MaximumDeliveryUnit/cbc:BatchQuantity` = `100`
- XPath: `/Order/cac:Delivery/cac:MinimumDeliveryUnit/cbc:BatchQuantity` = `4`
- XPath: `/Order/cac:Delivery/cbc:Quantity` = `108`
- Why: `BatchQuantity` is "The quantity of ordered Items that constitutes a batch for delivery purposes". The minimum batch of 4 matches the 4 benches per pallet of the despatch (`04-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine[1]/cbc:Note` = `24 pallets of 4 benches: one full truck.`), but a maximum batch of 100 items matches nothing: the order is one delivery of 108 items on 25 pallets (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:TotalTransportHandlingUnitQuantity` = `25`), and the side frames come 12 in one box pallet, not in batches of 4 to 100. No other document refers to the limit (IND5).
- Condition: Every delivery-unit value of the order corresponds to a real constraint used in the despatch, or is absent.
- Options: (a, preferred) remove `MaximumDeliveryUnit`; (b) give it a value that matches a real constraint (e.g. the pallet or truck limit) and state it in the despatch.
- Needs decision: no

### road/01#F8 · Low · Item number looks like a real GTIN-12 with issuer scope 771
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:ID` = `771020000027`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:BarcodeSymbologyID` = `Code128`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:StandardItemIdentification/cbc:IssuerScopeID` = `771`
- Why: The standard item numbers 771020000027 and 771020000034 (scheme `urn:ubl-examples:world:item`) are 12 digits with a valid GS1 mod-10 check digit (computed: 7 and 4), so any scanner or GS1 check reads them as GTIN-12s; a GTIN-12 starting with 7 lies in the UPC range administered by GS1 US, and the issuer scope `771` is also a GS1 prefix (GS1 Colombia, 770–771). This rests on my knowledge of the GS1 prefix allocation. The rule that fictional values must not be mistakable for real register entries applies. In addition, only the bench carries `BarcodeSymbologyID` and `IssuerScopeID`; the side frame's number from the same scheme carries neither.
- Condition: The item numbers cannot be read as validly check-digited GTINs of a real GS1 prefix, and both items of the same scheme are described the same way.
- Options: (a, preferred) confirm against the world's identifier rules whether the world item scheme is meant to mimic GTIN; if so, use a GS1 prefix reserved for demonstration or a non-GS1 structure; (b) drop `IssuerScopeID`/`BarcodeSymbologyID` where they have no role in the document.
- Needs decision: yes

## Checked and consistent
- Line arithmetic: 96 × 49 900 = 4 790 400 and 12 × 5 980 = 71 760; sum 4 862 160 = `LineExtensionAmount` = `TaxableAmount` = `PayableAmount`; `LineCountNumeric` 2 = number of lines.
- `Delivery/Quantity` 108 = 96 + 12 ordered items.
- Requested despatch 2026-03-23 14:00 lies in the requested despatch period 13:00–17:00, and matches the requested pickup in `03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:RequestedPickupTransportEvent/cbc:OccurrenceTime` = `14:00:00`.
- Tax: export from Urvania to Bayvarra, category G at 0 % with exemption reason EXP, consistent with the Incoterm FCA at the seller's 3PL and with `15-Invoice.xml`.
- Check digits: GLN 9520610900008 and ISIN XU0001042501 pass (`check_ids.py`).
- Parties: buyer Lumeway, seller Valdara, despatch party Castrano (Valdara's 3PL, 100 % owned by Valdara), carrier Trasvia: the same identifiers and names as in the other road examples.
- Item material story: steel from Serravona ore in Urvania and slats from Upland State agree with the certificate of origin's remark (`06-CertificateOfOrigin.xml:/CertificateOfOrigin/cac:CertificateOfOriginApplication/cbc:Remarks`).
- Physics: five hardwood slats of 1800 mm with 22.5 kg wood consumed per bench is plausible (about 4.5 kg per slat at roughly 700 kg/m³, own knowledge); 34 kg steel per bench fits two cast side frames of about 10 kg (the side frame's gross weight is 10.2 kg in `05-ExportCustomsDeclaration.xml`) plus rails, anchors and bolts.

## Considered and refuted
- `/Order/cac:Delivery/cbc:MinimumQuantity` = `108`: minimum = maximum = ordered quantity looked like filler — refuted: it states that no partial or excess delivery is accepted, which is a real instruction for one full-truck delivery.
- `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty`: the carrier is named on 2026-03-16 although the transport request to Trasvia is only issued on 2026-03-17 — refuted: under FCA the buyer chooses the carrier, and Lumeway has a framework contract with Trasvia (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:TransportContract/cbc:ID` = `LD-TH-FW-2026`).
- `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`: the en-XB rendering is Italian-sounding, not English — refuted: street and place names are proper names and keep their exonym form in English; the world uses these forms throughout.
- Valdara's address is tagged `en-XB` here but `en-XU` in `02-OrderResponse.xml` — refuted: each document tags English in the issuer's locale (Lumeway issues this order); the content is the same.
- `/Order/cac:BuyerCustomerParty/cac:Party/cbc:IndustryClassificationCode` = `4649` (wholesale of other household goods) for a distributor of park benches — refuted: ISIC 4649 includes the wholesale of furniture, and Lumeway may distribute more than street furniture.
- `/Order/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cac:SellerContact/cbc:Name` = `Key account desk`: SellerContact under a service provider looked misplaced — refuted: the definition is "The contact for the Service Provider", and a key account desk at the 3PL is such a contact.
- Weights: 34 kg steel + 22.5 kg wood consumed per bench (56.5 kg) is more than the 41.5 kg gross per bench of the customs declaration (3984 kg / 96) — refuted: `ConsumptionMeasure` is "The amount of the resource consumed", which includes casting and sawing losses; a finished bench of about 36–38 kg is plausible.
