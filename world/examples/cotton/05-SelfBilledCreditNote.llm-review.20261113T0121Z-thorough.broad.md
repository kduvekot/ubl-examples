# LLM review: 05-SelfBilledCreditNote.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

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

### cotton/05#F1 · High · The downgrade cites a certificate that says Middling and is signed six days later
- XPath: `/SelfBilledCreditNote/cbc:IssueDate` = `2026-02-14`
- XPath: `/SelfBilledCreditNote/cac:AdditionalDocumentReference/cbc:ID` = `XL-CLS-2026-0042`
- XPath: `/SelfBilledCreditNote/cac:DiscrepancyResponse/cbc:Description` = `2,500 kg classed Strict Low Middling instead of Middling.`
- XPath: `08-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:Certificate/cac:Signature/cbc:ValidationDate` = `2026-02-20`
- XPath: `08-Order.xml:/Order/cac:OrderLine/cac:LineItem/cac:Item/cac:Certificate/cbc:Remarks` = `Grade Middling, staple 1-1/8 inch, micronaire 4.2.`
- Why: the credit note justifies a price reduction for 2,500 kg classed Strict Low Middling and cites XL-CLS-2026-0042. Wherever that certificate is described (02, 07, 08, 10, 11, 15, 16) it is the chamber's classing certificate of the lint sold to the mill, grade Middling, signed on 2026-02-20, i.e. after this credit note was issued. It can neither have been available on 14 February nor support a downgrade to Strict Low Middling. The classing report that does support it is the work report SCC-CLS-26-0311 cited in the same document.
- Condition: the evidence cited for the downgrade existed on the issue date and states the lower grade.
- Options: (preferred) drop the additional reference and rely on the classing report SCC-CLS-26-0311 (with a type or description); or, if XL-CLS-2026-0042 is meant, make it a certificate issued before 14 February whose content covers both grades, and adapt the other examples.
- Needs decision: no

### cotton/05#F2 · High · Taxable amount ignores the allowance
- XPath: `/SelfBilledCreditNote/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `75.000`
- XPath: `/SelfBilledCreditNote/cac:AllowanceCharge/cbc:Amount` = `5.000`
- XPath: `/SelfBilledCreditNote/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `70.000`
- Why: the tax-exclusive amount is 75.000 − 5.000 = 70.000, but the only tax subtotal has a taxable amount of 75.000, so the subtotals do not add up to the tax-exclusive amount. The allowance also carries no tax category, so it is not clear in which category it reduces the base.
- Condition: the sum of the subtotals' taxable amounts equals `TaxExclusiveAmount`, and the allowance has a tax category.
- Options: (preferred) give the allowance its tax category and set the subtotal's taxable amount to 70.000 (or add a subtotal for the allowance's category).
- Needs decision: no

### cotton/05#F3 · High · Pricing currency Lume, but every price is in coral
- XPath: `/SelfBilledCreditNote/cbc:PricingCurrencyCode` = `XBL`
- XPath: `/SelfBilledCreditNote/cac:PricingExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/SelfBilledCreditNote/cac:CreditNoteLine/cac:Price/cbc:PriceAmount` = `0.03`
- Why: `PricingCurrencyCode` is "the currency used for prices", but the price reduction is given in coral (`currencyID="XLC"`), the document currency; the Lume pricing rate converts nothing in the document.
- Condition: the pricing currency is that of the prices in the document; no pricing exchange rate where prices are in the document currency.
- Options: (preferred) drop the pricing currency and rate; or give the price in Lume (0.075 XBL) with the rate.
- Needs decision: no

