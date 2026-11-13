# LLM review: 04-SelfBilledInvoice.xml

Flow: cotton (COTTON-2026-01) · Review date: 2026-11-13 · Part: broad

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

### cotton/04#F1 · High · Taxable amount leaves out the haulage charge of the same tax category
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cbc:TaxableAmount` = `4068.000`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cac:TaxCategory/cbc:ID` = `O`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:Amount` = `180.000`
- XPath: `/SelfBilledInvoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `4248.000`
- Why: `TaxableAmount` is "The net amount to which the tax percent (rate) is applied". The only tax subtotal is for category `O`, and both the seed-cotton line (4068.000) and the haulage charge (180.000) are in category `O`. The subtotal's taxable amount should therefore be 4068.000 + 180.000 = 4248.000, equal to the tax-exclusive amount; it is 4068.000. Document-level charges belong to the taxable base of their category.
- Condition: the sum of the taxable amounts of the tax subtotals equals `TaxExclusiveAmount` (4248.000), each charge counted in its own category.
- Options: (preferred) taxable amount 4248.000 in the `O` subtotal; or, if the haulage charge belongs to another category, a second subtotal for it.
- Needs decision: no

### cotton/04#F2 · High · Pricing currency Lume, but every price is in coral
- XPath: `/SelfBilledInvoice/cbc:PricingCurrencyCode` = `XBL`
- XPath: `/SelfBilledInvoice/cac:PricingExchangeRate/cbc:SourceCurrencyCode` = `XBL`
- XPath: `/SelfBilledInvoice/cac:PricingExchangeRate/cbc:CalculationRate` = `0.4`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Price/cbc:PriceAmount` = `0.226`
- Why: `PricingCurrencyCode` is "the currency used for prices in the Invoice", but the only price is given with `currencyID="XLC"` (coral), the same as the document currency. The pricing exchange rate (1 XBL = 0.4 XLC) is applied nowhere: no amount in the invoice is in Lume. If the season price was agreed in Lume (0.565 XBL/kg × 0.4 = 0.226 XLC/kg), the price element does not show it.
- Condition: the pricing currency is the currency of the prices in the document; a pricing exchange rate is present only when prices are in another currency than the document.
- Options: (preferred) drop `PricingCurrencyCode` and `PricingExchangeRate`, because the price is in coral; or give the price in Lume (0.565 XBL) and keep the rate that converts it to the coral line amount.
- Needs decision: no

### cotton/04#F3 · Medium · The delivery note given as a despatch advice
- XPath: `/SelfBilledInvoice/cac:DespatchDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- XPath: `/SelfBilledInvoice/cac:DeliveryNoteDocumentReference/cbc:ID` = `LCF-DN-26-0193`
- Why: `DespatchDocumentReference` is "A reference to a Despatch Advice associated with this document". LCF-DN-26-0193 is a Delivery Note (03), which the invoice also cites, correctly, in `DeliveryNoteDocumentReference`. No despatch advice exists in the flow.
- Condition: `DespatchDocumentReference` is absent or refers to a despatch advice.
- Options: (preferred) drop `DespatchDocumentReference`, because the delivery note is already referenced by the dedicated element.
- Needs decision: no

### cotton/04#F4 · Medium · The mill as originator of an order it did not place
- XPath: `/SelfBilledInvoice/cac:OriginatorCustomerParty/cac:Party/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/SelfBilledInvoice/cac:BeneficiaryParty/cac:PartyName/cbc:Name` = `Lumeport Textile Mill`
- XPath: `/SelfBilledInvoice/cac:OriginatorDocumentReference/cbc:ID` = `LTM-SEASON-2026`
- XPath: `/SelfBilledInvoice/cac:OrderReference/cbc:ID` = `SCG-SEASON-2026/03`
- Why: `OriginatorCustomerParty` is "The Party who originated the Order to which this Invoice is related". The order is the ginnery's own call-off under its season agreement with the farm (SCG-…); the mill buys lint from the ginnery under a separate order (08, issued two weeks later). The mill is not the originator of the seed-cotton purchase, nor the party for whom the seed cotton is ultimately intended (the ginnery turns it into lint and seed and sells them). The originator document LTM-SEASON-2026 exists nowhere in the flow and is not explained.
- Condition: the self-billed invoice names an originator and beneficiary only if they originated or benefit from this seed-cotton purchase, and an originator document that says what it is.
- Options: (preferred) drop the three elements; or, if the story is that the mill pre-finances the season's crop under LTM-SEASON-2026, state that in the season agreement and in this invoice and keep them.
- Needs decision: yes

