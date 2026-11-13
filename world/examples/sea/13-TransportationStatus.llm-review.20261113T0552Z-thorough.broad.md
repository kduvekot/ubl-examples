# LLM review: 13-TransportationStatus.xml

Flow: sea (SEA-2026-01) · Review date: 2026-11-13 · Part: broad

## Reviewed version
- Run: `20261113T0552Z-thorough`
- Example: `world/examples/sea/13-TransportationStatus.xml`, Git blob `96261f3aedd684757ce22785ce1d8da29955cd70` (committed)
- Last commit changing the example: d920be0 2026-11-11 Document identification: computed UBLVersionID, transaction CustomizationIDs, process profiles
- Checkout: branch `claude/keen-feynman-45qjti`, commit e7f2d60 2026-11-13 Reviews of the sea flow, run 20261113T0552Z-thorough: parts written so far
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

### sea/13#F1 · High · Actual departure two hours after the report was issued
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualDepartureTransportEvent/cbc:OccurrenceTime` = `18:10:00`
- XPath: `/TransportationStatus/cbc:IssueTime` = `16:05:00`
- Why: `ActualDepartureTransportEvent` is "The actual departure from a specific location". The report is issued on 2026-05-14 at 16:05 and states as actual a departure at 18:10 the same day; an actual event cannot lie in the future of the report. The scheduled departure in the service description is 18:00 (`08-TransportServiceDescription.xml:/TransportServiceDescription/cac:TransportationService/cac:TransportEvent/cbc:OccurrenceTime` = `18:00:00`), so 18:10 is plausible as the actual time, but then the report must be issued after it.
- Condition: every actual event of the report is at or before the report's issue date and time; a future departure is given as an estimate.
- Options: (a) preferred: issue time after 18:10 (the report then also covers the departure); (b) keep 16:05 and give the departure as `EstimatedDepartureTransportEvent`.
- Needs decision: no

### sea/13#F2 · Medium · The consignment ID used as shipping order and as document reference
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0133`
- XPath: `/TransportationStatus/cac:DocumentReference/cbc:ID` = `LD-CS-26-0133`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0133`
- Why: `ShippingOrderID` is "A reference number for a shipping order" and `DocumentReference` "A reference to another document". `LD-CS-26-0133` is the consignment's identifier (the report's own `Consignment/ID`, and the consignment of `09-ForwardingInstructions.xml`), neither a shipping order nor a document; no example has this ID as its document ID (`flow_index.py sea`: `-> ?`). An identifier of one kind is used as two others.
- Condition: `ShippingOrderID` holds a shipping order number (or is absent) and the document reference points to a document (e.g. the bill of lading `TOL-BL-26-0139` or the booking), with the consignment identified only in `Consignment/ID`.
- Options: (a) preferred: drop `ShippingOrderID`; reference the booking or bill of lading as document; (b) none better seen.
- Needs decision: no

### sea/13#F3 · Medium · Port facility security officer given as the ship's security officer
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:SecurityOfficerPerson/cbc:JobTitle` = `Port facility security officer`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:SecurityOfficerPerson/cbc:FamilyName` = `Orrel`
- Why: `SecurityOfficerPerson` is "The person on board the vessel, accountable to the master, designated by the company as responsible for the security of the ship … and for the liaison with … the port facility security officers" (the ISPS ship security officer). The person given is a port facility security officer, i.e. the counterpart on shore that the definition distinguishes. In addition, the terminal's status report to the forwarder has no use for the ship's security officer.
- Condition: `SecurityOfficerPerson` is absent, or is the vessel's ship security officer in a document that needs it.
- Options: (a) preferred: drop it; (b) if the port facility security officer matters, give him as a contact of the terminal operator.
- Needs decision: no

### sea/13#F4 · Medium · Language code in LocaleCode
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: `LocaleCode` is "A code signifying the locale in which this language is used"; `en` with listID `ISO 639` repeats the language. 213 of 250 examples carry `LocaleCode`.
- Condition: each `LocaleCode` is absent or a locale code from a locale list.
- Options: (a) preferred: `en-XB` from a locale list; (b) drop it.
- Needs decision: no

### sea/13#F5 · Low · Loading event without type and time
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Container TWLU4120872 loaded on board.`
- Why: the event the report is about (its description repeats it) is a loading on board; it has no event type code and no time, so a system cannot tell the loading from any other event, nor its order relative to the departure at 18:10. The container is named only in text; the report carries no transport equipment.
- Condition: the loading event has a type code and a time before the departure, and the container is identified as transport equipment of the consignment.
- Options: (a) preferred: `TransportEventTypeCode` for loading with time, and the container as `TransportHandlingUnit/TransportEquipment` in the consignment; (b) none better seen.
- Needs decision: no

### sea/13#F6 · Low · Instruction about a delivery slot in a report on loading
- XPath: `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`
- Why: the report tells the export forwarder that the container was loaded and the vessel left Lumeport. There is no delivery slot left to change at this port, and the report names none; the instruction fits a pre-arrival or gate-in report, not this one.
- Condition: the instruction refers to something the report states, or is absent.
- Options: (a) preferred: drop it; (b) state the slot it refers to.
- Needs decision: no

### sea/13#F7 · Low · Container port described as a small enterprise
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `SMALL`
- Why: the Port of Lumeport operates the container quay where a 1,000 TEU feeder (`08-TransportServiceDescription.xml`) calls, with its own port control and port facility security; under the usual size criteria (fewer than 50 employees) such an operator is not a small enterprise (own knowledge of the EU SME definition, used here as a plausibility yardstick).
- Condition: the size class fits a port and container terminal operator.
- Options: (a) preferred: `MEDIUM` or `LARGE`; (b) drop the size code.
- Needs decision: no

## Checked and consistent
- Container `TWLU4120872` is the bill of lading's container and has a valid ISO 6346 check digit; consignment `LD-CS-26-0133` is the consignment of the forwarding instructions and the packing list.
- Departure 18:10 on 2026-05-14 fits the scheduled sailing of 18:00 that day (`08-TransportServiceDescription.xml`).
- Sender Port of Lumeport is the terminal operator of the stage and the signatory; receiver Bayforth, the export forwarder, is the party that needs the report; carrier Tidewell as in the bill of lading.
- UN/LOCODE `XBLMP` for the port agrees with the bill of lading's freight charge location.

## Considered and refuted
- `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cac:LocationCoordinate/cbc:LatitudeDirectionCode` = `South`: real-world coordinates 40° S, 15° W lie in the open South Atlantic — refuted because the world is fictional and has its own map; the coordinates are not a real register value.

## Outside this review
- Timeline across documents: the bill of lading `14-BillOfLading.xml` is issued on 2026-05-14 at 10:54, before the loading on board that this report records for the same day; whether a shipped-on-board bill could be issued then belongs to the cross-document timeline (and to the review of the bill of lading for what it states itself).
