# LLM review: 08-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: context

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

### utilities/08#F1 · High · Monthly payments on account that the invoice does not know
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cbc:Note` = `Paid on account each month for the estimated use; the next bill settles it against the reading.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cac:PaymentTerms/cbc:Note` = `By direct debit on the first working day of each month.`
- XPath: `/UtilityStatement/cac:MainOnAccountPayment/cbc:Note` = `The basis of the direct debit limit.`
- XPath: `09-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `38.78`
- XPath: `09-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `Collected by direct debit 21 days after the invoice date.`
- Why: OnAccountPayment is "The planned prepayments (on account) regarding this subscription". The statement says the household pays on account each month by direct debit on the first working day, and that the next bill settles these payments against the reading. The parent invoice `09-Invoice.xml` bills the full March consumption and levy (38.78) with no PrepaidAmount, and collects it by direct debit 21 days after the invoice date, not on the first working day. Either March was paid on account (then the invoice must deduct it) or the household pays the monthly bill itself (then there are no payments on account). The reminder `10-Reminder.xml` also treats the 23 April collection of the full 38.78 as the only one.
- Condition: The statement's payments on account and the invoice's amounts and collection dates describe the same arrangement.
- Options: (a, preferred) remove both on-account aggregates: the flow bills monthly on actual readings, which the invoice, the reminder and the credit note all follow; (b) keep payments on account and give the invoice a PrepaidAmount and a settlement of the difference — this changes 09, 10 and 11.
- Needs decision: yes

### utilities/08#F2 · Medium · A district-heating cooling correction in the water company's water statement
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionTypeCode` = `COOL`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:MeterNumber` = `CSW-H-71844`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:Description` = `Poor cooling makes the network pump more water; the shortfall is charged on the annual account.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `19.84`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:HeatingTypeCode` = `DH`
- XPath: `/UtilityStatement/cac:SenderParty/cbc:IndustryClassificationCode` = `3600`
- Why: The statement is a water statement (type WATER) from Coastal State Water Company, ISIC 3600 "Water collection, treatment and supply". A cooling correction belongs to a district heating supply: it penalises a too-small temperature drop of the heating water at a heat meter. Nothing in the statement or its invoice is district heating, no example of the world has district heating besides this one (`grep -rli --include='*.xml' 'district heating' world/examples`), and the amount is "charged on the annual account", so this document does nothing with it. The meter CSW-H-71844 carries the water company's prefix but is not a meter of this consumption point.
- Condition: The correction appears only in a statement of the party that supplies the district heating, for a consumption that statement bills or settles.
- Options: (a, preferred) remove the correction (and the HeatingType, unless it explains the water use); (b) give the world a district heating supplier and put the correction in its statement — this adds to the story.
- Needs decision: yes

### utilities/08#F3 · Medium · CustomerParty repeats the receiver
- XPath: `/UtilityStatement/cac:CustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Robin Ashdale`
- Why: CustomerParty is "The buyer, if different from the receiver of the document." The receiver is Robin Ashdale.
- Condition: CustomerParty only when the buyer differs from the receiver.
- Options: (a, preferred) leave it out.
- Needs decision: no

