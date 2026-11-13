# LLM review: 14-CommonTransportationReport.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: context

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### cotton/14#F1 · Medium · A pre-arrival report without an arrival time or a port of arrival
- XPath: `/CommonTransportationReport/cbc:ReportTypeCode` = `PREARRIVAL`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cbc:ID` = `1`
- Why: The report is a pre-arrival report to the Port of Lumeport, but no element gives the expected
  time of arrival: the shipment stage has no estimated arrival (or any transport event), no load or
  discharge port and no last port of call; the only dates in the document are its issue date, the
  parties' registration dates, the ISSC expiry and the issue date of the sanitation exemption
  certificate. The port learns that the ship is coming, not when. A pre-arrival report's purpose
  depends on the arrival time (it is what the notification periods of the ISPS Code and the IHR run
  from; own knowledge).
- Condition: the report states the estimated arrival date and time at Lumeport and the port the ship
  comes from (Selanu).
- Options: (a, preferred) add to the shipment stage an EstimatedArrivalTransportEvent (or the
  stage's estimated arrival date and time) at the Port of Lumeport, and the loading port Selanu, in
  line with the B/L 13 and the map's sea route.
- Needs decision: no

### cotton/14#F2 · Low · "No valid ISSC" while the ship sails with a valid interim certificate
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:ValidISSCIndicator` = `false`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:ISSCAbsenceReason` = `The ship came under Bayvarra's flag on 15 January 2026 and sails with an interim certificate (ISPS Code A/19.4), valid for six months; …`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:ISSCExpiryDate` = `2026-07-14`
- Why: ValidISSCIndicator is "An indicator of whether the International Ship Security Certificate
  (ISSC) is valid (true) or not (false)". An interim ISSC issued under ISPS Code A/19.4 is a valid
  certificate for its six months (own knowledge: A/19.4 lets a ship trade on it as on a full ISSC,
  and port state control accepts it). The text says the interim certificate is valid until
  2026-07-14, and the expiry date is given; the indicator says the certificate is not valid. Read
  together, the reader cannot tell whether the port must treat the ship as without a valid ISSC.
- Condition: the indicator and the text agree on whether the ship holds a valid ISSC.
- Options: (a, preferred) set the indicator to true and keep the text as the explanation that the
  valid certificate is an interim one (moving it to AdditionalMattersDescription, since
  ISSCAbsenceReason is for "the reason if not having" an ISSC); (b) keep false if the world's port
  rules do not accept interim certificates, and say so.
- Needs decision: yes (whether the world treats an interim ISSC as valid)

## Checked and consistent
- Interim ISSC from 2026-01-15 for six months ends on 2026-07-14 = ISSCExpiryDate; issuer is the
  flag state's maritime administration, as the flag is Bayvarra.
- Health declaration: no infectious disease, 0 ill persons, a sick animal with SickAnimalOnBoard
  true and a description that explains it; ValidSanitationCertificateOnBoard true with the
  exemption certificate issued on 2026-01-14 (an SSCEC is valid six months, own knowledge).
- Reporter and sender are the carrier of the B/L 13; authority and receiver the Port of Lumeport,
  the destination of the cotton (mill at Lumeport).
- Container ship type 1511 and configuration FEEDER fit a carrier of the container of 12; gross
  tonnage 7,480 and net tonnage 3,910 are in proportion for a feeder (own knowledge).
- The stowaway search note refers to an event at Selanu on 1 March, before the issue date.

## Considered and refuted
- `/CommonTransportationReport/cac:Shipment/cbc:ID` = `TOL-SH-26-0208`: a shipment ID different
  from the cotton shipment SCG-SH-26-0200 suspected as an unlinked shipment — refuted because the
  report concerns the ship's voyage, a carrier's shipment of its own, not the ginnery's consignment.
- `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cbc:RadioCallSignID` = `QBTR4`:
  checked against real call sign allocations — the Q series is not allocated to any country by the
  ITU, so it cannot be mistaken for a real call sign.

## Outside this review
- Whether DirectionCode WB (westbound) fits the course from Selanu to Lumeport on the map, and
  whether the vessel Tidewell Reef can be at Lumeport at the time this voyage implies, are map and
  timeline questions across flows.
