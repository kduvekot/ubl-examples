# LLM review: 15-Manifest.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/15-Manifest.xml`, Git blob `4caf72d7f9decfbb65355d2cdfb4c4e93fc08906` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit fe38caa 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/15#F1 · High · Departure still an estimate ten hours after it was due, and a day after the port's "actual" departure
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-15`
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceTime` = `06:00:00`
- XPath: `/Manifest/cbc:IssueDate` = `2026-05-15`
- XPath: `/Manifest/cbc:IssueTime` = `16:08:00`
- XPath: `13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `18:10:00`
- Why: `EstimatedDepartureTransportEvent` describes an estimated departure. Issued on 2026-05-15 at 16:08, the manifest gives as an estimate a departure ten hours in its own past; by then the vessel has left (the departure is actual) or the estimate is stale. The port reports the actual departure of the same container and voyage on 2026-05-14 at 18:10, twelve hours earlier. The two examples contradict each other (High). Which time is the story is open: the transport service description schedules the sailing for 2026-05-14 18:00 but gives Friday (2026-05-15, recomputed) as the weekly sailing day (`08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:ScheduledServiceFrequency/cbc:WeekDayCode` = `5`); 15 May 06:00 fits the 64-hour passage to the 17 May 22:00 arrival (broad and logistics prefer 14 May 18:10 as actual; context prefers 15 May and correcting 13).
- Condition: the vessel's departure has one date and time in 08, 13, 15 and 16, and at the manifest's issue time it is given as actual if it has happened (an estimate only if it lies after the issue time).
- Options: (a) preferred: `ActualDepartureTransportEvent` with the departure the flow settles on, correcting 13 or 08 accordingly; (b) issue the manifest before the departure, with the estimate.
- Needs decision: yes (which departure time is the story: 14 May 18:10 or 15 May 06:00)
- From: broad (F1), logistics (F1), context (F1, F3)

### sea/15#F2 · High · Shipment gross weight smaller than the gross weight of its own container
- XPath: `/Manifest/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/Manifest/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". The shipment's only container weighs 7,856.4 kg in the same manifest (recomputed 4,106.4 + tare 3,750); the shipment cannot weigh less than its container (contradiction within the document, as in 10 and 14).
- Condition: the shipment's gross weight includes the container, or the goods' weight is carried by a goods item (F3).
- Options: (a) preferred: goods weight on the goods item and 7,856.4 kg or nothing on the shipment; (b) 7,856.4 kg.
- Needs decision: no
- From: logistics (F3, Medium), context (F5, Medium)

### sea/15#F3 · Medium · A cargo manifest that does not list the cargo
- XPath: `/Manifest/cbc:ManifestTypeCode` = `CARGO`
- XPath: `/Manifest/cbc:Note` = `One container for Selanu.`
- XPath: `/Manifest/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:ID` = `TWLU4120872`
- XPath: `/Manifest/cac:DocumentReference/cbc:ID` = `TOL-BL-26-0139`
- Why: a Manifest is "A document listing the contents, cargo, passengers and crew" of a ship; this one is a cargo manifest for the Island Customs Service. It gives the container, its weight and seal and the bill of lading number, but no consignment or goods item: no description, number or kind of packages, marks or commodity code. Customs at Selanu cannot tell what the container holds; the bill of lading has the goods ("Park benches and spare side frames", 25 pallets, `14-BillOfLading.xml`). Information the document's purpose depends on is missing.
- Condition: the manifest lists the cargo per bill of lading: consignment with its bill of lading, description, packages and gross weight, linked to the container.
- Options: (a) preferred: a consignment `LD-CS-26-0133` for `TOL-BL-26-0139` with a goods item (benches and frames, 25 pallets, 4,106.4 kg) in `TWLU4120872`; (b) at least a goods item per bill.
- Needs decision: no
- From: broad (F2), logistics (F2), context (F2)

### sea/15#F4 · Medium · Language code in LocaleCode
- XPath: `/Manifest/cac:SendingLogisticsOperatorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Manifest/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (listID `ISO 639`) repeats the language. 362 occurrences in 213 examples.
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: drop it; (b) a locale such as `en-XB`.
- Needs decision: no
- From: broad (F3), parties (F1), context (F6)

### sea/15#F5 · Medium · A gate in AdditionalStreetName of the consignor's postal address
- XPath: `/Manifest/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: "An additional street name used to further clarify the address"; a gate is not a street, and a postal address has no use for it. 79 occurrences in 76 examples.
- Condition: no street element of the postal address holds a gate.
- Options: (a) preferred: drop it.
- Needs decision: no
- From: broad (F4), parties (F3), context (F11, Low)

