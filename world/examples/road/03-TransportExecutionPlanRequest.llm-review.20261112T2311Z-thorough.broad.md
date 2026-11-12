# LLM review: 03-TransportExecutionPlanRequest.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/03-TransportExecutionPlanRequest.xml`, Git blob `fe5bfa14052d31ed395823661598b379931d78e9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b8faf2 2026-11-12 Reviews of the utilities and road flows: files written so far
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with `list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly different things, and a finding that appears in only one review counts as much as one that appears in all. Every finding below, and every entry under "Considered and refuted" and "Outside this review", is looked into and ends either resolved (its condition holds) or dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### road/03#F1 · Medium · Language code in LocaleCode
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is defined as "A code signifying the locale in which this language is used"; a locale is a combination of language and region (e.g. en-XB), not a language. The value repeats the ISO 639 language code of `Language/ID` (listID `ISO 639`), so the element carries a language, not a locale, and adds nothing to `Language/ID`. The same pattern occurs in 213 examples (`grep -rl --include='*.xml' 'LocaleCode listID="ISO 639"' world/examples | wc -l`).
- Condition: `LocaleCode` is either absent or holds a locale (language and region) from a locale list named in its listID, different in meaning from `Language/ID`.
- Options: (a, preferred) remove `LocaleCode`, since `Language/ID` already says English and nothing in the document needs the region; (b) give a real locale such as en-XB with a locale list as listID, if the region matters to the party.
- Needs decision: no

### road/03#F2 · Medium · Gate number in AdditionalStreetName of the postal address
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address (may be repeated only to provide the same content in multiple natural languages)". `Gate 3` is not a street name but an entrance of the business park, information that matters only to vehicles delivering goods, and it is carried in Lumeway's postal/registered address in every document. The road flow itself mentions other entrances (`Gate B` as alternative delivery location and `dock 4` in the Order and Waybill), so the gate is a delivery instruction, not part of the address. Counted over `*.xml`: 76 examples (`grep -rl --include='*.xml' '<cbc:AdditionalStreetName>Gate 3' world/examples | wc -l`).
- Condition: `AdditionalStreetName` holds no gate, dock or entrance; such information, where needed, is in a delivery location or delivery instruction.
- Options: (a, preferred) remove `Gate 3` from the party address and, where the document is about delivery, put the gate in `Delivery/DeliveryLocation` or the delivery instructions; (b) keep it only in a delivery address with a dedicated element such as `Location/Description`.
- Needs decision: no

### road/03#F3 · Medium · Province in Region instead of CountrySubentity
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located". A province is an administrative subdivision of the country, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located", with `CountrySubentityCode`). The Bayvarran addresses of the same examples do use `CountrySubentity` (`Upland State`), so the two countries' addresses are structured differently for the same kind of information. Counted over `*.xml`: 104 examples carry `<cbc:Region>Province of …` (`grep -rl --include='*.xml' '<cbc:Region>Province of' world/examples | wc -l`).
- Condition: No address of this example holds a province in `Region`; the province is in `CountrySubentity` (and, where a list exists, `CountrySubentityCode`).
- Options: (a, preferred) move the value to `CountrySubentity`, with a code from the Urvanian subdivision list if one exists, like the Bayvarran addresses; (b) keep `Region` only if Urvania's provinces are defined as economic regions rather than administrative divisions, and say so in the world's address rules.
- Needs decision: no

### road/03#F4 · Low · Transport user contact is the customer service desk
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: The sender of a transport request is the transport user; its contact should be the person who books and follows the transport (logistics or purchasing). Lumeway's only contact is its `Customer service` desk in `Sales`.
- Condition: The sender's contact is a logistics or purchasing contact.
- Options: (a, preferred) give Lumeway a logistics contact for transport roles; (b) omit JobTitle/Department.
- Needs decision: no

### road/03#F5 · Low · Locations named after the companies, not the places
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Lumeway Distribution`
- Why: `FromLocation`/`ToLocation` are locations; their `Name` should name the place (the warehouse in Ferrano, the distribution centre in Marrowdale), not the company that operates it. `Castrano Logistics` and `Lumeway Distribution` are party names; the parties are already given as consignor/consignee and service provider/user.
- Condition: The location names name places (e.g. `Castrano warehouse, Ferrano`), or are absent and the address identifies the place.
- Options: (a, preferred) name the place (warehouse, distribution centre) and keep the company in the party roles; (b) drop `Name` and keep the address.
- Needs decision: no

### road/03#F6 · Low · Consignor carried with its full master data and its sales contact
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: A transport request needs the consignor's identity and a contact for loading. Valdara is carried with its stock-exchange listing, corporate stock and its 3PL service relation, none of which the carrier uses (data copied from master data, section 4.8). Its contact is the `Order desk` in `Sales`, while the goods are loaded at Castrano's warehouse, whose `Warehouse office` is the loading contact in the order (`01-Order.xml:/Order/cac:Delivery/cac:Despatch/cac:Contact/cbc:Name` = `Warehouse office`).
- Condition: The consignor is described with what the carrier needs (identity, address, a contact for the loading), without listing, capital or service-provider data.
- Options: (a, preferred) reduce the consignor to identification, name, address and the loading contact; (b) keep Valdara's contact but add the warehouse contact at the from-location.
- Needs decision: no

## Checked and consistent
- Requested pickup 2026-03-23 14:00 at Ferrano and delivery 2026-03-25 10:00 at Marrowdale lie inside the service period (2026-03-23 to 2026-03-26) and match the order's requested despatch and the waybill's required delivery (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cbc:RequiredDeliveryTime` = `10:00:00`).
- Consignment ID LD-CS-26-0152, gross weight 4106.4 kg and 25 pallets agree with `04-DespatchAdvice.xml`, `05-ExportCustomsDeclaration.xml` and `08-Waybill.xml` (24 pallets of 4 benches plus one pallet of 12 boxed side frames).
- Response deadline 2026-03-18 after the issue date 2026-03-17; `TransportUserRemarks` asks for a confirmation, consistent with it.
- Roles: Lumeway is sender, transport user and bill-to party, consistent with FCA (the buyer pays the main carriage); Trasvia is receiver and service provider.
- UN/LOCODEs XUFER (Ferrano) and XBMRW (Marrowdale) are the same as in the waybill.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:Consignment/cbc:SummaryDescription` = `Park benches and spare side frames on 25 pallets.`: the number of pallets is given only as text — refuted: the request says what is to be carried (description, gross weight, number of pallets), which is what its purpose needs; a structured count would be an addition, not a fix.
- `/TransportExecutionPlanRequest/cac:BillToParty`: bill-to equal to the transport user looked redundant — refuted: the definition names the party to be billed, and stating it is meaningful when the framework contract could bill another party.
