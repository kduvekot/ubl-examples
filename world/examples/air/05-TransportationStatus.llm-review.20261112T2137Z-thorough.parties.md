# LLM review: 05-TransportationStatus.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: parties

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
in all. Every finding below, and every entry under "Considered and refuted", "Refuted in the merge"
and "Outside this review", is looked into and ends either resolved (its condition holds) or
dismissed with a stated reason. Findings marked "Needs decision: yes" are confirmed by a person
first. The example must remain valid against the UBL 2.5 schemas and the world's code lists. This
review only describes what is wrong; it does not say where or how the example is produced.

## Findings

### air/05#F1 · Medium · Language code `en` in LocaleCode
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:Language/cbc:LocaleCode` = `en` (Lumeport Airport Cargo Terminal)
- Why: UBL defines `Language/cbc:LocaleCode` as "A code signifying the locale in which this language is used." A locale is a language as used in a region (such as English as used in Bayvarra), not the language itself. The value is the ISO 639 language code `en` (listID `ISO 639`), the same value the sibling `cbc:ID` already carries, so the element repeats the language instead of stating a locale. The skill's severity guide names "a language code in `LocaleCode`" as a Medium case. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^<]*<' world/examples`).
- Condition: every `cbc:LocaleCode` in this example holds a locale code from a locale list (with a matching listID), or the element is absent.
- Options: (a) preferred: drop `LocaleCode` where the party has no locale beyond its language; (b) carry a real locale (e.g. a BCP 47 tag such as `en-XB`, with a listID naming that list), if the world has a reason to state the locale.
- Needs decision: no

### air/05#F2 · Low · English renderings of island addresses tagged en-XB here, en-XL elsewhere
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XB` (`Airfield Road`, Kelaro Air Cargo)
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XB` (`Port Wrenfield`, Kelaro Air Cargo)
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cac:RegistrationAddress/cbc:CityName[2]/@languageID` = `en-XB` (`Port Wrenfield`, Kelaro Air Cargo)
- Why: the English renderings of the addresses of island parties (Velumi Trading, Nalevi Warehousing, Kelaro Air Cargo) carry `languageID` `en-XB` (English as used in Bayvarra) in this example, but `en-XL` (English as used in Lisavu) for the same text of the same parties in other examples of the flow, e.g. `01-OrderChange.xml:/OrderChange/cac:BuyerCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XL`, `04-Waybill.xml:/Waybill/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]/@languageID` = `en-XL` and `09-TransportationStatus.xml:/TransportationStatus/cac:Consignment/cac:ConsigneeParty/cac:PostalAddress/cbc:CityName[2]/@languageID` = `en-XL`. The tag seems to follow the country of the issuer, not the address. The text is identical in both cases; `Port Wrenfield` and the street names are the island's own English names, which argues for `en-XL` everywhere. Across all examples, `languageID="en-XB">Port Wrenfield` occurs in 35 examples and `languageID="en-XL">Port Wrenfield` in 27 (`grep -rl --include='*.xml'`). Related: in this example the island parties' `CompanyLegalForm` appears in English only, without `languageID`, where island-issued examples give it in `qal` and `en-XL`.
- Condition: the same rendering of the same address carries the same `languageID` in every example of the flow, chosen by a stated rule (the language variety of the place, or of the writer).
- Options: (a) preferred: tag the English renderings of island addresses `en-XL` everywhere, since they are island names; (b) keep the writer's variety, and record that rule where the world's language conventions are written down.
- Needs decision: yes (which convention the world follows)

### air/05#F3 · Low · The same registration date 1996-01-01 for many unrelated companies
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Kelaro Air Cargo)
- XPath: `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Lumeport Airport Cargo Terminal)
- Why: UBL defines `PartyLegalEntity/cbc:RegistrationDate` as "The registration date of the CompanyID." The date `1996-01-01` (a New Year's Day) is given for 25 different companies in three countries and three registers (XB:FBR, XL:ICR, XU:CR), among them Bayforth Forwarding, Kelaro Air Cargo, Nalevi Warehousing, Velumi Trading, Selanu Airport Cargo and Lumeport Airport Cargo Terminal, while other companies of the same registers have individual dates (Lumeway Distribution `1988-10-03`, Tidewell Ocean Lines `1974-03-01`, Lisavu Cotton Farm `2009-08-17`). It occurs in 181 examples (`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`; companies counted by RegistrationName over all `*.xml`). Unless the world has an event that registered all these companies on that day (e.g. a register re-founded under the Trade Accord, which would not explain the XU and XB registers that have earlier dates), it reads as a default value, which the rule "no fillers" excludes.
- Condition: each company's `RegistrationDate` is its own date, consistent with its history, or it is absent; if a common date is meant, the world's story states why.
- Options: (a) give each company a date that fits its history (company histories are open work for the encyclopaedia); (b) drop `RegistrationDate` where no date is known; (c) if 1996-01-01 is an event in the story (a new register), keep it and say so there.
- Needs decision: yes (company histories)

### air/05#F4 · Low · Contact job title and department contradict the contact name
- XPath: `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Name` = `Cargo sales`; `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:JobTitle` = `Operations planner`; `/TransportationStatus/cac:Consignment/cac:CarrierParty/cac:Contact/cbc:Department` = `Operations` (Kelaro Air Cargo)
- Why: `Contact/cbc:JobTitle` is "The job title or function of this contact" and `cbc:Department` "The department where this contact works". The functional name says what the contact does, but its job title and department say something else: Kelaro Air Cargo's `Cargo sales` contact (the carrier's contact) is an operations planner in Operations, so either the name or the title is wrong. Name, job title and department of one contact do not agree with each other, and they do not show which function fits the party's role here. The same combinations recur for these parties in every example of the flow (and `Purchasing` with `Customer service officer`/`Sales` in 52 places over all `*.xml`, `grep -rh -A2 '<cbc:Name>Purchasing</cbc:Name>'`).
- Condition: in each contact, `Name`, `JobTitle` and `Department` describe the same function, and that function fits the party's role in the document (a buyer's contact buys, a delivery party's contact receives goods, a carrier's contact handles the transport).
- Options: (a) preferred: give each party's contact a job title and department that match its functional name (e.g. Purchasing: buyer / Purchasing; Goods inwards: warehouse supervisor / Warehouse; Cargo sales: cargo sales agent / Sales, or rename the Kelaro contact to a cargo operations desk); (b) drop `JobTitle` and `Department` where they add nothing to the functional name.
- Needs decision: no

