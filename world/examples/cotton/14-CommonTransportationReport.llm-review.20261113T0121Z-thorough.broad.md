# LLM review: 14-CommonTransportationReport.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/14-CommonTransportationReport.xml`, Git blob `081267759b51366ff3d8aad9d0f0d1d2385f1b91` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
- Checkout: branch `claude/keen-feynman-45qjti`, commit f604cb7 2026-11-13 Reviews of the cotton flow, run 20261113T0121Z-thorough: parts written so far
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

### cotton/14#F1 · Medium · Pre-arrival report without an arrival time or port
- XPath: `/CommonTransportationReport/cbc:ReportTypeCode` = `PREARRIVAL`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cbc:ID` = `1`
- XPath: `/CommonTransportationReport/cac:TransportMeans/cbc:JourneyID` = `TR-26-09W`
- Why: a pre-arrival report tells the port authority when and where a ship will arrive. The shipment stage has no estimated arrival, no arrival or departure location and no transport event; the only places are the ship's registry port and, in free text, that it "left Selanu". The port of Lumeport receives the report but cannot learn from it when the ship arrives or at which terminal.
- Condition: the report states the estimated time of arrival and the port (or port facility) of arrival, and the last port of call.
- Options: (preferred) estimated arrival date and time and the arrival port on the shipment stage (or a transport event of the arrival type), with the loading port Selanu as departure; or an arrival event in the transport means.
- Needs decision: no

### cotton/14#F2 · Medium · Language code in `LocaleCode`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:Language/cbc:LocaleCode` = `en`
- Why: as cotton/02#F2.
- Condition: `LocaleCode` absent or a real locale code.
- Options: (preferred) drop it.
- Needs decision: no

### cotton/14#F3 · Low · Valid interim security certificate reported as "no valid certificate"
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:ValidISSCIndicator` = `false`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:ISSCAbsenceReason` = `The ship came under Bayvarra's flag on 15 January 2026 and sails with an interim certificate (ISPS Code A/19.4), valid for six months; …`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:ISSCExpiryDate` = `2026-07-14`
- Why: `ValidISSCIndicator` is "An indicator of whether the International Ship Security Certificate (ISSC) is valid". An interim ISSC under ISPS Code A/19.4 is a valid certificate for its six months (own knowledge), and the report gives its identifier, issuer and expiry date. Saying "not valid" and giving an "absence reason" contradicts the presence of a valid interim certificate; a port would treat a ship without a valid ISSC very differently.
- Condition: indicator and text agree: either the ship has a valid (interim) certificate and the indicator is true, with the interim status in another text, or there is no valid certificate.
- Options: (preferred) indicator true and the interim status in `AdditionalMattersDescription`; or keep false if the world's port rules treat an interim certificate as "not a full ISSC", and say so.
- Needs decision: yes

### cotton/14#F4 · Low · Nothing ties the report to the cotton shipment
- XPath: `/CommonTransportationReport/cac:Shipment/cbc:ID` = `TOL-SH-26-0208`
- XPath: `13-BillOfLading.xml:/BillOfLading/cac:Shipment/cbc:ID` = `SCG-SH-26-0200`
- Why: the report is part of the cotton flow, but its shipment is a different one (the ship's call), and it refers neither to the bill of lading 13, nor to the container (12), nor to cargo at all. Since the bill of lading names no vessel either (cotton/13#F1), no document of the flow says that the cotton travels on the Tidewell Reef.
- Condition: the cotton's carriage on this voyage can be followed from the documents (in this report or in the bill of lading).
- Options: (preferred) name vessel and voyage in the bill of lading (13); or refer to the bill of lading or container from this report, if the report is meant to carry cargo information.
- Needs decision: no

## Checked and consistent
- Interim ISSC expiry 2026-07-14 is six months less a day after the flag change on 15 January; the certificate ID IISSC-XB-2026-0115 and the flag-state issuer fit.
- Sick-animal indicator true with a description of the ship's cat; no ill persons; ship sanitation exemption certificate issued 2026-01-14 (valid for six months under IHR 2005, own knowledge) and `ValidSanitationCertificateOnBoardIndicator` true.
- Ship data: gross tonnage 7480 and net tonnage 3910 (unit C62), segregated ballast 1900 t, type code 1511 (full container ship) and configuration FEEDER fit a small feeder.
- Radio call sign `QBTR4` starts with Q, a series not allocated to any country (own knowledge), so it cannot be a real call sign.
- Direction WB: the port of Lumeport (15°12.6′ W) lies west of the port of Selanu (15°8.4′ W), as the coordinates in this report and in 12 show.

## Considered and refuted
- `/CommonTransportationReport/cac:SenderParty`: sender and receiver repeat reporter and authority — refuted: both pairs are required in their own right (sender/receiver mandatory); repeating them is not a filler.
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:AdditionalMattersDescription`: search for stowaways — refuted: a plausible additional security matter.

## Outside this review
- Whether MMSI `298702231` uses an MID that ITU has assigned to a real country could not be checked offline; the same MID occurs in the sea flow (`grep -rl --include='*.xml' 'MMSIRegistrationID>298'`).
- The two ports are about 6 km apart at the same latitude (coordinates in this report and in 12); whether a sea voyage between them fits the world's map is a map question.