### cotton/04#F5 · Medium · Tax representative for a resident farm
- XPath: `/SelfBilledInvoice/cac:TaxRepresentativeParty/cac:PartyName/cbc:Name` = `Tevaro Customs Brokers`
- XPath: `/SelfBilledInvoice/cac:TaxRepresentativeParty/cac:PartyIdentification/cbc:ID` = `IC41585`
- Why: `TaxRepresentativeParty` is "The Party authorized to act as the Tax Representative for this Self Billed Invoice". A tax (fiscal) representative acts for a supplier that is not established in the taxing country. The farm is a Lisavan sole proprietorship selling to a Lisavan ginnery, with no sales tax on the supply and the presumptive tax withheld by the buyer; there is nothing a representative would account for. A customs broker in that role adds to the doubt.
- Condition: the invoice names a tax representative only if the supplier needs one under the world's tax rules, and that need is visible in the document.
- Options: (preferred) drop the tax representative; or, if Lisavan law requires farms to appoint an agent for the presumptive tax, record that rule in the world's tax story and name the agent in that role.
- Needs decision: yes

### cotton/04#F6 · Medium · Tax category "Services outside scope of tax" applied to goods
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:ID` = `O`
- XPath: `/SelfBilledInvoice/cac:InvoiceLine/cac:Item/cac:ClassifiedTaxCategory/cbc:SupplyTypeCode` = `GOODS`
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:ID` = `O`
- Why: in UN/EDIFACT 5305 `O` means "Services outside scope of tax"; the line is seed cotton, a supply of goods, as `SupplyTypeCode` says. EN 16931 practice uses `O` for any out-of-scope supply, but semantic conformance makes the code's meaning decisive. The same code is used in 17 examples (`grep -rl --include='*.xml' 'schemeID="UN/EDIFACT EDED 5305">O<'`). (For the haulage charge, a service, `O` fits.)
- Condition: the goods line and its subtotal carry a code whose meaning covers goods outside the scope of tax, or the deviation is recorded as a deliberate choice.
- Options: (preferred) one world-wide decision on how goods outside any sales tax are coded; or keep `O` and record it as a finding.
- Needs decision: yes

### cotton/04#F7 · Low · Currency and exchange-rate data with nothing to convert
- XPath: `/SelfBilledInvoice/cbc:TaxCurrencyCode` = `XLC`
- XPath: `/SelfBilledInvoice/cbc:PaymentCurrencyCode` = `XLC`
- XPath: `/SelfBilledInvoice/cbc:PaymentAlternativeCurrencyCode` = `XBL`
- XPath: `/SelfBilledInvoice/cac:TaxExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/SelfBilledInvoice/cac:PaymentExchangeRate/cbc:TargetCurrencyCode` = `XLC`
- XPath: `/SelfBilledInvoice/cac:PaymentAlternativeExchangeRate/cbc:CalculationRate` = `2.5`
- Why: tax and payment currency equal the document currency, and the tax and payment exchange rates convert coral into coral at 1. The alternative payment currency Lume has no use: the farm is paid by transfer into a coral account (`/SelfBilledInvoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XLC`) and the remittance advice 06 pays in coral. None of this information changes anything for the receiver (no fillers, IND5).
- Condition: currency codes and exchange rates appear only where a currency differs from the document currency and an amount is, or may be, converted.
- Options: (preferred) drop the four exchange rates and the three currency codes; or keep the Lume alternative only if the season agreement lets the farm ask for payment in Lume, and say so in the payment terms.
- Needs decision: no

