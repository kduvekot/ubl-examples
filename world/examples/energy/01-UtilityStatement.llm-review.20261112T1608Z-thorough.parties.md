# LLM review: 01-UtilityStatement.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: parties

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/01-UtilityStatement.xml`, Git blob `ddb038e38819569df4aa78c5bfc77925766f9bb9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 10e2be1 2026-11-12 Reviews of the ore flow, run 20261112T1527Z-thorough: merged reviews written so far
- Skill: `.claude/skills/ubl-example-review`, last commit 5b25ab8 2026-11-12 Review skill: several flows in one run (one run ID, each part over all of them, one merge per flow) (committed)
- Model: UBL 2.5, UBL-Entities-2.5.gc (SHA-256 c7df070e…fe988d1)

## What is expected
This is one review among possibly several of this example (other runs and parts; list them with
`list_reviews.py`). Whoever works through the reviews considers every one of them: runs find partly
different things, and a finding that appears in only one review counts as much as one that appears
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes what
is wrong; it does not say where or how the example is produced.

## Findings

### energy/01#F1 · Medium · CustomerParty repeats the ReceiverParty
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-105781`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyIdentification/cbc:ID` = `XU-R-105781`
- Why: UBL defines `UtilityStatement/CustomerParty` as "The buyer, if different from the receiver of the document." Here the customer is Ferrano Energy, the same party as the ReceiverParty, so the condition of the definition is not met and the aggregate states nothing the receiver does not already state. The same pattern (CustomerParty ID equal to ReceiverParty ID) occurs in utilities/01-UtilityStatement.xml, utilities/05-UtilityStatement.xml and utilities/12-UtilityStatement.xml (compared with lxml over the six `*UtilityStatement.xml` files).
- Condition: `cac:CustomerParty` is present only when it names a party other than the `cac:ReceiverParty`.
- Options: (a) preferred: leave `cac:CustomerParty` out, since the retailer receiving the statement is the buyer of the grid service; (b) keep it only if the story has a buyer different from the receiver (e.g. the statement goes to a billing agent).
- Needs decision: no

