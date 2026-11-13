# LLM review: 09-Invoice.xml

Flow: furniture (FURNITURE-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0047Z-thorough`
- Example: `world/examples/furniture/09-Invoice.xml`, Git blob `ee49a007b8043177d29c63f3b1b0c8223f117844` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2576809 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: merge complete
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

### furniture/09#F1 · Low · Resale exemption on a free care kit the store gives away
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReasonCode` = `RESALE`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory/cbc:TaxExemptionReason` = `Sale for resale or manufacture`
- XPath: `/Invoice/cac:InvoiceLine[2]/cbc:Note` = `Wood oil and a cloth, for the store to hand to its customers.`
- Why: `TaxExemptionReasonCode` is "The reason for tax being exempted, expressed as a code". The line's own note says the care kits are free of charge and meant to be handed to the store's customers, not sold on; the reason "Sale for resale or manufacture" does not describe that supply. In sales tax practice (own knowledge) promotional goods a retailer gives away are usually not covered by a resale exemption; whether a free supply with a taxable base of 0 needs an exemption reason at all, or another category, is a tax judgment the world has to make. The amount is 0.00 either way, so the totals are not affected.
- Condition: The tax category and reason of line 2 describe what happens to the care kits (handed on free with the benches, or given to the store for its own use), consistently with the line note.
- Options: (preferred) decide in the world whether free promotional goods passed on with resold goods count as resale; if yes, say so in the reason text (e.g. "supplied with goods for resale"); if not, use the category and reason that apply to a free supply; or drop the note's statement if the kits are in fact resold.
- Needs decision: yes

### furniture/09#F2 · Low · Supply type given for line 1 but not for line 2
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Item/cac:ClassifiedTaxCategory`
- Why: Both lines are goods under the same exempt STT category, but only line 1 states the supply type. A reader of line 2 cannot tell whether the omission means something (IND6, nothing implied by absence). In 17-Invoice every line carries `SupplyTypeCode`.
- Condition: Either both lines state their supply type, or neither does, unless a reason for the difference is given.
- Options: (preferred) add `SupplyTypeCode` GOODS to line 2; or remove it from line 1 if the world does not need it for this invoice.
- Needs decision: no

### furniture/09#F3 · Low · Sub-line prices and the free line's price without base quantity
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:SubInvoiceLine[1]/cac:Price/cbc:PriceAmount` = `380`
- XPath: `/Invoice/cac:InvoiceLine[1]/cac:SubInvoiceLine[2]/cac:Price/cbc:PriceAmount` = `115`
- XPath: `/Invoice/cac:InvoiceLine[2]/cac:Price/cbc:PriceAmount` = `0`
- Why: `BaseQuantity` is "The quantity at which this price applies". Line 1 states it (`/Invoice/cac:InvoiceLine[1]/cac:Price/cbc:BaseQuantity` = `1`, SET); the sub-line prices and the price of line 2 do not, so the unit they apply to is implied by absence (IND6). The same occurs in 08-Order and 10-Order; 12 of 117 `Price` elements with a `PriceAmount` in `world/examples/*/*.xml` lack `BaseQuantity` (script count).
- Condition: Every `Price` in the invoice states the quantity it applies to, or the convention that a missing base quantity means one unit is recorded as a deliberate decision.
- Options: (preferred) add `BaseQuantity` 1 EA to the three prices; or record the convention.
- Needs decision: no

## Checked and consistent
- Lines: 20 sets × 610 = 12200.00 (`/Invoice/cac:InvoiceLine[1]/cbc:LineExtensionAmount` = `12200.00`); sub-lines 20 × 380 = 7600.00 and 40 × 115 = 4600.00, sum 12200.00; line 2 free of charge, 0.00.
- Totals: `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `12200.00` = tax exclusive = tax inclusive (tax 0.00) = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `12200.00`; `/Invoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `12200.00` covers both lines (line 2 adds 0.00).
- Against the order: price, quantity and tax treatment equal 08-Order (`08-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `12200.00`).
- Due date: 2026-03-22 + 30 days = 2026-04-21 = `/Invoice/cbc:DueDate` = `2026-04-21` = `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-21`, as the terms note "30 days net" says.
- Penalty: 1.5 % × 12200.00 = 183.00 = `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `183.00`, for one month (`/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1`) starting the day after the due date (`/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:StartDate` = `2026-04-22`), as the note "1.5 % surcharge per month late" says.
- Payment reference: `/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF74BFINV260575` passes the ISO 11649 check (check_ids.py), is built from the invoice number by the creditor and is repeated in the instruction note.
- Account: `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB42BLUM38712004503347` passes the IBAN-style check, contains the branch code 387120 of the Marrowdale branch and the bank code BLUM of `BLUMXBLX`, is held in the seller's name, and is the same account in 17-Invoice (`17-Invoice.xml:/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB42BLUM38712004503347`).
- Follow-up: 13-CreditNote refers to this invoice with the right issue date and credits 6 of the 20 sets at the invoiced price 610.

## Considered and refuted
- `/Invoice/cac:InvoiceLine[2]/cbc:FreeOfChargeIndicator` = `true`: suspected that a line not in the order (08-Order has one line) is billed. Refuted because it is free of charge (0.00) and adds nothing to the amount to be paid.
- `/Invoice/cac:PaymentTerms/cbc:PenaltySurchargePercent` = `1.5`: suspected that a monthly rate in an element defined as "the penalty for payment after the settlement period, expressed as a percentage of the payment" is ambiguous about the period. Refuted because `PenaltyPeriod` (one month) and the terms note state the period, and the penalty amount matches.
