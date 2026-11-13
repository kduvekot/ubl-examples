# LLM review: 04-SelfBilledInvoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: money

## Reviewed version
- Run: `20261113T0121Z-thorough`
- Example: `world/examples/cotton/04-SelfBilledInvoice.xml`, Git blob `7ff28661ff5e42f702b07e4477e9454c7a6c7ebb` (committed)
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

### cotton/04#F1 · High · Tax subtotal leaves out the haulage charge of the same tax category
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `4068.000`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cac:TaxCategory/cbc:ID` = `O`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:Amount` = `180.000`
- XPath: `/SelfBilledInvoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `4248.000`
- Why: the document-level charge of 180.000 is placed in tax category O and is part of the
  tax-exclusive amount (4 068.000 + 180.000 = 4 248.000). The only tax subtotal, also category O,
  gives as its `TaxableAmount` ("the net amount to which the tax percent (rate) is applied")
  only the line amount, 4 068.000. The subtotals therefore do not add up to the tax-exclusive
  amount, and the charge belongs to a category whose subtotal does not contain it. The rate is 0,
  so no tax amount changes, but the arithmetic between the subtotal and the totals does not hold.
- Condition: the sum of the `TaxableAmount`s of the `TaxTotal` subtotals equals
  `TaxExclusiveAmount`, and every line and document-level allowance or charge is counted in the
  subtotal of its own tax category.
- Options: (a, preferred) make the O subtotal's taxable amount 4 248.000, as the charge's own tax
  category says; (b) if the haulage payment is not a supply at all, take it out of the
  tax-exclusive amount and say how it is settled, which changes the story (see F4).
- Needs decision: no

### cotton/04#F2 · High · Pricing currency Lume, but every price is in coral
- XPath: `/SelfBilledInvoice/cbc:PricingCurrencyCode` = `XBL`
- XPath: `/SelfBilledInvoice/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/SelfBilledInvoice/cac:PricingExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `0.226`
- Why: `PricingCurrencyCode` is "a code signifying the currency used for prices in the Invoice",
  and `PricingExchangeRate` "the exchange rate between the document currency and the pricing
  currency". The only price of the invoice is stated in XLC (`currencyID="XLC"`), as is the
  per-unit haulage amount, so no price of this invoice is in Lume; nor does the invoice say what
  the Lume price would be (0.226 / 0.4 = 0.565 XBL/kg, a figure that appears nowhere). The prepayment
  invoice 01 at the same price carries no pricing currency at all. The header therefore contradicts
  the prices it describes. The same pair occurs in 05.
- Condition: either every price of the invoice is in the currency `PricingCurrencyCode` names, with
  the pricing exchange rate converting it to the document currency, or the invoice carries no
  pricing currency and no pricing exchange rate.
- Options: (a, preferred) drop `PricingCurrencyCode` and `PricingExchangeRate`: the farm's price is
  a coral price in 01, 04 and 05; (b) if the season agreement really fixes the price in Lume, state
  the line price in XBL and keep the rate, which changes how 01 and 05 state the price too.
- Needs decision: yes (whether the season price is a Lume price is a question of the story)

