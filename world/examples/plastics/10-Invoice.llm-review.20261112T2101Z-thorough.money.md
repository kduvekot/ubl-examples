# LLM review: 10-Invoice.xml

Flow: plastics (PLASTICS-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2101Z-thorough`
- Example: `world/examples/plastics/10-Invoice.xml`, Git blob `1e3f9e5ae5dac5d74b0e7b9130b9a13721e9ec83` (committed)
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

### plastics/10#F1 · Low · Debtor's bank account in a credit-transfer invoice
- XPath: `/Invoice/cac:AccountingCustomerParty/cac:Party/cac:FinancialAccount/cbc:ID` = `XB96BLUM38020504712805`
- Why: `Party/FinancialAccount` is "the financial account associated with this party". The invoice asks for a credit transfer (`/Invoice/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`) to the seller's account; the customer's own account plays no part in it (it would only matter for a direct debit, which needs a mandate and `PaymentMeans/PaymentMandate/PayerFinancialAccount`). The account is the one Rivermouth later pays from (`11-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:ID` = `XB96BLUM38020504712805`), but the invoice does nothing with it; it is copied master data. The same account appears in the Rivermouth party of 14 XML examples (`grep -rl --include='*.xml' XB96BLUM38020504712805 world/examples`).
- Condition: the customer party in the invoice carries no financial account unless the invoice uses it.
- Options: (a, preferred) drop it.
- Needs decision: no

## Checked and consistent
- Line and totals: 120 t × 83,200 `XUF` (base 1 t) = 9,984,000 = `/Invoice/cac:InvoiceLine/cbc:LineExtensionAmount` = `9984000` = `/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `9984000` = `/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `9984000` = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `9984000`; same price, quantity and currency as `01-Order.xml`.
- Tax: category `G`, 0 %, exemption `EXP` (export outside Urvania) in the subtotal and on the line, supply type `GOODS`; taxable 9,984,000, tax 0. Export is evidenced by `05-ExportCustomsDeclaration.xml` (exporter = seller) and the exportation event on 2026-04-20 in `06-Waybill.xml`.
- Tax point `/Invoice/cbc:TaxPointDate` = `2026-04-20` equals the day of exportation (`06-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:MainCarriageShipmentStage/cac:ExportationTransportEvent/cbc:OccurrenceDate` = `2026-04-20`).
- Terms: due 2026-05-20 = issue + 30 days in `DueDate`, `PaymentMeans/PaymentDueDate` and `PaymentTerms/PaymentDueDate`; discount 2 % × 9,984,000 = 199,680 = `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `199680`; settlement period 2026-04-20 to 2026-04-30 = 10 days, as the note says; penalty interest 8 % per year, simple.
- What follows: the remittance advice pays 9,984,000 on 2026-05-19 (`11-RemittanceAdvice.xml:/RemittanceAdvice/cbc:TotalPaymentAmount` = `9984000`), after the discount period and before the due date, so neither discount nor penalty interest applies; the payment reference and payee account there equal `/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF89RRINV260894` and `/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XU700351041620000000418916`.
- `CPT` (note: the price includes the barge) agrees with the order's delivery terms and with the freight being billed to Rinova in `07-Invoice.xml`.
- RF reference and IBAN-like check digits OK (`check_ids.py`).

## Considered and refuted
- Payer's account in `XBL` (`/Invoice/cac:AccountingCustomerParty/cac:Party/cac:FinancialAccount/cbc:CurrencyCode` = `XBL`) against payment currency `/Invoice/cbc:PaymentCurrencyCode` = `XUF` — refuted: paying a foreign-currency amount from a home-currency account is ordinary; the bank converts.
- Charge bearer `SHAR` while the remittance reports the full amount — refuted: with shared charges the payer sends the full amount and bears its own bank's fees; the remittance advice reports what was sent.
