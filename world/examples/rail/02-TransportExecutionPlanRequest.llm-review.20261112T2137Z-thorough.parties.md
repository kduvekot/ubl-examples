# LLM review: 02-TransportExecutionPlanRequest.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/02-TransportExecutionPlanRequest.xml`, Git blob `52257b380a8d27db0a94e9c2db9b3ccb9b645ca6` (committed)
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

### rail/02#F1 · Medium · Province in Region of four Urvanian addresses
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: Address. Region is "The recognized geographic or economic region or group of countries in which this address is located." A province is a political or administrative division of the country, which UBL puts in Address. Country Subentity ("…such as the name of its county, province, or state"). The Bayvarran consignee's address in the same document uses CountrySubentity (`/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). The value occurs 219 times in 104 example files (`grep -o '<cbc:Region>Province of'` over `*.xml`).
- Condition: no Urvanian address in this example carries the province in cbc:Region; where the province is given, it is in cbc:CountrySubentity.
- Options: (a) move the province to CountrySubentity (preferred: the definition names provinces, and it matches the Bayvarran addresses); (b) drop it where postal zone and city already locate the address.
- Needs decision: no

### rail/02#F2 · Medium · Language code in LocaleCode of the consignee
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:LocaleCode` = `en`
- Why: Language. Locale Code is "A code signifying the locale in which this language is used." `en` (listID ISO 639) is a language code and repeats `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Language/cbc:ID` = `en`; a locale would name language and region (like the `en-XU` the document uses as languageID). No other party of the document carries a LocaleCode. The value occurs 362 times in 213 example files (`grep -o 'LocaleCode listID="ISO 639">en<'` over `*.xml`).
- Condition: the consignee's Language has no LocaleCode, or one that names a locale from a list of locales.
- Options: (a) drop it (preferred: nothing in the request depends on the locale); (b) a locale such as `en-XB` with a locale list (e.g. BCP 47).
- Needs decision: no

### rail/02#F3 · Medium · Gate in AdditionalStreetName of the consignee's postal address
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: Address. Additional Street Name is "An additional street name used to further clarify the address". "Gate 3" is an entrance of the site, not a street name; in the party's business address it only matters to vehicles. In a transport request the gate could matter, but then as part of the delivery place, and the goods go by rail to Lumeway's siding (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:Consignment/cac:MainCarriageShipmentStage/cbc:Instructions` = `Shunt to the Lumeway siding on arrival in Marrowdale.`), not through a road gate.
- Condition: Lumeway's postal address has no gate in AdditionalStreetName.
- Options: (a) remove it from the postal address (preferred); (b) if a gate is needed for the delivery, state it at a delivery location of the consignment.
- Needs decision: no

### rail/02#F4 · Low · "English" renderings of Urvanian addresses and legal forms are Italian
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]` = `Via delle Officine`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cac:Address/cbc:StreetName[2]` = `Via del Magazzino`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cac:Address/cbc:StreetName[2]` = `Via del Terminal`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società urvaniana per azioni (public limited company)`
- XPath: `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- Why: each repeated rendering must be in the language its languageID names (section 5). These renderings are tagged `en-XU` but are Italian (own knowledge), and the Urvanian renderings next to them are different names (e.g. `/TransportExecutionPlanRequest/cac:SenderParty/cac:PostalAddress/cbc:StreetName[1]` = `Bek Stuzman Nulban`), so the Italian text is neither the local name nor English. 63 example files have such an `en-XU` street name (`grep -l -E 'languageID="en-XU">(Via|Viale|Piazza|Valico|Corso|Largo|Strada) '` over `*.xml`).
- Condition: every rendering tagged as English is English, or the world records that English usage keeps Italianate names for Urvanian streets and legal forms and the values are those names.
- Options: (a) record the Italianate English usage in the world's story and keep the values (preferred if intended; it is a world decision); (b) translate into English; (c) tag with the language the text is in, if that language exists in the world.
- Needs decision: yes

### rail/02#F5 · Low · Transport user's contact is the sales order desk
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:Contact/cbc:Department` = `Sales`
- Why: Valdara sends the request as transport user and asks the carrier to "confirm by return" (`/TransportExecutionPlanRequest/cbc:TransportUserRemarks` = `Please confirm by return.`). The carrier's confirmation and questions about collection go to Valdara's shipping or logistics function, not to the order desk that takes customer orders. The carrier's own contact in the same document fits its role (`/TransportExecutionPlanRequest/cac:ReceiverParty/cac:Contact/cbc:Name` = `Freight desk`).
- Condition: the transport user's contact is a shipping, logistics or transport-buying function of Valdara, with matching name, job title and department.
- Options: (a) a shipping/logistics contact for Valdara (preferred); (b) role-specific contacts in Valdara's master data.
- Needs decision: no

