# LLM review: 07-TransportationStatus.xml

Flow: rail (RAIL-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/rail/07-TransportationStatus.xml`, Git blob `104dc14ba8f489635d6473fbc6d93903f6bf457e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit abfa39e 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
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

### rail/07#F1 · High · Document reference to a document that does not exist (the consignment ID)
- XPath: `/TransportationStatus/cac:DocumentReference/cbc:ID` = `VI-CS-26-0327`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `VI-CS-26-0327`
- Why: DocumentReference is "A reference to another document associated with this document", its ID "An identifier for the referenced document". VI-CS-26-0327 is the consignment's identifier ("An identifier assigned to a collection of goods for both import and export"), given as such in the same report and in 02, 03, 06, 08 and 09; no document of the flow, nor of any other flow, has this ID (`flow_index.py rail`: `-> ?`; verified in the merge with `grep -rl --include='*.xml' '<cbc:ID>VI-CS-26-0327<'`, which finds it, apart from this reference, only as Consignment/ID and ReferencedConsignment/ID). A reference without a type to a document that does not exist is a broken reference (section 6, High). The parts made this Medium together with ShippingOrderID (F2); it is split off because a broken reference deserves another severity.
- Condition: DocumentReference is absent, or points to a document that exists, with its kind stated.
- Options: (a) preferred: drop it; the consignment is identified in Consignment/ID and the plan in TransportExecutionPlanDocumentReference; (b) reference the transport request VI-TR-26-0326 (02) with a document type, if the report needs it.
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### rail/07#F2 · Medium · Consignment ID used as shipping order number
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `VI-CS-26-0327`
- Why: ShippingOrderID is "A reference number for a shipping order". VI-CS-26-0327 is the consignment's ID (see F1), an identifier of one kind used as another. The closest thing to a shipping order in the flow is the transport request VI-TR-26-0326 (02), confirmed by the plan FRC-TEP-26-0328 (03), which the report already references. The waybill has the same misuse (08). Medium, not High as in air (where another example states a different shipping-order ID): here no example states a shipping-order ID at all.
- Condition: ShippingOrderID is absent or holds the ID of the shipping order (or forwarding instruction) of this transport; the consignment ID appears only as the consignment's ID.
- Options: (a) preferred: drop it (broad, context: the consignment and the plan are identified); (b) VI-TR-26-0326, if the world treats the transport request as the shipping order (logistics' preference).
- Needs decision: no
- From: broad (F1), logistics (F1), context (F1)

### rail/07#F3 · Medium · Loading reported in generic events instead of the loading event
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Two containers loaded on the container train.`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-04-14`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportEvent/cbc:OccurrenceTime` = `05:40:00`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TransportEvent/cbc:CompletionIndicator` = `true`
- Why: The report's purpose (its Description) is the loading. The shipment stage has a dedicated LoadingTransportEvent ("The loading of goods in this shipment stage"), but the loading is given twice in generic events: at document level ("Any additional events … not defined elsewhere in this document") with text, date and place but no time, and in the stage as an anonymous TransportEvent ("A additional significant occurrence … not defined elsewhere in this Shipment Stage") at 05:40 with no type, description or location, which says nothing on its own. Only the waybill reveals that 05:40 is the loading (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadingTransportEvent/cbc:OccurrenceTime` = `05:40:00`).
- Condition: The loading is in MainCarriageShipmentStage/LoadingTransportEvent with date, time 05:40, completion and location (the hub); no event without type, description or dedicated element remains.
- Options: (a) preferred: one LoadingTransportEvent (14 April 05:40, Ferrano Intermodal Hub) and drop both generic events (or keep the document-level one only with a TransportEventTypeCode); (b) give the generic events a type code from a list and a location.
- Needs decision: no
- From: broad (F2), logistics (F3), context (F3)

### rail/07#F4 · Medium · Road pickup at the warehouse recorded in the rail main carriage
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualPickupTransportEvent/cbc:OccurrenceDate` = `2026-04-13`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:ActualPickupTransportEvent/cbc:OccurrenceTime` = `15:00:00`
- Why: The pickup on 13 April at 15:00 is the carrier's tractor collecting the containers at Castrano's warehouse (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:Pickup/cac:PickupLocation/cbc:Name` = `Castrano Logistics warehouse, Ferrano`), a road leg to the hub. The main carriage by train begins at the hub on 14 April; an event belongs to the stage it happens in (section 5).
- Condition: The road collection is in a pre-carriage stage (with its mode) or at consignment level; the main-carriage stage holds only rail events.
- Options: (a) preferred: a PreCarriageShipmentStage (TransportModeCode 3) with the pickup and the warehouse as location; (b) drop the pickup, since the report is about the loading.
- Needs decision: no
- From: broad (F3), logistics (F2), context (F2)

### rail/07#F5 · Medium · Province given in Region
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- Why: Region is "The recognized geographic or economic region or group of countries in which this address is located"; a province is an administrative division (CountrySubentity, "…such as the name of its county, province, or state"), as the flow's Bayvarran addresses use (`02-TransportExecutionPlanRequest.xml:/TransportExecutionPlanRequest/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CountrySubentity` = `Upland State`). 219 occurrences in 104 example files.
- Condition: No address in this example carries the province in Region; where given, it is in CountrySubentity.
- Options: (a) preferred: CountrySubentity; (b) drop it.
- Needs decision: no (broad, context said yes; aligned with rail 01–05, wood, plastics)
- From: broad (F4), parties (F1), context (F4)

### rail/07#F6 · Low · Optional takeover without place, party or reason
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:OptionalTakeoverTransportEvent/cbc:OccurrenceTime` = `17:00:00`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:OptionalTakeoverTransportEvent/cbc:CompletionIndicator` = `false`
- Why: OptionalTakeoverTransportEvent is "The optional takeover of the goods in this shipment stage". At 17:00 on 14 April the train is on its way to Marrowdale (left 06:52, due 15 April); no document of the flow describes a takeover option (by whom, where), and the event has no location. Without a reason it is a filler (IND5/IND6).
- Condition: The event is absent, or describes a takeover the story contains (place and party), with matching statements in 03 and 08.
- Options: (a) preferred: drop it; (b) make it the handover at the border station to a Bayvarran rail undertaking (location, type), which changes the story.
- Needs decision: no (logistics said yes; the preferred option changes no story, only (b) would)
- From: broad (F5), logistics (F4), context (F5)

### rail/07#F7 · Low · Terminal control reachable only in office hours
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Contact/cbc:Name` = `Terminal control`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Contact/cbc:Note` = `Weekdays 08:00–17:00`
- Why: The terminal's control loads the train at 05:40 and dispatches it at 06:52 (05, 08); availability on weekdays 08:00–17:00 does not fit a contact used at those hours. A contact note, hence Low (as rail 04/05 in the other merge).
- Condition: The stated availability covers the terminal's operating hours, or the note is absent.
- Options: (a) preferred: the hub's real hours; (b) drop the note.
- Needs decision: no
- From: broad (F6)

### rail/07#F8 · Low · The two loaded containers are not identified
- XPath: `/TransportationStatus/cbc:Description` = `Two containers loaded on the container train.`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `VI-CS-26-0327`
- Why: The report says two containers were loaded but names neither the containers (FRXU1044175, FRXU1044180 in 06 and 08) nor the train or wagon; the carrier has to infer them from the consignment ID. A loading report usually identifies the equipment.
- Condition: The containers the report is about are identified in it (e.g. Consignment/TransportHandlingUnit/TransportEquipment/ID), or the report is evidently about the consignment only.
- Options: (a) preferred: add the two containers, and optionally the train FRC 4417 in the stage's TransportMeans.
- Needs decision: no
- From: logistics (F5)

### rail/07#F9 · Low · Status and event locations are the company name, without identifier
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Ferrano Intermodal Hub`
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Ferrano Intermodal Hub`
- Why: The name of a location is the place, with identifiers where the same place is identified elsewhere (section 5). Both are the terminal operator's company name (`/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyName/cbc:Name` = `Ferrano Intermodal Hub`), while the waybill identifies the loading place by UN/LOCODE (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:TransportHandlingUnit[1]/cac:TransportEquipment/cac:LoadingLocation/cbc:ID` = `XUFER`) and the plan gives the terminal an address (`03-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:ToLocation/cac:Address/cbc:BuildingNumber` = `59`).
- Condition: The locations name the place and identify it as the other examples of the flow do.
- Options: (a) preferred: a place name and identifier (XUFER or a terminal ID) used in every example; (b) at least the plan's address.
- Needs decision: no
- From: parties (F3)

### rail/07#F10 · Low · "English" renderings of the addresses and legal forms are Italian
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Viale della Stazione`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:StreetName[2]` = `Via del Terminal`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[2]` = `Società a responsabilità urvaniana (private limited company)`
- Why: Each repeated rendering must be in the language its languageID names (section 5); these are tagged `en-XU` but are Italian (own knowledge). A world convention for street names cannot be ruled out from the XML; the legal form is not a proper name, the stronger case. 217 such renderings in 102 example files (count as in rail 06's merged review).
- Condition: Every rendering tagged as English is English, or the world records the Italianate English usage.
- Options: (a) record the convention in the story (preferred if intended); (b) translate; (c) tag with the language the text is in.
- Needs decision: yes
- From: parties (F2); the terminal operator's legal form added by the merge (same problem)

### rail/07#F11 · Low · Registration date 1996-01-01 of carrier and terminal operator
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: Not raised by any part of this run; added by the merge for consistency with rail 01–05 and earlier flows. The same date recurs for many unrelated companies (271 occurrences in 181 example files), which reads as a default, unless a 1996 (re-)registration is part of the story.
- Condition: Each company's registration date is its own, or the world records a general 1996 registration.
- Options: (a) preferred: own date per company; (b) record a 1996 re-registration in the story.
- Needs decision: yes
- From: merge

## Checked and consistent
- TransportExecutionPlanDocumentReference `FRC-TEP-26-0328` resolves to the plan 03 for the same consignment; the planned delivery 15 April 11:00 equals the plan's and is not completed, correct at 13:11 on 14 April.
- Times against the issue time (2026-04-14 13:11): loading 05:40 and pickup 13 April are past and completed; StatusPeriod 14 April; TransportExecutionStatusCode INPROGRESS fits a train under way; the loading at 05:40 lies between the train's arrival at the hub (05:30) and its departure (06:52, 05).
- Sender and signatory are the hub (`XU-R-105096`), the terminal operator of the stage; receiver and carrier Ferrano Rail Cargo (`XU-R-104685`), the provider of the plan; full descriptions identical to 04 and 05. Carrier contact "Freight desk / Operations planner / Operations" fits a carrier.

## Considered and refuted
- `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`: instruction to the wrong party, or without a reason — refuted because the carrier, which receives the report, is the party that would change the delivery slot, and the text tells it when an answer is expected. (from broad, context)
- `/TransportationStatus/cbc:IssueTime` = `13:11:00`: stale report (loading 05:40, departure 06:52 not reported) — refuted because a status report need not report every event and this one reports the loading; the delay is a timeline question (see "Outside this review"). (from broad)
- `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:DeliveryTransportEvent/cbc:CompletionIndicator` = `false`: a future delivery in a status report — refuted: the indicator marks it as not yet happened. (from logistics)
- `/TransportationStatus/cbc:TransportExecutionStatusCode` = `INPROGRESS`: checked, fits a train under way; consistent with 05 and 08. (from logistics)

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1 and F2: split; the DocumentReference to a non-existent document raised from Medium to High (section 6: a referenced document that does not exist), ShippingOrderID stays Medium. Merge verified that no document has the ID.
- broad/F2, logistics/F3, context/F3 → F3: combined.
- broad/F3, logistics/F2, context/F2 → F4: combined.
- broad/F4, parties/F1, context/F4 → F5: needs decision no (broad, context yes), aligned with rail 01–05 and earlier flows.
- broad/F5, logistics/F4, context/F5 → F6: needs decision no (logistics yes): only option (b) changes the story.
- parties/F2 → F10: terminal operator's legal form added; count replaced by 217 in 102 files.
- F11 added by the merge (registration date 1996-01-01).

## Outside this review
- Timeline: the report "Two containers loaded on the container train" is issued at 13:11 on 14 April, six hours after the train left the hub at 06:52 (05, 08). (from context)
