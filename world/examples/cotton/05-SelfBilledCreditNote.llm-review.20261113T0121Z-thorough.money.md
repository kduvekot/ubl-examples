# LLM review: 05-SelfBilledCreditNote.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/05-SelfBilledCreditNote.xml`, Git blob `ae986b70b136e1ac8647dd8051159b9d408be29a` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit eb215ba 2026-11-13 Reviews of the furniture flow, run 20261113T0047Z-thorough: merge complete
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

### cotton/05#F1 · High · Pricing currency Lume, but every price is in coral
- XPath: `/SelfBilledCreditNote/cbc:PricingCurrencyCode` = `XBL`
- XPath: `/SelfBilledCreditNote/cac:PricingExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/SelfBilledCreditNote/cac:CreditNoteLine/cac:Price/cbc:PriceAmount` = `0.03`
- Why: `PricingCurrencyCode` is "a code signifying the currency used for prices in the Self Billed
  Credit Note". The only price, the 0.03 per kg reduction for the downgraded cotton, is in XLC; no
  price of the credit note is in Lume, so the pricing currency and its exchange rate contradict the
  price they describe. The same contradiction is in the credited invoice 04
  (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cbc:PricingCurrencyCode` = `XBL`).
- Condition: either every price is in the currency `PricingCurrencyCode` names, with the pricing
  exchange rate converting it, or there is no pricing currency and no pricing exchange rate.
- Options: (a, preferred) drop `PricingCurrencyCode` and `PricingExchangeRate`, consistently with
  04; (b) state the price in Lume if the season agreement fixes it in Lume.
- Needs decision: yes (same question as for 04)

### cotton/05#F2 · Medium · Classing-fee allowance has no tax category, and the tax subtotal does not reflect it
- XPath: `/SelfBilledCreditNote/cac:AllowanceCharge/cbc:Amount` = `5.000`
- XPath: `/SelfBilledCreditNote/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `75.000`
- XPath: `/SelfBilledCreditNote/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `70.000`
- Why: the allowance reduces the tax-exclusive amount from 75.000 to 70.000, but carries no
  `TaxCategory`, so the credit note does not say how it is treated for tax; the only tax subtotal
  (category O) gives 75.000 as "the net amount to which the tax percent (rate) is applied". The
  subtotals add up to 75.000, not to the tax-exclusive 70.000. In the credited invoice 04 the
  document-level charge does carry category O
  (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:AllowanceCharge/cac:TaxCategory/cbc:ID` = `O`).
- Condition: the allowance has a tax category, and the subtotals' taxable amounts add up to
  `TaxExclusiveAmount`, each allowance counted in the subtotal of its category.
- Options: (a, preferred) give the allowance category O like the 04 charge and make the O
  subtotal's taxable amount 70.000; (b) if the fee is not part of the supply at all, move it out of
  the tax-exclusive amount (see F3 on what the fee is).
- Needs decision: no

### cotton/05#F3 · Low · Who bears the classing fee is unclear from the allowance's direction
- XPath: `/SelfBilledCreditNote/cac:AllowanceCharge/cbc:ChargeIndicator` = `false`
- XPath: `/SelfBilledCreditNote/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Classing fee`
- XPath: `/SelfBilledCreditNote/cac:DiscrepancyResponse/cbc:Description` = `2,500 kg classed Strict Low Middling instead of Middling.`
- Why: in a credit note an allowance reduces the amount credited. Here the ginnery credits itself
  75.000 for the downgraded cotton and then reduces that credit by a 5.000 "classing fee", i.e. the
  ginnery bears the fee in the farm's favour. A classing fee is normally a cost of the party that
  has the cotton classed; if the farm is to bear it (as the party whose cotton was downgraded), it
  would increase the credit, not reduce it. The credit note gives no text that explains which is
  meant, and the reason code `64` ("special agreement") does not say either.
- Condition: the direction of the classing-fee amount matches the party that bears the fee, and
  the credit note says (in the reason text or a note) who that is.
- Options: (a, preferred) state in `AllowanceChargeReason` that the ginnery refunds the farm's
  classing fee if that is the story; (b) if the farm bears the fee, make it a charge (ChargeIndicator
  true), credit 80.000 instead of 70.000 and adjust 06.
- Needs decision: yes

### cotton/05#F4 · Low · Withholding tax reversed without basis or rate
- XPath: `/SelfBilledCreditNote/cac:WithholdingTaxTotal/cbc:TaxAmount` = `1.500`
- Why: the withholding in 04 is tiered (1 % up to 2 000, 2 % above) and states its subtotals; here
  only 1.500 is given. It is 2 % of 75.000, which is correct because the credited value falls
  entirely in the upper tier (61.360 on 4 068.000 before, 59.860 on 3 993.000 after), but the
  credit note does not let the farm see that: no subtotal, taxable amount, rate or tax scheme
  (`Presumptive tax on farm produce`) is given, so the tax the 1.500 belongs to is not even named.
