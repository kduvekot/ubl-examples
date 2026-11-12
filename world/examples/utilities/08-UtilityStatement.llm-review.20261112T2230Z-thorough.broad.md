# LLM review: 08-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: broad

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/08-UtilityStatement.xml`, Git blob `2ad70d0c87bdcb2a69e49f63c3882af20185d03e` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 7b0e1fe 2026-11-12 Reviews of the rail flow, run 20261112T2137Z-thorough: merge complete
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

### utilities/08#F1 · High · Payments on account that the invoice neither deducts nor follows
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cbc:Note` = `Paid on account each month for the estimated use; the next bill settles it against the reading.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cac:PaymentTerms/cbc:Note` = `By direct debit on the first working day of each month.`
- XPath: `/UtilityStatement/cac:MainOnAccountPayment/cbc:EstimatedConsumedQuantity` = `14`
- XPath: `09-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `38.78`
- XPath: `09-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `Collected by direct debit 21 days after the invoice date.`
- Why: OnAccountPayment is "The planned prepayments (on account) regarding this subscription". The statement says the household pays on account every month by direct debit on the first working day, and that the bill settles these payments against the reading. Its parent invoice 09 for the same month bills the full 38.78 XBL (water 32.90 + levy 5.88) with no prepaid amount, and collects it by direct debit 21 days after the invoice date. Either the household pays twice (on account and in full), or there are no payments on account. The reminder 10-Reminder.xml and the credit note 11-CreditNote.xml also deal with the full invoice amount.
- Condition: The statement and invoice 09 describe the same payment arrangement: either payments on account that the invoice deducts (PrepaidAmount, with the balance collected), or monthly billing on the reading with no payments on account.
- Options: (a, preferred) remove OnAccountPayment and MainOnAccountPayment (the invoice bills each month on the reading, so there is nothing to pay on account); (b) keep them and let invoice 09 deduct the March prepayment, changing 10 and 11 accordingly.
- Needs decision: yes

### utilities/08#F2 · Medium · District-heating cooling correction in a water statement, with units that do not fit its own rate
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionTypeCode` = `COOL`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:MeterNumber` = `CSW-H-71844`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionUnitAmount` = `0.80`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionWaterQuantity` = `6.2`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `19.84`
- Why: The statement is a water statement (`/UtilityStatement/cbc:UtilityStatementTypeCode` = `WATER`) of a water company for one drinking-water meter (CSW-W-71844) under a water supply contract. The correction concerns a district-heating meter (CSW-H-71844) and the cooling of district-heating water, i.e. a different utility, which neither this statement's consumption point, its contract nor invoice 09 covers; no district-heating supplier or supply appears anywhere in the flow. In addition, CorrectionUnitAmount is defined as "Correction per MWH per degree C", but the amount is computed per cubic metre: 0.80 × 6.2 m³ × 4 °C = 19.84. With a rate per MWh, the heat quantity in MWh would be needed (ConsumptionEnergyQuantity), not the water volume.
- Condition: The correction belongs to a supply the statement covers, and its unit amount × the quantity in the unit its definition names × the temperature difference = the correction amount.
- Options: (a, preferred) remove the district-heating correction from the water statement (it belongs in a district-heating statement, if the world has one); (b) if Coastal State Water Company also supplies district heating, add that supply (consumption point, meter, contract, invoice line) and express the rate per MWh with the energy quantity.
- Needs decision: yes

