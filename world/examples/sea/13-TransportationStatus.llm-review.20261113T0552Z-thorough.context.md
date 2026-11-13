# LLM review: 13-TransportationStatus.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: context

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/13-TransportationStatus.xml`, Git blob `96261f3aedd684757ce22785ce1d8da29955cd70` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit 6fea8ca 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/13#F1 · High · An "actual" departure two hours after the report, a day before the manifest's departure
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `18:10:00`
- XPath: `/TransportationStatus/cbc:IssueTime` = `16:05:00`
- XPath: `15-Manifest.xml:/Manifest/cac:Shipment/cac:ShipmentStage/cac:EstimatedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-15`
- Why: ActualDepartureTransportEvent is "the actual departure from a specific location". The report
  was issued on 2026-05-14 at 16:05 and states as actual a departure at 18:10 the same day. The
  carrier's manifest has the vessel's departure on 15 May at 06:00, and the carrier's service sails
  on Fridays (`08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:ScheduledServiceFrequency/cbc:WeekDayCode`
  = `5`; 15 May 2026 is a Friday). The report's own description and event say the container was
  loaded on board, not that the vessel left.
- Condition: no actual event lies after the issue time; the stage's departure, if given, agrees
  with the manifest (15 May) and is an estimate until it has happened.
- Options: (a) preferred: replace the actual departure by the loading event (see F3) and, if wanted,
  an estimated departure 2026-05-15 06:00; (b) issue the report after the departure and use the
  manifest's time.
- Needs decision: no

### sea/13#F2 · High · The consignment ID given as shipping order and as a document
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0133`
- XPath: `/TransportationStatus/cac:DocumentReference/cbc:ID` = `LD-CS-26-0133`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0133`
- XPath: `14-BillOfLading.xml:/BillOfLading/cbc:ShippingOrderID` = `BF-FI-26-0137`
- Why: ShippingOrderID is "a reference number for a shipping order" and DocumentReference "a
  reference to another document". LD-CS-26-0133 is the consignment's identifier ("an identifier
  assigned to a collection of goods"), used here at the same time as consignment, shipping order and
  referenced document; no document of the flow has this ID. The bill of lading gives the shipping
  order as BF-FI-26-0137 (the forwarder's instructions to the carrier), 09 and 12 as the shipment ID
  LD-SH-26-0132.
- Condition: ShippingOrderID holds the shipping order number that the other documents of the flow
  use for this booking; DocumentReference points to a document (e.g. the bill of lading or the
  booking), not to the consignment.
- Options: (a) preferred: ShippingOrderID BF-FI-26-0137 (or the agreed booking reference) and a
  reference to the shipping order / bill of lading by its document ID with a type; (b) drop both,
  since the consignment ID already ties the report to the goods.
- Needs decision: no

### sea/13#F3 · Medium · Loading reported as an "additional" event, without time or type
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Container TWLU4120872 loaded on board.`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- Why: The document-level TransportEvent is for "any additional events associated with this
  Transportation Status report that are not defined elsewhere in this document". Loading has its
  own element in the main-carriage stage (ShipmentStage LoadingTransportEvent), which is the stage
  this report already uses. The event, which is the one the report exists for (its Description says
  the same), also has no time and no type code, so a system cannot read it as a loading.
- Condition: the loading is reported in the main-carriage stage's loading event, with date, time
  and location, and the container is identified in structure (not only in the text).
- Options: (a) preferred: a LoadingTransportEvent in the MainCarriageShipmentStage at the container
  quay, with the time and the equipment; (b) keep the general event but add a type code and time.
- Needs decision: no

### sea/13#F4 · Medium · A port facility security officer in the role of the ship's security officer
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:SecurityOfficerPerson/cbc:JobTitle` = `Port facility security officer`
- Why: SecurityOfficerPerson is "the person on board the vessel, accountable to the master,
  designated by the company as responsible for the security of the ship" (the ship security officer
  of the ISPS Code). A port facility security officer is the port's counterpart ashore, employed by
  the port, not by the shipping company; he or she is not on board and not accountable to the
  master (own knowledge of the ISPS Code). The report names no vessel at all.
- Condition: SecurityOfficerPerson is the ship's security officer of the vessel carrying the
  container, or the element is absent.
- Options: (a) preferred: drop it from the port's status report (the port has no business stating
  the ship's officer); (b) name the vessel and its ship security officer.
- Needs decision: no

### sea/13#F5 · Medium · A language code in LocaleCode (three places)
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "a code signifying the locale in which this language is used"; each is the ISO
  639 language code.
- Condition: absent or a locale.
- Options: (a) preferred: a locale; (b) drop it.
- Needs decision: no

### sea/13#F6 · Low · An instruction about a delivery slot in a report about loading
- XPath: `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`
- Why: OtherInstruction is "an instruction regarding this message". The port of loading reports to
  the forwarder that the container is on board; at origin there is no further delivery slot (the
  container was delivered to the terminal on 13 May, per the bill of lading's drop-off), and the
  delivery at Selanu is the business of another port. The instruction has no object in this report.
- Condition: the instruction refers to something the receiver could act on after this report, or is
  absent.
- Options: (a) preferred: drop it.
- Needs decision: no

### sea/13#F7 · Low · Full legal and tax data of the carrier, terminal operator and receiver in a status report
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:PartyLegalEntity/cac:CorporateRegistrationScheme/cbc:Name` = `Federal business register of Bayvarra`
- Why: A status report circulates events; nothing in it depends on the parties' registrations, tax
  schemes or legal forms. The sender (the same port) is given with ID and name only, which is
  enough.
- Condition: parties carry identification, name and, where useful, a contact.
- Options: (a) preferred: reduce them as the SenderParty is.
- Needs decision: no

## Checked and consistent
- Container `TWLU4120872` and consignment `LD-CS-26-0133` agree with the packing list and the bill of
  lading; carrier Tidewell, receiver Bayforth (the forwarder who booked) and sender Port of Lumeport
  (terminal operator, signatory) fit a port's status message.
- UN/LOCODE `XBLMP` for Lumeport; StatusPeriod and StatusLocation agree with the event.

## Considered and refuted
- `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeDirectionCode`:
  coordinates 40° 1.20′ S, 15° 12.60′ W lie in the real South Atlantic — refuted for this lens: the
  world's map places its own coordinates; whether they agree with the map is a world consistency
  check, not a semantic one.
- `/TransportationStatus/cbc:TransportExecutionStatusCode`: "in progress" — refuted: the carriage has
  started (container on board), the delivery is to come.
