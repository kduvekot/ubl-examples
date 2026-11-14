# LLM review: 28-OrderResponse.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/28-OrderResponse.xml`, Git blob `3ed78b3450611e60a961e71c98db29842ff2963f` (committed)
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

### tender/28#F1 · Medium · The accepted total of the release does not contain the installation that the invoice of the same order bills
- XPath: `/OrderResponse/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `19960.00`
- XPath: `/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount` = `20160.00`
- Why: `LegalMonetaryTotal` is "the total amount of the Order (or counter-offer)". The seller accepts the order as changed at 20160.00 lume: 40 benches and the colour charge. Six days later the same seller invoices the same order with a second line for the installation of the 40 benches (`32-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `720.00`), for a total of `32-Invoice.xml:/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `20880.00`. The two totals of the same release, both stated by the seller, differ by 720.00 lume, and no document of the flow orders or accepts the installation. See 26#F1 of this part.
- Condition: the total the seller accepts equals the total it invoices for the order before withholding, line by line.
- Options: (a, preferred) once the installation is ordered (26#F1), accept 20880.00 here; (b) a separate order and response for the installation.
- Needs decision: yes

### tender/28#F2 · Low · Pricing and tax currency and three exchange rates in a response that has no price, no tax amount and no payment currency
- XPath: `/OrderResponse/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/OrderResponse/cbc:TaxCurrencyCode` = `XUF`
- XPath: `/OrderResponse/cac:TaxExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/OrderResponse/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/OrderResponse/cac:PaymentExchangeRate/cbc:CalculationRate` = `100`
- XPath: `/OrderResponse/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate` = `2026-01-02`
- Why: `PricingCurrencyCode` is "the currency that is used for all prices in the Order Response" and `TaxCurrencyCode` "the currency that is used for all tax amounts in the Order Response". The response has no order line, no price and no tax amount; its three amounts are in lume. None of the three exchange rates converts anything in the document, and it names no payment currency. The forward contract is, moreover, the buyer's purchase of ferra (see 26#F4 of this part), cited here by the seller as the source of its pricing rate.
- Condition: a currency code and its exchange rate are present only if the document contains an amount in, or a conversion into, that currency.
- Options: (a, preferred) remove the two currency codes and the three exchange rates; (b) keep only what a decision on the contract's price currency (25#F2) requires.
- Needs decision: no

## Checked and consistent
- 19960.00 + 200.00 = 20160.00 = the buyer's anticipated total in 27-OrderChange.xml; the charge (code CAT, "Special colour", 200.00) is identical in 27, 28 and 32.
- The note "Accepted: moss green, at the quoted charge." agrees with the response code AP (Accepted) and with the charge.
- All amounts in XBL, the document currency.
- ISIN XU0001042501: check digit correct (`check_ids.py`).

## Considered and refuted
- `/OrderResponse/cac:AllowanceCharge/cbc:Amount`: no tax category on the charge — refuted as in the order change: the response has no tax totals, and the category follows from the goods.
- `/OrderResponse/cac:LegalMonetaryTotal/cbc:PayableAmount`: no payment terms or due date in the response — refuted because the terms are the contract's and the response accepts without change.
