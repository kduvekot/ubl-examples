# LLM review: 04-Invoice.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/04-Invoice.xml`, Git blob `b7615e989edc233d99c6d2b1a77b5e429b9d95e3` (committed)
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

### packaging/04#F1 · Low · Garment bags charged to the buyer's cost centre "Raw cotton"
- XPath: `/Invoice/cbc:AccountingCost` = `Raw cotton`
- XPath: `/Invoice/cbc:AccountingCostCode` = `2200`
- XPath: `/Invoice/cac:InvoiceLine/cac:Item/cbc:Name` = `Garment bag`
- Why: UBL defines `Invoice/AccountingCost` as "The buyer's accounting code, applied to the Invoice as a whole, expressed as text". The invoice bills 20 000 polyethylene garment bags, not raw cotton; it repeats the cost centre of `03-Order.xml:/Order/cbc:AccountingCost` = `Raw cotton`, which Lumeport Textile Mill also uses for raw cotton in the cotton flow. 5 XML files carry "Raw cotton" (`grep -rl --include='*.xml' '>Raw cotton<' world/examples`).
- Condition: the cost centre fits packaging material and equals the one in the order.
- Options: (a, preferred) a packaging cost centre for the mill, the same in order and invoice; (b) drop the accounting cost from both.
- Needs decision: no

### packaging/04#F2 · Low · A penalty period of one month against "1.5 % surcharge per month late"
- XPath: `/Invoice/cac:PaymentTerms/cac:PenaltyPeriod/cbc:DurationMeasure` = `1`
- XPath: `/Invoice/cac:PaymentTerms/cbc:Note` = `30 days net; 1.5 % surcharge per month late.`
- Why: `PenaltyPeriod` is "The period during which penalties may apply"; a one-month period from 2026-06-03 limits penalties to about a month, while the note makes the surcharge recur for every month late. `PenaltyAmount` = 24.00 is one month's surcharge (1.5 % × 1600.00). Same pattern as `02-Invoice.xml` and `07-Invoice.xml` (18 XML files with a one-month `PenaltyPeriod`, counted with `grep -rl --include='*.xml' '<cac:PenaltyPeriod>' world/examples`).
- Condition: the penalty period does not end before the terms say penalties stop.
- Options: (a, preferred) start date only, no duration; state in the note that 24.00 is the surcharge per month; (b) a stated cap in the terms, with the duration kept.
- Needs decision: no

## Checked and consistent
- Line arithmetic: `/Invoice/cac:InvoiceLine/cbc:InvoicedQuantity` = `20000` × `/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `0.08` = 1600.00 = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `1600.00`; tax 0.00; tax-exclusive and tax-inclusive amounts 1600.00.
- Against the order: `/Invoice/cac:OrderReference/cbc:ID` = `LTM-PO-26-0523` resolves to `03-Order.xml`; quantity, price, item and tax treatment (E, RESALE, STT) agree.
- Payment terms: 2026-05-03 + 30 days = 2026-06-02 = `/Invoice/cbc:DueDate` = `2026-06-02`, equal in `PaymentMeans` and `PaymentTerms`; `/Invoice/cac:PaymentTerms/cbc:PenaltyAmount` = `24.00` = 1.5 % × 1600.00.
- Payment means: credit transfer over the domestic rail (`MPNS`, `LUMEPAY`) between two Lumeport companies; payee account equals the supplier's account in `02-Invoice.xml`; RF reference `RF72RPINV260524` valid (check_ids.py). No charge bearer for a domestic transfer is fine.

## Considered and refuted
- `/Invoice/cac:PaymentMeans/cbc:PaymentChannelCode` = `MPNS` against `RTNS` in `02-Invoice.xml`: suspected an inconsistency of the same seller — refuted because 02 is paid from Urvania over the Trade Accord rail, 04 domestically over LUMEPAY; different rails explain different channels.
- `/Invoice/cac:AccountingSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`: refuted as a duplicate: it is the account of the party receiving the payment and equals the payee account.
