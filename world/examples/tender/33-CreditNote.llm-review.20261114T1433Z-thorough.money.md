# LLM review: 33-CreditNote.xml

Flow: tender (TENDER-2026-01) · Review date: 2026-11-14 · Part: money

## Reviewed version
- Run: `20261114T1433Z-thorough`
- Example: `world/examples/tender/33-CreditNote.xml`, Git blob `fedb04ee2964c2e08e60565d54f4c570247bdfda` (committed)
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

### tender/33#F1 · High · The credit is to be set off against the next release's invoice (line), against the next payment (document), and is in fact set off against this release's invoice
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:PaymentTerms/cbc:Note` = `Set off against the next release's invoice.`
- XPath: `/CreditNote/cac:PaymentTerms/cbc:Note` = `Settled against the next payment to the seller, unless refunded.`
- XPath: `/CreditNote/cac:BillingReference/cac:InvoiceDocumentReference/cbc:ID` = `VI-INV-26-0221`
- Why: the two payment terms of the credit note name different settlements. On 4 April the next payment to the seller is that of the first release's invoice, which is unpaid and due on 30 April; the next release's invoice does not exist in the flow. The documents that follow settle the credit against the first release's invoice: `35-Reminder.xml:/Reminder/cac:ReminderLine[2]/cbc:CreditLineAmount` = `515.20` reduces the balance of invoice VI-INV-26-0221, and the remittance advice pays that invoice less the credit (`36-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:CreditLineAmount` = `515.20`). The line's term is therefore contradicted by the document's own term and by what both parties then do.
- Condition: the credit note states one way of settlement, and it is the one the reminder and the remittance advice apply (deduction from the payment of invoice VI-INV-26-0221).
- Options: (a, preferred) remove the line-level payment terms and word the document-level note as "Deducted from the payment of invoice VI-INV-26-0221."; (b) keep "next release's invoice" and take the credit out of the reminder and the remittance advice, which changes their amounts.
- Needs decision: no

### tender/33#F2 · Medium · The pricing currency is the ferra, both prices are stated in lume
- XPath: `/CreditNote/cbc:PricingCurrencyCode` = `XUF`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:Price/cbc:PriceAmount` = `499`
- XPath: `/CreditNote/cac:CreditNoteLine[2]/cac:Price/cbc:PriceAmount` = `18`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:PricingReference/cac:AlternativeConditionPrice/cbc:PriceAmount` = `49900`
- Why: `PricingCurrencyCode` is "a code signifying the currency used for prices in the Credit Note"; both `Price/PriceAmount`s carry `currencyID="XBL"`. On line 1 the price in the declared pricing currency (49900 ferra) is present, but as `AlternativeConditionPrice`, "the price expressed in terms other than the actual price", so the document treats the lume price as the actual one and the ferra price as the alternative, the reverse of what the pricing currency says. Line 2 has no ferra price at all. As in 26#F2 and 32#F4 of this part.
- Condition: every `Price/PriceAmount` is in the currency named by `PricingCurrencyCode`; a price in another currency, if shown, is the alternative; both lines are treated alike.
- Options: (a) `Price` 49900 and 1800 XUF, and the lume price as the alternative or not at all; (b) drop the pricing currency, its rate and the alternative price. The choice follows the decision on the contract's price currency (25#F2); (b) is preferred if the contract is in lume.
- Needs decision: no

### tender/33#F3 · Medium · An invoice period on a credit note that corrects one specific invoice
- XPath: `/CreditNote/cac:InvoicePeriod/cbc:StartDate` = `2026-03-31`
- XPath: `/CreditNote/cac:InvoicePeriod/cbc:EndDate` = `2026-04-04`
- Why: `InvoicePeriod` "associates the Credit Note with Invoicing Periods rather than with a specific Invoice". This credit note is associated with a specific invoice (`BillingReference`, VI-INV-26-0221) and credits one bench of it; it does not credit a billing period. The period given, from the invoice's date to the credit note's date, is not a period that anything was billed for.
- Condition: a document-level `InvoicePeriod` is present only on a credit note that credits a period instead of an invoice.
- Options: (a, preferred) remove the document-level invoice period; (b) none seen.
- Needs decision: no

