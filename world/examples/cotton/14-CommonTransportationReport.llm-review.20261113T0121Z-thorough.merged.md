# LLM review: 14-CommonTransportationReport.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/14-CommonTransportationReport.xml`, Git blob `081267759b51366ff3d8aad9d0f0d1d2385f1b91` (committed)
- Last commit changing the example: b77996d 2026-11-12 Remove the last fillers from the examples
- Checkout: branch `claude/keen-feynman-45qjti`, commit 76dc6e7 2026-11-13 Reviews of the cotton and retail flows: files written so far
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

### cotton/14#F1 · Medium · Pre-arrival report without an arrival time, port of arrival or last port of call
- XPath: `/CommonTransportationReport/cbc:ReportTypeCode` = `PREARRIVAL`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cbc:ID` = `1`
- XPath: `/CommonTransportationReport/cac:TransportMeans/cbc:JourneyID` = `TR-26-09W`
- Why: a pre-arrival report tells the port authority when and where a ship will arrive and where it comes from. The only shipment stage carries the reporting person, the ISPS and the health data, but no estimated arrival date or time, no transport event of any kind, no port of arrival (Lumeport appears only as the authority's location and as the registry port) and no last port of call (Selanu appears only in the ISPS free text, "before it left Selanu"). The only dates in the document are its issue date, registration dates, the ISSC expiry and the sanitation certificate's issue date. The authority cannot plan the berth, the shore power requested ("Shore power at the container quay.") or the veterinarian the master asks for; the notification periods of the ISPS Code and the IHR run from the arrival time (own knowledge). The document's purpose depends on it.
- Condition: the report states the estimated arrival date and time at Lumeport (or the port facility) and the port the ship comes from (Selanu), in the stage or transport event where UBL places them.
- Options: (a, preferred) give the shipment stage (main carriage, sea) the estimated arrival date and time or an estimated-arrival transport event at the Port of Lumeport, with the loading port Selanu as departure, consistent with the bill of lading 13 (on board 2026-03-02) and the map's sea route.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### cotton/14#F2 · Medium · Language code in `LocaleCode`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used." `en` (listID `ISO 639`) is a language code repeating `cac:Language/cbc:ID`, not a locale. Same value in 213 example files (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<'`).
- Condition: every `LocaleCode` holds a locale from a list that defines locales, named in its listID, or is absent.
- Options: (a, preferred) drop `LocaleCode`; (b) a locale such as `en-XB` from a locale list (BCP 47).
- Needs decision: no
- From: broad (F2), parties (F1)

