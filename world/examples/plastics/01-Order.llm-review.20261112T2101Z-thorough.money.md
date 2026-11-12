# LLM review: 01-Order.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/01-Order.xml`, Git blob `1c959f7204add325b43b103744bcf375fb8ba1db` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 2203360 2026-11-12 Review of the placeholder values in minimal/ (branch claude/elegant-franklin-kk2dky, commit 779ede3), run 20261112T1724Z-minimal
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

### plastics/01#F1 · Low · Buyer's bank account in an order that moves no money
- XPath: `/Order/cac:BuyerCustomerParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: `Party/FinancialAccount` is "the financial account associated with this party". An order carries no payment means, no mandate and no payment instruction; the buyer's own current account (held in `XBL`, while the order is priced in `XUF`) is used by nothing in this document. It is the account Rivermouth later pays from (`11-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` = `XB96BLUM38020504712805`), so it looks copied from the party's master data. The same account appears in the Rivermouth party of 14 XML examples (`grep -rl --include='*.xml' XB96BLUM38020504712805 world/examples`: 10 in plastics, 4 in packaging), while the seller Rinova, which receives the money, carries no party account in any of them.
- Condition: the Order carries a party financial account only if the order itself uses it (e.g. a prepayment or direct-debit arrangement stated in the order).
- Options: (a, preferred) drop the `FinancialAccount` from the buyer party in the order; (b) keep it only if the order gains a real payment arrangement that needs the buyer's account.
- Needs decision: no

## Checked and consistent
- Line arithmetic: `/Order/cac:OrderLine/cac:LineItem/cbc:Quantity` = `120` × `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `83200` (base quantity 1 t) = 9,984,000 = `/Order/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `9984000` = `/Order/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `9984000` = `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `9984000`.
- Tax: `/Order/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `9984000`, category `G` at 0 % with Urvanian exemption reason `EXP` (export outside Urvania); tax amount 0. Matches the invoice (`10-Invoice.xml:/Invoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `G`) and the exporter role of the seller in `05-ExportCustomsDeclaration.xml`.
- Delivery terms `CPT` (River quay, Lumeport): the seller pays the carriage, which agrees with the freight being bought and paid by Rinova (`04-TransportExecutionPlan.xml:/TransportExecutionPlan/cac:BillToParty/cac:PartyName/cbc:Name` = `Rinova Recovery`, `07-Invoice.xml` billed to Rinova) and with the note on the goods invoice that the price includes the barge.
- Price, quantity and currency agree with the goods invoice (`10-Invoice.xml:/Invoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `83200`, 120 t, `XUF`).
- IBAN-like check digit of the buyer account: OK (`check_ids.py`).

## Considered and refuted
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode` = `EXP`: an Urvanian exemption code in an order issued by a Bayvarran buyer — refuted because the tax in an order is the buyer's expectation of the seller's tax treatment; the seller is in Urvania and exports, so the Urvanian list is the right one.
- `/Order/cbc:DocumentCurrencyCode` = `XUF`: the buyer orders in the seller's currency — refuted; a legitimate commercial choice, and the invoice and remittance stay in `XUF`.
- Absence of payment terms in the order while the invoice imposes 30 days net, 2 % discount and 8 % penalty interest — refuted: the invoice points to the seller's published terms (`10-Invoice.xml:/Invoice/cac:PaymentTerms/cbc:PaymentTermsDetailsURI` = `https://www.rinova.example/terms`); nothing is implied by the order's silence.