### tender/33#F4 · Low · The sub-line of 180.00 lume does not detail the 499.00 of its line
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cac:SubCreditNoteLine/cbc:LineExtensionAmount` = `180.00`
- XPath: `/CreditNote/cac:CreditNoteLine[1]/cbc:LineExtensionAmount` = `499.00`
- Why: `SubCreditNoteLine` is "a class defining one or more Credit Note Lines detailing the credit note line". The line credits a whole bench at 499.00; its only sub-line, "Side frames of the bench", carries 180.00. The remaining 319.00 is not detailed, the sub-line has no quantity or price, and nothing says what the 180.00 is (the value of the damaged part, a cost of repair, the part of the credit that relates to the frames). No other document of the flow uses the figure.
- Condition: the sub-lines of a line add up to the line's amount, or the sub-line states what its amount is and how it relates to the line.
- Options: (a, preferred) remove the sub-line, the whole bench being credited; (b) detail the line completely (frames, slats, anchors) so that the sub-lines sum to 499.00.
- Needs decision: no

### tender/33#F5 · Low · Tax and payment currency are the ferra, but the credit note has no ferra amounts and no payment
- XPath: `/CreditNote/cbc:TaxCurrencyCode` = `XUF`
- XPath: `/CreditNote/cac:TaxTotal/cbc:TaxAmount` = `0.00`
- XPath: `/CreditNote/cbc:PaymentCurrencyCode` = `XUF`
- XPath: `/CreditNote/cac:PaymentExchangeRate/cbc:Date` = `2026-04-04`
- XPath: `/CreditNote/cac:PricingExchangeRate/cac:ForeignExchangeContract/cbc:IssueDate` = `2026-01-02`
- Why: `TaxCurrencyCode` is "the currency used for tax amounts in the Credit Note"; the only tax total is in lume, whereas the invoice it corrects has a second tax total in ferra, which this credit should reduce (by 49900 ferra under G and 1800 under O). `PaymentCurrencyCode` and a payment exchange rate of the credit note's date are given for a credit that, by its own terms, is not paid but deducted. The forward contract dated before the procedure is cited again (see 26#F4 and 32#F7 of this part).
- Condition: a tax total in the tax currency mirrors the one in lume, as on the invoice, or there is no tax currency; payment currency and payment rate are present only if the credit is to be paid out.
- Options: (a, preferred) add the tax total in XUF with the two subtotals, and remove `PaymentCurrencyCode` and `PaymentExchangeRate`; (b) remove all three currency codes and rates if the decision on 25#F2 makes the lume the only currency.
- Needs decision: no

### tender/33#F6 · Low · The withholding tax reversed has no subtotal, category or scheme
- XPath: `/CreditNote/cac:WithholdingTaxTotal/cbc:TaxAmount` = `1.80`
- XPath: `/CreditNote/cac:CreditNoteLine[2]/cac:WithholdingTaxTotal/cbc:TaxAmount` = `1.80`
- Why: on the invoice the withholding is specified (taxable 720.00, 10 %, "Withholding tax on services of non-residents"). The credit note reverses 1.80 of it with a bare amount: neither base (18.00) nor rate nor the name of the tax is given, so the document alone does not show which tax is reduced or how 1.80 is derived.
- Condition: the credit note's withholding tax total has a subtotal with taxable amount, rate and the same scheme as the invoice's.
- Options: (a, preferred) add the subtotal (18.00, 10 %, same category and scheme as 32); (b) none seen.
- Needs decision: no

### tender/33#F7 · Low · A tax representative in Bayvarra, and no Bayvarran tax of the seller on the credit note
- XPath: `/CreditNote/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Bayforth Forwarding`
- Why: as 32#F8 of this part: `TaxRepresentativeParty` is "the Party authorized to act as the Tax Representative for this Credit Note"; the credit note carries Urvanian VAT at 0 % and the reversal of a tax the customer withholds, nothing the seller owes in Bayvarra.
- Condition: as 32#F8.
- Options: as 32#F8; decided together.
- Needs decision: yes

## Checked and consistent
- 499.00 + 18.00 = 517.00 = line extension = tax-exclusive = tax-inclusive amount; withholding 10 % of 18.00 = 1.80; 517.00 − 1.80 = 515.20 = `PayableAmount`, the amount the reminder and the remittance advice deduct.
- Prices equal the invoice's (499 and 18 lume); one bench and its installation; tax subtotals G 499.00 and O 18.00 with the invoice's categories and reasons; 49900 ferra × 0.01 = 499 lume.
- The withholding of the three documents nets to the amount the buyer paid to the tax office: 72.00 − 1.80 − 0.72 = 69.48 (`35-Reminder.xml:/Reminder/cac:PrepaidPayment/cbc:PaidAmount` = `69.48`).
- Credit note type 381; billing reference to the invoice that exists; all amounts in XBL except the alternative price.
- ISIN XU0001042501: check digit correct (`check_ids.py`).

## Considered and refuted
- `/CreditNote/cac:LegalMonetaryTotal/cbc:LineExtensionAmount`: the credited bench was a moss-green one, and its share of the colour charge (200.00 / 40 = 5.00) is not credited — refuted because the charge is a single amount for the release (quoted and accepted as such in 27 and 28), not a price per bench, so it is not reduced by one bench.
- `/CreditNote/cac:CreditNoteLine[2]/cbc:LineExtensionAmount`: crediting the installation of a bench that was damaged — refuted: a bench that is not usable is not installed, so the 18.00 billed in advance for it is rightly credited.
- `/CreditNote/cac:CreditNoteLine[1]/cac:PricingReference/cac:AlternativeConditionPrice/cbc:PriceAmount`: no base quantity or price type — refuted as a separate finding; its role is covered by F2.