### energy/01#F2 · Medium · Province held in Region
- XPath: `/UtilityStatement/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political/administrative division of the country, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located"). The Bayvarran addresses of the same flow use `CountrySubentity`/`CountrySubentityCode` for their states (e.g. `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:CountrySubentity` = `Northern Territory`), so the two countries' first-level divisions are encoded in different elements. `Province of Ferrano` occurs 219 times in 104 of the 250 `*.xml` examples, always in `cbc:Region` (lxml count over `world/examples/*/*.xml`).
- Condition: no Urvanian address carries its province in `cbc:Region`; the province is in `cbc:CountrySubentity` (with a code in `cbc:CountrySubentityCode` where a list exists).
- Options: (a) preferred: move the province to `CountrySubentity` (and add the Urvanian subentity code), as is done for Bayvarra; (b) keep `Region` only for a real region in UBL's sense (e.g. an economic region of the Trade Accord), if the story has one.
- Needs decision: no

### energy/01#F3 · Low · Contacts that do not fit the parties' roles in a utility statement
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:Contact/cbc:Department` = `Sales`
- Why: The receiver of the grid operator's metering statement is Ferrano Energy acting as buyer of the grid service and as biller of its customer; its contact for this document would be the billing or energy-data desk, not customer service in Sales. The subscriber Valdara's contact is its order desk in Sales, which sells furniture; for a gas consumption point the contact would be the plant's facility or energy management. Both look like the party's general master-data contact.
- Condition: each party's contact in this document is one that deals with metering, consumption or billing of the utility.
- Options: (a) preferred: give the receiver a billing/settlement contact and the subscriber a facilities or energy contact; (b) leave the contacts out where the document does not need them.
- Needs decision: no

### energy/01#F4 · Low · Subscriber master data the statement does nothing with
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:Contact/cac:OtherCommunication/cbc:Value` = `+999 1 344 474 4274`
- Why: A utility statement reports consumption at a consumption point. Valdara's customs trader number, its share listing on the Ferrano Stock Exchange and its logistics service provider for "Warehousing and despatch" play no part in metering gas for the coating line; they look copied from the party's master data (section 4.8 of the review rules). The ISIN check digit is correct (check_ids.py), so this is about presence only.
- Condition: the subscriber carries only data the utility statement uses (identity, address, contact for the consumption point).
- Options: (a) preferred: leave these four out of the subscriber; (b) keep one only if the story gives it a reason in this document.
- Needs decision: no

### energy/01#F5 · Low · Industry classification leaves out the gas business
- XPath: `/UtilityStatement/cac:SenderParty/cbc:IndustryClassificationCode` = `3510`
- XPath: `/UtilityStatement/cac:ReceiverParty/cbc:IndustryClassificationCode` = `3510`
- Why: ISIC Rev.4 3510 is "Electric power generation, transmission and distribution". This statement is a gas statement: the sender Ferrano Grid owns and reads the gas meter (`/UtilityStatement/cbc:Note[2]`) and bills gas network use in `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cac:Item/cbc:Name[2]` = `Gas network use`, and the receiver Ferrano Energy sells gas to Valdara and buys gas in `07-Invoice.xml`. Distribution of gaseous fuels through mains, and their sale, is ISIC 3520 (own knowledge of ISIC Rev.4). The code is not wrong, but incomplete for parties whose gas activity is what this document is about.
- Condition: the industry classification of Ferrano Grid and Ferrano Energy covers their gas activity (e.g. 3520 next to 3510), the same way in every example of the flow.
- Options: (a) preferred: add a second `IndustryClassificationCode` 3520 to both parties (the element repeats); (b) leave it as is if the world intends the parties to be classified by their main activity only, and record that.
- Needs decision: no

## Checked and consistent
- Sender Ferrano Grid (`XU-R-106055`) is described identically here and in `02-Invoice.xml:/Invoice/cac:AccountingSupplierParty/cac:Party` (51 leaf values compared); receiver Ferrano Energy (`XU-R-105781`) identically here and in 02 and 03.
- The note says the grid operator owns and reads the meter; the sender is the grid operator, its contact is the metering office, and the meter number `FG-G-20417` carries the grid operator's prefix.
- `SubscriberParty` is Valdara, the party consuming the gas at the consumption point whose address is Valdara's own (`Bek Stuzman Nulban` / `Via delle Officine` 17, 4120 Ferrano); `SubscriberID` `FE-C-0047121` is the retailer's customer number, which fits "an identifier for the subscriber responsible for the consumption".
- Legal entities: all three are SUA in the Urvanian commercial register, with register ID equal to `PartyIdentification`, registration and tax names agreeing, and legal form text agreeing with the code; Valdara (LARGE, listed) and Ferrano Energy (LARGE) are plausible sizes.
- check_ids.py: ISIN `XU0001042501` correct.

## Considered and refuted
- `/UtilityStatement/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]`: an Italian-form name (`Via della Rete`) tagged `en-XU` — refuted because Urvanian place names keep their Italianate form in English across the world (town names in both languages are a world convention), so the rendering is the Urvanian English name.
- `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `MEDIUM`: a provincial grid operator could be large — refuted because nothing in the flow gives staff or turnover, and a provincial distribution company of medium size is plausible.
- `/UtilityStatement/cac:SenderParty/cac:Language/cbc:ID` = `qau` with schemeID `ISO 639`: refuted because `qau` lies in the ISO 639 range reserved for local use (qaa–qtz), so it cannot be mistaken for a real language.
- `/UtilityStatement/cac:SenderParty/cac:Contact/cbc:Telephone` and the ISO 6523 identifier `0990:10605`: possible clash with real registers — refuted because +999 is not an assigned ITU country code and ICD 0990 is not assigned in ISO 6523 (own knowledge).
