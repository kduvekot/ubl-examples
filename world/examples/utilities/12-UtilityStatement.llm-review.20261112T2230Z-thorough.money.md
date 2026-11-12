# LLM review: 12-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/12-UtilityStatement.xml`, Git blob `56f0cda5a64095e59535dfa5c867cb5b911ef1b7` (committed)
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

### utilities/12#F1 · High · Line totals "including all allowances" ignore the allowance given on the same line
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cbc:TaxInclusiveLineExtensionAmount` = `21.180`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cbc:TaxInclusiveLineExtensionAmount` = `21.180`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[3]/cbc:TaxInclusiveLineExtensionAmount` = `21.180`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[4]/cbc:TaxInclusiveLineExtensionAmount` = `21.180`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[5]/cbc:TaxInclusiveLineExtensionAmount` = `21.180`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[6]/cbc:TaxInclusiveLineExtensionAmount` = `21.180`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:AllowanceCharge/cbc:Amount` = `1.059`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cbc:TaxInclusiveLineExtensionAmount` = `127.080`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:AllowanceCharge/cbc:Amount` = `6.354`
- Why: UBL defines `TaxInclusiveLineExtensionAmount` as "The total amount for this telecommunications supply line, including all allowances, charges and taxes", and for the consumption line as "The total amount for this consumption line, including all allowances, charges and taxes". Each business line carries a 5 % discount of 1.059 and no tax, so its total is 21.180 − 1.059 = 20.121, not 21.180. Consumption line 1 carries the discount of 6.354, so its total is 127.080 − 6.354 = 120.726. The consumption line's `LineExtensionAmount` is defined as "including discount", which also gives 120.726 (`/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cbc:LineExtensionAmount` = `127.080`).
- Condition: On every line that carries an allowance, the tax-inclusive total (and, on the consumption line, the line extension amount) equals the amount after that allowance.
- Options: (a, preferred) 20.121 on supply lines 1–6 and 120.726 on consumption line 1 (and as its LineExtensionAmount); (b) move the discount off the lines to the consumption level only, so that the line totals of 21.180 and 127.080 hold.
- Needs decision: no

### utilities/12#F2 · High · Allowance of 2.400 on an international call priced at 0, missing from every total
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cac:AllowanceCharge/cbc:Amount` = `2.400`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cac:AllowanceCharge/cbc:BaseAmount` = `2.400`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cbc:CallBaseAmount` = `0.000`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[2]/cac:Price/cbc:PriceAmount` = `0`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:AllowanceTotalAmount` = `6.354`
- Why: The call to Bayvarra (12 minutes) is priced at 0, with a base amount and an extension amount of 0. Its allowance takes 2.400 off a base of 2.400, an amount the call never had. If the allowance were applied, the call would cost −2.400. The consumption's allowance total, "the total monetary amount of all allowances", is 6.354, which is the bundle discount alone (6 × 1.059), so it does not contain the 2.400. Either the call's undiscounted value is 2.400 (then price, base amount and the allowance total must show it), or the call is simply included (then there is nothing to allow).
- Condition: The call's price, base amount, allowance and extension amount multiply out, and every allowance is in AllowanceTotalAmount.
- Options: (a, preferred) price 0.2 per minute and CallBaseAmount 2.400, with the allowance of 2.400 and extension 0.000, and AllowanceTotalAmount 8.754 with the line totals adjusted. This keeps the "included in the subscription" reason visible; (b) remove the allowance and keep price 0 with the reason in a note.
- Needs decision: no

### utilities/12#F3 · Medium · The same bundle discount appears at three levels
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:AllowanceCharge/cbc:Amount` = `6.354`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:AllowanceCharge/cbc:Amount` = `1.059`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:AllowanceCharge/cbc:Amount` = `6.354`
- Why: The Consumption carries the 5 % bundle discount of 6.354 as "an allowance or charge that may apply with this consumption". Each of its six supply lines carries its share of 1.059 again (6 × 1.059 = 6.354), and the supplier view's consumption line 1 carries 6.354 once more. Within the same Consumption the allowances add up to 12.708, while the total says 6.354. A reader cannot tell which of these is the allowance and which are repetitions. The invoice gives the discount once, at document level (`13-Invoice.xml:/Invoice/cac:AllowanceCharge/cbc:Amount` = `6.354`).
- Condition: Within one Consumption, the discount is given once (at the level where it is calculated), and the allowances present add up to AllowanceTotalAmount.
- Options: (a, preferred) keep the discount on the six supply lines and on consumption line 1 (each view once) and remove it from the Consumption level; (b) keep it only at the Consumption level.
- Needs decision: no

### utilities/12#F4 · Medium · Six lines for one month expressed as six months
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cbc:InvoicedQuantity` = `6`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:Price/cbc:BaseQuantity` = `1`
- Why: The quantity has unitCode MON, so it says six months of subscription. The period of the line is 2026-03-01 to 2026-03-31, and the supply lines show six telephone lines for that one month. The quantity counts lines, not months. The same quantity is in invoice 13 line 1 (`13-Invoice.xml:/Invoice/cac:InvoiceLine[1]/cbc:InvoicedQuantity` = `6`).
- Condition: The invoiced quantity's unit counts what is billed (line-months or lines), consistent with the one-month period.
- Options: (a, preferred) 6 with a count unit (C62 or a "line" unit), and the price per line per month stated in the base quantity or UnstructuredPrice; the same change in invoice 13.
- Needs decision: no

### utilities/12#F5 · Low · Exchange rates that convert nothing
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cac:ExchangeRate/cbc:CalculationRate` = `0.4`
- Why: The line-level rate is defined as "Exchanges rates used to calculate the amount for this line", and the service-level rate as "A exchanges rates used in the pricing". No amount on line 1 or on the roaming service is in XBL or results from a conversion: the line is the XLC subscription price of 21.180, and the roaming service has no amount at all. The rate itself (1 XBL = 0.4 XLC) is the same as in the other examples that convert XBL to XLC.
- Condition: An exchange rate is present only where an amount of the line or service was converted with it.
- Options: (a, preferred) remove both, or (b) give the roaming service its XBL charge and converted amount.
- Needs decision: no