### cotton/04#F3 · Medium · Base amount of the haulage charge is not the basis it is calculated from
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:BaseAmount` = `4068.000`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:PerUnitAmount` = `0.010`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:Amount` = `180.000`
- Why: `BaseAmount` is "the monetary amount to which the multiplier factor is applied in
  calculating the amount of this allowance or charge". There is no `MultiplierFactorNumeric`, and
  the charge is not a share of 4 068.000 (180 / 4 068 = 4.42 %, no agreed rate); it is calculated
  per kilogram: 0.010 × 18 000 kg = 180.000, as `PerUnitAmount` ("the allowance or charge per
  item; the total … is calculated by multiplying the per unit amount by the quantity") says. The
  base amount suggests a percentage calculation that did not take place.
- Condition: the charge carries a `BaseAmount` only together with a multiplier factor that yields
  its amount from it; a per-kilogram charge is described by its per-unit amount alone.
- Options: (a, preferred) drop `BaseAmount`; (b) replace the per-unit basis by a percentage of the
  line amount, which changes the agreed haulage rate.
- Needs decision: no

### cotton/04#F4 · Low · Buyer pays haulage on top of a DAP delivery
- XPath: `/SelfBilledInvoice/cac:DeliveryTerms/cbc:ID` = `DAP`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:AllowanceChargeReasonCode` = `CAB`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Haulage allowance`
- XPath: `05-SelfBilledCreditNote.xml:/SelfBilledCreditNote/cac:DeliveryTerms/cbc:ID` = `DAP`
- Why: under Incoterms DAP (own knowledge of Incoterms 2020) the seller delivers at the named
  place and bears the cost of carriage to it; the delivery place is the ginnery's weighbridge. The
  ginnery nevertheless pays the farm a cartage charge of 0.010 per kilogram on top of the price.
  That is possible as a separate agreement (a haulage allowance to growers), but then DAP no longer
  describes who bears the carriage cost; with a delivered price the charge would not exist. One
  of the two statements does not fit the other.
- Condition: the delivery terms and the haulage payment give the same answer to who bears the cost
  of carrying the seed cotton to the gin.
- Options: (a, preferred) keep the haulage allowance and use a term under which the buyer bears
  the carriage, or no Incoterm with a description of the arrangement in `DeliveryTerms`; (b) keep
  DAP and drop the charge (and with it the 180.000 in the totals and in 06).
- Needs decision: yes

### cotton/04#F5 · Low · Tax representative in a domestic sale without sales tax
- XPath: `/SelfBilledInvoice/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: the tax representative is "the Party authorized to act as the Tax Representative for this
  Self Billed Invoice". Both trading parties are established in Lisavu, the supply is outside the
  scope of tax (there is no general sales tax), and the only tax, the presumptive tax, is withheld
  by the ginnery itself. A tax representative is needed by a party that is not established where
  the tax is due; nothing here needs one, and a customs broker has no role in this domestic farm
  purchase. The same party appears in 05.
- Condition: the self-billed invoice names a tax representative only if one of the parties needs
  one for a tax this invoice declares, and the reason is visible in the document.
- Options: (a, preferred) drop `TaxRepresentativeParty`; (b) give it a reason (e.g. the farm has
  appointed the broker to file its presumptive-tax return), which is a change to the story.
- Needs decision: yes

### cotton/04#F6 · Low · Tax and payment currency repeat the document currency, with identity exchange rates
- XPath: `/SelfBilledInvoice/cbc:TaxCurrencyCode` = `XLC`
- XPath: `/SelfBilledInvoice/cac:TaxExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/SelfBilledInvoice/cbc:PaymentCurrencyCode` = `XLC`
- XPath: `/SelfBilledInvoice/cac:PaymentExchangeRate/cbc:CalculationRate` = `1`
- Why: the tax currency and the payment currency are the document currency; an "exchange rate
  between the document currency and the tax currency" from XLC to XLC at 1 says nothing. Nothing in
  the invoice is converted, so these four elements have no business reason (rule "no fillers").
  The prepayment invoice 01 between the same parties has none of them. The same occurs in 05.
- Condition: a tax or payment currency and its exchange rate are present only where they differ
  from the document currency.
- Options: (a, preferred) drop the four elements; (b) none other in this story.
- Needs decision: no

