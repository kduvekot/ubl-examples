# LLM review: 02-OrderResponse.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/02-OrderResponse.xml`, Git blob `4fa9a01f7c53c819946f93ff994818f91259d67f` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
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

### road/02#F1 · High · The proposed substitute is the old casting the response says is replaced
- XPath: `/OrderResponse/cac:OrderLine[2]/cac:SellerProposedSubstituteLineItem/cac:Item/cbc:Name` = `Bench side frame casting, 2025, from stock`
- XPath: `/OrderResponse/cac:OrderLine[2]/cac:SellerProposedSubstituteLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `2025`
- XPath: `/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Item/cbc:Name` = `Bench side frame casting, 2026`
- XPath: `/OrderResponse/cac:OrderLine[2]/cbc:Note` = `Same fit and price; the old casting is no longer made.`
- XPath: `/OrderResponse/cbc:Note[2]` = `Line 2: the 2025 side frame is replaced by the 2026 casting with a reinforced foot, at the same price.`
- Why: `SellerProposedSubstituteLineItem` is "a line item proposed by the seller describing a product that might substitute for the product described in this order line", and `SellerSubstitutedLineItem` "a line item that has replaced the original order line item". The response puts the 2025 casting, i.e. the item the buyer ordered, as the product the seller proposes as a substitute for itself, and states "from stock" while both notes say the 2025 casting is replaced and no longer made. The proposed substitute and the substituted line say different things about what the buyer will get.
- Condition: line 2 says one thing about what is delivered instead of the ordered casting: the 2026 casting as substituted line item, and no proposed substitute that is the ordered item or contradicts the notes.
- Options: (a) drop `SellerProposedSubstituteLineItem` and keep the substituted 2026 line with the notes (preferred: the substitution is decided, not proposed, as the code `CA` and the notes say); (b) if the seller really offers a choice (2026 casting, or the last 2025 castings from stock), say so in the notes and use the proposed substitute for the alternative that is not the ordered item, without "no longer made" contradicting "from stock".
- Needs decision: no

### road/02#F2 · High · Promised delivery date does not fit the guaranteed despatch
- XPath: `/OrderResponse/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate` = `2026-03-23`
- XPath: `/OrderResponse/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:EndDate` = `2026-03-23`
- XPath: `/OrderResponse/cac:Delivery/cac:Despatch/cbc:GuaranteedDespatchDate` = `2026-03-24`
- XPath: `/OrderResponse/cac:Delivery/cac:Despatch/cac:EstimatedDespatchPeriod/cbc:EndDate` = `2026-03-24`
- Why: `PromisedDeliveryPeriod` is "The period promised for delivery". Under the order's delivery term FCA (`01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FCA`) delivery takes place when the goods are handed to the carrier at the warehouse, i.e. at despatch; the seller promises it for 2026-03-23 only, but guarantees despatch only by 2026-03-24 12:00 and estimates it in a period up to 2026-03-24. Read as delivery at the buyer's address instead, 2026-03-23 is also impossible, because the goods leave on 2026-03-23 afternoon and the waybill expects them on 2026-03-25 (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:EstimatedDeliveryDate` = `2026-03-25`). Under neither reading does the promise fit the despatch dates.
- Condition: the promised delivery period contains the time at which delivery in the sense of the delivery terms can happen given the estimated and guaranteed despatch.
- Options: (a) under FCA, promise delivery for 2026-03-23 to 2026-03-24, matching the estimated despatch period (preferred: the delivery term makes despatch the delivery); (b) promise arrival at Marrowdale (2026-03-25) and say in a note that the period is for arrival.
- Needs decision: no

