# LLM review: 15-Manifest.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/15-Manifest.xml`, Git blob `4caf72d7f9decfbb65355d2cdfb4c4e93fc08906` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit c9983d2 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/15#F1 · High · Estimated departure after the actual departure, and already past when the manifest is issued
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-15`
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceTime` = `06:00:00`
- XPath: `/Manifest/cbc:IssueDate` = `2026-05-15`
- XPath: `/Manifest/cbc:IssueTime` = `16:08:00`
- Why: the manifest estimates the departure of voyage `TH-26-19E` from Lumeport for 2026-05-15 06:00. The port reported the actual departure of the same vessel and container on 2026-05-14 at 18:10 (`13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `18:10:00`). Issued on 2026-05-15 at 16:08, the manifest also gives as an estimate a time ten hours in its own past. It contradicts the status report and is stale.
- Condition: the manifest states the departure as it happened (actual, 2026-05-14 18:10), or an estimate that is in the future of its issue time and agrees with the other documents.
- Options: (a) preferred: `ActualDepartureTransportEvent` 2026-05-14 18:10; (b) none better seen.
- Needs decision: no

### sea/15#F2 · Medium · A cargo manifest that does not list the cargo
- XPath: `/Manifest/cbc:ManifestTypeCode` = `CARGO`
- XPath: `/Manifest/cbc:Note` = `One container for Selanu.`
- XPath: `/Manifest/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:ID` = `TWLU4120872`
- Why: the manifest is "A document listing the contents, cargo, passengers and crew" of the ship; this one is a cargo manifest for the import customs at Selanu. It gives the container, its weight and seal and the bill of lading number, but no goods: no description, no number of packages, no commodity code, no consignment. Customs cannot tell from it what the container holds; the bill of lading it references has the goods ("Park benches and spare side frames", 25 pallets, `14-BillOfLading.xml`).
- Condition: the cargo manifest lists, per bill of lading, the goods (description, packages, gross weight) and the container they are in, consistent with the bill of lading.
- Options: (a) preferred: a consignment for `TOL-BL-26-0139` with its goods item(s), package count and weight; (b) none better seen.
- Needs decision: no

### sea/15#F3 · Medium · Language code in LocaleCode
- XPath: `/Manifest/cac:SendingLogisticsOperatorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Manifest/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats the language. 213 of 250 examples carry `LocaleCode`.
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: `en-XB` from a locale list; (b) drop it.
- Needs decision: no

### sea/15#F4 · Medium · A gate in AdditionalStreetName
- XPath: `/Manifest/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: `AdditionalStreetName` is "An additional street name used to further clarify the address"; a gate is not a street name and does not belong in a postal address. Same value in 25 of 29 sea examples.
- Condition: no street-name element of the postal address holds a gate.
- Options: (a) preferred: drop it from the postal address.
- Needs decision: no

### sea/15#F5 · Low · Crew of 14, two crew listed
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cbc:CrewQuantity` = `14`
- XPath: `/Manifest/cac:CrewPerson[2]/cbc:RoleCode` = `CHIEFOFFICER`
- Why: the manifest lists crew (`CrewPerson`) and passengers, as its definition allows, but only the master and the chief officer of a crew of 14; a crew list that is meant to be complete lists all. As a cargo manifest (`ManifestTypeCode` `CARGO`) it has no need of a crew or passenger list at all.
- Condition: either the manifest is a cargo manifest without crew and passenger lists (the crew number may stay), or its crew list has all 14 persons.
- Options: (a) preferred: drop `CrewPerson` and `PassengerPerson` from the cargo manifest (the master stays in the stage); (b) list the whole crew and change the manifest type.
- Needs decision: no

### sea/15#F6 · Low · Customs authority described as a company in the commercial register
- XPath: `/Manifest/cac:AuthorityParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/Manifest/cac:AuthorityParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- Why: the Island Customs Service is a public authority; it is not registered in the island companies register as a commercial entity and has no liquidation status (section 5).
- Condition: the authority's legal entity carries no commercial registration or liquidation status (or no legal entity at all).
- Options: (a) preferred: drop `PartyLegalEntity` (or keep only the registration name).
- Needs decision: no

### sea/15#F7 · Low · Ship data for the port in a manifest to customs
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cbc:ShipsRequirements` = `Shore power at the container quay.`
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cbc:SegregatedBallastMeasure` = `2480`
- Why: `ShipsRequirements` is "Information about what services a vessel will require when it arrives at a port", addressed to the port, and segregated ballast belongs to port-state reporting; the customs authority does nothing with either in a cargo manifest. The values are the same as in the bill of lading and look copied from the vessel's master data.
- Condition: the manifest carries the vessel data that identify vessel and voyage, not the port's service requests.
- Options: (a) preferred: drop both.
- Needs decision: no

### sea/15#F8 · Low · Distribution to the authority the manifest is addressed to
- XPath: `/Manifest/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Island Customs Service`
- Why: the distribution list names the Island Customs Service, which is already the manifest's `AuthorityParty`, for this very document; it names no further interested party.
- Condition: document distribution names parties other than the addressee, or is absent.
- Options: (a) preferred: drop it; (b) name a real copy recipient (e.g. the Port of Selanu).
- Needs decision: no

### sea/15#F9 · Low · Contacts whose function does not fit
- XPath: `/Manifest/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Manifest/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Manifest/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Manifest/cac:SendingLogisticsOperatorParty/cac:Contact/cbc:Name` = `Bookings`
- Why: the consignor is reached through Sales' customer service, the consignee through purchasing with a seller's job title; for a manifest to customs the carrier's contact is its bookings desk rather than the function answering customs queries (documentation or the ship's agent).
- Condition: each contact's name, job title and department agree with each other and fit the party's role toward customs.
- Options: (a) preferred: shipping contact for the consignor, goods-in or customs contact for the consignee, documentation contact for the carrier.
- Needs decision: no

### sea/15#F10 · Low · Lisavu addresses tagged as Bayvarran English
- XPath: `/Manifest/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- XPath: `/Manifest/cac:AuthorityParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB`
- Why: English renderings of Lisavu addresses are tagged `en-XL` in the documents Velumi sends (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`); across the flow the tag follows the sender's country (for Velumi 16 × `en-XB`, 8 × `en-XL`).
- Condition: the same address carries the same `languageID` in every example.
- Options: (a) preferred: `en-XL` for English renderings of Lisavu addresses everywhere.
- Needs decision: no

## Checked and consistent
- Vessel, voyage, call sign, MMSI, tonnages, flag and registry agree with the bill of lading (`14-BillOfLading.xml`); the master listed as crew is the stage's `MasterPerson`.
- Container `TWLU4120872` (valid check digit), size type 42G1, gross 7,856.4 kg = 4,106.4 kg + tare 3,750 kg, seal `TWL-S-0884213`, last exit port Lumeport and first arrival port Selanu agree with the bill of lading; the document reference `TOL-BL-26-0139` resolves.
- Estimated arrival 2026-05-17 22:00 precedes the actual arrival reported later (`17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualArrivalTransportEvent/cbc:OccurrenceTime`, 2026-05-18 06:30): an estimate, plausibly missed.
- GLN check digit correct (`check_ids.py`).

## Considered and refuted
- `/Manifest/cac:PassengerPerson/cbc:FamilyName` = `Tavari`: a passenger on a container feeder — refuted because feeders may carry a few passengers or supernumeraries; the manifest's definition covers passengers.
- `/Manifest/cbc:Note` = `One container for Selanu.` on a 1,000 TEU feeder — refuted because a manifest can be filed per bill of lading or per carrier's cargo for a port; nothing says the ship carries nothing else.

## Outside this review
- Timeline across documents: the crossing takes from 2026-05-14 18:10 (`13-TransportationStatus.xml`) to 2026-05-18 06:30 (`17-TransportationStatus.xml`), three and a half days, while the service is announced with "two days at sea" (`08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:EstimatedDurationPeriod/cbc:DurationMeasure` = `2`).