### cotton/14#F3 · Low · "No valid ISSC" while the ship sails with a valid interim certificate
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:ValidISSCIndicator` = `false`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:ISSCAbsenceReason` = `The ship came under Bayvarra's flag on 15 January 2026 and sails with an interim certificate (ISPS Code A/19.4), valid for six months; …`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:ISSCExpiryDate` = `2026-07-14`
- Why: `ValidISSCIndicator` is "An indicator of whether the International Ship Security Certificate (ISSC) is valid (true) or not (false)"; `ISSCAbsenceReason` "A text describing the reason if not having a International Ship Security Certificate (ISSC)". An interim ISSC under ISPS Code A/19.4 is a valid certificate for its six months, on which a ship trades as on a full one (own knowledge); the report gives its identifier, issuer and expiry. The indicator says not valid and an "absence reason" is given, so a port cannot tell whether to treat the ship as without a valid ISSC (broad, context). Logistics refuted it: the indicator concerns the full ISSC, and the absence reason is the place to explain that only an interim one is held. Both readings are possible; whether the world treats an interim ISSC as valid is a decision.
- Condition: the indicator and the text agree on whether the ship holds a valid ISSC.
- Options: (a, preferred) indicator true, with the interim status explained in `AdditionalMattersDescription` (not as an absence reason); (b) keep false if the world's port rules do not accept interim certificates as valid, and say so.
- Needs decision: yes
- From: broad (F3), context (F2); refuted by logistics (argument carried)

### cotton/14#F4 · Low · Nothing ties the report to the cotton shipment
- XPath: `/CommonTransportationReport/cac:Shipment/cbc:ID` = `TOL-SH-26-0208`
- XPath: `13-BillOfLading.xml:/BillOfLading/cac:Shipment/cbc:ID` = `SCG-SH-26-0200`
- Why: the report is part of the cotton flow, but its shipment TOL-SH-26-0208 appears in no other example, it lists no cargo, container or bill of lading, and the bill of lading 13 names no vessel (cotton/13#F2): no document of the flow says that container TWLU4123110 (12) is aboard the Tidewell Reef. A separate shipment ID for the ship's voyage is legitimate (context refuted it on that ground, and the parts that raised it agree); the missing piece is the link.
- Condition: the cotton's carriage on this voyage can be followed from the documents: the vessel and journey are in the bill of lading, or this report refers to the cargo it carries.
- Options: (a, preferred) name vessel and journey TR-26-09W in the main-carriage stage of 13; (b) a consignment or document reference here, if the report is meant to carry cargo information.
- Needs decision: no
- From: broad (F4), logistics (F2)

### cotton/14#F5 · Low · Arrival contacts reachable only in weekday office hours; the carrier's bookings desk as reporter's contact
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:Contact/cbc:Name` = `Port control`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:Contact/cbc:Name` = `Bookings`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: a contact `Note` is "a textual description of the circumstances under which this contact can be used". An authority's contact in a pre-arrival report is reachable when ships arrive; port control is given as reachable on weekdays 08:00–17:00 only, and the reporting carrier's contact is its bookings desk with the same hours, although the report announces an arrival and asks for a veterinarian on arrival.
- Condition: the authority's and the reporter's contacts are ones that can be reached around the ship's arrival (e.g. 24-hour port control, the carrier's operations desk or the ship's agent).
- Options: (a, preferred) port control around the clock and the carrier's operations desk; (b) drop the hours note if the hours are not known.
- Needs decision: no
- From: parties (F3)

### cotton/14#F6 · Low · The port authority described as a small private limited company
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cbc:RegistrationName` = `Port of Lumeport Ltd`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Limited company (private)`
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- XPath: `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:MaritimeHealthDeclaration/cac:ShipSanitationControlExemptionDocumentReference/cac:IssuerParty/cac:PartyName/cbc:Name` = `Port of Lumeport`
- Why: `AuthorityParty` is "The Party who receives the Common Transportation Report. This Party is normally an Authority or regulator." The Port of Lumeport receives the security and health declarations and issued the ship's sanitation control exemption certificate, which under the IHR (Art. 39, Annex 3; own knowledge) the competent health authority of an authorised port issues. It is described as a small private limited company with a commercial registration. Port authorities run as companies exist, but a small private company as health and security authority for a container port is hard to reconcile with those roles; whether the world's ports are public authorities or companies is story.
- Condition: the party receiving the report and issuing the sanitation certificate is described as the kind of body that has those powers in the world, with a size that fits a container port.
- Options: (a, preferred) decide in the story whether the Port of Lumeport is a public port authority and describe it accordingly, or name the authority (e.g. a port health authority) that receives the report and issued the certificate; (b) keep the company and give it a size that fits.
- Needs decision: yes
- From: parties (F2)

### cotton/14#F7 · Low · Reporter's tax registration and share capital in a pre-arrival report
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyTaxScheme/cbc:CompanyID` = `CO-1235754`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/CommonTransportationReport/cac:ReporterParty/cac:PartyLegalEntity/cbc:FullyPaidSharesIndicator` = `true`
- Why: the report is "a common document used for reporting transport related issues to authorities"; it announces no dues, fee or charge, so the carrier's Coastal State sales-tax registration and its fully paid share capital of 40000000 XBL have no use in it (section 4.8, master data copied in). The same blocks are in 12 and 13.
- Condition: the report carries the reporter's tax registration or capital only if it does something with it (e.g. port dues billed from it, and said so).
- Options: (a, preferred) drop the reporter's `PartyTaxScheme`, `CorporateStockAmount` and `FullyPaidSharesIndicator`; (b) keep the tax registration if port dues are billed from the report, and make that visible.
- Needs decision: no
- From: money (F1)

### cotton/14#F8 · Low · Registration date 1 January 1996 shared by unrelated companies
- XPath: `/CommonTransportationReport/cac:AuthorityParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: `RegistrationDate` is "The registration date of the CompanyID." The Port of Lumeport shares 1 January 1996 with the ginnery, the mill, the forwarder and the Port of Selanu, in two registers; the date occurs 271 times in 181 example files (`grep -rho --include='*.xml' 'RegistrationDate>1996-01-01<' | wc -l`): a default rather than each company's history, unless the story makes it a register-wide date.
- Condition: each `RegistrationDate` is the party's registration date in the world's story, or absent.
- Options: (a, preferred) a date from the port's history; (b) drop it; (c) record a register-wide date in the story.
- Needs decision: yes
- From: parties (F4)

