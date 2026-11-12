# LLM review: 01-UtilityStatement.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: merged

## Reviewed version
- Run: `20261112T1608Z-thorough`
- Example: `world/examples/energy/01-UtilityStatement.xml`, Git blob `ddb038e38819569df4aa78c5bfc77925766f9bb9` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit dadf784 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: parts written so far; citations.py resolves review paths, so relative paths work for citations into other flows
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

### energy/01#F1 · High · Amount payable on the consumption is 0, but the parent invoice bills this consumption
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `0`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:TotalConsumedQuantity` = `61200`
- XPath: `/UtilityStatement/cac:ParentDocumentReference/cbc:ID` = `FG-INV-26-0150`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:InvoicedQuantity` = `61200`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:LineExtensionAmount` = `116280`
- Why: `Consumption/LegalMonetaryTotal` is "The total amount payable on this consumption, including any allowances, charges, or taxes", and the Utility Statement is "A supplement to an Invoice or Credit Note". The parent invoice FG-INV-26-0150 (02-Invoice.xml) bills exactly this consumption point's 61200 kWh as gas network use: 61200 × 1.9 = 116280 XUF net, 20 % VAT 23256, 139536 XUF including tax (recalculated in the merge). The statement says nothing is payable on the same consumption, so the two documents contradict each other; the zero looks like a filler for the mandatory element (IND5/IND6). The note ("Metered consumption for the retail company's billing") explains why the statement exists, not why nothing would be payable. Reading the statement as pure metering data does not help: the mandatory total still asks for the amount payable on this consumption, which the parent invoice fixes.
- Condition: the amount payable on this consumption in the statement agrees with what the parent invoice charges for it (139536 XUF including tax, or a stated net basis matching line 3), or the statement no longer presents itself as the supplement of an invoice that bills this consumption.
- Options: (a) preferred: PayableAmount 139536 XUF, optionally with LineExtensionAmount and TaxExclusiveAmount 116280 and TaxInclusiveAmount 139536, so the statement reconciles with line 3 of the invoice (broad, money, context agree); (b) if the statement is meant only as metering data for the retailer's own billing, attach it to the invoice that bills the consumption to the subscriber (utilities flow) with that invoice's amount, changing the parent reference and the story.
- Needs decision: no
- From: broad F1, money F1, context F1

### energy/01#F2 · Medium · CustomerParty is the same party as the receiver
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-105781`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyIdentification/cbc:ID` = `XU-R-105781`
- Why: `UtilityStatement/CustomerParty` is "The buyer, if different from the receiver of the document." Here it is Ferrano Energy, the receiver itself, so the condition of the definition is not met and the aggregate states nothing the receiver does not. The same pattern (CustomerParty ID equal to ReceiverParty ID) occurs in 4 of the 6 `*UtilityStatement.xml` examples: energy/01, utilities/01, utilities/05, utilities/12 (lxml comparison by the parties and context parts).
- Condition: CustomerParty is absent, or names a party different from ReceiverParty.
- Options: (a) preferred: omit CustomerParty, since the retailer receiving the statement is the buyer of the network service; (b) keep it only if the story has a buyer different from the receiver (e.g. a billing agent receives the statement). Valdara is not a candidate: it is already SubscriberParty.
- Needs decision: no
- From: broad F2, parties F1, context F2

### energy/01#F3 · Medium · Province held in Region
- XPath: `/UtilityStatement/cac:SenderParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:PostalAddress/cbc:Region` = `Province of Ferrano`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:Address/cbc:Region` = `Province of Ferrano`
- Why: `Address/Region` is "The recognized geographic or economic region or group of countries in which this address is located"; a province is a political/administrative division, which UBL puts in `CountrySubentity` ("The political or administrative division of a country in which this address is located"). The Bayvarran addresses of the same flow use `CountrySubentity`/`CountrySubentityCode` for their states (e.g. `04-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:ExporterParty/cac:PostalAddress/cbc:CountrySubentity` = `Northern Territory`). The Urvanian address format (AddressFormatCode `XU`) puts `Region` on the last line, so this is a world convention, but the value still names an administrative division. `Province of Ferrano` occurs 219 times in 104 of the 250 `*.xml` examples, always in `cbc:Region` (counts of the broad and parties parts).
- Condition: no Urvanian address carries its province in `cbc:Region`; the province is in `cbc:CountrySubentity` (with a code in `CountrySubentityCode` where a list exists), or the world states that Urvanian provinces are economic regions, not administrative divisions.
- Options: (a) preferred: move the province to `CountrySubentity` (with a code, like Bayvarra's states) and update the XU address format; (b) keep `Region` only for a real region in UBL's sense (e.g. an economic region of the Trade Accord).
- Needs decision: no
- From: broad F3, parties F2

### energy/01#F4 · Medium · ConsumptionEnergyQuantity is defined for district heating, used for gas
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity` = `61200`
- Why: UBL 2.5 defines `Consumption Correction. Consumption Energy. Quantity` as "Your consumpt for district heating energy." (verified in the model in the merge). The statement is for gas (`/UtilityStatement/cbc:UtilityStatementTypeCode` = `GAS`), and the energy content is already in `ConsumptionReport/TotalConsumedQuantity` and in the correction's Description. Under the semantic-conformance rule the element is used outside its definition. The definition looks like a drafting defect (truncated "consumpt", and nothing in the aggregate is otherwise specific to district heating), so it may be a finding for the UBL TC. The element occurs in 2 `*.xml` examples: this one and utilities/03-UtilityStatement.xml.
- Condition: the element is absent from a gas statement or carries district heating energy, or the deviation is recorded as a finding on the UBL definition in `analysis/codelist-decisions.md`.
- Options: (a) preferred by the context part: drop it, since TotalConsumedQuantity and the Description already carry the energy; (b) preferred by the broad part if the owner agrees the definition is a defect: keep it and record the definition problem as a finding for the TC; (c) cover it only through a district heating consumption elsewhere in the world.
- Needs decision: yes (whether the UBL definition is taken literally or recorded as a defect is the owner's call)
- From: broad F4, context F3

### energy/01#F5 · Low · Statement issued before the invoice it supplements
- XPath: `/UtilityStatement/cbc:IssueDate` = `2026-04-02`
- XPath: `/UtilityStatement/cbc:IssueTime` = `17:42:00`
- XPath: `/UtilityStatement/cac:ParentDocumentReference/cbc:ID` = `FG-INV-26-0150`
- XPath: `02-Invoice.xml:/Invoice/cbc:IssueDate` = `2026-04-03`
- XPath: `02-Invoice.xml:/Invoice/cbc:IssueTime` = `08:20:00`
- Why: the statement is "a supplement to an Invoice or Credit Note" and `ParentDocumentReference` is "a reference to the parent Invoice or Credit Note". At the statement's issue time (2026-04-02 17:42) the parent invoice does not exist yet; it is issued the next morning (2026-04-03 08:20). An invoice number reserved in the same billing run can be referenced in advance (the context part refuted the finding on that ground), so this is no contradiction; but the statement then points to a document nobody can retrieve yet, and the invoice does not refer back to the statement (energy/02#F2). Counted by the logistics part over `*UtilityStatement.xml`: 2 of 6 statements are issued before their parent invoice (this one and utilities/08-UtilityStatement.xml).
- Condition: the statement's issue date and time are not earlier than those of its parent invoice, or the story says why the invoice number is known in advance.
- Options: (a) preferred: issue the statement on or after 2026-04-03 08:20, or the invoice before the statement; (b) keep the order and let the invoice carry a reference to the statement, so the link exists in both directions once both are issued.
- Needs decision: no
- From: broad F5, logistics F1 (context listed it as refuted)

### energy/01#F6 · Low · Subscriber master data the statement does nothing with
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:ServiceProviderParty/cbc:ID` = `VI-SP-2026-01`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:ServiceProviderParty/cac:Party/cac:PartyName/cbc:Name` = `Castrano Logistics`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:Contact/cac:OtherCommunication/cbc:Value` = `+999 1 344 474 4274`
- Why: a utility statement reports consumption at a consumption point. Valdara's customs trader number, its share listing on the Ferrano Stock Exchange, its logistics service provider for "Warehousing and despatch" and the alternative contact channel play no part in metering gas for the coating line; they look copied from the party's master data (section 4.8). The ISIN check digit is correct (`check_ids.py`), so this is about presence only.
- Condition: every aggregate of SubscriberParty has a use in this statement (identity, address, a contact for the consumption point), or the statement's purpose explains it.
- Options: (a) preferred: leave these out of this document; (b) keep one only with a reason in the story (e.g. a note that the logistics provider operates the connection).
- Needs decision: no
- From: broad F6, parties F4, context F4

### energy/01#F7 · Low · Contacts do not fit the roles in a metering statement
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Name` = `Customer service`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Contact/cbc:Department` = `Sales`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:Contact/cbc:Name` = `Order desk`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:Contact/cbc:Department` = `Sales`
- Why: the receiver (the retailer) uses the statement to bill its customer; its contact for this document would be its billing or energy-data desk, not customer service in Sales. The subscriber Valdara's contact is its order desk in Sales, which takes furniture orders; for a gas connection it would be facility or energy management. Both look like the parties' general master-data contacts. The sender's metering office fits.
- Condition: the receiver's and subscriber's contacts are ones that deal with metering, consumption or billing of the connection.
- Options: (a) preferred: role-specific contacts (retailer's billing/settlement, subscriber's facility or energy management); (b) omit the contacts the document does not need.
- Needs decision: no
- From: broad F7, parties F3

### energy/01#F8 · Low · Industry classification covers electricity only, but the document is about gas
- XPath: `/UtilityStatement/cac:SenderParty/cbc:IndustryClassificationCode` = `3510`
- XPath: `/UtilityStatement/cac:ReceiverParty/cbc:IndustryClassificationCode` = `3510`
- Why: ISIC Rev.4 3510 is "Electric power generation, transmission and distribution"; distribution of gaseous fuels through mains, and their sale, is 3520 (own knowledge of ISIC). Ferrano Grid owns and reads the gas meter (`/UtilityStatement/cbc:Note[2]`) and bills gas network use (`02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cac:Item/cbc:Name[2]` = `Gas network use`); Ferrano Energy sells gas to Valdara and buys gas (07-Invoice.xml). The context part refuted this for the sender because 3510 can be its main activity; that is a fair reading, so the finding is about completeness only.
- Condition: the industry classification of Ferrano Grid and Ferrano Energy covers their gas activity (e.g. 3520 next to 3510), the same way in every example of the flow, or the world states that parties are classified by their main activity only.
- Options: (a) preferred: add a second `IndustryClassificationCode` 3520 (the element repeats); (b) keep the main activity only and record that rule.
- Needs decision: no
- From: broad F8 (sender), parties F5 (sender and receiver); context listed the sender as refuted

## Checked and consistent
- Meter arithmetic: 28410 + 1350 = 29760 m³; the same 1350 m³ in `DeliveredQuantity`, the meter's `TotalDeliveredQuantity` and `TotalMeteredQuantity`; `MeterConstant` 1 with `DIRECT`.
- Volume conversion, recalculated: (4 + 1.01325) / 1.01325 = 4.9477 (4 bar gauge to absolute reference); 1350 × 4.9477 = 6679.4 m³; 6679 × 9.163 kWh/m³ = 61200 kWh (6679.4 × 9.163 = 61204), equal to the consumption point's `TotalDeliveredQuantity`, `TotalConsumedQuantity`, `ConsumptionEnergyQuantity` and `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:InvoicedQuantity` = `61200`. Load: 61200 kWh / 744 h = 82 kW average, plausible for the coating ovens of one line.
- Periods: readings 2026-02-28 → 2026-03-31; MainPeriod and ConsumptionReport period 2026-03-01 → 2026-03-31, the same as `02-Invoice.xml:/Invoice/cac:InvoicePeriod/cbc:StartDate` = `2026-03-01`; all readings before the issue date.
- Parent reference FG-INV-26-0150 resolves to 02-Invoice.xml, an Invoice from the same sender to the same receiver (`flow_index.py`).
- Currency `XUF` in the document, the payable amount and the parent invoice.
- Parties: Ferrano Grid (`XU-R-106055`) described identically here and in 02-Invoice.xml (51 leaf values); Ferrano Energy (`XU-R-105781`) identically here and in 02 and 03; all three SUA in the Urvanian commercial register, register ID = PartyIdentification, plausible sizes. SubscriberParty Valdara at its own address, `SubscriberID` `FE-C-0047121` = the retailer's customer number, fitting "An identifier for the subscriber responsible for the consumption".
- Identifiers: consumption point FG-CP-4120-G1, meter FG-G-20417 and reading FG-G-20417-2603 consistent; meter number in the correction is the consumption point's meter. `check_ids.py`: ISIN XU0001042501 OK.
- Codes: `UtilityStatementTypeCode` GAS (top level and in Consumption), `CorrectionTypeCode` CONV, `LatestMeterReadingMethodCode` REMOTE agree with their text equivalents; units MTQ, KWH, BAR fit.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:Description`: calorific value 9.163 kWh/m³ too low — refuted: within the range of low-calorific natural gas (about 8.4–13.1 kWh/m³, own knowledge, DVGW G 260); a comparison with the Kelpstone gas of 04/06 (75 kg/MWh) gives a density of about 0.69 kg/m³, lean, but nothing says the gas at this connection is Kelpstone gas (from broad, logistics)
- Same element: missing temperature correction — refuted: a temperature factor of 1 is legitimate when the gas is metered at reference temperature, and the text names the corrections applied (from logistics)
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047121`: a retailer's customer number in a grid operator's statement — refuted: the definition asks for "An identifier for the subscriber responsible for the consumption", and a grid operator holds the supplier's customer reference in supplier-switching processes (from broad, context)
- Same element: mismatch with the electricity contract FE-C-0047120 of the same customer in `utilities/02-Invoice.xml` — refuted: a separate gas contract number is plausible and no example calls FE-C-0047121 anything else (from logistics)
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:TotalDeliveredQuantity`: unit KWH against MTQ on the meter — refuted: the point's total is energy after conversion, the meter's is volume (from broad)
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:GasPressureQuantity` = `4`: a line pressure is not a "correction of the gas pressure" — refuted: it is the pressure on which the correction is based, and the text shows its use (from logistics, context)
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ID` = `FG-CP-4120-G1-2603`, equal to `/UtilityStatement/cac:SubscriberConsumption/cbc:ConsumptionID`: one ID for two objects — refuted: one specification with one report for the same point and month (from logistics)
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cbc:MeterConstantCode` = `DIRECT`: electricity-only code on a gas meter — refuted: the world list defines DIRECT as "connected directly: the constant is 1", true here (from context)
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount`: should carry the retail price Valdara pays — refuted as an alternative: the parent is the grid operator's invoice, so the amount to reconcile is the network charge (F1) (from money)
- The electricity lines 1 and 2 of the parent invoice have no utility statement in this flow — refuted for this example: a statement may cover one consumption point; taken up in energy/02#F1 (from money)
- `/UtilityStatement/cac:SenderParty/cac:PostalAddress/cbc:StreetName[2]`: Italian-form name tagged `en-XU` — refuted: Urvanian place names keep their Italianate form in English across the world (from parties)
- `/UtilityStatement/cac:SenderParty/cac:PartyLegalEntity/cbc:EntitySizeCode` = `MEDIUM`: a grid operator could be large — refuted: nothing gives staff or turnover; a provincial operator of medium size is plausible (from parties)
- `/UtilityStatement/cac:SenderParty/cac:Language/cbc:ID` = `qau`: real language code — refuted: qaa–qtz is reserved for local use (from parties)
- `/UtilityStatement/cac:SenderParty/cac:Contact/cbc:Telephone` and `/UtilityStatement/cac:SenderParty/cac:AdditionalPartyIdentification/cbc:ID` = `0990:10605`: clash with real registers — refuted: +999 is not an assigned ITU country code and ICD 0990 is not assigned in ISO 6523 (own knowledge) (from parties)
- `/UtilityStatement/cbc:IssueDate` = `2026-04-02` before the parent invoice — the context part refuted it (reserved invoice number); the merge keeps it as Low F5 with that argument
- `/UtilityStatement/cac:SenderParty/cbc:IndustryClassificationCode` = `3510`: the context part refuted it (main activity electricity); the merge keeps it as Low F8 with that argument

## Changed in the merge
- broad F3, parties F2 → F3: Needs decision set to no (broad had yes), because section 6 names a province in Region as a Medium encoding problem and the fix does not change the story; the same decision is taken for 02–09 of this flow.
- broad F4, context F3 → F4: Needs decision set to yes (context had no), because whether to drop the element or record the UBL definition as a defect is an owner's decision; both preferred options kept.
- broad F5, logistics F1 → F5: combined, with the context part's counter-argument (reserved invoice number) in Why; Low kept.
- broad F6, parties F4, context F4 → F6: grouped all places named by the three parts (customs trader ID, security listing, service provider ID, service type and name, alternative contact channel).
- broad F7, parties F3 → F7: grouped; job title added from parties.
- broad F8, parties F5 → F8: grouped sender and receiver; the context part's refutation quoted in Why and condition widened to allow a stated main-activity rule.

## Outside this review
- `utilities/02-Invoice.xml` (issued 2026-04-02 13:20) bills the 61200 kWh of this connection "converted ... by the grid operator's metering report", four and a half hours before this statement (17:42) is issued: a timeline question across flows (from logistics).