### sea/15#F6 · Medium · The Island Customs Service described as a company in a commercial register, with a liquidation status
- XPath: `/Manifest/cac:AuthorityParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Manifest/cac:AuthorityParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- XPath: `/Manifest/cac:AuthorityParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Island companies register`
- Why: the customs authority of Lisavu (ISIC `8411`) is placed in the island companies register as a commercial registration and given a liquidation status; a public body is neither. Medium, as in `11-ExportCustomsDeclaration.xml` and all earlier flows.
- Condition: no commercial registration or liquidation status for the authority (a public-body register, only the registration name, or no legal entity).
- Options: (a) preferred: keep `RegistrationName`, drop the liquidation status and the commercial scheme; (b) drop `PartyLegalEntity`.
- Needs decision: no
- From: parties (F2, Medium), broad (F6, Low), context (F8, Low)

### sea/15#F7 · Low · A cargo manifest that lists two of fourteen crew and a passenger
- XPath: `/Manifest/cac:CrewPerson[1]/cbc:RoleCode` = `MASTER`
- XPath: `/Manifest/cac:CrewPerson[2]/cbc:RoleCode` = `CHIEFOFFICER`
- XPath: `/Manifest/cac:PassengerPerson/cbc:RoleCode` = `PASSENGER`
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cbc:CrewQuantity` = `14`
- XPath: `/Manifest/cbc:ManifestType` = `Cargo manifest`
- Why: `CrewPerson` is "A person registred as crew in this manifest". The cargo manifest lists the master and the chief officer of a crew of 14 and one passenger; the ship's report for the same voyage also names the chief engineer (`16-CommonTransportationReport.xml:/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:CrewMemberPerson[3]/cbc:FamilyName` = `Dunmore`), who is missing here. As a crew list it is incomplete; as a cargo manifest the persons have no role. A passenger on a feeder is possible (broad), but not explained anywhere.
- Condition: either a cargo manifest without persons (the master may stay as `MasterPerson`), or a manifest type that covers crew and passengers with complete lists consistent with `CrewQuantity` and 16.
- Options: (a) preferred: drop `CrewPerson` and `PassengerPerson`, leaving crew and passengers to `16-CommonTransportationReport.xml`; (b) a combined manifest with the full lists.
- Needs decision: yes (what the manifest covers, and whether the voyage carries a passenger)
- From: broad (F5), logistics (F4), parties (F6), context (F4, Medium)

### sea/15#F8 · Low · Port-service requirements and ballast data in a manifest for customs
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cbc:ShipsRequirements` = `Shore power at the container quay.`
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cbc:SegregatedBallastMeasure` = `2480`
- Why: `ShipsRequirements` is "Information about what services a vessel will require when it arrives at a port"; the recipient is customs, which provides no port services, and segregated ballast belongs to port-state reporting. The values are the bill of lading's and look copied from the vessel's master data.
- Condition: the manifest for customs carries the vessel data that identify vessel and voyage, or the port is among its recipients.
- Options: (a) preferred: drop both.
- Needs decision: no
- From: broad (F7), context (F7)

### sea/15#F9 · Low · The authority's contact is reachable on weekdays only; the ship arrives on a Sunday night
- XPath: `/Manifest/cac:AuthorityParty/cac:Contact/cbc:Name` = `Import office`
- XPath: `/Manifest/cac:AuthorityParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceDate` = `2026-05-17`
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedArrivalTransportEvent/cbc:OccurrenceTime` = `22:00:00`
- Why: the manifest is lodged for the arrival at Selanu, estimated for Sunday 2026-05-17 (recomputed) at 22:00; the authority's only contact is its import office "Weekdays 08:00–17:00". The checklist asks that an authority's contact be reachable when ships or goods arrive.
- Condition: the receiving authority's contact can be used at the estimated arrival time.
- Options: (a) preferred: the customs service's port or duty office at Selanu with arrival-time availability; (b) drop the restricting note if the office is reachable.
- Needs decision: no
- From: parties (F5)

### sea/15#F10 · Low · Contacts whose function does not fit the role
- XPath: `/Manifest/cac:ConsignorParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/Manifest/cac:ConsignorParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Manifest/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Manifest/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Manifest/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/Manifest/cac:SendingLogisticsOperatorParty/cac:Contact/cbc:Name` = `Bookings`
- Why: customs reaches the consignor through Sales' customer service and the consignee through "Purchasing" with a seller's title and department; the carrier's contact toward customs is its bookings desk rather than documentation or the ship's agent.
- Condition: contacts with agreeing name, title and department that fit the role toward customs, or none.
- Options: (a) preferred: shipping contact for the consignor, import or goods-receiving contact for the consignee, documentation contact for the carrier.
- Needs decision: no
- From: broad (F9), parties (F7, F8), context (F9)

### sea/15#F11 · Low · Reference to the bill of lading with only an ID
- XPath: `/Manifest/cac:DocumentReference/cbc:ID` = `TOL-BL-26-0139`
- Why: the only link between the manifest and the cargo is an untyped document-level reference (it resolves to `14-BillOfLading.xml`).
- Condition: the reference is typed as a bill of lading and, with F3, tied to the consignment it covers.
- Options: (a) preferred: the bill of lading number on the consignment, or a type code.
- Needs decision: no
- From: context (F10)

### sea/15#F12 · Low · Port of registry named but not identified
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cac:RegistryPortLocation/cbc:Name` = `Lumeport`
- Why: name only, while the document identifies Lumeport as `XBLMP` (last exit port).
- Condition: the registry port carries `XBLMP`.
- Options: (a) preferred: add `ID` `XBLMP`.
- Needs decision: no
- From: logistics (F5)