### cotton/05#F4 · Medium · A classing fee booked as an allowance on the credit
- XPath: `/SelfBilledCreditNote/cac:AllowanceCharge/cbc:ChargeIndicator` = `false`
- XPath: `/SelfBilledCreditNote/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Classing fee`
- XPath: `/SelfBilledCreditNote/cac:LegalMonetaryTotal/cbc:AllowanceTotalAmount` = `5.000`
- Why: the credit note reduces what the ginnery owes the farm. An allowance (`ChargeIndicator` false, "a discount") lowers the credit from 75.000 to 70.000, so the farm ends up 5.000 better off. A classing fee is something the farm pays (for having its cotton classed); charged to the farm it would increase the credit (a charge, to 80.000). Indicator and reason point in opposite directions, unless the ginnery is refunding a classing fee to the farm, which nothing says.
- Condition: the direction of the 5.000 (allowance or charge) agrees with who pays the classing fee to whom, and the reason text says so.
- Options: (preferred) `ChargeIndicator` true, if the farm bears the classing fee for the disputed lot; or keep the allowance and change the reason to what the ginnery concedes (e.g. "Classing fee borne by the ginnery").
- Needs decision: yes

### cotton/05#F5 · Medium · The farm as payee of a credit that flows to the ginnery
- XPath: `/SelfBilledCreditNote/cac:PayeeParty/cac:PartyName/cbc:Name` = `Lisavu Cotton Farm`
- XPath: `/SelfBilledCreditNote/cac:PaymentMeans/cbc:PaymentMeansCode` = `97`
- XPath: `/SelfBilledCreditNote/cac:PaymentTerms/cbc:Note` = `Set off against the payment of the self-billed invoice.`
- Why: `PayeeParty` is "The Party who receives the Payment". The credit of 69.250 is owed by the farm to the ginnery and settled by set-off (code 97, clearing between partners); the party that receives the value is the ginnery, not the farm. Copying the farm from the invoice into the credit note reverses the role.
- Condition: the credit note names no payee, or names the party that receives the credited amount.
- Options: (preferred) drop `PayeeParty`, because the amount is set off and no payment is made; or name the ginnery.
- Needs decision: no

### cotton/05#F6 · Medium · Tax representative for a resident farm
- XPath: `/SelfBilledCreditNote/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- Why: as in cotton/04#F5: a resident Lisavan farm selling to a Lisavan ginnery, with no sales tax, needs no tax representative; a customs broker in that role has no task in this credit note.
- Condition: a tax representative is named only where the world's tax rules require one.
- Options: (preferred) drop it; or record the rule that requires it.
- Needs decision: yes

### cotton/05#F7 · Medium · Tax category "Services outside scope of tax" applied to goods
- XPath: `/SelfBilledCreditNote/cac:CreditNoteLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `O`
- XPath: `/SelfBilledCreditNote/cac:CreditNoteLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- Why: as in cotton/01#F2: code `O` of UN/EDIFACT 5305 means "Services outside scope of tax", the line credits goods.
- Condition: the goods line carries a code whose meaning covers goods outside the scope of tax, or the deviation is recorded.
- Options: (preferred) one world-wide decision (17 examples use `O`).
- Needs decision: yes

### cotton/05#F8 · Medium · The delivery note given as a despatch advice
- XPath: `/SelfBilledCreditNote/cac:DespatchDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- XPath: `/SelfBilledCreditNote/cac:DeliveryNoteDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- Why: `DespatchDocumentReference` refers to a Despatch Advice; LCF-DN-26-0193 is the delivery note 03, already cited in `DeliveryNoteDocumentReference`.
- Condition: `DespatchDocumentReference` is absent or refers to a despatch advice.
- Options: (preferred) drop it.
- Needs decision: no

### cotton/05#F9 · Low · Currency and exchange-rate data with nothing to convert
- XPath: `/SelfBilledCreditNote/cbc:TaxCurrencyCode` = `XLC`
- XPath: `/SelfBilledCreditNote/cbc:PaymentCurrencyCode` = `XLC`
- XPath: `/SelfBilledCreditNote/cbc:PaymentAlternativeCurrencyCode` = `XBL`
- XPath: `/SelfBilledCreditNote/cac:TaxExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/SelfBilledCreditNote/cac:PaymentExchangeRate/cbc:CalculationRate` = `1`
- XPath: `/SelfBilledCreditNote/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `2.5`
- Why: the credit is set off in coral; tax and payment currencies equal the document currency, two exchange rates convert coral into coral at 1, and nothing is paid in the alternative currency Lume.
- Condition: currency codes and exchange rates appear only where a currency differs from the document currency and an amount is converted.
- Options: (preferred) drop them.
- Needs decision: no

