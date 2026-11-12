# LLM review: 05-TransportationStatus.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: context

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/05-TransportationStatus.xml`, Git blob `9e63ff7c8a83c2b085bcdc225a1065a3d43ba26b` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
- Skill: `.claude/skills/ubl-example-review`, last commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### air/05#F1 · High · Reference to a waybill that is issued only later
- XPath: `/TransportationStatus/cac:DocumentReference/cbc:ID` = `KXL-WB-26-0325`
- XPath: `/TransportationStatus/cbc:IssueTime` = `10:05:00`
- XPath: `04-Waybill.xml:/Waybill/cbc:IssueTime` = `10:43:00`
- Why: The status report is issued on 13 May at 10:05 and refers to the air waybill KXL-WB-26-0325, which Kelaro issues on 13 May at 10:43, 38 minutes later (both in places with TimezoneOffset -1). At the time of the report the referenced document does not exist yet. (Whether cargo acceptance before the waybill is plausible is a timeline question; the reference to a document that did not yet exist is the finding.)
- Condition: the report refers only to documents issued before it, or is issued after the waybill.
- Options: (preferred) issue time after 10:43 (the terminal reports acceptance of cargo against the issued waybill); or refer to the forwarding instructions or the booking instead.
- Needs decision: no

### air/05#F2 · High · Shipping order ID holds the consignment ID and contradicts the forwarding instructions
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0324`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`
- Why: ShippingOrderID is "A reference number for a shipping order". The value is the consignment ID; the forwarding instructions give LD-SH-26-0323 as the shipping order. An identifier of one kind used as another, contradicting the document that defines it.
- Condition: ShippingOrderID equals the shipping order (or forwarding instruction) ID used in 03-ForwardingInstructions.xml and 04-Waybill.xml, or is absent.
- Options: (preferred) the same value as the waybill once that is fixed (LD-FI-26-0322); or drop it, as the consignment and waybill already identify the cargo.
- Needs decision: no

### air/05#F3 · Medium · Acceptance reported as a generic event without time, where a dedicated event exists
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Cargo accepted and built up for the flight.`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-13`
- Why: TransportationStatus/TransportEvent is for events "not defined elsewhere in this document". Acceptance of cargo at the terminal is defined: ShipmentStage has AcceptanceTransportEvent (and ReceiptTransportEvent), and the report already has the main-carriage stage with the terminal operator. The generic event has no time and no TransportEventTypeCode, so the status the report exists to give (when the cargo was accepted) is only in free text and to the day.
- Condition: the acceptance is reported in the dedicated event of the main-carriage stage, with date, time and location.
- Options: (preferred) `MainCarriageShipmentStage/AcceptanceTransportEvent` with date, time and the terminal location; or keep the generic event with a type code and time.
- Needs decision: no

### air/05#F4 · Medium · LocaleCode holds a language code
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) is a language and repeats Language/ID. 362 such elements over `world/examples/*/*.xml` (grep).
- Condition: LocaleCode holds a locale, or is absent.
- Options: (preferred) drop it; or a real locale code with a locale list.
- Needs decision: no

### air/05#F5 · Low · Status location named after the company
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Lumeport Airport Cargo Terminal`
- Why: StatusLocation is one of the "Locations associated with this Transportation Status report"; its name is the operator's party name (TerminalOperatorParty and SenderParty), while the event location is `Lumeport airport, cargo terminal` and the terminal's physical location carries UN/LOCODE XBLMA. The same place is named in three ways, one of them a company.
- Condition: the status location is named as a place and, where possible, identified (XBLMA), consistently with the event location.
- Options: (preferred) one location `Lumeport airport, cargo terminal` with ID XBLMA; or drop StatusLocation, as the event and the terminal already give the place.
- Needs decision: no

### air/05#F6 · Low · Signature aggregate without a signature
- XPath: `/TransportationStatus/cac:Signature/cbc:ID` = `LACT-SIG-TS-05`
- Why: Signature is "A signature applied to this document"; the aggregate holds only an ID and the signatory, with no method, attachment or extension. An automatic tracking report (Note) is not signed in any verifiable way. 131 of 133 Signature aggregates over `world/examples/*/*.xml` are like this (lxml count).
- Condition: either a verifiable signature or no Signature aggregate.
- Options: (preferred) drop it.
- Needs decision: yes (a convention across many examples)

## Checked and consistent
- Consignment LD-CS-26-0324 and carrier Kelaro Air Cargo agree with 04-Waybill.xml; the terminal operator is at Lumeport airport (XBLMA), the loading airport of the waybill.
- Sender (terminal) and receiver (carrier) fit a terminal reporting acceptance to the airline; TransportExecutionStatusCode `INPROGRESS` fits cargo accepted before departure.

## Considered and refuted
- `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`: suspected an instruction that does not fit an origin terminal — refuted: the terminal's slot for the cargo delivered to it (or for the build-up) is a delivery slot from its point of view; the carrier may need to change it.

## Outside this review
- Whether the cargo could be accepted at the terminal on 13 May before 10:05 when the despatch advice (06-DespatchAdvice.xml) is issued only at 10:07 is a timeline question across documents.
