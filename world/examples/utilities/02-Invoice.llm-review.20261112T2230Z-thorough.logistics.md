# LLM review: 02-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: logistics

## Reviewed version
- Run: `20261112T2230Z-thorough`
- Example: `world/examples/utilities/02-Invoice.xml`, Git blob `b2993194ed77fe144060459952d69428ed29f5bc` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 7b0e1fe 2026-11-12 Reviews of the rail flow, run 20261112T2137Z-thorough: merge complete
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

### utilities/02#F1 · High · Energy tax per kWh and tier ranges do not give the tax amounts
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxAmount` = `60000`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TierRange` = `The first 50,000 kWh of the month`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cac:TaxCategory/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TaxAmount` = `228840`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TierRange` = `Above 50,000 kWh: the industrial rate`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:PerUnitAmount` = `1`
- Why: PerUnitAmount is "Where a tax is applied at a certain rate per unit, the rate per unit applied", with BaseUnitMeasure 1 kWh. At 1 XUF per kWh the first tier, "the first 50,000 kWh", can give at most 50,000 XUF, not 60,000; and the second tier is described as a different ("industrial") rate but has the same rate 1. The invoice bills 412,800 + 18,600 = 431,400 kWh of electricity (lines 1 and 2). The amounts work out only with other rates: 50,000 kWh × 1.2 = 60,000 and (431,400 − 50,000) = 381,400 kWh × 0.6 = 228,840. At 1 XUF/kWh the two tiers would together tax 288,840 kWh, which matches no quantity in the invoice (431,400 kWh electricity, 492,600 kWh with gas). The TaxableAmount of each subtotal is equal to its TaxAmount (60,000; 228,840), which is neither the taxed quantity nor a monetary base the rate applies to.
- Condition: for each tier, taxed kWh × PerUnitAmount = TaxAmount, the kWh of the tiers add up to the electricity billed (431,400 kWh, or the quantity the world's energy tax applies to), and the tier rates differ if the TierRange says they do.
- Options: (a, preferred) PerUnitAmount 1.2 and 0.6 (in subtotal and category), keeping the amounts; state the taxed quantity where UBL allows it (e.g. in the TierRange text) and give a TaxableAmount that is the monetary base, or leave the per-unit nature to BaseUnitMeasure; (b) keep the rate 1 and recompute both tiers and the totals (50,000 and 381,400), which changes VAT and payable amounts and the follow-up remittance 04.
- Needs decision: no

### utilities/02#F2 · Low · Billing reference to line 2 of an earlier invoice with no purpose stated
- XPath: `/Invoice/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `FE-INV-26-0211`
- XPath: `/Invoice/cac:BillingReference/cac:BillingReferenceLine/cbc:ID` = `2`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:InvoicedQuantity` = `18600`
- XPath: `03-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:Consumption/cac:EnergyWaterSupply/cac:EnergyWaterConsumptionCorrection/cbc:Description` = `February's estimate of 17,200 kWh was 750 kWh too high, as the actual reading shows.`
- Why: an ordinary invoice (380) refers to line 2 of the February invoice FE-INV-26-0211 (not among the examples, which is acceptable in itself) without saying why. The only link in the flow is the warehouse statement 03, which corrects February's estimate for the warehouse meter (this invoice's line 2). But nothing in this invoice applies a correction: line 2 bills 18,600 kWh × 27.3 = 507,780, the metered March quantity, with no allowance, charge or credit for 750 kWh. The reference therefore points at an earlier line whose correction this invoice does not carry (see also utilities/03#F1).
- Condition: either the invoice carries the correction that the reference to the February line stands for (and the statement 03 and this invoice agree on it), or the billing reference is absent or says what it refers to.
- Options: (a) if the February estimate is corrected on this bill, add the correction (e.g. an allowance on line 2 of 750 kWh × 27.3 = 20,475) and keep the reference; (b, preferred if the March reading already settles February, see utilities/03#F1) remove the billing reference.
- Needs decision: yes (whether this bill corrects February's estimate changes the story)

### utilities/02#F3 · Low · Delivery location of line 2 given only as text
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Delivery/cac:DeliveryLocation/cbc:Description` = `Castrano Logistics warehouse, Ferrano`
- XPath: `03-UtilityStatement.xml:/UtilityStatement/cac:SubscriberConsumption/cac:UtilityConsumptionPoint/cbc:ID` = `FE-CP-4160-07`
- Why: the line names the warehouse as its delivery location only in free text, while the statement 03 identifies the same place as consumption point FE-CP-4160-07 with an address. The meter in the line's PurchaseReference already links the line to the warehouse; the location as given adds nothing that can be matched to the statement. Line 1 (the factory) has no delivery location at all, so the two lines treat the same kind of information differently.
- Condition: the delivery location of line 2 is either absent or identified so that it matches the consumption point of 03 (its ID or address).
- Options: (a, preferred) give the location the consumption point's ID FE-CP-4160-07; (b) remove the Delivery aggregate, as the meter reference already identifies the point.
- Needs decision: no

## Checked and consistent
- Lines: 412,800 × 27.3 = 11,269,440; 18,600 × 27.3 = 507,780; 61,200 × 8.4 = 514,080; sum 12,291,300 = LineExtensionAmount; LineCountNumeric 3.
- VAT base 12,291,300 + 288,840 = 12,580,140; 20 % = 2,516,028; payable 15,096,168, as paid in 04-RemittanceAdvice.xml.
- Line 1 and line 2 match the statements 01 (meter FE-M-881204, 412,800 kWh) and 03 (meter FE-M-881377, 18,600 kWh) in quantity, price, amount and line number (ParentDocumentLineReferenceID 1 and 2).
- Gas line 3: 1,350 m³ at 4 bar converted to 61,200 kWh agrees with the grid operator's statement energy/01-UtilityStatement.xml (meter FG-G-20417, readings 28,410 to 29,760 m³, 1,350 m³ × 4.9477 = 6,679 m³ at standard conditions × 9.163 kWh/m³ = 61,200 kWh). Physics: a factor of 4.95 corresponds to 4 bar gauge (5.01 bar absolute / 1.013), and 9.16 kWh/m³ is within the range of a low-calorific natural gas (own knowledge).
- Invoice period 2026-03-01 to 2026-03-31 on header and lines; due date 2026-04-23 = issue date + 21 days.
- Check digits (check_ids.py): RF58FEINV260313, account XU080351041600000004084431 and ISIN XU0001042501 OK.

## Considered and refuted
- `/Invoice/cac:InvoiceLine[1]/cac:PurchaseReference/cbc:ID`: a meter number in a purchase reference — refuted because UBL 2.5 defines PurchaseReference as "A reference to an object, such as a subscription number, telephone number, meter, vehicle, person, etc., to which this Invoice Line relates".
- `/Invoice/cac:InvoiceLine[3]/cbc:Note`: "4 bar" could be gauge or absolute, which changes the conversion by about 25 % — refuted because the grid operator's statement in the energy flow gives the factor 4.9477, i.e. gauge pressure, and the arithmetic holds.

## Outside this review
- Outside the logistics lens (money): the settlement discount (2 % of the tax-inclusive 15,096,168 = 301,923) is computed on an amount that includes VAT and energy tax; for the money part to judge.