### road/02#F3 · Medium · ResponsibleParty is the warehouse, not the party that picks up
- XPath: `/OrderResponse/cac:Delivery/cac:Despatch/cac:ResponsibleParty/cac:PartyName/cbc:Name` = `Castrano Logistics`
- Why: UBL defines `Despatch/ResponsibleParty` as "The party who picks up the goods". Castrano Logistics is the seller's warehouse that hands the goods over (the order names it as despatch party, `01-Order.xml:/Order/cac:Delivery/cac:Despatch/cac:DespatchParty/cac:PartyName/cbc:Name` = `Castrano Logistics`); the goods are picked up by the buyer's carrier Trasvia Haulage (`01-Order.xml:/Order/cac:Delivery/cac:Despatch/cac:CarrierParty/cac:PartyName/cbc:Name` = `Trasvia Haulage`).
- Condition: `ResponsibleParty` is absent, or is the party that collects the goods (the carrier); the warehouse, if named, is in `DespatchParty`.
- Options: (a) name Castrano as `DespatchParty` and drop `ResponsibleParty` or make it Trasvia (preferred: both roles are then what UBL means); (b) drop it, since the order already names both.
- Needs decision: no

### road/02#F4 · Medium · Province given as Region
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country", i.e. `CountrySubentity`, which the Bayvarran address in the same document uses for its state. The same occurs in 104 examples (`grep -rl '<cbc:Region>Province'` over `*.xml`).
- Condition: the province is in `CountrySubentity`; `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred); (b) define Urvanian provinces as non-administrative regions in the world's address rules.
- Needs decision: no

### road/02#F5 · Medium · LocaleCode holds a language code
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (ISO 639) repeats `Language/ID` and names no locale (the document itself uses locales such as `en-XU` in `languageID`). All 362 `LocaleCode` elements in the examples are `en` with ISO 639 (`grep -rho '<cbc:LocaleCode[^<]*<'` over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) `en-XB` with a locale list (preferred); (b) drop it.
- Needs decision: no

### road/02#F6 · Low · Buyer's contact is its own customer service in Sales
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: the order response goes to the buyer's purchasing, which has to accept the substitution; Lumeway's customer service in Sales serves Lumeway's own customers.
- Condition: the buyer's contact is a purchasing function, or absent.
- Options: (a) a purchasing contact (preferred); (b) drop it.
- Needs decision: no

### road/02#F7 · Low · Seller's stock-exchange listing in an order response
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- Why: the listing of Valdara's shares plays no part in accepting the order or substituting a line; it looks copied from master data (section 4.8, IND5).
- Condition: the order response carries no `SecurityListing`, or its purpose explains it.
- Options: drop it (preferred).
- Needs decision: no

### road/02#F8 · Low · Line 1 refers to a document by ID only, without a reason
- XPath: `/OrderResponse/cac:OrderLine[1]/cac:DocumentReference/cbc:ID` = `VI-DS-B180`
- Why: line 1 is accepted unchanged (`NoStatus`); the reference to the bench data sheet, which the order already referred to as item specification, carries neither a type nor a description, so the response does nothing with it. For line 2 the reference to the 2026 data sheet has a use (the substituted casting), though it too says nothing about what it is.
- Condition: every document reference in the response has a use in it and says what the referenced document is (type code or description).
- Options: (a) drop the reference on line 1 and add a type or description to the one on line 2 (preferred); (b) keep both with a type.
- Needs decision: no

## Checked and consistent
- `OrderReference` `LD-PO-26-0149` resolves to `01-Order.xml`; buyer and seller are the same parties; the response is issued after the order (2026-03-17 17:42 after 2026-03-16 14:36).
- Quantities 96 and 12 EA match the order lines; the substituted line keeps the ordered price 5980 XUF per EA, as the notes say ("at the same price").
- `OrderResponseCode` `CA` (conditionally accepted) fits an acceptance with one substituted line; line 1 `NoStatus`, line 2 `Revised` with `SubstitutionStatusCode` `Substitution` fit.
- Estimated despatch 2026-03-23 14:00 matches the order's requested despatch.
- `NotifyParty` (Lumeway) is the party to be told of the despatch; it receives the despatch advice (`04-DespatchAdvice.xml`).

## Considered and refuted
- `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`: suspected master data — refuted because Castrano despatches this order, so the seller's logistics provider has a use.
- `/OrderResponse/cac:OrderLine[2]/cac:OrderLineReference/cbc:SalesOrderLineID` = `2` on line 2 only: suspected inconsistent — refuted because the seller's own line ID matters only for the revised line.

## Outside this review
- The downstream documents do not say which casting was shipped: `04-DespatchAdvice.xml` and `15-Invoice.xml` carry `VI-C180` without the `ExtendedID` `2026` this response introduces; that belongs to their reviews.
