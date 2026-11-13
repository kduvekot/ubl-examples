# LLM review: 15-Manifest.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/15-Manifest.xml`, Git blob `4caf72d7f9decfbb65355d2cdfb4c4e93fc08906` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5339b0e 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/15#F1 · High · Estimated departure after the actual departure, and already past at issue
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-15`
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceTime` = `06:00:00`
- XPath: `/Manifest/cbc:IssueTime` = `16:08:00`
- Why: the manifest, issued on 2026-05-15 at 16:08, estimates the departure for 2026-05-15 06:00, ten hours before its own issue, while the port reports the actual departure of the same container and voyage on 2026-05-14 at 18:10 (`13-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `18:10:00`), in line with the scheduled sailing on 2026-05-14 at 18:00 (`08-TransportServiceDescription.xml`). An estimate that is stale at issue and contradicts the reported departure by twelve hours.
- Condition: the manifest's departure agrees with the departure the flow reports (2026-05-14 18:10, as actual), and an estimated event lies after the issue time.
- Options: report the departure as actual 2026-05-14 18:10 (preferred: the manifest is issued at sea, after departure); or, if the manifest is meant as a pre-departure manifest, issue it before 2026-05-14 18:00 with the estimated departure.
- Needs decision: no

### sea/15#F2 · Medium · Cargo manifest without the cargo
- XPath: `/Manifest/cbc:ManifestTypeCode` = `CARGO`
- XPath: `/Manifest/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/Manifest/cac:DocumentReference/cbc:ID` = `TOL-BL-26-0139`
- Why: a Manifest is "A document listing the contents, cargo, passengers and crew" of a ship; this one is typed as a cargo manifest for the island's customs. It names the container and a gross weight, but no goods item: no description of the goods, no number or kind of packages, no consignment with its bill of lading number, marks or HS codes. The bill of lading is referenced only as a plain document reference at document level, not tied to the container or consignment. Customs at Selanu cannot see from the manifest what the container holds.
- Condition: the manifest lists the cargo: per consignment its bill of lading, description, packages and gross weight, linked to the container.
- Options: add a consignment `LD-CS-26-0133` with the bill of lading reference and a goods item (benches and frames, 25 pallets, 4,106.4 kg) in container `TWLU4120872` (preferred); or at least a goods item with description and packages.
- Needs decision: no

### sea/15#F3 · Medium · Shipment gross weight excludes the transport equipment its definition includes
- XPath: `/Manifest/cac:Shipment/cbc:GrossWeightMeasure` = `4106.4`
- XPath: `/Manifest/cac:Shipment/cac:TransportHandlingUnit/cac:TransportEquipment/cbc:GrossWeightMeasure` = `7856.4`
- Why: `Shipment/GrossWeightMeasure` is "The total gross weight of a shipment; the weight of the goods plus packaging plus transport equipment". The document's own container weighs 7,856.4 kg gross (4,106.4 + tare 3,750), so the shipment under the definition weighs 7,856.4 kg.
- Condition: the shipment's gross weight includes the transport equipment, or the goods weight is carried by a goods item (see F2).
- Options: goods weight on the goods item and 7,856.4 kg or nothing on the shipment (preferred).
- Needs decision: no

### sea/15#F4 · Low · Crew of 14, two listed
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cbc:CrewQuantity` = `14`
- XPath: `/Manifest/cac:CrewPerson[1]/cbc:RoleCode` = `MASTER`
- XPath: `/Manifest/cac:CrewPerson[2]/cbc:RoleCode` = `CHIEFOFFICER`
- Why: a manifest lists "passengers and crew"; the stage says 14 crew, the manifest lists two of them (master and chief officer) and a passenger. Either the manifest is a cargo manifest and the persons do not belong in it (then the crew list is for the common transportation report), or it lists the crew and then all 14.
- Condition: the persons listed agree with the crew count, or the manifest lists no persons and leaves crew and passengers to the report meant for them.
- Options: drop crew and passenger persons from the cargo manifest and keep the master in the shipment stage (preferred: the type is "Cargo manifest"); or list all 14 crew.
- Needs decision: no

### sea/15#F5 · Low · Port of registry named but not identified
- XPath: `/Manifest/cac:Shipment/cac:ShipmentStage/cac:TransportMeans/cac:MaritimeTransport/cac:RegistryPortLocation/cbc:Name` = `Lumeport`
- Why: the same document identifies Lumeport as UN/LOCODE `XBLMP` (last exit port), the registry port only by name.
- Condition: the registry port carries `XBLMP`.
- Options: add `ID` `XBLMP` (preferred).
- Needs decision: no

## Checked and consistent
- Vessel data (ID `XB-S-20117`, name, call sign `QBTH7`, MMSI `298702117`, gross tonnage 9,940, net tonnage 5,120, segregated ballast 2,480 t, feeder configuration, registry certificate `REG-XB-S-20117`) and voyage `TH-26-19E` eastbound are the same as in `14-BillOfLading.xml`.
- Container `TWLU4120872` `42G1`, gross 7,856.4 kg, tare 3,750 kg and seal `TWL-S-0884213` are the same as on the bill of lading; the reference `TOL-BL-26-0139` resolves to it.
- Ports: last exit `XBLMP`, first arrival `XLSEL`, as on the bill of lading.
- Passage: estimated 2026-05-15 06:00 to 2026-05-17 22:00 is 64 hours, about "two days at sea" as in `08-TransportServiceDescription.xml` (the distance question is a finding in the reviews of 08 and 13).
- Master `Corin Halvard` is the first crew person with role `MASTER`.
