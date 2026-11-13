# LLM review: 14-CommonTransportationReport.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: logistics

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/14-CommonTransportationReport.xml`, Git blob `081267759b51366ff3d8aad9d0f0d1d2385f1b91` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/14#F1 · Medium · Pre-arrival report without an arrival time or port call
- XPath: `/CommonTransportationReport/cbc:ReportTypeCode` = `PREARRIVAL`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cbc:ID` = `1`
- XPath: `/CommonTransportationReport/cac:TransportMeans/cbc:JourneyID` = `TR-26-09W`
- Why: A pre-arrival report tells the port authority when a ship will arrive and from where. The only shipment stage carries the reporting person, ISPS and health data, but no estimated arrival (no `EstimatedArrivalDate`/`Time`, no transport event of type arrival), no port of arrival (the port appears only as the authority's location) and no last port of call (Selanu appears only in the ISPS free text: "before it left Selanu"). The document's purpose depends on the arrival time; the authority cannot plan the berth, the shore power requested ("Shore power at the container quay.") or the veterinarian the master asks for without it.
- Condition: the report states the expected arrival (date and time) at Lumeport and the port of departure or last port of call, in the stage or transport event where UBL places them.
- Options: (preferred) give the shipment stage (main carriage, sea) the estimated arrival date and time, the loading port Selanu (`XLSEL`) and the discharge port Lumeport (`XBLMP`), and an estimated departure or actual departure date consistent with 13 (on board 2026-03-02).
- Needs decision: no

### cotton/14#F2 · Low · The report cannot be linked to the cotton shipment
- XPath: `/CommonTransportationReport/cac:Shipment/cbc:ID` = `TOL-SH-26-0208`
- XPath: `13-BillOfLading.xml:/BillOfLading/cac:Shipment/cbc:ID` = `SCG-SH-26-0200`
- Why: The report is part of the cotton flow, but nothing in it ties it to the cotton: its shipment `TOL-SH-26-0208` appears in no other example, it lists no cargo, container or bill of lading, and the bill of lading 13 names no vessel. A reader cannot tell that the container `TWLU4123110` (12) is aboard the `Tidewell Reef`. The shipment ID of a vessel-level report may well differ from the cargo shipment; the missing link is the vessel or voyage in the cargo documents, or a cargo reference here.
- Condition: the vessel or voyage of this report is identifiable from the bill of lading (vessel name, journey `TR-26-09W`), or the report refers to the cargo it carries (bill of lading or container).
- Options: (preferred) name the vessel and journey in the main-carriage stage of 13 (see the review of 13); or add a consignment or document reference here.
- Needs decision: no

## Checked and consistent
- ISSC: the ship came under the flag on 2026-01-15; an interim ISSC is valid for six months (ISPS Code A/19.4.4, own knowledge), so 2026-07-14 is the right expiry date.
- Ship Sanitation Control Exemption Certificate issued 2026-01-14 is within its six-month validity (IHR 2005 Art. 39, own knowledge) on 2026-03-03.
- Direction "westbound" and journey `TR-26-09W` agree with Lumeport (15° 12.60′ W) lying west of Selanu (15° 8.40′ W, 12).
- MMSI `298702231` uses MID 298 and call sign `QBTR4` the Q series, both recorded as unallocated by ITU (`world/codelists/sources/PROVENANCE-second-round.md`); `XBLMP` uses the user-assigned code XB.
- Reporter and sender Tidewell Ocean Lines is the carrier of 13; gross tonnage 7480 and net tonnage 3910 (52 %) are plausible for a feeder container ship.
- The ISPS note that the ship left Selanu after the fence gap of 1 March agrees with the bill of lading's on-board date 2026-03-02 (13).

## Considered and refuted
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:ValidISSCIndicator` = `false` while an interim certificate is on board: suspected contradiction with the absence reason — refuted because the indicator concerns the full ISSC, and `ISSCAbsenceReason` ("the reason if not having a … ISSC") is exactly the place to explain that only an interim one is held.

## Outside this review
- Location: the Port of Selanu (40° 1.20′ S, 15° 8.40′ W, 12) and the Port of Lumeport (40° 1.20′ S, 15° 12.60′ W, here) lie on the same latitude 4.2′ of longitude apart, i.e. 4.2 × 1.852 km × cos 40.02° ≈ 6.0 km. A sea voyage between an island and the mainland of another country over 6 km, with a pre-arrival report the day after loading, is a question for the map and the cross-flow review.