### utilities/08#F4 · Medium · SupplierConsumption used although there is only one supplier
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilitySupplierParty/cac:PartyName/cbc:Name` = `Coastal State Water Company`
- Why: SupplierConsumption is "The consumption in case the consumption is from more than one supplier"; the flat has one water supplier, and Consumption already describes it.
- Condition: SupplierConsumption only where there is more than one supplier.
- Options: (a, preferred) remove it here.
- Needs decision: yes

### utilities/08#F5 · Medium · A language code in LocaleCode
- XPath: `/UtilityStatement/cac:SenderParty/cac:Language/cbc:LocaleCode` = `en`
- Why: LocaleCode is "A code signifying the locale in which this language is used"; "en" (ISO 639) is a language code. World-wide pattern (362 elements in 213 examples, grep over `*.xml`).
- Condition: LocaleCode holds a locale or is absent.
- Options: (a, preferred) remove.
- Needs decision: no

### utilities/08#F6 · Medium · The subscriber identifier is the contract number
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:SubscriberID` = `CSW-C-311790`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberID` = `CSW-C-311790`
- Why: SubscriberID identifies the subscriber; CSW-C-311790 is the supply contract (`09-Invoice.xml:/Invoice/cac:PurchaseReference/cbc:ID` = `CSW-C-311790`, "Supply contract").
- Condition: SubscriberID holds a subscriber identifier, or is absent.
- Options: (a, preferred) a customer number; (b) remove.
- Needs decision: no

### utilities/08#F7 · Low · Energy consumer level in a water report
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ConsumersEnergyLevelCode` = `LOW`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ConsumersEnergyLevel` = `Low consumer`
- Why: ConsumersEnergyLevel is "The level of energy consumed, compared to the average for this residence type and the number of people living in the residence". The report is about 14 m³ of drinking water, not energy. (14 m³ for two occupants is about 230 l per person per day, which is not obviously "low" either, by own knowledge of typical household use of 100–150 l.)
- Condition: The level is given only for energy, or a water-use level is expressed where UBL has a place for it.
- Options: (a, preferred) remove; (b) record the lack of a water-use level as a UBL finding.
- Needs decision: no

### utilities/08#F8 · Low · Statement issued before the invoice it supplements
- XPath: `/UtilityStatement/cbc:IssueTime` = `15:10:00`
- XPath: `09-Invoice.xml:/Invoice/cbc:IssueTime` = `15:44:00`
- Why: A UtilityStatement is "A supplement to an Invoice or Credit Note", referenced by its ParentDocumentReference. Both are dated 2026-04-02, but the statement is issued 34 minutes before its parent; the other statements of the flow are issued after their invoices.
- Condition: The statement is issued at or after its parent invoice.
- Options: (a, preferred) a later issue time.
- Needs decision: no

### utilities/08#F9 · Low · Document references with only an ID, one of them in the wrong element
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:GuidanceDocumentReference/cbc:ID` = `CSW-SAVE-WATER`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:DocumentReference/cbc:ID` = `CSW-QUALITY-2026-Q1`
- Why: GuidanceDocumentReference is "A reference to a document providing an explanation of this kind of report"; a water-saving leaflet explains how to save water, not the report. ConsumptionReport/DocumentReference is "A reference to some other document (for example, this report in another format)"; a quarterly water quality report is neither this report nor about the consumption. Both carry only an ID.
- Condition: Each reference is in an element whose definition fits, and says what it refers to.
- Options: (a) move them to the statement's AdditionalDocumentReference with type and description; (b) remove them.
- Needs decision: no

### utilities/08#F10 · Low · Receiver's bank account in a statement
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- Why: The statement does not pay or collect anything; the account is the mandate account of the invoice (`09-Invoice.xml`), copied into the person's data here.
- Condition: The statement carries no account of the receiver, or uses it.
- Options: (a, preferred) remove.
- Needs decision: no

### utilities/08#F11 · Low · SubscriberType names the utility; descriptions without information
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:SubscriberType` = `Water`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `The consumption point of the statement.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Description` = `Earlier month.`
- Why: The item's SubscriberType ("Identification of the subscriber type") says "Water" while the subscriber type at the point is "Household"; the two descriptions repeat what the structure already says (IND5).
- Condition: As in `05-UtilityStatement.xml`: text and code aligned with their definitions; filler descriptions removed.
- Options: drop the text SubscriberType and the filler descriptions.
- Needs decision: no

## Checked and consistent
- ParentDocumentReference CSWC-INV-26-0319 → `09-Invoice.xml`, line 1: 14 m³ × 2.35 = 32.90, meter CSW-W-71844.
- Meter: 1844 − 1830 = 14 m³; customer readings, consistent with the WebSiteAccess for submitting readings.
- Average (15 + 13 + 14) / 3 = 14 m³ × 2.35 = 32.90 = AverageAmount (correct here, coincidentally equal to March).
- Cooling correction arithmetic: 0.80 × 6.2 m³ × 4 °C = 19.84 (the unit amount is per m³ per °C).
- Mandate limit (`09-Invoice.xml`, 150.00 per instruction) is above the estimate, as the note says.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:WebSiteAccess/cbc:Password`: a password in a document — refuted because the household reads the meter itself (method CUSTOMER) and the access is how it submits readings; UBL provides the element for this.
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cbc:ResidentOccupantsNumeric`: number of occupants — refuted because it is the basis of the consumption comparison the report gives.