## Checked and consistent
- Interim ISSC from the flag change on 2026-01-15 for six months ends on 2026-07-14 = `ISSCExpiryDate` (ISPS A/19.4.4, own knowledge); the issuer is the Maritime Administration of Bayvarra, the flag state's administration.
- Health declaration: no infectious disease, 0 ill persons, sick animal true with a description that explains it; the Ship Sanitation Control Exemption Certificate issued 2026-01-14 is within its six-month validity on 2026-03-03 (IHR 2005, own knowledge), and `ValidSanitationCertificateOnBoardIndicator` is true.
- Ship data: type 1511 (full container ship), configuration FEEDER, gross tonnage 7480 and net tonnage 3910 (52 %), segregated ballast 1900 t fit a small feeder (own knowledge).
- Radio call sign QBTR4 (Q series) and MMSI 298702231 (MID 298) are recorded as unallocated by the ITU in the repository's sources (logistics, `PROVENANCE-second-round.md`); XBLMP uses the user-assigned code XB.
- Direction WB and journey TR-26-09W agree with Lumeport (15°12.60′ W) lying west of Selanu (15°8.40′ W, 12).
- Reporter and sender are the carrier of 13 (Tidewell's description identical to 12, 13 and 17); authority and receiver are the Port of Lumeport (UN/LOCODE XBLMP), the destination of the cotton. The reporting person is the master, which fits `MASTER`.
- The stowaway search note refers to an event at Selanu on 1 March, before the issue date, and agrees with the on-board date 2026-03-02 in 13.

## Considered and refuted
- `/CommonTransportationReport/cac:SenderParty`: sender and receiver repeat reporter and authority — refuted: both pairs are required in their own right (from broad).
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:AdditionalMattersDescription`: the stowaway search — refuted: a plausible additional security matter (from broad).
- `/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:ISPSRequirements/cbc:ValidISSCIndicator` = `false`: contradiction with the absence reason — refuted by logistics (the indicator concerns the full ISSC); broad and context kept it, so it stays as F3 with both arguments.
- `/CommonTransportationReport/cac:Shipment/cbc:ID` = `TOL-SH-26-0208`: a shipment ID different from the cotton shipment — refuted because the report concerns the ship's voyage, a carrier's shipment of its own (from context); the missing link to the cargo remains F4.
- `/CommonTransportationReport/cac:TransportMeans/cac:MaritimeTransport/cbc:RadioCallSignID` = `QBTR4`: a real call sign — refuted, the Q series is not allocated by the ITU (from context).

## Changed in the merge
- broad/F3 and context/F2 → F3: kept Low/yes; logistics' refutation carried into Why.
- parties/F3: the reporter's bookings desk (a role mismatch for an arrival report) is named in the title; otherwise unchanged.

## Outside this review
- The Port of Selanu (40°1.20′ S, 15°8.40′ W, 12) and the Port of Lumeport (40°1.20′ S, 15°12.60′ W, here) lie on the same parallel 4.2′ of longitude apart: 4.2 × 1.852 km × cos 40.02° ≈ 6.0 km (recalculated). A sea voyage between an island and the mainland of another country over 6 km, with a pre-arrival report the day after loading, is a map question (from broad, parties, logistics).
- Whether MMSI 298702231 uses an MID that the ITU has assigned to a real country could not be checked offline by broad; logistics found MID 298 recorded as unallocated in the repository's sources. The same MID occurs in the sea flow.
- Whether WB fits the course on the map and whether the Tidewell Reef can be at Lumeport at the time this voyage implies are map and timeline questions across flows (from context).
