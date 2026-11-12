# LLM review: 05-TransportationStatus.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/05-TransportationStatus.xml`, Git blob `9e63ff7c8a83c2b085bcdc225a1065a3d43ba26b` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 5b6aed1 2026-11-12 Reviews of the rail and air flows, run 20261112T2137Z-thorough: parts written so far
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

### air/05#F1 · High · The report refers to a waybill that is issued 38 minutes later
- XPath: `/TransportationStatus/cac:DocumentReference/cbc:ID` = `KXL-WB-26-0325`
- XPath: `/TransportationStatus/cbc:IssueDate` = `2026-05-13`
- XPath: `/TransportationStatus/cbc:IssueTime` = `10:05:00`
- XPath: `04-Waybill.xml:/Waybill/cbc:IssueDate` = `2026-05-13`
- XPath: `04-Waybill.xml:/Waybill/cbc:IssueTime` = `10:43:00`
- Why: The status report is issued on 2026-05-13 at 10:05 and cites air waybill `KXL-WB-26-0325`, which Kelaro issues on the same day at 10:43 (both parties' addresses at TimezoneOffset −1). A document cannot refer to a document that does not yet exist. Merge check: refutation attempted on the ground that in air cargo the AWB number is allocated at booking, before the waybill is executed at acceptance; refuted, because the reference is the waybill's document ID, not a pre-allocated AWB number (the waybill's carrier shipment number is a different value, `04-Waybill.xml:/Waybill/cbc:CarrierAssignedID` = `KXL-AWB-26-0319`). Accepting cargo before the waybill is issued is itself normal; the reference is the problem.
- Condition: the report is issued after the waybill it refers to, or it refers only to identifiers that exist at its issue time (the consignment, the booking, the forwarding instructions).
- Options: (a) preferred: issue the report after 10:43 (the event date stays 2026-05-13); (b) drop the reference and identify the cargo by consignment and shipping order. Either way, check `06-DespatchAdvice.xml` (10:07) against the same sequence.
- Needs decision: no
- From: broad, logistics, context

### air/05#F2 · High · ShippingOrderID holds the consignment ID and contradicts the forwarding instructions
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0324`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`
- Why: ShippingOrderID is "A reference number for a shipping order". The value is the consignment ID, which the report already gives in Consignment/ID; the forwarding instructions give the shipping order as `LD-SH-26-0323`. An identifier of one kind used as another, contradicting the document that defines it. The same value is in `04-Waybill.xml` and `09-TransportationStatus.xml`.
- Condition: ShippingOrderID equals the shipping order (or forwarding instruction) ID used in 03 and 04, or is absent.
- Options: (a) preferred: the same value as the waybill once that is fixed (`LD-FI-26-0322`, see air/04#F1); (b) `LD-SH-26-0323` everywhere; (c) drop it, as the consignment and the waybill already identify the cargo.
- Needs decision: no
- From: broad, logistics, context

### air/05#F3 · Medium · Acceptance reported as a generic event without time or type, where a dedicated stage event exists
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-13`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Cargo accepted and built up for the flight.`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cbc:ID` = `1`
- Why: TransportationStatus/TransportEvent is for "Any additional events associated with this Transportation Status report that are not defined elsewhere in this document". Acceptance at the terminal is defined: ShipmentStage has AcceptanceTransportEvent (UBL 2.5 model), and the report already has the main-carriage stage with the terminal operator. The generic event has no time and no TransportEventTypeCode, so the status the report exists to give (when the cargo was accepted) is only in free text and to the day; two events (acceptance and build-up) are folded into one. Without a time the acceptance cannot be placed against the cut-off (03 has an untyped event at 2026-05-13 19:00) or against the despatch advice issued at 10:07.
- Condition: the acceptance is in the main-carriage stage's AcceptanceTransportEvent with date, time (before the report's issue time) and location; any build-up event that remains has a type code.
- Options: (a) preferred: MainCarriageShipmentStage/AcceptanceTransportEvent with date, time and the terminal location; (b) keep the generic event with a TransportEventTypeCode and time.
- Needs decision: no
- From: logistics (F3, F4), context, broad (as part of a Low finding)

### air/05#F4 · Medium · LocaleCode holds a language code
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Language/cbc:LocaleCode` = `en` (Lumeport Airport Cargo Terminal)
- Why: Language/LocaleCode is "A code signifying the locale in which this language is used". `en` with listID `ISO 639` is a language, not a locale, and repeats Language/ID. Counted over `*.xml`: 362 such elements in 213 files.
- Condition: LocaleCode holds a locale from a locale list, or is absent.
- Options: (a) preferred: drop it; (b) a real locale such as `en-XB` with a locale list.
- Needs decision: no
- From: broad, parties, context

### air/05#F5 · Low · Status location named after the terminal company, without identifier
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Lumeport Airport Cargo Terminal`
- XPath: `/TransportationStatus/cac:SenderParty/cac:PartyName/cbc:Name` = `Lumeport Airport Cargo Terminal`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Lumeport airport, cargo terminal`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cbc:ID` = `XBLMA`
- Why: StatusLocation is one of the "Locations associated with this Transportation Status report"; Location/Name is "The name of this location". The value is the sending party's name, not a place. The same place is named as a place in the event's location and identified as `XBLMA` in the terminal operator's physical location; the status location carries neither, so the report names one place in three ways, one of them a company.
- Condition: the status location names the place and, where available, carries UN/LOCODE `XBLMA`, consistent with the event's location.
- Options: (a) preferred: one location `Lumeport airport, cargo terminal` with ID `XBLMA` (schemeID UN/LOCODE), in both the status and the event location; (b) drop StatusLocation, as the event and the terminal already give the place.
- Needs decision: no
- From: broad, parties, logistics, context

### air/05#F6 · Low · An instruction about a delivery slot that no document states
- XPath: `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Kelaro Air Cargo`
- Why: The report goes from the origin cargo terminal to the airline about acceptance; no document of the flow gives a delivery slot, and neither party of this report delivers to the consignee, so the instruction has nothing to refer to (logistics). Against (broad, context): the terminal books the slot for delivering the built-up unit to the aircraft, which the airline may need to change. The merge cannot settle it: that reading is plausible, but the slot it would refer to is stated nowhere.
- Condition: the instruction refers to something the report or a referenced document states (the slot), or it is not there.
- Options: (a) preferred: state the slot it refers to (e.g. the delivery of the built-up unit to the aircraft), if the story keeps it; (b) drop it.
- Needs decision: yes (cannot be settled)
- From: logistics; broad and context refuted it

### air/05#F7 · Low · English renderings of the island carrier's address tagged en-XB here, en-XL elsewhere
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB` (`Airfield Road`, Kelaro Air Cargo)
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB` (`Port Wrenfield`, Kelaro Air Cargo)
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]/@languageID` = `en-XB` (`Port Wrenfield`, Kelaro Air Cargo)
- Why: The same text of the same party carries `en-XL` in the island-issued waybill (`04-Waybill.xml:/Waybill/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL`); the tag follows the issuer's country (here a Bayvarran terminal). Counted over `*.xml`: `en-XB">Port Wrenfield` in 35 files, `en-XL">Port Wrenfield` in 27. Against (broad): the tag consistently follows the issuer's English, a legitimate reading of languageID. The merge cannot settle which rule the world follows.
- Condition: the same rendering of the same address carries the same languageID throughout the flow, by a stated rule.
- Options: (a) preferred: `en-XL` for island names everywhere; (b) the writer's variety, recorded with the world's language conventions.
- Needs decision: yes (which convention the world follows)
- From: parties; broad refuted it

### air/05#F8 · Low · The island carrier's legal form in one untagged rendering
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:CompanyLegalForm` = `Island limited company`
- XPath: `04-Waybill.xml:/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:CompanyLegalForm[1]` = `Tivufo kilika humaki`
- Why: Kelaro's legal form appears once, in English, without languageID, while the waybill Kelaro issues gives it in Lisavan and English, each tagged, and its address is rendered in both languages here. Raised by parties only as a remark inside its language-tag finding; made a finding of its own for consistency with the wood and plastics merges.
- Condition: the legal form is rendered like the party's address (both languages, tagged), or one documented rule explains the difference.
- Options: render it like the address (preferred).
- Needs decision: no
- From: parties (remark)

### air/05#F9 · Low · The same registration date 1996-01-01 for many unrelated companies
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Kelaro Air Cargo)
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Lumeport Airport Cargo Terminal)
- Why: RegistrationDate is "The registration date of the CompanyID." `1996-01-01` is the date of 25 different companies in three countries and registers (lxml over `*.xml`), in 181 example files, while other companies have individual dates. It reads as a default value ("no fillers").
- Condition: each company's RegistrationDate is its own date, or it is absent; if a common date is meant, the story states why.
- Options: (a) preferred: a date per company from its history; (b) drop it where unknown; (c) record a 1996 (re-)registration in the story.
- Needs decision: yes (company histories)
- From: parties

### air/05#F10 · Low · The carrier's contact name does not match its job title and department
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Cargo sales`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Department` = `Operations`
- Why: A `Cargo sales` contact who is an operations planner in Operations: name and title disagree (`Cargo sales` occurs in 8 files over `*.xml`). For a status report an operations contact fits, so the name is the odd part.
- Condition: name, job title and department agree and fit the carrier's role in the report.
- Options: (a) preferred: rename the contact (e.g. "Cargo operations"); (b) drop JobTitle and Department.
- Needs decision: no
- From: broad, parties

### air/05#F11 · Low · Signature aggregate without a signature
- XPath: `/TransportationStatus/cac:Signature/cbc:ID` = `LACT-SIG-TS-05`
- Why: Signature is "A signature applied to this document"; the aggregate holds only an ID and the signatory, and an automatic tracking report (`/TransportationStatus/cbc:Note` = `Automatic report from the sender's tracking system.`) is not signed in any verifiable way. The ID also ends in the example's own number (`TS-05`) rather than the signatory's numbering, like the IDs the wood and plastics merges flagged. Counted with lxml over `*.xml` in the merge: 137 of 147 Signature aggregates hold only ID and SignatoryParty.
- Condition: either a verifiable signature or no Signature aggregate; a Signature ID, where kept, is the signatory's own.
- Options: (a) preferred: drop it; (b) add signature data where the story needs it.
- Needs decision: yes (a convention across many examples)
- From: context

## Checked and consistent
- `DocumentReference/ID` `KXL-WB-26-0325` resolves to `04-Waybill.xml`, an air waybill of the same consignment `LD-CS-26-0324` and carrier Kelaro Air Cargo (`04-Waybill.xml:/Waybill/cac:CarrierParty/cac:PartyIdentification/cbc:ID` = `IC41311`); see F1 for its timing.
- The terminal operator `20412055` at `XBLMA` is the loading airport of the waybill's main carriage; coordinates 39°59.40′ S, 15°16.20′ W have minutes below 60 and directions set.
- TransportExecutionStatusCode `INPROGRESS` fits cargo accepted for a flight not yet flown; StatusPeriod 2026-05-13 agrees with the event date.
- Lumeport Airport Cargo Terminal is sender, signatory and terminal operator: consistent; ISIC `5223` fits; its tax registration (Coastal State) matches its `CountrySubentityCode` `XB-CO`; its contact `Cargo acceptance`, Operations planner, Operations fits the role. Sender (the terminal) and receiver (the carrier) fit a handling agent's report to the airline.
- Kelaro's address ID `58930746`, legal entity and contact agree with 04 (apart from F7 and F8). `+999` telephone numbers and `.example` domains cannot be mistaken for real ones.

## Considered and refuted
- `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:CitySubdivisionName` = `Old town` for an airport cargo terminal — refuted: the postal address is the company's office; the terminal is given separately as PhysicalLocation (from parties).
- `/TransportationStatus/cac:ReceiverParty`: the terminal reports to the carrier, not to the forwarder or consignor — refuted: the terminal accepted the cargo on behalf of the airline, which is the party it reports to (from parties).
- `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.` (from broad and context, refuted as the terminal's slot for delivering the built-up unit to the aircraft): the merge does not follow the refutation with certainty; see F6.
- `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]` = `Airfield Road` tagged `en-XB`, refuted by broad as the issuer's English: the merge does not follow it; see F7.

## Changed in the merge
- broad/F1, logistics/F1, context/F1 → F1: combined; the merge's refutation attempt (pre-allocated AWB numbers) added.
- broad/F2, logistics/F2, context/F2 → F2: combined; preferred option aligned with air/04#F1 (`LD-FI-26-0322`), as context proposed, with broad's and logistics' `LD-SH-26-0323` as option (b).
- logistics/F3, logistics/F4, context/F3, broad/F4 (event part) → F3: Medium; the missing time (logistics F4, Low) folded in, since it is the same element and the same fix.
- broad/F4 (location part), parties/F5, logistics/F5, context/F5 → F5: combined, split from broad's F4.
- logistics/F6 → F6: needs decision yes, with the refutation of broad and context as the counter-argument; preferred option changed from "drop" to "state the slot", as the refutation shows a plausible slot.
- parties/F2 → F7 and F8 (legal form split off, for consistency with wood and plastics).
- broad/F5, parties/F4 → F10: combined.
- context/F6 → F11: count re-made; the signature-ID remark added.

## Outside this review
- Timeline: the terminal reports the cargo accepted (issued 10:05), while `06-DespatchAdvice.xml`, the shipper's despatch advice, is issued at 10:07, and `03-ForwardingInstructions.xml` requests despatch on 13 May; whether the goods could be at the terminal by then is for the timeline review (from broad, logistics, context).