### utilities/12#F6 · Low · Roaming data of 35 GB on one line, unpriced, equal to the whole data pool billed on line 7
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[1]/cac:TelecommunicationsService[3]/cbc:Quantity` = `35`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cac:TelecommunicationsService/cbc:Quantity` = `35`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[7]/cac:TelecommunicationsService/cbc:CallExtensionAmount` = `14.840`
- Why: Line 1 shows 35 GB of roaming data in Bayvarra on 18 March with no amount. The data pool (line 7) bills 35 GB "beyond the subscription" for 14.840, and the total metered quantity is 35 GB. The reader cannot tell whether the roaming 35 GB are the pool's 35 GB listed twice (then it is double), or extra data that is free (then the pool and the total are wrong), or charged under a roaming tariff that the statement does not show.
- Condition: Each gigabyte appears once with its charge, and the total metered quantity is their sum.
- Options: (a, preferred) mark the roaming service as part of the pool's 35 GB (for example with the pool line referring to it) and keep its amount at 0; (b) give roaming its own quantity and charge.
- Needs decision: yes

### utilities/12#F7 · Low · A pay-per-view film at no charge
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[2]/cbc:PayPerView` = `true`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:TelecommunicationsSupply/cac:TelecommunicationsSupplyLine[2]/cac:TelecommunicationsService[2]/cbc:CallExtensionAmount` = `0.000`
- Why: Pay-per-view means that the viewing is charged, but the amount to be paid is 0.000 and there is no allowance that explains it.
- Condition: A pay-per-view service carries its charge (or an allowance waiving it), or it is not marked as pay-per-view.
- Options: (a) set PayPerView false (training video included in the business plan); (b) give it a price.
- Needs decision: no

### utilities/12#F8 · Low · Telephone lines booked to "Stock for municipal projects"
- XPath: `/UtilityStatement/cbc:AccountingCostCode` = `500`
- XPath: `/UtilityStatement/cbc:AccountingCost` = `Stock for municipal projects`
- Why: Velumi Trading's accounting code for stock purchases is applied to its office telephone and data costs. It occurs in 10 XML examples (counted with grep over `world/examples/*/*.xml`), most of them goods purchases where it fits; here it looks copied from master data. Invoice 13 carries the same value.
- Condition: The accounting cost names a cost account that fits telecommunications.
- Options: (a, preferred) a telecom or office cost code, the same in 12 and 13.
- Needs decision: no

### utilities/12#F9 · Low · A 0 % rate with category O under a "no sales tax" scheme
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[1]/cac:UtilityItem/cac:TaxCategory/cbc:Percent` = `0`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:ConsumptionLine[2]/cac:UtilityItem/cac:TaxCategory/cbc:Percent` = `0`
- Why: Category O has no rate, so 0 % suggests zero-rating (Z). The same is in invoice 13 (13#F5).
- Condition: Category O carries no Percent.
- Options: (a, preferred) leave Percent out.
- Needs decision: no

## Checked and consistent
- 6 × 21.180 = 127.080 and the data pool's 35 × 0.424 = 14.840 add up to 141.920, which is TotalAmount and LineExtensionAmount. 141.920 − 6.354 = 135.566, which is PayableAmount and equals invoice 13's PayableAmount.
- The 5 % discount on each line: 21.18 × 0.05 = 1.059. On the subscriptions: 127.08 × 0.05 = 6.354.
- The consumption lines refer to invoice 13's lines 1 and 2 with the same quantities, prices and amounts.
- The exchange rate of 0.4 XBL→XLC is the same as in the other examples that convert XBL to XLC (counted over `world/examples/*/*.xml`).
- The amounts have three decimals, consistent with XLC as used throughout the flow.
