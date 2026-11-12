# LLM review: 02-OrderResponse.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/02-OrderResponse.xml`, Git blob `4fa9a01f7c53c819946f93ff994818f91259d67f` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2026531 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/02#F1 · Medium · Province in Region instead of CountrySubentity
- XPath: `/OrderResponse/cac:SellerSupplierParty/cac:Party/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative subdivision of the country, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located", with `CountrySubentityCode`). The Bayvarran addresses of the same examples do use `CountrySubentity` (`Upland State`), so the two countries' addresses are structured differently for the same kind of information. Counted over `*.xml`: 104 examples carry `<cbc:Region>Province of …` (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: No address of this example holds a province in `Region`; the province is in `CountrySubentity` (and, where a list exists, `CountrySubentityCode`).
- Options: (a, preferred) move the value to `CountrySubentity`, with a code from the Urvanian subdivision list if one exists, like the Bayvarran addresses; (b) keep `Region` only if Urvania's provinces are defined as economic regions rather than administrative divisions, and say so in the world's address rules.
- Needs decision: no

### road/02#F2 · Medium · Language code in LocaleCode
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is defined as "A code signifying the locale in which this language is used"; a locale is a combination of language and region (e.g. en-XB), not a language. The value repeats the ISO 639 language code of `Language/ID` (listID `ISO 639`), so the element carries a language, not a locale, and adds nothing to `Language/ID`. The same pattern occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: `LocaleCode` is either absent or holds a locale (language and region) from a locale list named in its listID, different in meaning from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`, since `Language/ID` already says English and nothing in the document needs the region; (b) give a real locale such as en-XB with a locale list as listID, if the region matters to the party.
- Needs decision: no

### road/02#F3 · Medium · Gate number in AdditionalStreetName of the postal address
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is not a street name but an entrance of the business park, information that matters only to vehicles delivering goods, and it is carried in Lumeway's postal/registered address in every document. The road flow itself mentions other entrances (`Gate B` as alternative delivery location and `dock 4` in the Order and Waybill), so the gate is a delivery instruction, not part of the address. Counted over `*.xml`: 76 examples (`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: `AdditionalStreetName` holds no gate, dock or entrance; such information, where needed, is in a delivery location or delivery instruction.
- Options: (a, preferred) remove `Gate 3` from the party address and, where the document is about delivery, put the gate in `Delivery/DeliveryLocation` or the delivery instructions; (b) keep it only in a delivery address with a dedicated element such as `Location/Description`.
- Needs decision: no

### road/02#F4 · Medium · Promised delivery on 23 March but despatch guaranteed only by 24 March noon
- XPath: `/OrderResponse/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:StartDate` = `2026-03-23`
- XPath: `/OrderResponse/cac:Delivery/cac:PromisedDeliveryPeriod/cbc:EndDate` = `2026-03-23`
- XPath: `/OrderResponse/cac:Delivery/cac:Despatch/cbc:GuaranteedDespatchDate` = `2026-03-24`
- XPath: `/OrderResponse/cac:Delivery/cac:Despatch/cbc:GuaranteedDespatchTime` = `12:00:00`
- XPath: `/OrderResponse/cac:Delivery/cac:Despatch/cac:EstimatedDespatchPeriod/cbc:EndDate` = `2026-03-24`
- Why: `PromisedDeliveryPeriod` is "The period promised for delivery"; under FCA at the 3PL's warehouse (`01-Order.xml:/Order/cac:DeliveryTerms/cbc:ID` = `FCA`) delivery takes place when the goods are loaded on the buyer's truck, i.e. at despatch. The seller promises delivery on 23 March only, yet guarantees despatch ("The date guaranteed for the despatch (pickup)") only by 24 March 12:00 and estimates despatch over 23–24 March. A delivery promise that ends before the guaranteed despatch deadline cannot both be kept if the seller uses its guarantee; the two commitments contradict each other. Partly mitigated: "guaranteed" can be read as an outer limit and "promised" as a target, so this is kept as Medium.
- Condition: The promised delivery period, the estimated despatch period and the guaranteed despatch date and time are mutually consistent (the guaranteed despatch is no later than the end of the promised delivery period under FCA).
- Options: (a, preferred) end the promised delivery period on 24 March, or guarantee despatch by the end of 23 March, whichever the story intends; (b) drop the guarantee if only the estimate matters.
- Needs decision: no

### road/02#F5 · Low · Buyer contact is the customer service desk
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/OrderResponse/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: The buyer's contact in an order response is the person who placed the order and must accept the substitution; Lumeway's only contact is its `Customer service` desk in `Sales`, which serves Lumeway's own customers.
- Condition: The buyer's contact is a purchasing contact.
- Options: (a, preferred) give Lumeway a purchasing contact for buying roles; (b) omit JobTitle/Department.
- Needs decision: no

