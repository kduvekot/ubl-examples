# LLM review: 15-Manifest.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

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

### sea/15#F1 · High · Departure on 15 May against the port's "actual" departure on 14 May
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-15`
- XPath: `13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `18:10:00`
- Why: The manifest and the port's status message describe the departure of the same container on
  the same main carriage. The carrier's manifest has the vessel leave Lumeport on 15 May at 06:00
  (a Friday, the service's sailing day in 08-TransportServiceDescription); the port reports an actual
  departure on 14 May at 18:10. Both cannot be right. The manifest's date is the one that fits the
  schedule and the two-day passage to the 17 May arrival, so the fix probably lies in 13.
- Condition: the departure date and time of the vessel are the same in 13 and 15.
- Options: (a) preferred: keep 15 May 06:00 here and correct 13 (see its review); (b) move the
  sailing to 14 May in 15 and the service description.
- Needs decision: no

### sea/15#F2 · Medium · A cargo manifest that lists no cargo
- XPath: `/Manifest/cbc:ManifestTypeCode` = `CARGO`
- XPath: `/Manifest/cbc:Note` = `One container for Selanu.`
- XPath: `/Manifest/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:ID` = `TWLU4120872`
- Why: A Manifest is "a document listing the contents, cargo, passengers and crew" of a ship, and
  this one is typed as a cargo manifest for the Island Customs Service. It lists the container but no
  goods: no consignment or goods item, no description, package count or bill of lading line for the
  25 pallets of benches and side frames; the bill of lading is referenced only by its ID. Customs at
  Selanu cannot see from it what is arriving.
- Condition: the manifest lists the cargo per bill of lading: consignment or goods item with
  description, number and kind of packages, gross weight, and the container it is in.
- Options: (a) preferred: a consignment for TOL-BL-26-0139 with one goods item (park benches and
  spare side frames, 25 pallets, 4,106.4 kg) in TWLU4120872; (b) at least a goods item per bill.
- Needs decision: no

### sea/15#F3 · Medium · Departure still an estimate ten hours after it was due
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-15`
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceTime` = `06:00:00`
- XPath: `/Manifest/cbc:IssueTime` = `16:08:00`
- Why: EstimatedDepartureTransportEvent "describes an estimated departure". The manifest is issued on
  2026-05-15 at 16:08, ten hours after the estimated departure at 06:00 the same day; by then the
  vessel has either left (the departure is actual) or the estimate is stale. A manifest for the
  authority at the port of arrival is a pre-arrival document whose purpose depends on the actual
  departure and the estimated arrival.
- Condition: at the issue time, the departure is given as actual (if it happened) or as an estimate
  that lies after the issue time.
- Options: (a) preferred: ActualDepartureTransportEvent 2026-05-15 06:00 (if the vessel left), keep
  the estimated arrival; (b) issue the manifest before 06:00.
- Needs decision: no

### sea/15#F4 · Medium · A cargo manifest that lists two of fourteen crew and a passenger
- XPath: `/Manifest/cac:CrewPerson[2]/cbc:RoleCode` = `CHIEFOFFICER`
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cbc:CrewQuantity` = `14`
- XPath: `/Manifest/cac:PassengerPerson/cbc:RoleCode` = `PASSENGER`
- XPath: `/Manifest/cbc:ManifestType` = `Cargo manifest`
- Why: CrewPerson is "a person registred as crew in this manifest" and PassengerPerson "a person
  registred as passenger in this manifest". The manifest is a cargo manifest; it nevertheless lists
  two crew members (master and chief officer) out of a crew of 14 stated on the stage, and one
  passenger. As a crew list it is incomplete; as a cargo manifest the persons have no role, and a
  passenger on a feeder container ship is not explained anywhere.
- Condition: either the manifest is a cargo manifest without persons (the master can stay in the
  stage's MasterPerson), or its type covers crew and passengers and it lists all 14 crew and the
  passenger with a reason for carrying one.
- Options: (a) preferred: drop CrewPerson and PassengerPerson from the cargo manifest and leave crew
  and passengers to the report for the maritime administration (16-CommonTransportationReport);
  (b) a manifest type for cargo, crew and passengers with the complete lists.
- Needs decision: yes (whether the voyage carries a passenger)

### sea/15#F5 · Medium · Gross weight of the shipment without its transport equipment
- XPath: `/Manifest/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/Manifest/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`
- Why: In Shipment, GrossWeightMeasure is "the weight of the goods plus packaging plus transport
  equipment"; the shipment's only container weighs 7,856.4 kg in the same manifest.
- Condition: the shipment's gross weight includes the container, or is absent (the goods' weight then
  goes on the goods item, see F2).
- Options: (a) preferred: 7,856.4 kg, or move 4,106.4 kg to the goods item.
- Needs decision: no

### sea/15#F6 · Medium · A language code in LocaleCode (two places)
- XPath: `/Manifest/cac:SendingLogisticsOperatorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Manifest/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; both are the ISO
  639 language code.
- Condition: absent or a locale.
- Options: (a) preferred: a locale; (b) drop it.
- Needs decision: no

### sea/15#F7 · Low · Port-service requirements in a manifest for customs
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cbc:ShipsRequirements` = `Shore power at the container quay.`
- Why: ShipsRequirements is "information about what services a vessel will require when it arrives
  at a port"; the recipient is the Island Customs Service, which provides no port services. The
  requirement belongs in the report to the port or the maritime administration.
- Condition: the manifest for customs carries no port-service requirements, or the port is among its
  recipients.
- Options: (a) preferred: drop it here.
- Needs decision: no

### sea/15#F8 · Low · The island's customs authority described as a company in the commercial register
- XPath: `/Manifest/cac:AuthorityParty/cac:PartyLegalEntity/cbc:CompanyLiquidationStatusCode` = `ACTIVE`
- XPath: `/Manifest/cac:AuthorityParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:CorporateRegistrationTypeCode` = `COMMERCIAL`
- Why: AuthorityParty is "the Authority or regulator who receives this Manifest"; a customs service
  is neither in the commercial register nor in liquidation or not.
- Condition: no company-only data for the authority.
- Options: (a) preferred: drop its PartyLegalEntity, or describe it as a public body.
- Needs decision: no

### sea/15#F9 · Low · Consignor's and consignee's contacts are sales customer service
- XPath: `/Manifest/cac:ConsignorParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Manifest/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- Why: customs would contact the consignee about the arriving goods (import, goods receiving), not
  its purchasing department with a sales title; the consignor's contact is sales customer service.
- Condition: contacts that fit the roles, or none.
- Options: (a) preferred: import/goods-receiving and shipping contacts.
- Needs decision: no

### sea/15#F10 · Low · Reference to the bill of lading with only an ID
- XPath: `/Manifest/cac:DocumentReference/cbc:ID` = `TOL-BL-26-0139`
- Why: the only link between the manifest and the cargo is an untyped reference.
- Condition: the reference is typed as a bill of lading (and, with F2, tied to the consignment).
- Options: (a) preferred: a type code, or the BL number on the consignment it covers.
- Needs decision: no

### sea/15#F11 · Low · A gate in AdditionalStreetName of the consignor's postal address
- XPath: `/Manifest/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3`
- Why: a gate is not a street.
- Condition: no gate in the postal address.
- Options: (a) preferred: drop it.
- Needs decision: no

## Checked and consistent
- ISO 6346 check digit of TWLU4120872 passes; container, seal TWL-S-0884213, size 42G1, tare
  3,750 kg and gross 7,856.4 kg agree with 14-BillOfLading.
- Vessel Tidewell Harbour (XB-S-20117, QBTH7, MMSI 298702117, journey TH-26-19E) agrees with the bill
  of lading; master Corin Halvard is the same in MasterPerson and CrewPerson[1].
- Estimated arrival 17 May 22:00 fits "two days at sea" (08) from a 15 May departure and the
  availability at Selanu on 18 May 14:00 (14).
- Ports XBLMP → XLSEL; authority and distribution to the Island Customs Service fit a manifest for
  arrival in Lisavu.

## Considered and refuted
- `/Manifest/cbc:AdValoremIndicator`: an explicit false in a manifest — refuted: the element's
  definition is about ad valorem duties on the manifested goods, and saying none are levied is a real
  statement for customs.
- `/Manifest/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cac:TransportEquipmentSeal/cbc:SealingPartyType`:
  a carrier seal applied by the shipper — refuted: carriers issue seals that shippers apply at
  stuffing; that is the usual practice.
