# LLM review: 03-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T1631Z-thorough`
- Example: `world/examples/packaging/03-Order.xml`, Git blob `4c3acea07de9e59031f62d8970fa32ff7a492ca6` (committed)
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

### packaging/03#F1 · Low · Garment bags charged to the buyer's cost centre "Raw cotton"
- XPath: `/Order/cbc:AccountingCost` = `Raw cotton`
- XPath: `/Order/cbc:AccountingCostCode` = `2200`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name` = `Garment bag`
- Why: UBL defines `Order/AccountingCost` as "The buyer's accounting cost centre, applied to the Order as a whole, expressed as text". The order is for 20 000 polyethylene garment bags (packaging), which are not raw cotton. The same cost centre is used by Lumeport Textile Mill in the cotton flow for seed and raw cotton (`cotton/08-Order.xml:/Order/cbc:AccountingCost` = `Raw cotton`), so it looks like the buyer's one cost centre copied into every purchase. "Raw cotton" occurs in 5 XML files (counted with `grep -rl --include='*.xml' '>Raw cotton<' world/examples`), two of them this order and its invoice.
- Condition: the cost centre in the order fits what is bought (packaging material), and the invoice `04-Invoice.xml` carries the same one.
- Options: (a, preferred) give the textile mill a packaging or production-supplies cost centre for this purchase (e.g. "Packaging materials"), with its own code; (b) drop `AccountingCost`/`AccountingCostCode` from this order if the mill has no other cost centre in the world.
- Needs decision: no

### packaging/03#F2 · Low · The seller's bank account in a buyer's order that pays nothing
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: as in `01-Order.xml`: the Order is issued by the buyer and has no `PaymentMeans` or `PaymentTerms`; nothing in it uses the seller's account (definition: "The financial account associated with this party"). The invoice `04-Invoice.xml` gives the account in `PaymentMeans/PayeeFinancialAccount`. The data looks copied from the seller's master data.
- Condition: the Order carries a party financial account only if the order itself uses it.
- Options: (a, preferred) remove the seller's `cac:FinancialAccount` from the order; (b) keep it only with payment terms in the order that use it.
- Needs decision: no

## Checked and consistent
- Line arithmetic: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `20000` × `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `0.08` = 1600.00 = `/Order/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `1600.00` = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `1600.00`.
- Tax: category `E` at 0 % with reason `RESALE` "Sale for resale or manufacture" fits garment bags that a garment maker passes on with its shirts (the shirts are sold "in a garment bag", `05-Order.xml`); both parties are registered for STT in Coastal State, so a domestic state sales tax applies; the order and the invoice agree.
- Currency XBL throughout.

## Considered and refuted
- `/Order/cac:DeliveryTerms/cbc:ID` = `DAP`: suspected a delivery cost that the order should price — refuted because under DAP the seller bears transport to the buyer's goods-in and includes it in the price; no separate charge is expected.
