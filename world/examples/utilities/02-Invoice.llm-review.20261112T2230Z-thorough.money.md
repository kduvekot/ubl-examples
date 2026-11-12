# LLM review: 02-Invoice.xml

Flow: utilities (UTILITIES-2026-01) · Review date: 2026-11-12 · Part: money

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
in all. Every finding below, and every entry under "Considered and refuted" and "Outside this
review", is looked into and ends either resolved (its condition holds) or dismissed with a stated
reason. Findings marked "Needs decision: yes" are confirmed by a person first. The example must
remain valid against the UBL 2.5 schemas and the world's code lists. This review only describes
what is wrong; it does not say where or how the example is produced.

## Findings

### utilities/02#F1 · High · Energy tax per-unit amount of 1 XUF/kWh contradicts the tier and the tax amounts
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cac:TaxCategory/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TierRange` = `The first 50,000 kWh of the month`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxAmount` = `60000`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cac:TaxCategory/cbc:PerUnitAmount` = `1`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TierRange` = `Above 50,000 kWh: the industrial rate`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TaxAmount` = `228840`
- Why: `PerUnitAmount` is, "where a tax is applied at a certain rate per unit, the rate per unit applied", here per `BaseUnitMeasure` 1 kWh. At 1 XUF/kWh the first tier ("the first 50,000 kWh") would yield 50,000 XUF, not 60,000, and the two tiers would have the same rate although the second is called "the industrial rate". The amounts work out with 1.2 XUF/kWh on the first 50,000 kWh (60,000) and 0.6 XUF/kWh on the remaining 381,400 kWh of electricity (412,800 + 18,600 − 50,000; 381,400 × 0.6 = 228,840). The subtotals also do not say that the energy tax applies to electricity only: the 61,200 kWh of gas on line 3 are not in either tier, while the tier text speaks of all kWh of the month.
- Condition: PerUnitAmount in each subtotal and its TaxCategory times the tier's quantity equals that subtotal's TaxAmount, and the tiers name the supply they apply to.
- Options: (a, preferred) PerUnitAmount 1.2 and 0.6, and a TierRange or category name that says "electricity"; (b) if 1 XUF/kWh is the intended rate, change the tax amounts and the totals (and statement 01's energy tax report) to match.
- Needs decision: no

### utilities/02#F2 · High · Due date is 21 days after the invoice date; the terms say 30 days net
- XPath: `/Invoice/cbc:DueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-23`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 2 % discount when paid within 10 days.`
- Why: Issued 2026-04-02, "30 days net" gives 2026-05-02; the three due dates give 21 days. The 10-day discount period (`/Invoice/cac:PaymentTerms/cac:SettlementPeriod/cbc:EndDate` = `2026-04-12`) does follow from the note, so the note is the stated term and the due date contradicts it. The same 2026-04-23 appears in 06 (also "30 days net") and in 13 ("45 days net"); only in 09 does it match the note (21 days).
- Condition: The due dates and the net term in the note give the same date.
- Options: (a) due date 2026-05-02; (b, preferred if the world's utility bills are due after 21 days) note "21 days net"; either way the reminder and remittance dates of the flow stay consistent (remittance 04 is within both).
- Needs decision: no

### utilities/02#F3 · Medium · TaxableAmount of the per-unit energy tax equals the tax amount
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cbc:TaxableAmount` = `60000`
- XPath: `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[2]/cbc:TaxableAmount` = `228840`
- Why: `TaxableAmount` is "the net amount to which the tax percent (rate) is applied to calculate the tax amount". The energy tax has no percent; it is calculated per kWh. A taxable amount equal to the tax amount says that a 100 % tax was applied to 60,000 and 228,840 XUF, which is not the case. The net amount of the electricity taxed in the two tiers is 50,000 × 27.3 = 1,365,000 and 381,400 × 27.3 = 10,412,220 XUF (together the 11,777,220 of lines 1 and 2).
- Condition: Each energy-tax subtotal either has no TaxableAmount or carries the net amount of the supply in its tier.
- Options: (a, preferred) leave TaxableAmount out (it is optional, 0..1), since a per-unit tax is fully described by BaseUnitMeasure, PerUnitAmount and TierRange; (b) the net amounts of the tiers.
- Needs decision: no

### utilities/02#F4 · Medium · Electricity and gas classified as a supply of services
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- XPath: `/Invoice/cac:InvoiceLine[3]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `SERVICES`
- Why: The world's SupplyTypeCode list defines GOODS as "A supply of goods, including energy and water delivered through a network." and SERVICES as "A supply of services." (`world/codelists/gc/SupplyTypeCode.gc`). Electricity (lines 1, 2) and natural gas (line 3) are therefore GOODS by the list's own definition, as in VAT practice. The same applies to water in 06, 09 and 11.
- Condition: The supply type of electricity and gas lines is GOODS.
- Options: (a, preferred) GOODS on all three lines.
- Needs decision: no

### utilities/02#F5 · Low · Buyer's accounting code for raw materials on an energy bill
- XPath: `/Invoice/cbc:AccountingCostCode` = `3100`
- XPath: `/Invoice/cbc:AccountingCost` = `Raw materials and parts`
- Why: The buyer's accounting code applied to the invoice as a whole books electricity and gas as raw materials and parts; line 2 has its own code for the warehouse (`/Invoice/cac:InvoiceLine[2]/cbc:AccountingCost` = `Warehouse, Castrano Logistics`). The value occurs in 12 XML examples (counted with `grep -c` over `world/examples/*/*.xml`), mostly orders and invoices for materials, where it fits; here it looks copied from Valdara's master data. The code equals Valdara's ISIC class 3100.
- Condition: The invoice-level accounting cost names an energy cost account of the buyer.
- Options: (a, preferred) an energy cost code, used in 01 and 03 too.
- Needs decision: no

## Checked and consistent
- Lines: 412,800 × 27.3 = 11,269,440; 18,600 × 27.3 = 507,780; 61,200 × 8.4 = 514,080; sum 12,291,300 = LineExtensionAmount = TaxExclusiveAmount.
- VAT: base 12,291,300 + energy tax 288,840 = 12,580,140 (energy tax CalculationSequenceNumeric 1 before VAT 2); 20 % = 2,516,028; TaxInclusiveAmount 15,096,168 = 12,291,300 + 288,840 + 2,516,028 = PayableAmount.
- Settlement discount 2 % of 15,096,168 = 301,923.36 → 301,923; settlement period 2026-04-02 to 2026-04-12 = 10 days as the note says; remittance 04 takes exactly this discount on 2026-04-10.
- Payee account XU080351041600000004084431 passes the IBAN-like check (`check_ids.py`) and is the payee account in remittance 04; RF58FEINV260313 passes the ISO 11649 check and is quoted in 04.
- Penalty interest 8 % per annum (ANN), simple.
- Purpose codes ELEC (lines 1, 2) and GASB (line 3) mean Electricity Bill and Gas Bill in ISO 20022 ExternalPurpose1Code, fitting the lines.

## Considered and refuted
- `/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount`: suspected to omit the excise — refuted: UBL defines it as net of tax, and the energy tax is a tax; TaxInclusiveAmount includes it.
- `/Invoice/cac:TaxTotal[1]/cac:TaxSubtotal[1]/cac:TaxCategory/cbc:Name`: "Energy tax" as a category name with category S was suspected as a scheme name in a category — refuted as minor: the name identifies the category within EXC and contradicts nothing.
- `/Invoice/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID`: the reference to an earlier invoice FE-INV-26-0211 (not among the examples) was considered for its money effect — no amount of this invoice depends on it; whether it should be there belongs to the other lenses.
- `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount`: suspected to be computed on the wrong base — refuted: 2 % of the payable amount, as the note's "2 % discount when paid" reads; whether the discount should reduce the VAT is a tax question raised in 04's review.
