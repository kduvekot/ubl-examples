# LLM review: 15-Invoice.xml

Flow: road (ROAD-2026-01) · Review date: 2026-11-12 · Part: money

## Reviewed version
- Run: `20261112T2311Z-thorough`
- Example: `world/examples/road/15-Invoice.xml`, Git blob `8fdcb4b50214e654097ed80dd7c97b81f9267569` (committed)
- Last commit changing the example: a8f6ba0 2026-11-12 Item descriptions in the seller's languages
- Checkout: branch `claude/keen-feynman-45qjti`, commit 8d0bb7f 2026-11-12 Reviews of the utilities flow, run 20261112T2230Z-thorough: parts written so far
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

### road/15#F1 · High · Payment exchange rate to a currency that is not the payment currency
- XPath: `/Invoice/cbc:DocumentCurrencyCode` = `XUF`
- XPath: `/Invoice/cbc:PaymentCurrencyCode` = `XUF`
- XPath: `/Invoice/cac:PaymentExchangeRate/cbc:SourceCurrencyCode` = `XUF`
- XPath: `/Invoice/cac:PaymentExchangeRate/cbc:TargetCurrencyCode` = `XBL`
- XPath: `/Invoice/cac:PaymentExchangeRate/cbc:CalculationRate` = `0.01`
- Why: Invoice. Payment_ Exchange Rate is "The exchange rate between the document currency and the payment currency." Payment Currency Code is "A code signifying the currency used for payment in the Invoice". Both the document currency and the payment currency are XUF, and the payment really is made in XUF into an XUF account (`/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:CurrencyCode` = `XUF`; `17-RemittanceAdvice.xml:/RemittanceAdvice/cbc:TotalPaymentAmount` = `4862160`, in XUF). The payment exchange rate, however, converts XUF into XBL, a currency that is neither the document nor the payment currency, so the rate contradicts the payment currency it is meant to explain. The rate itself (100 XUF = 1 XBL) matches the world's rate elsewhere; XBL is the buyer's home currency and the currency of the payer's account in the remittance (`17-RemittanceAdvice.xml:/RemittanceAdvice/cac:PaymentMeans/cac:PayerFinancialAccount/cbc:CurrencyCode` = `XBL`), but conversion on the payer's side is the payer's bank's business and has no element in the invoice. The same mismatch occurs in no other example: of the 10 examples with a PaymentExchangeRate (`grep -rl --include='*.xml' '<cac:PaymentExchangeRate>' world/examples`), only this one has a target currency different from its PaymentCurrencyCode.
- Condition: Either the invoice carries no payment exchange rate, or its source currency is the document currency and its target currency is the payment currency stated in `PaymentCurrencyCode`, and the payee account and the remittance advice agree with that payment currency.
- Options: (a) remove the PaymentExchangeRate (preferred: the payment is in XUF as the remittance shows, so no rate is needed and the story is unchanged); (b) make XBL the payment currency, which would also need an XBL payee account and a remittance in XBL, a change of the story.
- Needs decision: no

## Checked and consistent
- Lines: 96 × 49 900 = 4 790 400 = `/Invoice/cac:InvoiceLine[1]/cbc:LineExtensionAmount` = `4790400`; 12 × 5 980 = 71 760 = `/Invoice/cac:InvoiceLine[2]/cbc:LineExtensionAmount` = `71760`; both prices per 1 EA, and equal to the order's prices (`01-Order.xml:/Order/cac:OrderLine[1]/cac:LineItem/cac:Price/cbc:PriceAmount` = `49900`) and to the "same price" of the substituted 2026 casting (`02-OrderResponse.xml:/OrderResponse/cac:OrderLine[2]/cac:SellerSubstitutedLineItem/cac:Price/cbc:PriceAmount` = `5980`).
- Totals: 4 790 400 + 71 760 = 4 862 160 = `/Invoice/cac:LegalMonetaryTotal/cbc:LineExtensionAmount` = `4862160` = `/Invoice/cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` = `4862160` = `/Invoice/cac:LegalMonetaryTotal/cbc:TaxInclusiveAmount` = `4862160` = `/Invoice/cac:LegalMonetaryTotal/cbc:PayableAmount` = `4862160`, equal to the order's anticipated total; tax subtotal taxable amount the same, tax 0.
- Tax: header category and both line categories are the same (`G`, 0 %, `EXP`, VAT); the seller is the exporter of record (`05-ExportCustomsDeclaration.xml:/ExportCustomsDeclaration/cac:ExporterParty/cac:PartyIdentification/cbc:ID` = `XU-R-104274`), so the export exemption has its evidence; the goods leave Urvania (`08-Waybill.xml:/Waybill/cac:Shipment/cac:Consignment/cac:FinalDestinationCountry/cbc:IdentificationCode` = `XB`).
- Payment terms: 2 % of 4 862 160 = 97 243.2, rounded to `/Invoice/cac:PaymentTerms/cbc:SettlementDiscountAmount` = `97243`; settlement period 10 days (`/Invoice/cac:PaymentTerms/cac:SettlementPeriod/cbc:EndDate` = `2026-04-03`); due date 30 days after issue, the same in `/Invoice/cbc:DueDate` = `2026-04-23`, `/Invoice/cac:PaymentMeans/cbc:PaymentDueDate` = `2026-04-23` and `/Invoice/cac:PaymentTerms/cbc:PaymentDueDate` = `2026-04-23`. Penalty interest 8 % per year (ANN, Rec. 20 "year"), simple.
- What follows: the remittance pays 4 862 160 XUF on 2026-04-22, after the discount period and before the due date, so no discount is taken and the full amount is right (`17-RemittanceAdvice.xml:/RemittanceAdvice/cac:RemittanceAdviceLine/cbc:DebitLineAmount` = `4862160`, balance 0); it quotes the invoice's creditor reference `/Invoice/cac:PaymentMeans/cbc:PaymentID` = `RF78VIINV260166` (valid ISO 11649 check) and pays into the payee account given here (`/Invoice/cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` = `XU790351041600000000209458`, valid IBAN-style check).
- The bank identifiers `CREVXUFR` and `BLUMXBLX` cannot be real BICs: XU and XB are not ISO 3166 country codes in use (own knowledge).
- The import declaration converts the invoice values at this invoice's rate of 0.01 (`10-ImportCustomsDeclaration.xml:/ImportCustomsDeclaration/cac:Shipment/cac:GoodsItem[1]/cbc:DeclaredCustomsValueAmount` = `47904.00`).

## Considered and refuted
- `/Invoice/cbc:TaxPointDate` = `2026-03-24`: suspected that the tax point should be the day of supply (despatch on 2026-03-23, `04-DespatchAdvice.xml:/DespatchAdvice/cbc:IssueDate` = `2026-03-23`) rather than the invoice date — refuted because the element is "The date of the Invoice, used to indicate the point at which tax becomes applicable", and many VAT systems let the invoice date be the tax point when the invoice follows the supply within a short period (own knowledge); with a 0 % export treatment nothing depends on it.
- `/Invoice/cac:PaymentMeans/cbc:ChargeBearerCode` = `SHAR`: suspected that shared charges reduce what the seller receives below the payable amount — refuted because SHAR means each party pays its own bank's charges; the remittance reports the amount sent, which is the full payable amount.
