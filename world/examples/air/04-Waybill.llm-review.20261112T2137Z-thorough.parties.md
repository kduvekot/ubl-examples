# LLM review: 04-Waybill.xml

Flow: air (AIR-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T2137Z-thorough`
- Example: `world/examples/air/04-Waybill.xml`, Git blob `df051bb647e8d343d035d6fb70ee57e379ee8b0f` (committed)
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

### air/04#F1 · Medium · Language code `en` in LocaleCode
- XPath: `/Waybill/cac:ReceiverParty/cac:Language/cbc:LocaleCode` = `en` (Bayforth Forwarding)
- XPath: `/Waybill/cac:ConsignorParty/cac:Language/cbc:LocaleCode` = `en` (Lumeway Distribution)
- Why: UBL defines `Language/cbc:LocaleCode` as "A code signifying the locale in which this language is used." A locale is a language as used in a region (such as English as used in Bayvarra), not the language itself. The value is the ISO 639 language code `en` (listID `ISO 639`), the same value the sibling `cbc:ID` already carries, so the element repeats the language instead of stating a locale. The skill's severity guide names "a language code in `LocaleCode`" as a Medium case. The same value occurs 362 times in 213 examples (`grep -rho --include='*.xml' '<cbc:LocaleCode[^<]*<' world/examples`).
- Condition: every `cbc:LocaleCode` in this example holds a locale code from a locale list (with a matching listID), or the element is absent.
- Options: (a) preferred: drop `LocaleCode` where the party has no locale beyond its language; (b) carry a real locale (e.g. a BCP 47 tag such as `en-XB`, with a listID naming that list), if the world has a reason to state the locale.
- Needs decision: no

### air/04#F2 · Medium · A gate in AdditionalStreetName of a postal address
- XPath: `/Waybill/cac:ConsignorParty/cac:PostalAddress/cbc:AdditionalStreetName` = `Gate 3` (Lumeway Distribution)
- Why: UBL defines `Address/cbc:AdditionalStreetName` as "An additional street name used to further clarify the address". `Gate 3` is not a street name but the entrance of the site where vehicles or visitors come in, i.e. information about access, not part of the postal address of Lumeway Distribution (whose street, building number, block and plot are already given). The skill's checklist for addresses: "a gate or dock is not a street name; a postal address holds nothing that only matters for vehicles." The same value occurs 79 times in 76 examples (`grep -rho --include='*.xml' '<cbc:AdditionalStreetName>Gate 3<'`).
- Condition: Lumeway Distribution's `PostalAddress` has no `AdditionalStreetName` holding a gate; where the gate matters (a pickup or delivery place), it is carried by an element meant for it (e.g. the description of the pickup or despatch `Location`), not as a street name.
- Options: (a) preferred: remove it from the postal address; (b) move it to the pickup/despatch location of the documents that need it (forwarding instructions, despatch advice).
- Needs decision: no

### air/04#F3 · Medium · Nalevi Warehousing as SubstituteCarrierParty
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cbc:IndustryClassificationCode` = `5210`
- Why: UBL defines `Consignment/cac:SubstituteCarrierParty` as "The Party who subtitutes the carrier of this Consignment." Nalevi Warehousing is a warehouse operator (ISIC `5210`, warehousing and storage), the delivery party of the order (`01-OrderChange.xml:/OrderChange/cac:Delivery/cac:DeliveryParty/cac:PartyName/cbc:Name` = `Nalevi Warehousing`) and the delivery customer of the despatch advices (`06-DespatchAdvice.xml:/DespatchAdvice/cac:DeliveryCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Nalevi Warehousing`). Nothing in the flow has it carry the goods, let alone take the place of Kelaro Air Cargo, which carries the only stage of this waybill (main carriage by air, flight `KXL207`). Its contact `Goods inwards` is a receiving contact, not a carrier's. The party seems to stand for the receiving warehouse at destination, a role the waybill names nowhere else.
- Condition: `SubstituteCarrierParty` is absent, or holds a party that actually takes over the carriage from Kelaro Air Cargo; Nalevi Warehousing, if the waybill needs it, is in a role that fits a receiving warehouse (e.g. `cac:Delivery/cac:DeliveryParty` or `cac:NotifyParty` of the consignment).
- Options: (a) preferred: move Nalevi Warehousing to the consignment's delivery or notify party, matching the order; (b) drop it from the waybill if the consignee Velumi Trading is enough; (c) if the story wants a substitute carrier (e.g. a road feeder), name that carrier instead.
- Needs decision: yes (which role Nalevi plays in the air waybill)

### air/04#F4 · Low · Issue location named after a company, without the identifier used elsewhere for the place
- XPath: `/Waybill/cac:IssueLocation/cbc:Name` = `Lumeport Airport Cargo Terminal`
- Why: `cac:IssueLocation` is the place where the waybill was issued; its `cbc:Name` is "The name of this location." The value is the trading name of a party, Lumeport Airport Cargo Terminal Ltd (`05-TransportationStatus.xml:/TransportationStatus/cac:SenderParty/cac:PartyName/cbc:Name` = `Lumeport Airport Cargo Terminal`), not the name of a place, and the location carries no identifier, although the same place is identified in this waybill as `/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:LoadingPortLocation/cbc:ID` = `XBLMA` (`Lumeport airport`). The waybill's issuer is Kelaro Air Cargo, not the terminal company, so a reader may take the location for a party.
- Condition: the issue location is named as a place (e.g. `Lumeport airport, cargo terminal`, as in `05-TransportationStatus.xml:/TransportationStatus/cac:TransportEvent/cac:Location/cbc:Name` = `Lumeport airport, cargo terminal`) and, where available, identified with UN/LOCODE `XBLMA`.
- Options: (a) preferred: name the place and add `cbc:ID` `XBLMA`; (b) keep the facility name but add the UN/LOCODE so the place is unambiguous.
- Needs decision: no

### air/04#F5 · Low · The same registration date 1996-01-01 for many unrelated companies
- XPath: `/Waybill/cac:SenderParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Kelaro Air Cargo)
- XPath: `/Waybill/cac:ReceiverParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Bayforth Forwarding)
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Velumi Trading)
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cac:PartyLegalEntity/cbc:RegistrationDate` = `1996-01-01` (Nalevi Warehousing)
- Why: UBL defines `PartyLegalEntity/cbc:RegistrationDate` as "The registration date of the CompanyID." The date `1996-01-01` (a New Year's Day) is given for 25 different companies in three countries and three registers (XB:FBR, XL:ICR, XU:CR), among them Bayforth Forwarding, Kelaro Air Cargo, Nalevi Warehousing, Velumi Trading, Selanu Airport Cargo and Lumeport Airport Cargo Terminal, while other companies of the same registers have individual dates (Lumeway Distribution `1988-10-03`, Tidewell Ocean Lines `1974-03-01`, Lisavu Cotton Farm `2009-08-17`). It occurs in 181 examples (`grep -rl --include='*.xml' '<cbc:RegistrationDate>1996-01-01<'`; companies counted by RegistrationName over all `*.xml`). Unless the world has an event that registered all these companies on that day (e.g. a register re-founded under the Trade Accord, which would not explain the XU and XB registers that have earlier dates), it reads as a default value, which the rule "no fillers" excludes.
- Condition: each company's `RegistrationDate` is its own date, consistent with its history, or it is absent; if a common date is meant, the world's story states why.
- Options: (a) give each company a date that fits its history (company histories are open work for the encyclopaedia); (b) drop `RegistrationDate` where no date is known; (c) if 1996-01-01 is an event in the story (a new register), keep it and say so there.
- Needs decision: yes (company histories)

### air/04#F6 · Low · Contact job title and department contradict the contact name
- XPath: `/Waybill/cac:SenderParty/cac:Contact/cbc:Name` = `Cargo sales`; `/Waybill/cac:SenderParty/cac:Contact/cbc:JobTitle` = `Operations planner`; `/Waybill/cac:SenderParty/cac:Contact/cbc:Department` = `Operations` (Kelaro Air Cargo)
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Name` = `Purchasing`; `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:JobTitle` = `Customer service officer`; `/Waybill/cac:Shipment/cac:Consignment/cac:ConsigneeParty/cac:Contact/cbc:Department` = `Sales` (Velumi Trading)
- XPath: `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cac:Contact/cbc:Name` = `Goods inwards`; `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cac:Contact/cbc:JobTitle` = `Customer service officer`; `/Waybill/cac:Shipment/cac:Consignment/cac:SubstituteCarrierParty/cac:Contact/cbc:Department` = `Sales` (Nalevi Warehousing)
- Why: `Contact/cbc:JobTitle` is "The job title or function of this contact" and `cbc:Department` "The department where this contact works". The functional names say what the contact does: Velumi Trading's `Purchasing` (the buyer's and consignee's contact), Nalevi Warehousing's `Goods inwards` (the contact of the party receiving the goods), Kelaro Air Cargo's `Cargo sales`. Their job titles and departments say something else: a purchasing contact working as a customer service officer in Sales, a goods-inwards contact in Sales, a cargo-sales contact as operations planner in Operations. Name, job title and department of one contact do not agree with each other, and the job title and department of the buyer's and the receiving warehouse's contact do not fit the role these parties play here. The same combinations recur for these parties in every example of the flow (and `Purchasing` with `Customer service officer`/`Sales` in 52 places over all `*.xml`, `grep -rh -A2 '<cbc:Name>Purchasing</cbc:Name>'`).
- Condition: in each contact, `Name`, `JobTitle` and `Department` describe the same function, and that function fits the party's role in the document (a buyer's contact buys, a delivery party's contact receives goods, a carrier's contact handles the transport).
- Options: (a) preferred: give each party's contact a job title and department that match its functional name (e.g. Purchasing: buyer / Purchasing; Goods inwards: warehouse supervisor / Warehouse; Cargo sales: cargo sales agent / Sales, or rename the Kelaro contact to a cargo operations desk); (b) drop `JobTitle` and `Department` where they add nothing to the functional name.
- Needs decision: no