### cotton/05#F10 · Low · Withholding tax without its scheme and rate
- XPath: `/SelfBilledCreditNote/cac:WithholdingTaxTotal/cbc:TaxAmount` = `1.500`
- Why: the withholding total has no subtotal, so the credit note does not say which tax is corrected or at which rate. 1.500 is 2 % of 75.000, the top band of the presumptive tax in 04 (`04-SelfBilledInvoice.xml:/SelfBilledInvoice/cac:WithholdingTaxTotal/cac:TaxSubtotal[2]/cbc:Percent` = `2`), but the reader has to work that out.
- Condition: the withholding total has a subtotal with taxable amount, rate and tax scheme.
- Options: (preferred) one subtotal: 75.000 × 2 %, scheme "Presumptive tax on farm produce" as in 04.
- Needs decision: no

### cotton/05#F11 · Low · Tax scheme without an identifier that names a tax that does not exist
- XPath: `/SelfBilledCreditNote/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: as cotton/01#F3.
- Condition: the zero tax total names a real scheme, or is absent.
- Options: (preferred) one decision for the nine examples with this name.
- Needs decision: yes

### cotton/05#F12 · Low · References with an identifier only, of unclear kind
- XPath: `/SelfBilledCreditNote/cac:WorkReportDocumentReference/cbc:ID` = `SCC-CLS-26-0311`
- XPath: `/SelfBilledCreditNote/cac:OriginatorDocumentReference/cbc:ID` = `LTM-SEASON-2026`
- XPath: `/SelfBilledCreditNote/cac:StatementDocumentReference/cbc:ID` = `SCG-ACC-LCF-26-02`
- XPath: `/SelfBilledCreditNote/cac:ProjectReference/cbc:ID` = `SCC-COTTON-QUALITY-26`
- Why: the classing report that justifies the credit is filed as a "work report" without type or description; the mill's season document as originator, the statement and the chamber's project have no role in the credit and exist nowhere in the flow.
- Condition: each reference has a role in this credit note and says what it is where that is not obvious.
- Options: (preferred) keep the classing report with a description and drop the others.
- Needs decision: no

### cotton/05#F13 · Low · The ginnery's buying contact is its sales desk
- XPath: `/SelfBilledCreditNote/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`
- Why: as cotton/04#F13; the document routes to "Farm payments" (`/SelfBilledCreditNote/cac:BuyerAssignedReference/cbc:BuyerReference` = `Farm payments`).
- Condition: the accounting customer's contact handles farm payments.
- Options: (preferred) a farm-payments contact.
- Needs decision: no

## Checked and consistent
- Line: 2500 kg × 0.03 XLC/kg = 75.000; tax-exclusive 75.000 − 5.000 = 70.000; withholding 2 % × 75.000 = 1.500; levy 1 % × 75.000 = 0.750; payable 70.000 − 1.500 + 0.750 = 69.250 (same calculation scheme as 04).
- The remittance advice 06 sets the credit off: 3210.320 − 69.250 = 3141.070 (`06-RemittanceAdvice.xml:/RemittanceAdvice/cbc:TotalPaymentAmount` = `3141.070`), on the credit note's due date 2026-02-16.
- Billing reference to 04 with issue date 2026-02-07 resolves; 2500 kg is part of the 18000 kg billed there.
- Discrepancy code 2 of UN/EDIFACT 4465 is "Below specification goods", fitting a downgrade; reference ID 1 points to line 1.
- Credit note type 261 "Self billed credit note".

## Considered and refuted
- `/SelfBilledCreditNote/cbc:DueDate`: a due date on a credit settled by set-off — refuted: it tells when the set-off takes place, and 06 does it on that date.
- `/SelfBilledCreditNote/cac:CollectionCreditNoteLine`: reversal of a share of the levy — refuted: consistent with the levy collected in 04 (1 % of the credited value).
