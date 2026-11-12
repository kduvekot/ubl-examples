# LLM review: 05-UtilityStatement.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/05-UtilityStatement.xml`, Git blob `f5bb8506980bfe0a7e311a1ed3ba8b85f0c771d7` (committed)
- Last commit changing the example: c364f0c 2026-11-11 Stage 5, sea and fillers: the second feeder's report, the last fillers, a GRAI
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

### utilities/05#F1 · High · Average amount is March's amount, not the three-month average
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:AverageAmount` = `202.10`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionAverage/cbc:Description` = `The average over the last three months is 82 m³.`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[1]/cbc:Amount` = `190.35`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:ConsumptionReport/cac:ConsumptionHistory[2]/cbc:Amount` = `185.65`
- Why: The quantity average is right ((81 + 79 + 86) / 3 = 82 m³), but `AverageAmount`, "the average monetary amount of the consumption", is March's 202.10 alone; over the same three months it is (190.35 + 185.65 + 202.10) / 3 = 192.70 XBL. Same pattern as in 01 and 03 (in 08 the two happen to coincide).
- Condition: AverageAmount is the average of the amounts of the window the description names.
- Options: (a, preferred) 192.70.
- Needs decision: no

### utilities/05#F2 · Medium · Payable amount of the consumption leaves out the sewage levy billed per cubic metre of it
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `202.10`
- XPath: `/UtilityStatement/cac:SubscriberConsumption/cac:SupplierConsumption/cac:Consumption/cac:LegalMonetaryTotal/cbc:PayableAmount` = `202.10`
- XPath: `/UtilityStatement/cbc:Note` = `This statement explains the consumption behind your bill.`
- Why: The Consumption's `LegalMonetaryTotal` is "the total amount payable on this consumption, including any allowances, charges, or taxes". Invoice 06 bills, for the same 86 m³, the city's sewage levy of 0.42 XBL/m³ as a collection line (`06-Invoice.xml:/Invoice/cac:CollectionInvoiceLine/cbc:LineExtensionAmount` = `36.12`), and the bill totals 238.22 (`06-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `238.22`). The statement, which says it explains the bill, shows 202.10 as payable on this consumption and does not mention the levy. Whether a levy collected for a third party is "payable on this consumption" is arguable, but it is charged per m³ of exactly this consumption and paid with the same bill. The same occurs in 08 (levy 5.88 of invoice 09).
- Condition: The statement accounts for the whole amount the invoice charges for this consumption point, or states that the levy is billed separately on the invoice.
- Options: (a, preferred) a second ConsumptionLine for the levy (ParentDocumentLineReferenceID 2), with the payable totals at 238.22; (b) keep the totals at the water company's own supply and say in a note that the city's levy of 36.12 is added on the invoice.
- Needs decision: yes

## Checked and consistent
- 86 m³ × 2.35 = 202.10 = invoice 06 line 1; the exemption (E, 0 %, WATER) and the price equal the invoice line's.
- Meter: 4,298 − 4,212 = 86 m³ × MeterConstant 1 = DeliveredQuantity = TotalMeteredQuantity.
- History: 81 × 2.35 = 190.35; 79 × 2.35 = 185.65; February equals the ConsumptionReportReference (79 m³).
- Tax amount 0.00 for an exempt supply; TaxInclusiveLineExtensionAmount 202.10 equals the line amount.

## Considered and refuted
- `/UtilityStatement/cbc:AccountingCost`: "Garden department" for the water of a shop was suspected as copied master data — refuted: a store's garden department is a plausible user of water, and invoice 06 carries the same code.