### air/05#F5 · Low · Status location named after the terminal company, without identifier
- XPath: `/TransportationStatus/cac:StatusLocation/cbc:Name` = `Lumeport Airport Cargo Terminal`
- Why: `cac:StatusLocation` is the place the status applies to, and its `cbc:Name` is "The name of this location." The value is the name of the sending party (`/TransportationStatus/cac:SenderParty/cac:PartyName/cbc:Name` = `Lumeport Airport Cargo Terminal`), not of a place. The same place is named as a place in `/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Lumeport airport, cargo terminal` and identified in the terminal operator's `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PhysicalLocation/cbc:ID` = `XBLMA`; the status location carries neither.
- Condition: the status location is named as a place and, where available, identified (UN/LOCODE `XBLMA`), consistently with the transport event's location.
- Options: (a) preferred: use the place name of the transport event and add `cbc:ID` `XBLMA`; (b) keep the facility name and add the identifier.
- Needs decision: no

## Checked and consistent
- Lumeport Airport Cargo Terminal (`20412055`) is sender, signatory and terminal operator of the main carriage: consistent; ISIC `5223` (service activities incidental to air transportation) fits; its tax registration (state level, Coastal State) matches its `CountrySubentityCode` `XB-CO`.
- The receiver and the carrier are Kelaro Air Cargo, as in the referenced waybill (`04-Waybill.xml:/Waybill/cac:CarrierParty/cac:PartyIdentification/cbc:ID` = `IC41311`); its address ID `58930746`, legal entity and contact agree with 04 (apart from the language tags, see the finding on `en-XB`).
- Contact of the terminal operator: `Cargo acceptance`, Operations planner, Operations: consistent with each other and with the role (accepting cargo for the flight).
- Telephone numbers `+999 …`: E.164 country code 999 is not assigned to any country (reserved by the ITU), so the numbers cannot be mistaken for real ones (own knowledge); web and mail domains use `.example`.

## Considered and refuted
- `/TransportationStatus/cac:Consignment/cac:MainCarriageShipmentStage/cac:TerminalOperatorParty/cac:PostalAddress/cbc:CitySubdivisionName` = `Old town` for an airport cargo terminal — refuted: the postal address is the company's office, which may lie in the old town; the terminal itself is given separately as `PhysicalLocation`.
- `/TransportationStatus/cac:ReceiverParty`: the terminal reports to the carrier, not to the forwarder or consignor — refuted: the terminal accepted the cargo on behalf of the airline, which is the party it reports to.