- Condition: the withholding tax total names its tax scheme and gives the taxable amount and rate
  from which 1.500 follows.
- Options: (a, preferred) add one subtotal (taxable 75.000, 2 %, the OTH presumptive-tax scheme as
  in 04); (b) leave it as a bare total, accepting that the scheme is only implied.
- Needs decision: no

### cotton/05#F5 · Low · Tax representative in a domestic credit without sales tax
- XPath: `/SelfBilledCreditNote/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- Why: as in 04: both parties are established in Lisavu, the supply is outside the scope of tax,
  and the withholding tax is the ginnery's own; nothing in the credit note needs a party "authorized
  to act as the Tax Representative".
- Condition: a tax representative is named only with a reason visible in the document.
- Options: (a, preferred) drop it, consistently with 04.
- Needs decision: yes

### cotton/05#F6 · Low · Tax and payment currency repeat the document currency, with identity exchange rates
- XPath: `/SelfBilledCreditNote/cbc:TaxCurrencyCode` = `XLC`
- XPath: `/SelfBilledCreditNote/cac:TaxExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/SelfBilledCreditNote/cbc:PaymentCurrencyCode` = `XLC`
- XPath: `/SelfBilledCreditNote/cac:PaymentExchangeRate/cbc:CalculationRate` = `1`
- Why: XLC to XLC at 1; nothing is converted, and the credit is not even paid but set off
  (payment means 97). No business reason (rule "no fillers").
- Condition: tax or payment currency and rate only where they differ from the document currency.
- Options: (a, preferred) drop the four elements.
- Needs decision: no

### cotton/05#F7 · Low · Alternative payment currency for a credit that is set off
- XPath: `/SelfBilledCreditNote/cbc:PaymentAlternativeCurrencyCode` = `XBL`
- XPath: `/SelfBilledCreditNote/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `2.5`
- XPath: `/SelfBilledCreditNote/cac:PaymentMeans/cbc:PaymentMeansCode` = `97`
- Why: the credit is "set off against the payment of the self-billed invoice" (clearing between
  partners), and 06 nets it in coral. No payment in Lume can take place, and no payable
  alternative amount is given.
- Condition: no alternative payment currency unless a payment in it can occur under this document.
- Options: (a, preferred) drop both elements.
- Needs decision: no

## Checked and consistent
- Line: 2 500 kg × 0.03 per 1 kg = 75.000; less the 5.000 allowance = 70.000 tax-exclusive = tax-inclusive (tax 0.000); `AllowanceTotalAmount` 5.000.
- Withholding reversal: 04 withheld 20.000 + 41.360 = 61.360 on 4 068.000; on 4 068.000 − 75.000 = 3 993.000 it would be 20.000 + 39.860 = 59.860; difference 1.500, as stated.
- Levy reversal: `/SelfBilledCreditNote/cac:CollectionCreditNoteLine/cbc:LineExtensionAmount` = `0.750`, 1 % of 75.000, as the 40.680 in 04 is 1 % of 4 068.000.
- Payable: 70.000 − 1.500 + 0.750 = 69.250 = `/SelfBilledCreditNote/cac:LegalMonetaryTotal/cbc:PayableAmount` = `69.250` (the farm gets back the withheld tax on the credited value and is relieved of its levy); 06 nets exactly this: `06-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[2]/cbc:CreditLineAmount` = `69.250`.
- Set-off: payment means 97 and the terms note agree with 06, which remits 3 210.320 − 69.250 = 3 141.070 on 2026-02-16, the credit note's `DueDate`.
- Billing reference: SCG-SBI-26-0194 with issue date 2026-02-07 is 04.
- Tax treatment O "No general sales tax" and supply type GOODS as in 04.
- Exchange rates 0.4 and 2.5 are inverse and the same as in 04.

## Considered and refuted
- `/SelfBilledCreditNote/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `64`: a code from the allowance reason list (5189) was checked against its element — refuted as a problem because 5189 is the list for allowance reasons, which matches ChargeIndicator false, and 64 is "special agreement".
- `/SelfBilledCreditNote/cac:PaymentMeans/cbc:PaymentMeansCode` = `97`: clearing between partners suspected of contradicting the credit transfer in 06 — refuted because the credit itself is not transferred but deducted from the transfer that pays 04, which is exactly what 06 shows.
