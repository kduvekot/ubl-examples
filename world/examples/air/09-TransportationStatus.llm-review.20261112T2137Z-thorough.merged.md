# LLM review: 09-TransportationStatus.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/09-TransportationStatus.xml`, Git blob `96f9c4474b3f63541414ff30ba5eab834320aedc` (committed)
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

### air/09#F1 · High · ShippingOrderID holds the consignment ID and contradicts the forwarding instructions
- XPath: `/TransportationStatus/cbc:ShippingOrderID` = `LD-CS-26-0324`
- XPath: `/TransportationStatus/cac:Consignment/cbc:ID` = `LD-CS-26-0324`
- XPath: `03-ForwardingInstructions.xml:/ForwardingInstructions/cbc:ShippingOrderID` = `LD-SH-26-0323`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:ChildConsignment/cbc:ConsignorAssignedID` = `LD-FI-26-0322`
- Why: ShippingOrderID is "A reference number for a shipping order". The value is the consignment's ID, given again in Consignment/ID; the forwarding instructions, the shipper's order to the forwarder, give `LD-SH-26-0323` as the shipping order (re-checked in the merge: `04-Waybill.xml` and `05-TransportationStatus.xml` carry the consignment ID as well, so the flow has two different shipping order numbers for one shipment). An identifier of one kind used as another, contradicting another example of the flow. Note that 03's own value equals its Shipment/ID; which value is the true shipping order number is settled in the reviews of 03 and 04 (the forwarding instructions' own ID `LD-FI-26-0322` is the other candidate).
- Condition: ShippingOrderID holds the same shipping order identifier as `03-ForwardingInstructions.xml` and `04-Waybill.xml` (once settled there), or is absent.
- Options: (a) preferred: the same value as 03, 04 and 05 once settled there, which the merged reviews of 03–05 prefer to be the forwarding instructions' own number `LD-FI-26-0322`; (b) `LD-SH-26-0323` everywhere; (c) drop it, since the forwarder knows the consignment ID (broad's preference).
- Needs decision: no
- From: broad (F2), logistics (F2), context (F2)

### air/09#F2 · High · Arrival on 14 May contradicts the cancellation's "next day's flight", issued five minutes earlier
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/TransportationStatus/cbc:Description` = `Cargo arrived and ready for customs clearance.`
- XPath: `/TransportationStatus/cbc:IssueTime` = `17:58:00`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:CancellationNote` = `The cargo missed its flight; it goes on the next day's flight under a new despatch advice.`
- XPath: `07-FulfilmentCancellation.xml:/FulfilmentCancellation/cbc:IssueTime` = `17:53:00`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:RequestedDepartureTransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- Why: Five minutes before this report, on 14 May at 17:53, the seller's cancellation says the cargo missed its flight and goes on the next day's flight; the only booked flight is KXL207 on 14 May 07:00 (`04-Waybill.xml`), so the next day's is 15 May. This report says the same consignment `LD-CS-26-0324` arrived at Selanu on 14 May. The merge checked the reading in which a 13 May flight was missed: then the arrival here stands, but the cancellation's "it goes on" is contradicted by this very report (see 07's review, F2). Both statements cannot be true of the same consignment.
- Condition: the arrival date reported here agrees with the flight the cargo actually took according to `04-Waybill.xml` and `07-FulfilmentCancellation.xml`.
- Options: as in 07's review, F2 (preferred there: a 13 May flight was missed and the cargo flew KXL207 on the 14th; then this report stays as it is); otherwise move the arrival to 15 May.
- Needs decision: yes (when the cargo flew)
- From: broad (F1), logistics (F1), context (F1)

### air/09#F3 · Medium · Port of Selanu as head office of a separately registered company
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cac:HeadOfficeParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:CompanyID` = `IC41174`
- Why: UBL defines `PartyLegalEntity/cac:HeadOfficeParty` as "The head office of this Legal Entity." A head office is the main office of the same legal entity, relevant when the party is a branch. Selanu Airport Cargo is its own legal entity, registered as `IC41174` in the island companies register; Port of Selanu is another company (`IC41037`, Port of Selanu Ltd in `cotton/12-WeightStatement.xml:/WeightStatement/cac:WeighingParty/cac:PartyLegalEntity/cbc:RegistrationName`). A separately registered company's owner is not its head office; UBL has `ShareholderParty` for ownership. A transportation status report also has no use for the terminal operator's corporate structure. In the merge: this is the only HeadOfficeParty in all examples (`grep -rl --include='*.xml' HeadOfficeParty world/examples`: 1 file).
- Condition: `HeadOfficeParty` is absent, or names the main office of Selanu Airport Cargo Ltd itself; ownership by the port, if meant, is expressed as ownership in a document that uses it.
- Options: (a) preferred: drop `HeadOfficeParty` from this report; (b) `cac:ShareholderParty` where ownership matters in the story; (c) if Selanu Airport Cargo is meant to be a branch of the port, it is not a separate company in the register.
- Needs decision: yes (corporate relation between the airport cargo handler and the port)
- From: parties (F1)

### air/09#F4 · Medium · The arrival is a generic event without time, while the stage has a dedicated arrival event
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:OccurrenceDate` = `2026-05-14`
- XPath: `/TransportationStatus/cac:TransportEvent/cbc:Description` = `Cargo arrived and ready for customs clearance.`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Selanu airport, cargo terminal`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cbc:ID` = `1`
- Why: TransportationStatus/TransportEvent is for "Any additional events associated with this Transportation Status report that are not defined elsewhere in this document" (definition re-checked in the merge). The arrival of the main carriage has its own element, ShipmentStage/ActualArrivalTransportEvent, and the report already has the main-carriage stage at Selanu; readiness for clearance fits AvailabilityTransportEvent. The generic event has no TransportEventTypeCode and no time, so the status the report exists to give (when the cargo arrived and became available) is free text, to the day only: it cannot be placed against the 10:00 arrival of `04-Waybill.xml` or the cancellation at 17:53, which matters given F2.
- Condition: the arrival is the main-carriage stage's ActualArrivalTransportEvent with date, time (before the issue time 17:58) and location (Selanu airport, `XLSLA`); readiness for customs, if kept, is an event with a type code (or AvailabilityTransportEvent).
- Options: (a) preferred: ActualArrivalTransportEvent plus AvailabilityTransportEvent in the stage; (b) keep the generic event with a type code and time.
- Needs decision: no
- From: broad (F3), logistics (F3, and F4 for the missing time), context (F3)

### air/09#F5 · Medium · LocaleCode holds a language code
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en`
- Why: UBL defines `Language/cbc:LocaleCode` as "A code signifying the locale in which this language is used." The value is the ISO 639 language code `en` (listID `ISO 639`), repeating the sibling `cbc:ID`. Section 6 names it a Medium case. 362 occurrences in 213 examples (re-counted in the merge).
- Condition: every `cbc:LocaleCode` in this example holds a locale code from a locale list, or the element is absent.
- Options: (a) preferred: drop `LocaleCode`; (b) a real locale (e.g. `en-XB` from a locale list).
- Needs decision: no
- From: broad (F4), parties (F2), context (F4)

### air/09#F6 · Low · "Delivery slot" that no document states
- XPath: `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.`
- Why: OtherInstruction is "An instruction regarding this message". The report goes to the forwarder, but no document of the flow gives a delivery slot (a time window for collection or delivery at Selanu), so the instruction has nothing to refer to. The broad part refuted it (the terminal books the delivery slot and the forwarder may need to change it) and the context part found it fitting; the merge agrees that the instruction fits a destination handler, but the slot it asks the forwarder to check is stated nowhere, so the forwarder cannot act on it.
- Condition: the slot the instruction refers to is stated (here or in a referenced document), or the instruction is not there.
- Options: (a) preferred: state the collection slot at the cargo terminal (e.g. as an AvailabilityTransportEvent, with F4); (b) drop the instruction.
- Needs decision: no
- From: logistics (F6); refuted by broad (Considered and refuted), counter-argument above

### air/09#F7 · Low · The same registration date 1996-01-01 for many unrelated companies
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01`
- Why: UBL defines `PartyLegalEntity/cbc:RegistrationDate` as "The registration date of the CompanyID." 1996-01-01 is given for all four companies here (Velumi Trading, Kelaro Air Cargo, Selanu Airport Cargo, Bayforth Forwarding), and for 25 companies in three registers over 181 examples (`grep -rl --include='*.xml'`, re-counted in the merge), while other companies of the same registers have individual dates. Without a story event it reads as a default value ("no fillers").
- Condition: each company's `RegistrationDate` is its own date, or it is absent; if a common date is meant, the story states why.
- Options: (a) a date per company; (b) drop it where no date is known; (c) record 1996-01-01 as a story event.
- Needs decision: yes (company histories)
- From: parties (F3)

### air/09#F8 · Low · Contact name, job title and department disagree, and do not fit the role
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Cargo sales`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:JobTitle` = `Operations planner`
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Department` = `Operations`
- Why: `Contact/cbc:JobTitle` is "The job title or function of this contact" and `cbc:Department` "The department where this contact works". The consignee's contact, the one who should collect the arrived cargo, is `Purchasing`, a customer service officer in Sales; the carrier's `Cargo sales` contact is an operations planner in Operations. Name, title and department disagree and do not fit the roles (the same combinations throughout the flow).
- Condition: in each contact, `Name`, `JobTitle` and `Department` describe the same function, and that function fits the party's role (a consignee's contact receives goods, a carrier's handles the transport).
- Options: (a) preferred: matching titles and departments, a goods-receipt contact for the consignee; (b) drop `JobTitle` and `Department`.
- Needs decision: no
- From: broad (F6), parties (F4)

### air/09#F9 · Low · Signature aggregate without a signature
- XPath: `/TransportationStatus/cac:Signature/cbc:ID` = `SAC-SIG-TS-09`
- XPath: `/TransportationStatus/cbc:Note[2]` = `Automatic report from the sender's tracking system.`
- Why: Signature is "A signature applied to this document"; the aggregate holds only an ID and the signatory, with no method, attachment or extension, in an automatic tracking report. Of 147 Signature aggregates over `world/examples/*/*.xml`, 137 hold only ID and SignatoryParty (lxml count in the merge; the context part's 131 of 133 corrected).
- Condition: either a verifiable signature or no Signature aggregate.
- Options: (a) preferred: drop it; (b) a real signature.
- Needs decision: yes (a convention across many examples)
- From: context (F6)

### air/09#F10 · Low · Status location named after the company, without the airport's identifier
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Selanu Airport Cargo`
- XPath: `/TransportationStatus/cac:SenderParty/cac:PartyName/cbc:Name` = `Selanu Airport Cargo`
- XPath: `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Selanu airport, cargo terminal`
- XPath: `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:ID` = `XLSLA`
- Why: StatusLocation is one of the "Locations associated with this Transportation Status report" and its name "The name of this location". The value is the name of the sending company and terminal operator, not of a place; the event location in the same report names the place, and the waybill identifies Selanu airport as `XLSLA`. Neither location here carries the identifier.
- Condition: the status location is named as a place and identified with `XLSLA` (UN/LOCODE), consistently with the event location.
- Options: (a) preferred: one location `Selanu airport, cargo terminal` with ID `XLSLA`; (b) drop StatusLocation.
- Needs decision: no
- From: broad (F5), logistics (F5), context (F5), parties (F5)

## Checked and consistent
- `KXL-WB-26-0325` resolves to `04-Waybill.xml`, issued 2026-05-13, before this report; consignment `LD-CS-26-0324`, carrier Kelaro Air Cargo and consignee Velumi Trading agree with it, including the `en-XL` tags (all parts).
- Selanu Airport Cargo (`IC41174`) is sender, signatory and terminal operator, and the party the waybill sends the consignee's original to (`04-Waybill.xml:/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyIdentification/cbc:ID` = `IC41174`); ISIC 5223 fits; its `Import desk` contact fits an arrival report (parties, logistics, context).
- Receiver Bayforth Forwarding is the forwarder of air/03 and air/04 and is described as in 03, 04 and 10 (logistics, parties).
- The arrival date 14 May agrees with the waybill's flight on 14 May 07:00–10:00, and the report (17:58) is after it (broad).
- Telephone numbers use the unassigned code +999 and domains `.example` (parties).

## Considered and refuted
- `/TransportationStatus/cbc:TransportExecutionStatusCode` = `INPROGRESS`: on arrival — refuted because delivery to the consignee and customs clearance are still open (from broad; logistics and context agree).
- `/TransportationStatus/cac:ReceiverParty`: the arrival report goes to the origin forwarder with its `Export desk` contact, not to the consignee — refuted: Bayforth booked the shipment and tracks it to arrival; for Bayforth it is its export shipment (from parties).
- English renderings tagged `en-XL` here — not a finding of this example; the inconsistency is recorded in the reviews of the examples that use `en-XB` (from parties).
- `/TransportationStatus/cbc:OtherInstruction` = `Reply only if the delivery slot must change.` — refuted by broad (the terminal books the delivery slot); the merge keeps logistics' finding as F6.

## Changed in the merge
- logistics/F4 (Low, missing time) folded into F4 (generic event), since broad and context already named the missing time there; the condition now requires the time.
- broad/F2 options: preference changed from "drop" to the value settled for 03–05 (`LD-FI-26-0322`, as the merged reviews of 03–05 prefer; context proposed the same), in line with the merger of 01–05; `LD-SH-26-0323` (logistics) and drop (broad) kept as options (b) and (c).
- context/F6 → F9: count corrected to 137 of 147 (lxml count in the merge).
- broad/F5, logistics/F5, context/F5, parties/F5 → F10: combined.
- broad/F6 and parties/F4 → F8: combined, Department values added.

## Outside this review
- Customs: "ready for customs clearance" in Lisavu, but the air flow has no import declaration. Whether one belongs in the flow is a question about the flow's documents, not this report (from broad).