### road/02#F6 · Low · Line document references do not say what they refer to
- XPath: `/OrderResponse/cac:OrderLine[1]/cac:DocumentReference/cbc:ID` = `VI-DS-B180`
- XPath: `/OrderResponse/cac:OrderLine[2]/cac:DocumentReference/cbc:ID` = `VI-DS-C180-2026`
- Why: `OrderLine/DocumentReference` is "A reference to a document associated with this order line" and carries only an ID. In the order the same ID VI-DS-B180 is an item specification (`01-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Item/cac:ItemSpecificationDocumentReference/cbc:ID` = `VI-DS-B180`); here a generic reference without `DocumentTypeCode` or `DocumentType` leaves the recipient to guess that VI-DS-C180-2026 is the data sheet of the new casting.
- Condition: Each line document reference states what kind of document it is (type code or type text), or uses the item's `ItemSpecificationDocumentReference`.
- Options: (a, preferred) add `DocumentTypeCode`/`DocumentType` (data sheet); (b) move the reference into the line item's `ItemSpecificationDocumentReference`.
- Needs decision: no

### road/02#F7 · Low · Proposed substitute is the old 2025 casting that the note says is no longer made
- XPath: `/OrderResponse/cac:OrderLine[2]/cac:SellerProposedSubstituteLineItem/cac:Item/cbc:Name` = `Bench side frame casting, 2025, from stock`
- XPath: `/OrderResponse/cac:OrderLine[2]/cac:SellerProposedSubstituteLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `2025`
- XPath: `/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Item/cac:SellersItemIdentification/cbc:ExtendedID` = `2026`
- XPath: `/OrderResponse/cbc:Note[2]` = `Line 2: the 2025 side frame is replaced by the 2026 casting with a reinforced foot, at the same price.`
- XPath: `/OrderResponse/cac:OrderLine[2]/cbc:Note` = `Same fit and price; the old casting is no longer made.`
- Why: `SellerProposedSubstituteLineItem` is "a line item proposed by the seller describing a product that might substitute for the product described in this order line", and `SellerSubstitutedLineItem` is "a line item that has replaced the original order line item". The response contains both: the 2026 casting as the item that has replaced the line, and the 2025 casting "from stock" as a proposed substitute. The notes speak only of the replacement ("the 2025 side frame is replaced by the 2026 casting", "the old casting is no longer made"); they never offer the 2025 stock as an option for the buyer. If the ordered item was the 2025 casting, a proposed substitute equal to the ordered item makes no sense; if the 2025 stock is a real alternative, the notes should say so. The later documents treat the 2026 casting as delivered (`16-ApplicationResponse.xml:/ApplicationResponse/cac:DocumentResponse/cac:LineResponse/cac:Response/cbc:Description` = `Matched to the substituted 2026 casting.`).
- Condition: Each substitution element of line 2 has a stated business role: the replacing item is in `SellerSubstitutedLineItem`, and a proposed substitute is present only if the seller really offers a different alternative, explained in a note.
- Options: (a, preferred) remove `SellerProposedSubstituteLineItem`, keeping the 2026 casting as the substituted item; (b) keep it and say in the line note that the buyer may choose the remaining 2025 stock instead.
- Needs decision: yes

## Checked and consistent
- `/OrderResponse/cac:OrderReference/cbc:ID` = `LD-PO-26-0149` resolves to `01-Order.xml`; parties and line quantities (96, 12) and the price of the substituted casting (5 980, same as ordered) agree with the order.
- Estimated despatch 2026-03-23 14:00 matches the order's requested despatch and the transport request's requested pickup.
- `OrderResponseCode` CA (conditionally accepted, UN/EDIFACT 4343) fits a response that substitutes a line and needs the buyer's agreement; the line statuses (NoStatus, Revised) and `SubstitutionStatusCode` Substitution match the lines.
- `ResponsibleParty` ("The party who picks up the goods") is Castrano, which hands the goods over at its warehouse; `NotifyParty` is the buyer.

## Considered and refuted
- `/OrderResponse/cac:OrderLine[1]/cac:OrderLineReference/cbc:UUID` = `da67b26b-2501-5b9b-9b6f-d03d5ce50a97`: the order lines in 01 have no UUID, so the UUID looked like a dangling reference — refuted: the definition is "A universally unique identifier for this order line reference", i.e. of the reference itself, not of the order line.
- `/OrderResponse/cac:OrderLine[2]/cac:OrderLineReference/cbc:SalesOrderLineID` = `2` only on line 2 — refuted: the seller assigns its own line number where it changes the line; nothing requires it on unchanged lines.

## Outside this review
- The transport request `03-TransportExecutionPlanRequest.xml` is issued on 2026-03-17 at 14:16, before this order response (17:42): the buyer books transport before the seller has confirmed. A timeline question across documents, plausible under a framework contract.
