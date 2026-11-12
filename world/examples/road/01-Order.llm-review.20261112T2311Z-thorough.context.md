# LLM review: 01-Order.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/01-Order.xml`, Git blob `888e6ba193f9e99d9a10149a112547e954b6d115` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### road/01#F1 · High · Lifecycle stage code says manufacturing only, its text says cradle to gate
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageCode` = `MANUFACTURING`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:LifecycleStageDescription` = `From the ore at the mine to the bench leaving the factory gate.`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:Description` = `Mining, steel making, casting, galvanising, sawing and the transport between them.`
- Why: `LifecycleStageCode` is "A code indicating the lifecycle stage to which this emission applies" and `LifecycleStageDescription` is "The lifecycle stage to which this emission applies, expressed as a text", so both must name the same stage. In the world list `LifecycleStageCode`, `MANUFACTURING` is "Making the product (EN 15804 module A3)", while raw material supply and its transport (A1, A2) is `SOURCING`. The text and the emission's description include mining, steel making and the transport between the steps, i.e. A1 to A3 (cradle to gate, as the boundary code next to it also says). The code and its text equivalent contradict each other.
- Condition: the lifecycle stage code and the lifecycle stage text name the same stage(s), and the emission figure covers exactly what they name.
- Options: (a) keep the cradle-to-gate figure and describe the stage in text only, or with a code that covers A1 to A3 if the world list gets one (preferred: the figure is a cradle-to-gate figure); (b) keep `MANUFACTURING` and reduce the figure, text and description to module A3.
- Needs decision: no

### road/01#F2 · Medium · FullnessIndicationCode carries the emission system boundary
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cac:EmissionCalculationMethod/cbc:FullnessIndicationCode` = `CRADLETOGATE`
- Why: UBL 2.5 defines `EmissionCalculationMethod/FullnessIndicationCode` as "A code signifying whether a piece of transport equipment is full, partially full, or empty. This indication is used as a parameter when calculating the emission". The value is a code of the world list `EmissionBoundaryCode` (cradle to gate), which says how much of a product's life the figure covers; it says nothing about the load of transport equipment. This is a code from a list meant for another concept in an element with a precise definition (semantic conformance, UBL 2.5 §4.7). Counted over `*.xml` with `grep -rl 'FullnessIndicationCode listID="urn:ubl-examples:world:codelist:EmissionBoundaryCode"'`, 39 examples do the same; the other uses of the element take `LoadTypeCode`, which fits the definition.
- Condition: `FullnessIndicationCode` is absent from this emission, or holds a code that says how full transport equipment is; the system boundary, if kept, is stated where UBL allows it (e.g. in text).
- Options: (a) drop the element here and state the boundary in `LifecycleStageDescription` or `Description` (preferred: an item's cradle-to-gate figure has no transport equipment); (b) record the missing boundary element as a finding for the UBL TC.
- Needs decision: no

### road/01#F3 · Medium · Emission factor and base do not give the stated emission
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueMeasure` = `96`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueFactorNumeric` = `0.82`
- XPath: `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:EnvironmentalEmission/cbc:ValueBaseMeasure` = `1`
- Why: `ValueFactorNumeric` is "A numeric factor used to calculate the value measurement (e.g., emissions per unit of activity)" and `ValueBaseMeasure` "The base quantity to which the value factor applies (e.g., per km, per kg, per unit produced)". With a base of 1 EA the factor says 0.82 (kg CO2e) per bench, but the value for this item (one bench) is 96 kg; 96 / 0.82 = 117.1 benches, which matches nothing in the order (96 and 12 ordered). The factor as written cannot have produced the value, so it is data that does nothing, or the wrong figure.
- Condition: `ValueFactorNumeric` × the activity quantity in the unit of `ValueBaseMeasure` gives `ValueMeasure`, or the factor and base are absent.
- Options: (a) drop factor and base, since the value is a per-item figure taken from the LCA (preferred: nothing in the order needs the factor); (b) state a factor and base whose product is 96 kg per bench (e.g. per kg of steel and wood, with the activity quantity derivable from the item).
- Needs decision: no

### road/01#F4 · Medium · Maximum delivery unit smaller than the delivery it belongs to
- XPath: `/Order/cac:Delivery/cac:MaximumDeliveryUnit/cbc:BatchQuantity` = `100`
- XPath: `/Order/cac:Delivery/cbc:Quantity` = `108`
- XPath: `/Order/cac:Delivery/cbc:MinimumQuantity` = `108`
- XPath: `/Order/cac:Delivery/cbc:MaximumQuantity` = `108`
- Why: `MaximumDeliveryUnit` is "The maximum delivery unit for this delivery" and its `BatchQuantity` "The quantity of ordered Items that constitutes a batch for delivery purposes". The same delivery is to carry exactly 108 items (quantity, minimum and maximum all 108), so a maximum batch of 100 items for this delivery cannot be met; nothing in the order says that the delivery is split into batches, and the despatch advice delivers in one despatch.
- Condition: the maximum delivery unit of the delivery is at least the quantity the delivery is to carry, or the order says how the delivery is split.
- Options: (a) drop `MaximumDeliveryUnit` (preferred: the order has no reason for a maximum batch); (b) raise it to at least 108; (c) split the delivery and say so.
- Needs decision: no

### road/01#F5 · Medium · Province given as Region in Urvanian addresses
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is "The political or administrative division of a country ... such as the name of its county, province, or state", i.e. `CountrySubentity`, which the Bayvarran address in the same document uses for its state (`/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). Counted over `*.xml` with `grep -rl '<cbc:Region>Province'`, 104 examples carry a province in `Region`.
- Condition: the Urvanian province is in `CountrySubentity` (with `CountrySubentityCode` if the world has one), and `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred: the element the definition names, as for Bayvarra); (b) if Urvanian provinces are meant as non-administrative regions, say so in the world's address rules and use a name that is not "Province".
- Needs decision: no

### road/01#F6 · Medium · LocaleCode holds a language code
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; a locale is a language in a region (e.g. English as used in Bayvarra, `en-XB`, which this very document uses as `languageID` for the English renderings). `en` with `listID` ISO 639 repeats `Language/ID` = `en` and says nothing about the locale. Counted over `*.xml` with `grep -rho '<cbc:LocaleCode[^<]*<'`, all 362 `LocaleCode` elements in the examples are `en` with ISO 639.
- Condition: `LocaleCode` is absent or holds a locale (language and region) from a list of locales.
- Options: (a) `en-XB` with a locale list (BCP 47 / CLDR style) as listID (preferred: matches the `languageID` already used); (b) drop it.
- Needs decision: no

### road/01#F7 · Low · Contacts that do not fit the party's role in the order
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:Contact/cbc:Name` = `Warehouse office`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:Contact/cbc:Department` = `Sales`
- Why: the buyer's contact in a purchase order is the one who buys (purchasing), but the order names Lumeway's customer service in Sales, which serves Lumeway's own customers. The despatch party's contact is named "Warehouse office" (fitting the despatch) but has the job title and department of a sales customer service officer, so name, job title and department disagree.
- Condition: the buyer's contact is a purchasing function; the despatch party's contact has a name, job title and department that agree and fit the despatch.
- Options: (a) a purchasing contact for the buyer and a warehouse/despatch job title and department for Castrano (preferred); (b) drop the job title and department where no fitting one exists.
- Needs decision: no

### road/01#F8 · Low · Party master data the order does nothing with
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:PartyLegalEntity/cac:ShareholderParty/cbc:ParticipationPercent` = `100`
- XPath: `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- Why: the order asks the seller to supply benches. The seller's stock-exchange listing, the despatch party's shareholder and the carrier's road haulage operating permit play no part in ordering, despatch instructions or delivery terms; they look copied from the parties' master data (section 4.8, IND5).
- Condition: every party detail in the order has a use in ordering, despatching or delivering the goods, or the order's purpose explains it.
- Options: (a) drop these aggregates from the order (preferred); (b) keep the carrier permit only if the order makes the permit a condition of carriage (it does not now).
- Needs decision: no

## Checked and consistent
- Delivery quantity 108 = line 1 (96) + line 2 (12); both lines in EA, both multiples of the minimum delivery unit of 4.
- `FCA` at the Castrano warehouse in Ferrano fits the despatch address and despatch party (Castrano, c/o for Valdara), the buyer-appointed carrier and the despatch instruction to have the export declaration ready (export clearance is the seller's under FCA, own knowledge of Incoterms 2020).
- Requested despatch date and time (2026-03-23 14:00) lie inside the requested despatch period (2026-03-23 13:00–17:00), after the issue date 2026-03-16.
- Tax category `G` with exemption reason export from Urvania fits goods leaving Urvania for Bayvarra under FCA.
- The alternative delivery location's "dock 4" matches the waybill's delivery instruction (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cbc:DeliveryInstructions` = `Unload at dock 4; report to the gatehouse first.`).
- The commodity codes (HS 940179 / national 94017910 for the bench, 732599 / 73259990 for the cast side frame) fit the item descriptions.

## Considered and refuted
- `/Order/cac:Delivery/cbc:MinimumQuantity` / `cbc:MaximumQuantity` = 108, equal to the quantity: suspected filler — refuted because equal minimum and maximum state that neither short nor over-delivery is accepted, a real ordering condition (the flow later deals with a short delivery).
- `/Order/cac:Delivery/cac:Despatch/cac:CarrierParty`: suspected premature, since the transport request is issued a day later (`03-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cbc:IssueDate` = `2026-03-17`) — refuted because under FCA the buyer appoints the carrier and may name its haulier before booking.
- `/Order/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty`: suspected master data — refuted because Castrano is the party that despatches under this order (despatch party, FCA place), so naming the seller's logistics provider has a use here.
- `/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:AdditionalItemProperty[4]/cbc:ImportanceCode` = `OPTIONAL` for the frame colour: suspected wrong for an ordered colour — refuted because the importance code describes the property for describing the item, and the colour is also fixed by `SellersItemIdentification/ExtendedID`.
