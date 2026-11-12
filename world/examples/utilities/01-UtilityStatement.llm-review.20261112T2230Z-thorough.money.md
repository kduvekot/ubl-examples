# LLM review: 01-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/01-UtilityStatement.xml`, Git blob `5afddf1d0c8c1838c6abd6e06e483af49cb2664f` (committed)
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

### utilities/01#F1 · High · Energy tax reported for the whole invoice, but left out of this consumption's tax and payable amount
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyTaxReport/cbc:TaxEnergyAmount` = `288840`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyTaxReport/cbc:TaxEnergyBalanceAmount` = `288840`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TaxTotal/cbc:TaxAmount` = `2253888`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `13523328`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `13523328`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cbc:TaxInclusiveLineExtensionAmount` = `13523328`
- Why: The Consumption's `LegalMonetaryTotal` is "the total amount payable on this consumption, including any allowances, charges, or taxes", and `EnergyTaxReport` is "a tax on the consumption of energy or water". The statement covers one consumption point only (meter FE-M-881204, 412,800 kWh), yet its energy tax report carries 288,840 XUF, which is the energy tax of the whole invoice (`02-Invoice.xml:/Invoice/cac:TaxTotal[1]/cbc:TaxAmount` = `288840`). Recalculated from the invoice's tiers, 288,840 = 50,000 kWh × 1.2 + 381,400 kWh × 0.6, where 381,400 = 412,800 + 18,600 − 50,000: it includes the 18,600 kWh of the Castrano warehouse meter, which statement 03 reports (`03-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cbc:TotalMeteredQuantity` = `18600`). This point's own share is 277,680 (60,000 + 362,800 × 0.6). At the same time the VAT (2,253,888 = 20 % of 11,269,440) and the payable amount (13,523,328) leave the energy tax out entirely, while the invoice puts it into the VAT base (`02-Invoice.xml:/Invoice/cac:TaxTotal[2]/cac:TaxSubtotal/cbc:TaxableAmount` = `12580140` = 12,291,300 + 288,840). The two statements together show 14,132,664 payable for electricity, the invoice charges 14,479,272 for it (15,096,168 − 1.2 × 514,080 for gas); the difference 346,608 is exactly 1.2 × 288,840.
- Condition: The energy tax in this statement is the share of this consumption point; the Consumption's TaxTotal, PayableAmount and the line's TaxInclusiveLineExtensionAmount include that energy tax and the VAT on it, so that statements 01 and 03 together add up to the electricity part of invoice 02.
- Options: (a, preferred) report this point's energy tax (277,680) and add it and the VAT on it to the tax and payable amounts, with a second TaxTotal for the excise; this makes the statement explain the bill as its note says; (b) keep the whole-invoice energy tax in one place only and say so, if the world's energy tax is assessed per customer rather than per point; then the payable amounts still need the tax.
- Needs decision: no

### utilities/01#F2 · High · Average amount is March's amount, not the average of the three months
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:AverageAmount` = `11269440`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:Description` = `The average over the last three months is 405433 kWh.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Amount` = `10876320`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Amount` = `11059230`
- Why: `AverageAmount` is "the average monetary amount of the consumption", and the description sets the averaging window to the last three months: (398,400 + 405,100 + 412,800) / 3 = 405,433 kWh, which is right. The amount over the same window is (10,876,320 + 11,059,230 + 11,269,440) / 3 = 11,068,330 XUF, but the element carries 11,269,440, which is March's line amount alone (`/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `11269440`). The same pattern occurs in 03 and 05.
- Condition: AverageAmount is the average of the amounts of the same three months whose quantities the description averages (11,068,330 on a net basis), or the description states another window that the amount matches.
- Options: (a, preferred) 11068330, consistent with the history amounts, which are net of tax; (b) state in the description what the amount averages.
- Needs decision: no

### utilities/01#F3 · Medium · One-time charge type on a monthly-charged item
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:OneTimeChargeType` = `Connection to the 10 kV grid, paid once in 2024`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:OneTimeChargeTypeCode` = `CONN`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine/cac:UtilityItem/cbc:CurrentChargeType` = `Monthly`
- Why: UBL defines `OneTimeChargeType` as "Information about the one-time payment type in case everything is paid One time". The item of this line, electricity per kWh, is charged monthly (CurrentChargeType), so the condition of the definition is not met. The value describes another charge (a connection fee of 2024) that this line neither bills nor credits; nothing in this statement or in invoice 02 relates to it.
- Condition: The utility item carries no one-time charge type, or the line is about a charge that is in fact paid once.
- Options: (a, preferred) drop both elements from this line; (b) if the connection fee must be shown, use a note on the consumption point or contract.
- Needs decision: no

### utilities/01#F4 · Low · Buyer's accounting code for raw materials on an electricity statement
- XPath: `/UtilityStatement/cbc:AccountingCostCode` = `3100`
- XPath: `/UtilityStatement/cbc:AccountingCost` = `Raw materials and parts`
- Why: The buyer's accounting code says electricity for the factory is booked as raw materials and parts. Energy is normally an overhead or production-energy cost, not a raw material. The same value occurs in 12 XML examples (`grep -c 'Raw materials and parts'` over `world/examples/*/*.xml`), elsewhere on orders and invoices for ore, timber and packaging, where it fits; here it looks copied from Valdara's master data. The code 3100 also equals Valdara's ISIC class (`/UtilityStatement/cac:ReceiverParty/cbc:IndustryClassificationCode` = `3100`).
- Condition: The accounting cost of the electricity statement names a cost account that fits energy, the same as in invoice 02.
- Options: (a, preferred) an energy cost code for Valdara, used in 01, 02 and 03 alike; (b) leave the element out of the statement, which only explains the bill.
- Needs decision: no

## Checked and consistent
- Line amount 412,800 kWh × 27.3 = 11,269,440, equal to `02-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:LineExtensionAmount` = `11269440`; price and base quantity equal the invoice line's.
- Meter: (63,280 − 52,960) × MeterConstant 40 = 412,800 kWh = DeliveredQuantity = TotalMeteredQuantity = InvoicedQuantity.
- VAT 20 % × 11,269,440 = 2,253,888; 11,269,440 + 2,253,888 = 13,523,328 (internal arithmetic correct; F1 is about what it leaves out).
- History: 398,400 × 27.3 = 10,876,320 and 405,100 × 27.3 = 11,059,230; February's quantity equals the ConsumptionReportReference (405,100).
- EnergyTaxReport: 288,840 − 0 on account = 288,840 balance.
- Tax category S 20 % VAT matches the invoice line's ClassifiedTaxCategory; currency XUF throughout.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TaxTotal`: a tax total without subtotal or scheme was suspected to be ambiguous — refuted as a separate finding: its amount is identifiable as VAT (20 % of the line), and the missing excise is F1.
- `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount`: the same totals in Consumption and SupplierConsumption were suspected as double counting — refuted: UBL offers the two as alternative views (one supplier or several), and both carry the same amount; the error in them is F1.
