# LLM review: 13-TransportationStatus.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/13-TransportationStatus.xml`, Git blob `96261f3aedd684757ce22785ce1d8da29955cd70` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 41ae2a6 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/13#F1 · High · "Actual" departure two hours after the report was issued
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `18:10:00`
- XPath: `/TransportationStatus/cbc:IssueTime` = `16:05:00`
- Why: `ActualDepartureTransportEvent` reports a departure that has happened. The report is issued on 2026-05-14 at 16:05, and the departure it reports as actual is at 18:10 the same day, in the future at issue time. The transport service description scheduled the sailing for 18:00 (`08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:OccurrenceTime` = `18:00:00`), so at 16:05 the departure could at most be estimated. The report's own description is about loading, not departure ("loaded on board").
- Condition: an actual event in the report lies before its issue time; a later departure is reported as estimated or in a later status report.
- Options: report the loading as the actual event and the departure as estimated (`EstimatedDepartureTransportEvent` 18:00 or 18:10) (preferred: matches "loaded on board" at 16:05); or move the issue time after 18:10 and report the departure.
- Needs decision: no

### sea/13#F2 · High · Shipping order ID is the consignment ID and contradicts the bill of lading
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0133`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0133`
- Why: `ShippingOrderID` identifies a shipping order or forwarding instruction. The value is the consignment's ID; the bill of lading names the shipping order as the forwarder's instructions (`14-BillOfLading.xml:/BillOfLading/cbc:ShippingOrderID` = `BF-FI-26-0137`), and the forwarding instructions themselves give yet another value (`12-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0132`). The forwarder receiving this report cannot match it to its shipping order by this field.
- Condition: the shipping order ID, if present, is the one the bill of lading names (`BF-FI-26-0137`).
- Options: `BF-FI-26-0137` (preferred: the report goes to Bayforth, whose shipping order that is); or drop it and identify the consignment only.
- Needs decision: no

### sea/13#F3 · High · Port coordinates put Lumeport 3.2 nautical miles from Selanu, against a two-day passage
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `1.20`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `12.60`
- Why: the container quay of Lumeport is given at 40°1.20′ S 15°12.60′ W. The port of Selanu is at 40°1.20′ S 15°8.40′ W in `17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `8.40` and in `16-CommonTransportationReport.xml`. On one latitude, 4.2′ of longitude at 40° S is 4.2 × cos 40° = 3.2 nautical miles (calculated). The flow sails this as "two days at sea" (`08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:EstimatedDurationPeriod/cbc:DurationMeasure` = `2`); the manifest estimates 64 hours from departure to arrival, and the common transportation report places the ship 120 nautical miles west of Selanu during the passage. The coordinates and the voyage cannot both be right. (The anchorage of Lumeport in `16-CommonTransportationReport.xml` has the same coordinates as this quay.)
- Condition: the coordinates of Lumeport and Selanu are as far apart as the passage the flow describes (or the passage matches the coordinates).
- Options: correct the coordinates to the map's real distance between the two ports (preferred, if the map's scale gives several hundred nautical miles); or shorten the passage everywhere. The answer depends on the world's map and its scale.
- Needs decision: yes

### sea/13#F4 · Medium · Loading reported only in a free-text event, and the container only in text
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Container TWLU4120872 loaded on board.`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/TransportationStatus/cbc:Description` = `Container TWLU4120872 loaded on board.`
- Why: the status the report exists for, the container's loading, is a document-level `TransportEvent` with a date but no time and no event type, its meaning only in its description. UBL has a dedicated element for it in the stage (`LoadingTransportEvent` of the main-carriage shipment stage), and the container itself, the object whose status changes, appears nowhere as transport equipment: its number is only in two free-text descriptions. A receiving system cannot tell when or what was loaded from structured data.
- Condition: the loading is reported with the dedicated loading event (date and time) in the main-carriage stage, and the container is identified as transport equipment (with its ISO 6346 number) in the consignment.
- Options: add a `TransportHandlingUnit/TransportEquipment` with `TWLU4120872` to the consignment and a `LoadingTransportEvent` with time to the main-carriage stage (preferred); or keep the document-level event and give it a type code and time.
- Needs decision: no

### sea/13#F5 · Medium · Document reference holds a consignment ID
- XPath: `/TransportationStatus/cac:DocumentReference/cbc:ID` = `LD-CS-26-0133`
- Why: `DocumentReference` refers to a document; `LD-CS-26-0133` is the consignment's ID (`/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0133`, the same in the packing list and bill of lading), not a document, and it resolves to no example (`flow_index.py sea`: `-> ?`). An identifier of one kind is used as another. If a document is meant, the bill of lading `TOL-BL-26-0139` (issued that morning) is the natural reference, as in `17-TransportationStatus.xml`.
- Condition: the document reference identifies a document (or is absent).
- Options: reference the bill of lading `TOL-BL-26-0139` (preferred: the later status report does the same); or drop the reference.
- Needs decision: no

### sea/13#F6 · Low · Status location named but not identified
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Port of Lumeport`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Port of Lumeport, container quay`
- Why: the status location and the event location are names only, while the same document identifies the port with UN/LOCODE `XBLMP` in the terminal operator's physical location.
- Condition: the status and event locations carry the LOCODE `XBLMP`.
- Options: add `ID` `XBLMP` (preferred).
- Needs decision: no

## Checked and consistent
- Container `TWLU4120872` (in the descriptions) is the container of the packing list, bill of lading and manifest.
- Main-carriage stage ID `2` is the main-carriage stage ID on the bill of lading.
- Direction: by these coordinates Selanu lies east of Lumeport, consistent with direction `EB` (eastbound) and voyage `TH-26-19E` on the bill of lading.
