# LLM review: 09-GoodsItemItinerary.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/09-GoodsItemItinerary.xml`, Git blob `3dfd231396ba484476d5dfeef7a1accb9a1e27f9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### rail/09#F1 · Medium · Province in Region of sender and receiver
- XPath: `/GoodsItemItinerary/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Address. Region is "The recognized geographic or economic region or group of countries in which this address is located." A province is a political or administrative division of the country, which UBL puts in Address. Country Subentity ("…such as the name of its county, province, or state"); the flow's Bayvarran addresses do so (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). The value occurs 219 times in 104 example files (`grep -o '<cbc:Region>Province of'` over `*.xml`).
- Condition: no address in this example carries the province in cbc:Region; where given, it is in cbc:CountrySubentity.
- Options: (a) move it to CountrySubentity (preferred); (b) drop it.
- Needs decision: no

### rail/09#F2 · Low · "English" renderings of the addresses and legal forms are Italian
- XPath: `/GoodsItemItinerary/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/GoodsItemItinerary/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- Why: each repeated rendering must be in the language its languageID names (section 5). These are tagged `en-XU` but are Italian (own knowledge); the Urvanian renderings are different names. 63 example files have such an `en-XU` street name (`grep -l -E 'languageID="en-XU">(Via|Viale|Piazza|Valico|Corso|Largo|Strada) '` over `*.xml`).
- Condition: every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms.
- Options: (a) record the Italianate English usage in the world's story and keep the values (preferred if intended); (b) translate into English; (c) tag with the language the text is in.
- Needs decision: yes

### rail/09#F3 · Low · Receiver's contact is the sales order desk
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- Why: Valdara receives the itinerary of its two containers as transport user; it is used by whoever follows the shipment (shipping or logistics), not by the order desk that takes customer orders.
- Condition: the receiver's contact is Valdara's shipping or logistics function.
- Options: (a) a shipping/logistics contact (preferred); (b) role-specific contacts in Valdara's master data.
- Needs decision: no

### rail/09#F4 · Low · Master data the itinerary does nothing with
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/GoodsItemItinerary/cac:ReceiverParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- Why: Section 4.8: an itinerary does nothing with the receiver's stock-exchange listing or share capital. Valdara's warehousing provider is not a subcontracted provider of the transport service the itinerary describes (the only segment is the container train of Ferrano Rail Cargo), and no element of the itinerary refers to it.
- Condition: every legal-entity and service-provider element present has a purpose in the itinerary.
- Options: (a) drop them here (preferred); (b) a reduced party description for transport documents.
- Needs decision: no

## Checked and consistent
- Sender, signatory and transport service provider of the segment are Ferrano Rail Cargo (`XU-R-104685`), receiver Valdara (`XU-R-104274`): the same parties as in the plan the itinerary refers to (`03-TransportExecutionPlan.xml`), with identical full descriptions.
- ISIN `XU0001042501` and container `FRXU1044175`: check digits correct.