### utilities/08#F3 · Medium · Energy level used for water, and "Low consumer" against the figures
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ConsumersEnergyLevelCode` = `LOW`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ResidentOccupantsNumeric` = `2`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:TotalConsumedQuantity` = `14`
- Why: ConsumersEnergyLevelCode is "The level of energy consumed, compared to the average for this residence type and the number of people living in" it; the report is about water, not energy. Read as a water level, 14 m³ in 31 days for 2 residents is about 226 litres per person per day, well above typical household use of about 120–150 litres (own knowledge), so "Low consumer" does not fit. The history in the same report calls the earlier months "Normal".
- Condition: The energy level is absent from a water report, or the consumption level stated agrees with the consumption per resident.
- Options: (a, preferred) leave ConsumersEnergyLevel(Code) out; (b) lower the consumption or change the level if a water level is wanted (and record that UBL has only an energy-level element).
- Needs decision: no

### utilities/08#F4 · Medium · CustomerParty is the receiver
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Robin Ashdale`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:PartyName/cbc:Name` = `Robin Ashdale`
- Why: UtilityStatement/CustomerParty is "The buyer, if different from the receiver of the document." Both are Robin Ashdale.
- Condition: CustomerParty is present only when the buyer differs from the receiver.
- Options: (a, preferred) leave it out.
- Needs decision: no

### utilities/08#F5 · Medium · SupplierConsumption used for a single-supplier consumption that Consumption already describes
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `32.90`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `32.90`
- Why: Consumption is "The consumption in case the consumption is from one and only one supplier"; SupplierConsumption "The consumption in case the consumption is from more than one supplier". One supplier, both present with identical totals.
- Condition: Only the alternative matching the number of suppliers is used.
- Options: (a) Consumption only; (b) SupplierConsumption only with a second supplier; (c) record the UBL model limitation (consumption lines only under SupplierConsumption).
- Needs decision: yes

### utilities/08#F6 · Medium · Language code in LocaleCode
- XPath: `/UtilityStatement/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; "en" from ISO 639 is the language, not a locale. 213 examples carry the pattern (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">'`).
- Condition: LocaleCode is a locale or absent.
- Options: (a, preferred) leave it out.
- Needs decision: no

### utilities/08#F7 · Low · Statement issued before its parent invoice
- XPath: `/UtilityStatement/cbc:IssueTime` = `15:10:00`
- XPath: `09-Invoice.xml:/Invoice/cbc:IssueTime` = `15:44:00`
- Why: The statement is "A supplement to an Invoice or Credit Note" and refers to CSWC-INV-26-0319 as its parent, but is issued 34 minutes before that invoice on the same day. In 01, 03, 05 and 12 the statement follows its invoice.
- Condition: The statement is issued at or after its parent invoice.
- Options: (a, preferred) an issue time after 15:44.
- Needs decision: no

### utilities/08#F8 · Low · Password of the reading website in clear text
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:WebSiteAccess/cbc:Password` = `RD-4K7-918`
- Why: WebSiteAccess has a business reason here (the household submits its own readings). Sending the password itself in a business document is poor practice; a login ID and a link suffice, the password being given separately. As an example it teaches the wrong practice.
- Condition: The statement carries no password, or the story explains why it must (e.g. a one-time initial code).
- Options: (a, preferred) keep URI and Login, drop the password; (b) describe it as a one-time activation code.
- Needs decision: no

### utilities/08#F9 · Low · References and data the statement does nothing with
- XPath: `/UtilityStatement/cac:Signature/cbc:ID` = `CSW-SIG-26-0401`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:GuidanceDocumentReference/cbc:ID` = `CSW-SAVE-WATER`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:DocumentReference/cbc:ID` = `CSW-QUALITY-2026-Q1`
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- Why: The signature has only an ID and signatory, with no method or reason. The guidance and document references give only IDs; GuidanceDocumentReference is "A reference to a document providing an explanation of this kind of report", which a water-saving leaflet is not, and DocumentReference ("some other document (for example, this report in another format)") does not say what the quality report is. The receiver's bank account is used for the direct debit in invoice 09, not in this statement.
- Condition: Each of these has a role in the statement and says what it is, or is absent.
- Options: (a, preferred) drop the signature and the bank account; give the references a description or type, and use GuidanceDocumentReference only for an explanation of the report.
- Needs decision: no

### utilities/08#F10 · Low · Subscriber type of the utility item is "Water", the consumption point's is "Household"
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberType` = `Water`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberTypeCode` = `HH`
- Why: Under UtilityItem, SubscriberType is "Identification of the subscriber type, expressed as text", its code "The code identifying for the service type". As in 01, 03, 05.
- Condition: Consistent with the consumption point, or the service-type reading is recorded as deliberate.
- Options: (a) record the UBL definition inconsistency; (b) leave both out.
- Needs decision: yes

### utilities/08#F11 · Low · Filler descriptions
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Description` = `Earlier month.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Description` = `Earlier month.`
- Why: No information beyond the structured data next to them (rule "no fillers").
- Condition: Each description carries information of its own, or is absent.
- Options: (a, preferred) leave them out.
- Needs decision: no

## Checked and consistent
- Meter: 1844 − 1830 = 14 m³, constant 1; all quantities 14; customer readings on both dates, consistent with the WebSiteAccess for readings.
- Amounts: 14 × 2.35 = 32.90; history 15 × 2.35 = 35.25 and 13 × 2.35 = 30.55; average (15 + 13 + 14) / 3 = 14 m³ and 14 × 2.35 = 32.90 = AverageAmount (correct here).
- Parent invoice CSWC-INV-26-0319 is 09-Invoice.xml (line 1: 14 m³, 32.90, meter CSW-W-71844, contract CSW-C-311790, exemption WATER).
- Mandate: MainOnAccountPayment's note on the mandate limit agrees with 09's MaximumPaidAmount 150.00, well above 14 m³ × 2.35.
- ConsumptionReportReference for February (13 m³) agrees with ConsumptionHistory[2].
- check_ids.py: account XB64BLUM38010007251840 correct.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount`: correction 19.84 not in the payable amount — refuted, the description says it is charged on the annual account.
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:DifferenceTemperatureReductionQuantity`: sign of −4 °C — refuted, actual 31 − normal 35 = −4.

## Outside this review
- 09-Invoice.xml: PayerParty equal to the debtor Robin Ashdale, although PayerParty is "The Party, if different from the debtor, that makes the Payment" (that example's review).
