# LLM review: 09-TransportationStatus.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/09-TransportationStatus.xml`, Git blob `96f9c4474b3f63541414ff30ba5eab834320aedc` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit cde747e 2026-11-12 Reviews of the plastics flow, run 20261112T2101Z-thorough: merge complete
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

### air/09#F1 · Medium · Port of Selanu as head office of a separately registered company
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cac:HeadOfficeParty/cac:PartyName/cbc:Name` = `Port of Selanu`
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:CompanyID` = `IC41174`
- Why: UBL defines `PartyLegalEntity/cac:HeadOfficeParty` as "The head office of this Legal Entity." A head office is the main office of the same legal entity, relevant when the party is a branch. Selanu Airport Cargo is its own legal entity, a limited company with its own registration `IC41174` in the island companies register; Port of Selanu is another company (`IC41037`, Port of Selanu Ltd in `cotton/12-WeightStatement.xml:/WeightStatement/cac:WeighingParty/cac:PartyLegalEntity/cbc:RegistrationName`). A separately registered company's parent or owner is not its head office; UBL has `ShareholderParty` under the legal entity for ownership. Port of Selanu is also a seaport company, which makes it doubtful as the head office of an airport cargo handler. Nor does a transportation status report have any use for the terminal operator's corporate structure.
- Condition: `HeadOfficeParty` is absent, or names the main office of Selanu Airport Cargo Ltd itself; if the port company owns the terminal operator, that is expressed (if at all) as ownership, not as head office.
- Options: (a) preferred: drop `HeadOfficeParty` from this report; (b) if ownership matters in the story, use `cac:ShareholderParty` in a document where it is used; (c) if Selanu Airport Cargo is meant to be a branch of the port, it should not be a separate company in the register.
- Needs decision: yes (corporate relation between the airport cargo handler and the port)

### air/09#F2 · Medium · Language code `en` in LocaleCode
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en` (Bayforth Forwarding)
- Why: UBL defines `Language/cbc:LocaleCode` as "A code signifying the locale in which this language is used." A locale is a language as used in a region (such as English as used in Bayvarra), not the language itself. The value is the ISO 639 language code `en` (listID `ISO 639`), the same value the sibling `cbc:ID` already carries, so the element repeats the language instead of stating a locale. The skill's severity guide names "a language code in `LocaleCode`" as a Medium case. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^<]*<' world/examples`).
- Condition: every `cbc:LocaleCode` in this example holds a locale code from a locale list (with a matching listID), or the element is absent.
- Options: (a) preferred: drop `LocaleCode` where the party has no locale beyond its language; (b) carry a real locale (e.g. a BCP 47 tag such as `en-XB`, with a listID naming that list), if the world has a reason to state the locale.
- Needs decision: no