### cotton/04#F8 · Low · A charge called an allowance
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:ChargeIndicator` = `true`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:AllowanceChargeReason` = `Haulage allowance`
- Why: `ChargeIndicator` true makes this a charge (it adds 180.000 to what the ginnery owes the farm, which is what a payment for the farm's own haulage should do). The reason text calls it an allowance, which in UBL terms is the opposite (a discount). The indicator and the text read as contradicting each other, although the business meaning (the ginnery pays the farm for carting) is consistent.
- Condition: the reason text does not describe the charge as an allowance.
- Options: (preferred) reason text such as "Haulage paid to the farm" or "Cartage"; or keep the trade term and add a note that it is paid to the farm.
- Needs decision: no

### cotton/04#F9 · Low · Charge data the calculation does not use
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:BaseAmount` = `4068.000`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:PerUnitAmount` = `0.010`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cac:PaymentMeans/cbc:PaymentMeansCode` = `30`
- Why: `BaseAmount` is "The monetary amount to which the multiplier factor is applied". The charge has no multiplier factor; it is 0.010 XLC per kg × 18000 kg = 180.000, and 180/4068 is no agreed percentage. The base amount therefore plays no role. The charge's own payment means repeats the invoice's credit transfer: the charge is paid with the invoice, not separately.
- Condition: the charge carries only the data its calculation and settlement use.
- Options: (preferred) drop `BaseAmount` and the charge's `PaymentMeans`; or, if the haulage is a percentage, use `MultiplierFactorNumeric` with the base amount instead of the per-unit amount.
- Needs decision: no

### cotton/04#F10 · Low · Delivered terms with a haulage charge to the buyer
- XPath: `/SelfBilledInvoice/cac:DeliveryTerms/cbc:ID` = `DAP`
- XPath: `/SelfBilledInvoice/cac:AllowanceCharge/cbc:AccountingCost` = `Seed cotton haulage`
- Why: under Incoterms DAP the seller delivers at the named place at its own cost (own knowledge of Incoterms 2020). Here the buyer pays the seller a separate charge for the haulage to the gin. Either the price is ex farm and the buyer pays for the carriage (not DAP), or the terms are DAP and the haulage is part of the price.
- Condition: the delivery terms and the haulage charge describe the same allocation of carriage cost.
- Options: (preferred) keep DAP and describe the payment as a delivery premium agreed in the season contract; or use delivery terms under which the buyer bears the carriage (e.g. EXW / FCA farm) and keep the charge.
- Needs decision: yes

### cotton/04#F11 · Low · References with an identifier only, of unclear kind
- XPath: `/SelfBilledInvoice/cac:WorkReportDocumentReference/cbc:ID` = `SCG-OUT-26-0311`
- XPath: `/SelfBilledInvoice/cac:ReceiptDocumentReference/cbc:ID` = `SCG-WB-26-0311`
- XPath: `/SelfBilledInvoice/cac:StatementDocumentReference/cbc:ID` = `SCG-ACC-LCF-26-02`
- XPath: `/SelfBilledInvoice/cac:AdditionalDocumentReference/cbc:ID` = `XL-FARM-REG-0412`
- XPath: `/SelfBilledInvoice/cac:ProjectReference/cbc:ID` = `SCC-COTTON-QUALITY-26`
- Why: none of these documents exists in the flow and none says what it is. The "work report" SCG-OUT-… is presumably the gin's outturn report, but the price is per kg of seed cotton, so the outturn plays no part in the amount; the receipt reference is a weighbridge ticket, not a Receipt Advice; the farm registration and the chamber's quality project are not used by anything in the invoice. The credit note 05 cites a different work report (`05-SelfBilledCreditNote.xml:/SelfBilledCreditNote/cac:WorkReportDocumentReference/cbc:ID` = `SCC-CLS-26-0311`).
- Condition: each reference has a role in this invoice and, where not obvious, a type or description.
- Options: (preferred) keep the references that the amounts depend on (delivery note, weighbridge ticket as an additional document with a type) and drop the rest; or describe each one.
- Needs decision: no

### cotton/04#F12 · Low · Tax scheme without an identifier that names a tax that does not exist
- XPath: `/SelfBilledInvoice/cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cac:TaxScheme/cbc:Name` = `No general sales tax`
- Why: a tax total for "No general sales tax" totals a tax that does not exist, and the scheme has no `ID` (`TaxTotal`: "The total amount of a specific type of tax").
- Condition: the zero tax total names a real scheme of Lisavu, or is absent.
- Options: (preferred) as cotton/01#F3; one decision for the nine examples that use this name.
- Needs decision: yes

### cotton/04#F13 · Low · The ginnery's buying contact is its sales desk
- XPath: `/SelfBilledInvoice/cac:AccountingCustomerParty/cac:Party/cac:Contact/cbc:Name` = `Cotton sales`
- XPath: `/SelfBilledInvoice/cac:BuyerAssignedReference/cbc:BuyerReference` = `Farm payments`
- Why: the document itself routes the invoice to "Farm payments", but the accounting customer's contact is the lint sales desk.
- Condition: the accounting customer's contact is the function that handles farm payments.
- Options: (preferred) a farm-payments contact; or none.
- Needs decision: no

### cotton/04#F14 · Low · Note and annotation say the same
- XPath: `/SelfBilledInvoice/cbc:Note[2]` = `Self-billed under the season agreement: the ginnery writes the invoice on the farm's behalf.`
- XPath: `/SelfBilledInvoice/cac:Annotation/cbc:AnnotationContent` = `Written by the gin on the farm's behalf under the self-billing agreement.`
- Why: `Annotation` is "A structured annotation providing contextual or explanatory information"; here it repeats the note in other words and adds no structure or information.
- Condition: the annotation adds information the note does not carry, or one of the two is dropped.
- Options: (preferred) drop the annotation; or use it for something the note does not say (e.g. the self-billing agreement's reference and acceptance date).
- Needs decision: no

## Checked and consistent
- Line: 18000 kg × 0.226 XLC/kg = 4068.000; charge 0.010 × 18000 = 180.000; tax-exclusive 4068.000 + 180.000 = 4248.000; tax 0.
- Withholding: 1 % × 2000.000 = 20.000; 2 % × 2068.000 = 41.360; total 61.360; tiers sum to the line value 4068.000.
- Cotton-fund levy: 1 % of 4068.000 = 40.680; 01 said the levy falls on the delivery, not the advance.
- Payable: 4248.000 − 1017.000 (prepaid) − 61.360 (withheld) + 40.680 (levy collected) = 3210.320; paid in the remittance advice 06 (`06-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine[1]/cbc:DebitLineAmount` = `3210.320`).
- Prepayment: matches 01 (1017.000 XLC, 2026-01-13).
- Due date: 2026-02-07 + 45 days = 2026-03-24, as in the terms.
- Delivery note 03: same quantity, item, delivery date and order reference.
- Check digits: RF reference `RF77SCGSBI260194` and account pass.

## Considered and refuted
- `/SelfBilledInvoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount`: the definition says "the sum of payable amount and prepaid amount", and 3210.320 + 1017.000 = 4227.320 ≠ 4248.000 — refuted: the difference (61.360 − 40.680 = 20.680) is exactly the withholding tax less the collected levy, which UBL 2.5 subtracts and adds after the tax-inclusive amount; the older definition text does not cover withholding totals and collection lines.
- `/SelfBilledInvoice/cac:CollectionInvoiceLine`: a levy added to what the ginnery pays the farm — refuted: the line is an amount "collected on behalf of a third party" by the farm for the chamber, and the note says so.
- `/SelfBilledInvoice/cac:WithholdingTaxTotal/cac:TaxSubtotal[1]/cac:TaxCategory/cbc:ID`: standard-rate code `S` for tiered presumptive tax — refuted: each tier is the scheme's normal rate for its band.
- `/SelfBilledInvoice/cac:PayeeParty`: payee equal to the supplier — refuted: no "if different" condition in the definition.
- `/SelfBilledInvoice/cac:AllowanceCharge/cac:TaxCategory/cbc:ID`: `O` for haulage — refuted: haulage is a service, which `O` covers.
