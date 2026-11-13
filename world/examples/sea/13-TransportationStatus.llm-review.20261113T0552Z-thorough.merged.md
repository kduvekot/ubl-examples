# LLM review: 13-TransportationStatus.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: merged

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/13-TransportationStatus.xml`, Git blob `96261f3aedd684757ce22785ce1d8da29955cd70` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
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

### sea/13#F1 · High · An "actual" departure two hours after the report was issued, and a day before the manifest's departure
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `18:10:00`
- XPath: `/TransportationStatus/cbc:IssueTime` = `16:05:00`
- XPath: `15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-15`
- XPath: `15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceTime` = `06:00:00`
- Why: `ActualDepartureTransportEvent` is "The actual departure from a specific location". The report is issued on 2026-05-14 at 16:05 and states as actual a departure at 18:10 the same day, in the future at issue time. The report's own description and event say the container was loaded on board, not that the vessel left. The carrier's manifest, issued the next day, still gives the vessel's departure as an estimate for 2026-05-15 06:00. The transport service description scheduled the sailing for 2026-05-14 18:00 (`08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:OccurrenceTime` = `18:00:00`), while its weekly frequency says Friday (`08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:ScheduledServiceFrequency/cbc:WeekDayCode` = `5`; 2026-05-14 is a Thursday, 2026-05-15 a Friday, recomputed): the flow has no single departure time, and this report contradicts both its own issue time and the manifest.
- Condition: no actual event lies after the issue time; the departure, if given, agrees with the manifest and the other documents of the voyage and is an estimate until it has happened.
- Options: (a) preferred: report the loading as the actual event (F5) and, if wanted, an estimated departure agreeing with the manifest; (b) issue the report after the departure and use one departure time across 08, 13, 15 and 16.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### sea/13#F2 · High · The consignment ID given as shipping order, against the bill of lading's shipping order
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0133`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0133`
- XPath: `14-BillOfLading.xml:/BillOfLading/cbc:ShippingOrderID` = `BF-FI-26-0137`
- XPath: `12-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0132`
- Why: `ShippingOrderID` identifies a shipping order; the value is the consignment's ID ("an identifier assigned to a collection of goods"). The bill of lading gives the shipping order as `BF-FI-26-0137` (the forwarder's instructions to the carrier), 09 and 12 as the shipment ID: one booking, three shipping order numbers. The forwarder receiving this report cannot match it to its shipping order by this field.
- Condition: `ShippingOrderID`, if present, is the shipping order number the other documents use for this booking (`BF-FI-26-0137`).
- Options: (a) preferred: `BF-FI-26-0137` (the report goes to Bayforth, whose shipping order that is); (b) drop it, the consignment ID ties the report to the goods.
- Needs decision: no
- From: logistics (F2, High), context (F2, High), broad (F2, Medium)

### sea/13#F3 · High · Document reference to a document that does not exist: it holds the consignment ID
- XPath: `/TransportationStatus/cac:DocumentReference/cbc:ID` = `LD-CS-26-0133`
- Why: `DocumentReference` is "A reference to another document"; `LD-CS-26-0133` is the consignment's ID (`/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0133`, as in the packing list and bill of lading) and resolves to no example (`flow_index.py sea`: `-> ?`). A reference to a document that does not exist is High under section 6 (as in the earlier flows' merges for the same pattern). The natural reference is the bill of lading `TOL-BL-26-0139`, issued that morning, as in `17-TransportationStatus.xml`.
- Condition: the document reference identifies an existing document, with a type, or is absent.
- Options: (a) preferred: reference the bill of lading `TOL-BL-26-0139`; (b) drop the reference.
- Needs decision: no
- From: logistics (F5, Medium), context (F2, grouped), broad (F2, grouped)

### sea/13#F4 · High · The port facility security officer given as the ship's security officer; the ship's report names another person
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:SecurityOfficerPerson/cbc:FirstName` = `Tamsin`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:SecurityOfficerPerson/cbc:FamilyName` = `Orrel`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:SecurityOfficerPerson/cbc:JobTitle` = `Port facility security officer`
- Why: `SecurityOfficerPerson` is "The person on board the vessel, accountable to the master, designated by the company as responsible for the security of the ship …" (the ISPS ship security officer). A port facility security officer is the port's counterpart ashore (own knowledge of the ISPS Code). The ship's own report for this voyage names the chief officer Elsbeth Marrin as ship security officer (`16-CommonTransportationReport.xml:/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:SecurityOfficerPerson/cbc:FamilyName` = `Marrin`, `16-CommonTransportationReport.xml:/CommonTransportationReport/cac:Shipment/cac:ShipmentStage/cac:SecurityOfficerPerson/cbc:RoleCode` = `SSO`), and the manifest's crew lists her, not Tamsin Orrel (`15-Manifest.xml:/Manifest/cac:CrewPerson[2]/cbc:FamilyName` = `Marrin`). The value contradicts the definition and two other examples. A terminal's loading report also has no use for the ship's security officer.
- Condition: `SecurityOfficerPerson` of the main-carriage stage is the vessel's ship security officer, the same as in `16-CommonTransportationReport.xml`, or absent.
- Options: (a) preferred: drop it from the port's status report; (b) the ship security officer as in 16; the port facility security officer, if needed, as the terminal operator's contact.
- Needs decision: no
- From: parties (F1, High), broad (F3, Medium), context (F4, Medium)