## Checked and consistent
- Lumeway Distribution is described identically wherever it appears in full: register `20410274`, GLN `9520610900008` (check digit correct, `check_ids.py`; GS1 prefix 952 is GS1's range for demonstrations, so not a real company), customs trader `XB-TR-410274`, tax number `UL-1230822` at state level with tax scheme `STT` and jurisdiction Upland State, which matches its `CountrySubentityCode` `XB-UL`; legal entity Ltd, MEDIUM, registered 1988-10-03 in the federal business register.
- Kelaro Air Cargo is both `SenderParty` and `CarrierParty` (`IC41311`) and signs the waybill (`/Waybill/cac:Signature/cac:SignatoryParty/cac:PartyIdentification/cbc:ID` = `IC41311`): consistent for an air waybill issued by the carrier. ISIC `5120` (freight air transport) fits.
- The receiver Bayforth Forwarding is the forwarder that booked the flight (`03-ForwardingInstructions.xml:/ForwardingInstructions/cac:FreightForwarderParty/cac:PartyIdentification/cbc:ID` = `20411644`) and receives the electronic copy (`/Waybill/cac:DocumentDistribution[2]/cac:Party/cac:PartyIdentification/cbc:ID` = `20411644`).
- The consignor Lumeway Distribution and the consignee Velumi Trading match the forwarding instructions (`03-ForwardingInstructions.xml:/ForwardingInstructions/cac:ConsignorParty/cac:PartyIdentification/cbc:ID` = `20410274`).
- Selanu Airport Cargo `IC41174` in `/Waybill/cac:DocumentDistribution[1]/cac:Party/cac:PartyIdentification/cbc:ID` is the destination terminal of `09-TransportationStatus.xml:/TransportationStatus/cac:SenderParty/cac:PartyIdentification/cbc:ID` = `IC41174`.
- Telephone numbers `+999 …`: E.164 country code 999 is not assigned to any country (reserved by the ITU), so the numbers cannot be mistaken for real ones (own knowledge); web and mail domains use `.example`.

## Considered and refuted
- `/Waybill/cac:DocumentDistribution[1]/cac:Party`: the consignee's original goes to Selanu Airport Cargo, not to Velumi Trading — refuted because the consignee's original of an air waybill travels with the goods and is handed over by the destination handling agent; distributing it to that agent fits `DistributionType` `Original, with the goods: the consignee's original`.
- `/Waybill/cac:ConsignorParty`: Lumeway as consignor although the consignment has a house waybill (`/Waybill/cac:Shipment/cac:Consignment/cac:ChildConsignment/cbc:ID` = `BF-HAWB-26-0918`), where a master waybill would name the forwarder as shipper — refuted for the party lens: the parties fit a direct waybill, which `/Waybill/cbc:ConsolidatedIndicator` = `false` states; whether the child consignment and consolidated shipment fit that is a question for the logistics review.
- Kelaro Air Cargo as `SMALL` enterprise operating freight aircraft — refuted: a small island airline is plausible.
- English renderings tagged `en-XL` here; the inconsistency is recorded in the reviews of the examples that use `en-XB`.
