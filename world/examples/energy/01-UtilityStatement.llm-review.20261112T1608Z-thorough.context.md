# LLM review: 01-UtilityStatement.xml

Flow: energy (ENERGY-2026-01) · Review date: 2026-11-12 · Part: context

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

### energy/01#F1 · High · Payable amount 0 on a consumption the parent invoice charges for
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `0`
- XPath: `/UtilityStatement/cac:ParentDocumentReference/cbc:ID` = `FG-INV-26-0150`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:InvoicedQuantity` = `61200`
- XPath: `02-Invoice.xml:/Invoice/cac:InvoiceLine[3]/cbc:LineExtensionAmount` = `116280`
- Why: Under Consumption, LegalMonetaryTotal is "The total amount payable on this consumption, including any allowances, charges, or taxes", and the Utility Statement is "A supplement to an Invoice or Credit Note". The parent invoice 02 bills exactly this consumption (61200 kWh of gas network use, line 3) at 1.9 XUF/kWh = 116280 XUF net, 20 % VAT = 23256, so 139536 XUF including tax. The statement says nothing is payable on it. The two documents contradict each other; a zero also reads as "free of charge", which nothing in the world supports.
- Condition: The payable amount under the consumption equals what the parent invoice charges for this consumption (139536 XUF including tax, or a stated net basis that matches line 3), or the statement no longer claims an amount that contradicts the invoice.
- Options: (a) preferred: carry the amount of invoice line 3 including tax (139536 XUF), so the statement is the supplement its definition describes; (b) if the statement is meant to carry only quantities, the mandatory LegalMonetaryTotal still has to state the real amount, so (b) is not really open without changing the document type.
- Needs decision: no

### energy/01#F2 · Medium · CustomerParty is the receiver, but the element is only for a buyer different from the receiver
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` = `XU-R-105781`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyIdentification/cbc:ID` = `XU-R-105781`
- Why: UBL defines Utility Statement. Customer Party as "The buyer, if different from the receiver of the document." Here it is Ferrano Energy, which is also the ReceiverParty. The condition of the definition is not met, so the element repeats the receiver without a reason. The same pattern (CustomerParty with the same PartyIdentification/ID as ReceiverParty) occurs in 4 of the 6 UtilityStatement examples (energy/01, utilities/01, utilities/05, utilities/12; counted with an lxml script over `*/*-UtilityStatement.xml`).
- Condition: CustomerParty is absent, or names a buyer different from ReceiverParty.
- Options: (a) preferred: drop CustomerParty, because the buyer of the network service is the receiver; (b) keep it only if the story has a different buyer.
- Needs decision: no

### energy/01#F3 · Medium · ConsumptionEnergyQuantity, defined for district heating, used for gas
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity` = `61200`
- Why: UBL defines Consumption Correction. Consumption Energy. Quantity as "Your consumpt for district heating energy." The statement is about gas (`/UtilityStatement/cbc:UtilityStatementTypeCode` = `GAS`), and the energy content of the gas is already stated in `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:TotalConsumedQuantity` = `61200` and in the correction's Description. The element is used for something other than its definition names.
- Condition: ConsumptionEnergyQuantity is absent from a gas statement, or carries district heating energy.
- Options: (a) preferred: drop it; the converted quantity is in TotalConsumedQuantity and the Description explains the conversion; (b) keep it only through a district heating consumption in the world (another example).
- Needs decision: no

### energy/01#F4 · Low · Subscriber master data the statement does nothing with
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:PartyLegalEntity/cac:SecurityListing/cbc:ID` = `XU0001042501`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:ServiceProviderParty/cbc:ServiceType` = `Warehousing and despatch`
- XPath: `/UtilityStatement/cac:SubscriberParty/cac:AdditionalPartyIdentification[2]/cbc:ID` = `XU-TR-104274`
- Why: The statement reports a gas meter reading from the grid operator to the retailer. Valdara's listed shares, its warehousing provider (Castrano Logistics) and its customs trader number play no part in metering or billing gas network use; they look copied from the party's master data (section 4.8 of the review rules: data a document does nothing with).
- Condition: Every element under SubscriberParty has a role in the utility statement (identification of the subscriber, its address, a contact for meter matters), or the statement's purpose explains it.
- Options: (a) preferred: leave out SecurityListing, ServiceProviderParty and the customs trader identifier in this document; (b) keep any of them only with a reason in the statement (e.g. a note that the logistics provider operates the connection).
- Needs decision: no

## Checked and consistent
- Reference: ParentDocumentReference `FG-INV-26-0150` resolves to 02-Invoice.xml, an Invoice (the kind the definition names), from the sender (Ferrano Grid) to the receiver (Ferrano Energy).
- Meter reading arithmetic: 29760 − 28410 = 1350 m³ = DeliveredQuantity = meter TotalDeliveredQuantity = TotalMeteredQuantity.
- Conversion: absolute pressure (4 bar gauge + 1.01325) / 1.01325 = 4.9477 (own knowledge of standard conditions); 1350 × 4.9477 = 6679 m³; 6679 × 9.163 kWh/m³ = 61200 kWh, as in TotalConsumedQuantity, the consumption point's TotalDeliveredQuantity and invoice 02 line 3. A gross calorific value of about 9.2 kWh/m³ is plausible for natural gas.
- Periods: MainPeriod and ConsumptionReport/Period 2026-03-01 to 2026-03-31 match the reading dates (2026-02-28 to 2026-03-31) and `02-Invoice.xml:/Invoice/cac:InvoicePeriod/cbc:StartDate` = `2026-03-01`.
- UtilityStatementTypeCode GAS at document and consumption level agree with the meter (rotary gas meter) and the note.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cbc:MeterConstantCode` = `DIRECT`: suspected an electricity-only code (direct vs. current-transformer connection) on a gas meter — refuted because the world list defines DIRECT as "The meter is connected directly: the constant is 1", which holds for a gas meter with MeterConstant 1.
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:GasPressureQuantity` = `4`: suspected that a line pressure is not a "Correction of the gas pressure" — refuted because the pressure is the input of the pressure correction the element reports, a legitimate reading of the definition.
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `FE-C-0047121`: suspected that a retailer's customer number does not belong in a grid operator's statement — refuted because the definition asks for "An identifier for the subscriber responsible for the consumption", and a grid operator holds the supplier's customer reference for the connection in supplier-switching processes.
- `/UtilityStatement/cbc:IssueDate` = `2026-04-02`: the statement is issued the day before its parent invoice (`02-Invoice.xml:/Invoice/cbc:IssueDate` = `2026-04-03`) — not kept as a finding of this lens, because an invoice number reserved in the same billing run can be referenced before the invoice is sent; the order of dates belongs to the logistics part.
- `/UtilityStatement/cac:SenderParty/cbc:IndustryClassificationCode` = `3510`: suspected that a grid operator running a gas network should be ISIC 3520 — refuted because the party runs both networks and 3510 can be its main activity; the electricity lines of invoice 02 outweigh the gas line.
