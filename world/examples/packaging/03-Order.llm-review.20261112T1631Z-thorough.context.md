# LLM review: 03-Order.xml

Flow: packaging (PACKAGING-2026-01) · Review date: 2026-11-12 · Part: context

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

### packaging/03#F1 · Medium · `LocaleCode` holds a language code, not a locale
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:Language/cbc:LocaleCode` = `en`
- Why: `Language/LocaleCode` is "A code signifying the locale in which this language is used"; `en` (listID ISO 639) is the language that `Language/ID` already gives, not a locale (language in a region). Same value in 213 examples (`grep -rl --include='*.xml' '<cbc:LocaleCode listID="ISO 639">en<' world/examples | wc -l`).
- Condition: `LocaleCode` is absent or holds a locale from a list named in `listID`.
- Options: (a) preferred: remove it; (b) give a real locale with a locale list.
- Needs decision: no

### packaging/03#F2 · Low · Buyer's cost centre "Raw cotton" for a purchase of garment bags
- XPath: `/Order/cbc:AccountingCostCode` = `2200`
- XPath: `/Order/cbc:AccountingCost` = `Raw cotton`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Item/cbc:Name` = `Garment bag`
- Why: `AccountingCost` is "The buyer's accounting cost centre, applied to the Order as a whole". The only line orders 20000 polyethylene garment bags, packaging for the mill's shirts, yet the whole order is booked to the raw cotton cost centre. The pair 2200 / Raw cotton is the mill's constant: it is on every order and invoice where the mill buys (`cotton/08-Order.xml`, `cotton/16-Invoice.xml`, `cotton/17-Invoice.xml`, here and `04-Invoice.xml`; `grep -rl --include='*.xml' '<cbc:AccountingCost>Raw cotton<'`), so it looks copied from master data rather than chosen for this purchase.
- Condition: the cost centre of the order is one under which the mill books packaging material (or the order carries none).
- Options: (a) preferred: a packaging or consumables cost centre for this purchase, because the cost centre then fits the goods; (b) leave AccountingCost out of this order.
- Needs decision: no

### packaging/03#F3 · Low · Seller's bank account in an order that pays nothing
- XPath: `/Order/cac:SellerSupplierParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: The order has no payment means or terms; the seller's account with branch and bank address is not used by it (section 4.8). Among all Orders of the world only this one and `01-Order.xml` carry a seller `FinancialAccount` (XPath count over `world/examples/*/*.xml`). The account is used where it belongs in `04-Invoice.xml:/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XB96BLUM38020504712805`.
- Condition: the order carries no seller `FinancialAccount`, or a term that uses it.
- Options: (a) preferred: remove it.
- Needs decision: no

### packaging/03#F4 · Low · Buyer's contact: "Purchasing" in the Sales department
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Purchasing`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:JobTitle` = `Customer service officer`
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:Contact/cbc:Department` = `Sales`
- Why: Name, job title and department contradict each other: a purchasing contact is not a customer service officer in Sales. The name fits the buyer role, the title and department fit a seller. 89 examples have a contact named `Purchasing` or `Buying office` in Sales (XPath count over `world/examples/*/*.xml`).
- Condition: name, job title and department of the buyer's contact agree and describe a buying function.
- Options: (a) preferred: job title and department of purchasing (e.g. Buyer, Purchasing).
- Needs decision: no

## Checked and consistent
- Arithmetic: 20000 EA × 0.08 = 1600.00 = line and totals; tax 0.
- DAP with delivery to the buyer (`Delivery/DeliveryParty` = the mill) and delivery location "goods-in": consistent.
- Exemption "Sale for resale or manufacture" fits packaging bought by a manufacturer for the goods it sells (the shirts of `05-Order.xml` are sold "in a garment bag").
- HS 392321 and CPC 36410 both describe plastic sacks and bags.

## Considered and refuted
- `/Order/cac:OrderLine/cac:LineItem/cac:Item`: garment bag "of recycled polyethylene" without a CircularityProfile, unlike the film of `01-Order.xml` — refuted because absence is not a finding; the description states the material.
- `/Order/cac:Delivery/cac:DeliveryParty`: delivery party equal to the buyer — refuted because it names who receives the goods for the DAP delivery; it is not a filler.