### air/09#F3 · Low · The same registration date 1996-01-01 for many unrelated companies
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Velumi Trading)
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Kelaro Air Cargo)
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Selanu Airport Cargo)
- XPath: `/TransportationStatus/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Bayforth Forwarding)
- Why: UBL defines `PartyLegalEntity/cbc:RegistrationDate` as "The registration date of the CompanyID." The date `1996-01-01` (a New Year's Day) is given for 25 different companies in three countries and three registers (XB:FBR, XL:ICR, XU:CR), among them Bayforth Forwarding, Kelaro Air Cargo, Nalevi Warehousing, Velumi Trading, Selanu Airport Cargo and Lumeport Airport Cargo Terminal, while other companies of the same registers have individual dates (Lumeway Distribution `1988-10-03`, Tidewell Ocean Lines `1974-03-01`, Lisavu Cotton Farm `2009-08-17`). It occurs in 181 examples (`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`; companies counted by RegistrationName over all `*.xml`). Unless the world has an event that registered all these companies on that day (e.g. a register re-founded under the Trade Accord, which would not explain the XU and XB registers that have earlier dates), it reads as a default value, which the rule "no fillers" excludes.
- Condition: each company's `RegistrationDate` is its own date, consistent with its history, or it is absent; if a common date is meant, the world's story states why.
- Options: (a) give each company a date that fits its history (company histories are open work for the encyclopaedia); (b) drop `RegistrationDate` where no date is known; (c) if 1996-01-01 is an event in the story (a new register), keep it and say so there.
- Needs decision: yes (company histories)

### air/09#F4 · Low · Contact job title and department contradict the contact name
- XPath: `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`; `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`; `/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales` (Velumi Trading)
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Cargo sales`; `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:JobTitle` = `Operations planner`; `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Department` = `Operations` (Kelaro Air Cargo)
- Why: `Contact/cbc:JobTitle` is "The job title or function of this contact" and `cbc:Department` "The department where this contact works". The functional name says what the contact does, but its job title and department say something else: Kelaro Air Cargo's `Cargo sales` contact (the carrier's contact) is an operations planner in Operations, so either the name or the title is wrong; Velumi Trading's `Purchasing` contact (the buyer's or consignee's contact) is a customer service officer in Sales. Name, job title and department of one contact do not agree with each other, and they do not show which function fits the party's role here. The same combinations recur for these parties in every example of the flow (and `Purchasing` with `Customer service officer`/`Sales` in 52 places over all `*.xml`, `grep -rh -A2 '<cbc:Name>Purchasing</cbc:Name>'`).
- Condition: in each contact, `Name`, `JobTitle` and `Department` describe the same function, and that function fits the party's role in the document (a buyer's contact buys, a delivery party's contact receives goods, a carrier's contact handles the transport).
- Options: (a) preferred: give each party's contact a job title and department that match its functional name (e.g. Purchasing: buyer / Purchasing; Goods inwards: warehouse supervisor / Warehouse; Cargo sales: cargo sales agent / Sales, or rename the Kelaro contact to a cargo operations desk); (b) drop `JobTitle` and `Department` where they add nothing to the functional name.
- Needs decision: no

### air/09#F5 · Low · Status location named after the terminal company, without identifier
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Selanu Airport Cargo`
- Why: `cac:StatusLocation/cbc:Name` is "The name of this location". The value is the name of the sending company (`/TransportationStatus/cac:SenderParty/cac:PartyName/cbc:Name` = `Selanu Airport Cargo`), not of a place. The transport event in the same report names the place (`/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Selanu airport, cargo terminal`), and the waybill identifies Selanu airport as `04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:UnloadingPortLocation/cbc:ID` = `XLSLA`.
- Condition: the status location is named as a place and, where available, identified with UN/LOCODE `XLSLA`, consistently with the transport event's location.
- Options: (a) preferred: use the transport event's place name and add `cbc:ID` `XLSLA`; (b) keep a facility name that is a place name and add the identifier.
- Needs decision: no

## Checked and consistent
- Selanu Airport Cargo (`IC41174`) is sender, signatory and terminal operator: consistent; ISIC `5223` fits; it is the party that received the consignee's original of the waybill (`04-Waybill.xml:/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyIdentification/cbc:ID` = `IC41174`). Its contact `Import desk`, Operations planner, Operations is consistent and fits an arrival report.
- Consignee Velumi Trading and carrier Kelaro Air Cargo agree with the referenced waybill (`04-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyIdentification/cbc:ID` = `IC41859`), including the `en-XL` language tags.
- Receiver Bayforth Forwarding is described as in 03, 04 and 10.
- Telephone numbers `+999 …`: E.164 country code 999 is not assigned to any country (reserved by the ITU), so the numbers cannot be mistaken for real ones (own knowledge); web and mail domains use `.example`.

## Considered and refuted
- `/TransportationStatus/cac:ReceiverParty`: the arrival report goes to the origin forwarder with its `Export desk` contact, not to the consignee — refuted: Bayforth booked the shipment and tracks it to arrival; for Bayforth this is its export shipment.
- English renderings tagged `en-XL` here; the inconsistency is recorded in the reviews of the examples that use `en-XB`.