### rail/02#F6 · Low · Consignee's contact is its sales customer service
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- Why: Section 5: a consignee's contact receives goods. Lumeway's customer service in Sales serves Lumeway's own customers; the carrier needs the goods-receiving or siding contact (the plan agreed on this request says the consignee unloads: `03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:TransportExecutionTerms/cbc:TransportUserSpecialTerms` = `Delivery within the agreed slot; the consignee unloads.`).
- Condition: the consignee's contact is Lumeway's goods-receiving (warehouse, siding) function.
- Options: (a) a goods-in contact (preferred); (b) role-specific contacts in Lumeway's master data.
- Needs decision: no

### rail/02#F7 · Low · Origin location named after a company
- XPath: `/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Castrano Logistics`
- XPath: `/TransportExecutionPlanRequest/cac:ToLocation/cbc:Name` = `Ferrano Intermodal Hub`
- Why: Section 5: the name of a location is the place, not the company. The origin is Castrano's warehouse, which the waybill calls `08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Pickup/cac:PickupLocation/cbc:Name` = `Castrano Logistics warehouse, Ferrano`; the same place thus has two names in the flow. The destination name is the terminal's name and doubles as the operator's name; acceptable for a terminal, but neither location carries an identifier.
- Condition: the origin location's name names the place (the warehouse) and is the same name the other examples of the flow use for it.
- Options: (a) "Castrano Logistics warehouse, Ferrano" in all examples (preferred); (b) add a location identifier (e.g. a GLN) used wherever the warehouse and the terminal occur.
- Needs decision: no

### rail/02#F8 · Low · Legal-entity master data the transport request does nothing with
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/TransportExecutionPlanRequest/cac:SenderParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `250000000`
- XPath: `/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- Why: Section 4.8: data copied from master data into a document that does not use it. A request for rail transport does nothing with the transport user's stock-exchange listing or with the share capital of the transport user or the consignee.
- Condition: every legal-entity element present has a purpose in the transport request.
- Options: (a) drop SecurityListing and CorporateStockAmount here (preferred); (b) a reduced party description for transport documents.
- Needs decision: no

## Checked and consistent
- Roles: transport user, bill-to party and consignor are Valdara (`XU-R-104274`), transport service provider and receiver Ferrano Rail Cargo (`XU-R-104685`), consignee Lumeway (`20410274`); the same parties hold the same roles in `03-TransportExecutionPlan.xml`, and the freight invoice `10-Invoice.xml` is addressed to Valdara, matching the BillToParty under DAP.
- Valdara, Ferrano Rail Cargo and Lumeway are described identically here and in every other example of the flow that carries their full description (compared value by value).
- ToLocation address is the hub's postal address in `04-TransportProgressStatusRequest.xml` (`Via del Terminal 59`, 4180 Ferrano).
- GLN `9520610900008` and ISIN `XU0001042501`: check digits correct; GS1 prefix 952 is GS1's demonstration range, XU a user-assigned country code.

## Considered and refuted
- `/TransportExecutionPlanRequest/cac:SenderParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`: master data copied into the request — refuted because Castrano Logistics, Valdara's warehousing and despatch provider, is where the carrier collects the goods (`/TransportExecutionPlanRequest/cac:FromLocation/cbc:Name` = `Castrano Logistics`), so the request has a use for it.
- `/TransportExecutionPlanRequest/cac:ReceiverParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`: an international rail freight operator as a small enterprise — refuted because nothing in the flow states staff, turnover or fleet that contradicts it, and small rail freight operators exist; at most a plausibility question for the world's company histories.
- `/TransportExecutionPlanRequest/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedWaypointTransportEvent/cac:Location/cbc:Name` = `Rail border station Urvania–Bayvarra`: location without identifier — refuted because the name is a place name and no other example of the flow identifies the border station with a code.
