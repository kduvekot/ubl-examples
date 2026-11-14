# LLM review: 26-Order.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/26-Order.xml`, Git blob `6251abb7d11ec4be2651a2e8b809979afc7557fa` (committed)
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

### tender/26#F1 · Medium · The release orders 40 benches but not their installation, which the same release is then invoiced and penalised for
- XPath: `/Order/cbc:LineCountNumeric` = `1`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cbc:LineExtensionAmount` = `19960.00`
- XPath: `/Order/cac:AnticipatedMonetaryTotal/cbc:PayableAmount` = `19960.00`
- Why: the order is the first release under a contract with two lots, benches and their installation. It orders the benches only. The invoice of this order (`32-Invoice.xml:/Invoice/cac:OrderReference/cbc:ID` = `LPWD-PO-26-0212`) bills a second line of 40 installations (`32-Invoice.xml:/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `720.00`), and the buyer's debit note, which also refers to this order, charges a penalty for the late installation "of the release" (34-DebitNote.xml). Neither the order change (27) nor the order response (28) adds the installation; the agreed total stays 20160.00 while the invoice's lines come to 20680.00. So 720.00 lume are invoiced, withheld on, penalised and paid without an order. The notices' average release (`21-ContractAwardNotice.xml:/ContractAwardNotice/cac:ProcurementProject/cac:RequestedTenderTotal/cbc:AverageSubsequentContractAmount` = `20680.00`) is exactly benches plus installation, which suggests the release was meant to contain both.
- Condition: every line of 32-Invoice.xml that refers to this order corresponds to a line of the order (as changed and accepted), and the order's anticipated total equals the sum of those lines and charges.
- Options: (a, preferred) add an order line for 40 installations at 18 lume (720.00), raising the anticipated total to 20680.00 here and to 20880.00 in 27 and 28; (b) order the installation by a separate order in the flow and let the invoice's second line refer to it.
- Needs decision: yes

### tender/26#F2 · Medium · The pricing currency is the ferra, the price is stated in lume
- XPath: `/Order/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cbc:PriceAmount` = `499`
- Why: `PricingCurrencyCode` is "a code signifying the currency used for all prices in the Order". The only price in the order has `currencyID="XBL"`. Either the price is in lume, and then the pricing currency is not the ferra (and no pricing exchange rate is needed, the document currency being the lume too), or prices are in ferra, and then the price amount should be 49900 XUF (as in `25-Catalogue.xml:/Catalogue/cac:CatalogueLine[1]/cac:RequiredItemLocationQuantity/cac:Price/cbc:PriceAmount` = `49900`), with the pricing exchange rate turning it into the line amount in lume. The same pattern is in 32-Invoice.xml and 33-CreditNote.xml; 27 and 28 declare the pricing currency without any price.
- Condition: every `PriceAmount` of the order is in the currency named by `PricingCurrencyCode`; if that is the document currency, there is no `PricingCurrencyCode`/`PricingExchangeRate`.
- Options: (a) state the price as 49900 XUF and keep the pricing rate; (b) drop the pricing currency and rate and keep 499 XBL. Which one is right follows from the decision on the contract's price currency (25#F2 of this part); (b) is preferred if the contract is in lume, as tendered.
- Needs decision: no

### tender/26#F3 · Medium · The price's own exchange rate is the document's exchange rate, and its base rates say nothing
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/Order/cac:PricingExchangeRate/cbc:CalculationRate` = `0.01`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cac:PricingExchangeRate/cbc:SourceCurrencyBaseRate` = `1`
- XPath: `/Order/cac:OrderLine/cac:LineItem/cac:Price/cac:PricingExchangeRate/cbc:TargetCurrencyBaseRate` = `1`
- Why: `Price/PricingExchangeRate` is "the exchange rate applicable to this price, if it differs from the exchange rate applicable to the document as a whole". It does not differ: same currencies, same rate, same date as `/Order/cac:PricingExchangeRate`. The condition of the definition is not met. The two base rates are "in the case of a source [target] currency with denominations of small value, the unit base"; a base of 1 on both sides is the default and conveys nothing, and where a base would have a use (100 ferra to the lume) the rate is given as 0.01 instead.
- Condition: a `Price/PricingExchangeRate` is present only where its rate differs from the document's; base rates are present only with a value other than 1 that the calculation rate then refers to.
- Options: (a, preferred) remove the price-level exchange rate; (b) if the base rates are to be shown, use them properly on the document-level rate (source base 100, rate 1).
- Needs decision: no