### sea/13#F5 · Medium · Loading reported only as an "additional" free-text event, and the container only in text
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Container TWLU4120872 loaded on board.`
- XPath: `/TransportationStatus/cbc:Description` = `Container TWLU4120872 loaded on board.`
- Why: the document-level `TransportEvent` is for "any additional events associated with this Transportation Status report that are not defined elsewhere in this document"; the loading, the status the report exists for, has its own element in the main-carriage stage the report already uses (`LoadingTransportEvent`). The event has a date but no time and no type code, so a system cannot read it as a loading or order it relative to the departure, and the container, whose status changes, appears only in two free texts, not as transport equipment. Information the report's purpose depends on is not in structured form (Medium).
- Condition: the loading is reported in the main-carriage stage's loading event with date, time and location, and the container is identified as transport equipment of the consignment.
- Options: (a) preferred: `LoadingTransportEvent` at the container quay with time, and `TransportHandlingUnit/TransportEquipment` `TWLU4120872` in the consignment; (b) keep the general event with a type code and time.
- Needs decision: no
- From: logistics (F4), context (F3), broad (F5, Low)

### sea/13#F6 · Medium · Language code in LocaleCode
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` (listID `ISO 639`) repeats the language. 362 occurrences in 213 examples.
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: drop it; (b) a locale such as `en-XB`.
- Needs decision: no
- From: broad (F4), parties (F2), context (F5)