### sea/15#F13 · Low · Lisavu addresses (Velumi, Island Customs Service) tagged as Bayvarran English
- XPath: `/Manifest/cac:ConsigneeParty/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`
- XPath: `/Manifest/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Manifest/cac:ConsigneeParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Manifest/cac:AuthorityParty/cac:PostalAddress/cbc:StreetName[2]` = `Wharf Road`
- XPath: `/Manifest/cac:AuthorityParty/cac:PostalAddress/cbc:CityName[2]` = `Port Wrenfield`
- XPath: `/Manifest/cac:AuthorityParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]` = `Port Wrenfield`
- Why: tagged `en-XB` here (issued by Tidewell), `en-XL` in the Lisavu-issued documents (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName[2]` = `Reef Street`; `19-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:CustomsParty/cac:PostalAddress/cbc:StreetName[2]` = `Wharf Road`); the tag follows the issuer, a convention no document records.
- Condition: the same `languageID` in every example, or the issuer rule recorded.
- Options: (a) preferred: `en-XL` everywhere; (b) record the rule.
- Needs decision: yes (one rule for the world)
- From: broad (F10), parties (F4, address part)

### sea/15#F14 · Low · Velumi's legal form given once, in English, without its Lisavan form
- XPath: `/Manifest/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- Why: the order gives it in Lisavan and English (`05-Order.xml:/Order/cac:BuyerCustomerParty/cac:Party/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`); here only the English, untagged.
- Condition: the same renderings in every example.
- Options: (a) preferred: both renderings, tagged.
- Needs decision: no
- From: parties (F4, legal-form part; split by the merge)

### sea/15#F15 · Low · Registration date 1996-01-01 shared with unrelated companies
- XPath: `/Manifest/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Velumi's date is the New Year's Day 1996 given to 271 registrations in 181 examples, while Lumeway (`1988-10-03`) and Tidewell (`1974-03-01`) have their own; a default value, not a fact of the world.
- Condition: own date, or absent.
- Options: (a) preferred: own date; (b) leave the element out.
- Needs decision: yes
- From: parties (F9)

### sea/15#F16 · Low · Party master data the manifest does nothing with
- XPath: `/Manifest/cac:SendingLogisticsOperatorParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/Manifest/cac:ConsignorParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `2500000`
- XPath: `/Manifest/cac:SendingLogisticsOperatorParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/Manifest/cac:ConsignorParty/cac:PartyTaxScheme/cbc:CompanyID` = `UL-1230822`
- Why: share capital and state sales-tax registrations play no role in a cargo manifest to customs; they look copied from master data (section 4.8). The customs-trader numbers of consignor and consignee are left out: customs may use them. Not raised by any part; added by the merge, as in the earlier flows.
- Condition: the parties carry only what the manifest uses.
- Options: (a) preferred: drop them.
- Needs decision: no
- From: merge

### sea/15#F17 · Low · A signature with an ID and the signatory only
- XPath: `/Manifest/cac:Signature/cbc:ID` = `TWL-SIG-MF`
- Why: no method, date, attachment or signing person; the ID is formed from the document type. Not raised by any part; added by the merge, as in 09–14.
- Condition: a signature, where present, says how, when and by whom the manifest was signed.
- Options: (a) preferred: complete it or drop it.
- Needs decision: yes (whether the world's documents are signed at all)
- From: merge

## Checked and consistent
- Vessel (`XB-S-20117`, Tidewell Harbour, call sign `QBTH7`, MMSI `298702117`, tonnages, feeder configuration, registry certificate `REG-XB-S-20117`) and voyage `TH-26-19E` agree with `14-BillOfLading.xml`. MMSI MID 298: `world/codelists/sources/PROVENANCE-second-round.md` records that the ITU MID table re-read on 2026-11-11 lists none of 280–299, so the number cannot be mistaken for a real ship (verified by the merge).
- Container `TWLU4120872` 42G1 (valid ISO 6346 check digit), gross 7,856.4 kg = 4,106.4 + tare 3,750, seal `TWL-S-0884213`, last exit port `XBLMP` and first arrival port `XLSEL` agree with the bill of lading; `TOL-BL-26-0139` resolves.
- Passage: estimated 2026-05-15 06:00 to 2026-05-17 22:00 = 64 hours (recomputed), about the "two days at sea" of 08; the actual arrival on 2026-05-18 06:30 (`17-TransportationStatus.xml`) shows the estimate missed.
- Master Corin Halvard is `MasterPerson` and first `CrewPerson`, and the passenger Ines Tavari the same as in 16; issuer and signatory Tidewell; authority and distribution the Island Customs Service at the port of first arrival.
- GLN check digit correct (`check_ids.py`, from broad).

## Considered and refuted
- `/Manifest/cac:PassengerPerson/cbc:FamilyName` = `Tavari`: a passenger on a container feeder — refuted: feeders may carry a few passengers or supernumeraries, and the definition covers passengers (from broad; the open question is kept in F7).
- `/Manifest/cbc:Note` = `One container for Selanu.` on a 1,000 TEU feeder — refuted: a manifest can be filed per bill of lading or per consignment for a port (from broad).
- `/Manifest/cbc:AdValoremIndicator` = `false` — refuted: the definition concerns ad valorem duties on the manifested goods; saying none are levied is a real statement for customs (from context).
- `/Manifest/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:TransportEquipmentSeal/cbc:SealingPartyType`: a carrier seal applied by the shipper — refuted: usual practice (from context).

## Refuted in the merge
### broad/F8 · Low · Distribution to the authority the manifest is addressed to
- XPath: `/Manifest/cac:DocumentDistribution/cac:Party/cac:PartyName/cbc:Name` = `Island Customs Service`
- Why (broad): the distribution names the Island Customs Service, already the manifest's `AuthorityParty`, for this very document. Condition: distribution names parties other than the addressee, or is absent.
- Refuted because: `AuthorityParty` ("The Authority or regulator who receives this Manifest") names the role; the distribution list says to whom and how (`ELECTRONIC`) the document is sent, and its definition does not exclude the main addressee. The context part checked the distribution as fitting; same reasoning as in 09 and 12.

## Changed in the merge
- broad/F1, logistics/F1, context/F1 (High) and context/F3 (Medium, stale estimate) → F1: grouped; needs decision set to yes because the parts disagree on which departure time is right and 08 gives both a 14 May sailing and a Friday frequency.
- logistics/F3, context/F5 (Medium) → F2: High, because the same document states the container's gross weight (as in 10 and 14).
- parties/F2 (Medium), broad/F6, context/F8 (Low) → F6: Medium, aligned with all earlier flows.
- broad/F5, logistics/F4 (Low, no), parties/F6 (Low, yes), context/F4 (Medium, yes) → F7: Low, needs decision yes; Medium not kept: the persons are incomplete or superfluous, not a misuse of the elements.
- context/F11 (Low) → F5: Medium, aligned.
- parties/F4 → F13 and F14 (split); broad/F10 (no) aligned to yes.
- LocaleCode: preferred option set to drop.
- F16, F17 added by the merge.

## Outside this review
- Timeline across documents: the crossing takes from 2026-05-14 18:10 (`13-TransportationStatus.xml`) to 2026-05-18 06:30 (`17-TransportationStatus.xml`), three and a half days, while the service is announced with "two days at sea" (`08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:EstimatedDurationPeriod/cbc:DurationMeasure` = `2`); with this manifest's 15 May 06:00 it is 3 days and half an hour (from broad).
- Map scale: Lumeport and Selanu 3.2 nautical miles apart by their coordinates in 13 and 16/17, against this 64-hour passage (see `13-TransportationStatus.xml` and the review of 16).