### tender/26#F4 · Low · A forward contract concluded ten days before the procedure was announced fixes the pricing rate; the payment rate is a spot rate of the order date for a currency the order does not name
- XPath: `/Order/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate` = `2026-01-02`
- XPath: `/Order/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:ContractType` = `Forward purchase of ferra`
- XPath: `/Order/cac:PricingExchangeRate/cbc:Date` = `2026-01-02`
- XPath: `/Order/cac:PaymentExchangeRate/cbc:Date` = `2026-03-23`
- XPath: `/Order/cac:PaymentExchangeRate/cbc:CalculationRate` = `100`
- Why: three things do not fit together. (1) The forward contract BL-FX-26-0091 is a purchase of ferra, i.e. the hedge of whoever must pay in ferra (the buyer; the ID carries the prefix the flow uses for the Bank of Lumeport). It is dated 2 January 2026; the procedure was first announced on 12 January (01-PriorInformationNotice.xml) and awarded on 9 March, to one of two tenderers of whom the other is Bayvarran and would have been paid in lume. Nobody could know on 2 January that ferra would be needed, or how many. (2) A forward purchase fixes the rate at which a payment is converted; it is attached to the pricing rate, while `PaymentExchangeRate`, "the exchange rate between the document currency and the payment currency", carries a rate "established" on the order date, weeks before any payment, and the order names no payment currency. (3) The rate is exactly 100 (0.01) on 2 January, 23 March and on every later date of the flow (24, 25, 31 March, 5 May), so the forward contract hedges a rate that never moves. The contract is cited in six examples of this flow and in no other flow (counted with `grep -l 'BL-FX-26-0091' */*.xml` over `world/examples`).
- Condition: a foreign exchange contract cited in the order is dated on or after the day its need could be known and sits on the rate it actually fixes; a payment exchange rate is present only where the document names the payment currency and the rate applies to the payment.
- Options: (a, preferred) drop `PaymentExchangeRate` from the order, move the forward contract to the payment rate of the invoice, and date it after the award (e.g. on the contract date); (b) if the lume and the ferra are pegged at 100, say so once and remove the forward contract.
- Needs decision: yes

## Checked and consistent
- 40 × 499 = 19960.00 = line amount = `LineExtensionAmount` = `PayableAmount` of the anticipated total; tax subtotal taxable amount 19960.00, tax 0.00.
- Unit price 499 lume = winning tender (119760.00 / 240) = catalogue (49900 XUF × 0.01).
- Quantity 40 respects the tender's order terms (minimum 20, maximum 96, increment 4).
- Tax category G, 0 %, reason EXP (Urvanian list), scheme VAT: consistent with the catalogue and the invoice; the buyer's own exemption (PUBLIC, STT) is the party's status and is not applied to the amounts.
- Exchange rates are internally consistent: XUF → XBL × 0.01 and XBL → XUF × 100 are inverse.
- ISIN XU0001042501: check digit correct (`check_ids.py`).

## Considered and refuted
- `/Order/cbc:TaxCurrencyCode`: a Bayvarran buyer asking for tax amounts in ferra — refuted because the element is "the currency requested for tax amounts in Invoices related to this Order", the only tax involved is Urvanian VAT, and the invoice does give a tax total in XUF.
- `/Order/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:TaxExemptionReasonCode`: the buyer stating the seller's export exemption in its own order — refuted because the order follows the catalogue's applicable tax category and the anticipated total depends on it.
- `/Order/cac:TaxTotal/cbc:TaxAmount`: tax total in XBL although the tax currency is XUF — refuted because the tax currency of an order is a request for the invoice, not the currency of the order's own totals, and the amount is zero.
- `/Order/cac:DeliveryTerms/cbc:ID`: DAP and who bears duties — refuted for the money lens: under DAP the buyer clears the import, which is what 31-ImportCustomsDeclaration.xml shows (importer is the department).
