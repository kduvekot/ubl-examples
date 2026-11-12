# LLM review: 07-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/07-Invoice.xml`, Git blob `0345a2bca9a5957f58f15a04460ca368ab893cee` (committed)
- Last commit changing the example: 294c2e3 2026-11-12 English names for the island's towns; town names in both languages everywhere
- Checkout: branch `claude/keen-feynman-45qjti`, commit ebb6439 2026-11-12 Reviews of the energy flow, run 20261112T1608Z-thorough: all merged reviews
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

### packaging/07#F1 · Low · Men's shirts charged to the buyer's "Garden department"
- XPath: `/Invoice/cbc:AccountingCost` = `Garden department`
- XPath: `/Invoice/cbc:AccountingCostCode` = `6120`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Name` = `Cotton shirt`
- Why: UBL defines `Invoice/AccountingCost` as "The buyer's accounting code, applied to the Invoice as a whole, expressed as text". The invoice bills 600 men's shirts that Brightmarket sells in its clothing department (`08-PurchaseReceipt.xml:/PurchaseReceipt/cac:PointOfSaleLocation/cbc:Description` = `Clothing, first floor`); it repeats the order's `05-Order.xml:/Order/cbc:AccountingCost` = `Garden department`, Brightmarket's cost centre in 12 XML files (`grep -rl --include='*.xml' '>Garden department<' world/examples`).
- Condition: the cost centre fits clothing and equals the order's.
- Options: (a, preferred) a clothing-department cost centre in order and invoice; (b) drop it from both.
- Needs decision: no

### packaging/07#F2 · Low · A penalty period of one month against "1.5 % surcharge per month late"
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- Why: `PenaltyPeriod` is "The period during which penalties may apply"; one month from 2026-06-12 limits penalties to that month, while the note makes the surcharge recur monthly. `PenaltyAmount` = 130.50 is one month's surcharge (1.5 % × 8700.00). Same pattern as `02-Invoice.xml` and `04-Invoice.xml` (18 XML files with a one-month `PenaltyPeriod`, `grep -rl --include='*.xml' '<cac:PenaltyPeriod>' world/examples`).
- Condition: the penalty period does not end before the terms say penalties stop.
- Options: (a, preferred) start date only; the note states 130.50 as the surcharge per month; (b) a stated cap, with the duration kept.
- Needs decision: no

## Checked and consistent
- Line arithmetic: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `600` × `/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `14.5` = 8700.00 = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `8700.00`; tax 0.00.
- Against the order and the despatch: `/Invoice/cac:OrderReference/cbc:ID` = `BS-PO-26-0525` resolves to `05-Order.xml` (600 at 14.50, E/RESALE/STT); `06-DespatchAdvice.xml:/DespatchAdvice/cac:DespatchLine/cbc:DeliveredQuantity` = `600` equals the invoiced quantity, and the invoice (14:49) follows the despatch advice (11:35) on the same day.
- Payment terms: 2026-05-12 + 30 days = 2026-06-11 = `/Invoice/cbc:DueDate` = `2026-06-11`, equal in `PaymentMeans` and `PaymentTerms`; `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `130.50` = 1.5 % × 8700.00.
- Payment means: domestic credit transfer (`MPNS`, `LUMEPAY`) to Lumeport Textile Mill's own account `XB35BLUM38020504608076` (valid check digits, check_ids.py), RF reference `RF18LTMINV260529` valid.
