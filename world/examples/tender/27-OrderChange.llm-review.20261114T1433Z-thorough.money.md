# LLM review: 27-OrderChange.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/27-OrderChange.xml`, Git blob `e43fb0041dc6f797ab80a2e9f8efb406a7c4464c` (committed)
- Last commit changing the example: 8b83ce5 2026-11-13 Reviews of the contest flow, run 20261112T2358Z-thorough: parts written so far
- Checkout: branch `claude/stoic-noether-5pboei`, commit 4caf0b6 2026-11-14 Build: keep and skip the review files; document the required programs
- Skill: `.claude/skills/ubl-example-review`, last commit 0c94386 2026-11-14 Review skill: document how the thorough runs were done; save status and merge decisions (committed)
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

### tender/27#F1 · High · The payment term "as the contract says" is not what the contract says
- XPath: `/OrderChange/cac:PaymentTerms/cbc:Note` = `30 days after the invoice, as the contract says.`
- XPath: `/OrderChange/cac:TransactionConditions/cbc:Description` = `The framework contract's conditions apply.`
- Why: the note cites the contract for its term. The contract's payment term is `24-TenderContract.xml:/TenderContract/cac:TenderingTerms/cac:PaymentTerms/cbc:Note` = `30 days after each accepted release.` (the same wording in 01–03). Thirty days from the invoice and thirty days from the acceptance of the release are different due dates: the invoice of this release is dated 31 March, one day after the despatch advice and before any acceptance of the installed benches is recorded in the flow (the installation was late, 34-DebitNote.xml). The order change thus misquotes the document it relies on, while its transaction conditions say that the contract's conditions apply.
- Condition: a payment term that an order document attributes to the contract is the contract's term (same starting event, same number of days), or the order change carries no payment terms and leaves them to the contract.
- Options: (a, preferred) remove `PaymentTerms` from the order change: a change of colour does not change the terms, and `TransactionConditions` already points to the contract; (b) repeat the contract's wording; (c) if "after the invoice" is what the story wants, change the contract and the notices.
- Needs decision: no

### tender/27#F2 · Medium · The anticipated total is the new total of the order, not the amount of the change
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:LineExtensionAmount` = `19960.00`
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:ChargeTotalAmount` = `200.00`
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `20160.00`
- Why: in an order change `AnticipatedMonetaryTotal` is "the amount of change to the total cost of the order anticipated by the buyer". The change is the colour charge: 20160.00 − 19960.00 (`26-Order.xml:/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `19960.00`) = 200.00. The element carries the whole new total instead, so by its definition the order would become 20160.00 dearer. Stating the full new total is common practice for order changes that replace the order; under the rule of semantic conformance that does not change what the element means in UBL 2.5.
- Condition: the amounts of `AnticipatedMonetaryTotal` equal the difference between the changed order and the order it changes (here a payable amount of 200.00, charge total 200.00, no change in line extension).
- Options: (a, preferred) payable amount 200.00 with charge total 200.00 and no line extension amount (or 0.00); (b) keep the full total and record the difference between definition and practice as a finding for the UBL TC, if the owner prefers the practice.
- Needs decision: yes

### tender/27#F3 · Medium · The changed order still contains no installation, which the release's invoice bills
- XPath: `/OrderChange/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `20160.00`
- Why: with this change the buyer's order stands at 40 benches plus the colour charge. The invoice of the order bills 20880.00 before withholding (`32-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `20880.00`): the difference is the installation of the 40 benches (`32-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `720.00`), which neither the order nor this change orders. See 26#F1 of this part; it is a finding here because this document states the buyer's latest anticipated cost of the release.
- Condition: the order as changed contains every line the invoice of the release bills, and its anticipated cost equals the invoice's amount before withholding.
- Options: as 26#F1: (a, preferred) order the installation in the order (then nothing changes here if F2's option (a) is taken); (b) a separate order.
- Needs decision: yes

### tender/27#F4 · Low · Pricing and tax currency and three exchange rates in a document with no price, no tax amount and no payment currency
- XPath: `/OrderChange/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/OrderChange/cbc:TaxCurrencyCode` = `XUF`
- XPath: `/OrderChange/cac:TaxExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/OrderChange/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/OrderChange/cac:PaymentExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/OrderChange/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate` = `2026-01-02`
- Why: `PricingCurrencyCode` is "the currency that is used for all prices in the Order Change", and the three rates are the rates between the document currency and the pricing, tax and payment currency. The order change contains no price (its line has quantity and amount only), no tax total and names no payment currency; every amount in it is in lume. Nothing in the document is converted by any of the three rates. The tax and payment rates are dated 24 March, the day of the change, although they would apply to an invoice and a payment weeks later. The forward contract dated before the procedure is discussed in 26#F4 of this part.
- Condition: a currency code and its exchange rate are present only if the document contains an amount in, or a conversion into, that currency.
- Options: (a, preferred) remove `PricingCurrencyCode`, `TaxCurrencyCode` and the three exchange rates from the order change; (b) keep `TaxCurrencyCode` as the request for the invoice and remove the rest.
- Needs decision: no

### tender/27#F5 · Low · The seller's bank account appears in the buyer's change of colour, not in the order
- XPath: `/OrderChange/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- XPath: `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XU790351041600000000209458`
- Why: `PaymentMeans` in an order change is the "expected means of payment". The order it changes has none, and the change is about the colour of the benches; nothing about the payment changes. The account is the seller's, stated by the buyer, six days before the seller's own invoice gives it with reference and channel. It reads as master data added to this document rather than something the change needs.
- Condition: the order change carries payment means only if it changes them or the order had them.
- Options: (a, preferred) remove `PaymentMeans` from the order change; (b) put the expected payment means in the order and leave the change without.
- Needs decision: no

## Checked and consistent
- 19960.00 + 200.00 = 20160.00; the line (40 EA, 19960.00) is unchanged against the order; the charge total equals the one charge.
- The charge: reason code CAT ("Special colour service: providing a colour which is different from the default colour") fits the request for moss green instead of the grey of the order; 200.00 is 5 lume a bench. The same charge, code and amount are accepted in 28-OrderResponse.xml and billed in 32-Invoice.xml.
- `RequestedInvoiceCurrencyCode` XBL: the invoice's document currency is XBL.
- Payee account XU79 0351 0416 0000 0000 2094 58: check digits correct (`check_ids.py`); the same account, holder, branch and bank as in 32, 35 and 36.
- ISIN XU0001042501: check digit correct.

## Considered and refuted
- `/OrderChange/cac:AllowanceCharge/cbc:Amount`: the charge has no tax category although the invoice puts it under category G — refuted because the order change has no tax total at all and the category follows from the goods the charge belongs to.
- `/OrderChange/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode`: a UN/EDIFACT 7161 code in a document-level charge without `BaseAmount` or factor — refuted: a fixed charge needs neither.
- `/OrderChange/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode`: a ferra account for an order in lume — refuted because the invoice's payment currency is the ferra; the account's currency agrees with that.
