# LLM review: 03-TransportExecutionPlanRequest.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/03-TransportExecutionPlanRequest.xml`, Git blob `fe5bfa14052d31ed395823661598b379931d78e9` (committed)
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

### road/03#F1 · Medium · Province given as Region
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: `Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is the "political or administrative division of a country", i.e. `CountrySubentity`, which the Bayvarran addresses of the same document use (`/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:CountrySubentity` = `Upland State`). 104 examples carry a province in `Region` (`grep -rl '<cbc:Region>Province'` over `*.xml`).
- Condition: the province is in `CountrySubentity`; `Region` is absent or holds a real geographic or economic region.
- Options: (a) move it to `CountrySubentity` (preferred); (b) define Urvanian provinces as non-administrative regions in the world's address rules.
- Needs decision: no

### road/03#F2 · Medium · LocaleCode holds a language code
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (ISO 639) repeats `Language/ID` and names no locale, while the document uses the locale `en-XB` in `languageID`. All 362 `LocaleCode` elements in the examples are `en` with ISO 639 (`grep -rho '<cbc:LocaleCode[^<]*<'` over `*.xml`).
- Condition: `LocaleCode` is absent or holds a locale from a list of locales.
- Options: (a) `en-XB` with a locale list (preferred); (b) drop it.
- Needs decision: no

### road/03#F3 · Low · Contacts that do not fit a transport booking
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- Why: the sender books a truck, so its contact is the one the carrier answers ("Please confirm by return"); Lumeway's customer service in Sales serves Lumeway's customers, not its inbound transport. The consignor's contact is the one the haulier needs at pickup, which happens at Castrano's warehouse (`/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Castrano Logistics`); Valdara's order desk in Sales takes orders and is not at the pickup place.
- Condition: the sender's contact handles transport or purchasing logistics; the consignor's contact (or a contact for the pickup) can be reached about the loading.
- Options: (a) a logistics/transport contact for Lumeway and the warehouse office of Castrano as contact for the pickup, e.g. on the pickup event's location (preferred); (b) drop the job title and department where none fits.
- Needs decision: no

### road/03#F4 · Low · Location names are company names
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Lumeway Distribution`
- Why: `Location/Name` is "The name of this location"; a location's name is the place (e.g. the warehouse or distribution centre), not the company that owns it, which belongs in a party.
- Condition: the location names name places (e.g. "Castrano Logistics warehouse, Ferrano", "Lumeway distribution centre, Marrowdale"), or are absent where the address suffices.
- Options: (a) name the places (preferred: the order already describes the FCA place as "Castrano Logistics warehouse, Ferrano"); (b) drop the names.
- Needs decision: no

### road/03#F5 · Low · Party master data the transport request does nothing with
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyAuthorization/cac:Certificate/cbc:ID` = `XU-HAUL-2020-0877`
- Why: a carrier needs neither the consignor's stock-exchange listing nor its own operating permit sent back to it in a request for transport; both look copied from master data (section 4.8, IND5).
- Condition: every party detail in the request has a use in booking or performing the transport.
- Options: drop both (preferred).
- Needs decision: no

### road/03#F6 · Low · Document note narrates the example instead of informing the carrier
- XPath: `/TransportExecutionPlanRequest/cbc:Note` = `The truck the distributor booked, from the 3PL's warehouse across the border.`
- Why: `Note` is "Free-form text pertinent to this document, conveying information that is not contained explicitly in other structures". The text is written in the third person about the sender ("the distributor booked") and only repeats what the structures say (from Castrano's warehouse, cross-border); it reads as a caption of the example, not as a message from Lumeway to Trasvia.
- Condition: the note is absent, or says something to the carrier that the structures do not.
- Options: (a) drop it (preferred); (b) replace it with information the carrier can use (e.g. the export declaration at pickup).
- Needs decision: no

## Checked and consistent
- Sender = transport user = bill-to (Lumeway), receiver = transport service provider (Trasvia): fits FCA, under which the buyer contracts and pays the main carriage.
- Requested pickup 2026-03-23 14:00 in Ferrano matches the order's requested despatch (`01-Order.xml:/Order/cac:Delivery/cac:Despatch/cbc:RequestedDespatchTime` = `14:00:00`); requested delivery 2026-03-25 10:00 lies in the service end period ending 2026-03-26; the response deadline 2026-03-18 is after the issue date 2026-03-17.
- Original departure country XU and final destination country XB fit the route from Ferrano to Marrowdale.
- `ContainerizedIndicator` false and `GeneralCargoIndicator` true fit palletised benches on a curtain-side trailer; the carrier service instruction fits side loading by forklift.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:MainTransportationService/cbc:TransportServiceCode` = `FTL`: suspected a load type in an element whose definition asks for "the extent of this transportation service (e.g., door-to-door, port-to-port)" — refuted because the world list defines FTL as "One truck for one consignment, from the place of loading to the place of delivery", which states the extent.
- `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsignorParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`: suspected master data — refuted because it explains why the pickup is at Castrano and not at Valdara.
- Consignment without structured goods items or package count: suspected missing information — refuted because the summary description, gross weight, pallet count in text and FTL say what is to be carried, which is what the request depends on.