### cotton/04#F7 · Low · Alternative payment currency Lume without a reason or an amount
- XPath: `/SelfBilledInvoice/cbc:PaymentAlternativeCurrencyCode` = `XBL`
- XPath: `/SelfBilledInvoice/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `2.5`
- XPath: `/SelfBilledInvoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XLC`
- Why: the farm is paid by RTGS in coral into a coral account, and is paid that way in 06; nothing
  in the invoice offers payment in Lume, and `LegalMonetaryTotal` carries no
  `PayableAlternativeAmount`. A Lisavu micro farm being offered settlement in Bayvarra's currency
  has no reason in the document. The same occurs in 05.
- Condition: an alternative payment currency is present only if the payee can actually be paid in
  it under this invoice, and then the amount in that currency follows from the rate.
- Options: (a, preferred) drop both elements; (b) keep them with a reason and a payable
  alternative amount.
- Needs decision: yes

### cotton/04#F8 · Low · Zero total of allowances in an invoice without allowances
- XPath: `/SelfBilledInvoice/cac:LegalMonetaryTotal/cbc:AllowanceTotalTaxInclusiveAmount` = `0.000`
- Why: "the total monetary amount of all allowances, inclusive of all taxes" is 0.000 because
  there are no allowances; the invoice has no `AllowanceTotalAmount` either. A zero total of
  something absent carries no information (rule "nothing implied by absence").
- Condition: the monetary total carries allowance totals only when the invoice has allowances.
- Options: (a, preferred) drop the element.
- Needs decision: no

### cotton/04#F9 · Low · A payment means inside the haulage charge
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- Why: `AllowanceCharge/PaymentMeans` is "a means of payment for this allowance or charge", for a
  charge settled separately from the invoice. This charge is part of the payable amount, paid with
  the invoice by the invoice's own credit transfer (06 pays the full 3 210.320), so a separate means
  repeats the document-level one without adding anything.
- Condition: the charge carries its own payment means only if it is settled differently from the
  rest of the invoice.
- Options: (a, preferred) drop it.
- Needs decision: no

## Checked and consistent
- Line: 18 000 kg × 0.226 per 1 kg = 4 068.000 = `LineExtensionAmount`; charge 0.010 × 18 000 = 180.000 = `ChargeTotalAmount` = `ChargeTotalTaxInclusiveAmount`; tax-exclusive 4 248.000; tax 0.000; tax-inclusive 4 248.000.
- Withholding: 1 % of 2 000.000 = 20.000 and 2 % of 2 068.000 = 41.360, together 61.360 on the cotton value 4 068.000 (the tiers add up to the line amount, "of the delivery's value"), = `WithholdingTaxTotalAmount`.
- Cotton fund levy: `/SelfBilledInvoice/cac:CollectionInvoiceLine/cbc:LineExtensionAmount` = `40.680`, 1 % of 4 068.000.
- Payable: 4 248.000 − 1 017.000 prepaid − 61.360 withheld + 40.680 levy collected = 3 210.320 = `/SelfBilledInvoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `3210.320`; 06 remits exactly this as `06-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cbc:DebitLineAmount` = `3210.320`.
- Prepayment: 1 017.000 paid 2026-01-13 matches 01 (amount, date, billing reference with issue date).
- Payment terms: 2026-02-07 + 45 days = 2026-03-24 = `DueDate` = `PaymentTerms/PaymentDueDate` = `PaymentMeans/PaymentDueDate`; penalty interest 6 % per year, simple.
- Exchange rates: 1 XBL = 0.4 XLC and 1 XLC = 2.5 XBL are each other's inverse.
- `check_ids.py`: RF reference `RF77SCGSBI260194` and account `XL67BSEL0020004817534` valid; the payee account is the farm's, the same as in 01 and 06.
- The delivery note 03 delivered 18 000 kg, the quantity billed.

## Considered and refuted
- `/SelfBilledInvoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `4248.000`: its definition says "the sum of payable amount and prepaid amount", which gives 3 210.320 + 1 017.000 = 4 227.320 — refuted because the definition predates withholding tax and collected amounts, both of which UBL 2.5 places between the tax-inclusive and the payable amount; 4 248.000 is the amount including taxes, the first half of the definition, and the payable amount follows from it as shown above.
- `/SelfBilledInvoice/cac:AllowanceCharge/cbc:ChargeIndicator` = `true` against the text "Haulage allowance": suspected of an indicator contradicting its text — refuted because "haulage allowance" is the grower's term for a payment towards haulage, which raises the amount the farm receives, i.e. a charge from the invoice's point of view, and the reason code `CAB` (cartage) is a charge reason.
- `/SelfBilledInvoice/cac:PrepaidPayment/cbc:ID` = `SCG-ADV-26-0012`: an ID that occurs nowhere else in the flow was suspected of breaking the link to the advance — refuted because it is the ginnery's own payment number ("an identifier for this payment"), and the link to the advance invoice is made by the billing reference to SCG-SBI-26-0191.
- `/SelfBilledInvoice/cac:CollectionInvoiceLine/cbc:LineExtensionAmount` = `40.680` counted in the payable amount but in no other total — refuted because a collected amount is not the farm's supply (not in line extension or tax-exclusive amount) but is paid by the ginnery to the farm for passing on, so it belongs in the amount to be paid; 01 announced that the levy falls on the delivery.
- `/SelfBilledInvoice/cac:WithholdingTaxTotal/cac:TaxSubtotal[1]/cac:TaxCategory/cbc:ID` = `S`: standard-rate category for a presumptive tax suspected of misuse — refuted because the category describes the rate applied within the OTH scheme, and the tiers are stated explicitly.
