# LLM review: 03-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/03-UtilityStatement.xml`, Git blob `a8d48fa5c4e614ea05c1521143210974ea8bf6f9` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
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

### utilities/03#F1 · High · Correction amount does not equal unit amount × quantity
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionUnitAmount` = `27`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionEnergyQuantity` = `-750`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `-20475`
- Why: −750 kWh × 27 = −20,250, not −20,475; the amount stated was calculated with the tariff 27.3 (−750 × 27.3 = −20,475; `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:Price/cbc:PriceAmount` = `27.3`). In addition, UBL defines `CorrectionUnitAmount` as "Correction per MWH per degree C", a district-heating temperature correction; here it carries a price per kWh of an estimate correction with no temperature involved.
- Condition: CorrectionUnitAmount × ConsumptionEnergyQuantity = CorrectionAmount, and the unit amount is used with the meaning of its definition, or not at all.
- Options: (a, preferred) drop CorrectionUnitAmount (its definition does not fit an estimate correction) and let the description name the tariff; (b) 27.3, if the element is kept.
- Needs decision: no

### utilities/03#F2 · High · Estimate correction is neither needed nor applied: the March consumption already makes up for February's estimate
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:Description` = `February's estimate of 17,200 kWh was 750 kWh too high, as the actual reading shows.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:PreviousMeterQuantity` = `117250`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cac:UtilityMeter/cac:MeterReading/cbc:PreviousMeterReadingMethodCode` = `ESTIMATE`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `609336`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Quantity` = `17200`
- Why: March's 18,600 kWh are calculated from the estimated February reading (135,850 − 117,250). If that estimate was 750 kWh too high, the real February reading was 116,500 and March's real use is 19,350 kWh; billing 18,600 for March already gives back the 750 kWh over-billed in February. Crediting −20,475 on top would credit the customer twice. The statement does not apply the credit either: the payable amount 609,336 is 18,600 × 27.3 × 1.2 without it, and invoice 02 bills line 2 at the full 507,780 with no allowance or correction (`02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `507780`). The history still shows February at the estimated 17,200 kWh. So the statement announces a credit that no amount of the flow contains, and that the readings make unnecessary.
- Condition: Either the readings, March's quantity and the payable amounts settle February's estimate once (and the correction element says only what was done), or the correction is credited in the statement's totals and in invoice 02, with March billed from the real February reading.
- Options: (a, preferred) keep March at 18,600 kWh from the estimated reading and describe the correction as settled through this reading (no CorrectionAmount, or 0), which matches the totals; (b) bill March at 19,350 kWh from the real reading and credit −750 kWh, in the statement and in invoice 02. Option (b) changes the invoice.
- Needs decision: yes

### utilities/03#F3 · High · The warehouse's share of the energy tax is missing; tax and payable amount differ from the invoice
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TaxTotal/cbc:TaxAmount` = `101556`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `609336`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:TaxInclusiveLineExtensionAmount` = `609336`
- Why: Invoice 02 levies energy tax on all electricity, the warehouse meter included (its tiers add up only with the 18,600 kWh of this meter, see 02's review), and includes that tax in the VAT base (`02-Invoice.xml:/Invoice/cac:TaxTotal[2]/cac:TaxSubtotal/cbc:TaxableAmount` = `12580140`). This statement has no EnergyTaxReport and leaves the tax out of TaxTotal and PayableAmount ("the total amount payable on this consumption, including any allowances, charges, or taxes"). With 18,600 kWh in the upper tier at 0.6 XUF/kWh, the warehouse's energy tax is 11,160, and the amount payable for it 622,728 ((507,780 + 11,160) × 1.2), not 609,336. Statement 01 instead reports the energy tax of both meters (`01-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyTaxReport/cbc:TaxEnergyAmount` = `288840`).
- Condition: The statement reports the energy tax of this consumption point, and its tax and payable amounts include it and the VAT on it, consistent with invoice 02 and statement 01.
- Options: (a, preferred) an EnergyTaxReport of 11,160 and the corrected totals, together with the fix in 01; (b) if the world assesses the energy tax per customer, say so in both statements and still carry the VAT on it in the payable amounts.
- Needs decision: no

### utilities/03#F4 · High · Statement carries the invoice's header accounting code; the invoice books this consumption to another code
- XPath: `/UtilityStatement/cbc:AccountingCostCode` = `3100`
- XPath: `/UtilityStatement/cbc:AccountingCost` = `Raw materials and parts`
- Why: The statement covers only the warehouse meter, billed on invoice line 2 (`/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:ParentDocumentLineReferenceID` = `2`). The invoice gives that line the buyer's code 7100 (`02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:AccountingCostCode` = `7100`, `02-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:AccountingCost` = `Warehouse, Castrano Logistics`). The statement's header code "applied to the document as a whole" therefore contradicts the invoice for the only consumption it contains. The statement goes to Castrano Logistics (ReceiverParty), who has no use for Valdara's cost codes.
- Condition: The statement's accounting code is the one the invoice applies to line 2, or the statement has none.
- Options: (a, preferred) leave AccountingCost out of this statement, whose receiver is the subscriber, not the buyer; (b) 7100 and its text.
- Needs decision: no

### utilities/03#F5 · High · Average amount is March's amount, not the three-month average
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:AverageAmount` = `507780`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:Description` = `The average over the last three months is 17900 kWh.`
- Why: The quantity average over the three months is right ((17,900 + 17,200 + 18,600) / 3 = 17,900 kWh), but `AverageAmount` ("the average monetary amount of the consumption") is March's amount alone; the average of the three amounts (488,670 + 469,560 + 507,780) / 3 is 488,670 XUF. Same pattern as in 01 and 05.
- Condition: AverageAmount is the average of the amounts over the window the description names.
- Options: (a, preferred) 488670.
- Needs decision: no

## Checked and consistent
- 18,600 × 27.3 = 507,780 = invoice line 2; 20 % VAT = 101,556; 507,780 + 101,556 = 609,336 (internal arithmetic; F3 is about what is missing).
- Meter: 135,850 − 117,250 = 18,600 × MeterConstant 1 = DeliveredQuantity = TotalMeteredQuantity.
- History: 17,900 × 27.3 = 488,670; 17,200 × 27.3 = 469,560; February equals the ConsumptionReportReference (17,200).
- ParentDocumentLineReferenceID 2 points to invoice 02's line 2, with the same quantity, price and amount; the invoice's warehouse line names Castrano Logistics as originator.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:UtilityCustomerParty`: Valdara as utility customer while Castrano is subscriber was checked for money effect — consistent with the invoice, which bills Valdara for this meter.
