# LLM review: 08-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: money

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

### utilities/08#F1 · High · Monthly payments on account that the invoice neither deducts nor collects that way
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cbc:Note` = `Paid on account each month for the estimated use; the next bill settles it against the reading.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:OnAccountPayment/cac:PaymentTerms/cbc:Note` = `By direct debit on the first working day of each month.`
- XPath: `/UtilityStatement/cac:MainOnAccountPayment/cbc:Note` = `The basis of the direct debit limit.`
- Why: `OnAccountPayment` is "the planned prepayments (on account) regarding this subscription". The statement says the household pays on account each month by direct debit on the first working day, and that the bill settles these payments against the reading. Invoice 09, the bill this statement explains, does neither of these things. It bills the full March consumption with no prepaid amount (`09-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `38.78`, and the invoice has no PrepaidAmount). It also collects that amount by a single direct debit 21 days after the invoice date (`09-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:Note` = `Collected by direct debit 21 days after the invoice date.`). Reminder 10 then shows that this single debit of 38.78 on 23 April was returned. If on-account payments of 14 m³ had been collected on 1 March and 1 April, the March bill would be about 0 after settlement, not 38.78.
- Condition: The way the household pays (monthly on account and settled by the bill, or billed monthly and collected after 21 days) is the same in statement 08, invoice 09 and reminder 10.
- Options: (a, preferred) drop the on-account payments from the statement, because the flow bills each month's actual reading and collects it by direct debit; the mandate's limit can be explained in the mandate or the terms; (b) keep the on-account scheme and give invoice 09 a PrepaidAmount and a settlement amount, then rework 10 and 11 to match.
- Needs decision: yes

### utilities/08#F2 · Medium · The payable amount for the consumption leaves out the sewage levy charged per cubic metre of it
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `32.90`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `32.90`
- Why: Invoice 09 bills the city's sewage levy for the same 14 m³ (`09-Invoice.xml:/Invoice/cac:CollectionInvoiceLine/cbc:LineExtensionAmount` = `5.88`), so the bill comes to 38.78. The statement says it explains the bill, but it shows 32.90 as "the total amount payable on this consumption, including any allowances, charges, or taxes" and never mentions the levy. The same problem is in 05.
- Condition: The statement accounts for everything invoice 09 charges for this consumption point, or it says that the levy is added on the invoice.
- Options: (a, preferred) add a consumption line for the levy and set the payable totals to 38.78; (b) add a note naming the levy of 5.88.
- Needs decision: yes

### utilities/08#F3 · Medium · District-heating correction priced per cubic metre with a unit amount defined per MWh, charged by the water company
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionUnitAmount` = `0.80`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:ConsumptionWaterQuantity` = `6.2`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:CorrectionAmount` = `19.84`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:MeterNumber` = `CSW-H-71844`
- Why: UBL defines `CorrectionUnitAmount` as "Correction per MWH per degree C". The amount here is 6.2 m³ × 4 °C × 0.80 = 19.84 (the only product of the stated figures that gives 19.84), so the unit amount is applied per m³ per °C, not per MWh. The correction is also for a district-heating network: the meter CSW-H-71844 is not among this statement's meters, and the supplier is the water company, which supplies no heat in this flow. Nothing in the flow states who will charge the 19.84 "on the annual account".
- Condition: The unit amount, the quantity and the amount fit the definition (per MWh per °C) and multiply out, and the party charging the correction is the one that supplies the heat.
- Options: (a, preferred) drop the correction from the water statement (it belongs to a district-heating supplier's statement); (b) if the water company runs the heating network in the world, express the quantity in MWh and say so.
- Needs decision: yes

### utilities/08#F4 · Low · The household's bank account in a statement that collects nothing
- XPath: `/UtilityStatement/cac:ReceiverParty/cac:Person/cac:FinancialAccount/cbc:ID` = `XB64BLUM38010007251840`
- Why: A utility statement explains consumption; it carries no payment means. The account is the payer account of the mandate in invoice 09 (`09-Invoice.xml:/Invoice/cac:PaymentMeans/cac:PaymentMandate/cac:PayerFinancialAccount/cbc:ID` = `XB64BLUM38010007251840`), so here it reads as copied from the customer's master data.
- Condition: The statement carries the account only if it uses it.
- Options: (a, preferred) leave the account out of this statement.
- Needs decision: no

## Checked and consistent
- 14 m³ × 2.35 = 32.90 = invoice 09 line 1; exempt (E, WATER), tax 0.00.
- Meter: 1,844 − 1,830 = 14 m³ × MeterConstant 1 = DeliveredQuantity = TotalMeteredQuantity.
- History: 15 × 2.35 = 35.25; 13 × 2.35 = 30.55; average (15 + 13 + 14) / 3 = 14 m³, and (35.25 + 30.55 + 32.90) / 3 = 32.90 = AverageAmount (correct here).
- The mandate limit in 09 (150.00 per instruction) is well above the estimate (14 m³ ≈ 38.78 with the levy), as the MainOnAccountPayment terms say.
- Account XB64BLUM38010007251840 passes the IBAN-like check.

## Considered and refuted
- `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:DifferenceTemperatureReductionQuantity`: the sign −4 was checked. It is consistent: actual cooling 31 °C against a standard of 35 °C is a shortfall, and that makes a charge.