### sea/13#F7 · Low · Instruction about a delivery slot in a report on loading
- XPath: `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`
- Why: the port of loading tells the export forwarder that the container is on board; the container was delivered to the terminal on 13 May (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:AcceptanceTransportEvent/cbc:OccurrenceDate` = `2026-05-13`), and delivery at Selanu is another port's business. The report names no slot; the instruction has no object here.
- Condition: the instruction refers to something the report states, or is absent.
- Options: (a) preferred: drop it; (b) state the slot it refers to.
- Needs decision: no
- From: broad (F6), context (F6)

### sea/13#F8 · Low · The Port of Lumeport described as a small enterprise
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- Why: the Port of Lumeport runs the container quay where the carrier's feeder loads, has its own port control and port facility security, and in `16-CommonTransportationReport.xml` issues ships' certificates and supplies fuel; a container port operator is not a small enterprise (own knowledge of the usual size criteria, e.g. the EU SME definition, as a plausibility yardstick). Its size in the world is a matter of the story.
- Condition: the size class fits a container port operator in the world, or is absent.
- Options: (a) preferred: `MEDIUM` or `LARGE`, as the story gives the port; (b) drop the size code.
- Needs decision: yes (the port's size in the story; parties said yes, broad no)
- From: broad (F7), parties (F3)

### sea/13#F9 · Low · Status and event locations named but not identified
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Port of Lumeport`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Port of Lumeport, container quay`
- Why: both locations are names only, while the same document identifies the port with UN/LOCODE `XBLMP` in the terminal operator's physical location.
- Condition: the status and event locations carry the LOCODE `XBLMP`.
- Options: (a) preferred: add `ID` `XBLMP`.
- Needs decision: no
- From: logistics (F6)

### sea/13#F10 · Low · Full legal and tax data of carrier, terminal operator and receiver in a status report
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CorporateStockAmount` = `40000000`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- Why: a status report circulates events; nothing in it depends on the parties' registrations, share capital, tax schemes or legal forms. The sender (the same port) is given with ID and name only, which is enough. Copied master data (section 4.8).
- Condition: parties carry identification, name and, where useful, a contact.
- Options: (a) preferred: reduce them as the sender party is.
- Needs decision: no
- From: context (F7)

### sea/13#F11 · Low · The same registration date 1996-01-01 for unrelated companies
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: the Port of Lumeport and Bayforth Forwarding share New Year's Day 1996, while the carrier has its own date (`1974-03-01`); 271 occurrences in 181 examples.
- Condition: own dates, or absent (F10 may remove them).
- Options: (a) preferred: own dates; (b) leave the element out.
- Needs decision: yes
- From: parties (F4)

### sea/13#F12 · Low · A signature with an ID and the signatory only, its ID carrying the example number
- XPath: `/TransportationStatus/cac:Signature/cbc:ID` = `PL-SIG-TS-13`
- XPath: `/TransportationStatus/cac:Signature/cac:SignatoryParty/cac:PartyName/cbc:Name` = `Port of Lumeport`
- Why: an "Automatic report from the sender's tracking system" with a signature that has no method, date or attachment; its ID ends in `13`, this example's position in the flow. Not raised by any part; added by the merge, as in 09–12.
- Condition: a signature, where present, says how and when the document was signed, with the signer's own reference.
- Options: (a) preferred: drop it; (b) complete it.
- Needs decision: yes (whether the world's documents are signed at all)
- From: merge

## Checked and consistent
- Container `TWLU4120872` (in the texts) is the container of the packing list, bill of lading and manifest, with a valid ISO 6346 check digit; consignment `LD-CS-26-0133` is that of 09, 10 and 14; main-carriage stage ID `2` is the bill of lading's.
- Sender and signatory Port of Lumeport is the terminal operator of the loading port; receiver Bayforth is the forwarder that booked (`12-ForwardingInstructions.xml`); carrier Tidewell as in the bill of lading. `XBLMP` is the bill of lading's loading port (`14-BillOfLading.xml:/BillOfLading/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:ID` = `XBLMP`).
- Contacts: the carrier's "Bookings", the port's "Port control" and the forwarder's "Export desk", all operations planners, fit their roles.
- By the coordinates Selanu lies east of Lumeport, consistent with voyage `TH-26-19E` (from logistics).

## Considered and refuted
- `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeDirectionCode` = `South`: real-world coordinates 40° S, 15° W lie in the open South Atlantic — refuted because the world is fictional and has its own map; coordinates are not a register value (from broad, context).
- `/TransportationStatus/cbc:TransportExecutionStatusCode` = `INPROGRESS` — refuted: the carriage has started (container on board), delivery is to come (from context).

## Refuted in the merge
### logistics/F3 · High · Port coordinates put Lumeport 3.2 nautical miles from Selanu, against a two-day passage
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeMinutesMeasure` = `1.20`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `12.60`
- Why (logistics): the quay of Lumeport is at 40°1.20′ S 15°12.60′ W, Selanu at 40°1.20′ S 15°8.40′ W (`17-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LongitudeMinutesMeasure` = `8.40`, and in 16); 4.2′ × cos 40° = 3.2 nautical miles (recomputed: 4.2 × 0.766 = 3.22), against "two days at sea" (`08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:EstimatedDurationPeriod/cbc:DurationMeasure` = `2`), 64 hours in the manifest and 120 nautical miles west of Selanu in the ship's report. Condition: the coordinates and the passage agree. Needs decision: yes.
- Refuted because: this document states only Lumeport's coordinates and no voyage, distance or duration; nothing in it contradicts itself. The contradiction lies between the map scale implied across documents (a location question across documents, section 4: Outside this review), and it is a finding in `16-CommonTransportationReport.xml`, which states coordinates and distances in one document (aligned with sea-merge-decisions-a.md and -c.md: High only where one document contradicts itself). The calculation stands and is kept under "Outside this review".

## Changed in the merge
- broad/F2 (Medium), logistics/F2 and context/F2 (High) → F2 (shipping order, High) and F3 (document reference, High): split, as in the earlier flows (reference to a document that does not exist). logistics/F5 (Medium) raised to High.
- parties/F1 (High), broad/F3 and context/F4 (Medium) → F4: High kept (contradiction with `16-CommonTransportationReport.xml` and `15-Manifest.xml`).
- broad/F5 (Low), logistics/F4 and context/F3 (Medium) → F5: Medium.
- broad/F7 (no), parties/F3 (yes) → F8: needs decision yes.
- logistics/F3 → Refuted in the merge (Outside).
- LocaleCode: preferred option set to drop.
- F12 added by the merge.

## Outside this review
- Map scale: Lumeport (40°1.20′ S 15°12.60′ W, here) and Selanu (15°8.40′ W, in 16/17) are 3.2 nautical miles apart, against a two-day passage in 08, 64 hours in 15 and a noon position 120 nautical miles west of Selanu in 16 (from logistics F3 and parties; see the review of `16-CommonTransportationReport.xml`).
- Timeline: the bill of lading `14-BillOfLading.xml` is issued on 2026-05-14 at 10:54, before the loading on board this report records for the same day; whether a shipped-on-board bill could be issued then is a cross-document timeline question (and part of the bill of lading's own review) (from broad).
